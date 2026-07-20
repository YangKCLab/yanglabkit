# yanglabkit — agent guide

`yanglabkit` is a **Claude Code plugin marketplace** that distributes the Yang
Lab's agent skills. It is a focused, lab-specific collection — not a
general-purpose research toolkit. Skills follow the portable `SKILL.md`
convention, so any agent that reads markdown instruction files can use them.

## Repository layout

```
.claude-plugin/
  marketplace.json     # marketplace catalog (name, owner, plugins[])
  plugin.json          # plugin manifest — pins the plugin version
skills/
  <skill-name>/
    SKILL.md           # skill definition (frontmatter + When to Use / Workflow / Rules)
    reference/         # on-demand reference docs
    data/              # bundled data the skill reads at runtime
tasks/
  README.md            # task-system overview, workflow, and task index
  <task-name>/
    README.md          # human-readable task contract
    task.json          # versioned machine-readable contract, when applicable
    data/              # fixed task inputs, provenance, and checksums
    pyproject.toml     # shared Python environment, when applicable
    uv.lock            # exact Python dependency lock, when applicable
    submission-template/ # required candidate output structure
    submissions/       # isolated candidate runs
scripts/               # build-time-only scripts (NOT loaded as skills)
README.md              # user-facing install + skill list
```

The whole repo is a single plugin: the marketplace entry uses `source: "./"`, so
the plugin root is the repo root. On install, the entire repo (including
`README.md`, `scripts/`, etc.) is copied into the plugin cache, but only
`skills/<name>/` directories load as skills. Files under `tasks/` are inert
evaluation materials: agents use them only when explicitly asked to run a task.

## Skills

### `yanglabkit-scicolor`

Recommends a scientifically sound colour palette for a figure/chart/heatmap/map/
slide/UI. Applies the decision logic from **Crameri et al. (2020), "The misuse
of colour in science communication"** (doi:10.1038/s41467-020-19160-7) to pick a
palette class (categorical / sequential / diverging / multi-sequential) and
returns concrete hex codes, defaulting to colourblind-safe, perceptually uniform
choices and refusing rainbow/jet.

- **Pure markdown + data, no runtime dependency.** The skill reads two bundled
  JSON files and one reference guide; it never executes code.
- **File roles:**
  - `SKILL.md` — the always-loaded orchestrator: procedure + hard invariants.
    Delegates the taxonomy, decision flow, and detailed guardrails to the guide.
  - `reference/selection-guide.md` — the on-demand reference that solely owns the
    class taxonomy, the concrete decision flow (which palettes per class), and
    the Crameri guardrail checklist. Keep this the single source for that
    substance; do not re-duplicate it in `SKILL.md`.
  - `data/colors.json` — discrete/categorical palettes (54 schemes, 11
    collections). **Verbatim snapshot** of scicolor's
    `colorpicker/public/colors/colors.json`.
  - `data/continuous-colormaps.json` — 28 continuous colormaps (32 hex stops +
    class/CVD/perceptual-uniformity metadata), **extracted** from the scicolor
    Python package.
  - `data/SOURCE.md` — provenance + re-sync instructions for both data files.
  - `reference/target.md` — the acceptance spec (see "Instructions vs targets"
    below): items `C1`–`C10`, tiered, citing the guide's Step 5 guardrails and
    the SKILL.md rules.

### `yanglabkit-figures`

Styles matplotlib/seaborn figures to the Yang Lab's conventions for scientific
figures: minimal and print-first, spines dropped by plot type, subtle dashed
grids, frameless legends, percentage axes, gray dashed reference lines, and
vector PDF export. Refuses pie charts and rainbow/jet colormaps, and defers every
colour choice to the sibling `yanglabkit-scicolor` skill.

- **Pure markdown guidance, no runtime dependency.** The skill reads one
  reference doc and applies its conventions to the plotting code; it never
  executes code and bundles no data.
- **File roles:**
  - `SKILL.md` — the always-loaded orchestrator: the numbered styling procedure
    plus the hard invariants (never pie/rainbow, colour via scicolor, PDF vector
    for papers, frameless legend, spines by plot type, no title on paper figures).
    Delegates the full detail to the reference doc.
  - `reference/figure-conventions.md` — the on-demand reference that solely owns
    the method detail: the setup rcParams block, structure/sizing guidance,
    element-level defaults (spines table, grid, legend, ticks, reference lines),
    the scicolor colour policy, severity-ranked anti-patterns, and annotated
    examples. Keep this the single source for that substance; do not
    re-duplicate it in `SKILL.md`.
  - `reference/target.md` — the acceptance spec (see "Instructions vs targets"
    below): items `F1`–`F19`, tiered, each citing its source section in
    `figure-conventions.md`.
