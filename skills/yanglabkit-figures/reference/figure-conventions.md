# Scientific Figure Conventions (Python)

The Yang Lab's conventions for scientific figures in matplotlib/seaborn. Load
this as context when writing plotting code so figures come out in-voice on the
first pass.

Built on the [Parrott 2026 7-section framework](https://www.oneusefulthing.org/p/how-to-build-an-ai-style-guide),
adapted from prose to figures. Colour decisions defer to the
**`yanglabkit-scicolor`** skill / [scicolor](https://github.com/yang3kc/scicolor).

---

## 1. Visual Voice

How the figures should *feel* — five rules:

1. **Minimal, not decorated.** Data ink over chrome. No boxes, no drop shadows,
   no background fills, no 3D. When in doubt, remove an element.
2. **Print-first.** Every figure is destined for a paper column. Design at
   paper scale (small figsizes, ~14pt text as a starting reference — scale down
   for small/dense figures), export vector, assume greyscale might happen.
3. **Quantitatively honest.** Axes start where the data honestly starts;
   proportions are shown as percentages; reference lines mark meaningful
   thresholds (0, chance, a cutoff).
4. **Consistent across a paper.** The same variable is the same colour in every
   panel; the same size hierarchy everywhere; the same marker/linestyle per
   variable across panels; one colormap family per paper.
5. **Legible when shrunk.** If a label is unreadable at single-column width,
   the figure is wrong — not the reader.

---

## 2. Structure

### Figure sizing (`figsize`, inches)
Paper-column scale. Common footprints:

| Shape | figsize | Use |
|---|---|---|
| Square-ish single | `(5, 4.5)`, `(6, 6)` | scatter, single distribution |
| Wide single | `(8, 5)`, `(8, 6)` | bar / time series |
| Tall | `(5, 6)`, `(4.3, 7)` | horizontal bars, ranked lists |
| Multi-panel grid | `(12, 8)`, `(9, 12)` | 2×2 / 3×N panels |

Start small; only widen when labels collide.

**Target the column width — single by default.** Every figure lands in a paper
column. Default to **single-column width (~3.5 in / 9 cm)**; only design for
**two-column width (~7.2 in / 18.4 cm)** when you know the figures are for a
double-column paper. When unsure, assume single-column — a 2×2 grid that only
reads at full text-width is really two figures.

**Size for the final print size, not the screen.** A "14 pt" label is only 14 pt
*on the page* if the figure is placed at the width it was drawn at — don't assume
downstream scaling is free. Two consistent workflows:
- *Draw at final size* — pass the target column width as `figsize` (e.g.
  `(3.5, 2.6)`) and set the font base to true print points (~6–9 pt). What you
  save is what prints.
- *Draw on a larger canvas, let LaTeX scale it down* (the footprints in the table
  above) — the effective on-page font is `base × (column ÷ canvas width)`, so a
  14 pt base on an 8 in canvas lands ~6 pt at single-column. That is *why* the
  base is 14.

Either way, reason backwards from the printed column width and check the
effective font lands **~6–9 pt** on the page.

### Single vs. multi-panel — API choice
- **Single plot → imperative pyplot** (`plt.plot`, `plt.gca()`). Terse, fine for
  one axes.
- **Multi-panel → object-oriented** (`fig, axes = plt.subplots(...)`, then
  `ax.` methods). Scales cleanly, no ambiguity about which axes is current.

### Panel labels (signature move)
Multi-panel figures get lowercase letters in parentheses, upper-left, in axes
coordinates:

```python
plt.text(-0.01, 1.05, f"({'abcdefghi'[index]})", transform=plt.gca().transAxes)
```

- Lowercase `(a) (b) (c)`, parenthesized.
- Positioned just outside the top-left of each axes via `transform=...transAxes`.
- Often combined with a short panel subtitle: `(a) Model name`.

### Titles
- **Paper figures: no in-figure title** — the LaTeX caption does that job.
- **Slides / standalone figures: title is fine**, `plt.title(title, fontsize=14)`.
- Multi-panel always uses `(a)(b)` letters regardless.

### Layout
End every figure with `plt.tight_layout()` (or `fig.tight_layout()`). Tune
padding only when panels crowd: `tight_layout(h_pad=0.15, w_pad=0.1)`.

---

## 3. Element-Level Defaults

### The canonical setup block
Paste at the top of every plotting notebook/script (documented snippet, not a
shipped style file — kept inline on purpose):

```python
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import scicolor

plt.rcParams.update({
    "font.size": 14,        # reference base — adjust per figure, see below
    "axes.axisbelow": True, # grid/gridlines sit BEHIND the data
})
```

Font family is intentionally left at matplotlib's default **DejaVu Sans** — no
`font.family` override, so figures reproduce on any machine with zero font
dependencies.

### Font sizes
**14 is a reference, not a fixed rule.** Start from a base of 14 for
ticks/labels/titles, then adjust it to the figure — shrink the base (e.g. to
11–12) for a small figsize, a dense multi-panel grid, or anywhere 14 would
crowd or overflow. Whatever base you land on, apply it **consistently** to
every tick/label/title in the figure. One further deviation is fine for a
single element that still needs to be smaller for space — most commonly the
**legend** (a few points below the base, e.g. `fontsize=10` against a base of
14) — but cap the figure at **two distinct font sizes total**. Three or more
reads as messy; if another element is still crowded, fix it with layout,
shorter labels, or wrapping (see below) rather than adding a third size.

### Labels — short, and wrapped when long
Axis labels and titles should be **short**. A label that runs wider than the
axes it sits under unbalances the figure and steals space from the data — push
the detail into the caption, not onto the axis.

- Prefer a terse noun phrase (`"Accuracy"`, `"Share of posts"`) over a full
  sentence.
- If a long label is unavoidable, **break it across lines** so each line fits
  within the figure width — never let one line overrun the axes.

```python
plt.xlabel("Share of accounts\nflagged by the classifier")   # manual line break
# or wrap automatically to a width that fits under the axes:
import textwrap
plt.xlabel(textwrap.fill("Share of accounts flagged by the classifier", width=24))
```

### Label & number typography
Small consistency rules that keep text in-voice:
- **Sentence case** for axis labels and titles (`"Share of posts"`, not
  `"Share Of Posts"` or ALL-CAPS).
- **Units in parentheses**, SI where applicable: `"Latency (ms)"`,
  `"Distance (km)"` — not bare or in brackets.
- **Leading zero on decimals** (`0.05`, never `.05`), and a consistent number of
  significant figures across ticks and annotations.
- **LaTeX/mathtext for maths and Greek** — matplotlib renders `$...$` inline, so
  use `r"$\mu$"`, `r"$\alpha$"`, `r"$\pm$"`, `r"$\times$"`, `r"$\rightarrow$"`
  (raw strings), not `u`, `alpha`, `+/-`, `x`, `->` or spelled-out words. Works
  in any label, tick, title, or annotation: `plt.xlabel(r"Rate ($\mu$s$^{-1}$)")`.

### Spines & tick marks — a matched pair, by plot type
**Tick marks and their spine travel together.** Keep a spine wherever its axis
carries meaningful tick marks, and drop the spine *and its tick marks together*
everywhere else. Never orphan a tick mark from a removed spine (a tick floating
with no axis line to sit on), and never keep a spine that carries no ticks. Which
sides survive is then set by the plot type:

| Plot type | Spines + ticks kept | Dropped |
|---|---|---|
| Line / scatter | left + bottom, with their ticks | top + right (tickless already) |
| Horizontal bar / ranked list | bottom value/percent spine + its x ticks | top + left + right, **and the y (category) tick marks** — the category labels stay |
| Heatmap | *none* | all four spines **and** all tick marks (cells are self-labeled) |

```python
# line/scatter — keep left+bottom spines and their ticks, drop top+right:
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# horizontal bar — keep only the bottom value spine + its x ticks; drop the
# other three spines and the category (y) tick marks (labels stay):
for side in ("top", "right", "left"):
    ax.spines[side].set_visible(False)
ax.tick_params(axis="y", length=0)   # y labels stay; tick marks go with the left spine

# heatmap — drop all four spines and all tick marks (cells self-labeled):
for s in ax.spines.values():
    s.set_visible(False)
ax.tick_params(length=0)
```

### Grid
Subtle, dashed, single-axis, behind the data (`axisbelow=True` handles the last):

```python
plt.grid(True, axis="y", alpha=0.2, linestyle="--")   # vertical bars / lines
plt.grid(True, axis="x", alpha=0.3, linestyle="--")   # horizontal bars
```
- `alpha` in `0.1–0.3`. Grid on the axis the eye reads values along.
- **Cover the data max with a tick, then leave headroom past it.** Make sure the
  value axis has a tick (and its gridline) at or above the tallest bar/point so
  the max is readable — if data peaks at 56 but ticks stop at 50, add a tick at
  60. Then set the limit a hair *above* the top tick so that gridline/tick isn't
  clipped where it would coincide with the axes edge:
  ```python
  ax.set_yticks([0, 20, 40, 60])   # tick above the data max (56)
  ax.set_ylim(0, 62)               # headroom so the 60 gridline isn't clipped
  ```
  Keep the headroom small (a few percent) so it doesn't distort the comparison.

### Legend
Always frameless, tight, small:

```python
plt.legend(frameon=False, fontsize=10, labelspacing=0.2, loc="upper right")
```
- `frameon=False` **always**. Never a boxed legend.
- Tight `labelspacing` (`0.1–0.2`). Place where it doesn't cover data.

### Tick formatting
Proportions are **percentages**, not raw fractions. Use
`matplotlib.ticker.PercentFormatter` on whichever axis carries the proportion:

```python
import matplotlib.ticker as mtick

# xmax:     the value that corresponds to 100% (1 for [0,1] data, 100 if already scaled)
# decimals: number of decimal places after the point — choose to fit the data
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=100, decimals=0))
```
- `xmax=1` when data is in `[0,1]`; `xmax=100` when already scaled to `[0,100]`.
- **Choose `decimals` to suit the data**, don't just default it: `0` for
  whole-percent ticks, `1`/`2` only when the values genuinely need that
  precision to be distinguishable. Prefer the fewest places that keep the ticks
  meaningful — trailing zeros are noise.
- Swap `yaxis`↔`xaxis` for the axis the proportion sits on (percent on `x` for
  horizontal bars, on `y` for vertical bars / lines).

Rotate crowded categorical labels 30–50°, right-aligned:

```python
plt.xticks(rotation=35, ha="right")
```

### Reference lines
Meaningful thresholds as **gray dashed** lines:

```python
plt.axvline(0, color="gray", linestyle="--", alpha=0.8, linewidth=2)
```
Used for zero (bias), chance level, or a decision cutoff.

---

## 4. Colour

**All colour decisions route through scicolor / the `yanglabkit-scicolor` skill.**
Retire the legacy mix of matplotlib `tab10`/`tab20` defaults, ad-hoc Nord hexes,
and grays.

- **Continuous / heatmap:** scicolor perceptually-uniform maps. Established
  choices: `acton`, `batlow`.
  ```python
  cmap = scicolor.get_cmap("batlow")
  sns.heatmap(df, annot=annot, fmt="", cmap=scicolor.get_cmap("acton"))
  ```
- **Categorical:** pull a colourblind-safe categorical palette from scicolor
  rather than relying on matplotlib defaults. Ask `yanglabkit-scicolor` for the
  palette when in doubt.
- **Same variable → same colour** across every panel of a paper.
- **Greyscale-safe:** assume a reader may print in B&W; prefer palettes that
  survive it, or lean on ordering/position not just hue.

### Redundant encoding (don't rely on colour alone)
When more than one series/type shares an axes, pair each colour with a distinct
**second channel** so the series survive greyscale printing, colourblind readers,
and shrinking to single-column width. **Marker shape and line style are the
default channels** — reach for them first:

```python
# scatter: cycle marker over a distinct-shape sequence
markers = ["o", "s", "^", "D", "v"]
for i, (x, y, label) in enumerate(series):
    plt.scatter(x, y, marker=markers[i], label=label)   # colour set by scicolor palette

# line: cycle linestyle over dashed patterns
linestyles = ["-", "--", "-.", ":"]
for i, (x, y, label) in enumerate(series):
    plt.plot(x, y, linestyle=linestyles[i], marker=markers[i], label=label)
```

**Marker size — small and print-scale (~5–8 pt).** Keep symbols to simple solid
or open shapes at print size: `markersize=6` for line markers, `s≈30–60` for
`scatter` (its `s` is *area* in pt², so ~5–8 pt across). Oversized markers eat
data ink and blur when the figure shrinks to a column.

**Bar hatches — optional, use sparingly.** Grouped bars *can* take a `hatch`
(`["", "//", "..", "xx"]`) for the same reason, but hatches read as busy/noisy in
print, so prefer position + colour for bars and reach for hatch only when
greyscale distinguishability is genuinely essential:

```python
hatches = ["", "//", "..", "xx"]
for i, (bar, h) in enumerate(zip(bars, hatches)):
    bar.set_hatch(h)
```

The legend automatically carries the marker/linestyle (and hatch) alongside the
colour, so the redundant channel shows up there too — no extra work.

Consistent with the "same variable → same colour across panels" rule: a variable
should keep the **same marker/linestyle** across every panel too, not just the
same colour.

---

## 5. Anti-Patterns

What figures must **never** do.

- 🔴 **Kill on sight**
  - **Pie charts** — never. Humans read angle/area poorly; use a bar chart (or a
    stacked bar for parts-of-a-whole) instead.
  - Rainbow / `jet` / `hsv` colormaps (perceptually broken — scicolor exists for
    this reason).
  - Boxed legends (`frameon=True`), legend backgrounds.
  - In-figure titles on paper figures (that's the caption's job).
  - Raster export for a paper (`.png` where `.pdf` belongs) — vectors don't
    pixelate.
  - Setting a non-default `font.family` that won't exist on another machine.
- 🟡 **Rewrite**
  - Heavy solid gridlines — should be dashed, `alpha ≤ 0.3`, behind data.
  - Keeping all four spines on a line/scatter plot.
  - Tick marks orphaned from a removed spine (a tick floating with no axis line),
    or a spine kept with no ticks — keep spine + ticks together, drop them
    together (`tick_params(length=0)` on the side whose spine you dropped).
  - Raw fractions on an axis where a `PercentFormatter` reads better.
  - Truncated y-axis that visually exaggerates a difference (be honest).
  - Elaborate per-element font sizing when one consistent base would do.
  - More than two distinct font sizes in one figure — pick the one element that
    genuinely needs a deviation (usually the legend) and hold everything else at
    base size.
  - A title or axis label so long it overruns the axes width on one line —
    shorten it, or break it across lines so it aligns with the figure.
  - Multiple series distinguished by **colour alone** — add a shape/linestyle
    (hatch for bars, sparingly) so they survive greyscale and colourblind readers.
- 🟢 **Watch**
  - Legend overlapping data — reposition, don't shrink to illegibility.
  - Too many categorical colours (>~6) — reconsider the encoding.
  - Colliding tick labels — rotate 35°/`ha='right'` before shrinking.
  - Data max overshoots the top tick (bar peaks at 56, ticks end at 50) so it
    can't be read, or the top gridline is clipped by the axes edge — add a
    tick/gridline above the max and set the limit just past it
    (`set_ylim(0, 62)`, not `60`).

---

## 6. Examples (annotated)

### Single distribution — minimal line/scatter
```python
plt.figure(figsize=(5, 4.5))
plt.plot(x, y)
plt.gca().spines["top"].set_visible(False)     # drop top+right for line/scatter
plt.gca().spines["right"].set_visible(False)
plt.grid(True, axis="y", alpha=0.2, linestyle="--")   # subtle, behind data
plt.xlabel("Score")
plt.ylabel("Density")
plt.tight_layout()
plt.savefig("figures/distribution.pdf")        # vector, no dpi
```
*Why it's in-voice:* small footprint, top+right spines gone, faint dashed grid,
vector PDF, no title (caption handles it).

### Horizontal bar with percent axis — drop all spines
```python
plt.figure(figsize=(4.3, 7))
plt.barh(ys, values)
ax = plt.gca()
for side in ("top", "right", "left"):          # keep only the bottom value spine
    ax.spines[side].set_visible(False)
ax.tick_params(axis="y", length=0)             # category labels stay, ticks go with the left spine
ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=0))
plt.grid(True, axis="x", alpha=0.3, linestyle="--")
plt.tight_layout()
plt.savefig("figures/proportion_by_category.pdf")
```
*Why:* the bottom value spine + its x ticks stay so the percentages read off an
axis (not just gridlines), the other three spines and the category tick marks go,
and values are shown as `%` with the grid on the value axis (x).

### Bias plot with reference line
```python
plt.axvline(0, color="gray", linestyle="--", alpha=0.8, linewidth=2)  # zero = neutral
```
*Why:* the meaningful threshold is called out in unobtrusive gray dashes.

### Multi-panel — OO API + panel letters
```python
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
for index, ax in enumerate(axes.flat):
    ax.plot(...)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.text(-0.01, 1.05, f"({'abcd'[index]})", transform=ax.transAxes)  # panel label
fig.tight_layout()
fig.savefig("figures/regressions.pdf")
```
*Why:* object-oriented axes for multiple panels, lowercase `(a)–(d)` labels
upper-left in axes coords.

### Multiple series — redundant encoding (colour + linestyle + marker)
```python
plt.plot(x, y_a, color=c_a, linestyle="-",  marker="o", label="Model A")
plt.plot(x, y_b, color=c_b, linestyle="--", marker="s", label="Model B")
plt.legend(frameon=False, fontsize=10)   # legend carries colour + line/marker
```
*Why it's in-voice:* the two series differ by colour **and** linestyle **and**
marker, so they stay distinguishable in greyscale, for colourblind readers, and
when shrunk — not colour alone.

### Heatmap — scicolor continuous map
```python
cmap = scicolor.get_cmap("acton")
sns.heatmap(df_percent, annot=annot, fmt="", cmap=cmap)
plt.savefig("figures/category_heatmap.pdf")
```
*Why:* perceptually-uniform scicolor map, no rainbow.

### ✗ Avoid
```python
plt.plot(x, y)
plt.legend(frameon=True)               # ✗ boxed legend
plt.title("My Results")                # ✗ title on a paper figure
plt.savefig("fig.png")                 # ✗ raster for a paper
# (all four spines left on, solid grid, jet colormap...)
```

---

## 7. Revision Checklist

Moved to [`target.md`](target.md) — the skill's acceptance spec (items
`F1`–`F19`, tiered `[mechanical]`/`[judged]`/`[advisory]`). Run it before a
figure ships; automated runs use it as the definition of done per the
"Automated mode" section of `SKILL.md`.
