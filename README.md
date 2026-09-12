# 松的第二大脑

一个由 Obsidian 浏览、由 Codex 持续维护的个人知识 Wiki。方法参考 [Andre Karpathy 的 LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)。

## 在线访问

[打开“松的第二大脑”](https://p20230101.github.io/song-second-brain/)

## 架构

- `raw/`：用户提供的原始资料，代理只读。
- `wiki/`、`index.md`、`log.md`：代理维护的 Wiki。
- `AGENTS.md`：规定 Wiki 结构和维护工作流的 Schema。

使用方式请从 [Wiki 首页](index.md) 开始。

日常实验只看：

- [事件和频率概览](实验/PA12-双轴-DIC-VFM/results/02_事件和频率概览.md)
- [VFM 照片—力对应表](实验/PA12-双轴-DIC-VFM/results/01_VFM照片力对应.csv)

详细技术结果统一放在 `实验/PA12-双轴-DIC-VFM/results/审计/`，不作为日常入口。
