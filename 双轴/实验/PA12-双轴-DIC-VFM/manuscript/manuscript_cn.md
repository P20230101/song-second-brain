---
title: "PA12单/双轴拉伸中的图像—载荷时序可追溯性审计"
article_type: "实验力学测量方法研究论文工作稿"
target_journal_primary: "实验力学（需最终核对模板）"
target_journal_conditional: "兵工学报（仅在真实兵工/军民两用应用背景与保密审查成立时）"
status: "pre-submission draft; XY data-audit results included; VFM identification not yet eligible"
evidence_registry: "sources/source_manifest.json; sources/claims.csv"
---

# PA12单/双轴拉伸中的图像—载荷时序可追溯性审计

**作者：** [待补：全部作者姓名、单位、邮箱、ORCID]

**基金：** [待补：基金名称与编号；无则删除]

## 摘要（当前结果稿，投稿前仍需补齐元数据与 VFM 条件）

针对 PA12 单/双轴试验中图像帧与多通道载荷记录难以独立复核的问题，本文建立并应用一套面向 MatchID 2019 二维数字图像相关（two-dimensional digital image correlation，2D-DIC）数据的图像—载荷时序审计流程。流程以文件级试验编号为主键，读取 X 单轴、Y 单轴和 XY 双轴图像序列、`Press`/`Pos` 记录及 MatchID 工程输出，使用力侧起载候选与力记录末样本构造端点线性时间映射，并将该映射与独立同步证据严格区分。当前数据覆盖 10 组 XY 图像序列和 5309 张 JPG；估计图像频率为 7.98–375.66 Hz，力记录有效频率为 997.50–1000.00 Hz。针对图像与 MatchID 输入帧数差异，本文保留不一致项而不删除，并对一组图像、DIC 输入均完整且末端破坏证据明确的双轴序列开展假设的 ±1、±2 和 ±5 帧时间扰动分析。结果表明，平稳峰值附近的单通道载荷差约为 1 N 量级，而峰后骤降候选处的 ±1 帧情景可产生约 1.59 kN 的单通道载荷差。由于当前文件未提供共同相机—DAQ 触发号或可核验的逐帧相机时间戳，所有序列的 VFM 准入标志均为 `False`；本文不报告未经准入的本构参数或独立验证误差。研究结果给出了一条可复算的测量链审计基线，并明确了从文件级配对进入 2D-DIC—VFM 识别所需补齐的最小证据。[claim:C010] [claim:C011] [claim:C012] [claim:C013] [claim:C014] [claim:C015] [evidence:E019, E020, E021, E022, E023]

**关键词：** PA12；单/双轴拉伸；二维数字图像相关；图像—载荷配对；时序敏感性

> **数据状态声明：** 当前工作区已找到并解析 `D:\C盘迁移\Desktop\yuan\data\XY` 下的 10 组 XY 图像序列、与其对应的 `Press`/`Pos` Excel 记录、MatchID 2D 工程/逐帧结果及配对审计文件。尚缺或尚未核验的内容包括材料与试样元数据、相机/标定/DIC 参数、共同相机—DAQ 触发或逐帧时间戳、可直接用于 VFM 的带单位全场导出、边界牵引定义和独立验证集。因此当前版本可报告文件级测量链结果，但不能把 VFM 参数识别写成已完成结果。[claim:C006] [evidence:E017]

## 1 引言

选择性激光烧结（selective laser sintering，SLS）PA12 具有较好的成形自由度和工程应用潜力，但其力学响应受到打印取向、零件厚度、粉末与成形工艺以及层间结构的共同影响。已有研究表明，SLS PA12 的拉伸性能会随构建方向和零件厚度变化，且塑性区性能通常比弹性区更容易表现出方向差异。[E007,E016] [claim:C001] [evidence:E007, E016] 因而，某一牌号、某一批次和某一成形方向得到的单轴参数不能不加区分地作为所有 PA12 构件的多轴本构参数。

双轴拉伸试验可以在两个正交方向施加可控载荷，为屈服、失效和本构模型在组合应力状态下的检验提供实验基础。然而，十字形试样的几何轮廓、中心减薄、狭缝、圆角和夹持边界会影响载荷传递、中心区均匀性和非目标区域的局部化。近期十字形试样研究将均匀变形、高应变水平和本构识别作为设计目标，并通过有限元和 DIC 进行验证；这说明“双轴设备能够同时加载”并不等价于“中心区已经获得有效材料响应”。[E006,E013,E014] [claim:C005] [evidence:E006, E013, E014]

