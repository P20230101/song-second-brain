# “松的第二大脑”Wiki Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在当前 Obsidian Vault 中建立最小的三层 LLM Wiki，并以公开仓库 `P20230101/song-second-brain` 发布到 GitHub Pages。

**Architecture:** 根目录的 `AGENTS.md` 是 Schema，`raw/` 是不可由代理改写的原始资料层，根目录的 `index.md`、`log.md` 与 `wiki/` 共同构成 Wiki 层。GitHub Pages 使用仓库根目录的 Jekyll 配置构建，同一组标准 Markdown 文件同时服务 Obsidian、GitHub 和公开网站。

**Tech Stack:** Markdown、Obsidian、Git、GitHub CLI、GitHub Pages、Jekyll `jekyll-theme-minimal`

---

## 文件职责

- `.gitignore`：排除 Obsidian 本机状态和 Jekyll 构建产物。
- `_config.yml`：配置 GitHub Pages 的标题、语言、地址和官方支持主题。
- `README.md`：说明仓库用途、三层架构和公开网站入口。
- `raw/README.md`：规定原始资料的投放边界和不可变规则。
- `wiki/README.md`：说明 Wiki 页面类型、语言、文件名和链接约定。
- `AGENTS.md`：定义 Codex 的资料摄取、查询、写回、矛盾处理和巡检工作流。
- `index.md`：公开站点首页和 Wiki 唯一总目录。
- `log.md`：以固定标题格式保存追加式维护记录。
- `docs/superpowers/specs/2026-09-10-song-second-brain-design.md`：已批准设计，不再修改。

### Task 1: 建立仓库与 GitHub Pages 基础文件

**Files:**

- Create: `.gitignore`
- Create: `_config.yml`
- Create: `README.md`

- [ ] **Step 1: 运行基础文件缺失检查，确认检查会失败**

Run:

```powershell
$required = @('.gitignore', '_config.yml', 'README.md')
$missing = $required | Where-Object { -not (Test-Path -LiteralPath $_) }
if ($missing) { throw "缺少基础文件: $($missing -join ', ')" }
```

Expected: FAIL，错误中列出三个缺失文件。

- [ ] **Step 2: 创建 `.gitignore`**

```gitignore
# Obsidian 本机状态
.obsidian/

# Jekyll 本地构建产物
_site/
.jekyll-cache/
.jekyll-metadata
```

- [ ] **Step 3: 创建 `_config.yml`**

```yaml
title: 松的第二大脑
description: 基于 LLM 持续维护的个人知识 Wiki
lang: zh-CN
url: https://p20230101.github.io
baseurl: /song-second-brain
theme: jekyll-theme-minimal
show_downloads: false
```

- [ ] **Step 4: 创建 `README.md`**

```markdown
# 松的第二大脑

一个由 Obsidian 浏览、由 Codex 持续维护的个人知识 Wiki。方法参考 [Andre Karpathy 的 LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)。

## 在线访问

[打开“松的第二大脑”](https://p20230101.github.io/song-second-brain/)

## 架构

- `raw/`：用户提供的原始资料，代理只读。
- `wiki/`、`index.md`、`log.md`：代理维护的 Wiki。
- `AGENTS.md`：规定 Wiki 结构和维护工作流的 Schema。

使用方式请从 [Wiki 首页](index.md) 开始。
```

- [ ] **Step 5: 重跑基础文件检查，确认通过**

Run:

```powershell
$required = @('.gitignore', '_config.yml', 'README.md')
$missing = $required | Where-Object { -not (Test-Path -LiteralPath $_) }
if ($missing) { throw "缺少基础文件: $($missing -join ', ')" }
"基础文件齐全"
```

Expected: PASS，输出 `基础文件齐全`。

- [ ] **Step 6: 提交基础文件**

```powershell
git add -- .gitignore _config.yml README.md
git diff --cached --check
git commit -m "chore: set up Obsidian vault publishing"
```

Expected: 新提交只包含三个基础文件。

### Task 2: 建立 Raw sources、Wiki 与 Schema 三层

**Files:**

