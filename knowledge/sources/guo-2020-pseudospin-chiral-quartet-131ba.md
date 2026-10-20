---
type: source
title: "Guo et al. 2020 - Pseudospin-chiral quartet bands in 131Ba"
aliases: [Guo 2020 131Ba, pseudospin-chiral quartet 131Ba]
created: 2026-08-11
updated: 2026-08-11
status: active
review_status: unreviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Evidence for Pseudospin-Chiral Quartet Bands in the Presence of Octupole Correlations"
authors: [S. Guo, C. M. Petrache, D. Mengoni, Y. H. Qiang, Y. P. Wang, Y. Y. Wang, J. Meng, Y. K. Wang, S. Q. Zhang, P. W. Zhao, et al.]
journal: Physics Letters B
year: 2020
volume: 807
pages: 135572
doi: 10.1016/j.physletb.2020.135572
language: English
canonical_source: https://doi.org/10.1016/j.physletb.2020.135572
citation_key: guo_2020_Evidencepseudospinchiral
raw_file: "raw/papers/2020_Guo et al_Evidence for pseudospin-chiral quartet bands in the presence of octupole.pdf"
raw_sha256: 109019D2EF7338BA705462374E6CF30C0CF9D61175510DD92D63021271E8F29D
nuclei: [131ba]
reactions: ["122Sn(13C,4n)131Ba"]
experiments: [galileo-131ba-c13-65mev]
models: [reflection-asymmetric-triaxial-particle-rotor-model, tac-cdft]
observables: [two-point-angular-correlation-ratio, energy-staggering-parameter, bm1-be2-ratio, angular-momentum-alignment]
methods: [gamma-gamma-coincidence, two-point-angular-correlation-ratio, angular-distribution]
tags: [experiment-ingest, project-ingest, a130, nuclear-chirality, pseudospin, octupole-correlation]
---

# Evidence for Pseudospin-Chiral Quartet Bands in the Presence of Octupole Correlations

## Bibliographic Record

