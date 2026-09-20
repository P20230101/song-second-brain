---
title: 科研流水线 SOP
type: workflow
---

# 自动化科研流水线标准操作手册（SOP）

本页把截图中的阶段 0–3 转换为当前 Windows Vault 的可执行约定。它使用已经安装的 Agent Skills；`Research_Pipeline_Matrix_Engine` 不是已核实的公开仓库名称，因此不伪造同名文件，实际由技能注册表中的组合完成编排。

## 安装来源

- [GPT Researcher](https://github.com/assafelovic/gpt-researcher)：深度研究主项目；本机另有 `gptr-mcp` 运行包装器。
- [Scientific Agent Skills](https://github.com/K-Dense-AI/scientific-agent-skills)：164 个科学与研究技能。
- [Research-Agent-Skills-Collection](https://github.com/lensetek/Research-Agent-Skills-Collection)：28 个研究流水线技能。

## GitHub 网络配置

本机 Git 已全局配置本地代理：

```text
http.proxy  = http://127.0.0.1:7890
https.proxy = http://127.0.0.1:7890
```

验证命令：

```powershell
git ls-remote --heads https://github.com/K-Dense-AI/scientific-agent-skills.git refs/heads/main
```

该命令已在清空当前进程环境代理变量后成功返回远端 `main`，说明 GitHub 访问不依赖临时环境变量。代理程序关闭时，GitHub 下载会按网络错误直接失败，不会静默切换到未知路由。

## 阶段 0：规划本地物理路径

每次启动新课题，先把以下绝对路径作为唯一工作边界：

| 变量 | 当前路径 | 用途 |
| --- | --- | --- |
| `root_path` | `D:\松的第二大脑\松的第二大脑` | 论文全文、阶段性 Markdown 和 Wiki 页面 |
| `data_source_path` | `D:\松的第二大脑\松的第二大脑\双轴\raw` | 原始 PDF、数据集和外部来源；只读保存 |
| `code_and_images_path` | `D:\松的第二大脑\松的第二大脑\双轴\实验` | 可执行代码、Notebook、模型输出和图片 |

目录边界：

```text
松的第二大脑/
├── raw/                 # 原始来源与数据，只读
├── 实验/                # 代码、Notebook、图像和模型输出
├── wiki/                # 研究上下文、矩阵、综述和复盘
├── index.md             # Wiki 总入口
└── log.md               # 追加式维护日志
```

## 阶段 1：唤醒研究编排器

在 Codex 中使用以下指令。将方括号替换为真实值，路径保持绝对路径：

```text
读取 AGENTS.md、index.md、wiki/01_研究总控/01_项目入口/研究上下文.md 和本页。
启动研究编排流程。
研究主题：[主题]
成果路径：D:\松的第二大脑\松的第二大脑
原始数据路径：D:\松的第二大脑\松的第二大脑\双轴\raw
代码与图像路径：D:\松的第二大脑\松的第二大脑\双轴\实验
本阶段目标：[例如：完成文献矩阵并提出可证伪的研究问题]
请先输出：当前研究状态、已知证据、缺口、拟执行阶段、每阶段的产物和需要我确认的问题。
不要跨阶段执行；完成一个阶段后必须停下等待我的“是/否”确认。
```

实际技能映射见下表。它们在下一次 Codex 对话启动后自动可发现，也可以直接在提示中点名。

## 技能注册表

| 截图中的职责 | 已安装技能 | 产物 |
| --- | --- | --- |
| 文献搜索与捕获 | `gpt-researcher`、`literature-review`、`paper-lookup`、`research-lookup` | 来源清单、PDF 原件、`download_manifest.json` |
| 中央编排与论文矩阵 | `research_orchestrator`、`paper_matrix_builder`、`literature_review_generator` | 研究阶段计划、论文比较矩阵、综述草稿 |
| 研究问题与假设 | `research_question_builder`、`hypothesis_or_proposition_builder`、`hypothesis-generation` | 研究问题、假设/命题和证伪条件 |
| 研究设计与实证 | `research_design_planner`、`experimental-design`、`statistical-analysis`、`statistical-power` | 设计、变量、分析计划和功效依据 |
| 证据与同行审查 | `source_quality_appraiser`、`citation_and_reference_validator`、`academic_peer_reviewer`、`scientific-critical-thinking` | 证据等级、引用核验、审查意见 |
| 写作与 Obsidian 回写 | `scientific-writing`、`synthesize_research`、`obsidian_vault_exporter` | 章节草稿、综合结论、Vault 页面 |

## 阶段 2：级联问题与人工确认

每一个阶段性产物完成后，编排器必须输出：

1. 已完成的文件和可核查来源。
2. 来源事实、AI 推断、研究假设和待验证问题的分离结果。
3. 下一阶段的输入、预期产物和可能的停止条件。
4. 一个明确的确认问题。

我的回复约定：

- 回复“是”或“开始生成 [文件名]”：允许进入下一阶段。
- 回复“否”：停止流水线，保留当前产物，等待新的方向。
- 未收到确认：不得自动跨阶段，不得把草稿当作最终论文内容。

## 阶段 3：代码双轨产出与人工介入

当研究设计获得确认后，代码和文字分开生成：

- 文字轨：将研究框架、方法说明和证据链写入 `root_path` 或 `wiki/`。
- 代码轨：将可执行脚本、`.ipynb`、数据处理记录和图片写入 `code_and_images_path`。
- 运行前由人工确认数据完整性、变量定义、样本范围和环境；运行后把命令、版本、输出文件和失败信息写入实验记录。
- 不把模型输出直接写成论文结论；先回到 `wiki/01_研究总控/01_项目入口/研究上下文.md`，标注证据、推断、限制和下一步。

推荐的最小项目目录：

```text
实验/<项目名>/
├── README.md
├── notebooks/
├── scripts/
├── data/              # 数据副本或指向 raw/ 的说明，不替代原始来源
└── figures/
```

## 与每日学习闭环的连接

每天讨论文献后：

1. 将原始对话追加到本地 `inbox/对话/每日对话记录.md`。
2. 读取 `wiki/01_研究总控/01_项目入口/研究上下文.md` 和当天对话，生成每日闭环页。
3. 把文献矩阵的新增行、证据冲突、待验证问题和下一步确认写入闭环页。
4. 只有形成可复用结论并完成来源核验后，才回写主题 Wiki。

## 已知限制

- `gpt-researcher` 的深度研究 MCP 仍需要模型/搜索服务 API key；当前文献 PDF 下载器可独立运行，不依赖这些 key。
- `scientific-agent-skills` 是大型技能集合，本机已安装完整目录；并非每项技能都需要额外 Python 包，按任务再安装依赖。
- 个别第三方技能文档包含 macOS/Linux 的可选安装示例（例如 `curl | bash`）；Windows 环境不自动执行这些命令，需要单独确认替代安装方式。
- 技能只能提供流程知识，不能替代研究者对样本、识别策略、伦理和最终论文主张的判断。
