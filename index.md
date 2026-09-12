---
title: 首页
---

# 松的第二大脑

这是工程力学 PA12 双轴拉伸/压缩、3D DIC 与 VFM 研究的最小工作入口。原始资料只读，研究结论按证据写入 Wiki，日常实验结果只保留两张简版表。

## 日常只看

1. [研究上下文](wiki/研究上下文.md) — 当前题目、设备边界、已知事实和待确认问题。
2. [事件和频率概览](实验/PA12-双轴-DIC-VFM/results/02_事件和频率概览.md) — 加载、峰值、峰后和破坏候选帧。
3. [VFM 照片—力对应表](实验/PA12-双轴-DIC-VFM/results/01_VFM照片力对应.csv) — 一张照片一行，只保留四通道力和必要信息。

## 当前科研主线

- [阶段 1｜候选方向证据决策](wiki/阶段1-候选方向证据决策-2026-09-12.md) — 当前唯一研究问题、证据缺口和下一步顺序。
- [工程力学｜双轴试验-DIC-VFM研究路线](wiki/工程力学-双轴DIC-VFM研究路线.md) — 从选题到论文的阶段闸门。
- [双轴-DIC-VFM｜两篇核心文献研读与 PA12 路线](wiki/双轴-DIC-VFM-两篇核心文献研读-PA12路线.md) — 设备案例与 PA12 基线。
- [双轴-DIC-VFM｜同步采集与预试验方案](wiki/双轴-DIC-VFM-同步采集与预试验方案.md) — 触发、帧—力映射和质量闸门。
- [VFM 软件识别闭环与本构参数验收](wiki/VFM软件识别闭环与本构参数验收.md) — 3D DIC 场量、边界力、VFM/FEMU 与独立验证。
- [yuan｜仿真与实验数据深入分析](wiki/yuan-仿真与实验数据深入分析-2026-09-12.md) — `yuan` 数据事实、字段缺口和复现入口。

## 文献与工具（需要时使用）

- [文献捕获与筑巢](wiki/文献捕获与筑巢.md)
- [MinerU PDF 解析与图文研读流程](wiki/MinerU-PDF解析与图文研读流程.md)
- [Semantic Scholar 下载配置](wiki/Semantic-Scholar下载配置.md)
- [科研流水线 SOP](wiki/科研流水线SOP.md)

## 实验、原始资料与审计

- [实验区说明](实验/README.md)
- [全量照片—力—DIC 配对清单](实验/PA12-双轴-DIC-VFM/07_全量照片-力-DIC配对清单.md)
- [XZ 图像—DIC 元数据审计表](实验/PA12-双轴-DIC-VFM/results/审计/xz_image_dic_inventory.md) — 缺 `XZ.z01` 的力字段不填。
- [原始资料说明](raw/README.md)

详细技术 CSV/Markdown 统一放在 `实验/PA12-双轴-DIC-VFM/results/审计/`，不作为日常入口；原始 PDF、图片、机器数据和 MinerU 私有产物不发布到公开仓库。

## 按日期查看报告

- [科研报告中心](研究报告/README.md)
- [论文启发与 GitHub 工作时间线](wiki/论文启发与GitHub工作时间线.md)
- [维护日志](log.md)

## 固定规则

- [Wiki 页面说明](wiki/README.md)
- [AGENTS.md](AGENTS.md)
- 每晚 21:00 自动任务只处理当天变化；以本页两个简版文件为日常结果入口，删除前检查引用并记录路径。
