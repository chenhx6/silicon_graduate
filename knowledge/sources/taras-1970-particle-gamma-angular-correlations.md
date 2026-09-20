---
type: source
title: "Analysis of particle-gamma angular correlations and distributions"
aliases: ["Taras 1970 particle-gamma angular distributions", "Taras 1970 Method II curves"]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: method
reading_depth: deep-read
title_original: "ANALYSIS OF PARTICLE-GAMMA ANGULAR CORRELATIONS AND DISTRIBUTIONS"
authors: ["P. Taras"]
journal: "Nuclear Instruments and Methods"
year: 1970
volume: 85
pages: "313-323"
doi: "10.1016/0029-554X(70)90251-X"
language: en
canonical_source: "Taras, P. Analysis of particle-gamma angular correlations and distributions. Nucl. Instrum. Methods 85, 313-323 (1970)."
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/ADO/1970_Taras_Analysis of particle-gamma angular correlations and distributions.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/ADO/1970_Taras_Analysis of particle-gamma angular correlations and distributions.pdf"
raw_sha256: "1bd0ec877718f6cd98ae087ebbc78409694be407b1a66ff778488997a56a8813"
nuclei: ["35Cl", "29Si"]
reactions: ["34S(p,γ)35Cl", "26Mg(α,nγ)29Si"]
models: ["Rose-Brink-formalism"]
observables: ["angular-distribution-coefficient", "multipole-mixing-ratio", "finite-counter-attenuation", "particle-gamma-correlation"]
methods: ["angular-distribution", "multipole-mixing-ratio", "particle-gamma-angular-correlation"]
tags: [particle-gamma-correlation, Method-II, angular-distribution, mixing-ratio, finite-counter-size]
---

# Analysis of particle-gamma angular correlations and distributions

## Bibliographic Record

