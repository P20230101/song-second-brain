---
title: PA12｜Phase 12.1 真实数据审查与本构模型阶梯
date: 2026-09-19
status: completed_for_manual_review
source_is_real: true
synthetic_used: false
---

# PA12｜Phase 12.1 真实数据审查与本构模型阶梯

## 结论

Phase 12.1 已完成 8 个真实实验的 DIC/Force/帧元数据、几何、边界和曲线审查；Phase 12.2 已用同一真实单调加载支比较线弹性、J2 完美塑性、J2 幂律硬化和平台/软化诊断候选。当前没有实验达到严格的 `constitutive_validated` 层，Phase 14 正式恢复门保持关闭。

## Phase 12.1 审查结果

审查器读取正式 `formal_vfm_input.csv.gz`、Phase 8–12 JSON 和质量报告，不修改 raw 或正式输入。结果文件：[phase12_1_data_constitutive_audit.json](../../实验/PA12-双轴-DIC-VFM/reports/phase12_1_audit/phase12_1_data_constitutive_audit.json)。

| 实验 | formal帧 | 单调加载帧 | Phase 8相对残差 | Phase 12力相对RMSE | 主要结论 |
|---|---:|---:|---:|---:|---|
| `XY_X-06-1.0-01` | 133 | 59 | 0.047 | 0.029 | 力拟合较好，但 `nu` 触下界 |
| `XY_X-07-10-01` | 80 | 29 | 0.072 | 0.034 | 力拟合较好，但 `nu` 触下界 |
| `XY_Xy-0.1-01` | 289 | 226 | 0.496 | 0.095 | 双轴边界/虚功残差较大，`nu` 触下界 |
| `XY_Xy-03-10-01` | 21 | 8 | 0.076 | 0.185 | 加载帧过少，`E` 触 5000 MPa 上界 |
| `XY_Xy-04-1-01` | 253 | 144 | 0.342 | 0.072 | 虚功残差较大，`nu/H/n` 触边界 |
| `XY_Y-09-0.1-02` | 1825 | 1118 | 0.401 | 0.395 | Phase 12 联合损失下轴向曲线高残差 |
| `XY_Y-10-1-01` | 1558 | 890 | 0.419 | 0.416 | Phase 12 联合损失下轴向曲线高残差 |
| `XY_Y-11-10-01` | 711 | 1 | — | — | 非单调，排除 |

诊断图：

- [加载支力—位移审查](../../实验/PA12-双轴-DIC-VFM/reports/phase12_1_audit/phase12_1_force_displacement_audit.png)
- [残差审查](../../实验/PA12-双轴-DIC-VFM/reports/phase12_1_audit/phase12_1_residual_audit.png)
- [帧覆盖与加载支](../../实验/PA12-双轴-DIC-VFM/reports/phase12_1_audit/phase12_1_frame_geometry_audit.png)

图像审核结果为 3/3 通过，未发现空白、低分辨率或单色图。X-07 前几帧的零值是基线，首次正载荷之后保持正值，没有通过符号翻转掩盖原始力值。

## Phase 12.2 模型阶梯

模型比较统一使用真实加载支，首个基线点排除；残差定义为 Phase 12 单轴项的归一化轴向力残差 + `0.1 ×` 归一化横向 DIC 应变残差。结果：[phase12_2_model_ladder.json](../../实验/PA12-双轴-DIC-VFM/reports/phase12_2_model_ladder/phase12_2_model_ladder.json)。

### 关键判断

对 Y-09/Y-10，单独拟合真实轴向力时，J2 幂律硬化的相对 RMSE 约为 `0.012/0.014`；但加入横向 DIC 应变项后，联合拟合的轴向力相对 RMSE 回到 `0.395/0.416`。这说明当前主要矛盾不是简单的“J2 轴向硬化无法拟合”，而是横向 DIC 应变约束、平面应力口径、边界/几何或载荷方向与轴向力曲线不一致。

平台/软化曲线只作为诊断候选。它在部分实验降低轴向力残差，但部分参数触边，不能直接登记为 PA12 材料模型。每个实验只有一条加载速率路径，速率项与屈服/硬化参数混淆，当前标记为 `not_identifiable_per_single_experiment`，没有强行拟合速率系数。

诊断图：

- [模型阶梯曲线](../../实验/PA12-双轴-DIC-VFM/reports/phase12_2_model_ladder/phase12_2_model_ladder_force_curves.png)
- [模型残差比较](../../实验/PA12-双轴-DIC-VFM/reports/phase12_2_model_ladder/phase12_2_model_ladder_residuals.png)
- 图像审核在模型阶梯 JSON 中记录，`image_issues=[]`。

## Phase 12.3 数据库分层

分层文件：[phase12_3_database_stratification.json](../../实验/PA12-双轴-DIC-VFM/reports/phase12_3_database_stratification.json)。

- `quality_passed`：5 组——真实 DIC、Force、同步和正式 VFM 输入完整。
- `constitutive_validated`：0 组——没有实验同时满足无参数触边、加载帧充分、VFM 残差、联合力拟合和可辨识性条件。
- `diagnostic_only`：8 组——包括 5 组质量通过但本构证据不足的实验，以及 Y-09/Y-10/Y-11 等诊断/排除实验。

数据库 [PA12_database.h5](../../实验/PA12-双轴-DIC-VFM/PA12_database.h5) 已写入分层属性：`quality_status`、`constitutive_status`、`database_tier` 和 `stratification_reasons`。根属性确认 `constitutive_validated_experiment_count=0`、`phase14_recovery_gate_open=False`。

## 下一步

1. 优先人工复核横向 DIC 的符号、应变定义、ROI 边界、厚度和轴向几何；不先放宽 RMSE 门限。
2. 对 Y-09/Y-10 做同一实验的横向应变—时间、横向力—时间和局部化检查，判断是否存在平面应力假设失效、夹具传力或速率效应。
3. 只有在横向约束和边界条件被解释后，才决定是否引入速率/软化本构；软化诊断曲线暂不进入材料数据库常数层。
4. 获得更多不同速率和双轴比例的真实独立实验后，再打开 Phase 14 正式训练门。
