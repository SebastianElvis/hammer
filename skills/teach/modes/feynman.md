# Feynman mode

Goal: the learner explains a concept back to you, and you probe their explanation for gaps. This is a *consolidation* mode — use it after they have already seen the material, not for first exposure.

**Roots** (see the repo README for full citations): Feynman's *Lectures on Physics* preface (teaching as the test of one's own understanding); Feynman's *"Surely You're Joking"* Brazil chapter (fluency-without-recognition as the failure mode to detect); Feynman's *Cargo Cult Science* ("you must not fool yourself — and you are the easiest person to fool," which is the guiding principle for what to probe).

## The four steps (the technique, as Feynman practiced it)

1. **Pick a concept and name it.** Explicit, narrow, one concept.
2. **Explain it in plain language** as if to someone who does not know it. No jargon without definition.
3. **Find the gaps** — the places where the explanation breaks down, hand-waves, or requires unstated assumptions. This is the whole point: the gaps are the understanding that is missing.
4. **Return to the source** on those specific gaps, then simplify further and re-explain.

In this skill, the *tutor* runs steps 3 and 4 — the learner does steps 1 and 2, and the tutor surfaces the gaps and decides whether to dig (step 4 as Socratic sub-questioning) or note the gap for later study.

## The loop

1. **Pick a concept from `learner.md`** — something in "Shaky" that they have studied, or something in "Known solid" that you want to verify actually is solid.
2. **Frame the task.** "Explain X to me like I'm someone who knows programming but has never seen X. Take your time."
3. **Let them explain uninterrupted.** Do not correct mid-stream. Let the full explanation land.
4. **Probe the gaps.** Look for:
   - **Hand-waves** — places where they said "basically" or "kind of" or "it just works." That is where the understanding is thin.
   - **Jargon without definition** — they used a term without having introduced it. Ask what it means.
   - **Missing edge cases** — the explanation works for the happy path but they did not mention when it breaks. Ask.
   - **Causal gaps** — they said "X happens, and then Y" but did not explain *why* Y follows from X.
5. **Ask one gap at a time.** Same rule as Socratic — one question, wait, judge.
6. **When a gap appears, do not fill it.** Point at it and ask them to fill it. "You said it 'just works' there — can you go one level deeper?"

## What good probing looks like

- "You said `PARTITION BY` splits the data into groups. What happens to those groups after they're split?"
- "Walk me through what would happen if the input were empty."
- "You used the word 'frame' twice — what's a frame, in this context?"
- "That sounds right for a running total. Would the same explanation work for a running *average*?"

## When to stop

- The learner's explanation holds up to three or four probes without hand-waves. They understand it. Move it to "Known solid" at session end.
- The learner's explanation falls apart immediately. They did not actually have this consolidated — drop back to Socratic on the specific gap you found, and come back to Feynman later.

## Logging

Feynman-specific: concept explained and gaps surfaced (e.g. "Explained window frames; could not articulate `ROWS` vs `RANGE`. Moved to Shaky"). Often reveals that something both sides thought was solid actually is not.
