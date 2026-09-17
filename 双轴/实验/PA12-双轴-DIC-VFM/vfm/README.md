# VFM L0 基准

这是独立于 MatchID 的最小二维平面应力 VFM 求解基准。它只接受已明确列名、单位和来源的逐点应变 CSV，不读取 `.dat/.m2inp` 私有工程。

运行：

```powershell
python vfm_l0.py
```

程序会在 `examples/synthetic_l0/` 生成合成场并识别 `Q11,Q22,Q12,Q66`。当前合成实现只能作为代数矩阵原型：必须先修正位移—应变相容性、独立边界反力和噪声统计后，才能称为物理 Virtual Experiment。合成数据的 `sync_status=synthetic`，不能作为真实 PA12 结论。真实数据须在提供完整二维场、厚度、ROI、边界力和已验证同步后再接入。
