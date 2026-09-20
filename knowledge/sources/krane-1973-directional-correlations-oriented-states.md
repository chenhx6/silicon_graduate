---
type: source
title: "Krane, Steffen & Wheeler 1973 - Directional correlations of gamma radiations emitted from oriented nuclear states"
aliases: [Krane Steffen Wheeler 1973 DCO review]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: method-review
reading_depth: deep-read
title_original: "Directional correlations of gamma radiations emitted from nuclear states oriented by nuclear reactions or cryogenic methods"
authors: [K. S. Krane, R. M. Steffen, R. M. Wheeler]
journal: "Nuclear Data Tables"
year: 1973
volume: 11
pages: "351-406"
pii: "S0092-640X(73)80016-6"
canonical_source: "Krane, Steffen & Wheeler, Nucl. Data Tables 11, 351-406 (1973)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/DCO/1973_Krane et al_Directional correlations of gamma radiations emitted from nuclear states.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/DCO/1973_Krane et al_Directional correlations of gamma radiations emitted from nuclear states.pdf"
raw_sha256: "66f9b04ad093223c648036063e3e9631317660b532b2b77681089d9d79853848"
nuclei: [oriented-nuclei]
reactions: [Coulomb-excitation, heavy-ion-reaction, cryogenic-orientation]
experiments: []
models: [angular-correlation-formalism, statistical-tensor-orientation]
observables: [DCO, angular-correlation, multipole-mixing-ratio, nuclear-alignment]
methods: [DCO-ratio, angular-distribution, statistical-tensor]
tags: [DCO, angular-correlation, alignment, orientation, mixing-ratio, method-review]
---

# Directional correlations from oriented nuclear states

## Bibliographic Record

- K. S. Krane, R. M. Steffen and R. M. Wheeler, *Nuclear Data Tables* **11**, 351–406 (1973), PII `S0092-640X(73)80016-6`。
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/DCO/1973_Krane et al_Directional correlations of gamma radiations emitted from nuclear states.pdf`。
- 56-page method review with generalized F-coefficient tables and practical detector geometries.

## Scope and Reading Depth

- Full text read: orientation parameters, generalized DCO function, normal/parallel/unrestricted geometries, generalized F coefficients, sample calculation, numerical tables and sensitivity to δ.
- Not covered: reanalysis of every table entry or modern array-specific implementations.

## Key Results

- Oriented-state populations `P(m)` are represented by statistical-tensor orientation parameters `B_k`; DCO distributions combine orientation, radiation coefficients and geometry tensors.
- Mixed multipoles enter through explicit reduced-matrix-element conventions and δ; the review emphasizes phase/order conventions and odd-rank terms for polarized/oriented states.
- Ordinary directional correlations are recovered when initial state is random or one radiation is unobserved; DCO from oriented states is a more general object than a gate ratio.
- Tables of generalized F coefficients and normal detector geometries make the formalism calculable, but finite solid angle, alignment and reaction mechanism remain experiment-specific.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KSW73-1 | Generalized DCO function factorizes orientation parameters, radiation coefficients and geometry tensors. | formalism | direct | PDF pp.353–360, Eq.(10) | false |
| KSW73-2 | Mixed-multipole δ enters orientation parameters through explicit reduced-matrix-element/phase conventions. | formalism | direct | PDF pp.353–360, Eqs.(4–8) | true |
| KSW73-3 | Tables of F/geometrical coefficients enable practical DCO calculations across normal/parallel detector geometries. | method-result | direct | PDF pp.360–406, Tables | true |

## Summary

This review is the foundational generalized DCO reference: it separates nuclear orientation/alignment from detector geometry and multipole conventions, preventing a modern DCO ratio from being treated as a universal scalar.

## Competing Interpretations and Limitations

Orientation depends on reaction/cryogenic mechanism and feeding; odd-rank terms, finite solid angle and phase conventions can matter. A gate ratio such as `R_ac` or DCO is a compressed observable whose interpretation requires the underlying geometry and assumed transition.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| KSW73-AR-1 | Formal chain | `P(m)`/`B_k` → generalized F/radiation coefficients → geometry → DCO distribution/ratio. | PDF Eqs.1–27 | self-checking |
| KSW73-AR-2 | Transfer condition | Use matching orientation, detector geometry, multipole order and phase convention; no universal DCO threshold. | PDF Chs.III–V | active-L3 |
| KSW73-AR-3 | Independence | Method review; tabulated coefficients are not experiments. | Scope/Refs. | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[angular-correlation]], [[angular-distribution]], [[two-point-angular-correlation-ratio]] and [[multipole-mixing-ratio]].
- Persistence: update DCO/angle method map with generalized orientation/geometry boundary.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `KSW73-P0-1`: map DCO/R_ac to the full orientation and geometry formalism before cross-experiment comparison.

## Extracted Pages

- Methods: [[angular-correlation]], [[angular-distribution]], [[two-point-angular-correlation-ratio]]。
