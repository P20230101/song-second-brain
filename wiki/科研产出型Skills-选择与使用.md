---
title: 科研产出型 Skills 选择与使用
type: research-tooling
status: active
domain: 工程力学｜双轴试验-DIC-VFM｜PA12
updated: 2026-09-12
---

# 科研产出型 Skills 选择与使用

## 先给结论

真正能帮助你拿出成果的不是安装最多的技能，而是让每一次对话都留下可复核的研究资产：

```text
检索候选 → 验证来源 → MinerU 解析 → 方法矩阵 → 缺口与假设
→ 试验设计 → 同步/DIC/VFM 预试验 → 原始数据与元数据
→ 统计与不确定度 → 交叉验证 → 图表 → 论文稿件
```

本机已经具备这条链的大部分能力。我补充安装了三个缺口最小、产出最直接的技能：

| 状态 | 技能 | 安装位置 | 直接解决的问题 |
|---|---|---|---|
| 已安装 | `literature-research` | `C:\Users\Administrator\.codex\skills\literature-research` | 多库检索、前后向引文追踪、覆盖矩阵、缺口验证 |
| 已安装 | `experiment-design` | `C:\Users\Administrator\.codex\skills\experiment-design` | 单变量隔离、基线/消融矩阵、资源估计、分析计划 |
| 已安装 | `mineru` | `C:\Users\Administrator\.codex\skills\mineru` | PDF/Office → Markdown、图片、表格/公式和 Obsidian 输出 |

