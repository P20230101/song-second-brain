---
title: MatchID 2019｜2D DIC 字段映射
type: experiment-interface
status: real-phase-blocked-pending-common-time-and-boundary-force
domain: 工程力学
updated: 2026-09-18
---

# MatchID 2019｜2D DIC 字段映射

## Phase 6 实际检查（2026-09-18）

已对真实 `XY_Y-09-0.1-02` 的 `Job.m2inp` 和 1,825 个逐帧 `.dat` 执行接入检查。`.dat` 可逐帧解析，但 `MatchIDReader.exe` 将 `Job.m2inp` 作为 Dataset 参数时没有返回 `IDataset`，退出码为 `-532462766`，未生成正式 CSV。真实候选输出见 [Phase 6 接入记录](../../wiki/02_实验与VFM/Phase6-真实MatchID数据接入-2026-09-18.md)。

因此本页的“必须确认的逻辑字段”仍不能填入私有 `.dat` 的候选列；字段 7/8、9–12 和估计时间/力映射均保持候选或阻断状态。

对真实 `XY_Xy-0.1-01` 的派生工程执行了 MatchID 2019.2.2 运行：先将工程中的旧图像根路径重写为真实 D 盘路径，再直接运行工程，得到 289 个非空正式 CSV。CSV 表头锁定为 `X[Pixels];Y[Pixels];U[Pixels];V[Pixels];R;Sigma;Exx;Eyy;Exy;E1;E2;Gamma;VonMises`；归一化输出见 [正式 VFM 输入](real_data_pipeline/runs/XY_Xy-0.1-01/formal_vfm_input.csv.gz)，运行记录见 [MatchID 运行记录](real_data_pipeline/runs/XY_Xy-0.1-01/matchid_export_runtime.json)。

正式归一化表 `formal_vfm_input.csv.gz` 的实际表头还保留了帧/点 ID、毫米坐标和位移、`exx/eyy/exy`、`quality_r/quality_sigma/valid`、候选像素字段、`source_dat`、`conversion_mm_per_px`、估计时间/力、同步状态和边界力字段；`matchid_export_runtime.json` 记录 289 个非空 CSV、3,034,764 行。这个字段确认只对 `XY_Xy-0.1-01` 有效，不能自动推广到其他私有 `.dat`。

本页是接口模板，不假设 MatchID 2019 的具体列名或导出格式。拿到实际 CSV、MAT、HDF 或工程文件后，按“一列一字段”填写，并把原始文件只读保存到 `raw/设备/` 或对应试验目录。

## 必须确认的逻辑字段

| 逻辑字段 | 实际文件/列名 | 单位 | 坐标/时间基准 | 是否存在 | 备注 |
|---|---|---|---|---|---|
| `frame_id` | `frame_id`（归一化表） | — | 图像序列 | `XY_Xy-0.1-01` 已确认 | 289 帧；其他 `.dat` 待核对 |
| `t_frame` | `time_s` / `time_s_est` | s | 端点锚定/共同触发假设 | 该试样接口已确认，独立时钟未证实 | 不得当作硬件时间戳 |
| `x`, `y` | `x_mm`, `y_mm`；另保留像素候选列 | mm / px | ROI 坐标系 | 该试样已确认 | 标定列为 `conversion_mm_per_px` |
| `u`, `v` | `u_mm`, `v_mm`；另保留像素候选列 | mm / px | 同上 | 该试样已确认 | 正方向仍需与力通道交叉核对 |
| `exx`, `eyy`, `exy` | `exx`, `eyy`, `exy` | MatchID 输出定义 | ROI/应变设置 | 列名已确认，定义与阈值待核对 | 不把列名等同于已验证应变契约 |
| `correlation_quality` | `quality_r`, `quality_sigma` | 软件定义 | DIC 质量指标 | 该试样已确认 | 阈值和最终剔除规则待核对 |
| `roi_mask`/缺失标记 | `valid`, `valid_quality_candidate` | — | ROI 网格 | 该试样已确认 | 区分边缘缺失、遮挡和低相关仍待审计 |
| 标定参数 | `conversion_mm_per_px` | mm/px | MatchID 工程 | 该试样已确认 | 需与工程设置/已知尺寸复核 |
| subset/step/strain window | 工程/导出记录中待抽取 | px | DIC 设置 | 待确认 | 不从私有 `.dat` 候选列反推 |

## 导出核对顺序

1. 先用 3–5 帧确认 `frame_id` 单调、无重复、能回指原始图像。
2. 再确认坐标单位、原点和正方向，并用已知长度做比例检查。
3. 比较位移场的刚体平移/旋转是否符合加载方向；不要先计算 VFM。
4. 记录相关质量、缺失点和边缘剔除比例；原始场与处理后场分开保存。
5. 将实际列名写回本页，再由同步页建立 `frame_id → t_force/t_disp` 映射。

## 等待用户提供

- 一份 MatchID 2019 导出的原始样例（可先脱敏）；
- 导出对话框或工程设置截图；
- 相机触发、试验机/DAQ 采样时钟和通道说明；
- 与样例对应的一小段力—位移数据。
