# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

`hammer` is a skills repo, not an application. There is nothing to build, lint, or test — it ships plain markdown files that agents load on demand. Currently contains one skill: `teach` (a tutoring skill named after Richard Hamming).

The repo is dual-packaged:
- **`vercel-labs/skills` format** — installable via `npx skills add SebastianElvis/hammer`.
- **Claude Code plugin** — `.claude-plugin/marketplace.json` makes it `/plugin install`-able.

Both packagings point at the same `skills/teach/` directory; do not fork or duplicate content to serve them separately.

## Architecture: skill vs. learner state

The hardest thing to get right in this repo is the boundary between the skill (shipped, read-only at runtime) and the learner's state (persistent, user-owned).

- **Skill directory** (`skills/teach/`) — shipped content. `SKILL.md` is the thin entrypoint; `modes/*.md` are loaded on demand; `references/*.md` are authoritative policy; `templates/*.md` are seeds copied on first run.
- **Learner folder** (`$TEACH_HOME`, default `./.teach/` in the agent's cwd) — runtime state: `learner.md`, `review.md`, `syllabus.md` (optional, for multi-session topics), `sessions/YYYY-MM-DD.md`. Never inside this repo.

**The skill must never write back to its own directory.** Templates are read-only seeds, copied once on first run into `$TEACH_HOME`. Any change to skill behavior that requires new persistent state must (a) update the template and (b) leave existing learner files intact. `.teach/` is gitignored as a safety net in case someone runs the skill from a clone.

## Context discipline (why the skill is split the way it is)

`SKILL.md` is deliberately thin because everything it references costs context when loaded. Respect these rules when editing:

- **Load modes on demand, not up front.** `SKILL.md` names the modes but does not inline them. If you add a mode, follow the same pattern — one file, loaded only when entered.
- **References are high-stakes policy, not tips.** `references/refusal-rules.md`, `evaluation-rubric.md`, `review-buckets.md`, and `state-editing-protocol.md` encode behaviors the agent must not reconstruct from memory. `SKILL.md` instructs the agent to re-read them at the relevant points; preserve that pattern.
- **Don't merge modes or references into `SKILL.md`.** It would inflate every session's context even when the file isn't needed.

## State-editing discipline

`references/state-editing-protocol.md` exists because freeform edits to `learner.md` / `review.md` corrupt the profile over many sessions (heading drift, duplicates, format breakage, scope creep). If you change how state is edited — new fields, new buckets, new headings — update the protocol file and the templates together, and check the change doesn't silently break profiles written under the old schema.

## Citations and intellectual honesty

Several popular attributions (e.g., the "Feynman technique" as a named four-step method) are reconstructions, not primary sources. If you extend the skill or add principles, cite the actual source of the idea rather than the popular handle, and distinguish philosophical spine from empirical backing (see the Vygotsky/Bloom footnote under principle 2 in the README).

## Workflow

- **Branches:** prefix `SebastianElvis/`, concrete and concise (<30 chars).
- **Always open a PR and squash-merge to `main`.** No direct pushes to `main`, no merge commits — squash only. Base PRs against `main` (`gh pr create --base main`).