- Create: `raw/README.md`
- Create: `wiki/README.md`
- Create: `index.md`
- Create: `log.md`
- Create: `AGENTS.md`

- [ ] **Step 1: 运行三层结构缺失检查，确认检查会失败**

Run:

```powershell
$required = @('raw/README.md', 'wiki/README.md', 'index.md', 'log.md', 'AGENTS.md')
$missing = $required | Where-Object { -not (Test-Path -LiteralPath $_) }
if ($missing) { throw "三层结构不完整: $($missing -join ', ')" }
```

Expected: FAIL，错误中列出五个缺失文件。

- [ ] **Step 2: 创建 `raw/README.md`**

```markdown
---
title: 原始资料
---

# 原始资料（Raw sources）

把准备纳入 Wiki 的文章、论文、摘录、图片或数据放在此目录。

## 规则

- 已放入的来源是事实依据，Codex 只读，不改写、重命名或删除。
- 一次放入一份来源并要求“摄取”，最容易审阅知识更新。
- 此仓库公开，只能放入允许公开且有权保存的资料。
- 图片等附件统一放在 `raw/assets/`；首次需要时再创建该目录。
```

- [ ] **Step 3: 创建 `wiki/README.md`**

```markdown
---
title: Wiki 页面说明
---

# Wiki 页面说明

此目录保存由 Codex 创建和维护的知识页面，例如来源摘要、概念、人物、主题、项目、比较和综合分析。

## 约定

- 正文使用简体中文。
- 文件名使用稳定、可读的中文名称。
- 内部链接使用标准 Markdown 相对链接。
- 来源性陈述链接到 `raw/` 中的对应资料。
- 正式页面必须登记到根目录的 [`index.md`](../index.md)。
```

- [ ] **Step 4: 创建 `index.md`**

```markdown
---
title: 首页
---

# 松的第二大脑

这里是一座由原始资料持续编译而成的个人知识 Wiki。你负责选择资料、提出问题和判断重点；Codex 负责总结、交叉引用、维护页面和记录变化。

## 开始使用

1. 阅读[原始资料说明](raw/README.md)，将一份资料放入 `raw/`。
2. 告诉 Codex“摄取这份资料”。
3. 从本页进入新建或更新的知识页面。

## Wiki 导航

当前尚无正式知识页面。完成第一次资料摄取后，页面链接和一句话摘要会出现在这里。

## 系统入口

- [原始资料说明](raw/README.md)
- [Wiki 页面说明](wiki/README.md)
- [维护日志](log.md)
- [维护规则](AGENTS.md)
```

- [ ] **Step 5: 创建 `log.md`**

```markdown
---
title: 维护日志
---

# 维护日志

本文件按时间顺序追加记录，不改写历史条目。

## [2026-09-10] init | 建立“松的第二大脑”

- 建立 Raw sources、Wiki 与 Schema 三层结构。
- 配置 Obsidian 兼容的 Markdown Wiki 与 GitHub Pages 发布入口。
```

- [ ] **Step 6: 创建 `AGENTS.md`**

```markdown
# “松的第二大脑”维护规则

## 目标与分工

本仓库是一套持续积累的 LLM Wiki。用户负责选择原始资料、提出问题和判断方向；Codex 负责读取资料、维护相互链接的知识页面、更新索引并记录操作。

## 三层架构

### Raw sources

- `raw/` 保存用户提供的原始资料，是来源事实层。
- Codex 可以读取，但不得改写、重命名或删除已有原始资料。
- 只有用户明确要求时，才能改变 `raw/` 中的内容。

### The wiki

- `wiki/` 保存由 Codex 生成和维护的知识页面。
- 根目录 `index.md` 是全部正式 Wiki 页面的唯一总目录。
- 根目录 `log.md` 是追加式维护记录，不得重写历史条目。

### The schema

- 本文件是 Wiki 的 Schema。
- 只在真实使用暴露出规则缺口时修改本文件，不添加推测性流程。

## 内容规则

- Wiki 正文和日志使用简体中文。
- 页面标题清楚描述主题；文件名使用稳定、可读的中文名称。
- 内部链接统一使用 Markdown 相对链接，不使用仅 Obsidian 可解析的双括号链接。
- 来源性陈述必须链接到 `raw/` 中的资料。综合分析或推断要明确写成判断，不伪装成来源原文。
- 优先更新已有主题页并增加交叉链接，不为每次输入机械创建孤立页面。
- 每个正式 Wiki 页面都必须在 `index.md` 中登记相对链接和一句话摘要。

## 摄取工作流

当用户要求摄取一份或多份原始资料时：

1. 读取本文件、`index.md`、目标原始资料以及与它相关的既有 Wiki 页面。
2. 提取关键事实、观点、证据、限制以及与既有知识的关系。
3. 判断应更新已有页面还是创建新页面，只修改完成摄取所必需的文件。
4. 在 Wiki 页面中加入原始资料链接和必要的交叉链接。
5. 若新来源与现有结论冲突，在相关页面明确记录冲突内容和各自来源，不静默覆盖旧结论。
6. 更新 `index.md` 中受影响页面的链接和一句话摘要。
7. 在 `log.md` 末尾追加 `## [YYYY-MM-DD] ingest | 标题` 条目，列出来源和受影响页面。

