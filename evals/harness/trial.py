"""Run one trial: spin a sandbox, replay scripted user turns through `claude -p`,
capture the transcript.

Each trial is isolated: a fresh $TEACH_HOME copy, a fresh session id. The agent
is given the teach SKILL.md as appended system prompt and read access to the
skill directory so it can load references on demand.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import uuid
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SKILL_DIR = REPO_ROOT / "skills" / "teach"
SKILL_MD = SKILL_DIR / "SKILL.md"


@dataclass
class Turn:
    role: str  # "user" | "assistant"
    content: str
    raw: dict | None = None  # full claude -p JSON for assistant turns


@dataclass
class TrialResult:
    trial_id: str
    teach_home: Path
    model: str
    turns: list[Turn] = field(default_factory=list)
    error: str | None = None
    total_cost_usd: float = 0.0

    def transcript_md(self) -> str:
        out = [f"# Trial {self.trial_id}", ""]
        for t in self.turns:
            out.append(f"## {t.role}")
            out.append("")
            out.append(t.content.strip())
            out.append("")
        if self.error:
            out += ["## ERROR", "", self.error, ""]
        return "\n".join(out)


def _seed_teach_home(fixture_dir: Path, dest: Path) -> None:
    # Idempotent: if a previous run left a sandbox behind, blow it away rather
    # than letting copytree fail and look like a model error.
    if dest.exists():
        shutil.rmtree(dest)
    if fixture_dir.exists():
        shutil.copytree(fixture_dir, dest)
    else:
        dest.mkdir(parents=True)
    (dest / "sessions").mkdir(exist_ok=True)


def _build_system_prompt() -> str:
    """The agent runs as a vanilla Claude Code session with the teach SKILL.md
    appended to the default system prompt. The skill resolves $TEACH_HOME from
    the env var we set per trial."""
    return SKILL_MD.read_text()


def _run_turn(
    *,
    user_text: str,
    session_id: str,
    sandbox: Path,
    teach_home: Path,
    is_first: bool,
    model: str,
    timeout: int = 240,
) -> dict:
    cmd = [
        "claude",
        "-p",
        "--model", model,
        "--output-format", "json",
        "--dangerously-skip-permissions",
        "--add-dir", str(SKILL_DIR),
        "--add-dir", str(teach_home),
    ]
    if is_first:
        cmd += [
            "--session-id", session_id,
            "--append-system-prompt", _build_system_prompt(),
        ]
    else:
        cmd += ["--resume", session_id]

    cmd.append(user_text)

    env = os.environ.copy()
    env["TEACH_HOME"] = str(teach_home)

    proc = subprocess.run(
        cmd,
        cwd=str(sandbox),
        env=env,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"claude -p exited {proc.returncode}\nstderr:\n{proc.stderr}\nstdout:\n{proc.stdout[:2000]}"
        )
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        raise RuntimeError(
            f"could not parse claude -p output as JSON: {e}\nstdout:\n{proc.stdout[:2000]}"
        ) from e


def _extract_text(claude_json: dict) -> str:
    # claude -p --output-format json returns {"result": "...", ...} for the
    # final assistant message.
    return claude_json.get("result", "") or ""


def run_trial(
    *,
    trial_id: str,
    scripted_turns: list[str],
    fixture_dir: Path,
    work_root: Path,
    model: str = "opus",
) -> TrialResult:
    sandbox = work_root / trial_id
    sandbox.mkdir(parents=True, exist_ok=True)
    teach_home = sandbox / ".teach"
    _seed_teach_home(fixture_dir, teach_home)

    session_id = str(uuid.uuid4())
    result = TrialResult(trial_id=trial_id, teach_home=teach_home, model=model)

    for i, user_text in enumerate(scripted_turns):
        result.turns.append(Turn(role="user", content=user_text))
        try:
            raw = _run_turn(
                user_text=user_text,
                session_id=session_id,
                sandbox=sandbox,
                teach_home=teach_home,
                is_first=(i == 0),
                model=model,
            )
        except Exception as e:  # noqa: BLE001
            result.error = f"turn {i} failed: {e}"
            break
        result.total_cost_usd += float(raw.get("total_cost_usd") or 0.0)
        result.turns.append(Turn(role="assistant", content=_extract_text(raw), raw=raw))

    return result
