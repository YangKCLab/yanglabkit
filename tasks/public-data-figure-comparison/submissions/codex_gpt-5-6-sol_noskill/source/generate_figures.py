#!/usr/bin/env python3
"""Generate the six public-data figure comparison PNGs.

This submission is the intentionally skill-free baseline condition. It follows
the task's fixed data and output contract but does not use YangLabKit's figure
or colour skill guidance.
"""

from __future__ import annotations

from pathlib import Path
import textwrap

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.ticker import FuncFormatter, MultipleLocator, PercentFormatter
import numpy as np
import pandas as pd
import seaborn as sns


TASK_ROOT = Path(__file__).resolve().parents[3]
DATA = TASK_ROOT / "data"
OUTPUT = Path(__file__).resolve().parents[1] / "figures"
OUTPUT.mkdir(parents=True, exist_ok=True)

TEXT = "#202833"
MUTED = "#66717F"
GRID = "#D9DEE5"
ZERO = "#66717F"

OKABE_ITO_LINES = ["#0072B2", "#E69F00", "#009E73"]
BAR_BLUES = [
    "#DCEAF6",
    "#C6DBEF",
    "#9ECAE1",
    "#6BAED6",
    "#4292C6",
    "#2171B5",
    "#084594",
]
PENGUIN_COLORS = ["#56B4E9", "#E69F00", "#009E73"]
SCATTER_COLORS = {"USA": "#0072B2", "Europe": "#E69F00", "Japan": "#009E73"}
HEATMAP_ANCHORS = ["#2166AC", "#F7F7F7", "#B2182B"]
QUAKE_BLUES = [
    "#DCE9F2",
    "#C7DCEB",
    "#ABCBE1",
    "#83B2D2",
    "#5B97C2",
    "#367DB3",
    "#1E639B",
    "#114C7D",
]


plt.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "DejaVu Sans"],
        "font.size": 9,
        "text.color": TEXT,
        "axes.labelcolor": TEXT,
        "axes.edgecolor": "#7A8490",
        "axes.linewidth": 0.8,
        "axes.titlesize": 13,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.labelsize": 9.5,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "xtick.color": TEXT,
        "ytick.color": TEXT,
        "xtick.labelsize": 8.5,
        "ytick.labelsize": 8.5,
        "legend.fontsize": 8.5,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
        "savefig.bbox": "tight",
    }
)


def subtitle(ax: plt.Axes, value: str) -> None:
    """Place compact context immediately above an axes."""
    ax.text(
        0,
        1.015,
        value,
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=8,
        color=MUTED,
    )


def grid(ax: plt.Axes, axis: str = "y") -> None:
    ax.set_axisbelow(True)
    ax.grid(axis=axis, color=GRID, linewidth=0.65, linestyle=(0, (2.5, 2.5)))


def save(fig: plt.Figure, filename: str) -> None:
    fig.savefig(OUTPUT / filename, dpi=300, bbox_inches="tight", pad_inches=0.09)
    plt.close(fig)


def gistemp_lines() -> None:
    data = pd.read_csv(DATA / "gistemp-zonal-rolling.csv")
    series = [
        (
            "northern_extratropics_anomaly_c",
            "Northern extratropics",
            OKABE_ITO_LINES[0],
            "-",
        ),
        ("tropics_anomaly_c", "Tropics", OKABE_ITO_LINES[1], (0, (5, 2))),
        (
            "southern_extratropics_anomaly_c",
            "Southern extratropics",
            OKABE_ITO_LINES[2],
            (0, (1.5, 1.5)),
        ),
    ]

    fig, ax = plt.subplots(figsize=(6.2, 3.75))
    for column, label, color, line_style in series:
        ax.plot(
            data["year"],
            data[column],
            color=color,
            linestyle=line_style,
            linewidth=2.0,
            label=label,
        )
    ax.axhline(0, color=ZERO, linewidth=0.9, linestyle=(0, (4, 3)), zorder=0)
    ax.set_title("Temperature anomaly by latitude band", pad=21)
    subtitle(ax, "NASA GISTEMP v4 · centered 5-year mean")
    ax.set_xlabel("Year")
    ax.set_ylabel("Temperature anomaly (°C)")
    ax.set_xlim(data["year"].min(), data["year"].max())
    ax.xaxis.set_major_locator(MultipleLocator(20))
    ax.yaxis.set_major_locator(MultipleLocator(0.5))
    grid(ax)
    ax.legend(frameon=False, loc="upper left", ncol=1, handlelength=3.0)
    fig.tight_layout()
    save(fig, "gistemp-zonal-lines.png")


