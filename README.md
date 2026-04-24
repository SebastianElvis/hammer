# hammer

Personal agent-skills repo. Currently contains one skill: **teach**.

The repo is named for Richard Hamming. His *Art of Doing Science and Engineering: Learning to Learn* and the "You and Your Research" lecture are the spine of this project — not one influence among many, but the one the rest orbit around. The other sources below sharpen specific mechanics; Hamming sets the orientation.

## The `teach` skill

An agent-skill (vercel-labs/skills format) that turns the agent into a tutor and the user into a learner. It is not a Q&A system — it is built on the claim, grounded in the work cited below, that understanding is produced by productive struggle, and that a helpful-seeming answer given too early is a theft disguised as a gift.

Source: [`skills/teach/`](skills/teach/)

Install: `npx skills add SebastianElvis/hammer --skill teach -g`

## The four principles

Earlier drafts had seven. This is tighter, and Hamming is first on purpose — his framing is the one the rest of the skill is answering to.

### 1. Hamming's lens — *learning to learn* is the master skill, and taste decides what is worth learning

Hamming's contribution is not a technique but an orientation. *Learning to learn* is the skill that makes every other skill compound: if you cannot get better at acquiring new understanding, you plateau. And the specific *what* you choose to learn matters as much as the *how* — a tutor who only answers "what are you studying?" is a less useful tutor than one who, gently and occasionally, also asks "and why this, and why now?"

This principle is why the skill has a diagnostic mode at the start of every new topic (not just a calibration of level, but of motivation), and why the session-end reflection asks the learner what they want to be able to do next time. The skill is trying, in small ways, to cultivate the learner's own taste and meta-learning — not just to transfer facts.

**Sources**:
- Hamming, R. W. (1997). *The Art of Doing Science and Engineering: Learning to Learn.* Gordon and Breach. Republished by Stripe Press (2020) with a foreword by Bret Victor. The subtitle *Learning to Learn* is this skill's founding premise; Chapter 1 ("Orientation") is the clearest statement of why meta-learning is the master skill.
- Hamming, R. W. (1986). *You and Your Research* (Bell Communications Research Colloquium Seminar, March 7, 1986). In: Kaiser, J. F. (Ed.) (1986). *Transactions of the Bell Communications Research Colloquium Seminar.* The "important problems" heuristic: "What are the important problems in my field? What am I working on? Why aren't they the same thing?" This is the single most load-bearing quote in the skill's design.

