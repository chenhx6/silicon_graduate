---
type: source
title: "Li et al. 2025: IMP-DRAGON HPGe array"
aliases: [IMP-DRAGON, IMP DRAGON HPGe array, IMP-Detectors for Research by Analyzing Gamma-ray Observation in Nuclei]
created: 2026-11-01
archive_required: true
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
source_type: detector-method-paper
reading_depth: read
title_original: "IMP-DRAGON: A High-Purity Germanium detector array for probing the atomic nucleus"
authors: [G. S. Li, X. H. Zhou, M. L. Liu]
journal: "Nuclear Instruments and Methods in Physics Research A"
year: 2025
volume: 1080
pages: "170804"
doi: 10.1016/j.nima.2025.170804
arxiv:
language: en
canonical_source: "https://www.sciencedirect.com/science/article/pii/S0168900225006059"
citation_key: li_2025_imp_dragon
raw_file: "raw/papers/IMP-DRAGON A High-Purity Germanium detector array for probing the atomic nucleus.pdf"
raw_sha256: "4841f20f455670f028dbce8e0c1cd349aa0529635d4ffb4815071d8795392cec"
nuclei: []
reactions: []
experiments: [IMP-DRAGON]
models: [geant4]
observables: [gamma-ray-energy, gamma-gamma-coincidence, linear-polarization, angular-distribution, dsam-lifetime, counting-rate]
methods: [hpge, bgo-anti-compton, clover-polarimeter, list-mode-daq, geant4, auxiliary-detectors]
tags: [detector-method, imp-dragon, hpge, bgo, clover, polarization, dsam, high-spin]
---

# Li et al. 2025：IMP-DRAGON 高纯锗阵列

## Bibliographic Record

G. S. Li et al., *IMP-DRAGON: A High-Purity Germanium detector array for probing the
atomic nucleus*, *Nuclear Instruments and Methods in Physics Research A* **1080**
(2025) 170804, DOI `10.1016/j.nima.2025.170804`。本地 PDF 为 6 页，SHA-256 为
`4841f20f455670f028dbce8e0c1cd349aa0529635d4ffb4815071d8795392cec`。

## Scope and Reading Depth

本轮读取 PDF 全部正文、摘要、表述和图注，覆盖 detector configuration、BGO
anti-Compton、electronics/DAQ、Geant4、DSAM、ADO 和 clover polarization 段落。
没有取得原始波形、完整 Geant4 geometry/input、逐事件数据或全部 commissioning
文件，因此本文性能数字按装置论文报告和条件化设计输入记录。

## Research Question and Design Logic

论文展示一种可在高效率、高颗粒度、快定时和辅助粒子探测之间切换的 HPGe 阵列。
其核心不是单一“最好”构型，而是把 detector geometry、BGO suppression、list-mode
DAQ 和 auxiliary detectors 组合成面向不同核结构问题的可重排平台。

## Key Results

| ID | Narrow statement | claim_kind | evidence_level | locator | Boundary |
|---|---|---|---|---|
| ID25-1 | 阵列最多整合 16 个 coaxial HPGe 和 8 个 clover HPGe，每个带专用 BGO anti-Compton shield；可与 LaBr3(Ce)、plastic、Si 和 CsI(Tl) 辅助探测器组合。 | experimental-fact | PDF pp.1–2, abstract and Sec.2 | 具体实验使用的 detector subset、距离和辅助阵列仍需逐 run 记录 |
| ID25-2 | coaxial detector 相对效率约 70%，clover assembly 约 160%；`60Co` 1332.5-keV energy resolution 约 2.3–2.8 keV FWHM。 | detector-performance | PDF p.2, Sec.2.1 | relative efficiency 和 FWHM 是指定 detector/source geometry 下的装置性能 |
| ID25-3 | coaxial BGO 厚度约 11–35 mm，在 400–800 keV 区域报告约 77% background reduction 和 `P/C≈8.8`；clover 配置报告约 60% reduction 和 `P/C≈7.5`。 | detector-performance | PDF p.2, Sec.2.1 and Fig.2 | 不能把不同 BGO thickness、source geometry 和 energy window 混成统一响应 |
| ID25-4 | 16 coaxial + 8 clover 的紧凑构型几何覆盖约 65% of `4π`，1332.5-keV total photo-peak efficiency 约 10%（无 BGO shield 的距离说明）。 | detector-performance | PDF p.3, Sec.2.2 | full array 的实际效率仍依赖 shield、target position、add-back 和 event cuts |
| ID25-5 | electronics 以 100 MHz、14/16-bit waveform digitizers 和 FPGA 处理 list-mode energy/time；BGO veto window 为 400 ns；HPGe detector event rate 可到约 8 kHz/每探测器而不牺牲能量分辨。 | experimental-fact | PDF p.3, Sec.2.3 | rate、pile-up rejection 和 timing 仍依赖具体 card、signal shape 和 firmware |
| ID25-6 | 通过 face-to-face geometry 可服务 activated-sample γ/γ 测量；hybrid LaBr3/plastic 配置服务快定时，clover 可作 Compton polarimeter，HPGe 还用于 DSAM/ADO。 | design-capability | PDF pp.1–4, Secs.2–3 | capability 不是任意核素的已完成物理结果；需要目标反应和 response simulation |
| ID25-7 | 论文以 `45Sc` DSAM lineshape、`95Tc` ADO/polarization 等 commissioning/应用例展示装置用途，并强调稀有事件的高效率、背景抑制和颗粒度。 | application-example | PDF pp.4–6, Figs.7–8 and conclusion | 应用例不是同一 acquisition 的独立重复，也不自动迁移到 A≈130 |

