#!/usr/bin/env python3
"""Generate all six figures for yanglabkit-public-data-figures-v1.

Submission: claude_code_fable-5_noskill (no-skill baseline run — styling
reflects the agent's own defaults; the yanglabkit-figures and
yanglabkit-scicolor skill documents were deliberately not consulted).

Run from tasks/public-data-figure-comparison/:
    uv run --frozen python submissions/claude_code_fable-5_noskill/source/make_figures.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import PercentFormatter

TASK_DIR = Path(__file__).resolve().parents[3]
DATA_DIR = TASK_DIR / "data"
FIG_DIR = Path(__file__).resolve().parents[1] / "figures"

# Okabe & Ito colorblind-safe categorical colors.
BLUE = "#0072B2"
ORANGE = "#E69F00"
GREEN = "#009E73"
VERMILLION = "#D55E00"
GRAY = "#666666"

plt.rcParams.update(
    {
        "figure.dpi": 100,
        "savefig.dpi": 300,
        "font.size": 10,
        "axes.titlesize": 11,
        "axes.titleweight": "bold",
        "axes.titlepad": 10,
        "axes.labelsize": 10,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.color": "#DDDDDD",
        "grid.linewidth": 0.6,
        "axes.axisbelow": True,
        "legend.frameon": False,
        "figure.constrained_layout.use": True,
    }
)


def save(fig: plt.Figure, name: str) -> None:
    out = FIG_DIR / name
    fig.savefig(out)
    plt.close(fig)
    print(f"wrote {out.relative_to(TASK_DIR)}")


def gistemp_zonal_lines() -> None:
    df = pd.read_csv(DATA_DIR / "gistemp-zonal-rolling.csv")
    series = [
        ("northern_extratropics_anomaly_c", "Northern extratropics", VERMILLION),
        ("tropics_anomaly_c", "Tropics", GREEN),
        ("southern_extratropics_anomaly_c", "Southern extratropics", BLUE),
    ]
    fig, ax = plt.subplots(figsize=(7.0, 4.4))
    ax.axhline(0, color=GRAY, linewidth=0.9, linestyle="--", zorder=1)
    for column, label, color in series:
        ax.plot(df["year"], df[column], label=label, color=color, linewidth=1.8)
    ax.set_xlabel("Year")
    ax.set_ylabel("Temperature anomaly (\N{DEGREE SIGN}C, 5-year rolling mean)")
    ax.set_title("Zonal surface temperature anomalies (NASA GISTEMP v4)")
    ax.legend(loc="upper left")
    ax.set_xlim(df["year"].min(), df["year"].max())
    save(fig, "gistemp-zonal-lines.png")


def world_bank_urbanization_bars() -> None:
    df = pd.read_csv(DATA_DIR / "world-bank-urbanization-2024.csv")
    labels = [
        label.replace(
            "Middle East, North Africa, Afghanistan & Pakistan",
            "Middle East, North Africa,\nAfghanistan & Pakistan",
        )
        for label in df["region"]
    ]
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    positions = np.arange(len(df))
    ax.barh(positions, df["urban_population_percent"], color=BLUE, height=0.62)
    for y, value in zip(positions, df["urban_population_percent"]):
        ax.text(value + 1.2, y, f"{value:.1f}%", va="center", fontsize=9, color="#333333")
    ax.set_yticks(positions, labels)
    ax.set_xlim(0, 100)
    ax.xaxis.set_major_formatter(PercentFormatter(decimals=0))
    ax.set_xlabel("Urban population (% of total population, 2024)")
    ax.set_title("Urban share of population by world region (World Bank WDI)")
    ax.grid(axis="y", visible=False)
    save(fig, "world-bank-urbanization-bars.png")


def palmer_penguins_box() -> None:
    df = pd.read_csv(DATA_DIR / "palmer-penguins-body-mass.csv")
    species = ["Adelie", "Chinstrap", "Gentoo"]
    colors = [BLUE, ORANGE, GREEN]
    groups = [df.loc[df["species"] == name, "body_mass_g"].to_numpy() for name in species]

    fig, ax = plt.subplots(figsize=(6.2, 4.6))
    boxes = ax.boxplot(
        groups,
        positions=np.arange(len(species)),
        widths=0.5,
        showfliers=False,
        patch_artist=True,
        medianprops={"color": "#333333", "linewidth": 1.4},
        whiskerprops={"color": "#555555"},
        capprops={"color": "#555555"},
        boxprops={"linewidth": 1.0},
    )
    rng = np.random.default_rng(42)
    for i, (values, color) in enumerate(zip(groups, colors)):
        boxes["boxes"][i].set(facecolor=mpl.colors.to_rgba(color, 0.25), edgecolor=color)
        jitter = rng.uniform(-0.13, 0.13, size=len(values))
        ax.scatter(
            np.full(len(values), i) + jitter,
            values,
            s=12,
            color=color,
            alpha=0.55,
            linewidths=0,
            zorder=3,
        )
    ax.set_xticks(np.arange(len(species)), species)
    ax.set_xlabel("Species")
    ax.set_ylabel("Body mass (g)")
    ax.set_title("Penguin body mass by species (Palmer Station LTER)")
    ax.grid(axis="x", visible=False)
    save(fig, "palmer-penguins-box.png")


def wine_correlation_heatmap() -> None:
    df = pd.read_csv(DATA_DIR / "uci-red-wine-correlations.csv", index_col="variable")
    variables = df.index.to_list()

    fig, ax = plt.subplots(figsize=(7.4, 6.2))
    ax.grid(visible=False)
    for spine in ax.spines.values():
        spine.set_visible(False)
    image = ax.imshow(df.to_numpy(), cmap="RdBu_r", vmin=-1, vmax=1)
    ax.set_xticks(np.arange(len(variables)), variables, rotation=45, ha="right")
    ax.set_yticks(np.arange(len(variables)), variables)
    ax.tick_params(length=0)
    colorbar = fig.colorbar(image, ax=ax, fraction=0.046, pad=0.03)
    colorbar.set_label("Pearson correlation")
    colorbar.outline.set_visible(False)
    ax.set_title("Correlations among red-wine physicochemical variables (UCI)")
    save(fig, "wine-correlation-heatmap.png")


def auto_mpg_scatter() -> None:
    df = pd.read_csv(DATA_DIR / "uci-auto-mpg.csv")
    origins = [("USA", BLUE), ("Europe", ORANGE), ("Japan", GREEN)]
    fig, ax = plt.subplots(figsize=(7.0, 4.8))
    for origin, color in origins:
        subset = df[df["origin"] == origin]
        ax.scatter(
            subset["weight_lb"],
            subset["mpg"],
            s=24,
            color=color,
            alpha=0.65,
            linewidths=0.4,
            edgecolors="white",
            label=origin,
        )
    ax.set_xlabel("Vehicle weight (lb)")
    ax.set_ylabel("Fuel economy (mpg)")
    ax.set_title("Fuel economy versus vehicle weight (UCI Auto MPG)")
    ax.legend(title="Origin", loc="upper right")
    save(fig, "auto-mpg-scatter.png")


def usgs_earthquake_histogram() -> None:
    df = pd.read_csv(DATA_DIR / "usgs-2025-reviewed-m5.csv")
    magnitudes = df["magnitude"].to_numpy()
    bin_edges = np.arange(5.0, np.ceil(magnitudes.max() * 10) / 10 + 0.1, 0.1)
    weights = np.full(len(magnitudes), 100.0 / len(magnitudes))

    fig, ax = plt.subplots(figsize=(7.0, 4.4))
    ax.hist(
        magnitudes,
        bins=bin_edges,
        weights=weights,
        color=BLUE,
        edgecolor="white",
        linewidth=0.4,
    )
    ax.set_xlabel("Magnitude")
    ax.set_ylabel("Percentage of events (%)")
    ax.set_title("Magnitude distribution of M\N{GREATER-THAN OR EQUAL TO}5 earthquakes, 2025 (USGS/ANSS)")
    ax.grid(axis="x", visible=False)
    save(fig, "usgs-earthquake-histogram.png")


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    gistemp_zonal_lines()
    world_bank_urbanization_bars()
    palmer_penguins_box()
    wine_correlation_heatmap()
    auto_mpg_scatter()
    usgs_earthquake_histogram()


if __name__ == "__main__":
    main()
