---
title: "Traceable Image–Load Registration in Uniaxial and Biaxial PA12 Tests"
article_type: "Experimental mechanics measurement-method working draft"
target_journal_primary: "Strain"
target_journal_alternative: "Experimental Mechanics"
status: "pre-submission draft; XY data-audit results included; VFM identification not yet eligible"
evidence_registry: "sources/source_manifest.json; sources/claims.csv"
---

# Traceable Image–Load Registration in Uniaxial and Biaxial PA12 Tests

**Authors:** [To be completed: full names, affiliations, e-mail addresses, and ORCID]

**Funding:** [To be completed; delete if not applicable]

## Abstract (current results draft; metadata and VFM conditions remain to be completed)

This paper develops and applies a file-level audit for image–load registration in uniaxial and biaxial polyamide 12 (PA12) tests processed with MatchID 2019 two-dimensional digital image correlation (2D-DIC). The audit uses a trial identifier to link X- and Y-direction uniaxial sequences, XY biaxial sequences, `Press`/`Pos` records, and MatchID files. Because no common camera–DAQ trigger or verifiable per-frame camera timestamp is available, the mapping anchors the first image to a force-side loading-onset candidate and the last image to the final `Press.T` sample; it is reported as an estimate rather than hardware synchronization. The dataset covers 10 XY image sequences and 5,309 JPEG frames. The estimated image frequency ranges from 7.98 to 375.66 Hz, while the effective force-record frequency ranges from 997.50 to 1000.00 Hz. File-count mismatches are retained rather than removed. For the most complete equibiaxial sequence with 289 JPEG frames, 289 MatchID input frames, two-axis exports, and a documented endpoint candidate, hypothetical ±1, ±2, and ±5 frame shifts were applied to its `Press.T` record. A ±1-frame scenario changes channel force by about 1 N near the stable peak but can change the post-peak drop candidate by about 1.59 kN. These are scenarios, not measured synchronization uncertainty. Because all current sequences fail the VFM entry gate, no constitutive parameters or independent-validation errors are reported. The result is a reproducible audit baseline and a list of evidence required before 2D-DIC data can enter VFM. [claim:C010] [claim:C011] [claim:C012] [claim:C013] [claim:C014] [claim:C015] [evidence:E019, E020, E021, E022, E023]

**Keywords:** PA12; uniaxial and biaxial tension; two-dimensional digital image correlation; image–load registration; timing sensitivity

> **Data-status statement:** The workspace now contains and has parsed the 10 XY image sequences under `D:\C盘迁移\Desktop\yuan\data\XY`, their `Press`/`Pos` workbooks, MatchID 2D project/frame outputs, and the pairing audit files. Material/specimen metadata, camera/calibration/DIC settings, common trigger or per-frame timestamps, a validated full-field export with units, the boundary-traction definition, and an independent validation set remain missing or unverified. The current draft can report file-level measurement-chain results, but it does not present VFM parameters as completed results. [claim:C006] [evidence:E017]

## 1 Introduction

Selective laser sintering (SLS) PA12 offers useful geometric freedom for polymer additive manufacturing, but its mechanical response depends on build orientation, part thickness, powder and processing history, and interlayer structure. Published work shows that the tensile properties of SLS PA12 can vary with build orientation and part thickness, with orientation-related differences often becoming more apparent in the plastic regime.[E007,E016] [claim:C001] [evidence:E007, E016] Consequently, a uniaxial property set obtained from one grade, batch, thickness, and build direction cannot be treated without qualification as a multiaxial constitutive description for all PA12 parts.

Biaxial tension provides a way to impose controlled loading in two orthogonal directions and to evaluate yielding, localization, failure, and constitutive models under combined stress states. The performance of a cruciform specimen, however, depends on its profile, central thickness reduction, slots, fillets, arms, and gripping boundary conditions. Recent cruciform-specimen studies have treated deformation uniformity, high usable strain, and constitutive characterization as joint design objectives and have used finite element analysis and DIC for validation.[E006,E013,E014] [claim:C005] [evidence:E006, E013, E014] Thus, the existence of a biaxial machine does not by itself establish that the central gauge region provides a valid material measurement.

Full-field DIC adds displacement and strain information to the global force–displacement response. It can reveal localization, test whether deformation remains in the intended gauge region, and show whether a constitutive model explains spatial response as well as global response. Biaxial experiments on polymers have demonstrated the value of full-field deformation measurements for examining localization and constitutive predictions.[E005] Nevertheless, 2D-DIC is directly interpretable only when the planar-surface assumption is appropriate and out-of-plane motion is sufficiently controlled. Out-of-plane translation or rotation, lens distortion, speckle quality, and analysis settings can propagate into strain fields and subsequent parameter identification.[E003,E008,E009,E010] [claim:C003] [evidence:E003, E008]

