"""Create manuscript-safe descriptive tables and figures from the XY audit outputs.

The source audit maps images to force records with an endpoint estimate.  This
script therefore reports image/frame facts and force histories only; it does
not convert the mapping into hardware synchronization or VFM eligibility.
"""

from __future__ import annotations

import csv
import math
import sys
from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[2]
AUDIT = ROOT / "results" / "审计"
OUT = ROOT / "results" / "analysis"
DATA_ROOT = Path(r"D:\C盘迁移\Desktop\yuan\data")
TOOLS = ROOT.parents[1] / "tools"
sys.path.insert(0, str(TOOLS))
import photo_force_sync as sync  # noqa: E402


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def number(row: dict[str, str], key: str) -> float | None:
    value = row.get(key, "")
    return None if value in (None, "") else float(value)


def integer(row: dict[str, str], key: str) -> int | None:
    value = row.get(key, "")
    return None if value in (None, "") else int(float(value))


def active_force(row: dict[str, str], direction: str, axis: str | None = None) -> float | None:
    axes = [axis] if axis else ([direction] if direction in ("X", "Y") else ["X", "Y"])
    values: list[float] = []
    for current_axis in axes:
        for channel in (f"{current_axis}1_Press_N", f"{current_axis}2_Press_N"):
            value = number(row, channel)
            if value is not None:
                values.append(abs(value))
    return sum(values) / len(values) if values else None


def fmt(value: float | int | None, digits: int = 3) -> str:
    if value is None:
        return "—"
    return f"{value:.{digits}f}".rstrip("0").rstrip(".")


def facts_table(
    summary_rows: list[dict[str, str]],
    alignment_rows: list[dict[str, str]],
    force_rows: list[dict[str, str]],
) -> list[dict[str, object]]:
    by_trial: dict[str, list[dict[str, str]]] = {}
    for row in force_rows:
        by_trial.setdefault(row["test_id"], []).append(row)
    alignment = {row["test_id"]: row for row in alignment_rows}
    facts: list[dict[str, object]] = []
    for summary in summary_rows:
        trial = summary["test_id"]
        rows = by_trial[trial]
        direction = summary["direction"]
        axis_peak = {
            axis: max(active_force(row, direction, axis) or 0.0 for row in rows)
            for axis in ([direction] if direction in ("X", "Y") else ["X", "Y"])
        }
        item: dict[str, object] = {
            "test_id": trial,
            "direction": direction,
            "speed_mm_s": float(summary["speed_mm_s"]),
            "jpeg_frames": int(summary["photo_count"]),
            "force_samples": int(summary["force_sample_count"]),
            "image_frequency_est_Hz": float(summary["photo_actual_frequency_Hz_est"]),
            "camera_frequency_nominal_Hz": number(summary, "photo_set_frequency_Hz"),
            "force_frequency_effective_Hz": float(summary["force_effective_frequency_Hz"]),
            "image_window_s_est": float(summary["photo_window_time_s_est"]),
            "force_window_s": float(summary["force_time_s"]),
            "force_displacement_mm": float(summary["force_displacement_mm"]),
            "m2inp_frames": integer(summary, "m2inp_frame_count"),
            "dic_csv_unique_frames": integer(summary, "dic_csv_unique_frames"),
            "onset_frame_est": integer(alignment[trial], "image_frame_onset_est"),
            "peak_frame_est": integer(alignment[trial], "image_frame_peak_est"),
            "drop_frame_est": integer(alignment[trial], "image_frame_drop_est"),
            "last_frame": integer(alignment[trial], "image_frame_last_file"),
            "visual_last_candidate": alignment[trial]["image_frame_last_event_candidate"],
            "sync_status": summary["sync_status"],
            "vfm_eligible": summary["vfm_eligible"],
            "active_force_peak_X_N": axis_peak.get("X"),
            "active_force_peak_Y_N": axis_peak.get("Y"),
        }
        facts.append(item)
    return facts


