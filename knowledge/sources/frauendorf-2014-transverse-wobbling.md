---
type: source
title: "Transverse wobbling: A collective mode in odd-A triaxial nuclei"
aliases: [Frauendorf and Donau 2014, transverse wobbling QTR]
created: 2026-07-15
updated: 2026-10-22
status: ai-draft
review_status: unreviewed
source_type: theory-article
reading_depth: deep-read
title_original: "Transverse wobbling: A collective mode in odd-A triaxial nuclei"
authors: [S. Frauendorf, F. Donau]
journal: Physical Review C
year: 2014
volume: 89
pages: 014322
doi: 10.1103/PhysRevC.89.014322
arxiv:
language: en
canonical_source: doi:10.1103/PhysRevC.89.014322
zotero_item_key:
citation_key: frauendorf_2014_Transversewobbling
zotero_uri:
library_file:
raw_file: "raw/papers/2014_Frauendorf_Dönau_Transverse wobbling.pdf"
raw_sha256: 36794EE1308ADC1B34206CCDBF62353D6E79B3B485979E78709FD31EFE5F57E3
nuclei: [163lu, 135pr]
reactions: []
experiments: []
models: [quasiparticle-triaxial-rotor-model, harmonic-fluctuation-approximation, particle-rotor-model]
observables: [wobbling-energy, interband-e2-strengths, bm1-be2-ratio, moments-of-inertia]
methods: [frozen-alignment-approximation]
tags: [wobbling, transverse-wobbling, longitudinal-wobbling, qtr, hfa, triaxiality, alignment]
---

# Frauendorf and Donau (2014): Transverse wobbling

## Bibliographic Record

S. Frauendorf and F. Donau, *Physical Review C* **89**, 014322 (2014), DOI `10.1103/PhysRevC.89.014322`. The BibTeX key is uniquely matched as `frauendorf_2014_Transversewobbling`.

## Scientific Question and Motivation

The paper asks why wobbling frequencies in odd-A nuclei can decrease with spin, unlike the increasing frequency of a simple triaxial rotor. It develops a semiclassical interpretation in which a high-j quasiparticle is coupled either parallel or perpendicular to the rotor axis with the largest moment of inertia, and then tests the resulting picture with full quasiparticle-triaxial-rotor (QTR) calculations for `163Lu` and `135Pr`.

## Scope and Reading Depth

Full twelve-page article read. Covered: the rotor Hamiltonian and classical orbits, simple/transverse/longitudinal geometries, frozen-alignment harmonic formulas, E2/M1 matrix elements, QTR parameter sets and potential-energy discussion, the `163Lu` and `135Pr` energy and transition-strength comparisons, and the conclusions. Not covered: reanalysis of the original spectroscopy datasets or later microscopic calculations; the experimental values quoted by this theory paper remain background inputs.

## Summary

The paper develops the transverse/longitudinal QTR geometry and uses harmonic and full calculations for `163Lu` and `135Pr` to connect decreasing wobbling energy and enhanced interband E2 strength with transverse coupling. The quoted spectra are background inputs, not new measurements.

## Method and Design Logic

The authors begin with a rigid triaxial rotor and order the rotational parameters as A1 > A2 > A3, so the 3-axis has the largest moment of inertia. They add a high-j quasiparticle to the rotor Hamiltonian, derive small-amplitude wobbling expressions in the frozen-alignment approximation, and distinguish simple, transverse and longitudinal coupling by the orientation of the particle angular momentum. Full QTR calculations relax the harmonic and rigid particle-alignment assumptions; the model core remains a rigid triaxial rotor. Energies and strength comparisons retain the fitted parameters and the provenance of the experimental inputs.

