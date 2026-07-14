#!/usr/bin/env python3
"""Generate the codex_gpt-5-5_noskill public-data figure submission.

This run intentionally uses only the task contract plus ordinary Matplotlib
choices. It does not apply the repository's figure or colour skills.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import FuncFormatter, MultipleLocator


TASK_ROOT = Path(__file__).resolve().parents[3]
DATA = TASK_ROOT / "data"
OUT = TASK_ROOT / "submissions" / "codex_gpt-5-5_noskill" / "figures"
DPI = 300

TAB10 = {
    "blue": "#1f77b4",
    "orange": "#ff7f0e",
    "green": "#2ca02c",
    "red": "#d62728",
    "purple": "#9467bd",
    "brown": "#8c564b",
    "pink": "#e377c2",
    "gray": "#7f7f7f",
}


def setup() -> None:
    mpl.rcParams.update(
        {
            "figure.dpi": DPI,
            "savefig.dpi": DPI,
            "savefig.bbox": "tight",
            "savefig.pad_inches": 0.05,
            "font.size": 9,
            "axes.labelsize": 9,
            "axes.titlesize": 10,
            "legend.fontsize": 8,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "grid.color": "#d9d9d9",
            "grid.linewidth": 0.6,
            "grid.alpha": 0.7,
        }
    )


def save(fig: plt.Figure, filename: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / filename, dpi=DPI)
    plt.close(fig)


def percent_formatter(decimals: int = 0) -> FuncFormatter:
    return FuncFormatter(lambda value, _pos: f"{value:.{decimals}f}%")


def gistemp_zonal_lines() -> None:
    df = pd.read_csv(DATA / "gistemp-zonal-rolling.csv")
    series = [
        ("Northern extratropics", "northern_extratropics_anomaly_c", TAB10["blue"]),
        ("Tropics", "tropics_anomaly_c", TAB10["orange"]),
        ("Southern extratropics", "southern_extratropics_anomaly_c", TAB10["green"]),
    ]

    fig, ax = plt.subplots(figsize=(6.8, 3.9))
    for label, column, color in series:
        ax.plot(df["year"], df[column], label=label, color=color, linewidth=1.8)

    ax.axhline(0, color="#666666", linewidth=0.9, linestyle="--", zorder=0)
    ax.set_xlabel("Year")
    ax.set_ylabel("Temperature anomaly (°C)")
    ax.xaxis.set_major_locator(MultipleLocator(20))
    ax.yaxis.set_major_locator(MultipleLocator(0.5))
    ax.legend(frameon=False, loc="upper left")
    ax.grid(axis="y")
    ax.grid(axis="x", visible=False)
    save(fig, "gistemp-zonal-lines.png")


def world_bank_urbanization_bars() -> None:
    df = pd.read_csv(DATA / "world-bank-urbanization-2024.csv")
    y = np.arange(len(df))

    fig, ax = plt.subplots(figsize=(7.2, 4.1))
    ax.barh(y, df["urban_population_percent"], color=TAB10["blue"], height=0.68)
    ax.set_yticks(y, df["region"])
    ax.invert_yaxis()
    ax.set_xlabel("Urban population (% of population)")
    ax.xaxis.set_major_formatter(percent_formatter(0))
    ax.set_xlim(0, max(90, float(df["urban_population_percent"].max()) + 8))
    ax.grid(axis="x")
    ax.grid(axis="y", visible=False)

    for i, value in enumerate(df["urban_population_percent"]):
        ax.text(value + 1.0, i, f"{value:.1f}%", va="center", ha="left", fontsize=8)

    save(fig, "world-bank-urbanization-bars.png")


def palmer_penguins_box() -> None:
    df = pd.read_csv(DATA / "palmer-penguins-body-mass.csv")
    order = ["Adelie", "Chinstrap", "Gentoo"]
    data = [df.loc[df["species"] == species, "body_mass_g"].to_numpy() for species in order]
    colors = [TAB10["blue"], TAB10["orange"], TAB10["green"]]

    fig, ax = plt.subplots(figsize=(5.7, 4.1))
    box = ax.boxplot(
        data,
        tick_labels=order,
        widths=0.55,
        patch_artist=True,
        medianprops={"color": "#222222", "linewidth": 1.2},
        boxprops={"linewidth": 1.0, "color": "#555555"},
        whiskerprops={"linewidth": 1.0, "color": "#555555"},
        capprops={"linewidth": 1.0, "color": "#555555"},
        flierprops={"marker": "", "markersize": 0},
    )
    for patch, color in zip(box["boxes"], colors, strict=True):
        patch.set_facecolor(color)
        patch.set_alpha(0.28)

    rng = np.random.default_rng(20260714)
    for i, values in enumerate(data, start=1):
        jitter = rng.uniform(-0.18, 0.18, size=len(values))
        ax.scatter(
            np.full(len(values), i) + jitter,
            values,
            s=13,
            color=colors[i - 1],
            alpha=0.58,
            linewidths=0,
        )

    ax.set_xlabel("Species")
    ax.set_ylabel("Body mass (g)")
    ax.grid(axis="y")
    ax.grid(axis="x", visible=False)
    save(fig, "palmer-penguins-box.png")


def wine_correlation_heatmap() -> None:
    df = pd.read_csv(DATA / "uci-red-wine-correlations.csv")
    variables = df["variable"].tolist()
    matrix = df.drop(columns=["variable"]).to_numpy()

    fig, ax = plt.subplots(figsize=(7.5, 6.6))
    image = ax.imshow(matrix, cmap="RdBu_r", vmin=-1, vmax=1, interpolation="nearest")
    ax.set_xticks(np.arange(len(variables)), variables, rotation=45, ha="right")
    ax.set_yticks(np.arange(len(variables)), variables)
    ax.tick_params(length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.grid(visible=False)
    ax.set_xticks(np.arange(-0.5, len(variables), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(variables), 1), minor=True)
    ax.grid(which="minor", color="white", linewidth=0.6)
    ax.tick_params(which="minor", bottom=False, left=False)

    cbar = fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label("Pearson correlation")
    cbar.set_ticks([-1, -0.5, 0, 0.5, 1])
    save(fig, "wine-correlation-heatmap.png")


def auto_mpg_scatter() -> None:
    df = pd.read_csv(DATA / "uci-auto-mpg.csv")
    groups = [("USA", TAB10["blue"]), ("Europe", TAB10["orange"]), ("Japan", TAB10["green"])]

    fig, ax = plt.subplots(figsize=(6.2, 4.4))
    for origin, color in groups:
        part = df[df["origin"] == origin]
        ax.scatter(
            part["weight_lb"],
            part["mpg"],
            label=origin,
            color=color,
            s=24,
            alpha=0.72,
            edgecolors="none",
        )

    ax.set_xlabel("Vehicle weight (lb)")
    ax.set_ylabel("Fuel economy (mpg)")
    ax.legend(title="Origin", frameon=False)
    ax.grid(axis="both")
    save(fig, "auto-mpg-scatter.png")


def usgs_earthquake_histogram() -> None:
    df = pd.read_csv(DATA / "usgs-2025-reviewed-m5.csv")
    values = df["magnitude"].to_numpy()
    max_edge = np.ceil((values.max() - 5.0) / 0.1) * 0.1 + 5.0 + 0.1
    bins = np.round(np.arange(5.0, max_edge + 0.0001, 0.1), 1)
    weights = np.full_like(values, 100 / len(values), dtype=float)

    fig, ax = plt.subplots(figsize=(6.3, 3.9))
    ax.hist(values, bins=bins, weights=weights, color=TAB10["purple"], edgecolor="white", linewidth=0.5)
    ax.set_xlabel("Magnitude")
    ax.set_ylabel("Events (%)")
    ax.yaxis.set_major_formatter(percent_formatter(0))
    ax.xaxis.set_major_locator(MultipleLocator(0.5))
    ax.grid(axis="y")
    ax.grid(axis="x", visible=False)
    save(fig, "usgs-earthquake-histogram.png")


def main() -> None:
    setup()
    gistemp_zonal_lines()
    world_bank_urbanization_bars()
    palmer_penguins_box()
    wine_correlation_heatmap()
    auto_mpg_scatter()
    usgs_earthquake_histogram()


if __name__ == "__main__":
    main()
