#!/usr/bin/env python3
"""Generate the six YangLabKit public-data comparison figures."""

from __future__ import annotations

import json
import textwrap
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import pandas as pd
import seaborn as sns


SOURCE_DIR = Path(__file__).resolve().parent
SUBMISSION_DIR = SOURCE_DIR.parent
TASK_DIR = SUBMISSION_DIR.parents[1]
REPO_DIR = TASK_DIR.parents[1]
DATA_DIR = TASK_DIR / "data"
FIGURE_DIR = SUBMISSION_DIR / "figures"
SCICOLOR_DIR = REPO_DIR / "skills" / "yanglabkit-scicolor" / "data"

BASE_SIZE = 9
SMALL_SIZE = 8

plt.rcParams.update(
    {
        "font.size": BASE_SIZE,
        "axes.labelsize": BASE_SIZE,
        "axes.titlesize": BASE_SIZE,
        "xtick.labelsize": BASE_SIZE,
        "ytick.labelsize": BASE_SIZE,
        "legend.fontsize": SMALL_SIZE,
        "axes.axisbelow": True,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
    }
)


def discrete_palette(collection: str, name: str) -> list[str]:
    """Read an exact discrete palette from the bundled scicolor snapshot."""
    collections = json.loads((SCICOLOR_DIR / "colors.json").read_text())
    for item in collections:
        if item["collection"] != collection:
            continue
        for scheme in item["color_schemes"]:
            if scheme["name"] == name:
                return scheme["colors"]
    raise KeyError(f"Unknown palette: {collection} / {name}")


def continuous_palette(name: str) -> list[str]:
    """Read exact colormap stops from the bundled scicolor snapshot."""
    maps = json.loads((SCICOLOR_DIR / "continuous-colormaps.json").read_text())
    for item in maps:
        if item["name"] == name:
            assert item["perceptually_uniform"]
            assert item["color_blind_friendly"]
            return item["stops"]
    raise KeyError(f"Unknown continuous palette: {name}")


OKABE_ITO = discrete_palette("Masataka Okabe", "Color Blind")
BATLOW_10 = discrete_palette("Scientific colour", "batlow 10")
VIK = continuous_palette("vik")
GRAY_C = continuous_palette("grayC")

INK = GRAY_C[4]
GRID = GRAY_C[22]
REFERENCE = GRAY_C[17]
WHITE = GRAY_C[-1]


def style_quantitative_axes(ax: mpl.axes.Axes, grid_axis: str = "y") -> None:
    """Apply the line/scatter/distribution spine and grid conventions."""
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(INK)
    ax.spines["bottom"].set_color(INK)
    ax.tick_params(colors=INK)
    ax.grid(
        True,
        axis=grid_axis,
        color=GRID,
        alpha=0.28,
        linestyle="--",
        linewidth=0.7,
    )


def save_figure(fig: mpl.figure.Figure, filename: str) -> None:
    """Save a gallery-ready PNG using the task-specific export contract."""
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / filename, dpi=300, bbox_inches="tight")
    plt.close(fig)


def generate_gistemp() -> None:
    df = pd.read_csv(DATA_DIR / "gistemp-zonal-rolling.csv")
    expected = [
        "year",
        "northern_extratropics_anomaly_c",
        "tropics_anomaly_c",
        "southern_extratropics_anomaly_c",
    ]
    assert df.columns.tolist() == expected and len(df) == 142

    series = [
        (expected[1], "Northern extratropics", OKABE_ITO[5], "-"),
        (expected[2], "Tropics", OKABE_ITO[1], "--"),
        (expected[3], "Southern extratropics", OKABE_ITO[3], ":"),
    ]

    fig, ax = plt.subplots(figsize=(4.8, 3.15))
    for column, label, color, linestyle in series:
        ax.plot(
            df["year"],
            df[column],
            color=color,
            linestyle=linestyle,
            linewidth=1.7,
            label=label,
        )
    ax.axhline(0, color=REFERENCE, linestyle="--", linewidth=1.1, alpha=0.9)
    style_quantitative_axes(ax, "y")
    ax.set_xlim(1880, 2025)
    ax.set_xticks([1880, 1920, 1960, 2000, 2020])
    ax.set_ylim(-0.65, 2.05)
    ax.set_yticks([-0.5, 0.0, 0.5, 1.0, 1.5, 2.0])
    ax.set_xlabel("Year")
    ax.set_ylabel("Temperature anomaly (°C)")
    ax.set_title("Zonal temperature anomalies", fontweight="bold", loc="left")
    ax.legend(frameon=False, labelspacing=0.2, loc="upper left")
    save_figure(fig, "gistemp-zonal-lines.png")


