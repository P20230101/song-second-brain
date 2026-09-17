# LITERATURE DATABASE｜PA12–DIC–VFM 审计注册表 v0.1

更新时间：2026-09-17

## 使用声明

这是从真实本地题录、已解析全文、Wiki 矩阵和官方 DOI/出版社入口整理的审计注册表，不是“已经逐篇读完 60 篇论文”的声明。`正文/图像证据` 是本表的硬状态：只有实际打开并读取正文、图注或提取图像的条目才标为 `全文+图像` 或 `官方全文+图像`；从另一篇论文参考文献读出的题录只能标为 `本地引用`。

去重规则：同一 DOI 只保留一行；无 DOI 的条目保留作者、题名、期刊和来源位置，并标为待核。不得用书籍、标准、软件手册或坏 DOI 填补“论文数”。当前注册表共 84 个唯一条目，其中 `P00` 是项目内部学位论文、`VF40` 是方法专著；其余为论文/方法条目。两者均不计入同行评审论文数。

状态代码：

- `全文+图像`：正文、图注/图表已由 MinerU 或本地全文实际读取；
- `官方全文+图像`：官方开放全文已读取正文、图注或图表；
- `官方页`：作者/题名/DOI/期刊入口已由官方页面或 DOI 页面核对，正文与图像尚未登记；
- `本地引用`：题录从项目内已解析文献或内部论文参考文献读出，独立全文待核；
- `待补证`：只作为检索候选，不进入最终投稿参考文献表。

## A. PA12、SLS/MJF 与工艺—结构—性能