- **Provenance:** the public sanitized derivative of the private vault style
  guide (`writing-samples/figures/style-guide.md`), distilled from real analysis
  notebooks and interview. The vault guide stays the canonical source; this skill
  ships the sanitized conventions only.

### `yanglabkit-writing`

Tightens and revises prose to Kaicheng Yang's line-editing standard, and drafts
new prose to the same standard: never add explanation a sentence already
carries, merge redundant sentences, delete padding not content, prefer shorter
linear sentences, one paragraph one theme, arrange paragraphs by linear
dependency, lead each paragraph with its claim, prefer removals. In revision
mode the skill diagnoses by line,
proposes drop-in replacements with rationales, and never applies edits without
approval.

- **Pure markdown guidance, no runtime dependency.** No bundled data, no code
  execution, no worked examples — principles and method only.
- **File roles:**
  - `SKILL.md` — the always-loaded orchestrator: the two modes
    (revision: diagnose → propose → wait; drafting: apply while writing) and
    the two invariants the reference doesn't own (propose-before-apply; match
    the force of the edit to the problem — lighter fix when one suffices,
    aggressive removal/relocation when that's what truly helps). Delegates
    everything else to the reference doc without restating it.
  - `reference/prose-principles.md` — solely owns the eleven tightening
    principles (each with its tell and fix) and the delivery method
    (affirm-before-critique, line-anchored diagnosis, drop-in + rationale,
    recommended-vs-aggressive option, "Net:" bottom line). Do not re-duplicate
    in `SKILL.md`.
  - `reference/target.md` — the acceptance spec (see "Instructions vs targets"
    below): items `W1`–`W11`, numbered 1:1 to the principles, all judged or
    advisory (no mechanical items, by design).
- **Provenance:** the public sanitized distillation of a live manuscript
  revision session; the private vault worklogs and handoff notes remain the
  canonical source (with the original worked before/after evidence). This skill
  ships the sanitized principles only — no manuscript text.

### `yanglabkit-goalrun`

The automated-mode runner: drives any domain skill to its acceptance target
without a human in the loop, on explicit opt-in only (a Claude Code `/goal`
run or a direct user request). Does the work with the domain skill's method,
iterates until every `[mechanical]` and `[judged]` target item passes (or is
`n/a` with reason), and writes `<artifact-stem>.target-report.md` next to the
output as the decidable done-state for a goal evaluator. Owns the per-skill
carve-outs (writing: apply-and-iterate but leave all edits uncommitted for one
accumulated-diff review). Domain skills stay purely interactive; a new skill
becomes automatable by adding only its `reference/target.md`.

- **Pure markdown guidance, no runtime dependency, no bundled data.**
- **File roles:** `SKILL.md` only — the runner contract (workflow, goal
  condition template, rules, known-targets table). The per-skill substance it
  consumes lives in each domain skill's `reference/target.md`.

## Instructions vs targets (skill authoring)

Skills separate **instructions** (how to work — the method, only meaningful
with a human in the loop) from a **target** (what must be true of the finished
artifact — mode-independent). Layout per skill:

```
skills/<name>/
  SKILL.md              # orchestrator: interactive workflow + Automated mode
  reference/<method>.md # instructions: conventions, principles, delivery
  reference/target.md   # acceptance spec: the tiered checklist
```

**Target items** are structured markdown list items:
`id [tier] check → source ref` — stable per-skill id prefix (`F` figures,
`W` writing, `C` scicolor), one tier tag, and a back-reference to the method
doc section or principle that motivates the item.

**Tiers** (decidability, not importance):
- `[mechanical]` — checkable from code or a trivial look at the output;
  automated runs enforce, failures block.
- `[judged]` — needs LLM/human inspection and a judgment call; automated runs
  must pass each with one line of evidence, failures block.
- `[advisory]` — judgment proxy that cannot be pass/failed honestly; reported,
  **never blocks**. This is the anti-Goodhart guarantee — do not add a config
  that lets advisory items block.