全场 DIC 为双轴试验提供了整体力—位移曲线之外的位移和应变场，可用于识别变形集中、检查中心区有效性并比较不同模型对局部响应的解释能力。聚合物双轴试验研究已经显示，不同横向变形条件会改变局部化行为，测得的全场数据可用于检验本构模型。[E005] 但 2D-DIC 只在平面假设成立且面外运动可忽略时才具有直接的几何解释；面外平移或转动、镜头畸变、散斑质量和参数设置可能将系统误差传递到后续应变和参数识别中。[E003,E008,E009,E010] [claim:C003] [evidence:E003, E008]

VFM 基于虚功原理，将全场运动学测量与边界载荷结合起来反演本构参数；其优势是可以在一次异质试验中利用多个虚场约束材料参数，而不必对每个候选参数反复运行完整有限元正问题。[E001,E002,E011] [claim:C002] [evidence:E001, E002, E011] 但 VFM 的结果不是一个只由优化器决定的数字。双轴边界力的分布假设、场量有效区域、边缘缺失、同步误差、DIC 噪声、虚场独立性和拟合集/验证集划分，都会影响识别结果。已有双轴 VFM 研究专门考察了边缘缺失和 DIC 噪声对参数识别的影响。[E004] 如果只展示同一批数据上的拟合曲线，不能据此证明参数具有跨路径预测能力。

现有研究在 PA12 工艺各向异性、十字形试样设计、DIC 测量误差和 VFM 反演方面分别积累了方法，但当前项目资料首先需要解决的是文件级可追溯性和时间对应问题。本文将研究问题收敛为：

1. 现有 PA12 单/双轴图像、力/位移和 MatchID 文件能否按试验编号形成可复核的帧—载荷数据链？
2. 在缺少共同触发或逐帧时间戳时，端点线性映射的假设时间扰动会对峰值和峰后载荷事件造成多大影响？
3. 当前 2D-DIC 导出是否已经满足 VFM 所需的全场、单位、边界和独立验证条件？

本文的贡献限定为四项：

（1）对 X、Y 单轴及 XY 双轴共 10 组序列、5309 张 JPG、力学工作表和 MatchID 相关文件建立统一的文件级配对表；

（2）把力侧起载候选、力记录末样本、图像帧号和四通道载荷的映射规则写成可复算接口，并明确其不是硬件同步；

（3）在资料最完整的一组双轴序列上，量化假设帧登记扰动对平稳峰值和峰后骤降载荷的影响；

（4）以明确的 VFM 准入闸门区分“已有文件级结果”和“尚不能报告的本构参数/独立验证”。

本文不将图像序列数当作独立试样数，不预先给出 PA12 材料常数，也不把端点时间映射当作同步真值。材料/几何、相机与标定、共同触发、全场导出和独立试样信息补齐后，本文结果可继续升级为完整的 2D-DIC—VFM 本构识别论文。

## 2 理论基础与研究设计

### 2.1 十字形试样的评价目标

设候选试样几何参数为

\[
g=(h_c,N_s,l_s,r_f,s_s,w_a,\ldots),
\]

其中 \(h_c\) 为中心区厚度，\(N_s\) 为每个加载臂的狭缝数量，\(l_s\) 为狭缝长度，\(r_f\) 为圆角半径，\(s_s\) 为狭缝间距，\(w_a\) 为加载臂宽度。有限元筛选不只比较中心区峰值应力，还应输出：

1. 中心 gauge region 内主应变和应力的均匀性；
2. 中心区与臂根、圆角、狭缝端部的局部化比值；
3. X向、Y向及等双轴加载下的变形模式；
4. 主要失效位置是否落入预定义测量区；
5. 网格、边界、材料模型和参数来源。

本地学习基线报告的中心区厚度 1 mm、每臂 7 条狭缝、狭缝长度 40 mm、圆角半径 3 mm 和间距 0.2 mm，只能作为候选初值，不能直接变成本项目最终试样参数。最终参数要同时满足 PA12 实际厚度、设备夹具、加工/打印分辨率和安全边界。

### 2.2 2D-DIC 测量链

2D-DIC 的输入是参考图像和变形图像，输出为面内位移场 \(u(x,y,t)\)、\(v(x,y,t)\)，并可进一步得到应变场。本文把 DIC 结果视为带有测量误差的场量，而不是无误差真值。每一批分析至少保存以下字段：

```text
frame_id, t_image, x, y, u, v,
exx, eyy, exy（如由 MatchID 导出）, correlation_quality,
valid_mask, roi_id, dic_run_id
```

硬件与算法元数据至少包括相机和镜头型号、图像尺寸、视场、像素尺度、帧率、曝光、照明、散斑特征尺寸、平面标定方式、MatchID 版本、subset、step、形函数、插值、匹配准则、应变窗口和滤波设置。该记录结构遵循 iDICs 对 DIC 硬件和处理参数可复现报告的要求。[E009,E010,E018] [claim:C009] [evidence:E009, E010, E018]

![图1 可追溯单/双轴测量链示意图](figures/Fig1_traceable_measurement_chain.png)

