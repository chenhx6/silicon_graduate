---
type: source
title: "Starosta et al. 2001 - Chiral Doublet Structures in Odd-Odd N=75 Isotones: Chiral Vibrations"
aliases: [Starosta 2001 N75 chiral vibrations, N75 chiral doublet systematics]
created: 2026-08-11
updated: 2026-08-11
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Chiral Doublet Structures in Odd-Odd N = 75 Isotones: Chiral Vibrations"
authors: [K. Starosta, T. Koike, C. J. Chiara, D. B. Fossan, D. R. LaFosse, A. A. Hecht, C. W. Beausang, M. A. Caprio, J. R. Cooper, R. Krücken, J. R. Novak, N. V. Zamfir, K. E. Zyromski, D. J. Hartley, D. L. Balabanski, Jing-ye Zhang, S. Frauendorf, V. I. Dimitrov]
journal: Physical Review Letters
year: 2001
volume: 86
pages: 971-974
doi: 10.1103/PhysRevLett.86.971
language: English
canonical_source: https://doi.org/10.1103/PhysRevLett.86.971
citation_key: starosta_2001_ChiralDoublet
raw_file: "raw/papers/2001_Starosta et al_Chiral Doublet Structures in Odd-Odd N = 75 Isotones Chiral Vibrations.pdf"
raw_sha256: 9082C1E8CED3FBFEB2248F5B18C1B646F4DC1ADC77AF5C27C6A988855583CBF4
nuclei: [130cs, 132la, 134pr, 136pm, 138eu]
reactions: ["124Sn(10B,4n)130Cs", "123Sb(13C,4n)132La", "116Sn(24Mg,4n)136Pm [source text; charge-inconsistent]"]
experiments: [stony-brook-linac-130cs-b10-47mev, stony-brook-linac-132la-c13-64mev, yale-yrast-ball-136pm-mg24-130-135mev]
models: [tilted-axis-cranking]
observables: [energy-displacement, bm1-be2-ratio]
methods: [gamma-gamma-coincidence, angular-correlation]
tags: [experiment-ingest, theory-ingest, project-ingest, a130, odd-odd, n75, nuclear-chirality, chiral-vibration]
---

# Chiral Doublet Structures in Odd-Odd `N=75` Isotones: Chiral Vibrations

## Bibliographic Record

