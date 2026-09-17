"""Export one MatchID ``*.jpg.dat`` sequence as point-wise CSV.GZ files.

The field names stay conservative because the private MatchID payload has no
public schema in the project.  Fields 7/8 are exported as displacement
candidates and converted with the file's own ``<11>`` factor.  R/Sigma are
preserved and a screening mask is added; no raw value is overwritten.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import math
import pathlib
import re
import zlib


ROW_RE = re.compile(r"<18>=<([^>]*)>")


def tag(raw: str, number: int) -> str:
    match = re.search(rf"<{number}>=<([^>]*)>", raw)
    return match.group(1) if match else ""


def parse(path: pathlib.Path) -> tuple[str, float, list[list[float]]]:
    raw = zlib.decompress(path.read_bytes(), wbits=31).decode("latin1")
    rows: list[list[float]] = []
    for text in ROW_RE.findall(raw):
        values = [float(value) for value in text.split(";")]
        if len(values) == 18:
            rows.append(values)
    conversion_text = tag(raw, 11)
    conversion = float(conversion_text) if conversion_text else math.nan
    return tag(raw, 1), conversion, rows


def frame_number(path: pathlib.Path) -> int:
    match = re.search(r"Img(\d+)\.jpg\.dat$", path.name, re.IGNORECASE)
    if not match:
        raise ValueError(f"无法从文件名提取 Img 帧号: {path}")
    return int(match.group(1))


FIELDS = [
    "照片帧号", "点编号", "ROI原点X_px", "ROI原点Y_px", "ROI宽_px", "ROI高_px",
    "X_px", "Y_px", "U字段7候选_px", "V字段8候选_px", "字段9候选", "字段10候选",
    "字段11候选", "字段12候选", "R", "Sigma", "字段15", "字段16", "字段17",
    "U字段7候选_mm", "V字段8候选_mm", "valid_R90_Sigma010",
]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dat-root", type=pathlib.Path, required=True)
    parser.add_argument("--output-dir", type=pathlib.Path, required=True)
    parser.add_argument("--r-threshold", type=float, default=0.90)
    parser.add_argument("--sigma-threshold", type=float, default=0.10)
    args = parser.parse_args()

    dat_files = sorted(
        args.dat_root.glob("Img*.jpg.dat"),
        key=frame_number,
    )
    args.output_dir.mkdir(parents=True, exist_ok=True)
    manifest: list[dict[str, object]] = []
    total_points = 0
    for path in dat_files:
        frame = frame_number(path)
        deformed, conversion, rows = parse(path)
        output = args.output_dir / f"Img{frame:06d}.points.csv.gz"
        valid_count = 0
        with gzip.open(output, "wt", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS)
            writer.writeheader()
            for row in rows:
                r_value = row[13]
                sigma_value = row[14]
                valid = r_value >= args.r_threshold and sigma_value <= args.sigma_threshold
                valid_count += int(valid)
                writer.writerow(
                    {
                        "照片帧号": frame,
                        "点编号": int(row[0]),
                        "ROI原点X_px": row[1],
                        "ROI原点Y_px": row[2],
                        "ROI宽_px": row[3],
                        "ROI高_px": row[4],
                        "X_px": row[5],
                        "Y_px": row[6],
                        "U字段7候选_px": row[7],
                        "V字段8候选_px": row[8],
                        "字段9候选": row[9],
                        "字段10候选": row[10],
                        "字段11候选": row[11],
                        "字段12候选": row[12],
                        "R": r_value,
                        "Sigma": sigma_value,
                        "字段15": row[15],
                        "字段16": row[16],
                        "字段17": row[17],
                        "U字段7候选_mm": row[7] * conversion if not math.isnan(conversion) else "",
                        "V字段8候选_mm": row[8] * conversion if not math.isnan(conversion) else "",
                        "valid_R90_Sigma010": int(valid),
                    }
                )
        total_points += len(rows)
        manifest.append(
            {
                "照片帧号": frame,
                "DAT文件名": path.name,
                "变形图像": deformed,
                "点数": len(rows),
                "质量通过点数": valid_count,
                "质量通过率": valid_count / len(rows) if rows else "",
                "转换系数_mm每px": conversion,
                "输出文件": output.name,
            }
        )

    manifest_path = args.output_dir / "points_manifest.csv"
    with manifest_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(manifest[0]) if manifest else ["照片帧号"])
        writer.writeheader()
        writer.writerows(manifest)
    print(f"frames={len(dat_files)}")
    print(f"points={total_points}")
    print(f"manifest={manifest_path}")


if __name__ == "__main__":
    main()
