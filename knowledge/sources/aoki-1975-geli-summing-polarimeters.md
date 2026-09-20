---
type: source
title: "Aoki et al. 1975 - Ge(Li) summing spectrometers and multidirectional polarimeters"
aliases: [Aoki 1975 GeLi summing polarimeters]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: method-paper
reading_depth: deep-read
title_original: "Ge(Li) Summing Spectrometers of Special Type"
authors: [T. Aoki, J.-Z. Ruan, A. Yoshimura, Y. Matsuyama]
journal: "Nuclear Instruments and Methods"
year: 1975
volume: 128
pages: "53-60"
pii: "0029-554X(75)90773-9"
canonical_source: "Aoki et al., Nucl. Instr. Meth. 128, 53-60 (1975)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1975_Aoki et al_Ge(Li) summing spectrometers of special type.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1975_Aoki et al_Ge(Li) summing spectrometers of special type.pdf"
raw_sha256: "b0a36fa350a078021212b8cd9a28fecc389baf1ebbbd8a60f79f025b68cc70a7"
nuclei: [generic]
reactions: [22Na-annihilation, 60Co, 137Cs, 152Eu]
experiments: [GeLi-summing-polarimeter, GeLi-GeLi-summing-spectrometer]
models: [Compton-scattering-response]
observables: [linear-polarization, Compton-background, full-energy-efficiency]
methods: [Compton-polarimetry, coincidence-summing]
tags: [GeLi, summing-spectrometer, Compton-polarimetry, polarization]
---

# Ge(Li) summing spectrometers of special type

## Bibliographic Record

- T. Aoki *et al.*, *Nucl. Instr. Meth.* **128**, 53–60 (1975), PII `0029-554X(75)90773-9`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1975_Aoki et al_Ge(Li) summing spectrometers of special type.pdf`。

## Scope and Reading Depth

- PDF pp.53–60 fully read: six-sector and multi-directional single-crystal Ge(Li) polarimeter, annihilation-photon test, two-analyzer variant, Ge(Li)–Ge(Li) backscatter summing spectrometer, spectra/efficiency/background figures and conclusions.
- Not covered: raw electronics traces and later segmented-detector designs.

## Key Results

- A machined planar Ge(Li) crystal contains a central scatterer, four 30° analyzers (`φ=0°,30°,60°,90°`) and a rejector. All azimuths are measured simultaneously without rotating the polarimeter (PDF pp.53–56, Fig.1).
- Majority anticoincidence suppresses rescattered/Compton background by about a factor of four in the summed spectrum. The annihilation-photon test gives measured `I(φ=0)/I(φ=90)=2.47±0.30`, consistent with the predicted 2.50 after finite-solid-angle effects (PDF pp.55–57, Figs.2,5–6).
- An improved two-analyzer version (`φ=0°` and `90°`) reduces the need for multiple rotations and shortens measurement time by about a factor of four, at the cost of detector-specific efficiency/geometry tradeoffs (PDF pp.56–57, Fig.7).
- A ring-plus-reflector Ge(Li) summing Compton spectrometer reduces continuous background by about a factor of 20; the summed full-energy efficiency above 500 keV is below one-quarter of the reflector singles efficiency, and the practical lower energy threshold is about 300 keV for a flat background (PDF pp.57–60, Figs.8–12).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AO75-1 | Simultaneous four-angle Ge(Li) analyzers can measure polarization azimuths without rotating the detector. | method-result | direct | PDF pp.53–57, Figs.1,5–7 | true |
| AO75-2 | The annihilation test reproduces the finite-solid-angle intensity ratio within uncertainty. | method-validation | direct | PDF pp.56–57, Fig.6 | true |
| AO75-3 | Summing spectrometers trade efficiency for strong Compton-background reduction and a practical energy threshold. | detector-tradeoff | direct | PDF pp.57–60, Figs.9–12 | false |

## Summary

Aoki *et al.* demonstrate an early high-resolution, multidirectional Ge(Li) polarimeter and a ring-reflector summing spectrometer. The source supplies a historical detector-response baseline: simultaneous azimuthal coverage is valuable, but anti-coincidence, biasing, window setting, efficiency and energy threshold define the actual sensitivity.

## Competing Interpretations and Limitations

- The 2.47 ratio is an annihilation-photon benchmark, not a universal polarization sensitivity; finite solid angle and analyzer geometry are specific.
- Embedded-detector biasing can create anomalous efficiency; all sectors must be biased consistently.
- Background reduction in the summing spectrometer comes with severe efficiency loss and a threshold/Compton-tail tradeoff.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AO75-AR-1 | Polarimeter chain | Scatterer → azimuth analyzers/rejector → summed peak counts → polarization ratio; simultaneous angles avoid rotation systematic. | PDF Secs.2.1–2.3 | self-checking |
| AO75-AR-2 | Spectrometer chain | Backscatter reflector + ring detector coincidence → flat Compton background → weak-line visibility with efficiency/threshold cost. | PDF Sec.3, Figs.8–12 | self-checking |
| AO75-AR-3 | Transfer condition | Detector bias/window/geometry must be recalibrated before comparing with modern `Q` or figure-of-merit values. | PDF pp.54–60 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[compton-polarimetry]], [[linear-polarization-asymmetry]] and historical detector-response lineage.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `AO75-P0-1`: Preserve simultaneous-angle geometry, bias/window settings and efficiency/background tradeoff; do not treat the annihilation ratio as a universal calibration.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]]。
