# Submission notes

- **Implementation:** A single Python script,
  `source/generate_figures.py`, reads the six committed CSVs from `../../data/`
  and writes six 300 DPI PNGs to `figures/`. Uses matplotlib (with pandas/NumPy);
  seaborn is available but not required. Each figure follows the plot type,
  variable mapping, ordering, and required elements in `task.json`:
  - GISTEMP: three rolling-anomaly lines, zero reference line, legend, °C axis.
  - World Bank: horizontal bars in supplied ascending order (smallest at bottom),
    each bar directly labeled, percent-of-population x-axis fixed to 0–100.
  - Palmer Penguins: one box per species (Adelie, Chinstrap, Gentoo) with all
    observations overlaid as jittered points, grams axis.
  - Wine: full correlation matrix in supplied row/column order on a diverging
    −1…1 scale centered at zero, with a labeled colour bar.
  - Auto MPG: weight-vs-MPG scatter grouped by origin (USA, Europe, Japan),
    legend, no trend line.
  - USGS: 0.1-magnitude bins from 5.0 covering the observed maximum, normalized
    to percentage of all events.

- **Control condition (no-skill):** This is the "noskill" baseline. The
  `yanglabkit-figures` and `yanglabkit-scicolor` guidance documents were **not**
  read or applied. Styling and colour choices are ordinary competent matplotlib
  defaults (tab10 for categorical series, single hues for single-series charts,
  RdBu_r for the diverging correlation heatmap). Palette names/hex recorded in
  `submission.json` are the matplotlib/seaborn defaults actually used, not
  scicolor palettes.

- **Dependencies and versions:** Uses the locked task environment
  (`uv.lock`): matplotlib, numpy, pandas, seaborn 0.13.2 on Python 3.12.
  No non-Python runtime dependencies. A newer matplotlib required
  `boxplot(tick_labels=...)` in place of the deprecated `labels=`.

- **Determinism/reproduction:** Point jitter in the penguin plot uses a fixed
  seed (`numpy.random.default_rng(0)`), so output is deterministic. Reproduce
  from `tasks/public-data-figure-comparison/`:

  ```bash
  uv sync --frozen
  uv run --frozen python \
    submissions/claude_code_opus-4-8_noskill/source/generate_figures.py
  ```

- **Independence statement:** No competing submission or comparison output was
  accessed. No sibling directory under `submissions/`, no `_comparison/`
  artifact, and no prior candidate from git history was listed, read, or used.
  Only the task files, fixed inputs in `data/`, repository instructions, and this
  submission's own directory were used.

- **Known limitations:** These are visual demonstrations, not analyses; no
  causal or inferential claims are made. As a no-skill control, the figures do
  not apply the lab's figure conventions (spine treatment, frameless legends,
  colourblind-safe palette selection, vector export), and the task's own 300 DPI
  PNG requirement is met instead of the skill's paper-figure PDF default.
