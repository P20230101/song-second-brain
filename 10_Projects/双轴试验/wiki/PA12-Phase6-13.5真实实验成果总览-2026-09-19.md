---
title: PA12｜Phase 6–13.5 真实实验成果总览
date: 2026-09-19
status: active
data_status: real_experimental
synthetic_used: false
ai_used: false
valid_experiments: 8
tags:
  - PA12
  - DIC
  - VFM
  - real-data
  - material-identification
  - database
aliases:
  - PA12真实实验成果总览
---

# PA12｜Phase 6–13.5 真实实验成果总览

## 汇报结论

当前真实实验闭环已形成：质量审计从本地 PA12 数据中确认 **8 个可用实验**，并将这 8 个 `experiment_id` 写入 `PA12_database.h5`。质量报告与 HDF5 纳入清单一致，`synthetic_used=false`、`ai_used=false`。

当前纳入：5 个单轴记录、3 个双轴记录，共 **4870 帧**。每个纳入记录均有真实图像、MatchID/DIC 字段、真实 `Force.csv`、时间同步、`formal_vfm_input.csv.gz`、Phase 8–12 输出和日志。

Phase 9 与 Phase 12 的优化器均可能报告 `success=true`，但 Phase 12 明确记录 `uniqueness_proven=false`。因此，本页把识别参数作为真实数据上的当前拟合结果保存，不把它们表述为已经完成唯一性证明的最终材料常数。

## 数据边界

| 数据类别 | 本次处理方式 |
|---|---|
| 真实实验 | 原始相机图像、MatchID 导出、真实 `Force.csv`、时间同步、VFM、参数拟合、HDF5 数据库 |
| synthetic / 仿真 | 不写入质量报告有效清单，不写入 HDF5 `experiments` 组；现有旧 `fixture_optimization` 进程按用户要求继续运行，但其输出不作为实验依据 |
| AI | 本批次未用于数据生成或参数识别，报告字段为 `ai_used=false` |

## 技术路线与交付链

```mermaid
flowchart LR
  A[Phase 6 真实 MatchID/DIC] --> B[Phase 7 Force.csv 同步]
  B --> C[Phase 8 单轴 VFM]
  C --> D[Phase 9 J2 参数拟合]
  C --> E[Phase 11 二维双轴 VFM]
  D --> F[Phase 12 单轴+双轴联合识别]
  E --> F
  F --> G[Phase 13 HDF5 数据库]
  G --> H[Phase 13.5 质量审计]
  H --> I[汇报、复核、追加实验]
```

## 8 个有效实验

| experiment_id | 类型 | 帧数 | Phase 8 E / MPa | Phase 9 force relative L2 | Phase 12 joint loss | 唯一性证明 |
|---|---:|---:|---:|---:|---:|---|
| `XY_Xy-0.1-01` | 双轴 | 289 | 178.535 | 0.8576 | 48.0848 | 未证明 |
| `XY_Xy-03-10-01` | 双轴 | 21 | 112.633 | 0.9905 | 2.8383 | 未证明 |
| `XY_Xy-04-1-01` | 双轴 | 253 | 96.837 | — | — | 未证明 |
| `XY_X-06-1.0-01` | 单轴 | 133 | — | — | — | 未证明 |
| `XY_X-07-10-01` | 单轴 | 80 | — | — | — | 未证明 |
| `XY_Y-09-0.1-02` | 单轴 | 1825 | 290.353 | 0.4401 | 13.0603 | 未证明 |
| `XY_Y-10-1-01` | 单轴 | 1558 | 315.560 | 0.4542 | 23.3151 | 未证明 |
| `XY_Y-11-10-01` | 单轴 | 711 | -202.285 | 0.5861 | 186.4612 | 未证明 |

> 这里的 `Phase 12 joint loss` 是各结果文件中的归一化损失汇总，不同试验的加载量级和有效帧数不同，不能直接作为跨试验优劣排名。

