---
title: 实验区
---

# 实验区（代码与图像）

这里保存已获确认的实验脚本、`.ipynb`、模型输出和图片。原始 PDF 与原始数据仍放在 `raw/`，研究结论和证据链写入 `wiki/`。当前工程力学主线为双轴拉伸/压缩试验结合 DIC 与 VFM，正式实验前必须完成设备能力核对和预试验。

建议每个项目使用：

```text
实验/<项目名>/
├── README.md
├── protocols/
├── calibration/
├── notebooks/
├── scripts/
├── data/
├── results/
├── figures/
└── manuscript/
```

双轴-DIC-VFM 的固定阶段、闸门和输出文件见 [`wiki/工程力学-双轴DIC-VFM研究路线.md`](../wiki/工程力学-双轴DIC-VFM研究路线.md)；通用阶段门控和人工确认规则见 [`wiki/科研流水线SOP.md`](../wiki/科研流水线SOP.md)。
