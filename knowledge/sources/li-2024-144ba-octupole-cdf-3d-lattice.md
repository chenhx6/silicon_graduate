---
type: source
title: "Li & Wang 2024 - Robustness of the octupole collectivity in 144Ba"
aliases: [Li 2024 144Ba octupole, cranking CDFT 3D lattice 144Ba]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: theory-paper
reading_depth: deep-read
title_original: "Robustness of the octupole collectivity in 144Ba within the cranking covariant density functional theory in 3D lattice"
authors: [Ze-Kai Li, Yuan-Yuan Wang]
journal: "Nuclear Science and Techniques"
year: 2024
volume: 35
article: 139
pages: "1-8"
doi: "10.1007/s41365-024-01532-z"
canonical_source: "https://doi.org/10.1007/s41365-024-01532-z"
library_file: "raw/papers/gpt/high-spin-20260920/形变/2024_Li et al_Robustness of the octupole collectivity in $${^{144}textrm{Ba}}$$ within the cranking covariant den.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/形变/2024_Li et al_Robustness of the octupole collectivity in $${^{144}textrm{Ba}}$$ within the cranking covariant den.pdf"
raw_sha256: "294e1cc6ae9543ab3c6474d47ff91937be220f4cea3332b3a65897fd29f92155"
nuclei: [144Ba]
reactions: []
experiments: []
models: [covariant-density-functional-theory, cranking-covariant-density-functional-theory]
observables: [potential-energy-surface, rotational-frequency, angular-momentum, B(E2), B(E3), beta20, beta30, single-particle-routhian]
methods: [3d-lattice-cranking, semiclassical-transition-probability]
tags: [octupole, reflection-asymmetry, 144Ba, CDFT, high-spin, theory]
---

# Robustness of the octupole collectivity in 144Ba within cranking CDFT in 3D lattice

## Bibliographic Record

- Ze-Kai Li and Yuan-Yuan Wang, *Nuclear Science and Techniques* **35**, 139 (2024), pp.1–8; DOI `10.1007/s41365-024-01532-z`。
- 规范文件：`raw/papers/gpt/high-spin-20260920/形变/2024_Li et al_Robustness of the octupole collectivity in $${^{144}textrm{Ba}}$$ within the cranking covariant den.pdf`。
- PDF identity: title page, author list, journal/article number and DOI agree; 8-page selectable-text PDF, hash recorded above. The filename's TeX-like isotope string is a filename artifact, not a second title/version.

## Scope and Reading Depth

- Completed `reading_depth: deep-read`: PDF pp.1–8, including the abstract, introduction, effective Lagrangian Eq.(1), cranking Dirac Eqs.(2–3), multipole moments Eqs.(4–11), semiclassical `B(E2)`/`B(E3)` Eqs.(12–13), PES Fig.1, `I–ω` Fig.2, transition probabilities Fig.3, deformation evolution Fig.4, proton/neutron Routhians Fig.5, summary, data-availability statement and references.
- Figure/table audit: all five numbered figures were checked against their captions and surrounding discussion; no tables or supplementary files are supplied with this PDF.
- Not covered: the public Science Data Bank files named in the data-availability statement were not downloaded in this source-level pass; no event-level experiment or CDFT source code is supplied.

## Paper Question and Scientific Motivation

The paper asks whether a fully self-consistent cranking covariant density-functional calculation on a three-dimensional lattice can describe the observed rotational spectrum and electromagnetic collectivity of the octupole double-magic nucleus `144Ba`, and whether the reflection-asymmetric shape survives rotation to high spin.

## Method and Design Logic

1. Start from a point-coupling covariant Lagrangian and solve the cranking Dirac equation `h' = h0 − ω·J` self-consistently on a 3D lattice without imposing spatial reflection or axial symmetries (PDF pp.2–3, Eqs.1–3).
2. Obtain proton quadrupole/octupole moments `Q2μ` and `Q3μ`, convert them to deformation parameters with Eq.(11), and use the intrinsic angular-momentum direction `(θ,φ)` to derive semiclassical `B(E2)` and `B(E3)` (PDF p.3, Eqs.4–13).
3. Compare the calculated `I–ω`, `B(E2)` and `B(E3)` with the available `144Ba` data, then inspect constrained PES and single-particle Routhians for the mechanism stabilizing the octupole minimum (PDF pp.3–5, Figs.1–5).

