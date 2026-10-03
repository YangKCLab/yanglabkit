# Argument and structure principles

The two levels of `yanglabkit-writing` that sit above the prose principles.
`prose-principles.md` asks whether each sentence and paragraph is tight; this
file asks whether the text argues the right thing, in the right order, at the
right length. Each principle is stated with its *tell*, its *fix*, and — where
the rule has a legitimate exception — its *exception*.

The levels run in a fixed order: **argument → structure → prose.** A problem at
a higher level changes which sentences survive, so wording edits proposed
before it is settled are wasted. Do not propose prose edits inside a passage
that an open argument or structure finding will move, cut, or rewrite.

Several ideas here — the fixed order of levels, the intake, the preservation
check, the right of a good text to stay unchanged — are adapted from
[cida](https://github.com/mizzlelover/cida) (MIT).

## Intake — three facts before any diagnosis

State these in one line each before diagnosing. Take them from the text and
its context; ask the writer only when the text cannot tell you.

- **Claim.** What the piece asserts, in one sentence.
- **Reader.** Who reads it, what they already know, and what they are
  sceptical of.
- **Purpose.** What the reader should decide, believe, or do after reading —
  fund it, accept it, adopt the method, grant the request.

Every finding below is judged against these three facts, not against a general
idea of good writing.

When the text was adapted from a version written for a different reader — a
paper recast as a proposal, a proposal moved to another venue — say so in the
intake. Its emphasis, vocabulary, and choice of evidence often still serve the
first reader, and that one cause explains many of the findings below.

---

# Argument level

## A1. The piece states a claim the reader could dispute

- *Tell:* the intake claim cannot be written in one sentence, or it can only
  be written as a topic ("this section discusses X") rather than an assertion
  ("X fails because Y"). A weaker form: the claim can be written, but only by
  borrowing from another part — the abstract states it and the section it
  summarizes never does. Report that under A2.
- *Fix:* none available to an editor. Stop, say that the text needs a claim
  before it needs polish, and offer the candidate claims the material could
  support. Do not tighten sentences around a missing claim.
- *Exception:* purely descriptive passages — a schedule, a method recipe, a
  biography — carry facts, not a claim. Mark A1 `n/a` and move on.

## A2. The argument answers the questions this reader judges by

- *Tell:* list the questions the reader must have answered to act on the
  purpose (for a proposal: what is missing today, why now, why this venue,
  why these people, how it differs from what exists; for a paper: what is new,
  why believe it, why it matters). One of them has no answer in the text, its
  answer is implied rather than stated, or its answer sits in a section where
  this reader will not look for it.
- *Fix:* name the unanswered question and propose where its answer belongs —
  often by gathering sentences that are scattered across the text and stating
  the conclusion they share. If the material to answer it is absent, say so
  and ask the writer for it — never invent the fact.
- *Exception:* a question the venue or an earlier section already settles
  needs no second answer (prose principle 1).

## A3. Every claim rests on support that fits it

- *Tell:* a claim with no support; support of the wrong kind (one example
  carrying a general claim, a citation that shows something adjacent); support
  with no stated reading (a number with no baseline, or one the reader cannot
  tell is large or small); support that sits far from the claim it serves; or
  **more support than the claim needs** — a chain of five results where the
  strongest one or two would carry it, so the claim is buried under its own
  evidence. Figures and tables are support too: each must have a claim it
  serves.
- *Fix:* state the claim, then its support, in place. Where the support is
  weaker than the claim, narrow the claim to what the support shows (see A5)
  or flag that stronger support is needed. Where it is in excess, keep the
  strongest items and list the rest as proposed cuts (K2).

## A4. No inference step is left for the reader to supply

- *Tell:* a conclusion — marked by "therefore", "thus", "clearly", "which
  makes", or unmarked — that does not follow from the sentences before it
  without an unstated premise; a sentence whose relation to its paragraph is
  never stated. When the premise exists elsewhere in the text, this is the
  same finding as A3's distant support: report it once, here.
- *Fix:* state the missing step, once, at the gap. This is the one place where
  adding a sentence is the right edit — mark it as an addition so the writer
  sees it. If the step cannot be stated, the conclusion does not follow;
  report that instead of bridging it with a connective.
- *Exception:* steps the stated reader makes without effort. Spelling them out
  is over-explanation (S3).

## A5. The wording is as strong as the evidence — no stronger, no weaker

- *Tell:* "demonstrates", "all", "no prior work" over evidence that supports
  "suggests", "most", "little prior work"; a claim whose scope is wider than
  its evidence (a field credited with results from another field); or the
  reverse — a well-supported result buried under "may", "might", "could
  potentially".
- *Fix:* set each verb, quantifier, and scope to the level the support
  reaches. When
  confidence is low, state why it is low rather than stacking hedges.

## A6. Answer the likely objection where it arises

A2 covers the questions every reader of this kind of text asks; A6 covers an
objection that one specific claim in the text provokes. When a finding fits
both, file it under A2.

- *Tell:* a claim that the stated reader will meet with an obvious "but what
  about…" — an alternative explanation, a competing approach, a known
  limitation — and the text moves on without addressing it, or addresses it
  pages later.
- *Fix:* answer it at the point it arises, in a sentence or a clause — a
  scope limit, a concession, a pointer to the evidence.
- *Exception:* answer only objections this reader is likely to raise. A text
  that pre-empts every conceivable doubt reads as defensive and buries its
  claim.

---

# Structure level

Prose principles 6–8 (one paragraph one theme; linear dependency; lead with
the claim) are the paragraph-scale structure rules and run in this pass. The
principles below add the section-scale rules they do not cover.

## S1. Give space by importance

- *Tell:* the part that carries the claim gets the same length as, or less
  than, the parts that set it up; the reader reaches the main point after most
  of the space is spent. Figures, captions, and tables count as space.
- *Fix:* expand what carries the argument, compress what merely precedes it.
  State the proposed proportions, not only the direction.

## S2. Keep background out of the main line

- *Tell:* a paragraph on the main line stops to give history, definitions, or
  related work, then resumes; or a whole paragraph is a list of prior work
  with the argument returning only in its last sentence.
- *Fix:* move each piece of background to the claim it supports and cut it to
  what that claim requires, or collect it into its own unit ahead of the
  argument.
- *Exception:* one clause of background inside a sentence is not an
  interruption.

## S3. Start from what the reader knows; one new idea per step

- *Tell:* **under-explained** — a term the stated reader cannot understand
  from ordinary usage appears before it is introduced, or several new ideas
  arrive in one sentence; **over-explained** — basics spelled out for a reader
  who has them, or one idea explained in three ways. Adapted text often shows
  both at once: it glosses what the new reader knows and skips what the old
  reader knew.
- *Fix:* anchor on the last thing the stated reader already knows and build
  from there, one new idea at a time. Delete explanation pitched below that
  anchor.
- *Exception:* a tutorial or a first chapter over-explains by design.

---

# Preservation — after any restructure

A structural edit can lose content silently. Before presenting a proposed
restructure, check it against the original:

- **K1. Claims.** Every claim the original made is still made, or its removal
  is listed as a proposed cut.
- **K2. Evidence.** Every number, citation, quotation, and example survives,
  or its removal is listed.
- **K3. Qualifiers.** Scope limits, conditions, and stated uncertainty are
  intact; nothing possible became certain.
- **K4. Voice.** The writer's own phrasing survives wherever it was not the
  problem.

K1 and K2 are checked on the proposed outline; K3 and K4 can only be checked
on drafted text, so name the qualifiers at risk with the outline and check
them again after drafting. A restructure that fails K1–K3 is not presented.
Fall back to a lighter edit.

---

# Delivery method — argument and structure findings

The delivery method in `prose-principles.md` governs prose findings, and its
general rules — affirm before critique, end on a "Net:" line, respect workflow
constraints — apply here too. For argument and structure findings, add:

- **Open with the intake.** Claim, reader, purpose — one line each. If the
  writer disagrees with any of them, the diagnosis below is void; let them
  correct it first.
- **Show a reverse outline.** One line per paragraph stating the job it does
  in the argument (not its topic). Gaps, repeats, and misplaced paragraphs
  show up in the outline before they show up in the prose.
- **Evidence for every finding.** Name the paragraph and quote the sentence. A
  finding without a location is a hunch; label it as one or drop it.
- **Propose an outline, not sentences.** For a structural change, present the
  proposed outline next to the reverse outline and mark what moves, merges,
  grows, shrinks, or is cut. Where a finding calls for an added sentence (A2,
  A4), state in the outline what the sentence must say and where its content
  comes from. Draft sentences only after the writer approves the outline.
- **Stop at the outline.** The diagnosis ends with the proposed outline, the
  open questions for the writer, and a "Net:" line. The prose pass and the
  target checklist run later, on the text drafted from the approved outline.
- **Ask for what is missing.** A fact the fix needs, a section not supplied,
  the venue's requirements — list these as questions for the writer, few and
  specific. Do not guess.
- **In a long or multi-file document,** outline the section in focus, read the
  rest for context, and treat a move across sections as a normal proposal.
  Problems that lie wholly in other sections are flagged, not fixed.
- **Group findings by level, argument first.** Hold prose findings for
  passages that an open higher-level finding will change.
- **A good text has the right to stay unchanged.** When the argument and
  structure hold, say so in one line and proceed to the prose pass. Never
  restructure to show effort.
