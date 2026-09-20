---
type: source
title: "Rose and Brink 1967 - Angular distributions in phase-defined reduced matrix elements"
aliases: [Rose-Brink 1967 angular distributions]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: theory-method-review
reading_depth: deep-read
title_original: "Angular Distributions of Gamma Rays in Terms of Phase-Defined Reduced Matrix Elements"
authors: [H. J. Rose, D. M. Brink]
journal: "Reviews of Modern Physics"
year: 1967
volume: 39
pages: "306-347"
doi: "10.1103/RevModPhys.39.306"
canonical_source: "Rose & Brink, Rev. Mod. Phys. 39, 306-347 (1967)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1967_Rose et al_Angular Distributions of Gamma Rays in Terms of Phase-Defined Reduced Matrix Elements.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1967_Rose et al_Angular Distributions of Gamma Rays in Terms of Phase-Defined Reduced Matrix Elements.pdf"
raw_sha256: "8f846b61b9320de291ee5600126c5e286a0fe05968df819696816f0dc1ec57dc"
nuclei: [generic]
reactions: [generic-alignment-population]
experiments: [gamma-angular-distribution, gamma-gamma-correlation]
models: [Wigner-Eckart, statistical-tensor, multipole-expansion]
observables: [angular-distribution, gamma-width, mixing-ratio, alignment, polarization]
methods: [phase-defined-multipole-formalism, gamma-gamma-correlation]
tags: [Rose-Brink, angular-distribution, phase-convention, mixing-ratio, alignment]
---

# Angular distributions in phase-defined reduced matrix elements

## Bibliographic Record

- H. J. Rose & D. M. Brink, *Rev. Mod. Phys.* **39**, 306–347 (1967), DOI `10.1103/RevModPhys.39.306`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1967_Rose et al_Angular Distributions of Gamma Rays in Terms of Phase-Defined Reduced Matrix Elements.pdf`。

## Scope and Reading Depth

- PDF pp.306–347 (42 pages) fully read: perturbative emission/absorption starting point, time reversal, spherical-tensor phases, electric/magnetic multipole expansion, aligned-state angular distribution, widths, mixing ratios, alignment-production cases, reduced matrix elements, comments and Appendix coefficient tables.
- Not covered: later software implementations and numerical coefficient tables beyond the printed appendix.

## Key Results

- The derivation starts from first-order perturbation theory and detailed balance/time reversal, then expands a transverse electromagnetic field into electric and magnetic multipoles with explicitly defined phases (PDF pp.306–315, Eqs.2.1–3.23).
- Interaction multipole operators `T^L_M(λ)` are chosen to share consistent rotation, Hermitian-conjugation and time-reversal properties. This makes reduced matrix elements real under the stated phase convention and gives a reproducible sign for mixed-multipole amplitudes (PDF pp.315–317, Eqs.3.17–3.24).
- For a cylindrically aligned initial state, the angular distribution is expressed as a sum of Legendre polynomials weighted by statistical tensors `B_K(J_i)`, geometry coefficients `R_K(LL'J_iJ_f)` and products of reduced matrix elements (PDF pp.316–318, Eqs.3.25–3.37).
- The mixing ratio is defined as a ratio of phase-defined reduced matrix elements of the lowest-order competing multipoles (Eq.3.39). Its magnitude is related to the square root of partial γ widths, but its sign is a physical relative phase only within the common operator/state convention (PDF pp.318–320).
- For unpolarized γ detection and states of definite parity, odd-rank terms cancel and the usual even-`K` angular-distribution form results (PDF pp.320–324, Eqs.3.40–3.47). If the initial state is polarized or has mixed parity, odd-rank/interference terms require the more general formula.
- The paper treats alignment from resonant capture, particle–particle reactions and γ cascades. A γ–γ angular correlation is a product of a population tensor from the first transition and a response tensor from the second; Eq.3.73 exposes the relative phase factor for the two mixing ratios (PDF pp.321–326, Eqs.3.51–3.73).
- The authors provide single-particle, two-particle and hole reduced-matrix-element formulas and warn that switching the order of initial/final states or using effective/Siegert operators without phase mapping changes the apparent δ sign (PDF pp.327–336, Secs.IV–V).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| RB67-1 | A phase-defined interaction-multipole convention makes the sign of a mixing ratio comparable between measurement and model only after operator and state-order mapping. | formalism-result | direct | PDF pp.306–320, Eqs.3.17–3.39 | true |
| RB67-2 | Aligned-state γ angular distributions factor into population/alignment tensors, geometry coefficients and reduced transition amplitudes. | formalism-result | direct | PDF pp.316–324, Eqs.3.25–3.47 | false |
| RB67-3 | γ–γ correlations require the population tensor of the first transition and the response tensor of the second; mixed multipoles carry a convention-dependent relative phase. | formalism-result | direct | PDF pp.321–326, Eq.3.73 | true |
| RB67-4 | The compact even-`K` formula is not valid without its definite-parity/alignment assumptions. | limitation | direct | PDF pp.320–326 | false |

## Summary

Rose and Brink supply the phase-consistent foundation that lets angular distributions, γ–γ correlations and model electromagnetic matrix elements use a common mixing-ratio sign. The practical message is to define the interaction operators, state order, time-reversal phases, alignment tensor and convention together before comparing δ values.

## Competing Interpretations and Limitations

- Rose–Brink, Biedenharn and later experimental conventions may differ in operator phase and initial/final state order; numerical δ signs cannot be merged by magnitude-only comparison.
- The standard even-`K` angular-distribution expression assumes cylindrical alignment, definite parity and the stated polarization summation. Particle-reaction or mixed-parity cases require the general tensor expression.
- Effective electric operators from Siegert's theorem are equivalent only with the continuity/gauge assumptions discussed by the authors; replacing the interaction operator silently can alter phase interpretation.
- Model reduced matrix elements depend on wave functions, effective charges/g factors and particle/hole phase conventions; the formalism does not make a model assignment unique.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| RB67-AR-1 | Formal chain | Perturbation theory → multipole operators → Wigner–Eckart reduction → aligned-state tensor distribution → fitted mixing ratio. | PDF Eqs.2.1–3.47 | self-checking |
| RB67-AR-2 | Cascade chain | First γ transition creates `B_K(J)` population tensor; second transition contributes `R_K` and δ; product gives γ–γ correlation. | PDF Eqs.3.65–3.73 | self-checking |
| RB67-AR-3 | Convention transfer | Convert operator phase, state order, parity and alignment assumptions before comparing Hamilton/Taras/DCO values. | PDF pp.318–327, 335–336 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[angular-distribution]], [[angular-correlation]], [[multipole-mixing-ratio]], [[taras-1971-phase-defined-polarization-formulas]] and the convention audit for Hamilton 1969.
- New reusable rule: every stored δ claim must retain the source convention and state order; a sign disagreement is not a scientific conflict until the phase map is closed.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `RB67-P0-1`: Do not compare or average δ signs across source pages until Rose–Brink/Biedenharn/operator/state-order conventions are explicitly mapped.

## Extracted Pages

- Methods/observables: [[angular-distribution]], [[angular-correlation]], [[multipole-mixing-ratio]]。