The VFM combines full-field kinematics with boundary loading through the principle of virtual work. It can use multiple virtual fields to constrain constitutive parameters from a heterogeneous test without repeatedly solving a complete finite element forward problem for every parameter trial.[E001,E002,E011] [claim:C002] [evidence:E001, E002, E011] The identified parameters, however, are not determined by an optimizer alone. The assumed distribution of boundary traction, the valid field region, missing edge data, synchronization, DIC noise, independence of the virtual fields, and separation of fitting and validation data can all affect the result. Biaxial VFM work has explicitly examined the effects of DIC noise and missing deformation data near specimen edges.[E004] A curve that is fitted to the same frames used for identification is not evidence of cross-path predictive validity.

The literature separately provides evidence on process-related PA12 anisotropy, cruciform design, DIC metrology, and VFM. The immediate problem in the present project is first to establish file-level traceability and the consequences of an unverified image–load time origin. The study therefore asks:

1. Can the available PA12 uniaxial and biaxial images, force/displacement workbooks, and MatchID files be linked by trial identifier into a reproducible frame–load data chain?
2. Without a common trigger or per-frame timestamp, how much can a hypothetical endpoint-mapping shift change peak and post-peak load events?
3. Do the current 2D-DIC exports satisfy the field, unit, boundary, and independent-validation conditions required for VFM?

The contributions are limited to four methodological elements:

1. a unified file-level pairing of 10 X/Y-uniaxial and XY-biaxial sequences, 5,309 JPEG frames, force workbooks, and MatchID-associated files;
2. a reproducible mapping rule linking force-side loading onset, the last force sample, image frame numbers, and four-channel loads while explicitly distinguishing it from hardware synchronization;
3. a quantitative sensitivity analysis of hypothetical frame-registration shifts on stable-peak and post-peak event loads in the most complete biaxial sequence;
4. an explicit VFM entry gate that separates completed file-level results from constitutive parameters and independent validation that are not yet reportable.

Image-sequence count is not treated as independent specimen count, endpoint time mapping is not treated as synchronization truth, and no PA12 material constants are prespecified. Once material/specimen metadata, camera/calibration records, a common time base, full-field exports, and independent specimens are documented, the present results can be extended into a 2D-DIC–VFM identification study.

## 2 Theoretical basis and study design

### 2.1 Cruciform-specimen objectives

Let the candidate geometry be described by

\[
g=(h_c,N_s,l_s,r_f,s_s,w_a,\ldots),
\]

where \(h_c\) is central thickness, \(N_s\) is the number of slots per arm, \(l_s\) is slot length, \(r_f\) is fillet radius, \(s_s\) is slot spacing, and \(w_a\) is arm width. Each finite-element candidate should report:

1. the uniformity of principal strains and stresses within the gauge region;
2. the ratio of localization in the gauge region to that at arm roots, fillets, and slot ends;
3. deformation modes under X-direction, Y-direction, and equibiaxial loading;
4. whether the dominant failure location falls inside the predefined measurement region;
5. mesh, boundary, material-model, and parameter provenance.

The local learning baseline reports one candidate set of geometric values, but those values are not adopted as project facts. The final specimen must also satisfy the verified PA12 thickness, grip geometry, manufacturing resolution, actuator range, and safety limits.

### 2.2 2D-DIC measurement chain

2D-DIC takes a reference image and deformed images as input and returns in-plane fields \(u(x,y,t)\) and \(v(x,y,t)\), from which strains may be calculated. In this study, DIC fields are treated as measurements with uncertainty rather than as error-free truth. Each processed frame should retain at least:

```text
frame_id, t_image, x, y, u, v,
exx, eyy, exy (if exported by MatchID), correlation_quality,
valid_mask, roi_id, dic_run_id
```

The hardware and analysis metadata should include camera and lens model, image size, field of view, image scale, frame rate, exposure, illumination, speckle feature size, planar calibration method, MatchID version, subset, step, shape function, interpolation, matching criterion, strain window, and filtering. This reporting structure follows the reproducibility emphasis of the iDICs guide and the DIC Challenge.[E009,E010,E018] [claim:C009] [evidence:E009, E010, E018]

![Figure 1. Traceable uniaxial and biaxial measurement chain](figures/Fig1_traceable_measurement_chain.png)

