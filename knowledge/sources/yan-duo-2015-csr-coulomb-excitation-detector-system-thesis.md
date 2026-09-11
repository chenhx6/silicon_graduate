---
type: source
title: "闫铎 2015 博士论文：CSR 外靶中高能库仑激发探测器系统"
aliases: [闫铎CSR库仑激发论文, Yan Duo CSR Coulomb-excitation detector thesis, CsI telescope thesis]
created: 2026-09-11
updated: 2026-09-11
status: ai-draft
review_status: unreviewed
source_type: thesis-method
reading_depth: deep-read
title_original: "在 CSR 外靶终端开展中高能库仑激发反应实验相关探测器系统的研究"
authors: [闫铎]
advisor: [孙志宇, 徐瑚珊]
journal: "中国科学院大学/中国科学院近代物理研究所博士学位论文"
year: 2015
pages: 120
doi:
arxiv:
language: zh/en
canonical_source: "闫铎. 在 CSR 外靶终端开展中高能库仑激发反应实验相关探测器系统的研究[D]. 中国科学院大学, 2015."
zotero_item_key:
citation_key:
zotero_uri:
library_file: "raw/papers/degree dissertation/闫铎 - 在CSR 外靶终端开展中高能库仑激发反应.pdf"
raw_file: "raw/papers/degree dissertation/闫铎 - 在CSR 外靶终端开展中高能库仑激发反应.pdf"
raw_sha256: "9a7ba567b498edfa68b89a545698bf1c32f89a5c58d9cb3682448e0257f2a20e"
nuclei: []
reactions: []
experiments: []
models: [geant4]
observables: [gamma-ray-detection-efficiency, full-energy-peak-efficiency, particle-identification, energy-resolution, energy-calibration]
methods: [gamma-ball, csi-tl-telescope, delta-e-e-range, monte-carlo-simulation, beam-test]
tags: [degree-dissertation, detector-method, hirfl-csr, coulomb-excitation, gamma-ball, csi-tl, particle-identification]
---

# 闫铎 2015：CSR 外靶中高能库仑激发探测器系统

## Bibliographic Record

闫铎，*在 CSR 外靶终端开展中高能库仑激发反应实验相关探测器系统的研究*，中国科学院大学/中国科学院近代物理研究所博士学位论文，2015，PDF 120 页。原始文件 SHA-256 为 `9a7ba567b498edfa68b89a545698bf1c32f89a5c58d9cb3682448e0257f2a20e`。本论文与 [[yue-ke-2010-hirfl-csr-gamma-ball-csi-thesis]] 共享 CSR 外靶 Gamma Ball 装置谱系。

## Scope and Reading Depth

- Completed `reading_depth`: `deep-read`。
- Covered scope: 中英文题名页、摘要和目录（PDF pp.1–8）；CSR 外靶、中高能库仑激发物理目标和探测需求（pp.9–34）；靶前/靶后粒子鉴别系统和 Gamma Ball 结构（pp.21–49）；Gamma Ball 能量刻度、`60Co` 级联符合效率测量和 GEANT4 模拟（pp.35–49，视觉核对 pp.44–48）；七层 CsI(Tl) 望远镜设计、Range–E/ΔE–E 模拟、束流测试和能量刻度（pp.50–90）；总结（pp.91–100）。
- Not covered: 原始 60Co 计数谱、GEANT4 输入、束流测试原始事件和引用论文逐篇复核。
- Coverage caveats: Gamma Ball 实测/模拟差异接近因子 2，且已定位到 printed pp.41、47–49 的定义、计算和总结页；原因仍未闭合。PID 和能量分辨数字依赖晶体、束流和刻度条件，不得外推为通用探测器性能。

## Paper Question and Scientific Motivation

论文为 CSR 外靶终端的中高能库仑激发实验研究探测 γ 和带电反应产物，重点解决 Gamma Ball 效率输入和靶后粒子鉴别/散射角信息缺失问题（摘要；PDF pp.9–34）。

## Method and Design Logic

Gamma Ball 在 Add-back 模式下用 `60Co` 级联 γ 与 LaBr3(Ce) trigger 做效率测量，并以 GEANT4 模拟同一实验方案；printed p.41（Eq.4.7–4.8）定义全能峰效率，printed p.47（Eq.4.11）以 LaBr₃ `1332.5 keV` 窗内事件和 Gamma Ball 关联 `1173.2 keV` 事件的比值计算，实验值是在一期覆盖约全空间 6% 内报告的 `38.9%`，printed p.48 在同窗和归一化模拟下给 `66.0%`，printed p.49 明确称差异原因仍在探索（physical PDF pp.53、59–61）。靶后系统由七层不同厚度的 CsI(Tl) 晶体组成，每层晶体四角用 PMT 读出；通过 `ΔE–E–Range` 同时利用能损、剩余能量和射程信息，并比较 `ΔE–E` 与 `E–Range` 的同位素分辨能力（PDF pp.50–90）。

