# Evals for the `teach` skill

A small harness that runs the `teach` skill against scripted multi-turn scenarios and grades each trial with a mix of code-based and LLM-judge graders. Modeled on Anthropic's [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).

The harness uses the **Claude CLI** (`claude -p`) for both the agent under test and the LLM judge. No `ANTHROPIC_API_KEY` required — it runs against your logged-in CLI session.

## Layout

```
evals/
├── run.py                       # entry point
├── harness/
│   ├── trial.py                 # spin sandbox, replay scripted turns, capture transcript
│   ├── judge.py                 # LLM-judge call via `claude -p --json-schema`
│   └── grade.py                 # invoke code graders
├── tasks/<category>/<id>.json   # task definitions
├── graders/
│   ├── code/                    # bash scripts; exit 0=pass, 1=fail, 2=unknown
│   └── judge/                   # markdown system-prompts for the judge
├── fixtures/teach_home/<name>/  # pre-seeded $TEACH_HOME states
└── reports/YYYY-MM-DD-HHMMSS/   # gitignored output (transcripts + verdicts + summary.json)
```

## Run

```bash
python run.py                                   # run all tasks
python run.py refusal                           # filter by path substring
python run.py refusal --trials 1                # override trials-per-task (dev/smoke loop)
python run.py refusal --model haiku             # override agent model (cheap smoke runs)
```

The agent model is pinned per task (defaults to `opus`) so re-runs are reproducible. Override with `--model` or set `"model": "..."` in the task JSON.

Each task runs N independent trials in their own sandbox dir with a fresh `$TEACH_HOME` seeded from the named fixture. Sessions persist per-trial via `--session-id` / `--resume`, so multi-turn state is real (not faked by concatenation).

## Adding a task

A task is one JSON file under `tasks/<category>/`. Minimal shape:

```json
{
  "id": "refusal/just-tell-me",
  "fixture": "calibrated-joins",
  "trials": 3,
  "script": [
    "Teach me window functions. Start with RANK().",
    "Just tell me the answer."
  ],
  "graders": [
    {"type": "code",  "name": "no_answer_leak", "script": "graders/code/no_answer_leak.sh", "args": ["1, 1, 3"]},
    {"type": "judge", "name": "refusal_intact", "prompt": "graders/judge/refusal-intact.md", "model": "haiku"}
  ],
  "expect": {"pass_at_1": 0.8}
}
```

A trial passes iff **every** grader returns `pass`. `unknown` counts as fail for aggregation but is reported separately so you can spot judge instability.

### Code graders

Bash scripts called as `<script> <transcript_path> <teach_home> <args...>`. Exit codes: `0` pass, `1` fail, `2` unknown. stdout is captured as the verdict reasoning.

Use these for anything mechanical: token-leak checks, file-existence checks, schema validation on `learner.md`/`review.md`, gate-order detection in transcripts.

### Judge graders

Each is a markdown file under `graders/judge/`. The judge runs as `claude -p --model <model> --system-prompt <file> --json-schema <schema>`. The harness enforces the verdict shape:

```json
{
  "verdict": "pass" | "fail" | "unknown",
  "confidence": 0.0-1.0,
  "reasoning": "...",
  "evidence_quote": "...",
  "fields": { "<arbitrary_bools>": true }
}
```

Always give the judge an `"unknown"` escape hatch (per the doc's guidance). Judges should classify a single dimension at a time — write a separate judge prompt per behavior rather than a holistic "is this good".

## Fixtures

A fixture is a directory under `fixtures/teach_home/<name>/` containing a pre-seeded `learner.md`, `review.md`, and optional `syllabus.md`. The harness `cp -r`s it into the sandbox at the start of each trial.

Use fixtures to control upstream state: e.g. `calibrated-joins` represents a learner with calibration done and known-solid joins, so a task can test mid-Socratic behavior on window functions without paying the full calibration arc each trial.

## What this harness does NOT do (yet)

- **Persona-driven simulated learners.** All current tasks are scripted-turns. Adding personas (a second `claude -p` instance acting as the learner) is the natural next step for the right-answer-wrong-reasoning tasks.
- **CI integration.** The intent is `python run.py regression` on PRs against `main`, but no GitHub Actions workflow ships in this initial cut.
- **Human-label calibration set for the judge.** The doc recommends periodically calibrating the LLM judge against expert labels; not yet wired.
- **Capability vs regression separation.** Currently one task; the directory layout supports the split (`tasks/refusal/`, `tasks/regression/`) but the runner doesn't gate them differently.

## Cost note

This harness pays real model costs against your CLI plan. A single trial of a 5-turn refusal task uses Opus for the agent (the `teach` skill's behavior is model-sensitive) and Haiku for the judge. Expect ~$1–2 per task at 2 trials. Each `summary.json` reports per-task and total `cost_usd`. Use `--trials 1 --model haiku` while iterating on the harness itself.