**Figure 1.** Traceable uniaxial and biaxial measurement chain. This is a methodological workflow schematic and contains no project-specific experimental values. For submission, it should be supplied as a separate high-resolution figure and its labels should be checked against the actual equipment, channels, and software.

Before mechanical loading, the setup should be assessed using static-image noise, in-plane rigid-body motion, and out-of-plane risk tests. If rigid-body images produce unexplained strain, or if out-of-plane motion changes the image scale materially, that dataset should not be passed directly to VFM. The camera arrangement, calibration, speckle, or measurement dimension must be corrected first.

### 2.3 Frame-to-machine time mapping

For every trigger event, the experiment should record image-frame number \(k_i\) and machine time \(t_{m,i}\). If the trigger evidence supports a linear mapping over the relevant interval, the relation may be written as

\[
t_m(k)=a+bk,
\]

with a frame-specific mapping residual

\[
e_i=t_{m,i}^{\mathrm{mapped}}-t_{m,i}^{\mathrm{observed}}.
\]

If the trigger records reveal nonlinear clock drift, a single affine mapping must not be retained by convenience. The mapping should be redefined while preserving original timestamps, interpolation intervals, dropped frames, and repeated triggers. Equal nominal camera and data-acquisition frequencies do not establish synchronization.

The present project has no common camera–DAQ trigger identifier or verifiable per-frame camera timestamp. The current file-level audit therefore uses an endpoint estimate rather than a synchronization truth. The first 50 `Press` samples define a baseline; a force-side onset candidate is the first run of three samples exceeding (max(10\,\mathrm{MAD},5\,\mathrm N)). The first image is anchored to that candidate and the last image to the final `Press.T` sample; intermediate image times receive linearly interpolated four-channel force/displacement values. If no independent onset is detected, as in Y-11, the sequence retains a preloaded-start status. The resulting field is named `t_image_s_est`, and it does not produce an independently validated synchronization residual.

### 2.4 VFM identification

Under a verified quasi-static, plane-stress assumption, the virtual-work residual for time \(t_k\) and admissible virtual field \(\mathbf u^*\) is defined as

\[
r_k(\boldsymbol\theta)=
\int_{V}\boldsymbol\sigma(\boldsymbol\varepsilon(\mathbf x,t_k);\boldsymbol\theta):
\boldsymbol\varepsilon^*(\mathbf x)\,\mathrm dV
-\int_{\partial V}\bar{\mathbf t}\cdot\mathbf u^*\,\mathrm dA.
\]

Here \(\boldsymbol\theta\) denotes the unknown constitutive parameters and \(\bar{\mathbf t}\) is obtained from the four-channel boundary forces and the defined loaded regions. If only resultant forces are measured, the conversion from resultant force to boundary traction must be stated with its loaded width, thickness, and validity assumptions. A resultant must not be silently treated as a local traction at every boundary point.[E001,E002,E011] [claim:C002] [evidence:E001, E002, E011]

The first stage uses an L0 linear-elastic baseline to audit units, coordinates, signs, thickness, boundary terms, virtual fields, and integration. Finite-strain plastic, viscoelastic, or orthotropic models are introduced only if the observed loading history provides evidence for yielding, hysteresis, rate dependence, or build-direction anisotropy. VFM's ability to solve a nonlinear optimization problem is not evidence that a complex material model is justified.

The weighted fitting objective may be written as

\[
\hat{\boldsymbol\theta}=
\arg\min_{\boldsymbol\theta}\sum_{k\in\mathcal F}\sum_{q\in\mathcal Q}
w_{kq}r_{kq}^{2}(\boldsymbol\theta),
\]

where \(\mathcal F\) is the predeclared fitting-frame set, \(\mathcal Q\) is the virtual-field set, and the weights are derived from measurement uncertainty or a declared scaling rule. The fitting configuration must retain the initial values, parameter bounds, optimizer, fitting frames, virtual fields, ROI, weights, and run version.

### 2.5 Validation and sensitivity

Identification and validation are separated before analysis. Validation may use a loading path not used for fitting, independent specimens, or a predeclared unloading/hold segment when supported by the model. Parameters must not be retuned on the validation set.

The minimum comparison set is:

- baseline synchronization and controlled early/late time mappings;
- complete ROI and edge-masked ROI;
- predeclared combinations of subset, step, and strain-window settings;
- a global force–displacement baseline;
- full-field DIC-based VFM;
- an independent loading path or independent specimens.

The outputs should include global force/displacement prediction error, spatial field residuals, virtual-work residuals, parameter intervals, and between-specimen variation. Image frames from one specimen are a time series, not independent replicates. Missing edge data and DIC noise must be treated as analysis factors rather than hidden by a change of optimizer.[E004,E011] [claim:C004] [evidence:E004, E011]

