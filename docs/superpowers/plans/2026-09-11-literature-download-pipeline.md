# 文献捕获与下载流水线实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**目标：** 为“松的第二大脑”建立从学术检索到本地 PDF、下载清单和后续复盘入口的第一条可运行流水线。

**架构：** `tools/literature_capture.py` 负责检索、筛选、下载和生成清单；`raw/参考文献/<项目名>/PDF原件/` 保存不可改写的 PDF；`download_manifest.json` 保存标题、作者、年份、来源和本地文件名；`wiki/文献捕获与筑巢.md` 记录使用规则。检索支持 arXiv、Semantic Scholar 和外部结果 JSON，后续 GPT Researcher 只需把结果转换成同一字段即可接入，不依赖 API Key 才能完成基础下载。

**技术栈：** Python 3.12 标准库（`urllib`、`json`、`xml.etree`、`argparse`）、公开 arXiv/Semantic Scholar API、Markdown、Obsidian、GitHub Pages。

---

### Task 1：建立文献捕获脚本

**Files:**
- Create: `tools/literature_capture.py`

- [x] **Step 1：定义 CLI 输入和输出**

实现以下参数：`--query`、`--focus`、`--project`、`--limit`、`--year-from`、`--year-to`、`--download-root`、`--from-results`。默认下载根目录为 `raw/参考文献`；每个项目创建 `PDF原件/` 和 `download_manifest.json`。

- [x] **Step 2：实现公开检索**

对 `--query` 同时调用 Semantic Scholar Graph API 和 arXiv API；统一为 `title`、`authors`、`year`、`source`、`source_url`、`pdf_url` 字段。没有 PDF URL 的记录保留在清单中并标记 `no-pdf-url`，不伪造下载地址。

- [x] **Step 3：实现外部结果 JSON 接口**

`--from-results` 接受 JSON 数组或 `{"results": [...]}`，读取已有 GPT Researcher/人工筛选结果，字段名保持同上；缺少 `pdf_url` 的记录只登记，不执行下载。

- [x] **Step 4：实现下载和清单写入**

下载成功标记 `downloaded`，失败标记 `error` 并保存错误文本；文件名依据标题生成，冲突时加顺序后缀；已有同名 PDF 不覆盖，标记 `exists`。每次运行都重写当前项目的清单快照，但不删除 PDF。

- [x] **Step 5：添加命令行帮助和错误退出**

无 `--query` 且无 `--from-results` 时退出并显示用法；项目名只允许普通文件名字符，路径保持在下载根目录下。

### Task 2：建立 Obsidian 文献入口

**Files:**
- Create: `wiki/文献捕获与筑巢.md`
- Create: `raw/参考文献/README.md`
- Modify: `index.md`
- Modify: `AGENTS.md`
- Modify: `log.md`

- [x] **Step 1：写入图片对应的动态捕获模板**

记录用途、搜索主题、关注重点、时间范围、下载路径、筛选数量、执行结果和下一步复盘入口。

- [x] **Step 2：写入 Raw sources 规则**

规定 PDF 原件只读、清单可追溯、标题/作者/年份不能凭空补写、下载后再进入摘要/证据链流程。

- [x] **Step 3：登记入口和维护日志**

在 `index.md` 登记页面，在 `AGENTS.md` 增加文献捕获规则，在 `log.md` 追加 `capture` 条目。

### Task 3：端到端下载验证

**Files:**
- Create: `raw/参考文献/下载流程测试/download_manifest.json`
- Create: `raw/参考文献/下载流程测试/PDF原件/`

- [x] **Step 1：运行帮助和语法检查**

运行 `python tools/literature_capture.py --help` 和 `python -m py_compile tools/literature_capture.py`。

- [x] **Step 2：用公开 arXiv 论文测试搜索和下载**

运行一次真实查询，限制 1 篇，确认生成 PDF 和 `download_manifest.json`，不修改 `raw/` 既有文件。

- [x] **Step 3：重复运行验证不覆盖**

对同一项目重复运行，清单中的已有文件状态应为 `exists`，文件修改时间不应改变。

- [x] **Step 4：验证清单字段和路径**

确认每条记录有标题、来源、PDF URL、本地文件名和状态；确认所有 PDF 位于对应项目的 `PDF原件/` 下。

### Task 4：发布和交接

- [x] **Step 1：运行 Markdown/链接/敏感信息检查**

确认公开 Wiki 不包含每日私有对话日志或 API Key；确认新增入口能从 `index.md` 打开。

- [x] **Step 2：提交并推送公开文件**

只提交脚本、说明和实施计划；本地下载清单与测试 PDF 由 `.gitignore` 排除，不提交 `.env`、Codex 配置或 API Key。

- [x] **Step 3：给出下一阶段入口**

下一阶段读取 `download_manifest.json` 和 PDF，执行摘要、证据链、引用位置、章节映射及每日复盘。
