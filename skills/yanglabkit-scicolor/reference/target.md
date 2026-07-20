# yanglabkit-scicolor — Target

The acceptance spec for a colour recommendation and, where one is applied, its
use in a figure. Section references point to `selection-guide.md`; "rules"
refers to the Rules block in `SKILL.md`.

Tier semantics: `[mechanical]` — checkable from the returned hexes, the
bundled data files' metadata, or a trivial look; `[judged]` — needs inspection
and a judgment call; `[advisory]` — reported, never blocking.

## Items

- C1 `[judged]` Palette class matches the data structure per the decision flow
  (categorical / sequential / diverging / multi-sequential)? → §1–§2
- C2 `[mechanical]` Actual hex codes returned — with palette name and source
  collection — and resolvable in the bundled data files? → rules
- C3 `[mechanical]` No rainbow, jet, HSV, or Turbo? → §5.3
- C4 `[mechanical]` No red–green pair at similar lightness in a categorical
  scheme? → §5.2
- C5 `[mechanical]` Continuous choice carries `perceptually_uniform: true`
  metadata (or is a documented scientifically derived map)? → §5.1, §5.4
- C6 `[judged]` Lightness monotonic enough that the figure survives greyscale
  printing and CVD? → §5 caveats
- C7 `[mechanical]` Colour bar present for any continuous map, when applied in
  a figure? → §5 caveats
- C8 `[judged]` Colormap spans the data range without stretching or squeezing?
  → §5 caveats
- C9 `[advisory]` Heatmap tiles separated (gridlines/spacing) where colour
  bleed could shift perceived value? → §5 caveats
- C10 `[mechanical]` Colourblind-safe choice, unless the user explicitly opted
  out? → rules

## Target report (automated mode)

For standalone palette work, write `<artifact-stem>.target-report.md` per the
`yanglabkit-goalrun` contract (`id pass|fail|n/a — one-line evidence`). When
the palette is consumed inside a figure run, the figure's report covers these
items via F6 — no separate report needed. Done = every `[mechanical]` and
`[judged]` item `pass` or `n/a` with reason; C9 is reported, never blocking.
