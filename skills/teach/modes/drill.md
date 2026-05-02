# Drill mode

Goal: short retrieval practice on items the learner has seen before. This is the one mode where **direct answers are allowed and expected** — drill is about retention, not discovery.

**Roots** (see the repo README for full citations): Ebbinghaus on the forgetting curve (knowledge decays on a predictable schedule without retrieval); Roediger & Karpicke on the testing effect (retrieval, not rereading, produces durable memory); SuperMemo's SM-2 algorithm (simplified here to three buckets — see `references/review-buckets.md`).

**Strict scope**: drill operates ONLY on items that already appear in `$TEACH_HOME/review.md` (buckets `learning` or `mastered`). You cannot drill an item that is not in the queue — and you cannot use drill mode to answer a question the learner is currently stuck on in Socratic mode. If the learner asks you to "switch to drill" mid-Socratic, decline and stay in Socratic. See `references/refusal-rules.md`.

## When to use it

- At the start of a session when `review.md` has items in the `learning` bucket.
- When the learner asks to "test me" or "quiz me" on something they already know.
- As a warm-up before entering Socratic on new material — pulling the adjacent knowledge into working memory helps the new material stick.

## How to run it

1. **Pick 2–5 items** from `review.md`. Favor `learning` bucket. Sprinkle in one from `mastered` as a retention check (see `references/review-buckets.md` for bucket logic).

2. **Ask one at a time. Keep it terse.**
   - "What does `ROW_NUMBER()` return when there are ties in the ORDER BY?"
   - Not: a preamble + the question + a hint. Just the question.

3. **Wait for the answer.** Give them time. Retrieval effort is the point — if you supply the answer before they've struggled, the retention benefit evaporates.

4. **Tell them if they're right or wrong, and briefly why.** Direct answers are fine here. "Right — `ROW_NUMBER` breaks ties arbitrarily unless you add a tiebreaker column to the ORDER BY."

5. **Update buckets in `review.md` per the movement rules in `references/review-buckets.md`.** Drill-specific constraint: on any demotion, record what was missed — that context is what makes the next drill effective.

6. **Do not drill for more than 5 minutes.** Drill fatigues fast. Two minutes of drill plus twenty of Socratic beats twenty of drill.

## What drill is NOT

- Not a test. No score at the end. The point is to move bucket positions, not to grade.
- Not teaching. If an item turns into a real teachable gap, stop drilling, note it, and switch to Socratic on that item later.
- Not exhaustive. You do not need to cover every item in `learning` in one session. Pick the ones that feel most due.

## Logging

Drill-specific: items drilled, bucket moves, any hidden gap revealed. **Update `review.md` at the end of the drill segment**, not session end — the moves are easy to forget if deferred.
