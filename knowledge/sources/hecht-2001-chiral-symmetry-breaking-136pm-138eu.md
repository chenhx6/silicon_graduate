---
type: source
title: "Hecht et al. 2001 - Evidence for Chiral Symmetry Breaking in 136Pm and 138Eu"
aliases: [Hecht 2001 136Pm 138Eu chiral bands, 136Pm and 138Eu chiral-twin candidates]
created: 2026-08-11
updated: 2026-08-11
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Evidence for Chiral Symmetry Breaking in 136Pm and 138Eu"
authors: [A. A. Hecht, C. W. Beausang, K. E. Zyromski, D. L. Balabanski, C. J. Barton, M. A. Caprio, R. F. Casten, J. R. Cooper, D. J. Hartley, R. Krücken, D. Meyer, H. Newman, J. R. Novak, E. S. Paul, N. Pietralla, A. Wolf, N. V. Zamfir, Jing-Ye Zhang, F. Dönau]
journal: Physical Review C
year: 2001
volume: 63
pages: 051302(R)
doi: 10.1103/PhysRevC.63.051302
language: English
canonical_source: https://doi.org/10.1103/PhysRevC.63.051302
citation_key: hecht_2001_Evidencechiral
raw_file: "raw/papers/2001_Hecht et al_Evidence for chiral symmetry breaking in 136 Pm and 138 Eu.pdf"
raw_sha256: 2F9BD3DCE75EC29056EF5A59B26032A6510B7E9DC241A546A3D82A89C7EEA161
nuclei: [136pm, 138eu]
reactions: ["116Sn(24Mg,p3n)136Pm", "106Cd(35Cl,2pn)138Eu"]
experiments: [yale-yrast-ball-136pm-mg24-130-135mev, daresbury-eurogam-138eu-cl35-150mev]
models: [tilted-axis-cranking]
observables: [bm1-be2-ratio, angular-momentum-alignment]
methods: [gamma-gamma-coincidence, dco-ratio, linear-polarization-asymmetry]
tags: [experiment-ingest, project-ingest, a130, odd-odd, n75, nuclear-chirality, chiral-doublet-bands]
---

# Evidence for Chiral Symmetry Breaking in `136Pm` and `138Eu`

## Bibliographic Record

