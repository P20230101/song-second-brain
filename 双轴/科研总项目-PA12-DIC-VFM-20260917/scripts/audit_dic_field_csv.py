"""Audit semicolon-delimited, frame-wise DIC point exports.

This script audits provenance and field shape only. It does not infer strain,
pair force data, or declare a frame eligible for VFM.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


FRAME_RE = re.compile(r"^Img(?P<frame>\d{6})\.jpg\.csv$")
EXPECTED_HEADER = ["X[Pixels]", "Y[Pixels]", "U[Pixels]", "V[Pixels]", "R", "Sigma"]


def read_frame(path: Path) -> dict:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle, delimiter=";")
        header = next(reader)
        if header and header[-1] == "":
            header = header[:-1]

        rows = []
        invalid_rows = []
        for line_number, row in enumerate(reader, start=2):
            if not row or all(value == "" for value in row):
                continue
            if row and row[-1] == "":
                row = row[:-1]
            if len(row) != len(EXPECTED_HEADER):
                invalid_rows.append({"line": line_number, "reason": "field_count", "values": row})
                continue
            try:
                values = [float(value) for value in row]
            except ValueError:
                invalid_rows.append({"line": line_number, "reason": "non_numeric", "values": row})
                continue
            rows.append(values)

    r_values = [row[4] for row in rows]
    sigma_values = [row[5] for row in rows]
    return {
        "file": path.name,
        "frame": int(FRAME_RE.match(path.name).group("frame")),
        "header": header,
        "row_count": len(rows),
        "invalid_rows": invalid_rows,
        "x_min": min(row[0] for row in rows),
        "x_max": max(row[0] for row in rows),
        "y_min": min(row[1] for row in rows),
        "y_max": max(row[1] for row in rows),
        "u_min": min(row[2] for row in rows),
        "u_max": max(row[2] for row in rows),
        "v_min": min(row[3] for row in rows),
        "v_max": max(row[3] for row in rows),
        "r_min": min(r_values),
        "r_mean": sum(r_values) / len(r_values),
        "sigma_mean": sum(sigma_values) / len(sigma_values),
    }


def audit(input_dir: Path) -> dict:
    files = sorted(
        path
        for path in input_dir.iterdir()
        if path.is_file() and FRAME_RE.match(path.name)
    )
    frames = [read_frame(path) for path in files]
    frame_ids = [item["frame"] for item in frames]
    missing_frames = [frame for frame in range(frame_ids[-1] + 1) if frame not in frame_ids]
    headers = sorted({tuple(item["header"]) for item in frames})
    row_counts = [item["row_count"] for item in frames]
    return {
        "input_dir": str(input_dir),
        "frame_file_count": len(frames),
        "first_frame": frame_ids[0],
        "last_frame": frame_ids[-1],
        "missing_frames": missing_frames,
        "headers": [list(header) for header in headers],
        "expected_header": EXPECTED_HEADER,
        "header_matches_expected": headers == [tuple(EXPECTED_HEADER)],
        "min_row_count": min(row_counts),
        "max_row_count": max(row_counts),
        "files_with_invalid_rows": sum(bool(item["invalid_rows"]) for item in frames),
        "frames": frames,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="Directory containing Img######.jpg.csv files")
    parser.add_argument("--output", type=Path, help="Optional JSON report path")
    args = parser.parse_args()

    result = audit(args.input)
    payload = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output is None:
        print(payload)
    else:
        args.output.write_text(payload + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
