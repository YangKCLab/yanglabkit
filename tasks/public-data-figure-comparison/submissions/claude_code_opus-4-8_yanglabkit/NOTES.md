# Submission notes

- Implementation: A single self-contained script,
  `source/generate_figures.py`, generates all six figures with matplotlib and
  pandas (numpy for binning/jitter). Styling follows the `yanglabkit-figures`
  conventions and every colour is chosen via `yanglabkit-scicolor`:
  - Categorical figures (GISTEMP zones, penguin species, Auto MPG origins) use
    one consistent CVD-safe Okabe-Ito trio (`#0071b2` blue, `#d55e00`
    vermillion, `#009e73` bluish-green) so the collection reads as one family,
    paired with a distinct linestyle (lines) or marker shape (scatter) for
    redundant, greyscale-safe encoding.
  - The two single-series distributions (urbanization bars, earthquake
    histogram) use one Okabe-Ito accent blue; magnitude is carried by bar
    length/height, not by hue.
  - The correlation heatmap uses the perceptually-uniform, CVD-safe diverging
    `vik` map (Scientific colour maps), rebuilt in-script from its 32 hex stops,
    fixed to [-1, 1] centered at 0 with a labeled colour bar.
  - Applied figure conventions: spines/ticks paired by plot type (line/scatter
    keep left+bottom; horizontal bar keeps only the bottom value spine, category
    ticks off; heatmap drops all spines and ticks), subtle dashed grids behind
    the data, frameless legends, `PercentFormatter` on the proportion axes, a
    gray dashed zero-anomaly reference line on the GISTEMP chart, no in-figure
    titles, sentence-case labels with units in parentheses, and two font sizes
    (base 14, legend 10).
  - `scicolor` is not in the locked task environment, so palette hex values are
    hard-coded verbatim from the scicolor bundled data rather than imported at
    runtime; the script has no dependency beyond the locked env.
- Dependencies and versions (from `uv.lock`): Python 3.12.11, matplotlib 3.11.0,
  numpy 2.5.1, pandas 3.0.3, seaborn 0.13.2 (seaborn available but unused). No
  non-Python runtime dependencies.
- Determinism/reproduction notes: The only randomness is the penguin strip-plot
  jitter, seeded with `numpy.random.default_rng(0)`. Reproduce from
  `tasks/public-data-figure-comparison/` with:
  `uv run --frozen python submissions/claude_code_opus-4-8_yanglabkit/source/generate_figures.py`
- Independence statement: No competing submission or comparison output was
  accessed. Only the task files, fixed inputs in `data/`, the two installed
  YangLabKit skills, and this submission's own directory were used. No sibling
  `submissions/` directory, `_comparison/` artifact, or prior candidate from git
  history was listed, read, or otherwise consulted.
- Known limitations: Task contract requires 300 DPI PNG for the web gallery, so
  these are raster rather than the vector PDF the figure skill prefers for paper
  figures. The Auto MPG scatter has dense overplotting at high weight / low mpg;
  marker transparency mitigates but does not eliminate it. Long World Bank region
  names are wrapped across lines to keep the value axis readable.
