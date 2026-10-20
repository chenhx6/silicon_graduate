---
type: source
title: "Musangu et al. 2021 - Chiral vibrations and collective bands in 104,106Mo"
aliases: [Musangu 2021 Mo chirality, 104Mo 106Mo chiral vibrations]
created: 2026-08-11
updated: 2026-08-11
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Chiral vibrations and collective bands in 104,106Mo"
authors: [B. M. Musangu, E. H. Wang, J. H. Hamilton, S. Jehangir, G. H. Bhat, J. A. Sheikh, S. Frauendorf, C. J. Zachary, J. M. Eldridge, A. V. Ramayya, A. C. Dai, F. R. Xu, J. O. Rasmussen, Y. X. Luo, G. M. Ter-Akopian, Yu. Ts. Oganessian, S. J. Zhu]
journal: Physical Review C
year: 2021
volume: 104
issue: 6
pages: 064318
doi: 10.1103/PhysRevC.104.064318
language: English
canonical_source: https://doi.org/10.1103/PhysRevC.104.064318
citation_key: musangu_2021_Chiralvibrations
raw_file: "raw/papers/2021_Musangu et al_Chiral vibrations and collective bands in Mo 104 , 106.pdf"
raw_sha256: BBFC8907CA98BCF7439EBDA321F60988FD5A3052120532A4CE1D364484912DAC
nuclei: [104mo, 106mo]
reactions: ["252Cf spontaneous fission"]
experiments: [lbnl-gammasphere-cf252-fission-mo104-106]
models: [triaxial-projected-shell-model]
observables: [angular-correlation, energy-splitting, moments-of-inertia, bm1-be2-ratio, interband-e2-strengths, angular-momentum-geometry]
methods: [gamma-gamma-gamma-coincidence, gamma-gamma-gamma-gamma-coincidence, angular-correlation]
tags: [experiment-ingest, project-ingest, even-even, a105, nuclear-chirality, chiral-vibration, spontaneous-fission, tpsm]
---

# Chiral Vibrations and Collective Bands in `104,106Mo`

## Bibliographic Record

Physical Review C 104, 064318 (2021), DOI `10.1103/PhysRevC.104.064318`. The protected BibTeX key is `musangu_2021_Chiralvibrations`.

## Scope and Reading Depth

- Completed reading depth: `deep-read`.
- Covered scope: the CHORUS cover and all fifteen article pages; complete `104,106Mo` level tables and schemes; coincidence evidence; angular correlations; chiral-candidate energy and rotational-response plots; extended negative-parity TPSM setup, energies, moments of inertia, branching-derived ratios, predicted interband E2 strengths and `104Mo` angular-momentum components.
- Not covered: raw Gammasphere event cubes, earlier level-scheme papers, the unpublished generalized-TPSM description cited as Ref.39, or the prior `106Mo` analysis cited as Ref.9 beyond what this paper restates.
- Coverage caveats: no lifetimes or absolute experimental matrix elements are measured; the interband E2 evidence central to the TPSM interpretation is predicted rather than observed; the angular-momentum-component plot is only for `104Mo`.

## Extracted Pages

- PDF pp.1-2 / article p.1: CHORUS cover, abstract, motivation and experiment.
- PDF pp.3-8 / article pp.2-7: complete level tables/schemes and detailed `104,106Mo` placement logic.
- PDF pp.9-10 / article pp.8-9: coincidence spectra for new and revised transitions.
- PDF pp.10-12 / article pp.9-11: angular correlations, spin/parity constraints and start of TPSM analysis.
- PDF pp.13-15 / article pp.12-14: TPSM energies, inertias, ratios, predicted connecting strengths, wavefunctions, angular-momentum geometry and conclusion.
- PDF p.16 / article p.15: references.

## Paper Question and Scientific Motivation

