---
type: source
title: "Der Mateosian and Sunyar 1974 - Attenuation coefficients for partially aligned nuclei"
aliases: [Der Mateosian Sunyar 1974 attenuation tables]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: reference-tables
reading_depth: deep-read
title_original: "Tables of Attenuation Coefficients for Angular Distribution of Gamma Rays from Partially Aligned Nuclei"
authors: [E. Der Mateosian, A. W. Sunyar]
journal: "Atomic Data and Nuclear Data Tables"
year: 1974
volume: 13
pages: "391-406"
pii: "0092-640X(74)90007-2"
canonical_source: "Der Mateosian & Sunyar, ADNDT 13, 391-406 (1974)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/ADO/1974_Der Mateosian_Sunyar_Tables of attenuation coefficients for angular distribution of gamma rays from.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/ADO/1974_Der Mateosian_Sunyar_Tables of attenuation coefficients for angular distribution of gamma rays from.pdf"
raw_sha256: "d31d778674037b17ec2e47f3e9a2d917e46bf273b6cc6e01c607e3eccb843e90"
nuclei: [generic]
reactions: [heavy-ion-alignment]
experiments: [gamma-angular-distribution]
models: [Gaussian-magnetic-substate-alignment, Yamazaki-coefficients]
observables: [alpha2, alpha4, angular-distribution, alignment-width]
methods: [reference-tables, attenuation-correction]
tags: [angular-distribution, attenuation, alignment, tables]
---

# Attenuation coefficients for partially aligned nuclei

## Bibliographic Record

- E. Der Mateosian & A. W. Sunyar, *At. Data Nucl. Data Tables* **13**, 391–406 (1974), PII `0092-640X(74)90007-2`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/ADO/1974_Der Mateosian_Sunyar_Tables of attenuation coefficients for angular distribution of gamma rays from.pdf`。

## Scope and Reading Depth

- PDF pp.391–406 (16 pages) fully read: Gaussian m-substate alignment, `α2/α4` formulas, use example (`Ji=10→Jf=8`, `σ/J=0.3`), integral/half-integral tables and Yamazaki appendix extension to `J=26/51/2`.
- Not covered: later computerized table implementations.

## Key Results

- Partial alignment is represented by Gaussian magnetic-substate populations `w_m∝exp(−m²/2σ²)`. Attenuation coefficients `α_k(J,σ/J)` multiply the complete-alignment `A_k^max` in `W(θ)=1+α2A2^maxP2+α4A4^maxP4` (PDF pp.391–394, Eqs.2–8).
- Tables cover integer and half-integer spins to `J=26` and `51/2`, with `σ/J=0.1–2.0`; the appendix extends Yamazaki complete-alignment angular functions to the same spin range (PDF pp.393–406).
- Worked `Ji=10→Jf=8`, pure E2 example gives `A2^max=0.41353`, `A4^max=−0.17514`; for `σ/J=0.3`, `α2=0.7560`, `α4=0.4093`, yielding attenuated `A2=0.3126`, `A4=−0.0717` (PDF p.393).
- The tables are intended to supply alignment attenuation, not to infer `σ/J` universally; reaction mechanism and side feeding determine the appropriate population model (PDF pp.392–394).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DA74-1 | Gaussian magnetic-substate alignment produces tabulated `α2/α4` attenuation coefficients. | reference-result | direct | PDF pp.391–394 | false |
| DA74-2 | Complete-alignment angular coefficients and partial-alignment attenuation must be applied separately. | method-boundary | direct | PDF pp.392–394 | false |
| DA74-3 | `σ/J` is a reaction/feeding model parameter, not a universal prior. | limitation | direct | PDF pp.392–394 | true |

## Summary

This companion to HS-081 supplies the attenuation half of the high-spin angular-distribution calculation. It makes explicit the numerical bridge between assumed m-substate populations and measured `A2/A4`, and therefore the uncertainty entering DCO/ADO/mixing-ratio inference.

## Competing Interpretations and Limitations

- Gaussian m-substate populations and `σ/J` are reaction/feeding assumptions, not universal alignment truths.
- Table attenuation factors cannot repair an incorrect spin sequence, detector geometry or side-feeding model.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| DA74-AR-1 | Population chain | Reaction/feeding → Gaussian `w_m` → `α_k(σ/J)` → measured angular coefficients. | PDF Eqs.3–8, worked example | self-checking |
| DA74-AR-2 | Transfer condition | Use table only with matching spin, alignment model, gate and convention; otherwise propagate model variance. | PDF pp.392–394 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[angular-distribution]], [[angular-correlation]], [[multipole-mixing-ratio]] and HS-081's mixed-multipole coefficient tables.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `DA74-P0-1`: Do not treat table `α2/α4` values or `σ/J` as detector-independent alignment truth.

## Extracted Pages

- Methods: [[angular-distribution]], [[angular-correlation]]。
