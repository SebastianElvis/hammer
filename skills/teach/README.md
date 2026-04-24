# teach

An agent-skill that turns the agent into a tutor and the user into a learner. It is not a Q&A system — it is built on the claim, well-supported across the sources below, that understanding is produced by productive struggle, and that a helpful-seeming answer given too early is a theft disguised as a gift.

This README documents the principles the skill is built on and where they are cited in the skill's files. The separation exists so the ideas can be traced back to their sources, and so improvements to the skill can be grounded in the literature rather than intuition.

## Principles

### 1. Productive struggle is the mechanism of learning

The friction of trying, failing, and trying again is not a bug in the learning process — it is the process. A tutor who removes the friction removes the learning.

**Sources**:
- Bjork, R. A., & Bjork, E. L. (2011). *Making things hard on oneself, but in a desirable way: Creating desirable difficulties to enhance learning.* In M. A. Gernsbacher et al. (Eds.), *Psychology and the real world*. Worth Publishers. The "desirable difficulties" framework — retrieval effort, spacing, interleaving, and generation all *improve* long-term retention by making short-term performance harder.
- Roediger, H. L., & Karpicke, J. D. (2006). "Test-enhanced learning: Taking memory tests improves long-term retention." *Psychological Science*, 17(3), 249–255. The "testing effect" — retrieval practice outperforms rereading, even when rereading feels more productive in the moment.

**Where cited in the skill**: `SKILL.md` ("friction is where the learning happens"), `modes/socratic.md` (let silence sit, do not rescue), `references/refusal-rules.md` (the ladder exists to preserve struggle).

### 2. The Socratic method — answers that the learner produces are worth more than answers they receive

The teacher asks questions whose answers force the learner to examine their own understanding. The teacher refuses to supply the answer. Classical origin: Plato's *Meno*, where Socrates teaches a slave boy the Pythagorean theorem by asking only questions.

**Sources**:
- Plato. *Meno* (c. 380 BCE). Translated by G.M.A. Grube (1976), Hackett Publishing. See especially 82b–85b — the geometric demonstration that underlies all Socratic teaching.
- Moore, R. L. The "Moore method" in mathematics, University of Texas (c. 1920s–1960s). Documented in: Parker, J. (2005). *R. L. Moore: Mathematician and Teacher.* MAA. Moore famously refused to let students read textbooks — they had to prove every theorem themselves. Extreme but instructive.

**Where cited in the skill**: `modes/socratic.md` (the entire mode), `references/refusal-rules.md` (the core rule).

### 3. The Feynman technique — if you cannot explain it simply, you do not understand it

The test of understanding is the ability to teach the thing. Gaps in an explanation are gaps in the understanding. The technique, as popularly reconstructed from Feynman's habits: pick a concept, explain it in plain language as if to a novice, notice where the explanation breaks down, return to the source material on those specific points, simplify further.

**Sources**:
- Feynman, R. P., Leighton, R. B., & Sands, M. (1963). *The Feynman Lectures on Physics*, Vol. 1, Preface. Addison-Wesley. The preface explicitly frames the lectures as an attempt to explain physics to himself — "the best method of teaching ... is to prepare lectures that one would have liked to have heard as an undergraduate."
- Feynman, R. P. (1985). *"Surely You're Joking, Mr. Feynman!"*. Norton. See "O Americano, Outra Vez!" (Brazil chapter) — extended critique of memorization without understanding: students who could recite definitions but could not recognize the concept when shown it physically.
- Feynman, R. P. (1974). *Cargo Cult Science* (Caltech commencement address). "The first principle is that you must not fool yourself — and you are the easiest person to fool." This is the foundation of the Feynman mode's probing logic: a fluent explanation is not the same as understanding, and the tutor's job is to detect self-deception.

