---
title: PA12｜Phase 12 Recovery：真实本构、VFM拟合与虚功同步
date: 2026-09-19
status: completed_for_manual_review
data_status: real_experimental_only
source_is_real: true
synthetic_used: false
ai_used_for_curves: false
single_axis_experiments: 5
biaxial_experiments: 3
---

# PA12｜Phase 12 Recovery：真实本构、VFM拟合与虚功同步

> [!warning] 本页是 Recovery 的历史快照，包含旧的 8 组 Phase 14 划分和旧数据库统计。当前权威结果请查看 [一级二级三级修复与 Phase 13/14 质量门](../../01_研究总控/03_质量门/PA12-一级二级三级修复与Phase13-14质量门-2026-09-19.md)。

## 结论

本次 Recovery 已完成真实数据链的重新整理、Phase 13 数据库复核、Phase 14 真实数据重训，以及真实单轴曲线、VFM 本构对比和内外虚功同步证据图生成。所有曲线直接来自真实 `formal_vfm_input.csv.gz`、真实 `Force.csv`、Phase 8–12 JSON 和 `PA12_database.h5`；没有用 synthetic 数据补帧、补力或补参数。

需要把“计算完成”和“材料参数已经可信”分开：Phase 12 文件已经重建并可追溯，但当前若干拟合出现参数触边、`nu≈0`、Phase 8 虚功残差较大或 Phase 12 参数退化到 `E≈1 MPa`。所以本页的图是 Recovery 的真实计算证据和问题定位材料，不把当前 Phase 12 参数宣称为最终 PA12 本构常数。

## 一、现在有哪些数据

### 1. 单轴数据（5组）

这些实验按主实验工况归类为单轴；`formal_vfm_input.csv.gz` 仍保留 `Fx`、`Fy` 两个同步力通道，次轴力只用于审计。

| experiment_id | 加载轴 | 可用DIC/力同步帧 | Phase 12状态 | 说明 |
|---|---|---:|---|---|
| `XY_X-06-1.0-01` | X | 133 | 已计算 | X轴单轴分支，加载支59帧 |
| `XY_X-07-10-01` | X | 80 | 已计算 | X轴单轴分支，加载支29帧 |
| `XY_Y-09-0.1-02` | Y | 1825 | 已计算 | Y轴单轴分支，加载支1118帧 |
| `XY_Y-10-1-01` | Y | 1558 | 已计算 | Y轴单轴分支，加载支890帧 |
| `XY_Y-11-10-01` | Y | 711 | 已计算 | Y轴单轴分支，加载支453帧；原始力值方向为负，报告图按加载正号展示 |

### 2. 双轴数据（3组）

这些实验保留 `Fx/Fy`、`exx/eyy/exy` 和二维 Phase 11 虚功结果，支持 `sigma_xx`、`sigma_yy`、`tau_xy` 的双轴 VFM 记录。

| experiment_id | 双轴可用帧 | Phase 11输出 | Phase 12状态 |
|---|---:|---|---|
| `XY_Xy-0.1-01` | 289 | X/Y内外虚功、三应力分量 | 已计算 |
| `XY_Xy-03-10-01` | 21 | X/Y内外虚功、三应力分量 | 已计算 |
| `XY_Xy-04-1-01` | 253 | X/Y内外虚功、三应力分量 | 已计算 |

数据库汇总为 8 个真实实验、4870 个同步帧；2 个候选实验仍未纳入：`XY_X-05-0.1-01` 缺正式 MatchID 应变/Force/VFM闭合，`XY_XY-0.1-02` 缺 formal VFM 输入和准入检查。它们没有被 synthetic 数据替代。

完整机器可读清单：[phase12_recovery_data_inventory.csv](../../../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/phase12_recovery_data_inventory.csv)。数据库：[PA12_database.h5](../../../实验/PA12-双轴-DIC-VFM/PA12_database.h5)。

## 二、实际采用的计算方法

### 1. 数据入口和时间同步

每个实验先读取真实 MatchID/DIC 结果和 `Force.csv`。相机时间使用用户确认的首末帧硬件触发时间端点估计，并按逐帧硬件时间形成 `time_s`；Force 接口检查时间单位、采样频率、首末时间和缺失比，再将每一帧映射为：

```text
frame_id, time_s, Fx, Fy, boundary_force
```

最终供 VFM 使用的正式输入为 `formal_vfm_input.csv.gz`，每一行对应一个 DIC 场点，力值和时间在同一 `frame_id` 上重复写入，因而可以在帧内对 `exx/eyy/exy` 做场平均，也能保留全部场点追溯。

### 2. 真实实验应力–应变曲线

报告图中的实验曲线不是凭空生成的本构曲线，而是从真实测量量得到的名义场平均曲线：

```text
ε_exp = mean(exx)  （X轴单轴）
ε_exp = mean(eyy)  （Y轴单轴）
σ_exp = (F_axis − F_0) / A_0
A_0   = Phase 9/12 记录的试样初始截面面积 = 宽度 × 厚度
```

