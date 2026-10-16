---
type: source
title: "Multipole Mixing Ratios of Transitions in B 11"
aliases: [Rusev 2009 B11 mixing ratios, Rusev 2009 polarized-photon asymmetry, 11B multipole mixing ratios]
created: 2026-07-12
updated: 2026-07-12
status: ai-draft
review_status: human-reviewed
source_type: experiment-method-article
reading_depth: read
title_original: "Multipole Mixing Ratios of Transitions in B 11"
authors: [G. Rusev, A. P. Tonchev, R. Schwengner, C. Sun, W. Tornow, Y. K. Wu]
journal: Physical Review C
year: 2009
volume: 79
number: 4
pages: "047601"
doi: 10.1103/PhysRevC.79.047601
language: en
canonical_source: doi:10.1103/PhysRevC.79.047601
citation_key: rusev_2009_Multipolemixing
raw_file: "raw/papers/2009_Rusev et al_Multipole mixing ratios of transitions in B 11.pdf"
raw_sha256: ACF557C95F557A3DE075AE263E2EF3BC9F6B2E3F9E905928445DF20FAD3896F9
nuclei: []
reactions: []
observables: [multipole-mixing-ratio]
methods: [linear-polarization-asymmetry]
tags: [mixing-ratio, polarization, asymmetry, polarized-photon-beam, method-example]
---

# Rusev et al. (2009): Multipole Mixing Ratios in `11B`

## Bibliographic Record

G. Rusev et al., *Physical Review C* **79**(4), 047601 (2009), DOI `10.1103/PhysRevC.79.047601`, citation key `rusev_2009_Multipolemixing`.

The BibTeX key matches uniquely by title, year and DOI. Local file size is `317819` bytes; local timestamp `2025-03-10 15:17:33`; SHA-256 is recorded above.

## Scope and Reading Depth

The full four-page brief report was read from the PDF text layer. Key checks covered the asymmetry definition in Eq.(1), the analyzing-power relation in Eq.(2), the angular-distribution formula in Eq.(3), Table I, and the explicit Fig.4 two-solution discussion.

This is an `experiment-ingest + method-ingest` source. The `11B` nucleus here is mainly a method/calibration case. The Wiki uses this paper as an example of extracting `delta` from polarization-dependent asymmetry alone and of the resulting branch ambiguity.

## Summary

Rusev et al. determine `M1/E2` mixing ratios in `11B` by measuring the azimuthal asymmetry of gamma rays emitted after resonant absorption of nearly monoenergetic, linearly polarized photons. The method compares measured horizontal/vertical asymmetries with the predicted analyzing power for candidate `delta` values.

Its key methodological warning is explicit: the same measured asymmetry can correspond to two different `delta` solutions. The authors choose the smaller-`|delta|` branch on physical-plausibility grounds, not because the asymmetry observable alone uniquely selects it.

## Experimental or Theoretical Setup

