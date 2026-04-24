# hammer

Personal agent-skills for learning. The agent plays tutor, you play learner — it refuses to just hand you answers, keeps a persistent profile of what you know and what you've stumbled on, and spaces review of past material across sessions.

Currently ships one skill: **`teach`**. The repo is named for Richard Hamming, whose *Learning to Learn* is the spine of the approach.

## Install

The repo is in the [vercel-labs/skills](https://github.com/vercel-labs/skills) format and also carries a Claude Code plugin manifest, so you can install it via whichever path you prefer.

### Via `npx skills` (any supported agent)

```bash
# install the teach skill globally (available to all projects)
npx skills add SebastianElvis/hammer -g

# or scoped to the current project
npx skills add SebastianElvis/hammer

# target a specific agent (claude-code, codex, cursor, opencode, …)
npx skills add SebastianElvis/hammer -g -a claude-code
```

Supported agents are listed in the [vercel-labs/skills README](https://github.com/vercel-labs/skills#supported-agents). The CLI auto-detects what you have installed.

### As a Claude Code plugin

This repo includes a `.claude-plugin/marketplace.json`, so Claude Code can install it as a plugin:

```bash
/plugin install https://github.com/SebastianElvis/hammer
```

### Manually

Clone the repo and symlink `skills/teach/` into your agent's skills directory (e.g., `~/.claude/skills/teach` for Claude Code).

## Usage

Once installed, just talk to the agent the way you already do. The skill triggers automatically when you ask to *learn* something rather than *get something done*:

- "teach me SQL window functions"
- "let's learn Rust ownership — don't just explain, walk me through it"
- "quiz me on what we covered last time"
- "I want to understand how a Bloom filter works"

It will *not* fire on debugging help, one-shot factual lookups, or task execution — those are not tutoring. See [`skills/teach/SKILL.md`](skills/teach/SKILL.md) for the full trigger definition.

## Where your progress lives

The skill stores your learner profile outside the skill directory, so reinstalling or updating the skill never touches your data.

- **Default location**: `./.teach/` — the `.teach/` folder in the agent's current working directory. Learner state is scoped per project; `.teach/` is gitignored so it does not get committed.
- **Override**: set `TEACH_HOME` to any path — useful for a cross-project profile (`TEACH_HOME=~/.teach`) or per-topic folders (`TEACH_HOME=~/.teach/spanish`).

The folder contains:

```
./.teach/
├── learner.md        # your profile — known solid, shaky, misconceptions, currently studying
├── review.md         # spaced-review queue (new / learning / mastered buckets)
└── sessions/         # one markdown transcript per day
```

Everything is plain markdown. You can read it, edit it, back it up, sync it via git/Dropbox — it's just text.

## How a session flows

1. **Trigger.** Agent matches your intent against [`SKILL.md`](skills/teach/SKILL.md). If it looks like *learning* rather than *getting something done*, the skill activates.
2. **Bootstrap.** Resolve `$TEACH_HOME`. On first use, seed it from [`templates/`](skills/teach/templates/). Never write back to the skill directory.
3. **Read the learner.** Load `learner.md` and `review.md`, decide what kind of session this should be.
4. **Pick a mode:**
   - No profile, or a new topic → [`modes/diagnostic.md`](skills/teach/modes/diagnostic.md): calibrate level *and* motivation.
   - Review queue has items → [`modes/drill.md`](skills/teach/modes/drill.md): short retrieval practice.
   - New material → [`modes/socratic.md`](skills/teach/modes/socratic.md): default, question-driven. Answer-protection enforced by [`references/refusal-rules.md`](skills/teach/references/refusal-rules.md).
   - Consolidating familiar material → [`modes/feynman.md`](skills/teach/modes/feynman.md): you explain it back, the tutor probes for gaps.
5. **Session end.** State files updated per [`references/state-editing-protocol.md`](skills/teach/references/state-editing-protocol.md) — strict rules that prevent profile corruption over time.

## Repo layout

```
hammer/
├── .claude-plugin/
│   └── marketplace.json        # Claude Code plugin manifest
└── skills/
    └── teach/
        ├── SKILL.md            # trigger + orchestration (deliberately thin)
        ├── modes/              # one file per teaching mode, loaded on demand
        ├── references/         # policy: refusal, evaluation, review buckets, state protocol
        └── templates/          # seeds copied to ./.teach/ on first run
```

---

## The principles behind the skill

### 1. Hamming's lens — *learning to learn* is the master skill, and taste decides what is worth learning

Hamming's contribution is not a technique but an orientation. *Learning to learn* is the skill that makes every other skill compound: if you cannot get better at acquiring new understanding, you plateau. And the specific *what* you choose to learn matters as much as the *how* — a tutor who only answers "what are you studying?" is a less useful tutor than one who, gently and occasionally, also asks "and why this, and why now?"

This is why the skill has a diagnostic mode at the start of every new topic (calibration of motivation, not just level), and why session-end reflections ask what the learner wants to be able to do next time.

**Sources**:
- Hamming, R. W. (1997). *The Art of Doing Science and Engineering: Learning to Learn.* Gordon and Breach. Republished by Stripe Press (2020) with a foreword by Bret Victor. The subtitle is this skill's founding premise; Chapter 1 ("Orientation") is the clearest statement of why meta-learning is the master skill.
- Hamming, R. W. (1986). *You and Your Research* (Bell Communications Research Colloquium Seminar, March 7, 1986). In: Kaiser, J. F. (Ed.) (1986). *Transactions of the Bell Communications Research Colloquium Seminar.* The "important problems" heuristic: "What are the important problems in my field? What am I working on? Why aren't they the same thing?" — the single most load-bearing quote in the skill's design.

**Where applied**: [`modes/diagnostic.md`](skills/teach/modes/diagnostic.md), session-end reflection in [`SKILL.md`](skills/teach/SKILL.md).

### 2. Productive struggle — the learner must produce the answer

The act of producing the answer is what creates understanding. Receiving the answer produces the feeling of learning without the substance. A tutor who removes the friction removes the learning.

This principle covers the entire Socratic tradition (questions that force the learner to produce their own answer) as well as twentieth-century cognitive science showing that the *effort* of retrieval and reasoning is what produces durable memory, even when it feels less productive than being told.

**Sources**:
- Plato. *Meno* (c. 380 BCE). Translated by G.M.A. Grube (1976), Hackett Publishing. 82b–85b — Socrates teaches a slave boy geometry by asking only questions.
- Moore, R. L. (the "Moore method"). Documented in: Parker, J. (2005). *R. L. Moore: Mathematician and Teacher.* MAA. Moore refused to let students read the textbook — they had to prove every theorem themselves.
- Pólya, G. (1945). *How to Solve It.* Princeton University Press. The four-stage framework (understand → plan → execute → look back) gives the principle a practical shape.
- Bjork, R. A., & Bjork, E. L. (2011). *Making things hard on oneself, but in a desirable way.* In M. A. Gernsbacher et al. (Eds.), *Psychology and the real world.* Worth Publishers. "Desirable difficulties": effort, spacing, interleaving, and generation improve long-term retention by making short-term performance harder.
- Roediger, H. L., & Karpicke, J. D. (2006). "Test-enhanced learning." *Psychological Science*, 17(3), 249–255. The testing effect — retrieval outperforms rereading.

**Where applied**: [`modes/socratic.md`](skills/teach/modes/socratic.md), [`references/refusal-rules.md`](skills/teach/references/refusal-rules.md).

*Calibration mechanics — Vygotsky's "zone of proximal development" and Bloom's two-sigma finding — back the diagnostic mode empirically; they're not the philosophical spine, but they're what makes individualized Socratic teaching as effective as the data shows.*

### 3. Understanding is tested by explanation — and the learner is the easiest person to fool

A learner who can recite a definition but cannot recognize the concept when shown it does not understand it. A correct answer produced by bad reasoning is worse than a wrong one, because it hides the gap. The tutor's job is not just to ask — it is to listen for self-deception and surface it, gently, without letting it pass.

This is why the skill treats "right answer, wrong reasoning" as a separate evaluation category rather than collapsing it into "correct."

**Sources**:
- Feynman, R. P., Leighton, R. B., & Sands, M. (1963). *The Feynman Lectures on Physics*, Vol. 1, Preface. Addison-Wesley. The preface frames the lectures as Feynman explaining physics to *himself* — the test of understanding is the ability to teach.
- Feynman, R. P. (1985). *"Surely You're Joking, Mr. Feynman!"*. Norton. See "O Americano, Outra Vez!" — case study of students who could recite the definition of polarized light but could not recognize it physically.
- Feynman, R. P. (1974). *Cargo Cult Science* (Caltech commencement address, reprinted in *Surely You're Joking* and elsewhere). "The first principle is that you must not fool yourself — and you are the easiest person to fool."

**Where applied**: [`modes/feynman.md`](skills/teach/modes/feynman.md), [`references/evaluation-rubric.md`](skills/teach/references/evaluation-rubric.md).

### 4. Retention requires retrieval over time

Understanding at the end of a session is not the same as knowing the thing a week later. Without retrieval across a gap, knowledge decays on a predictable curve. The cure is spaced retrieval practice.

**Sources**:
- Ebbinghaus, H. (1885). *Über das Gedächtnis: Untersuchungen zur experimentellen Psychologie* (*Memory: A Contribution to Experimental Psychology*). The original forgetting curve.
- Karpicke, J. D., & Roediger, H. L. (2008). "The critical importance of retrieval for learning." *Science*, 319(5865), 966–968. *Retrieval*, not repeated study, is what produces long-term retention. Learners who study-study-study-study perform worse one week out than learners who study-test-test-test — even though the second group feels less confident at the time.
- Wozniak, P. (1990). *Optimization of learning* (Master's thesis, Poznan University of Technology). The SuperMemo SM-2 algorithm. This skill uses a simplified three-bucket variant rather than date-based intervals, because date math is fragile in an LLM-driven substrate.

**Where applied**: [`modes/drill.md`](skills/teach/modes/drill.md), [`references/review-buckets.md`](skills/teach/references/review-buckets.md).

## License

[MIT](LICENSE).
