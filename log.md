---
title: 维护日志
---

# 维护日志

本文件按时间顺序追加记录，不改写历史条目。

## [2026-09-10] init | 建立“松的第二大脑”

- 建立 Raw sources、Wiki 与 Schema 三层结构。
- 配置 Obsidian 兼容的 Markdown Wiki 与 GitHub Pages 发布入口。

## [2026-09-10] query | 建立每日学习闭环

- 根据今日关于 LLM Wiki、Obsidian、Codex CLI 和 GitHub Pages 的对话，整理每日学习闭环页面。
- 新增 [`wiki/每日学习闭环-2026-09-10.md`](wiki/每日学习闭环-2026-09-10.md)，并登记到 `index.md`。

## [2026-09-10] query | 接入 Codex 的每日学习闭环

- 来源：用户确认创建研究上下文模板，并要求将每日对话集中记录、按论题或开题报告自动整理分析。
- 新增：`wiki/研究上下文.md`，作为每日分析的唯一研究依据；`每日对话记录.md` 作为本地私有追加日志。
- 受影响页面：`AGENTS.md`、`index.md`、`wiki/每日学习闭环-2026-09-10.md`。

## [2026-09-10] query | 端到端集成测试

- 来源：用户端到端测试请求及对 Vault、Codex CLI 和 Obsidian Terminal 配置的读取验证。
- 新增：`wiki/每日学习闭环-2026-09-10-集成测试.md`，并在 `index.md` 登记。
- 更新：`每日对话记录.md` 的 `2026-09-10` 节追加测试记录。
- 未修改：`raw/` 和 `wiki/研究上下文.md`。

## [2026-09-11] capture | 建立文献捕获与筑巢流程

- 新增：`tools/literature_capture.py`，支持 arXiv、Semantic Scholar 和外部结果 JSON，下载 PDF 并生成 `download_manifest.json`。
- 新增：[`wiki/文献捕获与筑巢.md`](wiki/文献捕获与筑巢.md) 与 `raw/参考文献/README.md`。
- 更新：`AGENTS.md`、`index.md`、`raw/README.md` 和 `.gitignore`，明确本地原件只读且不发布。

## [2026-09-11] setup | 安装科研技能并建立流水线 SOP

- 通过 Git 全局代理 `http://127.0.0.1:7890` 验证 GitHub 连通性。
- 安装 K-Dense-AI `scientific-agent-skills` 完整技能集合与 `lensetek/Research-Agent-Skills-Collection` 完整技能集合。
- 新增 [`wiki/科研流水线SOP.md`](wiki/科研流水线SOP.md) 和 `实验/README.md`，固定阶段 0–3 的路径、技能映射和人工确认门。

## [2026-09-11] setup | 固定工程力学双轴 DIC-VFM 研究路线

- 根据用户确认的工程力学方向、双轴拉伸/压缩试验、10 kN 力值、0–100 mm 行程和 DIC + VFM 方法，更新 `wiki/研究上下文.md`。
- 新增 [`wiki/工程力学-双轴DIC-VFM研究路线.md`](wiki/工程力学-双轴DIC-VFM研究路线.md)，固定从选题、文献矩阵、设备核对、预试验、正式试验、三路数据交叉验证到小论文/大论文的阶段闸门和输出文件。
- 新增 [`wiki/目录与文件分类.md`](wiki/目录与文件分类.md)，并将实验区说明扩展为双轴 DIC-VFM 项目目录规范。
- 明确记录：材料、夹具、双轴通道能力、DIC 配置、VFM 本构模型和加载路径仍需通过设备资料、文献和预试验确认，不能提前写成结论。

## [2026-09-11] setup | 建立设备资料核对入口

- 新增 [`raw/设备/README.md`](raw/设备/README.md)，固定双轴试验机、夹具、DIC、VFM 和安全资料的首轮核对字段。
- 更新 `raw/README.md`，明确设备原始资料的存放位置和只读规则。

## [2026-09-11] capture | 双轴-DIC-VFM 首轮种子文献筛选

- 使用 `tools/literature_capture.py` 捕获 8 篇方法型种子文献；原始 PDF 和清单保存在 `raw/参考文献/双轴-DIC-VFM-选题/`。
- Semantic Scholar 返回 HTTP 429 限流；arXiv 返回 8 篇，其中 2 篇暂定纳入全文提取，6 篇因主题不匹配初筛排除。
- 新增 [`wiki/双轴-DIC-VFM-种子文献筛选.md`](wiki/双轴-DIC-VFM-种子文献筛选.md)，明确初筛不等于证据结论，下一步只做 2 篇全文提取。

