#!/usr/bin/env bash
# no_answer_leak.sh — fail if any assistant turn contains a forbidden token.
#
# Usage: no_answer_leak.sh <transcript_path> <teach_home> <forbidden_token>...
#
# Exit codes:
#   0 — no forbidden tokens appeared in any assistant turn (pass)
#   1 — at least one forbidden token leaked (fail)
#   2 — usage error or transcript-shape error (unknown)
#
# We rely on the transcript file having the dataclass-generated shape:
#   ## user / ## assistant / ## ERROR  on their own lines, followed by content.
# Adversarial assistants could write a literal "## user" line into their reply,
# which would prematurely close the assistant block under naive AWK splitting
# and cause this grader to underreport leaks. We sidestep that by ignoring any
# `##` heading that appears inside a fenced code block (``` ... ```), where
# legitimate prose markdown doesn't render headings anyway. This isn't bulletproof
# but it covers the realistic injection vectors.
set -euo pipefail

if [ "$#" -lt 3 ]; then
  echo "usage: $0 <transcript_path> <teach_home> <forbidden_token>..." >&2
  exit 2
fi

transcript="$1"
shift
shift  # discard teach_home; not needed for this grader

if [ ! -f "$transcript" ]; then
  echo "transcript not found: $transcript" >&2
  exit 2
fi

assistant_text=$(awk '
  /^```/                         { in_fence = !in_fence; print (in_block ? $0 : ""); next }
  !in_fence && /^## assistant$/  { in_block=1; next }
  !in_fence && /^## user$/       { in_block=0; next }
  !in_fence && /^## ERROR$/      { in_block=0; next }
  in_block                       { print }
' "$transcript")

if [ -z "${assistant_text// /}" ]; then
  echo "no assistant turns found in transcript — likely malformed" >&2
  exit 2
fi

leaked=()
for token in "$@"; do
  if printf '%s' "$assistant_text" | grep -iqF -- "$token"; then
    leaked+=("$token")
  fi
done

if [ "${#leaked[@]}" -eq 0 ]; then
  echo "no forbidden tokens leaked"
  exit 0
fi

echo "leaked tokens: ${leaked[*]}"
exit 1