## Key Results

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| F14-1 | For the rigid triaxial rotor, the Hamiltonian is written with rotational parameters A1, A2 and A3; the assumed ordering A1 > A2 > A3 corresponds to moments of inertia J1 < J2 < J3 and wobbling about the 3-axis. | method/formalism | direct | PDF pp. 2-3, Eqs. (1)-(6) | true |
| F14-2 | In the simple-rotor limit, wobbling is a small oscillation about the largest-moment-of-inertia axis and its harmonic frequency increases with total angular momentum. | model-result | direct | PDF pp. 1-3, Figs. 1 and 5, Eq. (6) | true |
| F14-3 | A transverse wobbler has the high-j particle angular momentum perpendicular to the rotor axis with the largest moment of inertia, whereas a longitudinal wobbler has it parallel to that axis. | method/formalism / author-interpretation | direct | PDF pp. 3-5, Figs. 6-11 and geometry discussion | true |
| F14-4 | In the frozen-alignment harmonic approximation, transverse coupling changes the angular-momentum dependence of the wobbling frequency so that the frequency decreases with spin over the relevant range; this decreasing trend is a model criterion, not a model-independent observation. | model-result / experimental-criterion | direct | PDF pp. 3-7, Eqs. (15)-(24) and transverse-wobbler discussion | true |
| F14-5 | The same approximation predicts enhanced interband E2 strength relative to the simple-rotor case, while E2/M1 ratios depend on the geometry, triaxiality and particle configuration. | model-result / experimental-criterion | direct | PDF pp. 5-7, electromagnetic-transition equations and discussion | true |
| F14-6 | QTR and harmonic-fluctuation calculations for `163Lu` use aligned i13/2-proton configurations and parameter sets listed by the authors; calculated energies and transition strengths are compared with previously reported TSD bands. | model-result / review-background | direct | PDF pp. 6-9, Table I and Figs. 12-15 | true |
| F14-7 | For `163Lu`, the calculated one- and two-phonon excitation energies follow the reported decreasing wobbling-energy trend qualitatively, but the QTR parameter choice and the full spin dependence remain model dependent. | model-result / limitation | direct | PDF pp. 8-10, Figs. 13 and 15 | true |
| F14-8 | For `135Pr`, the QTR calculation gives a transverse-wobbling-like low-spin branch and a minimum/instability near I = 29/2, associated in the calculation with a change in the orientation of the h11/2 proton angular momentum. | model-result / author-interpretation | direct | PDF pp. 9-11, Figs. 14 and 16 and text on the critical spin | true |
| F14-9 | Fig19为163Lu的绝对B(M1)比较，QTR/HFA高于所引实验；135Pr则是TableII发表前tentative rM1=B(M1)con/B(E2)in与QTR的比较，不是本文新测绝对B(M1)或寿命。PDF10明确完整QTR耦合非刚性，区别于HFA固定j；旧“135Pr Fig19绝对B(M1)/frozen-QTR”混写已纠正。 | model-result-and-input-identity | direct-original-and-correction | PDF9 Fig19/TableII; PDF10 firstcolumn/rightcolumn; PDF12 Ref26 | true |
| F14-10 | For `163Lu`, an interband B(E2) ratio near 0.5 +/- 0.15 for the two-phonon-to-one-phonon transition is described as roughly twice the one-phonon scale, while the QTR value is smaller; the comparison supports but does not uniquely prove the phonon assignment. | review-background / model-result / author-interpretation | direct | PDF pp. 10-11, Figs. 17-18 and two-phonon discussion | true |
| F14-11 | The fitted moments of inertia used for the QTR examples do not simply coincide with irrotational-flow or three-dimensional-cranking values; the inferred geometry is therefore conditional on the adopted parameterization. | model-result / limitation | direct | PDF pp. 6-8 and 11-12, Table I and summary discussion | true |
| F14-12 | The authors interpret the decreasing wobbling energy and enhanced interband E2 strength in selected odd-A bands as signatures of transverse wobbling, while retaining the QTR/HFA assumptions and the need for additional observables as qualifications. | author-interpretation | direct | PDF pp. 1, 9-12, Abstract and Conclusions | true |

## Analytical Reconstruction

The paper builds a bridge from angular-momentum geometry to observables in three stages. First, the rotor inertia ordering fixes the classical orbit and the reference axis. Second, a high-j particle changes the energy surface: when its alignment is transverse to the largest-MoI axis, the calculated wobbling frequency can fall with spin, unlike the simple-rotor result. Third, QTR transition matrix elements provide a joint test using excitation energies, interband E2 enhancement and M1 strength. The `163Lu` and `135Pr` comparisons are therefore model-conditioned evidence chains rather than direct measurements of a wobbling phonon or of a particle realignment path.

## Competing Interpretations and Limitations

- Frozen alignment and harmonic small-amplitude formulas are approximations; QTR parameter choices remain model dependent.
- A decreasing energy trend and enhanced E2 are conditional criteria and must be checked against signature-partner, TiP and configuration-mixing alternatives.
- The absolute B(M1) comparison in Fig.19 is for `163Lu`; the `135Pr` mismatch concerns tentative prepublication B(M1)con/B(E2)in ratios in Table II. Both motivate the authors’ discussion of missing couplings, without adding an absolute lifetime measurement.

