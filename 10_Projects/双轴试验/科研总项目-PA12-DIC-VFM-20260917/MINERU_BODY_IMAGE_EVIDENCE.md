# MinerU 正文与图像证据页

更新时间：2026-09-20

本页记录已经实际解析到正文和图像对象的资料。它不是最终参考文献表，也不把 OCR 结果自动视为可发表证据。每一条结论都保留来源类型、解析质量和在本项目中的用途。

## 1. 解析记录

| 来源                                                                                    | 解析方式                            | 解析结果                                                                        | 证据等级               | 用途                        |
| ------------------------------------------------------------------------------------- | ------------------------------- | --------------------------------------------------------------------------- | ------------------ | ------------------------- |
| `袁颖诗-2026-SLS-PA12-双轴拉伸.pdf`                                                          | MinerU 本地离线引擎（PyMuPDF4LLM，保留图像） | 45 页；约 51,111 字符；63 个图像引用；63 个提取图像文件                                        | 项目内部全文；OCR/表格部分有乱码 | 审查已有实验、试样、DIC 和结果声明       |
| `A Virtual Fields Method-Genetic Algorithm...`                                        | 已有 MinerU 全文解析                  | 约 166,358 字符；36 个图像引用                                                       | 同行评审方法全文           | VFM 输入、同步、虚功、优化、多初值和噪声设计  |
| `Identification of Constitutive Parameters...`                                        | 已有 MinerU 全文解析                  | 约 22,655 字符；9 个图像/表格对象                                                      | 同行评审方法全文           | DIC、随机虚场、SBVF、参数识别和 FE 验证 |
| `Cruciform specimen design for large plastic strain...`                               | MinerU 3.4.5 本地离线解析；7 页        | 7 个内容项；1 个 Markdown；4 个 JSON；24 个提取图像文件；含 1:2 力比和屈服轨迹图表 | 同行评审试样方法全文         | 双轴比例、臂部提前断裂、DIC/屈服轨迹      |
| `Design of Biaxial Tensile Cruciform Specimen Based on Simulation Optimization`       | MinerU 3.4.5 本地离线解析；9 页        | 9 个内容项；1 个 Markdown；4 个 JSON；21 个提取图像文件；出版社题录与 DOI 已核对 | 会议论文集全文；金属试样方法，不是 PA12 材料证据 | 中心区均匀性、圆角和中心厚度的有限元设计；不移植金属参数 |
| `A comparative study of calibration techniques for finite strain elastoplasticity...` | MinerU 3.4.5 本地离线解析；44 页        | 44 个内容项；1 个 Markdown；4 个 JSON；41 个 Markdown 图像引用；107 个提取图像文件；含真值表、噪声和参数误差图表 | 同行评审计算方法全文         | 真值回收、FEMU/VFM 对照、噪声和模型校准  |
| `Gaussian pre-filtering for uncertainty minimization in digital image correlation using numerically-designed speckle patterns` | MinerU 3.4.5 本地离线解析；15 页 | 15 个内容项；1 个 Markdown；4 个 JSON；63 个提取图像文件；正文涉及图像噪声、子区尺寸、频率内容和高斯预滤波 | 同行评审 DIC 方法全文 | Gate 6 的 DIC 噪声算子、预滤波和空间分辨率敏感性；不作为 PA12 本构证据 |
| `Cruciform specimens biaxial extension performance relationship to constitutive identification` | MinerU 3.4.5 本地离线解析；14 页 | 14 个内容项；1 个 Markdown；4 个 JSON；28 个提取图像文件；正文含等双轴性能指标、沿测量线的应变积分、有限元形状优化、DIC 验证和弹性常数拟合 | arXiv 预印本全文；非同行评审 | Gate 7 的双轴几何/ROI/测量线设计依据；不能替代 PA12 材料证据或同行评审缺口判断 |
| `An experimental and theoretical investigation on the hyper-viscoelasticity of polyamide 12 produced by selective laser sintering`（PA22） | MinerU hybrid-engine 本地解析；18 页；18/18 页完成 | 1 个 Markdown；4 个 JSON；40 个提取图像文件；官方开放同行评审 PA12 全文已与项目本地 PDF 绑定 | 同行评审 PA12 全文 | 用于核对单调/循环/松弛历史依赖和 M6 准入边界；不能把 PA2200/FORMIGA 参数直接移植到当前样品 |
| `Effect of Strain Rates and Heat Exposure on Polyamide (PA12) Processed via Selective Laser Sintering`（PA23） | MinerU hybrid-engine 本地解析；13 页；13/13 页完成 | 1 个 Markdown；4 个 JSON；20 个提取图像文件；官方开放同行评审 PA12 全文已与项目本地 PDF 绑定 | 同行评审 PA12 全文 | 用于核对速率/热暴露的物理证据；可作为 M3 先验线索，但不能替代当前试验的独立同步和率相关参数识别 |
| `Modeling of hyperelasticity in polyamide 12 produced by selective laser sintering`（PA24） | MinerU hybrid-engine 本地解析；10 页；10/10 页完成 | 1 个 Markdown；4 个 JSON；20 个提取图像文件；Springer 官方 PDF 已与项目本地 PDF/MinerU 绑定 | 同行评审 PA12 全文 | 用于核对 PA2200 四方向单轴、循环与速率相关超弹性；不能替代当前 M0–M2 弹塑性筛选或直接移植参数 |
| `Characterization and Simulation of Shear-Induced Damage in Selective-Laser-Sintered Polyamide 12`（PA25） | MinerU hybrid-engine 本地解析；15 页；15/15 页完成 | 1 个 Markdown；4 个 JSON；43 个提取图像文件；MDPI 官方 PDF 已与项目本地 PDF/MinerU 绑定 | 同行评审 PA12 全文 | 用于核对剪切、DIC、Chaboche–改进 GTN、UMAT 与 Abaqus–DIC 场验证；图 8 为剪切应力场，图 10 为剪切因子 $k_w$ 敏感性，图 13 为 Abaqus 与 DIC 的 εᵧ/εₓ 场对比；损伤仍不纳入首篇 M0–M2 主线 |
| `Variability in the mechanical properties of laser sintered PA-12 components`（PA19A） | MinerU 本地离线解析；10 页；正文/图注完成 | 1 个 Markdown；PDF 由 pypdf 打开为 10 页并识别 11 个图像对象；MinerU local 输出正文、Figure 1–6 和 Table 1–6 的图注/文字，但未单独导出图片文件 | 审稿会议论文全文；独立于 PA19 Wiley 期刊版本 | 90 个 PA2200 单轴样本、DIC/MatchID 参数、双轴应变激活和 VFM 识别 `Qij` 的直接证据；支持“PA12 已有 DIC+VFM 先例”和“试样/批次/热历史异质性必须审查”，不能移植其材料参数到 FS3300PA |
| `Influence of Build Orientation and Part Thickness on Tensile Properties of Polyamide 12 Parts Manufactured by Selective Laser Sintering`（PA28） | MinerU 本地离线解析；21 页；正文/图注完成 | 1 个 Markdown；pypdf 打开验证 21 页、题名/作者元数据匹配、正文约 85,344 字符；MinerU 输出 Figure 1–16 与 Table 1–4 等正文/图注和关键统计结果，但 PDF 无独立 `/Image` 对象且 MinerU 未导出单独图片文件 | 同行评审 PA12 全文；官方 MDPI/PMC 与项目本地 PDF/MinerU 已绑定 | 144 个试样、0.8/3.2 mm 厚度、六个方向、Video Gauge/DIC 轴向测量、厚度与方向的 DoA；支持材料契约与正交模型边界，不能移植其参数到 FS3300PA，也不能把 Video Gauge 当成当前 MatchID DIC |
| `On the orthotropic elasto-plastic material response of additively manufactured polyamide 12`（PA17） | MinerU 3.4.5 hybrid-engine high；6/6 页完成 | 1 个 Markdown；4 个 JSON；9 个提取图像文件；pypdf 验证 6 页、题名/PA12/SLS/DIC 关键词一致；图像含三种打印方向试样与应力–应变/刚度/泊松比等图表 | UGent 公开会议全文；公开会议证据，不计同行评审期刊篇数 | 正文给出 P395/PA2200、50/50 新旧粉、单一批次、三种打印方向、每方向 4 个试样、2 Hz 3D-DIC；报告近似各向同性弹性、方向性失效和明显黏性贡献。可约束 M3/M4 的准入审查，但不能替代 PA19 期刊 VFM 证据或移植参数 |
| `Biaxial Extension of Cruciform Specimens: Embedding Equilibrium Into Design and Constitutive Characterization`（BX05） | MinerU 3.4.5 hybrid-engine high；12/12 页完成 | 1 个 Markdown；4 个 JSON；17 个图像/表格对象；pypdf 验证 12 页、题名/DOI/DIC/equilibrium 一致；图像含几何、DIC/载荷链、平衡积分和参数识别流程 | 同行评审 Experimental Mechanics 全文；作者机构 IRIS 开放 PDF 与 DOI/出版社题录交叉核对 | 正文将 load-cell 合力、DIC 位移/应变线、平面应力假设和本构法向应力通过平衡积分连接起来，并用 FE 优化十字形几何；支持本项目审查“边界力 + 全场场线/虚功”的物理契约，但材料为软弹性体，参数不进入 PA12 模型 |

