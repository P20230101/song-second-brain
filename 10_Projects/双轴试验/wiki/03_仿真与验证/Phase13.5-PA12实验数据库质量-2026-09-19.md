---
title: Phase 13.5｜PA12 实验数据库质量审计
status: historical_pre_reaudit
---

# Phase 13.5｜PA12 实验数据库质量审计

## 状态说明

本页记录的是修复前的候选实验闭合扫描，原文中的“8 个有效实验”不再是当前数据库准入口径。2026-09-19 完成 Phase 12.1–12.3 重审和三级修复后，当前权威状态为：5 组 `quality_passed`、0 组 `constitutive_validated`；以 [一级二级三级修复与 Phase 13/14 质量门](../01_研究总控/PA12-一级二级三级修复与Phase13-14质量门-2026-09-19.md) 和 `database_quality_report.json` 为准。

## 历史扫描结果

修复前曾按真实数据逐个搜索、绑定和闭合候选实验；该扫描没有生成或写入 synthetic 实验，但其“8 个有效实验”统计已被后续质量门重审收窄。

有效 `experiment_id`：

- `XY_Xy-0.1-01`
- `XY_Xy-03-10-01`
- `XY_Xy-04-1-01`
- `XY_X-06-1.0-01`
- `XY_X-07-10-01`
- `XY_Y-09-0.1-02`
- `XY_Y-10-1-01`
- `XY_Y-11-10-01`

每个有效实验均具备：正式 MatchID DIC 字段、真实 Force.csv、相机—力值同步、`vfm_eligible=true`、Phase 11 结果和 Phase 12 五参数识别结果。

## 输出

- [真实实验成果总览](../05_结果与论文/PA12-Phase6-13.5真实实验成果总览-2026-09-19.md)
- [可汇报 PPT](../../实验/PA12-双轴-DIC-VFM/reports/PA12_Phase6_13_5_真实实验汇报_v5.pptx)
- [database_quality_report.json](../../实验/PA12-双轴-DIC-VFM/database_quality_report.json)
- [PA12_database.h5](../../实验/PA12-双轴-DIC-VFM/PA12_database.h5)
- [quality audit script](../../实验/PA12-双轴-DIC-VFM/real_data_pipeline/phase13_5_quality.py)
- [database build log](../../实验/PA12-双轴-DIC-VFM/PA12_database.recovery_usable_frames.log)

质量报告字段：

| 字段 | 结果 |
|---|---:|
| `valid_experiment_count` | 5（当前质量门口径） |
| `target_valid_experiment_count` | 5 |
| `target_reached` | true |
| `synthetic_used` | false |
| `ai_used` | false |

## 排除候选

| `experiment_id` | 失败原因 |
|---|---|
| `XY_X-05-0.1-01` | 实际可用 DIC 为 151 帧，但无 formal MatchID 应变导出、Force.csv 和力值闭合 |
| `XY_XY-0.1-02` | 缺 formal VFM 输入和准入检查 |

已排除的 2 个候选保存在 HDF5 的 `audit/excluded_experiments` 和质量报告 `missing_experiments` 中。DIC 审计按实际可用 `frame_id` 集合执行：X-05 保留 151 个可用帧；Xy-04 的 14 对多余文件、X-07 的 1 对多余文件已移动到原始试验目录下的 `excluded_frames`，未永久删除。没有用其他实验数据补齐。

## 完成条件

当前 `PA12_database.h5` 的 `experiments` 组包含 5 组质量门通过的真实实验，问题实验写入 `audit/excluded_experiments`；根属性 `synthetic_used=false`、`ai_used=false`。本页历史扫描的 8 个 ID 不得直接解释为当前数据库准入或本构验证通过。
