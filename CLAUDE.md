# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

`hammer` is a skills repo. The shipped artifact is plain markdown: agents load it on demand, there is nothing to build or lint. Currently contains one skill: `teach` (a tutoring skill named after Richard Hamming).

There is also a Python eval harness in `evals/` (see "Evals" below). It is **not** part of the shipped skill — it exists to validate skill behavior against scripted scenarios. Don't import or reference `evals/` from `skills/`.

The repo is dual-packaged:
- **`vercel-labs/skills` format** — installable via `npx skills add SebastianElvis/hammer`.
- **Claude Code plugin** — `.claude-plugin/marketplace.json` makes it `/plugin install`-able.

Both packagings point at the same `skills/teach/` directory; do not fork or duplicate content to serve them separately.

## Architecture: skill vs. learner state

The hardest thing to get right in this repo is the boundary between the skill (shipped, read-only at runtime) and the learner's state (persistent, user-owned).

- **Skill directory** (`skills/teach/`) — shipped content. `SKILL.md` is the thin entrypoint; `modes/*.md` are loaded on demand; `references/*.md` are authoritative policy; `assets/*.md` are seeds copied on first run.
- **Learner folder** (`$TEACH_HOME`, default `./.teach/` in the agent's cwd) — runtime state: `learner.md`, `review.md`, `syllabus.md` (optional, for multi-session topics), `sessions/YYYY-MM-DD.md`. Never inside this repo.

**The skill must never write back to its own directory.** Asset files are read-only seeds, copied once on first run into `$TEACH_HOME`. Any change to skill behavior that requires new persistent state must (a) update the asset seed and (b) leave existing learner files intact. `.teach/` is gitignored as a safety net in case someone runs the skill from a clone.

## Context discipline (why the skill is split the way it is)

`SKILL.md` is deliberately thin because everything it references costs context when loaded. Respect these rules when editing:

- **Load modes on demand, not up front.** `SKILL.md` names the modes but does not inline them. If you add a mode, follow the same pattern — one file, loaded only when entered.
- **References are high-stakes policy, not tips.** `references/refusal-rules.md`, `evaluation-rubric.md`, `review-buckets.md`, and `state-editing-protocol.md` encode behaviors the agent must not reconstruct from memory. `SKILL.md` instructs the agent to re-read them at the relevant points; preserve that pattern.
- **Don't merge modes or references into `SKILL.md`.** It would inflate every session's context even when the file isn't needed.

## Mode lifecycle (two gates + teach loop)

The teach skill's runtime shape has two upstream gates and one tutoring loop. `SKILL.md`'s decision tree is organized around this shape; preserve it when editing.

- **Calibration gate** (`modes/calibration.md`) — run once per topic. Everything downstream consumes the calibrated profile, so planning and teaching both require it first.
- **Syllabus planning gate** (`modes/prepare-syllabus.md`) — run once for multi-session topics, and again on replan. Authors `syllabus.md`; does not teach. Holds both first-draft and revise shapes in a single file.
- **Teach loop** (`modes/socratic.md`, `modes/feynman.md`, `modes/drill.md`) — the agent picks the tutoring mode per turn based on learner state. Switching mid-session is expected, not exceptional. The only hard constraint inside the loop is answer-protection on the current target (see `references/refusal-rules.md`).

If you add a mode, classify it as a gate or a tutoring mode and update `SKILL.md`'s decision tree accordingly. Do not hard-code ordering rules between tutoring modes — they interleave by judgment. The cross-cutting invariant (answer-protection persists across mode switches) lives in `references/refusal-rules.md`; preserve the pattern of `SKILL.md` pointing to it rather than restating it.

## State-editing discipline

`references/state-editing-protocol.md` exists because freeform edits to `learner.md` / `review.md` corrupt the profile over many sessions (heading drift, duplicates, format breakage, scope creep). If you change how state is edited — new fields, new buckets, new headings — update the protocol file and the asset seeds together, and check the change doesn't silently break profiles written under the old schema.

## Citations and intellectual honesty

Several popular attributions (e.g., the "Feynman technique" as a named four-step method) are reconstructions, not primary sources. If you extend the skill or add principles, cite the actual source of the idea rather than the popular handle, and distinguish philosophical spine from empirical backing (see the Vygotsky/Bloom footnote under principle 2 in the README).

## Agent Skills spec & best practices

This repo follows the Agent Skills spec (https://agentskills.io/specification) and its companion guides on best practices (https://agentskills.io/skill-creation/best-practices) and description optimization (https://agentskills.io/skill-creation/optimizing-descriptions). See also Anthropic's complete guide to building skills for Claude (https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf). Edits must keep the skill conformant.

**Spec-level invariants:**
- `SKILL.md` requires YAML frontmatter with `name` (lowercase alphanumeric + hyphens, ≤64 chars, matches parent directory) and `description` (≤1024 chars). Optional: `license`, `compatibility`, `metadata`, `allowed-tools`.
- Canonical optional directories are `scripts/`, `references/`, and `assets/`. Templates and seed files belong in `assets/`, not `templates/`.
- `SKILL.md` should stay under ~500 lines / 5,000 tokens. Push detail into `references/` or `assets/` and tell the agent *when* to load each file (progressive disclosure).

**Description (the trigger surface):**
- Imperative ("Use when…"), focused on user intent, explicit about both should-trigger and should-not-trigger cases. The current description encodes the learning-vs-task-execution distinction; preserve that shape on edits.
- When changing the description, treat it as a triggering change: re-check the ≤1024-char limit and the negative-trigger list, not just the positive examples.

**Content discipline:**
- Add what the agent wouldn't already know (project-specific conventions, gotchas, exact procedures); omit general background.
- Prefer defaults over menus, procedures over one-shot answers, and concrete templates over prose descriptions of format.
- Match prescriptiveness to fragility: be strict where order/consistency matters (state edits, gate ordering, refusal rules), looser where judgment is appropriate (mode interleaving inside the teach loop).

## Evals

`evals/` runs the `teach` skill against scripted multi-turn scenarios and grades each trial with a mix of code and LLM-judge graders. It uses the **Claude CLI** (`claude -p`) for both the agent under test and the judge — no `ANTHROPIC_API_KEY`. See `evals/README.md` for layout and how to add tasks.

**Canonical methodology reference:** Anthropic's [*Demystifying evals for AI agents*](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents). When designing or extending eval coverage, treat this as authoritative — the harness is built around its vocabulary (task / trial / grader / transcript / outcome), grader hierarchy (code > judge > human), capability vs regression split, and `pass@k` / `pass^k` consistency metrics. Specifically:

- **Favor deterministic graders.** Use code graders for anything mechanically checkable (token leaks, file layout, schema validity); reserve LLM-judges for genuinely subjective surfaces (ladder adherence, reasoning quality).
- **Give judges an `"unknown"` escape hatch** and grade one dimension at a time — separate prompts per behavior beat one holistic "is this good".
- **Capability evals start at low pass rates; regression evals stay near 100%.** Don't conflate them; keep refresh paths different.
- **Class-balance positive and negative cases.** Every "agent should refuse" task needs a "agent should comply" twin.
- **Calibrate against humans periodically.** When a code grader and judge disagree on a transcript, that disagreement is the calibration signal — usually the rule is under-specified.

**The eval surface tracks the policy surface, not the code.** Most of `skills/teach/` is markdown that names rules ("don't state the answer", "MCQ with the answer is disclosure", category-3 right-answer-wrong-reasoning). The graders are the only thing checking those rules at runtime. So:

- **When you tighten a rule in `references/`, also tighten the matching judge prompt under `evals/graders/judge/`.** If the agent could pass the judge while violating the rule, the judge is wrong. The smoke run that produced this eval found exactly this gap: `refusal-rules.md` forbade prose-form answer leaks but not MCQ-form, and the judge inherited the gap.
- **When you change `state-editing-protocol.md`, update or add code graders** under `evals/graders/code/` (heading set, item format, dedup) — those are mechanically checkable and shouldn't be left to a judge.
- **Prefer code graders for anything mechanical.** Judges are for genuinely subjective surfaces (ladder adherence, reasoning probing). Code/judge disagreement on a transcript is a real signal — usually the rule is under-specified.

Operational invariants:

- **The agent model is pinned per task** (`"model": "opus"` default). Re-runs across model versions are not "the same eval"; they are a different eval. Don't unpin to chase cost.
- **`evals/` writes nothing to `skills/`.** The harness uses scripted `$TEACH_HOME` fixtures under `evals/fixtures/teach_home/`. Adding new state shapes to a fixture does not change the asset seeds; the asset-seed contract still owns first-run behavior.
- **`reports/` is gitignored.** Transcripts contain learner content and verdicts; don't commit them.
- **Self-consistency:** before scaling a new judge prompt, re-grade a frozen transcript K times via `python evals/regrade.py <task.json> <transcript.md> --k 5`. Unstable judges are useless even if their median verdict is right.

## Workflow

- **Branches:** prefix `SebastianElvis/`, concrete and concise (<30 chars).
- **Always open a PR and squash-merge to `main`.** No direct pushes to `main`, no merge commits — squash only. Base PRs against `main` (`gh pr create --base main`).
