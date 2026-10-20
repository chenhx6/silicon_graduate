---
type: source
title: "Hecht et al. 2003 - Evidence for Chiral Symmetry Breaking in 140Eu?"
aliases: [Hecht 2003 140Eu, 140Eu chiral bands and shape coexistence]
created: 2026-08-11
updated: 2026-08-11
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Evidence for Chiral Symmetry Breaking in 140Eu?"
authors: [A. A. Hecht, C. W. Beausang, H. Amro, C. J. Barton, Z. Berant, M. A. Caprio, R. F. Casten, J. R. Cooper, D. J. Hartley, R. Krücken, D. A. Meyer, H. Newman, J. R. Novak, N. Pietralla, J. J. Ressler, A. Wolf, N. V. Zamfir, Jing-Ye Zhang, K. E. Zyromski]
journal: Physical Review C
year: 2003
volume: 68
pages: 054310
doi: 10.1103/PhysRevC.68.054310
language: English
canonical_source: https://doi.org/10.1103/PhysRevC.68.054310
citation_key: hecht_2003_Evidencechiral
raw_file: "raw/papers/2003_Hecht et al_Evidence for chiral symmetry breaking in Eu 140.pdf"
raw_sha256: 5EE92742D8E78A8CCC1A37058BEE711D99FADCAF38023A710AF186A4FE497463
nuclei: [140eu]
reactions: ["92Mo(51V,2pn)140Eu"]
experiments: [yale-yrast-ball-140eu-v51-205mev]
models: [total-routhian-surface, cranked-shell-model, triaxial-particle-rotor-model]
observables: [bm1-be2-ratio, angular-momentum-alignment, dco-ratio, linear-polarization-asymmetry]
methods: [gamma-gamma-coincidence, angular-distribution, dco-ratio, compton-polarimetry]
tags: [experiment-ingest, project-ingest, a140, odd-odd, n77, nuclear-chirality, shape-coexistence]
---

# Evidence for Chiral Symmetry Breaking in `140Eu`?

## Bibliographic Record

