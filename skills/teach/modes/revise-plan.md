# Revise-plan mode

Goal: negotiate changes to the arc with the learner until they commit to (or recommit to) it. Runs after `propose-plan` for the initial commit, and whenever the learner asks to replan mid-course. Same loop in both cases — surface what's there, ask for changes, edit live, confirm.

**Roots** (see `README.md` for full citations): Vygotsky's zone of proximal development (the arc has to land in the band between what the learner can do alone and with help); Bloom's "2 sigma" on tutoring (individualized calibration is most of why tutoring works); Knowles on andragogy (adult learners need to own the plan, not receive it); Hamming on research areas (replan when evidence has accumulated, not on every bad day).

## How to run it

1. **Read `$TEACH_HOME/syllabus.md`.** This mode has two shapes depending on what you find:
   - **First commit** — all items `pending`, no deviations. You just came from `propose-plan`; the task is to commit the draft or send it back for redrafting.
   - **Mid-course** — any item is `done` / `in progress` / `deferred`, or there are deviation entries. You are reshaping a committed plan.

2. **Surface what's there.**
   - First commit: show the full arc with `Goal` and `Non-goals` above it. Not piecemeal — the whole ladder in order.
   - Mid-course: "You're three items in. Two `done`, one `in progress`. Three deviations so far, all around the frame clause." Ground the conversation in evidence, not feelings.

3. **Ask the right opening question.**
   - First commit — three pushback axes force engagement:
     - "Anything here you already have and can skip?"
     - "Anything missing that should be on this list?"
     - "Anything in the wrong order for how you want to learn it?"
   - Mid-course: "What's prompting the replan?"

4. **Route by the answer.**
   - First commit:
     - Substantive pushback → go to step 5.
     - Passive agreement / "looks good" → force a choice: "Which item are you most excited to get to? Which least?" If they still can't name one, the arc is too abstract. Back to `propose-plan` to concretize — with an explicit instruction that the redraft must use observable-behavior phrasing (verb + object), not concept names. If the second draft also fails this test, end planning: "I don't have enough about what you want to *do* with this to design the arc. Let's talk about what the first concrete win would look like before drafting further."
   - Mid-course:
     - **"The goal has changed"** → this is a topic pivot, not a reshape. Archive the current syllabus first (see *Archive before redraft* below), then hand to `propose-plan` for a fresh syllabus under the new goal.
     - **"Items are wrong / missing"** → edit live on remaining `pending` items only.
     - **"The order is wrong"** → reorder remaining items in place.
     - **"Bored / losing momentum"** → not yet a replan reason. Probe: is the current item too easy, too hard, or disconnected from the goal?

5. **Edit `$TEACH_HOME/syllabus.md` live** per `references/state-editing-protocol.md`. Visible change gives the learner ownership and catches drift early ("wait, I didn't mean to drop that one").

6. **Check the deviations log (mid-course only).** If the same topic shows up three or more times, that is the learner's attention voting — offer to add it as an arc item.

7. **Scale check.** Bloat (learner keeps adding without removing) → remind of non-goals, ask what they'd drop to add. Meaningfully different arc:
   - First commit → back to `propose-plan` for a fresh draft (safe to overwrite; no progress yet).
   - Mid-course → this is effectively a topic pivot. Archive the current syllabus first (see *Archive before redraft* below), then hand to `propose-plan`. Do not salvage in place.

8. **Show the final diff before committing.** "Dropping 5, moving 7 up, adding a new item between 3 and 4 on X. OK?" Wait for confirmation.

9. **Confirm commitment out loud.**
   - First commit: "So this is what we're learning. Tutoring will work through this arc in order. If you want to replan partway, we'll do that explicitly."
   - Mid-course: "Arc updated — resuming on item N."
   - Wait for acknowledgement, not silence.

10. **Exit.** The session flow returns to the main decision tree in `SKILL.md`, which picks a tutoring mode.

## Archive before redraft

When a mid-course revise-plan routes back to `propose-plan` (goal changed, or the arc is meaningfully different), the existing `$TEACH_HOME/syllabus.md` contains real progress (`done` items, deviations) that must not be destroyed. Before handing to `propose-plan`:

1. Rename `$TEACH_HOME/syllabus.md` to `$TEACH_HOME/syllabus-archived-YYYY-MM-DD.md`. If that name already exists, append a short topic slug (e.g. `syllabus-archived-YYYY-MM-DD-sql.md`).
2. Tell the learner: "Archiving the previous syllabus to `<filename>`. Done items and deviations are preserved there; the new syllabus starts fresh."
3. Update `learner.md`'s `Currently studying` and `Goal` to the new values before calling `propose-plan`.

`propose-plan` then writes a fresh `syllabus.md` normally.

Never overwrite a non-empty `syllabus.md` directly — always archive first. This rule preserves the append-only `Deviations` contract in `references/state-editing-protocol.md`.

## When the right answer is "no change" (mid-course only)

Not every replan request should produce edits. If the arc is working and the learner is hitting friction because the material is genuinely hard, say so:

> "Looking at the arc and the deviations, the plan still fits what you said you wanted. The current item is harder than the last two — that is the point where most people want to replan. My read is we push through. Does that land?"

If they agree, write nothing. The deviations log already speaks for itself.

## What not to do

- **Do not accept passive agreement.** "Sounds fine" is a no-signal. Make them choose.
- **Do not oversell the arc.** If a reasonable alternative order exists, say so rather than defending the draft. Credibility depends on not spinning.
- **Do not replan preemptively (mid-course).** If the learner did not ask, do not propose.
- **Do not let the learner defer an item because it was hard today.** Hard is a learning signal, not a planning signal. Probe for the specific gap; a conceptual gap is material for a tutoring mode, not for replanning.

## Output

- Edited `syllabus.md` reflecting agreed changes, or unchanged if mid-course concluded "push through."
- `Goal` and `Non-goals` may be updated if reshaped during a first-commit pass.
- `Deviations` untouched — that log is written only by tutoring sessions, not by planning modes.

## Logging

Append to today's session log: what shifted between pre- and post-revise-plan state (items added, dropped, reordered). "Revised arc, kept as-is" is also data — log it when no change was made.