## Key Evidence and Reasoning Chain

- The PC-PK1 constrained PES has a global minimum at `(β20, β30)=(0.22, 0.13)`; the lowest reflection-symmetric point is within `<1 MeV`, and a secondary minimum appears near `(-0.15, 0.05)` at about `3 MeV` (PDF p.3–4, Fig.1). This is a model PES, not a direct shape image.
- The calculated `I–ω` curve slightly overestimates the measured angular momentum, indicating an excessive moment of inertia; the authors identify omitted pairing as the expected correction (PDF p.4, Fig.2).
- `B(E2)` is nearly constant over the plotted spin range and agrees in order of magnitude with the available data. `B(E3)` is reproduced by the semiclassical expression built from microscopic octupole moments (PDF p.4, Fig.3). The figures provide curves and points but no machine-readable table in the supplied PDF.
- The self-consistent yrast solution keeps `β20` near `0.22→0.20`; `β30` changes only slightly, with an average `β30≈0.128` up to `ℏω=0.45 MeV` (`I≈24ℏ`) (PDF p.4–5, Fig.4).
- Proton and neutron Routhians retain gaps associated with `Z=56` and `N=88` near the Fermi surfaces; the authors interpret these gaps as the microscopic reason for the octupole minimum and its rotational robustness (PDF p.5, Fig.5). This is an author/model interpretation, not an independently measured shell gap in the rotating nucleus.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LI24-1 | PC-PK1 3D-lattice constrained CDFT gives a reflection-asymmetric minimum near `β20=0.22, β30=0.13` for `144Ba`. | model-result | direct | PDF pp.3–4, Fig.1 | true |
| LI24-2 | The calculated `I–ω`, `B(E2)` and `B(E3)` curves reproduce the available data at the level shown in Figs.2–3. | model-data-comparison | direct | PDF p.4, Figs.2–3 | true |
| LI24-3 | The yrast solution has nearly unchanged quadrupole deformation and average `β30≈0.128` through `I≈24ℏ`. | model-result | direct | PDF pp.4–5, Fig.4; Summary | true |
| LI24-4 | `Z=56` proton and `N=88` neutron Routhian gaps are proposed as the mechanism stabilizing octupole collectivity against rotation. | author-interpretation/model-result | indirect | PDF p.5, Fig.5 | true |
| LI24-5 | The calculation neglects pairing, treats total angular momentum semiclassically and cannot calculate parity splitting/interleaved-band parity quantum numbers. | limitation | direct | PDF p.6, final paragraph | false |

## Summary

The PC-PK1 3D-lattice cranking calculation reproduces the plotted `144Ba` rotational and electromagnetic systematics and keeps a nonzero octupole mean-field deformation to `I≈24ℏ`. Pairing and parity projection are omitted, so the result is a constrained model benchmark rather than a quantum proof of alternating-parity bands.

## Experimental or Theoretical Setup

- Functional and mesh: PC-PK1 point-coupling CDFT; 3D lattice step `1 fm`, 30 grid points on each axis. Iteration criteria are occupied-state energy uncertainty `<10⁻9 MeV²` and adjacent-potential difference `<10⁻3 MeV` (PDF p.3).
- Constrained PES: `β20∈[−0.3,0.4]`, `β30∈[0,0.3]`, step `0.05`; cranking frequencies `ω=0–0.45 MeV` (PDF p.3).
- The model is reflection-unrestricted and self-consistent in the lattice, but pairing is omitted. The semiclassical transition formulas also require an intrinsic angular-momentum orientation and do not constitute a projected quantum spectrum.

## Authors' Interpretation vs Agent Reconstruction

- **Direct/model output:** moment fields, deformations, Routhians, `I–ω`, `B(E2)` and `B(E3)` curves reported by the calculation (Figs.1–5).
- **Author interpretation:** persistent octupole shape is driven by the `Z=56`/`N=88` gaps and is robust to rotation up to `I≈24ℏ`.
- **Agent reconstruction:** agreement of several observables is useful evidence for the calculation's consistency, but the omitted pairing and lack of parity projection leave the parity-doublet splitting and quantum alternating-parity spectrum untested. The `β30` value is a mean-field order parameter, not a model-independent experimental measurement.

## Competing Interpretations and Limitations