The paper asks whether newly completed negative-parity bands in soft even-even `104Mo`, together with the established `106Mo` structures, form chiral-vibrational doublets based on a common two-quasineutron configuration, and whether extended TPSM calculations reproduce their experimental fingerprints (PDF pp.2,11-15).

## Method and Design Logic

- High-fold prompt coincidences from `252Cf` spontaneous fission establish weak transitions, correct earlier placements and extend multiple collective structures (PDF pp.2-10; Figs.1-12; Tables I-II).
- Gammasphere angular correlations constrain selected spin/parity assignments and, for two `106Mo` in-band cascades, yield two-fold or single mixing-ratio solutions (PDF pp.10-12; Fig.13; Table III).
- Same-spin separations, `I(ω)`, kinematic moments and branching-derived `B(M1)/B(E2)` ratios compare proposed Bands 4 and 5 (PDF pp.11-13; Figs.14-19).
- A negative-parity extension of TPSM tests energies, transition ratios, unobserved connecting E2 strengths, configuration weights and angular-momentum components (PDF pp.11-15; Figs.17-21; Table IV).

## Summary

The experiment adds a new tentative negative-parity Band 5 in `104Mo`, adds a `3-` level to `106Mo` Band 5, and revises or extends several other collective sequences. The authors propose Bands 4 and 5 in each nucleus as soft chiral-vibrational partners: experimental same-spin separations are roughly `60 keV` in `104Mo` and `100-140 keV` in `106Mo`, and the pairs have similar rotational response. Extended TPSM gives a common `νh11/2` plus mixed `ν(d5/2,g7/2)` two-quasineutron basis and broadly reproduces energies and branching-derived ratios. However, the predicted collective interband E2 transitions are not clearly observed, some `106Mo` predicted intensities exceed experimental upper limits, model inertias show discrepancies, and the explicit angular-momentum-component geometry is shown only for `104Mo` with an axis-order workaround. The stable Wiki identity is therefore a model-supported soft chiral-vibration candidate, not observed static chirality.

## Experimental or Theoretical Setup