默认一次处理一份来源；只有用户明确要求时才批量摄取。

## 查询与知识沉淀

回答 Wiki 相关问题时：

1. 先读取 `index.md`，再读取相关 Wiki 页面和必要的原始资料。
2. 回答中给出可追溯的 Markdown 文件链接。
3. 只有答案形成可复用知识且用户要求写回时，才创建或更新 Wiki 页面。
4. 写回后更新 `index.md`，并在 `log.md` 末尾追加 `## [YYYY-MM-DD] query | 标题` 条目。

## Wiki 巡检

用户要求巡检时，检查并修复：

- 指向不存在文件的内部链接；
- 未登记在 `index.md` 中的正式 Wiki 页面；
- 没有入口或交叉链接的孤立页面；
- 页面之间相互矛盾的结论；
- 已被新来源取代但未标明的陈述；
- 被反复提及但尚无独立页面的重要概念。

完成后在 `log.md` 末尾追加 `## [YYYY-MM-DD] lint | Wiki 巡检` 条目，记录发现和修改。

## 修改边界

- 只修改当前请求必须改变的文件。
- 不删除或整理用户已有的 Obsidian 笔记、Canvas 和本地配置。
- 不添加搜索、数据库、自动化脚本、模板系统或插件，除非用户明确要求。
- 不吞掉错误；无法读取来源、链接失效或事实冲突时直接说明。
```

- [ ] **Step 7: 重跑三层结构检查，确认通过**

Run:

```powershell
$required = @('raw/README.md', 'wiki/README.md', 'index.md', 'log.md', 'AGENTS.md')
$missing = $required | Where-Object { -not (Test-Path -LiteralPath $_) }
if ($missing) { throw "三层结构不完整: $($missing -join ', ')" }
"三层结构齐全"
```

Expected: PASS，输出 `三层结构齐全`。

- [ ] **Step 8: 提交三层结构**

```powershell
git add -- raw/README.md wiki/README.md index.md log.md AGENTS.md
git diff --cached --check
git commit -m "feat: create minimal LLM wiki structure"
```

Expected: 新提交只包含五个三层架构文件。

### Task 3: 验证本地结构和 Markdown 链接

**Files:**

- Test only; no files are created or modified.

- [ ] **Step 1: 验证 Git 跟踪文件范围**

Run:

```powershell
git status --short
git ls-files
```

Expected: `.obsidian/` 不出现；已跟踪文件只包括设计、计划和本计划创建的 Wiki 文件。用户已有的日记、Canvas 或欢迎页即使仍显示为未跟踪，也不得加入提交。

- [ ] **Step 2: 验证 Markdown 内部链接目标存在**

Run:

```powershell
$broken = [System.Collections.Generic.List[string]]::new()
Get-ChildItem -Recurse -File -Filter '*.md' |
  Where-Object { $_.FullName -notmatch '[\\/]\.git[\\/]' } |
  ForEach-Object {
    $source = $_
    $text = Get-Content -Raw -LiteralPath $source.FullName
    [regex]::Matches($text, '\[[^\]]+\]\((?!https?://|mailto:|#)([^)#]+)(?:#[^)]*)?\)') |
      ForEach-Object {
        $target = [uri]::UnescapeDataString($_.Groups[1].Value)
        $path = Join-Path $source.DirectoryName $target
        if (-not (Test-Path -LiteralPath $path)) {
          $broken.Add("$($source.FullName) -> $target")
        }
      }
  }
