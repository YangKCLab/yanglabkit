# Colour-scheme selection guide

Decision logic for picking a colour palette, encoded from **Crameri, Shephard &
Heron (2020), "The misuse of colour in science communication"** (Nature
Communications, doi:10.1038/s41467-020-19160-7). This is the machine-readable
version of that paper's Fig. 5 (class taxonomy), Fig. 6 (decision flow), and its
four-point "how to recognise an unscientific colour map" checklist.

The concrete palette names below resolve to real entries in the two bundled data
files: `data/colors.json` (discrete / categorical) and
`data/continuous-colormaps.json` (continuous). Always return **actual hex codes**
from those files, not just names.

---

## Step 1 — Map the data structure to a colour-map CLASS (Fig. 5)

Ask what the colour is encoding, then pick the class:

| Data structure | Class | Example |
|---|---|---|
| Qualitative groups with **no order** (categories, labels) | **categorical** | species, country, treatment arm |
| A single quantity **ordered low → high** | **sequential** | temperature, density, count, probability |
| A quantity with a **meaningful midpoint**, deviation in two directions | **diverging** | correlation (−1…+1), anomaly vs baseline, log-ratio |
| **Two independent sequential** quantities meeting at a natural boundary | **multi-sequential** | elevation (below/above sea level), bathymetry+topography |

Notes:
- "Ordered but with a critical centre value" ⇒ diverging, **not** sequential. Put
  the neutral/light colour exactly on the midpoint.
- If in doubt between sequential and diverging, ask whether the midpoint is
  special. No special midpoint ⇒ sequential.

## Step 2 — Discrete vs continuous

- **Discrete** (a fixed, countable set of classes/levels — bar chart, choropleth
  bins, categorical legend) ⇒ pick from `data/colors.json`.
- **Continuous** (a smoothly varying field — heatmap, contour, image, density) ⇒
  pick from `data/continuous-colormaps.json` and return evenly-spaced hex stops
  plus the canonical name.

## Step 3 — Gather constraints

- Number of categories / levels needed (must not exceed the palette's colour count).
- Colourblind-safe? **Default: yes.** Only relax if the user explicitly opts out.
- Greyscale / print-safe needed? Prefer perceptually-ordered (monotonic-lightness) maps.
- Scientific-strict vs aesthetic? Strict ⇒ Scientific colour maps / viridis family.

---

## Step 4 — Decision flow to a concrete palette (Fig. 6)

CVD-safe defaults are listed **first**. All names below exist in the bundled data.

### Categorical (discrete only)

- **≤ 8 groups, CVD-safe (default):**
  - `Masataka Okabe / Color Blind` — Okabe–Ito, 8 colours. The recommended default.
  - `tableau / Color Blind 10` — 10 colours, CVD-safe.
  - `MetBrewer / Johnson` (5), `MetBrewer / Kandinsky` (4), `MetBrewer / Isfahan2` (5),
    `RPTH / RPTH palette` (6) — CVD-safe categorical alternatives.
- **10–20 groups:**
  - `tableau / Tableau 10` (10) for up to 10 groups.
  - `Trubetskoy / 20-colors-1` + `Trubetskoy / 20-colors-2` (10 each → 20 combined)
    when you truly need many categories. **Caveat:** CVD-safety degrades as the
    count rises; prefer redundant encoding (shape, direct labels) beyond ~8.
- **General rule:** minimise the number of categories. Beyond ~8–10, no palette is
  reliably CVD-safe; encode the extra dimension some other way.

### Sequential

- **Discrete:** `Scientific colour / batlow 10`, `acton 10`, `oslo 10` (all
  CVD-safe, 10 levels — subset to the number of levels you need); `MetBrewer / Hokusai2` (6, CVD-safe).
- **Continuous:** `viridis`, `cividis` (matplotlib), `batlow`, `acton`, `oslo`,
  `bamako`, `lajolla`, `davos` (Scientific colour maps) — all perceptually uniform
  and CVD-safe. `cividis` is optimised specifically for CVD. `grayC` for a
  perceptually-uniform greyscale.

### Diverging

- **Discrete:** `Scientific colour / vik 10`, `broc 10` (CVD-safe, 10 levels);
  `MetBrewer / Cassatt1` (8), `OKeeffe1` (11), `Hiroshige` (10) — CVD-safe.
- **Continuous:** `vik`, `broc`, `roma`, `cork` (Scientific colour maps) — all
  perceptually uniform and CVD-safe. Anchor the light midpoint on the critical value.

### Multi-sequential

- **Discrete:** `Scientific colour / oleron 10` (CVD-safe).
- **Continuous:** `oleron`, `topo` — for two-sided fields such as
  elevation/bathymetry that meet at a natural boundary (e.g. sea level at 0).

---

## Step 5 — Guardrails (the paper's four-point checklist)

Before returning a recommendation, enforce these. They are the paper's test for
"how to recognise an unscientific colour map," plus its practical caveats.

1. **Perceptual uniformity.** Equal steps in the data must map to equal perceived
   colour steps. Reject maps whose lightness gradient is uneven — they distort data
   (the paper shows distortion can exceed ~7% of the displayed range).
2. **No red–green at equal luminosity.** Such pairs are indistinguishable to the
   ~8% of men / ~0.5% of women with CVD. Never build a categorical scheme that
   relies on red-vs-green at similar lightness.
3. **Never rainbow / jet.** Reject rainbow, jet, HSV, and "improved" rainbows
   including Google's **Turbo** — they fail the uniformity requirement. Offer a
   perceptually-uniform replacement (viridis / batlow) instead.
4. **Prefer maps documented as scientifically derived.** The bundled Scientific
   colour maps, viridis/cividis/inferno, and CET maps all carry
   `perceptually_uniform: true` metadata. Prefer them over ad-hoc palettes.

Also apply the paper's practical caveats:
- **Perceptual order / greyscale test.** Prefer monotonic-lightness maps so the
  figure survives greyscale printing and CVD. (This is why `cividis`, `batlow`,
  and the sequential Scientific maps are safe defaults.)
- **Always include a colour bar** for any continuous map — colour without a scale
  is unreadable.
- **Don't stretch or squeeze the colour map** across the data range; that warps the
  mapping like a distorted axis.
- **Avoid contiguous heatmap tiles** where adjacent colours bleed and shift
  perceived value; add separation or gridlines.
