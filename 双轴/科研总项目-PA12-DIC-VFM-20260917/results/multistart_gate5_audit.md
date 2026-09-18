# Gate 5｜M0–M2 多初值识别审计

初审日期：2026-09-17；统一预算复算验收：2026-09-18。数据为通用 synthetic FE–VFM 基准，不是实测 PA12 参数。

## 试验契约

- 固定随机种子：`20260917`；每个模型 20 个 LHS 初值。
- 识别路径：UX + EQ；R05 为完全留出的比例路径。
- 参数来自同一模型真值，目标函数使用 VFM 虚功残差；不混入真实 DIC、同步或实验力数据。
- M0、M1 原运行使用 `max_nfev=60` 且均在该预算内收敛；M2 首轮使用 `40`，统一验收复算使用 `120`。原触限实例与复算结果同时保留，不能通过删除起点隐藏预算敏感性。

## 结果

| 拟合模型 | 起点 | 收敛 | 失败/触限 | nfev | 参数标准差 | 最好/中位/最差最大相对参数误差 |
|---|---:|---:|---:|---:|---|---|
| M0 | 20 | 20 | 0 | 见 JSON | `[1.28e-8, 4.49e-7]` | `1.4208e-5 / 1.4217e-5 / 1.4224e-5` |
| M1 | 20 | 20 | 0 | `8–39` | `[1.16e-8, 1.05e-7, 7.59e-7]` | `2.3430e-4 / 2.3431e-4 / 2.3440e-4` |
| M2 | 20 | 20 | 0 | `13–44` | `[1.167e-6, 3.645e-9, 2.578e-8]` | `1.2856e-3 / 1.2868e-3 / 1.2874e-3` |

M1 的 UX/EQ 训练虚功相对误差为 `2.99e-6/6.11e-6`，R05 留出虚功误差为 `2.12e-6`。M2 的对应值为 `4.24e-6/5.52e-6` 和 `1.92e-5`；这些误差均不能替代多初值稳定性判断。

## M2 预算敏感性

在首轮 `max_nfev=40` 运行中，`start_index=13` 曾触限：

- 初值：`[K=48.112754, eps0=0.00555614, n=0.455954]`；
- 终点：`[K=18.498080, eps0=0.0115735, n=0.190999]`；
- 当时 `status=0`、`nfev=40`，cost 为 `1.0880e-8`。

完整工作环境以同一 20 点 LHS、固定 seed 和 `max_nfev=120` 复算后，20/20 全部收敛，实际 `nfev=13–44`，最差 cost 为 `2.425950477e-11`。因此首轮现象是优化预算截断；该起点没有被删除或替换。

## Gate 判断

- 按统一验收预算 `max_nfev=120`，M0/M1/M2 均为 20/20 收敛且参数散布很小，synthetic Gate 5 通过。
- M2 首轮 40 次预算的触限证明结果对优化预算敏感；后续运行上限必须覆盖已观测的 `nfev=44`，不能把较低预算的截断解释为材料不可辨识。
- 该结论只覆盖当前 synthetic FE–VFM 参数盒、固定 seed 和路径组合，不是实际 PA12 的全局可辨识性结论。

## 完整环境复算状态

早期 Abaqus 2025 SMApy 路径曾在 SciPy–MKL LAPACK 工作区报错；该结果只说明该运行时不适合复算，不能作为模型证据。随后使用生成原始结果的完整 SciPy/joblib 工作环境完成 `max_nfev=120` 的 20-start 复算并通过验收，故 Gate 判断以完整环境结果为准，同时保留 SMApy 故障记录作为运行环境限制。

## 下一步约束

后续 M2 多初值运行使用至少 `max_nfev=120` 或等效、已验证的终止预算，并继续保存全部起点。下一步是 profile likelihood、多 seed 噪声和 Gate 7 FIM/路径信息分析；所有结果继续保持 synthetic 标签，不外推为真实 PA12 结论。

机器可读原始结果：

- [M0 20-start](../../实验/PA12-双轴-DIC-VFM/simulation/constitutive_virtual_experiment/results/M0_multistart_20.json)
- [M1 20-start](../../实验/PA12-双轴-DIC-VFM/simulation/constitutive_virtual_experiment/results/M1_multistart_20.json)
- [M2 20-start，40 次预算](../../实验/PA12-双轴-DIC-VFM/simulation/constitutive_virtual_experiment/results/M2_multistart_20.json)
- [M2 20-start，120 次验收预算](../../实验/PA12-双轴-DIC-VFM/simulation/constitutive_virtual_experiment/working/M2_multistart_20_maxnfev120.json)
