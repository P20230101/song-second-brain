# JOURNAL MATRIX｜目标期刊比较

更新时间：2026-09-17。指标、APC、首轮决定时间和相似论文必须在投稿前按官方页面/JCR/Scopus 当日核验；这里不提前填入会变化的数字，也不保证录用。

| 期刊 | 当前匹配度 | 适合的最终贡献 | 必须已有的证据 | 风险/条件 | 官方入口 |
|---|---|---|---|---|---|
| Experimental Mechanics | 高 | 实验力学、DIC、全场反演、误差/可辨识性和验证 | 真实 DIC、力/同步契约、独立验证、方法对实验问题有增益 | 若只有合成数据或没有全场闭环，匹配下降 | [期刊入口](https://link.springer.com/journal/11340) |
| Polymer Testing | 高 | PA12 材料实验、本构和路径验证 | 材料/工艺元数据、重复性、实验验证、模型物理解释 | 若 VFM 方法占主导且材料证据弱，需换定位 | [期刊入口](https://www.sciencedirect.com/journal/polymer-testing) |
| Mechanics of Materials | 高 | 材料力学 + 本构识别/跨路径预测 | 清晰材料机制、模型判别、独立预测和不确定性 | 不能只是常规模型换一个识别器 | [期刊入口](https://www.sciencedirect.com/journal/mechanics-of-materials) |
| International Journal of Mechanical Sciences | 条件高 | 多轴材料力学、各向异性/率效应或严谨识别方法 | 超出描述性实验的机制/方法增益，完整全场和预测 | M0–M2 常规模型若无强方法或物理新意，可能不够 | [期刊入口](https://www.sciencedirect.com/journal/international-journal-of-mechanical-sciences) |
| Computational Mechanics | 条件 | 可复现的 VFM/FEMU 数值方法与误差/优化贡献 | 真值回收、独立数值验证、算法与现有方法清楚比较 | PA12 仅作示例时需有真正计算方法贡献 | [期刊入口](https://link.springer.com/journal/466) |
| Computer Methods in Applied Mechanics and Engineering | 低/条件 | 新的计算反演、离散化、算法或理论方法 | 方法层面明显超出现有 VFM/SBVF，严格基准和泛化 | 仅把已有 VFM 用于 PA12 通常不够 | [期刊入口](https://www.sciencedirect.com/journal/computer-methods-in-applied-mechanics-and-engineering) |

## 选刊顺序

当前先按 `Experimental Mechanics / Polymer Testing / Mechanics of Materials` 准备三种定位；若最后形成真正的方法学增益，再考虑 `Computational Mechanics` 或 `IJMS`；没有算法原创性时不把 CMAME 作为主投。

## 投稿前核验字段

逐刊补齐：scope 原文、ISSN、文章类型、是否接受纯数值、实验验证要求、数据/代码政策、开放获取类型、官方 APC、JCR/Scopus 指标年份、首轮决定时间、近五年相似 VFM 论文 DOI 和匹配度。所有字段写入本表时附核验日期和来源。

## 官方证据附录（2026-09-17）

### 证据边界

- 本附录只核验期刊 scope、投稿类型/倾向和真实文章线索，不填没有明确来源的影响因子、CiteScore、APC、首轮决定时间或投稿难度。
- 项目当前仍是 `synthetic + 真实实验契约未闭合`：合成 Virtual Experiment 已用于数值闭环，但真实 PA12 的全场、同步、边界力、几何/厚度和模型契约尚未同时通过。以下判断不等于录用保证。
- 当前按 **2D DIC** 记录；双视角、空间标定和 3D 场量尚未成为当前实验事实。历史工作标题中的 `stereo-DIC` 不得直接写入本矩阵的当前研究定位。
- “最低科学证据”是根据官方 scope 与已核验文章作出的投稿准备判断，不是编辑部逐项发布的硬性清单。

| 期刊 | 官方 scope / 文章类型证据 | 近五年真实相似线索（2021–2026） | 纯数值与实验验证倾向 | 当前核验状态 |
|---|---|---|---|---|
| Experimental Mechanics | [Aims and scope](https://link.springer.com/journal/11340/aims-and-scope) 明确覆盖实验设计、改进实验、系统识别和逆问题；[投稿说明](https://link.springer.com/journal/11340/submission-guidelines)列出 Research、Brief Technical Note、Review（仅邀稿），并要求实验部分在实验—数值结合论文中构成主要贡献。 | [Vitucci 2024](https://link.springer.com/article/10.1007/s11340-024-01052-2)：十字形双轴、DIC 与本构表征；[Gonçalves et al. 2025](https://link.springer.com/article/10.1007/s11340-025-01168-z)：实验测得全场与异质试验。 | 不适合“只有合成/纯数值”的主定位；数值可用于支撑实验，但真实测量、误差和验证必须是主证据。 | scope-confirmed；paper-lead-confirmed；metric/policy待补 |
| Polymer Testing | [官方 scope](https://shop.elsevier.com/journals/polymer-testing/0142-9418)覆盖聚合物测试、分析和表征，并明确 modelling/simulation 需与新的或已有实验结果关联；官方文章页可见 Research article 等类型标签。 | [Ren et al. 2021](https://www.sciencedirect.com/science/article/pii/S0142941821002622)：3D 打印多孔结构的全场应力/应变与 DIC；[Cobian et al. 2022](https://doi.org/10.1016/j.polymertesting.2022.107556)：SLS PA12 不同尺度、方向和应变率的力学表征。 | 纯数值且不连接聚合物实验不匹配；材料、工艺/批次、加载条件和实验结果应先于模型。 | scope-confirmed；paper-lead-confirmed；metric/policy待补 |
| Mechanics of Materials | [官方 scope](https://shop.elsevier.com/journals/mechanics-of-materials/0167-6636)强调流动、断裂和一般本构行为，明确包含 polymers，并特别欢迎实验—计算—解析联合研究；已核验文章页使用 Research paper。 | [Dynamic hardening 2021](https://www.sciencedirect.com/science/article/pii/S0167663621003185)：DIC 全场、VFM/逆识别与率相关硬化；[316L 参数识别 2025](https://www.sciencedirect.com/science/article/pii/S0167663624003247)：DIC 与 FEMU 本构参数识别。 | scope 未明示排除纯数值，但必须有材料力学问题和实质机制/本构贡献；仅换识别器或仅做常规实验会削弱匹配。 | scope-confirmed；paper-lead-confirmed；纯数值政策待 author guide 核验 |
| International Journal of Mechanical Sciences | [官方 scope](https://shop.elsevier.com/journals/international-journal-of-mechanical-sciences/0020-7403)接受有工程应用的解析/计算建模，明确不欢迎纯描述性/纯经验内容；实验/测试用于验证主要贡献是强烈鼓励，既有公式的设计型研究不在 scope。 | [Johnson–Cook VFM 2021](https://www.sciencedirect.com/science/article/abs/pii/S0020740321002460)：异质热—力全场与 VFM 标定；[动态各向异性 VFM 2022](https://www.sciencedirect.com/science/article/abs/pii/S0020740322004441)；[FE-VFM/S-VFM 2025](https://www.sciencedirect.com/science/article/pii/S0020740325008975)。 | 可以有纯计算/解析成分，但须对应明确工程力学问题；实验验证不是绝对字面要求，却是本项目提高可信度的关键。 | scope-confirmed；paper-lead-confirmed；指标/APC待补 |
| Computational Mechanics | [Aims and scope](https://link.springer.com/journal/466/aims-and-scope)聚焦计算工程、力学—数学—数值方法和计算挑战；明确不鼓励仅使用既有方法或商业软件的计算结果；官方投稿页运行 type 1 research data policy。 | [Hartmann & Gilbert 2021](https://link.springer.com/article/10.1007/s00466-021-01998-3)：有限元参数识别结合实验全场应变；[mCRE model/mesh selection 2025](https://link.springer.com/article/10.1007/s00466-025-02598-1)：DIC 全场、模型选择和噪声协方差。 | 纯数值方法研究可匹配，但需要新方法/难计算/严格验证；仅用商业软件或把既有 VFM 应用于 PA12 不足。 | scope-confirmed；paper-lead-confirmed；metric/APC待补 |
| Computer Methods in Applied Mechanics and Engineering（CMAME） | [官方 scope](https://shop.elsevier.com/journals/computer-methods-in-applied-mechanics-and-engineering/0045-7825)要求前沿计算方法的实质发展，覆盖固体/材料/优化/不确定性等，并明确不发表 review/survey。官方文章页使用 Research article。 | [DIC-mCRE 2022](https://www.sciencedirect.com/science/article/abs/pii/S0045782522004947)：全场 DIC、线性/非线性参数识别和合成/真实场验证；[ML-based VFM 2025](https://www.sciencedirect.com/science/article/pii/S004578252400834X)：新 VFM 损失函数、各向异性模型发现与数值/实验数据。 | 纯数值方法论文原则上符合其 scope；实验不是必需的字面条件，但需要算法/理论新意、数值基准、鲁棒性和可复现性。当前 PA12 应用稿不宜直接按 CMAME 定位。 | scope-confirmed；paper-lead-confirmed；metric/APC待补 |

### 与本项目直接对应的证据门槛

| 定位 | 进入投稿准备的最低证据 | 主要否决信号 |
|---|---|---|
| Experimental Mechanics | 真实 2D DIC 标定与质量、时间同步、四通道边界映射、误差/不确定度、VFM 识别和独立路径验证 | 只有 synthetic，或实验只是展示设备而不支撑核心结论 |
| Polymer Testing | 同一 PA12 工艺/批次的材料与试验元数据、实验重复性、全场/力学结果、本构解释和留出路径验证 | 模型与实验脱节，或材料证据弱而算法占主导 |
| Mechanics of Materials | 可解释的材料本构/机制问题、全场识别增益、模型判别和独立预测 | 仅把已有模型换成另一优化器，缺少材料力学新意 |
| IJMS | 明确的多轴材料力学或工程问题、分析/计算新意、对主要结论的实验支撑 | 仅做常规十字形设计或纯描述性实验 |
| Computational Mechanics | VFM/FEMU 的算法或离散化贡献、synthetic 真值回收、数值稳健性/收敛、与基线比较和真实数据验证 | 主要结果来自商业软件或既有方法的直接应用 |
| CMAME | 新的计算反演/求解方法、严格数值基准、复杂度/鲁棒性/泛化证据；实验验证可作为增强证据 | 论文贡献只剩 PA12 数据集或常规 VFM 应用 |

### 当前未核实项

以下字段继续保留 `待官方核验`：JCR/Scopus 指标及年份、CiteScore、APC、首轮决定时间、完整数据/代码政策、每刊具体文章类型下拉项和投稿难度。近五年线索只表示“已找到真实官方文章页面”，不表示这些文章已全部完成全文+图像审计，也不构成录用率或录用保证。