应变和力先减去首帧基线。为统一不同相机坐标方向，报告图把加载力方向旋转为正号；CSV 同时保留 `axial_strain_raw_signed`、`force_raw_N` 和 `stress_raw_signed_MPa`，没有覆盖原始符号。图中只画达到峰值力之前的加载支，避免把峰值后的卸载/回程段当作单调本构数据；全部帧仍在 CSV 中。

这一定义是“DIC场平均 + 初始截面面积”的名义应力代理，不是局部应力场，也不等同于有限元积分得到的真实局部应力。

### 3. Phase 8 单轴 VFM：内外虚功怎样同步

虚功平衡的基本式为：

```text
Wint = ∫Ω σ : δε* dΩ
Wext = ∫Γ T · δu* dΓ
```

本项目的单轴实现采用加载轴线性虚位移场：加载边虚位移为单位量，反力边虚位移为零，场内按加载方向线性变化。代码中的实际计算为：

```text
Wint = E_phase8 × Wint_per_E_N
Wext = ΔF_axis
residual = Wint − Wext
```

其中 `Wint_per_E_N` 来自真实 DIC 的 `exx/eyy` 场平均、厚度、参考 ROI 尺寸和选定虚应变场；`Wext` 来自真实同步力值。图 [single_axis_virtual_work_sync.png](../../../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/single_axis_virtual_work_sync.png) 把每个实验的 `Wint`、`Wext` 和残差按 `frame_id` 画在一起，因此可以直接看出是否闭合，而不是只看一个最终标量。

双轴实验直接读取 Phase 11 的真实 `frame_results`，分别画 X内/外虚功和 Y内/外虚功：[biaxial_virtual_work_sync.png](../../../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/biaxial_virtual_work_sync.png)。

### 4. Phase 9：真实力–位移拟合

Phase 9 使用 J2 von Mises 单轴响应函数，以真实力–位移残差为主目标、真实横向 DIC 应变为辅助识别约束，用 `scipy.optimize.least_squares` 识别：

```text
E, nu, sigma_y, H, n
```

图 [single_axis_force_displacement_vfm_compare.png](../../../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/single_axis_force_displacement_vfm_compare.png) 中：蓝线是真实实验力，橙线是 Phase 9 的 J2 力–位移预测，绿线是 Phase 12 联合参数对应的单轴预测。橙线与蓝线的接近程度才是 Phase 9 力拟合的直接证据；应力–应变本构图是把同一组参数代入 J2 响应函数后的材料响应展示。

### 5. Phase 12：单轴 + 双轴联合识别

Phase 12 把 Phase 9 单轴力–位移/横向应变信息和 Phase 11 双轴虚功/应力信息放到同一组参数中优化，输出 `PA12_multiaxial_material.json`。图 [single_axis_vfm_constitutive_compare.png](../../../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/single_axis_vfm_constitutive_compare.png) 对每个单轴实验同时画：

1. 真实 DIC+Force 名义应力–应变加载支；
2. Phase 9 力–位移拟合得到的 J2 本构响应；
3. Phase 12 单轴+双轴联合参数得到的 J2 本构响应。

当前图中有些 Phase 12 绿线接近零，这是输入结果的真实表现：相应 JSON 中 `E≈1 MPa` 或其他参数触边，不能把它解释成 PA12 的真实弹性模量。它说明当前 Recovery 已经把真实数据送入优化闭环，但参数唯一性和边界设置仍需人工复核。

## 三、真实照片与虚功证据一一对应

下图左侧是 Obsidian 已归档的真实 DIC 原始照片，右侧是同一 `experiment_id` 的虚功曲线；前两行为 Phase 8 单轴，第三行为 Phase 11 双轴。照片文件名和右图标题使用同一个实验编号，避免把照片和计算结果错配。

![真实照片与同编号VFM内外虚功同步证据](../../../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/vfm_virtual_work_sync_evidence.png)

单张原始照片也可直接查看：

- `XY_X-06-1.0-01_frame066.jpg`：[真实照片](../../assets/pa12-real/2026-09-19/XY_X-06-1.0-01_frame066.jpg)
- `XY_X-07-10-01_frame040.jpg`：[真实照片](../../assets/pa12-real/2026-09-19/XY_X-07-10-01_frame040.jpg)
- `XY_Xy-04-1-01_frame126.jpg`：[真实照片](../../assets/pa12-real/2026-09-19/XY_Xy-04-1-01_frame126.jpg)

## 四、流程图：从真实数据到 VFM 本构

