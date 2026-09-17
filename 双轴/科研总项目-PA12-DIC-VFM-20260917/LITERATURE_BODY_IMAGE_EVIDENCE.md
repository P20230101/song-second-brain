# LITERATURE BODY–IMAGE EVIDENCE｜PA12 公开全文核验

更新时间：2026-09-17

## 目的与边界

本页只登记已经打开正文或图注的公开全文证据。它与 `MINERU_BODY_IMAGE_EVIDENCE.md` 的本地解析证据分开：前者来自官方开放全文页面，后者来自项目私有 PDF 的 MinerU/本地解析。摘要或搜索结果只能支持题录与摘要级判断，不能升级为“正文/图像证据”。

## 已核实条目

| ID | 正式题名与入口 | 正文中实际核实的材料/方法 | 图像、图表或场信息 | 对本项目的直接约束 |
|---|---|---|---|---|
| PA22 | Kadkhodaei et al. 2024, [PLOS One 全文](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0304823) | FORMIGA P100、PA2200、ISO-527 标准拉伸试样；四种构建方向；单调/循环拉伸与两阶段应力松弛；0.05 和 0.5 mm/s；每组重复三次。模型用应变函数与时间函数的卷积，并以 Prony 级数表示记忆核；另有晶格结构 FE 验证。 | 正文图组覆盖试样尺寸、构建方向、晶格几何与实验/仿真布置、不同方向力–位移、循环响应、两阶段松弛和加载/卸载曲线。 | 时间相关参数需要松弛或历史加载数据；仅有单调单轴和等双轴数据不能直接开放 M6。 |
| PA23 | Morano, Alfano & Pagnotta 2023, [PubMed 记录与开放 PMC 入口](https://pubmed.ncbi.nlm.nih.gov/37444968/) | SLS PA12；位移速率与热暴露；粉末和烧结件 DSC；拉伸试验；研究结论明确支持速率依赖，热处理只部分改变力学行为。 | Figure 1–4 为试样与热分析；Figure 5 为典型应力–应变曲线并含 y 位移场 inset；Figure 6 为批次变化；Figure 7 为断口孔隙显微图；Figure 8 为不同速率曲线及强度指标；Figure 9 为热处理影响。 | 速率效应可以作为 M3 的物理先验，但该文不是 VFM 识别文；本项目仍需用自身同步全场数据验证率相关参数。 |
| PA24 | Kadkhodaei et al. 2023, [Springer 开放全文](https://link.springer.com/article/10.1007/s00161-023-01199-8) | SLS PA2200；ISO-527 试样；四种构建方向；0.05、0.5、5 mm/s；循环响应约 10 个循环后稳定；比较 2 参数与 5 参数 Mooney–Rivlin，并给出率相关参数。每种方向/速率重复三次。 | Figure 1 为试样尺寸，Figure 2 为构建方向，Figure 3 为拉伸布置，Figure 4 为非线性弹性与 0.2% 偏移示意，Figure 5 为方向对比，Figure 6 为速率对比，Figure 7 为循环稳定化；Table 1–2 给出模型参数与循环前后模量。 | “初始弹性必须线性”不能作为默认假设；但该证据是单轴弹性/循环证据，不能单独证明塑性 M0–M2 的优劣。 |
| PA25 | Schob et al. 2023/2024, [Materials/PMC 开放全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10780187/) | 五个准静态剪切试验；DIC 测量；Chaboche 黏塑模型与修正 GTN 损伤模型组合；参数通过 pattern search 调整并移植到 Abaqus UMAT；平均剪切模量 667.37 MPa、标准差 10.34 MPa，极限强度 32.22 MPa、标准差 2.51 MPa。 | Figure 5 为实验剪应力–时间；Figure 6 为变形体与剪应力；Figure 7 为 MATLAB/UMAT/实验对比；Figure 8 为剪应力场；Figure 9 为局部节点响应；Figure 10 为剪切损伤因子 `k_w` 敏感性，优化值为 0.12，并比较 0 与 0.18。 | 损伤/剪切是后续路线而非首篇主线；VFM 首篇若没有剪切激活与独立损伤数据，不应声称可识别 GTN/Chaboche 损伤参数。 |

## 题录纠正记录

- PA18 的正式题名为 “On the visco-elasto-plastic response of additively manufactured polyamide-12 (PA-12) through selective laser sintering”，不是原注册表中的工作题名；[ScienceDirect 文章页](https://www.sciencedirect.com/science/article/pii/S0142941816310315) 的摘要还明确报告：弹性近似各向同性，而塑性曲线和松弛行为存在明显正交性与非线性。
- PA19 的正式题名为 “Variability, heterogeneity, and anisotropy in the quasi-static response of laser sintered PA12 components”；[MatchID 发表列表](https://www.matchid.eu/publications) 与题录入口显示该文采用 DIC 和 VFM，报告 Young 模量变异系数最高约 6.5%，并将弹性 PA12 描述为更接近各向同性。
- PA27 的正式题名为 “Temperature-Dependent Multiaxial Ratchetting of Polyamide 12 Fabricated by Selective Laser Sintering”；[Wiley 文章页](https://onlinelibrary.wiley.com/doi/10.1111/ffe.70373) 明确包含温度、比例/非比例多轴循环与构建方向效应，因此不能再把“PA12 多轴研究空白”作为缺口。

## 状态解释

本页的“已核实”表示正文或图注已被读取，不表示这些论文的全部原始数据可获得，也不表示其参数可直接移植到本项目的 FS3300PA 批次。材料牌号、设备、试样、热历史和加载路径必须逐项对齐后，才能作为本项目的模型先验。
