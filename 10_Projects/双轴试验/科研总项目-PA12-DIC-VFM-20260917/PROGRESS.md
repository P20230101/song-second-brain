# PROGRESS｜项目进度与反方审查

更新时间：2026-09-20。

## 当前阶段

`Phase 13.5–14：真实实验质量分层与 AI pilot 审查；正式 Phase 14 门关闭`。

当前状态以 2026-09-19 的三级修复、Phase 12.1–12.3 审查和机器可读质量报告为准：5 组真实实验通过工程质量门，0 组达到 `constitutive_validated`；Phase 14 仅保留 `pilot_only=true` 的实验级拆分结果。

- 真实 `XY_Y-09-0.1-02` 的 1,825 个 `.dat`、1,825 张图像和 1,825 行力映射进入 `real_data_pipeline`，逐点输出各为 1,042,512 行；
- 真实 `XY_Xy-0.1-01` 的 289 个 `.dat`、289 张图像和 289 行力映射也已进入同一管线；候选逐点输出为 3,035,477 行，正式归一化表为 3,034,764 行；
- `MatchIDReader.exe` 实际接收真实 `Job.m2inp` 后以 `-532462766` 退出，没有生成正式 CSV；`Job.m2inp` 不是 `GetFromExternal` 的 Dataset ID；
- 对 `XY_Xy-0.1-01` 的派生真实工程，已将旧图像根路径重写为真实 D 盘路径；MatchID 2019.2.2 完成 289 帧并生成 289 个非空带表头正式 CSV，原始工程保持不变；
- 正式 CSV 已归一化为 `formal_vfm_input.csv.gz`，共 3,034,764 行；`x/y/u/v/exx/eyy/exy` 和质量字段已绑定，时间与边界力仍按估计列隔离；
- 已从真实 `Press` 文件生成 `Force.csv`：36,244 点，0–36.3 s，单位 N，单调无重复，中位采样频率约 1000 Hz；
- 在端点锚定/共同触发假设下完成 289 帧到真实力值的匹配，`force_missing_ratio=0`、`boundary_complete=true`、最大最近样本误差 0.000881944 s；正式输入新增并填充 `Fx/Fy/boundary_force`，但这不是独立硬件同步证明；
- 运行 manifest 与 `vfm_ready_check.json` 明确 `source_is_real=true`、`synthetic_used=false`、`ai_used=false`；
- `vfm_ready_check.json` 将首末帧端点锚定得到的 `t_image_s_est` 记录为共同触发假设下的估计时间，并标记 `vfm_eligible=true`；当前没有独立相机/机器时间戳、触发 ID 或原始同步日志，因此该标记不等于同步已被实验记录独立证明。
- Phase 8 已新增真实单轴 VFM 求解入口并运行 `XY_Xy-0.1-01`：数值迭代 2 次收敛到 `E=178.534841 MPa`，但相对 L2 虚功残差为 `0.857603520`；
- 当前试验横向力峰值比为 `0.996269096`，单轴适用性未通过；本次结果仅作为真实 VFM 闭环审计，不进入 PA12 材料数据库，需明确单轴试验或转入 Phase 11 双轴 VFM。
- Phase 9 已使用真实 Phase 8 输入和 `scipy.optimize.least_squares` 识别 J2 幂律硬化参数；拟合主支路为峰值帧 225 之前的 226 帧，末段缺少边界位移的 285–288 帧已排除并记录；
- 识别数值收敛到 `E=976.581521 MPa`、`ν≈0`、`σ_y=42.858276 MPa`、`H=208.950633 MPa`、`n=0.883580`，力相对 L2 误差 `0.439011425`；因近双轴载荷和高残差，参数不作为 PA12 材料数据库结果。
- Phase 10 已用上述真实识别参数完成实验—模型力—位移验证，输出 `force_compare.png`、`error_report.json` 和 `validation.md`；226 个加载点的 `RMSE=558.625175 N`、`MAE=494.674219 N`、最大绝对误差 `894.555780 N`。
- Phase 10 结论为诊断性完成，不判定材料验证通过：当前试验近双轴、单轴适用性未通过，Phase 9 参数有效性为 false。
- Phase 11 已在真实 `Fx/Fy` 和 `exx/eyy/exy` 上建立二维虚功方程，867 条方程满秩，输出 `biaxial_vfm_result.json` 及逐帧 `σxx/σyy/τxy`。
- Phase 11 的 `Q11=141.447654 MPa`、`Q22=136.925560 MPa`、`Q12=132.498045 MPa`、`Q66=-2810.116231 MPa`，相对 L2 虚功残差 `0.887819653`；剪切结果受无边界牵引分布限制，不能作为独立材料参数。
- Phase 12 已将真实单轴和真实双轴 `Fx/Fy` 残差联合输入 J2 幂律硬化优化，识别 `E=792.359795 MPa`、`ν≈0`、`σy=132.428563 MPa`、`H=715.921722 MPa`、`n=0.802127`，`nfev=25`。
- Phase 12 使用归一化误差正和，不执行“单轴误差减双轴误差”；联合目标收敛但参数唯一性未证明，结果不进入 PA12 材料数据库。
- Phase 13 已按最新质量门重建 `PA12_database.h5`：纳入 5 组真实实验，5 个问题实验写入 `audit/excluded_experiments`；数据库是数据容器，不宣称跨试样参数唯一。
- Phase 13 数据库根属性确认 `source_is_real=true`、`synthetic_used=false`、`ai_used=false`；当前分层为 `quality_passed=5`、`constitutive_validated=0`，其余结果只作 `diagnostic_only`。
- Phase 14 已在这 5 组实验上完成一次 pilot，按 `experiment_id` 划分为 3/1/1；验证/测试误差仍大，正式代理模型门保持关闭。