## Key Evidence and Reasoning Chain

1. `60Co` coincidence measurement and GEANT4 → Gamma Ball efficiency benchmark (PDF pp.40–49).
2. Seven-layer CsI(Tl) telescope and Monte Carlo → compare `ΔE–E` with `E–Range` isotope separation (PDF pp.50–71).
3. Beam test → measure single-layer resolution and oxygen-isotope PID improvement from range information (PDF pp.72–90).
4. Calibration comparison → test whether deposited-energy calibration agrees with experiment within stated error (PDF pp.79–90).

## Summary

The thesis reports, for the first-phase Gamma Ball coverage (about 6% of 4π) and `1173.2 keV` γ rays, `38.9%` experimental full-energy-peak efficiency in Add-back mode after the small-peak correction (physical PDF p.59 / printed p.47, Eq.4.11), versus `66.0%` from GEANT4 using the same `1332.5 keV` LaBr₃ coincidence window and normalized simulation spectrum (physical PDF p.60 / printed p.48). The physical PDF p.61 / printed p.49 summary repeats that the measured efficiency is markedly lower and the cause remains under investigation. This establishes the detector-method discrepancy but does not identify its cause. The seven-layer CsI(Tl) telescope with four PMTs per crystal favors `E–Range` over `ΔE–E` for isotope identification in simulations. Beam tests give about `5%` FWHM single-layer energy resolution; oxygen isotopes with similar energy per nucleon are not fully separated at this resolution, but including range improves the separation. Calibration agrees with experiment within about `5%`.

## Experimental or Theoretical Setup

- Gamma Ball: CsI(Tl) array, Add-back reconstruction, `60Co` cascade with LaBr3(Ce) trigger.
- Particle telescope: seven CsI(Tl) layers, four PMTs per crystal, `ΔE–E–Range` readout.
- Simulation: GEANT4 for efficiency and PID comparisons.
- Beam tests: single-crystal resolution, oxygen-isotope PID and energy calibration.

## Key Results

| issue_id | priority | source_and_locator | core_claim | claim_kind | evidence_level | locator | conflict_or_gap | competing_explanations | l3_l4_route | research_status | stage_conclusion | knowledge_increment | remaining_uncertainty | next_autonomous_route | needs_review |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DD-20260910-CSR-01 | P0 | physical PDF pp.53, 59–61 / printed pp.41, 47–49，Eq.4.7–4.8、4.11，Fig.4.8–4.11 | Gamma Ball Add-back measurement gives `38.9%` full-energy-peak efficiency at `1173.2 keV` within the first-phase covered solid angle (about 6% of 4π), while GEANT4 gives `66.0%` using the same LaBr₃ coincidence-window procedure. | experimental-fact + model-result | direct | printed p.41 defines `ε_SP`; p.47 derives `ε_SP=N_P/N` and reports `38.9%` after small-peak correction; p.48 reports normalized-simulation `66.0%`; p.49 summary says the cause remains under investigation. | The measured and simulated values differ by nearly a factor of two, but the thesis localizes the comparison pipeline and explicitly leaves the cause unresolved. This is not evidence that either value is universally correct. | Geometry/first-phase coverage, source and trigger acceptance, coincidence window, background/small-peak treatment, threshold, dead material and GEANT4 response can all contribute. | L3：locator 级重建 measured-vs-simulated definitions and procedure completed；L4 only with raw spectra and manifest. | completed | L3 completed: discrepancy and its comparison boundary are page-localized; preserve `38.9%` and `66.0%` as lineage-specific reported values and do not choose one as “true”. | 新知识 + 边界/失败知识 | Raw spectra, exact solid angle, full event-selection record and GEANT4 input are missing; cause remains unresolved. | Recover efficiency tables/geometry, then run a manifest-based sensitivity and negative-control check. | true |
| DD-20260910-CSR-02 | P0 | PDF pp.50–71、Fig.5.1–5.14 | Seven-layer CsI(Tl) telescope with four PMTs per crystal uses `ΔE–E–Range`; simulated `E–Range` outperforms `ΔE–E` for isotope identification. | model-result | direct | PDF pp.50–71、Fig.5.1–5.14 | The comparison is simulation/beam-condition specific and does not provide a universal PID threshold. | Light-output nonlinearity, range straggling, layer thickness, PMT gain and beam contamination can change separation. | L3：compare PID observables under stated geometry; L4 not started. | completed | Engineering result is reusable as a design rationale, not a universal isotope-identification claim. | 总结知识 | Full detector response and event-by-event contamination are unavailable. | Reproduce ΔE–E and E–Range plots with the original geometry and negative isotope pairs. | true |
| DD-20260910-CSR-03 | P1 | 摘要、PDF pp.72–90、结论 | Beam tests give about `5%` FWHM single-layer CsI resolution; O-isotopes with similar energy per nucleon are not fully separated, while Range–ΔE improves clarity; calibration agrees within `5%`. | experimental-fact | direct | 摘要、PDF pp.72–90、结论 | “5%” and “within 5%” refer to different resolution/calibration comparisons. | Beam spread, crystal response, temperature, PMT gain and calibration function affect each metric. | L3：separate resolution, PID and calibration error budgets；L4 only with raw beam spectra. | completed | Keep the three statements separate and conditional. | 边界/失败知识 | No full error budget or isotope-by-isotope confusion matrix. | Build a calibration/PID table with beam conditions and failure cases. | true |
| DD-20260910-CSR-04 | P1 | PDF pp.40–90 | No reproducible manifest, code archive, raw spectra or sensitivity/negative-control analysis is available in this batch, so L4 remains zero. | our-inference | contextual | PDF pp.40–90 | Detector performance cannot be independently re-simulated from the thesis alone. | Alternate thresholds, geometry and response functions may alter the reported gap and PID ranking. | L3 provenance audit; L4 stopped for data/provenance. | stopped | Stop reason is missing data, not a negative physical result. | 边界/失败知识 | Reproducibility and cross-device transfer remain unresolved. | Obtain GEANT4 geometry, raw spectra and beam-test files, then rerun sensitivity/negative controls. | true |

