#!/usr/bin/env python3
"""Generate the six public-data comparison figures.

This is the "noskill" control submission: it applies ordinary, competent
matplotlib/seaborn defaults without consulting the yanglabkit-figures or
yanglabkit-scicolor guidance documents. All six figures are written as 300 DPI
PNGs into ../figures/ next to this script.

Run (from tasks/public-data-figure-comparison/):
    uv run --frozen python \
        submissions/claude_code_opus-4-8_noskill/source/generate_figures.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Paths -----------------------------------------------------------------------
HERE = Path(__file__).resolve().parent
SUBMISSION = HERE.parent
FIGURES = SUBMISSION / "figures"
# task root is submissions/<name>/../../  -> tasks/public-data-figure-comparison
DATA = SUBMISSION.parent.parent / "data"
FIGURES.mkdir(parents=True, exist_ok=True)

DPI = 300


def save(fig: plt.Figure, name: str) -> None:
    fig.savefig(FIGURES / name, dpi=DPI, bbox_inches="tight")
    plt.close(fig)


# 1. GISTEMP zonal-anomaly line chart -----------------------------------------
def gistemp() -> None:
    df = pd.read_csv(DATA / "gistemp-zonal-rolling.csv")
    series = {
        "northern_extratropics_anomaly_c": "Northern extratropics",
        "tropics_anomaly_c": "Tropics",
        "southern_extratropics_anomaly_c": "Southern extratropics",
    }
    colors = plt.get_cmap("tab10").colors  # standard categorical default
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.axhline(0.0, color="gray", linewidth=1.0, zorder=1)
    for (col, label), color in zip(series.items(), colors):
        ax.plot(df["year"], df[col], label=label, color=color, linewidth=1.8)
    ax.set_xlabel("Year")
    ax.set_ylabel("Temperature anomaly (°C)")
    ax.set_title("GISTEMP zonal temperature anomalies (5-year rolling mean)")
    ax.legend(title="Zonal band")
    ax.grid(True, alpha=0.3)
    save(fig, "gistemp-zonal-lines.png")


# 2. World Bank regional-urbanization horizontal bar chart --------------------
def world_bank() -> None:
    df = pd.read_csv(DATA / "world-bank-urbanization-2024.csv")
    # Preserve supplied ascending order: smallest at bottom.
    y = np.arange(len(df))
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.barh(y, df["urban_population_percent"], color="#4C72B0")
    ax.set_yticks(y)
    ax.set_yticklabels(df["region"])
    ax.set_xlabel("Urban population (% of total)")
    ax.set_xlim(0, 100)
    ax.set_title("Urban population share by region, 2024")
    for bar, value in zip(bars, df["urban_population_percent"]):
        ax.text(
            bar.get_width() + 1.0,
            bar.get_y() + bar.get_height() / 2,
            f"{value:.1f}%",
            va="center",
            ha="left",
            fontsize=9,
        )
    ax.grid(True, axis="x", alpha=0.3)
    save(fig, "world-bank-urbanization-bars.png")


# 3. Palmer Penguins body-mass box plot ---------------------------------------
def penguins() -> None:
    df = pd.read_csv(DATA / "palmer-penguins-body-mass.csv")
    order = ["Adelie", "Chinstrap", "Gentoo"]
    colors = plt.get_cmap("tab10").colors
    fig, ax = plt.subplots(figsize=(7, 5))
    data = [df.loc[df["species"] == sp, "body_mass_g"].values for sp in order]
    bp = ax.boxplot(
        data,
        tick_labels=order,
        patch_artist=True,
        showfliers=False,
        widths=0.5,
    )
    for patch, color in zip(bp["boxes"], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.5)
    for median in bp["medians"]:
        median.set_color("black")
    # Overlay all observations with jitter.
    rng = np.random.default_rng(0)
    for i, sp in enumerate(order, start=1):
        vals = df.loc[df["species"] == sp, "body_mass_g"].values
        jitter = rng.uniform(-0.12, 0.12, size=len(vals))
        ax.scatter(
            np.full(len(vals), i) + jitter,
            vals,
            color=colors[i - 1],
            edgecolor="black",
            linewidth=0.3,
            alpha=0.6,
            s=18,
            zorder=3,
        )
    ax.set_xlabel("Species")
    ax.set_ylabel("Body mass (g)")
    ax.set_title("Penguin body mass by species")
    ax.grid(True, axis="y", alpha=0.3)
    save(fig, "palmer-penguins-box.png")


# 4. UCI red-wine correlation heatmap -----------------------------------------
def wine() -> None:
    df = pd.read_csv(DATA / "uci-red-wine-correlations.csv", index_col="variable")
    labels = list(df.columns)
    fig, ax = plt.subplots(figsize=(9, 8))
    im = ax.imshow(df.values, cmap="RdBu_r", vmin=-1, vmax=1, aspect="auto")
    ax.set_xticks(np.arange(len(labels)))
    ax.set_yticks(np.arange(len(df.index)))
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=8)
    ax.set_yticklabels(list(df.index), fontsize=8)
    ax.set_title("Red-wine physicochemical correlations")
    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label("Pearson correlation")
    save(fig, "wine-correlation-heatmap.png")


# 5. UCI Auto MPG weight-versus-economy scatter -------------------------------
def auto_mpg() -> None:
    df = pd.read_csv(DATA / "uci-auto-mpg.csv")
    order = ["USA", "Europe", "Japan"]
    colors = plt.get_cmap("tab10").colors
    fig, ax = plt.subplots(figsize=(8, 6))
    for origin, color in zip(order, colors):
        sub = df[df["origin"] == origin]
        ax.scatter(
            sub["weight_lb"],
            sub["mpg"],
            label=origin,
            color=color,
            alpha=0.7,
            edgecolor="white",
            linewidth=0.4,
            s=30,
        )
    ax.set_xlabel("Vehicle weight (lb)")
    ax.set_ylabel("Fuel economy (miles per gallon)")
    ax.set_title("Fuel economy versus vehicle weight by origin")
    ax.legend(title="Origin")
    ax.grid(True, alpha=0.3)
    save(fig, "auto-mpg-scatter.png")


# 6. USGS 2025 earthquake-magnitude percentage histogram ----------------------
def usgs() -> None:
    df = pd.read_csv(DATA / "usgs-2025-reviewed-m5.csv")
    mags = df["magnitude"].values
    start = 5.0
    width = 0.1
    top = np.ceil((mags.max() - start) / width) * width + start
    edges = np.arange(start, top + width / 2, width)
    weights = np.full(len(mags), 100.0 / len(mags))
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.hist(mags, bins=edges, weights=weights, color="#55A868", edgecolor="white")
    ax.set_xlabel("Magnitude")
    ax.set_ylabel("Percentage of events (%)")
    ax.set_title("2025 reviewed earthquakes (M ≥ 5.0)")
    ax.grid(True, axis="y", alpha=0.3)
    save(fig, "usgs-earthquake-histogram.png")


def main() -> None:
    gistemp()
    world_bank()
    penguins()
    wine()
    auto_mpg()
    usgs()
    print(f"Wrote 6 figures to {FIGURES}")


if __name__ == "__main__":
    main()