## Phase 9 J2 拟合参数

单位：`E`、`sigma_y`、`H` 为 MPa；`nu`、`n` 无量纲。

| experiment_id | E | nu | sigma_y | H | n | force RMSE / N | 最大绝对误差 / N | nfev |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `XY_Xy-0.1-01` | 976.582 | 0.0000 | 42.858 | 208.951 | 0.884 | 558.625 | 894.556 | 36 |
| `XY_Xy-03-10-01` | 5000.000 | 0.0000 | 43.990 | 580.080 | 0.479 | 296.409 | 418.747 | 11 |
| `XY_Y-09-0.1-02` | 219.728 | 0.0000 | 60.059 | 83.764 | 0.482 | 575.939 | 1077.943 | 21 |
| `XY_Y-10-1-01` | 263.616 | 0.0000 | 59.805 | 93.837 | 0.483 | 594.331 | 1081.201 | 19 |
| `XY_Y-11-10-01` | 1.000 | 0.3500 | 10.000 | 100.000 | 0.500 | 0.000 | 0.000 | 1 |

### Phase 9 结果解释

- 多个结果出现 `nu≈0` 或 `E` 到达边界，说明当前观测量、边界定义或参数化仍存在识别退化。
- `XY_Y-11-10-01` 的零拟合误差来自优化器在初值处立即终止，不能单独作为材料模型已验证的证据。
- 这些数值保留在原始 JSON 和 HDF5 中，后续 Phase 10 复核应检查单位、加载轴、边界牵引定义和参数边界。

## Phase 12 联合识别参数

| experiment_id | E | nu | sigma_y | H | n | single loss | biaxial loss |
|---|---:|---:|---:|---:|---:|---:|---:|
| `XY_Xy-0.1-01` | 792.360 | 0.0000 | 132.429 | 715.922 | 0.802 | 47.5888 | 0.4961 |
| `XY_Xy-03-10-01` | 5000.000 | 0.0000 | 206.749 | 3942.226 | 0.344 | 2.6861 | 0.1522 |
| `XY_X-06-1.0-01` | 1.000 | 0.0000 | 34.211 | 217.167 | 0.493 | — | — |
| `XY_X-07-10-01` | 1.000 | 0.0000 | 47.178 | 508.483 | 0.481 | — | — |
| `XY_Xy-04-1-01` | 2298.097 | 0.0000 | 127.977 | 641.329 | 0.844 | — | — |
| `XY_Y-09-0.1-02` | 1.150 | 0.0000 | 0.010 | 0.001 | 2.000 | 11.0789 | 1.9815 |
| `XY_Y-10-1-01` | 1.670 | 0.0000 | 0.053 | 0.009 | 0.157 | 21.8868 | 1.4283 |
| `XY_Y-11-10-01` | 1.000 | 0.0000 | 10.000 | 100.000 | 0.500 | 175.4877 | 10.9734 |

## 原始照片与证据

以下图片复制到本页附件目录，保留原始实验照片的代表性起始、中间和末帧。完整图像序列仍保留在原始数据目录，不用附件副本替代原始数据。

### `XY_Xy-0.1-01`

![[assets/pa12-real/2026-09-19/XY_Xy-0.1-01_frame000.jpg]]

`frame144`、`frame288`：[中间帧](assets/pa12-real/2026-09-19/XY_Xy-0.1-01_frame144.jpg)、[末帧](assets/pa12-real/2026-09-19/XY_Xy-0.1-01_frame288.jpg)。

### `XY_Xy-03-10-01`

![[assets/pa12-real/2026-09-19/XY_Xy-03-10-01_frame000.jpg]]

`frame010`、`frame020`：[中间帧](assets/pa12-real/2026-09-19/XY_Xy-03-10-01_frame010.jpg)、[末帧](assets/pa12-real/2026-09-19/XY_Xy-03-10-01_frame020.jpg)。

