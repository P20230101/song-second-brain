"""Create an auditable photo-to-force mapping for the XY trial files.

The source images do not contain a usable capture timestamp, so the default
mapping anchors the first image at the detected force-onset candidate and the
last image at the last Press.T sample. Every image consequently receives one
interpolated force value, while the output keeps the mapping method explicit
and marks VFM as not yet eligible until a camera timestamp/trigger is supplied.
"""

from __future__ import annotations

import argparse
import csv
import math
import re
from bisect import bisect_right
from io import BytesIO, StringIO
from pathlib import Path
from statistics import median

import openpyxl


IMAGE_DIR_TO_FORCE = {
    "X-05-0.1-01": ["x-05-0.1_state_20250529133138_20250529133153.xls"],
    "X-06-1.0-01": ["x-6-1_state_20250529133928_20250529133930.xls"],
    "X-07-10-01": ["x-7-10_state_20250529134610_20250529134611.xls"],
    "Xy-0.1-01": ["xy-1-0.1_state_20250529102303_20250529102339.xls"],
    "XY-0.1-02": ["xy-2-0.1_state_20250529104919_20250529104947.xls"],
    "Xy-03-10-01": ["xy-3-10_state_20250529111421_20250529111422.xls"],
    "Xy-04-1-01": ["xy-04-1_state_20250529112959_20250529113003.xls"],
    "Y-09-0.1-02": ["y-9-0.1_state_20250529140828_20250529141127.xls"],
    "Y-10-1-01": ["y-10-1_state_20250529141618_20250529141633.xls"],
    "Y-11-10-01": ["y-11-10_state_20250529142519_20250529142520.xls"],
}

SPEED_MM_S = {
    "X-05-0.1-01": 0.2,
    "X-06-1.0-01": 2.0,
    "X-07-10-01": 20.0,
    "Xy-0.1-01": 0.2,
    "XY-0.1-02": 0.2,
    "Xy-03-10-01": 20.0,
    "Xy-04-1-01": 2.0,
    "Y-09-0.1-02": 0.2,
    "Y-10-1-01": 2.0,
    "Y-11-10-01": 20.0,
}

# Values shown in the user's latest two summary tables. They are retained as
# a source-labelled field; they are not recomputed from the endpoint mapping.
SCREENSHOT_CAMERA_HZ = {
    "X-05-0.1-01": 10.0,
    "X-06-1.0-01": 50.0,
    "X-07-10-01": 200.0,
    "Y-09-0.1-02": 10.0,
    "Y-10-1-01": 101.0,
    "Y-11-10-01": 375.0,
}

SCREENSHOT_DIC_DISPLACEMENT_MM = {
    "X-05-0.1-01": 2.58,
    "X-06-1.0-01": 2.66,
    "X-07-10-01": 8.00,
    "Y-09-0.1-02": 35.9,
    "Y-10-1-01": 30.6,
    "Y-11-10-01": 37.8,
}

# Frame counts used for the DIC-frequency table.  These are the contiguous
# MatchID input counts that are usable for a frequency estimate.  The
# XY-0.1-02 input contains only ten non-contiguous frames, so its frequency is
# intentionally left unavailable until the MatchID input is rebuilt.
DIC_FREQUENCY_FRAME_COUNT: dict[str, int | None] = {
    "X-05-0.1-01": 130,
    "X-06-1.0-01": 133,
    "X-07-10-01": 81,
    "Xy-0.1-01": 289,
    "XY-0.1-02": None,
    "Xy-03-10-01": 21,
    "Xy-04-1-01": 267,
    "Y-09-0.1-02": 1825,
    "Y-10-1-01": 1558,
    "Y-11-10-01": 711,
}


def numeric_frame(path: Path) -> int:
    match = re.search(r"Img(\d+)\.jpg$", path.name, flags=re.IGNORECASE)
    if not match:
        raise ValueError(f"not an image frame: {path}")
    return int(match.group(1))


def image_files(directory: Path) -> list[Path]:
    files = [p for p in directory.rglob("*.jpg") if re.search(r"Img\d+\.jpg$", p.name, re.I)]
    return sorted(files, key=numeric_frame)


