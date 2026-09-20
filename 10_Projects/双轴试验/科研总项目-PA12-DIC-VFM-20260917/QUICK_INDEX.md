# QUICK INDEX｜PA12-DIC-VFM 快速定位

## 研究总控

- [总计划](MASTER_PLAN.md)
- [当前进度与 Gate](PROGRESS.md)
- [研究缺口](RESEARCH_GAP.md)
- [论文计划](PAPER_PLAN.md)
- [期刊矩阵](JOURNAL_MATRIX.md)

## 证据与数据

- [文献地图](LITERATURE_MAP.md)
- [文献数据库审计注册表](LITERATURE_DATABASE.md)
- [DOI 元数据存在性审计](DOI_VALIDATION_AUDIT.md)
- [MinerU 正文与图像证据](MINERU_BODY_IMAGE_EVIDENCE.md)
- [受控文献全文与 MinerU 目录](literature_fulltext/README.md)
- [公开全文正文与图像证据](LITERATURE_BODY_IMAGE_EVIDENCE.md)
- [数据审计](DATA_AUDIT.md)
- [`.dat`–legacy CSV 首帧交叉检查](results/xy_dat_legacy_crosscheck.md)
- [MatchID `.dat` Schema 审计](results/matchid_dat_schema_audit.md)
- [全试样 MatchID 审计](ALL_TRIALS_AUDIT.md)
- [试验矩阵](EXPERIMENT_PLAN.md)
- 真实样本证据：[双轴/wiki/02_实验与VFM/01_方法与输入/真实PA12中心试样-证据与建模契约-2026-09-17.md](../wiki/02_实验与VFM/01_方法与输入/真实PA12中心试样-证据与建模契约-2026-09-17.md)
- 原始数据：`D:\C盘迁移\Desktop\yuan\data`（只读，不复制进仓库）
- legacy DIC 候选导出：`D:\C盘迁移\Desktop\yuan\DIC-xy_0.2`（133 帧；作为独立交叉检查）
- MatchID 全量逐点入口：`D:\C盘迁移\Desktop\yuan\data\XY\袁-20250529\XY-0.1-02\Test1\33061_1_16`（259 个 `.jpg.dat`，全部可解析）

## 计算与方法

- [本构模型阶梯](CONSTITUTIVE_MODELS.md)
- [VFM 计划](VFM_PLAN.md)
- [可辨识性计划](IDENTIFIABILITY_PLAN.md)
- VFM 原型：`双轴/实验/PA12-双轴-DIC-VFM/vfm/`
- DIC 字段审计器：`科研总项目-PA12-DIC-VFM-20260917/scripts/audit_dic_field_csv.py`（只读审计，不推断应变/力/同步）
- MatchID `.dat` 帧审计器：`tools/audit_matchid_dat.py`（只读解压并生成 259 行摘要，不修改原始 `.dat`）
- 全集 MatchID 审计器：`tools/audit_matchid_collection.py`（只读扫描 XY/XZ 全部 `.dat`，输出试验汇总和照片—力—DAT 候选关联）
- 仿真资产：`双轴/实验/PA12-双轴-DIC-VFM/simulation/`（保存在 D 盘；Stage-A 基准 Gate 3/4 已通过，真实 PA12 Gate 仍未通过）
- [Abaqus–VFM Stage-A 审计报告](results/abaqus_vfm_gate_audit.md)
- [M0–M2 synthetic 基线 handoff](results/m0_m2_virtual_experiment_handoff.md)
- [Abaqus ODB 实际打开验证](results/abaqus_odb_open_validation.md)
- ODB 场量审计：`scripts/audit_abaqus_vfm_odb.py`
- 离散 FE–VFM 重算：`scripts/recompute_vfm_from_abaqus_odb.py`

## 现有派生结果

- 照片—力候选表：`双轴/实验/PA12-双轴-DIC-VFM/results/01_VFM照片力对应.csv`
- DIC 结构审计结果：`科研总项目-PA12-DIC-VFM-20260917/results/dic_field_audit_xy_0.2.json`
- MatchID `.dat` 摘要和照片—力候选表：保存在 `D:\C盘迁移\Desktop\yuan\analysis\real_specimen_XY-0.1-02`（不复制原始场量到仓库）
- XY 同步审计：`双轴/实验/PA12-双轴-DIC-VFM/results/审计/xy_photo_force_sync.csv`
- 同步事件表：`双轴/实验/PA12-双轴-DIC-VFM/同步/events.csv`（当前只有表头）
- VFM L0 状态页：`双轴/实验/PA12-双轴-DIC-VFM/09_VFM-L0基准与仿真状态.md`
- Stage-A JSON 结果：`results/abaqus_vfm_recompute_UX.json`、`results/abaqus_vfm_recompute_EQ.json`、`results/abaqus_vfm_recompute_R05.json`
- 论文草稿：`双轴/draft_paper/`
- 日报/研究报告：`双轴/研究报告/`

## 使用规则

先读 `MASTER_PLAN` 和 `PROGRESS`；再读 `DATA_AUDIT`；只有 Gate 3/4 重开后才运行真实 VFM。`raw/`、原始照片、机器文件、MatchID 工程、PDF、ODB 和未提交用户文件不在本导航范围内，也不做移动或公开。