### `XY_X-06-1.0-01`

![[assets/pa12-real/2026-09-19/XY_X-06-1.0-01_frame000.jpg]]

`frame066`、`frame132`：[中间帧](assets/pa12-real/2026-09-19/XY_X-06-1.0-01_frame066.jpg)、[末帧](assets/pa12-real/2026-09-19/XY_X-06-1.0-01_frame132.jpg)。

### `XY_X-07-10-01`

![[assets/pa12-real/2026-09-19/XY_X-07-10-01_frame000.jpg]]

`frame040`、`frame079`：[中间帧](assets/pa12-real/2026-09-19/XY_X-07-10-01_frame040.jpg)、[末帧](assets/pa12-real/2026-09-19/XY_X-07-10-01_frame079.jpg)。

### `XY_Xy-04-1-01`

![[assets/pa12-real/2026-09-19/XY_Xy-04-1-01_frame000.jpg]]

`frame126`、`frame253`：[中间帧](assets/pa12-real/2026-09-19/XY_Xy-04-1-01_frame126.jpg)、[末帧](assets/pa12-real/2026-09-19/XY_Xy-04-1-01_frame253.jpg)。

### `XY_Y-09-0.1-02`

![[assets/pa12-real/2026-09-19/XY_Y-09-0.1-02_frame000.jpg]]

`frame912`、`frame1824`：[中间帧](assets/pa12-real/2026-09-19/XY_Y-09-0.1-02_frame912.jpg)、[末帧](assets/pa12-real/2026-09-19/XY_Y-09-0.1-02_frame1824.jpg)。

### `XY_Y-10-1-01`

![[assets/pa12-real/2026-09-19/XY_Y-10-1-01_frame000.jpg]]

`frame778`、`frame1557`：[中间帧](assets/pa12-real/2026-09-19/XY_Y-10-1-01_frame778.jpg)、[末帧](assets/pa12-real/2026-09-19/XY_Y-10-1-01_frame1557.jpg)。

### `XY_Y-11-10-01`

![[assets/pa12-real/2026-09-19/XY_Y-11-10-01_frame000.jpg]]

`frame355`、`frame710`：[中间帧](assets/pa12-real/2026-09-19/XY_Y-11-10-01_frame355.jpg)、[末帧](assets/pa12-real/2026-09-19/XY_Y-11-10-01_frame710.jpg)。

已有真实力值对比图：[XY_Xy-0.1-01 force_compare](assets/pa12-real/2026-09-19/XY_Xy-0.1-01_force_compare.png)。

## 结果文件索引

## Phase 12 Recovery：本构与虚功同步讲解材料

详细方法、真实单轴/双轴数据清单、VFM 内外虚功公式、照片与同编号虚功曲线一一对应证据，以及 Mermaid 流程图见：[[Phase12-Recovery-VFM本构与虚功同步说明-2026-09-19]]。

- [真实单轴应力–应变加载支](../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/single_axis_real_stress_strain.png)
- [真实本构与 VFM 本构对比](../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/single_axis_vfm_constitutive_compare.png)
- [真实力–位移与 Phase 9/12 预测](../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/single_axis_force_displacement_vfm_compare.png)
- [内外虚功同步与照片对应证据](../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/vfm_virtual_work_sync_evidence.png)

### 数据库与质量审计

- [PA12_database.h5](../实验/PA12-双轴-DIC-VFM/PA12_database.h5)
- [database_quality_report.json](../实验/PA12-双轴-DIC-VFM/database_quality_report.json)
- [可汇报 PPT](../实验/PA12-双轴-DIC-VFM/reports/PA12_Phase6_13_5_真实实验汇报_v5.pptx)
- [Phase 13 数据库说明](Phase13-PA12材料数据库-2026-09-18.md)
- [Phase 13.5 质量审计](Phase13.5-PA12实验数据库质量-2026-09-19.md)