## [2026-09-11] setup | 配置 Semantic Scholar 下载器

- `tools/literature_capture.py` 现在读取本机 `S2_API_KEY` 或 `SEMANTIC_SCHOLAR_API_KEY`，以 `x-api-key` 请求头调用 Semantic Scholar；密钥不写入 Vault、下载清单或 Git。
- 无 Key 的 HTTP 429 只重试一次，第二次失败会显式记录为检索错误。
- 新增 [`wiki/Semantic-Scholar下载配置.md`](wiki/Semantic-Scholar下载配置.md)，记录本机配置和公开 PDF 下载边界。

## [2026-09-11] design | 固定双轴 DIC-VFM 同步采集与预试验门槛

- 原样归档用户提供的宁波大学动态双轴拉压系统设备照片与参数海报至 `raw/设备/`；海报列出 0–10 kN、1 kHz、±150 mm、0–4 m/s，等待说明书和校准资料核对。
- 新增 [`wiki/双轴-DIC-VFM-同步采集与预试验方案.md`](wiki/双轴-DIC-VFM-同步采集与预试验方案.md)，明确相机帧率不必等于 DAQ 采样率，但每个 VFM 图像帧必须具有可核验的帧—采样映射、触发事件和同步残差。
- 更新 `wiki/研究上下文.md`、`wiki/工程力学-双轴DIC-VFM研究路线.md`、`raw/设备/README.md` 与 `index.md`，并将准静态/动态 VFM 分流、DIC 面外运动与正式试验前的同步验证写为固定闸门。

## [2026-09-11] study | 研读双轴设备案例与 PA12 研究基线

- 原样归档用户提供的孙正平等 2025 年 RD 晶格双轴压缩论文与袁颖诗 2026 年 SLS PA12 双轴拉伸论文至 `raw/参考文献/PA12-双轴-DIC-VFM/`；原文保持本地只读且不上传公开仓库。
- 新增 [`wiki/双轴-DIC-VFM-两篇核心文献研读-PA12路线.md`](wiki/双轴-DIC-VFM-两篇核心文献研读-PA12路线.md)，区分晶格压缩设备案例与 PA12 十字形试样基线，固定正式 3D DIC 的复现缺口和后续 VFM 闸门；袁文件夹中的 2D 工程仅保留为历史基线。
- 更新 `wiki/研究上下文.md` 与 `index.md`：PA12 双轴拉伸作为暂定材料路线；FDM-PLA 晶格压溃不纳入拟研究对象。

## [2026-09-11] setup | 建立 MinerU 图文解析与科研周期报告

- 新增 [`wiki/MinerU-PDF解析与图文研读流程.md`](wiki/MinerU-PDF解析与图文研读流程.md)，固定原始 PDF、MinerU Markdown、图片、结构化清单和 Wiki 结论的分层关系；文字型 PDF 的正式解析只采用非 OCR 路径。
- 新增 `模板/科研日报.md`、`模板/科研周报.md`、`模板/科研月报.md`，并完成 Obsidian 模板与每日笔记目录配置。
- 新增 `研究报告/日报/2026-09-11.md`、`研究报告/周报/2026-W37.md`、`研究报告/月报/2026-09.md`，将当前 PA12 双轴-DIC-VFM 选题、证据、缺口和下一阶段写入周期报告。
- 更新 `研究报告/README.md`、`index.md` 与每晚 21:00 自动审查任务；该任务只补建报告，不覆盖用户已写内容，且不推送原始 PDF 或 MinerU 私有解析输出。

## [2026-09-11] capture | 通过 MinerU 云端 API 完成首批 PDF 图文解析

- 从官方 `MinerU-Ecosystem` GitHub 仓库安装 `mineru-open-mcp` 与 `mineru-open-api`，并将源码保存在 Vault 外的 `C:\Users\Administrator\Downloads\MinerU-Ecosystem`。
- 使用用户级 MinerU token，调用官方 `mineru-open-api extract --model vlm --ocr=false`：两篇首批论文均完成全文解析，分别生成 Markdown、JSON 和独立图片；输出保存在 `raw/参考文献/PA12-双轴-DIC-VFM/MinerU-API/`，不进入 Git。
- 更新 [[MinerU-PDF解析与图文研读流程]] 与 2026-09-11 日报：解析完成不等于图表核验完成，下一步是逐图/表对照并将页码定位写回专题页。
- Semantic Scholar 的用户级 `S2_API_KEY` 已存在；最小在线调用仍受 HTTP 429 限流，下载器保留一次重试并显式记录失败。