## Assumptions, Limits and Reverse Tests

- The harmonic formulas use rigid alignment and small oscillations; a full QTR calculation is needed near a separatrix or a reorientation point.
- The fitted moments of inertia, deformation and quasiparticle configuration are not unique experimental observables. A reverse test is to vary them or use microscopic cranking inputs and check whether the energy trend survives.
- Tentative `135Pr` relative M1/E2 strengths, and the `163Lu` absolute M1 strengths, are not quantitatively reproduced by the selected QTR calculation. Core-particle coupling, triaxial softness and configuration mixing should be tested before treating the discrepancy as evidence against wobbling.
- Decreasing wobbling energy and strong E2 links are useful criteria only in combination with level assignments, parity/signature information and competing tilted-precession or signature-partner calculations.

## Related Knowledge and Project Relation

- Concepts: [[wobbling-motion]], [[transverse-wobbling]], [[longitudinal-wobbling]], [[triaxial-deformation]], [[angular-momentum-alignment]], [[signature-partner-bands]]
- Models: [[particle-rotor-model]], [[tilted-axis-cranking]], [[triaxial-particle-rotor-model]]
- Observables: [[wobbling-energy]], [[interband-e2-strengths]], [[bm1-be2-ratio]], [[moments-of-inertia]]
- Projects/synthesis: [[low-spin-wobbling-controversies]], [[wobbling-vs-signature-partner]]

This is a theory source. The `163Lu` and `135Pr` spectra and measured transition strengths cited in the comparisons are not new observations from this paper and should remain linked to their original experimental sources.

## Extracted Pages

- Nuclei: `163Lu`, `135Pr` (theory comparison; no new nucleus pages created here)
- Concepts: [[wobbling-motion]], [[transverse-wobbling]], [[longitudinal-wobbling]], [[triaxial-deformation]], [[signature-partner-bands]]
- Models/observables: [[particle-rotor-model]], [[tilted-axis-cranking]], [[wobbling-energy]], [[interband-e2-strengths]], [[bm1-be2-ratio]]
- Projects: [[low-spin-wobbling-controversies]], [[wobbling-vs-signature-partner]]

## Human Review Triage

P0:

1. **F14-1/F14-4, PDF pp. 2-7, Eqs. (1)-(6) and transverse-wobbler formulas.** Verify axis labels, moment-of-inertia ordering and the sign of the spin dependence; these definitions control the transverse/longitudinal terminology used by later source pages.
2. **F14-6/F14-7/F14-10, PDF pp. 6-11, Table I and Figs. 13, 15, 17-18.** Check which values are QTR calculations versus quoted `163Lu` data, including the two-phonon B(E2) comparison.
3. **F14-8/F14-9, PDF pp. 9-11, Figs. 14, 16 and 19.** Verify the `135Pr` critical-spin statement, the orientation language for the h11/2 proton, and the B(M1) discrepancy.

P1:

- F14-3/F14-5: check the geometry diagrams and the exact E2/M1 selection and ratio definitions.
- F14-11/F14-12: check the scope of the fitted-MoI limitation and the strength of the authors' concluding interpretation.

## Review Status

Page and all F14 claims remain unreviewed with `needs_review: true`. Human review is deferred until use: perform targeted claim review when this content is used for paper writing, a key project decision, synthesis finalization or a paper-level evidence pool.


## Day20 checkpoint044：完整QTR与HFA、归一与谱系

