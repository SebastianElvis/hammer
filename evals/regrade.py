#!/usr/bin/env python3
"""Re-grade an existing transcript N times to measure grader consistency.

Used for self-consistency / judge-stability checks: feed a frozen transcript
to the same graders K times and compare the verdicts. Stable graders should
return the same verdict every time on identical input.

Usage:
    python regrade.py <task_json> <transcript.md> [--k 5]
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from harness.judge import judge_transcript  # noqa: E402
from harness.grade import run_code_grader  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("task_json", type=Path)
    ap.add_argument("transcript", type=Path)
    ap.add_argument("--k", type=int, default=5, help="Number of regrade rounds")
    args = ap.parse_args()

    task = json.loads(args.task_json.read_text())
    transcript_md = args.transcript.read_text()

    by_grader: dict[str, list[str]] = {}
    detail: list[dict] = []
    for round_i in range(args.k):
        round_verdicts = []
        for grader in task.get("graders", []):
            kind = grader["type"]
            name = grader.get("name", grader.get("script") or grader.get("prompt"))
            if kind == "code":
                v = run_code_grader(
                    script=ROOT / grader["script"],
                    transcript_path=args.transcript,
                    teach_home=Path("/dev/null"),  # not used by current code graders
                    args=grader.get("args", []),
                )
            elif kind == "judge":
                v = judge_transcript(
                    judge_prompt_path=ROOT / grader["prompt"],
                    transcript_md=transcript_md,
                    model=grader.get("model", "haiku"),
                )
            else:
                v = {"verdict": "unknown", "reasoning": f"unknown type: {kind}"}
            by_grader.setdefault(name, []).append(v["verdict"])
            round_verdicts.append({"grader": name, "verdict": v["verdict"], "reasoning": v.get("reasoning", "")[:200]})
        detail.append({"round": round_i + 1, "verdicts": round_verdicts})
        print(f"round {round_i + 1}: " + ", ".join(f"{r['grader']}={r['verdict']}" for r in round_verdicts))

    print("\nconsistency:")
    overall_stable = True
    for name, verdicts in by_grader.items():
        counts = Counter(verdicts)
        modal = counts.most_common(1)[0]
        stable = (modal[1] == len(verdicts))
        if not stable:
            overall_stable = False
        print(f"  {name}: {dict(counts)}  ({'stable' if stable else 'UNSTABLE'})")

    print(f"\noverall: {'stable' if overall_stable else 'UNSTABLE'}")
    return 0 if overall_stable else 1


if __name__ == "__main__":
    sys.exit(main())