已完成：

- 找到实际原始数据根目录并完成文件级规模审计；
- 核对 XY/XZ 的主要文件类型、XZ 分卷缺失和项目内派生审计表；
- 确认现有 `events.csv` 只有表头，现有 XY 映射是端点锚定估计；另已找到 S16 的 259 帧图像 manifest，并由 DIC 文件名确认 0–132 的逐点输出帧号；
- 确认逐帧 MatchID `.dat` 存在；对 `XY-0.1-02` 的 259 个 `.dat` 已全部解压并解析成功。0–250、252 帧为 10,505 点，251、253–257 帧为 10,504 点，258 帧为 7,599 点。另有 `DIC-xy_0.2` 的 133 个 CSV，每帧 3,104 点、字段为像素坐标/位移与 `R/Sigma`，完整有效子集为 0–131，132 失效；其 ROI/点布局与 `.dat` 不一致，作为独立交叉检查，不能再表述为 133–258“没有逐点场”；
- 用户确认当前中心减薄厚度为 1.0 mm，名义几何按实物/模型固定；外轮廓数值化仍待录入；
- 完成第一轮 PA12、SLS/MJF、双轴 DIC–VFM、可辨识性和模型识别的交叉文献审查；
- 把宽泛创新主张降级为“未发现完整组合先例”的中等置信度候选缺口；
- 明确 M0–M7 阶梯和不新增实验优先路线。
- 新增并运行逐点 DIC CSV 审计器；133 帧结构审计通过。新增 `.dat` 全量帧审计和照片—力—`.dat` 候选表，完整场入口已确认；`.dat` 字段语义/最终有效掩膜和共同触发时间基准仍待核对。
- 将审计扩展到 `yuan/data` 全集：14 个 XY/XZ 试验目录共 6,327 个 `.dat`（XY 5,295、XZ 1,032）全部可解析；XY 的 5,309 行照片—力候选表已按试验编号/帧号合并，X-05 有 14 张照片没有对应 DAT。主试样 `XY-0.1-02` 的 259 帧已逐点导出为压缩标准化表，保留像素/毫米候选位移、R/Sigma 和筛选掩膜。
- 使用 MinerU 本地离线引擎解析项目内 PA12 双轴论文，得到正文、表格、公式和图像对象；另登记已解析的 VFM、SBVF、FE 校准和十字形试样全文证据。OCR 乱码、图注错位和项目内部来源已在 `MINERU_BODY_IMAGE_EVIDENCE.md` 中隔离，未将其升级为同行评审结论。
- 将本地题录、Wiki 矩阵和全文引用整理为 89 个唯一条目的 `LITERATURE_DATABASE.md`；当前 18 个条目含正文/图像证据（同行评审/审稿全文 15 个、公开会议全文 1 个、项目内部全文 1 个、arXiv 预印本 1 个），其中 14 条已完成项目本地 PDF/MinerU 或 pypdf 绑定：P00、PA17、PA19A、PA22–PA25、PA28、BX05、BX16、BX18、BX19、VF25、DIC01。PA17 的 UGent 会议全文已完成 6 页 pypdf 校验、6/6 页 MinerU high 解析和 9 个图像文件提取；BX05 的作者机构开放全文已完成 12 页 pypdf 校验、12/12 页 MinerU high 解析和 17 个图像/表格对象提取；PA22–PA25、PA28 的正文/图像来自官方开放全文核验；PA19A 为独立的 2015 审稿会议论文；VF08 已完成 Springer/Europe PMC 官方在线全文、公式、图表和限制条件核验，但本地 PDF/MinerU 尚未绑定；DIC01 用于 DIC 噪声/预滤波证据，BX19 为已解析的 arXiv 双轴设计预印本，其余按官方页、本地引用或待补证分级，未把条目数写成“已读 50+ 篇全文”。
- 新增全文获取与证据绑定要求：当前 `双轴` 树下共有 57 个 PDF 文件，但其中包含重复检索副本、无关条目、项目草稿和虚拟环境文件；过滤后 raw 参考文献目录有 34 个候选 PDF，且 34/34 可由 pypdf 打开。已建立受控 `literature_fulltext/literature_pdf_manifest.json`；VF25、BX16、BX18、DIC01、BX19 已用 MinerU 3.4.5 分别完成 44/44、7/7、9/9、15/15、14/14 页解析、正文/图像输出和本地绑定。上述数量仍是文件盘点，不等于 50 篇论文全文；其余条目继续按合法来源逐篇完成题录、正文页码、表/图证据和 MinerU 绑定。
- PA23 的官方开放 PDF 已保存到 `literature_fulltext/source_pdf/`，并由 MinerU hybrid-engine 完成 13/13 页解析，生成 1 个 Markdown、4 个 JSON 和 20 个提取图像文件；PA22、PA23 已完成项目本地 PDF/MinerU 绑定。
- PA24 的 Springer 官方开放 PDF 已保存到 `literature_fulltext/source_pdf/`，pypdf 成功打开并确认 10 页、题名元数据匹配；MinerU hybrid-engine 随后完成 10/10 页解析，生成 1 个 Markdown、4 个 JSON 和 20 个提取图像文件，PA24 已计入本地 PDF/MinerU 绑定。
- PA25 的 MDPI 官方开放 PDF 已保存到 `literature_fulltext/source_pdf/`，pypdf 成功打开并确认 15 页、题名/作者元数据匹配；MinerU hybrid-engine 完成 15/15 页解析，生成 1 个 Markdown、4 个 JSON 和 43 个提取图像文件，PA25 已计入本地 PDF/MinerU 绑定。正文明确记录 SLS PA12 剪切、DIC、Chaboche–改进 GTN、Abaqus UMAT 和 Abaqus–DIC 应变场对比；损伤仍不纳入首篇 M0–M2 主线。
- 文献清单生成器已将“项目本地 PDF + MinerU 绑定”作为显式 ID 注册表维护；重新生成的 `literature_pdf_manifest.json` 保持 34/34 个候选 PDF 可打开、0 个 PDF 错误，并准确登记 14 个已绑定 ID：P00、PA17、PA19A、PA22、PA23、PA24、PA25、PA28、BX05、BX16、BX18、BX19、DIC01、VF25。可读 PDF 未因存在文件而自动升级为正文证据。
- PA18 的官方 UGent 题录/摘要已完成题名、作者、年份、期刊、页码和 DOI 核对；本轮官方文件入口未形成可用全文：两次返回题名不匹配的 PDF，另一次返回访问控制 HTML。三份错误来源均已隔离到 `literature_fulltext/source_pdf/quarantine/`。PA18 未计入本地 PDF/MinerU 绑定，Gate 0 计数与证据等级不变。
- 定量比较 `XY-0.1-02` `.dat` 首帧与 legacy `DIC-xy_0.2` 首帧：点数、坐标支持域和位移范围均不一致，已确认两套导出不能按点合并；结果登记在 `results/xy_dat_legacy_crosscheck.md`。
- 只读审计并打开现有 `FO_G00_reference_UX/EQ/R05.odb`，确认 `U/S/E/RF`、非零边界反力和非均匀应变；用 CPS4R 节点虚位移—双线性插值—单点积分的离散规则重算 VFM，三条路径均回收线弹性基准参数。完整数值见 `results/abaqus_vfm_gate_audit.md` 和对应 JSON。
- 建立独立 nonlinear synthetic FE–VFM 基准：M0 线性硬化、M1 Voce、M2 Swift 均以 UX+EQ 识别并完全留出 R05；最大无噪声参数误差分别为 `1.42e-5`、`2.34e-4`、`1.29e-3`，R05 虚功误差为 `6.00e-6`、`2.12e-6`、`1.92e-5`。全部仅为通用合成参数，详见 `results/m0_m2_virtual_experiment_handoff.md`。
- 主线程用 Abaqus Python 对 9/9 个 M0–M2 ODB 以只读方式实际打开并完成逐帧抽取；每个含 23 帧、692 个 CPS4R 单元和 `E/S/PEEQ/RF`，真应力场内外虚功闭合误差为 `9.79e-7`–`1.97e-5`。证据见 `results/abaqus_odb_open_validation.md`。
- synthetic Gate 5 的 M0/M1/M2 正确模型均完成 20-start 固定种子 LHS。M0/M1 分别为 20/20 收敛，参数标准差为 `[1.28e-8, 4.49e-7]` 和 `[1.16e-8, 1.05e-7, 7.59e-7]`。M2 在完整工作环境、统一验收预算 `max_nfev=120` 下也为 20/20 收敛，`nfev=13–44`，参数标准差为 `[1.167e-6, 3.645e-9, 2.578e-8]`，最差最大相对参数误差为 `1.2874e-3`，R05 留出虚功误差为 `1.9158e-5`。原 `max_nfev=40` 时 `start_index=13` 的触限保留为优化预算敏感性，而非删除失败起点或材料不可辨识证据。详见 `results/multistart_gate5_audit.md`。
- 完成 M1 synthetic 高斯噪声边界情景：mild `strain/force=0.001/0.005` 的 seed20260917/20260918/20260919 均 20/20 收敛，最大参数误差为 `12.31%/4.89%/3.35%`；strong `0.005/0.01` 的 seed20260917/20260918/20260919 也均 20/20 收敛，最大参数误差为 `32.55%/9.00%/6.89%`。三 seed 结果仍不能形成置信区间，Gate 6 未通过。空间相关应变噪声（相对标准差 `0.001`、相关长度 `10 mm`）和一帧非循环外部功时移各完成一个单起点敏感性情景，最大参数误差分别为 `18.44%` 和 `185.71%`。全部仍是 synthetic generic benchmark，不代表真实 DIC/同步误差或 PA12 参数；完整矩阵见 `simulation/constitutive_virtual_experiment/results/gate6/gate6_m1_noise_matrix.json`。
- 新增 M0 mild 高斯噪声 20-start：`seed20260920` 在 `max_nfev=120` 下 20/20 收敛，最大参数误差 `8.206%`；R05 留出虚功/广义反力/应力场误差 `0.653%/0.687%/1.227%`。结果为 `simulation/constitutive_virtual_experiment/results/gate6/M0_mild_seed20260920_s20_retry1.json`，仅扩充 generic synthetic 噪声证据，不代表真实 PA12，也不能使 Gate 6 通过。
- M1 strong iid 高斯噪声 `strain/force=0.005/0.01` 的 `seed20260918` 已完成统一 `max_nfev=120` 的 20-start：20/20 收敛，最大参数相对误差 `9.004%`，R05 留出虚功/广义反力/应力场误差 `1.299%/1.522%/3.163%`；结果为 `simulation/constitutive_virtual_experiment/results/gate6/M1_strong_seed20260918_s20_retry2.json`。随后 `seed20260919` 也完成 20/20 收敛，最大参数相对误差 `6.887%`，R05 留出虚功/广义反力/应力场误差 `1.524%/1.701%/3.217%`，结果为 `simulation/constitutive_virtual_experiment/results/gate6/M1_strong_seed20260919_s20_retry1.json`。这两项仍是 generic synthetic benchmark；M1 strong 三 seed 已齐，但不能据此使 Gate 6 通过。
- 新增 synthetic M0 profile objective：脚本 `simulation/constitutive_virtual_experiment/gate6_profile_likelihood.py` 在保留全部 692 个单元、仅每 4 帧抽样的条件下完成无噪声回收和 M0 mild profile。无噪声最佳参数 `[5.00846, 24.99195]`，mild 最佳参数 `[4.93220, 27.36930]`，后者最大参数相对误差 `9.477%`；结果和图见 `results/GATE6_PROFILE_HANDOFF.md`。该 profile 没有残差协方差校准，不能写成 95% 置信区间，Gate 6 仍未通过。
- M2 profile 预算诊断在 `max_nfev=10`、每 8 帧抽样、1 个起点下为 `0/1` 收敛，`status=0`；JSON 已显式写入 `profile_valid=false`。随后完成 `max_nfev=50` 的同分辨率单起点检查，`1/1` 收敛、`nfev=30`、`profile_valid=true`，但最佳参数 `[20.00021, 0.05000, 0.28636]` 相对真值 `[18, 0.01, 0.18]` 的最大偏差约 `400%`，且 `eps0` 命中上界；这是参数耦合/边界诊断，不是 M2 识别成功。新增 M2 strong `strain/force=0.005/0.01`、seed20260921、20-start、5 点 profile 网格结果 `M2_strong_profile_frame8_seed20260921_g5.json`：20/20 收敛、基准 `nfev=68`、最佳参数 `[43.95703, 0.0288039, 0.50000]`，`n` profile 最低点命中上界，最佳/中位/最差最大参数误差为 `157.876%/188.038%/268.476%`。这进一步证明收敛不等于参数回收，Gate 6 仍需跨噪声 profile、CI 和真实误差量级。
- 从主试样 `Job.m2inp` 与 `.dat` 首帧结构交叉审计：确认工程使用 affine、Step=3 px、Subset=15 px、LOG Euler–Almansi、Q8、像素导出和 `0.097519 mm/px`；确认 `<18>` 有 10,505 条 18 值记录。字段 7/8 仅保留位移候选，字段 9–12 改为局部仿射参数候选，字段 13/14 改为质量指标候选；主试样和全集审计表已按新命名重生成。
- 直接读取 `XY_Xy-0.1-01/formal_vfm_input.csv.gz` 的实际表头和首行，并与 MatchID 运行记录交叉核对：289/289 个正式 CSV、3,034,764 行，`frame_id/point_id/x_mm/y_mm/u_mm/v_mm/exx/eyy/exy/quality/valid/source_dat/conversion_mm_per_px` 等字段在该试样已确认；`time_s_est`、`Fx/Fy` 和 `sync_status` 仍受端点锚定/共同触发假设约束。Gate 1 从“字段 schema 未闭合”更新为“单试样字段 schema 已确认、全项目仍部分通过”。
- 只读运行真实管线审计器 `tools/audit_real_pipeline.py`：8 个 run contract 均通过代码/状态契约审查，`passed=true`、`error_count=0`。该结果不改变真实参数唯一性和跨路径预测仍未成立的判断。

