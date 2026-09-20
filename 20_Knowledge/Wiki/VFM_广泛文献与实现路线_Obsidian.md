---
title: VFM广泛文献与实现路线
created: 2026-09-13
tags:
  - VFM
  - DIC
  - 全场测量
  - 本构识别
  - 实验力学
status: literature-map
---

# VFM 广泛文献与实现路线

## 结论先行

VFM（Virtual Fields Method，虚拟场法）的核心不是把力–位移曲线直接拟合成材料参数，而是：

1. 从 DIC、立体 DIC、数字体相关、网格法、干涉法或高速成像得到全场位移/应变；
2. 为试样构造满足运动学约束的虚拟位移场；
3. 把虚拟场代入虚功原理，使内部虚功、边界力虚功以及动态情况下的惯性虚功平衡；
4. 通过一个或多个虚拟场，把测得的全场信息转换成材料本构参数的方程组或目标函数；
5. 用线性求解、最小二乘、非线性优化或有限元求解识别材料参数。

因此，VFM 成败首先取决于 **DIC 位移场是否可靠、力与图片是否同步、边界力方向是否正确、单位和厚度是否一致、虚拟场是否满足边界条件，以及试验是否激活了待识别参数**。仅有力 CSV 不能完成 VFM；力 CSV 只是外功项的一部分。

本笔记不声称穷尽全球所有论文。这里采用可复现的广泛边界：VFM 原理、虚拟场构造、噪声/不确定度、线性弹性、各向异性、塑性、黏弹性、超弹性、泡沫、复合材料、木材、损伤、3D/体数据、动态/高应变率、试样设计、软件实现和工程应用。

## 1. 数学主线

### 1.1 静力虚功方程

对满足运动学可容许条件的虚位移场 \(\mathbf{u}^{\ast}\)，其虚应变为

$$
\boldsymbol{\varepsilon}^{\ast}
=\frac{1}{2}\left(\nabla\mathbf{u}^{\ast}+\nabla\mathbf{u}^{\ast T}\right).
$$

无体力、准静态条件下，虚功原理写为

$$
\int_{\Omega}\boldsymbol{\sigma}:\boldsymbol{\varepsilon}^{\ast}\,\mathrm{d}\Omega
=
\int_{\Gamma_t}\mathbf{t}\cdot\mathbf{u}^{\ast}\,\mathrm{d}\Gamma.
$$

左边是内部虚功，右边是已知边界力的虚功。虚位移场在反力分布未知的边界上必须取零，或者使该边界上的贡献能够消失；否则会把未知夹具反力错误地带入方程。

### 1.2 线性本构识别

若应力可写为待识别参数的线性组合

$$
\boldsymbol{\sigma}(\mathbf{x},t)
=\sum_{k=1}^{n_p}p_k\,\boldsymbol{\sigma}_k(\mathbf{x},t),
$$

对第 \(q\) 个虚拟场有

$$
\sum_{k=1}^{n_p}
\left[
\int_{\Omega}
\boldsymbol{\sigma}_k:\boldsymbol{\varepsilon}^{\ast(q)}\,\mathrm{d}\Omega
\right]p_k
=
\int_{\Gamma_t}\mathbf{t}\cdot\mathbf{u}^{\ast(q)}\,\mathrm{d}\Gamma.
$$

汇总多个虚拟场后得到

$$
\mathbf{A}\mathbf{p}=\mathbf{b},
\qquad
\widehat{\mathbf{p}}
=\arg\min_{\mathbf{p}}\left\|\mathbf{A}\mathbf{p}-\mathbf{b}\right\|_2^2.
$$

各向同性平面应力弹性可用 \(E,\nu\) 表示；平面正交各向异性通常需要 \(Q_{11},Q_{22},Q_{12},Q_{66}\) 或等价参数。参数个数决定所需的独立虚拟场数量和试验中的应变状态丰富度。

各向同性平面应力下，常用关系为