## Detector-to-Physics Mapping

| Physics question | Useful configuration | Dominant response |
|---|---|---|
| weak high-spin cascade / band extension | compact HPGe+BGO | efficiency, Compton suppression, γγγ |
| mixing-ratio and parity test | clover at selected angles | linear polarization plus angular distribution |
| ps-scale lifetime | HPGe + LaBr3 hybrid or DSAM geometry | timing or Doppler lineshape |
| recoil/particle-tagged rare channel | HPGe + Si/CsI auxiliary detectors | event identity and background rejection |
| activated sample decay | adjustable face-to-face geometry | coincidence efficiency and summing control |

## Summary

IMP-DRAGON is a reconfigurable HPGe/BGO platform whose useful physics value comes from
combining high-resolution energy measurement with selected polarization, timing and
particle-tagging modes. The paper supports a detector response design and commissioning
baseline; it does not supply a target-specific A≈130 experiment or a complete replayable
response matrix.

## Competing Interpretations and Limitations

- Nominal efficiency, background suppression and timing depend on detector subset,
  geometry, thresholds, add-back and calibration.
- A hybrid LaBr3 configuration improves timing but changes the event response and data
  model; HPGe and fast channels require separate calibration and covariance blocks.
- Geant4 and commissioning plots do not replace raw waveforms, source spectra or
  target-specific response simulations.

## Model and Reproducibility Boundary

Geant4 simulations are detector-response models. The paper does not provide the complete
geometry, event generator, calibration covariance, raw commissioning spectra or a
replayable response matrix. The design therefore supports an experiment proposal and a
response-contract template, while a target-specific L4 sensitivity study still needs
reaction kinematics, target position, detector subset, thresholds, deadtime and source
or beam calibration inputs.

## Knowledge Impact and Learning Decision

- `extends`: the detector-method layer with a current IMP array capable of switching between
  HPGe efficiency, polarization, DSAM and auxiliary-particle modes.
- `supports`: a proposal architecture that uses the same event stream for branch identity,
  lifetime and polarization rather than treating these as unrelated measurements.
- `limits`: the paper alone does not provide A≈130 event data, target-specific efficiency,
  joint covariance or a completed new-physics observation.
- `design inference`: the most promising upgrade path is a response-aware hybrid mode:
  compact HPGe+BGO for weak cascades, clover polarization at selected rings, and a small
  fast-timing/particle subsystem rather than maximizing HPGe count alone.

## Extracted Pages

- PDF pp.1–2: motivation, detector inventory and HPGe/BGO specifications.
- PDF pp.3–4: support structure, electronics, list-mode DAQ and Geant4 setup.
- PDF pp.4–6: DSAM, ADO, polarization and selected commissioning applications.

## Related Knowledge

- [[cross-mass-phenomena-detector-beam-prospectus-20261101]]
- [[tracking-array]]
- [[gamma-ray-linear-polarization-in-nuclear-spectroscopy]]

## Human Review

This page is a Codex self-audit of a detector-method source. `review_status: unreviewed`;
reported performance and proposed mappings remain conditional on the paper's geometry and
commissioning conditions.