- LBNL Gammasphere with 101 Ge detectors and a `62 μCi 252Cf` source sandwiched between two `10 mg/cm²` Fe foils inside a `7.62 cm` plastic ball.
- Sorted data: `5.7×10^11` triple-and-higher-fold and `1.9×10^11` quadruple-and-higher-fold coincidence events; RADWARE analysis.
- Extended TPSM negative-parity space: opposite-parity two-quasiparticle excitations drawn from two major oscillator shells, with pairing plus quadrupole-quadrupole Hamiltonian.
- Adopted deformation: `ε=0.24`, `γ=20°` for `104Mo` and `γ=36°` for `106Mo`; free orbital `g` factors and spin `g` factors attenuated by `0.85`.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU21-1 | The experiment used 101 Gammasphere Ge detectors, a `62 μCi 252Cf` source, `5.7×10^11` triple-and-higher-fold events and `1.9×10^11` quadruple-and-higher-fold events. | experimental-fact | direct | PDF p.2, Sec.II | true |
| MU21-2 | In `104Mo`, the work replaces the earlier `601.6-keV` two-phonon-γ-band transition with `597.3 keV`, extends that collective structure and establishes numerous new links. | experimental-fact | direct | PDF pp.2-5; Fig.1; Table I | true |
| MU21-3 | `104Mo` Band 4 has angular-correlation-supported `4-` and `5-` states, whereas the Band-5 `5-` bandhead remains tentative from decay-pattern and energy arguments. | experimental-assignment | direct | PDF pp.10-12; Fig.13; Table III | true |
| MU21-4 | `104Mo` Bands 4 and 5 form two negative-parity sequences with same-spin separations near `60 keV` over the observed common range. | derived-observable | direct | PDF pp.4-5,11-12; Figs.1,14,16 | true |
| MU21-5 | The new `104Mo` Band 8 is tentatively assigned as a three-phonon γ-vibrational band, but a quasiparticle-band alternative is explicitly retained. | author-interpretation | direct | PDF p.7, Sec.II.A | true |
| MU21-6 | In `106Mo`, the analysis adds a new `3-` level to proposed partner Band 5 and revises/extends negative-parity Bands 4, 6 and 8 through new links and even-spin members. | experimental-fact | direct | PDF pp.5-10; Fig.2; Table II | true |
| MU21-7 | `106Mo` Bands 4 and 5 have same-spin separations of about `100-140 keV`; the new analysis and earlier data give similar rotational-response trends across the pair. | derived-observable | direct | PDF pp.11-13; Figs.14-16 | true |
| MU21-8 | The authors propose Bands 4 and 5 in each nucleus as soft chiral-vibrational partners, based on small nearly constant separations, similar `I(ω)` and model comparisons. | author-interpretation | indirect | PDF pp.11,15; Figs.14-16 | true |
| MU21-9 | The proposed microscopic structure is one `νh11/2` quasiparticle coupled with a mixed/pseudospin-related `νd5/2-νg7/2` quasiparticle, described in particle-hole language in the abstract. | model-assignment | indirect | PDF pp.2,14-15 | true |
| MU21-10 | Negative-parity TPSM calculations use `ε=0.24`, `γ=20°` for `104Mo` and `γ=36°` for `106Mo`; the generalized opposite-parity-shell implementation is cited as in preparation rather than fully documented here. | model-input | direct | PDF pp.11-12; Ref.39 | true |
| MU21-11 | TPSM broadly reproduces the energies and small pair separations, but overestimates high-spin `106Mo` energies and shows spin-dependent over/underestimation in `104Mo`, attributed to fixed deformation. | model-boundary | direct | PDF pp.13; Figs.14-17 | true |
| MU21-12 | Calculated kinematic moments show low-spin staggering unlike experiment and predict untested large high-spin staggering in `104Mo`; medium-spin averages are closer. | model-boundary | direct | PDF p.13; Fig.18 | true |
| MU21-13 | Experimental in-band `B(M1)/B(E2)` information is branching/mixing-ratio derived rather than lifetime-separated absolute strength; TPSM reproduces broad trends but not every point. | evidence-boundary | indirect | PDF pp.11-13; Table III; Fig.19 | true |
| MU21-14 | TPSM predicts `B(E2;I→I-1)_out` values about `40-90%` of stretched intraband E2 values at most spins, interpreting them as collective reorientation rather than two unrelated configurations. | model-result | direct | PDF pp.13-14; Fig.20 | true |
| MU21-15 | The predicted connecting transitions are not clearly identified experimentally; Table IV gives `106Mo` upper limits below several predictions and no printed experimental limit for the two listed `104Mo` cases. | counter-evidence | direct | PDF p.14; Table IV | true |
| MU21-16 | TPSM wavefunctions contain two related two-quasineutron configurations whose projected `K` weights differ between partners; this is a model explanation of reorientation, not a measured configuration. | model-result | direct | PDF p.14 | true |
| MU21-17 | Nonzero and pairwise similar squared angular-momentum components are shown only for `104Mo`; the calculation uses `γ=100°` instead of `20°` to mitigate truncation-related errors and asserts that this only permutes intrinsic axes. | model-boundary | direct | PDF pp.14-15; Fig.21 caption | true |
| MU21-18 | A sharp calculated change at `I=17` in the `104Mo` partner is assigned to a four-neutron crossing; no experimental partner-band data at that spin test the prediction. | model-boundary | direct | PDF pp.13-15; Figs.18-21 | true |
| MU21-19 | No lifetime, absolute transition-probability, polarization or direct observation of the predicted collective interband E2 network is reported for either proposed pair. | evidence-gap | direct | Full paper; Tables I-IV | true |
| MU21-20 | The paper's “pseudospin pair” denotes the `d5/2-g7/2` single-particle sector inside the two-quasineutron model basis; it does not establish pseudospin-chiral quartet bands. | terminology-boundary | indirect | PDF pp.14-15 | true |

