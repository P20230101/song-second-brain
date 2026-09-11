---
title: Semantic Scholar 下载配置
type: tool-configuration
status: local-only
---

# Semantic Scholar 下载配置

`tools/literature_capture.py` 会检索 Semantic Scholar 的论文元数据，并在结果提供公开 PDF 地址时下载 PDF 原件。下载器优先读取本机 `S2_API_KEY`，也兼容 `SEMANTIC_SCHOLAR_API_KEY`。

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
- 下载器在 HTTP 429 后只等待并重试一次；第二次仍被限流时，会把错误写入下载清单，不将失败伪装成成功。
- Semantic Scholar 的搜索元数据不等于可下载全文。只有 `openAccessPdf` 返回可公开访问的 PDF 地址时，下载器才保存原件。
- 文献下载后仍需按主题筛选；关键词命中不等于与双轴-DIC-VFM 研究方向相关。
