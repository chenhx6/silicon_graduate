---
type: source
title: "Static electromagnetic moments and nuclear shapes in 129,131Ce"
aliases: ["Ionescu-Bujor 1998 Ce moments", "129Ce 131Ce TDPAD shapes"]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: experiment
reading_depth: deep-read
title_original: "Static electromagnetic moments and nuclear shapes in 129,131Ce"
authors: ["M. Ionescu-Bujor", "A. Iordachescu", "F. Brandolini", "M. De Poli", "N. H. Medina", "P. Pavan", "M. N. Rao", "C. Rossi Alvarez"]
journal: "Nuclear Physics A"
year: 1998
volume: 633
pages: "459-478"
doi: "10.1016/S0375-9474(98)00157-2"
language: en
canonical_source: "Ionescu-Bujor, M. et al. Static electromagnetic moments and nuclear shapes in 129,131Ce. Nucl. Phys. A 633, 459-478 (1998)."
library_file: "raw/papers/gpt/high-spin-20260920/形变/1998_Ionescu-Bujor et al_Static electromagnetic moments and nuclear shapes in 129,131Ce.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/形变/1998_Ionescu-Bujor et al_Static electromagnetic moments and nuclear shapes in 129,131Ce.pdf"
raw_sha256: "2735874b2be1116741f421a114ffa5995be93c99891ed284d962b53f0446484b"
nuclei: ["129Ce", "131Ce", "128Ce", "130Ce"]
reactions: ["116Sn(16O,3n)129Ce", "119Sn(16O,4n)131Ce"]
experiments: ["lnl-tpad-129-131ce-o16-70mev"]
models: ["particle-plus-triaxial-rotor-model", "BCS-pairing"]
observables: ["g-factor", "quadrupole-moment", "TDPAD", "signature-splitting", "level-energies", "alignment"]
methods: ["time-differential-perturbed-angular-distribution", "g-factor-measurement", "angular-distribution"]
tags: [129Ce, 131Ce, TDPAD, static-moments, triaxiality, shape-evolution, odd-mass]
---

# Static electromagnetic moments and nuclear shapes in 129,131Ce

## Bibliographic Record

- 作者：M. Ionescu-Bujor 等；*Nuclear Physics A* 633, 459-478 (1998)。DOI：`10.1016/S0375-9474(98)00157-2`。
- 规范文件：`raw/papers/gpt/high-spin-20260920/形变/1998_Ionescu-Bujor et al_Static electromagnetic moments and nuclear shapes in 129,131Ce.pdf`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: PDF pp.459-478 全文；TDPAD QI/MI setup, lifetime/ratio fitting, g/Q extraction, `129,131Ce` spin/parity revision, PTR Hamiltonian/parameters, negative/positive-parity bands, figures/tables and conclusions all read.
- Not covered: cited spectroscopy papers and later lifetime/shape calculations.
- Coverage caveats: deformation parameters are PTR-model optima constrained by measured moments and spectra; they are not direct shape images。

## Paper Question and Scientific Motivation

The paper measures static electromagnetic moments of low-lying `9−` isomers in neutron-deficient `129,131Ce`, then uses particle-plus-triaxial-rotor calculations to determine how the odd neutron polarizes the core and how shape changes across two neutrons.

## Experimental and Theoretical Setup

- Reactions: `116Sn(16O,3n)129Ce` and `119Sn(16O,4n)131Ce`, 70-MeV pulsed `16O`, 3-ns pulses every 800 ns.
- TDPAD: quadrupole interaction in polycrystalline Sn foils; magnetic interaction in Sn evaporated on Pb foils with 14.6/32.0 kG external field; planar HPGe at 0°/90°/±135°; time resolution about 11 ns。
- PTR: modified oscillator single-particle space, BCS pairing, hydrodynamic moments of inertia, variable Coriolis attenuation `ξ`, `ε2`, `ε4`, `γ` and core `E(2+)`。

## Key Evidence and Reasoning Chain

1. QI modulation of 108-keV (`129Ce`) and 162-keV (`131Ce`) isomers gives half-lives 60(2) ns and 88(2) ns and strongly favors `J=9` over previous `J=7` for `129Ce` (`χ²=2.7` vs `13.9`) (PDF pp.461-464, Figs.1-2).
2. QI calibration yields `|Q(129Ce,9−)|=1.32(13) eb` and `|Q(131Ce,9−)|=0.92(10) eb`; MI gives `g(129Ce,9−)=−0.185(10)` and `g(131Ce,9−)=−0.189(7)` (PDF pp.463-465, Table 1).
3. E1 decay from `9−` isomers fixes ground states as `7/2+`; this changes earlier `129Ce` ground/isomer assignments and shifts spins in its negative-parity band (PDF p.466).
4. PTR optimum parameters: `131Ce` small `ε2≈0.14-0.18`, `γ≈20-23°`, with `ξ≈0.7-1`; `129Ce` larger `ε2≈0.24`, `γ≈12-14°`, and `ε4≈0.07` needed to reproduce Q and negative-parity structure (PDF pp.466-477, Tables 1-2, Figs.4-11).
5. The Q ratio `Q(129Ce)/Q(131Ce)=1.44(7)` supports a pronounced shape change across two neutrons, but its numerical decomposition into `ε2/γ/ε4` remains PTR-model dependent (PDF pp.466-477).

