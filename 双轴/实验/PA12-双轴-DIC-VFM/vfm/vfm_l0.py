"""最小可复现的二维平面应力 VFM 基准。

输入为已经整理好的逐点应变和虚场，不读取 MatchID 私有工程文件。
所有数值默认使用 N、mm、MPa；剪应变 gxy 为工程剪应变。
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np


def assemble_equations(field_rows, virtual_rows, boundary_rows, thickness_mm):
    """组装 A q = b，q=[Q11,Q22,Q12,Q66]。"""
    fields = {}
    for r in field_rows:
        if int(r["valid"]) != 1:
            continue
        fields[(str(r["frame_id"]), str(r["point_id"]))] = r
    vmap = {(str(r["virtual_field_id"]), str(r["point_id"])): r for r in virtual_rows}
    bmap = {str(r["virtual_field_id"]): r for r in boundary_rows}
    rows = []
    rhs = []
    for vid, br in bmap.items():
        coeff = np.zeros(4, dtype=float)
        for (frame, pid), fr in fields.items():
            vr = vmap.get((vid, pid))
            if vr is None or str(fr["frame_id"]) != str(br["frame_id"]):
                continue
            a = float(fr["area_mm2"])
            exx, eyy, gxy = (float(fr[k]) for k in ("exx", "eyy", "gxy"))
            exs, eys, gys = (float(vr[k]) for k in ("exx_star", "eyy_star", "gxy_star"))
            coeff += thickness_mm * a * np.array([exx * exs, eyy * eys, exx * eys + eyy * exs, gxy * gys])
        rows.append(coeff)
        rhs.append(float(br["fx_N"]) * float(br["loaded_ux_star"]) + float(br["fy_N"]) * float(br["loaded_uy_star"]))
    A = np.asarray(rows, dtype=float)
    b = np.asarray(rhs, dtype=float)
    if A.shape[0] < 4:
        raise ValueError("虚场方程少于4行，不能识别四个刚度参数")
    rank = int(np.linalg.matrix_rank(A))
    if rank < 4:
        raise ValueError(f"虚场矩阵秩为 {rank}，低于4，完整参数不可辨识")
    q, residuals, _, _ = np.linalg.lstsq(A, b, rcond=None)
    rel = float(np.linalg.norm(A @ q - b) / max(np.linalg.norm(b), np.finfo(float).eps))
    return {"q": q.tolist(), "rank": rank, "condition_number": float(np.linalg.cond(A)), "relative_residual": rel}


def synthetic_dataset(out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    q_true = np.array([420.0, 360.0, 110.0, 150.0])
    # 非均匀应变场；四个虚场使 A 满秩。每个虚场只用一个共同的合力边界自由度。
    points = [(i, float(i % 5) * 5.0, float(i // 5) * 5.0) for i in range(25)]
    strain = {pid: (0.010 + 0.0002 * x + 0.0001 * y,
                   0.004 + 0.0001 * x + 0.0002 * y,
                   0.003 + 0.0001 * (x + y)) for pid, x, y in points}
    virtual_ids = tuple(range(12))
    rng = np.random.default_rng(42)
    field_rows = []
    vrows = []
    for pid, x, y in points:
        exx, eyy, gxy = strain[pid]
        field_rows.append({"frame_id": "0", "point_id": str(pid), "x_mm": x, "y_mm": y, "u_mm": 0, "v_mm": 0, "exx": exx, "eyy": eyy, "gxy": gxy, "quality": 1, "valid": 1, "area_mm2": 25})
        for vid in virtual_ids:
            exs, eys, gys = rng.normal(0.0, 1.0, 3)
            vrows.append({"virtual_field_id": str(vid), "point_id": str(pid), "ux_star": 1 if vid == 0 else 0, "uy_star": 0, "exx_star": exs, "eyy_star": eys, "gxy_star": gys})
    boundary_rows = []
    # 使每一行的外虚功恰好等于内虚功；合力以 N 表示，厚度和面积均为 mm。
    for vid in virtual_ids:
        coeff = np.zeros(4)
        for fr in field_rows:
            vr = next(r for r in vrows if r["virtual_field_id"] == str(vid) and r["point_id"] == fr["point_id"])
            coeff += 2.0 * fr["area_mm2"] * np.array([fr["exx"] * vr["exx_star"], fr["eyy"] * vr["eyy_star"], fr["exx"] * vr["eyy_star"] + fr["eyy"] * vr["exx_star"], fr["gxy"] * vr["gxy_star"]])
        b = float(coeff @ q_true)
        boundary_rows.append({"frame_id": "0", "virtual_field_id": str(vid), "fx_N": b, "fy_N": 0, "loaded_ux_star": 1, "loaded_uy_star": 0, "sync_status": "synthetic"})
    def dump(name, rows):
        with (out_dir / name).open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    dump("field.csv", field_rows); dump("virtual_fields.csv", vrows); dump("virtual_boundary.csv", boundary_rows)
    result = assemble_equations(field_rows, vrows, boundary_rows, 2.0)
    result["q_true"] = q_true.tolist()
    result["max_relative_parameter_error"] = float(np.max(np.abs((np.asarray(result["q"]) - q_true) / q_true)))
    (out_dir / "result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result


if __name__ == "__main__":
    out_dir = Path(__file__).parent / "examples" / "synthetic_l0"
    result = synthetic_dataset(out_dir)
    # 固定随机种子的扰动试验，用于检查 10% 误差门，而不是伪造实测精度。
    base = out_dir
    with (base / "field.csv").open(encoding="utf-8") as f: fields = list(csv.DictReader(f))
    with (base / "virtual_fields.csv").open(encoding="utf-8") as f: vfields = list(csv.DictReader(f))
    with (base / "virtual_boundary.csv").open(encoding="utf-8") as f: bounds = list(csv.DictReader(f))
    rng = np.random.default_rng(20260915); true = np.array(result["q_true"])
    rows = []
    for pct in (0.01, 0.02, 0.05, 0.10):
        noisy_fields = []
        for row in fields:
            item = dict(row)
            for key in ("exx", "eyy", "gxy"): item[key] = str(float(row[key]) * (1.0 + pct * rng.uniform(-1.0, 1.0)))
            noisy_fields.append(item)
        noisy_bounds = []
        for row in bounds:
            item = dict(row); item["fx_N"] = str(float(row["fx_N"]) * (1.0 + pct * rng.uniform(-1.0, 1.0))); noisy_bounds.append(item)
        fit = assemble_equations(noisy_fields, vfields, noisy_bounds, 2.0)
        err = float(np.max(np.abs((np.asarray(fit["q"]) - true) / true)))
        rows.append({"relative_noise": pct, "max_relative_parameter_error": err, "relative_residual": fit["relative_residual"], "pass_10pct_gate": err <= 0.10})
    with (base / "noise_sensitivity.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print(json.dumps(result, ensure_ascii=False, indent=2))