$$
Q_{11}=\frac{E}{1-\nu^2},
\qquad
Q_{12}=\frac{\nu E}{1-\nu^2},
\qquad
Q_{66}=G=\frac{E}{2(1+\nu)}.
$$

所以，若软件报告 \(Q_{11},Q_{12}\)，应检查

$$
\nu=\frac{Q_{12}}{Q_{11}},
\qquad
E=Q_{11}(1-\nu^2).
$$

出现负的 \(E\)、明显超出物理范围的 \(\nu\)、或正交各向异性矩阵不满足正定性时，应先检查数据和边界映射，不能把优化“收敛”当成物理正确。

### 1.3 非线性本构识别

塑性、黏弹性、超弹性、损伤等模型一般写成

$$
\boldsymbol{\sigma}(t)
=\boldsymbol{\sigma}\left(\boldsymbol{\varepsilon}(\tau\leq t),
\dot{\boldsymbol{\varepsilon}}(\tau\leq t),
\mathbf{p}\right).
$$

对应目标函数可以写成

$$
\Phi(\mathbf{p})
=
\sum_{q=1}^{n_v}\sum_{m=1}^{n_t}
\omega_{qm}
\left[
\mathcal{W}_{\mathrm{int}}^{(q)}(t_m;\mathbf{p})
-
\mathcal{W}_{\mathrm{ext}}^{(q)}(t_m)
\right]^2.
$$

识别过程需要在每一组候选参数下执行本构积分、计算应力场和虚功，再使用最小二乘、信赖域、遗传算法或其他优化器。优化器找到“剩余为零”并不等于材料模型、边界条件和数据同步都正确。

### 1.4 动态 VFM

动态情况下，达朗贝尔形式可写为

$$
\int_{\Omega}
\boldsymbol{\sigma}:\boldsymbol{\varepsilon}^{\ast}\,\mathrm{d}\Omega
+
\int_{\Omega}
\rho\,\mathbf{a}\cdot\mathbf{u}^{\ast}\,\mathrm{d}\Omega
=
\int_{\Gamma_t}
\mathbf{t}\cdot\mathbf{u}^{\ast}\,\mathrm{d}\Gamma
+
\int_{\Omega}
\rho\,\mathbf{b}\cdot\mathbf{u}^{\ast}\,\mathrm{d}\Omega.
$$

其中 \(\mathbf{a}\) 为由全场位移二阶时间导数得到的加速度。动态 VFM 对时间同步、空间噪声和二阶微分非常敏感，不能把准静态力 CSV 直接套到动态方程中。

## 2. VFM 的主要实现分支

| 分支 | 输入 | 参数识别方式 | 适用范围 | 对当前项目的意义 |
|---|---|---|---|---|
| 特殊/手工虚拟场 | DIC 应变、边界力、几何 | 直接方程或线性最小二乘 | 线性弹性、正交各向异性 | 适合先验证双轴数据和边界方向 |
| 优化虚拟场 | DIC 全场、噪声模型、材料初值 | 最小化噪声传播或参数方差 | 线性弹性、部分非线性 | 适合减少 DIC 噪声导致的参数漂移 |
| 敏感度虚拟场 | 全场位移/应变、本构切线 | 根据应力对参数的敏感度自动生成虚拟场 | 塑性、非线性材料 | 适合塑性和复杂参数模型，但实现难度更高 |
| FE-VFM | DIC 位移、FE 网格、几何、厚度、边界 | 有限元离散虚功方程 | 复杂几何、3D、超弹性、异质材料 | 适合从 MatchID/DIC CSV 进入可追溯代码流程 |
| 空间/分片/正则化 VFM | 全场数据、局部网格或先验模型 | 局部参数、正则化优化 | 非均匀复合材料、焊接接头、损伤 | 可用于局部缺陷和打印方向差异 |
| 动态/惯性 VFM | 高速 DIC、加速度、密度、可能无力传感器 | 将惯性虚功加入平衡 | 高应变率、冲击、振动 | 不适合直接处理当前低速普通相机数据 |
| 频域/Fourier VFM | 时间序列全场数据 | 频域虚功和快速积分 | 振动、黏弹性、周期载荷 | 若以后做频率响应，可减少时间域微分噪声 |

