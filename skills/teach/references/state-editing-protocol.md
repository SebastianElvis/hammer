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

- The six canonical sections are, in this order: `Currently studying`, `Goal`, `Known solid`, `Shaky`, `Misconceptions caught`, `Calibration notes`. Do not add new top-level sections without a skill-level reason.
- `Currently studying` is a single topic, not a list. Replace it when the topic shifts.
- `Goal` is a single sentence stating what the learner wants to be able to *do* once they understand the current topic. Written by calibration mode. Paired with `Currently studying` — when the topic shifts, replace both together. `Goal` holds the motivation/terminal behavior; `Calibration notes` holds level/shape notes from each run. Do not conflate them.
- `Misconceptions caught` entries should include both the wrong belief and the correction. Example: `- Thought PARTITION BY required ORDER BY — corrected 2026-04-20. In fact ORDER BY is required only for ranking functions.`
- When an item moves from Shaky to Known solid (or vice versa), move the entire bullet line. Do not leave a ghost entry behind. Do not copy — move.

### Older profiles missing the `Goal` section

`Goal` was added to the canonical set after initial profiles were created. If you read a `learner.md` that has the other five canonical sections but no `Goal` heading:

1. Tell the learner: "Your profile was created before we tracked a `Goal` field — want me to add it?"
2. If yes, insert the `Goal` heading after `Currently studying` and populate it with the learner's answer.
3. If no, proceed without it. Future sessions can offer again.

This is the one allowed exception to the "never silently rewrite state" rule, and only with explicit learner consent — never autonomously.

## `review.md` specific rules

- The three canonical buckets are: `new`, `learning`, `mastered`. Do not add others.
- An item lives in exactly one bucket at a time. When moving, delete from the source bucket and add to the destination. No duplicates across buckets.
- When demoting a `mastered` item back to `learning`, append a note explaining what was missed — that context is what makes the next drill effective.

## `syllabus.md` specific rules

- The four canonical sections are: `Goal`, `Non-goals`, `Arc`, `Deviations`. Do not add new top-level sections without a skill-level reason.
- `Goal` is a single sentence. Replace it only when `prepare-syllabus` mode concludes the goal has changed — otherwise leave it alone.
- `Arc` items use a **numbered** list, not a bulleted one. Format:

  ```
  N. <concept, short noun phrase> — <status/date/note>
  ```

  Status vocabulary, use exactly these forms:
  - `pending`
  - `in progress since YYYY-MM-DD`
  - `done YYYY-MM-DD`
  - `deferred YYYY-MM-DD (reason)`

- **Do not renumber the Arc list** when an item is deferred, dropped, or rewritten. Items keep their number for the life of the syllabus; numeric gaps are fine. Renumbering invalidates references in the Deviations log and in session logs. New items get the next unused number, not a reused one.
- `done YYYY-MM-DD` is written **only at session end by tutoring sessions**, and only when the arc item meets the same mastery bar used for moving items from `learning` to `mastered` in the review queue (two clean retrievals on separate sessions). `prepare-syllabus` mode does not write `done` — it authors the arc; tutoring sessions author progress.
- `Deviations` is append-only. Format:

  ```
  - YYYY-MM-DD: <what was done instead> — <why>
  ```

  Never delete deviation entries. They are the evidence trail that tells `prepare-syllabus` mode whether the arc still fits reality.

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
