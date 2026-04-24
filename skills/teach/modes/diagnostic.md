# Diagnostic mode

Goal: in 5–10 minutes, figure out roughly what the learner knows about the topic they named, so future sessions can start at the right level. Output is a populated `learner.md`, not teaching.

**Roots** (see `README.md` for full citations): Vygotsky's zone of proximal development (teaching is most effective in the band between what the learner can do alone and what they can do with help — you have to find the band before you can teach in it); Bloom's "2 sigma" result on tutoring (individualized calibration is most of why tutoring beats group instruction); Hamming's *You and Your Research* ("why this, and why now?" — knowing the learner's motivation is part of calibrating what is worth teaching).

## How to run it

1. **Tell the learner what this is.** One sentence: "Before I start teaching, I want to ask a few calibration questions so I pitch this at the right level. Five minutes, no grades."

2. **Ask once, early, why the learner wants to learn this** (Hamming's nudge). Not in a gatekeeping way — just one light question: "What do you want to be able to do once you understand this?" Their answer shapes what you prioritize and gets logged as a one-liner in the diagnostic summary. If they genuinely do not know, that is a signal to treat the topic as exploratory; lower the bar for declaring "Currently studying" concrete.

3. **Ask 3–5 questions that span the difficulty range.** Start easy, climb. Each question should probe a different sub-skill. Examples for "SQL window functions":
   - Easy: "What does `GROUP BY` do?" (tests: do they have the aggregation foundation window functions build on?)
   - Medium: "If I wanted to compute a running total of sales over time, how would you approach that?" (tests: do they know window functions exist, or would they reach for a self-join?)
   - Harder: "What's the difference between `PARTITION BY` and `GROUP BY`?" (tests: conceptual separation, common sticking point)
   - Edge: "What does the frame clause do?" (tests: awareness of the deeper structure; most people have never heard of it)

3. **Do not teach during diagnostic.** If they get something wrong, say "okay, noted" and move on. Fix the urge to correct. Corrections during calibration contaminate the signal.

4. **Listen for misconceptions, not just wrong answers.** A wrong answer says "they don't know"; a misconception says "they know something false and confidently." The second is more important to catch.

5. **When done, write the profile.** Update `$TEACH_HOME/learner.md`:
   - "Known solid": what they answered confidently and correctly
   - "Shaky": what they fumbled, what they only half-knew
   - "Misconceptions caught": anything they said confidently that was wrong
   - "Currently studying": the topic they came in for
   - Add a one-line "Diagnostic summary — 2026-04-24" with your overall read (e.g., "Comfortable with GROUP BY, hasn't seen window functions, confused PARTITION BY with GROUP BY")

6. **Tell the learner what you heard.** One or two sentences. "Sounds like you're solid on aggregation but haven't really used window functions. Next session I'll start from `ROW_NUMBER` and work up." This gives them a chance to correct your read before it ossifies in their profile.

## When to re-run diagnostic

- They come back after a long gap and their self-assessment has shifted.
- They ask for a topic that their current profile doesn't cover.
- You're getting surprised repeatedly — either teaching things they already knew, or hitting walls on things you thought they had. The profile is wrong; recalibrate.

## What this mode is NOT

- Not a test. No pass/fail. Do not score or grade.
- Not teaching. If you catch yourself explaining, stop.
- Not exhaustive. Five minutes is the budget. A rough map beats an accurate map the learner never gets to use.
