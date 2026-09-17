# Abaqus ODB 实际打开与场量抽取验证

更新时间：2026-09-17

## 验证目的

确认 M0–M2 synthetic 基准的 ODB 不只是生成了文件，而且能够由 Abaqus/Standard 的 Python 解释器以只读方式打开、读取完整加载步并抽取 VFM 所需场量。该验证属于 synthetic FE 接口验收，不是 PA12 实验验证。

## 方法与命令

验证脚本为 `simulation/constitutive_virtual_experiment/extract_odb_history.py`。脚本调用 `odbAccess.openOdb(..., readOnly=True)`，逐帧要求 `Load` 步、`SPECIMEN-1` 实例以及 `E`、`S`、`PEEQ`、`RF` 场，并按 692 个 CPS4R 单元重建应变、真应力、PEEQ 和八个离散虚场的内外虚功。抽取结果写入 D 盘项目目录下的私有 `working/odb_open_validation/`，不进入 Git。

实际验证了以下 9 个 ODB：

| ODB | 帧数 | 单元数 | 最大 PEEQ | 真应力场内/外虚功相对误差 |
|---|---:|---:|---:|---:|
| `VE_M0_UX.odb` | 23 | 692 | 0.113954 | `5.82e-6` |
| `VE_M0_EQ.odb` | 23 | 692 | 0.118594 | `1.97e-5` |
| `VE_M0_R05.odb` | 23 | 692 | 0.111595 | `5.45e-6` |
| `VE_M1_UX_DENSE.odb` | 23 | 692 | 0.057626 | `1.81e-6` |
| `VE_M1_EQ_DENSE.odb` | 23 | 692 | 0.071624 | `4.98e-6` |
| `VE_M1_R05_DENSE.odb` | 23 | 692 | 0.065029 | `9.79e-7` |
| `VE_M2_UX_DENSE.odb` | 23 | 692 | 0.091587 | `4.40e-6` |
| `VE_M2_EQ_DENSE.odb` | 23 | 692 | 0.103198 | `5.10e-6` |
| `VE_M2_R05_DENSE.odb` | 23 | 692 | 0.098165 | `1.93e-5` |

## 结论与边界

- 9/9 ODB 实际打开并完成逐帧抽取，Abaqus 文件可用性通过。
- 所有作业均含当前 nonlinear FE–VFM 基线所需的应变、应力、PEEQ 和反力场；内外虚功闭合误差处于 `9.79e-7`–`1.97e-5`。
- 这只通过 synthetic Gate 3 的文件/场量与物理闭合子门，并支持 synthetic Gate 4 的真参数回收；不证明真实 PA12、真实 MatchID-DIC 字段、实验同步或四通道力传感器契约已经闭合。