def write_facts(facts: list[dict[str, object]]) -> None:
    fields = list(facts[0])
    with (OUT / "xy_trial_facts.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(facts)

    lines = [
        "# XY 试验事实表（论文工作稿）",
        "",
        "本表由 `results/审计/xy_frequency_summary.csv`、`xy_event_alignment.csv` 和 `xy_photo_force_sync.csv` 生成。它描述当前文件级审计事实，不把照片—力端点映射当作硬件同步，也不把图像序列数当作独立试样数。",
        "",
        "| 试验 | 方向 | 速度 (mm/s) | JPG 帧数 | 力样本数 | 图像频率估计 (Hz) | 力频率 (Hz) | DIC/MatchID 输入帧数 | 峰值候选帧 | 末端候选 | VFM 准入 |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|",
    ]
    for item in facts:
        lines.append(
            "| {trial} | {direction} | {speed} | {jpg} | {force} | {image_hz} | {force_hz} | {m2inp} | {peak} | {last} | {vfm} |".format(
                trial=item["test_id"],
                direction=item["direction"],
                speed=fmt(item["speed_mm_s"], 1),
                jpg=item["jpeg_frames"],
                force=item["force_samples"],
                image_hz=fmt(item["image_frequency_est_Hz"], 2),
                force_hz=fmt(item["force_frequency_effective_Hz"], 2),
                m2inp=item["m2inp_frames"] if item["m2inp_frames"] is not None else "—",
                peak=item["peak_frame_est"] if item["peak_frame_est"] is not None else "—",
                last=item["visual_last_candidate"],
                vfm=item["vfm_eligible"],
            )
        )
    lines.extend(
        [
            "",
            "## 字段解释",
            "",
            "- `图像频率估计` =（JPG 帧数−1）/端点估计的照片时间窗口；不是相机时间戳测得的帧率。",
            "- `峰值候选帧`由力侧峰值时间投影到上述端点映射；`末端候选`来自当前图像侧记录，待人工复核。",
            "- `VFM 准入` 当前全部为 `False`，因为文件中没有共同相机—DAQ 触发号或可核验的逐帧相机时间戳。",
            "- 10 组序列和 5309 张 JPG 是文件/帧计数，不等于 10 个独立试样；试样数量和几何批次仍待作者记录。",
        ]
    )
    (OUT / "xy_trial_facts.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def setup_figure(width: float = 12.0, height: float = 7.0):
    plt.rcParams.update({"font.size": 9, "axes.titlesize": 10, "axes.labelsize": 9})
    fig = plt.figure(figsize=(width, height), dpi=180, constrained_layout=True)
    return fig


def figure_force_history(force_rows: list[dict[str, str]], summary_rows: list[dict[str, str]], path: Path) -> None:
    by_trial: dict[str, list[dict[str, str]]] = {}
    for row in force_rows:
        by_trial.setdefault(row["test_id"], []).append(row)
    fig, axes = plt.subplots(2, 5, figsize=(13, 5.8), dpi=180, sharey=True, constrained_layout=True)
    colors = {"X": "#2563a6", "Y": "#b33c3c", "XY": "#2f855a"}
    global_max = max(
        active_force(row, summary["direction"], axis)
        or 0.0
        for summary in summary_rows
        for row in by_trial[summary["test_id"]]
        for axis in ([summary["direction"]] if summary["direction"] in ("X", "Y") else ["X", "Y"])
    )
    for ax, summary in zip(axes.flat, summary_rows):
        trial = summary["test_id"]
        rows = by_trial[trial]
        direction = summary["direction"]
        frames = [int(row["image_frame"]) for row in rows]
        if direction in ("X", "Y"):
            values = [active_force(row, direction) for row in rows]
            ax.plot(frames, values, color=colors[direction], lw=1.1, label=f"|F{direction}| mean")
        else:
            for axis, color in (("X", "#2563a6"), ("Y", "#b33c3c")):
                values = [active_force(row, direction, axis) for row in rows]
                ax.plot(frames, values, color=color, lw=1.0, label=f"|F{axis}|")
        peak_frame = integer(summary, "image_frame_peak_est")
        if peak_frame is not None:
            peak_row = next(row for row in rows if int(row["image_frame"]) == peak_frame)
            peak = active_force(peak_row, direction, direction) if direction in ("X", "Y") else None
            if peak is not None:
                ax.scatter([peak_frame], [peak], s=13, color="#111827", zorder=3)
            else:
                ax.axvline(peak_frame, color="#111827", lw=0.8, ls=":", zorder=2)
        ax.set_title(f"{trial.replace('XY_', '')}\nv={summary['speed_mm_s']} mm/s")
        ax.set_xlabel("Image frame")
        ax.grid(alpha=0.22, lw=0.5)
        ax.set_ylim(0, global_max * 1.05)
        if direction == "XY":
            ax.legend(frameon=False, fontsize=7, loc="upper left")
    axes[0, 0].set_ylabel("Absolute force magnitude (N)")
    axes[1, 0].set_ylabel("Absolute force magnitude (N)")
    fig.suptitle("XY tests: frame-indexed force histories from endpoint-mapped records", fontsize=12)
    fig.text(0.5, 0.002, "The horizontal axis is the saved JPEG frame number; the force–frame pairing is estimated and not hardware-trigger validated.", ha="center", fontsize=8)
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def figure_frequency_frames(summary_rows: list[dict[str, str]], path: Path) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.4), dpi=180, constrained_layout=True)
    colors = {"X": "#2563a6", "Y": "#b33c3c", "XY": "#2f855a"}
    for summary in summary_rows:
        direction = summary["direction"]
        speed = float(summary["speed_mm_s"])
        image_hz = float(summary["photo_actual_frequency_Hz_est"])
        marker = {"X": "o", "Y": "s", "XY": "^"}[direction]
        ax1.scatter(speed, image_hz, s=38, marker=marker, color=colors[direction], edgecolor="white", linewidth=0.5, zorder=3)
        nominal = number(summary, "photo_set_frequency_Hz")
        if nominal is not None:
            ax1.scatter(speed, nominal, s=48, marker="x", color=colors[direction], linewidth=1.2, zorder=4)
        jpeg = int(summary["photo_count"])
        m2inp = integer(summary, "m2inp_frame_count")
        y = m2inp if m2inp is not None else math.nan
        ax2.scatter(jpeg, y, s=38, marker=marker, color=colors[direction], edgecolor="white", linewidth=0.5, zorder=3)
    ax1.set_xscale("log")
    ax1.set_yscale("log")
    ax1.set_xlabel("Nominal actuator speed (mm/s)")
    ax1.set_ylabel("Image frequency estimate (Hz)")
    ax1.grid(alpha=0.25, which="both", lw=0.5)
    ax1.set_title("Sampling-rate audit")
    ax1.text(0.03, 0.04, "● endpoint estimate\n× nominal camera setting", transform=ax1.transAxes, fontsize=8, bbox={"facecolor": "white", "alpha": 0.78, "edgecolor": "none"})
    max_frames = max(int(row["photo_count"]) for row in summary_rows)
    ax2.plot([1, max_frames], [1, max_frames], ls="--", color="#6b7280", lw=0.8, label="1:1")
    ax2.set_xscale("log")
    ax2.set_yscale("log")
    ax2.set_xlabel("Saved JPEG frames")
    ax2.set_ylabel("MatchID input frame count")
    ax2.grid(alpha=0.25, which="both", lw=0.5)
    ax2.set_title("Image-to-DIC frame-count audit")
    ax2.legend(frameon=False, fontsize=8)
    fig.suptitle("XY image acquisition and DIC frame consistency", fontsize=12)
    fig.text(0.5, 0.002, "Markers are sequence-level file counts; they do not establish independent specimens or frame timestamps.", ha="center", fontsize=8)
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def figure_events(alignment_rows: list[dict[str, str]], path: Path) -> None:
    fig, ax = plt.subplots(figsize=(11, 5.6), dpi=180, constrained_layout=True)
    y_positions = list(range(len(alignment_rows)))[::-1]
    for y, row in zip(y_positions, alignment_rows):
        last = integer(row, "image_frame_last_file")
        ax.hlines(y, 0, 1, color="#d1d5db", lw=2)
        points = [
            ("image_frame_onset_est", "onset", "#2563a6"),
            ("image_frame_peak_est", "peak", "#111827"),
            ("image_frame_drop_est", "drop", "#d97706"),
        ]
        for key, _, color in points:
            frame = integer(row, key)
            if frame is not None and last:
                ax.scatter(frame / last, y, s=28, color=color, zorder=3)
        visual = row["image_frame_last_event_candidate"]
        if visual.isdigit() and last:
            ax.scatter(int(visual) / last, y, s=38, marker="D", facecolor="white", edgecolor="#b33c3c", zorder=4)
        ax.scatter(1, y, s=20, marker="|", color="#6b7280", zorder=3)
    ax.set_yticks(y_positions, [row["test_id"].replace("XY_", "") for row in alignment_rows])
    ax.set_xlim(-0.02, 1.04)
    ax.set_xlabel("Candidate frame position / file last frame")
    ax.set_title("Event-frame projection under endpoint time mapping")
    ax.grid(axis="x", alpha=0.25, lw=0.5)
    from matplotlib.lines import Line2D

    legend = [
        Line2D([0], [0], marker="o", color="w", markerfacecolor="#2563a6", label="load onset", markersize=6),
        Line2D([0], [0], marker="o", color="w", markerfacecolor="#111827", label="force peak", markersize=6),
        Line2D([0], [0], marker="o", color="w", markerfacecolor="#d97706", label="post-peak drop", markersize=6),
        Line2D([0], [0], marker="D", color="#b33c3c", markerfacecolor="white", label="visual endpoint candidate", markersize=6),
        Line2D([0], [0], marker="|", color="#6b7280", label="last saved frame", markersize=8),
    ]
    ax.legend(handles=legend, frameon=False, ncol=3, loc="lower center", bbox_to_anchor=(0.5, -0.18), fontsize=8)
    fig.text(0.5, 0.002, "All markers are candidates for review; Y-11 begins under preloading and has no detected zero-load onset.", ha="center", fontsize=8)
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)


