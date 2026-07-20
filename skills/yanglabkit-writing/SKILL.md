---
name: yanglabkit-writing
user-invocable: true
disable-model-invocation: false
description: >-
  Tighten and revise prose the Yang Lab way, and draft new prose to the same
  standard. Applies a distilled line-editing method — never add explanation a
  sentence already carries, merge redundant sentences, delete padding not
  content, prefer shorter linear sentences, one paragraph one theme, arrange
  paragraphs by linear dependency and lead each with its claim. In revision
  mode it diagnoses by line and
  proposes drop-in replacements with rationales, and never applies edits
  without approval. Trigger when the user asks to tighten, condense, polish,
  review, or revise prose, or asks the agent to draft substantive prose (an
  abstract, section, letter, or post).
---

# yanglabkit-writing — Prose tightening

Edit and draft prose to Kaicheng Yang's line-editing standard, anchored by one
north star: **don't add explanation if an existing sentence already carries the
message.**

This skill is pure markdown guidance and applies to any writing — papers,
posts, letters, documentation. The substance lives in two reference docs:
`reference/prose-principles.md` (eleven tightening principles, each with its
tell and fix, plus the delivery method for presenting a diagnosis) and
`reference/target.md` (the acceptance checklist, numbered to the principles).
This file only orchestrates.

## When to Use

- Requests to tighten, condense, polish, review, or line-edit existing prose.
- Drafting substantive new prose for the user — an abstract, paper section,
  cover letter, blog post — so it comes out in-voice on the first pass.
- Questions like "is this paragraph too wordy", "does this section flow".

## Workflow

**Revision mode** (existing text) — diagnose, propose, wait:

1. Diagnose the passage against the principles in
   `reference/prose-principles.md`, run the target checklist
   (`reference/target.md`) over the proposed result, and present the diagnosis
   following the delivery method.
2. **Apply nothing until the user approves.** Only after approval, apply the
   accepted edits exactly as approved.

**Drafting mode** (new text) — apply the same principles while writing. No
proposal step — but flag any spot where you consciously traded concision for
something else.

## Rules

- **Never apply edits without approval** in revision mode — propose first,
  always.
- **Match the force of the edit to the problem.** Don't restructure when a
  lighter local fix exists — but when the structure *is* the problem, be
  aggressive: propose the deletion or relocation outright, not a timid local
  patch. Propose-before-apply makes boldness safe; shyness, not overreach, is
  the failure mode to avoid.
- Everything else — what to fix and how to present it — lives in
  `reference/prose-principles.md`; follow it rather than improvising.

## Automated mode

Handled by the sibling `yanglabkit-goalrun` skill (explicit opt-in only): it
applies and iterates against `reference/target.md` on a dedicated
`goalrun/<slug>` branch, committing and pushing as it progresses; the user
reviews the branch diff and merges. The interactive contract above — propose
before apply — is unchanged.
