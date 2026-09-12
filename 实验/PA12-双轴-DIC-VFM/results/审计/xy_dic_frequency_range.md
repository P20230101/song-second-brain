# XY DIC 有效频率范围表

频率只作为平均有效频率范围使用，不代表逐帧硬件时间戳。下限使用完整 `Press.T` 时间窗口，上限使用加载起点候选到力记录末端的窗口；帧数优先采用已审计的连续 MatchID 输入帧数。

| 试验 | 方向 | 速度 (mm/s) | 名义相机频率 (Hz) | DIC 帧数 | 完整力记录频率 (Hz) | 事件窗口频率 (Hz) | 建议范围 (Hz) | 计数来源 | 状态 |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| XY_X-05-0.1-01 | X | 0.2 | 10 | 130 | 8.74 | 9.2 | 8.74–9.2 | contiguous_m2inp_or_csv_audited | blocked_incomplete_dic_frames |
| XY_X-06-1.0-01 | X | 2 | 50 | 133 | 47.33 | 49.16 | 47.33–49.16 | contiguous_m2inp_or_csv_audited | blocked_incomplete_dic_frames |
| XY_X-07-10-01 | X | 20 | 200 | 81 | 199.5 | 227.92 | 199.5–227.92 | contiguous_m2inp_or_csv_audited | blocked_incomplete_dic_frames |
| XY_Xy-0.1-01 | XY | 0.2 | 待补 | 289 | 7.93 | 7.98 | 7.93–7.98 | contiguous_m2inp_or_csv_audited | blocked_incomplete_dic_frames |
| XY_XY-0.1-02 | XY | 0.2 | 待补 | 待补 | 待补 | 待补 | 待补 | unavailable_noncontiguous_m2inp | blocked_incomplete_dic_frames |
| XY_Xy-03-10-01 | XY | 20 | 待补 | 21 | 39.22 | 43.48 | 39.22–43.48 | contiguous_m2inp_or_csv_audited | blocked_incomplete_dic_frames |
| XY_Xy-04-1-01 | XY | 2 | 待补 | 267 | 58.13 | 58.81 | 58.13–58.81 | contiguous_m2inp_or_csv_audited | blocked_incomplete_dic_frames |
| XY_Y-09-0.1-02 | Y | 0.2 | 10 | 1825 | 10.16 | 10.19 | 10.16–10.19 | contiguous_m2inp_or_csv_audited | blocked_incomplete_dic_frames |
| XY_Y-10-1-01 | Y | 2 | 101 | 1558 | 101.45 | 102.08 | 101.45–102.08 | contiguous_m2inp_or_csv_audited | blocked_incomplete_dic_frames |
| XY_Y-11-10-01 | Y | 20 | 375 | 711 | 375.66 | 375.66 | 375.66–375.66 | contiguous_m2inp_or_csv_audited | blocked_incomplete_dic_frames |

## 使用规则

- `DIC 帧数`不使用原始 JPEG 总数；优先使用连续 MatchID 输入/已核对 CSV 帧数。
- `XY-0.1-02` 的 m2inp 只有 10 个非连续帧，无法给出有意义的频率，暂时跳过；图片和力文件仍保留在逐帧清单中。
- 频率范围只用于粗同步和方案筛选；正式 VFM 仍以共同触发号或逐帧时间戳为准。
