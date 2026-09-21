---
type: source
title: "Ma et al. 1990 - Competing proton and neutron rotational alignments in 131Ba"
aliases: [Ma 1990 131Ba competing alignments]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: experiment-and-cranking-model
reading_depth: deep-read
title_original: "Competing proton and neutron rotational alignments: Band structures in 131Ba"
authors: [R. Ma, Y. Liang, E. S. Paul, N. Xu, D. B. Fossan, L. Hildingsson, R. A. Wyss]
journal: "Physical Review C"
year: 1990
volume: 41
pages: "717-728"
doi: "10.1103/PhysRevC.41.717"
citation_key: Ma_1990
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "Ma et al., Phys. Rev. C 41, 717-728 (1990)"
library_file: "raw/papers/gpt/high-spin-20260920/形变/1990_Ma et al_Competing proton and neutron rotational alignments.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/形变/1990_Ma et al_Competing proton and neutron rotational alignments.pdf"
raw_sha256: "a0dbdd4957d1d11af570b5daffc9c44609d9ef5ed570dc3ad32a67388dad90de"
nuclei: [131Ba, 131Ce, 133Ce, 135Nd, 137Sm, 139Gd]
reactions: [119Sn-12C-4n]
experiments: [five-Ge-array, gamma-gamma-coincidence, angular-distribution, DCO]
models: [cranked-shell-model, total-routhian-surface, Nilsson-Strutinsky]
observables: [signature-splitting, alignment, crossing-frequency, angular-distribution, DCO, E2-M1-mixing]
methods: [gamma-gamma-coincidence, angular-distribution, gamma-gamma-angular-correlation]
tags: [131Ba, proton-alignment, neutron-alignment, signature-splitting, gamma-soft, triaxiality]
---

# Competing proton and neutron rotational alignments in `131Ba`

## Bibliographic Record

- R. Ma *et al.*, *Phys. Rev. C* **41**, 717–728 (1990), DOI `10.1103/PhysRevC.41.717`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/形变/1990_Ma et al_Competing proton and neutron rotational alignments.pdf`。

## Scope and Reading Depth

- PDF pp.717–728 (13 pages) fully read: `119Sn(12C,4n)` experiment, five-Ge coincidence/angle setup, Fig.1 ten bands, Table I angular/DCO/mixing data, alignment/reference analysis, cranking/TRS interpretation, N=75 isotone systematics (Table II) and conclusions.
- Not covered: cited neighboring-nucleus raw data and later reanalyses.

## Key Results

- About 60 million coincidence events established ten bands in `131Ba`; bands 1–6 are `ΔI=1` sequences with both signatures, while bands 7–10 are decoupled `ΔI=2` structures (PDF pp.718–725, Fig.1 and discussion).
- The yrast `νh11/2` band has large low-spin signature splitting (about 160 keV), consistent with a triaxial shape near `γ≈−30°` in cranked-shell calculations. A proton `πh11/2^2` alignment near `ℏω≈0.43 MeV` drives the shape toward near-prolate `γ≈0°`, reducing signature splitting and producing a strong-dipole `ΔI=1` band (PDF pp.717, 725–728, Figs.5–7).
- Neutron `νh11/2` pair alignment occurs at a similar frequency and drives the core toward near-oblate `γ≈−40°` to `−80°`; the resulting decoupled `ΔI=2` bands 7/8 are candidates for neutron-aligned configurations. Their close bandheads and differing crossing frequencies preserve configuration/shape alternatives (PDF pp.725–728, Fig.6).
- Angular distributions, DCO ratios and mixing ratios identify E2, dipole and M1/E2 transitions. The 560-keV `ΔI=1` transition in band 6 has a large anisotropy and a fitted negative `δ`; the 1403/1421-keV E1 links support band-2 spin/parity assignments (PDF pp.719–725, Table I, Figs.3–4).
- N=75 isotone systematics show proton crossing frequencies decrease from `131Ba` to heavier isotones, while low-spin signature splitting decreases and post-crossing splitting increases; this is interpreted as a movement from more negative γ-soft/triaxial shapes toward prolate configurations as the proton Fermi surface changes (PDF pp.727–728, Table II, Fig.7).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MA90-1 | `131Ba` yrast `νh11/2` signature splitting and angular data establish a triaxial/γ-soft high-spin baseline under the stated cranking interpretation. | experiment-interpretation | mixed | PDF pp.717–725, Table I | true |
| MA90-2 | Proton and neutron h11/2 alignments occur near `ℏω≈0.43 MeV` and drive opposite near-prolate/near-oblate shape tendencies. | alignment-result | mixed | PDF pp.725–728, Figs.5–7 | true |
| MA90-3 | Decoupled `ΔI=2` bands 7/8 are consistent with neutron-aligned configurations but retain assignment uncertainty. | configuration-interpretation | mixed | PDF pp.727–728 | true |
| MA90-4 | Angular-distribution/DCO/mixing data are detector and alignment specific; bands 3/4 and 10 lack unique multipolarity information. | evidence-boundary | direct | PDF pp.719–725 | false |

## Summary

Ma *et al.* give a useful A≈130 example in which competing proton and neutron alignments reshape the same soft/triaxial core in opposite directions. The direct level/coincidence and angular data support the band map; the γ values, configuration labels and shape evolution remain cranking/TRS interpretations tied to alignment and convention assumptions.

## Competing Interpretations and Limitations

- A large signature splitting can reflect triaxiality, γ softness, configuration mixing or alignment blocking; it is not a unique `γ` meter.
- Proton/neutron crossing frequencies depend on Harris reference, pairing and cranking parameters. The inferred `γ≈0`/`−60°` minima are model outputs.
- Bands 3/4 have weak/unresolved linking transitions and uncertain spin/parity; band 10 parity is not unambiguous.
- Table-I δ values rely on alignment coefficients, finite-detector corrections and phase conventions; use the source-specific mapping.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| MA90-AR-1 | Experimental chain | Coincidence level scheme → angular distributions/DCO → multipolarity/mixing → spin/signature assignments. | PDF pp.718–725, Table I | self-checking |
| MA90-AR-2 | Alignment chain | Transition energies/alignment relative to Harris reference → proton/neutron crossing frequencies → configuration/shape-driving hypothesis. | PDF pp.725–728, Eq.2, Figs.5–7 | self-checking |
| MA90-AR-3 | Transfer condition | Cross-isotone comparisons require common reference, reaction/gating and cranking conventions; do not map γ labels directly to `131Ce` or other nuclei. | PDF Table II and discussion | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[signature-partner-bands]], [[signature-inversion]], [[angular-distribution]], [[angular-correlation]], [[angular-momentum-alignment]], [[rotating-mean-field]] and the A≈130 collective-mode evidence map.
- New reusable rule: treat proton/neutron alignment as a shape-driving mechanism and test it with crossing frequency, signature splitting and transition data together; do not infer a fixed shape from one band.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `MA90-P0-1`: Keep direct band/multipolarity observations separate from CSM/TRS `γ` and alignment interpretations; preserve uncertain bands and convention-specific δ values.

## Extracted Pages

- Concepts/methods: [[signature-partner-bands]], [[signature-inversion]], [[angular-distribution]], [[angular-correlation]], [[rotating-mean-field]]。
