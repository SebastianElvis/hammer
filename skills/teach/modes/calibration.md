# Calibration mode

Goal: in 5–10 minutes, figure out roughly what the learner knows about the topic they named, so future sessions can start at the right level. Output is a populated `learner.md`, not teaching. This mode is upstream of tutoring and of planning — everything downstream depends on calibration landing first.

**Roots** (see the repo README for full citations): Vygotsky's zone of proximal development (teaching is most effective in the band between what the learner can do alone and what they can do with help — you have to find the band before you can teach in it); Bloom's "2 sigma" result on tutoring (individualized calibration is most of why tutoring beats group instruction); Hamming's *You and Your Research* ("why this, and why now?" — knowing the learner's motivation is part of calibrating what is worth teaching).

## How to run it

1. **Tell the learner what this is.** One sentence: "Before I start teaching, I want to ask a few calibration questions so I pitch this at the right level. Five minutes, no grades."

2. **Ask once, early, why the learner wants to learn this** (Hamming's nudge). Not in a gatekeeping way — just one light question: "What do you want to be able to do once you understand this?" Their answer becomes the `Goal` recorded in `learner.md` (see step 5) and is what downstream modes — tutoring and planning — read to calibrate what is worth emphasizing. If they genuinely do not know, that is a signal to treat the topic as exploratory; write a short placeholder ("explore enough to decide whether this is worth pursuing") and lower the bar for declaring "Currently studying" concrete.

3. **Ask 3–5 questions that span the difficulty range.** Start easy, climb. Each probes a different sub-skill. Examples for "SQL window functions":
   - Easy: "What does `GROUP BY` do?" (foundation check)
   - Medium: "How would you compute a running total of sales over time?" (do they reach for window functions or a self-join?)
   - Harder: "What's the difference between `PARTITION BY` and `GROUP BY`?" (common sticking point)
   - Edge: "What does the frame clause do?" (awareness of deeper structure)

   If they get something wrong, say "okay, noted" and move on. Do not teach during calibration — corrections contaminate the signal.

4. **Listen for misconceptions, not just wrong answers.** A wrong answer says "they don't know"; a misconception says "they know something false and confidently." The second is more important to catch.

5. **Write the profile.** Update `$TEACH_HOME/learner.md` in canonical section order:
   - `Currently studying` — the topic they came in for.
   - `Goal` — the one-sentence answer from step 2 (follow the migration note in `references/state-editing-protocol.md` if the section is missing).
   - `Known solid`, `Shaky`, `Misconceptions caught` — per the rubric above.
   - Append a bullet under `Calibration notes` in the canonical item format (see `references/state-editing-protocol.md`): `- YYYY-MM-DD — <overall read of level and shape>`. Example: `- 2026-04-24 — Comfortable with GROUP BY, hasn't seen window functions, confused PARTITION BY with GROUP BY`. Level goes here; goal goes in `Goal` — do not duplicate.

6. **Reflect back what you heard.** "Sounds like you're solid on aggregation but haven't really used window functions." Gives them a chance to correct your read before it ossifies.

## When to re-run calibration

- They come back after a long gap and their self-assessment has shifted.
- They ask for a topic that their current profile doesn't cover.
- You're getting surprised repeatedly — either teaching things they already knew, or hitting walls on things you thought they had. The profile is wrong; recalibrate.

## What this mode is NOT

- Not a test. No pass/fail. Do not score or grade.
- Not teaching. If you catch yourself explaining, stop.
- Not exhaustive. Five minutes is the budget. A rough map beats an accurate map the learner never gets to use.
