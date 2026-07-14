#!/usr/bin/env python3
"""Validate one public-data figure comparison submission using stdlib only."""

from __future__ import annotations

import argparse
import json
import re
import struct
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
HEX_COLOR = re.compile(r"^#[0-9A-Fa-f]{6}$")
PLACEHOLDERS = ("replace", "yyyy-mm-dd")
PALETTE_CLASSES = {"categorical", "sequential", "diverging", "multi-sequential"}


def parse_png(path: Path) -> tuple[int, int, float | None, float | None]:
    content = path.read_bytes()
    if not content.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("not a PNG file")
    offset = 8
    width = height = None
    dpi_x = dpi_y = None
    while offset + 12 <= len(content):
        length = struct.unpack(">I", content[offset : offset + 4])[0]
        chunk_type = content[offset + 4 : offset + 8]
        chunk = content[offset + 8 : offset + 8 + length]
        if chunk_type == b"IHDR":
            width, height = struct.unpack(">II", chunk[:8])
        elif chunk_type == b"pHYs" and len(chunk) == 9:
            pixels_per_meter_x, pixels_per_meter_y, unit = struct.unpack(">IIB", chunk)
            if unit == 1:
                dpi_x = pixels_per_meter_x * 0.0254
                dpi_y = pixels_per_meter_y * 0.0254
        if chunk_type == b"IEND":
            break
        offset += 12 + length
    if width is None or height is None:
        raise ValueError("PNG has no IHDR dimensions")
    return width, height, dpi_x, dpi_y


def safe_path(root: Path, relative: str) -> Path:
    candidate = (root / relative).resolve()
    if root.resolve() not in candidate.parents:
        raise ValueError(f"path escapes submission directory: {relative}")
    return candidate


def contains_placeholder(value: object) -> bool:
    return isinstance(value, str) and any(token in value.lower() for token in PLACEHOLDERS)


def file_safe_slug(value: str) -> str:
    """Normalize metadata text for comparison with a submission directory name."""
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def validate_submission(submission_dir: Path) -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warnings: list[str] = []
    task = json.loads((ROOT / "task.json").read_text(encoding="utf-8"))
    metadata_path = submission_dir / "submission.json"
    notes_path = submission_dir / "NOTES.md"
    if not metadata_path.is_file():
        return ["missing submission.json"], warnings, {}
    if not notes_path.is_file():
        errors.append("missing NOTES.md")

    try:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        return [f"cannot read submission.json: {exc}"], warnings, {}

    if metadata.get("schema_version") != 1:
        errors.append("submission schema_version must be 1")
    if metadata.get("task_id") != task["task_id"]:
        errors.append(f"task_id must be {task['task_id']}")
    if metadata.get("task_version") != task["task_version"]:
        errors.append(f"task_version must be {task['task_version']}")
    if metadata.get("submission_id") != submission_dir.name:
        errors.append("submission_id must exactly match its directory name")
    if contains_placeholder(metadata.get("submission_id")):
        errors.append("submission_id still contains a template placeholder")

    generator = metadata.get("generator")
    if not isinstance(generator, dict):
        errors.append("generator must be an object")
    else:
        for field in ("agent", "model", "provider", "run_date"):
            value = generator.get(field)
            if not isinstance(value, str) or not value.strip() or contains_placeholder(value):
                errors.append(f"generator.{field} must be filled in")
        submission_slug = file_safe_slug(str(metadata.get("submission_id", "")))
        for field in ("agent", "model"):
            value = generator.get(field)
            if isinstance(value, str) and value.strip() and not contains_placeholder(value):
                expected_token = file_safe_slug(value)
                if expected_token and expected_token not in submission_slug:
                    errors.append(
                        f"submission_id must identify generator.{field} ({expected_token})"
                    )

    figure_metadata = metadata.get("figures")
    if not isinstance(figure_metadata, dict):
        return errors + ["figures must be an object"], warnings, metadata

    expected_ids = [figure["id"] for figure in task["figures"]]
    if set(figure_metadata) != set(expected_ids):
        missing = sorted(set(expected_ids) - set(figure_metadata))
        extra = sorted(set(figure_metadata) - set(expected_ids))
        if missing:
            errors.append(f"missing figure metadata: {', '.join(missing)}")
        if extra:
            errors.append(f"unexpected figure metadata: {', '.join(extra)}")

    for figure in task["figures"]:
        figure_id = figure["id"]
        entry = figure_metadata.get(figure_id)
        if not isinstance(entry, dict):
            continue
        expected_file = f"figures/{figure['output']}"
        if entry.get("file") != expected_file:
            errors.append(f"{figure_id}: file must be {expected_file}")

        try:
            image_path = safe_path(submission_dir, expected_file)
        except ValueError as exc:
            errors.append(f"{figure_id}: {exc}")
            continue
        if not image_path.is_file():
            errors.append(f"{figure_id}: missing {expected_file}")
        else:
            try:
                _, _, dpi_x, dpi_y = parse_png(image_path)
                required_dpi = float(task["output"]["dpi"])
                if dpi_x is None or dpi_y is None:
                    errors.append(f"{figure_id}: PNG has no physical-resolution metadata")
                elif abs(dpi_x - required_dpi) > 1 or abs(dpi_y - required_dpi) > 1:
                    errors.append(
                        f"{figure_id}: PNG must be {required_dpi:g} dpi; "
                        f"metadata reports {dpi_x:.1f} x {dpi_y:.1f} dpi"
                    )
            except (OSError, ValueError, struct.error) as exc:
                errors.append(f"{figure_id}: invalid PNG: {exc}")

        source = entry.get("source")
        if not isinstance(source, str) or not source.startswith("source/"):
            errors.append(f"{figure_id}: source must point inside source/")
        else:
            try:
                source_path = safe_path(submission_dir, source)
                if not source_path.is_file() or source_path.stat().st_size == 0:
                    errors.append(f"{figure_id}: source file does not exist or is empty: {source}")
            except ValueError as exc:
                errors.append(f"{figure_id}: {exc}")

        alt_text = entry.get("alt_text")
        if not isinstance(alt_text, str) or len(alt_text.strip()) < 40 or contains_placeholder(alt_text):
            errors.append(f"{figure_id}: alt_text must be a filled descriptive sentence")

        palette = entry.get("palette")
        if not isinstance(palette, dict):
            errors.append(f"{figure_id}: palette must be an object")
        else:
            palette_class = palette.get("class")
            if palette_class not in PALETTE_CLASSES:
                allowed = ", ".join(sorted(PALETTE_CLASSES))
                errors.append(f"{figure_id}: palette.class must be one of: {allowed}")
            name = palette.get("name")
            if not isinstance(name, str) or not name.strip() or contains_placeholder(name):
                errors.append(f"{figure_id}: exact palette.name is required")
            colors = palette.get("colors")
            if not isinstance(colors, list) or not colors or any(
                not isinstance(color, str) or not HEX_COLOR.fullmatch(color) for color in colors
            ):
                errors.append(f"{figure_id}: palette.colors must contain actual #RRGGBB values")

    return errors, warnings, metadata


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("submission", type=Path, help="path to one submission directory")
    args = parser.parse_args()
    submission_dir = args.submission.resolve()
    errors, warnings, _ = validate_submission(submission_dir)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"FAIL: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"PASS: {submission_dir.name} ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
