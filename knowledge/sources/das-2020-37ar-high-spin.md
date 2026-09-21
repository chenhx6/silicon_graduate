---
type: source
title: "Das et al. 2020 - High spin states of 37Ar"
aliases: [Das 2020 37Ar high spin]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: experiment-and-shell-model
reading_depth: deep-read
title_original: "High spin states of 37Ar"
authors: [Ananya Das, Abhijit Bisoi, M. Saha Sarkar, S. Sarkar, S. Ray, D. Pramanik, R. Kshetri, S. Nag, P. Singh, K. Selvakumar, A. Goswami, S. Saha, J. Sethi, T. Trivedi, B. S. Naidu, R. Donthi, V. Nanal, R. Palit]
journal: "Physical Review C"
year: 2020
volume: 101
pages: "044310"
doi: "10.1103/PhysRevC.101.044310"
citation_key: Das_2020
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "Das et al., Phys. Rev. C 101, 044310 (2020)"
library_file: "raw/papers/gpt/high-spin-20260920/纲图/2020_Das et al_High spin states of Ar 37.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/纲图/2020_Das et al_High spin states of Ar 37.pdf"
raw_sha256: "b7c28e74a0c6a572a9c46642982c2d8b19a4ee643fc9f8f7be03aee8f13b6483"
nuclei: [37Ar, 36Ar, 38Ar]
reactions: [27Al-12C-np]
experiments: [INGA, Pixie-16, RDCO, RADO, IPDCO]
models: [large-basis-shell-model, sd-pf-cross-shell, two-level-mixing]
observables: [level-scheme, RDCO, RADO, IPDCO, mixing-ratio, configuration-mixing]
methods: [gamma-gamma-coincidence, DCO, ADO, linear-polarization]
tags: [37Ar, INGA, high-spin, level-scheme, shell-model, RDCO, IPDCO]
---

# High-spin states of `37Ar`

## Bibliographic Record

- A. Das *et al.*, *Phys. Rev. C* **101**, 044310 (2020), DOI `10.1103/PhysRevC.101.044310`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/纲图/2020_Das et al_High spin states of Ar 37.pdf`。

## Scope and Reading Depth

- PDF pp.044310-1–13 fully read: `27Al(12C,np)` at 40 MeV, 15-clover INGA/Pixie-16 analysis, RDCO/RADO/IPDCO definitions, level scheme to 10.5 MeV, Tables I–II, shell-model restrictions, two-level mixing and conclusion.
- Not covered: raw event list, full shell-model code and later evaluations.

## Key Results

- About `6×10^8` twofold coincidences were recorded with 15 clovers at six angles. The `37Ar` scheme was extended to 10.5 MeV with 18 new γ transitions and eight new levels (PDF pp.1–4, Fig.3, Tables I–II).
- DCO uses θ=157° gates and `σ/J=0.3`; pure dipole/pure quadrupole RADO references are approximately 0.8/1.7. IPDCO signs provide electric/magnetic character after the measured clover asymmetry correction (PDF pp.2–4, Eqs.1–6).
- New/confirmed assignments use combined observables: ten new δ values were extracted, several earlier E2 mixing ratios were simplified to pure E2, and Doppler-shifted peaks were handled with angle-independent matrices (PDF pp.3–6, Table I).
- Large-basis shell-model calculations with different sd/pf particle restrictions and a two-level mixing calculation are used to interpret single-particle versus multiparticle–multihole components; these are model interpretations of the observed scheme (PDF pp.7–12).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DA20-1 | `37Ar` level scheme is extended to 10.5 MeV with multimethod spin/parity evidence. | experiment-result | direct | PDF pp.1–6, Fig.3, Tables I–II | true |
| DA20-2 | `σ/J=0.3`, RADO reference values and clover calibration enter δ/IPDCO assignments. | method-boundary | direct | PDF pp.2–4 | false |
| DA20-3 | sd–pf shell-model restrictions and two-level mixing explain configuration content but do not directly measure shape. | model-result | mixed | PDF pp.7–12 | true |

## Summary

Das *et al.* provide a modern light-nucleus high-spin benchmark in which level placement, RDCO/RADO/IPDCO and δ are jointly used before shell-model interpretation. The source reinforces that alignment and detector calibration are part of the assignment evidence, while cross-shell configuration mixing remains a model layer.

## Competing Interpretations and Limitations

- RADO/RDCO thresholds depend on the INGA geometry, gate multipolarity and `σ/J`; low statistics and Doppler shifts can weaken assignments.
- Earlier pure-E2 versus mixed assignments may differ because of statistical fluctuations and limited ANGCOR branch resolution.
- Shell-model particle restrictions and two-level mixing are not direct deformation measurements and should not be transplanted to A≈130 without a model-space audit.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| DA20-AR-1 | Assignment chain | Coincidence scheme → RDCO/RADO/IPDCO/δ → spin/parity and multipolarity; retain weak/tentative branches. | PDF pp.2–6, Tables I–II | self-checking |
| DA20-AR-2 | Model chain | Level energies/transition strengths → restricted sd–pf shell-model and two-level mixing; model results are not measured shape. | PDF pp.7–12 | self-checking |
| DA20-AR-3 | Transfer condition | Recalibrate `σ/J`, angles and detector response before comparing to other INGA runs or nuclei. | PDF pp.2–4 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[angular-distribution]], [[angular-correlation]], [[compton-polarimetry]], [[linear-polarization-asymmetry]], [[multipole-mixing-ratio]] and light-nucleus method comparators.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `DA20-P0-1`: Preserve the INGA alignment/calibration and shell-model restriction boundaries; do not treat model configuration mixing as direct shape evidence.

## Extracted Pages

- Methods/observables: [[angular-distribution]], [[angular-correlation]], [[compton-polarimetry]], [[multipole-mixing-ratio]]。