- The PES is soft around the minimum; a shallow reflection-symmetric competitor means a static minimum and strong octupole correlations should not be conflated.
- Pairing can reduce the moment of inertia and alter deformation/Routhian evolution; the paper explicitly flags this missing physics.
- Because total angular momentum and parity are treated semiclassically, the calculation cannot resolve the parity splitting of interleaved positive/negative bands. A parity-projected or beyond-mean-field calculation is required for that question.
- The available data comparison is inherited from Ref.14 and related spectroscopy sources; this paper does not remeasure `144Ba` and the plotted points should not be counted as an independent experiment.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| LI24-AR-1 | Identity and scope | Title-page identity, DOI and all eight pages agree; no SI is attached. | PDF pp.1–8 | self-checking |
| LI24-AR-2 | Equation/observable chain | Eqs.1–3 define the rotating CDFT; Eqs.4–11 define moments/deformations; Eqs.12–13 map them to semiclassical transition probabilities. | PDF pp.2–3 | self-checking |
| LI24-AR-3 | Transfer condition | `β30≈0.128` can be reused only as a PC-PK1, unpaired, 3D-cranking model result at the stated spin range. | PDF pp.3–6 | provisional |
| LI24-AR-4 | Failure condition | Pairing, parity projection, quantum angular-momentum restoration or a different functional could change the predicted deformation and parity splitting. | PDF p.6 | active-L3 |
| LI24-AR-5 | L4 readiness | Data availability names a public repository, but the PDF alone lacks the machine-readable data, code, parameter manifest and uncertainty model required for reproducible L4. | PDF p.6 | candidate-L4 / not-ready |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: octupole correlation, softness and stable octupole deformation are already separated; CDFT/TAC pages contain model-boundary rules but no `144Ba` rotating 3D-lattice example.
- Effect of this source: `supports` the distinction between a self-consistent static octupole minimum and a quantum parity-doublet claim; `extends` the CDFT model map to `A≈150` high-spin rotation.
- Persistence decision: update the octupole deformation/correlation/softness pages, CDFT and rotating-mean-field model pages, and add this source to the high-spin project map. Preserve `LI24-5` as an explicit limitation.
- Review state: Codex self-audited; not `human-reviewed`.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[octupole-deformation]] | A direct example of a nonzero mean-field `β30` minimum, with the static-order-parameter boundary preserved. |
| supports | [[octupole-softness]] | Fig.1's shallow neighborhood shows why a minimum and softness must be reported separately. |
| methodological-bridge | [[covariant-density-functional-theory]] | PC-PK1 3D-lattice cranking implementation and self-consistent multipole moments. |
| methodological-bridge | [[rotating-mean-field]] | Routhian `h−ω·J`, intrinsic deformation evolution and semiclassical observable mapping. |
| candidate-L3 | [[a130-high-spin-collective-modes-evidence-map]] | Cross-mass comparison of parity-sensitive observables versus mean-field octupole robustness. |

## Human Review Triage

### P0

- `LI24-P0-1`: do not quote `β30≈0.128` or the `Z=56/N=88` mechanism as direct experimental facts; both are model outputs/interpretations, and pairing/parity projection are omitted.

### P1

- `LI24-P1-1`: the data-availability repository is named but not yet ingested; any L4 reuse requires a hashable dataset, units, point-to-figure mapping, and an uncertainty/rounding policy.
- `LI24-P1-2`: the experimental points in Figs.2–3 derive from cited prior work and are not independent observations in this source.

## Extracted Pages

- Concepts: [[octupole-deformation]], [[octupole-correlation]], [[octupole-softness]], [[reflection-asymmetric-nuclei]], [[rotating-mean-field]]。
- Models: [[covariant-density-functional-theory]], [[routhian]]。
- Projects: [[a130-high-spin-collective-modes-evidence-map]]。

## L3/L4 Follow-up

- L3 question: when pairing and parity projection are added, does the `144Ba` high-spin stability conclusion survive while preserving the measured `I–ω`, `B(E2)` and `B(E3)` systematics? Discriminants are the parity splitting, alternating-parity energies and transition strengths, not another mean-field `β30` curve.
- L4 candidate: the paper cites Science Data Bank DOI `10.57760/sciencedb.j00186.00114`. Status is `candidate-L4 / not-ready` until the public data, version/hash, units, figure mapping, code/parameters and sensitivity/negative checks are obtained. No L4 claim is made from the PDF alone.