**图1** 可追溯单/双轴测量链示意图。该图为方法流程示意，不包含本项目的实验数值；正式投稿时应将其作为独立高分辨率图件提交，并根据实际设备、通道和软件名称复核图中标签。

**Figure 1.** Traceable uniaxial and biaxial measurement chain. This methodological workflow schematic contains no project-specific experimental values.

在正式加载前，进行静止图像噪声底、面内刚体移动和面外运动风险评估。若刚体图像中出现不能由噪声解释的应变，或面外运动明显改变图像尺度，则不能直接把该批场量送入 VFM；应先修正相机布置、标定、散斑或测量维度。

### 2.3 帧—力/位移时间映射

对每个触发事件记录图像帧号 \(k_i\) 和机器时间 \(t_{m,i}\)。在采样区间内若线性时钟映射得到充分证据，可拟合

\[
t_m(k)=a+bk,
\]

并为每个 DIC 帧保存映射时间和同步残差

\[
e_i=t_{m,i}^{\mathrm{mapped}}-t_{m,i}^{\mathrm{observed}}.
\]

如果触发记录显示非线性漂移，不能继续使用单一线性关系；应重新定义映射并保留原始时间戳、插值区间、掉帧和重复触发记录。相机与数据采集系统的标称频率相同，也不能替代帧—采样映射验证。

本项目当前没有共同相机—DAQ 触发号或可核验的逐帧相机时间戳，因此采用文件级端点映射作为审计估计，而不是同步真值。具体实现以 `Press` 表前 50 个样本估计基线，使用 `max(10×MAD, 5 N)` 作为力侧偏离阈值，并要求连续 3 个样本超过阈值以确定起载候选；首张照片锚定该候选时刻，末张照片锚定 `Press.T` 的末样本，中间帧按线性插值取得 `t_image_est` 和四通道力/位移。若未检出独立起载（如 Y-11），则保留预载起点状态。该规则对应 `endpoint_linear_force_onset_to_force_record_end`，不产生可用于验证的同步残差。[claim:C012] [evidence:E020, E021]

### 2.4 VFM 识别方程

在准静态、平面应力假设成立时，对时刻 \(t_k\) 和任意满足运动学约束的虚场 \(\mathbf u^*\)，定义虚功残差

\[
r_k(\boldsymbol\theta)=
\int_{V}\boldsymbol\sigma(\boldsymbol\varepsilon(\mathbf x,t_k);\boldsymbol\theta):
\boldsymbol\varepsilon^*(\mathbf x)\,\mathrm dV
-\int_{\partial V}\bar{\mathbf t}\cdot\mathbf u^*\,\mathrm dA.
\]

其中 \(\boldsymbol\theta\) 是待识别参数，\(\bar{\mathbf t}\) 是由四通道边界力和受力区域定义得到的边界牵引。若机器只输出边界合力而没有牵引分布，必须显式记录由合力换算牵引的假设、受力宽度和厚度。不能把合力自动当作边界上每一点的局部应力。[E001,E002,E011] [claim:C002] [evidence:E001, E002, E011]

第一阶段使用 L0 线弹性基线检查单位、坐标、符号、厚度、边界项、虚场和积分实现。若实验历史显示明显屈服、卸载滞回、速率依赖或打印取向相关的各向异性，再依证据升级到有限应变弹塑性、黏弹性或正交各向异性模型。不能因为 VFM 具有非线性求解能力，就在数据尚未支持时指定复杂模型。

拟合集的加权目标函数可写为

\[
\hat{\boldsymbol\theta}=
\arg\min_{\boldsymbol\theta}\sum_{k\in\mathcal F}\sum_{q\in\mathcal Q}
w_{kq}r_{kq}^{2}(\boldsymbol\theta),
\]

其中 \(\mathcal F\) 为预先定义的拟合帧集合，\(\mathcal Q\) 为虚场集合，权重由测量不确定度或预设的尺度规则给出。分析必须保存初值、参数边界、优化器、拟合帧、虚场、ROI、权重和运行版本。

### 2.5 验证与敏感性

参数识别和验证分离执行。验证可采用未参与拟合的加载路径、独立试样、保留的卸载/保持段（仅当模型适用）或预先锁定的不同 ROI。验证时不重新调整参数，否则仍然属于拟合。

至少比较以下分析版本：

- 同步基线与受控提前/延后映射；
- 完整 ROI 与边缘掩膜 ROI；
- 预先定义的 subset、step 和应变窗口组合；
- 仅整体力—位移的基线；
- DIC 全场 VFM；
- 未参与拟合的加载路径或独立试样。

当前数据阶段只执行到文件级载荷历史和时间扰动分析：10 组 XY 序列全部标记为 `vfm_eligible=false`，因此本文不把下述 VFM 比较项写成已完成结果。