**Automated mode** is owned by a single runner skill, `yanglabkit-goalrun` —
domain skills stay purely interactive and carry only a pointer section. The
runner activates on explicit opt-in only (a `/goal` run or the user asking),
does the work with the domain skill's method, iterates against the target,
and writes `<artifact-stem>.target-report.md` next to the output — item id →
pass/fail/n/a → one-line evidence. A goal condition should test the report,
not the artifact's quality directly ("report exists, no failing
mechanical/judged items") — judgment stays with the strong model doing the
work; the goal evaluator only needs decidable state. Skills whose interactive
contract is propose-before-apply (writing) relax it in automated mode to
apply-and-iterate but must leave all edits **uncommitted** for one
accumulated-diff review.

**Anti-drift rule:** the target is derived from the method doc; every item
cites its source. When editing a convention or principle, update both files in
the same commit, and never re-duplicate item text between them.

**Rollout status:** all three domain skills have `reference/target.md`
(figures F1–F19, writing W1–W11, scicolor C1–C10); `yanglabkit-goalrun`
consumes them. A new skill becomes automatable by adding only its target.

## Evaluation tasks

`tasks/` contains versioned, agent-neutral packages for exercising and
comparing YangLabKit skills under controlled conditions. Tasks are not new
skills: they link to the canonical guidance in `skills/` and add a concrete
objective, fixed inputs, output requirements, validation, and a human review
rubric.

Read [`tasks/README.md`](tasks/README.md) before adding or running a task. Every
new task must also be added to its task index.

### Public-data figure comparison

`tasks/public-data-figure-comparison/` is the first included task. It gives
different coding agents identical plot-ready public-data snapshots and asks each
to produce the same six scientific figure types using `yanglabkit-figures` and
`yanglabkit-scicolor`. Kaicheng will compare the candidates later and promote
only selected PNGs into the public README.

The package owns these roles:

- `README.md` — human-readable, vendor- and programming-language-neutral brief;
- `task.json` — versioned six-figure input/output contract;
- `data/` — small derived CSV snapshots plus authoritative provenance,
  transformations, reuse terms, row counts, and SHA-256 checksums;
- `pyproject.toml` + `uv.lock` — shared Python 3.12 plotting/tool environment;
- `submission-template/` — required PNG, source, notes, alt-text, palette, and
  hidden generator-metadata structure;
- `validate_submission.py` — standard-library structural validator;
- `build_comparison.py` — blinded HTML matrix builder with a separate identity
  key;
- `build_showcase.py` — per-submission annotated showcase images (identity-
  revealing; for sharing after blinded scoring); and
- `RUBRIC.md` — per-figure scoring and final collection-coherence review.

Rules when working with evaluation tasks:

1. **Task-specific contracts may override a general skill default.** For
   example, the public-data task requires 300 DPI PNG because its candidates are
   for a web README, even though `yanglabkit-figures` correctly prefers PDF for
   paper figures. Its `task.json` deliberately avoids prescribed visual styles:
   agents must determine visual design by applying the installed figure and
   colour skills while showing all required figure elements.
2. **Do not silently refresh fixed inputs.** Candidate runs use the committed
   files without network access. Any regeneration requires provenance review,
   checksum updates, and a task-version bump because upstream products can
   change.
3. **Use the locked Python environment.** From the task directory, run
   `uv sync --frozen`, then execute Python generation and task utilities with
   `uv run --frozen python ...`. Do not edit `pyproject.toml` or `uv.lock` during
   an individual candidate run.
4. **Keep candidate work isolated and attributable.** Generation code and
   outputs belong under `submissions/<agent-harness>_<model>_<run-id>/`, never
   in the immutable task root or canonical `skills/` directories. The directory
   name and `submission_id` must identify the agent harness and model; the
   comparison builder is responsible for replacing them with blinded slot paths
   during review.
5. **Never inspect competing submissions during a candidate run.** The agent may
   use the task, fixed inputs, linked skills, repository instructions, and its
   own submission directory only. Do not list, search, open, read, diff, copy,
   execute, or summarize sibling submissions; inspect `_comparison/` or its
   identity key; or retrieve prior candidates from git history, remote branches,
   caches, or another copy. Prefer a clean worktree with prior candidates and
   comparison artifacts absent. Record accidental exposure in the run's
   `NOTES.md` so the evaluator can judge comparability.
