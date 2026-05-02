"""Run code-based graders. Each is a script that takes a transcript path and
optional args, and exits 0 (pass), 1 (fail), or 2 (unknown). stdout is captured
as the grader's reasoning."""
from __future__ import annotations

import subprocess
from pathlib import Path


def run_code_grader(
    *,
    script: Path,
    transcript_path: Path,
    teach_home: Path,
    args: list[str],
    timeout: int = 30,
) -> dict:
    cmd = [str(script), str(transcript_path), str(teach_home), *args]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    if proc.returncode == 0:
        verdict = "pass"
    elif proc.returncode == 1:
        verdict = "fail"
    else:
        verdict = "unknown"
    return {
        "verdict": verdict,
        "reasoning": (proc.stdout + proc.stderr).strip(),
        "exit_code": proc.returncode,
    }