## Gate 状态

| Gate | 状态 |
|---|---|
| 0 文献缺口 | 条件通过；89 个候选条目与全文/图像证据分开统计，18 个正文/图像证据中同行评审/审稿全文 15 个、公开会议全文 1 个；其中 14 条已有项目本地 PDF/MinerU 或 pypdf 绑定：P00、PA17、PA19A、PA22–PA25、PA28、BX05、BX16、BX18、BX19、VF25、DIC01；VF08 仍为官方在线全文/图像核验但本地 PDF/MinerU 待补，BX19为预印本线索，不改变窄缺口；禁止宽泛首次表述 |
| 1 已有数据足够 | 部分通过；14 个试验的 `.dat` 均可读，全场 payload 入口已确认，字段 schema 仅部分可解释，最终应变列、同步和边界契约未闭合 |
| 2 模型阶梯 | 条件通过；首篇只开放 M0–M2 |
| 3 Abaqus 真值 | Stage-A 与 synthetic M0–M2 基准通过；真实 PA12 阻塞。ODB 独立场量/反力与离散 VFM 已闭环 |
| 4 无噪声回收 | synthetic M0–M2 通过；真实 PA12 未开始。材料/几何/参数仍是通用仿真基准 |
| 5 多初值 | synthetic M0/M1/M2 在统一 `max_nfev=120` 验收预算下均为 20/20 通过；原 M2 `max_nfev=40` 触限保留为预算敏感性；真实 PA12 未开始 |
| 6 噪声稳健 | 未通过；M1 mild 与 strong 各三个 seed、M0 一个 mild seed、M2 mild 和 M2 strong 各一个 seed均完成20/20；M0 与 M2 各有保留全单元的低分辨率 profile。M2 strong 的 `n` profile 最低点命中上界，最佳/中位/最差最大参数误差为 `157.876%/188.038%/268.476%`；跨噪声 profile、profile-based CI 和真实误差量级仍缺失；空间相关噪声和一帧时移各为单起点；M2 mild seed20260920 最大参数误差 67.123%，R05 虚功/反力/应力场误差 0.732%/0.795%/1.139%；仍不代表真实 DIC/同步噪声，也不足以形成噪声曲线 |
| 7 路径信息增益 | synthetic 条件通过、真实未通过；M0/M1/M2 各路径满秩，UX+EQ 相对 UX 的 FIM `logdet` 增益为 2.007/3.060/3.247，条件数改善约 0.5%/15.4%/11.2%，但最大参数相关性仍为 0.9662/0.9869/0.9983；见 `results/GATE7_PATH_INFORMATION_HANDOFF.md` |
| 8 未见路径预测 | synthetic R05 整路径留出通过；实验验证未开始 |
| 9 真实验证 | 真实 J2 参数识别已执行并收敛，但当前试验为近等双轴载荷、单轴适用性未通过，参数不进入材料数据库；Phase 10 曲线验证仅作诊断 |
| 10 投稿完整度 | 阻塞 |
| 11 二维双轴 VFM | 真实二维虚功方程已执行；`σxx/σyy/τxy` 已输出，但 `τxy` 受边界合力近似限制，整体残差较大 |
| 12 单轴-双轴联合识别 | 真实联合 `least_squares` 已收敛；`ν` 仍在数值下界附近，独立唯一性证据未完成 |
| 13 PA12 材料数据库 | HDF5 已按最新质量门重建；5 组 `quality_passed`，0 组 `constitutive_validated`，问题实验保留排除审计 |
| 14 AI 代理模型 | 仅完成真实数据 pilot；按实验级 3/1/1 留出，正式门关闭，不宣称泛化 |

