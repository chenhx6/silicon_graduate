---
type: source
title: "Garg et al. 2015 - Negative-parity high-spin states and possible magnetic rotation in 135Pr"
aliases: [Garg 2015 135Pr magnetic rotation]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: experiment-and-TAC
reading_depth: deep-read
title_original: "Negative-parity high-spin states and a possible magnetic rotation band in 135Pr"
authors: [Ritika Garg, S. Kumar, Mansi Saxena, Savi Goyal, Davinder Siwal, Sunil Kalkal, S. Verma, R. Singh, S. C. Pancholi, R. Palit, Deepika Choudhury, S. S. Ghugre, G. Mukherjee, R. Kumar, R. P. Singh, S. Muralithar, R. K. Bhowmik, S. Mandal]
journal: "Physical Review C"
year: 2015
volume: 92
pages: "054325"
doi: "10.1103/PhysRevC.92.054325"
citation_key: Garg_2015
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "Garg et al., Phys. Rev. C 92, 054325 (2015)"
library_file: "raw/papers/gpt/high-spin-20260920/纲图/2015_Garg et al_Negative-parity high-spin states and a possible magnetic rotation band in Pr 76.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/纲图/2015_Garg et al_Negative-parity high-spin states and a possible magnetic rotation band in Pr 76.pdf"
raw_sha256: "c74e7c12614cf405861c639194e132f3096d5f46d22062b0164fa166282b9e88"
nuclei: [135Pr]
reactions: [123Sb-16O-4n]
experiments: [INGA, RDCO, IPDCO]
models: [tilted-axis-cranking, 3qp-5qp-configuration]
observables: [negative-parity-band, M1-E2, signature, crossing, polarization, DCO]
methods: [gamma-gamma-coincidence, DCO, linear-polarization]
tags: [135Pr, magnetic-rotation, TAC, high-spin, M1-E2]
---

# Negative-parity high-spin states and possible magnetic rotation in `135Pr`

## Bibliographic Record

- R. Garg *et al.*, *Phys. Rev. C* **92**, 054325 (2015), DOI `10.1103/PhysRevC.92.054325`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/纲图/2015_Garg et al_Negative-parity high-spin states and a possible magnetic rotation band in Pr 76.pdf`。

## Scope and Reading Depth

- PDF pp.054325-1–9 fully read: `123Sb(16O,4n)` experiment, INGA matrices, level scheme, RDCO/IPDCO, Table I, alignments/crossing plots, TAC 3qp/5qp comparison and conclusion.
- Not covered: raw events and later lifetime measurements.

## Key Results

- About `3×10^8` triple-and-higher γ coincidences were recorded with 15 INGA clovers. A negative-parity `ΔI=1` band with new crossover E2 transitions was established; RDCO/IPDCO assigned M1/E2 and E2 character for many links (PDF pp.1–4, Table I, Fig.1).
- The band shows strong M1 transitions, small/medium E2 crossovers and a crossing in alignment/energy behavior. TAC calculations use a 3qp `πh11/2⊗νh11/2^-2` configuration for the lower band and a 5qp `πh11/2(g7/2)^2⊗νh11/2^-2` configuration above the crossing (PDF pp.5–9, Figs.4–6).
- The authors call the band a possible magnetic-rotation band; the interpretation is based on M1/E2 pattern, alignment and TAC, while lifetime-derived `B(M1)/B(E2)` remains a requested follow-up (PDF pp.8–9).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GA15-1 | `135Pr` negative-parity high-spin band has M1-dominated ΔI=1 links and new E2 crossovers. | experiment-result | direct | PDF pp.1–4, Table I | true |
| GA15-2 | TAC 3qp/5qp configurations reproduce the crossing/energy systematics and motivate a possible magnetic-rotation interpretation. | model-interpretation | mixed | PDF pp.5–9 | true |
| GA15-3 | Without lifetimes/absolute strengths, the magnetic-rotation label remains possible rather than established. | limitation | direct | PDF pp.8–9 | false |

## Summary

Garg *et al.* provide an A≈130 high-spin magnetic-rotation candidate with direct multipolarity/polarization evidence and TAC configuration comparison. The paper appropriately leaves the conclusion provisional pending lifetimes and `B(M1)/B(E2)`.

## Competing Interpretations and Limitations

- Strong M1/weak E2 patterns can also reflect signature/configuration mixing or core rotation; TAC fits are not unique.
- The 3qp→5qp crossing and possible MR identity depend on configuration assignments and alignment reference.
- No DSAM/RDDS lifetimes or absolute transition probabilities are provided in this source; a magnetic-rotation claim should not be upgraded beyond candidate level.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| GA15-AR-1 | Assignment chain | Coincidence scheme → RDCO/IPDCO/δ → M1/E2 links and negative-parity band identity. | PDF pp.2–4, Table I | self-checking |
| GA15-AR-2 | MR chain | Alignment/crossing + M1/E2 pattern → TAC 3qp/5qp comparison → possible MR ranking. | PDF pp.5–9 | self-checking |
| GA15-AR-3 | Missing discriminator | Lifetimes and absolute B(M1)/B(E2) needed to distinguish MR from competing core/signature explanations. | PDF conclusion | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[magnetic-rotation]], [[tilted-axis-cranking]], [[multipole-mixing-ratio]], [[linear-polarization-asymmetry]] and the A≈130 magnetic-rotation candidate map.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `GA15-P0-1`: Retain “possible magnetic rotation” wording and missing-lifetime boundary; do not promote a TAC-supported candidate to established MR.

## Extracted Pages

- Concepts/methods: [[magnetic-rotation]], [[tilted-axis-cranking]], [[multipole-mixing-ratio]], [[linear-polarization-asymmetry]]。
