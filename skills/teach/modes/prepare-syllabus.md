# Prepare-syllabus mode

Goal: produce a committed learning arc for a multi-session topic, written to `$TEACH_HOME/syllabus.md`. This mode does not teach — it builds or reshapes the plan the tutor and learner both respect.

Runs in two shapes:

- **First draft** — no syllabus exists yet (or the `Arc` section is empty). Draft the arc, negotiate with the learner, commit.
- **Revise** — syllabus exists with progress (any item `done` / `in progress` / `deferred`, or any deviation entries). Reshape the committed arc.

The loop is the same in both shapes: surface what's there, ask for changes, edit live, confirm. What differs is the starting point.

**Roots** (see the repo README for full citations): Mager on instructional objectives (state the terminal behavior before designing the path to it); Wiggins & McTighe's *Understanding by Design* (backward design); Hamming's *You and Your Research* ("what are the important problems?"); Vygotsky's zone of proximal development (the arc has to land in the band between alone-capable and with-help-capable); Bloom's "2 sigma" on tutoring; Knowles on andragogy (adult learners need to own the plan, not receive it).

## Before running

1. **Verify calibration.** Read `$TEACH_HOME/learner.md`.
   - If the profile is not calibrated for the current topic — `Goal` / `Currently studying` missing, or no relevant `Known solid` / `Shaky` / `Misconceptions caught` entries — **exit this mode and run `modes/calibration.md` first.** Arc planning consumes calibration, not the other way around.
   - If calibration exists but the `Goal` section itself is missing (older profile schema), follow the migration note in `references/state-editing-protocol.md`.

2. **Read `$TEACH_HOME/syllabus.md`.** Which shape to run depends on what you find:
   - `Arc` empty or missing → **first draft** path.
   - `Arc` populated with any item `done` / `in progress` / `deferred`, or any deviation entries → **revise** path.

## First draft

1. **Frame the task.** "Before we start teaching, I'll draft an arc — the ordered topics we'll work through. You'll shape it before we commit."

2. **Confirm the goal and ask for non-goals.**
   - "Your goal is *<goal>* — still right?" If they revise, update `learner.md`.
   - "Anything you explicitly do NOT want to cover?" Non-goals surprise learners and surface real constraints; a syllabus without non-goals tends to bloat during revision.

3. **Draft 5–10 items, ordered by dependency.**
   - Read `learner.md` carefully. Items in "Known solid" should not appear. Items in "Shaky" may appear as early review items, not as new teaching. Misconceptions caught are the highest-value signal — if the topic touches them, the arc addresses the misconception head-on.
   - Each item is a short noun phrase. Order matters: each item should be learnable given the ones above it. If two items are parallel, one likely belongs in a later syllabus.
   - Concrete beats abstract ("ROW_NUMBER and ranking functions" > "ranking concepts"). One new idea per item — if an item contains "and" or "or," consider splitting. Visible difficulty gradient: first item a foothold the learner can almost reach, last item a stretch.

4. **Write the file.** Populate `$TEACH_HOME/syllabus.md` per `references/state-editing-protocol.md`:
   - `Goal`: the confirmed sentence from step 2.
   - `Non-goals`: bulleted list from step 2.
   - `Arc`: numbered list, all items `pending`.
   - `Deviations`: leave empty — tutoring sessions append here later.

5. **Show the whole arc** with `Goal` and `Non-goals` above it. Not piecemeal — the full ladder in order.

6. **Force engagement with three pushback axes.**
   - "Anything here you already have and can skip?"
   - "Anything missing that should be on this list?"
   - "Anything in the wrong order for how you want to learn it?"

7. **Route by the answer.**
   - **Substantive pushback** → edit live (step 8).
   - **Passive agreement / "looks good"** → force a choice: "Which item are you most excited to get to? Which least?" If they still can't name one, the arc is too abstract. Redraft with observable-behavior phrasing (verb + object), not concept names. If the second draft also fails this test, end planning: "I don't have enough about what you want to *do* with this to design the arc. Let's talk about what the first concrete win would look like before drafting further."
   - **Meaningfully different arc requested** → safe to overwrite; no progress yet. Redraft.

8. **Edit live** per `references/state-editing-protocol.md`. Visible change gives the learner ownership and catches drift early ("wait, I didn't mean to drop that one").

9. **Show the final diff before committing.** "Dropping 5, moving 7 up, adding a new item between 3 and 4 on X. OK?" Wait for confirmation.

