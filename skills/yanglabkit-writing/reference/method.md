# Method — voice, intake, delivery, preservation

How `yanglabkit-writing` works across its four levels: whose text it is, what
to establish before diagnosing, how to present a diagnosis, how to touch the
file, and how to check that a restructure lost nothing. The principles themselves live in the level files
(`p0-argument.md`, `p1-structure.md`, `p2-flow.md`, `p3-polish.md`).

The fixed order of levels, the intake, the preservation check, and the right
of a good text to stay unchanged are adapted from
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
