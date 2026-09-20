---
title: "VFM：引伸计、DIC与试验机位移的定义及代码计算"
aliases:
  - "VFM位移定义"
  - "双轴试验VFM数据排查"
tags:
  - research/PA12
  - experiment/biaxial
  - method/DIC
  - method/VFM
  - data/synchronization
  - measurement/extensometer
type: research-note
status: "待验证"
created: 2026-09-13
updated: 2026-09-13
---

# VFM：引伸计、DIC 与试验机位移的定义及代码计算

## 核心结论

引伸计位移、DIC 位移、试验机横梁位移和“力数据位移”通常不是同一个物理量。它们的测量位置、标距、时间基准和数据来源不同，因此数值不一致并不一定表示数据错误。

已有四组 XY 数据中的“力数据位移”与设定速度乘以力数据记录时间完全一致。因此该字段应先解释为“按速度计算的理论行程”，不能直接当作引伸计实测位移。

只有力的 CSV 可以作为 VFM 的外载输入，但不能独立完成 VFM 本构识别。完整 VFM 还需要 DIC 全场位移或应变、试样几何、厚度、载荷边界和虚拟场定义。

## 1. 不同位移的物理含义

| 数据名称 | 物理含义 | 典型表达 | 是否包含夹具和机架变形 |
|---|---|---|---|
| 引伸计位移 | 引伸计两个刀口或标距点之间的局部伸长 | $\Delta L_{\mathrm{ext}}=L(t)-L_0$ | 通常不包含 |
| DIC 标距位移 | DIC 中两个对应点或两个区域之间的相对位移 | $\Delta u_{\mathrm{DIC}}=u(B)-u(A)$ | 取决于选点和刚体校正 |
| 试验机位移 | 横梁、执行器或控制器记录的位移 | $u_{\mathrm{machine}}$ | 通常包含 |
| 力数据位移 | 由控制器输出，或由速度和时间计算得到的行程 | $u_{\mathrm{nominal}}=vt$ | 不代表标距变形 |

试验机横梁位移可以近似写成：

$$
\Delta L_{\mathrm{machine}}
=
\Delta L_{\mathrm{specimen}}
+
\Delta L_{\mathrm{grip}}
+
\Delta L_{\mathrm{frame}}
$$

## 2. 当前四组 XY 数据的判断

已有数据满足：

$$
\Delta u_{\mathrm{nominal}}
=
v_{\mathrm{set}}t_{\mathrm{force}}
$$

| 试验 | 设定速度 | 力数据时间 | 计算结果 | 当前力数据位移 |
|---|---:|---:|---:|---:|
| Xy-0.1-01 | $0.2\ \mathrm{mm/s}$ | $36.300\ \mathrm{s}$ | $7.2600\ \mathrm{mm}$ | $7.2600\ \mathrm{mm}$ |
| XY-0.1-02 | $0.2\ \mathrm{mm/s}$ | $28.049\ \mathrm{s}$ | $5.6098\ \mathrm{mm}$ | $5.6098\ \mathrm{mm}$ |
| Xy-03-10-01 | $20.0\ \mathrm{mm/s}$ | $0.510\ \mathrm{s}$ | $10.2000\ \mathrm{mm}$ | $10.2000\ \mathrm{mm}$ |
| Xy-04-1-01 | $2.0\ \mathrm{mm/s}$ | $4.576\ \mathrm{s}$ | $9.1520\ \mathrm{mm}$ | $9.1520\ \mathrm{mm}$ |

建议把当前字段改名为：

~~~text
u_nominal_x / u_nominal_y
按速度计算的理论行程
~~~

不要把它直接命名为 u_ext、引伸计位移 或 DIC位移。

## 3. 双轴试验中的 X/Y 位移定义

双轴试验需要分别处理 X 和 Y 方向，不能把两个方向合成为一个总位移或总力。

X 方向标距位移：

$$
\Delta u_X=u_X(B_X)-u_X(A_X)
$$

Y 方向标距位移：

$$
\Delta u_Y=u_Y(B_Y)-u_Y(A_Y)
$$

建议保留以下字段：

| 字段 | 含义 |
|---|---|
| u_ext_x | X 方向引伸计位移 |
| u_ext_y | Y 方向引伸计位移 |
| u_dic_x | DIC X 方向标距相对位移 |
| u_dic_y | DIC Y 方向标距相对位移 |
| u_machine_x | 试验机 X 方向位移 |
| u_machine_y | 试验机 Y 方向位移 |
| u_nominal_x | 由速度和时间计算的 X 方向理论行程 |
| u_nominal_y | 由速度和时间计算的 Y 方向理论行程 |