## Nuclear Structure Information

This is a detector-system thesis. `Gamma Ball` and CsI telescope performance are method inputs for future nuclear-structure experiments; no independent level scheme or nucleus page is created here.

## Authors' Interpretation

The author interprets the lower experimental Gamma Ball efficiency as an unresolved detector/simulation discrepancy and the range-enhanced PID as a solution to the angular-information limitation of the previous magnetic spectrometer.

## Model Results

GEANT4 efficiency/PID curves and detector response are simulation outputs. They must retain geometry, thresholds and calibration conditions.

## Competing Interpretations and Limitations

- Efficiency values compare different pipelines unless trigger, solid angle, thresholds and full-energy definitions are identical.
- Range information can improve isotope separation while still leaving unresolved neighboring isotopes at finite resolution.
- This thesis and Yue's Gamma Ball thesis are dependent apparatus sources, not independent experiments.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-CSR-1 | Efficiency discrepancy | The measured/simulated gap is itself the important reproducible boundary. | DD-20260910-CSR-01；PDF pp.40–49 | unreviewed |
| AR-CSR-2 | PID transfer | `E–Range` advantage is conditional on layer geometry and response, not universal. | DD-20260910-CSR-02/03；PDF pp.50–90 | unreviewed |
| AR-CSR-3 | L4 reproducibility | No manifest/raw data means no L4 claim; future rerun needs sensitivity and negative controls. | DD-20260910-CSR-04 | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki had CSR external-target and Gamma Ball context but lacked the thesis's measured-vs-simulated efficiency discrepancy and PID locator.
- Effect of this source: `extends` detector-method knowledge and adds a failure/boundary case for efficiency transfer.
- Persistence decision: source; no duplicate experiment or nucleus page.
- Review state: `unreviewed`; all claims retain `needs_review: true`.

## Related Knowledge and Project Relations

| relation_type | target | specific_relation |
|---|---|---|
| detector-lineage | [[yue-ke-2010-hirfl-csr-gamma-ball-csi-thesis]] | Same Gamma Ball apparatus design/efficiency lineage. |
| methodological-bridge | [[wu-hongyi-2020-general-purpose-digital-daq-thesis]] | Digital DAQ and detector readout engineering context. |
| methodological-bridge | [[sun-yazhou-2019-16c-single-proton-knockout-thesis]] | Shared HIRFL-CSR/RIBLL-II external-target analysis environment. |

## Human Review Triage

### P0

- `DD-20260910-CSR-01/02`：`38.9%/66.0%` 的定义、窗选和页码已完成 L3 定位；后续人工复核重点是 geometry/acceptance 和 E–Range comparison。

### P1

- `DD-20260910-CSR-03/04`：核对 5% resolution, within-5% calibration and missing-manifest stop reason.

## Extracted Pages

- PDF pp.1–8：title, abstract and contents.
- PDF pp.35–49：Gamma Ball calibration and efficiency.
- PDF pp.50–90：CsI telescope design, simulation, beam test and calibration.

## Non-source Notes and Follow-up

论文题名页、摘要、效率章节、PID 模拟/束测章节和结论已实际读取；效率定义、`38.9%`/`66.0%` 比较页、PID 和 calibration 关键页已视觉核对。未修改 raw、BibTeX 或相关 Gamma Ball source 页。
