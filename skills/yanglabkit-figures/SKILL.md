---
name: yanglabkit-figures
user-invocable: true
disable-model-invocation: false
description: >-
  Style scientific figures the Yang Lab way when writing matplotlib/seaborn
  plotting code. Applies a distilled set of conventions — minimal print-first
  design, spines dropped by plot type, frameless legends, percentage axes, gray
  dashed reference lines, vector PDF export, and colour deferred to scicolor — so
  figures come out paper-ready on the first pass. Refuses pie charts and
  rainbow/jet colormaps. Trigger when the user writes or asks for
  matplotlib/seaborn/plotting code, a scientific figure/chart for a paper or
  slides, or asks how to style/export a figure.
---

# yanglabkit-figures — Scientific figure style

Style matplotlib/seaborn figures to Kaicheng Yang's conventions for scientific
figures, so a plot comes out in-voice on the first pass: minimal and print-first,
spines and grid tuned per plot type, frameless legends, proportions as
percentages, meaningful thresholds as gray dashed lines, and vector PDF export
for papers. Colour decisions defer to the sibling `yanglabkit-scicolor` skill.

This skill is pure markdown guidance: it reads two bundled reference docs —
`reference/figure-conventions.md` (the method) and `reference/target.md` (the
acceptance spec) — and applies their conventions to the plotting code you
write. **No code execution and no runtime dependency.**

## When to Use

- Writing or editing matplotlib/seaborn plotting code.
- Styling a scientific figure or chart for a paper or slides.
- Exporting a figure (which format, which settings) for print vs. web/slides.
- Questions like "how should this plot look", "make this figure paper-ready",
  "what figsize / spines / legend / export settings should I use".

## Workflow

Work through `reference/figure-conventions.md`, which owns the full detail: the
setup rcParams block, structure/sizing guidance, element-level defaults (the
spines-by-plot-type table, grid, legend, ticks, reference lines), the scicolor
colour policy, severity-ranked anti-patterns, and annotated examples. This is
the procedure:

1. **Apply the setup block** from the reference (§3), then pick a paper-scale
   `figsize` and API — single plot → imperative pyplot, multi-panel →
   object-oriented `subplots` with `(a)(b)(c)` panel labels (§2).
2. **Set element defaults for the plot type** — spines, grid, legend, tick
   formatting, and reference lines per §3, keyed off the spines-by-plot-type
   table.
3. **Colour via `yanglabkit-scicolor`.** Defer every colour/colormap choice to the
   sibling skill (§4). When one axes shows multiple series, also encode them
   redundantly (marker/linestyle/hatch) per the redundant-encoding subsection (§4).
4. **Export and revise** — vector PDF for papers, raster only for slides/web
   (§3), then run the target checklist (`reference/target.md`) before the
   figure ships.

## Rules

- **Never pie charts.** Humans read angle/area poorly — use a bar chart (or a
  stacked bar for parts-of-a-whole).
- **Never rainbow / `jet` / `hsv`.** Perceptually broken; scicolor exists for this.
- **Colour via scicolor.** Route every colour and colormap choice through
  `yanglabkit-scicolor`; retire matplotlib defaults and ad-hoc hexes.
- **Encode series redundantly.** When one axes shows multiple series/types, pair
  colour with a distinct marker (scatter), linestyle (line), or hatch (bar) — not
  colour alone — so they survive greyscale and colourblind readers.
- **PDF vector for papers.** Export `.pdf` for the paper (no dpi); raster only for
  slides/web.
- **Frameless legend.** `frameon=False` always — never a boxed legend.
- **Spines & ticks are a matched pair.** Keep a spine wherever its axis has
  meaningful tick marks and drop the spine *with its tick marks* elsewhere — never
  orphan a tick. Line/scatter keep left+bottom (drop top+right); horizontal bar
  keeps only the bottom value spine + its x ticks (drop the other three spines and
  the category tick marks); heatmap drops all four spines and all ticks.
- **No title on paper figures.** The LaTeX caption does that job; titles are only
  for slides / standalone figures.

## Automated mode

Only on explicit opt-in — a `/goal` run or the user asking for an unattended
pass; never self-initiated. Iterate the figure against `reference/target.md`
and write the target report it specifies (`<figure-stem>.target-report.md`,
next to the output). Done = every `[mechanical]` and `[judged]` item passes
with one line of evidence; `[advisory]` items are reported, never blocking.

Goal condition template:

    /goal <figure>.pdf exists and <figure>.target-report.md marks every
    mechanical and judged item of the yanglabkit-figures target pass or n/a

Interactive sessions instead finish by running the target as the step-4
revision checklist.

## Cross-skill

Defer **all** colour choices — categorical palettes, continuous/heatmap colormaps,
greyscale-safety — to the sibling `yanglabkit-scicolor` skill.