- 作者：P. Taras。
- 期刊：*Nuclear Instruments and Methods* 85, 313-323 (1970)。DOI：`10.1016/0029-554X(70)90251-X`。
- 原始文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/ADO/1970_Taras_Analysis of particle-gamma angular correlations and distributions.pdf`；SHA-256：`1bd0ec877718f6cd98ae087ebbc78409694be407b1a66ff778488997a56a8813`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: PDF pp.313-323 全文；general angular-distribution equations, s=1/2 population restriction, dipole-quadrupole/quadrupole-octupole curves, Table 1 isotropy δ values, `34S(p,γ)35Cl` example, Method II Litherland-Ferguson, finite particle-counter correction `T_k(J)`, Table 2 and plotted curves。
- Not covered: cited Rose-Brink/Sharp coefficient tables and raw experimental spectra。
- Coverage caveats: plots are theoretical point-detector curves; real γ/particle counter solid-angle corrections must be applied before comparison。

## Paper Question and Scientific Motivation

- 论文为 particle-gamma capture 和 Litherland-Ferguson Method II 提供可直接查用的 angular-distribution curves，用于约束 spin sequence 和 mixing ratio，而不是每个实验都重新执行完整 symbolic derivation（摘要；PDF pp.313-314）。

## Method and Design Logic

- Starting from `W(θ)=W_LL+2δW_LL′+δ²W_L′L′`, the paper computes `a_k/a_0` for dipole-quadrupole and quadrupole-octupole mixtures using Rose-Brink statistical tensors and Z coefficients。
- For entrance channel spin `s=1/2`, only `m=±1/2` substates are populated and tensors are uniquely defined; this supports `26Mg(α,nγ)29Si`-type Method II curves。
- Finite particle-counter size is represented by `T_k(J)` coefficients; values decline rapidly with initial spin, making the correction less important at higher spin (PDF pp.314-316，Table 2)。

## Key Evidence and Reasoning Chain

1. 24 theoretical curves cover selected `J=3/2` through `9/2` initial states and `I=1/2` through `7/2` final states, with allowed δ ranges and isotropic δ values listed in Table 1（PDF pp.314-323）。
2. In `34S(p,γ)35Cl`, measured `a2/a0≈0.17` and `a4/a0≈−0.005` for a 7.84-MeV level are compared to curves; for a possible `J=3/2` final state, δ branches include approximately `0.13-0.19` and `−14.3 to −8.1`（PDF p.315，Fig.1A）。
3. Method II is most useful when reaction geometry restricts magnetic substates to `m=±1/2` (or `m=0`); otherwise population parameters are not unique and the curves require correction or a fit with additional information（PDF pp.315-316）。
4. Finite particle-counter corrections `T_k(J)` are largest at low spin and decrease with J; both uncorrected and corrected values should be reported when the reaction mechanism is uncertain（PDF p.316，Table 2）。

## Summary

Taras provides a practical library of particle-gamma angular-correlation curves and explicit limits for using them to extract δ and spin. The method is strongest when entrance-channel spin and magnetic-substate population are restricted; finite counter size, solid-angle attenuation and multiple δ branches remain essential boundaries. The source complements Taras 1971's phase-defined polarization formalism and gives an early quantitative warning against treating a small set of angular coefficients as a unique assignment.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| T70-1 | s=1/2 entrance reactions uniquely define the `m=±1/2` statistical tensors used in the theoretical Method II curves. | method-condition | direct | PDF pp.313-315，式 (1)-(5) | false |
| T70-2 | Theoretical curves provide allowed δ ranges and isotropic values for many spin sequences; multiple branches can occur. | method-result/limitation | direct | PDF p.314，Table 1，Figs.1-13 | false |
| T70-3 | Finite particle-counter correction `T_k(J)` decreases rapidly with initial spin and must be considered when particle acceptance is not point-like. | method-limitation | direct | PDF pp.315-316，Eq.(7)，Table 2 | false |
| T70-4 | The `34S(p,γ)35Cl` example shows angular-distribution coefficients can leave widely separated δ branches for one spin sequence. | experimental-example | direct | PDF p.315，Fig.1A | true |

## Nuclear Structure Information

- `35Cl` and `29Si` are method examples only; no standalone nuclear structure page is created。

## Competing Interpretations and Limitations

- Isotropic angular distributions may arise from many spin sequences at special δ values; isotropy is not evidence of a unique spin or zero alignment。
- Point-detector theory curves require γ detector solid-angle attenuation and particle-counter finite-size corrections before experimental use。
- If reaction mechanism is unknown, higher magnetic substates may be populated and the s=1/2 Method II assumption fails。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-T70-1 | Core reconstruction | The value is a reusable curve library plus a clear population/geometry validity test, not a universal δ lookup table. | PDF §§2-5 | self-checking |
| AR-T70-2 | Assumptions and dependencies | Depends on spin/parity, entrance-channel s, magnetic-substate population, detector attenuation and finite particle-counter response. | PDF pp.313-316 | self-checking |
| AR-T70-3 | Transfer conditions | Curves can guide comparable s=1/2 reactions; arbitrary fusion-evaporation or unknown feeding needs a new population calculation. | PDF pp.314-316 | provisional |
| AR-T70-4 | Failure conditions | Ignoring finite counter correction or selecting one δ branch from one coefficient can produce false spin/multipolarity assignments. | PDF pp.315-316 | active-L3 |
| AR-T70-5 | Reverse/falsification test | Compare both δ branches with linear polarization, ICC or independent DCO/known transitions; vary counter acceptance and population model. | PDF pp.315-316 | candidate-L3 |
| AR-T70-6 | Research-question decision | Add to angular-distribution/mixing-ratio method lineage; no L4. | PDF pp.313-323 | completed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Existing angular-distribution and `σ/I` pages record multi-solution and alignment limits; this source supplies the classic Method II curve and finite-particle-counter correction lineage.
- Effect of this source: `foundational-background` and `methodological-bridge`。
- Reason: It tightens the conditions under which ADO/DCO-style angular information can constrain δ and spin.
- Persistence decision: update [[angular-distribution]] and [[multipole-mixing-ratio]] source lists。
- Review state: `unreviewed`; method claims self-audited by Codex, not human-reviewed。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| foundational-background | [[angular-distribution]] | Theoretical curves, attenuation and finite-particle-counter correction。 |
| methodological-bridge | [[multipole-mixing-ratio]] | Multiple δ branches and phase-consistent branch testing。 |
| supports | [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]] | Population/alignment assumptions affect δ extraction and uncertainty。 |

## Human Review Triage

### P0

- T70-P0-1：Method II curves require the stated reaction population condition; do not apply s=1/2 `m=±1/2` curves to arbitrary data。

### P1

- T70-P1-1：A single angular-distribution coefficient or isotropy point cannot choose a unique δ/spin branch。

### P2/P3

- DOI, volume and pages are aligned from PDF PII; no nucleus page created。

## Extracted Pages

- Nuclei: none。
- Bands: none。
- Concepts: population/alignment, finite-counter attenuation, Method II。
- Methods: [[angular-distribution]], [[multipole-mixing-ratio]]。

## Non-source Notes and Follow-up

- Next: compare T70 curves with HS-002 ADO and HS-011 phase-defined δ formalism; continue HS-015.