def urbanization_bars() -> None:
    data = pd.read_csv(DATA / "world-bank-urbanization-2024.csv")
    labels = [
        textwrap.fill(label, width=30, break_long_words=False)
        for label in data["region"]
    ]

    fig, ax = plt.subplots(figsize=(6.4, 4.25))
    bars = ax.barh(
        np.arange(len(data)),
        data["urban_population_percent"],
        color=BAR_BLUES,
        edgecolor="white",
        linewidth=0.7,
        height=0.68,
    )
    ax.set_yticks(np.arange(len(data)), labels=labels)
    ax.invert_yaxis()
    ax.set_title("Urban population by region", pad=21)
    subtitle(ax, "World Bank regional aggregates · 2024")
    ax.set_xlabel("Urban population (% of population)")
    ax.set_xlim(0, 91)
    ax.xaxis.set_major_locator(MultipleLocator(20))
    ax.xaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))
    grid(ax, axis="x")
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0)
    for bar, value in zip(bars, data["urban_population_percent"], strict=True):
        ax.text(
            value + 1.0,
            bar.get_y() + bar.get_height() / 2,
            f"{value:.1f}%",
            va="center",
            ha="left",
            fontsize=8.3,
            color=TEXT,
        )
    fig.tight_layout()
    save(fig, "world-bank-urbanization-bars.png")


def penguin_boxplot() -> None:
    data = pd.read_csv(DATA / "palmer-penguins-body-mass.csv")
    order = ["Adelie", "Chinstrap", "Gentoo"]
    values = [data.loc[data["species"] == species, "body_mass_g"].to_numpy() for species in order]
    rng = np.random.default_rng(20260714)

    fig, ax = plt.subplots(figsize=(5.6, 4.15))
    boxes = ax.boxplot(
        values,
        tick_labels=order,
        widths=0.52,
        patch_artist=True,
        showfliers=False,
        medianprops={"color": TEXT, "linewidth": 1.5},
        whiskerprops={"color": "#68727E", "linewidth": 1.0},
        capprops={"color": "#68727E", "linewidth": 1.0},
    )
    for patch, color in zip(boxes["boxes"], PENGUIN_COLORS, strict=True):
        patch.set_facecolor(color)
        patch.set_alpha(0.27)
        patch.set_edgecolor(color)
        patch.set_linewidth(1.4)

    for position, (points, color) in enumerate(zip(values, PENGUIN_COLORS, strict=True), start=1):
        jitter = rng.uniform(-0.19, 0.19, size=len(points))
        ax.scatter(
            np.full(len(points), position) + jitter,
            points,
            s=14,
            color=color,
            alpha=0.55,
            edgecolor="white",
            linewidth=0.25,
            zorder=3,
        )
    ax.set_title("Penguin body mass by species", pad=21)
    subtitle(ax, "Palmer Penguins · every observation shown (n = 342)")
    ax.set_xlabel("Species")
    ax.set_ylabel("Body mass (g)")
    ax.yaxis.set_major_locator(MultipleLocator(500))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value:,.0f}"))
    grid(ax)
    fig.tight_layout()
    save(fig, "palmer-penguins-box.png")