边缘缺失和 DIC 噪声可能影响双轴 VFM 参数识别，因此敏感性结果必须同时报告虚功残差、整体响应预测误差、场量空间残差、参数变化区间和试样间差异。[E004,E011] [claim:C004] [evidence:E004, E011]

## 3 材料与实验方法

> 本章中的方括号字段必须根据实际记录填入；没有记录的内容保持“待补”，不得使用文献或设备海报代填。

### 3.1 材料与试样

材料牌号：`[待补]`；成形工艺：`[待补：SLS/其他]`；设备型号：`[待补]`；粉末或材料批次：`[待补]`；含水状态与干燥过程：`[待补]`；打印/加工方向定义：`[待补]`；后处理：`[待补]`。

十字形试样 CAD 版本：`[待补]`；中心区厚度：`[待补]`；臂宽与长度：`[待补]`；狭缝数量/长度/间距：`[待补]`；圆角半径：`[待补]`；实际测得尺寸及公差：`[待补]`。候选几何通过有限元版本 `[待补]` 和加载边界 `[待补]` 筛选。

若研究比较 XY 与 XZ，必须给出打印坐标、拉伸方向和层面关系图，不能只写方向缩写。若实际材料不是 SLS，删除所有层间结合和打印取向推断。

### 3.2 双轴加载系统

设备品牌/型号：`[待补]`；加载通道数量：`[待补]`；控制量：`[待补：力/位移/混合]`；四个力传感器量程及校准信息：`[待补]`；行程及限位：`[待补]`；控制器采样频率：`[待补]`；实际试验速率：`[待补]`；触发信号：`[待补]`。

正式试验前进行无试样夹具运动、通道零点和通道平衡检查。加载路径记录为：`[待补：X单轴、Y单轴、等双轴及其他应力比]`。每条路径的控制命令、终止条件、力/位移符号和异常处理写入运行清单。

### 3.3 散斑、相机与 MatchID 2019

散斑制备：`[待补：底漆、喷点、特征尺寸]`；相机：`[待补]`；镜头：`[待补]`；图像尺寸：`[待补]`；视场：`[待补]`；像素尺度：`[待补]`；帧率：`[待补]`；曝光：`[待补]`；光源：`[待补]`；同步方式：`[待补]`。

当前工程和逐帧结果可确认使用 MatchID 2D-Version 19.2.0.0（属于 MatchID 2019 路线）；subset、step、形函数、匹配准则、插值、应变窗口、滤波、相机型号和标定记录仍待从工程设置中逐项核验。静止图像噪声底和刚体检验结果存放于 `[待补路径]`。

### 3.4 数据处理

原始数据不改写。机器数据、原始图像、MatchID 工程、导出场量、同步记录、分析配置和结果图按试样编号关联。每次改变 ROI、掩膜、DIC 参数、时间映射或本构模型，生成新的 `run_manifest`，并保留输入文件与输出文件关系。

当前文件级处理读取 `D:\C盘迁移\Desktop\yuan\data\XY` 下 10 个图像序列和对应的 `Press`/`Pos` 工作表，生成 `results/审计/xy_photo_force_sync.csv` 和 `results/01_VFM照片力对应.csv`。每张 JPG 均获得一个端点映射时间和插入力值，但由于没有共同触发/相机时间戳，该时间只能写作 `t_image_s_est`。当前 `Serie;X;Y` 导出和逐帧 `.dat` 结果已保留；在确认其完整字段、单位、质量指标和有效掩膜之前，不把它们直接送入 VFM。坐标转换、厚度和边界受力区域仍待补齐。

## 4 结果：XY 文件级测量链审计

本节结果由原始 XY 图像、`Press`/`Pos` 工作表、MatchID 文件和审计脚本生成。数值描述的是文件和记录层面的事实；端点图像时间和事件帧是估计/候选值，不是共同触发验证结果。

### 4.1 设备、标定与同步

当前可确认的文件级结果是：10 组 XY 序列共有 5309 张 JPG；每组均有对应力学工作簿并可读取 `Press`、`Pos` 表；力侧标称采样频率为 1000 Hz，按 `Press.T` 首末样本计算的有效频率范围为 997.50–1000.00 Hz。端点映射得到的图像频率估计为 7.98–375.66 Hz。各序列的 MatchID 输入计数与 JPG 总数不完全一致；其中 `XY_XY-0.1-02` 的 `Job.m2inp` 已核实为 1 个参考帧加 258 个变形帧，另一个 `DIC-xy_0.2` 目录只有 133 个逐点 CSV，缺少与原图的导出帧清单，因此该序列的 VFM 空间/时间覆盖仍标记为阻断。当前没有可核验的共同相机—DAQ 触发号或逐帧相机时间戳，不能从端点映射残差推出同步精度。[claim:C010] [claim:C011] [claim:C012] [claim:C014] [claim:C015] [evidence:E019, E020, E021, E022]

