---
name: yanglabkit-writing
user-invocable: true
disable-model-invocation: false
description: >-
  Revise and tighten prose the Yang Lab way, and draft new prose to the same
  standard. Works at three levels in a fixed order — argument (is the claim
  stated, supported, and scoped for this reader), structure (order, proportion,
  background, explanation level), then prose (a distilled line-editing method:
  never add explanation a sentence already carries, merge redundant sentences,
  delete padding not content, prefer shorter linear sentences, one paragraph
  one theme, lead each paragraph with its claim). In revision mode it diagnoses
  with evidence, proposes an outline or drop-in replacements with rationales,
  and never applies edits without approval. Trigger when the user asks to
  tighten, condense, polish, review, restructure, or revise prose, asks whether
  a text argues or flows well, or asks the agent to draft substantive prose (an
  abstract, section, letter, or post).
---

# yanglabkit-writing — Argument, structure, prose

Edit and draft prose to Kaicheng Yang's standard, at three levels in a fixed
order: **argument → structure → prose.** The prose level is anchored by one
north star: **don't add explanation if an existing sentence already carries the
message.**

This skill is pure markdown guidance and applies to any writing — papers,
proposals, posts, letters, documentation. The substance lives in three
reference docs: `reference/argument-structure.md` (the intake, the argument
principles A1–A6, the structure principles S1–S3, the preservation check, and
the delivery method for those levels), `reference/prose-principles.md` (twelve
tightening principles, each with its tell and fix, plus the delivery method for
a prose diagnosis), and `reference/target.md` (the acceptance checklist, keyed
to the principles). This file only orchestrates.

## When to Use

- Requests to revise, review, or restructure existing text, or questions like
  "does this argue well", "is the logic sound", "does this section flow".
- Requests to tighten, condense, polish, or line-edit existing prose.
- Drafting substantive new prose for the user — an abstract, paper section,
  proposal, cover letter, blog post — so it comes out in-voice on the first
  pass.

## Workflow

**Revision mode** (existing text) — pick the scope, diagnose, propose, wait:

1. **Pick the scope from the request.**
   - *Full revision* ("revise", "review", "restructure", "does this argue
     well") runs all three levels.
   - *Tightening* ("tighten", "condense", "polish", "line-edit") runs the
     prose level only. Still read for argument and structure problems, and
     report any you see in one line each without fixing them — the writer
     decides whether to widen the scope.
2. **Full revision: argument and structure first.** Follow
   `reference/argument-structure.md`: state the intake, diagnose A1–A6 and
   S1–S3 (with prose principles 6–8), and present the findings with the
   reverse outline and a proposed outline. **Stop here** and wait for the
   writer's decision on the outline. When both levels hold, say so in one
   line and go straight to step 3. After the writer approves an outline,
   draft the restructured text from it and continue with step 3 on that
   draft.
3. **Prose level.** Diagnose the passage against
   `reference/prose-principles.md`, run the target checklist
   (`reference/target.md`) over the proposed result, and present the
   diagnosis following the prose delivery method.
4. **Apply nothing until the user approves.** Only after approval, apply the
   accepted edits exactly as approved.

**Drafting mode** (new text) — state the intake (claim, reader, purpose)
before writing, then apply all three levels while writing. No proposal step —
but flag any spot where you consciously traded concision for something else.

## Rules

- **Never apply edits without approval** in revision mode — propose first,
  always.
- **Higher level first.** Do not polish sentences that an argument or
  structure fix will remove. If the text has no statable claim (A1), say so
  and stop; do not tighten around it.
- **Match the force of the edit to the problem.** Don't restructure when a
  lighter local fix exists — but when the structure *is* the problem, be
  aggressive: propose the deletion or relocation outright, not a timid local
  patch. Propose-before-apply makes boldness safe; shyness, not overreach, is
  the failure mode to avoid.
- **A good text may stay unchanged.** When a level holds, say so in one line
  and move on. Never manufacture findings to show effort.
- **Never invent content.** An argument gap that needs a fact the text does
  not contain is reported to the writer, not filled.
- Everything else — what to fix and how to present it — lives in the two
  method docs; follow them rather than improvising.

## Automated mode

Handled by the sibling `yanglabkit-goalrun` skill (explicit opt-in only): it
applies and iterates against `reference/target.md` on a dedicated
`goalrun/<slug>` branch, committing and pushing as it progresses; the user
reviews the branch diff and merges. The interactive contract above — propose
before apply — is unchanged.
