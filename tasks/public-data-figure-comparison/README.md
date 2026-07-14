# Public-data figure comparison task

This is a versioned, agent-neutral task for comparing how different coding
agents apply YangLabKit's scientific-figure and scientific-colour guidance.
Every participant receives the same plot-ready data and output contract. The
task does not assume Claude Code, Codex, a particular prompt format, or a
specific programming language.

## Objective

Create one polished PNG for each of six figure types:

1. NASA GISTEMP zonal-anomaly line chart;
2. World Bank regional-urbanization horizontal bar chart;
3. Palmer Penguins body-mass box plot with jittered observations;
4. UCI red-wine correlation heatmap;
5. UCI Auto MPG weight-versus-economy scatter plot; and
6. USGS 2025 earthquake-magnitude percentage histogram.

The figures are visual demonstrations, not substantive scientific analyses.
Do not add causal or inferential claims.

## Normative guidance

Read and apply these repository-local documents before writing plotting code:

- [`yanglabkit-figures`](../../skills/yanglabkit-figures/SKILL.md) and its
  [full conventions](../../skills/yanglabkit-figures/reference/figure-conventions.md);
- [`yanglabkit-scicolor`](../../skills/yanglabkit-scicolor/SKILL.md) and its
  [selection guide](../../skills/yanglabkit-scicolor/reference/selection-guide.md).

The task-specific contract below overrides a general skill default when they
differ. In particular, these are web-gallery candidates, so PNG is required
even though the figure skill correctly prefers vector PDF for papers.

## Fixed inputs

Use only the committed files in [`data/`](data/). They are small, derived,
plot-ready snapshots made from the authoritative public sources documented in
[`data/README.md`](data/README.md). Do not fetch fresher values or substitute a
similar dataset: identical inputs are essential for comparison.

The exact plot requirements and filenames are machine-readable in
[`task.json`](task.json). The essential transformations have already been
frozen into the inputs where doing so removes avoidable analytical variation:

- the GISTEMP series already contain centered five-year rolling means;
- the World Bank regions are already sorted by the 2024 value;
- missing penguin body masses are already removed;
- the wine input is the fixed Pearson correlation matrix;
- Auto MPG origin codes are already mapped to labels; and
- the USGS input is the reviewed 2025 M≥5 event snapshot.

## Shared figure contract

- Produce exactly the six PNG filenames listed in `task.json`.
- Use a six-inch source width and plot-appropriate height. Save at 300 dpi with
  a white background and a tight bounding box.
- Use DejaVu Sans and no more than two font sizes. Start from 14 pt ordinary
  text and 12 pt only for a smaller legend or annotation.
- Do not put a title inside the figure. The eventual README caption supplies it.
- Keep labels concise and in sentence case, put units in parentheses, and keep
  all text readable when displayed about 3.5 inches wide.
- Apply the figure-type-specific spines, ticks, grids, legends, direct labels,
  markers, and reference lines from `yanglabkit-figures`.
- Choose every colour through `yanglabkit-scicolor`. Record the palette class,
  exact palette name, and actual hexadecimal colours in `submission.json`.
- Use redundant line styles or marker shapes for multiple series or groups.
- Use a deterministic jitter seed of `20260713` for the penguin observations.
- Do not redistribute additional upstream data inside a submission.

## Submission layout

Copy [`submission-template/`](submission-template/) to
`submissions/<agent-harness>_<model>_<run-id>/`, then replace its placeholders:

```text
submissions/<agent-harness>_<model>_<run-id>/
├── submission.json
├── NOTES.md
├── figures/
│   ├── gistemp-zonal-lines.png
│   ├── world-bank-urbanization-bars.png
│   ├── palmer-penguins-box.png
│   ├── wine-correlation-heatmap.png
│   ├── auto-mpg-scatter.png
│   └── usgs-earthquake-histogram.png
└── source/
    └── <the code used to generate all six figures>
```

The submission directory name and matching `submission_id` must identify the
agent harness and model used. Use a file-safe form such as
`<agent-harness>_<model>_<run-id>`; for example,
`codex_gpt-5_20260713-01` or `claude-code_claude-opus-4_20260713-01`. The run ID
distinguishes repeated attempts with the same harness/model pair. Record the
full harness, model, provider, date, and run reference in `submission.json`.
The comparison builder copies images to anonymous slot paths, so descriptive
submission names do not reveal generator identity during scoring.

`NOTES.md` should briefly identify implementation choices, dependencies, and
any limitation. It must not contain a self-evaluation or instructions to the
reviewer.

## Validate and compare

From the repository root:

```bash
python tasks/public-data-figure-comparison/validate_submission.py \
  tasks/public-data-figure-comparison/submissions/<agent-harness>_<model>_<run-id>

python tasks/public-data-figure-comparison/build_comparison.py
```

The comparison builder scans validator-passing submission layouts and writes a
local `_comparison/index.html` plus a separate identity key. Review candidates
with [`RUBRIC.md`](RUBRIC.md); do not inspect the identity key until scoring is
complete.

## What is not part of this task

- editing the repository's public README;
- selecting winners or claiming that one agent is generally better;
- fetching or revising data;
- producing PDF/SVG versions;
- a tutorial, notebook collection, or scientific analysis; or
- changing either YangLabKit skill to suit a submission.