```mermaid
flowchart LR
  accTitle: PA12真实实验到VFM本构与代理模型流程
  accDescr: 真实DIC和Force进入时间同步与质量门控，经过单轴和双轴虚功计算、J2参数识别、HDF5数据库和真实数据MLP试验。
  real_input[真实MatchID DIC与Force csv] --> time_sync[相机帧与力值时间同步]
  time_sync --> quality_gate[真实数据质量门控]
  quality_gate --> formal_input[formal_vfm_input csv gz]
  formal_input --> field_average[逐帧场平均与加载支]
  field_average --> virtual_work[Phase 8/11内外虚功]
  virtual_work --> j2_fit[Phase 9 J2力位移拟合]
  j2_fit --> joint_fit[Phase 12单轴加双轴联合识别]
  joint_fit --> hdf5_db[Phase 13真实HDF5数据库]
  hdf5_db --> mlp_pilot[Phase 14真实数据MLP试验]
```

讲解时可以按三句话展开：第一，VFM 不先假定局部应力，而是用虚场把真实 DIC 应变场和真实边界力投影到虚功平衡；第二，Phase 9/12 通过调整 `E、nu、sigma_y、H、n` 让模型力–位移和虚功残差尽可能接近实验；第三，只有当虚功闭合、参数不触边、跨实验验证通过后，识别参数才可以进入材料数据库的“可用材料常数”层级。

## 五、Phase 13 与 Phase 14 状态

### Phase 13

`PA12_database.h5` 已更新为 8 个真实实验，包含 `strain_history`、`stress_history`、`force_history`、`identified_parameters` 和派生单轴视图。HDF5 属性为 `source_is_real=true`、`synthetic_used=false`、`ai_used=false`。

### Phase 14

已从当前 8 组真实实验重训 MLP，实验级拆分为：

| split | 实验数 | experiment_id |
|---|---:|---|
| train | 5 | `XY_X-06-1.0-01`, `XY_X-07-10-01`, `XY_Xy-0.1-01`, `XY_Y-09-0.1-02`, `XY_Y-10-1-01` |
| validation | 2 | `XY_Xy-03-10-01`, `XY_Xy-04-1-01` |
| test | 1 | `XY_Y-11-10-01` |

输入为 153 个真实场/力历史特征，标签来自 Phase 12，不由 AI 生成。当前输出位于 [phase14_real_recovery](../../../实验/PA12-双轴-DIC-VFM/PA12_AI_VFM/AI_Model/phase14_real_recovery/)。测试集只有 1 个实验，整体 RMSE=`212.2289`、MAE=`114.7329`；验证集整体 RMSE=`2216.4172`。因此仍标记为 `pilot_only=true`，不作为泛化模型结论。

## 六、图表、数据和复现文件

- [真实单轴实验应力–应变加载支](../../../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/single_axis_real_stress_strain.png)
- [真实本构与VFM识别本构对比](../../../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/single_axis_vfm_constitutive_compare.png)
- [真实力–位移与Phase 9/12预测](../../../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/single_axis_force_displacement_vfm_compare.png)
- [单轴内外虚功同步](../../../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/single_axis_virtual_work_sync.png)
- [双轴X/Y内外虚功同步](../../../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/biaxial_virtual_work_sync.png)
- [照片—虚功一一对应证据](../../../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/vfm_virtual_work_sync_evidence.png)
- [单轴曲线原始数据](../../../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/single_axis_real_stress_strain_data.csv)
- [VFM对比原始数据](../../../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/single_axis_vfm_comparison_data.csv)
- [逐帧虚功数据](../../../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/single_axis_virtual_work_sync_data.csv)
- [Phase 12 参数对比表](../../../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/single_axis_constitutive_parameters.csv)
- [图表与数据清单](../../../实验/PA12-双轴-DIC-VFM/reports/phase12_recovery/phase12_recovery_figure_manifest.json)
- [可汇报 PPT](../../../实验/PA12-双轴-DIC-VFM/reports/PA12_Phase6_13_5_真实实验汇报_v5.pptx)

## 已知限制

- 当前 Phase 8 的部分 `relative_l2` 残差仍接近 1，说明内外虚功没有充分闭合；图中保留了残差，不用视觉平滑掩盖。
- Phase 9/12 的优化成功标记只代表数值优化器停止，不代表材料参数已经唯一或物理可信。
- 单轴本构图的实验应力是场平均名义应力，Phase 9 参数主要由 DIC 位移–力曲线识别；二者的应变测量口径不同，必须结合力–位移图一起解释。
- Phase 14 的样本数仍只有 8 个独立实验，MLP 只作为数据管线试验，等待人工检查 Phase 12 参数边界和虚功残差后再决定是否恢复正式 AI 阶段。

## 关联笔记

[[Phase12-Recovery-真实实验材料参数闭环-2026-09-19]] · [[PA12-Phase6-13.5真实实验成果总览-2026-09-19]] · [[Phase13-PA12材料数据库-2026-09-18]] · [[Phase13.5-PA12实验数据库质量-2026-09-19]] · [[Phase14-PA12真实数据MLP代理模型-2026-09-19]]