X/Y 力通道应始终分别保留为 F_x 和 F_y。

## 4. 为什么不同设备的位移会不同

### 4.1 测量位置和标距不同

引伸计测量局部标距伸长，DIC 测量所选区域的相对运动，试验机记录的是执行器或横梁运动。应力集中、圆角和双轴试样中心区域的应变通常不均匀，因此不同标距会得到不同位移。

### 4.2 试验机位移包含系统柔度

$$
\Delta L_{\mathrm{machine}}
=
\Delta L_{\mathrm{specimen}}
+
\Delta L_{\mathrm{grip}}
+
\Delta L_{\mathrm{frame}}
$$

夹具滑移、机架柔度和连接件变形都会使试验机位移与引伸计位移产生差异。

### 4.3 初始零点不同

所有通道应使用同一个有效起始时刻：

$$
t_0=\text{开始有效加载或开始有效运动的时刻}
$$

每个通道都应使用增量位移：

$$
\Delta u(t)=u(t)-u(t_0)
$$

### 4.4 时间同步不同

力传感器可能以 $1000\ \mathrm{Hz}$ 采样，而相机可能以 $10\ \mathrm{Hz}$、$50\ \mathrm{Hz}$ 或 $200\ \mathrm{Hz}$ 采样。应根据 event_id、trigger_id、frame_id、t_machine 和 t_image 对齐，不能只按行号配对。

同步误差带来的位移误差近似为：

$$
\Delta u_{\mathrm{sync}}=v\Delta t
$$

### 4.5 引伸计安装误差

接触式引伸计可能存在刀口滑移、压入 PA12 表面、安装方向偏转和横向运动影响。双轴试验中还要考虑两个方向的夹具运动。

### 4.6 DIC 刚体运动和剪切定义

DIC 位移中可能含有整体平移、整体转动和相机抖动。计算标距位移或应变前，应先进行刚体运动校正。

还必须区分工程剪切应变和张量剪切应变：

$$
\gamma_{xy}
=
\frac{\partial u_x}{\partial y}
+
\frac{\partial u_y}{\partial x}
$$

$$
\varepsilon_{xy}=\frac{1}{2}\gamma_{xy}
$$

如果两者混用，VFM 的剪切虚功会产生系统性误差。

## 5. VFM 的基本方程

二维虚功方程为：

$$
\int_{\Omega}
\boldsymbol{\sigma}:\boldsymbol{\varepsilon}^{*}
\,\mathrm{d}\Omega
=
\int_{\partial\Omega_t}
\mathbf{t}\cdot\mathbf{u}^{*}
\,\mathrm{d}\Gamma
$$

内部虚功的离散表达式为：

$$
W_{\mathrm{int}}
=
\sum_{i=1}^{N}
\left(
\sigma_{xx,i}\varepsilon_{xx,i}^{*}
+
\sigma_{yy,i}\varepsilon_{yy,i}^{*}
+
2\sigma_{xy,i}\varepsilon_{xy,i}^{*}
\right)w_i
$$

双轴外部虚功应分别保留 X、Y 方向：

$$
W_{\mathrm{ext}}
=
F_xu_x^{*}
+
F_yu_y^{*}
$$

虚功残差为：

$$
r=W_{\mathrm{int}}-W_{\mathrm{ext}}
$$

如果本构关系写成 $\boldsymbol{\sigma}(\boldsymbol{\varepsilon},\boldsymbol{\theta})$，则材料参数可以通过最小化虚功残差识别：

$$
\min_{\boldsymbol{\theta}}
\sum_{k=1}^{N_{\mathrm{VF}}}
\left[
W_{\mathrm{int}}^{(k)}(\boldsymbol{\theta})
-
W_{\mathrm{ext}}^{(k)}
\right]^2
$$

## 6. 代码计算所需的最小输入

### DIC 全场数据

至少需要：

~~~text
frame_id, x, y, u_x, u_y
~~~

如果直接使用应变场，还需要确认：

~~~text
epsilon_xx, epsilon_yy, epsilon_xy 或 gamma_xy
~~~

### 力和同步数据

~~~text
event_id, trigger_id, t_machine, t_image
F_x, F_y, frame_id, sync_residual, source_file
~~~

### 试样和设备信息

