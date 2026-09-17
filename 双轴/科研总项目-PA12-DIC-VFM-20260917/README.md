# PA12 单轴/双轴全场力学与 VFM 总项目

更新时间：2026-09-17
项目状态：研究路线审查中，尚未进入真实 PA12 参数识别或投稿定稿阶段。

本目录是项目的总控文档区，服务于一个可投稿、可答辩、可复现的研究闭环：

> 研究缺口 → 可证伪假设 → 数据审计 → 本构模型筛选 → Virtual Experiment → 无噪声 VFM 回收 → 可辨识性与加载路径设计 → 真实数据验证 → 论文。

## 先读

- [QUICK_INDEX.md](QUICK_INDEX.md)：按研究总控、证据/数据、计算方法和现有结果快速定位。
- [MASTER_PLAN.md](MASTER_PLAN.md)：范围、阶段、Gate 与停止规则。
- [LITERATURE_MAP.md](LITERATURE_MAP.md)：公开证据和文献矩阵。
- [DATA_AUDIT.md](DATA_AUDIT.md)：原始数据、派生数据、缺失项和可重算项。
- [RESEARCH_GAP.md](RESEARCH_GAP.md)：收窄后的主问题、子问题与假设。
- [CONSTITUTIVE_MODELS.md](CONSTITUTIVE_MODELS.md)：M0–M7 模型阶梯和准入条件。
- [VFM_PLAN.md](VFM_PLAN.md)：虚拟实验、VFM 数据契约和验证顺序。
- [IDENTIFIABILITY_PLAN.md](IDENTIFIABILITY_PLAN.md)：FIM、敏感度、噪声和路径信息分析。
- [EXPERIMENT_PLAN.md](EXPERIMENT_PLAN.md)：已有试验矩阵与不新增实验路线。
- [PAPER_PLAN.md](PAPER_PLAN.md)：第一篇论文的结果驱动结构和图表计划。
- [JOURNAL_MATRIX.md](JOURNAL_MATRIX.md)：目标期刊筛选表。
- [PROGRESS.md](PROGRESS.md)：当前进度、Gate 状态和下一步。

## 数据边界

原始照片、MatchID 工程、机器数据和 PDF 不复制进本目录，也不作为公开仓库资产。当前实际原始数据位置为 `D:\C盘迁移\Desktop\yuan\data`，只读使用。项目内的仿真资产保留在 `双轴/实验/PA12-双轴-DIC-VFM/simulation/`；派生审计表和合成 VFM 结果位于对应 `results/` 与 `vfm/` 目录。

“原始存在”不等于“VFM 可用”。当前已确认用户给出的中心厚度为 1.0 mm，S16 图像 manifest 覆盖 259 帧；原始 MatchID `.dat` 也覆盖 0–258 且全部可解析，`DIC-xy_0.2` 则是 0–132 的独立简洁导出（其中 0–131 质量稳定、132 无效）。事件表没有有效共同触发事件，字段单位、有效掩膜和边界力绑定仍需验证。因此可以立即开展全量 `.dat` 的字段审计与稳定帧候选 VFM，不能宣称已完成全程真实 VFM 识别。

## 证据标记

- `confirmed`：由本地文件或官方文献页面直接核实。
- `derived`：项目脚本或派生表生成，必须保留来源路径。
- `pending`：存在文件或线索，但关键字段/假设未核实。
- `blocked`：缺少必要数据，不能进入下一 Gate。
- `synthetic`：虚拟/合成数据，只用于方法验证和设计分析，不冒充实验结果。