Physics Letters B 807, 135572 (2020), DOI `10.1016/j.physletb.2020.135572`. The protected BibTeX key is `guo_2020_Evidencepseudospinchiral`.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`.
- Covered scope: all six pages; experiment and partial level scheme; coincidence, `R_ac` and angular-distribution constraints; positive-parity D3-D6 quartet; negative-parity D7/D8 pair; alignments, `S(I)` and branching-derived ratios; E1 links; TAC-CDFT deformation input and RAT-PRM comparison.
- Not covered: Ref.27's full channel-selection/analysis details, unpublished Ref.35, or the promised Ref.41 azimuthal plots, angular-momentum components and full RAT-PRM discussion.
- Coverage caveat: several weak in-band mixing ratios are assumed rather than measured; no lifetimes or absolute reduced probabilities are reported.

## Extracted Pages

- PDF pp.1-2: motivation, experiment, `R_ac` method, prior bands and new/extended structures.
- PDF p.3: partial level scheme, representative double gates and `R_ac` examples.
- PDF p.4: positive-quartet configuration exclusions, pseudospin argument and experimental systematics for D3-D8.
- PDF p.5: RAT-PRM inputs/results, relative E1 comparison, model discrepancy and summary.
- PDF p.6: references.

## Paper Question and Scientific Motivation

The paper asks whether one odd-A nucleus can show a same-parity four-band manifold shaped jointly by pseudospin and chiral symmetries, while a directly E1-linked opposite-parity chiral system exposes octupole correlations without an intermediary nonchiral band.

## Experimental or Theoretical Setup

- `122Sn(13C,4n)131Ba`, `65 MeV`, LNL Tandem; two self-supporting `122Sn` foils, each `0.5 mg/cm²`.
- GALILEO: 25 Compton-suppressed Ge detectors at `90°`, `119°`, `129°` and `152°`; approximately `1.2×10^9` triple-or-higher events.
- Two-point `R_ac=Iγ(152°)/Iγ(90°)` calibration: approximately `1.5` for stretched quadrupole and `0.8` for stretched dipole; Fig.3 calculations adopt `σ/I=0.24`.
- Four-angle angular distributions determine mixing ratios for most in-band M1/E2 transitions.
- RAT-PRM uses TAC-CDFT `β2=0.22`, `γ=27.1°` for the `πh11/2g7/2⊗νh11/2` reference and tentatively adopts `β3=0.05`.

## Summary

The experiment newly establishes D4 and D8 and significantly extends D3 and D5-D7. D3-D6 form a positive-parity, mutually linked four-band manifold interpreted through mixed `πh11/2(g7/2,d5/2)⊗νh11/2` configurations as the first pseudospin-chiral quartet candidate. D7/D8 form a negative-parity chiral-doublet candidate assigned `π(h11/2)^2⊗νh11/2`. Many D7-to-D3-D6 E1 links support octupole correlations between the two systems. RAT-PRM reproduces much of the energy/ratio systematics but underpredicts feeding to D5, and the promised angular-momentum geometry is not contained in this paper.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU20-1 | The data set contains about `1.2×10^9` triple-or-higher GALILEO events from `122Sn(13C,4n)` at `65 MeV`. | experimental-fact | direct | PDF p.2, Sec.2 | true |
| GU20-2 | D4 and D8 are newly established, while D3 and D5-D7 are significantly extended in the partial `131Ba` scheme. | experimental-fact | direct | PDF pp.2-3; Figs.1-2 | true |
| GU20-3 | `R_ac` and four-angle angular distributions constrain transition character; 549-keV D6→D3 and 715/721-keV D8→D7 links are M1/E2, supporting same parity within each linked group. | experimental-fact | direct | PDF pp.2-3; Fig.3 | true |
| GU20-4 | Four positive-parity D3-D6 bands are interconnected by many M1/E2 and some weak E2 transitions; energy ordering of D4-D6 changes with spin and links connect every pair. | experimental-fact | direct | PDF pp.2-4; Figs.1,4 | true |
| GU20-5 | The paper assigns all four positive bands to the `πh11/2(g7/2,d5/2)⊗νh11/2` family using parity, signature behavior, alignments near `8-10ℏ`, neighboring-nucleus systematics and exclusion of a low-Ω-neutron alternative. | configuration-assignment | indirect | PDF pp.3-4; Fig.4 | true |
| GU20-6 | An earlier D5/D6 interpretation as two signatures of the same `πh11/2g7/2⊗νh11/2` configuration is rejected because it predicts interband ΔI=1 strengths opposite to observation. | competing-interpretation | direct | PDF p.4, Sec.3.1 | true |
| GU20-7 | D3-D6 cannot be divided into two experimental pairs uniquely by energies or links; their pseudospin-chiral quartet interpretation treats pseudospin and chiral splittings as competing, comparable effects. | author-interpretation | direct | PDF pp.1,4, Abstract and Sec.3.1 | true |
| GU20-8 | Branching-derived `B(M1)/B(E2)` values are broadly similar for D3-D6, but several have large uncertainties; staggering appears above `29/2ℏ`, with D4/D5 opposite in phase to D3. | derived-observable | direct | PDF p.4; Fig.4 | true |
| GU20-9 | D7/D8 are proposed as a negative-parity chiral pair with `π(h11/2)^2⊗νh11/2`, based on energy, `S(I)`, ratio and alignment similarities to `133Ce/135Nd`. | author-interpretation | indirect | PDF p.4; Fig.4 | true |
| GU20-10 | More than half of D7's intensity decays to D3-D6 through many E1 links, supporting octupole correlations between configurations differing by `πh11/2` versus `π(g7/2,d5/2)`. | experimental-fact | direct | PDF pp.4-5; Figs.1,5 | true |
| GU20-11 | The measured same-initial-state relative E1 pattern supports a `πd5/2` component in all four positive bands, but RAT-PRM significantly underpredicts transitions feeding D5. | model-comparison | direct | PDF p.5; Fig.5 | true |
| GU20-12 | RAT-PRM gives dominant `πh11/2g7/2⊗νh11/2` components for D3/D4, stronger `πd5/2` mixing for D5/D6 and `π(h11/2)^2⊗νh11/2` for D7/D8. | model-result | indirect | PDF p.5, Sec.3.2 | true |
| GU20-13 | RAT-PRM broadly reproduces energies, D4/D5 crossing near `27/2ℏ`, `S(I)` and ratios, but transition amplitudes feeding D5 are sensitive to nearby mixed states and not reproduced. | model-discrepancy | direct | PDF p.5; Figs.4-5 | true |
| GU20-14 | `β3=0.05` is a tentative RAT-PRM input for octupole-correlation effects, not an experimental determination or evidence of stable octupole deformation. | model-assumption | direct | PDF p.5, Sec.3.2 | true |
| GU20-15 | The paper defers azimuthal plots, angular-momentum components and the detailed RAT-PRM geometry for all three proposed pairs to a future reference. | source-completeness-boundary | direct | PDF p.5, Sec.3.2; Ref.41 | true |
| GU20-16 | For a few weak in-band transitions the analysis assumes `δ=-0.2(1)`; no lifetimes or absolute reduced transition probabilities are measured. | evidence-boundary | direct | PDF p.4, Fig.4 caption; p.5, Summary | true |
| GU20-17 | A two-same-configuration-doublet alternative is excluded only within the calculated quasiparticle mapping, not by a direct configuration observable. | model-boundary | direct | PDF p.5, Sec.3.2 | true |

## Nuclear Structure Information

| Structure | Experimental identity | Configuration/interpretation status |
|---|---|---|
| D3-D6 | four mutually linked positive-parity dipole bands; D4 new | mixed pseudospin `πh11/2(g7/2,d5/2)⊗νh11/2`; pseudospin-chiral quartet candidate |
| D7/D8 | negative-parity linked doublet; D8 new | RAT-PRM `π(h11/2)^2⊗νh11/2`; chiral-doublet candidate |
| D7→D3-D6 | many E1 links and relative E1 ratios | octupole-correlation evidence; not stable octupole deformation |

## Competing Interpretations and Limitations

- The experimental four-band manifold is secure, but its decomposition into two chiral pairs and two pseudospin sectors is not uniquely defined by energy or links.
- Common-configuration and pseudospin-component assignments rely on systematics, alignment exclusions and RAT-PRM wavefunctions.
- The key chiral angular-momentum geometry is deferred; energy/`S(I)`/ratio similarity remains nonunique.
- Branching-derived ratios depend on angular-distribution mixing ratios, including assumed values for weak lines, and lack lifetime normalization.
- E1 links support reflection-asymmetric correlations but do not determine a static `β3`; the model's `β3=0.05` is tentative.
- D5 is a visible model stress point in relative E1 feeding and state mixing.

## Analytical Reconstruction

| ID | Audit item | Agent judgment | Evidence / locator | review_status |
|---|---|---|---|---|
| AR-1 | Core reconstruction | The durable experimental result is a six-band, two-parity linked manifold; “two positive chiral pairs plus one negative pair” is an experiment-model interpretation. | GU20-2 to GU20-10 | unreviewed |
| AR-2 | Quartet identifiability | D3-D6 should persist as one four-band object because the paper explicitly cannot pair them uniquely from energies/links. | GU20-4/7 | unreviewed |
| AR-3 | Octupole scope | Direct E1 connectivity supports octupole correlations between the proposed systems, not stable reflection-asymmetric deformation. | GU20-10/11/14 | unreviewed |
| AR-4 | Geometry gap | RAT-PRM agreement strengthens configuration consistency but cannot replace the missing azimuthal/angular-momentum demonstration. | GU20-12/13/15 | unreviewed |
| AR-5 | Failure condition | Lifetimes or a geometry calculation that separates the four positive bands into a different coupling scheme would revise the pseudospin-chiral label while preserving the level scheme. | GU20-7/15/16 | unreviewed |
| AR-6 | Research decision | Create one positive quartet page and one negative doublet page; do not force D3-D6 into two stable pair identities. | Full paper | unreviewed |

## Knowledge Impact and Learning Decision

- Effect: `supports` coupled pseudospin/chirality/octupole phenomenology in `131Ba` while `limits` model-independent pair counting and geometry claims.
- Persistence: source, positive-quartet and negative-doublet pages; on-touch update `131Ba`, GALILEO experiment, pseudospin/chiral and octupole concepts, project and index.
- Review state: all `GU20-*` and AR claims remain unreviewed and outside the paper evidence gate.

## Human Review Triage

### P0

P0: none identified.

### P1

- **GU20-4/7 — four-band identity.** Do not impose two fixed positive pairs that the experimental ordering/links do not select.
- **GU20-5/12/17 — configuration logic.** Keep systematics/exclusion and RAT-PRM wavefunctions separate from direct observables.
- **GU20-10/11/14 — octupole language.** E1 correlations are not stable octupole deformation; `β3` is tentative input.
- **GU20-13/15 — model completeness.** Retain D5 mismatch and missing angular-momentum geometry.
- **GU20-16 — electromagnetic gap.** Carry assumed mixing ratios and absent lifetimes into any use of the ratios.

## Related Knowledge and Project Relations

- [[131ba]], [[galileo-131ba-c13-65mev]].
- [[131ba-positive-parity-pseudospin-chiral-quartet]], [[131ba-negative-parity-chiral-doublet-candidate]].
- [[pseudospin-chiral-quartet-bands]], [[octupole-correlation]], [[chirality-parity-quartet-band]].
- [[nuclear-chirality-and-multiple-chiral-doublet-bands]].

## Sources

- Protected BibTeX record: `guo_2020_Evidencepseudospinchiral` in `raw/zotero/wiki-inbox.bib` (read-only).
- Raw PDF: `raw/papers/2020_Guo et al_Evidence for pseudospin-chiral quartet bands in the presence of octupole.pdf`.

## Day18定量审计：四重带电磁寿命缺失、机制争论与流形波函数解耦界限

在Day18正式学习中对本文建立的131Ba正宇称四重带（D3-D6）与负宇称双重带（D7-D8）电磁比值及RAT-PRM模型计算开展定量核验，raw SHA256 `109019D2EF7338BA705462374E6CF30C0CF9D61175510DD92D63021271E8F29D`已核。原GU20-1–18各claim保持；新GU20-D18-1待审。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU20-D18-1 | 本文报道的131Ba四重正宇称带与八极关联定量核验揭示：(1) 全核六条候选带（D3–D8）全无任何在束能级寿命测量（DSAM或RDDS均缺），所报告的B(M1)/B(E2)比值严重依赖对弱跃迁混合比的假定，且向四重带去布居的E1强度仅为几何均值归一化比值，完全缺乏绝对跃迁矩阵元定标；(2) 理论机制上，本文明确反驳并排除了Kuti 2014用于103Rh的同组态MchiD模型，转而引入pi(g7/2, d5/2)赝自旋混合假说，暴露出四带流形在缺乏绝对跃迁强度时存在截然对立的理论解释争议；(3) 确立方法学底线：对于包含四条同宇称带的多带流形，在缺乏在束寿命测定绝对B(E2)与B(M1)的条件下，仅凭能级能量相近与分支比拟合，根本无法唯一性地判决其属于同组态MchiD、赝自旋四重态还是三轴形状振动态。 | task-rate-decomposition-audit | derived-and-boundary | PDF pp.3–5, Fig. 4, Fig. 5；新guo20-131ba-pseudospin-result-041 | true |

新[分析合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/guo20-131ba-pseudospin-contract-041.json)及[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/guo20-131ba-pseudospin-result-041.json)4项检查全过。