前两个技能来自 [fcakyon/phd-skills](https://github.com/fcakyon/phd-skills) 的独立技能目录；它的仓库还提供论文—代码—数据审计、复现和审稿防守能力。由于该仓库的完整形态是 Claude Code 插件，本机只安装了能直接被 Codex 调用的两个目录，没有把整套插件强行当作 Codex 插件安装。`mineru` 来自 [nebutra/mineru-skill](https://github.com/nebutra/mineru-skill)，是 MinerU API 的统一入口，不会改变当前 API 后端的解析能力。

## 已有技能如何组成科研流水线

下面的分工是固定的。重复安装同类技能不会增加证据质量；需要的是在正确阶段调用正确技能。

| 科研阶段 | 已有/新增技能 | 你会得到的文件或结果 | 本项目的落点 |
|---|---|---|---|
| 1. 发现文献 | `gpt-researcher`、`literature-research`、`paper-lookup`、`research-lookup` | 检索式、候选论文、去重后的 DOI/arXiv/Semantic Scholar 记录、下载清单 | `raw/参考文献/<批次>/download_manifest.json` |
| 2. 解析和方法提取 | `mineru`、`paper-analyzer`、`extract-methodology` | 非 OCR 的 Markdown、图片目录、公式/表格位置、材料/试样/加载/DIC/VFM 字段 | `raw/参考文献/<批次>/MinerU/`、`实验/PA12-双轴-DIC-VFM/02_文献方法矩阵.md` |
| 3. 证据质量 | `source-quality-appraiser`、`citation-and-reference-validator`、`citation-management` | 发表版本核对、作者/年份/期刊核对、可追溯引用和证据等级 | `wiki/双轴-DIC-VFM-种子文献筛选.md`、证据矩阵 |
| 4. 缺口与问题 | `literature-review`、`research-question-builder`、`hypothesis-generation`、`scientific-critical-thinking` | 研究现状、已知证据、来源缺口、2–4 个可证伪候选 RQ/假设 | `wiki/研究上下文.md`、每日闭环页 |
| 5. 试验设计 | 新增 `experiment-design`、`experimental-design`、`research-design-planner` | 因素/水平、基线、重复数、加载路径、停止条件、分析计划 | `实验/PA12-双轴-DIC-VFM/01_设备与同步核对表.md`及预试验方案 |
| 6. 数据与不确定度 | `exploratory-data-analysis`、`data-scientist-analyst`、`statistical-analysis`、`statistical-power`、`uncertainty-and-units` | 清洗规则、单位、误差传播、重复性、置信区间、异常记录 | `实验/<项目>/results/` |
| 7. DIC/VFM 与图表 | `model-evaluator-validator`、`scientific-visualization`、`scientific-schematics`、`matplotlib`、`matlab` | 场量质量检查、VFM 参数识别/验证、出版级图表和流程图 | `实验/<项目>/results/`、论文图表索引 |
| 8. 综合与写作 | `synthesize-research`、`scientific-writing`、`citation-management` | 研究叙事、方法/结果/局限、引用和审稿前自检 | `wiki/<项目>-论文大纲.md`、论文稿件 |

## 为什么这些技能对“拿出成果”有用

### `literature-research`：把“我感觉没人做过”变成可核查的缺口

它要求先定义检索边界和纳入/排除标准，再做多种表述检索、前向/后向引文追踪、期刊/会议挖掘和 GitHub 实现检索。每个候选缺口都要用至少三种表述复查，并标记置信度。

对本项目的价值是把“PA12 双轴 + DIC + VFM”拆成可检索的子问题：

- 双轴试样和加载路径；
- 2D DIC 的散斑、标定、应变空间分辨率；
- 图像帧与力/位移数据的触发和时钟映射；
- VFM 的场量、虚场、本构参数可辨识性；
- PA12 的各向异性、应变率和独立加载路径验证。

产出不是一段泛泛综述，而是“论文—方法—证据—局限—可复现实验”的矩阵。

### `experiment-design`：让有限的机时优先回答一个能发表的问题

它强制每个实验先写假设、因变量、自变量和基线；单变量比较时只改变一个因素；多因素时先计算总试验数、时间和存储；执行前先规定指标、统计检验和图表。

这正好对应你的约束：双轴机容量、行程和可用试样数有限，不能一开始铺开很多材料和加载路径。第一篇小论文应先选择一个最小闭环问题，等同步、DIC、VFM 和交叉验证稳定后再扩展为大论文。

### `mineru`：让全文研读留下可定位的原始证据

它把 PDF 转成 Markdown，并把图片、表格和公式位置分开保存，适合在 Obsidian 中链接。对于原生文本 PDF，固定使用非 OCR 路径；只有扫描件或明确缺字时才讨论 OCR。当前项目已经采用 MinerU 解析并在 `raw/参考文献/` 保留 PDF 原件、Markdown、图片和清单。

### 其余已有技能：把证据转成可复核结果

`source-quality-appraiser` 和引用校验避免把预印本、二手摘要或错误元数据当成证据；`uncertainty-and-units` 避免把像素、毫米、应变、力和时间单位混用；`scientific-visualization` 和 `scientific-writing` 把结果变成可审阅的图表和论文段落。这些环节看似不“炫”，但决定了结果能否被复现和审稿。

## 相机参数到底重不重要

需要把“相机型号”与“测量参数”分开：

| 当前阶段 | 相机型号是否阻塞 | 必须做什么 |
|---|---|---|
| 选题和文献筛选 | 否 | 先用文献和设备边界收敛问题，不必等待品牌/型号 |
| 方案与安全核对 | 部分重要 | 确认视场能覆盖标距区、镜头能稳定对焦、是否有共同触发/时间戳 |
| DIC 标定和预试验 | 重要 | 记录像素标定、曝光、帧率、镜头/工作距离、照明、散斑和标定误差 |
| VFM 正式识别 | 必须 | 对每一帧给出唯一的试验机时间/样本映射，并报告同步残差、漂移和场量质量 |

所以：相机“品牌和型号”现在不是选题阻塞项；相机“帧率、曝光、像素尺度、触发延迟、时间戳、标定误差”在真正计算应变和 VFM 时是硬条件。即使两套设备标称频率相同，也不能自动证明帧和力来自同一时刻。

### 现在只需预留的最小元数据

设备资料到手后，至少记录以下字段；未知的先写 `待核对`，不要猜：

```text
camera_id
image_width_px, image_height_px
nominal_fps, actual_fps（如可得）
exposure_us, lens_or_working_distance
pixel_scale_mm_per_px, calibration_error_px_or_mm
trigger_type, trigger_id, camera_timestamp
machine_timestamp_or_sample_id
frame_id → machine_sample_id 的映射规则
lighting、speckle_batch、MatchID 2019 处理参数
```

这些字段的目的不是写设备介绍，而是让 `实验/PA12-双轴-DIC-VFM/04_帧力位移同步验证.md` 能回答：某张图像对应哪一个力/位移样本、残差多大、该帧是否可进入 VFM。

## 面向 PA12 双轴 DIC/VFM 的最小成果路线

下面是建议顺序，不代表已经选定研究问题。

### 候选 A：同步误差对 VFM 识别的影响

问题：在同一双轴加载路径下，帧—力/位移映射的偏移和漂移会把 VFM 参数误差放大到什么程度？

可验证产出：共同触发记录、同步残差曲线、不同映射质量下的参数稳定性和独立路径验证。只有在文献确认该问题的缺口且设备可记录时间轴后，才进入正式问题。

### 候选 B：整体力—位移与 DIC 全场约束的交叉识别

问题：对 PA12 双轴响应，单独使用整体力—位移与加入 DIC 全场信息时，本构参数的可辨识性、重复性和验证误差有何差异？

可验证产出：同一试样/加载路径的两套识别结果、误差与置信区间、独立加载路径验证。不能把同一试样的图像帧当成独立试样重复。

### 候选 C：双轴加载路径对全场失稳/非均匀性的作用

问题：在有限的双轴比例或路径变化下，全场应变集中、边缘效应和模型残差如何变化？

可验证产出：加载路径矩阵、DIC 全场指标、试样有效区域规则和 VFM 适用性边界。具体比例和试样尺寸必须等设备、夹具和文献核对后再定。

选择原则：优先选择能由现有设备和数据闭环完成、可与至少一个文献基线直接比较、失败时仍能形成方法学结论的候选。当前不把 A/B/C 中任何一个写成已确定创新点。

## 每次对话应留下什么

每天只推进一个闸门，结束时在 `研究报告/日报/YYYY-MM-DD.md` 写下：

1. 当前研究状态；
2. 已知证据及其来源；
3. 来源缺口和不确定项；
4. 当前研究阶段；
5. 拟执行的下一阶段；
6. 下一阶段会生成哪些文件；
7. 需要用户确认的问题。

### 推荐调用模板

```text
按 literature-research：围绕“PA12 biaxial tension + DIC + VFM”做三组检索，
给出纳入/排除标准、前后向引文链、证据矩阵和可核查缺口；不要把检索摘要当作全文证据。

按 mineru：解析指定 PDF，禁止 OCR；保留原始 PDF，输出 Markdown、图片、表格/公式位置和 manifest，
并把每条方法结论链接到页码或原文段落。

按 experiment-design：针对候选问题 X 设计最小实验矩阵；每行只改变一个因素，
固定设备、试样、DIC、同步和统计规则，先写预期结果、停止条件和分析图表。

按 scientific-critical-thinking + uncertainty-and-units：审计以下结论的证据链、单位、
重复性、同步残差和可能的替代解释；把不能由数据支持的句子标为待验证。
```

## 不安装或暂不启用的技能

- `itallstartedwithaidea/agent-skills` 的 `research-methodology`：公开页面的示例偏临床/RCT，且来源仓库主要不是工程力学；不如本机已有研究设计和批判性思维技能贴合当前问题，因此不安装。
- `fcakyon/phd-skills` 的整套 Claude Code 插件：功能有价值，但宿主格式不是 Codex 技能格式；已提取可直接使用的两个目录，避免安装后出现不可调用或重复命名。
- 继续堆叠更多“论文总结”技能：不会替代原始 PDF、页码、表格、原始图像、力/位移数据和同步记录。

## 成功标准

当且仅当满足以下条件，才把阶段结论写成“已完成”：

- 每篇纳入论文有可验证元数据和原始来源；
- 每个研究缺口至少有多种检索表述和反向核查记录；
- 每个候选问题都有可获得的数据、基线、反驳条件和最小实验矩阵；
- 正式试验前，帧—力—位移映射、DIC 标定和单位链通过预试验；
- VFM 结果有独立加载路径或独立试样验证，并报告重复性和不确定度；
- 论文图表可以追溯到原始 PDF、原始图像、原始机器数据或明确的处理脚本。

技能可以减少检索、整理和审计的重复劳动，但不能替你生成尚不存在的实验事实，也不能保证论文必然发表。当前最有效的下一步是：继续补齐设备/触发资料，同时用 `literature-research` 完成候选 A/B/C 的缺口核查；相机型号可以稍后确认，帧率、触发和时间轴不能在预试验前省略。
