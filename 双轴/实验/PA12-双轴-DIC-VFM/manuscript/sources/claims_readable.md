# Claim registry 可读版

机器审计所用的 `claims.csv` 遵循工具的严格 schema，主张正文以 SHA-256 绑定；本文件保留对应的可读文本、证据和状态，便于作者逐条打开来源核对。

| ID | 主张 | 证据 | 当前状态 | 使用位置 |
|---|---|---|---|---|
| C001 | PA12 SLS tensile response depends on build orientation and part thickness. | E007; E016 | 摘要级部分支持；需作者打开全文/核对 claim | 引言、讨论边界 |
| C002 | VFM identifies constitutive parameters by combining full-field kinematics, boundary loading and virtual work. | E001; E002; E011 | E001 摘要级部分支持；需作者打开全文/核对 claim | 理论基础 |
| C003 | Out-of-plane motion can bias 2D-DIC displacement/strain measurements and therefore VFM identification. | E003; E008 | 当前自动片段未支持；需作者打开原文/补充准确定位 | DIC 质量控制 |
| C004 | Missing deformation data near specimen edges and DIC noise can affect biaxial VFM parameter identification. | E004; E011 | E004 摘要级完全支持；需作者核对全文和 E011 | 敏感性分析 |
| C005 | Cruciform geometry influences gauge-zone homogeneity, load transfer and constitutive characterization. | E006; E013; E014 | E006 摘要级部分支持；需作者打开全文/核对 claim | 试样设计 |
| C006 | This project has no verified original experimental results, camera specification, sample count or calibration record at draft intake. | E017 | 已由工作区材料核实 | 数据状态/局限性 |
| C007 | The proposed study will treat specimen rather than image frame as the independent replicate. | E010 | 方法计划，需作者确认统计方案；不能由自动摘要代替 | 统计方案 |
| C008 | A claim of improved identifiability requires an independent loading path or specimen not used for fitting. | E001; E002; E004 | 方法计划，需作者确认验证方案并核对方法依据 | 独立验证 |
| C009 | DIC reporting requires hardware, calibration and processing metadata sufficient for reproducibility. | E009; E010; E018 | 当前自动片段未支持；需作者打开指南/原文核对 | DIC 参数报告 |
| C010 | The current XY dataset contains 10 image sequences and 5309 JPEG frames. | E019; E022 | 已由本地文件清点和可复算事实表核实 | 摘要、结果 |
| C011 | The effective force-record frequency across the current XY sequences is 997.50-1000.00 Hz. | E020; E022 | 已由 `Press.T` 和事实表核实 | 摘要、结果 |
| C012 | The endpoint map estimates image frequency as 7.98-375.66 Hz and uses force-onset/end anchors without a common trigger. | E020; E021 | 已由脚本规则和审计输出核实；估计量 | 方法、结果 |
| C013 | In XY_Xy-0.1-01, a hypothetical +/-1-frame registration shift can change channel force by about 1.59 kN at the post-peak-drop candidate. | E023 | 已由可复算情景分析核实；不是同步置信区间 | 摘要、结果、讨论 |
| C014 | All current XY sequences are marked vfm_eligible=false. | E020; E021 | 已由审计输出核实 | 结果、结论 |
| C015 | MatchID input-frame counts and unique DIC-CSV frame identifiers differ; XY_XY-0.1-02 has 10 input frames and 259 unique DIC-CSV frame identifiers. | E019; E020 | 已由本地文件清点和审计表核实 | 结果、讨论 |
| C016 | The current 2D-DIC exports have not been validated as a complete unit-bearing x,y,u,v,exx,eyy,exy,quality,valid-mask field table. | E019 | 已由导出字段审计核实 | DIC 质量、VFM 准入 |

## 变更规则

- 若正文主张改写，先更新本文件和 `claims.csv` 的哈希，再重跑 claim 审计。
- 若新增或删除证据，先更新 `references.json`、`source_manifest.json` 和本文件，再重跑 DOI、manifest、claim 三项审计。
- `source_opened=true` 只有在作者实际打开并确认来源内容后才能填写；Crossref 元数据通过不等于 claim 已被全文核实。