## 下一步三件事

1. 人工复核 5 组正式曲线、Phase 12 参数边界、屈服面和当前修复版图像；先处理单轴空间求积、横向应变符号/字段映射及双轴边界牵引限制。
2. 对 `XY_Y-09-0.1-02`、`XY_Y-10-1-01` 的平台/软化与当前 J2 不匹配做定向审查；不通过放宽 RMSE 阈值恢复数据库准入。
3. 暂停 Phase 14 正式训练；只有新增独立真实实验并稳定 Phase 12 标签后，才重新按实验级拆分验证代理模型。synthetic Gate 6 的 profile/噪声扩展仍是方法线，不得替代真实质量门。

补充：M1 mild `strain/force=0.001/0.005` 的 seed20260919 已完成 20/20 收敛；中位最大参数相对误差为 `3.35%`，R05 留出虚功/反力/应力场误差为 `0.750%/0.829%/0.688%`。结果文件为 `simulation/constitutive_virtual_experiment/results/gate6/M1_mild_seed20260919_s20.json`。该结果只扩充 synthetic 噪声证据，不构成真实 PA12 结论，也不足以使 Gate 6 通过。Gate 6 的完整噪声矩阵与强噪声未完成尝试见 `simulation/constitutive_virtual_experiment/results/gate6/gate6_m1_noise_matrix.json` 和 `results/GATE6_NOISE_HANDOFF.md`。