## Summary

TDPAD moments provide direct spin-sensitive electromagnetic observables for `129,131Ce`. The measurements establish `J=9−` isomers, revise the `129Ce` ground-state spin assignment, and show a large quadrupole-moment difference. PTR fits associate `131Ce` with smaller quadrupole deformation and larger triaxiality, while `129Ce` needs larger `ε2`, smaller `γ` and nonzero hexadecapole deformation. This source materially strengthens the `131Ce` shape/systematics context but does not by itself identify the collective mode of its high-spin bands.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| IB98-1 | QI patterns strongly support `J=9` for the `129,131Ce` isomers; `129Ce` spin-7 fit is substantially worse. | experimental-result | direct | PDF pp.461-464, Figs.1-2 | false |
| IB98-2 | Measured isomer moments are `g=-0.185(10), |Q|=1.32(13) eb` for `129Ce` and `g=-0.189(7), |Q|=0.92(10) eb` for `131Ce`. | experimental-result | direct | PDF pp.463-465, Table 1 | false |
| IB98-3 | PTR optimum shapes differ strongly: `131Ce` `ε2≈0.14-0.18, γ≈20°-23°`; `129Ce` `ε2≈0.24, γ≈12°-14°, ε4≈0.07`. | model-result | direct | PDF pp.466-477, Tables 1-2 | true |
| IB98-4 | The two-neutron isotope change produces a large Q-moment ratio `1.44(7)` and a pronounced shape-evolution candidate. | experimental-result/author-interpretation | direct | PDF p.466, Conclusions | true |

## Competing Interpretations and Limitations

- QI/MI moments are direct observables, but mapping them to `ε2`, `γ`, and `ε4` depends on PTR single-particle space, pairing, Coriolis attenuation and core `E(2+)`。
- The rapid shape change is a model-constrained inference; the source does not provide independent lifetimes for every positive/negative band or a model-independent triaxiality measurement。
- `129Ce` level-spin revision changes comparisons to earlier source pages; source lineage must be preserved rather than silently overwriting old assignments。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-IB98-1 | Core reconstruction | TDPAD QI/MI closes a direct moment→spin/parity chain, while PTR converts moments/energies into shape parameters. | PDF pp.461-477 | self-checking |
| AR-IB98-2 | Transfer conditions | Moment evidence transfers to neighboring odd-mass Ce only with matched lattice calibration and TDPAD response; PTR shapes require model re-fit. | PDF §§2-4 | provisional |
| AR-IB98-3 | Failure conditions | Alternative Coriolis attenuation, ε4, core inertia or band assignments can change the extracted shape ranking. | PDF pp.466-477 | active-L3 |
| AR-IB98-4 | Research-question decision | Add to `131Ce`/A≈130 shape evidence map and a candidate L3 comparison of moments versus high-spin collective modes. | Full paper | candidate-L3 |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: `131Ce` pages emphasize high-spin band structures, lifetimes and γ-soft/triaxial competition; this source adds static moments, firm isomer spin evidence and a two-neutron shape-evolution anchor。
- Effect of this source: `supports` and `revises`。
- Persistence decision: update `131Ce` shape project/source links; retain PTR parameters as model results, not direct facts。
- Review state: `unreviewed`; claims self-audited by Codex, not human-reviewed。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[131ce-collective-mode-discrimination]] | Static moments constrain shape inputs for the 131Ce competing-mode map。 |
| methodological-bridge | [[time-differential-perturbed-angular-distribution]] | TDPAD QI/MI gives direct moment and spin evidence。 |
| supports | [[gamma-soft-vs-gamma-rigid-diagnostics]] | Provides A≈130 odd-mass Ce shape-systematics context, with PTR model boundary。 |

## Human Review Triage

### P0

- IB98-P0-1：`J=9` and moment values are direct TDPAD results; `ε2/γ/ε4` are PTR-dependent and must remain separated。

### P1

- IB98-P1-1：`129Ce` spin revision changes historical level labels; cross-source use must preserve old/new assignment lineage。

### P2/P3

- DOI, reaction and page metadata are aligned; no new independent L4 input is present。

## Extracted Pages

- Nuclei: update [[131ce]]/`129Ce` related context only if existing pages support it。
- Bands: no new band page。
- Concepts: [[triaxial-deformation]], [[gamma-soft-deformation]], [[angular-momentum-alignment]]。
- Methods: [[time-differential-perturbed-angular-distribution]], [[g-factor-measurement]]。