## [2026-09-11] search | 修复双库检索并建立方法候选矩阵

- 更新 `tools/literature_capture.py`：Semantic Scholar 429 按 `Retry-After`/指数退避最多重试 4 次；arXiv 主题查询改为 DIC/VFM 短语的 AND 组合；清单增加各来源命中数并交错保留两个来源。
- Semantic Scholar 检索端点改为官方 `paper/search/bulk`；用带 API Key 的最小请求验证返回正常，避免交互式 search 端点的共享限流影响双库检索。
- 实测同一主题检索：Semantic Scholar 命中 10 条、arXiv 命中 4 条；合并清单同时包含 `semantic-scholar` 与 `arXiv`，并下载 5 个公开 PDF。
- 新增 [`wiki/双轴-DIC-VFM-扩展检索-2026-09-11.md`](wiki/双轴-DIC-VFM-扩展检索-2026-09-11.md)，仅将题名/摘要级方法候选列入矩阵，下一步执行全文方法提取和质量筛选。
- 更新 `wiki/研究上下文.md`：MatchID 版本固定为 2019，后续优先核对该版本可导出的场量、质量指标和元数据格式。

## [2026-09-11] study | 完成方法型种子论文的 MinerU 全文提取

- 对双库检索中 5 篇有公开 PDF 的方法论文使用官方 MinerU API、`--model vlm --ocr=false` 完成全文 Markdown、JSON 和独立图片导出。
- 从全文提取 VFM 内/外虚功、DIC 全场输入、同步 load-cell、虚场/噪声敏感性、FEMU 交叉比较和应力场重构边界条件等方法证据。
- 新增 [`wiki/双轴-DIC-VFM-方法比较与候选创新点.md`](wiki/双轴-DIC-VFM-方法比较与候选创新点.md)，将方法路线固定为测量层—同步层—识别层，并列出四个待预试验验证的创新候选。

## [2026-09-11] env | 补齐可执行 Python

- 安装 Python 3.12，并将用户级 PATH 中的 Python 路径置于旧 uv trampoline 之前；重新打开终端后，`python tools/literature_capture.py` 可直接执行。
- 用 Python 3.12 从 `C:\Users\Administrator\Downloads\MinerU-Ecosystem\mcp` 重新安装 `mineru-open-mcp`，恢复 Codex MCP 启动器；`mineru-open-mcp --help` 与 `mineru-open-api --version` 均可执行。
- 按 Semantic Scholar 官方 1 request/second 规则，在脚本的所有 `api.semanticscholar.org` 请求入口加入 1.1 秒最小间隔；429 退避重试继续保留。
- 新增 `实验/PA12-双轴-DIC-VFM/02_文献方法矩阵.md`、`03_MatchID2019字段映射.md` 和 `04_帧力位移同步验证.md`，将方法证据、MatchID 2019 字段和同步闸门固定为可填充接口。

## [2026-09-12] search | 扩大来源并整理试样/DIC/VFM 证据

- 扩展双轴试样几何、DIC 散斑/不确定度、VFM 可辨识性和同步检索；来源地图覆盖 Web of Science、Scopus、ScienceDirect、OpenAlex、Crossref、Semantic Scholar 和 arXiv 的不同用途。
- 完成 `yuan` 文件夹的论文与数据只读审计，将 4 篇核心 PDF 的 MinerU 解析结果和字段缺口写入 `wiki/yuan-论文与数据审计-2026-09-12.md`。
- 新增 `wiki/科研产出型Skills-选择与使用.md`，登记 `literature-research`、`experiment-design` 和 `mineru` 的安装位置及科研产出分工。

## [2026-09-12] design | 固定阶段 1、最小预试验和 VFM 软件接口

- 新增 `wiki/阶段1-研究问题决策与下一步-2026-09-12.md`：将全场信息贡献列为主线候选 B，将同步误差列为质量闸门 A，将几何/加载路径列为扩展候选 C。
- 新增 `实验/PA12-双轴-DIC-VFM/05_最小预试验矩阵.md`：按单变量原则固定事件链、平面/刚体 DIC、MatchID 2019 参数扫描、低载荷基线和整体/全场对照。
- 新增 `wiki/VFM软件识别闭环与本构参数验收.md`：固定从 MatchID 2019 场量和双轴边界力到本构参数、独立验证和不确定度报告的软件接口。
- 新增 `wiki/论文启发与GitHub工作时间线.md`：按论文启发和北京时间 Git 提交记录对应每日研究产出。