def generate_urbanization() -> None:
    df = pd.read_csv(DATA_DIR / "world-bank-urbanization-2024.csv")
    assert len(df) == 7
    assert df["urban_population_percent"].is_monotonic_increasing
    palette_indices = np.linspace(0, len(BATLOW_10) - 1, len(df), dtype=int)
    colors = [BATLOW_10[index] for index in palette_indices]
    labels = [textwrap.fill(label, width=25) for label in df["region"]]

    fig, ax = plt.subplots(figsize=(5.0, 3.75))
    y = np.arange(len(df))
    bars = ax.barh(y, df["urban_population_percent"], color=colors, height=0.66)
    ax.set_yticks(y, labels=labels)
    ax.invert_yaxis()
    for bar, value in zip(bars, df["urban_population_percent"], strict=True):
        ax.text(
            value + 1.0,
            bar.get_y() + bar.get_height() / 2,
            f"{value:.1f}%",
            va="center",
            ha="left",
            color=INK,
            fontsize=SMALL_SIZE,
        )

    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(INK)
    ax.tick_params(axis="y", length=0, colors=INK)
    ax.tick_params(axis="x", colors=INK)
    ax.grid(
        True,
        axis="x",
        color=GRID,
        alpha=0.28,
        linestyle="--",
        linewidth=0.7,
    )
    ax.set_xlim(0, 102)
    ax.set_xticks([0, 20, 40, 60, 80, 100])
    ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=100, decimals=0))
    ax.set_xlabel("Urban population")
    ax.set_title("Regional urbanization in 2024", fontweight="bold", loc="left")
    save_figure(fig, "world-bank-urbanization-bars.png")


def generate_penguins() -> None:
    df = pd.read_csv(DATA_DIR / "palmer-penguins-body-mass.csv")
    species = ["Adelie", "Chinstrap", "Gentoo"]
    assert len(df) == 342 and set(df["species"]) == set(species)
    colors = [OKABE_ITO[1], OKABE_ITO[2], OKABE_ITO[3]]
    groups = [df.loc[df["species"] == name, "body_mass_g"].to_numpy() for name in species]

    fig, ax = plt.subplots(figsize=(4.1, 3.35))
    boxes = ax.boxplot(
        groups,
        tick_labels=species,
        patch_artist=True,
        widths=0.58,
        showfliers=False,
        medianprops={"color": INK, "linewidth": 1.4},
        whiskerprops={"color": INK, "linewidth": 1.0},
        capprops={"color": INK, "linewidth": 1.0},
        boxprops={"edgecolor": INK, "linewidth": 0.9},
    )
    for patch, color in zip(boxes["boxes"], colors, strict=True):
        patch.set_facecolor(color)
        patch.set_alpha(0.78)

    rng = np.random.default_rng(20260714)
    for position, (values, color) in enumerate(zip(groups, colors, strict=True), start=1):
        jitter = rng.uniform(-0.18, 0.18, size=len(values))
        ax.scatter(
            position + jitter,
            values,
            s=13,
            color=color,
            alpha=0.52,
            edgecolors="none",
            zorder=3,
        )

    style_quantitative_axes(ax, "y")
    ax.set_ylim(2500, 6650)
    ax.set_yticks([3000, 4000, 5000, 6000, 6500])
    ax.yaxis.set_major_formatter(mtick.StrMethodFormatter("{x:,.0f}"))
    ax.set_xlabel("Species")
    ax.set_ylabel("Body mass (g)")
    ax.set_title("Palmer penguin body mass", fontweight="bold", loc="left")
    save_figure(fig, "palmer-penguins-box.png")