## 3 Materials and experimental procedure

> Bracketed fields must be completed from original records. Missing records must remain marked as missing; literature values and equipment posters must not be used as substitutes.

### 3.1 Material and specimen

Material grade: `[to be completed]`; manufacturing route: `[to be completed: SLS or other]`; machine: `[to be completed]`; powder/material batch: `[to be completed]`; moisture condition and drying: `[to be completed]`; build/loading coordinate definition: `[to be completed]`; post-processing: `[to be completed]`.

Cruciform CAD version: `[to be completed]`; central thickness: `[to be completed]`; arm width and length: `[to be completed]`; slot count/length/spacing: `[to be completed]`; fillet radius: `[to be completed]`; measured dimensions and tolerances: `[to be completed]`. The selected geometry is screened by finite-element model version `[to be completed]` with loading boundary `[to be completed]`.

If XY and XZ are compared, the manuscript must show the build coordinates, tensile directions, and layer relationship rather than using unexplained abbreviations. If the material is not SLS, all inferences about layers and build orientation must be removed.

### 3.2 Biaxial loading system

Equipment manufacturer/model: `[to be completed]`; number of loading channels: `[to be completed]`; control mode: `[to be completed: force/displacement/hybrid]`; force-cell ranges and calibration: `[to be completed]`; travel and limits: `[to be completed]`; controller sampling rate: `[to be completed]`; actual test rate: `[to be completed]`; trigger signal: `[to be completed]`.

Before specimen loading, perform unloaded grip motion, channel zeroing, and force-balance checks. The tested paths are `[to be completed: X uniaxial, Y uniaxial, equibiaxial, and any other ratios]`. Control commands, stopping criteria, force/displacement signs, and anomaly rules are retained in the run manifest.

### 3.3 Speckle, camera, and MatchID 2019

Speckle preparation: `[to be completed: base coat, dots, feature size]`; camera: `[to be completed]`; lens: `[to be completed]`; image size: `[to be completed]`; field of view: `[to be completed]`; image scale: `[to be completed]`; frame rate: `[to be completed]`; exposure: `[to be completed]`; illumination: `[to be completed]`; synchronization: `[to be completed]`.

The project and frame-result headers identify MatchID 2D-Version 19.2.0.0 (the MatchID 2019 route). The subset, step, shape function, matching criterion, interpolation, strain window, filtering, camera model, and calibration record still require item-by-item verification from the project settings. Static-noise and rigid-body test results are stored at `[to be completed]`.

### 3.4 Data processing

Raw data are not modified. Raw images, machine data, MatchID project files, exported fields, synchronization records, analysis configurations, and result figures are linked by specimen ID. Any change to ROI, mask, DIC settings, time mapping, or constitutive model creates a new `run_manifest` while preserving input/output provenance.

The current file-level processing reads 10 XY image sequences and their `Press`/`Pos` workbooks under `D:\C盘迁移\Desktop\yuan\data\XY`, producing `results/审计/xy_photo_force_sync.csv` and `results/01_VFM照片力对应.csv`. Each JPEG receives an endpoint-mapped time and interpolated load, but without a common trigger or camera timestamp it is named `t_image_s_est`. The existing `Serie;X;Y` exports and per-frame `.dat` results are retained; until their complete fields, units, quality metrics, and valid masks are confirmed, they are not passed directly to VFM. Coordinate conversion, thickness, and loaded boundary regions remain to be documented. [claim:C012] [evidence:E020, E021]

## 4 Results: file-level audit of the XY measurement chain

This section is generated from the original XY images, `Press`/`Pos` workbooks, MatchID files, and the audit scripts. Numerical values describe file and record facts. Endpoint image times and event frames are estimates or candidates, not common-trigger validation results.

### 4.1 Equipment, calibration, and synchronization

**Evidence for the file-level counts and coverage statements:** [claim:C010] [claim:C011] [claim:C012] [claim:C014] [claim:C015] [evidence:E019, E020, E021, E022]

The file-level results are as follows: the 10 XY sequences contain 5,309 JPEG frames, and each sequence has a corresponding workbook with readable `Press` and `Pos` sheets. The nominal force-record rate is 1,000 Hz; the effective rate calculated from the first and last `Press.T` samples is 997.50–1000.00 Hz. The endpoint-mapped image-frequency estimate is 7.98–375.66 Hz. MatchID input-frame counts total 5,025, whereas unique-frame counts in the DIC CSV exports total 5,295; neither equals the JPEG total. `XY_XY-0.1-02` is the clearest coverage conflict, with only 10 MatchID input frames but 259 unique DIC-CSV frame identifiers, so its frequency and VFM coverage are blocked. No common camera–DAQ trigger identifier or verifiable per-frame camera timestamp is available, and endpoint-map residuals therefore cannot be interpreted as synchronization accuracy.