**Where cited in the skill**: `modes/feynman.md` (the mode's whole premise and method), `references/evaluation-rubric.md` (the "right answer, wrong reasoning" category is a direct application of "you must not fool yourself").

### 4. Pólya's heuristic — the stages of working a problem

Before leaping to a solution, the learner should understand the problem, devise a plan, execute it, and then look back and reflect. Skipping any of these stages produces brittle learning. This is the structural backbone of how Socratic mode escalates: first ensure the learner understands *what is being asked* before probing their solution.

**Sources**:
- Pólya, G. (1945). *How to Solve It: A New Aspect of Mathematical Method.* Princeton University Press. The four-stage framework (understand → plan → execute → look back) is in Part I. The "looking back" stage is the most neglected in practice and the most valuable.

**Where cited in the skill**: `modes/socratic.md` (question ladder structure), `modes/feynman.md` (the "look back" stage corresponds to Feynman-style explaining-back).

### 5. Hamming's taste — teach what is worth learning

Hamming's framing pushes past *how* to learn and asks *what* is worth learning. A tutor who only answers "what are you studying?" is less useful than one who occasionally asks "why this, and why now?" — gently, without dismissing the learner's interests.

**Sources**:
- Hamming, R. W. (1986). *You and Your Research* (Bell Communications Research Colloquium Seminar, March 7, 1986). Widely transcribed; the canonical text is in: Kaiser, J. F. (Ed.) (1986). *Transactions of the Bell Communications Research Colloquium Seminar.* The "important problems" heuristic — ask yourself *what are the important problems in my field*, *what am I working on*, and *why aren't they the same thing?*
- Hamming, R. W. (1997). *The Art of Doing Science and Engineering: Learning to Learn.* Gordon and Breach. Republished by Stripe Press (2020) with a foreword by Bret Victor. See especially Chapter 1 ("Orientation") on why learning-to-learn is the master skill, and the closing chapters on taste and courage.

**Where cited in the skill**: `modes/diagnostic.md` (the diagnostic asks *why* the learner cares about this topic, not just what they know), and the `README.md` (this document) names the skill's project folder `hammer` in acknowledgment of Hamming.

### 6. Calibration before instruction

Teaching at the wrong level — too easy, too hard — produces boredom or despair. Before teaching anything, the tutor calibrates. This is why diagnostic is a distinct mode.

**Sources**:
- Vygotsky, L. S. (1978). *Mind in Society: The Development of Higher Psychological Processes.* Harvard University Press. The "zone of proximal development" — the gap between what a learner can do alone and what they can do with guidance — is where teaching is most effective. Below it is boring; above it is hopeless.
- Bloom, B. S. (1984). "The 2 Sigma Problem: The Search for Methods of Group Instruction as Effective as One-to-One Tutoring." *Educational Researcher*, 13(6), 4–16. One-to-one tutoring with mastery feedback produces a two-standard-deviation improvement over conventional instruction — largely because tutoring calibrates to the individual and conventional instruction cannot.

**Where cited in the skill**: `modes/diagnostic.md` (the entire mode and its placement at the front of the session loop), `modes/socratic.md` ("pick a starting question at or just below the learner's current level").

### 7. Spaced retrieval for retention

Learning is not finished when the concept is understood; it is finished when it can be retrieved after a gap. Retrieval with spacing produces durable memory; reading alone does not.

**Sources**:
- Ebbinghaus, H. (1885). *Über das Gedächtnis: Untersuchungen zur experimentellen Psychologie* (*Memory: A Contribution to Experimental Psychology*). The original forgetting curve.
- Karpicke, J. D., & Roediger, H. L. (2008). "The critical importance of retrieval for learning." *Science*, 319(5865), 966–968. Shows that retrieval practice, not repeated study, produces long-term retention.
- SuperMemo (SM-2) algorithm: Wozniak, P. (1990). "Optimization of learning." Master's thesis, University of Technology in Poznan. The canonical adaptive-interval algorithm; this skill uses a simplified bucket-based variant for robustness in a markdown-only context.

**Where cited in the skill**: `modes/drill.md` (retrieval practice is the whole purpose), `references/review-buckets.md` (bucket logic — a simplified SM-2).

## How the skill is organized

- [`SKILL.md`](SKILL.md) — the trigger description and orchestration logic. Deliberately thin; policy lives in the references below.
- [`modes/diagnostic.md`](modes/diagnostic.md) — Vygotsky + Bloom: calibrate before teaching.
- [`modes/socratic.md`](modes/socratic.md) — Plato + Moore + Pólya: questions that force the learner to produce the answer.
- [`modes/feynman.md`](modes/feynman.md) — Feynman: explain it back, gaps surface, do not fool yourself.
- [`modes/drill.md`](modes/drill.md) — Ebbinghaus + Roediger: retrieval practice for retention.
- [`references/refusal-rules.md`](references/refusal-rules.md) — Bjork's desirable difficulties, operationalized as a mechanical ladder that prevents the tutor from capitulating.
- [`references/evaluation-rubric.md`](references/evaluation-rubric.md) — Feynman's *cargo cult science* principle: a correct answer produced by bad reasoning is worse than a wrong one.
- [`references/review-buckets.md`](references/review-buckets.md) — simplified SM-2.
- [`references/state-editing-protocol.md`](references/state-editing-protocol.md) — engineering, not pedagogy: protects the learner's profile from silent corruption.

## A note on intellectual honesty

Several of these citations are for works whose ideas are widely repeated but not always accurately attributed. The "Feynman technique" as a named four-step method is a popular reconstruction, not something Feynman wrote down in those words — the *spirit* is in the Lectures preface and the Brazil chapter, but the explicit procedure is not. Similarly, "you must not fool yourself" is from Cargo Cult Science, not from a teaching manual.

Where this skill cites a source, it cites the actual source of the idea, not the popular handle. If you extend this skill, please maintain that discipline.
