# yanglabkit-figures — Target

The acceptance spec for a finished scientific figure. Mode-independent: an
interactive session runs it as the final revision checklist; an automated run
treats it as the definition of done (see "Automated mode" in `SKILL.md`).

Item format: `id [tier] check → source section`, where sections refer to
`figure-conventions.md`. Tier semantics:

- `[mechanical]` — checkable from the plotting code or a trivial look at the
  output. Automated runs must pass every one.
- `[judged]` — needs inspection of the rendered figure and a judgment call.
  Automated runs must pass every one, each with one line of evidence.
- `[advisory]` — a quality signal. Reported, never blocking.

## Items

- F1 `[mechanical]` Exported as vector PDF for the paper (no dpi arg); raster
  (PNG, `dpi=300`, `bbox_inches='tight'`) only for slides/web? → §3
- F2 `[mechanical]` Spines match the plot type, and tick marks survive only
  where their spine does — no orphaned ticks? (line/scatter: left+bottom;
  horizontal bar: bottom value spine + x ticks only; heatmap: none) → §3
- F3 `[mechanical]` Grid dashed, `alpha ≤ 0.3`, on the value axis, drawn behind
  the data? → §3
- F4 `[mechanical]` Legend `frameon=False`? → §3
- F5 `[mechanical]` Proportions shown as percentages (`PercentFormatter`), not
  raw fractions? → §3
- F6 `[mechanical]` Every colour and colormap from scicolor — no
  rainbow/jet/HSV/Turbo, no matplotlib defaults, no ad-hoc hexes? → §4
- F7 `[mechanical]` Same variable = same colour in every panel? → §4
- F8 `[mechanical]` Multiple series on one axes distinguished by more than
  colour (marker for scatter, linestyle for lines, hatch for bars)? → §4
- F9 `[mechanical]` Multi-panel figures labelled `(a)(b)(c)` upper-left; no
  in-figure title on a paper figure? → §2, §3
- F10 `[mechanical]` `tight_layout()` (or constrained layout) applied? → §3
- F11 `[mechanical]` No more than two distinct font sizes? → §1
- F12 `[mechanical]` Labels sentence-case with units in parentheses; decimals
  carry a leading zero; maths/Greek via LaTeX/mathtext? → §3
- F13 `[mechanical]` Figure sized for its target column (single-column
  default), at final print width? → §2
- F14 `[judged]` Nothing clipped — a tick above the data max leaves headroom so
  the top gridline and marks render fully? → §3
- F15 `[judged]` Legend placed clear of the data? → §3
- F16 `[judged]` Effective on-page font lands at ~6–9 pt at print size? → §2
- F17 `[judged]` Titles and axis labels fit the figure width (wrapped, not
  overrunning the axes)? → §3
- F18 `[judged]` Readable at single-column width? → §2
- F19 `[advisory]` Reads as minimal and print-first — nothing on the canvas
  that doesn't encode or label data? → §1

## Target report (automated mode)

Write `<figure-stem>.target-report.md` next to the output, one line per item:

```
# Target report — fig1.pdf
- F1 pass — savefig("fig1.pdf"), no dpi arg
- F2 pass — bar chart: top/right/left spines off, bottom kept with x ticks
- …
- F19 pass — advisory: no decorative elements
```

Done = every `[mechanical]` and `[judged]` item is `pass`, each with one line
of evidence. `[advisory]` items are reported either way and never block. If an
item is genuinely inapplicable (e.g. F5 with no proportion axis, F9 for a
single panel), mark it `n/a` with the reason — `n/a` counts as pass.
