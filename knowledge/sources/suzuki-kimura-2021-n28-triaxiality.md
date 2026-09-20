---
type: source
title: "Suzuki & Kimura 2021 - Triaxial deformation and the loss of the N=28 shell gap"
aliases: [Suzuki Kimura 2021 N28 triaxiality]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: arxiv-theory
reading_depth: deep-read
title_original: "Triaxial deformation and the loss of the N=28 shell gap"
authors: [Y. Suzuki, M. Kimura]
journal: "arXiv:2103.06086v1"
year: 2021
pages: "1-18"
arxiv: "2103.06086v1"
canonical_source: "https://arxiv.org/abs/2103.06086"
library_file: "raw/papers/gpt/high-spin-20260920/形变/2021_Suzuki_Kimura_Triaxial deformation and the disappearance of the N = 28 shell gap.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/形变/2021_Suzuki_Kimura_Triaxial deformation and the disappearance of the N = 28 shell gap.pdf"
raw_sha256: "7719016e6ae01cbf5b70f4128420c9802d3f4b6054150baad0c443d43b813423"
nuclei: [38Mg, 40Mg, 42Si, 44S, 46S, 48Ar]
reactions: []
experiments: []
models: [antisymmetrized-molecular-dynamics, Gogny-D1S, angular-momentum-projection, GCM]
observables: [triaxial-deformation, N28-shell-gap, E2, interband-transition]
methods: [constraint-variation, angular-momentum-projection, generator-coordinate]
tags: [N28, shell-evolution, triaxiality, AMD, GCM, exotic-nuclei]
---

# Triaxial deformation and the loss of the N=28 shell gap

## Bibliographic Record

- Y. Suzuki and M. Kimura, arXiv:2103.06086v1 (2021), 18 pp.
- 规范文件：`raw/papers/gpt/high-spin-20260920/形变/2021_Suzuki_Kimura_Triaxial deformation and the disappearance of the N = 28 shell gap.pdf`。

## Scope and Reading Depth

- Full PDF read: AMD Gogny-D1S Hamiltonian, parity/AM projection, β–γ constrained mesh, GCM Hill–Wheeler, N=26/28/30 isotones, shell occupations, spectra, E2/interband transitions and conclusions.
- Not covered: code, parameter files and later arXiv versions.

## Key Results

- N=26,28,30 isotones near `42Si` show deformed and often γ-soft/triaxial projected ground states; N=28 magicity erodes gradually without a sharp boundary.
- Angular-momentum projection changes axial intrinsic minima into triaxial projected minima; `N=26/30` isotones have non-yrast `K=2+` bands.
- Interband electric transitions are proposed as probes of triaxial deformation; occupation/shell effects, proton-neutron interplay and oblate/prolate tendencies vary across Mg/Si/S/Ar.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SK21-1 | AMD+GCM predicts triaxial/soft projected ground states across N=26–30 isotones and gradual N=28 shell-gap erosion. | model-result | direct | PDF pp.5–15, Figs.1–8 | true |
| SK21-2 | Interband E2 strengths are proposed as diagnostics of triaxial deformation and shell-evolution patterns. | model-prediction | direct | PDF results/conclusion | true |
| SK21-3 | Magicity loss has no definite proton/neutron-number boundary and need not involve single-particle level inversion in oblate `42Si`. | model-interpretation | direct | Abstract/conclusion | true |

## Summary

Suzuki & Kimura provide a projected AMD/GCM theory map linking N=28 shell erosion to triaxial/γ-soft deformation near `42Si`; all deformation and transition predictions are model outputs pending experimental comparison.

## Competing Interpretations and Limitations

Gogny-D1S, AMD basis, constraint mesh, GCM truncation and projection prescriptions affect minima and transition strengths; no direct experimental data or reproducible code are supplied.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| SK21-AR-1 | Model chain | constrained AMD → parity/AM projection → GCM mixing → spectra/E2/occupation. | PDF Eqs.1–15, Figs.1–10 | self-checking |
| SK21-AR-2 | Transfer condition | Use as theory comparator only with stated Gogny/AMD/GCM assumptions; interband E2 is a prediction, not measurement. | PDF conclusions | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[triaxial-deformation]] and shell-evolution model layer; provides a non-A≈130 comparison for the high-spin map.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `SK21-P0-1`: do not treat AMD/GCM β/γ minima or E2 predictions as direct experimental shape measurements.

## Extracted Pages

- Concepts: [[triaxial-deformation]], [[gamma-soft-deformation]]。
- Models: [[triaxial-projected-shell-model]] (methodological comparison only).
