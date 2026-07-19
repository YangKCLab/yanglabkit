---
name: yanglabkit-writing
user_invocable: true
disable-model-invocation: false
description: >-
  Tighten and revise prose the Yang Lab way, and draft new prose to the same
  standard. Applies a distilled line-editing method — never add explanation a
  sentence already carries, merge redundant sentences, delete padding not
  content, order claims general → specific, one paragraph one theme — plus an
  academic layer for reviewer-driven manuscript revision (significance over
  novelty, terminology discipline, claims precise enough to survive their own
  counterexamples). In revision mode it diagnoses by line and proposes drop-in
  replacements with rationales, and never applies edits without approval.
  Trigger when the user asks to tighten, condense, polish, review, or revise
  prose, respond to referee/reviewer comments, or asks the agent to draft
  substantive prose (an abstract, section, letter, or post).
---

# yanglabkit-writing — Prose tightening & academic revision

Edit and draft prose to Kaicheng Yang's line-editing standard. The north star:
**don't add explanation if an existing sentence already carries the message.**
Everything else follows from it — prefer removals, merge redundancy, keep every
idea while deleting its padding, and make any *added* word earn its place.

This skill is pure markdown guidance with two layers:

- **Core layer (always on)** — general prose tightening; applies to any writing.
- **Academic layer** — activates when the target is a scholarly manuscript,
  referee response, or grant text, especially under reviewer pressure.

## When to Use

- Requests to tighten, condense, polish, review, or line-edit existing prose.
- Revising a manuscript or section in response to referee/reviewer comments.
- Drafting substantive new prose for the user — an abstract, paper section,
  cover letter, blog post — so it comes out in-voice on the first pass.
- Questions like "is this paragraph too wordy", "does this section flow",
  "how do I answer this reviewer".

## Modes

**Revision mode** (existing text) — diagnose, propose, wait:

1. Read the full target passage before judging any sentence.
2. **Affirm before critique** — first name what already works, so the writer
   knows what to preserve.
3. **Diagnose by line** — cite the exact sentences and the exact flaw (which
   two sentences repeat one message, which claim pre-empts which), never
   abstract "tighten this" notes. Work through the core principles in
   `reference/prose-principles.md`; if the academic layer is active, also apply
   `reference/academic-revision.md`.
4. **Propose drop-in replacements** — for each diagnosis give replacement text
   plus a one-line rationale tied to the principle it serves.
5. Where a deeper cut is possible, offer a **recommended option and a separate
   aggressive option** (what to cut if space gets tight), kept distinct so the
   writer chooses the trade-off.
6. **End with a "Net:" bottom line** — one recommended next action, not an
   undifferentiated menu.
7. **Apply nothing until the user approves.** Only after approval, apply the
   accepted edits exactly as approved.

**Drafting mode** (new text) — apply the same principles while writing: state
each message once, order claims general → specific, one theme per paragraph,
compress parallel structure, no padding. No proposal step — but flag any spot
where you consciously traded concision for something else.

## Rules

- **Prefer removals.** A word that must be *added* has to earn its place by
  doing load-bearing work, not explaining.
- **Never add explanation a sentence already carries.** If the point is made, a
  clarifying sentence is redundancy, not help.
- **Condense by deleting padding, not content.** Every idea in the original
  survives the tightening; only its costume shrinks.
- **Don't restructure when a lighter local fix exists.** Relocation and rewrites
  are last resorts after merging and trimming.
- **Never apply edits without approval** in revision mode — propose first,
  always.
- **Inherit the writer's own standard.** Tie every fix to the writer's stated
  principles and voice; don't import an external house style.
- **Stay in scope.** Flag cross-section redundancy or out-of-scope issues for a
  later pass instead of fixing them mid-task, and respect the project's workflow
  constraints (e.g. sync/pull before editing shared files).

## Reference docs

- `reference/prose-principles.md` — the core tightening principles and the
  delivery method in full detail.
- `reference/academic-revision.md` — the academic layer: when it activates and
  its principles for reviewer-driven manuscript revision.