def timing_sensitivity(summary_rows: list[dict[str, str]], alignment_rows: list[dict[str, str]]) -> None:
    """Quantify explicitly hypothetical frame-registration shifts."""
    trial = "XY_Xy-0.1-01"
    summary = next(row for row in summary_rows if row["test_id"] == trial)
    alignment = next(row for row in alignment_rows if row["test_id"] == trial)
    force_path = DATA_ROOT / Path(summary["force_file"])
    header, force_rows = sync.load_sheet(force_path, "Press")
    press = {name: [row[index] for row in force_rows] for index, name in enumerate(header)}
    force_times = press.pop("T")
    onset, _, _ = sync.detect_events(force_times, press, "XY")
    anchor_start = onset if onset is not None else force_times[0]
    anchor_end = force_times[-1]
    image_count = int(summary["photo_count"])
    mapped_times = [
        anchor_start + i / (image_count - 1) * (anchor_end - anchor_start)
        for i in range(image_count)
    ]

    def axis_force(time_value: float, axis: str) -> float:
        values = [
            abs(sync.interpolate(time_value, force_times, press[f"{axis}{channel}_Press"]))
            for channel in (1, 2)
        ]
        return sum(values) / len(values)

    reference = {
        axis: [axis_force(time_value, axis) for time_value in mapped_times]
        for axis in ("X", "Y")
    }
    peak_frame = int(alignment["image_frame_peak_est"])
    drop_frame = int(alignment["image_frame_drop_est"])
    shifts = (-5, -2, -1, 0, 1, 2, 5)
    rows: list[dict[str, object]] = []
    shifted_norm: dict[int, list[float]] = {}
    for shift in shifts:
        errors: list[float] = []
        shifted_norm[shift] = []
        for frame, time_value in enumerate(mapped_times):
            shifted_frame = min(max(frame + shift, 0), image_count - 1)
            shifted_time = mapped_times[shifted_frame]
            shifted = {axis: axis_force(shifted_time, axis) for axis in ("X", "Y")}
            errors.extend(abs(shifted[axis] - reference[axis][frame]) for axis in ("X", "Y"))
            shifted_norm[shift].append(math.hypot(shifted["X"], shifted["Y"]))
        rows.append(
            {
                "trial": trial,
                "shift_frames": shift,
                "max_abs_channel_delta_N": max(errors),
                "mean_abs_channel_delta_N": sum(errors) / len(errors),
                "delta_at_force_peak_N": max(
                    abs(axis_force(mapped_times[peak_frame + shift], axis) - reference[axis][peak_frame])
                    if 0 <= peak_frame + shift < image_count
                    else 0.0
                    for axis in ("X", "Y")
                ),
                "delta_at_postpeak_drop_N": max(
                    abs(axis_force(mapped_times[drop_frame + shift], axis) - reference[axis][drop_frame])
                    if 0 <= drop_frame + shift < image_count
                    else 0.0
                    for axis in ("X", "Y")
                ),
                "interpretation": "hypothetical frame-registration scenario; not a confidence interval",
            }
        )
    fields = list(rows[0])
    with (OUT / "XY_Xy-0.1-01_timing_sensitivity.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    lines = [
        "# XY_Xy-0.1-01 时间扰动敏感性（假设场景）",
        "",
        "本表使用原始 `Press.T` 和四通道力记录，沿现有 `endpoint_linear_force_onset_to_force_record_end` 映射，对图像帧索引施加假设的 ±1、±2、±5 帧登记扰动。它回答“若帧—力对应向前/后错若干帧，载荷会改变多少”，不提供实测同步精度或置信区间。",
        "",
        "| 帧索引扰动 | 全序列最大通道载荷差 (N) | 全序列平均通道载荷差 (N) | 力峰值候选帧处差值 (N) | 峰后下降候选帧处差值 (N) |",
        "|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            "| {shift} | {maximum} | {mean} | {peak} | {drop} |".format(
                shift=row["shift_frames"],
                maximum=fmt(row["max_abs_channel_delta_N"], 1),
                mean=fmt(row["mean_abs_channel_delta_N"], 1),
                peak=fmt(row["delta_at_force_peak_N"], 1),
                drop=fmt(row["delta_at_postpeak_drop_N"], 1),
            )
        )
    lines.extend(
        [
            "",
            "选择该序列是因为它具有 289 张 JPG、289 个 MatchID 输入帧、X/Y 两方向 DIC 导出记录和明确的图像末端破坏候选。当前仍未获得共同相机—DAQ 触发号，因此此分析只用于识别同步风险。",
        ]
    )
    (OUT / "XY_Xy-0.1-01_timing_sensitivity.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.7), dpi=180, constrained_layout=True)
    lo, hi = peak_frame - 35, drop_frame + 15
    reference_norm = [math.hypot(reference["X"][i], reference["Y"][i]) for i in range(image_count)]
    ax1.plot(range(lo, hi + 1), reference_norm[lo : hi + 1], color="#111827", lw=1.7, label="reference endpoint map")
    for shift, color in ((-1, "#2563a6"), (1, "#b33c3c")):
        ax1.plot(
            range(lo, hi + 1),
            shifted_norm[shift][lo : hi + 1],
            color=color,
            lw=1.0,
            ls="--",
            label=f"{shift:+d} frame scenario",
        )
    ax1.axvline(peak_frame, color="#6b7280", lw=0.8, ls=":")
    ax1.axvline(drop_frame, color="#d97706", lw=0.9, ls=":")
    ax1.text(peak_frame, ax1.get_ylim()[1] * 0.9, "peak", ha="center", fontsize=8)
    ax1.text(drop_frame, ax1.get_ylim()[1] * 0.8, "drop", ha="center", fontsize=8)
    ax1.set_xlabel("Image frame")
    ax1.set_ylabel("Two-axis force-vector norm (N)\n(channel magnitudes)")
    ax1.set_title("Illustrative timing displacement near force collapse")
    ax1.grid(alpha=0.25, lw=0.5)
    ax1.legend(frameon=False, fontsize=8)
    x = [row["shift_frames"] for row in rows]
    width = 0.22
    ax2.bar([value - width for value in x], [row["max_abs_channel_delta_N"] for row in rows], width=width, color="#6b7280", label="maximum over sequence")
    ax2.bar(x, [row["delta_at_postpeak_drop_N"] for row in rows], width=width, color="#d97706", label="at drop candidate")
    ax2.bar([value + width for value in x], [row["delta_at_force_peak_N"] for row in rows], width=width, color="#2563a6", label="at peak candidate")
    ax2.axhline(0, color="#111827", lw=0.7)
    ax2.set_xticks(x)
    ax2.set_xlabel("Hypothetical frame-registration shift")
    ax2.set_ylabel("Absolute channel-force difference (N)")
    ax2.set_title("Scenario sensitivity; not measured uncertainty")
    ax2.grid(axis="y", alpha=0.25, lw=0.5)
    ax2.legend(frameon=False, fontsize=7, loc="upper left")
    fig.suptitle("How image–load time registration can change the observed event load", fontsize=12)
    fig.text(0.5, 0.002, "XY_Xy-0.1-01; shifts are analytical scenarios applied to the original Press.T record.", ha="center", fontsize=8)
    fig.savefig(OUT / "Fig5_timing_sensitivity_Xy-0.1-01.png", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    summary_rows = read_csv(AUDIT / "xy_frequency_summary.csv")
    alignment_rows = read_csv(AUDIT / "xy_event_alignment.csv")
    force_rows = read_csv(AUDIT / "xy_photo_force_sync.csv")
    if {row["test_id"] for row in summary_rows} != {row["test_id"] for row in alignment_rows}:
        raise ValueError("summary and event alignment trial IDs differ")
    if sum(int(row["photo_count"]) for row in summary_rows) != len(force_rows):
        raise ValueError("summary photo count does not equal force-map row count")
    facts = facts_table(summary_rows, alignment_rows, force_rows)
    write_facts(facts)
    figure_force_history(force_rows, summary_rows, OUT / "Fig2_force_history_audit.png")
    figure_frequency_frames(summary_rows, OUT / "Fig3_frequency_frame_audit.png")
    figure_events(alignment_rows, OUT / "Fig4_event_frame_audit.png")
    timing_sensitivity(summary_rows, alignment_rows)
    print(f"facts={len(facts)} force_rows={len(force_rows)}")
    print(f"outputs={OUT}")


if __name__ == "__main__":
    main()
