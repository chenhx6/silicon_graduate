---
type: source
title: "Suzuki et al. 2008 - Lifetimes of candidate chiral doublets in 103,104Rh"
aliases: [Suzuki 2008 Rh lifetimes, 103Rh 104Rh RDDS lifetimes]
created: 2026-08-11
updated: 2026-08-11
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Lifetime measurement of candidate chiral doublet bands in the 103,104Rh isotopes with the recoil-distance Doppler-shift method in inverse kinematics"
authors: [T. Suzuki, G. Rainovski, T. Koike, T. Ahn, M. P. Carpenter, A. Costin, M. Danchev, A. Dewald, R. V. F. Janssens, P. Joshi, C. J. Lister, O. Möller, N. Pietralla, T. Shinozuka, J. Timár, R. Wadsworth, C. Vaman, S. Zhu]
journal: Physical Review C
year: 2008
volume: 78
pages: 031302(R)
doi: 10.1103/PhysRevC.78.031302
language: English
canonical_source: https://doi.org/10.1103/PhysRevC.78.031302
citation_key: suzuki_2008_Lifetimemeasurement
raw_file: "raw/papers/2008_Suzuki et al_Lifetime measurement of candidate chiral doublet bands in the Rh 103 , 104.pdf"
raw_sha256: F9C421090B33DA94206F9D1D4EBD36AD0F5BE79EE1DCD6A19FE38B32A7EC5927
nuclei: [103rh, 104rh]
reactions: ["11B(96Zr,4n)103Rh", "11B(96Zr,3n)104Rh"]
experiments: [atlas-gammasphere-rdds-103rh-104rh-zr96-330mev]
models: [particle-rotor-model]
observables: [lifetime, bm1, be2, bm1-be2-ratio, energy-staggering-parameter]
methods: [recoil-distance-doppler-shift, differential-decay-curve-method, gamma-gamma-coincidence]
tags: [experiment-ingest, project-ingest, a100, nuclear-chirality, lifetime, rdds, inverse-kinematics]
---

# Lifetimes of Candidate Chiral Doublets in `103,104Rh`

## Bibliographic Record

