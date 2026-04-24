# Propose-plan mode

Goal: draft an initial arc for the topic, ready for `revise-plan` to negotiate. The output is a draft written to `$TEACH_HOME/syllabus.md` — not a commitment. Commitment happens in `revise-plan`.

**Roots** (see `README.md` for full citations): Mager on instructional objectives (state the terminal behavior before designing the path to it); Wiggins & McTighe's *Understanding by Design* (backward design — work from what "done" looks like back to the first step); Hamming's *You and Your Research* ("what are the important problems?" — applied to learning arcs: the important ladder, not the comprehensive one).

## How to run it

1. **Frame the task in one sentence.** "Before we start teaching, I'm going to draft an arc — the ordered topics we'll work through. You'll get to reshape it in the next step."

2. **Verify calibration, then confirm the goal.** Read `$TEACH_HOME/learner.md`.
   - If the profile is not calibrated for the current topic — `Goal` / `Currently studying` missing, or no relevant `Known solid` / `Shaky` / `Misconceptions caught` entries — **exit this mode and run `modes/calibration.md` first.** Do not ask the goal cold; arc planning consumes calibration, not the other way around.
   - If calibration exists but the `Goal` section itself is missing (older profile schema), follow the migration note in `references/state-editing-protocol.md`.
   - Otherwise, one-line confirm: "Your goal is *<goal>* — still right?" If they revise, update `learner.md`.

3. **Ask for non-goals.** "Anything you explicitly do NOT want to cover?" This question surprises learners and surfaces real constraints. A syllabus without non-goals tends to bloat during revision.

4. **Read `$TEACH_HOME/learner.md` carefully for the arc draft.** Items in "Known solid" should not appear. Items in "Shaky" may appear as early review items but not as new teaching. Misconceptions caught are the highest-value signal — if the topic touches them, the arc addresses the misconception head-on.

5. **Draft 5–10 items, ordered by dependency.** Each item is a short noun phrase. Order matters: each item should be learnable given the items above it. If you cannot order two items ("these are parallel"), one of them likely belongs in a later syllabus.

6. **Write the file.** Populate `$TEACH_HOME/syllabus.md`:
   - `Goal`: the confirmed sentence from step 2.
   - `Non-goals`: bulleted list from step 3.
   - `Arc`: numbered list, all items `pending`.
   - `Deviations`: leave empty — tutoring sessions append here later.

7. **Hand off to `revise-plan`.** One sentence: "Draft is written. Now we'll go through it together — you shape it until it's what you want to learn."

## What a good draft looks like

- **Concrete, not abstract.** "ROW_NUMBER and ranking functions" beats "ranking concepts."
- **One new idea per item.** If an item contains "and" or "or," consider splitting.
- **Visible difficulty gradient.** First item a foothold the learner can almost reach; last item a stretch.
- **Addresses known misconceptions directly.** Arc has an item whose note says "distinguish from GROUP BY" — not one that silently subsumes the distinction.

## What not to do

- **Do not reproduce a generic curriculum from memory.** Anchor to this learner's goal and profile. A SQL course for a data analyst looks different from one for a backend engineer debugging a slow query.
- **Do not estimate sessions or calendar time.** Arcs inflate in estimation and contract in practice. Commitments about time corrupt the focus on content.

## Logging

Append to today's session log: draft goal, number of arc items, notable shaping decisions (items dropped because the learner already had them, misconceptions that drove a specific item).