## 3. 核心文献与实现要点

### 3.1 VFM 原理与总览

1. [Grédiac, Pierron, Avril & Toussaint, 2006/2008, The Virtual Fields Method for Extracting Constitutive Parameters From Full-Field Measurements](https://doi.org/10.1111/j.1475-1305.2006.tb01504.x)
   - 最重要的总览文献。
   - 说明 VFM 基于虚功原理，覆盖线性和非线性本构以及全场光学测量。
   - 第一篇应先读，用来建立术语和公式框架。

2. [Grédiac, Toussaint & Pierron, 2002, Special virtual fields—Principle and definition](https://doi.org/10.1016/S0020-7683(02)00127-0)
   - 介绍如何自动构造特殊虚拟场，使参数能够直接从异质应变场中提取。

3. [Grédiac, Toussaint & Pierron, 2002, Special virtual fields—Application to in-plane properties](https://doi.org/10.1016/S0020-7683(02)00128-2)
   - 面向平面正交各向异性和 Iosipescu/短梁类异质试验。
   - 说明多个独立虚拟场、参数解耦、稳定性和非线性剪切识别。

4. [Grédiac & Pierron, 2002, Identification of mechanical properties with VFM as an alternative to FEMU](https://doi.org/10.1016/S1631-0721(02)01435-3)
   - 适合对比 VFM 与 FEMU 的思想差异：VFM直接使用全场数据和虚功关系，不必每次迭代都完整更新有限元模型。

### 3.2 虚拟场优化、噪声和数值问题

5. [Avril, Grédiac & Pierron, 2004, Sensitivity of the virtual fields method to noisy data](https://doi.org/10.1007/s00466-004-0579-6)
   - 研究测量噪声如何通过空间微分和积分传播到材料参数。
   - 对 DIC 的 subset、step、strain window、平滑方式选择非常关键。

6. [Grédiac & Pierron, 2004, Numerical issues in the virtual fields method](https://doi.org/10.1002/nme.1167)
   - 关注离散化、数值积分、虚拟场选择和病态问题。

7. [Grédiac et al., 2006, The virtual fields method with piecewise virtual fields](https://doi.org/10.1016/j.ijmecsci.2005.10.002)
   - 将虚拟场定义为分片/节点自由度，适合局部异质材料和实际网格实现。

8. [Pierron & Grédiac, 2021, Towards Material Testing 2.0](https://doi.org/10.1111/str.12370)
   - 把试样设计、应变状态、参数可辨识性、DIC误差和全流程不确定度放在同一框架下。
   - 明确提出试验设计不能只凭经验，应考虑从图像生成、DIC处理直到参数识别的完整链路。

### 3.3 弹塑性、各向异性和双轴试验

9. [Grédiac & Pierron, 2006, Applying VFM to elasto-plastic constitutive parameters](https://doi.org/10.1016/j.ijplas.2005.04.007)
   - 通过虚功构造目标函数，再最小化材料参数。
   - 适用于复杂试样和非均匀场；文献强调不需要每次迭代进行完整 FE 更新，但仍需要正确的本构积分和虚拟场。

10. [Martins, Andrade-Campos & Thuillier, 2019, Calibration of anisotropic plasticity models using a biaxial test and VFM](https://doi.org/10.1016/j.ijsolstr.2019.05.019)
   - 直接关联双轴/十字形试样、Hill'48 和 Yld2000-2d/Swift 等模型。
   - 对当前双轴试验最有参考价值：试样几何、载荷路径和应变状态必须能区分待识别参数。

11. [A VFM-based identification method for dynamic anisotropic plasticity of sheet metals](https://doi.org/10.1016/j.ijmecsci.2022.107550)
   - 将 VFM 扩展到动态各向异性塑性；动态惯性项和时间同步是核心问题。

12. [Inverse identification of hardening behavior with a fully 3D VFM](https://link.springer.com/article/10.1186/s40323-025-00293-7)
   - 关注 3D 场、硬化行为和自动/手工虚拟场的差异。

### 3.4 敏感度虚拟场和自动生成

13. [Marek, Davis & Pierron, 2017, Sensitivity-based virtual fields for the non-linear VFM](https://doi.org/10.1007/s00466-017-1411-6)
   - 通过材料参数对应的应力敏感度自动生成虚拟场。
   - 对低信噪比塑性参数识别具有优势，但原始 DIC 数据的时间/空间噪声仍需要平滑处理。

14. [Mei et al., 2021, General finite-element framework of VFM in nonlinear elasticity](https://doi.org/10.1007/s10659-021-09842-8)
   - 给出通用 FE-VFM 思路，面向超弹性、软材料和复杂几何。
   - 适合作为自己写 Python/Matlab/FE 代码的理论入口。

15. [Nikolov et al., 2026, Variation-Matching Sensitivity-Based Virtual Fields for Hyperelastic Material Model Calibration](https://doi.org/10.1111/str.70031)
   - 进一步研究三维全场和超弹性参数标定中的敏感度虚拟场。

### 3.5 超弹性、橡胶、生物材料和软材料

16. [Identification of constitutive parameters governing the hyperelastic response of rubber using full-field measurement and VFM](https://arxiv.org/abs/1907.02687)
   - 说明异质试验和全场位移可用于超弹性模型参数识别。

17. [General finite-element framework of VFM in nonlinear elasticity](https://link.springer.com/article/10.1007/s10659-021-09842-8)
   - 覆盖软组织和复杂几何，是从二维 VFM 过渡到有限元离散 VFM 的关键文献。

18. [Adaptation of VFM for biphasic hyperelastic model parameters in soft biological tissues with osmotic swelling](https://doi.org/10.1111/str.12435)
   - 说明 VFM 可以扩展到耦合场和生物软组织，不局限于工程塑料或金属。

19. [How robust is VFM with respect to experimental inhomogeneities for bulge inflation testing of hyperelastic materials?](https://doi.org/10.1016/j.jmbbm.2025.106965)
   - 直接讨论实验不均匀性、鼓胀试验和超弹性识别稳健性。

20. [Finite-strain identification of hyperelastic polyurethane adhesive using VFM](https://doi.org/10.1016/j.compstruc.2026.108356)
   - 代表有限应变胶黏剂/聚合物材料的近期应用。

### 3.6 泡沫、木材、复合材料和异质材料

21. [Guo, Pierron & Rotinat, 2008, Identification of low density polyurethane foam properties by DIC and VFM](https://doi.org/10.1117/12.839331)
   - 将 DIC 与 VFM 用于低密度聚氨酯泡沫的弹性和大变形压缩行为。

22. [Wang et al., 2016, Optimised experimental characterisation of polymeric foam material using DIC and VFM](https://doi.org/10.1111/str.12170)
   - 重点是把试样几何、DIC 参数、噪声和识别误差一起用于试验优化。

23. [Rahmani et al., 2014, In-situ mechanical properties identification of 3D particulate composites using VFM](https://doi.org/10.1016/j.ijsolstr.2014.05.006)
   - 3D 全场、颗粒复合材料、局部相性能和正则化 VFM。

24. [Latourte et al., 2014, Regularized VFM for mechanical properties identification of composite materials](https://doi.org/10.1016/j.cma.2014.05.010)
   - 将微观力学先验作为正则化项，减弱局部参数识别的病态性。

25. [Direct identification of damage behaviour of composite materials using VFM](https://doi.org/10.1016/j.compositesa.2004.01.011)
   - 将 VFM 用于复合材料剪切损伤本构，而不是仅识别弹性常数。

26. [Variation of transverse and shear stiffness properties of wood in a tree](https://userweb.fct.unl.pt/~jmc.xavier/pdf/Xavier2009_Variation%20of%20transverse%20and%20shear%20stiffness%20properties%20of%20wood%20in%20a%20tree.pdf)
   - 代表木材和天然各向异性材料的 VFM 识别。

27. [Optimized experimental characterisation of orthotropic foam material](https://onlinelibrary.wiley.com/doi/10.1111/str.12170)
   - 适合学习如何用参数可辨识性反向设计加载方向和试样几何。

### 3.7 黏弹性、振动和频域 VFM

28. [Extension of the optimized VFM to estimate viscoelastic material parameters from 3D dynamic displacement fields](https://pmc.ncbi.nlm.nih.gov/articles/PMC4486339/)
   - 适用于 3D 动态位移场、黏弹性和频域处理。
   - 需要注意时间滤波、频率选择和空间分辨率对参数偏差的影响。

29. [Characterising frequency-response of ultra-soft polymers with VFM](https://doi.org/10.1111/str.12386)
   - 关注超软聚合物、频率响应和 DIC 噪声抑制。

30. [A Fourier-series-based VFM for identification of 2-D stiffness distributions](https://doi.org/10.1002/nme.4665)
   - 用 Fourier 形式和快速变换处理二维刚度分布，适合周期或规则采样问题。

### 3.8 动态、高应变率和惯性释放

31. [Inertia-based identification of elastic anisotropic properties under dynamic loadings using VFM](https://www.sciencedirect.com/science/article/pii/S0264127521001477)
   - 将高速全场测量、惯性项和各向异性弹性识别结合起来。

32. [Image-Based Inertial Release test: a new high strain rate test](https://doi.org/10.1007/s11340-019-00580-6)
   - 通过高速图像和加速度场构造惯性释放试验，可在特定条件下减少对传统力传感器的依赖。

33. [Analysing high strain rate behaviour of cortical bone with IBII](https://pmc.ncbi.nlm.nih.gov/articles/PMC12713302/)
   - 代表生物材料高应变率 VFM/IBII 应用。

34. [The VFM in dynamic elastoplastic identification](https://eprints.soton.ac.uk/446213/1/Fletcheretal_2020_ElastoPlasIBII_Part2.pdf)
   - 展示动态虚功中内部、外部和惯性贡献的组织方式。

### 3.9 3D、体数据和有限元实现

35. [FEniCS implementation of the Virtual Fields Method for nonhomogeneous hyperelastic identification](https://doi.org/10.1016/j.advengsoft.2022.103343)
   - 将 VFM 与 FEniCS/有限元实现结合，适合复杂几何和非均匀超弹性参数场。

36. [FEniCS implementation preprint/code paper](https://cnrs.hal.science/hal-03836286/document)
   - 可作为实现细节和代码结构的补充材料。

37. [Miguel J. G. Oliveira 的 Python VFM 开源实现](https://github.com/migueljgoliveira/virtual-fields-method)
   - 公开输入结构包括节点、单元、逐时间步位移、材料方向、厚度和力演化文件。
   - 这是当前最适合用来对照自己数据接口的开源入口之一。

38. [NguyenLabJHU 的 MATLAB VFM 实现](https://github.com/NguyenLabJHU/virtual_field_method)
   - 可用于了解 MATLAB 形式的虚拟场优化、数据组织和结果输出。

39. [MatCal VFM Uniaxial Tension Models](https://matcal.readthedocs.io/en/latest/VFMUniaxialTensionModels.html)
   - 文档明确要求实验全场数据与网格坐标对齐，说明自由边缘缺失点需要插值/外推，并提醒平面应力假设和厚度应力处理会造成误差。

## 4. 当前本地资料与广泛文献的关系

本地目录 `D:\C盘迁移\Desktop\yuan` 只读扫描到 4 个 PDF：

- [3D打印尼龙材料的双轴拉伸测试方法与力学性能](<D:\C盘迁移\Desktop\yuan\3D打印尼龙材料的双轴拉伸测试方法与力学性能(1).pdf>)
- [VARIABILITY IN THE MECHANICAL PROPERTIES OF LASER SINTERED PA-12](<D:\C盘迁移\Desktop\yuan\VARIABILITY IN THE MECHANICAL PROPERTIES OF LASER SINTERED PA-12 .pdf>)
- [Variability, heterogeneity, and anisotropy in the quasi-static response of laser sintered PA12 components](<D:\C盘迁移\Desktop\yuan\Variability, heterogeneity, and anisotropy in the quasi‐static response of laser sintered PA12 components.pdf>)
- [1-s2.0-S1751616122004271-main (1)](<D:\C盘迁移\Desktop\yuan\1-s2.0-S1751616122004271-main (1).pdf>)

本地资料主要回答“材料和试验背景是什么”，公开 VFM 文献主要回答“如何从全场数据建立虚功方程、选择虚拟场、处理噪声并识别本构参数”。两者需要通过以下链路连接：

```text
试样几何/打印方向
        ↓
双轴加载与边界力方向
        ↓
DIC 位移场 u_x, u_y
        ↓
应变场 ε_xx, ε_yy, γ_xy
        ↓
虚拟位移场 u*
        ↓
内部虚功 W_int 与外部虚功 W_ext
        ↓
Q11, Q22, Q12, Q66 或 E, ν, G
        ↓
弹性/塑性/损伤/各向异性模型验证
```

## 5. 对当前双轴 VFM 数据的直接判断

当前双轴项目中的关键检查顺序应是：

1. **先检查照片和 DIC 场**：确认 `Img000000` 是参考帧；确认断裂前最后一帧与力峰值/骤降位置一致；断裂后的图像不得继续作为连续变形场。
2. **再检查力的符号和方向**：分别建立 `F_x`、`F_y`，不要把四个执行器通道简单拼成一个力；每个方向先按传感器坐标和受力方向确定正负，再映射到虚功边界法向。
3. **再检查坐标系**：DIC 的 X/Y 方向、VFM 项目的 X/Y 方向、试样加载方向和虚拟场方向必须一致；不能只凭文件名中的 X/Y 判断。
4. **再检查单位**：力、长度、厚度、面积、DIC 位移、应变和应力必须在同一单位系统中；力值的原始单位不能由列名 `force` 或 `press` 猜测。
5. **最后才识别参数**：先用小应变弹性段识别线性参数，再逐步加入塑性或大变形模型；不要把断裂后的力骤降段和失配 DIC 场带入弹性识别。

此前双轴 VFM 结果出现负的弹性参数，这不是可以接受的“材料结论”。它更像是符号、边界法向、虚拟场、单位、坐标映射或有效帧范围中的至少一项不一致。已有 VFM 文件中的力序列和当前力-only CSV 能够对上，并不能证明内部虚功计算已经正确，因为 VFM 仍然需要 DIC 位移/应变场和正确的边界映射。

## 6. 推荐的代码实现路线

### 阶段 A：先做线性二维验证

输入统一为：

```text
frame_id, image_file, x, y, u_x, u_y, epsilon_xx, epsilon_yy, gamma_xy,
F_x, F_y, thickness, source_file
```

每一帧至少保留：

```text
frame_id
image_file
x, y
u_x, u_y
epsilon_xx, epsilon_yy, gamma_xy
F_x, F_y
thickness
source_file
```

首先只实现平面应力正交各向异性：

$$
\begin{bmatrix}
\sigma_{xx}\\
\sigma_{yy}\\
\tau_{xy}
\end{bmatrix}
=
\begin{bmatrix}
Q_{11}&Q_{12}&0\\
Q_{12}&Q_{22}&0\\
0&0&Q_{66}
\end{bmatrix}
\begin{bmatrix}
\varepsilon_{xx}\\
\varepsilon_{yy}\\
\gamma_{xy}
\end{bmatrix}.
$$

先用手工构造的 4 个独立虚拟场做基线版本，再实现优化虚拟场。这样可以把“数据问题”和“自动虚拟场算法问题”分开。

### 阶段 B：再接入真实 DIC

- 从 MatchID 导出的 CSV 中读取参考坐标和每帧位移；
- 用同一套网格对所有帧重采样；
- 对位移做适度空间平滑后再求应变；
- 用实际试样厚度和 ROI 几何做积分；
- 对每一帧分别计算内部虚功和外部虚功；
- 输出残差、条件数、参数轨迹和有效帧标记。

### 阶段 C：加入双轴边界和模型比较

至少比较三种模型：

1. 各向同性线弹性；
2. 平面正交各向异性线弹性；
3. 含硬化的弹塑性模型。

比较指标不是只看某一个参数，而是同时看：

$$
R_q(t)=W_{\mathrm{int}}^{(q)}(t)-W_{\mathrm{ext}}^{(q)}(t),
$$

参数的时间稳定性、重复试验一致性、残差结构、物理正定性和断裂前有效范围。

## 7. 阅读优先级

### 第一优先级：必须读

1. Grédiac et al. VFM 总览；
2. Special virtual fields—Principle and definition；
3. Special virtual fields—Application to in-plane properties；
4. Grédiac & Pierron 的弹塑性 VFM；
5. Pierron & Grédiac 的 Material Testing 2.0。

### 第二优先级：直接服务当前双轴数据

6. Martins et al. 双轴各向异性塑性；
7. DIC/立体 DIC 的 VFM 误差与精度论文；
8. Piecewise virtual fields；
9. 开源 Python VFM 和 MatCal 文档；
10. FE-VFM/General FE framework。

### 第三优先级：按研究方向扩展

- 塑性：Marek 的 sensitivity-based VFM、动态各向异性塑性；
- 超弹性：Mei et al.、FEniCS VFM、橡胶/泡沫论文；
- 复合材料：RVFM、损伤、3D particulate composites；
- 动态：IBIR、IBII、3D 黏弹性 VFM；
- 局部/异质：piecewise、Fourier、空间正则化和焊接接头映射。

## 8. 必须保留的证据链

```text
原始照片
原始力/位移/控制器日志
原始 DIC/MatchID 导出
力-照片同步映射
单位和坐标说明
VFM 输入文件
代码和参数配置
VFM 输出参数、虚功残差和图像
```

原始文件不删除、不覆盖。处理结果另存；每个结果保留 `source_file` 和有效帧范围。原始 PDF、原始实验数据和任何 API Key 不上传到公开 GitHub。

## 9. 目前的研究创新候选

在不夸大结论的前提下，当前项目可以形成的创新方向不是“首次使用 VFM”，而是：

1. 建立适用于双轴聚合物/增材制造材料的“图像—DIC—力—虚拟功—参数”可追溯数据链；
2. 比较单轴和双轴异质场对各向同性与正交各向异性参数可辨识性的差异；
3. 将断裂前有效帧、同步残差和 DIC 质量纳入 VFM 参数识别的有效性判据；
4. 用试样几何和加载路径设计，让双轴试验同时激活 \(Q_{11},Q_{22},Q_{12},Q_{66}\) 或塑性参数；
5. 分析增材制造方向、孔隙/层间结构和局部异质性对全场参数的影响；
6. 在不伪造数据的前提下，用合成场只验证代码数值正确性，再用真实 DIC 数据做实验结论。

## 10. 当前阶段不应做的事

- 不能用只有 `F_x` 或 `F_y` 的 CSV 代替 DIC 位移场；
- 不能用断裂后图像继续延长连续应变场；
- 不能因为软件显示“剩余为 0、迭代完成”就接受负弹性模量；
- 不能把 `X1/X2`、`Y1/Y2` 通道未经受力方向判断就相加；
- 不能用单位未知的 `press` 列直接报告 MPa；
- 不能把合成数据或平滑后的结果冒充原始实验数据。
