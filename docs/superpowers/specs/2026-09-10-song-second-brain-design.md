# “松的第二大脑”LLM Wiki 设计规格

## 目标

在现有 Obsidian Vault 中建立一套最小、可持续维护的个人知识 Wiki，并以公开 GitHub 仓库 `song-second-brain` 发布到 GitHub Pages。

系统采用 Andrej Karpathy 的 LLM Wiki 三层模型：用户负责提供原始资料和提出问题；Codex 负责把资料持续整理为相互链接的 Markdown Wiki；`AGENTS.md` 负责约束维护流程。

## 非目标

第一版不引入全文搜索、向量数据库、RAG、Dataview、Quartz、MkDocs、自动摄取脚本、定时任务或自定义前端。需要这些能力时，应先由实际规模或使用问题证明其必要性。

## 技术方案

使用 GitHub Pages 原生支持的 Jekyll 构建 Markdown 网站。仓库默认分支为 `main`，Pages 从仓库根目录发布。

选择这一方案的原因：

- 不需要额外的 Node.js 或 Python 工具链。
- 同一组 Markdown 文件可同时用于 Obsidian、GitHub 仓库浏览和 GitHub Pages。
- 第一版配置与维护成本最低。

代价是第一版不提供 Obsidian 风格的反向链接、知识图谱网页展示或站内搜索。Obsidian 桌面端仍可使用自己的图谱视图。

## 目录结构

```text
松的第二大脑/
├── .obsidian/              # Obsidian 本地配置，不属于知识三层
├── raw/                    # Raw sources：用户提供的原始资料
│   └── README.md           # 原始资料投放规则
├── wiki/                   # The wiki：Codex 维护的知识页面
│   └── README.md           # Wiki 页面与命名约定
├── docs/superpowers/specs/ # 已批准的设计规格
├── AGENTS.md               # The schema：维护规则和操作流程
├── index.md                # Wiki 总目录与 GitHub Pages 首页
├── log.md                  # 追加式操作记录
├── README.md               # GitHub 仓库说明与网站入口
├── _config.yml             # Jekyll/GitHub Pages 最小配置
└── .gitignore              # 本地状态排除规则
```

Wiki 层由根目录的 `index.md`、`log.md` 和 `wiki/` 共同组成。这样既保留清晰的三层职责，也避免为了网站首页复制一份索引。

## 三层职责

### Raw sources

`raw/` 保存文章、论文、摘录、图片、数据和其他用户选定的资料。已经进入该目录的资料视为来源事实，Codex 在维护 Wiki 时可以读取，但不得改写、重命名或删除；只有用户明确要求时才能改变原始资料。

### The wiki

`wiki/` 保存由 Codex 生成和维护的知识页面。页面可以表达来源摘要、人物、概念、主题、项目、比较或综合分析。Codex应根据新来源更新既有页面，而不是为每次输入机械创建孤立笔记。

`index.md` 是内容导向的唯一总入口。每个正式 Wiki 页面都应在其中出现，并带有相对链接和一句话摘要。

`log.md` 是时间导向的追加式记录，用于记录资料摄取、重要查询沉淀和巡检。历史条目不得重写。

### The schema

根目录 `AGENTS.md` 是 Wiki 的操作规范。它规定文件所有权、语言、链接、引用、资料摄取、查询、知识沉淀、矛盾处理和巡检规则。后续只有在真实使用暴露出规则缺口时才扩展 Schema。

## 内容约定

- Wiki 正文和操作日志使用简体中文。
- 页面使用清晰的中文标题，文件名使用稳定、可读的中文名称。
- 内部链接统一采用 Markdown 相对链接，不使用只能由 Obsidian 解析的双括号链接。
- 来源性陈述应链接到 `raw/` 中的对应资料；分析或推断必须在正文中明确标为综合判断。
- 新来源与现有结论冲突时，不静默覆盖旧结论；应在相关页面中说明冲突内容及各自来源。
- `log.md` 条目标题格式为 `## [YYYY-MM-DD] 操作类型 | 标题`。第一版支持 `ingest`、`query` 和 `lint` 三类操作。

## 核心工作流

### 摄取资料

1. 用户把一份新资料放入 `raw/` 并要求摄取。
2. Codex 阅读资料和 `index.md`，识别需要新建或更新的页面。
3. Codex把关键事实、观点、证据和与既有知识的关系写入 Wiki。
4. Codex更新受影响页面之间的交叉链接。
5. Codex更新 `index.md`。
6. Codex在 `log.md` 追加一条 `ingest` 记录。

默认一次处理一份来源，以便用户审阅重点；用户明确要求时可以批量处理。

### 查询与沉淀

1. Codex先读 `index.md`，再读取与问题有关的页面和必要的原始来源。
2. 回答时提供可追溯的 Markdown 链接。
3. 只有当答案形成可复用的知识，且用户要求写回时，才新建或更新 Wiki 页面。
4. 写回后更新 `index.md`，并在 `log.md` 追加 `query` 记录。

### 巡检

巡检检查实际可达的问题：失效的内部链接、没有被 `index.md` 收录的正式页面、没有入口的孤立页面、相互矛盾的结论、被新来源取代的陈述，以及被反复提及但尚无独立页面的重要概念。修复完成后在 `log.md` 追加 `lint` 记录。

## 发布方式

本地仓库创建完成后，通过已登录的 GitHub 账号创建公开仓库 `song-second-brain`，推送 `main` 分支，并启用 GitHub Pages。预期网址格式为：

```text
https://<github-username>.github.io/song-second-brain/
```

`_config.yml` 只设置站点标题、说明、语言和 GitHub Pages 支持的主题。Pages 首页直接使用根目录 `index.md`。

## 验收标准

- Obsidian 能把当前目录作为 Vault 正常打开。
- Raw sources、Wiki 和 Schema 三层职责可从目录和说明中直接辨认。
- `AGENTS.md` 完整约束摄取、查询、写回、矛盾处理和巡检流程。
- `index.md` 能作为本地 Wiki 总入口和 GitHub Pages 首页。
- 所有内部 Markdown 链接均指向存在的文件。
- 本地 Jekyll 构建或等价的 GitHub Pages 构建成功。
- GitHub 公开仓库 `song-second-brain` 已创建并推送。
- GitHub Pages 成功部署，公开网址可以访问首页。

## 已知限制

- 第一版没有网页端全文搜索和反向链接展示。
- GitHub Pages 发布需要用户在本机完成 GitHub 登录；登录完成后才能创建远程仓库和返回最终网址。