def load_sheet(path: Path, sheet_name: str) -> tuple[list[str], list[list[float]]]:
    workbook = openpyxl.load_workbook(BytesIO(path.read_bytes()), read_only=True, data_only=True)
    sheet = workbook[sheet_name]
    rows = sheet.iter_rows(values_only=True)
    header = next(rows)
    names: list[str] = []
    columns: list[int] = []
    for index, value in enumerate(header):
        if value is None:
            continue
        name = str(value)
        if name in names:
            continue
        names.append(name)
        columns.append(index)

    values: list[list[float]] = []
    for row in rows:
        if not row or row[columns[0]] is None:
            continue
        try:
            values.append([float(row[index]) for index in columns])
        except (TypeError, ValueError):
            continue
    return names, values


def interpolate(time_value: float, times: list[float], values: list[float]) -> float:
    if time_value <= times[0]:
        return values[0]
    if time_value >= times[-1]:
        return values[-1]
    right = bisect_right(times, time_value)
    left = right - 1
    span = times[right] - times[left]
    if span == 0:
        return values[left]
    alpha = (time_value - times[left]) / span
    return values[left] + alpha * (values[right] - values[left])


def robust_median_absolute_deviation(values: list[float]) -> float:
    center = median(values)
    return median([abs(value - center) for value in values])


def detect_events(times: list[float], press: dict[str, list[float]], direction: str) -> tuple[float | None, float, float | None]:
    if direction == "X":
        channels = ["X1_Press", "X2_Press"]
    elif direction == "Y":
        channels = ["Y1_Press", "Y2_Press"]
    else:
        channels = ["X1_Press", "X2_Press", "Y1_Press", "Y2_Press"]
    channels = [channel for channel in channels if channel in press]
    if not channels:
        raise ValueError(f"no force channels available for direction {direction}")
    signal = [max(abs(press[channel][index]) for channel in channels) for index in range(len(times))]
    baseline_values = signal[: min(50, len(signal))]
    baseline = median(baseline_values)
    mad = robust_median_absolute_deviation(baseline_values)
    # A deviation below the baseline is not a loading onset.  The previous
    # implementation used ``abs(signal - baseline)`` and therefore treated
    # the initial settling/preload release as the start of loading (notably
    # for X-05 and Y-11).  Five force units is the minimum practical rise
    # threshold when the first 50 samples are perfectly flat; otherwise the
    # MAD-based threshold controls the noise floor.
    threshold = max(10.0 * mad, 5.0)
    onset: float | None = None
    for index in range(len(baseline_values), len(signal) - 2):
        if all(signal[j] - baseline > threshold for j in range(index, index + 3)):
            onset = times[index]
            break

    peak_index = max(range(len(signal)), key=signal.__getitem__)
    peak_time = times[peak_index]
    peak_excess = max(signal[peak_index] - baseline, 0.0)
    drop: float | None = None
    if peak_excess > threshold:
        drop_limit = baseline + 0.2 * peak_excess
        for index in range(max(peak_index, 0), len(signal) - 4):
            if all(signal[j] <= drop_limit for j in range(index, index + 5)):
                drop = times[index]
                break
    return onset, peak_time, drop


def unique_csv_frames(directory: Path) -> int | None:
    counts: list[int] = []
    for path in directory.rglob("*.csv"):
        if path.name.lower().startswith("img"):
            continue
        try:
            rows = list(csv.reader(path.read_text(encoding="utf-8-sig", errors="replace").splitlines(), delimiter=";"))
        except OSError:
            continue
        frame_ids = {row[1] for row in rows[1:] if len(row) > 1 and row[1]}
        if frame_ids:
            counts.append(len(frame_ids))
    return max(counts) if counts else None


def m2inp_frames(directory: Path) -> int | None:
    counts: list[int] = []
    for path in directory.rglob("*.m2inp"):
        text = path.read_text(encoding="utf-8", errors="replace")
        counts.append(len(re.findall(r"<Deformed\$image>=<", text, flags=re.I)))
    return max(counts) if counts else None