| ID | 作者/年份/题名与 DOI | 材料/实验 | 本构/识别方法 | DIC | VFM | 双轴 | 速率 | 各向异性 | 可辨识性 | 正文/图像证据 | 本项目用途 |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| P00 | 袁颖诗 2026，《3D 打印尼龙材料的双轴拉伸测试方法与力学性能》，项目内部学位论文 | SLS FS3300PA PA12；XY/XZ；单轴/等双轴；0.1/1/10 mm/s | 几何优化用各向同性弹塑性；Von Mises 屈服对照 | 是 | 否 | 是 | 是 | 是 | 未报告 | 全文+图像 | 已有实验条件和图注审查，不计同行评审论文数 |
| PA01 | Goodridge, Tuck & Hague 2012, “Laser sintering of polyamides and other polymers” | 聚合物粉末床工艺综述 | 工艺—结构—性能综述 | 未报告 | 否 | 否 | 未报告 | 未报告 | 未报告 | 本地引用 | 工艺背景，不能给当前参数 |
| PA02 | 史玉升等 2015，《选择性激光烧结 3D 打印用高分子复合材料》 | SLS 高分子复合材料 | 材料与工艺综述 | 未报告 | 否 | 否 | 未报告 | 可能 | 未报告 | 本地引用 | 材料背景 |
| PA03 | Cai et al. 2021, “Comparative study on 3D printing of polyamide 12 by selective laser sintering and multi jet fusion” | PA12；SLS 与 MJF 对比 | 工艺与性能比较 | 未报告 | 否 | 否 | 可能 | 可能 | 未报告 | 本地引用 | 限定 SLS/MJF 不能混合 |
| PA04 | Xu et al. 2019, “The process and performance comparison of polyamide 12 manufactured by multi jet fusion and selective laser sintering” | PA12；MJF/SLS | 工艺—性能比较 | 未报告 | 否 | 否 | 可能 | 可能 | 未报告 | 本地引用 | 工艺边界 |
| PA05 | Yang et al. 2023, “A review of aging, degradation, and reusability of PA12 powders in selective laser sintering additive manufacturing” | SLS PA12 粉末 | 老化/复用综述 | 未报告 | 否 | 否 | 未报告 | 可能 | 未报告 | 本地引用 | 粉末状态元数据 |
| PA06 | Caulfield, McHugh & Lohfeld 2007, “Dependence of mechanical properties of polyamide components on build parameters in the SLS process” | SLS PA；构建参数与力学试验 | 参数—性能关系 | 未报告 | 否 | 否 | 未报告 | 是 | 未报告 | 本地引用 | 打印参数控制 |
| PA07 | Drummer et al. 2019, “A novel approach for understanding laser sintering of polymers” | 激光烧结聚合物 | 工艺机理/实验表征 | 未报告 | 否 | 否 | 未报告 | 未报告 | 未报告 | 本地引用 | 工艺解释 |
| PA08 | Wudy & Drummer 2019, “Aging effects of polyamide 12 in selective laser sintering: Molecular weight distribution and thermal properties” | SLS PA12；粉末老化 | 热学/分子量表征 | 未报告 | 否 | 否 | 未报告 | 未报告 | 未报告 | 本地引用 | 粉末复用风险 |
| PA09 | Sanders, Cant & Jenkins 2024, “Re-use of polyamide-12 in powder bed fusion and its effect on process-relevant powder characteristics and final part properties” | PBF PA12；粉末复用 | 粉末—成形件性能 | 未报告 | 否 | 否 | 未报告 | 可能 | 未报告 | 本地引用 | 批次/粉末状态 |
| PA10 | Hejmady et al. 2022, “Laser sintering of PA12 particles studied by in-situ optical, thermal and X-ray characterization” | SLS PA12 颗粒；原位光学/热/X 射线 | 结晶/烧结机理 | 未报告 | 否 | 否 | 未报告 | 未报告 | 未报告 | 本地引用 | 微观机制背景 |
| PA11 | Balemans et al. 2020, “Numerical analysis of the crystallization kinetics in SLS” | SLS；结晶动力学 | 结晶动力学数值模型 | 未报告 | 否 | 否 | 未报告 | 未报告 | 未报告 | 本地引用 | 工艺历史解释 |
| PA12 | Battu et al. 2020, “Build orientation dependent microstructure in polymer laser sintering: Relationship to part performance and evolution with aging” | 聚合物激光烧结；构建方向 | 微观结构—性能 | 未报告 | 否 | 否 | 未报告 | 是 | 未报告 | 本地引用 | XY/XZ 假设边界 |
| PA13 | Sindinger et al. 2020, “Thickness dependent anisotropy of mechanical properties and inhomogeneous porosity characteristics in laser-sintered polyamide 12 specimens” | 激光烧结 PA12；厚度/孔隙 | 各向异性与孔隙表征 | 未报告 | 否 | 否 | 未报告 | 是 | 未报告 | 本地引用 | 方向性和厚度效应 |
| PA14 | Dadbakhsh et al. 2017, “Effect of PA12 powder reuse on coalescence behaviour and microstructure of SLS parts” | SLS PA12；粉末复用 | 烧结颈/微结构 | 未报告 | 否 | 否 | 未报告 | 可能 | 未报告 | 本地引用 | 粉末批次审查 |
| PA15 | Yao, Li & Zhu 2020, “Effect of powder recycling on anisotropic tensile properties of selective laser sintered PA2200 polyamide” | SLS PA2200；回收粉末；拉伸 | 方向性拉伸表征 | 未报告 | 否 | 否 | 未报告 | 是 | 未报告 | 本地引用 | 不能把 PA2200 参数移植 PA12 |
| PA16 | Schneider & Kumar 2020, “Multiscale characterization and constitutive parameters identification of polyamide PA12 processed via selective laser sintering”, DOI [10.1016/j.polymertesting.2020.106357](https://doi.org/10.1016/j.polymertesting.2020.106357) | SLS PA12；拉/压/弯/剪/断裂 | Three-Network；多试验标定 | 非核心 | 否 | 否 | 间接 | 是 | 未重点报告 | 官方页 | PA12 本构先验；不等于双轴 VFM |
| PA17 | Lammens et al. 2016, SLS PA12 directional/rate response [题名待官方页复核] | SLS PA12；方向/速率拉伸 | 方向性、速率响应 | 是 | 否 | 否 | 是 | 是 | 未重点报告 | 本地引用 | M3/M4 准入依据 |
| PA18 | Lammens, Kersemans, De Baere & Van Paepegem 2017, “On the visco-elasto-plastic response of additively manufactured polyamide-12 (PA-12) through selective laser sintering”, DOI [10.1016/j.polymertesting.2016.11.032](https://doi.org/10.1016/j.polymertesting.2016.11.032) | SLS PA12；拉伸/压缩/剪切/松弛 | 黏弹塑/方向性 | 辅助 | 否 | 否 | 是 | 是 | 未重点报告 | 官方页 | M6 只能条件开放 |
| PA19 | Faes, Wang, Lava & Moens 2016/2017, “Variability, heterogeneity, and anisotropy in the quasi-static response of laser sintered PA12 components”, DOI [10.1111/str.12219](https://doi.org/10.1111/str.12219) | SLS PA12；多方向单轴；DIC | 弹性刚度与变异性；VFM | 是 | 是 | 否 | 未报告 | 是 | 部分 | 官方页 | 批次/位置变异性；支持“已有 PA12-VFM 先例” |
| PA20 | Salazar, Cano & Rodríguez 2022, “Mechanical and fatigue behaviour of polyamide 12 processed via injection moulding and selective laser sintering” | PA12；注塑/SLS；疲劳 | Kitagawa–Takahashi 图 | 未报告 | 否 | 否 | 未报告 | 可能 | 未报告 | 本地引用 | 失效扩展背景 |
| PA21 | Cobian et al. 2022, “Micromechanical characterization of the material response in a PA12-SLS fabricated lattice structure and its correlation with bulk behavior” | SLS PA12 晶格与块体 | 微观—宏观相关 | 未报告 | 否 | 否 | 未报告 | 可能 | 未报告 | 本地引用 | 晶格不替代块体 |
| PA22 | Kadkhodaei, Pawlikowski, Drobnicki & Domański 2024, “An experimental and theoretical investigation on the hyper-viscoelasticity of polyamide 12 produced by selective laser sintering”, DOI [10.1371/journal.pone.0304823](https://doi.org/10.1371/journal.pone.0304823) | SLS PA12；单调/循环/两阶段松弛；标准试样与晶格 | 超黏弹卷积模型 + FE | 非核心 | 否 | 否 | 是 | 是 | 未重点报告 | 官方全文+图像 | 只有历史数据足够时才开放 M6 |
| PA23 | Morano, Alfano & Pagnotta 2023, “Effect of Strain Rates and Heat Exposure on Polyamide (PA12) Processed via Selective Laser Sintering”, DOI [10.3390/ma16134654](https://doi.org/10.3390/ma16134654), PMC [全文入口](https://pmc.ncbi.nlm.nih.gov/articles/PMC10342904/) | SLS PA12；速率/热暴露；DSC/拉伸/DIC | 速率效应表征 | 是 | 否 | 否 | 是 | 未重点报告 | 未报告 | 官方全文+图像 | 速率扩展物理依据；正文 Figure 5 明确含 y 位移场 |
| PA24 | Kadkhodaei, Pawlikowski, Drobnicki & Domański 2023, “Modeling of hyperelasticity in polyamide 12 produced by selective laser sintering”, DOI [10.1007/s00161-023-01199-8](https://doi.org/10.1007/s00161-023-01199-8) | SLS PA12；PA2200；四方向单轴；循环/速率 | 2/5 参数 Mooney–Rivlin；率相关超弹性 | 否 | 否 | 否 | 是 | 近似各向同性 | 未报告 | 官方全文+图像 | M0–M2 前的弹性非线性筛选；支持不要把弹性默认线性 |
| PA25 | Schob et al. 2023/2024, “Characterization and Simulation of Shear-Induced Damage in Selective-Laser-Sintered Polyamide 12”, DOI [10.3390/ma17010038](https://doi.org/10.3390/ma17010038), PMC [全文入口](https://pmc.ncbi.nlm.nih.gov/articles/PMC10780187/) | SLS PA12；准静态剪切；DIC/FE/UMAT | Chaboche 黏塑 + 修正 GTN 损伤；kw 敏感性 | 是 | 否 | 可能 | 可能 | 是 | 未重点报告 | 官方全文+图像 | 损伤后续线，不进首篇 |
| PA26 | Chen et al. 2021, “A finite strain viscoelastic-viscoplastic model for additively manufactured PA12”, DOI [10.1016/j.ijplas.2021.103029](https://doi.org/10.1016/j.ijplas.2021.103029) | MJF PA12；加载—卸载—恢复；μCT/RVE | 有限应变黏弹–黏塑–损伤 | 相关 | 否 | 组合 | 是 | 可能 | 未重点报告 | 官方页 | MJF 与 SLS 分开处理 |
| PA27 | Zhao, Chen, Linghu, Kan & Kang 2026, “Temperature-Dependent Multiaxial Ratchetting of Polyamide 12 Fabricated by Selective Laser Sintering”, DOI [10.1111/ffe.70373](https://doi.org/10.1111/ffe.70373) | SLS PA12；多轴比例/非比例循环；温度/方向 | 温度相关多轴棘轮 | 非核心 | 否 | 是 | 是 | 是 | 未报告 | 官方页 | 否定“PA12 多轴空白”；数据按作者要求提供 |

## B. 双轴十字形试样、设备与路径设计

| ID | 作者/年份/题名与 DOI | 材料/实验 | 本构/识别方法 | DIC | VFM | 双轴 | 速率 | 各向异性 | 可辨识性 | 正文/图像证据 | 本项目用途 |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| BX01 | Makinde, Thibodeau & Neale 1992, “Development of an apparatus for biaxial testing using cruciform specimens” | 十字形双轴设备 | 装置与载荷路径 | 未报告 | 否 | 是 | 未报告 | 未报告 | 未报告 | 本地引用 | 设备边界背景 |
| BX02 | Makinde, Thibodeau & Lefebvre 1992, “Design of a biaxial extensometer for measuring strains in cruciform specimens” | 十字形双轴；应变引伸计 | 应变测量 | 未报告 | 否 | 是 | 未报告 | 未报告 | 未报告 | 本地引用 | 应变测量对照 |
| BX03 | Demmerle & Boehler 1993, “Optimal design of biaxial tensile cruciform specimens”, DOI [10.1016/0022-5096(93)90067-P](https://doi.org/10.1016/0022-5096(93)90067-P) | 金属板；十字形试样 | 应力均匀性/夹具转动顺应 | 未报告 | 否 | 是 | 未报告 | 是 | 部分 | 官方页 | 几何优化不能只看载荷 |
| BX04 | Nasdala & Husni 2020, “Determination of Yield Surfaces in Accordance With ISO 16842 Using an Optimized Cruciform Test Specimen” | 金属板；多力比屈服面 | 屈服轨迹 | 未报告 | 否 | 是 | 未报告 | 是 | 部分 | 本地引用 | 屈服面路径模板 |
| BX05 | Vitucci 2024, “Biaxial Extension of Cruciform Specimens: Embedding Equilibrium Into Design and Constitutive Characterization”, DOI [10.1007/s11340-024-01052-2](https://doi.org/10.1007/s11340-024-01052-2) | 弹性体/十字形双轴 | 平衡约束与本构表征 | 是 | 否 | 是 | 未报告 | 未报告 | 部分 | 官方页 | 中心 ROI 与平衡审查 |
| BX06 | Zhang et al. 2021, “Effect of cruciform specimen design on strain paths and fracture location in equi-biaxial tension” | 金属板；等双轴 | 试样设计/断裂位置 | 未报告 | 否 | 是 | 未报告 | 未报告 | 未报告 | 本地引用 | 断裂位置不能直接作材料失效 |
| BX07 | Lamkanfi et al. 2010 Part 1, “Strain distribution in cruciform specimens subjected to biaxial loading conditions: Two-dimensional versus three-dimensional finite element model” | 聚合物十字形 | 2D/3D FE 场量比较 | 未报告 | 否 | 是 | 未报告 | 可能 | 未报告 | 本地引用 | 2D 平面假设审查 |
| BX08 | Lamkanfi et al. 2010 Part 2, “Strain distribution in cruciform specimens subjected to biaxial loading conditions: Influence of geometrical discontinuities” | 聚合物十字形 | 几何不连续与应变场 | 未报告 | 否 | 是 | 未报告 | 可能 | 未报告 | 本地引用 | 狭缝/圆角设计 |
| BX09 | Lamkanfi, Van Paepegem & Degrieck 2015, “Shape optimization of a cruciform geometry for biaxial testing of polymers” | 聚合物十字形 | 几何形状优化 | 未报告 | 否 | 是 | 未报告 | 可能 | 部分 | 本地引用 | 试样优化先验 |
| BX10 | Smits et al. 2006, “Design of a cruciform specimen for biaxial testing of fibre reinforced composite laminates”, DOI [10.1016/j.compscitech.2005.08.011](https://doi.org/10.1016/j.compscitech.2005.08.011) | 纤维增强复材；双轴 | 全场应变/几何优化 | 是 | 否 | 是 | 未报告 | 是 | 部分 | 官方页 | 不能移植材料参数 |
| BX11 | Tiernan & Hannon 2014, “An investigation of the effect of cruciform specimen geometry on the stress distribution under biaxial loading” | 低碳钢；FEM + 实验 | 几何优化 | 未报告 | 否 | 是 | 未报告 | 可能 | 部分 | 官方页 | 不存在通用几何 |
| BX12 | Martins, Andrade-Campos & Thuillier 2019, “Design of biaxial tensile tests for the identification of anisotropic plasticity parameters” | 金属；十字形/VFM | 硬化 + 各向异性参数 | 是 | 是 | 是 | 未报告 | 是 | 是 | 官方页 | 直接支持路径/FIM 设计 |
| BX13 | Serna Moreno & Horta Muñoz 2024, “Biaxial compression testing of composite laminates using cruciform specimens” | 复合材料；双轴压缩/DIC | 屈曲/损伤 | 是 | 否 | 是 | 未报告 | 是 | 未报告 | 官方页 | 压缩稳定性边界 |
| BX14 | “A miniaturized biaxial deformation rig”, 2016, DOI [10.1007/s11340-016-0244-0](https://doi.org/10.1007/s11340-016-0244-0) | 多材料；微型双轴设备 | 四轴顺应性/导向 | 未报告 | 否 | 是 | 未报告 | 未报告 | 未报告 | 官方页 | 夹具变量 |
| BX15 | Hoferlin et al. 1998, “Biaxial tests on cruciform specimens for the validation of crystallographic yield loci”, DOI [10.1016/S0924-0136(98)00123-X](https://doi.org/10.1016/S0924-0136(98)00123-X) | 钢板；多力比双轴 | 晶体屈服轨迹 | 未报告 | 否 | 是 | 未报告 | 是 | 部分 | 官方页 | 路径多样性证据 |
| BX16 | Hou et al. 2018, “Cruciform specimen design for large plastic strain during biaxial tensile testing”, DOI [10.1088/1742-6596/1063/1/012160](https://doi.org/10.1088/1742-6596/1063/1/012160) | 钢板；多力比；DIC | 臂部加强/屈服轨迹 | 是 | 否 | 是 | 未报告 | 是 | 部分 | 全文+图像 | 多力比与臂先断裂 |
| BX17 | Yang et al. 2022, “Optimization of cruciform specimen geometry for biaxial tensile testing using a genetic algorithm”, DOI [10.1007/s11665-022-07258-6](https://doi.org/10.1007/s11665-022-07258-6) | 金属/十字形 | 遗传算法几何优化 | 未报告 | 否 | 是 | 未报告 | 可能 | 部分 | 官方页 | 只作优化方法参考 |

## C. DIC、全场应力、VFM/FEMU 与参数可辨识性

| ID | 作者/年份/题名与 DOI | 材料/实验 | 本构/识别方法 | DIC | VFM | 双轴 | 速率 | 各向异性 | 可辨识性 | 正文/图像证据 | 本项目用途 |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| VF01 | Grediac, Pierron, Avril & Toussaint 2006, “The virtual fields method for extracting constitutive parameters from full-field measurements: a review”, DOI [10.1111/j.1475-1305.2006.tb01504.x](https://doi.org/10.1111/j.1475-1305.2006.tb01504.x) | 多材料全场测量综述 | VFM 原理/虚功 | 是 | 是 | 视案例 | 视案例 | 可扩展 | 部分 | 官方页 | 方法总框架 |
| VF02 | Avril et al. 2008, “Overview of identification methods of mechanical parameters based on full-field measurements” | 多类材料/全场 | VFM、FEMU、缺陷/场量反演综述 | 是 | 是 | 视案例 | 视案例 | 视案例 | 是 | 本地引用 | 方法比较 |
| VF03 | Promma et al. 2009, “Application of the virtual fields method to mechanical characterization of elastomeric materials” | 橡胶；异质试验 | 超弹性 VFM | 是 | 是 | 可能 | 否 | 否 | 部分 | 本地引用 | 异质场减少均匀试验 |
| VF04 | Guélon et al. 2009, “A new characterization method for rubbers”, DOI [10.1016/j.polymertesting.2009.06.001](https://doi.org/10.1016/j.polymertesting.2009.06.001) | 橡胶；全场 | 超弹性参数反演 | 是 | 是 | 可能 | 否 | 否 | 部分 | 官方页 | 全场/参数反演先例 |
| VF05 | Pierron 2010, “Identification of Poisson’s ratios of standard and auxetic low-density polymeric foams from full-field measurements” | 聚合物泡沫 | 全场弹性参数 | 是 | 是 | 未报告 | 否 | 可能 | 部分 | 本地引用 | 聚合物全场识别 |
| VF06 | Geymonat, Hild & Pagano 2002, “Identification of elastic parameters by displacement field measurement” | 弹性材料；位移场 | 位移场反演 | 是 | 是 | 未报告 | 否 | 未报告 | 是 | 本地引用 | 线弹性基线 |
| VF07 | Avril, Grédiac & Pierron 2004, “Sensitivity of virtual fields to noisy data” | 全场测量；噪声 | VFM 噪声灵敏度 | 是 | 是 | 未报告 | 未报告 | 可扩展 | 是 | 本地引用 | 噪声与虚场设计 |
| VF08 | Marek, Davis & Pierron 2017, “Sensitivity-based virtual fields for the non-linear virtual fields method”, DOI [10.1007/s00466-017-1411-6](https://doi.org/10.1007/s00466-017-1411-6) | 非线性材料/塑性场 | SBVF | 是 | 是 | 视案例 | 未报告 | 可扩展 | 是 | 官方页 | 不把 SBVF 宣称为首次 |
| VF09 | Marek et al. 2018, “Extension of the sensitivity-based virtual fields to large deformation anisotropic plasticity” | 各向异性塑性；大变形 | SBVF/各向异性塑性 | 是 | 是 | 可能 | 未报告 | 是 | 是 | 本地引用 | M4/SBVF 后续扩展 |
| VF10 | Rahmani, Villemure & Levesque 2014, “Regularized virtual fields method for mechanical properties identification of composite materials”, DOI [10.1016/j.cma.2014.05.010](https://doi.org/10.1016/j.cma.2014.05.010) | 复材；全场 | 正则化 VFM | 是 | 是 | 可能 | 未报告 | 是 | 是 | 官方页 | 正则化边界 |
| VF11 | Périé et al. 2009, “Digital image correlation and biaxial test on composite material for anisotropic damage law identification” | 复材；双轴/DIC | 各向异性损伤识别 | 是 | 否 | 是 | 未报告 | 是 | 部分 | 本地引用 | DIC 双轴损伤先例 |
| VF12 | Zhang et al. 2018, “A special stereo-DIC system for VFM identification”, DOI [10.1016/j.optlaseng.2017.11.016](https://doi.org/10.1016/j.optlaseng.2017.11.016) | 铝合金；单轴/纯剪 | 立体 DIC + VFM | 是 | 是 | 否 | 否 | 可能 | 部分 | 官方页 | 2D 面外误差边界 |
| VF13 | Sutton et al. 2008, “Three-dimensional digital image correlation for displacement and deformation measurement”, DOI [10.1016/j.optlaseng.2008.05.005](https://doi.org/10.1016/j.optlaseng.2008.05.005) | 刚体/变形测量 | 2D/3D DIC 误差 | 是 | 否 | 否 | 未报告 | 未报告 | 未报告 | 官方页 | 2D 平面假设闸门 |
| VF14 | Wittevrongel et al. 2015, “Improvement of DIC measurements using out-of-plane motion compensation”, DOI [10.1111/str.12146](https://doi.org/10.1111/str.12146) | 多次拉伸；2D DIC | 面外补偿 | 是 | 否 | 可能 | 未报告 | 未报告 | 未报告 | 官方页 | 刚体/面外预试验 |
| VF15 | Maček et al. 2024, “Uncertainty quantification of material parameters identified from full-field measurements”, DOI [10.1016/j.optlaseng.2023.107958](https://doi.org/10.1016/j.optlaseng.2023.107958) | 复材/全场；不确定度 | 参数概率/传播 | 是 | 相关 | 可能 | 未报告 | 是 | 是 | 官方页 | 系统误差和置信区间 |
| VF16 | Pierron & Grédiac 2021, “Towards Material Testing 2.0: A review of test design for identification of constitutive parameters from full-field measurements”, DOI [10.1111/str.12370](https://doi.org/10.1111/str.12370) | 全场测试综述 | 试验设计/识别 | 是 | 是 | 视案例 | 视案例 | 视案例 | 是 | 官方页 | FIM/试验设计总依据 |
| VF17 | Jiang et al. 2022, “Extracting material parameters under biaxial tensile tests using virtual fields and investigating missing-edge data”, DOI [10.1080/15376494.2021.1979138](https://doi.org/10.1080/15376494.2021.1979138) | 硅橡胶；双轴/DIC | 多步 VFM/边缘缺失 | 是 | 是 | 是 | 否 | 否 | 是 | 官方页 | 噪声/边缘缺失设计 |
| VF18 | Jiang & Wang 2023, “Reformulation of the virtual fields method based on the variation of elastic energy for hyperelastic materials”, DOI [10.1016/j.ijsolstr.2023.112303](https://doi.org/10.1016/j.ijsolstr.2023.112303)（Crossref/OpenAlex 未找到匹配元数据，待补证） | 超弹性材料 | 弹性能变分 VFM | 全场 | 是 | 可能 | 否 | 否 | 是 | 缺失/待补证 | 内外功接口检查 |
| VF19 | Nguyen et al. 2026, “Full-field identification of anisotropic polymer behavior from biaxial experiments: FEMU and VFM comparison”, DOI [10.1002/pen.70150](https://doi.org/10.1002/pen.70150) | PET；十字形双轴/DIC | FEMU/VFM；各向异性 | 是 | 是 | 是 | 未报告 | 是 | 是 | 官方页 | 直接否定宽泛方法空白 |
| VF20 | Zhang et al. 2025, “Anisotropic plasticity identification using FE-VFM and sensitivity-based virtual fields”, DOI [10.1016/j.ijmecsci.2025.110815](https://doi.org/10.1016/j.ijmecsci.2025.110815) | SUS316；单轴/双轴虚拟试验 | Hill48/Yld2000-2D；FE/S-VFM | 是 | 是 | 是 | 否 | 是 | 是 | 官方页 | M4 路径和 FIM 先例 |
| VF21 | Meng, Yousefi & Avril 2025, “Machine-learning-driven virtual fields for anisotropic hyperelastic identification”, DOI [10.1016/j.cma.2024.117580](https://doi.org/10.1016/j.cma.2024.117580) | 生物组织/异质全场 | 学习式 VFM/各向异性超弹 | 是 | 是 | 视案例 | 未报告 | 是 | 是 | 官方页 | AI 后置，不进首篇 |
| VF22 | Nikolov et al. 2026, “Variationally matched sensitivity-based virtual fields”, DOI [10.1111/str.70031](https://doi.org/10.1111/str.70031) | 含噪体积场/超弹性 | vSBVF/aSBVF | 是 | 是 | 未报告 | 未报告 | 可能 | 是 | 官方页 | 后续方法升级 |
| VF23 | Nowak et al. 2026, “Full-field identification and test design for finite-strain polymer materials”, DOI [10.1016/j.compstruc.2026.108356](https://doi.org/10.1016/j.compstruc.2026.108356) | 聚氨酯黏合剂；T 形异质场 | FIM/全场逆识别 | 是 | 相关 | 未报告 | 可能 | 可能 | 是 | 官方页 | 异质激励必要性 |
| VF24 | “Stress-sensitivity VFM for time-dependent materials”, 2025, DOI [10.1007/s11043-025-09781-0](https://doi.org/10.1007/s11043-025-09781-0) | 聚合物/时间相关全场 | 黏弹参数 VFM | 是 | 是 | 未报告 | 是 | 未报告 | 是 | 官方页 | M3/M6 仅条件开放 |
| VF25 | Seidl et al. 2025, “A comparative study of calibration techniques for finite strain elastoplasticity: Numerically-exact sensitivities for FEMU and VFM” | 合成有限应变弹塑性；非对称缺口板 | FEMU/VFM；自动微分/前向与伴随灵敏度 | 是 | 是 | 否 | 未报告 | 否 | 是 | 全文+图像 | 真值回收、初值、噪声、模型误差、网格误差 |
| VF26 | Yan et al. 2025, “A Virtual Fields Method–Genetic Algorithm calibration framework for isotropic hyperelastic constitutive models” | 弹性泡沫；均匀/非均匀变形 | VFM-GA；稳定性过滤器 | 是 | 是 | 可能 | 否 | 否 | 是 | 全文+图像 | 多种群、噪声和独立验证 |
| VF27 | VFM 全场橡胶参数识别论文，“Identification of Constitutive Parameters Governing the Hyperelastic Response of Rubber by Using Full-field Measurement and the Virtual Fields Method” | 碳黑填充天然橡胶；异质双轴试验 | Mooney/Ogden；随机虚场/SBVF | 是 | 是 | 是 | 否 | 否 | 是 | 全文+图像 | 虚场独立性和 FE 力验证 |
| VF28 | “On discontinuities when computing the stress-field from the strain: a finite volume discretization” | 全场测量；不连续应变场 | 有限体积应力重构 | 是 | 相关 | 可能 | 可能 | 可扩展 | 部分 | 全文+图像 | 边界/断裂邻域不稳定性 |
| VF29 | Rethore 2010, “A fully integrated noise robust strategy for the identification of constitutive laws from digital images” | 全场图像；历史依赖材料 | 图像到本构的噪声鲁棒识别 | 是 | 相关 | 未报告 | 可能 | 可扩展 | 是 | 本地引用 | 数据处理对照；原始 DOI 待核 |
| VF30 | Florentin & Lubineau 2010, “Identification of the parameters of an elastic material model using the constitutive equation gap method”, DOI [10.1007/s00466-010-0496-y](https://doi.org/10.1007/s00466-010-0496-y) | 弹性材料；全场 | Constitutive equation gap | 是 | 否 | 可能 | 否 | 可扩展 | 是 | 官方页 | VFM 的独立方法对照 |
| VF31 | Florentin & Lubineau 2011, “Using constitutive equation gap method for identification of elastic material parameters: Technical insights and illustrations”, DOI [10.1007/s12008-011-0129-5](https://doi.org/10.1007/s12008-011-0129-5) | 弹性材料；场量识别 | Gap method | 是 | 否 | 可能 | 否 | 可扩展 | 是 | 官方页 | 逆识别方法对照 |
| VF33 | Cameron & Tasan 2021, “Full-field stress computation from measured deformation fields: A hyperbolic formulation”, DOI [10.1016/j.jmps.2020.104186](https://doi.org/10.1016/j.jmps.2020.104186) | 金属/全场 | 应力场重构 | 是 | 否 | 未报告 | 可能 | 可扩展 | 部分 | 官方页 | 不把应变直接当应力 |
| VF34 | Liu 2021, “Nonuniform Stress Field Determination Based on Deformation Measurement”, DOI [10.1115/1.4050535](https://doi.org/10.1115/1.4050535) | 非均匀变形场 | 应力场确定 | 是 | 否 | 可能 | 可能 | 可扩展 | 部分 | 官方页 | 场量边界审查 |
| VF35 | Langlois, Coret & Réthoré 2022, “Non-parametric stress field estimation for history-dependent materials”, DOI [10.1111/str.12410](https://doi.org/10.1111/str.12410) | 延性金属；局部化带 | 非参数应力场 | 是 | 否 | 未报告 | 可能 | 未报告 | 部分 | 官方页 | 局部化时避免误识别 |
| VF36 | Fletcher et al. 2021, “High strain rate elasto-plasticity identification using the image-based inertial impact test part 1: Error quantification”, DOI [10.1111/str.12375](https://doi.org/10.1111/str.12375) | 高速冲击；弹塑性 | IBII/误差量化 | 是 | 相关 | 未报告 | 是 | 可能 | 是 | 官方页 | 速率扩展而非首篇主线 |
| VF37 | Avril et al. 2007, “Overview of the identification methods of mechanical parameters based on full-field measurements”, DOI [10.1016/j.ijsolstr.2006.12.018](https://doi.org/10.1016/j.ijsolstr.2006.12.018) | 全场测量综述 | VFM/FEMU/反演 | 是 | 是 | 视案例 | 视案例 | 视案例 | 是 | 官方页 | 方法谱系 |
| VF38 | Grama, Subramanian & Pierron 2015, “Parameter identification of an Anand viscoplastic model using the virtual fields method”, DOI [10.1016/j.actamat.2014.11.052](https://doi.org/10.1016/j.actamat.2014.11.052) | 金属；宽应变/速率场 | Anand 黏塑性 VFM | 是 | 是 | 否 | 是 | 否 | 是 | 官方页 | 参数激活和相关性 |
| VF39 | Wang et al. 2012, “Identification of mechanical properties of PVC foams using the virtual fields method”, DOI [10.1007/s11340-012-9703-4](https://doi.org/10.1007/s11340-012-9703-4) | PVC 泡沫；全场 | VFM 弹性参数 | 是 | 是 | 可能 | 否 | 可能 | 部分 | 官方页 | 聚合物场量经验 |
| VF40 | Pierron & Grédiac 2012, “The Virtual Fields Method: Extracting Constitutive Mechanical Parameters from Full-Field Deformation Measurements” | 多类材料/方法专著 | VFM/虚场/非线性扩展 | 是 | 是 | 视案例 | 视案例 | 可扩展 | 是 | 本地引用 | 理论参考，不计论文数 |

## D. 检索与证据计数

| 分类 | 数量 | 可以说什么 | 不能说什么 |
|---|---:|---|---|
| 项目内部全文 P00 | 1 | 已有资料明确覆盖 PA12 十字形、DIC、XY/XZ、单轴/等双轴和三档速率 | 不能替代同行评审证据 |
| 同行评审全文+图像 | 9 | PA22–PA25、BX16、VF25–VF28 已实际读取正文/图注或图表 | 不能把不同材料或不同工艺批次的参数/模型移植到当前 PA12 |
| 官方页（未完成正文/图像） | 39 | 作者/题名/期刊/DOI 入口或摘要级信息已核对，可支撑方向性判断 | 不等于正文和图像已经逐篇审计 |
| 本地引用题录 | 34 | 有真实本地来源线索，可排入待全文核查队列 | 不能支撑精确数值、方法细节或“首次” |
| 元数据/题录待补证 | 1 | VF18 的原登记 DOI 未通过 Crossref/OpenAlex 元数据核验；相关官方记录见字段审计附录 | 不得把该 DOI 或相近题名直接当作同一篇期刊论文 |
| 最终可用于投稿参考文献 | 0（当前审计阶段） | 需完成全文、图像/图注、版本、DOI 和与正文论断逐条绑定 | 不提前生成投稿版参考文献表 |

## E. 字段状态审计（2026-09-17）

本轮对本注册表的 84 个唯一 ID 做了记录级字段盘点，覆盖目标 `≥50`。这里的“状态清楚”指每条记录都明确标出证据等级和字段是否为 `是/否/未报告/可能/视案例`；它不把未报告字段升级为已证实事实。

### E.1 记录级状态映射

| 本表原状态 | 统一审计状态 | 数量 | 含义 |
|---|---|---:|---|
| `全文+图像`、`官方全文+图像` | 已核验 | 10 | 正文、图注或图表已实际读取；其中 P00 是项目内部全文，同行评审条目为 9 篇 |
| `官方页` | 摘要核验 | 39 | 官方期刊/出版社/DOI 页面已核对；未完成本项目登记所需的正文与图像审计 |
| `本地引用` | 仅线索 | 34 | 有本地题录或引用位置，但没有在本轮取得可直接复核的外部来源页 |
| `缺失/待补证` | 缺失 | 1 | VF18 原登记 DOI 元数据核验失败，暂不作为可引用的有效来源 |

### E.2 目标字段盘点

| 字段 | 当前覆盖/状态 | 仍缺失或不能据此声称 |
|---|---|---|
| 作者、年份、题名 | 80/84 行显式给出作者与年份；BX14、VF24、VF27、VF28 仍缺作者或年份；PA17 的题名待官方页复核 | 题名占位或作者缺失的记录不能进入投稿参考文献表 |
| 材料、实验 | 84/84 行有登记值 | 只有“已核验”子集的正文/图像证据可支撑实验细节；其余仍按摘要级或线索级使用 |
| 本构/模型、识别方法 | 84/84 行有登记值；可辨识性为“是”27、“部分”21、“未报告”30、“未重点报告”6 | “未报告/部分”不能写成已完成参数可辨识性验证 |
| DIC | 是 48；否 1；非核心 3；辅助 1；相关 1；全场 1；未报告 29 | 29 条未报告，不能当作无 DIC；但也不能当作使用了 DIC |
| VFM | 是 28；相关 5；否 51 | 相关不等于 VFM 识别已完成 |
| 双轴 | 是 24；组合 1；可能 14；视案例 7；未报告 10；否 28 | 只有 24 条明确写“是”；不能把可能/视案例并入双轴先例计数 |
| 速率 | 是 11；否 13；可能 9；视案例 5；间接 1；未报告 45 | 速率字段是当前最大未报告项之一，不能据此比较材料速率规律 |
| 各向异性 | 是 26；否 8；可能 20；可扩展 10；视案例 3；近似各向同性 1；未重点报告 1；未报告 15 | 可能/可扩展/视案例不是当前材料的已证实各向异性 |
| 主要创新、局限 | `LITERATURE_MAP.md` 核心矩阵规范化 15/84 行；数据库其余 69 行没有独立的创新/局限字段 | 不能把 15 条核心矩阵的判断外推为 84 篇逐篇创新审计 |
| 与本项目关系 | 84/84 行有“本项目用途” | 用途字段是项目决策，不是论文原文结论 |
| 真实来源链接 | 题录行有直接 URL 42/84；其中 41 个 DOI 通过元数据核验，VF18 失败；42/84 行没有直接外部链接 | 本地引用和项目内部全文仍需补作者/出版社/DOI 或机构全文入口 |

无直接外部链接的 ID：`P00, PA01–PA15, PA17, PA20–PA21, BX01–BX02, BX04, BX06–BX09, VF02–VF03, VF05–VF07, VF09, VF11, VF25–VF29, VF40`。其中 VF25–VF28 有本地正文解析记录，但尚未在题录行补入可追溯外部来源链接。

### E.3 元数据纠正与证据边界

- VF18 的 DOI `10.1016/j.ijsolstr.2023.112303` 在本轮 Crossref/OpenAlex 校验中未找到匹配元数据；已保留原登记值作为待补证线索，不把它替换成相近题名的另一条记录。可核对的相关官方记录是 [TechScience ICCES 页面](https://www.techscience.com/icces/v26n2/53906)，其 DOI 为 `10.32604/icces.2023.08949`，不能据此自动修复原 IJSS 题录。
- 本轮没有新增 PDF 或正文图像读取，因此 `LITERATURE_BODY_IMAGE_EVIDENCE.md` 仍只支持 PA22–PA25 四条公开全文记录；`MINERU_BODY_IMAGE_EVIDENCE.md` 仍是项目内部解析和四条同行评审本地全文的独立证据页。
- “已核验”不等于材料参数可移植，也不等于全文所有实验事实、图表数值和原始数据可获得；正式写作仍须把具体论断绑定到正文/图注和真实来源。

## 交叉结论

1. PA12/SLS 的方向性、速率、松弛、黏塑和损伤已有公开研究；不能把 M3–M7 当成从零提出。
2. VFM、SBVF、FEMU 对照、双轴 DIC、加载路径设计和参数可辨识性已有公开先例；不能把“使用 VFM”本身作为创新。
3. 可以继续验证的窄缺口仍是：同一工艺/批次/方向 PA12 中，整体曲线与 DIC 全场 + 边界力是否激活不同参数，双轴场量的信息增益是否转化为完全留出路径的整体与全场预测增益。
4. 本注册表达到“候选条目 50+”，但没有达到“50+ 篇逐篇全文+图像完成”。后者必须继续补证，且不允许用题录行数替代。

## 下一步补证顺序

1. 优先补 PA17–PA19、PA26–PA27 的全文和图像，确认 SLS PA12 的方向/速率/历史依赖证据；PA22–PA25 已登记公开全文证据；
2. 补 VF17–VF24、BX05、BX12、BX15–BX17，重点抽取加载比例、边界力、虚场构造、噪声、FIM/条件数和独立验证图；
3. 为每篇全文创建 `body_image_evidence` 条目，并把正文论断与论文中的图表编号绑定；
4. 最终投稿参考文献只从 `全文+图像` 或经过逐篇官方全文复核的条目生成。
