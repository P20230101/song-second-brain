# 图件来源与替换规则

## Fig1_traceable_measurement_chain.png

- 用途：展示双轴加载、边界力/位移、帧—机器时间映射、2D-DIC、ROI 质量门和 VFM 独立验证之间的关系。
- 类型：方法流程示意图，不是实验结果图，不包含本项目测得的数字。
- 来源：根据本研究的测量链定义生成并人工检查可读性；当前文件为 2172 × 724 像素 PNG。
- 使用边界：只能支持“研究流程如何连接”的说明，不能支持 PA12 材料常数、精度、误差或优越性结论。
- 投稿替换：提交前按目标期刊图件分辨率要求导出；依据真实设备、通道数量、软件名称和数据流更新标签；若实际流程不同，以实验记录为准修改或删除。

## 当前已生成的实证审计图件

- `results/analysis/Fig2_force_history_audit.png`：10 组 XY 序列的逐帧通道载荷历史；由 `results/审计/xy_photo_force_sync.csv` 生成。横轴为 JPG 帧号，载荷采用端点估计映射，不能解释为硬件同步结果。
- `results/analysis/Fig3_frequency_frame_audit.png`：端点估计图像频率与 JPG/MatchID 输入帧数一致性；由 `xy_frequency_summary.csv` 生成。
- `results/analysis/Fig4_event_frame_audit.png`：加载、峰值、峰后下降和图像末端候选帧投影；所有事件标记均需复核。
- `results/analysis/Fig5_timing_sensitivity_Xy-0.1-01.png`：`XY_Xy-0.1-01` 的 ±1/±2/±5 帧假设时间扰动；这是情景敏感性图，不是实测同步不确定度。

上述图件均由本项目数据和可复算脚本生成，使用序列级文件计数而非独立试样统计。CAD/有限元中心区验证、完整 DIC 质量图、VFM 参数图和独立路径验证图仍待相应字段补齐，不能用示意数据填充。
