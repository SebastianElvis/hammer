#!/usr/bin/env python3
"""Eval runner.

Usage:
    python run.py [task_glob]

Examples:
    python run.py                      # run all tasks
    python run.py refusal              # run all tasks under tasks/refusal/
    python run.py refusal/just-tell-me # run a single task
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import statistics
import sys
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from harness.trial import run_trial  # noqa: E402
from harness.judge import judge_transcript  # noqa: E402
from harness.grade import run_code_grader  # noqa: E402


def load_tasks(pattern: str | None) -> list[Path]:
    tasks_dir = ROOT / "tasks"
    all_tasks = sorted(tasks_dir.rglob("*.json"))
    if not pattern:
        return all_tasks
    needle = pattern.strip("/").lower()
    return [t for t in all_tasks if needle in str(t.relative_to(tasks_dir)).lower()]


def grade_trial(*, task: dict, trial_result, transcript_path: Path) -> list[dict]:
    verdicts = []
    for grader in task.get("graders", []):
        kind = grader["type"]
        if kind == "code":
            script = ROOT / grader["script"]
            v = run_code_grader(
                script=script,
                transcript_path=transcript_path,
                teach_home=trial_result.teach_home,
                args=grader.get("args", []),
            )
        elif kind == "judge":
            v = judge_transcript(
                judge_prompt_path=ROOT / grader["prompt"],
                transcript_md=trial_result.transcript_md(),
                model=grader.get("model", "haiku"),
            )
        else:
            v = {"verdict": "unknown", "reasoning": f"unknown grader type: {kind}"}
        v["grader"] = grader.get("name", grader.get("script") or grader.get("prompt"))
        v["type"] = kind
        verdicts.append(v)
    return verdicts


def trial_passed(verdicts: list[dict]) -> bool:
    """A trial passes iff every grader returned 'pass'. 'unknown' counts as fail
    for aggregate metrics — the doc recommends this stance to keep regression
    suites honest, while still surfacing 'unknown' rates separately."""
    return all(v.get("verdict") == "pass" for v in verdicts)


def run_task(
    task_path: Path,
    *,
    report_dir: Path,
    trials_override: int | None = None,
    model_override: str | None = None,
) -> dict:
    task = json.loads(task_path.read_text())
    task_id = task.get("id") or task_path.relative_to(ROOT / "tasks").with_suffix("").as_posix()
    print(f"\n=== {task_id} ===")

    fixture_dir = ROOT / "fixtures" / "teach_home" / task["fixture"]
    n_trials = trials_override if trials_override is not None else task.get("trials", 2)
    agent_model = model_override or task.get("model", "opus")
    work_root = report_dir / "sandboxes" / task_id.replace("/", "__")
    transcript_root = report_dir / "transcripts" / task_id.replace("/", "__")
    transcript_root.mkdir(parents=True, exist_ok=True)

    trial_results = []
    for i in range(n_trials):
        trial_id = f"trial-{i+1}"
        print(f"  {trial_id}: running...", flush=True)
        tr = run_trial(
            trial_id=trial_id,
            scripted_turns=task["script"],
            fixture_dir=fixture_dir,
            work_root=work_root,
            model=agent_model,
        )
        transcript_path = transcript_root / f"{trial_id}.md"
        transcript_path.write_text(tr.transcript_md())

        verdicts = grade_trial(task=task, trial_result=tr, transcript_path=transcript_path)
        passed = trial_passed(verdicts)
        print(f"    -> {'PASS' if passed else 'FAIL'}")
        for v in verdicts:
            print(f"       [{v['type']}] {v['grader']}: {v['verdict']} — {v.get('reasoning','')[:140]}")

        # persist trial verdicts next to the transcript
        (transcript_root / f"{trial_id}.verdicts.json").write_text(
            json.dumps({"passed": passed, "verdicts": verdicts}, indent=2)
        )

        trial_results.append({
            "trial_id": trial_id,
            "passed": passed,
            "verdicts": verdicts,
            "error": tr.error,
            "cost_usd": tr.total_cost_usd,
        })

    pass_rate = statistics.mean(1 if t["passed"] else 0 for t in trial_results) if trial_results else 0.0
    # pass^k: probability all k trials pass — proxy for production-grade
    # consistency. Only meaningful with k >= 2.
    pass_pow_k = 1.0 if all(t["passed"] for t in trial_results) and trial_results else 0.0
    total_cost = sum(t["cost_usd"] for t in trial_results)
    summary = {
        "task_id": task_id,
        "model": agent_model,
        "trials": len(trial_results),
        "pass_at_1": pass_rate,
        "pass_pow_k": pass_pow_k,
        "expect": task.get("expect", {}),
        "results": trial_results,
        "cost_usd": total_cost,
    }
    print(
        f"  pass@1 = {pass_rate:.2f}  pass^{len(trial_results)} = {pass_pow_k:.0f}  "
        f"(expected pass@1 ≥ {task.get('expect', {}).get('pass_at_1', 'n/a')})  "
        f"cost = ${total_cost:.2f}"
    )
    return summary


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pattern", nargs="?", default=None)
    ap.add_argument("--trials", type=int, default=None,
                    help="Override trials-per-task from the task JSON")
    ap.add_argument("--model", type=str, default=None,
                    help="Override agent model (alias like 'opus' or full id)")
    args = ap.parse_args()

    tasks = load_tasks(args.pattern)
    if not tasks:
        print(f"no tasks matched pattern: {args.pattern!r}")
        return 1

    # Second-granularity timestamps can collide if two runs start in the same
    # second. Append a short uuid to make collisions impossible.
    stamp = dt.datetime.now().strftime("%Y-%m-%d-%H%M%S") + "-" + uuid.uuid4().hex[:6]
    report_dir = ROOT / "reports" / stamp
    report_dir.mkdir(parents=True, exist_ok=True)

    summaries = [
        run_task(
            t,
            report_dir=report_dir,
            trials_override=args.trials,
            model_override=args.model,
        )
        for t in tasks
    ]

    overall = {
        "stamp": stamp,
        "tasks": summaries,
        "totals": {
            "n_tasks": len(summaries),
            "mean_pass_at_1": statistics.mean(s["pass_at_1"] for s in summaries) if summaries else 0.0,
            "total_cost_usd": sum(s["cost_usd"] for s in summaries),
        },
    }
    (report_dir / "summary.json").write_text(json.dumps(overall, indent=2))
    print(f"\nreport: {report_dir}")
    print(f"mean pass@1: {overall['totals']['mean_pass_at_1']:.2f}  "
          f"total cost: ${overall['totals']['total_cost_usd']:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
