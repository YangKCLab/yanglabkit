# Frozen task inputs

These CSVs are small, derived, plot-ready snapshots for
`yanglabkit-public-data-figures-v1`. They exist to give every candidate generator
identical inputs. They are not intended as general-purpose redistributions of
the upstream datasets.

[`manifest.json`](manifest.json) records row counts, columns, file checksums,
upstream URLs, upstream download checksums, reuse terms, and transformations.
The committed CSV checksums are used by task version `1.2.0`; a future refresh
must bump the task version and regenerate the manifest.

## Sources and attribution

- **NASA GISTEMP v4:** zonal annual temperature anomalies, credited to NASA
  GISS/GISTEMP. NASA requests citation of the dataset webpage, access date, and
  current scholarly publication for derived graphics. Do not describe this
  input as CC0.
- **World Bank WDI:** `SP.URB.TOTL.IN.ZS`, seven standard regional aggregates,
  2024. The selected indicator is published under CC BY 4.0; credit the World
  Bank and disclose that this task uses a transformed snapshot.
- **Palmer Penguins:** CC0; cite Horst, Hill, and Gorman and the original Palmer
  Station LTER/EDI sources.
- **UCI Wine Quality:** CC BY 4.0; credit Cortez et al. and the UCI Machine
  Learning Repository, DOI `10.24432/C56S3T`.
- **UCI Auto MPG:** CC BY 4.0; credit Quinlan and the UCI Machine Learning
  Repository, DOI `10.24432/C5859H`.
- **USGS Earthquake Catalog / ANSS:** public domain; credit USGS/ANSS and retain
  the fixed query and snapshot date.

## Regeneration

`prepare_inputs.py` uses the Python standard library and falls back to `curl`
when the local Python TLS stack cannot reach an upstream source. It is a
maintainer tool, not part of a candidate run. Run it through the locked task
environment from `tasks/public-data-figure-comparison/`:

```bash
uv sync --frozen
uv run --frozen python prepare_inputs.py
```

Upstream products can be revised. Regenerating at a later date creates a new
benchmark input set even if filenames stay the same; review the diff and bump
`task_version` before accepting it.
