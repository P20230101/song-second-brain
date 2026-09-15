# PA12 单轴到双轴场 VFM L0 软件设计

日期：2026-09-15

## 1. 目标与科学边界

本项目实现一个独立于 MatchID 内置 VFM 模块的本地 Python 求解器。第一版只处理准静态、小应变、平面应力线弹性问题，支持普通单轴基线、单轴外载诱导的双轴异质场和真实双轴加载三类数据。

软件不得把普通单轴数据复制或旋转后称为真实双轴数据。数据来源固定为以下三类：

- `measured`：真实实验测量；
- `synthetic`：用于验证程序的已知解合成数据；
- `model_predicted`：由已标定模型计算的预测数据。

普通单轴狗骨数据只允许识别其可辨识的弹性模量和泊松比基线。完整面内正交各向异性参数 `Q11、Q22、Q12、Q66` 只有在全场数据对这些参数具有足够独立激励且线性系统满秩时才允许输出。

## 2. 已有项目上下文

当前项目路径为 `双轴/实验/PA12-双轴-DIC-VFM`。现有 `results/01_VFM照片力对应.csv` 已提供四个机器力通道的逐帧候选映射，但该映射没有共同硬件触发或逐帧相机时间戳，不能作为正式 VFM 同步真值。

现有 MatchID 数据包含图像、`.dat`、`.m2inp` 和少量 CSV；已检查的 `XZ` CSV 是序列型结果，尚不是包含 `x、y、u、v、exx、eyy、gxy` 的完整二维场导出。因此第一版必须先用合成已知解闭环，真实数据适配只接收明确字段和单位的导出文件。

Faes 等人的 PA12 工作提供方法依据：特殊几何可在单轴外载下产生双轴应变场，并利用 VFM 识别面内刚度。其试样尺寸、DIC 参数和材料数值只作为文献参照，不写成软件默认值。

## 3. 方案选择

### 方案 A：只做普通单轴回归

优点是实现快，可先得到 `E、ν`。缺点是不能验证 VFM 积分，也不能独立识别完整面内刚度，因此不能解决当前目标。

### 方案 B：直接接真实双轴数据

优点是目标直接。缺点是当前 DIC 全场字段和同步真值尚未闭合，若直接实现会把数据缺口误判为求解器问题。

### 方案 C：统一接口、合成基准、再接真实数据

先建立单轴/双轴统一数据接口，用已知刚度和已知虚功的合成场验证求解器，再接普通单轴基线和真实异质场。这一方案能把软件错误、可辨识性不足和实验数据问题分开，作为第一版实施方案。

## 4. 软件目录

```text
双轴/实验/PA12-双轴-DIC-VFM/vfm/
├─ README.md
├─ examples/
│  └─ synthetic_l0/
├─ input/
├─ results/
├─ src/
│  └─ pa12_vfm/
│     ├─ __init__.py
│     ├─ schema.py
│     ├─ io.py
│     ├─ identifiability.py
│     ├─ virtual_work.py
│     ├─ elasticity.py
│     ├─ solver.py
│     ├─ synthetic.py
│     ├─ report.py
│     └─ cli.py
└─ tests/
```

不复制原始图像、机器原始文件或 MatchID 工程。`input/` 只保存可重建的派生输入，`results/` 只保存软件输出。

## 5. 统一数据接口

### 5.1 全场 CSV

每行代表一个帧中的一个 DIC 点：

```text
frame_id,point_id,x_mm,y_mm,u_mm,v_mm,exx,eyy,gxy,quality,valid,area_mm2
```

约定：

- `gxy` 是工程剪应变，满足 `tau_xy = Q66 * gxy`；
- `area_mm2` 是该点的积分权重；
- `valid` 为 `0` 的点不进入积分；
- 第一版不从位移数值微分应变，避免把平滑和差分规则隐藏在求解器中；
- 缺少单位、点标识、有效标记或积分权重时快速失败。

### 5.2 边界载荷 CSV

每行代表一个帧的边界合力：

```text
frame_id,time_s,fx_N,fy_N,sync_status
```

第一版只接收 `sync_status=verified` 的真实识别数据。合成基准使用 `sync_status=synthetic`。现有端点插值结果可以进入接口审查，但不能进入正式参数识别。

### 5.3 虚场 CSV

每行代表一个虚场在一个 DIC 点上的值：

```text
virtual_field_id,point_id,ux_star,uy_star,exx_star,eyy_star,gxy_star
```

每个虚场另有一条边界系数记录：

```text
virtual_field_id,loaded_ux_star,loaded_uy_star
```

当边界只提供合力时，外虚功按 `Fx * loaded_ux_star + Fy * loaded_uy_star` 计算。第一版不假设未知的局部牵引分布。

### 5.4 运行配置 JSON

```text
dataset_id
provenance
loading_mode
dic_mode
model
thickness_mm
field_csv
load_csv
virtual_field_csv
virtual_boundary_csv
fit_frame_ids
validation_frame_ids
```

`loading_mode` 只允许：

- `uniaxial_x`；
- `uniaxial_y`；
- `biaxial_field_from_uniaxial_loading`；
- `measured_biaxial`。

`dic_mode` 记录 `2d` 或 `stereo`，但第一版不会声称二者具有相同的面外误差水平。

