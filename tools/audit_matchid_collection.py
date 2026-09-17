"""Audit every MatchID ``*.jpg.dat`` file in the yuan data collection.

The script deliberately writes summaries only: raw images, DIC payloads and
force workbooks stay outside the Wiki.  It is useful before choosing which
trial can enter the first VFM run.
"""

from __future__ import annotations

import argparse
import csv
import math
import pathlib
import re
import statistics
import zlib


ROW_RE = re.compile(r"<18>=<([^>]*)>")
FRAME_RE = re.compile(r"(?:Img)?(\d+)\.jpg\.dat$", re.IGNORECASE)


def tag(raw: str, number: int) -> str:
    match = re.search(rf"<{number}>=<([^>]*)>", raw)
    return match.group(1) if match else ""


def parse_dat(path: pathlib.Path) -> dict[str, object]:
    decoder = zlib.decompressobj(31)
    raw = decoder.decompress(path.read_bytes()).decode("latin1")
    rows: list[list[float]] = []
    malformed = 0
    for text in ROW_RE.findall(raw):
        try:
            values = [float(value) for value in text.split(";")]
        except ValueError:
            malformed += 1
            continue
        if len(values) != 18:
            malformed += 1
            continue
        rows.append(values)

    def column(index: int) -> list[float]:
        return [row[index] for row in rows]

    expected_text = tag(raw, 55)
    conversion_text = tag(raw, 11)
    expected = int(float(expected_text)) if expected_text else 0
    conversion = float(conversion_text) if conversion_text else math.nan
    r_values = column(13)
    sigma_values = column(14)
    return {
        "参考图像": tag(raw, 0),
        "变形图像": tag(raw, 1),
        "期望点数": expected,
        "实际点数": len(rows),
        "行解析错误数": malformed,
        "转换系数_mm每px": conversion,
        "R均值": statistics.fmean(r_values) if r_values else math.nan,
        "Sigma均值": statistics.fmean(sigma_values) if sigma_values else math.nan,
        "解析状态": "可解析" if rows and malformed == 0 else "需检查",
    }


def trial_name(path: pathlib.Path, data_root: pathlib.Path) -> str:
    parts = path.relative_to(data_root).parts
    for marker in ("袁-20250529", "xz_tu数据"):
        if marker in parts:
            index = parts.index(marker)
            if index + 1 < len(parts):
                return parts[index + 1]
    return path.parent.name


def frame_number(path: pathlib.Path) -> int:
    match = FRAME_RE.search(path.name)
    if not match:
        raise ValueError(f"无法从文件名提取帧号: {path}")
    return int(match.group(1))


def fmt(value: object) -> str:
    if isinstance(value, float):
        if math.isnan(value):
            return ""
        return f"{value:.8g}"
    return str(value)


