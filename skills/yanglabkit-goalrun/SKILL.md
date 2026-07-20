---
name: yanglabkit-goalrun
user-invocable: true
disable-model-invocation: false
description: >-
  Run a yanglabkit skill unattended against its acceptance target. Given an
  artifact task (a figure, a passage, a palette) and explicit user opt-in, it
  does the work with the domain skill's method, iterates until every
  mechanical and judged item in that skill's reference/target.md passes, and
  writes a target report the /goal evaluator (or the user) can check.
  Advisory items are reported, never blocking. Trigger when the user asks for
  an unattended or automated pass, sets up a Claude Code /goal for
  figure/prose/palette work, or asks to run a yanglabkit skill "to target".
---

# yanglabkit-goalrun — Automated runs against a skill target

Drive any yanglabkit domain skill to its acceptance target without a human in
the loop. The domain skills stay purely interactive; this skill owns the
automated contract: **iterate against the target, prove it with a report.**

## When to Use

- The user explicitly asks for an unattended/automated pass over a figure,
  passage, or palette task.
- The user is setting up a Claude Code `/goal` for work covered by a
  yanglabkit skill.
- **Never self-initiated.** Without an explicit opt-in, hand the task to the
  domain skill's interactive workflow instead.

## Workflow

1. **Resolve the domain skill and its target.** Targets live at a fixed path:
   `skills/<name>/reference/target.md` (figures, writing, scicolor). Load the
   target and the domain skill's method docs.
2. **Do the work with the domain skill's method.** The runner changes the
   *contract*, not the craft — conventions, principles, and hard invariants
   (never pie charts, never rainbow, colour via scicolor) all still bind.
3. **Self-check against the target and iterate** until every `[mechanical]`
   and `[judged]` item is `pass` (or `n/a` with a reason). The strong model
   doing the work is the judge; iterate-fix-recheck, don't grade on hope.
4. **Write the target report** next to the artifact:
   `<artifact-stem>.target-report.md`, one line per item —
   `id pass|fail|n/a — one-line evidence`. Include `[advisory]` items with
   their observations.
5. **Stop** when the report shows no failing mechanical/judged items. Report
   what was produced, where the report is, and any advisory observations.

## Goal condition template

    /goal <artifact> exists and <artifact-stem>.target-report.md next to it
    marks every mechanical and judged item of the <skill> target pass or n/a

The condition tests the **report**, not the artifact's quality — judgment
stays with the strong model doing the work; the goal evaluator only needs
decidable state.

## Rules

- **Explicit opt-in only.** A `/goal` invocation or the user's direct request;
  never infer it.
- **Advisory items never block.** Report them; do not fail a run on them, and
  do not accept a configuration that would.
- **`n/a` needs a reason** and counts as pass (e.g. no proportion axis, single
  panel, deliberate payoff paragraph).
- **Honest reports only.** Evidence lines cite the actual code/text/render —
  a false `pass` is worse than a failed run.
- **Per-skill carve-out — writing:** the interactive propose-before-apply gate
  relaxes to apply-and-iterate, but every edit stays **uncommitted**; finish
  by presenting the accumulated diff for one human review. Never commit.
- **Respect workflow constraints** from the surrounding project (pull before
  editing live-synced files, branch conventions).

## Known targets

| Skill | Target | Artifact | Automation ceiling |
|---|---|---|---|
| `yanglabkit-figures` | `reference/target.md` (F1–F19) | figure file | mostly mechanical |
| `yanglabkit-writing` | `reference/target.md` (W1–W11) | passage/file | judged (no mechanical items, by design) |
| `yanglabkit-scicolor` | `reference/target.md` (C1–C10) | palette / its use in a figure | mixed |

When a figure task uses scicolor (it always should), the figure's report
covers the colour items via F6 — a separate scicolor report is only needed for
standalone palette work.
