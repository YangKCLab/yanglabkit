# Submission notes

- Implementation: One deterministic Python script generates all six figures
  from the committed task CSV files. This run is the intentionally no-skill
  baseline: the YangLabKit figure and colour skill documents were not consulted
  or applied. The fixed mappings and output requirements in `task.json` were
  followed directly.
- Dependencies and versions: Python 3.12 in the task's frozen uv environment;
  matplotlib 3.11.0, NumPy 2.5.1, pandas 3.0.3, and seaborn 0.13.2. There are no
  non-Python runtime dependencies.
- Determinism/reproduction notes: From
  `tasks/public-data-figure-comparison/`, run
  `uv run --frozen python submissions/codex_gpt-5-6-sol_noskill/source/generate_figures.py`.
  The only randomized marks are penguin-point x offsets, generated with the
  fixed seed `20260714`.
- Independence statement: No competing submission, comparison output, identity
  key, prior candidate from history, cache, branch, or external copy was listed,
  searched, opened, read, diffed, copied, executed, or summarized during this
  run.
- Known limitations: As a deliberate baseline condition, palette choices and
  styling are independent selections rather than recommendations produced by
  the two YangLabKit skills evaluated by the task.
