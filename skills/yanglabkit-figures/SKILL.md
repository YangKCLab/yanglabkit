---
name: yanglabkit-figures
user_invocable: true
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

This skill is pure markdown guidance: it reads one bundled reference doc and
applies its conventions to the plotting code you write. **No code execution and
no runtime dependency.**

## When to Use

- Writing or editing matplotlib/seaborn plotting code.
- Styling a scientific figure or chart for a paper or slides.
- Exporting a figure (which format, which settings) for print vs. web/slides.
- Questions like "how should this plot look", "make this figure paper-ready",
  "what figsize / spines / legend / export settings should I use".

## Workflow

Work through `reference/figure-conventions.md`, which holds the full detail: the
setup block, element-level defaults, the spines-by-plot-type table, the scicolor
colour policy, severity-ranked anti-patterns, annotated examples, and the
revision checklist. This is the procedure:

1. **Apply the setup block.** Paste the canonical rcParams block (base font 14,
   `axes.axisbelow=True`); leave `font.family` at matplotlib's default.
2. **Pick structure.** Choose a paper-scale `figsize`; single plot → imperative
   pyplot, multi-panel → object-oriented `subplots` with lowercase `(a)(b)(c)`
   panel labels.
3. **Set element defaults per plot type.** Drop spines per the table (line/scatter:
   top+right off; horizontal bar / heatmap: all off), add a subtle dashed grid on
   the value axis behind the data, frameless legend, percentage tick formatter,
   gray dashed reference lines for meaningful thresholds.
4. **Colour via `yanglabkit-scicolor`.** Defer every colour/colormap choice to the
   sibling skill — no matplotlib defaults, no ad-hoc hexes.
5. **Export.** Vector PDF for papers (no dpi); PNG @ dpi=300 `bbox_inches='tight'`
   only for slides/web.
6. **Run the revision checklist** in the reference before the figure ships.

## Rules

- **Never pie charts.** Humans read angle/area poorly — use a bar chart (or a
  stacked bar for parts-of-a-whole).
- **Never rainbow / `jet` / `hsv`.** Perceptually broken; scicolor exists for this.
- **Colour via scicolor.** Route every colour and colormap choice through
  `yanglabkit-scicolor`; retire matplotlib defaults and ad-hoc hexes.
- **PDF vector for papers.** Export `.pdf` for the paper (no dpi); raster only for
  slides/web.
- **Frameless legend.** `frameon=False` always — never a boxed legend.
- **Spines by plot type.** Line/scatter drop top+right; horizontal bar and heatmap
  drop all four.
- **No title on paper figures.** The LaTeX caption does that job; titles are only
  for slides / standalone figures.

## Cross-skill

Defer **all** colour choices — categorical palettes, continuous/heatmap colormaps,
greyscale-safety — to the sibling `yanglabkit-scicolor` skill.
