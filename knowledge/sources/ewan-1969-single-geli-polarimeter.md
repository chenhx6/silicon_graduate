---
type: source
title: "Ewan et al. 1969 - Gamma-ray polarization with a single Ge(Li) detector"
aliases: [Ewan 1969 single GeLi polarimeter]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: method-and-application
reading_depth: deep-read
title_original: "Gamma-ray polarization measurements with a single Ge(Li) detector"
authors: [G. T. Ewan, G. I. Andersson, G. A. Bartholomew, A. E. Litherland]
journal: "Physics Letters B"
year: 1969
volume: 29B
pages: "352-354"
pii: "0370-2693(69)90382-7"
canonical_source: "Ewan et al., Phys. Lett. B 29B, 352-354 (1969)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1969_Ewan et al_Gamma-ray polarization measurements with a single Ge(Li) detector.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1969_Ewan et al_Gamma-ray polarization measurements with a single Ge(Li) detector.pdf"
raw_sha256: "ded2493ef0e816b3ed74bc5921f61324ec71b1ae34de8be96c988c71fa3e7be5"
nuclei: [102Ru, 100Mo, 56Fe, 24Mg, 28Si, 12C]
reactions: [100Mo-alpha-2n, 56Fe-p-p-gamma, 24Mg-p-p-gamma, 28Si-p-p-gamma, 12C-p-p-gamma]
experiments: [single-planar-GeLi-Compton-polarimeter]
models: [Klein-Nishina-response, angular-distribution]
observables: [polarization-asymmetry, Q, E2-M1-mixing, parity]
methods: [Compton-polarimetry, angular-distribution]
tags: [GeLi, polarization, Compton-polarimeter, 102Ru]
---

# Polarization with a single planar Ge(Li) detector

## Bibliographic Record

- G. T. Ewan *et al.*, *Phys. Lett. B* **29B**, 352–354 (1969), PII `0370-2693(69)90382-7`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1969_Ewan et al_Gamma-ray polarization measurements with a single Ge(Li) detector.pdf`。

## Scope and Reading Depth

- Three-page letter fully read: planar 4×2.5×0.35 cm³ Ge(Li) geometry, 0.8–4.4 MeV calibration, `100Mo(α,2n)102Ru` application, angular-distribution correction and conclusion.
- Not covered: detailed theoretical calculation in the companion report.

## Key Results

- A single thin planar Ge(Li) detector measures polarization from Compton events in its total-absorption peak; asymmetry `Q=2(N⊥−N∥)/(N⊥+N∥)` is calibrated with polarized γ rays from `56Fe`, `24Mg`, `28Si` and `12C` (PDF pp.352–353, Table 1, Fig.1).
- Sensitivity is about 15.7% at 0.847 MeV, 10.4% at 1.368 MeV, 12.6% at 1.779 MeV and 6.4% at 4.43 MeV after incomplete-polarization correction; photoelectric absorption attenuates the response below 1 MeV (PDF pp.352–353, Table 1, Fig.1).
- In `100Mo(α,2n)102Ru`, 475/631/766-keV transitions show positive E2 polarization, while an 833-keV line has opposite asymmetry and weak angular distribution, indicating mixed multipolarity (E1+M2 or M1+E2) (PDF pp.353–354, Table 2).
- Detector orientation/solid-angle differences are corrected below 1% for the calibration geometry, but response remains energy/geometry dependent (PDF p.353).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| EW69-1 | A single planar Ge(Li) detector can measure parity-sensitive γ polarization with sufficient sensitivity above ~0.8 MeV. | method-result | direct | PDF pp.352–354 | true |
| EW69-2 | `102Ru` calibration/application separates pure E2 and a mixed-polarity 833-keV transition. | application-result | direct | PDF pp.353–354, Table 2 | true |
| EW69-3 | Detector geometry, photoelectric contribution and incomplete-polarization correction control `Q`. | limitation | direct | PDF pp.352–353 | false |

## Summary

Ewan *et al.* demonstrate that even a single planar Ge(Li) can provide useful polarization/parity information. The source is a historical baseline for later segmented and Clover polarimeters; its `Q` values are calibration-specific.

## Competing Interpretations and Limitations

- Photoelectric absorption and finite detector geometry change `Q(E)`; the historical calibration cannot be transferred without remeasurement.
- The mixed 833-keV assignment remains a method demonstration rather than a universal parity rule.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| EW69-AR-1 | Response chain | Known polarized calibration → single-detector Compton asymmetry → corrected `Q(E)` → `102Ru` parity/mixing inference. | PDF Table 1, Fig.1 | self-checking |
| EW69-AR-2 | Transfer condition | Recalibrate orientation, solid angle, threshold and photoelectric fraction for another detector. | PDF pp.352–354 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[compton-polarimetry]], [[linear-polarization-asymmetry]], [[multipole-mixing-ratio]] and historical GeLi detector lineage.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `EW69-P0-1`: Do not transfer single-Ge(Li) `Q` values across energies/geometries without calibration.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]]。