**表 1 设备、采集和试样元数据（待补）**

**Table 1.** Equipment, acquisition and specimen metadata (to be completed from the original records).

| 类别 | 字段 | 数值/状态 | 来源 |
|---|---|---|---|
| 设备 | 品牌与型号 | 待补 | 说明书/铭牌 |
| 载荷 | 每通道量程与校准日期 | 待补 | 校准记录 |
| 采集 | 力记录标称频率；有效频率范围 | 1000 Hz；997.50–1000.00 Hz | `Press.T` |
| 图像 | JPG 序列数；总帧数 | 10 组；5309 张 | XY 图像目录 |
| 图像 | 端点映射图像频率估计 | 7.98–375.66 Hz | `xy_frequency_summary.csv` |
| 相机 | 型号、图像尺寸、曝光、硬件时间戳 | 待补/未找到 | 相机设置/触发记录 |
| DIC | MatchID 版本 | 2D-Version 19.2.0.0 | 逐帧 `.dat` 头信息 |
| DIC | 输入帧覆盖 | MatchID 计数合计 5025；DIC CSV 唯一帧合计 5295 | XY 工程/导出 |
| 材料 | 牌号、批次、成形方式 | PA12；其余待补 | 材料/打印记录 |
| 试样 | 几何版本、厚度、公差、独立试样数 | 待补 | CAD/实测/试样记录 |
| 同步 | 共同触发/逐帧时间戳与同步残差 | 未找到；不具备硬件同步验证 | 文件清单 |

### 4.2 十字形试样中心区有效性

当前资料中未找到可核验的 CAD 几何版本、试样厚度/公差和有限元结果，因此不能对十字形中心区均匀性、臂根局部化或失效位置作定量结论。已有图像末端证据只能用于事件候选筛选，不能替代中心区有效性验证。后续补齐 CAD、实测几何和场量后，按预定义中心 ROI 输出几何示意与 FE—DIC 对照图。

### 4.3 DIC 测量质量

当前目录已确认存在 MatchID 2D 工程、13 个工程/结果关联文件和逐帧 `.dat`；但可直接核验的 `x,y,u,v,exx,eyy,exy` 全场表、单位、相关质量字段和有效掩膜尚未形成统一导出接口。现有 `Serie;X;Y` 表可作为点/线导出存在性的证据，不能单独作为全场应变质量报告。因而本文暂不报告静止噪声、刚体应变、无效点比例或面外误差数值，并将全部序列保持在 VFM 不准入状态。[claim:C016] [evidence:E019]

### 4.4 整体响应和场量演化

当前可以报告的是序列级绝对通道载荷历史和文件覆盖，不能报告材料应力—应变或独立试样统计。图 2 展示四通道力记录按端点映射投影到图像帧后的历史；单轴序列以主动方向两通道绝对力均值表示，双轴序列分别显示 X/Y 两方向通道均值。图中峰值标记是力侧峰值候选帧，不是经同步真值校准的峰值。[claim:C010] [claim:C014] [evidence:E019, E020, E021, E022]

![图2 XY 序列的逐帧载荷历史审计](../results/analysis/Fig2_force_history_audit.png)

**图2** XY 序列的逐帧载荷历史审计。横坐标为保存的 JPG 帧号；力值来自端点时间映射后的插值，当前不具备硬件触发验证。双轴序列的两条曲线为 X/Y 两方向通道绝对值均值。

**Figure 2.** Frame-wise load-history audit for the XY sequences. The force values are interpolated after endpoint time mapping; hardware-trigger verification is unavailable in the current records.

**表 2 XY 序列级覆盖与事件候选**

**Table 2.** Sequence-level coverage and candidate event frames for the XY tests.

| 序列 | 方向 | 速度 (mm/s) | JPG 帧数 | 力样本数 | 图像频率估计 (Hz) | MatchID 输入帧数 | 力峰值候选帧 | 图像末端候选 |
|---|---|---:|---:|---:|---:|---:|---:|---|
| X-05-0.1-01 | X | 0.2 | 165 | 14735 | 11.69 | 130 | 141 | 待核验 |
| X-06-1.0-01 | X | 2 | 133 | 2789 | 49.16 | 133 | 58 | 132 |
| X-07-10-01 | X | 20 | 81 | 402 | 227.92 | 81 | 28 | 待核验 |
| Xy-0.1-01 | XY | 0.2 | 289 | 36244 | 7.98 | 289 | 223 | 288 |
| XY-0.1-02 | XY | 0.2 | 259 | 27980 | 9.30 | 10 | 235 | 258（DIC 输入未覆盖） |
| Xy-03-10-01 | XY | 20 | 21 | 511 | 43.48 | 21 | 7 | 20 |
| Xy-04-1-01 | XY | 2 | 267 | 4570 | 58.81 | 267 | 142 | 250/266（待核验） |
| Y-09-0.1-02 | Y | 0.2 | 1825 | 179260 | 10.19 | 1825 | 1112 | 1824 |
| Y-10-1-01 | Y | 2 | 1558 | 15328 | 102.08 | 1558 | 888 | 1557（事件类型待核验） |
| Y-11-10-01 | Y | 20 | 711 | 1889 | 375.66 | 711 | 0（预载） | 710 |