~~~text
specimen_geometry, thickness, coordinate_system
pixel_scale, load_direction, boundary_condition
~~~

## 7. 代码计算流程

~~~mermaid
flowchart TD
    A[读取DIC全场位移或应变] --> B[读取Fx和Fy]
    B --> C[按trigger_id和时间同步]
    A --> D[刚体运动校正]
    D --> E[统一坐标、单位和剪切应变定义]
    C --> F[建立虚拟场]
    E --> G[计算真实应变和应力]
    F --> H[计算虚拟应变]
    G --> I[计算内部虚功]
    H --> I
    C --> J[计算外部虚功]
    I --> K[计算虚功残差]
    J --> K
    K --> L[识别材料参数]
    L --> M[残差和敏感性验证]
~~~

最小代码逻辑：

~~~python
# 读取 DIC 全场数据：frame_id, x, y, ux, uy, exx, eyy, exy
# 读取双轴力数据：event_id, t_machine, Fx, Fy

# 将力数据插值到图像时刻
Fx_img = interpolate(t_machine, Fx, t_image)
Fy_img = interpolate(t_machine, Fy, t_image)

# 计算虚拟应变
exx_v, eyy_v, exy_v = virtual_strain(x, y)

# 根据本构关系计算应力
sxx, syy, sxy = constitutive_model(exx, eyy, exy, parameters)

# 计算内部虚功
W_int = sum(
    (sxx * exx_v + syy * eyy_v + 2.0 * sxy * exy_v) * weights
)

# 计算外部虚功
W_ext = Fx_img * ux_virtual_load + Fy_img * uy_virtual_load

# 计算虚功残差并识别材料参数
residual = W_int - W_ext
parameters = solve_parameters(residual)
~~~

## 8. 推荐的验证顺序

1. 选择一组低速、近似单轴的数据。
2. 只使用 X 方向或只使用 Y 方向。
3. 使用已知线弹性参数进行正向虚功计算。
4. 检查内部虚功和外部虚功是否同量级。
5. 检查力、位移、应变和厚度的单位。
6. 检查工程剪切应变与张量剪切应变是否一致。
7. 检查 DIC 标距点是否与引伸计刀口位置一致。
8. 再加入双轴载荷。
9. 最后再识别 PA12 的非线性、塑性或应变率相关参数。

## 9. 成功标准

- F_x 和 F_y 未混合。
- 拉伸和压缩的正负号定义明确。
- DIC 与力数据按时间或触发号匹配。
- 变形量使用同一单位。
- 使用相同标距比较引伸计和 DIC。
- 剪切应变定义一致。
- 内部虚功和外部虚功同量级。
- 虚功残差没有明显系统性偏差。
- 更换相近虚拟场后结果不会完全失稳。
- 换一组试验后识别参数具有合理重复性。

## 10. 当前限制

- 尚未确认“力数据”列是否来自控制器位移通道，还是完全由速度和时间计算得到。
- DIC 位移尚未导出，因此暂时无法完成引伸计与 DIC 的数值对比。
- 没有完整的 DIC 网格、试样厚度、边界载荷区域和虚拟场表达式时，不能可靠识别 PA12 本构参数。
- 对于大变形或明显塑性阶段，需要确认小变形假设是否仍然适用。

## 11. 下一步行动

- [ ] 保留所有原始力、位移、图像和事件文件。
- [ ] 确认 u_machine 是否为设备真实位移通道。
- [ ] 导出 DIC 的 frame_id, x, y, u_x, u_y。
- [ ] 确认 X/Y 方向及拉伸、压缩符号。
- [ ] 确认引伸计标距和 DIC 对应测点。
- [ ] 用 trigger_id、t_machine、t_image 建立同步表。
- [ ] 先完成一组低速数据的线弹性虚功闭环验证。
- [ ] 输出每个虚拟场的 $W_{\mathrm{int}}$、$W_{\mathrm{ext}}$ 和残差。
- [ ] 闭环通过后，再进入 PA12 非线性本构识别。

## 相关笔记

- [[总体研究背景与方法框架-PA12双轴-DIC-VFM|PA12 双轴试验总体框架]]
- [[工程力学-双轴DIC-VFM研究路线|DIC 全场位移路线]]
- [[VFM软件识别闭环与本构参数验收|VFM 本构识别]]
- [[双轴-DIC-VFM-同步采集与预试验方案|实验数据同步]]
- [[双轴-DIC-VFM-同步采集与预试验方案|引伸计与机器位移同步]]
