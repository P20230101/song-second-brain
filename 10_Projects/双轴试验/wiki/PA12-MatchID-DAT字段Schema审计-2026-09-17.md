---
title: PA12 MatchID .dat 字段 Schema 审计
date: 2026-09-17
tags:
  - PA12
  - MatchID
  - DIC
  - 数据审计
---

# PA12 MatchID `.dat` 字段 Schema 审计

## 结论

主试样 `XY-0.1-02` 的 259 个 `.dat` 均可解压并解析；首帧 `<18>` 记录包含 10,505 条、每条 18 个值。`Job.m2inp` 同时确认了 affine、Step=3 px、Subset=15 px、LOG Euler–Almansi、Q8、像素导出和 `0.097519 mm/px`。

当前可以确认全场 payload 入口，但不能把私有 `<18>` 记录当作已有官方列名表：

- 字段 7–8 是位移候选；
- 字段 9–12 更符合 affine 局部变换参数候选，不直接作为 `exx/eyy/gxy`；
- 字段 13–14 是 `R/Sigma` 质量指标候选；
- 其余字段仍保留为内部索引、ROI 或有效性候选。

因此真实 VFM 仍需带表头的 MatchID CSV 或官方字段映射，并需另外闭合最终有效掩膜、单位、同步和边界力。

详细结构表和证据边界见[项目内审计页](../科研总项目-PA12-DIC-VFM-20260917/results/matchid_dat_schema_audit.md)。代码审计表已重生成，但不改变原始 `.dat`。
