# Method — voice, intake, delivery, drafting, preservation

How `yanglabkit-writing` works across its four levels: whose text it is, what
to establish before diagnosing, how to present a diagnosis, how to run the
special scopes (check only, adapt for a new reader), how to draft new text,
how to touch the file, and how to check that a restructure lost nothing. The principles themselves live in the level files
(`p0-argument.md`, `p1-structure.md`, `p2-flow.md`, `p3-polish.md`).

The fixed order of levels, the intake, the preservation check, the right of a
good text to stay unchanged, the drafting sequence, and the scope-widening
rule are adapted from
[cida](https://github.com/mizzlelover/cida) (MIT).

## Naming levels and principles

Always give a level its name with its number: **P0 Argument**, **P1
Structure**, **P2 Flow**, **P3 Polish** — never a bare "P1". Cite a principle
by number and level name, with its short title on first mention in a report:
"P1.4 Structure — lead each paragraph with its claim". The writer should never
need to look a number up.

## Voice — binds every level

The text belongs to the writer, not to you. Your job is to remove what is not
working, not to rewrite in your own voice.

- Keep the writer's word choices, sentence rhythm, and claims unless a
  principle requires a change.
- Prefer deletion and merging over rewriting. When a rewrite is needed, keep
  as many of the writer's words as possible.
- Never change meaning, claims, numbers, citations, or hedges. If a claim
  looks wrong, say so in the diagnosis; do not silently fix it.
- Do not add transitions, summaries, restating topic sentences, or "in other
  words" glosses.
- Do not flatten rhythm. Keep the writer's mix of short and long sentences.
  Uniform sentence length reads as machine-made.
- Do not add opinions, first person, or asides the writer did not write.
- **Audit your own text.** Every replacement and every draft is reread
  against `tells.md` before it is presented. Replacements are where AI tells
  enter.

## Intake — three facts before diagnosing P0 Argument or P1 Structure

State these in one line each. Take them from the text and its context; ask the
writer only when the text cannot tell you.

- **Claim.** What the piece asserts, in one sentence.
- **Reader.** Who reads it, what they already know, and what they are
  sceptical of.
- **Purpose.** What the reader should decide, believe, or do after reading —
  fund it, accept it, adopt the method, grant the request.

When the text was adapted from a version written for a different reader — a
paper recast as a proposal, a proposal moved to another venue — say so in the
intake. Its emphasis, vocabulary, and choice of evidence often still serve the
first reader, and that one cause explains many findings.

A run scoped to P2 Flow or P3 Polish needs no stated intake.

## Delivery — all levels

How the diagnosis is presented matters as much as what it says.

- **Read the whole text first,** whatever the scope. Local edits made without
  the full context break structure that is invisible line by line.
- **State the scope.** Open by naming the levels this run covers, with their
  names ("Scope: P2 Flow and P3 Polish").
- **Affirm before critique.** Open with what already lands well, as its own
  section, so the writer knows what to preserve. Only then list issues.
- **Group findings by level, highest first,** each group under its level name.
  Within the scope, do not propose an edit in a passage that a higher-level
  finding will move, cut, or rewrite — hold it and say so.
- **Evidence for every finding.** Name the exact paragraph or sentences and
  the exact flaw ("these two sentences both assert X"), never a vague "this
  could be tighter". A finding without a location is a hunch; label it as one
  or drop it.
- **Tie every fix to the principle it serves.** The advice inherits the
  writer's own standard; it never imports an external house style.
- **Above the scope: one line each, no fix.** A problem at a level above the
  scope, noticed while reading, is reported in one line with its level name so
  the writer can widen the scope — a handful of lines at most, not a second
  diagnosis. An in-scope edit that sits in such a passage is still proposed,
  with a note that it may be overtaken if the scope widens. Problems below the
  scope are not reported.
- **Say when the scope is too narrow.** If the edits of a P2 Flow or P3 Polish
  run would rewrite more than about 40% of the words in the passage, the
  problem is above the scope. Stop, show the few edits that are safe, and
  recommend widening to P1 Structure or P0 Argument with one line on why.
- **A finding that fits two levels is filed under the higher one.** Moving
  content between paragraphs is P1 Structure even when the motive is
  redundancy; one thing under several names is P2 Flow, not P3 Polish.
- **Flag what lies outside the passage; don't fix it.** Problems wholly in
  other sections get noted for a later pass. In a long or multi-file document,
  work on the section in focus, read the rest for context, and treat a move
  across sections as a normal proposal.
- **Ask for what is missing.** A fact the fix needs, a section not supplied,
  the venue's requirements — list these as questions for the writer, few and
  specific. Do not guess.
- **A good text has the right to stay unchanged.** When a level holds, say so
  in one line and move to the next. Never manufacture findings to show effort.
- **End on a "Net:" bottom line.** One recommended next action — not an
  undifferentiated menu of possibilities.
- **Respect workflow constraints.** Before offering to apply edits, honor the
  project's rules (pull before editing live-synced files, branch conventions,
  approval gates) — including staging preferences: if the writer wants edits
  applied but uncommitted so they can review one accumulated diff, never
  auto-commit per edit.

