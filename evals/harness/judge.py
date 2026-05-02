"""Invoke `claude -p` as an LLM judge over a transcript.

The judge prompt lives in graders/judge/<name>.md and must instruct the model
to return strict JSON. We pin the model and use --json-schema to enforce the
verdict shape, with an "unknown" escape hatch per the eval methodology.
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

DEFAULT_JUDGE_MODEL = "haiku"

VERDICT_SCHEMA = {
    "type": "object",
    "properties": {
        "verdict": {"type": "string", "enum": ["pass", "fail", "unknown"]},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
        "reasoning": {"type": "string", "minLength": 1},
        "evidence_quote": {"type": "string"},
        "fields": {
            "type": "object",
            "additionalProperties": {"type": ["boolean", "string", "number"]},
        },
    },
    # Require all fields so judge prompts cannot silently omit them; this also
    # forces judges to corroborate `verdict` with `fields` rather than waving
    # at the rubric in `reasoning` only.
    "required": ["verdict", "confidence", "reasoning", "evidence_quote", "fields"],
    "additionalProperties": False,
}


def judge_transcript(
    *,
    judge_prompt_path: Path,
    transcript_md: str,
    model: str = DEFAULT_JUDGE_MODEL,
    timeout: int = 180,
) -> dict:
    judge_prompt = judge_prompt_path.read_text()
    user_input = (
        "Transcript to evaluate:\n\n"
        "<transcript>\n"
        f"{transcript_md}\n"
        "</transcript>\n\n"
        "Return your verdict as a JSON object matching the schema."
    )

    cmd = [
        "claude",
        "-p",
        "--model", model,
        "--output-format", "json",
        "--system-prompt", judge_prompt,
        "--json-schema", json.dumps(VERDICT_SCHEMA),
        "--dangerously-skip-permissions",
        user_input,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if proc.returncode != 0:
        # claude -p surfaces auth and quota errors on stdout, not stderr —
        # surface both so failures aren't silently mis-diagnosed.
        return {
            "verdict": "unknown",
            "reasoning": (
                f"judge invocation failed (exit {proc.returncode}). "
                f"stderr: {proc.stderr[:300]} stdout: {proc.stdout[:300]}"
            ),
        }

    try:
        outer = json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        return {
            "verdict": "unknown",
            "reasoning": f"could not parse claude -p envelope: {e}",
            "raw": proc.stdout[:1000],
        }

    # With --json-schema, the validated output lives at structured_output;
    # `result` is just a free-text confirmation string from the model.
    if "structured_output" in outer and outer["structured_output"]:
        return outer["structured_output"]

    # Fallback: model returned its JSON inline in `result`. We still apply a
    # minimum-viable shape check so a free-form "looks like JSON" reply can't
    # masquerade as a verdict.
    inner = outer.get("result", "")
    try:
        parsed = json.loads(inner)
    except json.JSONDecodeError:
        return {
            "verdict": "unknown",
            "reasoning": "judge returned no structured_output and result was not parseable JSON",
            "raw_result": inner[:1000],
        }
    required = {"verdict", "reasoning"}
    if not isinstance(parsed, dict) or not required.issubset(parsed):
        return {
            "verdict": "unknown",
            "reasoning": f"fallback JSON missing required keys {required - set(parsed) if isinstance(parsed, dict) else 'n/a'}",
            "raw_result": inner[:1000],
        }
    return parsed