Physical Review C 68, 054310 (2003), DOI `10.1103/PhysRevC.68.054310`. The question mark is part of the original title and is scientifically material: the paper ends with two unresolved interpretations rather than a discovery claim.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`.
- Covered scope: all 14 PDF pages, complete level scheme and transition table, coincidence spectra, angular-distribution/DCO/polarization calibrations, spin-parity and configuration arguments, alignments, TRS/Routhian and particle-rotor calculations, branching-ratio table, chirality/shape-coexistence alternatives and conclusion.
- Not covered: event-level matrices, efficiency/polarization calibration files, the earlier isomer-tagging and level-scheme papers, or independent lifetime data.
- Coverage caveats: several transitions/spins are tentative; the 20.5-keV Band-5 link is conjectural; branching ratios do not supply individual absolute `B(M1)` or `B(E2)` values.

## Extracted Pages

- PDF pp. 1-2: abstract, motivation, prior `140Eu` structures and experimental setup.
- PDF pp. 3-8: level scheme, spectra, Table I, angular-distribution/DCO/asymmetry methods and band-by-band placement.
- PDF pp. 9-11: TRS, alignments, configuration assignments, regional systematics and branching-ratio calculation.
- PDF pp. 12-13: possible chirality, missing signature partners, shape coexistence and conclusion.
- PDF p. 14: remaining references only.

## Paper Question and Scientific Motivation

The authors test whether `140Eu` extends the `A≈130` chiral-candidate region beyond the `N=75` isotones. The same TRS calculations also predict two close triaxial minima near `β≈0.2, γ≈±25°`, so the experiment is explicitly framed as a discrimination problem between chiral twins and shape coexistence (PDF pp. 1-2 / journal pp. 054310-1–2).

## Method and Design Logic

- High-statistics doubles and triples from `92Mo(51V,2pn)140Eu` establish five bands and their links. `Kα` x-ray coincidences and an excitation function constrain the isotope assignment (PDF pp. 2-8; Figs. 1-4; Table I).
- Gated angular distributions, DCO ratios and YRAST-Ball clover Compton asymmetry constrain transition multipolarity and electric/magnetic character. The paper defines `A=(N_parallel-N_perpendicular)/(N_parallel+N_perpendicular)`, so magnetic transitions have positive `A`; this convention must not be mixed with the opposite sign convention used in Hecht 2001 (PDF pp. 3-7; Figs. 5-7).
- Alignments, interband links and regional systematics motivate common-configuration assignments for Bands 1/2 and Bands 3/4. TRS, Woods-Saxon Routhians and a triaxial particle-rotor calculation then test possible intrinsic structures, while measured branchings supply only `B(M1)/B(E2)` ratios (PDF pp. 9-13; Figs. 9-13; Table II).

## Summary

The paper establishes a much expanded `140Eu` high-spin level scheme with five bands and 69 transitions. Bands 1/2 are assigned a mixed `π(g7/2,d5/2)⊗νh11/2` negative-parity configuration; Bands 3/4 are assigned `πh11/2⊗νh11/2` positive parity. Each pair has same-spin near-degenerate levels and can be discussed as a chiral-twin candidate, but TRS also supplies a viable same-configuration shape-coexistence scenario at `γ≈+25°` and `−25°`. Missing signature partners and the absence of lifetimes/absolute strengths prevent a decision.

## Experimental or Theoretical Setup

- `92Mo(51V,2pn)140Eu` at 205 MeV, selected after a 190–220 MeV excitation function; two stacked `700 μg/cm²` targets (PDF p. 2).
- Yale ESTU Tandem and YRAST Ball: seven segmented clovers at `90°`, 16 coaxial Ge at `50°/126°/160°`, and three LEPS at `50°/90°`; total photopeak efficiency about `2.5%` (PDF p. 2).
- Five-day run: about `1.0×10^9` unfolded doubles and `4.7×10^8` unfolded triples (PDF p. 2).
- TRS calculations predict two persistent minima around `β≈0.2, γ≈±25°` through `ℏω≈0.45 MeV`; particle-rotor calculations use `γ≈25°` for branching-ratio comparisons (PDF pp. 8-13; Figs. 9, 13).

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HE03-1 | The 205-MeV experiment produced about `1.0×10^9` unfolded doubles and `4.7×10^8` unfolded triples; x-ray coincidences and excitation-function behavior support assignment to `140Eu`. | experimental-fact | direct | PDF p. 2 / journal p. 054310-2 | true |
| HE03-2 | The new level scheme contains five bands and 69 transitions. | experimental-fact | direct | Abstract; PDF pp. 1, 13; Fig. 1; Table I | true |
| HE03-3 | Bands 1 and 2 are negative parity, linked by two E2 and two mixed M1/E2 transitions; Band 2 is new and changes from E2-dominated low spin to dipole-dominated decay after a crossing near `I≈12ℏ`. | experimental-fact | direct | PDF pp. 4, 7; Fig. 1 | true |
| HE03-4 | Bands 3 and 4 are positive parity and connected by E2 and mixed M1/E2 transitions; Band 4 is reconstructed from a previously reported side-feeding cascade. | experimental-fact | direct | PDF pp. 7-8; Fig. 1 | true |
| HE03-5 | Band 3 spins are revised upward by `2ℏ` relative to Ref. 17 using regional `πh11/2⊗νh11/2` systematics and a newly placed 71.0-keV `10+→9+` transition. | experimental-assignment | indirect | PDF pp. 7-8; Fig. 8 | true |
| HE03-6 | Band 5 contains three observed `ΔI=2` transitions, but its proposed 20.5-keV link is unobserved and inferred from coincidence and intensity ordering; the band interpretation is unclear. | experimental-fact | indirect | PDF p. 8; Fig. 1 | true |
| HE03-7 | The paper's gated angular-distribution, DCO and asymmetry calibrations support the assigned dipole/quadrupole and electric/magnetic characters in Table I. | experimental-criterion | direct | PDF pp. 3-7; Figs. 5-7; Table I | true |
| HE03-8 | Bands 1 and 2 are assigned the same mixed `π(g7/2,d5/2)⊗νh11/2` configuration; treating either proton orbital as pure is explicitly considered misleading because of mixing. | author-interpretation | indirect | PDF pp. 9, 13; Fig. 10(a) | true |
| HE03-9 | Bands 3 and 4 are assigned the same `πh11/2⊗νh11/2` configuration from linking-transition character, selection-rule reasoning, initial alignment near `7ℏ` and regional systematics. | author-interpretation | indirect | PDF pp. 8, 10-11; Figs. 10(b), 12 | true |
| HE03-10 | Same-spin levels in Bands 3/4 differ by about `30 keV` at `13ℏ` and `15ℏ` and about `140 keV` at `11ℏ` and `17ℏ`; the authors therefore propose Band 4 as a possible chiral partner of Band 3. | author-interpretation | direct | PDF pp. 11-12 | true |
| HE03-11 | Same-spin levels in Bands 1/2 differ by about `110 keV` at `6−` and `8−` and about `10 keV` at `10−`; their chiral-partner interpretation is explicitly described as speculative. | author-interpretation | direct | PDF p. 12 | true |
| HE03-12 | The lack of observed signature partners for Bands 2 and 4 is a problem for the chiral interpretation, though rough intensity estimates allow that sequences near the `≈5%` relative-intensity level could have been missed. | author-interpretation | indirect | PDF p. 12 | true |
| HE03-13 | TRS calculations give two close, persistent minima around `β≈0.2, γ≈±25°` for reasonable positive- and negative-parity configurations. | model-result | indirect | PDF pp. 8-9, 12-13; Fig. 9 | true |
| HE03-14 | The two minima allow Bands 1/2 and Bands 3/4 to be interpreted instead as same-configuration bands at different triaxial shapes; the data do not choose this shape-coexistence scenario over chirality. | author-interpretation | indirect | PDF pp. 12-13 | true |
| HE03-15 | Branching-derived `B(M1)/B(E2)` values agree reasonably with the particle-rotor calculation for Band 3 above `I=13ℏ` but disagree strongly for Band 1; no individual absolute strengths were measured. | model-result | direct | PDF p. 11; Fig. 13; Table II | true |
| HE03-16 | The authors identify lifetime measurements as the discriminator: chirality predicts a sharp intraband `B(E2)` change near `I≈15ℏ`, whereas shape coexistence predicts a smoother increase. | author-interpretation | direct | PDF p. 13, Conclusion | true |

## Nuclear Structure Information

| Structure | Observed relation | Paper assignment | Calibrated status |
|---|---|---|---|
| Bands 1/2 | linked negative-parity structures; near-degenerate same-spin states; different crossing behavior | mixed `π(g7/2,d5/2)⊗νh11/2` | possible chiral twins or same-configuration shape coexistence |
| Bands 3/4 | linked positive-parity structures; near-degenerate same-spin states; related alignments | `πh11/2⊗νh11/2` | stronger of the two chiral candidates, but shape coexistence remains viable |
| Band 5 | three `ΔI=2` transitions; connection depends on an unobserved 20.5-keV transition | unclear | incomplete structure, not a chiral candidate in this source |

## Competing Interpretations and Limitations

- Chirality and shape coexistence are co-primary interpretations in the paper; neither is a later Agent-added objection.
- A same orbital label is inferred through links, alignments, systematics and selection rules, not measured by a configuration-specific observable.
- Missing signature partners weaken both scenarios and are rescued only by rough sensitivity estimates.
- Particle-rotor comparison uses branching-derived ratios. Without lifetimes, the sharp-versus-smooth `B(E2)` prediction is untested.
- Band 1 disagrees with the calculation, plausibly because of proton-orbital mixing; Band 5 remains unexplained.

## Analytical Reconstruction

| ID | Audit item | Agent judgment | Evidence / locator | review_status |
|---|---|---|---|---|
| AR-1 | Core reconstruction | The paper establishes two linked same-configuration candidate pairs, but its scientific result is an unresolved chirality-versus-shape-coexistence dilemma, not evidence uniquely selecting chirality. | HE03-3 to HE03-16; Abstract and Conclusion | unreviewed |
| AR-2 | Assumptions and dependencies | Absolute spins, configuration purity, missed-signature sensitivity and TRS minima all introduce model/systematics dependencies. | HE03-5, HE03-8/9, HE03-12/13 | unreviewed |
| AR-3 | Transfer conditions | DCO, angular-distribution and asymmetry values are array/gate/convention specific; only the general calibration logic is transferable. | PDF pp. 3-7 | unreviewed |
| AR-4 | Failure conditions | Different configurations, observation of incompatible signature partners, or smooth absolute strengths inconsistent with the chiral prediction would break the proposed assignment chain. | HE03-8 to HE03-16 | unreviewed |
| AR-5 | Reverse/falsification test | Measure level lifetimes and mixing ratios in both members of both pairs, extract absolute intraband/interband strengths, and compare chirality and two-minimum shape mixing on the same observable set. | HE03-15/16 | unreviewed |
| AR-6 | Research-question decision | Persist two separate candidate-pair pages and one experiment page; keep Band 5 source/nucleus-only until a later paper provides a stable identity. | Full paper | unreviewed |

### Companion Evidence Audit

- Five-band level scheme and 69 transitions: `observed` at publication level; event-level reanalysis is unavailable.
- Interband links for Bands 1/2 and 3/4: `observed`, with multipolarity/electromagnetic character constrained for selected strong links.
- Common configurations and intrinsic handedness: `expected-but-not-established`.
- Signature partners of Bands 2/4: `not-observed`; the sensitivity explanation is an author estimate.
- Band-5 20.5-keV link: `expected-but-not-established`.
- Lifetime discriminator: `not-measured` in this source.

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: early chiral candidates combine linked same-parity bands, configuration arguments and triaxial model support, but energy proximity is not unique.
- Effect of this source: `supports`, `limits`, and `competes-with`.
- Persistence decision: create a `140Eu` nucleus page, two candidate-pair pages and the Yale experiment page; add project claims that keep chirality and shape coexistence symmetric until later lifetime evidence is ingested.
- Review state: all HE03 claims and analytical reconstruction remain unreviewed and outside the paper evidence pool.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[nuclear-chirality-and-multiple-chiral-doublet-bands]] | Adds an `N=77` two-pair candidate with unusually explicit competing interpretation. |
| supports | [[chiral-doublet-bands]] | Supplies linked same-parity near-degenerate candidate pairs and configuration arguments. |
| competes-with | [[triaxial-shape-coexistence]] | The same TRS minima support an alternative same-configuration shape-coexistence reading. |
| limits | [[bm1-be2-ratio]] | Uses branching-derived ratios without lifetime-separated absolute strengths. |

## Human Review Triage

Use the canonical P0/P1/P2/P3 definitions in `system/workflows/ingest-strategies.md`.

### P0

P0: none identified.

### P1

- **HE03-10 to HE03-16 and AR-1 — candidate strength and competing interpretation.** Grounded evidence: title includes a question mark, Abstract and Conclusion retain both chirality and shape coexistence. Agent inference: neither pair should be counted as confirmed chirality. User check: confirm equal visibility of the two scenarios. Risk: turning a discrimination paper into a discovery claim.
- **HE03-5/8/9 and AR-2 — spin/configuration inference.** Grounded evidence: Band 3 spins are revised by systematics and configuration assignments combine links, selection rules and alignments. Agent inference: common configuration remains indirect. User check: verify band crosswalk and configuration labels. Risk: unstable pair identity or circular systematics.
- **HE03-6/12 — absent or conjectural companions.** Grounded evidence: Bands 2/4 lack observed signature partners and Band 5 uses an unobserved 20.5-keV link. Agent inference: sensitivity estimates do not convert absence into observation. User check: preserve `not-observed`/`expected-but-not-established`. Risk: completing the level scheme in prose.
- **HE03-7 — asymmetry sign convention.** Grounded evidence: this paper defines parallel-minus-perpendicular and magnetic-positive, opposite to Hecht 2001's printed convention. User check: ensure later cross-source tables compare electromagnetic assignments, not raw sign. Risk: reversing electric/magnetic conclusions.

### P2/P3

- P2: verify the quoted pair splittings, YRAST Ball inventory, Band-3 spin revision and Table-II ratio characterization.
- P3: review aliases, page navigation and project placement before finalization.

## Sources

- Protected BibTeX record: `hecht_2003_Evidencechiral` in `raw/zotero/wiki-inbox.bib` (read-only).
- Raw PDF: `raw/papers/2003_Hecht et al_Evidence for chiral symmetry breaking in Eu 140.pdf`.

## Day18修订：形变幅度、转轴几何与原文寿命判别

Checkpoint045重新核对全部14页文字主线，视觉核PDF9的Fig.9/10与PDF13参数/结论；Table I/II为文字选行核，未重新逐格或全图视觉重建。原HE03-1–16及其needs_review保持。旧checkpoint044尚未提交，先前自动摘要和handoff声称“已实际提交”不符Git事实，已撤回。旧result/contract-043保留为被取代的历史产物；其四条文字checks和固定passed不构成验证。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HE03-D18-1 | 撤回旧版本把1.5625称为实际两带B(E2)比、把手征严格等Qt与DSAM唯一裁判作普适定律，以及“全核至今无寿命”的断言。仅保留beta平方的条件算术，现由HE03-D18-2–5限定。 | task-correction | superseded-interpretation | checkpoint045；旧result/contract-043；PDF p.13 | true |
| HE03-D18-2 | 原p.13在hbar omega=0.30 MeV的signature-splitting讨论中印beta2=.20,beta4=-.021,gamma≈-26°与beta2=.16,beta4=-.021,gamma≈+28°；“band4 may correspond”负gamma、“band3 may correspond”正gamma是候选解释。Fig.9在p.9，计算频率=.2 MeV，caption概述beta≈.2/gamma≈±25°；Fig.8是能级系统学而非TRS图。 | model-input-and-author-interpretation | direct | PDF pp.9,13；Fig.9；Sec.III D | true |
| HE03-D18-3 | 在本任务自定义无量纲四极张量q_k=beta cos(gamma-2pi k/3)的经典高自旋条件设计中，2omega辐射强度正比横向各向异性平方。两组参数的beta平方比为1.5625，但固定同编号主轴的三个强度比为1.36234、.489184、5.53710；这些轴未认证为原TRS/PRM转轴，不是paper B(E2)预测。 | task-conditional-design | derived | PDF p.13参数；新geometry-correction-result-045的tensor/sine/axial/permutation checks | true |
| HE03-D18-4 | 同一条件张量设计允许两组不同beta/gamma具有相同2omega强度：a沿自定义轴1，b在轴1/2平面53.12221°即可得到比值1；它只证明缺少取向/波函数时反演不唯一，不是实际稳定TAC解或实验两带等强证据。 | task-counterexample | derived-and-boundary | HE03-D18-3；geometry-correction-result-045 equal_strength_witness | true |
| HE03-D18-5 | 原结论比较I≈15hbar附近手征模型所预期的带内B(E2)大跳变与形状共存的平滑增长，并要求lifetime experiments；本文未给个别绝对B(M1)/B(E2)。它不指定DSAM为唯一方法，也不能支撑2026年全核无寿命的穷尽断言；实际判别仍需branch/mixing、feeding/stopping、几何和同自旋模型矩阵元。 | author-interpretation-and-scope-boundary | direct | PDF p.11末段；p.13 Conclusion；HE03-15/16 | true |

本任务的radial幅度估计Q_beta=(3/sqrt(5pi)) Z(1.2 A^(1/3))² beta/100给3.70294和2.96235 eb，只是均匀电荷形变幅度的低阶映射；三轴体系没有据此认证唯一轴向Q0或观测Qt。旧118.4/75.8 W.u.由额外采用轴对称高自旋系数产生，撤为未认证原体系的示例值。

[新程序](../../system/scripts/day18_hecht03_140eu_shape_coexistence_audit.py)与[实际18项断言结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/hecht03-geometry-correction-result-045.json)验证哈希、原结论文字、张量恒等式、轴对称/零形变极限、轴置换不变性及同强度witness；不重现原fit/CI，不增加独立实验。原review状态不升级。