def generate_wine_heatmap() -> None:
    raw = pd.read_csv(DATA_DIR / "uci-red-wine-correlations.csv")
    labels = raw["variable"].tolist()
    matrix = raw.drop(columns="variable")
    assert labels == matrix.columns.tolist() and matrix.shape == (12, 12)
    assert np.allclose(matrix.to_numpy(), matrix.to_numpy().T)

    wrapped_y = [textwrap.fill(label, width=13) for label in labels]
    cmap = mpl.colors.LinearSegmentedColormap.from_list("vik", VIK, N=256)
    fig, ax = plt.subplots(figsize=(5.2, 5.25))
    heatmap = sns.heatmap(
        matrix,
        ax=ax,
        cmap=cmap,
        vmin=-1,
        vmax=1,
        center=0,
        square=True,
        linewidths=0.35,
        linecolor=WHITE,
        xticklabels=labels,
        yticklabels=wrapped_y,
        cbar_kws={
            "label": "Pearson correlation",
            "ticks": [-1, -0.5, 0, 0.5, 1],
            "shrink": 0.78,
            "pad": 0.03,
        },
    )
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(axis="both", length=0, labelsize=BASE_SIZE)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha="center", va="top")
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_title("Red-wine variable correlations", fontweight="bold", loc="left")
    colorbar = heatmap.collections[0].colorbar
    colorbar.ax.tick_params(length=0, labelsize=BASE_SIZE, colors=INK)
    colorbar.set_label("Pearson correlation", fontsize=BASE_SIZE)
    colorbar.outline.set_visible(False)
    save_figure(fig, "wine-correlation-heatmap.png")


def generate_auto_mpg() -> None:
    df = pd.read_csv(DATA_DIR / "uci-auto-mpg.csv")
    origin_order = ["USA", "Europe", "Japan"]
    assert len(df) == 398 and set(df["origin"]) == set(origin_order)
    colors = [OKABE_ITO[5], OKABE_ITO[1], OKABE_ITO[3]]
    markers = ["o", "s", "^"]

    fig, ax = plt.subplots(figsize=(4.6, 3.35))
    for origin, color, marker in zip(origin_order, colors, markers, strict=True):
        group = df[df["origin"] == origin]
        ax.scatter(
            group["weight_lb"],
            group["mpg"],
            s=25,
            marker=marker,
            color=color,
            alpha=0.66,
            edgecolors="none",
            label=origin,
        )
    style_quantitative_axes(ax, "y")
    ax.set_xlim(1400, 5600)
    ax.set_xticks([1500, 2500, 3500, 4500, 5500])
    ax.xaxis.set_major_formatter(mtick.StrMethodFormatter("{x:,.0f}"))
    ax.set_ylim(7, 51)
    ax.set_yticks([10, 20, 30, 40, 50])
    ax.set_xlabel("Vehicle weight (lb)")
    ax.set_ylabel("Fuel economy (mpg)")
    ax.set_title("Vehicle weight and fuel economy", fontweight="bold", loc="left")
    ax.legend(frameon=False, labelspacing=0.2, loc="upper right")
    save_figure(fig, "auto-mpg-scatter.png")


def generate_earthquakes() -> None:
    df = pd.read_csv(DATA_DIR / "usgs-2025-reviewed-m5.csv")
    values = df["magnitude"].to_numpy()
    assert len(values) == 2128 and values.min() >= 5.0
    last_edge = np.ceil(values.max() * 10) / 10 + 0.1
    bins = np.arange(5.0, last_edge + 1e-9, 0.1)
    weights = np.full(values.shape, 100 / len(values))

    fig, ax = plt.subplots(figsize=(4.6, 3.25))
    _, edges, patches = ax.hist(
        values,
        bins=bins,
        weights=weights,
        edgecolor=INK,
        linewidth=0.25,
    )
    centers = (edges[:-1] + edges[1:]) / 2
    normalized = (centers - bins[0]) / (bins[-1] - bins[0])
    for patch, position in zip(patches, normalized, strict=True):
        index = min(int(np.floor(position * len(BATLOW_10))), len(BATLOW_10) - 1)
        patch.set_facecolor(BATLOW_10[index])

    style_quantitative_axes(ax, "y")
    ax.set_xticks([5, 6, 7, 8, 9])
    ax.set_xlim(4.95, 9.05)
    ax.set_ylim(0, 31)
    ax.set_yticks([0, 5, 10, 15, 20, 25, 30])
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=100, decimals=0))
    ax.set_xlabel("Magnitude")
    ax.set_ylabel("Percentage of events")
    ax.set_title(r"Reviewed $M \geq 5$ earthquakes in 2025", fontweight="bold", loc="left")
    save_figure(fig, "usgs-earthquake-histogram.png")


def main() -> None:
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    generate_gistemp()
    generate_urbanization()
    generate_penguins()
    generate_wine_heatmap()
    generate_auto_mpg()
    generate_earthquakes()


if __name__ == "__main__":
    main()
