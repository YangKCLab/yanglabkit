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
  asks whether a text argues or flows well, asks to check a text or adapt it
  for another venue or reader, or asks the agent to draft substantive prose
  (an abstract, section, letter, or post) from a topic, notes, or dictation.
---

# yanglabkit-writing — Argument, structure, flow, polish

Edit and draft prose to Kaicheng Yang's standard, at four levels in a fixed
order. One north star binds all of them: **don't add explanation if an
existing sentence already carries the message** (P3.1).

| Level | Asks | Principles | Delivers |
|---|---|---|---|
| **P0 Argument** | Does the text assert something, support it, and answer what this reader needs? | `reference/p0-argument.md` (P0.1–P0.6) | findings + proposed outline |
| **P1 Structure** | Is the argument in the right order, at the right length, in units that each do one job? | `reference/p1-structure.md` (P1.1–P1.6) | reverse outline + proposed outline |
| **P2 Flow** | Does each sentence do its local job and read in one pass? | `reference/p2-flow.md` (P2.1–P2.4) | numbered diffs |
| **P3 Polish** | Does every sentence and word carry something not already said? | `reference/p3-polish.md` (P3.1–P3.5) | numbered diffs |

Pure markdown guidance, for any writing — papers, proposals, posts, letters,
documentation. This file picks the scope and states the invariants; the
reference files own everything else:

- `reference/method.md` — how to work: voice, intake, delivery, the special
  scopes, drafting, applying edits, preservation. **Always load.**
- `reference/tells.md` — the AI tells (T1–T14). **Always load.**
- the level files — **load only the levels in scope.** In an all-levels run,
  load P2 Flow and P3 Polish after the writer has decided on the outline.
  Drafting uses all four.
- `reference/target.md` — the acceptance checklist, numbered 1:1 to the
  principles. Load before presenting P2 Flow or P3 Polish edits, a draft, or
  a check-only report.

## When to Use

Any request to revise, restructure, tighten, polish, check, or adapt existing
prose, to judge whether it argues or flows well or sounds machine-written, or
to draft substantive new prose from a topic, bullet points, notes, or
dictation.

## Workflow

**Revision** (existing text):

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
   | names a level or a range | exactly that |
   | "unslop", "does this sound like AI" | AI tells only (`tells.md`) |
   | "check", "audit", "run the checklist" | check only (`method.md`) |
   | "adapt this for <reader or venue>" | adapt for a new reader (`method.md`) |

2. **Diagnose from the highest level in scope down, and present** as
   `method.md` prescribes for those levels. A run that includes P0 Argument
   or P1 Structure stops at the proposed outline and waits; the lower levels
   then run on the text drafted from the approved outline.
3. **Wait for approval, then apply** exactly what was approved.

**Drafting** (new text) — follow the drafting sequence in `method.md`.

## Rules

- **Never apply edits without approval** in revision — propose first, always.
- **Higher level first.** Within the scope, do not propose an edit in a
  passage that a higher-level finding will change. If the text has no
  statable claim (P0.1), say so and stop; do not tighten around it.
- **Name every level.** Write "P1 Structure", never a bare "P1"; cite a
  principle as "P1.4 Structure — lead each paragraph with its claim", and a
  tell as "T3 tail participle clause". The writer should never need to look
  a number up.
- **Match the force of the edit to the problem.** Don't restructure when a
  lighter local fix exists — but when the structure *is* the problem, be
  aggressive: propose the deletion or relocation outright, not a timid local
  patch. Propose-before-apply makes boldness safe; shyness, not overreach, is
  the failure mode to avoid.
- **A good text may stay unchanged.** When a level holds, say so in one line
  and move on. Never manufacture findings to show effort.
- **Never invent content.** A gap that needs a fact the text or the input
  does not contain is a question for the writer, not something to fill.

## Automated mode

Handled by the sibling `yanglabkit-goalrun` skill (explicit opt-in only): it
applies and iterates against `reference/target.md` on a dedicated
`goalrun/<slug>` branch, committing and pushing as it progresses; the user
reviews the branch diff and merges. The interactive contract above — propose
before apply — is unchanged.