## Nuclear Structure Information

| Nucleus | Experimental structure | Interpretation boundary |
|---|---|---|
| `104Mo` | completed/revised collective level scheme; negative Bands 4 and 5 separated by about `60 keV` over common spins | Band-5 parity is tentative; TPSM geometry only, no observed connecting E2 network or lifetimes |
| `106Mo` | extended negative Bands 4 and 5, including a new `3-` Band-5 level; separation about `100-140 keV` | no angular-momentum-component plot for this nucleus; several predicted connecting intensities meet upper-limit tension |

## Competing Interpretations and Limitations

- Near-degenerate bands plus similar rotational response are not a model-independent chirality criterion; ordinary configuration mixing or another collective vibration remains possible.
- The predicted large interband E2 collectivity is the main discriminator against two unrelated quasineutron configurations, but the relevant transitions are not established.
- The negative-parity TPSM extension is not fully documented in this paper, fixed deformation drives visible discrepancies, and the `γ=100°` axis-order workaround deserves code-level audit.
- Branching-derived ratios do not substitute for partner-resolved absolute matrix elements.
- The `104Mo` and `106Mo` analyses use acquisition descriptors matching the Luo 2009 `252Cf` dataset; until run-level provenance is independently documented, they are treated as a shared evidence lineage rather than experimental replication.

## Analytical Reconstruction

| ID | Audit item | Agent judgment | Evidence / locator | review_status |
|---|---|---|---|---|
| AR-1 | Core reconstruction | The experimental result is two close negative-parity sequences in each nucleus; “soft chiral vibration” is the joint spectrum-plus-TPSM interpretation. | MU21-3/4, MU21-6 to MU21-8 | unreviewed |
| AR-2 | Strongest discriminator | A measured collective `I→I-1` E2 network would support reorientation of one triaxial density; only TPSM values and weak/upper-limit comparisons are available. | MU21-14/15/19 | unreviewed |
| AR-3 | Geometry boundary | The component geometry is model-derived, restricted to `104Mo`, and affected by an explicit intrinsic-axis reordering workaround. | MU21-16 to MU21-18 | unreviewed |
| AR-4 | Reverse test | Lifetimes plus mixing ratios should determine absolute in-band and interband E2/M1 strengths for both members and test Table-IV predictions directly. | MU21-13 to MU21-15, MU21-19 | unreviewed |
| AR-5 | Terminology | The orbital pseudospin pair inside a two-quasineutron configuration must not be conflated with the four-band pseudospin-chiral quartet mechanism. | MU21-9/20 | unreviewed |
| AR-6 | Research decision | Persist both nuclei as soft chiral-vibration candidates, with `104Mo` carrying the explicit TPSM geometry and `106Mo` carrying the sharper interband-upper-limit tension. | Full paper | unreviewed |

### Companion Evidence Audit

- Bands, levels, links and selected angular correlations: `observed/assigned`.
- Close pair energies and rotational response: `derived from observed level schemes`.
- Common configuration and left/right combinations: `TPSM interpretation`.
- Collective interband E2 network: `predicted, not clearly observed`.
- Static chirality: `not established`; source concludes soft chiral vibration.

## Knowledge Impact and Learning Decision

- Effect: adds `104Mo` to the even-even chiral-vibration candidate set and reanalyzes `106Mo` with a common TPSM framework.
- Persistence: source, two nucleus pages, two stable candidate-pair pages and one analysis-specific experiment page; extend [[chiral-vibration]] and the chirality project.
- Review state: all `MU21-*` and AR claims remain unreviewed and outside the paper evidence gate.

## Human Review Triage

### P0

P0: none identified.

### P1

