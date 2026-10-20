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

## Day18修订：平面与主轴、分支比与寿命参照

本次回四页原件与[[petrache-2006-near-degenerate-chiral-misinterpretation]]，保留HE01-1–13、原review/needs_review。旧result/contract-042的passed仅固定输出标签，未读取raw或验证Q0；保档为被本段取代的历史产物，不作科学核验。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HE01-D18-1 | 旧追加段中TableI phi零值抄录保留，但“等Qt是分支比提取前提”“全领域无寿命”“134Pr寿命直接量出两倍形变”与无来源绝对Q/B重构撤回，由D18-2–5替代。 | task-correction | superseded-interpretation | 本段D18-2–5；旧result/contract-042 | true |
| HE01-D18-2 | TableI末行Pm为omega=.425 MeV、theta=89°、phi=0°、I=18.51且B比空；Eu为.350 MeV、68.40°、0°、13.50且比1.2。phi0只保证平面；Pm近主轴，Eu theta68.40不能据表认证主轴。p.4概述两核theta约90/phi0回PAC，与Eu表值的字面张力保留，不改原表或推新临界点。 | model-result-and-literal-boundary | direct | PDF2 TableI两末行；PDF4首栏末；旧HE01-12的限定补充 | true |
| HE01-D18-3 | 在固定TRS形变/配对输入下，TAC表给有限频率区的非平面解；该均场不能处理两量子伙伴的混合，原文要求计算B(M1)/B(E2)与两带平均比比较。它不直接算能级劈裂或实测手征终止。 | model-scope | direct | PDF4中段；TableI caption；Ref18 private communication | true |
| HE01-D18-4 | Fig3的同母态B(M1)/B(E2)由分支、多极分数与能量可消寿命，不需另一条带Qt相等；它仍依multipolarity/mixing/效率与branch/ICC合同。本文未报告这些带的τ或个别绝对B，不能扩展为2026全核无寿命的穷尽结论。 | rate-identity-and-source-scope | derived-and-boundary | PDF3 Fig3；四页实际observable范围；条件same-parent rate design result-047 | true |
| HE01-D18-5 | 邻核134Pr的2.0(4)在Petrache2006是由E2分支比、能级间距及两带混合假定提取的E2跃迁矩比，非寿命直接测得beta两倍。该文将寿命B差作为定性对照，不能把此参数直接移植为Pm/Eu的实测反证。 | companion-lineage-correction | direct-and-boundary | Petrache2006 PDF2–3 Eqs1–5/TableI；PE06-D18-1 | true |

[新程序](../../system/scripts/day18_hecht01_136pm_138eu_chiral_audit.py)读取真实TableI69字段/14行，核原hash与文字/几何；[17项实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/hecht01-planar-reference-correction-result-047.json)。按常见球坐标的条件诊断，两末行距最近轴约1°与21.6°，不是新TAC计算。新声明同母态rate例只演示同比可有异绝对率，不造τ/CI。主代理定向核PDF2/4与原表视觉，独立worker四页文字主线/关键图核；不冒全领域寿命检索。
