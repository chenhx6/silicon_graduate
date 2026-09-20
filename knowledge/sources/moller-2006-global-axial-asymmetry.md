---
type: source
title: "Möller et al. 2006 - Global Calculations of Ground-State Axial Shape Asymmetry of Nuclei"
aliases: [Moller 2006 global triaxial ground states]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: journal-article-theory
reading_depth: deep-read
title_original: "Global Calculations of Ground-State Axial Shape Asymmetry of Nuclei"
authors: [Peter Möller, Ragnar Bengtsson, B. Gillis Carlsson, Peter Olivius, Takatoshi Ichikawa]
journal: "Physical Review Letters"
year: 2006
volume: 97
article: 162502
pages: "1-4"
doi: "10.1103/PhysRevLett.97.162502"
canonical_source: "https://doi.org/10.1103/PhysRevLett.97.162502"
library_file: "raw/papers/gpt/high-spin-20260920/形变/2006_Möller et al_Global Calculations of Ground-State Axial Shape Asymmetry of Nuclei.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/形变/2006_Möller et al_Global Calculations of Ground-State Axial Shape Asymmetry of Nuclei.pdf"
raw_sha256: "6f56615cf523369591820f4abac6cece7ce3adee02dd33763346d1dc5fff4ebc"
nuclei: [108Ru, 140Gd, 194Pt]
reactions: []
experiments: []
models: [finite-range-liquid-drop-model, macroscopic-microscopic-PES]
observables: [ground-state-shape, triaxiality, gamma-band, nuclear-mass]
methods: [global-PES-calculation]
tags: [triaxiality, ground-state, global-model, gamma-band, mass-model]
---

# Global Calculations of Ground-State Axial Shape Asymmetry of Nuclei

## Bibliographic Record

- Peter Möller *et al.*, *Physical Review Letters* **97**, 162502 (2006), DOI `10.1103/PhysRevLett.97.162502`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/形变/2006_Möller et al_Global Calculations of Ground-State Axial Shape Asymmetry of Nuclei.pdf`。
- 4-page PRL; global calculation, no new experiment.

## Scope and Reading Depth

- Full PDF pp.1–4 read: FRLDM shape parametrization/grid, 7206-nucleus calculation, axial-asymmetry energy map, 108Ru/140Gd/194Pt spectra, mass residual correction and conclusion.
- Not covered: full FRLDM code and modern global recalculations.

## Key Results

- Global 3D PES calculations over 7206 nuclei (`A=31–290`) predict non-negligible ground-state axial asymmetry in regions around `Z≈44,N≈64` and `Z≈62,N≈76`, with smaller effects near Pt.
- Characteristic γ bands are proposed as a necessary experimental companion where axial asymmetry is calculated; `108Ru`, `140Gd`, `194Pt` examples show such bands.
- Including axial-asymmetry energy corrections lowers systematic mass residuals for affected nuclei by ~76.5% in mean deviation, but the model omits zero-point-energy effects in the plotted correction.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MO06-1 | FRLDM global PES predicts ground-state axial asymmetry in selected Z/N regions. | model-result | direct | PDF pp.1–3, Figs.1–2 | true |
| MO06-2 | Calculated axial asymmetry correlates with observed γ bands, treated as a necessary condition rather than a full proof. | model-data-comparison | mixed | PDF pp.1–3, Fig.2 | true |
| MO06-3 | Axial-asymmetry corrections reduce systematic mass-model residuals for affected nuclei. | model-result | direct | PDF p.3, Fig.3 | true |

## Summary

Möller *et al.* provide a global macroscopic–microscopic benchmark linking ground-state triaxial minima, γ bands and mass residuals; the calculated γ parameter is not a direct experimental shape measurement.

## Competing Interpretations and Limitations

Zero-point motion, γ softness, functional/PES parameterization and omitted beyond-mean-field corrections can change minima. γ bands are a necessary companion signal in the authors' logic, not sufficient proof of a rigid triaxial ground state.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| MO06-AR-1 | Model chain | FRLDM 3D PES → axial-asymmetry energy correction → γ-band/mass comparison. | PDF pp.1–4 | self-checking |
| MO06-AR-2 | Transfer condition | Use model γ only with matching observable and zero-point assumptions; no universal triaxial threshold. | PDF pp.2–4 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[triaxial-deformation]], [[gamma-soft-deformation]] and cross-mass γ-band comparator.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `MO06-P0-1`: global model minima and γ-band companion evidence do not directly establish rigid triaxial deformation.

## Extracted Pages

- Concepts: [[triaxial-deformation]], [[gamma-soft-deformation]]。
