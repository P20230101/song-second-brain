# LITERATURE BODY–IMAGE EVIDENCE｜PA12 公开全文核验

更新时间：2026-09-20

## 目的与边界

本页只登记已经打开正文或图注的公开全文证据。它与 `MINERU_BODY_IMAGE_EVIDENCE.md` 的本地解析证据分开：前者来自官方开放全文页面，后者来自项目私有 PDF 的 MinerU/本地解析。摘要或搜索结果只能支持题录与摘要级判断，不能升级为“正文/图像证据”。

## 已核实条目

| ID | 正式题名与入口 | 正文中实际核实的材料/方法 | 图像、图表或场信息 | 对本项目的直接约束 |
|---|---|---|---|---|
| PA22 | Kadkhodaei et al. 2024, [PLOS One 全文](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0304823) | FORMIGA P100、PA2200、ISO-527 标准拉伸试样；四种构建方向；单调/循环拉伸与两阶段应力松弛；0.05 和 0.5 mm/s；每组重复三次。模型用应变函数与时间函数的卷积，并以 Prony 级数表示记忆核；另有晶格结构 FE 验证。 | 正文图组覆盖试样尺寸、构建方向、晶格几何与实验/仿真布置、不同方向力–位移、循环响应、两阶段松弛和加载/卸载曲线。 | 时间相关参数需要松弛或历史加载数据；仅有单调单轴和等双轴数据不能直接开放 M6。 |
| PA23 | Morano, Alfano & Pagnotta 2023, [PubMed 记录与开放 PMC 入口](https://pubmed.ncbi.nlm.nih.gov/37444968/) | SLS PA12；位移速率与热暴露；粉末和烧结件 DSC；拉伸试验；研究结论明确支持速率依赖，热处理只部分改变力学行为。 | Figure 1–4 为试样与热分析；Figure 5 为典型应力–应变曲线并含 y 位移场 inset；Figure 6 为批次变化；Figure 7 为断口孔隙显微图；Figure 8 为不同速率曲线及强度指标；Figure 9 为热处理影响。 | 速率效应可以作为 M3 的物理先验，但该文不是 VFM 识别文；本项目仍需用自身同步全场数据验证率相关参数。 |
| PA24 | Kadkhodaei et al. 2023, [Springer 开放全文](https://link.springer.com/article/10.1007/s00161-023-01199-8) | SLS PA2200；ISO-527 试样；四种构建方向；0.05、0.5、5 mm/s；循环响应约 10 个循环后稳定；比较 2 参数与 5 参数 Mooney–Rivlin，并给出率相关参数。每种方向/速率重复三次。 | Figure 1 为试样尺寸，Figure 2 为构建方向，Figure 3 为拉伸布置，Figure 4 为非线性弹性与 0.2% 偏移示意，Figure 5 为方向对比，Figure 6 为速率对比，Figure 7 为循环稳定化；Table 1–2 给出模型参数与循环前后模量。 | “初始弹性必须线性”不能作为默认假设；但该证据是单轴弹性/循环证据，不能单独证明塑性 M0–M2 的优劣。 |
| PA25 | Schob et al. 2023/2024, [Materials/PMC 开放全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10780187/) | 五个准静态剪切试验；DIC 测量；Chaboche 黏塑模型与修正 GTN 损伤模型组合；参数通过 pattern search 调整并移植到 Abaqus UMAT；平均剪切模量 667.37 MPa、标准差 10.34 MPa，极限强度 32.22 MPa、标准差 2.51 MPa。 | Figure 5 为实验剪应力–时间；Figure 6 为变形体与剪应力；Figure 7 为 MATLAB/UMAT/实验对比；Figure 8 为剪应力场；Figure 9 为局部节点响应；Figure 10 为剪切损伤因子 `k_w` 敏感性，优化值为 0.12，并比较 0 与 0.18。 | 损伤/剪切是后续路线而非首篇主线；VFM 首篇若没有剪切激活与独立损伤数据，不应声称可识别 GTN/Chaboche 损伤参数。 |
| PA28 | Slager, Earp & Ibrahim 2024, [MDPI 全文](https://www.mdpi.com/2073-4360/16/16/2241)；[PMC 全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC11360372/) | SLS neat PA12；Formlabs Fuse 1；单次构建中比较 0.8/3.2 mm 厚度和多打印方向；共 144 个 ASTM-D638 试样，每种方向/厚度 12 个；用 Video Gauge 采集轴向/横向位移并报告 E、屈服、UTS、断裂应变、泊松比和离散度。 | 正文 Figure 3–5 覆盖标准/薄壁试样尺寸、构建区域布置、方向命名和测试对象；结果图和断口显微图比较厚度与方向对弹塑性指标的影响；本地 MinerU 保留图注/表格文字，但未生成独立图片文件。 | 直接支持“厚度、构建方向和同批次重复数必须写入材料契约”；不能把 Video Gauge 当作当前 MatchID DIC，也不能把正交模型建议当成已识别参数。21 页官方 PDF 已由 pypdf 打开并完成 MinerU 本地绑定。 |
| VF08 | Marek, Davis & Pierron 2017, [Springer 开放全文](https://link.springer.com/article/10.1007/s00466-017-1411-6)；[Europe PMC 全文记录](https://pmc.ncbi.nlm.nih.gov/articles/PMC6961464/) | 论文用小应变塑性数值试验比较手工、刚度型和 sensitivity-based virtual fields；正文给出平面应力虚功式、只知边界合力时的外虚功条件、非线性参数最小二乘目标函数，以及线性硬化/Voce 硬化的灵敏度场构造。 | 正文图 7–10 展示虚场和内部/外部虚功；图 11–12 展示噪声下目标函数景观；表 3、6 和图 15–17 给出噪声、参数误差、平滑和虚场缩放影响；结论明确指出 Voce 噪声识别可能落入局部极小值，需多初值，且灵敏度场仍有扰动量、缩放和虚网格选择限制。 | 直接支持本项目把边界合力条件、参数激活、multi-start、噪声、profile/目标景观和虚场超参数纳入 Gate 6–8；它是通用 VFM 方法证据，不是 PA12 材料参数证据。该条为在线官方全文/图像核验，尚未完成本地 PDF/MinerU 绑定。 |
| PA17 | Lammens, De Baere & Van Paepegem 2016, [UGent 公开会议全文](https://biblio.ugent.be/publication/8086754)；[本地 PDF](literature_fulltext/source_pdf/PA17_Lammens_2016_orthotropic_elastoplastic_PA12.pdf) | 正文 p.1–3 明确说明 SLS PA12 的全弹塑性拉伸响应、打印方向比较、3D DIC 和重复性问题；p.2 给出 P395/PA2200、50/50 新旧粉、单一批次、三种打印方向和 ASTM D638 试样；p.2–3 给出每方向 4 个试样、2 Hz 3D-DIC、0–0.2% 应变区间的刚度比较及近似各向同性弹性判断。 | Figure 1 为 edgewise/flatwise/upright 试样和尺寸；Figure 2–5 为方向应力–应变、DIC/引伸计刚度、泊松比和极限强度；本地 MinerU 提取 9 个图像文件，并已人工查看 Figure 1 图像对象。 | 公开会议全文；不计同行评审期刊篇数，也不与 PA19 或 PA19A 合并 | 直接支持方向、批次、重复试样和 DIC 质量作为模型准入条件；不能把 PA2200 或该会议材料参数移植到 FS3300PA，也不能把会议全文当作 PA19 期刊 VFM 证据。 |
| BX05 | G. Vitucci 2024, [作者机构 IRIS 开放全文](https://iris.poliba.it/handle/11589/267160)；[本地 PDF](literature_fulltext/source_pdf/BX05_Vitucci_2024_biaxial_cruciform_equilibrium.pdf) | p.1–4 明确讨论等双轴十字形试样的几何性能指标、平面应力假设、DIC 场量与 load-cell 合力；正文提出沿具有静力意义的 gauge line 用平衡积分识别线弹性参数，并用 FE 优化形状。 | Figure 1 为十字形几何与对称边界；Figure 2 为“载荷—DIC—后处理—平衡—本构参数”流程；后续图表比较几何目标、DIC 测量线和参数识别；MinerU 提取 17 个图像/表格对象，并已人工查看 Figure 2。 | 同行评审 Experimental Mechanics；DOI `10.1007/s11340-024-01052-2` 与 IRIS/出版社题录一致 | 直接支持本项目把边界力合力、场量/虚功平衡、中心 ROI 和几何优化分开审计；材料为软弹性体，不能移植其参数，也不能把其线积分方法直接等同于本项目的 CPS4R 全域 VFM。 |

## 题录纠正记录

- PA18 的正式题名为 “On the visco-elasto-plastic response of additively manufactured polyamide-12 (PA-12) through selective laser sintering”，不是原注册表中的工作题名；[ScienceDirect 文章页](https://www.sciencedirect.com/science/article/pii/S0142941816310315) 的摘要还明确报告：弹性近似各向同性，而塑性曲线和松弛行为存在明显正交性与非线性。
- PA19 的正式题名为 “Variability, heterogeneity, and anisotropy in the quasi-static response of laser sintered PA12 components”；[MatchID 发表列表](https://www.matchid.eu/publications) 与题录入口显示该文采用 DIC 和 VFM，报告 Young 模量变异系数最高约 6.5%，并将弹性 PA12 描述为更接近各向同性。
- PA27 的正式题名为 “Temperature-Dependent Multiaxial Ratchetting of Polyamide 12 Fabricated by Selective Laser Sintering”；[Wiley 文章页](https://onlinelibrary.wiley.com/doi/10.1111/ffe.70373) 明确包含温度、比例/非比例多轴循环与构建方向效应，因此不能再把“PA12 多轴研究空白”作为缺口。

## 状态解释

本页的“已核实”表示正文或图注已被读取，不表示这些论文的全部原始数据可获得，也不表示其参数可直接移植到本项目的 FS3300PA 批次。材料牌号、设备、试样、热历史和加载路径必须逐项对齐后，才能作为本项目的模型先验。
