# Submission notes

- Implementation: One deterministic Python script generates all six figures from the committed CSV snapshots. Styling follows `yanglabkit-figures`; categorical, sequential, and diverging colours are read directly from the bundled `yanglabkit-scicolor` JSON data at runtime.
- Dependencies and versions: Python 3.12 in the frozen uv environment; matplotlib 3.11.0, NumPy 2.5.1, pandas 3.0.3, and seaborn 0.13.2 from `uv.lock`. There are no non-Python runtime dependencies.
- Determinism/reproduction notes: From `tasks/public-data-figure-comparison/`, run `uv sync --frozen`, then `uv run --frozen python submissions/codex_gpt-5-6-sol_yanglabkit/source/generate_figures.py`.
- Independence statement: No competing submission, prior candidate, comparison output, or identity key was listed, opened, searched, executed, or otherwise accessed during this run.
- Known limitations: The dense heatmap uses wrapped full variable labels and omits cell-value annotations to preserve legibility at gallery width.
