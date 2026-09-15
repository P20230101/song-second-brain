# PA12 单/双轴 DIC–VFM 投稿工作包

## 当前结论

这是一个已经收敛研究问题、方法、证据注册、期刊适配和图件计划的中英文投稿工作包。项目原始资料已部分进入工作区并完成 XY 文件级审计：`D:\C盘迁移\Desktop\yuan\data` 下有 XY/XZ 数据，当前 XY 结果覆盖 10 组图像序列和 5309 张 JPG；已生成逐帧照片—力对应表、事件表、频率/帧数审计和时间扰动敏感性图。当前仍不能直接上传投稿系统，因为材料/试样元数据、相机与校准记录、共同触发或逐帧时间戳、可验证的完整 DIC 场量和 VFM 识别/独立验证结果尚未齐全。不得用本地学习基线或文献数字代替这些缺失内容。

## 当前数据状态

已找到并解析：XY 图像、10 个力学 Excel 工作簿的 `Press`/`Pos` 表、MatchID 2D 工程/逐帧结果文件、XY 频率与事件审计表。

已计算：5309 条端点时间映射的照片—力记录；图像频率估计 7.98–375.66 Hz；力记录有效频率 997.50–1000.00 Hz；`XY_Xy-0.1-01` 的 ±1/±2/±5 帧假设时间扰动敏感性。

确实缺失或未验证：共同相机—DAQ 触发号/逐帧相机时间戳、相机和镜头完整参数、平面标定与 DIC 参数记录、试样数量与几何/材料批次、可直接用于 VFM 的带单位全场导出、边界牵引分布假设和独立验证集。所有当前 XY 序列的 `vfm_eligible` 均为 `False`。

## 入口文件

- 中文工作稿：[manuscript_cn.md](manuscript_cn.md)
- 英文工作稿（Strain 首选）：[manuscript_en.md](manuscript_en.md)
- 研究决策与标题：[00_研究决策与期刊标准.md](00_研究决策与期刊标准.md)
- 可复现实验与数据补齐：[01_可复现实验方案与数据补齐清单.md](01_可复现实验方案与数据补齐清单.md)
- patch 拆解与 12 小时顺序：[02_论文patch拆解与执行顺序.md](02_论文patch拆解与执行顺序.md)
- 投稿前自审：[03_投稿前自审与期刊适配清单.md](03_投稿前自审与期刊适配清单.md)
- 广撒网期刊矩阵：[期刊广撒网矩阵.md](期刊广撒网矩阵.md)
- 投稿信和题名模板：[投稿信与标题版本模板.md](投稿信与标题版本模板.md)
- 作者字段模板：[作者待补信息模板.md](作者待补信息模板.md)

## 证据与图件

- DOI/题名参考文献：[sources/references.json](sources/references.json)
- DOI 验证报告：[sources/reference_validation.json](sources/reference_validation.json)
- source manifest：[sources/source_manifest.json](sources/source_manifest.json)
- claim 机器注册表：[sources/claims.csv](sources/claims.csv)
- claim 可读版：[sources/claims_readable.md](sources/claims_readable.md)
- 证据审计摘要：[sources/evidence_audit_summary.md](sources/evidence_audit_summary.md)
- 图件计划与来源：[figures/README.md](figures/README.md)
- 当前已有方法图：[figures/Fig1_traceable_measurement_chain.png](figures/Fig1_traceable_measurement_chain.png)
- 当前 XY 力历史审计图：[results/analysis/Fig2_force_history_audit.png](../results/analysis/Fig2_force_history_audit.png)
- 当前频率与帧数一致性图：[results/analysis/Fig3_frequency_frame_audit.png](../results/analysis/Fig3_frequency_frame_audit.png)
- 当前事件帧投影图：[results/analysis/Fig4_event_frame_audit.png](../results/analysis/Fig4_event_frame_audit.png)
- 当前图像—载荷时间扰动图：[results/analysis/Fig5_timing_sensitivity_Xy-0.1-01.png](../results/analysis/Fig5_timing_sensitivity_Xy-0.1-01.png)
- 当前 XY 事实表：[results/analysis/xy_trial_facts.md](../results/analysis/xy_trial_facts.md)

## 选刊顺序

1. 测量链、DIC 参数和同步误差方法最匹配：Strain；当前稿需明确是数据审计/测量方法稿，不能把未运行的 VFM 写成结果。
2. 实验方法和实验—数值结合最强：Experimental Mechanics 或《实验力学》。
3. 本构模型和材料力学响应最强：Mechanics of Materials。
4. SLS 工艺/取向/厚度和材料工程最强：Polymer Testing、Materials & Design 或 Rapid Prototyping Journal。
5. 只有真实兵工/军民两用背景和单位保密审查成立时，才考虑《兵工学报》。

每次只能选择一个目标期刊；中英文稿是同一研究的替代语言版本，不能同时投稿。
