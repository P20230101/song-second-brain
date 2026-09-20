---
title: Phase 6｜真实 MatchID 2019.2.2 数据接入
type: experiment-phase
status: blocked-pending-common-time-and-boundary-force
domain: 工程力学
updated: 2026-09-18
---

# Phase 6｜真实 MatchID 2019.2.2 数据接入

## 结论

真实 PA12 数据已经进入独立的 `real_data_pipeline`。修正派生工程中的旧图像根路径后，MatchID 2019.2.2 已完成真实 `XY_Xy-0.1-01` 的 289 帧计算，并生成 289 个非空带表头 CSV；真实 VFM 仍未开放，原因收窄为共同时间基准、边界合力契约和跨帧点标识。

本阶段停止 synthetic 测试，不扩展 AI，不把任何 synthetic 结果写入真实实验结果。

## 本次真实输入

- 试验：`XY_Y-09-0.1-02`
- 原始目录：`D:\C盘迁移\Desktop\yuan\data\XY\袁-20250529\Y-09-0.1-02\Test1\33061_1_22`
- MatchID 工程：`Job.m2inp`
- 逐帧数据：1,825 个 `Img*.jpg.dat` 和 1,825 张 JPEG
- 已有力映射：1,825 行 `xy_photo_force_sync.csv`，但其 `t_image_s_est` 是端点映射估计

另外执行了较小的真实试样 `XY_Xy-0.1-01`：289 张 JPEG、289 个 `.jpg.dat`、289 行力映射；MatchID 正式 CSV 共 289 个，归一化后的正式 VFM 布局为 3,034,764 行。该试样使用原始 `Job.m2inp` 的派生副本执行，原始工程保持不变。

## MatchID 接口检查

将原始 `Job.m2inp` 路径直接传给 `MatchIDReader.exe` 的 Dataset 参数，程序退出码为 `-532462766`，没有生成 CSV；这是 PLI 外部 Dataset 接口检查，不等于 MatchID 工程运行失败。进一步发现原始工程中的图像路径仍指向已迁移的旧盘路径，于是只在派生工程中重写为真实 D 盘路径。随后直接运行派生工程，MatchID 2019.2.2 完成 289 帧并生成 289 个非空正式 CSV。证据保存在 [MatchID 运行记录](../../实验/PA12-双轴-DIC-VFM/real_data_pipeline/runs/XY_Xy-0.1-01/matchid_export_runtime.json) 中。

这不是把 `.dat` 解析失败：`.dat` 已能逐帧解压和读取；阻断点在 MatchID PLI 的运行时连接和正式字段语义。

## 已生成的真实管线输出

- [运行 manifest](../../实验/PA12-双轴-DIC-VFM/real_data_pipeline/runs/XY_Y-09-0.1-02/run_manifest.json)
- [真实输入盘点](../../实验/PA12-双轴-DIC-VFM/real_data_pipeline/runs/XY_Y-09-0.1-02/inventory.json)
- [逐点候选字段](../../实验/PA12-双轴-DIC-VFM/real_data_pipeline/runs/XY_Y-09-0.1-02/field_candidates.csv.gz)
- [VFM 输入布局候选](../../实验/PA12-双轴-DIC-VFM/real_data_pipeline/runs/XY_Y-09-0.1-02/vfm_input_candidate.csv.gz)
- [管线说明](../../实验/PA12-双轴-DIC-VFM/real_data_pipeline/README.md)
- [Xy-0.1-01 运行记录](../../实验/PA12-双轴-DIC-VFM/real_data_pipeline/runs/XY_Xy-0.1-01/matchid_export_runtime.json)
- [正式 MatchID→VFM 输入](../../实验/PA12-双轴-DIC-VFM/real_data_pipeline/runs/XY_Xy-0.1-01/formal_vfm_input.csv.gz)
- [正式输入 manifest](../../实验/PA12-双轴-DIC-VFM/real_data_pipeline/runs/XY_Xy-0.1-01/formal_manifest.json)

Y-09 的两份候选逐点输出各含 1,042,512 行。由于该试样尚未完成正确的派生工程路径重定位，正式字段仍保持为空。

`XY_Xy-0.1-01` 的 MatchID 正式 CSV 表头为 `X[Pixels];Y[Pixels];U[Pixels];V[Pixels];R;Sigma;Exx;Eyy;Exy;E1;E2;Gamma;VonMises`。按工程 `0.096193 mm/px` 转换后，`x_mm/y_mm/u_mm/v_mm/exx/eyy/exy/quality_r/quality_sigma` 已正式绑定；`time_s/fx_N/fy_N` 留空，估计值仅保留在 `_est` 列。原始目录内的旧 `Serie;X;Y` 系列/剖面 CSV 未被混入正式全场输入。

## 当前运行纪律

- synthetic 测试进程已停止并复核为 0 个匹配进程；
- 本阶段没有调用 AI 模块，也没有将模拟结果写入真实管线；
- 原始 `D:\C盘迁移\Desktop\yuan\data` 下的图像、`.dat`、工程和力文件保持只读。

## VFM 准入状态

`vfm_eligible=false`。当前阻断项：

1. 当前正式 VFM 输入尚未绑定共同触发或逐帧相机时间；
2. 四通道力尚未完成物理边界合力契约；
3. MatchID CSV 没有跨帧稳定点标识，当前 `point_id` 明确标为帧内行号；
4. Y-09 仍需按同样的旧路径重定位规则完成正式导出。

## 解除阻断的最小动作

1. 为 Y-09 派生工程重写旧图像根路径并完成正式导出；
2. 提供相机—试验机共同触发或可追溯时间戳，再重建 `frame_id → t_force → Fx/Fy`；
3. 确认跨帧点标识或采用明确的网格重采样契约；
4. 仅在上述证据通过后进入真实 VFM 识别。
