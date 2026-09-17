# Abaqus–VFM Stage-A Gate 审计

更新时间：2026-09-17

## 审计对象

本审计只读打开项目已有的三个十字形基准 ODB：

- `双轴/实验/PA12-双轴-DIC-VFM/simulation/fixture_optimization/jobs/FO_G00_reference_UX.odb`
- `双轴/实验/PA12-双轴-DIC-VFM/simulation/fixture_optimization/jobs/FO_G00_reference_EQ.odb`
- `双轴/实验/PA12-双轴-DIC-VFM/simulation/fixture_optimization/jobs/FO_G00_reference_R05.odb`

它们是 Abaqus 线弹性基准，不是当前 FS3300PA 的实验真值模型。输入卡材料参数为 `E=300 MPa, ν=0.35`；几何、厚度分区和四侧位移边界均来自仿真输入卡。

## 独立闭环

ODB 同时提供 `U`、`S`、`E` 和 `RF`。重算脚本从 ODB 独立读取单元应变、应力和节点反力；虚位移在单元节点上赋值，再用 CPS4R 双线性形函数插值到约化积分点。这样，内部虚功和外部反力虚功使用同一离散运动学/积分规则，避免把连续多项式导数直接套到单点积分单元上。

## 结果

| 路径 | 元素数 | A 秩 | A 条件数 | 外功/内功相对误差 | 外部反力右端项最大相对参数误差 |
|---|---:|---:|---:|---:|---:|
| UX | 692 | 4 | 31.0373 | 3.61e-7 | 2.18e-5 |
| EQ | 692 | 4 | 26.5941 | 2.28e-7 | 2.04e-5 |
| R05 | 692 | 4 | 25.4417 | 2.48e-7 | 2.15e-5 |

三条路径均为满秩，且外部反力右端项可回收输入的四个线弹性基准参数。具体原始 JSON 为：

- `abaqus_vfm_recompute_UX.json`
- `abaqus_vfm_recompute_EQ.json`
- `abaqus_vfm_recompute_R05.json`

## Gate 判定

- `Gate 3`（Stage-A 基准：独立 FE 场量、边界反力、离散虚功闭环）：通过。
- `Gate 4`（Stage-A 基准：无噪声回收线弹性真参数）：通过。
- 项目总 Gate 3/4：仍为“基准通过、真实 PA12 阻塞”。原因是当前基准还没有使用真实 PA12 材料、真实 MatchID-DIC 场、实验力通道映射、同步残差或 M0–M2 模型形式比较。

## 可复现入口

使用 Abaqus Python 只读运行：

```text
abaqus python scripts/audit_abaqus_vfm_odb.py --odb-path <ODB> --vfm-json <已有结果 JSON> --output-json <审计 JSON>
abaqus python scripts/recompute_vfm_from_abaqus_odb.py <ODB> <输出 JSON>
```

该审计没有复制、修改或覆盖 ODB。后续进入真实 PA12 前，必须另外闭合 `.dat` 字段 schema、单位、有效掩膜、四通道边界合力和图像—力时间映射。