表中 10 组是图像/文件序列数，不是独立试样数；试样编号、几何、材料批次和重复关系仍需由实验记录确认。图 3 给出加载起点、力峰值、峰后下降和图像末端候选在文件帧轴上的投影。

![图3 事件候选帧投影](../results/analysis/Fig4_event_frame_audit.png)

**图3** 事件候选帧投影。事件帧由端点时间映射得到或来自图像侧末端核对；所有标记均需人工复核，Y-11 序列从预载状态开始，未检出零载起点。

**Figure 3.** Projection of candidate event frames. The candidates are obtained from endpoint mapping or image-side end-frame checks and require manual review.

图 4 对图像采样估计和 MatchID 帧覆盖作可视化核对。

![图4 图像采样与 DIC 帧数一致性审计](../results/analysis/Fig3_frequency_frame_audit.png)

**图4** 图像采样与 DIC 帧数一致性审计。左图的圆点为端点估计频率，叉号为少数序列中可读取的名义相机设置；右图比较保存 JPG 与 MatchID 输入帧数。所有点均为序列级文件计数，不能推导相机时间戳或独立试样数。

**Figure 4.** Consistency audit of image sampling and DIC frame counts. All points are sequence-level file counts and do not establish camera timestamps or independent specimen counts.

### 4.5 VFM 基线识别

当前未执行可用于论文结论的 VFM 基线识别。原因不是优化器或计算资源，而是 10 组序列均没有经过共同时间基准验证，且尚未形成带单位的完整面内场量、有效掩膜、试样厚度、边界受力区域和合力到牵引的换算定义。因而本节不填本构参数、虚功残差或独立预测误差。

**表 3 VFM 识别配置与结果（待补）**

**Table 3.** VFM identification configuration and results (to be completed only after full-field DIC and boundary data are available).

| 项目 | 拟合设置 | 验证设置 | 结果 |
|---|---|---|---|
| 本构模型 | 未运行 | 未运行 | 不报告 |
| 拟合帧/路径 | 未定义 | 未定义 | 不报告 |
| ROI 与掩膜 | 全场导出接口未核验 | 未定义 | 不准入 |
| 虚场数量与形式 | 未定义 | 未定义 | 不报告 |
| 参数估计与区间 | 未运行 | 不重新调参 | 不报告 |
| 虚功残差 | 未运行 | 未运行 | 不报告 |

### 4.6 同步、ROI 与 DIC 参数敏感性

在 VFM 尚未准入的条件下，本文先对图像—载荷对应本身开展时间扰动敏感性分析。选择 `XY_Xy-0.1-01` 的依据是：该序列有 289 张 JPG、289 个 MatchID 输入帧、X/Y 两方向导出记录，且末端有明确的图像破坏候选。沿原始 `Press.T` 记录施加假设的 ±1、±2、±5 帧登记扰动，比较全序列和两个事件帧处的通道载荷差。[claim:C013] [evidence:E023]

**表 4 XY_Xy-0.1-01 假设时间扰动结果（非实测同步不确定度）**

**Table 4.** Hypothetical timing-perturbation results for XY_Xy-0.1-01 (not a measured synchronization uncertainty).

| 帧索引扰动 | 全序列最大通道载荷差 (N) | 全序列平均通道载荷差 (N) | 力峰值候选帧处差值 (N) | 峰后下降候选帧处差值 (N) |
|---:|---:|---:|---:|---:|
| -5 | 1595 | 55.1 | 5 | 1591 |
| -2 | 1594 | 22.1 | 2 | 1592.5 |
| -1 | 1592.5 | 11.1 | 1.5 | 1592.5 |
| 0 | 0 | 0 | 0 | 0 |
| +1 | 1592.5 | 11.1 | 0.5 | 1.5 |
| +2 | 1594 | 22.0 | 0.5 | 2 |
| +5 | 1595 | 54.5 | 1594 | 1.5 |

![图5 载荷—图像时间对应扰动敏感性](../results/analysis/Fig5_timing_sensitivity_Xy-0.1-01.png)

**图5** 载荷—图像时间对应扰动敏感性。左图以两方向通道绝对力均值的向量范数展示参考端点映射及 ±1 帧情景；右图汇总全序列最大差值、峰值候选处差值和峰后下降候选处差值。扰动是分析情景，不是同步置信区间；峰后骤降处的差异来自载荷记录的快速变化。