Physical Review Letters 86, 971-974 (2001), DOI `10.1103/PhysRevLett.86.971`. The four-page article and protected BibTeX export uniquely match `starosta_2001_ChiralDoublet`.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`.
- Covered scope: complete article, Fig. 1 chirality/octupole analogy, Fig. 2 four-isotone partial level schemes, Fig. 3 doublet-energy systematics, Table I five-isotone 3D TAC results, experimental descriptions, alternative explanations and conclusions.
- Not covered: raw coincidence data, the earlier level-scheme papers for each yrast band, event-level timing/angle calibration, or the preliminary `138Eu` proceedings source.
- Coverage caveats: the printed `136Pm` reaction `116Sn(24Mg,4n)136Pm` violates charge conservation; the same beam-target system is given as `p3n` by Hecht 2001. Detector-count descriptions also differ, so exact data-set identity/overlap remains unresolved rather than silently normalized.

## Paper Question and Scientific Motivation

- The authors ask whether similar low-lying same-parity doublet bands in the odd-odd `N=75` isotones form a finite island of chiral rotation and whether their nonzero band separation represents a collective chiral-vibrational precursor to nearly degenerate chiral partners (PDF pp. 1-2 / journal pp. 971-972).
- The proposed geometry couples proton `h11/2` along the short axis, neutron `h11/2` along the long axis and core rotation along the intermediate axis; laboratory symmetry restoration should produce doublet `ΔI=1` bands, while a soft/low-barrier system can oscillate or tunnel between handed orientations (PDF pp. 1, 3 / journal pp. 971, 973; Fig. 1).

## Method and Design Logic

- Coincidence experiments extend known `πh11/2⊗νh11/2` yrast bands and identify new sidebands in `130Cs`, `132La` and `136Pm`; `134Pr` is imported from Petrache et al. Ref. 3 for a four-isotone comparison (PDF p. 2 / journal p. 972; Fig. 2).
- Timing-resolved γ-ray angular correlations identify links between each new sideband and yrast band as `ΔI=1` mixed `M1/E2`, establishing positive parity and relative-spin sequences. Cross-isotone energy-spacing patterns are then used to choose a common `I=9ℏ` bandhead (PDF pp. 2-3 / journal pp. 972-973).
- Energy displacement, interleaving and selection-rule arguments motivate a common configuration and distinguish near-degenerate `134Pr` from the more separated `130Cs/132La/136Pm` pairs. A 3D TAC calculation across `Z=55–63` supplies deformation, tilt angles, barrier heights and transition strengths, but the chiral vibration itself is proposed analytically rather than calculated as a collective quantum spectrum (PDF pp. 3-4 / journal pp. 973-974; Fig. 3; Table I).

## Key Evidence and Reasoning Chain

- New sidebands + mixed `M1/E2` links + similar alternating `ΔI=1` spacings → same-parity doublet structures with a shared relative-spin pattern (Fig. 2; PDF pp. 2-3).
- Mixed links plus an orbital-selection-rule argument → author inference that the sidebands share the yrast `πh11/2⊗νh11/2` configuration (PDF p. 3).
- `134Pr` near-degeneracy versus roughly constant `0.25/0.37/0.29 MeV` displacement in `130Cs/132La/136Pm` → central chiral-rotation island surrounded by soft chiral-vibrational structures (PDF pp. 3-4; Fig. 3).
- Aplanar 3D TAC solutions and barrier/deformation systematics across `Z=55–63` → model support for a bounded island, strongest near `Z=59–61`; the experimental nondegenerate pairs are interpreted as vibrations/tunnelling over a shallow saddle (PDF pp. 3-4; Table I).

## Summary

The paper establishes a four-isotone experimental doublet-band systematics and embeds it in a five-isotone TAC calculation. It promotes `134Pr` as the near-degenerate center of a chiral-rotation island and interprets the surrounding nondegenerate partners as soft chiral vibrations. This is a landmark cross-isotone interpretation, but not an independent confirmation of all individual pairs: `134Pr` is reused from Petrache 1996, the `136Pm` dataset/authors overlap Hecht 2001, common configuration is inferred, and no quantum chiral-vibration calculation produces the measured displacements.

## Experimental or Theoretical Setup

- `130Cs`: `124Sn(10B,4n)130Cs` at `47 MeV`, Stony Brook LINAC; 2-3 mg/cm² `124Sn` target backed with Pb; suppressed Ge detectors at `±30°`, `±90°`, `±150°` plus multiplicity filter (PDF p. 2 / journal p. 972).
- `132La`: `123Sb(13C,4n)132La` at `64 MeV`, same facility/geometry class; 2-3 mg/cm² `123Sb` target backed with Pb (PDF p. 2 / journal p. 972).
- `136Pm`: source text reports `116Sn(24Mg,4n)136Pm` at `130 MeV`, Yale Tandem/YRAST Ball with 28 suppressed Ge including five segmented clovers and two stacked `≈800 μg/cm²` targets (PDF p. 2 / journal p. 972). The printed `4n` channel is charge-inconsistent and conflicts with Hecht 2001 `p3n`.
- 3D TAC: hybrid spherical Woods-Saxon plus deformed modified-harmonic-oscillator potential; pairing gaps fixed to 80% of empirical even-odd mass differences; full self-consistency in tilt/deformation at `ℏω=0.35 MeV`, with fixed `ε,γ` and refitted tilt angles at other frequencies (PDF p. 3 / journal p. 973).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ST01-1 | `130Cs/132La/136Pm` 新 sidebands 由当前 coincidence studies 建立，并与 Ref. 3 的 `134Pr` pair 组成四个 `N=75` isotone partial level schemes。 | experimental-fact | direct | PDF p. 2 / journal p. 972; Fig. 2 | true |
| ST01-2 | `130Cs` 与 `132La` 分别由 `124Sn(10B,4n)` 47 MeV 和 `123Sb(13C,4n)` 64 MeV 产生；`136Pm` 段原文印作 `116Sn(24Mg,4n)` 130 MeV。 | experimental-fact | direct | PDF p. 2 / journal p. 972 | true |
| ST01-3 | 原文 `116Sn(24Mg,4n)136Pm` 在电荷数上不自洽；Hecht 2001 对相近 Yale/YRAST beam-target system 报告 `p3n`。当前把它记录为 source-internal metadata conflict，不把推定修正冒充本文原文。 | wiki-synthesis | indirect | ST01 PDF p. 2; HE01-1, PDF p. 1 | true |
| ST01-4 | `±20 ns` coincidence timing 下的 γ angular correlations 把 sideband-to-yrast links 指认为 `ΔI=1` mixed `M1/E2`，据此给出 positive parity 与相对自旋序列。 | experimental-criterion | direct | PDF p. 2 / journal p. 972; Fig. 2 | true |
| ST01-5 | 四核系统学支持共同 `I=9ℏ` bandhead；作者明确说明实验技术只给 relative spins，并主张这足以讨论 chirality。 | author-interpretation | indirect | PDF pp. 2-3 / journal pp. 972-973 | true |
| ST01-6 | `134Pr` 双带位移从低自旋约 `0.19 MeV` 降至 `I=14` 近简并；`130Cs/132La/136Pm` 位移分别约恒定为 `0.25/0.37/0.29 MeV`。 | experimental-fact | direct | PDF p. 3 / journal p. 973; Fig. 3 | true |
| ST01-7 | 作者以 mixed `M1/E2` links 和正宇称轨道的 M1/E2 selection-rule argument 推断 sidebands 也建立在 `πh11/2⊗νh11/2` 上。 | author-interpretation | indirect | PDF p. 3 / journal p. 973, left column | true |
| ST01-8 | 非简并 pairs 被解释为 γ-soft core 中角动量跨越/穿隧浅 saddle barrier 的 collective chiral vibration；Fig. 1 以 octupole vibration 作类比。 | author-interpretation | indirect | PDF p. 3 / journal p. 973, right column; Fig. 1 | true |
| ST01-9 | 作者以 `ℏω=0.4 MeV` 时最低同壳 quasiparticle routhian 差约 `0.75 MeV`、区域 γ-vibration energies `≥0.60 MeV` 排斥两种替代解释，但允许小 admixtures。 | author-interpretation | indirect | PDF p. 3 / journal p. 973, right column | true |
| ST01-10 | Table I 的 3D TAC 对 `Z=55,57,59,61,63` 给出 `(ε,γ)`、tilt angles、saddle barrier `E_b` 与 intra/interband `B(M1),B(E2)`；所有列均有 aplanar solutions，`134Pr/136Pm` barrier 最大（各 `30 keV`）。 | model-result | direct | PDF pp. 3-4 / journal pp. 973-974; Table I | true |
| ST01-11 | 模型判断 chirality 在 `Z=59/61` 最显著，并在 `Z<55`、`Z>63` 消失；实验 sidebands 的 spin intervals 被概括为 `134Pr` 7ℏ、`132La` 5ℏ、`130Cs/136Pm` 4ℏ。 | model-result | indirect | PDF p. 4 / journal p. 974 | true |
| ST01-12 | 结论提出一个以 `134Pr` 为中心、周围为 soft chiral vibrations 的小型 chiral-rotation island；“若该解释正确”，它才可能构成 stable triaxial shapes 的首次直接证据。 | author-interpretation | direct | PDF p. 4 / journal p. 974, Summary | true |

## Nuclear Structure Information

| Nucleus | Experimental role | Energy relation | Paper interpretation |
|---|---|---|---|
| `130Cs` | new sideband linked to known yrast band | roughly constant `≈0.25 MeV` displacement | soft chiral-vibrational doublet candidate |
| `132La` | new sideband linked to known yrast band | roughly constant `≈0.37 MeV` displacement | soft chiral-vibrational doublet candidate |
| `134Pr` | pair imported from Petrache et al. | `≈0.19 MeV` at low spin, near-degenerate at `I=14` | central chiral-restored doublet / strongest chiral-rotation case |
| `136Pm` | new sideband and extended yrast structure | roughly constant `≈0.29 MeV` displacement | soft chiral-vibrational doublet candidate |
| `138Eu` | included only in the five-isotone TAC table and as preliminary data in Ref. 11 | no current-work experimental scheme | shallower/narrower modeled chiral solution; later direct experiment must be checked separately |

## Authors' Interpretation

The authors treat the recurring doublets as a collective `N=75` phenomenon, not ordinary signature partners. `134Pr` is the most stable/near-degenerate chiral case; the other observed pairs are soft chiral vibrations in which the core angular momentum oscillates or tunnels between left- and right-handed orientations. The conclusion explicitly retains the conditional “if the chiral doublet interpretation is correct” for the stable-triaxiality implication.

## Model Results

- At the quoted frequencies, Table I gives `γ=39°,32°,27°,27°,20°` for `Z=55–63`, and barriers `E_b=3,12,30,30,10 keV`.
- The calculation predicts both interband (`+→+`) and intraband (`+→−`) transition strengths for aplanar solutions; a planar solution would yield one band. The table is a TAC output, not a direct calculation of the measured doublet excitation energy.
- Self-consistency is complete at one frequency; deformation is then frozen while tilt angles are recalculated over `0.20–0.45 MeV`. This weak-frequency-dependence approximation is part of the model boundary.

## Competing Interpretations and Limitations

- Quasiparticle and γ-vibrational alternatives are rejected mainly by characteristic energy scales; no unified quantum calculation compares their spectra and transition matrix elements with the chiral-vibration proposal.
- The same-configuration claim depends on a qualitative selection-rule argument and observed mixed links, not absolute matrix elements or a configuration-specific measurement.
- Relative spins and a common `I=9` bandhead are systematics-driven; absolute bandhead spins are not directly fixed by the experiment.
- The article does not calculate a collective chiral-vibrational wave function, excitation energy or tunnelling splitting. TAC supplies static/aplanar mean-field minima and barriers.
- Evidence independence is limited: `134Pr` is imported from earlier work; Starosta and Hecht share many authors and related `136Pm` data/systematics; Hecht 2001 uses this paper for its bandhead spins.
- The printed `136Pm` reaction and detector description conflict with Hecht 2001; exact experiment overlap remains unresolved.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-1 | Core reconstruction | Starosta 2001 converts several nucleus-specific partner-band observations into an evolutionary hypothesis: central near-degenerate chiral rotation (`134Pr`) plus soft chiral vibrations (`130Cs/132La/136Pm`). This is cross-source/systematics interpretation, not four independent discoveries. | ST01-1, ST01-6 to ST01-12; Figs. 2-3 | unreviewed |
| AR-2 | Assumptions and dependencies | Common bandhead spin, common configuration, deformation/barrier systematics and the mapping from band displacement to vibrational energy are all necessary; only relative spins and decay links are direct experiment. | ST01-4 to ST01-10 | unreviewed |
| AR-3 | Transfer conditions | The pattern can motivate comparisons across isotones only when band identities, parity, links and configurations are checked independently. Shared authors/data and imported level schemes must not be counted as independent replication. | Fig. 2 provenance; HE01 overlap | unreviewed |
| AR-4 | Failure conditions | If absolute electromagnetic observables or a competing quantum model reproduce the same pairs without left/right dynamics, energy-displacement systematics alone cannot identify chiral vibration. | ST01-7 to ST01-10 and missing quantum calculation | unreviewed |
| AR-5 | Reverse/falsification test | Recalculate each pair in a quantum particle-rotor/collective Hamiltonian including γ softness and tunnelling, compare absolute inter/intraband strengths and staggering, and test whether the inferred vibrational energy tracks a calculated barrier/mass rather than merely the band displacement. | Table I plus experimental gaps | unreviewed |
| AR-6 | Research-question decision | Persist a project-level N=75 evolution map and a metadata-conflict question. Do not create a standalone chiral-vibration synthesis until later lifetime/model papers show whether the 2001 island picture survives. | Full article and HE01 comparison | unreviewed |

### Companion Evidence Audit

- Sideband-to-yrast mixed links in `130Cs/132La/136Pm`: `observed` in the reported coincidence/angle analysis and drawn in Fig. 2.
- Absolute/common bandhead spin `I=9`: `expected-but-not-established`; selected by systematics and prior Ref. 8.
- Same `πh11/2⊗νh11/2` configuration: `expected-but-not-established`; inferred from link strength/selection rules.
- Collective chiral vibration: `expected-but-not-established`; no vibrational eigenstate calculation is supplied.
- Exact `136Pm` channel and Starosta/Hecht event-set overlap: `blocked-needs-experiment-log/raw-metadata`.

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: chirality fingerprints are model dependent, and energy nondegeneracy can represent finite tunnelling/chiral vibration rather than refuting the mechanism outright.
- Effect of this source: `supports`, `revises` and `limits`.
- Reason: it establishes the historical N=75 island/vibration narrative and strengthens the 134Pr reinterpretation, while revealing non-independent provenance, a reaction-metadata conflict and the absence of a quantum vibrational calculation.
- Persistence decision: create source, `130Cs/132La` nucleus/experiment/pair pages and a `134Pr` stable pair mapping; update `134Pr/136Pm`, the existing Hecht pair/experiment and the chirality project. Record the N=75 thematic REFLECT in the project; defer overview/QMD until a later batch checkpoint.
- Review state: all ST01 claims and analytical reconstruction remain unreviewed and outside the paper evidence pool.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[nuclear-chirality-and-multiple-chiral-doublet-bands]] | Supplies the original four-isotone doublet systematics and five-isotone TAC island/vibration hypothesis. |
| supports | [[chiral-vibration]] | Introduces nonzero partner displacement as a soft collective oscillation/tunnelling interpretation. |
| retrospective-connection | [[134pr-chiral-doublet-candidate-pair]] | Reinterprets Petrache 1996 Band 1/Band 2 as the central near-degenerate chiral pair; it does not change the 1996 authors' wording. |
| limits | [[hecht-2001-chiral-symmetry-breaking-136pm-138eu]] | Supplies Hecht's bandhead systematics but shares authors/data context, so the two papers are not independent confirmation. |

## Human Review Triage

Use the canonical P0/P1/P2/P3 definitions in `system/workflows/ingest-strategies.md`.

### P0

P0: none identified.

### P1

- **ST01-2/ST01-3 — `136Pm` reaction metadata conflict.** Grounded evidence: PDF p. 972 prints `116Sn(24Mg,4n)136Pm`, which violates charge conservation; Hecht 2001 prints `p3n` for a related Yale/YRAST experiment. Agent inference: likely source typo, but exact dataset identity and correction cannot be assumed. User check: verify against an erratum, original experiment record or cited proceedings. Risk: propagating an impossible channel or silently rewriting source evidence.
- **ST01-5/ST01-7 and AR-2 — spin/configuration inference.** Grounded evidence: relative spins come from angular correlations; common `I=9` and `πh11/2⊗νh11/2` follow systematics/selection-rule reasoning. Agent inference: links strongly constrain but do not directly measure configuration. User check: assess whether project wording retains this hierarchy. Risk: circular systematics and overconfident common-basis claims.
- **ST01-8 to ST01-12 and AR-1/AR-4 — chiral-vibration/island model boundary.** Grounded evidence: band displacements, TAC barriers and regional energy scales support the narrative, but no collective quantum vibration calculation is performed and the final stable-triaxial claim is conditional. User check: preserve “author interpretation/candidate” language and do not equate displacement with a measured vibrational eigenenergy. Risk: turning an influential analogy into direct dynamics evidence.
- **Evidence independence — Starosta/Hecht overlap.** Grounded evidence: shared authors, related `136Pm` YRAST data and Hecht's explicit use of Ref. 6 spin systematics. Agent inference: these are complementary papers in one evidence lineage, not independent replication. User check: confirm the project evidence map marks the dependency. Risk: inflated confidence from double-counting.

### P2/P3

- P2: verify the Fig. 2 band mapping, energy-displacement transcription and Table I values.
- P3: review source aliases, two Stony Brook experiment pages, pair navigation and batch-reflect wording.

## Extracted Pages

- Nuclei: [[130cs]], [[132la]], [[134pr]], [[136pm]], with [[138eu]] as model/preliminary context.
- Bands: [[130cs-chiral-vibration-doublet-candidate]], [[132la-chiral-vibration-doublet-candidate]], [[134pr-chiral-doublet-candidate-pair]], [[136pm-chiral-twin-candidate-pair]]
- Concepts: [[nuclear-chirality]], [[chiral-vibration]], [[static-chirality]]
- Methods: [[gamma-gamma-coincidence]], [[angular-correlation]]

## Non-source Notes and Follow-up

Next corpus source: Hecht 2003 `140Eu`. Preserve the distinction between Starosta's N=75 island/systematics and later single-nucleus evidence, and continue checking whether “chiral vibration” is calculated or only inferred from partner displacement.

## Day21 checkpoint054：134Pr原始手征主张与数据血缘审计

在冻结前置回忆后，重新核对Starosta等2001年PRL 86, 971全文4页及Table I、Fig. 2、Fig. 3。原文BibTeX为`starosta_2001_ChiralDoublet`，本地raw文件SHA-256匹配为`9082C1E8CED3FBFEB2248F5B18C1B646F4DC1ADC77AF5C27C6A988855583CBF4`。原ST01-1至12、review_status与needs_review保持。以下为本检查点补充的定向审计声明：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ST01-D21-R54-1 | Table I给出的134Pr (Z=59) 3D TAC计算结果为：ε=0.175, γ=27°, ℏω=350 keV, θ=65°, ψ=41°, 鞍点势垒Eb=30 keV, J=11.9, B(M1, 1→1)=0.80 μN², B(M1, 1→2)=0.41 μN², 10B(E2, 1→1)=2.11 (eb)², 10B(E2, 1→2)=0.13 (eb)²。该计算仅为微观均场基态与势垒，未计算量子隧穿劈裂。 | model-result | direct-original | PRL 86, 971 p. 974 Table I | true |
| ST01-D21-R54-2 | 134Pr实验能级数据并非本文测量，而是直接引用Petrache 1996 (Ref. 3)。本文将低自旋约0.19 MeV在I=14处降为近简并（约0.04 MeV）的特征解释为手征转动岛中心，未在此核测定任何能级寿命或跃迁几率。 | source-lineage-and-data-scope | direct-original | PRL 86, 971 p. 972右栏、p. 973左栏、Fig. 3、Ref. 3 | true |
| ST01-D21-R54-3 | 作者在结论中对稳定三轴形变证据作了明确的有条件陈述：“If the chiral doublet interpretation is correct, this would be the first direct evidence for stable triaxial shapes in nuclei”。作者保留了该解释的前提条件。 | author-hedging-and-limitation | direct-original | PRL 86, 971 p. 974 Summary | true |
| ST01-D21-R54-4 | 本文确立了134Pr作为手征候选核的历史基准，但由于缺乏寿命与绝对矩阵元，其对手征转动的指认完全依赖能谱近简并与TAC计算，直接构成了Petrache 2006（四极矩比2.0(4)与多带交叉）反驳的历史对象。 | historical-evidence-chain | direct-and-derived | PRL 86, 971 pp. 971–974 | true |

### 科学判定与学习决策

- 既有理解：Starosta 2001是N=75同中子素手征振动与手征转动岛假说的提出文献。
- 影响：limits。核定134Pr数据完全依赖Petrache 1996输入，未测定寿命；其将能级近简并等同于手征转动岛的推断，在缺乏跃迁矩阵元下是不充分的，随后被Tonev 2006与Petrache 2006严格否定。
- 持久化：更新本source页与方法页推断阶梯Case Study 1。
