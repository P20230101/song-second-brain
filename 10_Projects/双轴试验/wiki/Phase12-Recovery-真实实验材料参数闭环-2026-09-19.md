---
phase: 12-recovery
status: waiting_manual_review
data_status: real_only
synthetic_used: false
phase14_status: paused
included_experiments: 8
excluded_experiments: 2
---

# Phase 12 Recovery｜真实实验材料参数识别闭环

## 状态

Phase 14 已暂停；Recovery 已用当前 8 个真实实验完成一次实验级 5/2/1 MLP 重训，但不作泛化结论。Phase 12 Recovery 已完成，正式数据库已重建；当前停止，等待人工检查。

## 根因与修复

1. `XY_X-06-1.0-01` 有 266 个 `exx/eyy/exy=nan` 点，但原正式化逻辑仍将其标记为 `valid=1`。已修正有效性判定：应变字段非有限的点变为 `valid=0`，不填充、不插值、不生成 synthetic 数据。
2. Phase 13.5 审计已与求解器保持一致，只对 `valid=1` 行检查有限性。
3. 数据库构建器已修正：缺少 `run_manifest.json` 的 experiment_id 也必须写入 `audit/excluded_experiments`，不再静默丢失。

## 重新运行结果

八个真实实验均完成 Phase 11 二维 VFM 和 Phase 12 联合识别；每个结果都包含完整的 `E_MPa`、`nu`、`sigma_y_MPa`、`H_MPa`、`n`，并且 `fit.success=true`。

| experiment_id | E_MPa | nu | sigma_y_MPa | H_MPa | n |
|---|---:|---:|---:|---:|---:|
| `XY_X-06-1.0-01` | 1.0000 | 0.0000 | 34.2112 | 217.1667 | 0.4928 |
| `XY_X-07-10-01` | 1.0000 | 0.0000 | 47.1781 | 508.4831 | 0.4815 |
| `XY_Xy-0.1-01` | 792.3598 | 0.0000 | 132.4286 | 715.9217 | 0.8021 |
| `XY_Xy-03-10-01` | 5000.0000 | 0.0000 | 206.7489 | 3942.2261 | 0.3440 |
| `XY_Xy-04-1-01` | 2298.0971 | 0.0000 | 127.9771 | 641.3293 | 0.8435 |
| `XY_Y-09-0.1-02` | 1.1500 | 0.0000 | 0.0100 | 0.0010 | 2.0000 |
| `XY_Y-10-1-01` | 1.6696 | 0.0000 | 0.0528 | 0.0087 | 0.1573 |
| `XY_Y-11-10-01` | 1.0000 | 0.0000 | 10.0000 | 100.0000 | 0.5000 |

参数出现触边和极小值，说明识别稳定性仍需人工复核；本页面只记录计算结果，不把它们解释为已验证的 PA12 本构常数。

## 数据库

- [PA12_database.h5](../实验/PA12-双轴-DIC-VFM/PA12_database.h5)
- [database_quality_report.json](../实验/PA12-双轴-DIC-VFM/database_quality_report.json)
- [数据库构建日志](../实验/PA12-双轴-DIC-VFM/PA12_database.recovery_usable_frames.log)

HDF5 校验结果：

- `included_experiment_count=8`
- `excluded_experiment_count=2`
- `source_is_real=true`
- `synthetic_used=false`
- `ai_used=false`
- 每个纳入实验均存在完整五参数组

## 纳入与排除

纳入：`XY_X-06-1.0-01`、`XY_X-07-10-01`、`XY_Xy-0.1-01`、`XY_Xy-03-10-01`、`XY_Xy-04-1-01`、`XY_Y-09-0.1-02`、`XY_Y-10-1-01`、`XY_Y-11-10-01`。

排除：

- `XY_X-05-0.1-01`：实际可用 DIC 为 151 帧；缺正式 MatchID 应变导出、Force.csv 和力值闭合，因此仍不能进入 VFM。
- `XY_XY-0.1-02`：无正式 VFM 输入和准入检查。

### 可用帧集合修正与照片归档

本次审计按“同时存在 `.jpg` 与 `.jpg.dat` 的 `frame_id` 集合”判定 DIC 可用帧，不再要求它等于相机原始拍摄总数。为使原始目录与可用集合一致，以下多余文件已移动到各试验目录下的 `excluded_frames`，保留可恢复副本，未永久删除：

- `XY_X-05-0.1-01`：归档 14 个无 `.dat` 对应的 `.jpg`，可用集合为 151 帧。
- `XY_Xy-04-1-01`：归档 frame 250、254–266 的 14 对 `.jpg/.jpg.dat`，正式 DIC 与可用集合均为 253 帧，已完成 Phase 11/12 并纳入数据库。
- `XY_X-07-10-01`：归档 frame 80 的 `.jpg/.jpg.dat`，正式 DIC 与可用集合均为 80 帧，已纳入数据库。

上述排除项已写入 HDF5 的 `audit/excluded_experiments`，没有被静默删除。

## 关键文件

- [Phase 11/12 真实运行目录](../实验/PA12-双轴-DIC-VFM/real_data_pipeline/runs)
- [Phase 12 识别脚本](../实验/PA12-双轴-DIC-VFM/PA12_AI_VFM/VFM_Biaxial/real_multiaxial_identification.py)
- [Phase 13.5 审计脚本](../实验/PA12-双轴-DIC-VFM/real_data_pipeline/phase13_5_quality.py)
- [数据库构建脚本](../实验/PA12-双轴-DIC-VFM/PA12_AI_VFM/Database/build_pa12_database.py)
- [真实本构、VFM拟合与虚功同步说明](Phase12-Recovery-VFM本构与虚功同步说明-2026-09-19.md)
- [真实单轴应力–应变加载支](../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/single_axis_real_stress_strain.png)
- [真实本构与VFM识别本构对比](../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/single_axis_vfm_constitutive_compare.png)
- [照片与同编号虚功同步证据](../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/vfm_virtual_work_sync_evidence.png)
- [Phase 14 Recovery输出](../实验/PA12-双轴-DIC-VFM/PA12_AI_VFM/AI_Model/phase14_real_recovery)

## 人工检查项

1. 核对 X-06 的 266 个 `valid=0` 点是否符合 MatchID 原始点质量语义。
2. 复核八个实验的力值符号、厚度、ROI 尺寸和 Phase 11 虚功残差。
3. 复核 Phase 12 中 `E`、`H`、`sigma_y` 的触边结果；人工确认前不恢复 Phase 14。

## 关联

[[Phase12-Recovery-VFM本构与虚功同步说明-2026-09-19]] · [[Phase14-PA12真实数据MLP代理模型-2026-09-19]] · [[PA12-Phase6-13.5真实实验成果总览-2026-09-19]]
