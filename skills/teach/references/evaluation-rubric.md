# Evaluation rubric

**Roots** (see `README.md` for full citations): Feynman's *Cargo Cult Science* — "the first principle is that you must not fool yourself — and you are the easiest person to fool." The evaluation rubric exists to catch self-deception, especially in the "right answer, wrong reasoning" category — the one that *looks like* success and *is* failure.

When the learner answers, classify the response into one of four categories. Each routes to a different next move. The classification is the most important judgment you make in a session — it decides what happens next.

## The four categories

### 1. Correct with good reasoning

The answer is right AND the reasoning they showed (or would show, if asked) is sound.

**Signals**: they explained *why*, the why is correct, and the explanation used the right concepts at the right level.

**Next move**: climb the ladder. Ask the next harder question, or introduce the next concept that builds on this one.

### 2. Partially correct

Part of the answer is right, part is missing or wrong. Often looks like: correct for the happy path, missing an edge case, or correct at the surface level but missing the mechanism.

**Signals**: you find yourself wanting to say "yes, and..." or "yes, but...". That means you are about to acknowledge the correct part and target the gap.

**Next move**: explicitly acknowledge the correct part in one short sentence, then ask a narrower question that targets the gap. Do NOT move on. Partially correct that is treated as correct becomes "Known solid" in the profile and rots from there.

### 3. Right answer, wrong reasoning

**This is the most important category to catch.** The learner said the correct final thing but got there by bad reasoning — coincidence, pattern-matching without understanding, or a broken mental model that happened to produce the right output on this input.

**Signals**:
- The answer is right but the explanation doesn't mention the real mechanism.
- They generalized from a surface feature ("it's about joins, so it's NULL").
- They guessed and you can tell.
- You ask "why?" and they can't say.

**Next move**: do NOT accept it. "You got the right answer — walk me through how you got there." If the walkthrough reveals broken reasoning, treat it like a misconception (category 4). Never let a right answer with wrong reasoning promote an item to "Known solid" — it is a time bomb that will fail on the next variation.

This is the category most tutors miss, because the right answer looks like success. The whole point of Socratic mode is catching this one — if you are not catching it, you are not Socratic teaching, you are just asking questions.

### 4. Wrong / misconception

The answer is wrong. Sub-categories:

- **Simple wrong** — they just do not know yet. Neutral, easy to work with.
- **Misconception** — they confidently believe something false. More dangerous, because the false belief is actively interfering with learning the true one.

**Signals of misconception vs simple wrong**: confidence. A learner who says "I think maybe it returns zero?" is simple-wrong. A learner who says "Obviously it returns zero, because of X" is mis-conceiving.

**Next move for simple wrong**: step down the refusal ladder — ask a smaller question that lets them try again.

**Next move for misconception**: do not correct directly. Ask a question that puts their belief under pressure. "Okay — if that's true, what would happen if I changed X?" Let them discover the contradiction. Then, *after* they've felt the contradiction, you can explain the correct model briefly. Record it under "Misconceptions caught" in `learner.md` — these are the highest-signal entries in the profile because they are the beliefs most likely to interfere with future learning.

## Practical tips

- **When in doubt between categories 1 and 3, assume 3 and probe.** Cost of a false alarm: one extra question. Cost of a miss: the learner builds on a bad foundation.
- **Resist speed.** It is tempting to treat the first plausible answer as correct and move on. The learner's time is better spent on three questions probed carefully than ten questions rushed.
- **State the classification implicitly through your next move, not explicitly.** Do not say "that is partially correct" — just acknowledge the correct part and ask about the gap. Labels feel like grading; probing feels like collaboration.