- Photon-scattering measurements were carried out at the Duke Free-Electron Laser Laboratory / HIγS using nearly monoenergetic, linearly polarized photon beams.
- The asymmetry uses horizontal and vertical detectors and an efficiency ratio `epsilon_h / epsilon_v` calibrated with `56Co`.
- Finite-opening-angle correction `C(theta)` was obtained from GEANT3 simulations.
- The paper studies several `11B` transitions, including ground-state and branching transitions.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| RU09-1 | 本文通过 resonant absorption of linearly polarized photons 后发射 gamma rays 的 azimuthal asymmetry 来提取 `11B` 跃迁的 `M1/E2` mixing ratios。 | observed-fact | direct | p.047601-1, Abstract and opening paragraph | false |
| RU09-2 | 实验 asymmetry 定义为水平/垂直平面计数与效率比构成的量 `a`；它再通过 analyzing power 与 `P_gamma`、`W(theta,phi)`、以及 finite-opening-angle correction `C(theta)` 相联系。 | method-formalism | direct | p.047601-2, Eqs.(1)--(2) | false |
| RU09-3 | 作者用 GEANT3 为该装置给出 `C(theta)=0.950` 和 `0.941`，分别对应 `3/2 -> 5/2 -> 3/2` 与 `3/2 -> 3/2 -> 3/2` 两种自旋序列。 | observed-fact | direct | p.047601-2, paragraph below Eq.(2) | false |
| RU09-4 | Table I 报告了若干 ground-state 与 branching transitions 的 measured asymmetries 和 deduced `delta`；其中 `4443.93 keV`、`5019.08 keV` 的结果与文献值相容，而 `8916.39 keV` 在本文不支持先前给出的较大混合解。 | observed-fact | direct | p.047601-3, Table I and paragraph below | false |
| RU09-5 | 文章明确说明，predicted asymmetry 作为 `delta` 的函数会对同一个 measured asymmetry 给出两个 `delta` 解；Fig.4 就把这些双解分支画了出来。 | experimental-criterion | direct | p.047601-3, text above Fig.4; Fig.4 caption | false |
| RU09-6 | 作者没有把 asymmetry 当作可唯一选枝的证据，而是明确按物理可接受性选择较小 `abs(delta)` 的分支：他们写道另一支会对应相对已知数值“异常大”的 `E2` admixture；对 `8.916 MeV` transition 给出的另一解为 `delta=-1.30`，对应约 `63%` 的 `E2` admixture。 | author-interpretation | direct | pp.047601-3--047601-4, paragraph spanning Fig.4 and opening of p.4 | false |
| RU09-7 | 对 branching transitions，作者把 excitation transition 的 `delta_1` 不确定度通过重新计算 `delta_1 ± Delta delta_1` 的 predicted asymmetry 传播到 emission-transition `delta_2`。 | experimental-practice | direct | p.047601-4, first paragraph | false |

## Nuclear Structure Information

The `11B` transitions are treated here as a calibration and method-validation dataset. The current Wiki does not expand this into a dedicated `11B` structure map.

## Authors' Interpretation

- The polarized-photon asymmetry method provides a direct route to `delta` without additional distorted-wave or alignment models.
- The method is considered validated by the isotropic `2.125 MeV` case and the near-pure `E1` `7.283 MeV` case.
- The small-`|delta|` branch is preferred on physical grounds when asymmetry alone leaves two solutions.

## Model Results

- GEANT3 simulations are used only for finite-angle correction and efficiency support.
- The theoretical layer is the analyzing-power calculation for candidate `delta` values in the angular-distribution formalism.

## Competing Interpretations and Limitations

- The paper does not show that asymmetry alone always uniquely fixes `delta`; it explicitly shows the opposite in Fig.4.
- The chosen branch uses physical plausibility and prior knowledge about expected admixtures.
- This asymmetry observable is not the same object as in-beam clover Compton polarimetry, even though both probe polarization dependence.

## Extracted Pages

- Nuclei:
- Bands:
- Concepts:
- Methods: [[linear-polarization-asymmetry]]
- Observables: [[multipole-mixing-ratio]]
- Projects: [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]

## Personal Notes

This is a very useful counterexample to the idea that "a polarization-like observable automatically resolves `delta`." Here the asymmetry itself is measured cleanly, but the inversion to `delta` still branches, so outside information remains necessary.

## 2026-10-17 Supplement — 原件重读与后续相位批评

本节为Codex新self-audit，**不在人审范围内**。原page review、RU09-1–7及全部旧正文逐字保持；包括原RU09-6目前为false，不因project摘要曾提“待复核”或本次primed回忆误以为true而回写旧flag。新claims均needs_reviewtrue。

原4页PDF hash `acf557c95f557a3de075ae263e2ef3bc9f6b2e3f9e905928445df20fad3896f9`匹配，完整读text、视觉核pp2–4 Eq1–4、TableI、Fig1–4。source Eq3说Krane–Steffen coefficients且elastic取δ1=δ2；作者选smallroot的physical-plausibility理由及−1.30/约63%E2原文确认。标题中的“model-independent”不自动消除multipole截断、已知spin、beam/geometry和先验选择。

### 当前使用时的精确量与边界

