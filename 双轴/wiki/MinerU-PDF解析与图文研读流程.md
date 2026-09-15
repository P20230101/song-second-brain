---
title: MinerU PDF 解析与图文研读流程
type: workflow
status: active
---

# MinerU PDF 解析与图文研读流程

本流程服务于 PA12 双轴拉伸、工业相机 3D 立体 DIC 与 VFM 研究。它将每篇 PDF 的原件、版面化 Markdown、导出图片和研究结论分开保存；不以 OCR 识别有原生文字层的论文正文。

## 适用范围与边界

- 仅处理已放入 `raw/参考文献/<项目>/` 的本地 PDF；原件只读、不改名、不上传公开仓库。
- 首选具有原生文字层的 PDF，并在 MinerU 中指定 `txt`。扫描件、文字层损坏件不进入本流程，等待可检索版本或人工补充。
- 不使用会启动 OCR 检测模块的 `pipeline` 后端作为正式产物来源。
- 正式解析使用 MinerU `hybrid-engine` 的 `txt` 方法；该后端在文本 PDF 中直接抽取文字，同时保留图、表和版面结构。它需要可用 CUDA GPU，或配置好兼容的远程 VLM 服务。

## 固定目录

```text
raw/参考文献/<项目>/
├── <原始论文>.pdf                 # 原始资料：只读、私有
└── MinerU-API/
    └── <论文短名>/
        ├── <论文短名>.md          # MinerU 版面化 Markdown
        ├── images/                # 从论文独立导出的图片、图表和图注关联素材
        ├── <论文短名>_content_list.json
        └── <论文短名>_middle.json

wiki/
└── <专题研读页>.md                # 只写已核对的结论、页码/图表定位与下一步
```

`raw/` 中的 PDF、MinerU Markdown、图片和 JSON 都是私有研究材料；`wiki/` 只发布可公开的综合判断，不复制受版权保护的全文或图片。

## 执行方式

当前已配置 MinerU 官方云端 API。对单篇文字型 PDF 使用 `mineru-open-api`，先以单页执行确认输出，再扩展到全文；`--ocr=false` 始终显式关闭 OCR。

```powershell
$env:MINERU_TOKEN = [Environment]::GetEnvironmentVariable('MINERU_TOKEN', 'User')
mineru-open-api extract '<PDF 绝对路径>' --model vlm --ocr=false `
  --format md,json -o '<MinerU-API 输出目录>' --timeout 1800
```

本机用户环境中的 `MINERU_TOKEN` 只由 CLI 读取，`MINERU_API_TOKEN` 由 MCP 读取；两个变量均不写入仓库。也可以在 Codex 重启后直接调用已注册的 `mineru` MCP 服务。

提出“按 MinerU 非 OCR 流程解析这篇 PDF”时，依次完成：

1. 确认 PDF 有可提取文字层，登记论文题名、作者、年份、DOI/URL 与项目目录。
2. 先解析 1 页；仅当日志没有 OCR 步骤且生成 Markdown、`images/` 和结构化清单时，才解析全文。
3. 以原 PDF 对照核验标题层级、至少两张关键图/表和对应图注；不把未核对的图像说明写成研究结论。
4. 从 Markdown 与图片清单提取“设备参数、试样、加载路径、相机/DIC、同步、VFM、局限”七类信息，写入专题研读页与文献矩阵。
5. 将可复用判断写入日报；需要确认的参数留在“来源缺口”，不以推测填补。

## 当前机器状态

本机已安装 MinerU 3.4.5、官方 `mineru-open-api` CLI v0.5.9 和 `mineru-open-mcp` 1.0.21；官方 `MinerU-Ecosystem` 源码保存在 Vault 外的 `C:\Users\Administrator\Downloads\MinerU-Ecosystem`。当前电脑无可用 CUDA，但云端 API 已成功以 `--ocr=false` 解析两篇首批论文：

- `MinerU-API/孙正平等-2025/`：1 个 Markdown、1 个 JSON、45 张图片。
- `MinerU-API/袁颖诗-2026/`：1 个 Markdown、1 个 JSON、87 张图片。

这些文件仍是私有原始研究材料，尚未将图表逐项核验后升级为 Wiki 结论。

## 研读输出的最小格式

每篇论文解析后，在对应专题页补充以下信息：

| 类别 | 必须记录 |
|---|---|
| 书目信息 | 题名、作者、年份、DOI/稳定链接 |
| 图文定位 | MinerU Markdown 标题、原 PDF 页码、图/表号、图片文件名 |
| 方法 | 试样、材料、加载路径、设备、相机/DIC、同步方式 |
| 证据等级 | 原文明确、由图表读取、待确认 |
| 可复用性 | 可直接复现的步骤、缺失参数、是否支持 PA12-DIC-VFM 路线 |

## 与报告的关系

- 日报登记当日新增 PDF、解析目录、已核对的图表和研究判断。
- 周报比较本周多篇论文的共识与矛盾，更新选题方向和来源缺口。
- 月报只汇总已完成“原件—解析—核验—专题页”闭环的文献资产。
