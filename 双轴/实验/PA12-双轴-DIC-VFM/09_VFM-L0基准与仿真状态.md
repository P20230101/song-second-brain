# VFM L0 基准与仿真状态（2026-09-15）

## 已完成

- 建立独立于 MatchID 的二维平面应力 VFM 最小求解器：输入逐点 `exx、eyy、gxy`、积分面积、厚度、虚场和边界合力，求解 `Q11、Q22、Q12、Q66`。
- 合成已知解闭环：真值 `[420, 360, 110, 150] MPa`，矩阵秩 4，条件数 28.73；无噪声最大相对误差 `2.1×10^-15`。
- 固定随机扰动敏感性：1% 应变/载荷扰动最大参数误差 2.33%，2% 为 8.79%，均通过“相对误差≤10%”门；5% 和 10% 扰动未通过。这说明当前虚场数量和布置可作为基准，但不能把 90% 精度外推到真实数据。
- 输出目录：`vfm/examples/synthetic_l0/`，包括 `field.csv`、`virtual_fields.csv`、`virtual_boundary.csv`、`result.json`、`noise_sensitivity.csv`。
- 提供并运行 Abaqus/CAE 2025 基准脚本 `simulation/abaqus_biaxial_benchmark.py`：100×100 mm、厚度 2 mm、CPS4R、E=300 MPa、ν=0.35 的双轴平面应力模型；ODB 已由桥接会话生成，并已导出节点位移和积分点应力/应变。

## 文献交叉结论

1. VFM 的核心是将全场测量代入虚功原理，通过合适虚场直接识别本构参数；参数可辨识性取决于应变场异质性和虚场矩阵秩，而不是只看全局力—位移曲线。[Grédiac 等 VFM 综述](https://doi.org/10.1111/j.1475-1305.2006.tb01504.x)
2. 特殊几何和有限元“虚拟试验”可在一次加载中制造多种应变状态，再用 DIC 全场和 VFM 识别多个刚度常数；公开验证案例的误差约 0.71–5.94%，但材料为复合材料，不能直接当作 PA12 结果。[单试样各向异性 VFM](https://doi.org/10.1016/j.compositesb.2020.108338)
3. 聚合物双轴试验中，局部应变场与整体响应共同约束本构模型；仅依靠力—位移不足以区分材料本构和试样结构效应。[玻璃态聚合物双轴试验](https://doi.org/10.1016/j.ijsolstr.2016.10.013)
4. DIC 与有限元模型联合校准时，ROI、测量噪声和重建参数都会改变识别常数，必须做敏感性与独立验证。[DIC-FEMU 不确定度研究（ScienceDirect）](https://www.sciencedirect.com/science/article/pii/S0263822317320482)
5. 同步不是形式要求：已有聚合物多轴系统明确记录应力与应变同步，并报告图像处理延迟会影响反馈信号。[聚合物多轴 DIC 同步系统（ScienceDirect）](https://www.sciencedirect.com/science/article/pii/S0142941805001029)

## 当前门状态

- D1 数学契约：`PASS`（合成无噪声闭环）。
- D3 合成闭环：`PASS`（满秩、参数恢复、扰动敏感性已输出）。
- Abaqus ODB：`PASS`（桥接会话求解完成；ODB 原件位于 `D:\SIMULIA\Commands\PA12_Biaxial_Benchmark_20260915.odb`，派生 CSV 位于本项目 `simulation/`）。
- D2/D5 真实数据识别：`BLOCKED`。`yuan` 目录已有 MatchID 2019 `.dat` 和若干曲线 CSV，但尚未提供包含逐点二维 `exx、eyy、gxy`、单位、ROI、厚度、边界力和已验证同步的完整导出，因此当前不能合法计算真实 VFM 参数。

## 下一步

1. 将已导出的 Abaqus 场量转为统一 CSV，与 Python VFM 结果交叉核对；如需重新计算，先把 Abaqus 当前工作目录设为项目 `simulation/`，避免 ODB 与后处理路径分离。
2. 从 MatchID 2019 导出一个试验的参考帧、3–5 个加载帧的逐点二维场，保留列名和单位；不要只提供截图或单条剖面曲线。
3. 提供该试验的厚度、ROI/边界定义、四通道力的物理含义和共同触发/时间戳。未经验证的端点插值只能做敏感性分析，不能标为 `verified`。
4. 先在弹性窗口识别 `Q`；通过独立加载路径验证后，再决定是否扩展到 PA12 的弹塑性/黏弹性模型。

## 保护边界

本页和 `vfm/` 只保存可复现的派生输入与结果；没有复制、删除或覆盖 `D:\C盘迁移\Desktop\yuan\data` 下的原始图像、力文件和 MatchID 工程。