**Table 1. Equipment, acquisition, and specimen metadata (to be completed).**

| Category | Field | Value/status | Evidence |
|---|---|---|---|
| Equipment | Manufacturer and model | To be completed | Manual/nameplate |
| Load | Force-record nominal/effective rate | 1,000 Hz; 997.50–1000.00 Hz | `Press.T` |
| Acquisition | XY image sequences/JPEG frames | 10 sequences; 5,309 frames | XY image directories |
| Acquisition | Endpoint-mapped image-frequency estimate | 7.98–375.66 Hz | `xy_frequency_summary.csv` |
| Camera | Model, image size, exposure, hardware timestamp | To be completed/not found | Camera settings/trigger record |
| DIC | MatchID version | 2D-Version 19.2.0.0 | Per-frame `.dat` header |
| DIC | Input-frame coverage | 5,025 MatchID input frames; 5,295 unique DIC-CSV frame identifiers | XY project/exports |
| Material | Grade, batch, manufacturing route | PA12; remaining fields to be completed | Material/print record |
| Specimen | Geometry version, thickness, tolerance, independent n | To be completed | CAD/measurement/specimen log |
| Synchronization | Common trigger/per-frame timestamp and residual | Not found; hardware synchronization not validated | File inventory |

### 4.2 Gauge-zone validity

The current files do not provide a verifiable CAD revision, specimen thickness/tolerance, or finite-element result. Central-zone uniformity, arm-root localization, and failure location therefore cannot be reported quantitatively. Existing image-endpoint notes are used only to screen event candidates and do not substitute for gauge-zone validation. After CAD, measured geometry, and field exports are documented, the predefined gauge region can be evaluated with the planned FE–DIC comparison.

### 4.3 DIC measurement quality

**Evidence for the DIC-file completeness statement:** [claim:C016] [evidence:E019]

The directory confirms MatchID 2D projects, 13 associated project/result files, and per-frame `.dat` outputs. A unified, directly verifiable full-field table containing `x,y,u,v,exx,eyy,exy`, units, correlation quality, and a valid mask has not yet been produced. The current `Serie;X;Y` tables establish that point/line exports exist, but they cannot alone support a full-field strain-quality report. Static noise, rigid-body strain, invalid-point fraction, and out-of-plane error are therefore not reported, and every sequence remains outside the VFM entry gate.

### 4.4 Global response and field evolution

**Evidence for the sequence-level force-history statement:** [claim:C010] [claim:C014] [evidence:E019, E020, E021, E022]

The current results support sequence-level absolute channel-force histories and file coverage, not material stress–strain or independent-specimen statistics. Figure 2 shows the four-channel force records projected onto image frames by the endpoint map. For uniaxial sequences, the active-direction mean absolute force is shown; for biaxial sequences, X and Y channel means are shown separately. The marker is the force-side peak candidate projected to the image axis, not a hardware-synchronized peak.

![Figure 2. Frame-indexed force-history audit for the XY sequences](../results/analysis/Fig2_force_history_audit.png)

**Figure 2.** Frame-indexed force-history audit for the XY sequences. The horizontal coordinate is the saved JPEG frame number. Loads are interpolated through the endpoint map and are not hardware-trigger validated. The two biaxial curves are the mean absolute channel forces in X and Y.

**Table 2. Sequence-level coverage and event candidates**

| Sequence | Direction | Rate (mm/s) | JPEG frames | Force samples | Image-frequency estimate (Hz) | MatchID input frames | Peak candidate frame | Image-end candidate |
|---|---|---:|---:|---:|---:|---:|---:|---|
| X-05-0.1-01 | X | 0.2 | 165 | 14,735 | 11.69 | 130 | 141 | Review required |
| X-06-1.0-01 | X | 2 | 133 | 2,789 | 49.16 | 133 | 58 | 132 |
| X-07-10-01 | X | 20 | 81 | 402 | 227.92 | 81 | 28 | Review required |
| Xy-0.1-01 | XY | 0.2 | 289 | 36,244 | 7.98 | 289 | 223 | 288 |
| XY-0.1-02 | XY | 0.2 | 259 | 27,980 | 9.30 | 10 | 235 | 258 (DIC input incomplete) |
| Xy-03-10-01 | XY | 20 | 21 | 511 | 43.48 | 21 | 7 | 20 |
| Xy-04-1-01 | XY | 2 | 267 | 4,570 | 58.81 | 267 | 142 | 250/266 (review) |
| Y-09-0.1-02 | Y | 0.2 | 1,825 | 179,260 | 10.19 | 1,825 | 1,112 | 1,824 |
| Y-10-1-01 | Y | 2 | 1,558 | 15,328 | 102.08 | 1,558 | 888 | 1,557 (event type review) |
| Y-11-10-01 | Y | 20 | 711 | 1,889 | 375.66 | 711 | 0 (preloaded) | 710 |

