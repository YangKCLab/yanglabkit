#!/usr/bin/env python3
"""Build a blinded local HTML comparison from valid candidate submissions."""

from __future__ import annotations

import argparse
import html
import json
import os
import shutil
import string
import sys
from pathlib import Path

from validate_submission import ROOT, validate_submission


def candidate_label(index: int) -> str:
    if index < len(string.ascii_uppercase):
        return f"Candidate {string.ascii_uppercase[index]}"
    return f"Candidate {index + 1}"


def build(submissions_dir: Path, output_dir: Path) -> tuple[int, list[str]]:
    task = json.loads((ROOT / "task.json").read_text(encoding="utf-8"))
    accepted = []
    skipped = []
    if submissions_dir.is_dir():
        for path in sorted(item for item in submissions_dir.iterdir() if item.is_dir()):
            errors, warnings, metadata = validate_submission(path)
            if errors:
                skipped.append(f"{path.name}: {len(errors)} validation error(s)")
                continue
            accepted.append((path, metadata, warnings))
    if not accepted:
        raise ValueError("no validator-passing submissions found")

    output_dir.mkdir(parents=True, exist_ok=True)
    labels = {path.name: candidate_label(index) for index, (path, _, _) in enumerate(accepted)}
    identity_key = {
        "task_id": task["task_id"],
        "candidates": [
            {
                "label": labels[path.name],
                "submission_id": path.name,
                "generator": metadata.get("generator", {}),
            }
            for path, metadata, _ in accepted
        ],
    }
    (output_dir / "identity-key.json").write_text(
        json.dumps(identity_key, indent=2) + "\n", encoding="utf-8"
    )

    headers = "".join(f"<th>{html.escape(labels[path.name])}</th>" for path, _, _ in accepted)
    rows = []
    for figure in task["figures"]:
        cells = []
        for candidate_index, (path, metadata, warnings) in enumerate(accepted):
            entry = metadata["figures"][figure["id"]]
            image_path = path / entry["file"]
            blind_directory = output_dir / "assets" / f"slot-{candidate_index + 1:03d}"
            blind_directory.mkdir(parents=True, exist_ok=True)
            blind_image = blind_directory / figure["output"]
            shutil.copy2(image_path, blind_image)
            relative_image = os.path.relpath(blind_image, output_dir)
            palette = entry["palette"]
            warning_text = ""
            if warnings:
                warning_text = f'<p class="warning">{len(warnings)} validator warning(s)</p>'
            cells.append(
                "<td>"
                f'<a href="{html.escape(relative_image)}">'
                f'<img src="{html.escape(relative_image)}" alt="{html.escape(entry["alt_text"])}"></a>'
                f'<p><strong>{html.escape(palette["name"])}</strong> '
                f'({html.escape(palette["class"])})</p>'
                f'<details><summary>Alt text</summary><p>{html.escape(entry["alt_text"])}</p></details>'
                f"{warning_text}</td>"
            )
        rows.append(f'<tr><th scope="row">{html.escape(figure["id"])}</th>{"".join(cells)}</tr>')

    document = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>YangLabKit figure candidates</title>
<style>
body {{ font-family: system-ui, sans-serif; margin: 2rem; color: #202124; }}
.notice {{ max-width: 72rem; padding: 1rem; background: #f3f5f7; border-left: 4px solid #59636e; }}
.table-wrap {{ overflow-x: auto; }}
table {{ border-collapse: collapse; min-width: 100%; table-layout: fixed; }}
th, td {{ border: 1px solid #d8dde3; padding: 0.75rem; vertical-align: top; min-width: 22rem; }}
thead th, tr > th:first-child {{ background: #f7f8fa; }}
img {{ display: block; width: 100%; height: auto; background: white; }}
p, summary {{ font-size: 0.9rem; line-height: 1.4; }}
.warning {{ color: #8a4b08; }}
</style>
</head>
<body>
<h1>YangLabKit public-data figure candidates</h1>
<p class="notice">Generator identities are intentionally hidden. Score each figure with
<a href="../RUBRIC.md">the rubric</a> before opening <code>identity-key.json</code>.</p>
<div class="table-wrap">
<table>
<thead><tr><th>Figure</th>{headers}</tr></thead>
<tbody>{''.join(rows)}</tbody>
</table>
</div>
</body>
</html>
"""
    (output_dir / "index.html").write_text(document, encoding="utf-8")
    return len(accepted), skipped


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--submissions", type=Path, default=ROOT / "submissions")
    parser.add_argument("--output", type=Path, default=ROOT / "_comparison")
    args = parser.parse_args()
    try:
        count, skipped = build(args.submissions.resolve(), args.output.resolve())
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 1
    print(f"wrote {args.output / 'index.html'} for {count} valid submission(s)")
    print(f"wrote {args.output / 'identity-key.json'}; keep it closed until scoring is complete")
    for item in skipped:
        print(f"SKIPPED: {item}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