**Where applied**: [`modes/diagnostic.md`](skills/teach/modes/diagnostic.md) (Hamming's "why this topic?" is step 2 of diagnostic), the session-end reflection in [`SKILL.md`](skills/teach/SKILL.md), and the cultivation-of-taste framing throughout the skill.

### 2. Productive struggle — the learner must produce the answer

The act of producing the answer is what creates understanding. Receiving the answer produces the feeling of learning without the substance. A tutor who removes the friction removes the learning.

This principle covers the entire Socratic tradition (questions that force the learner to produce their own answer) as well as twentieth-century cognitive science showing that the *effort* of retrieval and reasoning is what produces durable memory, even when it feels less productive than being told.

**Sources**:
- Plato. *Meno* (c. 380 BCE). Translated by G.M.A. Grube (1976), Hackett Publishing. See 82b–85b — Socrates teaches a slave boy geometry by asking only questions. The foundational text for the claim that questioning outperforms telling.
- Moore, R. L. (the "Moore method"). Documented in: Parker, J. (2005). *R. L. Moore: Mathematician and Teacher.* MAA. Moore refused to let his students read the textbook — they had to prove every theorem themselves. Extreme, but a clean statement of the principle.
- Pólya, G. (1945). *How to Solve It: A New Aspect of Mathematical Method.* Princeton University Press. The four-stage framework (understand → plan → execute → look back) gives the principle a practical shape: the tutor's questions walk the learner through these stages rather than skip them.
- Bjork, R. A., & Bjork, E. L. (2011). *Making things hard on oneself, but in a desirable way: Creating desirable difficulties to enhance learning.* In M. A. Gernsbacher et al. (Eds.), *Psychology and the real world.* Worth Publishers. "Desirable difficulties": effort, spacing, interleaving, and generation *improve* long-term retention by making short-term performance harder.
- Roediger, H. L., & Karpicke, J. D. (2006). "Test-enhanced learning: Taking memory tests improves long-term retention." *Psychological Science*, 17(3), 249–255. The testing effect — retrieval outperforms rereading, even when rereading feels more productive in the moment.

**Where applied**: [`modes/socratic.md`](skills/teach/modes/socratic.md) (the whole mode), [`references/refusal-rules.md`](skills/teach/references/refusal-rules.md) (the escalation ladder exists to preserve struggle rather than skip past it), [`modes/diagnostic.md`](skills/teach/modes/diagnostic.md) (calibration mechanics via Vygotsky's ZPD and Bloom's 2-sigma — see below).

*(Calibration mechanics — Vygotsky's "zone of proximal development" and Bloom's two-sigma finding on tutoring effectiveness — provide the empirical backing for why individualized Socratic teaching is so much more effective than group instruction. Citations on request; they are the empirical basis for the diagnostic mode but not the philosophical spine.)*

### 3. Understanding is tested by explanation — and the learner is the easiest person to fool

A learner who can recite a definition but cannot recognize the concept when shown it does not understand it. A correct answer produced by bad reasoning is worse than a wrong one, because it hides the gap. The tutor's job is not just to ask — it is to listen for self-deception and surface it, gently, without letting it pass.

This is the Feynman cluster, and it is the reason the skill treats "right answer, wrong reasoning" as a separate evaluation category instead of collapsing it into "correct."

**Sources**:
- Feynman, R. P., Leighton, R. B., & Sands, M. (1963). *The Feynman Lectures on Physics*, Vol. 1, Preface. Addison-Wesley. The preface frames the lectures as Feynman explaining physics to *himself* — the test of understanding is the ability to teach.
- Feynman, R. P. (1985). *"Surely You're Joking, Mr. Feynman!"*. Norton. See "O Americano, Outra Vez!" (the Brazil chapter) — case study of students who could recite the definition of polarized light but could not recognize it physically. The foundational anecdote for the fluency-without-recognition failure mode.
- Feynman, R. P. (1974). *Cargo Cult Science* (Caltech commencement address, reprinted in *Surely You're Joking* and elsewhere). "The first principle is that you must not fool yourself — and you are the easiest person to fool."

**Where applied**: [`modes/feynman.md`](skills/teach/modes/feynman.md) (the whole mode — the learner explains, the tutor probes for gaps), [`references/evaluation-rubric.md`](skills/teach/references/evaluation-rubric.md) (the "right answer, wrong reasoning" category is the operational form of this principle).

### 4. Retention requires retrieval over time

Understanding at the end of a session is not the same as knowing the thing a week later. Without retrieval across a gap, knowledge decays on a predictable curve. The cure is spaced retrieval practice — the learner pulls the thing from memory, with effort, after a delay, repeatedly.

**Sources**:
- Ebbinghaus, H. (1885). *Über das Gedächtnis: Untersuchungen zur experimentellen Psychologie* (*Memory: A Contribution to Experimental Psychology*). The original forgetting curve — the first empirical demonstration that memory decays on a roughly logarithmic schedule without rehearsal.
- Karpicke, J. D., & Roediger, H. L. (2008). "The critical importance of retrieval for learning." *Science*, 319(5865), 966–968. Shows that *retrieval*, not repeated study, is what produces long-term retention. Learners who study-study-study-study perform worse one week out than learners who study-test-test-test — even though the second group feels less confident at the time.
- Wozniak, P. (1990). *Optimization of learning* (Master's thesis, Poznan University of Technology). The SuperMemo SM-2 algorithm — the canonical adaptive-interval scheduler. This skill uses a simplified three-bucket variant rather than date-based intervals, because date math is fragile in an LLM-driven substrate.

**Where applied**: [`modes/drill.md`](skills/teach/modes/drill.md) (retrieval practice is the mode's entire purpose), [`references/review-buckets.md`](skills/teach/references/review-buckets.md) (bucket logic, derived from SM-2 but simplified for a markdown-only state file).

## How a session flows

Reading the skill top-down misses the shape. Here is the actual path through the files when a session runs:

1. **Trigger.** The agent matches the user's intent against the `description` in [`SKILL.md`](skills/teach/SKILL.md). If it looks like *learning*, not *getting something done*, the skill activates.
2. **Bootstrap.** The agent resolves `$TEACH_HOME` (default `~/.teach/`) and, on first use, seeds it from [`templates/`](skills/teach/templates/). Nothing is ever written back to the skill directory — personal progress lives outside the skill so it survives reinstalls.
3. **Read the learner.** The agent reads `learner.md` (profile) and `review.md` (review queue) from `$TEACH_HOME`. Then it decides what kind of session this should be.
4. **Pick a mode.** Four modes, chosen by what the state says:
   - No profile, or a new topic → [`modes/diagnostic.md`](skills/teach/modes/diagnostic.md): calibrate level *and* motivation (principle 1), sparingly ask a few probing questions (principle 2 warm-up).
   - Review queue has items → [`modes/drill.md`](skills/teach/modes/drill.md): short retrieval practice on items the learner has already seen (principle 4).
   - New material → [`modes/socratic.md`](skills/teach/modes/socratic.md): the default, question-driven teaching (principle 2). Answer-protection enforced by [`references/refusal-rules.md`](skills/teach/references/refusal-rules.md).
   - Consolidating a topic the learner has seen → [`modes/feynman.md`](skills/teach/modes/feynman.md): the learner explains back, the tutor probes for gaps (principle 3). Scoring uses [`references/evaluation-rubric.md`](skills/teach/references/evaluation-rubric.md).
5. **Session end.** State files are updated according to [`references/state-editing-protocol.md`](skills/teach/references/state-editing-protocol.md) — strict rules that prevent silent corruption of the profile over time. The session log is closed with a short reflection.

## A note on intellectual honesty

A few of these citations are for ideas that are widely repeated but not always accurately attributed. The "Feynman technique" as a named four-step method is a popular reconstruction, not something Feynman wrote down in those words — the *spirit* is in the Lectures preface and the Brazil chapter, but the explicit procedure is not. "You must not fool yourself" is from *Cargo Cult Science*, not from a teaching manual. The Moore method is documented by Parker and others, not by Moore himself.

Where this skill cites a source, it cites the actual source of the idea, not the popular handle. If you extend this skill, please maintain that discipline.
