---
type: source
title: "Pfützner et al. 2012 - Radioactive decays at limits of nuclear stability"
aliases: [Pfützner 2012 drip-line radioactive decays]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: review
reading_depth: deep-read
title_original: "Radioactive decays at limits of nuclear stability"
authors: [M. Pfützner, M. Karny, L. V. Grigorenko, K. Riisager]
journal: "Reviews of Modern Physics"
year: 2012
volume: 84
pages: "567-613"
doi: "10.1103/RevModPhys.84.567"
canonical_source: "Pfützner et al., Rev. Mod. Phys. 84, 567-613 (2012)"
library_file: "raw/papers/gpt/high-spin-20260920/review/2012_Pfützner et al_Radioactive decays at limits of nuclear stability.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/review/2012_Pfützner et al_Radioactive decays at limits of nuclear stability.pdf"
raw_sha256: "8e70ebfb00b61f7288535dc70de5de15b88f81cccde43a412fd9fcae7b4decd2"
nuclei: [45Fe, 6Be, 19Mg, 48Ni, 54Zn, 105Te, 186Pb, 26O]
reactions: [fusion-evaporation, fragmentation, spallation, fission, beta-decay, proton-radioactivity, two-proton-radioactivity]
experiments: [DSSSD, OTPC, in-flight-decay, recoil-decay-tagging, storage-ring]
models: [FRDM, HFB-17, WKB, R-matrix, three-body-continuum, continuum-shell-model, microscopic-cluster]
observables: [Sp, Sn, S2p, S2n, half-life, branching-ratio, proton-energy, momentum-correlation, spectroscopic-factor]
methods: [radioactive-beam-production, silicon-decay-spectroscopy, neutron-detection, digital-signal-processing]
tags: [drip-lines, radioactive-decay, proton-radioactivity, two-proton-radioactivity, neutron-radioactivity, exotic-nuclei]
---

# Radioactive decays at limits of nuclear stability

## Bibliographic Record