The ten sequences are image/file sequences, not independent specimens. Specimen identifiers, geometry, material batch, and replicate relationships must still be confirmed from the laboratory record. Figure 3 projects the onset, peak, post-peak drop, and image-end candidates onto the file frame axis.

![Figure 3. Event-candidate projection](../results/analysis/Fig4_event_frame_audit.png)

**Figure 3.** Event-candidate projection. Event frames are obtained from the endpoint map or image-side endpoint notes and require review; Y-11 begins under preload and has no detected zero-load onset.

Figure 4 provides the image-rate and MatchID frame-coverage audit.

![Figure 4. Image sampling and DIC frame-consistency audit](../results/analysis/Fig3_frequency_frame_audit.png)

**Figure 4.** Image sampling and DIC frame-consistency audit. The left panel shows endpoint-estimated image frequency as circles and readable nominal camera settings as crosses; the right panel compares saved JPEG frames with MatchID input frames. These are sequence-level file counts, not camera timestamps or independent specimen counts.

### 4.5 Baseline VFM identification

No VFM baseline identification suitable for a paper conclusion was run. The reason is not an optimizer or computational limitation: the ten sequences lack a verified common time base, and a complete field export with units, valid mask, specimen thickness, loaded boundary regions, and a resultant-to-traction definition has not been established. Constitutive parameters, virtual-work residuals, and independent prediction errors are therefore not filled.

**Table 3. VFM identification configuration and results (to be completed).**

| Item | Fitting setting | Validation setting | Result |
|---|---|---|---|
| Constitutive model | Not run | Not run | Not reported |
| Fitting frames/paths | Not defined | Not defined | Not reported |
| ROI and mask | Full-field export not verified | Not defined | Not eligible |
| Virtual-field count/form | Not defined | Not defined | Not reported |
| Parameter estimate/interval | Not run | No retuning | Not reported |
| Virtual-work residual | Not run | Not run | Not reported |

### 4.6 Synchronization, ROI, and DIC sensitivity

**Evidence for the timing-sensitivity result:** [claim:C013] [evidence:E023]

Before VFM entry, the current paper evaluates the sensitivity of image–load registration itself. `XY_Xy-0.1-01` was selected because it has 289 JPEG frames, 289 MatchID input frames, X/Y exports, and a clearly documented visual endpoint candidate. Hypothetical ±1, ±2, and ±5 frame registration shifts were applied to the original `Press.T` record, and channel-force differences were evaluated over the sequence and at the two candidate event frames.

**Table 4. Hypothetical timing-perturbation results for XY_Xy-0.1-01 (not measured synchronization uncertainty)**

| Frame-index shift | Maximum channel-force difference (N) | Mean channel-force difference (N) | Difference at force-peak candidate (N) | Difference at post-peak-drop candidate (N) |
|---:|---:|---:|---:|---:|
| -5 | 1,595 | 55.1 | 5 | 1,591 |
| -2 | 1,594 | 22.1 | 2 | 1,592.5 |
| -1 | 1,592.5 | 11.1 | 1.5 | 1,592.5 |
| 0 | 0 | 0 | 0 | 0 |
| +1 | 1,592.5 | 11.1 | 0.5 | 1.5 |
| +2 | 1,594 | 22.0 | 0.5 | 2 |
| +5 | 1,595 | 54.5 | 1,594 | 1.5 |

![Figure 5. Sensitivity of event load to image–load timing](../results/analysis/Fig5_timing_sensitivity_Xy-0.1-01.png)

**Figure 5.** Sensitivity of event load to image–load timing. The left panel shows the reference endpoint map and ±1-frame scenarios using the norm of the two axis-wise mean absolute channel forces; the right panel summarizes the sequence maximum, peak-candidate, and post-peak-drop differences. These are analytical scenarios, not a synchronization confidence interval; the large difference at the drop candidate arises from the rapid load collapse.

### 4.7 Independent-path validation

