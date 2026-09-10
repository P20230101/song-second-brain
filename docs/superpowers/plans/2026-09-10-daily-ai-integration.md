# Daily AI Learning Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在现有 Karpathy LLM Wiki 上完成可运行的 Obsidian + Codex CLI 每日学习闭环，并保留一个可选的嵌入式终端入口。

**Architecture:** Claudian 作为 Obsidian 内的 AI 侧栏，调用已安装的本机 Codex CLI。原始对话追加到被 Git 忽略的单一 Markdown 日志；Codex 读取研究上下文和当天日志，生成公开的每日闭环页，只把可复用结论写回 `wiki/`。终端插件只增强交互，不参与核心数据流。

**Tech Stack:** Obsidian 1.13.7、Claudian 2.2.6、Codex CLI 0.153.4、Markdown、GitHub Pages/Jekyll、Windows PowerShell。

---

### Task 1: 建立研究上下文与每日对话文件

**Files:**
- Create: `wiki/研究上下文.md`
- Create: `每日对话记录.md`
- Modify: `.gitignore`

- [ ] **Step 1: 创建研究上下文模板**

写入 `wiki/研究上下文.md`，包含以下固定字段，并明确“待填写”是用户输入而非已知事实：

```markdown
---
title: 研究上下文
type: research-context
---

# 研究上下文

> 本页是每日学习分析的唯一研究依据。请把论题或开题报告中的稳定内容填入对应小节；没有依据的内容不要写成事实。

## 研究主题

- 研究题目：待填写
- 所属领域：待填写
- 当前阶段：选题 / 文献综述 / 方法设计 / 实验 / 写作 / 答辩准备

## 核心问题

1. 待填写

## 研究目标与范围

- 目标：待填写
- 纳入范围：待填写
- 不纳入范围：待填写

## 核心概念与术语

| 术语 | 当前定义 | 来源或依据 |
|---|---|---|
| 待填写 | 待填写 | 待填写 |

## 方法与评价标准

- 计划采用的方法：待填写
- 评价标准：待填写
- 必须满足的约束：待填写

## 当前已知结论

- 尚未填写。后续结论必须能追溯到 `raw/` 来源或每日闭环页。

## 待解决问题

- 待填写

## 更新规则

- 只有用户确认后的稳定信息才写入本页。
- Codex 的推断和临时假设写在每日闭环页，不直接升级为研究事实。
```

- [ ] **Step 2: 创建单一追加式对话日志**

创建 `每日对话记录.md`，包含标题、使用说明和第一条空白日期节：

```markdown
# 每日对话记录

> 本文件只保存本地原始对话和简短上下文，不提交到公开仓库。每天在当天日期下追加，不覆盖旧记录。

## 2026-09-10

### 今日主题

从零搭建“松的第二大脑”并接入 Codex CLI。

### 原始对话

<!-- 将当天与 AI 的原始对话或可复核摘要追加在这里。 -->

### 当天补充

<!-- 目标、来源、疑问、决定。 -->
```

- [ ] **Step 3: 将原始对话加入 Git 忽略**

在 `.gitignore` 末尾加入精确规则 `/每日对话记录.md`，保留现有规则不改写。

- [ ] **Step 4: 验证文件和忽略规则**

运行：`Test-Path wiki/研究上下文.md; Test-Path 每日对话记录.md; git check-ignore -v -- 每日对话记录.md`

预期：前两个命令返回 `True`，最后一条显示 `.gitignore` 中的 `/每日对话记录.md` 规则；若失败，修正对应文件后再继续。

- [ ] **Step 5: Commit**

运行：`git add wiki/研究上下文.md .gitignore; git commit -m "docs: add research context template"`

不要把 `每日对话记录.md` 加入提交。

### Task 2: 把每日闭环规则写入代理和入口页

**Files:**
- Modify: `AGENTS.md`
- Modify: `index.md`
- Modify: `wiki/每日学习闭环-2026-09-10.md`
- Modify: `log.md`

- [ ] **Step 1: 在 AGENTS.md 增加每日闭环规则**

加入“每日对话与研究上下文”小节，规定：读取 `每日对话记录.md` 和 `wiki/研究上下文.md`；对话原文只追加；分析必须分离事实、推断、待验证项；确认后才写回 Wiki；写回后更新 `index.md` 和 `log.md`。

- [ ] **Step 2: 在 index.md 登记研究上下文和每日闭环入口**

加入 `wiki/研究上下文.md` 的一句话摘要，并把每日闭环入口说明更新为“读取研究上下文、整理单一对话日志并写回可复用知识”。

- [ ] **Step 3: 在每日闭环页加入可直接复制的一键提示词**

提示词必须指向 `每日对话记录.md` 和 `wiki/研究上下文.md`，要求先读取规则、区分事实/推断、追加当天对话、生成当天页面、只在可复用时更新 Wiki，并列出下一步问题。

- [ ] **Step 4: 在 log.md 追加 query 记录**

追加 `## [2026-09-10] query | 接入 Codex 的每日学习闭环`，列出本次新增文件和受影响入口。

- [ ] **Step 5: 验证入口链接**

运行：`rg -n "研究上下文|每日对话记录|每日学习闭环|index.md|log.md" AGENTS.md index.md wiki/每日学习闭环-2026-09-10.md log.md`

预期：每个文件都能找到对应入口或规则；任何缺失都在提交前补齐。

- [ ] **Step 6: Commit**

运行：`git add AGENTS.md index.md wiki/每日学习闭环-2026-09-10.md log.md; git commit -m "docs: wire daily learning workflow"`

### Task 3: 固化并测试 Claudian 的 Codex CLI 配置

**Files:**
- Modify: `.claudian/claudian-settings.json`（仅在实际设置缺失时）

