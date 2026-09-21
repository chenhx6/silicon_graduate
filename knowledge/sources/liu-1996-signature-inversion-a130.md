---
type: source
title: "Liu et al. 1996 - Spin assignments and signature inversion of pi h11/2 times nu h11/2 bands"
aliases: [Liu 1996 signature inversion A130]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: systematics-and-particle-triaxial-rotor-comparison
reading_depth: deep-read
title_original: "Systematic study of spin assignments and signature inversion of πh11/2⊗νh11/2 bands in doubly odd nuclei around A≈130"
authors: [Yunzuo Liu, Jingbin Lu, Yingjun Ma, Shangui Zhou, Hua Zheng]
journal: "Physical Review C"
year: 1996
volume: 54
pages: "719-730"
doi: "10.1103/PhysRevC.54.719"
citation_key: Liu_1996
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "Liu et al., Phys. Rev. C 54, 719-730 (1996)"
library_file: "raw/papers/gpt/high-spin-20260920/旋称/1996_Liu et al_Systematic study of spin assignments and signature inversion of π h 1 1 - 2 ⊗ν.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/旋称/1996_Liu et al_Systematic study of spin assignments and signature inversion of π h 1 1 - 2 ⊗ν.pdf"
raw_sha256: "ca3e1c1bc834158112dee525fa4c42c3d44596975a506f3a2a1da023580a346f"
nuclei: [120Cs, 122Cs, 124Cs, 126Cs, 128Cs, 130Cs, 124La, 126La, 128La, 130La, 132La, 134La, 130Pr, 132Pr, 134Pr, 136Pr, 134Pm, 136Pm, 138Pm, 138Eu]
reactions: [compiled-literature-systematics]
experiments: [band-systematics]
models: [particle-triaxial-rotor, Semmes-Ragnarsson-residual-interaction]
observables: [signature-inversion, excitation-energy-systematics, spin-assignment, signature-splitting]
methods: [level-scheme-crosswalk, isotopic-systematics]
tags: [signature-inversion, A130, h11/2, spin-assignment, triaxial-rotor]
---

# Signature inversion in `πh11/2⊗νh11/2` bands around A≈130

## Bibliographic Record

- Y. Liu *et al.*, *Phys. Rev. C* **54**, 719–730 (1996), DOI `10.1103/PhysRevC.54.719`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/旋称/1996_Liu et al_Systematic study of spin assignments and signature inversion of π h 1 1 - 2 ⊗ν.pdf`。

## Scope and Reading Depth

- PDF pp.719–730 (12 pages) fully read: excitation-energy systematics, revised `I0` assignments for La/Pr/Pm/Eu/Cs chains, Table I/II, signature-inversion plots, comparison with particle–triaxial-rotor calculations and conclusions.
- Not covered: primary spectroscopy papers cited for each isotope and later reassessments.

## Key Results

- The authors revise many lowest observed spins `I0` in `πh11/2⊗νh11/2` bands by requiring smooth excitation-energy systematics across isotopic/isotonic chains. For La/Pr/Pm/Eu, most previously assigned `I0=8` values shift to 7 or 9; Cs admits competing reference choices (`124Cs I0=7`, `130Cs I0=9` or 11) that cannot both be correct (PDF pp.719–725, Tables I–II, Figs.1–14).
- With the revised assignments, all discussed A≈130 doubly odd nuclei show low-spin signature inversion. The inversion spin increases with neutron number in Cs and La isotopes (PDF pp.728–729, Fig.15).
- Particle–triaxial-rotor calculations with a Semmes–Ragnarsson zero-range p–n interaction reproduce the inverted signatures and inversion-spin trend when the revised spin assignments are used (PDF pp.729–730, Tables I–II).
- The paper warns that prior conclusions about equilibrium γ deformation can reverse sign if the bandhead spin is wrong by an odd integer; Cs spin assignments remain unresolved pending new data (PDF pp.728–730).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LU96-1 | Smooth excitation-energy systematics motivate revised bandhead spin assignments across A≈130 chains. | systematics-result | mixed | PDF pp.719–725, Tables I–II | true |
| LU96-2 | Revised assignments make low-spin signature inversion systematic in the discussed `πh11/2⊗νh11/2` bands. | systematics-result | mixed | PDF pp.728–729, Fig.15 | true |
| LU96-3 | Particle–triaxial-rotor calculations agree with inversion trends only after the revised spin crosswalk. | model-comparison | mixed | PDF pp.729–730 | true |
| LU96-4 | Cs reference assignments remain mutually incompatible/undetermined. | unresolved-boundary | direct | PDF pp.723–730, Tables II | false |

## Summary

Liu *et al.* show that signature-inversion systematics and spin assignments are coupled: changing a bandhead by an odd `ΔI` can reverse the inferred signature order and the inferred γ-deformation discussion. The source is a cautionary crosswalk rather than a direct new spectroscopy experiment.

## Competing Interpretations and Limitations

- The method assumes smooth level-energy trends and similarity of band structures across isotopic/isotonic chains; this is a model/systematics prior, not an independent spin measurement.
- Cs chains have insufficient mutually consistent anchors; the paper presents alternatives rather than a final assignment.
- Particle–triaxial-rotor agreement depends on fitted parameters and the revised spin choices; it does not uniquely establish a triaxial shape.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| LU96-AR-1 | Crosswalk chain | Literature level schemes → common reference spin → smooth excitation curves → revised `I0`/signature labels. | PDF Figs.1–14, Tables I–II | self-checking |
| LU96-AR-2 | Interpretation chain | Revised signature order → inversion spin trend → particle–triaxial-rotor comparison; preserve unresolved Cs alternatives. | PDF Fig.15 and Secs.V–VI | self-checking |
| LU96-AR-3 | Transfer condition | No direct δ/lifetime input; do not transfer γ-shape inference to `131Ba/131Ce` without nucleus-specific assignments. | PDF conclusion | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[signature-inversion]], [[signature-partner-bands]], [[triaxial-deformation]], [[multipole-mixing-ratio]] and A≈130 spin-assignment audit.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `LU96-P0-1`: Preserve the spin-crosswalk prior and unresolved Cs assignments; do not use revised signature inversion as direct γ-deformation evidence.

## Extracted Pages

- Concepts: [[signature-inversion]], [[signature-partner-bands]], [[triaxial-deformation]]。