10. **Confirm commitment out loud.** "So this is what we're learning. Tutoring will work through this arc in order. If you want to replan partway, we'll do that explicitly." Wait for acknowledgement, not silence.

## Revise

1. **Surface what's there.** "You're three items in. Two `done`, one `in progress`. Three deviations so far, all around the frame clause." Ground the conversation in evidence, not feelings.

2. **Ask the opening question.** "What's prompting the replan?"

3. **Route by the answer.**
   - **"The goal has changed"** → topic pivot, not a reshape. Archive first (see *Archive before redraft* below), then enter the first-draft path with the new goal.
   - **"Items are wrong / missing"** → edit live on remaining `pending` items only.
   - **"The order is wrong"** → reorder remaining items in place.
   - **"Bored / losing momentum"** → not yet a replan reason. Probe: is the current item too easy, too hard, or disconnected from the goal?
   - **Arc meaningfully different** → topic pivot. Archive first, then enter the first-draft path. Do not salvage in place.

4. **Edit `$TEACH_HOME/syllabus.md` live** per `references/state-editing-protocol.md`.

5. **Check the deviations log.** If the same topic shows up three or more times, that is the learner's attention voting — offer to add it as an arc item.

6. **Scale check.** Bloat (learner keeps adding without removing) → remind of non-goals, ask what they'd drop to add.

7. **Show the final diff before committing.** Same as first-draft step 9.

8. **Confirm commitment out loud.** "Arc updated — resuming on item N." Wait for acknowledgement.

## When the right answer is "no change" (revise only)

Not every replan request should produce edits. If the arc is working and the learner is hitting friction because the material is genuinely hard, say so:

> "Looking at the arc and the deviations, the plan still fits what you said you wanted. The current item is harder than the last two — that is the point where most people want to replan. My read is we push through. Does that land?"

If they agree, write nothing. The deviations log already speaks for itself.

## Archive before redraft

When a revise routes back to a first draft (goal changed, or the arc is meaningfully different), the existing `$TEACH_HOME/syllabus.md` contains real progress (`done` items, deviations) that must not be destroyed. Before redrafting:

1. Rename `$TEACH_HOME/syllabus.md` to `$TEACH_HOME/syllabus-archived-YYYY-MM-DD.md`. If that name already exists, append a short topic slug (e.g. `syllabus-archived-YYYY-MM-DD-sql.md`).
2. Tell the learner: "Archiving the previous syllabus to `<filename>`. Done items and deviations are preserved there; the new syllabus starts fresh."
3. Update `learner.md`'s `Currently studying` and `Goal` to the new values before redrafting.

Then write a fresh `syllabus.md` via the first-draft path.

Never overwrite a non-empty `syllabus.md` directly — always archive first. This rule preserves the append-only `Deviations` contract in `references/state-editing-protocol.md`.

## Exit

The session flow returns to the main decision tree in `SKILL.md`, which enters the teach loop.

## What not to do

- **Do not reproduce a generic curriculum from memory.** Anchor to this learner's goal and profile. A SQL course for a data analyst looks different from one for a backend engineer debugging a slow query.
- **Do not estimate sessions or calendar time.** Arcs inflate in estimation and contract in practice. Commitments about time corrupt the focus on content.
- **Do not accept passive agreement.** "Sounds fine" is a no-signal. Make them choose.
- **Do not oversell the arc.** If a reasonable alternative order exists, say so rather than defending the draft. Credibility depends on not spinning.
- **Do not replan preemptively (revise only).** If the learner did not ask, do not propose.
- **Do not let the learner defer an item because it was hard today.** Hard is a learning signal, not a planning signal. Probe for the specific gap; a conceptual gap is material for a tutoring mode, not for replanning.
- **Do not answer substantive learning questions here.** If the learner asks a teaching question during planning, note it for when tutoring resumes; do not answer on the spot (see `references/refusal-rules.md`).

## Output

- Committed `syllabus.md` reflecting the agreed arc, or unchanged if revise concluded "push through."
- `Goal` and `Non-goals` may be updated if reshaped during a first-draft or goal-pivot pass.
- `Deviations` untouched — that log is written only by tutoring sessions.

## Logging

Append to today's session log:
- First draft: draft goal, number of arc items, notable shaping decisions (items dropped because the learner already had them, misconceptions that drove a specific item).
- Revise: what shifted between pre- and post-revise state (items added, dropped, reordered). "Revised arc, kept as-is" is also data — log it when no change was made.
