# Prose-tightening principles

The principles of `yanglabkit-writing`. Each principle is stated with its
*tell* — the textual symptom that signals it applies — and its *fix*. Principles
are ordered roughly by how often they fire; the first is the north star that
anchors all the others.

## 1. Don't add explanation if a sentence already carries the message

**The north star.** If the point is already made, a clarifying sentence is
redundancy, not help.

- *Tell:* the urge to append "in other words…", "this means that…", or a
  restatement "for clarity". The test spans the whole document, not just
  neighbors: a sentence that re-derives a point an earlier section already
  established fails it too.
- *Fix:* delete the would-be addition. If the original sentence genuinely fails
  to carry the message, revise *that sentence* instead of adding a second one.

## 2. Redundancy is one message wearing several costumes — find it and merge

- *Tell:* two sentences asserting the same **effect**, even with different
  subjects or vocabulary. Strip each sentence to its effect claim; if two
  effects match, they are one message.
- *Fix:* merge into a single sentence that states the effect once and the cause
  once. The merged sentence is usually stronger than either original because
  cause and effect now sit together. A special case: when one sentence merely
  defines or unpacks a noun in the other, fold it in as an appositive rather
  than keeping two sentences.

## 3. Cut connective verbs that merely restate the premise

- *Tell:* a verb phrase whose only content is the section's own thesis —
  "compounds these risks and", "further underscores", "adds to this picture" —
  bolted onto a verb that does the real work.
- *Fix:* drop the restating verb phrase; keep the specific one. If the whole
  section *is* the compounding argument, saying "compounds" adds nothing.

## 4. Condense by deleting padding, not content

- *Tell:* padded relative clauses and nominalizations — "become aware that X was
  due to Y" for "connect X to Y", "convinced by an exchange that" for
  "reassured that".
- *Fix:* trim the scaffolding while keeping every idea. A good condensation
  halves the words and loses zero content; if an idea disappeared, the cut went
  too deep.

## 5. Prefer shorter, linear sentences

- *Tell:* a sentence the reader must parse twice — nested subordinate clauses,
  stacked qualifiers or parentheticals, the subject and its verb far apart.
- *Fix:* restructure so each sentence advances one step in reading order,
  splitting only where needed — a multi-clause pile-up often splits naturally
  into cause → effect steps. The target is linearity, not brevity: a clause
  or two is fine as long as it doesn't nest, and over-splitting produces
  choppy prose that reads worse than the original. Work two knobs in order:
  first pick the right sentence *unit* (how much belongs together), then
  simplify the structure within it.

## 6. One paragraph, one theme

- *Tell:* a sentence whose theme belongs to a different paragraph — it reads
  fine alone but pulls the paragraph sideways.
- *Fix:* relocate it to the paragraph that owns its theme. Done right, the move
  purifies *both* paragraphs at once. When a theme recurs in several places,
  consolidate it into one paragraph — and place that paragraph where the theme
  does its work (e.g. a constraint goes *after* the things it constrains).

## 7. Arrange paragraphs by linear dependency

- *Tell:* a paragraph that leans on something only explained later, or one that
  could be moved elsewhere without anything breaking — either way the sequence
  isn't carrying the argument. At section scale: content organized by a surface
  taxonomy (by actor, by category) instead of by the argument's logic — a
  taxonomy is not an argument.
- *Fix:* order paragraphs so each builds only on what earlier ones established —
  conditions before consequences, problem before remedy. Nothing may depend on
  material that arrives later. Fold taxonomy items in at their causal position
  instead of listing them flat.

## 8. Lead each paragraph with its claim

- *Tell:* skimming the first sentence of each paragraph doesn't reconstruct the
  argument; points surface mid-paragraph or at the end.
- *Fix:* state the paragraph's point in its opening sentence and spend the rest
  supporting it. When principle 8 holds, checking principle 7 is cheap: the
  first sentences read top to bottom should form the argument's chain. A
  build-up-then-payoff paragraph stays legal as a deliberate, marked choice —
  not a habit.

## 9. Frame a sentence by its local function, not its grandest possible framing

- *Tell:* a sentence that re-sounds the piece's thesis when its job where it
  sits is smaller — qualifying, bridging, scoping.
- *Fix:* match the frame to the work the sentence does in place. A constraint
  paragraph opens as a constraint, not as another statement of the spine; not
  every sentence gets the biggest framing it could carry.

## 10. Prefer a concrete pointer over an abstract label

- *Tell:* an abstract label ("this asymmetry", "the paradox") that needs an
  inline definition to be understood — especially when that definition would
  restate material from elsewhere in the document.
- *Fix:* drop the label and state the concrete thing itself, adding new content
  rather than re-deriving old. Beware that "make it explicit" can *create*
  restatement (principle 1); a label that requires a gloss is usually a signal
  to just name the thing.

## 11. Prefer removals; an added word must earn its place

- *Tell:* any edit whose diff adds words.
- *Fix:* default to deletion and merging. Permit an addition only when it does
  structural, load-bearing work rather than explaining. In a healthy tightening
  pass, additions are rare enough to count on one hand.

---

# Delivery method

How the diagnosis is presented matters as much as what it says.

- **Read the whole passage first.** Local edits made without the full context
  break paragraph-level structure (principles 6–8 are invisible line-by-line).
- **Affirm before critique.** Open with what already lands well, as its own
  section, so the writer knows what to preserve. Only then list issues.
- **Diagnose by line, not in the abstract.** Name the exact sentences and the
  exact flaw ("these two sentences both assert X"), never a vague "this could
  be tighter".
- **Drop-in replacement + rationale, per change.** Every diagnosis comes with
  concrete replacement text and a one-line reason tied to the principle it
  serves — a verdict without a fix is half an edit.
- **Recommended option and aggressive option, kept distinct.** Where deeper
  cuts are possible, present the safe recommendation and, separately, what to
  cut if space gets tight — the writer owns the trade-off.
- **Tie every fix to the writer's stated principle.** The advice inherits the
  writer's own standard; it never imports an external house style.
- **Flag out-of-scope issues; don't fix them.** Cross-section redundancy or
  problems beyond the passage get noted for a later dedicated pass.
- **End on a "Net:" bottom line.** One recommended next action — not an
  undifferentiated menu of possibilities.
- **Respect workflow constraints.** Before offering to apply edits, honor the
  project's rules (pull before editing live-synced files, branch conventions,
  approval gates) — including staging preferences: if the writer wants edits
  applied but uncommitted so they can review one accumulated diff, never
  auto-commit per edit.
