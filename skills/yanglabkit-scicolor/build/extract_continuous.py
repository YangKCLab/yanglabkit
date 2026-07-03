#!/usr/bin/env python3
"""Extract continuous colormaps from the scicolor package into a self-contained JSON.

This is a BUILD-TIME script. It is NOT read by the skill at runtime. Its committed
output (`../data/continuous-colormaps.json`) is the only thing the skill reads, so
the skill has no Python runtime dependency.

Usage (run inside the scicolor repo so `scicolor` + matplotlib are importable):

    cd git_repos/standalone/scicolor
    uv run python /path/to/yanglabkit/skills/yanglabkit-scicolor/build/extract_continuous.py

It:
  1. Iterates every colormap in scicolor's `color_info_list` with cm_type == "continuous".
  2. Loads each via `scicolor.get_cmap(name)` (reads scicolor's raw RGB .txt files
     for the scientific/cet/ocean maps; samples matplotlib for viridis/inferno/cividis).
  3. Downsamples each to N evenly-spaced hex stops (default 32).
  4. Joins class/type/perceptual-uniformity/CVD metadata from `color_info_df`.
  5. Writes `../data/continuous-colormaps.json`.

Re-run this whenever scicolor's continuous colormaps or metadata change.
"""

import json
import os

import numpy as np

import scicolor

# Number of evenly-spaced hex stops to emit per colormap. 32 is enough to
# interpolate a smooth gradient without bloating agent context; the full-resolution
# colormap object remains available via scicolor.get_cmap(name).
N_STOPS = 32


def _to_hex(rgb):
    """Convert an (r, g, b[, a]) float tuple in [0, 1] to a #rrggbb string."""
    r, g, b = (int(round(c * 255)) for c in rgb[:3])
    return f"#{r:02x}{g:02x}{b:02x}"


def extract():
    df = scicolor.color_info_df
    continuous = df[df["cm_type"] == "continuous"]

    entries = []
    fractions = np.linspace(0, 1, N_STOPS)
    for _, row in continuous.iterrows():
        name = row["cm_name"]
        cmap = scicolor.get_cmap(name)
        if cmap is None:
            raise RuntimeError(f"scicolor.get_cmap({name!r}) returned None")
        stops = [_to_hex(cmap(f)) for f in fractions]
        entries.append(
            {
                "name": name,
                "source": row["source"],
                "cm_class": row["cm_class"],
                "cm_type": row["cm_type"],
                "perceptually_uniform": bool(row["perceptually_uniform"]),
                "color_blind_friendly": bool(row["color_blind_friendly"]),
                "stops": stops,
            }
        )

    entries.sort(key=lambda e: (e["cm_class"], e["name"]))

    out_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "data",
        "continuous-colormaps.json",
    )
    out_path = os.path.abspath(out_path)
    with open(out_path, "w") as f:
        json.dump(entries, f, indent=2)
        f.write("\n")

    print(f"Wrote {len(entries)} continuous colormaps to {out_path}")


if __name__ == "__main__":
    extract()