No independently fitted parameter set, independent loading-path split, or confirmed independent specimen identifier is available in the current package. This section therefore makes no claim of completed validation. Global response, central fields, and spatial residuals can be compared only after the time base, full-field export, specimen independence, and boundary conditions are documented.

## 5 Discussion

### 5.1 Separating timing from event-load interpretation

The file-level audit shows an effective force-record rate close to 1,000 Hz, while the endpoint-estimated image rate varies from 7.98 to 375.66 Hz. Similar nominal rates do not establish a common time origin or frame-by-frame correspondence. In `XY_Xy-0.1-01`, a ±1-frame scenario can pair a high-load frame with a low-load frame across the post-peak collapse, producing about 1.59 kN of channel-force difference. Image event frames should therefore not be fixed from the last file or visual curve overlap alone.

### 5.2 File completeness and 2D-DIC/VFM entry

The MatchID files establish that a 2D-DIC processing chain exists, but MatchID input counts, unique DIC-CSV frame identifiers, and JPEG counts are not always equal. `XY_XY-0.1-02` is the clearest coverage conflict. Running VFM before resolving such temporal and spatial coverage would mix missing data with material parameters. The present paper retains the conflict and sets `vfm_eligible=false`; this is a traceability limitation, not a conclusion about PA12 constitutive behavior.

### 5.3 Relation to prior work

Compare the present results with literature by object, manufacturing route, thickness, loading path, and DIC settings. Published orientation/thickness trends for SLS PA12 can motivate interpretations, but cannot replace project-specific batch data.[E007,E016] Cruciform and VFM papers provide methodological comparisons, but differences in polymer, boundary conditions, and constitutive model must be stated.[E004,E005,E006]

### 5.4 Limitations

1. 2D-DIC relies on a planar-surface assumption. Without stereo images, out-of-plane effects can be bounded by risk tests and sensitivity analysis but cannot be claimed to have been removed by 3D measurement.
2. If only four resultant forces are available, the VFM traction distribution is based on an explicit conversion assumption that must be supported by grip and finite-element evidence.
3. PA12 manufacturing route, powder/material batch, moisture, thickness, and post-processing limit generalization.
4. Without an independent specimen or loading path, the constitutive model is not validated.
5. The XY file-level audit is complete, but material/specimen metadata, camera and calibration settings, a common trigger/per-frame timestamp, a validated full-field export, the boundary-traction assumption, and independent validation remain incomplete; the current draft is therefore not a VFM-parameter submission.

## 6 Conclusions (currently supportable version)

This study establishes and recomputes a file-level image–load timing audit for biaxial PA12 testing. The current XY results cover 10 image sequences and 5,309 JPEG frames, with an effective force-record frequency of 997.50–1000.00 Hz, an endpoint-estimated image frequency of 7.98–375.66 Hz, and explicit image/MatchID coverage and event-candidate tables. In the most complete sequence, `XY_Xy-0.1-01`, hypothetical timing shifts show approximately 1 N-scale channel-force differences near the stable peak but approximately 1.59 kN at the post-peak-drop candidate for a ±1-frame scenario.

These shifts are analytical scenarios, not synchronization precision or confidence intervals. Because no common camera–DAQ trigger identifier or verifiable per-frame camera timestamp is available, and because a validated full-field export, boundary-traction definition, and independent specimen validation are not yet complete, every current sequence remains outside the VFM entry gate. No unsupported PA12 strength, modulus, or constitutive parameters are reported. Once the missing fields are documented, the present facts table and scripts provide the audit baseline for a 2D-DIC–VFM identification study.

## Data availability statement (to be completed)

Current status: `Data availability statement pending.` Before submission, the authors must decide—based on rights, laboratory policy, raw images, machine data, MatchID files, code, and material restrictions—whether the data are publicly archived, available on reasonable request, or not shareable, and provide a persistent identifier where applicable.

## Ethics, competing interests, funding, and AI-use statements (to be completed)

- Confidentiality review: `[to be completed; mandatory institutional review if submitting to Acta Armamentarii]`.
- Competing interests: `[to be completed and confirmed by all authors]`.
- Funding: `[to be completed]`.
- Author contributions: `[to be completed using CRediT and confirmed by all authors]`.
- AI use: `[to be completed according to the target journal's current policy; authors remain responsible for all scientific content]`.

## References

The reference records and DOI/title validation are stored in `sources/references.json` and `sources/reference_validation.json`, respectively. The following working-draft reference list is included for completeness. Before submission, the authors must apply the target journal's reference style and open each cited source to confirm claim-level support. The `[E###]` markers are evidence IDs for this working draft and must be converted to the target journal's citation style in the clean submission file while retaining the claim registry.

