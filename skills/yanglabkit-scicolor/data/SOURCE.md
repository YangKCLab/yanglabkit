# Data provenance & re-sync

Both data files are self-contained snapshots derived from the lab's **scicolor**
repository (`git@github.com:yang3kc/scicolor.git`). The skill reads only these
committed JSON files at runtime — there is no Python dependency at runtime.

Snapshot source commit: `bb40a9342ed9785b880581f2167e314a9b0b3135` (2025-10-13).

## `colors.json` — discrete / categorical palettes

- **Source:** `colorpicker/public/colors/colors.json` in the scicolor repo.
- **Contents:** ~54 colour schemes across 11 collections (Tableau, Nord,
  Trubetskoy, Gruvbox, RPTH, MetBrewer, Scientific colour, Wes Anderson,
  Chromotome, Black Variants, Masataka Okabe). Each scheme has `name`, `labels`
  (`categorical` / `discrete` / `sequential` / `diverging` /
  `color_blind_friendly`), and an explicit hex `colors` array.
- **Re-sync:** copy the file verbatim.
  ```bash
  cp <scicolor>/colorpicker/public/colors/colors.json ./colors.json
  ```

## `continuous-colormaps.json` — continuous colormaps

- **Source:** EXTRACTED from scicolor's Python package — the raw RGB `.txt` data
  files (`scicolor/scientific_colors/*.txt`, `scicolor/cet_colors/*.txt`,
  `scicolor/ocean_colors/topo.txt`) plus matplotlib's viridis/inferno/cividis —
  with class/type/CVD/perceptual-uniformity metadata joined from
  `color_info_list` in `scicolor/__init__.py`.
- **Contents:** every colormap in `color_info_list` with `cm_type == "continuous"`
  (28 maps), each downsampled to 32 evenly-spaced hex `stops` plus metadata
  (`cm_class`, `cm_type`, `perceptually_uniform`, `color_blind_friendly`,
  `source`).
- **Re-sync:** re-run the build-time extractor inside the scicolor repo's uv env
  (requires Python + matplotlib + scicolor **at build time only**):
  ```bash
  cd <scicolor>
  uv run python <yanglabkit>/skills/yanglabkit-scicolor/build/extract_continuous.py
  ```

## Full-resolution continuous colormaps

The 32-stop snapshots are for recommendation and interpolation. The
full-resolution continuous colormap **objects** live in the `scicolor` pip
package — install it and call `scicolor.get_cmap(name)` (matplotlib-compatible)
if you need the native-resolution map.