**Figure 5.** Sensitivity of load–image time registration to timing perturbation. The perturbation is an analysis scenario rather than a synchronization confidence interval.

### 4.7 独立路径验证

当前没有经过 VFM 拟合的参数、独立加载路径划分或可确认的独立试样编号，因此本节不声称完成验证。后续只有在同步、全场导出、试样独立性和边界条件定义完成后，才比较整体力—位移、中心场量和空间残差。

## 5 讨论

### 5.1 时间对应与事件载荷的区分

当前文件级审计显示，力记录的有效采样频率接近 1000 Hz，但图像序列的端点估计频率随加载速度和序列长度变化于 7.98–375.66 Hz。频率接近并不意味着时间零点和逐帧对应关系已验证。尤其在 `XY_Xy-0.1-01` 的峰后骤降处，±1 帧假设可把高载荷帧与低载荷帧互相错配，造成约 1.59 kN 的单通道差值。因此，图像事件帧不能仅由文件末帧或拟合曲线视觉重合确定。

### 5.2 文件完整性与 2D-DIC/VFM 准入

当前 MatchID 文件表明 2D-DIC 处理链存在，但 MatchID 输入计数、DIC CSV 唯一帧和 JPG 计数并非始终一致；`XY_XY-0.1-02` 是最明显的覆盖冲突。若在这种覆盖状态下直接做 VFM，时间和空间缺失会被混入材料参数。本文先保留冲突并将 `vfm_eligible` 设为 `False`，这是对结果可追溯性的限制，而不是对 PA12 本构行为的判断。

### 5.3 与已有研究的边界

本研究应将自身结果与文献的对象、成形方式、厚度、加载路径和 DIC 设置逐项比较。已有 SLS PA12 研究的取向/厚度趋势可用于提出解释，但不能直接替代本项目的材料批次数据。[E007,E016] 十字形试样和 VFM 文献可用于方法对照，但聚合物类型、边界和本构模型差异必须写明。[E004,E005,E006]

### 5.4 局限性

1. 2D-DIC 依赖平面假设；若缺少立体图像，面外运动只能通过风险评估和误差分析限制，而不能声称已被三维测量消除。
2. 如果边界只有四个合力，VFM 的牵引分布由换算假设决定；该假设需要通过夹具和 FE/实测证据约束。
3. PA12 的成形方式、粉末/材料批次、含水和厚度变化会限制结论外推。
4. 没有独立试样或独立加载路径时，不能声称模型已验证。
5. 当前已完成 XY 文件级审计，但材料/试样元数据、相机与标定参数、共同触发/逐帧时间戳、完整全场导出、边界牵引假设和独立验证仍未齐全；因此当前稿不能以 VFM 参数论文直接投稿。

## 6 结论（当前可确认版本）

本文建立并复算了一套面向 PA12 双轴拉伸的图像—载荷时序审计流程。当前 XY 文件级结果包括 10 组图像序列、5309 张 JPG、力记录有效频率 997.50–1000.00 Hz、端点映射图像频率估计 7.98–375.66 Hz，以及图像/MatchID 帧覆盖和事件候选表。对资料最完整的 `XY_Xy-0.1-01` 进行假设时间扰动后发现，±1 帧在平稳峰值附近只产生约 1 N 量级的通道载荷差，但在峰后骤降候选处可产生约 1.59 kN 的差值。

上述扰动是情景分析，不是同步精度或置信区间。由于当前没有共同相机—DAQ 触发号或逐帧相机时间戳，且完整带单位 DIC 场量、边界牵引定义和独立试样验证尚未齐全，所有当前序列的 VFM 准入标志保持为 `False`；本文不报告未经准入的 PA12 强度、模量或本构参数。补齐这些字段后，现有事实表和脚本可直接作为 2D-DIC—VFM 识别的输入审计基线。

## 数据可用性声明（待作者确认）

当前版本：`Data availability statement pending.` 正式投稿前需根据原始图像、机器数据、MatchID 工程文件、代码、材料权限和实验室政策，选择公开仓储、受限访问或无法共享的准确表述，并提供持久化链接（如适用）。

## 伦理、利益冲突、基金与 AI 使用声明（待作者确认）

- 保密审查：`[待补；若投《兵工学报》必须提供单位保密审查表]`。
- 利益冲突：`[待补；无则由全部作者确认后填写无]`。
- 基金：`[待补]`。
- 作者贡献：`[待补；依据 CRediT 并由全部作者确认]`。
- AI 使用：`[待补；按照目标期刊当前政策说明 AI 参与范围，作者对全部科学内容负责]`。

## 参考文献

