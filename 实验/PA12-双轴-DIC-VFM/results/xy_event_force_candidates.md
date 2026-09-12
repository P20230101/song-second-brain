# XY 事件帧—力—位移候选表

本表把事件对齐表中的候选图像帧直接展开为四通道力和四通道机器位移，作为 VFM 输入准备表。当前力值来自端点时间映射估计，`event_vfm_ready=false` 的行不得直接视为硬件同步结果。

| 试验 | 事件 | 图像帧 | 估计图像时间 (s) | X1 力 (N) | X2 力 (N) | Y1 力 (N) | Y2 力 (N) | X1 位移 (mm) | X2 位移 (mm) | Y1 位移 (mm) | Y2 位移 (mm) | 映射状态 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| XY_X-05-0.1-01 | load_onset | 0 | 0.727 | -39 | -38 | -5 | -3 | 21.6758 | 19.6357 | 39.4775 | 0.0801 | estimated_from_endpoint_time_map |
| XY_X-05-0.1-01 | force_peak | 141 | 12.7868 | -1113 | -1112 | -4 | -4 | 23.2162 | 21.1894 | 39.4773 | 0.0799 | estimated_from_endpoint_time_map |
| XY_X-05-0.1-01 | force_drop | 142 | 12.8723 | -7 | -9 | -4 | -2 | 23.0427 | 20.9408 | 39.4746 | 0.0784 | estimated_from_endpoint_time_map |
| XY_X-05-0.1-01 | file_last | 164 | 14.754 | -7 | -8 | -4 | -3 | 23.0791 | 21.0381 | 39.4766 | 0.0762 | estimated_from_endpoint_time_map |
| XY_X-06-1.0-01 | load_onset | 0 | 0.104 | -83 | -84 | -4 | -3 | 10.7002 | 8.6943 | 39.4863 | 0.0752 | estimated_from_endpoint_time_map |
| XY_X-06-1.0-01 | force_peak | 58 | 1.2838 | -1182 | -1183 | -4 | -3 | 12.2839 | 10.3014 | 39.4863 | 0.0754 | estimated_from_endpoint_time_map |
| XY_X-06-1.0-01 | force_drop | 61 | 1.3448 | -154 | -114 | -4 | -4 | 12.1353 | 10.1006 | 39.4906 | 0.0668 | estimated_from_endpoint_time_map |
| XY_X-06-1.0-01 | file_last | 132 | 2.789 | -7 | -8 | -4 | -3 | 13.4102 | 11.3906 | 39.4834 | 0.0723 | estimated_from_endpoint_time_map |
| XY_X-06-1.0-01 | visual_last_event | 132 | 2.789 | -7 | -8 | -4 | -3 | 13.4102 | 11.3906 | 39.4834 | 0.0723 | estimated_from_endpoint_time_map |
| XY_X-07-10-01 | load_onset | 0 | 0.05 | -82 | -89 | -4 | -3 | 9.3086 | 7.3174 | 39.4893 | 0.0723 | estimated_from_endpoint_time_map |
| XY_X-07-10-01 | force_peak | 28 | 0.1729 | -931 | -940 | -4 | -3 | 11.0368 | 9.1042 | 39.4893 | 0.0732 | estimated_from_endpoint_time_map |
| XY_X-07-10-01 | force_drop | 40 | 0.2255 | -147.5 | -113 | -4 | -4 | 11.2822 | 9.1157 | 39.4898 | 0.0654 | estimated_from_endpoint_time_map |
| XY_X-07-10-01 | file_last | 80 | 0.401 | -7 | -8 | -4 | -3 | 12.9551 | 10.9619 | 39.4844 | 0.0723 | estimated_from_endpoint_time_map |
| XY_Xy-0.1-01 | load_onset | 0 | 0.202 | -6 | -11 | -22 | -16 | 10.2168 | 10.2178 | 10.2148 | 10.2139 | estimated_from_endpoint_time_map |
| XY_Xy-0.1-01 | force_peak | 223 | 28.1529 | -1592 | -1607 | -1611 | -1597 | 13.0156 | 13.0155 | 13.0098 | 13.0128 | estimated_from_endpoint_time_map |
| XY_Xy-0.1-01 | force_drop | 226 | 28.5289 | -11 | -20 | -15 | -9 | 13.2504 | 13.0675 | 13.2109 | 13.3706 | estimated_from_endpoint_time_map |
| XY_Xy-0.1-01 | file_last | 288 | 36.3 | -14 | -25 | -18 | -9 | 13.8291 | 13.8301 | 13.8242 | 13.8281 | estimated_from_endpoint_time_map |
| XY_Xy-0.1-01 | visual_last_event | 288 | 36.3 | -14 | -25 | -18 | -9 | 13.8291 | 13.8301 | 13.8242 | 13.8281 | estimated_from_endpoint_time_map |
| XY_XY-0.1-02 | load_onset | 0 | 0.313 | -24 | -23 | -24 | -18 | 10.2344 | 10.2256 | 10.2275 | 10.2314 | estimated_from_endpoint_time_map |
| XY_XY-0.1-02 | force_peak | 235 | 25.5764 | -1617 | -1616 | -1610 | -1583 | 12.7646 | 12.7553 | 12.7539 | 12.7637 | estimated_from_endpoint_time_map |
| XY_XY-0.1-02 | force_drop | 237 | 25.7914 | -1435 | -1421 | -1408 | -1381 | 12.9292 | 12.7385 | 12.652 | 13.4406 | estimated_from_endpoint_time_map |
| XY_XY-0.1-02 | file_last | 258 | 28.049 | -18 | -18 | -16 | -10 | 13.0127 | 13.002 | 13.001 | 13.0107 | estimated_from_endpoint_time_map |
| XY_Xy-03-10-01 | load_onset | 0 | 0.05 | -80 | -88 | -88 | -81 | 10.543 | 10.5459 | 10.584 | 10.4775 | estimated_from_endpoint_time_map |
| XY_Xy-03-10-01 | force_peak | 7 | 0.211 | -1677 | -1698 | -1670 | -1628 | 12.1494 | 12.2217 | 12.2969 | 12.0215 | estimated_from_endpoint_time_map |
| XY_Xy-03-10-01 | force_drop | 9 | 0.257 | -551 | -481 | -482 | -441 | 12.6895 | 12.8516 | 12.4688 | 13.0869 | estimated_from_endpoint_time_map |
| XY_Xy-03-10-01 | file_last | 20 | 0.51 | -9 | -8 | -5 | 2 | 15.3037 | 15.2881 | 15.2617 | 15.3291 | estimated_from_endpoint_time_map |
| XY_Xy-03-10-01 | visual_last_event | 20 | 0.51 | -9 | -8 | -5 | 2 | 15.3037 | 15.2881 | 15.2617 | 15.3291 | estimated_from_endpoint_time_map |
| XY_Xy-04-1-01 | load_onset | 0 | 0.053 | -18 | -21 | -15 | -9 | 10.2324 | 10.2354 | 10.2393 | 10.2275 | estimated_from_endpoint_time_map |
| XY_Xy-04-1-01 | force_peak | 142 | 2.4675 | -1508 | -1534 | -1548 | -1490 | 12.6616 | 12.6631 | 12.6626 | 12.6607 | estimated_from_endpoint_time_map |
| XY_Xy-04-1-01 | force_drop | 147 | 2.5526 | -202 | -154 | -153 | -132 | 12.9791 | 12.8077 | 12.9555 | 13.107 | estimated_from_endpoint_time_map |
| XY_Xy-04-1-01 | file_last | 266 | 4.576 | -15 | -21 | -15 | -11 | 14.7734 | 14.7725 | 14.7695 | 14.7793 | estimated_from_endpoint_time_map |
| XY_Y-09-0.1-02 | load_onset | 0 | 0.525 | -8 | -8 | -31 | -30 | 0.0938 | 39.5381 | 7.0615 | 7.2344 | estimated_from_endpoint_time_map |
| XY_Y-09-0.1-02 | force_peak | 1112 | 109.6467 | -9 | -8 | -1486 | -1488 | 0.0928 | 39.5381 | 17.9736 | 18.152 | estimated_from_endpoint_time_map |
| XY_Y-09-0.1-02 | force_drop | 1819 | 179.0253 | -9 | -8 | -3 | -4 | 0.084 | 39.5439 | 24.8809 | 25.3054 | estimated_from_endpoint_time_map |
| XY_Y-09-0.1-02 | file_last | 1824 | 179.516 | -8 | -8 | -4 | -3 | 0.0898 | 39.5391 | 24.96 | 25.1387 | estimated_from_endpoint_time_map |
| XY_Y-09-0.1-02 | visual_last_event | 1824 | 179.516 | -8 | -8 | -4 | -3 | 0.0898 | 39.5391 | 24.96 | 25.1387 | estimated_from_endpoint_time_map |
| XY_Y-10-1-01 | load_onset | 0 | 0.095 | -7 | -8 | -31 | -29 | 0.0898 | 39.5391 | 6.1113 | 6.2129 | estimated_from_endpoint_time_map |
| XY_Y-10-1-01 | force_peak | 888 | 8.7936 | -7 | -8 | -1458 | -1459 | 0.0898 | 39.5391 | 14.8151 | 14.9449 | estimated_from_endpoint_time_map |
| XY_Y-10-1-01 | file_last | 1557 | 15.347 | -7 | -8 | -1243 | -1245 | 0.0898 | 39.5391 | 21.3662 | 21.4941 | estimated_from_endpoint_time_map |
| XY_Y-11-10-01 | force_peak | 0 | 0 | -9 | -8 | -1559 | -1552 | 0.0869 | 39.5391 | 10.5977 | 10.6309 | estimated_from_endpoint_time_map |
| XY_Y-11-10-01 | file_last | 710 | 1.89 | -7 | -8 | -3 | -11 | 0.0859 | 39.5391 | 29.501 | 29.5645 | estimated_from_endpoint_time_map |
| XY_Y-11-10-01 | visual_last_event | 710 | 1.89 | -7 | -8 | -3 | -11 | 0.0859 | 39.5391 | 29.501 | 29.5645 | estimated_from_endpoint_time_map |

## 使用规则

- `load_onset`、`force_peak`、`force_drop` 是力侧事件投影到图像帧的候选；`file_last` 和 `visual_last_event` 是图像末端候选。
- VFM 试跑先使用事件顺序完整且图像证据明确的试验；`XY-0.1-02` 的破坏候选帧因 DIC 输入未覆盖，必须先重建 MatchID 输入。
- 该表用于准备和筛选，真正提交论文前仍需共同触发/时间戳或同步敏感性分析。
