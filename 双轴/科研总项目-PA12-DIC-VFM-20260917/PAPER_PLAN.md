# PAPER PLAN｜第一篇最小可发表论文

## 1. 暂定题目

`Full-field constitutive identification and loading-path validation of PA12 under uniaxial and biaxial loading: a virtual-fields and identifiability study`

题目中的 `PA12`、`biaxial`、`full-field` 和 `identification` 只有在数据契约与 Gate 4–9 通过后才可以保留。

## 2. 论文主线

```text
文献缺口
  → 可证伪假设
  → 数据审计与准入
  → M0/M1/M2 模型筛选
  → Abaqus Virtual Experiment 真参数回收
  → 单轴/双轴/联合 VFM
  → FIM、噪声、初值和模型形式误差
  → 独立路径/试样留出
  → 真实 PA12 全场验证
  → 材料与测量链解释
```

## 3. 结果图计划

1. 研究流程图与 Gate；
2. 试样、打印方向、DIC/加载装置和坐标系；
3. 单轴整体曲线与可用帧窗口；
4. 双轴 Fx/Fy 与 DIC 位移/应变场；
5. M0/M1/M2 本构曲线和残差比较；
6. Virtual Experiment 真参数回收；
7. 多初值结果和 objective landscape；
8. 参数灵敏度、相关矩阵与 FIM 条件数；
9. 噪声/时移/空间分辨率对参数误差的影响；
10. 不同比例双轴路径的信息量；
11. 未见路径的载荷预测与区间；
12. FEM–DIC 全场对比及边缘/局部化误差。

若一项计算不能支撑上述结果图或明确的审稿问题，删除它，不为“做过分析”保留。

## 4. 章节结构

1. Introduction：窄缺口、假设和贡献边界；
2. Materials and data audit：工艺、试样、DIC、力和同步契约；
3. Constitutive candidates and VFM：M0–M2、虚功、Virtual Experiment；
4. Verification：真参数回收、噪声和数值实现；
5. Identification and identifiability：曲线-only、单轴场、联合场；
6. Held-out prediction：整条未见路径/独立试样；
7. Physical interpretation and limitations：材料、全场信息和数据边界；
8. Conclusions：只总结已通过 Gate 的结论。

## 5. 反方审稿人门槛

投稿前必须能回答：VFM 比传统拟合多提供了什么？双轴比单轴多提供了什么？参数是否可辨识？是否有独立预测？结果是否依赖单一初值、噪声假设、单一试样或过度复杂模型？若其中任一项没有证据，论文主张必须降级。

## 6. 复现与补充材料

补充材料至少包含：数据字段契约、版本与单位、VFM 虚场、参数范围/初值、优化器设置、所有模型公式、synthetic truth、噪声情景、失败解、留出划分、图表生成脚本和不公开原始数据的访问说明。
