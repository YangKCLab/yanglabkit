#!/usr/bin/env python3
"""Build one identity-revealing showcase image per valid candidate submission.

Unlike build_comparison.py, output is deliberately unblinded: each composite
names its agent, model, and setup. Generate and share showcase images only
after blinded rubric scoring is complete.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from validate_submission import ROOT, validate_submission


def setup_label(submission_id: str) -> str:
    """Derive the skill setup from the submission directory-name suffix."""
    run_id = submission_id.rsplit("_", 1)[-1]
    if run_id == "noskill":
        return "no skill"
    if run_id == "yanglabkit":
        return "with yanglabkit skills"
    return run_id


def render_showcase(
    submission_dir: Path, metadata: dict, task: dict, output_path: Path
) -> None:
    generator = metadata.get("generator", {})
    setup = setup_label(metadata["submission_id"])
    headline = " · ".join(
        (generator.get("agent", "?"), generator.get("model", "?"), setup)
    )
    subline = (
        f"{generator.get('provider', '?')} · run {generator.get('run_date', '?')} · "
        f"{task['task_id']} v{task['task_version']}"
    )

    fig, axes = plt.subplots(2, 3, figsize=(20, 13.2), dpi=150)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.885, bottom=0.02, wspace=0.06, hspace=0.12)
    fig.text(0.5, 0.965, headline, ha="center", va="center", fontsize=24, fontweight="bold")
    fig.text(0.5, 0.925, subline, ha="center", va="center", fontsize=13, color="0.35")

    for ax, figure in zip(axes.flat, task["figures"]):
        entry = metadata["figures"][figure["id"]]
        image = plt.imread(submission_dir / entry["file"])
        ax.imshow(image)
        ax.set_axis_off()
        ax.set_title(figure["id"], fontsize=12, color="0.25", pad=6)

    fig.savefig(output_path, dpi=150)
    plt.close(fig)


def build(
    submissions_dir: Path, output_dir: Path, only: list[str] | None
) -> tuple[list[Path], list[str]]:
    task = json.loads((ROOT / "task.json").read_text(encoding="utf-8"))
    accepted = []
    skipped = []
    if submissions_dir.is_dir():
        for path in sorted(item for item in submissions_dir.iterdir() if item.is_dir()):
            if only and path.name not in only:
                continue
            errors, _, metadata = validate_submission(path)
            if errors:
                skipped.append(f"{path.name}: {len(errors)} validation error(s)")
                continue
            accepted.append((path, metadata))
    if only:
        found = {path.name for path, _ in accepted} | {item.split(":")[0] for item in skipped}
        for name in only:
            if name not in found:
                raise ValueError(f"submission not found: {name}")
    if not accepted:
        raise ValueError("no validator-passing submissions found")

    output_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for path, metadata in accepted:
        output_path = output_dir / f"{path.name}.png"
        render_showcase(path, metadata, task, output_path)
        written.append(output_path)
    return written, skipped


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--submissions", type=Path, default=ROOT / "submissions")
    parser.add_argument("--output", type=Path, default=ROOT / "_showcase")
    parser.add_argument(
        "--only",
        action="append",
        metavar="SUBMISSION_ID",
        help="rebuild only this submission (repeatable)",
    )
    args = parser.parse_args()
    try:
        written, skipped = build(args.submissions.resolve(), args.output.resolve(), args.only)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 1
    for path in written:
        print(f"wrote {path}")
    for item in skipped:
        print(f"SKIPPED: {item}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
