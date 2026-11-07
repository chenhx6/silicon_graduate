---
type: source
title: "Isomer depletion as experimental evidence of nuclear excitation by electron capture"
aliases: [Chiara 2018 Mo93m NEEC, Chiara 2018 Nature NEEC claim]
created: 2026-11-07
updated: 2026-11-07
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: experiment-article
reading_depth: deep-read
title_original: "Isomer depletion as experimental evidence of nuclear excitation by electron capture"
authors: [C. J. Chiara, J. J. Carroll, M. P. Carpenter, J. P. Greene, D. J. Hartley, R. V. F. Janssens, G. J. Lane, J. C. Marsh, D. A. Matters, M. Polasik, J. Rzadkiewicz, D. Seweryniak, S. Zhu, S. Bottoni, A. B. Hayes, S. A. Karamian]
journal: Nature
year: 2018
volume: 554
pages: 216--219
doi: 10.1038/nature25483
language: en
canonical_source: doi:10.1038/nature25483
raw_file: "raw/papers/isomer/isomer_application/nuclear battery/2018_Chiara et al_Isomer depletion as experimental evidence of nuclear excitation by electron capture.pdf"
raw_sha256: 5a6d0f39b280e527fce655e37a894c49ce90720ac252915327d880425fcf16ee
archive_required: true
nuclei: [93mo]
reactions: ["7Li(90Zr,p3n)93mMo"]
observables: [isomer-depletion-probability, triple-gamma-coincidence, doppler-shifted-feeding, resonance-cross-section]
methods: [inverse-kinematics-fusion-evaporation, digital-gammasphere, beam-foil-stopping, double-gating-background-subtraction]
tags: [mo93m, neec, isomer-depletion, gammasphere, controversial-observation, nuclear-battery]
---

# Chiara et al. (2018): Isomer depletion as experimental evidence of nuclear excitation by electron capture

## Bibliographic Record

C. J. Chiara, J. J. Carroll, M. P. Carpenter, J. P. Greene, D. J. Hartley, R. V. F. Janssens, G. J. Lane, J. C. Marsh, D. A. Matters, M. Polasik, J. Rzadkiewicz, D. Seweryniak, S. Zhu, S. Bottoni, A. B. Hayes, and S. A. Karamian, "Isomer depletion as experimental evidence of nuclear excitation by electron capture," *Nature* **554**, 216--219 (2018), DOI: `10.1038/nature25483`. Primary PDF is 10 pages, SHA-256: `5a6d0f39b280e527fce655e37a894c49ce90720ac252915327d880425fcf16ee`.

## Scope and Reading Depth

Deep reading of main text, Methods, and Extended Data display items. Visual inspection of Fig. 1 decay scheme (PDF p. 2 / printed p. 217), Fig. 2 coincidence spectra (PDF p. 2 / printed p. 217), Fig. 3 Doppler-corrected 2475-keV and unshifted 268-keV spectra (PDF p. 3 / printed p. 218), and Methods background subtraction parameter \(k_{\text{ave}} = 0.99(8)\).

## Summary

The paper reports claimed experimental evidence for Nuclear Excitation by Electron Capture (NEEC) in \(^{93\text{m}}\)Mo. Reconstructing \(^{90}\text{Zr} + {}^{7}\text{Li}\) reaction products stopping in a carbon foil, the authors report prompt coincidences between Doppler-shifted 2475-keV \(\gamma\)-rays feeding the 6.85-h isomer and unshifted 268-keV \(\gamma\)-rays depopulating a 2430-keV intermediate state. They extract an excitation probability \(P_{\text{exc}} = 1.0(3)\%\) and average cross section \(\bar{\sigma}_{\text{exc}} \approx 40\text{ b}\).

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| C18-1 | Reports observation of prompt coincidences between Doppler-shifted 2475-keV feeding line and unshifted 268-685-1478 keV cascade in 93Mo. | measured-coincidence | direct experimental report | printed p.216--217, Fig. 2 | true |
| C18-2 | Extracts isomer depletion probability P_exc = 1.0(3)% from ratio of unshifted 268-keV area (510 counts) to Doppler-corrected 2475-keV area (15400 counts). | derived-quantity | derived experimental value | printed p.217--218, Fig. 3 | true |
| C18-3 | Deduces average target-stopping cross section sigma_exc ~ 40 b across 5 mg/cm2 carbon catcher. | derived-quantity | derived value | printed p.217--218 | true |
| C18-4 | Calculates Coulomb excitation (GOSIA: 3e-6) and inelastic scattering (FRESCO: 2e-6) as insufficient to explain observed 1% depletion. | model-calculation | model bound | printed p.218, Methods | true |

## Competing Interpretations and Limitations

后续证据不能倒写成2018原实验已经唯一查明的污染来源。Guo2021提出产生/停止靶反应及符合背景的竞争解释，原作者的时间门答复也须保留；Wu2019的理论率与实验率比较依赖停止、电子态和核输入。Guo2022使用隔离异能束，在其条件下未见显著268-keV峰，给出约\(2\times10^{-5}\)的上限，对百分比量级的先前报告构成实质挑战。该上限既不是所有NEEC过程的排除，也不单独证明2018数据的唯一背景机制。评论、答复与隔离束的实际证据及各自依赖见[[mo93-neec-evidence-and-depletion-transfer-20261107]]、[[guo-2021-mo93m-depletion-contamination-challenge]]和[[guo-2022-mo93m-isomer-beam-depletion-limit]]。

## Extracted Pages

- mo93m
- neec
- isomer-depletion
- gammasphere
