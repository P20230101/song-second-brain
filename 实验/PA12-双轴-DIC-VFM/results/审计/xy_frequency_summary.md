# XY 照片—力同步汇总表

本表按用户提供的列结构生成。照片实际频率和照片窗口位移采用首尾事件锚定估算；DIC 位移列只有用户截图提供的六组保留值，其余写为待导出。DIC 有效频率范围见 `xy_dic_frequency_range.md`，加载—峰值—破坏事件帧见 `xy_event_alignment.md`，逐帧结果见 `xy_photo_force_sync.csv`。

| 试验 | 方向 | 速度 (mm/s) | 照片数量 | 照片设置频率 (Hz) | 照片实际拍摄频率估算 (Hz) | 照片导出的位移 (mm) | 力的数量 | 力数据算位移 (mm) | 力数据算时间 (s) | 力传感器频率 (Hz) | 同步状态 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| XY_X-05-0.1-01 | X | 0.2 | 165 | 10 | 11.692 | 2.58 | 14735 | 2.9508 | 14.754 | 1000 | estimated_unique_force_value |
| XY_X-06-1.0-01 | X | 2 | 133 | 50 | 49.162 | 2.66 | 2789 | 5.578 | 2.789 | 1000 | estimated_unique_force_value |
| XY_X-07-10-01 | X | 20 | 81 | 200 | 227.92 | 8 | 402 | 8.02 | 0.401 | 1000 | estimated_unique_force_value |
| XY_Xy-0.1-01 | XY | 0.2 | 289 | 待补 | 7.978 | 待导出 | 36244 | 7.26 | 36.3 | 1000 | estimated_unique_force_value |
| XY_XY-0.1-02 | XY | 0.2 | 259 | 待补 | 9.302 | 待导出 | 27980 | 5.6098 | 28.049 | 1000 | estimated_unique_force_value |
| XY_Xy-03-10-01 | XY | 20 | 21 | 待补 | 43.478 | 待导出 | 511 | 10.2 | 0.51 | 1000 | estimated_unique_force_value |
| XY_Xy-04-1-01 | XY | 2 | 267 | 待补 | 58.811 | 待导出 | 4570 | 9.152 | 4.576 | 1000 | estimated_unique_force_value |
| XY_Y-09-0.1-02 | Y | 0.2 | 1825 | 10 | 10.19 | 35.9 | 179260 | 35.9032 | 179.516 | 1000 | estimated_unique_force_value |
| XY_Y-10-1-01 | Y | 2 | 1558 | 101 | 102.085 | 30.6 | 15328 | 30.694 | 15.347 | 1000 | estimated_unique_force_value |
| XY_Y-11-10-01 | Y | 20 | 711 | 375 | 375.661 | 37.8 | 1889 | 37.8 | 1.89 | 1000 | estimated_preloaded_start |

## 判定规则

- `t_image_s_est` 将首张照片锚定到 `Press.T` 的加载起点候选，将末张照片锚定到力记录末样本，再对中间帧线性插值。每张照片因此都有唯一的插入力值。
- 该映射没有使用相机硬件时间戳或共同触发号，`vfm_eligible=false`；取得触发/时间戳后应替换 `t_image_s_est`，而不是把估算值当成实测同步。
- `照片导出的位移` 标有 `user_screenshot` 的行来自用户最新截图，其他行没有擅自从单点 CSV 推导。`photo_window_displacement_mm_est` 是本次端点映射对应的运动窗口位移。
