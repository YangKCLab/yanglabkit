# Method — voice, intake, delivery, drafting, preservation

How `yanglabkit-writing` works, at every level. The principles live in the
level files; the scope table and the invariants live in `SKILL.md`.

The fixed order of levels, the intake, the preservation check, the drafting
sequence, and the scope-widening rule are adapted from
[cida](https://github.com/mizzlelover/cida) (MIT).

## Voice

The text belongs to the writer, not to you. Your job is to remove what is not
working, not to rewrite in your own voice.

- Keep the writer's word choices, sentence rhythm, and claims unless a
  principle requires a change. When a rewrite is needed, keep as many of the
  writer's words as possible.
- Never change meaning, claims, numbers, citations, or hedges. If a claim
  looks wrong, say so in the diagnosis; do not silently fix it.
- Do not flatten rhythm. Keep the writer's mix of short and long sentences.
- Do not add opinions, first person, or asides the writer did not write.
- **Audit your own text.** Reread every replacement and every draft against
  `tells.md` before presenting it. Replacements are where AI tells enter, and
  a replacement that adds a tell is worse than the original sentence.

## Intake — before diagnosing P0 Argument or P1 Structure

State three facts in one line each. Take them from the text and its context;
ask the writer only when the text cannot tell you.

- **Claim.** What the piece asserts, in one sentence.
- **Reader.** Who reads it, what they already know, and what they are
  sceptical of.
- **Purpose.** What the reader should decide, believe, or do after reading —
  fund it, accept it, adopt the method, grant the request.

If the text was adapted from a version written for a different reader, say so:
its emphasis, vocabulary, and evidence often still serve the first reader,
and that one cause explains many findings.

## Delivery — every run

- **Read the whole text first,** whatever the scope.
- **State the scope,** with level names ("Scope: P2 Flow and P3 Polish").
- **Affirm before critique.** Open with what already lands well, as its own
  section, so the writer knows what to preserve.
- **Group findings by level, highest first,** each under its level name, with
  the tells tagged to that level. List any edit you are holding because a
  higher-level finding will change its passage.
- **Evidence for every finding.** Name the exact paragraph or sentences and
  the exact flaw ("these two sentences both assert X"), never a vague "this
  could be tighter". A finding without a location is a hunch; label it as one
  or drop it.
- **One principle per finding.** The advice inherits the writer's own
  standard; it never imports an external house style. A finding that fits two
  levels is filed under the higher one: moving content between paragraphs is
  P1 Structure even when the motive is redundancy.
- **Above the scope: one line each, no fix.** Report a higher-level problem
  you noticed while reading, with its level name — a handful of lines at
  most; do not search for more. An in-scope edit in such a passage is still
  proposed, with a note that it may be overtaken. Do not report problems
  below the scope.
- **Say when the scope is too narrow.** If the edits of a P2 Flow or P3 Polish
  run would rewrite more than about 40% of the words in the passage, stop,
  show the few edits that are safe, and recommend a wider scope with one line
  on why.
- **Outside the passage: flag, don't fix.** In a long or multi-file document,
  work on the section in focus and read the rest for context. A move across
  sections is a normal proposal; a problem wholly elsewhere is a note.
- **Ask for what is missing.** A fact the fix needs, a section not supplied,
  the venue's requirements — list these as questions, few and specific.
- **End on a "Net:" line.** One recommended next action, not a menu.
- **Respect workflow constraints.** Before offering to apply edits, honor the
  project's rules (pull before editing live-synced files, branch conventions,
  approval gates) — including staging preferences: if the writer wants edits
  applied but uncommitted so they can review one accumulated diff, never
  auto-commit per edit.

## Delivery — P0 Argument and P1 Structure

These levels change which sentences exist, so they are delivered as outlines.

- **Open with the intake.** If the writer disagrees with any of its three
  lines, the diagnosis is void; let them correct it first.
- **Show a reverse outline.** One line per paragraph stating the job it does
  in the argument (not its topic). Gaps, repeats, and misplaced paragraphs
  show up in the outline before they show up in the prose.
- **Propose an outline, not sentences.** Mark what moves, merges, grows,
  shrinks, or is cut. Where a finding calls for an added sentence, state what
  it must say and where its content comes from. List the proposed cuts and
  the qualifiers at risk (Preservation).
- **Note what you hold for lower levels** — one thing under several names, a
  repeated sentence — in a short "held" list, not in the findings.
- **Stop at the outline.** Draft sentences only after the writer approves it.

## Delivery — P2 Flow and P3 Polish

These levels change sentences in place, so they are delivered as diffs.

- **One numbered item per change,** so the writer can approve by number.
  Number consecutively through the level groups, document order within each
  group. Each item carries the original, the drop-in replacement, and a one-line
  reason naming the principle or tell. A verdict without a fix is half an
  edit. A deletion is an item with an empty replacement.