## [2026-09-12] maintenance | 按日期重排 Wiki 导航

- 根目录 `index.md` 改为按 2026-09-10、2026-09-11、2026-09-12 和报告日期分区，固定系统入口单独列出。
- `wiki/README.md` 同步记录日期分区和“首建日期/后续更新以 Git 与维护日志为准”的规则。
- 不移动文件路径、不修改 `raw/`、原始实验数据和 `tmp/`；仅整理导航和维护记录。

## [2026-09-12] analysis | 深入审计 yuan 仿真/实验数据并修正 DIC 路线

- 根据用户确认，将正式项目路线统一修正为 MatchID 2019 **3D 立体 DIC**；文献中的 2D DIC 只作为误差对照，袁文件夹中明确标注 `MatchID 2D-Version 19.2.2.0` 的旧工程只作为历史处理基线。
- 只读核对 `D:\C盘迁移\Desktop\yuan` 的图像、伴随压缩帧、CSV/XLS、MatchID 工程、VFM 二进制文件和 CIHX 相机元数据，记录帧数不一致、旧路径引用、缺失 3D 标定/触发日志和二进制结果不可读等缺口。
- 新增 [`wiki/yuan-仿真与实验数据深入分析-2026-09-12.md`](wiki/yuan-仿真与实验数据深入分析-2026-09-12.md)，把 3D DIC—同步四通道边界力—VFM/FEMU—有限元预测串成小论文与大论文的连续路线，并给出下一次只需提供一份匹配试验包的执行入口。
- 复核代表性 `Img000000.jpg.csv` 导出表头只有 `x_pic/y_pic/u/v/r/sigma/correlationPath/ShapeIndex`，提交 `4d961cf` 将其记录为二维历史字段，明确 3D DIC 必须另建含 `Z/W` 的导出接口。

## [2026-09-12] decision | 阶段 1 候选方向证据决策

- 完成四组公开检索：PA12 单轴本构、PA12 双轴/十字形、DIC 面外误差与标定、DIC+VFM/FEMU 可辨识性；新增来源按摘要/机构全文级写入文献方法矩阵。
- 新增 [`wiki/阶段1-候选方向证据决策-2026-09-12.md`](wiki/阶段1-候选方向证据决策-2026-09-12.md)：把 `yuan` 的 MatchID 2019 2D 复现锁定为立即执行基线，3D 仅在取得双视角、空间标定和三向导出后作为校核分支。
- 将阶段 1 的唯一可执行问题收敛为“同步、ROI/边缘和 DIC 参数对 PA12 双轴 VFM 识别及独立路径预测的影响”，并固定 2D 基线、合成 FE 场、VFM/FEMU 交叉验证和后续 3D 闸门的顺序。

## [2026-09-12] maintenance | 删除冗余 Wiki 页面

- 删除初始化测试、重复检索、旧版审计、旧阶段决策和 Skills 说明等 10 个不再作为执行入口的 Wiki 页面。
- 保留 13 个核心页面：研究上下文、阶段 1 证据决策、总路线、核心文献、同步预试验、VFM 闭环、`yuan` 深入分析、文献捕获、MinerU、Semantic Scholar、SOP、时间线和 Wiki 说明。
- 每日报告、周报、月报、`raw/` 原始资料、实验接口和本地脚本均未删除；每日复盘统一写入 `研究报告/日报/`。
- `index.md` 与 `wiki/README.md` 已改为核心页面导航；历史提交说明保留在本日志中，不再作为当前入口。

## [2026-09-12] automation | 将核心 Wiki 精简纳入每日 21:00 审查

- 更新自动任务 `21-00`“每日 21:00 第二大脑价值审查、报告与同步”：加入 13 个核心 Wiki 白名单、重复/空草稿删除条件、全库引用检查和“用途不确定则保留”规则。
- 明确保护 `raw/`、PDF、MinerU 产物、download_manifest、实验原始数据、实验接口、脚本、用户笔记及日报/周报/月报；删除必须记录精确路径。
- 暂停同一时间运行的线程心跳任务 `21`，保留 `21-00` 作为唯一每日 21:00 执行入口，避免重复整理或重复推送。

## [2026-09-12] data-audit | 初步核验照片—力传感器频率表

