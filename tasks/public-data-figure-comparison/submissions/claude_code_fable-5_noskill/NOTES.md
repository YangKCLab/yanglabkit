# Submission notes

- Implementation: A single Python script, `source/make_figures.py`, generates
  all six figures with matplotlib and pandas from the committed CSVs in
  `data/`. This is a **no-skill baseline run**: the `yanglabkit-figures` and
  `yanglabkit-scicolor` skill documents (and every other styling skill
  available in the harness) were deliberately not read or applied. All design
  decisions — Okabe–Ito colorblind-safe categorical colors, the RdBu_r
  diverging map for the correlation matrix, minimal spines, light grids,
  frameless legends, direct bar labels, and jittered point overlays — are the
  model's own defaults.
- Dependencies and versions: The locked task environment from `uv.lock`
  (Python 3.12.9, matplotlib 3.11.0, numpy 2.5.1, pandas 3.0.3; seaborn 0.13.2
  is installed but unused). No non-Python runtime dependencies.
- Determinism/reproduction notes: From `tasks/public-data-figure-comparison/`,
  run `uv sync --frozen` and then
  `uv run --frozen python submissions/claude_code_fable-5_noskill/source/make_figures.py`.
  The only stochastic element (box-plot point jitter) uses a fixed seed
  (`numpy.random.default_rng(42)`), so output is reproducible.
- Independence statement: No competing submission, `_comparison/` output, or
  identity key was listed, opened, or otherwise accessed during this run; the
  `submissions/` directory was never enumerated.
- Known limitations: In the earthquake histogram, the sparse tail bins above
  magnitude 7.7 hold single events (about 0.05% each) and are barely visible
  at the linear percentage scale, though they are plotted. The longest World
  Bank region name is wrapped onto two lines to preserve figure width.