- **Use a diff tool when the harness has one** (for example a `propose` tool
  that draws word-level diffs): one call per diagnosis, with the file path
  when the tool can check the originals. Otherwise write each item as a
  fenced `diff` block with a `- original` and a `+ replacement` line.
- **Quote the original verbatim** — the exact span an edit would replace,
  copied from the file. Confirm that each original occurs in the file before
  presenting.
- **Recommended option and aggressive option, kept distinct.** Where deeper
  cuts are possible, present the safe recommendation and, separately, what to
  cut if space gets tight — the writer owns the trade-off. But when the
  aggressive edit is genuinely the better one, make *it* the recommendation.
- **Before presenting,** check the 40% rule, then run the target items
  (`target.md`) for the levels in scope over the proposed result. Report the
  outcome in one line, naming any item that still fails.

## Scope — AI tells only

State the scope as "AI tells only". List the items in document order, one per
sentence, naming every tell in it. Check only the `WT` items. Any other
problem noticed while reading gets one line with its level name and no fix.
The "Net:" line says whether the passage as a whole reads as machine-written,
and which tells drive that.

## Scope — check only

Diagnose and propose nothing.

- Run the items of `target.md` for the levels named, or for all levels when
  none is named, highest first, in its report format. State the intake first
  if P0 Argument or P1 Structure is included. For each `fail`, name the
  paragraph or sentence.
- Skip the preservation items unless the writer names an earlier version.
- The "Net:" line names the highest level that fails.

## Scope — adapt for a new reader

The text moves to a different reader — another venue, another funder, a paper
recast as a proposal. The content stays; what changes is what this reader
needs from it.

- **State two intakes:** the reader and purpose the text was written for, and
  the reader and purpose it must now serve. The claim usually stays; say so
  if it must change.
- **Load** the P0 Argument, P1 Structure, and P2 Flow files, and **run only
  the principles that depend on the reader:**
  - P0.2 Argument — which of the new reader's questions are unanswered, and
    which answers are now unnecessary?
  - P0.3 Argument — which support can this reader judge, and which needs
    background they lack?
  - P1.1 Structure — what was the argument for the old reader may be setup
    for the new one.
  - P1.6 Structure — what is glossed that the new reader knows, and what is
    assumed that they do not?
  - P2.3 Flow — terms, short names, and labels carried over from the old
    venue.
- **Deliver as an outline** (above). The proposed outline may apply the other
  P1 Structure principles where moving content requires it. Deliver P2.3 as a
  list of term choices. Reach the new proportions by cutting what served the
  old reader before adding anything.
- **Other problems** — ones that do not depend on the reader — get one line
  each with the level name, and no fix.
- **The adapted text must stand alone.** Nothing may depend on the earlier
  version or mention it, unless the venue asks for that history. Flag traces
  of the old venue outside the passage in focus.

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
     wording once. Do not carry the speaking order into the outline. Drop
     spoken fillers ("um", "I guess"); keep a hedge that qualifies a fact
     ("maybe half", "I didn't measure it").
   - *A transcript from speech recognition:* names, numbers, and technical
     terms may be wrong. List the ones the draft depends on, with your best
     reading of each, and ask the writer to confirm them.
2. **State the intake.**
3. **Sharpen the claim until someone could disagree with it.** If the input
   gives only a topic, use the two methods in P0.1 to propose one to three
   candidate claims and let the writer choose. Do not draft around a topic.
4. **Write the outline:** one line per paragraph stating its job in the
   argument, in the order P1 Structure requires, each line marked with the
   input points it uses. For a draft of more than about five paragraphs, show
   the outline and wait for the writer's decision; ask every question in that
   same stop.
5. **Draft from the outline,** applying P2 Flow and P3 Polish as you write.
   Keep the writer's own phrases where they work; a draft from dictation
   should still sound like its speaker. Supply a title only when the genre
   needs one; a title may restate the claim. **Write to the length the
   content supports:** if the writer named a length the input cannot fill,
   say so and name the material that would fill it; never pad.
6. **Check before presenting:** the target items for all four levels, the
   tells, and the drafting items (`WD`). After the draft, add short notes:
   points left out and why, unconfirmed readings, open questions, and any
   spot where you traded concision for something else.

## Applying approved edits

- Apply exactly what was approved, one accepted item at a time. Replace the
  smallest span that carries the change; never re-paste a whole paragraph to
  change one sentence.
- **LaTeX:** do not touch `\cite`, `\ref`, `\label`, math, macros,
  environments, comments, or the preamble. Edit the prose inside them.
- **Markdown:** keep frontmatter, links, footnotes, and code blocks unchanged.
- Keep the file's line-break convention (for example one sentence per line).

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