### 每个有效实验的共同输出

每个 run 目录均保留以下证据链：

- `vfm_ready_check.json`：时间同步、力值缺失率、边界完整性和 `vfm_eligible`。
- `formal_vfm_input.csv.gz`：供 VFM 使用的真实 DIC + Force 正式输入。
- `vfm_single_result.json`：Phase 8 单轴虚功结果。
- `PA12_identified_material.json`：Phase 9 J2 参数识别、误差和收敛曲线。
- `biaxial_vfm_result.json`：Phase 11 二维虚功结果。
- `PA12_multiaxial_material.json`：Phase 12 联合识别和唯一性状态。
- `phase*.log`：每一步的计算日志。

运行目录：[real_data_pipeline/runs](../实验/PA12-双轴-DIC-VFM/real_data_pipeline/runs)。

## 排除候选与后续可恢复工作

| experiment_id | 当前状态 | 失败原因 | 后续动作 |
|---|---|---|---|
| `XY_X-05-0.1-01` | 未纳入 | 实际可用 DIC 为 151 帧，但无 formal MatchID 应变导出、Force.csv 和力值闭合 | 补齐真实导出和力值接口后再闭合 |
| `XY_XY-0.1-02` | 未纳入 | 缺 formal VFM 输入与准入检查 | 补齐真实 formal 导出后再闭合 |

对 `XY_X-05-0.1-01`、`XY_Xy-04-1-01`、`XY_X-07-10-01` 的非可用照片/数据对已移入原始试验目录下的 `excluded_frames`，保留可恢复副本；审计按实际可用 DIC `frame_id` 集合，不按相机总拍摄数强制补齐。

## 后续规划

### P0｜当前交付已完成

完成 8 个真实实验的收集、质量门控、HDF5 更新、代表性照片归档和汇报材料。

### P1｜Phase 10 识别结果复核

对 8 个实验逐一核对力值符号、单位、加载轴、厚度、面积和边界牵引定义。重点复核 `nu≈0`、参数触边和 `XY_Y-11-10-01` 的零误差早停。

### P2｜独立实验验证

将一个实验用于拟合、另一个独立实验用于预测，输出 `force_compare.png`、RMSE、MAE、最大误差和 `validation.md`。只有跨实验预测通过，才提升材料参数的可信度。

### P3｜数据库扩充

优先补齐当前 2 个失败候选的真实导出问题，再追加不同加载比例和重复试样。每个新增实验必须重新通过 Phase 6–13.5，不使用 synthetic 补数。

### P4｜Phase 12 Recovery 后暂停 Phase 14

Phase 14 已暂停。Phase 12 Recovery 已完成真实参数识别闭环，数据库当前纳入 8 个真实实验、排除 2 个不完整实验；等待人工复核参数触边、力值符号和虚功残差后，再决定是否恢复 AI 阶段。

## 关联笔记

[[Phase6-真实MatchID数据接入-2026-09-18]] · [[Phase7-实验力值闭合-2026-09-18]] · [[Phase8-真实单轴VFM求解-2026-09-18]] · [[Phase9-PA12弹塑性参数识别-2026-09-18]] · [[Phase10-实验仿真验证-2026-09-18]] · [[Phase11-二维双轴VFM-2026-09-18]] · [[Phase12-单轴双轴联合识别-2026-09-18]] · [[Phase12-Recovery-真实实验材料参数闭环-2026-09-19]] · [[Phase13-PA12材料数据库-2026-09-18]] · [[Phase13.5-PA12实验数据库质量-2026-09-19]] · [[Phase14-PA12真实数据MLP代理模型-2026-09-19]]

## 可检索视图

```dataview
TABLE status, data_status, valid_experiments, synthetic_used, ai_used
FROM "双轴/wiki"
WHERE contains(file.name, "PA12") OR contains(file.name, "Phase")
SORT file.mtime DESC
```