补充：M0 mild `seed20260920` 的 20-start 结果位于 `simulation/constitutive_virtual_experiment/results/gate6/M0_mild_seed20260920_s20_retry1.json`；20/20 收敛、最大参数误差 `8.206%`，R05 留出虚功/反力/应力场误差 `0.653%/0.687%/1.227%`。该结果仍是 generic synthetic benchmark，不进入 PA12 材料数据库。

补充：M2 mild `seed20260920` 在统一 `max_nfev=120` 下 20/20 收敛，但最大参数误差为 `67.123%`，R05 留出虚功/反力/应力场误差为 `0.732%/0.795%/1.139%`；该结果证明噪声下的优化器收敛不能替代参数回收，仍是 generic synthetic benchmark，不进入 PA12 材料数据库。

补充：Gate 7 synthetic 路径信息分析已完成，脚本为 `simulation/constitutive_virtual_experiment/gate7_path_information.py`，结果为 JSON/CSV/PNG 三件套；所有模型路径组合满秩，但 M2 最大参数相关性仍约 `0.9983`，真实 PA12 尚未通过。可复现方法、表格和限制见 `results/GATE7_PATH_INFORMATION_HANDOFF.md`。

## 当前最大拒稿风险

1. 没有共同时间基准却声称逐帧 VFM；
2. 只有近似曲线却声称真实参数已识别；
3. 用同一连续试样的帧拆分冒充独立验证；
4. 把合成满秩当成实验可辨识性；
5. VFM 没有相对整体曲线拟合提供可量化新信息；
6. 用文献模型参数替代当前 PA12 的工艺/批次证据；
7. 用 MJF、XZ 或损伤数据填补当前 SLS XY 数据的缺口。

