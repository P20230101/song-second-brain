# LITERATURE MAP｜PA12、双轴全场、VFM 与可辨识性

更新时间：2026-09-17。下表是研究路线审查用的证据矩阵，不是最终投稿参考文献表。正式写作前仍需逐篇核对全文、版本、页码和 DOI。

## 1. 检索边界

检索主题覆盖：`SLS PA12`、`MJF PA12`、`uniaxial PA12`、`biaxial PA12`、`rate-dependent PA12`、`viscoelastic PA12`、`viscoplastic PA12`、`anisotropic PA12`、`damage PA12`、`DIC PA12`、`biaxial cruciform specimen`、`Virtual Fields Method`、`nonlinear VFM`、`elastoplastic VFM`、`viscoplastic VFM`、`anisotropic VFM`、`Sensitivity-Based Virtual Fields`、`SBVF`、`FE-VFM`、`parameter identifiability`、`optimal experimental design`、`full-field inverse identification`。

证据优先级：出版社/期刊正式页面与 DOI > PubMed Central 或机构全文 > 学位论文/项目本地全文 > 搜索摘要。搜索摘要只能支持方向判断，不能单独支撑精确数值和“首次”表述。

## 2. 核心文献矩阵

| 作者/年份 | 材料与实验 | 本构/识别 | DIC | VFM | 双轴 | 速率 | 各向异性 | 可辨识性 | 主要贡献与局限 | 与本项目关系 |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| Grédiac, Pierron et al. 2006 | 金属/静态非均匀试验 | 弹塑性参数，VFM | 是 | 是 | 未作为本项目核心 | 否 | 可扩展 | 部分 | 建立弹塑性 VFM 和噪声敏感性；不是 PA12 | 方法基础 |
| Pannier et al. 2006 | 金属、静态不定试验 | 弹塑性 + Voce，VFM | 是 | 是 | 非本项目双轴主线 | 否 | 非核心 | 部分 | 实验验证和虚场设计；说明全场并不自动保证参数可辨识 | VFM 基线 |
| Grama, Subramanian & Pierron 2015 | 金属，宽应变/应变率场 | Anand 黏塑性 | 是 | 是 | 非本项目核心 | 是 | 非核心 | 是 | 参数必须被强烈激活，异质场本身不够；DOI: 10.1016/j.actamat.2014.11.052 | Gate 5–7 理论依据 |
| Sensitivity-based VFM 2020 | 非线性材料数值/实验案例 | SBVF | 是/输入全场 | 是 | 视案例 | 视案例 | 可扩展 | 是 | 用灵敏度虚场改善非线性识别；方法创新已存在 | 不能把 SBVF 本身作为首次 |
| Lammens et al. 2016 | SLS PA12，拉伸，打印方向 | 正交弹塑性/失效 | 是 | 否 | 否 | 有黏性贡献 | 是 | 未重点报告 | 弹性接近各向同性，塑性与失效体现方向性 | PA12 物理先验；不支持直接选 J2 |
| Lammens et al. 2017 | SLS PA12，拉/压/剪/松弛 | 黏弹塑、正交、非线性塑性 | 未作为核心 | 否 | 否 | 是 | 是 | 未重点报告 | 联合试验显示松弛和黏性贡献；复杂模型需要时间历史数据 | M3/M6 的准入依据 |
| Schneider & Kumar 2020 | SLS PA12，拉/压/弯/剪/断裂 | Three-Network，多试验标定 | 非核心 | 否 | 否 | 间接 | 方向差异 | 未重点报告 | 单轴模型研究已有深度；不能据此声称双轴识别空白 | 防止过度创新 |
| Kadkhodaei et al. 2024 | SLS PA12，单调/循环拉伸、松弛 | 超黏弹卷积模型 + FE | 非核心 | 否 | 否 | 是 | 未必 | 需要长短期数据 | 率/历史依赖和恢复会改变模型选择 | M6 只能条件性开放 |
| Effect of strain rates and heat exposure 2023 | SLS PA12，速率/热暴露 | 速率效应表征 | 有 DIC 相关 | 否 | 否 | 是 | 可能 | 未重点报告 | 证明速率效应可存在，但项目数据不能直接移植其参数 | M3 的物理动机 |
| Chen et al. 2021 | MJF PA12，多载荷/恢复 | 有限应变黏弹–黏塑–损伤 | 相关实验 | 否 | 组合载荷 | 是 | 可能 | 非本项目重点 | MJF 已有复杂路径模型；不能与 SLS 直接合并 | 限定材料工艺边界 |
| Jiang et al. 2022 | 双轴橡胶/非线性案例 | 多模型 VFM 比较 | 是 | 是 | 是/等双轴 | 非核心 | 非核心 | 是 | 双轴 VFM 模型判别和场量利用不是新概念 | M0–M2 判别设计参考 |
| Peshave et al. 2024 | 双轴超弹性案例 | 多模型与适配指标 | 是 | 是 | 是 | 非核心 | 非核心 | 部分 | 展示模型形式选择需要多路径；材料不同 | 反对只按单轴拟合选模 |
| Nguyen et al. 2025/2026 | PET 十字形双轴 | FEMU/VFM + 灵敏度 | 是 | 是 | 是 | 噪声分析 | 是 | 是 | 已有聚合物双轴 DIC 下 VFM/FEMU 可辨识性比较；DOI: 10.1002/pen.70150 | 直接否定宽泛方法空白 |
| Anisotropic plasticity identification 2025 | SUS316，多类试验 | Hill48/Swift、Yld2000-2d、FE/S-VFM | 是 | 是 | 平衡双轴进入代价函数 | 非核心 | 是 | 是 | 各向异性模型和 SBVF 已有新近方法；DOI: 10.1016/j.ijmecsci.2025.110815 | M4/M5 不能因“新”而默认 |
| Zhao et al. 2026 | SLS PA12，多轴棘轮 | 温度相关多轴路径模型 | 非项目 DIC–VFM 主线 | 否 | 多轴 | 温度/循环 | 构建方向 | 路径效应 | 已研究 SLS PA12 多轴棘轮、温度和非比例路径；DOI: 10.1111/ffe.70373 | 否定“PA12 多轴空白” |