Physical Review C 63, 051302(R) (2001), DOI `10.1103/PhysRevC.63.051302`. The four-page Rapid Communication and the protected BibTeX export uniquely match `hecht_2001_Evidencechiral`.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`.
- Covered scope: complete main text, both experimental data sets, Fig. 1 partial level schemes, Fig. 2 spectrum/polarization asymmetry, Fig. 3 experimental `B(M1)/B(E2)` systematics, Table I 3D TAC results, conclusions and cited model boundaries.
- Not covered: raw coincidence cubes, event-level polarization calibration, the preliminary `136Pm` report and earlier `138Eu` spectroscopy cited by the paper, or the Starosta 2001 isotone paper used for bandhead-spin systematics.
- Coverage caveats: no supplementary material is identified. Several spins in Fig. 1 are parenthesized/tentative; bandhead spins are assigned from Ref. 6 systematics rather than independently fixed in this paper.

## Paper Question and Scientific Motivation

- The authors ask whether the recently predicted left-/right-handed aplanar geometry in odd-odd triaxial nuclei has experimental counterparts across the `N=75` isotones, using same-parity `ΔI=1` partner bands as its expected finite-spin signature (PDF p. 1 / journal p. 051302-1).
- They target new partner structures in `136Pm` and `138Eu`, where TRS calculations for the low-lying `πh11/2⊗νh11/2` configuration indicate appreciable triaxiality and the valence-particle/core angular momenta can form an aplanar triad (PDF p. 1 / journal p. 051302-1).

## Method and Design Logic

- Independent fusion-evaporation experiments populate `136Pm` and `138Eu`. γ-γ doubles/triples establish the new `ΔI=1` sequences and their links to known yrast bands (PDF pp. 1-2 / journal pp. 051302-1–2; Fig. 1).
- DCO ratios constrain relative spins and transition multipolarities in both nuclei; YRAST Ball clover polarization in `136Pm` additionally tests electric versus magnetic character for selected in-band and interband `ΔI=1` transitions (PDF pp. 2-3 / journal pp. 051302-2–3; Fig. 2).
- Transition energies, alignments and branching-derived in-band `B(M1;I→I-1)/B(E2;I→I-2)` ratios are compared between each new and yrast band. Their similarity motivates a common configuration assignment, while TRS-fed 3D TAC calculations test whether an aplanar solution gives the observed ratio scale and spin trend (PDF pp. 3-4 / journal pp. 051302-3–4; Fig. 3; Table I).

## Key Evidence and Reasoning Chain

- Coincidence placement + `ΔI=1`/`ΔI=2` multipolarity constraints + observed interband links → a new partner sequence next to the known yrast band in each nucleus (Fig. 1; PDF pp. 2-3).
- Similar transition energies, alignment and in-band `B(M1)/B(E2)` → author assignment of the new bands to the same `πh11/2⊗νh11/2` configuration as the yrast bands (PDF p. 3; Fig. 3).
- Roughly `300 keV` partner-band displacement + common assigned configuration + calculated aplanar TAC solutions → author proposal of chiral-twin candidates, with finite left/right tunnelling invoked to explain the nonzero splitting (PDF pp. 3-4; Table I).
- Diminishing calculated tilt angle `φ` at higher rotational frequency → model-predicted return to principal-axis rotation and termination of the chiral regime, rather than indefinite chirality at all spins (PDF p. 4; Table I).

## Summary

The paper reports new positive-parity `ΔI=1` bands in `136Pm` and `138Eu`, assigns them the same `πh11/2⊗νh11/2` configuration as the respective yrast bands, and offers the two pairs as chiral-twin candidates. It is direct experimental/model candidate evidence, but the conclusion does not claim a model-independent observation of broken chirality: configuration and aplanar geometry remain inferred, the partners stay about `300 keV` apart, and 3D TAC cannot calculate their quantum mixing.

## Experimental or Theoretical Setup

- `136Pm`: `116Sn(24Mg,p3n)136Pm` at `130` and `135 MeV`; two stacked `116Sn` foils, each `0.8 mg/cm²`; Yale ESTU Tandem and YRAST Ball with 18 coaxial Ge, three LEPS and four clover detectors; about `6.7×10^8` γ-γ coincidences in five days (PDF p. 1 / journal p. 051302-1).
- `138Eu`: `106Cd(35Cl,2pn)138Eu` at `150 MeV`; Daresbury Tandem and Eurogam Phase I with 45 large-volume Ge detectors; about `5.7×10^8` unfolded γ-γ coincidences (PDF pp. 1-2 / journal pp. 051302-1–2).
- 3D TAC: constant deformation/pairing parameters taken from TRS at `ℏω≈0.25 MeV`; `136Pm` uses `(ε2,ε4,γ)=(0.194,0.028,-25°)` and `138Eu` `(0.202,0.032,-24°)` (PDF p. 2 / journal p. 051302-2; Table I).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HE01-1 | 两个独立实验分别以 `116Sn(24Mg,p3n)136Pm`（130/135 MeV，YRAST Ball）和 `106Cd(35Cl,2pn)138Eu`（150 MeV，Eurogam Phase I）建立高统计 γ-γ 数据集。 | experimental-fact | direct | PDF pp. 1-2 / journal pp. 051302-1–2 | true |
| HE01-2 | doubles/triples analysis 在两核中建立新的 `ΔI=1` 带；`138Eu` 为本文首次报告，`136Pm` 则在早期 preliminary report 上补充新数据。 | experimental-fact | direct | Abstract; PDF pp. 1-2; Fig. 1 | true |
| HE01-3 | 新带含 `ΔI=1` mixed `M1/E2` 带内跃迁与 `ΔI=2` crossover `E2`，并由 `ΔI=1 M1/E2` 和 `ΔI=2 E2` links 接入对应 yrast `πh11/2⊗νh11/2` 带。 | experimental-fact | direct | PDF pp. 2-3 / journal pp. 051302-2–3; Fig. 1 | true |
| HE01-4 | DCO analysis 支持相对自旋与 multipolarity；bandhead spins 取自 Ref. 6 的 isotone systematics，而非本文独立测定。 | experimental-criterion | direct | PDF p. 3 / journal p. 051302-3, text below Fig. 2 | true |
| HE01-5 | `136Pm` 中已知 M1/E2 的平均偏振 asymmetry 分别为 `-0.055(35)` 与 `0.175(47)`；364-keV 带内及 595/684-keV 带间跃迁的 `A=-0.08(16), -0.01(12), -0.18(22)` 与 magnetic-dipole assignment 相容。 | experimental-criterion | direct | PDF p. 3 / journal p. 051302-3; Fig. 2(b) | true |
| HE01-6 | 新带与 yrast 带的 transition-energy、alignment 和 in-band `B(M1)/B(E2)` 相似，作者据此把新带指认为相同 `πh11/2⊗νh11/2` 组态。 | author-interpretation | indirect | PDF p. 3 / journal p. 051302-3; Fig. 3 | true |
| HE01-7 | 在当前可观测范围内，新带相对 yrast 对应能级约高 `300 keV`；作者把两对结构表述为 chiral-twin-band candidates。 | author-interpretation | direct | PDF p. 3 / journal p. 051302-3 | true |
| HE01-8 | 作者认为普通 principal-axis-cranking 的 unfavoured proton-signature 解释面临 `400–500 keV` 邻近奇质子 signature splitting，而实验双带约为 `300 keV`；邻区 quasiparticle 和 γ-vibrational states 也被认为更高。 | author-interpretation | indirect | PDF p. 3 / journal p. 051302-3, final paragraphs | true |
| HE01-9 | 文中以有限势垒导致左右手组态 tunnelling/mixing 来解释非零 `≈300 keV` splitting；这是引用早期工作的动力学解释，不是本文直接测量。 | author-interpretation | indirect | PDF p. 4 / journal p. 051302-4, first paragraph | true |
| HE01-10 | 3D TAC 在一段频率/自旋区间给出两个 tilt angles 均远离 `0°/90°` 的 aplanar solutions，并在 Fig. 3 再现实验 `B(M1)/B(E2)` 的量级与趋势。 | model-result | indirect | PDF pp. 2, 4 / journal pp. 051302-2, 051302-4; Table I; Fig. 3 | true |
| HE01-11 | TAC 曲线应与两条 dipole bands 的平均 ratios 比较，因为该平均场计算不能处理两条 chiral bands 之间的量子 mixing。 | model-result | direct | PDF p. 4 / journal p. 051302-4 | true |
| HE01-12 | 在 `ℏω≈0.42 MeV`（Pm）与 `≈0.35 MeV`（Eu）附近，计算的 `θ→90°`、`φ→0°`，作者据此判断 rotation 回到 principal axis、chiral structure 结束。 | model-result | indirect | PDF p. 4 / journal p. 051302-4; Table I | true |
| HE01-13 | 结论把两核的新带称为 predicted chiral-twin bands 的 “good candidates”；正文没有把候选升级为模型无关证明。 | author-interpretation | direct | PDF p. 4 / journal p. 051302-4, Summary | true |

## Nuclear Structure Information

| Nucleus | Observed pair | Experimental relation | Paper interpretation |
|---|---|---|---|
| `136Pm` | known positive-parity yrast band plus new `ΔI=1` band, with the new sequence shown approximately over `11+–15+` in Fig. 1 | mixed-dipole in-band transitions, E2 crossovers and multiple interband links; selected magnetic character checked with clover asymmetry | common `πh11/2⊗νh11/2` configuration and chiral-twin candidate |
| `138Eu` | known positive-parity yrast band plus new `ΔI=1` band, with the new sequence shown approximately over `11+–17+` in Fig. 1 | mixed-dipole in-band transitions, E2 crossovers, multiple links and a double-gated spectrum | common `πh11/2⊗νh11/2` configuration and chiral-twin candidate |

Parenthesized spins in Fig. 1 remain tentative. The pair labels above are stable page identities for this source and do not imply that later literature must preserve every level assignment unchanged.

## Authors' Interpretation

The authors interpret the two pairs within the particle-hole/core triaxial geometry proposed for `N=75` odd-odd nuclei. They reject simple exact degeneracy as a requirement at all spins, attribute the observed `≈300 keV` separation to left/right tunnelling, and use 3D TAC to support an aplanar interval followed by return to principal-axis rotation. Their calibrated endpoint is “good candidates,” despite the stronger wording in the paper title.

## Model Results

- TRS supplies fixed deformations at one reference frequency; the cited TRS result is attributed to a private communication and is not an experimental shape measurement.
- Table I gives `θ`, `φ`, spin and calculated `B(M1)/B(E2)` versus rotational frequency. For `136Pm`, the aplanar solution persists longer in the table than for `138Eu`; both trend toward `φ=0°` at their upper-frequency end.
- The solid curves in Fig. 3 reproduce the broad decrease in the ratios, but the calculation represents one intrinsic aplanar solution and cannot generate the observed quantum doublet splitting/mixing.

## Competing Interpretations and Limitations

- The authors discuss unfavoured signature, quasiparticle and γ-vibrational alternatives mainly through excitation-energy systematics; they do not calculate all alternatives against the same transition data.
- Common configuration is inferred from energy/alignment/ratio similarity, not measured by a configuration-specific observable such as a `g` factor.
- No lifetimes or absolute `B(M1)`/`B(E2)` values are reported; Fig. 3 uses ratios derived from observed decay branches.
- Bandhead spins depend on the Starosta 2001 systematics. Several Fig. 1 assignments are tentative, and the paper provides partial rather than complete level schemes.
- Near-degenerate same-parity bands plus an aplanar mean-field solution do not constitute a model-independent selection rule for chirality. Later chiral-vibration, tunnelling and configuration-mixing analyses must be compared explicitly.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-1 | Core reconstruction | This is the first direct chiral-candidate experiment in the rolling corpus: it combines linked same-parity bands, electromagnetic assignments and aplanar TAC support. The source supports a candidate interpretation, not proof of spontaneous chiral-symmetry breaking. | HE01-2 to HE01-13; especially Summary on PDF p. 4 | unreviewed |
| AR-2 | Assumptions and dependencies | The chain depends on Ref. 6 bandhead systematics, common-configuration inference, TRS deformations/pairing fixed near one frequency, branching-derived ratios and comparison of a mixed quantum doublet to an unmixed TAC solution. | HE01-4, HE01-6, HE01-10/11; Table I | unreviewed |
| AR-3 | Transfer conditions | DCO/polarization plus interband links are reusable evidence classes, but the numerical asymmetry calibration and inferred spin/configuration cannot be transferred to another array or nucleus without its own calibration and level scheme. | PDF pp. 2-3; Fig. 2 | unreviewed |
| AR-4 | Failure conditions | If later lifetime/mixing-ratio/configuration-sensitive data show different intrinsic structures, or a quantum model reproduces the same observables as a vibration/signature/mixed configuration, the present fingerprint set no longer uniquely supports chirality. | Missing observables and alternatives listed on PDF pp. 3-4 | unreviewed |
| AR-5 | Reverse/falsification test | Compare absolute in-band/interband matrix elements, measured mixing ratios and common-configuration observables with a quantum model that treats left/right tunnelling and competing γ vibration/signature structures on the same footing. | HE01-8 to HE01-11 plus source omissions | unreviewed |
| AR-6 | Research-question decision | Persist the two pair identities and project-level evidence row, then use Starosta 2001 to test whether the five-isotone systematics actually strengthen the chiral interpretation or mainly restate common fingerprints. | Full paper; Ref. 6 dependency | unreviewed |

### Companion Evidence Audit

- New bands and their in-band cascades: `observed` in Fig. 1; the `138Eu` band is also visible in the double-gated Fig. 2(a) spectrum.
- Interband links required to relate each pair: `observed` in the partial level schemes, though several weak branches lack individual quantitative discussion.
- `136Pm` magnetic character: `observed` only as calibration-consistent asymmetry for the 364/595/684-keV transitions; the uncertainties are large and do not establish all band transitions individually.
- Common intrinsic configuration and left/right handedness: `expected-but-not-established`; inferred from systematics and TAC rather than directly observed.
- Raw-event re-evaluation of weak links, DCO and asymmetry: `blocked-needs-raw/event-level data`.

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: chiral candidates require linked partner structures, electromagnetic evidence and an explicit aplanar model, while energy similarity alone is insufficient.
- Effect of this source: `supports` and `limits`.
- Reason: it supplies early direct experimental candidate evidence in two isotones and a 3D TAC comparison, but exposes dependence on tentative spins, inferred configuration, branching ratios and a model that cannot treat doublet mixing.
- Persistence decision: create source, nucleus, experiment and stable candidate-pair pages; add two candidate-evidence claims to the nuclear-chirality project. Defer synthesis/overview until the N=75 core-paper batch including Starosta 2001 is complete.
- Review state: all HE01 claims and analytical reconstruction remain unreviewed and outside the paper evidence pool.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[nuclear-chirality-and-multiple-chiral-doublet-bands]] | Adds two original-experiment candidate pairs with DCO/polarization, band links and 3D TAC support. |
| supports | [[chiral-doublet-bands]] | Provides same-parity linked doublets assigned to a common configuration and interpreted as chiral-twin candidates. |
| limits | [[static-chirality]] | The partners remain split by about 300 keV and TAC cannot treat their mixing; the paper invokes tunnelling rather than establishing a static degenerate limit. |
| methodological-bridge | [[linear-polarization-asymmetry]] | Uses YRAST Ball clover scattering asymmetry to distinguish selected magnetic and electric transitions in `136Pm`. |

## Human Review Triage

Use the canonical P0/P1/P2/P3 definitions in `system/workflows/ingest-strategies.md`.

### P0

P0: none identified.

### P1

- **HE01-7/HE01-13 and AR-1 — title versus candidate-level conclusion.** Grounded evidence: the title says “symmetry breaking,” while the Summary calls the structures “good candidates.” Agent inference: project wording must stay at candidate strength. User check: verify this calibrated historical role. Risk: converting an early fingerprint paper into a model-independent discovery claim.
- **HE01-4/HE01-6 and AR-2 — spin/configuration dependency.** Grounded evidence: bandhead spins are imported from Ref. 6 systematics and the common `πh11/2⊗νh11/2` assignment follows energy/alignment/ratio similarity. Agent inference: spin and configuration layers are not equivalent to direct measurement. User check: confirm the two dependencies remain explicit. Risk: circular isotone systematics or overconfident band identity.
- **HE01-9 to HE01-12 — tunnelling and 3D TAC boundary.** Grounded evidence: Table I/Fig. 3 use fixed TRS inputs; the paper states TAC cannot account for mixing and therefore compares the calculation with average ratios. Agent inference: aplanar support and partner splitting are joined by an interpretation, not one self-contained quantum calculation. User check: preserve model-result versus author-interpretation layers. Risk: overstating agreement as a calculation of the observed doublet.

### P2/P3

- P2: verify the approximate Fig. 1 spin ranges, selected 136Pm asymmetry values and two experiment metadata blocks.
- P3: review page aliases, candidate-pair navigation, index/project placement and rolling-WIP status synchronization.

## Extracted Pages

- Nuclei: [[136pm]], [[138eu]]
- Bands: [[136pm-chiral-twin-candidate-pair]], [[138eu-chiral-twin-candidate-pair]]
- Concepts: [[nuclear-chirality]], [[chiral-doublet-bands]], [[static-chirality]]
- Methods: [[gamma-gamma-coincidence]], [[dco-ratio]], [[linear-polarization-asymmetry]]

## Non-source Notes and Follow-up

Next corpus source: Starosta 2001. Use it to audit the imported bandhead-spin/systematics dependency and to distinguish isotone-level chiral-vibration interpretation from the candidate wording of this paper.

## Day18定量审计：3D TAC倾角塌缩、在束寿命缺失与邻核134Pr形变落差警示

在Day18正式学习中对本文Table I中3D TAC倾角演化及手征双重带寿命证据链开展定量核验，raw SHA256 `2F9BD3DCE75EC29056EF5A59B26032A6510B7E9DC241A546A3D82A89C7EEA161`已核。原HE01-1–13各claim保持；新HE01-D18-1待审。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HE01-D18-1 | 本文报道的N=75同中子素136Pm与138Eu手征候选带定量核验揭示：(1) Table I展示的3D TAC计算表明，非平面倾角phi随频率增加发生急剧塌缩：136Pm在0.425 MeV (I=18.5)处phi降为0度，138Eu在0.350 MeV (I=13.5)处phi降为0度，证明微观模型本身预言非主轴手征解仅存在于狭窄的低自旋窗口并迅速终止为平面转动；(2) 两核全无在束能级寿命测量（DSAM或RDDS均缺），所绘制的B(M1)/B(E2)比值基于两带内禀四极矩完全相同的假设；(3) 邻核N=75同中子素134Pr后续寿命测量（Petrache 2006, Tonev 2006）确凿证实两伙伴带内禀四极矩存在2.0倍巨大落差（Q_0,1/Q_0,2 = 2.0(4)），推翻了手征等形变假定；136Pm与138Eu缺乏绝对寿命使得相同假定面临完全相同的系统学风险。 | task-rate-decomposition-audit | derived-and-boundary | PDF pp.2–4, Table I, Fig. 3；新hecht01-136pm-138eu-result-042 | true |

新[分析合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/hecht01-136pm-138eu-contract-042.json)及[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/hecht01-136pm-138eu-result-042.json)4项检查全过。