## 6. L0 虚功与求解

未知参数向量定义为：

```text
q = [Q11, Q22, Q12, Q66]
```

对每个帧和每个虚场计算：

```text
A1 = h * Σ(area * exx * exx_star)
A2 = h * Σ(area * eyy * eyy_star)
A3 = h * Σ(area * (exx * eyy_star + eyy * exx_star))
A4 = h * Σ(area * gxy * gxy_star)
b  = Fx * loaded_ux_star + Fy * loaded_uy_star
```

组成 `Aq=b`，使用最小二乘求解。求解前必须检查：

- 行数不少于未知参数数；
- `A` 的秩为 4；
- 输入值有限且单位完整；
- 每个虚场在所有帧中能按 `point_id` 唯一对齐。

软件报告条件数，但第一版不设置无文献或无仿真依据的任意条件数阈值。秩不足时拒绝输出完整正交各向异性参数，并明确列出不可辨识状态。

求得刚度后转换为工程常数：

```text
E11, E22, nu12, nu21, G12
```

刚度矩阵必须满足对称性和正定性。若不满足，结果标记为物理不合格，不通过改变符号或裁剪参数掩盖错误。

## 7. 普通单轴基线

普通狗骨试样使用独立的基线命令，不调用完整四参数 VFM：

- 由声明的线性应变窗口拟合 `E`；
- 由横向与纵向应变拟合 `nu`；
- 若根据 `E、nu` 推导 `G`，输出必须带 `derived=true`；
- 单一加载方向不能通过检查时，禁止输出完整 `Q11、Q22、Q12、Q66`。

这条基线用于验证单位、符号、DIC 场平均和材料量级，不代替双轴场识别。

## 8. 合成验证基准

软件生成一个带明确 `synthetic` 标签的结构化二维网格，预设正定刚度 `q_true`、四个独立虚场和满足虚功方程的边界力。基准包含：

- 无噪声、满秩数据：应恢复预设参数；
- 交换 X/Y 坐标：应得到相应交换后的参数；
- 秩不足数据：必须拒绝完整参数识别；
- 错误剪应变约定：测试应暴露结果偏差；
- 非正定目标刚度：输入生成阶段应拒绝；
- `synthetic` 数据不得被标记为 `measured`。

合成基准只验证程序实现和可辨识性，不用于论文中的实验结论。

## 9. 命令行接口

第一版提供三个命令：

```text
pa12-vfm inspect CONFIG.json
pa12-vfm identify CONFIG.json --output RESULTS_DIR
pa12-vfm synthetic --output EXAMPLE_DIR
```

- `inspect` 只检查字段、单位、数据来源、同步状态、矩阵秩和可辨识性；
- `identify` 在检查通过后求解并生成结果；
- `synthetic` 生成可重复的已知解基准。

第一版不开发图形界面、非线性本构、自动虚场优化、有限元网格生成或 MatchID 私有 `.dat` 解析器。

## 10. 输出与追溯

一次成功识别输出：

```text
run_manifest.json
stiffness_parameters.csv
engineering_constants.json
virtual_work_residuals.csv
identifiability.json
identification_report.md
```

`run_manifest.json` 保存输入路径、数据来源标签、配置、拟合帧、验证帧和软件版本。报告必须明确区分测量值、推导值、模型预测值和合成值。

## 11. 错误处理

只在系统边界进行校验：CSV/JSON 输入、单位、枚举值、点和帧关联、同步状态、矩阵秩及物理正定性。内部函数依赖已验证的数据结构，错误直接抛出，不做静默默认、自动补零或猜测列名。

特别禁止：

- 缺失 `Fy` 时擅自把另一列复制为 `Fy`；
- 缺失横向应变时由纵向应变猜测完整双轴场；
- 把当前端点映射的力标记为 `verified`；
- 把合成数据写入真实结果目录而不保留来源标签。

## 12. 测试策略

实施时采用测试驱动开发。每个行为先写失败测试，再写最小实现。测试层次为：

1. CSV/JSON 模式和来源标签；
2. 刚度与工程常数双向转换；
3. 单个虚场的内外虚功计算；
4. 多虚场矩阵组装；
5. 满秩/秩不足可辨识性；
6. 合成已知解参数恢复；
7. 单轴基线不越权输出完整正交参数；
8. CLI 端到端结果文件。

真实数据不作为单元测试固定答案；真实输入接入后另做只读验收报告。

## 13. 成功标准

第一版完成必须同时满足：

- 合成无噪声基准在浮点容差内恢复预设 `Q11、Q22、Q12、Q66`；
- X/Y 交换测试通过；
- 秩不足数据拒绝输出完整参数；
- 普通单轴模式只输出其可辨识基线；
- 输出中始终保留 `measured、synthetic、model_predicted` 来源；
- 现有未经硬件验证的照片—力映射不能通过正式识别门；
- 全部自动化测试通过且无未解释警告；
- 原始图像、机器文件、MatchID 工程和现有分析结果均未被覆盖。

## 14. 后续阶段

L0 闭环通过后，才进入真实 MatchID 全场 CSV 适配、虚场优化、噪声/ROI/同步敏感性、独立双轴加载验证和非线性本构。后续阶段不属于本设计的第一版实现范围。