if ($broken.Count) { throw "失效链接:`n$($broken -join "`n")" }
"内部链接全部有效"
```

Expected: PASS，输出 `内部链接全部有效`。若失败，修正对应 Markdown 链接并重新运行。

- [ ] **Step 3: 验证提交内容不存在空白错误**

Run:

```powershell
git diff --check HEAD
```

Expected: PASS，无输出。

### Task 4: 创建公开 GitHub 仓库并启用 Pages

**Files:**

- External state: create `github.com/P20230101/song-second-brain`
- External state: enable GitHub Pages from `main` branch root

- [ ] **Step 1: 确认目标仓库尚不存在**

Run:

```powershell
gh repo view P20230101/song-second-brain
```

Expected: FAIL，GitHub 返回仓库不存在。如果仓库已经存在，立即停止，不覆盖或复用，先向用户报告。

- [ ] **Step 2: 创建公开仓库并推送 `main`**

Run:

```powershell
gh repo create song-second-brain --public --source=. --remote=origin --push --description "松的第二大脑：基于 LLM 持续维护的个人知识 Wiki"
```

Expected: 创建 `https://github.com/P20230101/song-second-brain`，添加 `origin`，并成功推送 `main`。

- [ ] **Step 3: 启用从 `main` 根目录发布的 GitHub Pages**

Run:

```powershell
gh api --method POST repos/P20230101/song-second-brain/pages --field 'source[branch]=main' --field 'source[path]=/'
```

Expected: HTTP 201；响应中的 `html_url` 为 `https://p20230101.github.io/song-second-brain/`。

### Task 5: 验证远程仓库与公开页面

**Files:**

- Test only; no files are created or modified.

- [ ] **Step 1: 验证远程仓库公开、默认分支正确**

Run:

```powershell
gh repo view P20230101/song-second-brain --json nameWithOwner,visibility,defaultBranchRef,url
```

Expected: `nameWithOwner` 为 `P20230101/song-second-brain`，`visibility` 为 `PUBLIC`，默认分支为 `main`。

- [ ] **Step 2: 等待 Pages 构建完成**

Run:

```powershell
$deadline = (Get-Date).AddMinutes(5)
do {
  $build = gh api repos/P20230101/song-second-brain/pages/builds/latest | ConvertFrom-Json
  if ($build.status -eq 'built') { break }
  if ($build.status -eq 'errored') { throw "GitHub Pages 构建失败" }
  Start-Sleep -Seconds 10
} while ((Get-Date) -lt $deadline)
if ($build.status -ne 'built') { throw "GitHub Pages 构建在 5 分钟内未完成" }
"Pages 构建成功"
```

Expected: PASS，输出 `Pages 构建成功`。若失败，读取构建错误并只修复导致 Jekyll 构建失败的配置或 Markdown。

- [ ] **Step 3: 验证公开首页内容**

Run:

```powershell
$response = Invoke-WebRequest -UseBasicParsing 'https://p20230101.github.io/song-second-brain/'
if ($response.StatusCode -ne 200) { throw "首页 HTTP 状态为 $($response.StatusCode)" }
if ($response.Content -notmatch '松的第二大脑') { throw '首页缺少站点标题' }
"公开首页可访问"
```

Expected: PASS，输出 `公开首页可访问`。

- [ ] **Step 4: 最终核对本地与远程提交一致**

Run:

```powershell
git fetch origin main
$local = git rev-parse HEAD
$remote = git rev-parse origin/main
if ($local -ne $remote) { throw "本地与远程提交不一致" }
git status --short --branch
```

Expected: 本地 `HEAD` 与 `origin/main` 相同；用户原有未跟踪文件可以存在，但没有本计划产生的未提交修改。