## Delivery — P0 Argument and P1 Structure

These levels change which sentences exist, so they are delivered as outlines.

- **Open with the intake,** then what already works. If the writer disagrees
  with any of the three intake lines, the diagnosis is void; let them correct
  it first.
- **Show a reverse outline.** One line per paragraph stating the job it does
  in the argument (not its topic). Gaps, repeats, and misplaced paragraphs
  show up in the outline before they show up in the prose.
- **Propose an outline, not sentences.** Present the proposed outline next to
  the reverse outline and mark what moves, merges, grows, shrinks, or is cut.
  Where a finding calls for an added sentence (P0.2, P0.4), state in the
  outline what the sentence must say and where its content comes from.
- **Note what you hold for lower levels.** A P2 Flow or P3 Polish problem
  noticed on the way — one thing under several names, a repeated sentence —
  goes in a short "held" list, not in the findings.
- **Stop at the outline.** The diagnosis ends with the proposed outline, the
  open questions for the writer, and the "Net:" line. Draft sentences only
  after the writer approves the outline; P2 Flow, P3 Polish, and the target
  checklist then run on that draft.

## Delivery — P2 Flow and P3 Polish

These levels change sentences in place, so they are delivered line by line.

- **Drop-in replacement + rationale, per change.** Every finding comes with
  concrete replacement text and a one-line reason naming the principle — a
  verdict without a fix is half an edit.
- **Recommended option and aggressive option, kept distinct.** Where deeper
  cuts are possible, present the safe recommendation and, separately, what to
  cut if space gets tight — the writer owns the trade-off. But when the
  aggressive edit is genuinely the better one, make *it* the recommendation:
  don't downgrade a bold cut or relocation to an "optional extra" out of
  caution.

## Check only

A request to "check", "audit", or "run the checklist" diagnoses and proposes
nothing.

- Run the items of `target.md` for the levels named, or for all levels when
  none is named, highest level first. State the intake first if P0 Argument
  or P1 Structure is included.
- Output one line per item under its level name:
  `id pass|fail|n/a — one-line evidence`. For each `fail`, name the paragraph
  or sentence.
- Skip the preservation items unless the writer names an earlier version to
  compare against.
- End with a "Net:" line naming the highest level that fails. Propose no
  replacement text and no outline.

## Adapt for a new reader

A request to move a text to a different reader — another venue, another
funder, a paper recast as a proposal, a technical report recast for a general
audience. The content stays; what changes is what this reader needs from it.

- **State two intakes:** the reader and purpose the text was written for, and
  the reader and purpose it must now serve. The claim usually stays; say so
  if it must change.
- **Run only the principles that depend on the reader,** in level order:
  - P0.2 Argument — the new reader's questions. Which are unanswered, and
    which answers are now unnecessary?
  - P0.3 Argument — the choice of evidence. Which support can this reader
    judge, and which needs background they lack?
  - P1.1 Structure — proportion. What was the argument for the old reader may
    be setup for the new one.
  - P1.6 Structure — explanation level. What is glossed that the new reader
    knows, and what is assumed that they do not?
  - P2.3 Flow — names. Terms, short names, and labels carried over from the
    old venue.
