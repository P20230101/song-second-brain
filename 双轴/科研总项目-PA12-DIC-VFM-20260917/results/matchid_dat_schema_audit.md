# MatchID `.dat` 字段 Schema 审计

更新时间：2026-09-17

## 证据范围

审计对象为：

`D:\C盘迁移\Desktop\yuan\data\XY\袁-20250529\XY-0.1-02\Test1\33061_1_16\Img000000.jpg.dat`

同目录的 `Job.m2inp` 记录了 MatchID 2D 19.2.2 工程设置：`Transformation=1`（affine）、Step=3 px、Subset=15 px、`Correlation=5`（ZNSSD）、`Strain$window=15`、`Strain$convention=1`（LOG Euler–Almansi）、`Strain$interpolation=1`（Q8）、`Export$unit=0`（pixels）、`Conversion=0.097519`，以及主 ROI 的像素边界。

`.dat` 的首个压缩成员可解析出 10,505 条 `<18>` 记录，每条 18 个分号分隔值。前 10,501 条属于主 ROI，最后 4 条对应额外种子点。结构统计为：

| 0 起始列 | 当前最小解释 | 证据 | 状态 |
|---:|---|---|---|
| 0 | 逐点序号候选 | 0–10,504 连续且无重复 | 结构确认 |
| 1–4 | ROI 包围框候选 | 主 ROI 内恒为 167、168、449、441，与 `<16>` ROI 设置一致 | 强候选 |
| 5–6 | 子集中心坐标候选 | 主要为 3 px 网格量，受 ROI/扫描顺序影响 | 候选 |
| 7–8 | 平移/位移候选 | `Transformation=1` 时与六个连续局部变换量成组，跨帧均值随加载变化 | 候选 |
| 9–12 | 局部仿射变换参数候选 | 六个连续量与 affine 变换自由度相匹配；不能直接命名为 `exx/eyy/exy` | 候选，禁止直接作应变 |
| 13 | `R` 质量指标候选 | 主 ROI 首帧约为 1，跨帧可下降；与独立 CSV 的 `R` 量纲/范围相似 | 候选 |
| 14 | `Sigma` 质量指标候选 | 首帧主 ROI 近零，末端和低质量点增大；与独立 CSV 的 `Sigma` 量纲/范围相似 | 候选 |
| 15–17 | ROI、有效性或扫描索引候选 | 离散值/重复结构明显，但没有公开字段定义 | 未命名 |

## 结论

当前已经证明“`.dat` 是可读的 MatchID 全场 payload，并含逐点局部求解信息”，但没有证明私有 `<18>` 记录的官方字段名。特别是字段 9–12 不能直接作为 VFM 的应变列；如需应变，应使用带表头的 MatchID 导出，或依据确认后的仿射参数定义和应变约定重新计算，并保留独立复核。

公开资料建议 MatchID 结果优先导出为开放 CSV；开源 FEMU-DIC 的 MatchID 转换入口使用 `X,Y,U,V,exx,eyy,exy` 七列，但这不能反向证明本项目私有 `.dat` 的内部顺序：[MatchID 软件](https://www.matchid.eu/software)、[FEMU-DIC 数据格式说明](https://github.com/BinChenOPEN/FEMU-DIC)。

因此 Gate 1/9 的状态更新为：全场 payload 入口已确认；字段 schema、最终有效掩膜、同步和边界力仍未闭合，暂不进入真实 VFM 参数识别。
