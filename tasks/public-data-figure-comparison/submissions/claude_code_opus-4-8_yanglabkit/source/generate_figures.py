"""Generate the six public-data comparison figures.

Applies the YangLabKit ``yanglabkit-figures`` conventions (minimal, print-first,
spines/ticks paired by plot type, frameless legends, percentage axes, gray
dashed reference lines, redundant encoding) and routes every colour choice
through ``yanglabkit-scicolor``.

Colours are hard-coded hex values taken verbatim from the scicolor bundled data
so this script has no runtime dependency on the ``scicolor`` package (it is not
in the locked task environment):

- Categorical figures use the CVD-safe Okabe-Ito trio (blue / vermillion /
  bluish-green) from ``Masataka Okabe / Color Blind``.
- Single-series bar/histogram figures use one Okabe-Ito accent blue.
- The correlation heatmap uses the perceptually-uniform, CVD-safe diverging
  ``vik`` map (Scientific colour maps), rebuilt from its 32 hex stops.

The task contract overrides the skill's default PDF export: web-gallery
candidates require 300 DPI PNG.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap

# --- Paths ----------------------------------------------------------------
HERE = Path(__file__).resolve().parent
SUBMISSION = HERE.parent
TASK_ROOT = SUBMISSION.parent.parent
DATA = TASK_ROOT / "data"
FIGURES = SUBMISSION / "figures"
FIGURES.mkdir(exist_ok=True)

# --- scicolor palettes (verbatim hex from the scicolor bundled data) ------
# Okabe-Ito ("Masataka Okabe / Color Blind"), CVD-safe categorical.
OKABE_BLUE = "#0071b2"
OKABE_VERMILLION = "#d55e00"
OKABE_GREEN = "#009e73"
# One consistent categorical trio reused across every categorical figure so a
# figure "reads" as part of one collection.
CAT_TRIO = [OKABE_BLUE, OKABE_VERMILLION, OKABE_GREEN]
# Single accent for single-series bars/histograms.
ACCENT = OKABE_BLUE
REFERENCE_GRAY = "gray"

# Scientific colour maps / vik, diverging, perceptually uniform + CVD-safe.
VIK_STOPS = [
    "#001261", "#021f69", "#022b71", "#023779", "#034582", "#05528a",
    "#0e6093", "#1e6f9d", "#3681a9", "#4e92b4", "#67a2c0", "#80b2ca",
    "#9dc4d6", "#b6d3e1", "#cfe0e8", "#e5e7e8", "#eee0d8", "#ecd1c3",
    "#e5c1ad", "#dfb298", "#d7a081", "#d1926d", "#cb835a", "#c57548",
    "#be6533", "#b55521", "#a74310", "#963107", "#832106", "#741506",
    "#670a07", "#590008",
]
VIK = LinearSegmentedColormap.from_list("vik", VIK_STOPS)

# --- Canonical setup block (yanglabkit-figures §3) ------------------------
plt.rcParams.update(
    {
        "font.size": 14,        # reference base; legend drops to 10 (two sizes)
        "axes.axisbelow": True,  # grid sits behind the data
    }
)

SAVE_KW = dict(dpi=300, bbox_inches="tight")  # task override: 300 DPI PNG


def drop_line_scatter_spines(ax):
    """Line/scatter: keep left+bottom (+ their ticks), drop top+right."""
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


# --------------------------------------------------------------------------
# 1. NASA GISTEMP zonal-anomaly line chart
# --------------------------------------------------------------------------
def fig_gistemp():
    df = pd.read_csv(DATA / "gistemp-zonal-rolling.csv")
    series = [
        ("northern_extratropics_anomaly_c", "Northern extratropics", OKABE_VERMILLION, "-", "o"),
        ("tropics_anomaly_c", "Tropics", OKABE_BLUE, "--", "s"),
        ("southern_extratropics_anomaly_c", "Southern extratropics", OKABE_GREEN, "-.", "^"),
    ]

    plt.figure(figsize=(8, 5))
    ax = plt.gca()
    # Zero-anomaly reference line (meaningful threshold -> gray dashed).
    ax.axhline(0, color=REFERENCE_GRAY, linestyle="--", alpha=0.8, linewidth=1.5)
    for col, label, color, ls, marker in series:
        ax.plot(
            df["year"], df[col],
            color=color, linestyle=ls,
            marker=marker, markevery=18, markersize=5,  # sparse redundant channel
            linewidth=2, label=label,
        )

    drop_line_scatter_spines(ax)
    ax.grid(True, axis="y", alpha=0.2, linestyle="--")
    ax.set_xlabel("Year")
    ax.set_ylabel(r"Temperature anomaly ($^{\circ}$C)")
    ax.legend(frameon=False, fontsize=10, labelspacing=0.2, loc="upper left")
    plt.tight_layout()
    plt.savefig(FIGURES / "gistemp-zonal-lines.png", **SAVE_KW)
    plt.close()


# --------------------------------------------------------------------------
# 2. World Bank regional-urbanization horizontal bar chart
# --------------------------------------------------------------------------
def fig_urbanization():
    import textwrap

    df = pd.read_csv(DATA / "world-bank-urbanization-2024.csv")
    # Keep the supplied ascending order: smallest at the bottom.
    y = np.arange(len(df))
    values = df["urban_population_percent"].to_numpy()
    # Wrap long region names so they don't squeeze the plot area (a long label
    # on one line would overrun and crowd the value axis).
    labels = [textwrap.fill(r, width=22) for r in df["region"]]

    plt.figure(figsize=(8.5, 6.5))
    ax = plt.gca()
    ax.barh(y, values, height=0.72, color=ACCENT)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)

    # Horizontal bar: keep only the bottom value spine + its x ticks.
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.tick_params(axis="y", length=0)  # category labels stay, ticks go

    ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=100, decimals=0))
    ax.set_xlim(0, 100)
    ax.set_xticks([0, 20, 40, 60, 80, 100])
    ax.grid(True, axis="x", alpha=0.3, linestyle="--")
    ax.set_xlabel("Urban share of population")

    # Directly label every bar with its percentage.
    for yi, v in zip(y, values):
        ax.text(v + 1.2, yi, f"{v:.0f}%", va="center", ha="left", fontsize=10)

    plt.tight_layout()
    plt.savefig(FIGURES / "world-bank-urbanization-bars.png", **SAVE_KW)
    plt.close()


# --------------------------------------------------------------------------
# 3. Palmer Penguins body-mass box plot
# --------------------------------------------------------------------------
def fig_penguins():
    df = pd.read_csv(DATA / "palmer-penguins-body-mass.csv")
    order = ["Adelie", "Chinstrap", "Gentoo"]
    colors = dict(zip(order, CAT_TRIO))
    groups = [df.loc[df["species"] == sp, "body_mass_g"].to_numpy() for sp in order]

    plt.figure(figsize=(6, 5))
    ax = plt.gca()
    positions = np.arange(1, len(order) + 1)
    bp = ax.boxplot(
        groups, positions=positions, widths=0.5,
        patch_artist=True, showfliers=False,  # raw points overlaid instead
        medianprops=dict(color="black", linewidth=1.5),
        whiskerprops=dict(color="black"), capprops=dict(color="black"),
        boxprops=dict(edgecolor="black"),
    )
    for patch, sp in zip(bp["boxes"], order):
        patch.set_facecolor(colors[sp])
        patch.set_alpha(0.35)

    # Overlay every observation with a small jitter.
    rng = np.random.default_rng(0)
    for pos, sp, vals in zip(positions, order, groups):
        jitter = rng.uniform(-0.13, 0.13, size=vals.shape)
        ax.scatter(
            np.full_like(vals, pos, dtype=float) + jitter, vals,
            s=14, color=colors[sp], alpha=0.6, edgecolors="none", zorder=3,
        )

    drop_line_scatter_spines(ax)
    ax.grid(True, axis="y", alpha=0.2, linestyle="--")
    ax.set_xticks(positions)
    ax.set_xticklabels(order)
    ax.set_xlabel("Species")
    ax.set_ylabel("Body mass (g)")
    plt.tight_layout()
    plt.savefig(FIGURES / "palmer-penguins-box.png", **SAVE_KW)
    plt.close()


# --------------------------------------------------------------------------
# 4. UCI red-wine correlation heatmap
# --------------------------------------------------------------------------
def fig_wine():
    df = pd.read_csv(DATA / "uci-red-wine-correlations.csv", index_col="variable")
    mat = df.to_numpy()

    fig, ax = plt.subplots(figsize=(8.5, 7.5))
    im = ax.imshow(mat, cmap=VIK, vmin=-1, vmax=1, aspect="equal")

    ax.set_xticks(np.arange(len(df.columns)))
    ax.set_yticks(np.arange(len(df.index)))
    ax.set_xticklabels(df.columns, rotation=40, ha="right")
    ax.set_yticklabels(df.index)

    # Heatmap: drop all four spines and all tick marks (cells self-labeled).
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(length=0)

    # Annotate every cell; pick text colour for contrast against the map.
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            v = mat[i, j]
            txt_color = "white" if abs(v) > 0.55 else "black"
            ax.text(j, i, f"{v:.2f}", ha="center", va="center",
                    fontsize=7, color=txt_color)

    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04, ticks=[-1, -0.5, 0, 0.5, 1])
    cbar.set_label("Pearson correlation")
    cbar.outline.set_visible(False)
    plt.tight_layout()
    plt.savefig(FIGURES / "wine-correlation-heatmap.png", **SAVE_KW)
    plt.close()


# --------------------------------------------------------------------------
# 5. UCI Auto MPG weight-versus-economy scatter plot
# --------------------------------------------------------------------------
def fig_auto_mpg():
    df = pd.read_csv(DATA / "uci-auto-mpg.csv")
    groups = [
        ("USA", OKABE_VERMILLION, "o"),
        ("Europe", OKABE_BLUE, "s"),
        ("Japan", OKABE_GREEN, "^"),
    ]

    plt.figure(figsize=(6, 5))
    ax = plt.gca()
    for origin, color, marker in groups:  # colour + marker = redundant encoding
        sub = df[df["origin"] == origin]
        ax.scatter(
            sub["weight_lb"], sub["mpg"],
            s=34, color=color, marker=marker,
            alpha=0.75, edgecolors="none", label=origin,
        )

    drop_line_scatter_spines(ax)
    ax.grid(True, axis="y", alpha=0.2, linestyle="--")
    ax.set_xlabel("Weight (lb)")
    ax.set_ylabel("Fuel economy (mpg)")
    ax.legend(frameon=False, fontsize=10, labelspacing=0.2, loc="upper right",
              title="Origin", title_fontsize=10)
    plt.tight_layout()
    plt.savefig(FIGURES / "auto-mpg-scatter.png", **SAVE_KW)
    plt.close()


# --------------------------------------------------------------------------
# 6. USGS 2025 earthquake-magnitude percentage histogram
# --------------------------------------------------------------------------
def fig_usgs():
    df = pd.read_csv(DATA / "usgs-2025-reviewed-m5.csv")
    mags = df["magnitude"].to_numpy()

    bin_start, bin_width = 5.0, 0.1
    top = np.ceil((mags.max() - bin_start) / bin_width) * bin_width + bin_start
    edges = np.arange(bin_start, top + bin_width / 2, bin_width)
    weights = np.full_like(mags, 100.0 / mags.size)  # percent of all events

    plt.figure(figsize=(8, 5))
    ax = plt.gca()
    ax.hist(mags, bins=edges, weights=weights, color=ACCENT,
            edgecolor="white", linewidth=0.3)

    drop_line_scatter_spines(ax)
    ax.grid(True, axis="y", alpha=0.2, linestyle="--")
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=100, decimals=0))
    ax.set_xlabel("Magnitude")
    ax.set_ylabel("Share of events")
    ax.set_xlim(bin_start, edges[-1])
    plt.tight_layout()
    plt.savefig(FIGURES / "usgs-earthquake-histogram.png", **SAVE_KW)
    plt.close()


def main():
    fig_gistemp()
    fig_urbanization()
    fig_penguins()
    fig_wine()
    fig_auto_mpg()
    fig_usgs()
    print("Wrote 6 figures to", FIGURES)


if __name__ == "__main__":
    main()