- [ ] **Step 1: 验证 CLI**

运行：`& 'C:\Users\Administrator\AppData\Local\OpenAI\Codex\bin\fd4c151a749f3ab4\codex.exe' --version`

预期：输出 `codex-cli 0.153.4` 或更高版本号。

- [ ] **Step 2: 验证 Claudian 配置**

读取 `.claudian/claudian-settings.json`，确认 `providerConfigs.codex.enabled` 为 `true`，并且当前设备的 `cliPathsByHost` 值为真实 `codex.exe` 路径。若缺失，只补这两个字段，不改模型目录或其他用户设置。

- [ ] **Step 3: 在 Obsidian UI 做只读代理测试**

聚焦 Obsidian 的 Claudian 面板，选择 Codex，发送：`只读测试：请读取 AGENTS.md，只返回“已读取”以及每日对话日志的写入规则，不要修改任何文件。`

预期：面板返回“已读取”并准确提到 `每日对话记录.md` 只能追加；不要让测试代理写文件。

- [ ] **Step 4: Commit（仅配置有变化时）**

若 Task 3 改动了 `.claudian/claudian-settings.json`，运行：`git add .claudian/claudian-settings.json; git commit -m "chore: configure codex cli for claudian"`。如果配置已正确，不创建空提交。

### Task 4: 安装并启用 Obsidian Terminal（可选增强）

**Files:**
- Create/Modify: `.obsidian/plugins/terminal/`（第三方插件运行文件，不提交到公开仓库）

- [ ] **Step 1: 通过 Obsidian 社区插件搜索 Terminal**

在 Obsidian 中打开“设置 → 社区插件 → 浏览”，搜索 `Terminal`，安装作者 `polyipseity` 的插件并启用。若搜索结果不可用，记录原因，不改变 Codex 主流程。

- [ ] **Step 2: 打开终端面板并执行只读命令**

打开命令面板执行 Terminal 插件的打开命令，在面板中运行：`codex --version`。

预期：终端显示 Codex CLI 版本；不执行写入、删除或发布命令。

- [ ] **Step 3: 验证终端历史保存设置**

在 Terminal 设置中确认“保存终端历史”可用；不指定额外目录，不把插件资源加入 Git。

### Task 5: 端到端运行每日闭环

**Files:**
- Modify: `每日对话记录.md`（本地私有）
- Create: `wiki/每日学习闭环-2026-09-10-集成测试.md`
- Modify: `index.md`, `log.md`（按规则）

- [ ] **Step 1: 追加一条可公开的测试对话摘要**

在 `每日对话记录.md` 的 `2026-09-10` 节追加一条不含隐私的摘要，内容为“验证 Codex CLI 已安装，研究上下文模板已创建，终端插件为可选入口”。

- [ ] **Step 2: 在 Claudian 发送固定整理提示词**

使用以下完整提示词：

```text
这是今天的学习整理任务。请先读取 AGENTS.md、index.md、wiki/研究上下文.md 和每日对话记录.md 中今天的日期节。不要修改原始资料，不要把推断写成事实。

请按顺序执行：
1. 追加一条带时间的“今日整理请求”到每日对话记录.md；
2. 输出并写入 wiki/每日学习闭环-2026-09-10-集成测试.md，分成：已确认事实、基于研究上下文的分析、待验证问题、下一步行动、是否需要更新其他 Wiki 页面；
3. 只有可复用结论才更新已有 Wiki 页面，并同步 index.md 与 log.md；没有可复用结论时明确写“本次不新增主题页”；
4. 最后报告实际修改的文件路径。
```

- [ ] **Step 3: 验证生成结果**

运行：`Test-Path wiki/每日学习闭环-2026-09-10-集成测试.md; rg -n "已确认事实|基于研究上下文的分析|待验证问题|下一步行动|实际修改" wiki/每日学习闭环-2026-09-10-集成测试.md; git check-ignore --quiet -- 每日对话记录.md`

预期：测试页存在且包含五个结构段，原始日志仍被忽略；若失败，读取代理输出和实际文件后修正提示词或规则，再重跑一次。

- [ ] **Step 4: 检查公开内容不包含原始日志**

运行：`git status --short --ignored 每日对话记录.md; git ls-files --error-unmatch 每日对话记录.md`

预期：第一条显示被忽略，第二条返回非零并提示未跟踪；若日志已被跟踪，立即从索引移除但保留本地文件：`git rm --cached -- 每日对话记录.md`。

- [ ] **Step 5: Commit and push public Wiki changes**

运行：`git add wiki/每日学习闭环-2026-09-10-集成测试.md index.md log.md; git commit -m "docs: verify daily AI learning loop"; git push origin main`

预期：提交只包含公开 Wiki 页和入口，不包含私有日志、`.obsidian/`、`.claudian/` 或其他本机工具目录。

### Task 6: 发布检查

**Files:**
- Verify: `index.md`, `wiki/研究上下文.md`, `wiki/每日学习闭环-2026-09-10-集成测试.md`

- [ ] **Step 1: 检查工作树和提交范围**

运行：`git status --short; git show --stat --oneline HEAD`

预期：只报告本次公开文档改动或用户已有未跟踪目录；最新提交统计不含私有日志和插件目录。

- [ ] **Step 2: 检查 GitHub Pages**

打开 `https://p20230101.github.io/song-second-brain/`，确认首页含“研究上下文”和“每日学习闭环”入口；打开集成测试页，确认标题和五个结构段可见。

- [ ] **Step 3: 运行最终链接检查**

运行：`rg -o '\[[^]]+\]\(([^)]+\.md)\)' index.md wiki/*.md raw/*.md | ForEach-Object { $_.Line }`

预期：输出的相对 Markdown 链接均指向仓库中存在的文件；发现失效链接时先修复再推送。
