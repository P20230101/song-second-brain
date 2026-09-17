"""Audit MatchID 2D .jpg.dat payloads and join them to the photo/force table."""

from __future__ import annotations

import argparse
import csv
import math
import pathlib
import re
import statistics
import zlib


ROW_RE = re.compile(r"<18>=<([^>]*)>")


def tag(raw: str, number: int) -> str:
    match = re.search(rf"<{number}>=<([^>]*)>", raw)
    return match.group(1) if match else ""


def parse_dat(path: pathlib.Path) -> dict[str, object]:
    decoder = zlib.decompressobj(31)
    raw = decoder.decompress(path.read_bytes()).decode("latin1")
    rows = []
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

    expected = int(float(tag(raw, 55))) if tag(raw, 55) else 0
    conversion = float(tag(raw, 11)) if tag(raw, 11) else math.nan

    def column(index: int) -> list[float]:
        return [row[index] for row in rows]

    r_values = column(13)
    sigma_values = column(14)
    u_values = column(7)
    v_values = column(8)
    summary: dict[str, object] = {
        "文件名": path.name,
        "参考图像": tag(raw, 0),
        "变形图像": tag(raw, 1),
        "期望点数": expected,
        "实际点数": len(rows),
        "行解析错误数": malformed,
        "转换系数_mm每px": conversion,
        "R最小": min(r_values) if r_values else math.nan,
        "R均值": statistics.fmean(r_values) if r_values else math.nan,
        "R低于0.90点数": sum(value < 0.90 for value in r_values),
        "Sigma均值": statistics.fmean(sigma_values) if sigma_values else math.nan,
        "Sigma高于0.10点数": sum(value > 0.10 for value in sigma_values),
        "U字段7均值_px": statistics.fmean(u_values) if u_values else math.nan,
        "V字段8均值_px": statistics.fmean(v_values) if v_values else math.nan,
        "U字段7均值_mm": statistics.fmean(u_values) * conversion if u_values else math.nan,
        "V字段8均值_mm": statistics.fmean(v_values) * conversion if v_values else math.nan,
        "应变字段9均值": statistics.fmean(column(9)) if rows else math.nan,
        "应变字段10均值": statistics.fmean(column(10)) if rows else math.nan,
        "应变字段11均值": statistics.fmean(column(11)) if rows else math.nan,
        "字段12均值": statistics.fmean(column(12)) if rows else math.nan,
        "解析状态": "可解析" if rows and malformed == 0 else "需检查",
    }
    return summary


def fmt(value: object) -> str:
    if isinstance(value, float):
        if math.isnan(value):
            return ""
        return f"{value:.8g}"
    return str(value)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dat-root", type=pathlib.Path, required=True)
    parser.add_argument("--force-csv", type=pathlib.Path, required=True)
    parser.add_argument("--output-dir", type=pathlib.Path, required=True)
    args = parser.parse_args()

    dat_files = sorted(args.dat_root.glob("Img*.jpg.dat"))
    audits = []
    for path in dat_files:
        match = re.fullmatch(r"Img(\d{6})\.jpg\.dat", path.name)
        if not match:
            continue
        item = parse_dat(path)
        item["照片帧号"] = int(match.group(1))
        audits.append(item)
    audits.sort(key=lambda item: int(item["照片帧号"]))

    args.output_dir.mkdir(parents=True, exist_ok=True)
    audit_fields = [
        "照片帧号", "文件名", "参考图像", "变形图像", "解析状态", "行解析错误数",
        "实际点数", "期望点数", "转换系数_mm每px", "R最小", "R均值", "R低于0.90点数",
        "Sigma均值", "Sigma高于0.10点数", "U字段7均值_px", "V字段8均值_px",
        "U字段7均值_mm", "V字段8均值_mm", "应变字段9均值", "应变字段10均值",
        "应变字段11均值", "字段12均值",
    ]
    audit_path = args.output_dir / "XY-0.1-02_MatchID-DAT_帧审计_259行.csv"
    with audit_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=audit_fields)
        writer.writeheader()
        for item in audits:
            writer.writerow({field: fmt(item.get(field, "")) for field in audit_fields})

    with args.force_csv.open("r", encoding="utf-8-sig", newline="") as handle:
        force_rows = list(csv.DictReader(handle))
    by_frame = {int(row["照片帧号"]): row for row in force_rows}
    merged_fields = [
        "试样编号", "照片帧号", "估计时间_s", "Fx平均力_N", "Fy平均力_N", "加载类型",
        "照片状态", "事件标签", "MatchID文件名", "实际点数", "期望点数", "点数完整率",
        "R均值", "Sigma均值", "U字段7均值_px", "V字段8均值_px", "U字段7均值_mm",
        "V字段8均值_mm", "DAT解析状态", "VFM候选状态", "同步状态",
    ]
    merged_path = args.output_dir / "XY-0.1-02_照片力MatchID-DAT_259行候选表.csv"
    with merged_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=merged_fields)
        writer.writeheader()
        for item in audits:
            frame = int(item["照片帧号"])
            force = by_frame[frame]
            expected = int(item["期望点数"])
            actual = int(item["实际点数"])
            ratio = actual / expected if expected else math.nan
            candidate = (
                "首轮候选（点数完整）" if item["解析状态"] == "可解析" and ratio >= 0.9
                else "末帧点数减少，先质量筛选"
            )
            row = {
                "试样编号": force["试样编号"],
                "照片帧号": frame,
                "估计时间_s": force["估计时间_s"],
                "Fx平均力_N": force["Fx平均力_N"],
                "Fy平均力_N": force["Fy平均力_N"],
                "加载类型": force["加载类型"],
                "照片状态": force["照片状态"],
                "事件标签": force["事件标签"],
                "MatchID文件名": item["文件名"],
                "实际点数": actual,
                "期望点数": expected,
                "点数完整率": fmt(ratio),
                "R均值": fmt(item["R均值"]),
                "Sigma均值": fmt(item["Sigma均值"]),
                "U字段7均值_px": fmt(item["U字段7均值_px"]),
                "V字段8均值_px": fmt(item["V字段8均值_px"]),
                "U字段7均值_mm": fmt(item["U字段7均值_mm"]),
                "V字段8均值_mm": fmt(item["V字段8均值_mm"]),
                "DAT解析状态": item["解析状态"],
                "VFM候选状态": candidate,
                "同步状态": force["同步状态"],
            }
            writer.writerow(row)

    print(f"dat_files={len(audits)}")
    print(f"parse_ok={sum(item['解析状态'] == '可解析' for item in audits)}")
    print(f"reduced_points={[item['照片帧号'] for item in audits if int(item['实际点数']) < int(item['期望点数'])]}")
    print(audit_path)
    print(merged_path)


if __name__ == "__main__":
    main()