def wine_heatmap() -> None:
    correlations = pd.read_csv(DATA / "uci-red-wine-correlations.csv", index_col="variable")
    cmap = LinearSegmentedColormap.from_list("custom_blue_white_red", HEATMAP_ANCHORS)

    fig, ax = plt.subplots(figsize=(7.35, 6.15))
    heatmap = sns.heatmap(
        correlations,
        ax=ax,
        cmap=cmap,
        vmin=-1,
        vmax=1,
        center=0,
        square=True,
        linewidths=0.4,
        linecolor="white",
        cbar_kws={
            "label": "Pearson correlation",
            "ticks": [-1, -0.5, 0, 0.5, 1],
            "shrink": 0.78,
            "pad": 0.03,
        },
    )
    ax.set_title("Red-wine variable correlations", pad=21)
    subtitle(ax, "UCI Wine Quality · Pearson correlation matrix")
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=42, ha="right", rotation_mode="anchor")
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
    ax.tick_params(axis="both", length=0, labelsize=7.5)
    heatmap.collections[0].colorbar.ax.tick_params(labelsize=8)
    heatmap.collections[0].colorbar.ax.yaxis.label.set_size(8.5)
    fig.tight_layout()
    save(fig, "wine-correlation-heatmap.png")


def auto_mpg_scatter() -> None:
    data = pd.read_csv(DATA / "uci-auto-mpg.csv")
    markers = {"USA": "o", "Europe": "s", "Japan": "^"}

    fig, ax = plt.subplots(figsize=(5.9, 4.05))
    for origin in ["USA", "Europe", "Japan"]:
        group = data.loc[data["origin"] == origin]
        ax.scatter(
            group["weight_lb"],
            group["mpg"],
            label=origin,
            marker=markers[origin],
            color=SCATTER_COLORS[origin],
            s=27,
            alpha=0.72,
            edgecolor="white",
            linewidth=0.4,
        )
    ax.set_title("Fuel economy and vehicle weight", pad=21)
    subtitle(ax, "UCI Auto MPG · 398 vehicles")
    ax.set_xlabel("Vehicle weight (lb)")
    ax.set_ylabel("Fuel economy (mpg)")
    ax.xaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value:,.0f}"))
    ax.yaxis.set_major_locator(MultipleLocator(5))
    grid(ax)
    ax.legend(title="Origin", frameon=False, loc="upper right", borderaxespad=0.2)
    fig.tight_layout()
    save(fig, "auto-mpg-scatter.png")


def earthquake_histogram() -> None:
    data = pd.read_csv(DATA / "usgs-2025-reviewed-m5.csv")
    maximum = np.ceil(data["magnitude"].max() * 10) / 10
    edges = np.arange(5.0, maximum + 0.1001, 0.1)
    counts, _ = np.histogram(data["magnitude"], bins=edges)
    percentages = counts / len(data) * 100
    color_indices = np.floor(np.linspace(0, len(QUAKE_BLUES) - 1, len(counts))).astype(int)
    colors = [QUAKE_BLUES[index] for index in color_indices]

    fig, ax = plt.subplots(figsize=(5.9, 4.05))
    ax.bar(
        edges[:-1],
        percentages,
        width=0.096,
        align="edge",
        color=colors,
        edgecolor="white",
        linewidth=0.35,
    )
    ax.set_title("Magnitude distribution of reviewed earthquakes", pad=21)
    subtitle(ax, "USGS/ANSS · 2025 · M≥5 · n = 2,128")
    ax.set_xlabel("Magnitude")
    ax.set_ylabel("Percentage of events")
    ax.set_xlim(5.0, edges[-1])
    ax.xaxis.set_major_locator(MultipleLocator(0.5))
    ax.yaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))
    grid(ax)
    fig.tight_layout()
    save(fig, "usgs-earthquake-histogram.png")


def main() -> None:
    gistemp_lines()
    urbanization_bars()
    penguin_boxplot()
    wine_heatmap()
    auto_mpg_scatter()
    earthquake_histogram()


if __name__ == "__main__":
    main()