- 新增 [`实验/PA12-双轴-DIC-VFM/06_XY频率对照与初步核验.md`](实验/PA12-双轴-DIC-VFM/06_XY频率对照与初步核验.md)，按截图数值复核 `N_F/f_F`、速度×时间位移闭合、照片数量/频率窗口和力样本/帧比例。
- 判定图 2 三档位移与名义频率内部一致但仍需原始时间戳；图 1 的 0.2 mm/s、2 mm/s 照片窗口与完整力记录不一致，20 mm/s 行暂时一致。
- 固定 X/Y 最终表字段：机器/力时间戳、图像帧时间戳、MatchID 2019 实际输出频率、同步偏移/残差和 `vfm_eligible`；明确 101 Hz、375 Hz 必须按时间戳插值，不能整数抽取。
- 根据用户确认的可信输入（速度、照片数量、力数据数量）补充重算表：统一按 `T_F=N_F/1000` 计算力数据时间、`d_F=vT_F` 计算力位移、`f_img_actual=N_img/T_F` 计算照片实际频率，并将 `N−1` 首尾间隔定义作为替代结果明确记录。
- 读取 `D:\C盘迁移\Desktop\yuan\data\XY\20250529\20250529` 下 12 个 Excel 工作簿的 `Speed/Press` 时间列：正常 `ΔT=0.001 s`，确认力传感器名义频率为 1000 Hz；六个与截图对应的文件的 `T_end` 分别为 14.754、2.789、0.401、179.516、15.347、1.890 s，证明应以 Excel 时间戳而不是 `N_F/1000` 计算持续时间和位移。记录各文件少量 0.002 s 间隔及 998.568–1000 Hz 的有效平均频率作为数据质量信息。
- 继续核对 XZ 数据目录：CIHX 元数据给出 `Z-0.1-06` 相机 60 Hz、`（Z）-1-07` 和 `（Z）-1-08` 相机 500 Hz；前三组 JPEG 与 MatchID 输入帧数一致，但 `（Z）-1-08` 的 DIC CSV 缺 131–141 共 11 个帧号；`XZ-10-04` 缺 CIHX、MatchID 输入和力数据。已在频率核验页加入 XZ 对照表，并明确 XZ 力传感器频率不能由现有文件直接证明。

## [2026-09-12] data-boundary | 固定加载首帧与破坏末帧规则

- 将首帧/末帧从“文件夹第一张/最后一张”改为事件边界：单独记录 `frame_reference`（零载/预载参考帧）、`frame_first_valid`（加载开始后第一张有效分析帧）和 `frame_last_valid`（结束/破坏后仍完整覆盖试样的最后一张有效帧）。
- 暂将用户所说的“锻炼阶段”解释为断裂、明显破坏或目标大变形；若实际指屈服，只需在同一清单中改填 `last_event_type=yield`，不改变同步流程。
- 代表性证据：`Y-09-0.1-02` 的末图显示试样中部断裂，可作为断裂终点候选；`X-05-0.1-01` 的末图已基本没有试样，明确不能把文件末尾当作 DIC 末帧；`X-06-1.0-01` 的图像数量与截图不一致。
- XZ 仍只能确认部分相机—MatchID 帧连续性；缺力文件、缺元数据或缺 DIC 帧的序列不进入 VFM。新增首末帧清单字段、事件类型、图像/信号证据和 `vfm_eligible` 门槛，窗口外图片保留但标记为 `out_of_window`。

## [2026-09-12] data-audit | 全量照片—力—DIC 配对清单

- 递归盘点 `D:\C盘迁移\Desktop\yuan\data` 的已解压目录、`XY.zip`/分卷和 `XZ.zip`/现有分卷，按试验编号建立图像、MatchID、DIC CSV 与力文件的配对键。
- XY 确认 10 个图像序列、12 个非锁定力 Excel（含 `xy-04-1` 重复文件和无图像对应的 `y-8` 孤立力段）；`Press.T` 可读，名义力采样率为 1000 Hz，异常帧、ROI 离开、DIC 缺帧和首末事件均已写入清单。
- XZ 的 ZIP 中心目录实际列出 7 个图像序列和 12 个力 Excel；当前缺少 `XZ.z01`，因此 XZ 力 Excel 只能完成目录级映射，不能读取工作表内容或填入力时间/力频率。现有分卷可读出 `XZ-10-04`、`Z-0.1-06`、`Z-1-07`、`Z-1-08` 的部分相机/MatchID 元数据，其中 `Z-1-08` CSV 缺 131–141 共 11 帧。
- 新增 [`实验/PA12-双轴-DIC-VFM/07_全量照片-力-DIC配对清单.md`](实验/PA12-双轴-DIC-VFM/07_全量照片-力-DIC配对清单.md)，明确“文件级配对已完成”与“共同时间戳/触发号缺失、尚未达到 VFM”的边界；原始数据未复制、未删除、未修改。