def write_csv(path: pathlib.Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: fmt(row.get(field, "")) for field in fields})


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-root", type=pathlib.Path, required=True)
    parser.add_argument("--output-dir", type=pathlib.Path, required=True)
    parser.add_argument("--force-map", type=pathlib.Path)
    args = parser.parse_args()

    dat_files = sorted(args.data_root.rglob("*.jpg.dat"))
    frame_rows: list[dict[str, object]] = []
    for path in dat_files:
        item = parse_dat(path)
        item.update(
            {
                "试验编号": trial_name(path, args.data_root),
                "帧号": frame_number(path),
                "DAT相对路径": path.relative_to(args.data_root).as_posix(),
            }
        )
        frame_rows.append(item)
    frame_rows.sort(key=lambda row: (str(row["试验编号"]), int(row["帧号"])))

    force_rows: list[dict[str, str]] = []
    force_trials: set[str] = set()
    if args.force_map:
        with args.force_map.open("r", encoding="utf-8-sig", newline="") as handle:
            force_rows = list(csv.DictReader(handle))
        force_trials = {
            row["试样编号"][3:]
            for row in force_rows
            if row.get("试样编号", "").startswith("XY_")
        }

    summary_rows: list[dict[str, object]] = []
    by_trial: dict[str, list[dict[str, object]]] = {}
    for row in frame_rows:
        by_trial.setdefault(str(row["试验编号"]), []).append(row)
    for trial, rows in sorted(by_trial.items()):
        expected = [int(row["期望点数"]) for row in rows if int(row["期望点数"]) > 0]
        actual = [int(row["实际点数"]) for row in rows]
        expected_median = statistics.median(expected) if expected else 0
        reduced = [row for row in rows if expected_median and int(row["实际点数"]) < expected_median]
        relative_paths = [pathlib.Path(str(row["DAT相对路径"])) for row in rows]
        image_directory = (args.data_root / relative_paths[0]).parent
        image_files = list(image_directory.glob("*.jpg"))
        frames = sorted(int(row["帧号"]) for row in rows)
        missing_count = (frames[-1] - frames[0] + 1) - len(frames)
        reduced_preview = [str(row["帧号"]) for row in reduced[:20]]
        if len(reduced) > 25:
            reduced_preview.extend(["...", *[str(row["帧号"]) for row in reduced[-5:]]])
        elif len(reduced) > 20:
            reduced_preview.extend(str(row["帧号"]) for row in reduced[20:])
        conversion_values = [
            float(row["转换系数_mm每px"])
            for row in rows
            if not math.isnan(float(row["转换系数_mm每px"]))
        ]
        summary_rows.append(
            {
                "试验编号": trial,
                "DAT文件数": len(rows),
                "可解析数": sum(row["解析状态"] == "可解析" for row in rows),
                "首帧": min(int(row["帧号"]) for row in rows),
                "末帧": max(int(row["帧号"]) for row in rows),
                "期望点数中位数": expected_median,
                "实际点数最小": min(actual),
                "实际点数最大": max(actual),
                "图像文件数": len(image_files),
                "DAT缺失帧数": missing_count,
                "点数减少帧数": len(reduced),
                "点数减少帧号示例": ",".join(reduced_preview),
                "点数完整率中位数": statistics.median(
                    [int(row["实际点数"]) / expected_median for row in rows]
                )
                if expected_median
                else math.nan,
                "转换系数中位数_mm每px": statistics.median(conversion_values) if conversion_values else math.nan,
                "力映射": "已有 XY 逐照片候选表" if trial in force_trials else "未找到逐照片力表",
                "VFM准入": "先做字段/质量/同步审计",
            }
        )

    frame_fields = [
        "试验编号", "帧号", "DAT相对路径", "参考图像", "变形图像", "解析状态",
        "行解析错误数", "实际点数", "期望点数", "转换系数_mm每px", "R均值", "Sigma均值",
    ]
    summary_fields = [
        "试验编号", "DAT文件数", "可解析数", "首帧", "末帧", "期望点数中位数",
        "实际点数最小", "实际点数最大", "图像文件数", "DAT缺失帧数", "点数减少帧数", "点数减少帧号示例", "点数完整率中位数",
        "转换系数中位数_mm每px", "力映射", "VFM准入",
    ]
    write_csv(args.output_dir / "all_matchid_dat_frame_audit.csv", frame_rows, frame_fields)
    write_csv(args.output_dir / "all_matchid_dat_summary.csv", summary_rows, summary_fields)
    if force_rows:
        frame_by_key = {
            (str(row["试验编号"]), int(row["帧号"])): row
            for row in frame_rows
        }
        merged: list[dict[str, object]] = []
        for force in force_rows:
            test_id = force["试样编号"]
            trial = test_id[3:] if test_id.startswith("XY_") else test_id
            frame = int(force["照片帧号"])
            audit = frame_by_key.get((trial, frame))
            merged.append(
                {
                    "试样编号": test_id,
                    "照片帧号": frame,
                    "估计时间_s": force.get("估计时间_s", ""),
                    "Fx平均力_N": force.get("Fx平均力_N", ""),
                    "Fy平均力_N": force.get("Fy平均力_N", ""),
                    "加载类型": force.get("加载类型", ""),
                    "事件标签": force.get("事件标签", ""),
                    "同步状态": force.get("同步状态", ""),
                    "DAT文件名": pathlib.Path(str(audit["DAT相对路径"])).name if audit else "",
                    "实际点数": audit.get("实际点数", "") if audit else "",
                    "期望点数": audit.get("期望点数", "") if audit else "",
                    "点数完整率": (int(audit["实际点数"]) / int(audit["期望点数"])) if audit and int(audit["期望点数"]) else "",
                    "R均值": audit.get("R均值", "") if audit else "",
                    "Sigma均值": audit.get("Sigma均值", "") if audit else "",
                    "DAT解析状态": audit.get("解析状态", "") if audit else "无DAT对应",
                    "VFM候选状态": "先质量筛选；同步仍为估计" if audit else "照片有力、缺少DAT",
                }
            )
        merged_fields = [
            "试样编号", "照片帧号", "估计时间_s", "Fx平均力_N", "Fy平均力_N", "加载类型", "事件标签", "同步状态",
            "DAT文件名", "实际点数", "期望点数", "点数完整率", "R均值", "Sigma均值", "DAT解析状态", "VFM候选状态",
        ]
        write_csv(args.output_dir / "all_matchid_dat_force_candidates.csv", merged, merged_fields)
    print(f"dat_files={len(frame_rows)}")
    print(f"trials={len(summary_rows)}")
    print(f"parse_ok={sum(row['解析状态'] == '可解析' for row in frame_rows)}")
    print(args.output_dir / "all_matchid_dat_summary.csv")


if __name__ == "__main__":
    main()
