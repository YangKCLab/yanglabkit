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
scripts/               # build-time-only scripts (NOT loaded as skills)
README.md              # user-facing install + skill list
```

The whole repo is a single plugin: the marketplace entry uses `source: "./"`, so
the plugin root is the repo root. On install, the entire repo (including
`README.md`, `scripts/`, etc.) is copied into the plugin cache, but only
`skills/<name>/` directories load as skills.

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
    the full detail: the setup rcParams block, structure/sizing guidance,
    element-level defaults (spines table, grid, legend, ticks, reference lines),
    the scicolor colour policy, severity-ranked anti-patterns, annotated
    examples, and the 10-item revision checklist. Keep this the single source for
    that substance; do not re-duplicate it in `SKILL.md`.
- **Provenance:** the public sanitized derivative of the private vault style
  guide (`writing-samples/figures/style-guide.md`), distilled from real analysis
  notebooks and interview. The vault guide stays the canonical source; this skill
  ships the sanitized conventions only.

## Data provenance & regeneration

Both data files derive from the lab's [scicolor](https://github.com/yang3kc/scicolor)
repo. There is **no Python dependency at runtime** — extraction is a build-time
step whose committed JSON output is all the skill reads.

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

## Conventions

- Keep `SKILL.md` lean and delegate substance to `reference/` docs; avoid
  duplicating the same guidance across both.
- Never hand-transcribe colormaps or re-curate palettes — reuse scicolor's data
  and the build script.
- Ground the selection logic and guardrails in the Crameri (2020) paper.