### 1.1 现有方法类全文的本地 PDF 绑定复核

以下 5 条不是 PA12 材料参数证据，但已满足“项目本地 PDF 可打开 + MinerU 正文/图表输出 + 数据库 ID 对应”的绑定条件。它们的题录和用途仍按各自官方/出版社/预印本入口核对；图像对象数量不等于独立实验结果图数量。

| ID | 项目本地 PDF / MinerU 输出 | pypdf 正文核验 | 图/表证据 | 题录/来源交叉核验 | 使用边界 |
|---|---|---:|---|---|---|
| BX16 | `literature_fulltext/mineru/output/cruciform_large_strain/hybrid_auto/cruciform_large_strain_origin.pdf` | 7 页；22,715 字符；27 个 PDF 图像对象 | 正文含多力比、DIC 应变场和屈服轨迹图表 | DOI [10.1088/1742-6596/1063/1/012160](https://doi.org/10.1088/1742-6596/1063/1/012160)；公开题录/全文入口已核对 | 只支撑十字形路径和臂部强化设计；材料为钢，不移植参数 |
| BX18 | `literature_fulltext/mineru/output/cruciform_optimization/hybrid_auto/cruciform_optimization_origin.pdf` | 9 页；18,202 字符；310 个 PDF 图像对象 | 中心区均匀性、圆角/厚度参数与 FE 优化图表 | DOI [10.2991/mmeceb-15.2016.37](https://doi.org/10.2991/mmeceb-15.2016.37)；Atlantis Press 题录已核对 | 只支撑试样几何优化；45 钢参数不能进入 PA12 模型 |
| BX19 | `literature_fulltext/mineru/output/cruciform_constitutive_identification/cruciform_constitutive_identification/auto/cruciform_constitutive_identification_origin.pdf` | 14 页；46,170 字符；24 个 PDF 图像对象 | 等双轴性能指标、测量线应变积分、DIC 验证和弹性常数拟合 | [arXiv:2308.01260](https://arxiv.org/abs/2308.01260)；预印本版本已核对 | 预印本；只作双轴 ROI/路径设计线索，不计同行评审材料证据 |
| VF25 | `literature_fulltext/mineru/output/finite_strain_elastoplasticity/hybrid_auto/finite_strain_elastoplasticity_origin.pdf` | 44 页；92,502 字符；18 个 PDF 图像对象 | FEMU/VFM、真值回收、噪声、灵敏度和模型误差图表 | DOI [10.1016/j.cma.2025.118159](https://doi.org/10.1016/j.cma.2025.118159)；ScienceDirect 与 OSTI 公开版本交叉核对 | 通用有限应变计算方法；不作为 PA12 实验或参数来源 |
| DIC01 | `literature_fulltext/mineru/output/gaussian_prefilter/hybrid_auto/gaussian_prefilter_origin.pdf` | 15 页；64,143 字符；6 个 PDF 图像对象 | 预滤波、散斑尺度、偏差/不确定度和频率内容图表 | DOI [10.1016/j.optlaseng.2014.08.004](https://doi.org/10.1016/j.optlaseng.2014.08.004)；作者机构库题录/全文已核对 | 只支撑 DIC 噪声、预滤波和空间分辨率情景；不作为 PA12 本构证据 |

PA25 图 13 的本地提取图像为 `literature_fulltext/mineru/output/PA25_Schob_2024_shear_damage_PA12/PA25_Schob_2024_shear_damage_PA12/hybrid_auto/images/1ddb611fa8d5ea37eece9d27efc53d451c91ad7119871dc6e0663c797687bc14.jpg`；正文图注明确为 “Comparison of the strain field of Abaqus and DIC in y-direction and x-direction”。

解析输出保存在本地 `科研总项目-PA12-DIC-VFM-20260917/literature_fulltext/mineru/`；受控输入副本和输出均在 D 盘，未把私有 PDF 或提取图像发布到 GitHub。原始 PDF 只读，路径见 [DATA_AUDIT.md](DATA_AUDIT.md)。

## 2. 项目内部 PA12 双轴论文：正文证据

来源：宁波大学本科毕业设计《3D 打印尼龙材料的双轴拉伸测试方法与力学性能》，由 MinerU 本地解析。它可以证明项目已有研究资料包含哪些内容，但不能替代同行评审文献，也不能自动证明原始实验数据已可用于 VFM。

### 2.1 已从正文读到的实验与模型信息

| 主题 | 正文中明确给出的信息 | 对本项目的直接意义 | 当前限制 |
|---|---|---|---|
| 材料与工艺 | Farsoon HT252P；FS3300PA，PA12 基粉末；表 3.2 给出激光功率 45 W、轮廓功率 12 W、扫描速度 1000 mm/s、扫描间距 0.25 mm、粉床预热约 168 °C、层厚 0.1 mm、能量密度 0.18 J/mm² | 可作为工艺/批次审查线索 | 仍须与原始打印记录和试样编号绑定；不能把供应商或论文表格参数直接当成当前样品真值 |
| 试样优化 | 中心区厚度 1 mm、每臂 7 条狭缝、狭缝长度 40 mm、圆角半径 3 mm、狭缝—减薄区间距 0.2 mm | 支持把十字形几何作为 VFM ROI 候选并优先检查中心场 | 优化 FE 使用的是几何比较用各向同性弹塑性，不是 PA12 的已验证识别模型 |
| 几何优化指标 | 中心区 Von Mises 应力分布和相对应力误差；正文报告狭缝间距 0.2 mm 时误差约 2.06%，狭缝数量贡献率最高 | 可用于设计中心 ROI 的结构效应审查 | 该误差是 FE 结构指标，不等于 DIC 场误差，也不等于 VFM 识别误差 |
| 几何优化 FE 模型 | 四分之一模型、对称约束、三维实体网格；统一采用 `E=1800 MPa`、`ν=0.375`、初始屈服约 21 MPa、线性硬化模量约 180 MPa | 说明已有 FE 资料能支撑试样几何初筛 | 不能用这些参数直接宣称 M0 已被真实 PA12 识别；需要独立真值模型和反力导出 |
| 加载 | 单轴和等双轴；速率 0.1、1.0、10 mm/s；等双轴时 X/Y 同步 | 形成现有实验条件矩阵 | 正文未提供足够的非等双轴比例和完整逐帧时间映射；不支持直接开展“最优比例”实验证明 |
| 传感与 DIC | 四个 0–10 kN 力传感器；MatchID DIC；中心区随机散斑；记录 X/Y 位移场及主应变场 | 说明存在力 + 全场测量的研究基础 | 当前 raw `.dat`、力表和 `DIC-xy_0.2` 的同源关系尚未证明；同步和边界牵引仍是 Gate 1/9 阻塞项 |
| XY/XZ 结果声明 | 文中报告 XY 响应更稳定、XZ 更易受层间结合影响；速率升高后应力水平和屈服面整体外扩；XY 屈服点较接近 Von Mises，XZ 有内缩偏离 | 提供模型阶梯 M0–M5 的物理审查假设 | 这些是内部论文的结果声明，必须用原始逐试样曲线、重复性、DIC 质量和同步审计复核；不能直接作为最终论文结论 |

### 2.2 正文中明确承认的范围

该论文明确指出主要研究了等双轴加载，尚未展开不同应力比和复杂路径。这与当前 Gate 审查一致：已有资料可优先做固定速率、XY、单轴 + 等双轴的最小闭环；非等双轴路径先做 synthetic/virtual data 信息量研究，不能把它包装成已有实验结果。

## 3. 项目内部 PA12 双轴论文：图像清单

下表按 MinerU 图像文件的页码 token 和正文图注整理。文件名中的页码是 PDF 页索引线索，正式投稿时仍需以 PDF 页面复核。

| 图号          | 图像内容                      | 对本项目可复用的信息       | 不能直接支持的结论                        |
| ----------- | ------------------------- | ---------------- | -------------------------------- |
| 图 2.1       | 十字形试样四分之一几何与中心测量区截面       | 建立几何参数和中心 ROI 审查 | 不能证明中心区真实应力均匀                    |
| 图 2.2–2.3   | 中心厚度对应力分布/应力误差的影响         | 结构参数敏感性候选        | 不能替代真实材料参数灵敏度                    |
| 图 2.4–2.5   | 狭缝数量对应力分布/误差率             | 支撑优先检查狭缝数和臂刚度    | 不能把几何误差当作 VFM 噪声                 |
| 图 2.6–2.7   | 狭缝长度对应力分布/误差率             | 支撑几何筛选           | 不能证明不同加载路径可辨识性                   |
| 图 2.8–2.9   | 圆角半径对应力分布/误差率             | 支撑边缘应力集中审查       | 不能证明损伤起始位置                       |
| 图 2.10–2.11 | 狭缝间距对应力分布/误差率             | 支撑最终几何参数选择       | OCR 对部分图前说明有错位，数值需回到 PDF/FE 输出复核 |
| 图 2.12      | 几何因素误差贡献率比较               | 可作为结构优化结果图的模板    | 不是材料参数 FIM 或灵敏度矩阵                |
| 图 3.1       | 双轴装置与 DIC 测量流程            | 说明四传感器 + 相机的测量链  | 流程图不能验证真实硬件同步                    |
| 图 3.2       | SLS 设备与 PA12 成形原理         | 工艺背景图            | 不能替代打印日志或微观证据                    |
| 图 3.3       | XY/XZ 设备坐标取向              | 支撑取向标签和坐标约定      | 不能证明每个 raw 文件的实际取向               |
| 图 4.1       | X/Y 方向传感器力—时间曲线           | 可作为双向平衡性诊断图模板    | 正文“峰值差异小于 5%”仍需逐帧原始数据审计          |
| 图 4.2       | 不同速率 DIC 表面位移场            | 可作为 DIC 全场质量图模板  | 不能证明字段与当前 `DIC-xy_0.2` 同源        |
| 图 4.3       | 不同速率 DIC 表面应变场            | 可用于中心 ROI/局部化检查  | 不能替代位移梯度、空间分辨率和边界缺失审计            |
| 图 4.4–4.5   | XY/XZ 在速率和加载方式下的工程应力—应变曲线 | 支撑曲线级模型筛选的图形结构   | 图像曲线不能提供逐帧反力、参数置信区间或独立验证         |
| 图 4.6       | XY/XZ 断裂形貌                | 支撑取向—失效假设        | 当前第一篇最小论文应先不把损伤模型作为主线            |
| 图 4.7       | 实验屈服点与 Von Mises 屈服面对比    | 支撑 M0 与方向扩展的判别问题 | 只有单轴/等双轴点不能唯一识别一般各向异性屈服面         |
|             |                           |                  |                                  |

提取图像对象包括公式、表格或版面图，不等于 63 张都是独立实验结果图；正式整理时应按图注去重。

### 3.1 两个图像对象的可视核验

- `...pdf-0039-02.png`：屈服面散点图可读，坐标为 `σ1/σ2`（MPa），包含 0.1、1、10 mm/s 三条速率曲线，并用符号区分单轴/双轴和 XY/XZ。它支持“该论文展示了屈服面比较图”的图像级事实；不能从低分辨率图像反算原始点值或置信区间。
- `...pdf-0034-01.png`：可读为中心区域 DIC 应变云图，试样散斑和十字形中心区均可见。它支持“存在 DIC 全场展示”的事实；不能单凭截图证明应变分量、单位、时间同步、边界质量或场量可用于 VFM。
- `...pdf-0034-13.png`、`...14.png`、`...15.png`：实际是独立色标对象，不是完整 DIC 场；后续图像清单不得把它们计作三张独立全场结果图。

## 4. 同行评审 VFM 全文：可迁移的方法证据

### 4.1 VFM-GA 框架

正文明确把实验图像、DIC 位移场、未变形网格、形变梯度/对数应变、给定参数下的应力场、同步 load-cell 数据、内外虚功平衡和目标函数串成一条链，并在优化前加入稳定性过滤器。它还用独立初始种群、遗传算法收敛图、加载路径验证和 13 个噪声水平 × 3 个权重参数开展噪声研究。

图像信息包括：

- Fig. 1：DIC + load cell 同步、虚功残差和目标函数的总流程；
- Fig. 2–3：遗传算法流程和多初始种群收敛；
- Fig. 9–10：均匀/非均匀变形输入与独立验证；
- Fig. 11：位移噪声水平与应力/横向应变误差的关系；
- Appendix Tables A.1–A.4：参数范围、VFM 参数和 GA 超参数。

迁移到本项目的结论是“同步、全场、独立验证、多初值、噪声研究必须写进方法链”，而不是照搬遗传算法。该文材料为超弹性泡沫，不能证明 PA12 的模型形式。

### 4.2 全场测量 + VFM 识别橡胶参数

正文采用 DIC 位移/梯度场、随机虚位移场与 sensitivity-based virtual fields 比较 Mooney/Ogden 参数，并用 Abaqus 力—位移模拟做验证。图像/表格包括样品几何、实验装置、ROI/ZOI、位移梯度、两类虚场识别参数以及 FE—实验力对比。

迁移到本项目的结论是：虚场独立性、灵敏度缩放和 FE 验证是可审计的组成部分；但橡胶材料和超弹性模型不支持直接选定 PA12 的 M1/M2。

### 4.3 双轴十字形试样设计全文

该文明确使用多组力比（包括 0:1、1:4、1:2、3:4、1:1、4:3、2:1、4:1、1:0）来获取第一象限屈服信息；通过加强狭缝臂避免臂部提前断裂，并结合 DIC 和载荷计算规区真应力/塑性应变及屈服轨迹。

图像包括 ISO 与改进十字形尺寸、显微组织、硬度、单轴载荷—位移、断裂位置、Von Mises—塑性应变和实验屈服轨迹。它直接支持本项目把加载比例和“臂先断裂”作为设计变量；材料是钢，不能外推 PA12 的速率、孔隙和层间机制。

## 5. 对研究路线的更新

1. `Gate 1` 不因存在一篇完整内部论文而自动通过：仍需证明 raw `.dat`、力时序和 DIC CSV 的同源与同步。
2. `Gate 3/4` 继续保持失败/阻塞：内部论文的均匀等双轴 FE 只能作为几何背景，不能提供独立反力和参数激活充分的 Virtual Experiment。
3. 第一篇论文仍采用固定速率、XY、单轴 + 等双轴的最小闭环；非等双轴比例先用 virtual data 做信息量和 FIM 设计。
4. 文献数据库增加 `body_evidence`、`image_evidence`、`source_type`、`evidence_limit` 字段。只有正文或图注已实际读取的文献，才可进入“全文证据”子集；其余保留为题录/摘要候选。

## 6. 下一步 Gate

下一步不是继续堆模型，而是完成两件可判定的工作：

- 对 `DIC-xy_0.2` 与 `XY-0.1-02` 建立同源证明或明确拆分为独立 legacy field；
- 在 Abaqus 中生成具有运动学相容位移场、独立边界反力、非均匀应力/应变激活和可导出逐帧状态的真值模型。

在这两项没有通过前，不进入真实数据 VFM 参数识别，也不把任何优化器收敛图写成论文结论。