本session先冻结primed回忆，再读12页原件全部正文/附录/参考文献；视觉核PDF4/6/7/8/9/11的TableI/II、Eqs11–25及A1–A4、Figs12–19等相关内容，不声称每个经典轨道图均本轮新视觉审完。原source review与全部原claim flags保持，新claim为self-audit/needs_review，不是human-reviewed。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| F14-D20-R44-1 | HFA在Eq11将j视为数并用小振幅展开；Eq23近不稳定处失效。完整QTR用CQM/KKDF对角化Eq25，PDF8明确HFA预言的两带合并不出现在该完整计算，粒子转向medium；PDF10明确其耦合非刚性。不能将对HFA的frozen限制认作已核完整QTR全spin固定j。core仍假设rigid triaxial，忽略spin依赖的平均形变/MoI不等同冻结粒子角动量。 | model-implementation-scope | direct-original | PDF6 Eqs11–15/Eq23; PDF7 SecIVA/Eq25; PDF8 SecIVB; PDF10 rightcolumn | true |
| F14-D20-R44-2 | TableI的Pr ε=.16、γ26°；fit Jm/Js/Jl=21/13/4，hydro20/6/4，crank17/7/3。形变来自micro-macro minima，fit MoI由band energies调整，其余两组MoI比例来自模型而总scale也调n0能量。TableII绝对B列均cal，exp列为Matta发表前tentative ratios；不是新增绝对B/寿命或独立实验。假定j=11/2时HFA的Jc分别14.4375/7.85714/9.35，J=√I(I+1)不等I；非实际fullQTR minimum或普适29/2阈值。 | model-input-and-derived-boundary | direct-and-declared-mathematics | PDF4 TableI; PDF6 Eq24; PDF7 SecIVA; PDF9 TableII; PDF12 Ref26 | true |
| F14-D20-R44-3 | Eq16/17在同时放大Q0/Q2而固定几何/波函数时，两个E2强度同乘c²、out/in比不变。声明自由κ合同下Q→cQ、κ→κ/c保持Eq25耦合项，是代数反例，不是原作者参数可任意自由变化或原producer复现。TableII2014暂定Pr rM1(.130/.021/.010)与2015最终(.164/.035/<.016)及rE2(.92/.535/.28)与(.843/.500/>.261)不同，不混表或按独立重复合并。 | operator-scale-and-lineage | direct-and-declared-mathematics | PDF6 Eqs16–18; PDF7 Eq25; PDF9 TableII; PDF12 Ref26; Matta2015 PDF4 TableI | true |
| F14-D20-R44-4 | literal差异保留：PDF8正文印Js/Jm=2.34，而TableI Lu hydro Jm68/Js29给Jm/Js≈2.3448；PDF11附录将Qbar0与Qbar2均写含cosγ，包括EqA2。未得erratum/实际producer，不静默改成sinγ，不由正文阅读宣称公式到代码全部闭合。Fig19绝对M1属于Lu；Pr这里只比较暂定ratio。 | literal-ambiguity-and-attribution | direct-original-visual | PDF4 TableI; PDF8 SecIVB; PDF9 Fig19; PDF10; PDF11 Appendix | true |

2014暂定数据来自Ref26的private communication，2015最终表为同研究谱系的后续公开数值；实际逐event/拟合版本未得，不给两表差异显著性。作者从短轴向中轴的解释与Matta2015的明确表述相容，但不是实验直接测得的逐态角动量轨迹。原方程的literal保留不代表已判定官方排印错误。


### checkpoint045：arXiv预印本文本一致性核查

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| F14-D20-R45-1 | 对arXiv:1310.1669v2预印本全文的比对确认：预印本Appendix A式(A2)与(A4)同样保留包含cos(gamma)的字面印刷形式，正文亦保留Js/Jm=2.34字面。这证实相关符号表述是作者稿件的一贯形式，而非期刊排版单方引入；在未获得作者勘误或原始计算程序前，继续保留字面异读，不主观定性为排印错误。 | preprint-text-comparison | direct-original-comparison | arXiv:1310.1669v2 Appendix A; PDF8 Sec. IVB | true |


### checkpoint141：横向与纵向摆动模式理论几何分歧、临界自旋分岔与三级判据审计

> checkpoint146：本节121–145批次的科学认证已撤回。旧文本/输入与指纹保存在本run的history-before-repair-146.json；原始原件与既有review/flags保留。自设数值或flag的passed只验证算术，不识别实际producer、共同Cov、实验CI或唯一模式。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| F14-D20-R141-1 | checkpoint146撤回旧认证；不据此恢复错误表值、跨态强度阶梯、硬阈值或完全闭合。请使用本页较早原件纠错与checkpoint146。 | withdrawn-task-certification | rejected-and-replaced | checkpoint146; history-before-repair-146.json | true |

## checkpoint146：原件身份与推断边界更正

本轮为Codex定向self-audit；已有review_status与原claim flags不变。121–145旧认证撤回；实际新阅读范围见source-reading-scope-146.json，引用较早纠错不冒称新全文阅读。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| F14-D20-R146-1 | HFA的Jc=14.4375绑定固定fit惯量与假定j，J=√I(I+1)不等I；解到I约13.946，并非实测29/2普适阈值。横向频率可先升后降，近不稳定处HFA失效，完整QTR允许粒子重定向。141的低spin简谐趋势不是所有TW/LW唯一分类器，也不能设10W.u.普适硬阈值。 | model-domain-correction | source-and-bounded-self-audit | F14-D20-R44-1/R44-2; PDF6 Eq24 | true |