## 计算力学复核与已解决项

- synthetic 实场曾出现 `u=v=0` 而应变非零，虚场也存在“虚位移为零、虚应变非零”；不能作为 admissible field。
- 合成外功直接由 `Aq_true` 构造，机器精度回收不能证明 FE–VFM 接口。
- 旧的 100×100 mm 简单板确实只有一种均匀等双轴状态，不能识别 `Q66`，也不足以分离所有正交常数；它仍不作为主基准。现有十字形 `G00_reference` ODB 已提供异质应变、四侧 FE 反力和三条路径，且离散 VFM 外内功已闭合。
- 每个噪声水平只有一次随机实现，不能支持“参数误差 ≤10%”作为论文精度门。
- 四个力通道直接平均的物理含义未确认，不能作为 VFM 边界合力。

已解决的 Stage-A 接口问题：离散虚场与 CPS4R 约化积分的一致性已修正；三条既有基准 ODB 的外部反力右端项和内部场量回收结果一致。未解决的问题仍属于真实 PA12 数据契约、模型阶梯和统计验证，而非把基准 ODB 直接当作实验结果。

## 资源与变更纪律

后续新任务统一使用 `gpt-5.6-luna`，优先 `xhigh`，以节省额度；原始数据只读；新增 Markdown、Wiki、索引和日志必须小范围提交；不把 PDF、图片、机器数据、ODB 或 MatchID 私有资产推到公开仓库。