Physical Review C 78, 031302(R) (2008), DOI `10.1103/PhysRevC.78.031302`. The protected BibTeX key is `suzuki_2008_Lifetimemeasurement`.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`.
- Covered scope: all five PDF pages; motivation and chirality criteria; inverse-kinematics RDDS setup; direct- and indirect-feeding DDCM equations; Tables I-V; lifetime and reduced-probability extraction; staggering comparison; interpretation and requested future tests.
- Not covered: raw coincidence matrices, detector efficiency files, the earlier level-scheme papers that supply energies/branching ratios, or the cited particle-rotor calculations in their original sources.
- Coverage caveat: lifetimes are measured for only one member of each proposed doublet. The paper does not provide an absolute-strength comparison between partner bands.

## Extracted Pages

- PDF p.1: experimental chirality criteria, prior candidate context and configuration expectations.
- PDF p.2: `103,104Rh` energy/`S(I)` systematics, inverse-kinematics Gammasphere-plunger setup and DDCM equations.
- PDF p.3: RDDS spectra, Tables I-III, extracted lifetimes and absolute `B(M1)`/`B(E2)` values.
- PDF p.4: staggering systematics, comparison with A≈130 candidates, interpretation and explicit partner-band decision test.
- PDF p.5: references.

## Paper Question and Scientific Motivation

The paper asks what absolute electromagnetic information can be obtained for the proposed `103Rh` and `104Rh` chiral doublets and whether the previously reported odd-even staggering of `B(M1)/B(E2)` originates in `B(M1)` or `B(E2)`. It frames two experimental requirements for chirality: nearly degenerate same-configuration `ΔI=1` bands and similar in-band/interband electromagnetic properties (PDF p.1).

## Method and Design Logic

- A `96Zr` beam at `330 MeV` on a thin `11B` target populates `103Rh` through 4n evaporation and `104Rh` through 3n evaporation in inverse kinematics (PDF p.2).
- Gammasphere plus the Cologne plunger separates shifted and unshifted components at seven target-degrader distances. A `93Nb` degrader reduces but does not stop the recoils (PDF pp.2-3; Fig.2).
- DDCM uses a direct feeding gate when clean. If that feeder is contaminated, an upper transition and an intensity correction are used (PDF p.2, Eqs.1-2).
- Lifetimes, prior branching ratios and an assumed pure-M1 character for `I→I-1` transitions yield absolute `B(M1)` and `B(E2)` values (PDF p.3; Tables I-III).

## Summary

Three candidate-band lifetimes in `103Rh` and five in `104Rh` are reported. In both nuclei `B(M1)` decreases with spin, while weak odd-even staggering lies in `B(E2)` and therefore drives the previously reported `B(M1)/B(E2)` staggering. This is a useful absolute-strength constraint, but not a completed chiral-partner test: the measured values belong to one candidate-band member in each nucleus, and the authors explicitly require higher-spin and partner-band lifetimes. They give conditional outcomes—convergent partner properties would support chiral rotation; persistent differences or absence of convergence would disfavor it (PDF p.4).

## Experimental or Theoretical Setup

- `11B(96Zr,4n)103Rh` and `11B(96Zr,3n)104Rh` at `330 MeV`, Argonne Tandem Linear Accelerator System.
- `300 μg/cm²` `11B` target deposited on `4 mg/cm²` `93Nb`; `3.5 mg/cm²` `93Nb` degrader.
- Gammasphere with 101 Compton-suppressed Ge detectors and Cologne plunger.
- Seven target-degrader distances from `8` to `100 μm`; about `4×10^8` unfolded twofold-or-higher events per distance.
- Mean velocities before the degrader: `β=5.1(1)%` (`103Rh`) and `5.7(3)%` (`104Rh`); after it: `3.1(1)%` and `3.3(2)%`.
- Seven forward/backward analysis rings at `35°, 50°, 58°, 122°, 130°, 146°, 163°`; middle rings serve only as cleaning gates for `104Rh` and are excluded for `103Rh` because of low statistics.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SU08-1 | The single inverse-kinematics experiment populated `103Rh` and `104Rh` via 4n and 3n evaporation and measured shifted/unshifted γ components at seven distances. | experimental-fact | direct | PDF p.2 | true |
| SU08-2 | The degrader geometry enabled sub-picosecond sensitivity but deliberately did not stop the recoils; target/degrader transit was kept below `0.2 ps`. | experimental-fact | direct | PDF p.2 | true |
| SU08-3 | Direct-feeder DDCM and an intensity-corrected upper-gate variant were used; the latter supplies the starred `103Rh` lifetimes in Table I. | method-result | direct | PDF pp.2-3; Eqs.1-2; Table I | true |
| SU08-4 | `103Rh` Table I reports seven lifetimes, including candidate Band-3 values `0.99(27), 0.95(17), 1.0(1), 0.72(23) ps` for `23/2+` through `29/2+`. | experimental-fact | direct | PDF p.3; Table I | true |
| SU08-5 | `104Rh` lifetimes are `6.21(45), 1.25(9), 1.34(12), 1.05(10), 0.71(19) ps` for `9−` through `13−`. | experimental-fact | direct | PDF p.3; Table II | true |
| SU08-6 | Absolute `B(M1)`/`B(E2)` values are tabulated for `103Rh` Band 3 at `25/2+–29/2+` and for the measured `104Rh` sequence at `9−–13−`; no partner-band absolute strengths are tabulated. | experimental-fact | direct | PDF p.3; Table III | true |
| SU08-7 | The `B(M1)` extraction assumes pure M1 multipolarity and imports transition energies/branching ratios from earlier experiments. | model-boundary | direct | PDF p.3 | true |
| SU08-8 | In both nuclei `B(M1)` decreases with spin while `B(E2)` shows weak odd-even staggering; the ratio staggering is therefore attributed to `B(E2)`. | derived-observable | direct | PDF pp.3-4; Fig.3; Tables IV-V | true |
| SU08-9 | The measured staggering differs from cited A≈130 cases, where the authors report the dominant odd-even variation in `B(M1)` rather than `B(E2)`. | author-comparison | indirect | PDF p.4; Tables IV-V | true |
| SU08-10 | The observed bandheads, `23/2+` in `103Rh` and `8−` in `104Rh`, are interpreted as compatible with perpendicular semiclassical coupling for the assigned configurations. | author-interpretation | indirect | PDF p.3 | true |
| SU08-11 | The decrease of `B(M1)` is not uniquely interpreted: cited PRM results connect it with evolving valence-particle angles, while a shape change and particle-shape coupling remain alternatives. | author-interpretation | indirect | PDF p.3 | true |
| SU08-12 | Near-constant `S(I)` and energy degeneracy below `400 keV` in `103Rh` are cited as candidate fingerprints, with core structure inferred to influence isotopic degeneracy strongly. | author-interpretation | indirect | PDF p.2; Fig.1 | true |
| SU08-13 | The measurements cover one member of each proposed doublet, not both partners; the authors call partner-band and higher-spin lifetimes absolutely necessary. | evidence-boundary | direct | PDF pp.3-4; Tables I-III; Summary | true |
| SU08-14 | Similar partner-band `B(M1)`/`B(E2)` behavior, or convergence at high spin together with energy degeneracy, is proposed as support; failure of both outcomes would indicate nonchiral bands. | author-proposed-test | direct | PDF p.4 | true |
| SU08-15 | Consequently, this paper strengthens the lifetime baseline but does not itself verify the identical-electromagnetic-properties criterion for either doublet. | analytical-inference | direct | SU08-6, SU08-13/14 | true |

## Nuclear Structure Information

| Nucleus | Candidate configuration | Measured member | Evidence boundary |
|---|---|---|---|
| `103Rh` | `πg9/2^-1⊗ν(h11/2)^2`, bandhead `23/2+` | Band 3 candidate states; absolute values reported at `25/2+–29/2+` | partner-band lifetimes absent |
| `104Rh` | `πg9/2^-1⊗νh11/2`, bandhead `8−` | one candidate sequence; absolute values reported at `9−–13−` | partner-band lifetimes absent |

## Competing Interpretations and Limitations

- Absolute transition strengths for one band cannot establish equality of two partner bands.
- `B(M1)` values depend on the pure-M1 assumption; mixing ratios are not measured here.
- Energies and branching ratios come from earlier experiments and are not independently redetermined in this RDDS paper.
- The cause of decreasing `B(M1)` and `B(E2)` staggering is unresolved; angular-momentum recoupling and shape evolution remain possible.
- The comparison between `103Rh` and `104Rh` is an isotopic/systematic comparison, not a substitute for within-nucleus partner-band symmetry.

## Analytical Reconstruction

| ID | Audit item | Agent judgment | Evidence / locator | review_status |
|---|---|---|---|---|
| AR-1 | Core reconstruction | The durable result is an absolute-strength baseline and a localization of ratio staggering in `B(E2)`, not confirmation of chirality. | SU08-6, SU08-8, SU08-13 | unreviewed |
| AR-2 | Assumptions | Pure-M1 transitions and imported branching ratios enter the strength extraction; the band configurations are prior/model-supported assignments. | PDF pp.1,3 | unreviewed |
| AR-3 | Transfer conditions | The inverse-kinematics degrader/DDCM design is transferable to short-lived high-spin states, but its velocity, foil and distance parameters are experiment-specific. | SU08-1 to SU08-3 | unreviewed |
| AR-4 | Failure condition | If partner-band strengths remain different and do not converge where energies approach, the paper's stated test classifies the pair as nonchiral. | SU08-14 | unreviewed |
| AR-5 | Reverse test | Measure higher-spin and partner-band lifetimes with mixing ratios, then compare both bands' in-band and interband matrix elements using the same model. | PDF p.4 | unreviewed |
| AR-6 | Research decision | Retain both pairs as candidates with a one-sided lifetime constraint; never label the paper as an electromagnetic equality test already passed. | Full paper | unreviewed |

### Companion Evidence Audit

- Candidate-band energy/`S(I)` fingerprints: `observed/derived from earlier schemes`.
- One-member lifetimes and absolute strengths: `observed/derived in this experiment`.
- Partner-band equality: `not measured`.
- Perpendicular/aplanar geometry: `model/systematics interpretation, not directly observed`.
- Origin of `B(E2)` staggering: `not understood` in the source.

## Knowledge Impact and Learning Decision

- Effect: `supports` a lifetime-constrained candidate baseline, `limits` claims based on ratio staggering, and `requires` partner-band measurements.
- Persistence: create source, experiment, two nuclei and two candidate-pair pages; extend the RDDS method page and the chirality evidence map.
- Review state: all `SU08-*` and AR claims remain unreviewed and outside the paper evidence gate.

## Human Review Triage

### P0

P0: none identified.

### P1

- **SU08-6/13/15 — one-sided lifetime scope.** Confirm that no wording implies both partner bands were measured.
- **SU08-7 — strength-extraction assumptions.** Preserve pure-M1 and imported-branching dependencies.
- **SU08-8/9 — staggering origin.** Keep the source's `B(E2)` attribution distinct from the A≈130 `B(M1)` comparison.
- **SU08-10/11 — geometry versus alternatives.** Treat perpendicular coupling as interpretation and preserve shape change as an alternative.

### P2/P3

- P2: verify earlier-paper band-number crosswalks before assigning a stable label to the unmeasured partners.
- P3: review navigation and notation before finalization.

## Related Knowledge and Project Relations

- [[103rh-chiral-doublet-candidate]] and [[104rh-chiral-doublet-candidate]].
- [[atlas-gammasphere-rdds-103rh-104rh-zr96-330mev]].
- [[recoil-distance-doppler-shift]].
- [[nuclear-chirality-and-multiple-chiral-doublet-bands]].

## Sources

- Protected BibTeX record: `suzuki_2008_Lifetimemeasurement` in `raw/zotero/wiki-inbox.bib` (read-only).
- Raw PDF: `raw/papers/2008_Suzuki et al_Lifetime measurement of candidate chiral doublet bands in the Rh 103 , 104.pdf`.


## Day18定量审计：B(M1)/B(E2)交错的物理成因——B(E2)交错而非B(M1)交错

在Day18正式学习中对本文Table I–III中103,104Rh候选手征带的寿命与跃迁几率进行定量审计，raw SHA256 `f9c421090b33da94206f9d1d4ebd36ad0f5be79ee1dcd6a19fe38b32a7ec5927`已核。原SZ08-1–9各claim及review状态保持；新SZ08-D18-1待审。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SZ08-D18-1 | 对Table III中104Rh（10−–13−）和103Rh（25/2+–29/2+）的定量分析揭示：文献中广泛观察到的 $B(M1)/B(E2)$ 奇偶自旋交错（104Rh中依次为 15.1, 9.8, 11.3, 6.3）完全是由 $B(E2)$ 自身的奇偶交错（0.063, 0.093, 0.039, 0.067 e²b²）所驱动；与此同时，两核的 $B(M1)$ 随自旋单调平滑递减（104Rh为 0.95, 0.91, 0.44, 0.42 $\mu_N^2$；103Rh为 2.3, 1.8, 1.2 $\mu_N^2$），完全不存在奇偶交错。这与教科书基于左右手征隧穿预测的“$B(M1)$ 交错而 $B(E2)$ 平滑”形成尖锐反例，证明单纯 $B(M1)/B(E2)$ 比值交错不足以诊断手征几何。 | task-staggering-origin-audit | derived-and-boundary | PDF pp.3–4 Tables I–III, Fig.3；新suzuki08-rh103-104-result-016 | true |

新[分析合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/suzuki08-rh103-104-contract-016.json)及[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/suzuki08-rh103-104-result-016.json)5项检查全过，确立了绝对寿命测量在解耦 $B(M1)$ 与 $B(E2)$ 机制中的不可替代性。

## Day18限定补充：单调中心、交错诊断与跨论文身份

旧SZ08-D18-1所列原TableIII中心值保持，但其中“完全没有交错/完全由分母驱动”只应作为作者对有限点模式的解释，不能当已做趋势/协方差检验的百分之百因果证明；旧artifact保档，不改原SZ08-1–9及reviewflags。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SZ08-D18-2 | 原TableIII 103Rh正宇称Band3为25/2+/27/2+/29/2+，BM1=2.3/1.8/1.2、BE2=.077/.14/.11；104Rh10−–13−为BM1=.95/.91/.44/.42、BE2=.063/.093/.039/.067。原作者据BM1下降/BE2弱交错解释比值模式；B仍依纯M1及引用的能量/分支，不增加独立观测。 | reported-input-and-author-interpretation | direct | PDF3 TableIII/Fig3及其前两段 | true |
| SZ08-D18-3 | 新条件诊断选择S[x]=ln x_next−2ln x+ln x_prev，则S[M1/E2]=S[M1]−S[E2]。上述单调BM1中心的S不为零，故“单调”不等价于任意去趋势后交错幅度零；该任意诊断不是物理交错唯一分解，不反驳作者的定性模式描述，也不是显著性或CI。 | task-conditional-central-diagnostic | derived-and-boundary | TableIII中心；parent-branch-exercise-result-048 suzuki_central_curvature | true |
| SZ08-D18-4 | 本文正宇称103Rh Band3不能因相同编号而当作Kuti2014负宇称Bands3–6的寿命测量。后者旧脚本.46/.40/.35及.18/.35/.20也不在本TableIII，均不能用于推前者或后者的实验因果结论。 | cross-paper-identity-correction | direct-and-boundary | PDF3 TablesI/III；[[kuti-2014-multiple-chiral-doublets-103rh]] KU14-D18-2–11 | true |

本次独立worker针对实际主线与TableIII核验；主代理新读PDF3和原表视觉，不声称重新全文原读。新[程序](../../system/scripts/day18_parent_branch_identity_controls.py)只把打印中心作明示诊断，不提原τ/强度误差或新CI。