## 3. 可核实来源

- [Lammens et al. 2016, UGent record](https://biblio.ugent.be/publication/8086754)
- [Lammens et al. 2017, Polymer Testing](https://www.sciencedirect.com/science/article/pii/S0142941816310315)
- [Schneider & Kumar 2020, Polymer Testing](https://www.sciencedirect.com/science/article/pii/S0142941819320860)
- [SLS PA12 hyper-viscoelasticity, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11285931/)
- [SLS PA12 strain-rate/heat exposure, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10342904/)
- [SLS PA12 shear-induced damage, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10780187/)
- [MJF PA12 viscoelastic-viscoplasticity](https://www.sciencedirect.com/science/article/pii/S0749641921001042)
- [Elasto-plastic VFM, 2006](https://www.sciencedirect.com/science/article/abs/pii/S0749641905000896)
- [Anand parameter identifiability with VFM](https://www.sciencedirect.com/science/article/pii/S1359645414009057)
- [Sensitivity-based VFM](https://pmc.ncbi.nlm.nih.gov/articles/PMC6961464/)
- [PET biaxial DIC–VFM/FEMU comparison](https://4spepublications.onlinelibrary.wiley.com/doi/10.1002/pen.70150)
- [Anisotropic plasticity FE/S-VFM](https://www.sciencedirect.com/science/article/pii/S0020740325008975)
- [SLS PA12 multiaxial ratchetting](https://onlinelibrary.wiley.com/doi/10.1111/ffe.70373)

## 4. 交叉验证后的缺口判断

已被排除的表述：

- “首次 PA12 DIC/VFM”；
- “首次 PA12 双轴/多轴”；
- “首次 VFM 可辨识性或模型判别”；
- “没有 PA12 速率、黏塑、各向异性或损伤模型”。

仍可作为候选、但置信度只有中等的组合缺口：

> 对明确工艺、批次和方向的 SLS PA12，使用可追溯的单轴/双轴 DIC 全场和边界力，直接比较整体力—位移标定与 VFM 在参数可辨识性、模型判别、测量误差传播和完全留出路径预测上的差异。

该判断要求后续继续核查 PA12 双轴全场识别的最新全文，并以“本轮检索未发现完整先例”替代“国际首次”。

## 5. 本轮补充的可执行方法证据（2026-09-17）

| 来源 | 直接证据 | 对本项目的固定决策 |
|---|---|---|
| Kim & Lee, 2021, DOI [10.1016/j.ijsolstr.2021.111204](https://doi.org/10.1016/j.ijsolstr.2021.111204) | FE-VFM 将实验全场位移映射到 FE 网格，用高斯积分计算内部虚功；塑性场下网格尺寸、单元阶次和积分阶次会显著影响识别，伪真实变形虚场可改善局部化区域的参数识别。 | `.dat` 不能直接把散点平均后送入 VFM；先统一坐标/单位/掩膜，再映射到可追溯的 FE 网格，并记录积分设置。 |
| Nguyen et al., 2025, DOI [10.1002/pen.70150](https://doi.org/10.1002/pen.70150) | 聚合物双轴 DIC 下已有 FEMU/VFM 与灵敏度比较；全场数据是否能辨识参数取决于模型与加载路径，不是“有 DIC 就能识别”。 | 真实 PA12 首轮必须同时报告曲线-only、单轴场和双轴场三种信息集，并留出整条路径验证。 |
| Bayesian full-field identification, 2025, DOI [10.1016/j.cma.2024.117489](https://doi.org/10.1016/j.cma.2024.117489) | FEMU-F 将全场位移和外力纳入反演，并用变分贝叶斯处理位移、参数和模型不确定性；可限制在监测子域以应对边界不完整。 | 同步误差、质量掩膜和边界不完整先作为不确定性/敏感性情景，不能用单个最优参数掩盖它们。 |
| Fayad et al., 2025, DOI [10.1111/str.70007](https://doi.org/10.1111/str.70007) | 双轴十字试样的加载路径会改变参数识别不确定性；用灵敏度矩阵构造 Fisher 信息矩阵，行列式作为 OED 判据，并以带噪 FE/DIC 数据验证。 | 在真实试验扩展前，先用 Abaqus 虚拟试验比较 1:0、1:0.25、1:0.5、1:0.75、1:1 等路径的 FIM/条件数；不先宣称某一比例最优。 |
| Yan et al., 2025, [arXiv:2510.07683](https://arxiv.org/abs/2510.07683) | VFM-GA 用 DIC 位移与力传感器同步数据构造目标函数，并在优化中剔除不稳定的本构参数集合；目前是预印本和超弹性泡沫案例。 | 可借鉴“稳定性筛选 + 优化器”结构，但不把预印本的算法精度或材料结论移植为 PA12 证据。 |
| Oliveira, [开源 Python VFM](https://github.com/migueljgoliveira/virtual-fields-method) | README 要求节点、单元、逐时刻位移、方向、厚度和力等输入，并提供识别/仿真两种模式。 | 首轮代码数据契约固定为 `nodes/elements/U(t)/thickness/force`；缺节点、厚度、边界合力或同步证据时只做审计/虚拟试验。 |
| Fully 3D VFM, 2025, DOI [10.1186/s40323-025-00293-7](https://doi.org/10.1186/s40323-025-00293-7) | 提供 Python 数组化的 3D VFM，用几何、位移场、载荷和本构方程识别硬化行为。 | 该路线证明代码化 VFM 可行，但本项目先完成平面内 2D 场的可复现闭环；只有真实立体场和标定齐备时才升级 3D。 |

### 交叉结论

1. **最先要解决的是数据契约，不是换软件。** 多篇方法论文都把全场位移、外力、几何/厚度和边界条件作为同时输入；当前 XY 的 `.dat` 入口已找到，但字段语义、有效掩膜和共同时间基准仍是准入闸门。
2. **可发表的最小贡献应是“可追溯误差影响 + 完全留出路径验证”。** 仅报告某一组参数拟合得很好，无法区分同步误差、DIC 质量和模型形式误差；需把这些情景逐项加入 Virtual Experiment。
3. **加载路径和模型形式必须联动比较。** FIM/OED 能提出候选路径，但它依赖当前模型和参数先验；因此先用 Abaqus 做候选路径排序，再用真实数据验证，不把通用比例当成结论。
