# State editing protocol

The learner's state (`learner.md`, `review.md`, session logs) is the skill's long-term memory. It must not degrade. Markdown freeform editing by an LLM tends to drift — sections rename themselves, items duplicate, formatting inconsistencies pile up — and a corrupted profile is worse than no profile.

These rules are strict. Follow them literally, not in spirit.

## Universal rules for all state files

1. **Preserve headings verbatim.** Section headings (`## Known solid`, `## Shaky`, etc.) are contracts with future sessions. Do not rename, rewrite, reorder, or translate them. If a heading needs to change, that is a skill-level change, not a session-level edit.

2. **Edit only the sections your current action requires.** If you are moving an item from Shaky to Known solid, do not also reword other entries in Known solid. Unrelated sections stay untouched. This rule prevents the most common corruption mode: the LLM "tidies up" and loses signal.

3. **Read before writing.** Every time. Do not write based on memory of what the file contained — file it from disk, then edit, then write. State may have been edited between your reads (by the learner, by a concurrent session, or by a prior you who forgot).

4. **Append, don't rewrite.** When adding a new item to a section, append to the existing list. Do not rebuild the list.

5. **Dedupe on write.** Before adding an item, scan the target section for an existing entry on the same concept. If one exists, update that entry (add the date, adjust the note) rather than creating a duplicate. Duplicate detection is semantic, not string-equal — "window frame clause" and "ROWS vs RANGE in frame clauses" likely refer to the same thing.

## Item format

Every item in `learner.md` and `review.md` is a single bullet line. Format:

```
- <concept, short noun phrase> — <status/date/note>
```

Examples:
- `- PARTITION BY vs GROUP BY — confused 2026-04-22, corrected 2026-04-24`
- `- ROW_NUMBER tie behavior — clean retrieval 2026-04-20`
- `- Frame clauses (ROWS vs RANGE) — introduced 2026-04-24`

Rules for the note:
- Keep it on one line. Multi-line notes fragment the file structure and confuse future sessions.
- Dates in `YYYY-MM-DD`.
- Append new status to the existing note rather than replacing it — the history is useful.
- If a note gets too long to read (more than ~100 chars), summarize and move the detail to the most recent session log.

## `learner.md` specific rules

- The five canonical sections are: `Currently studying`, `Known solid`, `Shaky`, `Misconceptions caught`, `Diagnostic summaries`. Do not add new top-level sections without a skill-level reason.
- `Currently studying` is a single topic, not a list. Replace it when the topic shifts.
- `Misconceptions caught` entries should include both the wrong belief and the correction. Example: `- Thought PARTITION BY required ORDER BY — corrected 2026-04-20. In fact ORDER BY is required only for ranking functions.`
- When an item moves from Shaky to Known solid (or vice versa), move the entire bullet line. Do not leave a ghost entry behind. Do not copy — move.

## `review.md` specific rules

- The three canonical buckets are: `new`, `learning`, `mastered`. Do not add others.
- An item lives in exactly one bucket at a time. When moving, delete from the source bucket and add to the destination. No duplicates across buckets.
- When demoting a `mastered` item back to `learning`, append a note explaining what was missed — that context is what makes the next drill effective.

## Session logs

- One file per date: `sessions/YYYY-MM-DD.md`. If a second session occurs on the same day, append to the existing file under a `## Session 2` heading — do not create a new file with a suffix.
- Logs are append-only during a session. Do not rewrite earlier entries in the same session.
- At session end, you may append a short reflection section, but do not rewrite the turn-by-turn notes.

## When the file is already corrupted

If you read a state file and it has drifted — unexpected headings, malformed items, duplicates — do NOT silently "fix" it by rewriting. Instead:

1. Tell the learner: "I notice `learner.md` has some structure I didn't expect — I'm going to leave it alone for now and work with what I can parse."
2. Work with the parseable parts.
3. At session end, offer to help them clean it up as an explicit, collaborative action — not a silent edit.

Silent correction of corruption is how the profile's history gets rewritten without the learner knowing, which is the worst failure mode.