参考文献条目及 DOI/题名程序化核验结果分别保存在 `sources/references.json` 和 `sources/reference_validation.json`。以下为工作稿参考文献表；正式提交前需依据目标期刊统一格式，并由作者逐条打开原文核对与正文 claim 的对应关系。当前正文中的 `[E###]` 仅为工作稿证据 ID，导出投稿文件前应转换为目标期刊的数字引文格式，同时保留 claim registry。

1. E001. Grédiac M, Pierron F, Avril S, Toussaint E. The Virtual Fields Method for Extracting Constitutive Parameters From Full-Field Measurements: a Review. *Strain*. 2006. doi:10.1111/j.1475-1305.2006.tb01504.x.
2. E002. Avril S, Pierron F. General framework for the identification of constitutive parameters from full-field measurements in linear elasticity. *International Journal of Solids and Structures*. 2007. doi:10.1016/j.ijsolstr.2006.12.018.
3. E003. Zhang Z, Pan B, Grédiac M, Song W. Accuracy-enhanced constitutive parameter identification using virtual fields method and special stereo-digital image correlation. *Optics and Lasers in Engineering*. 2018. doi:10.1016/j.optlaseng.2017.11.016.
4. E004. Jiang M, Wang Z, Freed AD, Moreno MR, Erel V, Dubrowski A. Extracting material parameters of silicone elastomers under biaxial tensile tests using virtual fields method and investigating the effect of missing deformation data close to specimen edges on parameter identification. *Mechanics of Advanced Materials and Structures*. 2021. doi:10.1080/15376494.2021.1979138.
5. E005. Engqvist J, Wallin M, Ristinmaa M, Hall SA. Modelling and experiments of glassy polymers using biaxial loading and digital image correlation. *International Journal of Solids and Structures*. 2016. doi:10.1016/j.ijsolstr.2016.10.013.
6. E006. Vitucci G. Biaxial Extension of Cruciform Specimens: Embedding Equilibrium Into Design and Constitutive Characterization. *Experimental Mechanics*. 2024. doi:10.1007/s11340-024-01052-2.
7. E007. Slager JJ, Earp BC, Ibrahim AM. Influence of Build Orientation and Part Thickness on Tensile Properties of Polyamide 12 Parts Manufactured by Selective Laser Sintering. *Polymers*. 2024. doi:10.3390/polym16162241.
8. E008. Sutton MA, Yan JH, Tiwari V, Schreier HW, Orteu JJ. The effect of out-of-plane motion on 2D and 3D digital image correlation measurements. *Optics and Lasers in Engineering*. 2008. doi:10.1016/j.optlaseng.2008.05.005.
9. E009. Reu PL, Toussaint E, Jones E, et al. DIC Challenge: Developing Images and Guidelines for Evaluating Accuracy and Resolution of 2D Analyses. *Experimental Mechanics*. 2017. doi:10.1007/s11340-017-0349-0.
10. E010. International Digital Image Correlation Society, Bigger R, Blaysat B, et al. A Good Practices Guide for Digital Image Correlation. International Digital Image Correlation Society. 2018. doi:10.32720/idics/gpg.ed1.
11. E011. Wang P, Pierron F, Thomsen OT. Identification of Material Parameters of PVC Foams using Digital Image Correlation and the Virtual Fields Method. *Experimental Mechanics*. 2012. doi:10.1007/s11340-012-9703-4.
12. E012. Guélon T, Toussaint E, Le Cam JB, Promma N, Grédiac M. A new characterisation method for rubber. *Polymer Testing*. 2009. doi:10.1016/j.polymertesting.2009.06.001.
13. E013. Yang X, Wu ZR, Yang YR, Pan Y, Wang SQ, Lei H. Optimization Design of Cruciform Specimens for Biaxial Testing Based on Genetic Algorithm. *Journal of Materials Engineering and Performance*. 2022. doi:10.1007/s11665-022-07258-6.
14. E014. Hartmann S, Gilbert RR, Sguazzo C. Basic studies in biaxial tensile tests. *GAMM-Mitteilungen*. 2018. doi:10.1002/gamm.201800004.
15. E015. Arrington A, Westra A, Jannotti P, Reu P, Lamberson L. Review of High-Speed Digital Image Correlation: Advancements and Good Practices. *Strain*. 2025. doi:10.1111/str.70018.
16. E016. Slager JJ, Green JT, Levine SD, Gonzalez RV. The Influence of Print Orientation and Discontinuous Carbon Fiber Content on the Tensile Properties of Selective Laser-Sintered Polyamide 12. *Polymers*. 2025. doi:10.3390/polym17152028.
17. E018. International Digital Image Correlation Society, Jones EMC, Iadicola MA, eds. A Good Practices Guide for Digital Image Correlation, Edition 2. International Digital Image Correlation Society. 2025. doi:10.32720/idics/gpg.ed2.
