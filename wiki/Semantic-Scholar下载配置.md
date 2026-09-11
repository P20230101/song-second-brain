---
title: Semantic Scholar 下载配置
type: tool-configuration
status: local-only
---

# Semantic Scholar 下载配置

`tools/literature_capture.py` 会通过 Semantic Scholar Academic Graph 的 **paper search bulk** 端点检索论文元数据，并在结果提供公开 PDF 地址时下载 PDF 原件。下载器优先读取本机 `S2_API_KEY`，也兼容 `SEMANTIC_SCHOLAR_API_KEY`。

## 为什么需要 Key

无 Key 时，Semantic Scholar 使用共享限流池，可能返回 HTTP 429。设置个人 Key 后，下载器会以 `x-api-key` 请求头调用官方 API，提高请求稳定性。

## 一次性本机配置

1. 在 [Semantic Scholar API Key 页面](https://www.semanticscholar.org/product/api#api-key-form)申请个人 API Key。
2. 在 Windows PowerShell 中执行：

   ```powershell
   setx S2_API_KEY "你的密钥"
   ```

3. 关闭并重新打开 Obsidian Terminal 或 PowerShell。
4. 在 Vault 根目录验证变量只显示是否存在，不显示密钥：

   ```powershell
   [bool]$env:S2_API_KEY
   ```

## 使用规则

- Key 只保存在本机环境变量中，不写入 Markdown、`download_manifest.json`、`.env` 或 Git。
- 下载器优先使用官方 bulk search 端点；若仍遇 HTTP 429，会读取 `Retry-After`，否则按 2、4、8、16 秒指数退避，最多重试 4 次。仍被限流时会把错误写入下载清单，不将失败伪装成成功。
- Semantic Scholar 的搜索元数据不等于可下载全文。只有 `openAccessPdf` 返回可公开访问的 PDF 地址时，下载器才保存原件。
- 文献下载后仍需按主题筛选；关键词命中不等于与双轴-DIC-VFM 研究方向相关。

## 当前机器状态（2026-09-11）

- 用户级 `S2_API_KEY` 已配置，下载器会从 `S2_API_KEY` 读取并发送 `x-api-key` 请求头；密钥值不写入本页。
- 交互式 search 端点曾受 HTTP 429 限流；现已切换到官方 bulk search 端点，并完成带 API Key 的最小请求验证。若出口仍被整体限流，脚本会按既定策略重试并显式记录失败，不把限流当成检索成功。
- 恢复稳定后可在 Vault 根目录运行：

  ```powershell
  python tools/literature_capture.py --help
  ```

  再按帮助中的检索参数执行，生成的原始 PDF 仍只保存到 `raw/参考文献/`。