- Eq1的Ah/Av是峰计数，须除th/tv，再用epsilon_h/epsilon_v=1.011(.010)归一；它由>2MeV的56Co线weightedmean得到，不能当每个高能physics点的独立exactefficiency。
- Eq2的a=C P_gamma Sigma，C=.950/.941由10MeV GEANT3方向响应取得，P仅称nearly100%。本任务nominal P=1是选择，不是补出的实测精度。
- 2.125MeV intermediateJ=1/2给a≈0，可检offset，但不能独立认证非零beamP×response。7.283MeV nearpureE1控制还用“小M2需异常strength”的物理合理性论证，不是无先验的独立M2零测量。
- blankcontainer控制在同beamflux条件未见可影响4.444峰的12C线，作者据此不修correction；不扩成任何背景/feeding均为0。Fig1 caption的12C4.437、正文4.439与Fig2 caption的beam8.02/正文8.92保留原出版label范围，不修raw或据caption单独改transitionidentity。
- TableI的目标energy是8916.3keV，旧summary的8916.39多出的末位不受此table支持；当前引用以原行8916.3为准，旧人审行作为历史不重写。
- branching ratios由同γareas/GEANTefficiency/W计算，δ2误差沿已选δ1±error传播；不是独立排除δ1其它根，也不自动覆盖全部non-gamma decay inventory。

[[iliadis-friman-gayer-2021-polarization-direction-correlations]] VoRp5 Sec3明确批评本篇Steffen同号文字。该作者判断与对本篇producer的实证核验有区别：本session未得到RU09程序、full response或Cov。ALPACA README又报告modified-KSW体系可以同时改incoming系数以保留same-sign convention，原review脚注尚未取得，不能只凭两个相同符号判全部实现错误。

[[polarized-photon-branch-audit]]给出来源后一致IF21定义的conditional四/两根及45°companion；数学由两个不同收缩路线核对，非本篇δ的新实验推荐。旧table值与原文−1.30保持，unrounded implementation/response未闭合仍open。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| RU09-8 | a为水平/垂直散射方向的rate/efficiency不对称，epsilon_h/v=1.011(.010)；不是outgoinggamma的ComptonA或P。 | observable-and-calibration-definition | direct | printed047601-2 Eq1/2 | true |
| RU09-9 | C=.950/.941源自作者10MeVGEANT3，Pbeam只称nearly100%；scalarC/beamuncertainty及actualΣ未给，不把本任务P1/Cnominal反演写成完整experimentalCI。 | response-and-error-boundary | direct-and-self-audit | printed047601-2 paragraphbelowEq2 | true |
| RU09-10 | 2.125isotropic与blankcontainer分别检验特定offset/contamination；7.283nearE1论证还用M2strength合理性。控制不能扩成对全部beamP/response/feeding无模型认证。 | counter-evidence-and-control-scope | direct-and-self-audit | printed047601-2 Fig1/discussion；printed047601-3 paragraphbelowTableI | true |
| RU09-11 | Eq3声明KScoefficients并取elasticδ1=δ2；IF21VoRp5对这种文字提出已发表criticism。改坐标必须连系数定义，当前未得RU09producer，不能据任务模型直接判代码错误或更正发表δ。 | phase-source-dispute-and-use-boundary | direct-and-later-source-attribution | printed047601-2 Eq3；IF21VoRp5 Sec3 | true |
| RU09-12 | TableI本线energy为8916.3，不是旧Wiki8916.39；Fig2caption beam8.02与正文8.92不一致，raw原样保留，不用caption作新能量赋值。 | print-label-boundary | direct-and-self-audit | printed047601-3 TableI/Fig2caption andbody | true |
| RU09-13 | smallroot选择以另支E2unusuallylarge为物理先验，作者−1.30约63%为radiativefraction；branchδ2和B由相同选定δ1/峰面积/GEANT推得，非独立选根measurement。 | attributed-interpretation-and-dependence | direct | printed047601-3–4 Fig4discussion/Eq4 | true |
| RU09-14 | 一致IF21摘要模型的all-real-root反演与本篇producer不等同；所选point/P1/Cnominal下5/2路径可有4根、3/2路径2根，−1.30未闭合。保留来源值和模型边界，未据此新增实测δ/置信域。 | bounded-reproduction-boundary | task-calculation | printed047601-3 TableI；IF21Eq3–9/18；本任务rootmatrix | true |
