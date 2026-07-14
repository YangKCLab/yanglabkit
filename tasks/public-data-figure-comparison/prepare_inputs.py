#!/usr/bin/env python3
"""Fetch authoritative sources and rebuild the frozen plot-ready task inputs."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import math
import shutil
import shlex
import subprocess
import urllib.error
import urllib.request
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
SNAPSHOT_DATE = "2026-07-13"

SOURCES = {
    "gistemp": {
        "name": "NASA GISTEMP v4 zonal annual means",
        "url": "https://data.giss.nasa.gov/gistemp/tabledata_v4/ZonAnn.Ts+dSST.csv",
        "landing_page": "https://data.giss.nasa.gov/gistemp/",
        "reuse": "NASA GISS/GISTEMP derived-graphic permission with requested citation and credit; not labeled CC0",
    },
    "world_bank": {
        "name": "World Bank WDI urban population (% of total population)",
        "url": "https://api.worldbank.org/v2/country/EAS;ECS;LCN;MEA;NAC;SAS;SSF/indicator/SP.URB.TOTL.IN.ZS?date=2024&format=json&per_page=100",
        "landing_page": "https://data.worldbank.org/indicator/SP.URB.TOTL.IN.ZS",
        "reuse": "CC BY 4.0",
    },
    "penguins": {
        "name": "Palmer Penguins",
        "url": "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv",
        "landing_page": "https://allisonhorst.github.io/palmerpenguins/",
        "reuse": "CC0 with scholarly attribution requested",
    },
    "wine": {
        "name": "UCI Wine Quality",
        "url": "https://archive.ics.uci.edu/static/public/186/wine+quality.zip",
        "landing_page": "https://archive.ics.uci.edu/dataset/186/wine+quality",
        "doi": "10.24432/C56S3T",
        "reuse": "CC BY 4.0",
    },
    "auto_mpg": {
        "name": "UCI Auto MPG",
        "url": "https://archive.ics.uci.edu/static/public/9/auto+mpg.zip",
        "landing_page": "https://archive.ics.uci.edu/dataset/9/auto",
        "doi": "10.24432/C5859H",
        "reuse": "CC BY 4.0",
    },
    "usgs": {
        "name": "USGS Earthquake Catalog / ANSS",
        "url": "https://earthquake.usgs.gov/fdsnws/event/1/query.csv?starttime=2025-01-01&endtime=2026-01-01&minmagnitude=5&eventtype=earthquake&reviewstatus=reviewed&orderby=time-asc&limit=20000",
        "landing_page": "https://earthquake.usgs.gov/fdsnws/event/1/",
        "reuse": "Public domain; credit USGS/ANSS",
    },
}

TRANSFORMATIONS = {
    "gistemp": "Selected 24N-90N, 24S-24N, and 90S-24S annual anomalies; calculated centered five-year means; dropped the two edge years on each side.",
    "world_bank": "Selected seven standard regional aggregates for indicator SP.URB.TOTL.IN.ZS in 2024 and sorted them by value ascending.",
    "penguins": "Selected species and body_mass_g and removed the two observations with missing body mass.",
    "wine": "Selected the red-wine file and calculated the Pearson correlation matrix for its 11 physicochemical variables plus quality in source-column order.",
    "auto_mpg": "Selected mpg, weight, and origin; mapped origin codes 1/2/3 to USA/Europe/Japan.",
    "usgs": "Queried reviewed global earthquakes from 2025-01-01 through 2026-01-01 with M≥5 and retained event ID, time, preferred magnitude, and magnitude type.",
}


def download(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "yanglabkit-task-builder/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            return response.read()
    except urllib.error.URLError:
        curl = shutil.which("curl")
        if curl is None:
            raise
        return subprocess.run(
            [curl, "--location", "--fail", "--silent", "--show-error", url],
            check=True,
            stdout=subprocess.PIPE,
        ).stdout


def digest_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def digest_file(path: Path) -> str:
    return digest_bytes(path.read_bytes())


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def pearson(xs: list[float], ys: list[float]) -> float:
    mean_x = sum(xs) / len(xs)
    mean_y = sum(ys) / len(ys)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    denominator = math.sqrt(
        sum((x - mean_x) ** 2 for x in xs) * sum((y - mean_y) ** 2 for y in ys)
    )
    return numerator / denominator


def prepare_gistemp(content: bytes) -> tuple[str, list[str], int]:
    source_rows = list(csv.DictReader(io.StringIO(content.decode("utf-8-sig"))))
    series = [
        ("24N-90N", "northern_extratropics_anomaly_c"),
        ("24S-24N", "tropics_anomaly_c"),
        ("90S-24S", "southern_extratropics_anomaly_c"),
    ]
    rows: list[dict[str, object]] = []
    for index in range(2, len(source_rows) - 2):
        output: dict[str, object] = {"year": source_rows[index]["Year"]}
        window = source_rows[index - 2 : index + 3]
        for source_name, output_name in series:
            output[output_name] = f"{sum(float(row[source_name]) for row in window) / 5:.3f}"
        rows.append(output)
    filename = "gistemp-zonal-rolling.csv"
    fields = ["year", *(name for _, name in series)]
    write_csv(DATA_DIR / filename, fields, rows)
    return filename, fields, len(rows)


def prepare_world_bank(content: bytes) -> tuple[str, list[str], int]:
    payload = json.loads(content)
    values = payload[1]
    rows = [
        {
            "region_code": item["countryiso3code"],
            "region": item["country"]["value"],
            "year": item["date"],
            "urban_population_percent": f"{float(item['value']):.6f}",
        }
        for item in values
    ]
    rows.sort(key=lambda row: float(row["urban_population_percent"]))
    filename = "world-bank-urbanization-2024.csv"
    fields = ["region_code", "region", "year", "urban_population_percent"]
    write_csv(DATA_DIR / filename, fields, rows)
    return filename, fields, len(rows)


def prepare_penguins(content: bytes) -> tuple[str, list[str], int]:
    source_rows = csv.DictReader(io.StringIO(content.decode("utf-8-sig")))
    rows = []
    for observation_id, row in enumerate(source_rows, start=1):
        if row["species"] in ("", "NA") or row["body_mass_g"] in ("", "NA"):
            continue
        rows.append(
            {
                "observation_id": observation_id,
                "species": row["species"],
                "body_mass_g": row["body_mass_g"],
            }
        )
    filename = "palmer-penguins-body-mass.csv"
    fields = ["observation_id", "species", "body_mass_g"]
    write_csv(DATA_DIR / filename, fields, rows)
    return filename, fields, len(rows)


def prepare_wine(content: bytes) -> tuple[str, list[str], int]:
    with zipfile.ZipFile(io.BytesIO(content)) as archive:
        red_csv = archive.read("winequality-red.csv").decode("utf-8-sig")
    source_rows = list(csv.DictReader(io.StringIO(red_csv), delimiter=";"))
    variables = list(source_rows[0])
    columns = {name: [float(row[name]) for row in source_rows] for name in variables}
    rows = []
    for row_name in variables:
        output: dict[str, object] = {"variable": row_name}
        for column_name in variables:
            output[column_name] = f"{pearson(columns[row_name], columns[column_name]):.6f}"
        rows.append(output)
    filename = "uci-red-wine-correlations.csv"
    fields = ["variable", *variables]
    write_csv(DATA_DIR / filename, fields, rows)
    return filename, fields, len(rows)


def prepare_auto_mpg(content: bytes) -> tuple[str, list[str], int]:
    with zipfile.ZipFile(io.BytesIO(content)) as archive:
        source_text = archive.read("auto-mpg.data").decode("utf-8-sig")
    origins = {"1": "USA", "2": "Europe", "3": "Japan"}
    rows = []
    for observation_id, line in enumerate(source_text.splitlines(), start=1):
        if not line.strip():
            continue
        fields = shlex.split(line)
        rows.append(
            {
                "observation_id": observation_id,
                "mpg": fields[0],
                "weight_lb": fields[4],
                "origin": origins[fields[7]],
            }
        )
    filename = "uci-auto-mpg.csv"
    output_fields = ["observation_id", "mpg", "weight_lb", "origin"]
    write_csv(DATA_DIR / filename, output_fields, rows)
    return filename, output_fields, len(rows)


def prepare_usgs(content: bytes) -> tuple[str, list[str], int]:
    source_rows = csv.DictReader(io.StringIO(content.decode("utf-8-sig")))
    rows = []
    for row in source_rows:
        if row["status"] != "reviewed" or row["type"] != "earthquake":
            continue
        magnitude = float(row["mag"])
        if magnitude < 5 or not row["time"].startswith("2025-"):
            continue
        rows.append(
            {
                "event_id": row["id"],
                "time_utc": row["time"],
                "magnitude": f"{magnitude:.3f}",
                "magnitude_type": row["magType"],
            }
        )
    filename = "usgs-2025-reviewed-m5.csv"
    fields = ["event_id", "time_utc", "magnitude", "magnitude_type"]
    write_csv(DATA_DIR / filename, fields, rows)
    return filename, fields, len(rows)


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    builders = {
        "gistemp": prepare_gistemp,
        "world_bank": prepare_world_bank,
        "penguins": prepare_penguins,
        "wine": prepare_wine,
        "auto_mpg": prepare_auto_mpg,
        "usgs": prepare_usgs,
    }
    files = []
    sources = {}
    for source_id, builder in builders.items():
        metadata = SOURCES[source_id]
        content = download(metadata["url"])
        filename, columns, row_count = builder(content)
        files.append(
            {
                "file": filename,
                "source_id": source_id,
                "rows": row_count,
                "columns": columns,
                "sha256": digest_file(DATA_DIR / filename),
                "transformation": TRANSFORMATIONS[source_id],
            }
        )
        sources[source_id] = {
            **metadata,
            "snapshot_date": SNAPSHOT_DATE,
            "upstream_sha256": digest_bytes(content),
        }
        print(f"wrote {filename}: {row_count} rows")

    manifest = {
        "schema_version": 1,
        "task_id": "yanglabkit-public-data-figures-v1",
        "task_version": "1.1.0",
        "snapshot_date": SNAPSHOT_DATE,
        "files": files,
        "sources": sources,
    }
    (DATA_DIR / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print("wrote manifest.json")


if __name__ == "__main__":
    main()