- **MU21-3/4/6/7 — level identity.** Verify precise common-spin ranges and tentative signs against Figs.1-2 before numerical reuse.
- **MU21-13 — ratio semantics.** Keep branching/mixing-ratio-derived values separate from absolute lifetime strengths.
- **MU21-14/15 — decisive but missing links.** Do not report predicted collectivity as observed evidence; preserve the `106Mo` upper-limit tension.
- **MU21-17 — geometry implementation.** Review the `γ=20°→100°` axis-order statement before using component plots quantitatively.
- **MU21-20 — pseudospin terminology.** Do not connect this two-orbital basis automatically to pseudospin-chiral quartets.

### P2/P3

- P2: compare the revised `106Mo` Band-5 `12-` identity with Refs.9 and 44.
- P3: confirm whether the Musangu and Luo papers reuse the identical raw run or only the same acquisition configuration.

## Related Knowledge and Project Relations

- [[104mo-bands-4-5-soft-chiral-vibration-candidate]], [[106mo-bands-4-5-soft-chiral-vibration-candidate]].
- [[lbnl-gammasphere-cf252-fission-mo104-106]].
- [[chiral-vibration]], [[triaxial-projected-shell-model]] and [[nuclear-chirality-and-multiple-chiral-doublet-bands]].

## Sources

- Protected BibTeX record: `musangu_2021_Chiralvibrations` in `raw/zotero/wiki-inbox.bib` (read-only).
- Raw PDF: `raw/papers/2021_Musangu et al_Chiral vibrations and collective bands in Mo 104 , 106.pdf`.

## Day18定量审计：Table IV跨带跃迁理论预测与实验上限张力对账

**checkpoint047更正：旧MU21-D18-1的过强解释部分已superseded。** 下列旧行原文保留为审计历史；“1σ上限”“刚性真实B(E2)界限”“104Mo低于探测灵敏度一个数量级”及历史范围的寿命全无断言不再沿用。真实表值、条件缩放与证据边界由MU21-D18-2–8承接，原MU21-1–20及既有review/flags不变。

在Day18正式学习中对本文Table IV预测的带间跃迁几率与探测上限开展定量对账，raw SHA256 `BBFC8907CA98BCF7439EBDA321F60988FD5A3052120532A4CE1D364484912DAC`已核。原MU21-1–21各claim保持；新MU21-D18-1待审。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU21-D18-1 | 本文Table IV针对104,106Mo预测的带间I->I-1跃迁强度与实验上限定量对账揭示：(1) 在106Mo中，自旋7、8、9处TPSM理论计算强度I_theo分别为0.26、0.20、0.12，系统性超出实验1sigma上限（分别为<0.20、<0.15、<0.10）达20%至33.3%，将真实跨带比值B(E2)_out/B(E2)_in分别刚性限制在<=0.226、<=0.574与<=0.621（显著低于模型声称的0.294、0.766与0.745）；(2) 在104Mo中，预测跨带强度（0.006与0.0038）因低跃迁能量受到(E_in/E_out)^5相空间严重压低，整整低于探测灵敏度一个数量级，导致104Mo对三轴电荷密度重取向的集体E2增强完全缺乏实验观测支撑；(3) 两核负宇称带均无DSAM或RDDS能级寿命测量，绝对B(E2)与B(M1)完全未定，证明在缺乏寿命测量时，单凭微观模型预测的集体跨带E2不能直接等价于手征对称破缺实验事实。 | task-rate-decomposition-audit | derived-and-boundary | Table IV, Fig. 20；新musangu21-mo104-106-result-036 | true |

旧[分析合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/musangu21-mo104-106-contract-036.json)及[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/musangu21-mo104-106-result-036.json)保留用于追踪历史输入和算术。合同中的`status: passed`为固定输出标签，脚本没有恢复上限构造、验证置信水平或重拟合实验，不能视为四项科学结论已验证；原件未被改写，本次未运行会覆盖旧输出的脚本。

## Day18 checkpoint047更正：Mo跨带相对强度、打印上限与共享输入边界

