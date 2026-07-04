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
   paper scale (small figsizes, ~14pt text), export vector, assume greyscale
   might happen.
3. **Quantitatively honest.** Axes start where the data honestly starts;
   proportions are shown as percentages; reference lines mark meaningful
   thresholds (0, chance, a cutoff).
4. **Consistent across a paper.** The same variable is the same colour in every
   panel; the same size hierarchy everywhere; one colormap family per paper.
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
    "font.size": 14,        # base size — everything scales from here
    "axes.axisbelow": True, # grid/gridlines sit BEHIND the data
})
```

Font family is intentionally left at matplotlib's default **DejaVu Sans** — no
`font.family` override, so figures reproduce on any machine with zero font
dependencies.

### Font sizes
**One base size (14), at most one deviation.** Keep ticks, labels, and titles at
14 for uniformity. Shrinking an element that would otherwise crowd the plot is
fine — most commonly the **legend to `fontsize=10`** — but cap a figure at **two
distinct font sizes total**. A third size (or more) reads as messy; if another
element is crowded, fix it with layout, shorter labels, or wrapping (see below)
rather than introducing a third size.

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

### Spines — by plot type
| Plot type | Spines kept |
|---|---|
| Line / scatter | left + bottom (drop **top + right**) |
| Horizontal bar / ranked list | drop **all four** |
| Heatmap | drop **all four** |

```python
# line/scatter default:
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# horizontal bar / heatmap:
for s in ax.spines.values():
    s.set_visible(False)
```

### Grid
Subtle, dashed, single-axis, behind the data (`axisbelow=True` handles the last):

```python
plt.grid(True, axis="y", alpha=0.2, linestyle="--")   # vertical bars / lines
plt.grid(True, axis="x", alpha=0.3, linestyle="--")   # horizontal bars
```
- `alpha` in `0.1–0.3`. Grid on the axis the eye reads values along.

### Legend
Always frameless, tight, small:

```python
plt.legend(frameon=False, fontsize=10, labelspacing=0.2, loc="upper right")
```
- `frameon=False` **always**. Never a boxed legend.
- Tight `labelspacing` (`0.1–0.2`). Place where it doesn't cover data.

### Tick formatting
Proportions are **percentages**, not raw fractions:

```python
plt.gca().xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=0))
```
- `xmax=1` when data is in `[0,1]`; `xmax=100` when already scaled.
- `decimals=0` unless finer precision is genuinely needed.

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
  - Raw fractions on an axis where a `PercentFormatter` reads better.
  - Truncated y-axis that visually exaggerates a difference (be honest).
  - Elaborate per-element font sizing when base-14 would do.
  - More than two distinct font sizes in one figure — pick the one element that
    genuinely needs a deviation (usually the legend) and hold everything else at
    base size.
  - A title or axis label so long it overruns the axes width on one line —
    shorten it, or break it across lines so it aligns with the figure.
- 🟢 **Watch**
  - Legend overlapping data — reposition, don't shrink to illegibility.
  - Too many categorical colours (>~6) — reconsider the encoding.
  - Colliding tick labels — rotate 35°/`ha='right'` before shrinking.

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
for s in plt.gca().spines.values():            # horizontal bar → no frame
    s.set_visible(False)
plt.gca().xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=0))
plt.grid(True, axis="x", alpha=0.3, linestyle="--")
plt.tight_layout()
plt.savefig("figures/proportion_by_category.pdf")
```
*Why:* frameless for a ranked bar list, values shown as `%`, grid on the value
axis (x).

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

Run before a figure ships:

1. Exported as **vector PDF** for the paper? (PNG @ dpi=300, `bbox_inches='tight'`
   only for slides/web.)
2. Spines correct for the plot type? (line/scatter: top+right off; bar/heatmap:
   all off.)
3. Grid dashed, `alpha ≤ 0.3`, on the value axis, **behind** the data?
4. Legend `frameon=False`, not covering data?
5. Proportions shown as **percentages** (`PercentFormatter`), not raw fractions?
6. All colours from **scicolor** — no rainbow/jet, greyscale-survivable?
7. Same variable = same colour across every panel?
8. Multi-panel labelled `(a)(b)(c)` upper-left; no stray in-figure title on paper
   figures?
9. `tight_layout()` called; nothing clipped?
10. Titles/axis labels short and within the figure width — long ones wrapped
    across lines, not overrunning the axes?
11. No more than **two distinct font sizes** in the figure?
12. Readable at single-column width?