- M. Pfützner *et al.*, *Rev. Mod. Phys.* **84**, 567–613 (2012), DOI `10.1103/RevModPhys.84.567`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/review/2012_Pfützner et al_Radioactive decays at limits of nuclear stability.pdf`。

## Scope and Reading Depth

- PDF pp.567–613 (53 pages) fully read: stability limits, production/separation/detection, β-delayed particles, proton and α radioactivity, true two-proton radioactivity, neutron emission and conclusions.
- Not covered: primary data sets, post-2012 discoveries and cited model codes.

## Key Results

- Proton and neutron separation energies define the nominal drip-line conditions, but Coulomb/centrifugal barriers and pairing mean that decay mode and half-life cannot be inferred from separation energy alone (PDF pp.571–573, Eqs.1–3).
- Radioactive-decay experiments combine fusion-evaporation, transfer, fragmentation, spallation or fission with in-flight/ISOL separation and DSSSD/OTPC/neutron/digital-signal detection; delayed decay provides strong event tagging at very low yields (PDF pp.573–581, Figs.7–12).
- β-delayed particle emission is enhanced near drip lines; the relevant branching depends on β-strength, particle thresholds, sequential versus direct breakup and continuum coupling. The review emphasizes that β-delayed multiparticle spectra can expose shell structure and astrophysical waiting-point inputs (PDF pp.582–590, Eqs.8–10, Figs.13–21).
- Proton radioactivity combines `Qp`, half-life, emitted angular momentum and spectroscopic factor to constrain single-particle/deformed configurations. The `145Tm` fine-structure example demonstrates that a small low-`l` component can dominate a branch despite a larger high-`l` component (PDF pp.590–596, Eqs.12–25, Tables III–V).
- α-decay tagging and fine structure probe shell ordering near `100Sn` and shape coexistence, including the `101Sn` d5/2–g7/2 ordering controversy and `186Pb` three-`0+` interpretation (PDF pp.596–597).
- True two-proton radioactivity requires one-proton emission to be energetically forbidden and is therefore a genuine three-body continuum problem. The review separates true simultaneous decay, sequential decay through a narrow resonance and “democratic” broad-state decay; measured examples include `6Be`, `19Mg` and `45Fe` (PDF pp.597–609, Figs.25–38, Table VI).
- Three-body models, R-matrix/continuum-shell approaches and microscopic-cluster models make different compromises in asymptotics, configuration mixing and p–p interaction; lifetime and momentum-correlation predictions remain model-sensitive (PDF pp.603–610).
- One-neutron radioactivity in s–d shells is unlikely because the required decay-energy window is extremely narrow, whereas true 2n/4n radioactivity may have broader windows but remains structurally and experimentally open (PDF pp.610–612, Fig.39).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PF12-1 | Separation energy identifies a nominal stability boundary, not the observed radioactive mode or exact drip line. | boundary | review | PDF pp.571–573, Eqs.1–3 | false |
| PF12-2 | Proton-radioactivity energies/half-lives and branching provide configuration and spectroscopic-factor constraints. | review-synthesis | review | PDF pp.590–596, Eqs.12–25 | true |
| PF12-3 | True 2p decay is a three-body process distinct from sequential one-proton emission. | decay-mechanism | review | PDF pp.597–609, Figs.25–38 | true |
| PF12-4 | β-delayed multiparticle emission and true 2n/4n radioactivity retain open mechanism and model uncertainties. | open-problem | review | PDF pp.582–590, 610–612 | true |

## Summary

Pfützner *et al.* provide a unified review of how decay modes emerge at the limits of nuclear stability and how decay observables become structure probes. The most reusable boundary for this Wiki is the separation of energetics, barrier penetration, configuration/spectroscopic content and few-body continuum dynamics; a nominal drip-line label alone is not a complete physical assignment.

## Competing Interpretations and Limitations

- FRDM/HFB drip-line positions are model predictions; observed proton radioactivity can occur beyond a predicted line because of Coulomb barriers, while neutron radioactivity is much more restrictive.
- WKB/R-matrix proton widths depend on potential, angular momentum, spectroscopic factor and deformation; simple spherical models fail for strongly deformed emitters.
- True 2p lifetime and correlation analyses are sensitive to three-body asymptotic boundary conditions, configuration mixing, p–p interaction and detector acceptance; sequential and democratic interpretations must be tested against correlations.
- Review-level examples and 2012 model comparisons must not be promoted to current universal limits or independent experiments without primary-source checks.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| PF12-AR-1 | Energetics chain | Mass/separation energies → open channels → barrier penetration and half-life; pairing can open two-particle modes before single-particle stability changes. | PDF Sec.II, Eqs.1–3, 10–17 | self-checking |
| PF12-AR-2 | Spectroscopic chain | Proton/α energy and half-life → `l`, potential and spectroscopic/preformation factor → orbital/configuration inference. | PDF Secs.V–VI, Eqs.12–25 | self-checking |
| PF12-AR-3 | Few-body chain | Three-body energy and Jacobi/momentum correlations → sequential/democratic/true-2p ranking; model asymptotics are essential. | PDF Sec.VII, pp.597–610 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[drip-line-radioactivity]] and provides a cross-domain boundary for [[nuclear-astrophysics-structure]], shell evolution and shape-coexistence interpretation.
- New L3 question: which decay observables most efficiently distinguish structure changes (shell gap, pairing, deformation, configuration mixing) from continuum/barrier effects near a drip line?
- This source is a review and adds no independent A≈130 high-spin experiment; its methods/limitations are reusable for exotic-isomer and decay-tagging evidence audits.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `PF12-P0-1`: Preserve review-versus-primary-source lineage and the true-2p/sequential/democratic distinctions; do not convert review examples into current drip-line constants.

## Extracted Pages

- Concept: [[drip-line-radioactivity]]。
