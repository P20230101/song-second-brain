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
- 新增 [`wiki/双轴-DIC-VFM-两篇核心文献研读-PA12路线.md`](wiki/双轴-DIC-VFM-两篇核心文献研读-PA12路线.md)，区分晶格压缩设备案例与 PA12 十字形试样基线，固定工业相机单相机 2D DIC 的复现缺口和后续 VFM 闸门。
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
