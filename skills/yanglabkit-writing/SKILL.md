---
name: yanglabkit-writing
user-invocable: true
disable-model-invocation: false
description: >-
  Revise and tighten prose the Yang Lab way, and draft new prose to the same
  standard. Works at four levels in a fixed order — P0 Argument (is the claim
  stated, supported, and scoped for this reader), P1 Structure (proportion,
  paragraph order, one theme per paragraph, lead with the claim), P2 Flow
  (each sentence does its local job, one name per thing, linear sentences),
  P3 Polish (never add explanation a sentence already carries, merge
  redundant sentences, delete padding not content, prefer removals) — plus a
  scan for AI-writing tells, also run on its own ("unslop"). A request
  can run all levels or only some, e.g. polish only. In revision mode it
  diagnoses with evidence, proposes an outline or drop-in replacements with
  rationales, and never applies edits without approval. Trigger when the user
  asks to tighten, condense, polish, review, restructure, or revise prose,
  asks whether a text argues or flows well, or asks the agent to draft
  substantive prose (an abstract, section, letter, or post).
---

# yanglabkit-writing — Argument, structure, flow, polish

Edit and draft prose to Kaicheng Yang's standard, at four levels in a fixed
order. One north star binds all of them: **don't add explanation if an
existing sentence already carries the message.**

| Level | Asks | Principles | Delivers |
|---|---|---|---|
| **P0 Argument** | Does the text assert something, support it, and answer what this reader needs? | `reference/p0-argument.md` (P0.1–P0.6) | findings + proposed outline |
| **P1 Structure** | Is the argument in the right order, at the right length, in units that each do one job? | `reference/p1-structure.md` (P1.1–P1.6) | reverse outline + proposed outline |
| **P2 Flow** | Does each sentence do its local job and read in one pass? | `reference/p2-flow.md` (P2.1–P2.4) | drop-in replacements |
| **P3 Polish** | Does every sentence and word carry something not already said? | `reference/p3-polish.md` (P3.1–P3.5) | drop-in replacements |

This skill is pure markdown guidance and applies to any writing — papers,
proposals, posts, letters, documentation. Each level file owns its principles
(tell, fix, exception). `reference/tells.md` owns the AI tells (T1–T14), a
cross-level scan that is also the audit for your own replacement text.
`reference/method.md` owns the voice rules, the intake, the delivery method,
the rules for applying edits, and the preservation check; `reference/target.md` owns the acceptance
checklist, numbered 1:1 to the principles. This file only orchestrates. Load
`method.md`, `tells.md`, and the level files in scope — not the other level files — and
`target.md` when you reach a checklist step. In an all-levels run, load the P2
Flow and P3 Polish files only after the writer has decided on the outline.

## When to Use

- Requests to revise, review, or restructure existing text, or questions like
  "does this argue well", "is the logic sound", "does this section flow".
- Requests to tighten, condense, polish, or line-edit existing prose.
- Drafting substantive new prose for the user — an abstract, paper section,
  proposal, cover letter, blog post — so it comes out in-voice on the first
  pass.

## Workflow

**Revision mode** (existing text) — pick the scope, diagnose, propose, wait.

1. **Pick the scope from the request.** When the wording fits no row, take the
   narrowest scope that covers what was asked, and say which one you chose.

   | The user says | Scope |
   |---|---|
   | "revise", "review", "improve" | P0 Argument → P3 Polish (all levels) |
   | "check the logic", "does this argue well" | P0 Argument |
   | "restructure", "reorganize", "fix the order" | P1 Structure |
   | "does this flow", "smooth this" | P2 Flow |
   | "tighten", "condense", "line-edit" | P2 Flow + P3 Polish |
   | "polish", "trim" | P3 Polish |
   | "unslop", "does this sound like AI" | AI tells only (`tells.md`) |
   | names a level or a range | exactly that |

2. **Read the whole text**, whatever the scope.
3. **Work from the highest level in scope down.**
   - *P0 Argument and P1 Structure:* state the intake, diagnose, and present
     the findings with the reverse outline and a proposed outline. **Stop
     here** and wait for the writer's decision. When both levels hold, say so
     in one line and continue. After the writer approves an outline, draft
     the restructured text from it and continue on that draft if lower levels
     are in scope.
   - *AI tells:* in every level run, also scan for the tells tagged with
     that level and list them with its findings.
   - *P2 Flow and P3 Polish:* diagnose, run the target checklist for the
     levels in scope over the proposed result, and present drop-in
     replacements.
4. **Report what lies above the scope** in one line per problem, without
   fixing it — the writer decides whether to widen the scope. Report only what
   you noticed while reading; do not search for more or load the higher level
   files. Name the level from the table above; no principle number is needed.
   Do not report problems below the scope.
5. **Apply nothing until the user approves.** Only after approval, apply the
   accepted edits exactly as approved.

**Drafting mode** (new text) — state the intake (claim, reader, purpose)
before writing, then apply all four levels while writing. Reread the draft
once against `tells.md` and fix what reads as machine-written before
presenting it. No proposal step — but flag any spot where you consciously traded concision for something else.

## Rules

- **Never apply edits without approval** in revision mode — propose first,
  always.
- **Higher level first.** Within the scope, do not propose an edit in a
  passage that a higher-level finding will change. If the text has no
  statable claim (P0.1), say so and stop; do not tighten around it.
- **Name every level.** Write "P1 Structure", never a bare "P1"; cite a
  principle as "P1.4 Structure — lead each paragraph with its claim". The
  writer should never need to look a number up.
- **The north star binds every level.** A fix at any level must not add
  explanation the text already carries (P3.1). The one licensed addition is a
  missing step or answer at P0 Argument, marked as an addition.
- **The text belongs to the writer.** Keep their words, rhythm, claims, and
  hedges unless a principle requires a change (`method.md`, Voice).
- **Audit your own text for AI tells** before presenting any replacement or
  draft (`tells.md`).
- **Match the force of the edit to the problem.** Don't restructure when a
  lighter local fix exists — but when the structure *is* the problem, be
  aggressive: propose the deletion or relocation outright, not a timid local
  patch. Propose-before-apply makes boldness safe; shyness, not overreach, is
  the failure mode to avoid.
- **A good text may stay unchanged.** When a level holds, say so in one line
  and move on. Never manufacture findings to show effort.
- **Never invent content.** An argument gap that needs a fact the text does
  not contain is reported to the writer, not filled.
- Everything else — what to fix and how to present it — lives in the
  reference docs; follow them rather than improvising.

## Automated mode

Handled by the sibling `yanglabkit-goalrun` skill (explicit opt-in only): it
applies and iterates against `reference/target.md` on a dedicated
`goalrun/<slug>` branch, committing and pushing as it progresses; the user
reviews the branch diff and merges. The interactive contract above — propose
before apply — is unchanged.
