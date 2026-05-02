# Review buckets

**Roots** (see the repo README for full citations): Ebbinghaus's forgetting curve (knowledge decays without retrieval); Karpicke & Roediger on retrieval practice (the act of recalling, not rereading, is what produces durable memory); Wozniak's SM-2 algorithm (the canonical adaptive-interval scheduler, here simplified to three buckets because the LLM-driven substrate makes date-math fragile).

Spaced retrieval for retention, using three buckets instead of date-based intervals. Buckets are simpler than SM-2 and robust — no date math, no fragile intervals, and items move based on observed performance, not a schedule.

## The three buckets

- **new** — items introduced this session or very recently. Not yet tested for retention.
- **learning** — items the learner has seen and partially holds. Due for retrieval practice. Most drill activity happens here.
- **mastered** — items the learner has retrieved correctly on multiple past occasions with no hint needed.

## Movement rules

- **new → learning**: first successful retrieval after introduction.
- **learning → mastered**: two consecutive clean retrievals on separate sessions (not two in the same session — same-session retrieval overestimates retention).
- **mastered → learning**: any failed retrieval on a `mastered` item. Also add a note on what was missed.
- **learning → learning** (stays): retrieval with hint, or partial retrieval.
- **any → dropped**: if the learner explicitly says they don't want to revisit this, or it has been demoted three times (the item is poorly specified or the underlying concept is missing — address that instead of drilling).

## How `review.md` looks

A single markdown file with three sections. Example:

```markdown
# Review queue

## new
- Frame clauses (ROWS vs RANGE) — introduced 2026-04-24

## learning
- PARTITION BY vs GROUP BY — hinted 2026-04-22, clean 2026-04-24 (one more clean moves to mastered)
- ROW_NUMBER tie behavior — clean 2026-04-20

## mastered
- Basic window function syntax — last retrieved 2026-04-18
```

Items are one-liners. The prose after the em-dash is a note for you — last status, date, any relevant detail. Keep it readable; this is not a database.

## Picking items for drill

At session start:
1. Look at `learning` first. Pick 2–3 items, preferring ones you haven't drilled in the last session or two.
2. Add 1 item from `mastered` as a retention check. Rotate which mastered items get checked — do not always pick the same one.
3. If `learning` is empty and `new` has items, those items are not yet due for drill — they were just introduced. Let them settle for a session before drilling.

## What not to do

- **Do not drill `new` items.** They haven't been learned yet — the first retrieval should come after a short gap, not immediately.
- **Do not move things to `mastered` aggressively.** Two clean retrievals *on separate sessions* is the bar. Same-session success means the item is still in working memory, not long-term.
- **Do not let `learning` grow past ~15 items.** If it's overflowing, the learner is being introduced to new material faster than they can consolidate. Slow down new intake; drill the backlog.