- **Load** the P0 Argument, P1 Structure, and P2 Flow files at the start.
- **Deliver as P0 Argument and P1 Structure are delivered:** reverse outline,
  proposed outline, proposed cuts, stop. The proposed outline may also apply
  the other P1 Structure principles (order, one theme, claim first) where
  moving content requires it; cite them. Deliver P2.3 as a list of term
  choices, not as replacement sentences. Reach the new proportions by cutting
  what served the old reader before adding anything.
- **Other problems** — ones that do not depend on the reader — get one line
  each with the level name, and no fix. Traces of the old venue outside the
  passage in focus (an abstract, a disclosure, a short name) are flagged.
- Requirements of the new venue that were not supplied (length, required
  sections) are questions for the writer.
- **The adapted text must stand alone.** Nothing may depend on the earlier
  version or mention it, unless the venue asks for that history.

## Drafting — new text

The writer supplies a topic, bullet points, notes, or dictation and asks for
prose. There is no proposal step for sentences, but the claim and the outline
are settled before any paragraph is written.

1. **Read the input for what it is.**
   - *Bullet points or an outline:* the points are the content. Their order
     is a suggestion.
   - *Rough notes or dictation:* the claims are scattered, repeated, and in
     speaking order. First list the distinct claims and the support given for
     each. Treat repetition as the speaker's emphasis and keep the strongest
     wording once. Drop false starts and filler. Do not carry the speaking
     order into the outline.
   - *A transcript from speech recognition:* names, numbers, and technical
     terms may be wrong. List the ones the draft depends on, with your best
     reading of each, and ask the writer to confirm them; a reading the
     writer has not confirmed is flagged in the draft's notes.
   - *Hedges and fillers:* drop spoken fillers ("um", "I guess", "you know").
     Keep a hedge that qualifies a fact ("maybe half", "I think four", "I
     didn't measure it").
2. **State the intake:** claim, reader, purpose (see above).
3. **Sharpen the claim until someone could disagree with it** (P0.1). If the
   input gives only a topic, use the two methods in P0.1 to propose one to
   three candidate claims and let the writer choose. Do not draft around a
   topic.
4. **Write the outline:** one line per paragraph stating its job in the
   argument, in the order P1 Structure requires. Mark each line with the
   input points it uses. Mark any line that needs a fact the input does not
   contain — that is a question for the writer, not something to fill in.
   For a draft of more than about five paragraphs, show the outline and wait
   for the writer's decision before drafting. Ask the transcript
   confirmations and any other questions in that same stop, not separately.
   **Write to the length the content supports.** If the writer named a length
   the input cannot fill, say so with the outline and name the material that
   would fill it; never pad to reach a word count.
5. **Draft from the outline,** applying P2 Flow and P3 Polish as you write.
   Supply a title only when the genre needs one; a title may restate the
   claim.
   Keep the writer's own phrases from the input where they work; a draft from
   dictation should still sound like its speaker (Voice).
6. **Check before presenting:** every point the writer supplied is present or
   listed as left out with the reason; every fact, number, and hedge comes
   from the input; the draft passes the tells audit (`tells.md`) and the
   target items. After the draft, add short notes: points left out and why,
   unconfirmed readings, open questions, and any spot where you traded
   concision for something else.

## Applying approved edits

- Apply exactly what was approved, one accepted item at a time. Replace the
  smallest span that carries the change; never re-paste a whole paragraph to
  change one sentence.
- **LaTeX:** do not touch `\cite`, `\ref`, `\label`, math, macros,
  environments, comments, or the preamble. Edit the prose inside them.
- **Markdown:** keep frontmatter, links, footnotes, and code blocks unchanged.
- Keep the file's line-break convention (for example one sentence per line).
- Do not fix issues outside the requested passage while applying; they were
  flagged in the diagnosis.

## Preservation — after any P0 Argument or P1 Structure change

A structural edit can lose content silently. Check the proposal against the
original:

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