def direction_for(name: str) -> str:
    if name.startswith("X-"):
        return "X"
    if name.startswith("Y-"):
        return "Y"
    return "XY"


def format_number(value: float | int | None, digits: int = 6) -> str:
    if value is None:
        return ""
    if digits == 0:
        return str(int(round(value)))
    return f"{value:.{digits}f}".rstrip("0").rstrip(".")


def analyse_trial(data_root: Path, image_directory: Path, force_directory: Path) -> tuple[list[dict[str, object]], dict[str, object]]:
    name = image_directory.name
    force_path = force_directory / IMAGE_DIR_TO_FORCE[name][0]
    photos = image_files(image_directory)
    press_header, press_rows = load_sheet(force_path, "Press")
    pos_header, pos_rows = load_sheet(force_path, "Pos")
    press = {header: [row[index] for row in press_rows] for index, header in enumerate(press_header)}
    pos = {header: [row[index] for row in pos_rows] for index, header in enumerate(pos_header)}
    force_times = press.pop("T")
    position_times = pos.pop("T")
    onset, peak_time, drop = detect_events(force_times, press, direction_for(name))
    anchor_start = onset if onset is not None else force_times[0]
    anchor_end = force_times[-1]
    image_span = anchor_end - anchor_start
    if image_span <= 0:
        raise ValueError(f"non-positive force span for {name}: {anchor_start}, {anchor_end}")
    speed = SPEED_MM_S[name]
    dic_displacement = SCREENSHOT_DIC_DISPLACEMENT_MM.get(name)
    actual_camera = (len(photos) - 1) / image_span if len(photos) > 1 else None
    force_span = force_times[-1] - force_times[0]
    force_frequency = (len(force_times) - 1) / force_span if force_span else None
    rows: list[dict[str, object]] = []
    for frame_index, photo in enumerate(photos):
        fraction = frame_index / (len(photos) - 1) if len(photos) > 1 else 0.0
        image_time = anchor_start + fraction * image_span
        row: dict[str, object] = {
            "test_id": f"XY_{name}",
            "direction": direction_for(name),
            "speed_mm_s": speed,
            "image_frame": numeric_frame(photo),
            "image_file": photo.relative_to(data_root).as_posix(),
            "image_count_saved": len(photos),
            "t_image_s_est": image_time,
            "sync_method": "endpoint_linear_force_onset_to_force_record_end",
            "force_onset_candidate_s": onset,
            "force_peak_candidate_s": peak_time,
            "force_drop_candidate_s": drop,
            "force_row_left": bisect_right(force_times, image_time) - 1,
            "force_row_right": bisect_right(force_times, image_time),
            "vfm_eligible": False,
        }
        for channel in ["X1_Press", "X2_Press", "Y1_Press", "Y2_Press"]:
            if channel in press:
                row[f"{channel}_N"] = interpolate(image_time, force_times, press[channel])
        for channel in ["X1_Pos", "X2_Pos", "Y1_Pos", "Y2_Pos"]:
            if channel in pos:
                row[f"{channel}_mm"] = interpolate(image_time, position_times, pos[channel])
        rows.append(row)

    summary: dict[str, object] = {
        "test_id": f"XY_{name}",
        "direction": direction_for(name),
        "speed_mm_s": speed,
        "photo_count": len(photos),
        "photo_first_frame": numeric_frame(photos[0]),
        "photo_last_frame": numeric_frame(photos[-1]),
        "photo_set_frequency_Hz": SCREENSHOT_CAMERA_HZ.get(name),
        "photo_actual_frequency_Hz_est": actual_camera,
        "photo_window_time_s_est": image_span,
        "photo_window_displacement_mm_est": speed * image_span,
        "dic_export_displacement_mm": dic_displacement,
        "dic_export_displacement_source": "user_screenshot" if dic_displacement is not None else "not_provided",
        "force_sample_count": len(force_times),
        "force_time_s": force_span,
        "force_displacement_mm": speed * force_span,
        "force_sensor_frequency_Hz": 1000.0,
        "force_effective_frequency_Hz": force_frequency,
        "force_file": force_path.relative_to(data_root).as_posix(),
        "m2inp_frame_count": m2inp_frames(image_directory),
        "dic_csv_unique_frames": unique_csv_frames(image_directory),
        "force_onset_candidate_s": onset,
        "force_peak_candidate_s": peak_time,
        "force_drop_candidate_s": drop,
        "sync_method": "endpoint_linear_force_onset_to_force_record_end",
        "sync_status": "estimated_preloaded_start" if onset is None else "estimated_unique_force_value",
        "vfm_eligible": False,
    }
    dic_frequency_count = DIC_FREQUENCY_FRAME_COUNT[name]
    summary["dic_frame_count_for_frequency"] = dic_frequency_count
    summary["dic_frequency_count_source"] = (
        "contiguous_m2inp_or_csv_audited" if dic_frequency_count is not None else "unavailable_noncontiguous_m2inp"
    )
    if dic_frequency_count is not None:
        dic_frequency_full = (dic_frequency_count - 1) / force_span if force_span else None
        dic_frequency_event = (dic_frequency_count - 1) / image_span if image_span else None
        summary["dic_frequency_full_record_Hz"] = dic_frequency_full
        summary["dic_frequency_event_window_Hz"] = dic_frequency_event
        summary["dic_frequency_range_low_Hz"] = min(dic_frequency_full, dic_frequency_event)
        summary["dic_frequency_range_high_Hz"] = max(dic_frequency_full, dic_frequency_event)
        summary["dic_frequency_status"] = "estimated_range"
    else:
        for field in [
            "dic_frequency_full_record_Hz",
            "dic_frequency_event_window_Hz",
            "dic_frequency_range_low_Hz",
            "dic_frequency_range_high_Hz",
        ]:
            summary[field] = None
        summary["dic_frequency_status"] = "blocked_incomplete_dic_frames"
    return rows, summary


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields: list[str] = []
    for row in rows:
        for field in row:
            if field not in fields:
                fields.append(field)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_summary_markdown(path: Path, summaries: list[dict[str, object]]) -> None:
    lines = [
        "# XY 照片—力同步汇总表",
        "",
        "本表按用户提供的列结构生成。照片实际频率和照片窗口位移采用首尾事件锚定估算；DIC 位移列只有用户截图提供的六组保留值，其余写为待导出。DIC 有效频率范围见 `xy_dic_frequency_range.md`，逐帧结果见 `xy_photo_force_sync.csv`。",
        "",
        "| 试验 | 方向 | 速度 (mm/s) | 照片数量 | 照片设置频率 (Hz) | 照片实际拍摄频率估算 (Hz) | 照片导出的位移 (mm) | 力的数量 | 力数据算位移 (mm) | 力数据算时间 (s) | 力传感器频率 (Hz) | 同步状态 |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for item in summaries:
        lines.append(
            "| {test_id} | {direction} | {speed} | {photo_count} | {set_hz} | {actual_hz} | {dic_disp} | {force_count} | {force_disp} | {force_time} | {force_hz} | {status} |".format(
                test_id=item["test_id"],
                direction=item["direction"],
                speed=format_number(item["speed_mm_s"], 3),
                photo_count=item["photo_count"],
                set_hz=format_number(item["photo_set_frequency_Hz"], 3) or "待补",
                actual_hz=format_number(item["photo_actual_frequency_Hz_est"], 3) or "待算",
                dic_disp=format_number(item["dic_export_displacement_mm"], 3) or "待导出",
                force_count=item["force_sample_count"],
                force_disp=format_number(item["force_displacement_mm"], 4),
                force_time=format_number(item["force_time_s"], 4),
                force_hz=format_number(item["force_sensor_frequency_Hz"], 0),
                status=item["sync_status"],
            )
        )
    lines.extend(
        [
            "",
            "## 判定规则",
            "",
            "- `t_image_s_est` 将首张照片锚定到 `Press.T` 的加载起点候选，将末张照片锚定到力记录末样本，再对中间帧线性插值。每张照片因此都有唯一的插入力值。",
            "- 该映射没有使用相机硬件时间戳或共同触发号，`vfm_eligible=false`；取得触发/时间戳后应替换 `t_image_s_est`，而不是把估算值当成实测同步。",
            "- `照片导出的位移` 标有 `user_screenshot` 的行来自用户最新截图，其他行没有擅自从单点 CSV 推导。`photo_window_displacement_mm_est` 是本次端点映射对应的运动窗口位移。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_dic_frequency_range_markdown(path: Path, summaries: list[dict[str, object]]) -> None:
    lines = [
        "# XY DIC 有效频率范围表",
        "",
        "频率只作为平均有效频率范围使用，不代表逐帧硬件时间戳。下限使用完整 `Press.T` 时间窗口，上限使用加载起点候选到力记录末端的窗口；帧数优先采用已审计的连续 MatchID 输入帧数。",
        "",
        "| 试验 | 方向 | 速度 (mm/s) | 名义相机频率 (Hz) | DIC 帧数 | 完整力记录频率 (Hz) | 事件窗口频率 (Hz) | 建议范围 (Hz) | 计数来源 | 状态 |",
        "|---|---|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for item in summaries:
        low = item.get("dic_frequency_range_low_Hz")
        high = item.get("dic_frequency_range_high_Hz")
        if low is None or high is None:
            range_text = "待补"
        else:
            range_text = f"{format_number(low, 2)}–{format_number(high, 2)}"
        lines.append(
            "| {test_id} | {direction} | {speed} | {nominal} | {count} | {full} | {event} | {range_text} | {source} | {status} |".format(
                test_id=item["test_id"],
                direction=item["direction"],
                speed=format_number(item["speed_mm_s"], 3),
                nominal=format_number(item["photo_set_frequency_Hz"], 3) or "待补",
                count=item.get("dic_frame_count_for_frequency") or "待补",
                full=format_number(item.get("dic_frequency_full_record_Hz"), 2) or "待补",
                event=format_number(item.get("dic_frequency_event_window_Hz"), 2) or "待补",
                range_text=range_text,
                source=item["dic_frequency_count_source"],
                status=item["dic_frequency_status"],
            )
        )
    lines.extend(
        [
            "",
            "## 使用规则",
            "",
            "- `DIC 帧数`不使用原始 JPEG 总数；优先使用连续 MatchID 输入/已核对 CSV 帧数。",
            "- `XY-0.1-02` 的 m2inp 只有 10 个非连续帧，无法给出有意义的频率，暂时跳过；图片和力文件仍保留在逐帧清单中。",
            "- 频率范围只用于粗同步和方案筛选；正式 VFM 仍以共同触发号或逐帧时间戳为准。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-root", type=Path, default=Path(r"D:\C盘迁移\Desktop\yuan\data"))
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("实验/PA12-双轴-DIC-VFM/results"),
    )
    args = parser.parse_args()
    image_root = args.data_root / "XY" / "袁-20250529"
    force_root = args.data_root / "XY" / "20250529" / "20250529"
    missing = [name for name in IMAGE_DIR_TO_FORCE if not (image_root / name).is_dir()]
    if missing:
        raise FileNotFoundError(f"missing XY image directories: {missing}")
    all_rows: list[dict[str, object]] = []
    summaries: list[dict[str, object]] = []
    for name in IMAGE_DIR_TO_FORCE:
        rows, summary = analyse_trial(args.data_root, image_root / name, force_root)
        all_rows.extend(rows)
        summaries.append(summary)
    write_csv(args.out_dir / "xy_photo_force_sync.csv", all_rows)
    write_csv(args.out_dir / "xy_frequency_summary.csv", summaries)
    write_summary_markdown(args.out_dir / "xy_frequency_summary.md", summaries)
    write_dic_frequency_range_markdown(args.out_dir / "xy_dic_frequency_range.md", summaries)
    print(f"mapped_images={len(all_rows)} trials={len(summaries)}")
    print(f"output_dir={args.out_dir.resolve()}")


if __name__ == "__main__":
    main()