6. **Retain complete audit metadata.** A submission includes source code,
   `NOTES.md`, alt text, exact palette names and hex values, and agent/model/run
   identity in `submission.json`.
7. **Validate before comparison.** Only validator-passing submissions enter the
   blinded comparison. Do not inspect the generated identity key until rubric
   scoring is complete.
8. **Do not generate candidates while scaffolding a task.** Task definition,
   candidate generation, human selection, and README promotion are distinct
   stages.
9. **Keep task instructions portable.** Do not require Claude Code commands,
   Codex tools, hidden prompts, or another vendor-specific runtime unless the
   task explicitly exists to evaluate that runtime.

## Skill data provenance & regeneration

Both scicolor palette data files derive from the lab's
[scicolor](https://github.com/yang3kc/scicolor) repo. There is **no Python
dependency at runtime** — extraction is a build-time step whose committed JSON
output is all the skill reads.

- **Discrete (`colors.json`):** copy verbatim from scicolor's
  `colorpicker/public/colors/colors.json`. Do not re-curate by hand.
- **Continuous (`continuous-colormaps.json`):** regenerate with the repo-level
  build script (requires Python + matplotlib + scicolor **at build time only**):
  ```bash
  cd <path-to>/scicolor
  uv run python <path-to>/yanglabkit/scripts/extract_continuous_colormaps.py
  ```
  It iterates every `cm_type == "continuous"` colormap in scicolor's
  `color_info_list` and downsamples each to 32 evenly-spaced hex stops. Keep this
  script in `scripts/` (outside `skills/`) so skill users never load it.

Full-resolution continuous colormap *objects* live in the `scicolor` pip package
via `scicolor.get_cmap(name)`; the 32-stop snapshots are for recommendation.

## Plugin & marketplace mechanics

- `marketplace.json` — required `name` (kebab-case), `owner.name`, `plugins[]`.
  The single plugin entry uses `source: "./"` and lists its skills explicitly:
  `"skills": ["./skills/yanglabkit-scicolor"]`. When multiple plugin entries
  share the root `skills/` folder, each must list its own subdirectories.
- `plugin.json` — declares the plugin and **pins its `version`**. With the
  default `strict: true`, `plugin.json` is the authority and the marketplace
  entry supplements it (e.g. the `skills` paths); both merge.
- Validate before pushing: `claude plugin validate .` (checks marketplace schema
  and each local-path entry's `plugin.json`).

## Versioning & releases

Version resolution order: `plugin.json` `version` → marketplace entry `version` →
git commit SHA. This repo pins the version in **`plugin.json` only** (recommended
single source of truth — if you also set it in the marketplace entry,
`plugin.json` silently wins).

**Rules when cutting a release:**
1. **Bump `version` in `plugin.json`.** Because the version is pinned, pushing
   new commits to `main` without bumping delivers **no** update to existing users
   (Claude Code sees the same version and keeps the cache). Updates are
   tag-gated.
2. Cut a matching GitHub release/tag (e.g. `vX.Y.Z`) whose commit actually
   contains that `plugin.json` version, so the tag and manifest agree.
3. Optionally sync `metadata.version` in `marketplace.json` (marketplace-manifest
   version; distinct from the plugin version).

## Distribution

`/plugin marketplace add YangKCLab/yanglabkit` resolves to the **default branch
(`main`)**. A skill is only distributable once it is on `main` — merge feature
branches before announcing. Install:

```
/plugin marketplace add YangKCLab/yanglabkit
/plugin install yanglabkit@yanglabkit
```

See `README.md` for clone-based and `skills`-CLI install alternatives.

## Local skill installations

The canonical, tracked skill sources are always `skills/<name>/`. Local agent
installers may create copies or symlinks under `.agents/skills/` and
`.claude/skills/`, plus a root `skills-lock.json`. These paths are intentionally
gitignored to prevent duplicate skill content from entering commits. Do not edit
an installed copy as the source of truth; make changes in `skills/` and
reinstall or refresh the local copy as needed.

## Conventions

- Keep `SKILL.md` lean and delegate substance to `reference/` docs; avoid
  duplicating the same guidance across both.
- Never hand-transcribe colormaps or re-curate palettes — reuse scicolor's data
  and the build script.
- Ground the selection logic and guardrails in the Crameri (2020) paper.
- Keep task definitions agent-neutral, version fixed inputs, and separate
  candidate submissions from immutable task materials.