本次回读CHORUS accepted manuscript封面及全部15页文章主线，视觉核对PDF p.14（印刷p.13）的Table IV/Fig.20；原raw哈希与本页一致。未取得原始event、逐行上限gate/count/background/efficiency producer、完整Cov或TPSM实际作业，未进行历史寿命文献穷尽检索。下列为Codex定向self-audit，新增行保留`needs_review: true`，不改变原审核状态。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU21-D18-2 | Table IV给出106Mo自旋7、8、9的预测相对γ强度0.26、0.20、0.12，与打印实验上限<0.20、<0.15、<0.10比较；按打印中央值超出30.0%、33.3%、20.0%。自旋12为0.020与<0.02，在打印精度上接近边界。这是数值比较，不是统计显著性或拒绝判决。 | task-table-audit | direct-and-derived | PDF p.14/印刷p.13 Table IV及右栏讨论 | true |
| MU21-D18-3 | Table IV及相邻正文没有说明上限的置信水平、1σ定义或构造方法，不能称其为“实验1σ上限”。正文仅称部分理论预期略高于实验上限；不能从其它角关联段的1σ措辞移植该表的统计语义。 | evidence-boundary | direct-and-boundary | PDF p.14/印刷p.13 Table IV及其后段落；对照PDF pp.10–11角关联讨论 | true |
| MU21-D18-4 | 表中B(E2)out/B(E2)in是TPSM对Band 5→Band 4的I→I−1与Band 5内I→I−2的计算强度比；Iγ-theo由该比值结合实测带内E2强度，并考虑连接线M1/E2混合而得，不是独立于实验归一的纯理论概率。Tables I–II的相对γ强度分别以104Mo192.0 keV、106Mo171.5 keV线归一为100(5)；Table IV未另给绝对单位或独立归一。 | model-data-input-contract | direct | PDF p.3 Table I caption；p.5 Table II caption；p.14 Table IV caption及左栏末段 | true |
| MU21-D18-5 | 若保持作者所用实测带内归一、混合修正及全部强度转换条件不变，按RE2模型值×I上限/I预测可得106Mo自旋7、8、9的条件代理界限约0.22615、0.5745、0.62083。它们不是原文直接测得或无条件刚性的B(E2)界限；缺少原producer、相关误差与模型误差，不能据此建立真实分支置信区间。 | task-conditional-rescaling | derived-and-boundary | PDF p.14 Table IV及强度构造段；本次固定输入比例复算 | true |
| MU21-D18-6 | 104Mo自旋7、8的Table IV预测相对γ强度为0.006、0.0038，Eγ为273.2、321.0 keV；实验上限栏均为空白。作者称预测线通常过弱、至少比馈入同态的其它强线弱一个数量级，该比较对象不是一条已标定的探测阈值，不能由空白栏补造低于探测灵敏度的倍数。 | observed-table-and-boundary | direct | PDF p.14/印刷p.13 Table IV及右栏首段 | true |
| MU21-D18-7 | 条件采用同母态纯E2分量的通常率公式，低连接线能量会带来(Eout/Ein)^5抑制；对104Mo表中两行及Band 5带内392.4、474.9 keV参考线，该因子约0.1636、0.1411。但实测带内强度、M1/E2修正等同样参与Table IV的Iγ-theo，不能把全部预测强度归因于能量，也不能称已复现原强度producer。 | our-inference | conditional-derived | PDF p.3 Table I中Band 5参考线；p.14 Table IV及混合修正说明 | true |
| MU21-D18-8 | 本文没有报告所提双带的DSAM/RDDS寿命或实验绝对B(E2)/B(M1)测量；Fig.20的绝对B(E2)out来自TPSM，连接E2网络未被清楚识别。结论为模型支持的soft chiral-vibrational候选，不应把预测集体性等同实测静态手征破缺；本次未检索核验其它文献中是否存在相关寿命资料。 | evidence-boundary | direct-and-boundary | PDF pp.2–12实验方法/结果；pp.13–15 Figs.19–21、Table IV及结论 | true |
