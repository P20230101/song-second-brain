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
