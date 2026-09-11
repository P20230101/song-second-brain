---
title: 双轴-DIC-VFM｜种子文献筛选
type: literature-screening
domain: 工程力学
status: preliminary
updated: 2026-09-11
---

# 双轴-DIC-VFM｜种子文献筛选

## 检索记录

- 项目：`双轴-DIC-VFM-选题`
- 检索式：`biaxial test digital image correlation virtual fields method constitutive identification`
- 时间范围：2010 年至今
- 捕获数量：8 篇
- 来源状态：arXiv 成功返回；Semantic Scholar 返回 HTTP 429 限流
- 原始清单：`raw/参考文献/双轴-DIC-VFM-选题/download_manifest.json`
- 筛选依据：当前只根据标题和主题匹配做初筛，尚未完成全文方法核对；初筛不是科学结论。

## 初筛结果

| 状态 | 论文 | 原始来源 | 下一步 |
|---|---|---|---|
| 暂定纳入 | [Cruciform specimens biaxial extension performance relationship to constitutive identification](http://arxiv.org/abs/2308.01260) | arXiv，2023 | 阅读全文，提取试样、加载路径、识别参数和验证方法 |
| 暂定纳入 | [Identification of Constitutive Parameters Governing the Hyperelastic Response of Rubber by Using Full-field Measurement and the Virtual Fields Method](http://arxiv.org/abs/1907.02687) | arXiv，2019 | 阅读全文，提取全场测量、VFM 假设和参数可辨识性 |
| 初筛排除 | A Novel Approach to Analyze Fashion Digital Archive from Humanities | arXiv，2021 | 与工程力学主题不匹配，保留原始下载记录，不进入矩阵 |
| 初筛排除 | Magnetic field dynamics in isolated neutron stars with an external dipole field | arXiv，2026 | 与双轴试验、DIC、VFM 不匹配，保留原始下载记录，不进入矩阵 |
| 初筛排除 | Fitted avatars: automatic skeleton adjustment for self-avatars in virtual reality | arXiv，2023 | 与工程力学主题不匹配，保留原始下载记录，不进入矩阵 |
| 初筛排除 | Lossless Digital Image Compression Method for Bitmap Images | arXiv，2011 | 仅涉及图像压缩，不是 DIC 测量方法，保留原始下载记录，不进入矩阵 |
| 初筛排除 | A Review of Machine Learning Techniques for Applied Eye Fundus and Tongue Digital Image Processing with Diabetes Management System | arXiv，2020 | 与工程力学主题不匹配，保留原始下载记录，不进入矩阵 |
| 初筛排除 | Underdetermined Blind Source Separation via Weighted Simplex Shrinkage Regularization and Quantum Deep Image Prior | arXiv，2026 | 与 DIC/VFM 双轴试验不匹配，保留原始下载记录，不进入矩阵 |

## 目前能说什么

- 当前只确认有 2 篇标题与双轴试样、全场测量或 VFM 参数识别直接相关。
- 还不能据此确定研究缺口、材料选择、加载路径、VFM 本构模型或创新点。
- 6 篇排除项不删除，因为它们是检索过程的原始记录；它们不进入正式文献矩阵。
- 这次结果说明单一长检索式的精度不足。后续应拆成“试样/加载”“DIC 测量”“VFM 识别”三组短检索式，并逐批筛选。

## 下一道闸门

只对 2 篇暂定纳入论文做全文提取，固定记录：

1. 材料、试样几何、夹具和边界条件；
2. 双轴加载方向、控制模式、加载路径和重复试验；
3. DIC 相机、标定、散斑、位移/应变计算设置；
4. VFM 的本构假设、虚场、待识别参数和输入场量；
5. 力—位移、全场应变和 VFM 结果如何相互验证；
6. 作者明确写出的限制，以及可从方法中直接核对的限制。

全文提取完成并通过来源核对后，才进入 `wiki/<项目名>-文献矩阵.md` 和研究问题生成阶段。
