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
# XY-0.1-02 currently covers Img000000--Img000257 while the photo set also
# contains Img000258. Its frequency is intentionally left unavailable until
# the final MatchID frame is included.
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

VISUAL_ENDPOINT_EVIDENCE = {
    "X-05-0.1-01": "末端 Img000128/129 起离开 ROI，Img000164 不作为破坏终点",
    "X-06-1.0-01": "Img000132 可见断裂/破坏，候选有效末帧",
    "X-07-10-01": "Img000080 模糊，末端破坏未确认",
    "Xy-0.1-01": "Img000288 可见明显破坏，候选有效末帧",
    "XY-0.1-02": "Img000258 可见破坏；当前 m2inp 覆盖到 Img000257，末帧未覆盖",
    "Xy-03-10-01": "Img000020 可见明显破坏，候选有效末帧",
    "Xy-04-1-01": "Img000250/266 可见破坏，需确认最后有效 ROI",
    "Y-09-0.1-02": "Img001824 中部断裂，候选有效末帧",
    "Y-10-1-01": "Img001557 破坏；末端力大幅变化，事件类型需核对",
    "Y-11-10-01": "Img000710 破坏；记录从高预载开始",
}

VISUAL_LAST_EVENT_CANDIDATE = {
    "X-05-0.1-01": "待核验（建议回溯至 ROI 完整帧）",
    "X-06-1.0-01": "132",
    "X-07-10-01": "待核验",
    "Xy-0.1-01": "288",
    "XY-0.1-02": "258（MatchID 输入未覆盖）",
    "Xy-03-10-01": "20",
    "Xy-04-1-01": "250/266（待核验）",
    "Y-09-0.1-02": "1824",
    "Y-10-1-01": "1557（事件类型待核验）",
    "Y-11-10-01": "710",
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


def event_frame(event_time: float | None, anchor_start: float, anchor_end: float, image_count: int) -> int | None:
    if event_time is None:
        return None
    fraction = (event_time - anchor_start) / (anchor_end - anchor_start)
    fraction = min(max(fraction, 0.0), 1.0)
    return int(math.floor(fraction * (image_count - 1) + 0.5))


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
    summary["image_frame_onset_est"] = event_frame(onset, anchor_start, anchor_end, len(photos))
    summary["image_frame_peak_est"] = event_frame(peak_time, anchor_start, anchor_end, len(photos))
    summary["image_frame_drop_est"] = event_frame(drop, anchor_start, anchor_end, len(photos))
    summary["image_frame_last_file"] = numeric_frame(photos[-1])
    summary["image_frame_last_event_candidate"] = VISUAL_LAST_EVENT_CANDIDATE[name]
    summary["visual_endpoint_evidence"] = VISUAL_ENDPOINT_EVIDENCE[name]
    summary["event_alignment_status"] = "preloaded_start_review" if onset is None else "event_frames_estimated_endpoint_review"
    summary["event_vfm_ready"] = False
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
        "本表按用户提供的列结构生成。照片实际频率和照片窗口位移采用首尾事件锚定估算；DIC 位移列只有用户截图提供的六组保留值，其余写为待导出。DIC 有效频率范围见 `xy_dic_frequency_range.md`，加载—峰值—破坏事件帧见 `xy_event_alignment.md`，逐帧结果见 `xy_photo_force_sync.csv`。",
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
            "- `XY-0.1-02` 的 m2inp 覆盖 Img000000–Img000257，照片 Img000258 尚未进入 MatchID；暂不计算完整 DIC 频率，图片和力文件仍保留在逐帧清单中。",
            "- 频率范围只用于粗同步和方案筛选；正式 VFM 仍以共同触发号或逐帧时间戳为准。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_event_alignment_markdown(path: Path, summaries: list[dict[str, object]]) -> None:
    lines = [
        "# XY 加载起点—峰值—破坏/结束事件对齐表",
        "",
        "本表把力记录事件投影到图像帧号，供人工确认和后续 VFM 窗口筛选。帧号是端点映射下的候选值；没有共同触发/相机时间戳时，状态保持 `review`，不能写成实测同步。",
        "",
        "| 试验 | 首帧加载起点候选帧 | 力峰值时间 (s) | 峰值候选帧 | 力下降时间 (s) | 下降候选帧 | 文件末帧 | 破坏/结束图像候选 | 图像证据 | 状态 |",
        "|---|---:|---:|---:|---:|---:|---:|---|---|---|",
    ]
    for item in summaries:
        lines.append(
            "| {test_id} | {onset_frame} | {peak_time} | {peak_frame} | {drop_time} | {drop_frame} | {last_file} | {last_event} | {visual} | {status} |".format(
                test_id=item["test_id"],
                onset_frame=item.get("image_frame_onset_est") if item.get("image_frame_onset_est") is not None else "待补（预载）",
                peak_time=format_number(item.get("force_peak_candidate_s"), 3),
                peak_frame=item.get("image_frame_peak_est") if item.get("image_frame_peak_est") is not None else "待补",
                drop_time=format_number(item.get("force_drop_candidate_s"), 3),
                drop_frame=item.get("image_frame_drop_est") if item.get("image_frame_drop_est") is not None else "待补",
                last_file=item["image_frame_last_file"],
                last_event=item["image_frame_last_event_candidate"],
                visual=item["visual_endpoint_evidence"],
                status=item["event_alignment_status"],
            )
        )
    lines.extend(
        [
            "",
            "## 固定使用规则",
            "",
            "- `首帧加载起点候选帧`、`峰值候选帧`和`下降候选帧`由同一端点时间映射得到，三者可以在同一帧轴上比较。",
            "- `破坏/结束图像候选`来自当前图像侧核对；若写“待核验”，不得把文件末帧直接送入 VFM。",
            "- 首帧、峰值、末帧三项均需在图像侧和力侧各有证据，且共同时间戳/触发号可复核后，`event_vfm_ready` 才能改为 `true`。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_event_force_candidates(all_rows: list[dict[str, object]], summaries: list[dict[str, object]]) -> list[dict[str, object]]:
    by_key = {(row["test_id"], row["image_frame"]): row for row in all_rows}
    candidates: list[dict[str, object]] = []
    for item in summaries:
        event_specs = [
            ("load_onset", item.get("image_frame_onset_est"), item.get("force_onset_candidate_s")),
            ("force_peak", item.get("image_frame_peak_est"), item.get("force_peak_candidate_s")),
            ("force_drop", item.get("image_frame_drop_est"), item.get("force_drop_candidate_s")),
            ("file_last", item.get("image_frame_last_file"), None),
        ]
        candidate_text = str(item["image_frame_last_event_candidate"])
        match = re.match(r"^(\d+)$", candidate_text)
        if match:
            event_specs.append(("visual_last_event", int(match.group(1)), None))
        seen: set[tuple[str, int]] = set()
        for event_type, frame, event_time in event_specs:
            if frame is None:
                continue
            key = (item["test_id"], int(frame))
            if (event_type, int(frame)) in seen:
                continue
            seen.add((event_type, int(frame)))
            source_row = by_key.get(key)
            if source_row is None:
                candidates.append(
                    {
                        "test_id": item["test_id"],
                        "event_type": event_type,
                        "image_frame": frame,
                        "image_file": "",
                        "t_image_s_est": "",
                        "event_time_s": event_time,
                        "force_mapping_status": "frame_not_in_photo_map",
                    }
                )
                continue
            row = {
                "test_id": item["test_id"],
                "direction": item["direction"],
                "speed_mm_s": item["speed_mm_s"],
                "event_type": event_type,
                "image_frame": frame,
                "image_file": source_row["image_file"],
                "t_image_s_est": source_row["t_image_s_est"],
                "event_time_s": event_time,
                "force_mapping_status": "estimated_from_endpoint_time_map",
                "visual_endpoint_evidence": item["visual_endpoint_evidence"],
                "event_alignment_status": item["event_alignment_status"],
                "event_vfm_ready": item["event_vfm_ready"],
            }
            for field in [
                "X1_Press_N",
                "X2_Press_N",
                "Y1_Press_N",
                "Y2_Press_N",
                "X1_Pos_mm",
                "X2_Pos_mm",
                "Y1_Pos_mm",
                "Y2_Pos_mm",
            ]:
                row[field] = source_row.get(field)
            candidates.append(row)
    return candidates


def write_event_force_candidates_markdown(path: Path, candidates: list[dict[str, object]]) -> None:
    lines = [
        "# XY 事件帧—力—位移候选表",
        "",
        "本表把事件对齐表中的候选图像帧直接展开为四通道力和四通道机器位移，作为 VFM 输入准备表。当前力值来自端点时间映射估计，`event_vfm_ready=false` 的行不得直接视为硬件同步结果。",
        "",
        "| 试验 | 事件 | 图像帧 | 估计图像时间 (s) | X1 力 (N) | X2 力 (N) | Y1 力 (N) | Y2 力 (N) | X1 位移 (mm) | X2 位移 (mm) | Y1 位移 (mm) | Y2 位移 (mm) | 映射状态 |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in candidates:
        lines.append(
            "| {test_id} | {event_type} | {frame} | {time} | {x1f} | {x2f} | {y1f} | {y2f} | {x1p} | {x2p} | {y1p} | {y2p} | {status} |".format(
                test_id=row["test_id"],
                event_type=row["event_type"],
                frame=row["image_frame"],
                time=format_number(float(row["t_image_s_est"]), 4) if row.get("t_image_s_est") not in (None, "") else "待补",
                x1f=format_number(float(row["X1_Press_N"]), 2) if row.get("X1_Press_N") not in (None, "") else "待补",
                x2f=format_number(float(row["X2_Press_N"]), 2) if row.get("X2_Press_N") not in (None, "") else "待补",
                y1f=format_number(float(row["Y1_Press_N"]), 2) if row.get("Y1_Press_N") not in (None, "") else "待补",
                y2f=format_number(float(row["Y2_Press_N"]), 2) if row.get("Y2_Press_N") not in (None, "") else "待补",
                x1p=format_number(float(row["X1_Pos_mm"]), 4) if row.get("X1_Pos_mm") not in (None, "") else "待补",
                x2p=format_number(float(row["X2_Pos_mm"]), 4) if row.get("X2_Pos_mm") not in (None, "") else "待补",
                y1p=format_number(float(row["Y1_Pos_mm"]), 4) if row.get("Y1_Pos_mm") not in (None, "") else "待补",
                y2p=format_number(float(row["Y2_Pos_mm"]), 4) if row.get("Y2_Pos_mm") not in (None, "") else "待补",
                status=row["force_mapping_status"],
            )
        )
    lines.extend(
        [
            "",
            "## 使用规则",
            "",
            "- `load_onset`、`force_peak`、`force_drop` 是力侧事件投影到图像帧的候选；`file_last` 和 `visual_last_event` 是图像末端候选。",
            "- VFM 试跑先使用事件顺序完整且图像证据明确的试验；`XY-0.1-02` 的破坏候选帧因 DIC 输入未覆盖，必须先重建 MatchID 输入。",
            "- 该表用于准备和筛选，真正提交论文前仍需共同触发/时间戳或同步敏感性分析。",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def chinese_event_labels(summaries: list[dict[str, object]]) -> dict[tuple[str, int], str]:
    labels: dict[tuple[str, int], list[str]] = {}
    for item in summaries:
        events = [
            ("加载起点", item.get("image_frame_onset_est")),
            ("力峰值", item.get("image_frame_peak_est")),
            ("峰后下降", item.get("image_frame_drop_est")),
            ("文件末帧", item.get("image_frame_last_file")),
        ]
        candidate_text = str(item["image_frame_last_event_candidate"])
        match = re.match(r"^(\d+)$", candidate_text)
        if match:
            events.append(("图像破坏候选", int(match.group(1))))
        for label, frame in events:
            if frame is None:
                continue
            key = (str(item["test_id"]), int(frame))
            labels.setdefault(key, []).append(label)
    return {key: "、".join(value) for key, value in labels.items()}


def simple_vfm_rows(all_rows: list[dict[str, object]], summaries: list[dict[str, object]]) -> list[dict[str, object]]:
    event_labels = chinese_event_labels(summaries)
    rows: list[dict[str, object]] = []
    for source in all_rows:
        key = (str(source["test_id"]), int(source["image_frame"]))
        rows.append(
            {
                "试验编号": source["test_id"],
                "方向": source["direction"],
                "速度_mm_s": source["speed_mm_s"],
                "照片帧号": source["image_frame"],
                "照片文件": source["image_file"],
                "估计时间_s": source["t_image_s_est"],
                "Fx1力_N": source.get("X1_Press_N"),
                "Fx2力_N": source.get("X2_Press_N"),
                "Fy1力_N": source.get("Y1_Press_N"),
                "Fy2力_N": source.get("Y2_Press_N"),
                "事件标签": event_labels.get(key, ""),
                "同步状态": "预载起点待核验" if source.get("force_onset_candidate_s") in (None, "") else "估计同步待核验",
            }
        )
    return rows


def write_simple_vfm_force_csv(path: Path, all_rows: list[dict[str, object]], summaries: list[dict[str, object]]) -> None:
    write_csv(path, simple_vfm_rows(all_rows, summaries))


def write_per_trial_vfm_force_csvs(output_dir: Path, all_rows: list[dict[str, object]], summaries: list[dict[str, object]]) -> None:
    rows = simple_vfm_rows(all_rows, summaries)
    output_dir.mkdir(parents=True, exist_ok=True)
    grouped: dict[str, list[dict[str, object]]] = {}
    for row in rows:
        grouped.setdefault(str(row["试验编号"]), []).append(row)
    for test_id, trial_rows in grouped.items():
        safe_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", test_id)
        write_csv(output_dir / f"{safe_name}_照片力对应.csv", trial_rows)


def write_simple_overview_markdown(path: Path, summaries: list[dict[str, object]]) -> None:
    lines = [
        "# 事件和频率概览",
        "",
        "日常只需要看本页和 `01_VFM照片力对应.csv`。频率使用范围，事件帧使用候选值；缺失证据的试验保留为“待核验”，不填猜测值。",
        "按试验拆分的逐照片四通道力 CSV 保存在同目录的 `照片力对应/` 文件夹。",
        "",
        "| 试验 | 方向 | 速度 (mm/s) | 照片数 | DIC 频率范围 (Hz) | 加载帧 | 峰值帧 | 峰后帧 | 破坏/结束候选 | 状态 |",
        "|---|---|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for item in summaries:
        low = item.get("dic_frequency_range_low_Hz")
        high = item.get("dic_frequency_range_high_Hz")
        frequency = "待补" if low is None or high is None else f"{format_number(low, 2)}–{format_number(high, 2)}"
        lines.append(
            "| {test_id} | {direction} | {speed} | {photo_count} | {frequency} | {onset} | {peak} | {drop} | {last_event} | {status} |".format(
                test_id=item["test_id"],
                direction=item["direction"],
                speed=format_number(item["speed_mm_s"], 3),
                photo_count=item["photo_count"],
                frequency=frequency,
                onset=item.get("image_frame_onset_est") if item.get("image_frame_onset_est") is not None else "预载/待补",
                peak=item.get("image_frame_peak_est") if item.get("image_frame_peak_est") is not None else "待补",
                drop=item.get("image_frame_drop_est") if item.get("image_frame_drop_est") is not None else "待补",
                last_event=item["image_frame_last_event_candidate"],
                status="预载起点待核验" if item["event_alignment_status"] == "preloaded_start_review" else "候选事件待核验",
            )
        )
    lines.extend(
        [
            "",
            "## 怎么用",
            "",
            "1. 先打开 `01_VFM照片力对应.csv`，一张照片对应一行，直接筛选试验编号或事件标签。",
            "2. 再用本页确认加载帧、峰值帧、峰后帧和破坏候选帧。",
            "3. 只有图像证据、力事件和同步时间都确认后，才把对应窗口送入 VFM；当前所有行仍是估计同步。",
            "",
            "详细审计文件统一保存在 `results/审计/`，日常不需要打开。",
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
    audit_dir = args.out_dir / "审计"
    write_csv(audit_dir / "xy_photo_force_sync.csv", all_rows)
    write_csv(audit_dir / "xy_frequency_summary.csv", summaries)
    write_summary_markdown(audit_dir / "xy_frequency_summary.md", summaries)
    write_dic_frequency_range_markdown(audit_dir / "xy_dic_frequency_range.md", summaries)
    write_event_alignment_markdown(audit_dir / "xy_event_alignment.md", summaries)
    event_fields = [
        "test_id",
        "direction",
        "speed_mm_s",
        "image_frame_onset_est",
        "force_peak_candidate_s",
        "image_frame_peak_est",
        "force_drop_candidate_s",
        "image_frame_drop_est",
        "image_frame_last_file",
        "image_frame_last_event_candidate",
        "visual_endpoint_evidence",
        "event_alignment_status",
        "event_vfm_ready",
    ]
    write_csv(
        audit_dir / "xy_event_alignment.csv",
        [{field: item.get(field) for field in event_fields} for item in summaries],
    )
    event_force_candidates = build_event_force_candidates(all_rows, summaries)
    write_csv(audit_dir / "xy_event_force_candidates.csv", event_force_candidates)
    write_event_force_candidates_markdown(audit_dir / "xy_event_force_candidates.md", event_force_candidates)
    write_simple_vfm_force_csv(args.out_dir / "01_VFM照片力对应.csv", all_rows, summaries)
    write_per_trial_vfm_force_csvs(args.out_dir / "照片力对应", all_rows, summaries)
    write_simple_overview_markdown(args.out_dir / "02_事件和频率概览.md", summaries)
    print(f"mapped_images={len(all_rows)} trials={len(summaries)}")
    print(f"output_dir={args.out_dir.resolve()}")


if __name__ == "__main__":
    main()