1. E001. Grédiac M, Pierron F, Avril S, Toussaint E. The Virtual Fields Method for Extracting Constitutive Parameters From Full-Field Measurements: a Review. *Strain*. 2006. doi:10.1111/j.1475-1305.2006.tb01504.x.
2. E002. Avril S, Pierron F. General framework for the identification of constitutive parameters from full-field measurements in linear elasticity. *International Journal of Solids and Structures*. 2007. doi:10.1016/j.ijsolstr.2006.12.018.
3. E003. Zhang Z, Pan B, Grédiac M, Song W. Accuracy-enhanced constitutive parameter identification using virtual fields method and special stereo-digital image correlation. *Optics and Lasers in Engineering*. 2018. doi:10.1016/j.optlaseng.2017.11.016.
4. E004. Jiang M, Wang Z, Freed AD, Moreno MR, Erel V, Dubrowski A. Extracting material parameters of silicone elastomers under biaxial tensile tests using virtual fields method and investigating the effect of missing deformation data close to specimen edges on parameter identification. *Mechanics of Advanced Materials and Structures*. 2021. doi:10.1080/15376494.2021.1979138.
5. E005. Engqvist J, Wallin M, Ristinmaa M, Hall SA. Modelling and experiments of glassy polymers using biaxial loading and digital image correlation. *International Journal of Solids and Structures*. 2016. doi:10.1016/j.ijsolstr.2016.10.013.
6. E006. Vitucci G. Biaxial Extension of Cruciform Specimens: Embedding Equilibrium Into Design and Constitutive Characterization. *Experimental Mechanics*. 2024. doi:10.1007/s11340-024-01052-2.
7. E007. Slager JJ, Earp BC, Ibrahim AM. Influence of Build Orientation and Part Thickness on Tensile Properties of Polyamide 12 Parts Manufactured by Selective Laser Sintering. *Polymers*. 2024. doi:10.3390/polym16162241.
8. E008. Sutton MA, Yan JH, Tiwari V, Schreier HW, Orteu JJ. The effect of out-of-plane motion on 2D and 3D digital image correlation measurements. *Optics and Lasers in Engineering*. 2008. doi:10.1016/j.optlaseng.2008.05.005.
9. E009. Reu PL, Toussaint E, Jones E, et al. DIC Challenge: Developing Images and Guidelines for Evaluating Accuracy and Resolution of 2D Analyses. *Experimental Mechanics*. 2017. doi:10.1007/s11340-017-0349-0.
10. E010. International Digital Image Correlation Society, Bigger R, Blaysat B, et al. A Good Practices Guide for Digital Image Correlation. International Digital Image Correlation Society. 2018. doi:10.32720/idics/gpg.ed1.
11. E011. Wang P, Pierron F, Thomsen OT. Identification of Material Parameters of PVC Foams using Digital Image Correlation and the Virtual Fields Method. *Experimental Mechanics*. 2012. doi:10.1007/s11340-012-9703-4.
12. E012. Guélon T, Toussaint E, Le Cam JB, Promma N, Grédiac M. A new characterisation method for rubber. *Polymer Testing*. 2009. doi:10.1016/j.polymertesting.2009.06.001.
13. E013. Yang X, Wu ZR, Yang YR, Pan Y, Wang SQ, Lei H. Optimization Design of Cruciform Specimens for Biaxial Testing Based on Genetic Algorithm. *Journal of Materials Engineering and Performance*. 2022. doi:10.1007/s11665-022-07258-6.
14. E014. Hartmann S, Gilbert RR, Sguazzo C. Basic studies in biaxial tensile tests. *GAMM-Mitteilungen*. 2018. doi:10.1002/gamm.201800004.
15. E015. Arrington A, Westra A, Jannotti P, Reu P, Lamberson L. Review of High-Speed Digital Image Correlation: Advancements and Good Practices. *Strain*. 2025. doi:10.1111/str.70018.
16. E016. Slager JJ, Green JT, Levine SD, Gonzalez RV. The Influence of Print Orientation and Discontinuous Carbon Fiber Content on the Tensile Properties of Selective Laser-Sintered Polyamide 12. *Polymers*. 2025. doi:10.3390/polym17152028.
17. E018. International Digital Image Correlation Society, Jones EMC, Iadicola MA, eds. A Good Practices Guide for Digital Image Correlation, Edition 2. International Digital Image Correlation Society. 2025. doi:10.32720/idics/gpg.ed2.
