---
type: source
title: "Calibration of Compton Polarimeters"
aliases: [Jones 2002 Compton polarimeter calibration, Compton polarimeter sensitivity calibration]
created: 2026-07-13
updated: 2026-07-13
status: active
review_status: human-reviewed
source_type: method-formalism-article
reading_depth: deep-read
title_original: "Calibration of Compton polarimeters"
authors: [G. D. Jones]
journal: Nuclear Instruments and Methods in Physics Research A
year: 2002
volume: 491
number: 3
pages: "452-459"
doi: 10.1016/S0168-9002(02)01235-4
language: en
canonical_source: doi:10.1016/S0168-9002(02)01235-4
citation_key: jones_2002_CalibrationCompton
raw_file: "raw/papers/2002_Jones_Calibration of Compton polarimeters.pdf"
raw_sha256: 96157E69E7D77F038D372F20448F59F52B89B25FDD90EDE21B88128B60688475
nuclei: []
reactions: []
observables: [gamma-ray-linear-polarization, experimental-asymmetry, polarization-sensitivity, angular-distribution-coefficient]
methods: [compton-polarimetry, angular-distribution, linear-polarization-asymmetry]
tags: [compton-polarimetry, calibration, klein-nishina, rose-brink, alignment]
---

# Jones (2002): Calibration of Compton Polarimeters

## Bibliographic Record

G. D. Jones, *Nuclear Instruments and Methods in Physics Research A* **491**(3), 452-459 (2002), DOI `10.1016/S0168-9002(02)01235-4`, citation key `jones_2002_CalibrationCompton`.

The title, author, year, DOI and local PDF match the BibTeX record uniquely. The full eight-page PDF was read, including the abstract, Sections 1-8, Eqs. (1)-(12), Table 1 and the calibration-method discussion.

## Scope and Reading Depth

This is a `formalism-ingest + calibration-method-ingest` source. It supplies the notation and calibration logic for nuclear gamma-ray Compton polarimetry. It is not a claim that every in-beam transition is fully aligned or that the special full-polarization examples apply to ordinary fusion-evaporation data.

## Summary

The paper writes the angular dependence of physical gamma-ray linear polarization in a form that separates the nuclear polarization `P(theta)` from the measured detector asymmetry `A` and the energy-dependent polarimeter sensitivity `Q(Egamma)`. It relates `P` to angular-distribution coefficients `a2` and `a4`, multipole mixing in the Rose-Brink convention, and magnetic-substate populations. It also surveys calibration reactions and explains why low-energy strip or tracking detectors require new sensitivity calibrations.

## Key Results

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| J02-1 | The paper motivates calibration for new multi-pixel strip and tracking detectors because earlier Compton-polarimeter reactions may not extend to low-energy gamma rays and large effective solid angles. | method-boundary | direct | Abstract; p.452, Sec.1 | false |
| J02-2 | Physical linear polarization is defined as `P(theta) = [W(theta,phi=0)-W(theta,phi=90)]/[W(theta,phi=0)+W(theta,phi=90)]`, with `-1 <= P <= 1` and `P=0` for an unpolarized gamma ray. | method/formalism | direct | p.453, Eq. (1) | false |
| J02-3 | The experimentally inferred polarization is `P_E(theta) = A/Q(Egamma)`, where `A=[N(theta,phi=90)-N(theta,phi=0)]/[N(theta,phi=90)+N(theta,phi=0)]` is the experimental asymmetry and `Q` is the polarimeter sensitivity. | method/formalism | direct | p.453, Eqs. (2)-(3) | false |
| J02-4 | `Q` can be estimated from the Klein-Nishina Compton cross section and depends on the Compton scattering angle; strip or tracking analysis can restrict the accepted scatter-angle range. | method/formalism | direct | p.453, Sec.2 and Fig.1 discussion | false |
| J02-5 | For a pure E2 calibration transition, `P(90 degrees)=(3a2+1.25a4)/(2-a2+0.75a4)`, with `a2` and `a4` obtained from angular-distribution coefficients that depend on magnetic-substate populations and radiation geometry. | method/formalism | direct | p.454, Eqs. (4)-(6) | false |
| J02-6 | The 197-keV E2 transition in 19F is used as a practical example: the paper quotes `P(90 degrees)=0.23(6)`, measured `A=0.077(8)` and inferred `Q=0.34(9)`. | calibration-observation | direct | p.454, Sec.3, case (a) | false |
| J02-7 | The same example shows that limited counts can give about 30% statistical uncertainty in `A` and consequently in `Q`; a larger known polarization would produce a larger asymmetry for the same detector. | method-boundary | direct | p.454, Sec.3, cases (a)-(b) | false |
| J02-8 | For mixed quadrupole/dipole transitions, the polarization expression contains the interference factor `delta/(1+delta^2)` and uses the Rose-Brink sign convention; the paper identifies the plus branch with E2/M1 and the minus branch with M2/E1 in its notation. | method/formalism | direct | pp.454-455, Eq. (7) | false |
| J02-9 | A pure dipole transition has `\|P(theta)\|=1` for all angles except the beam-axis limit when `a2=-1`; the paper associates this with a maximum-alignment `w(0)=1` state before a `1 -> 0` dipole transition. | method-boundary | direct | p.455, Eq. (8) and following paragraph | false |
| J02-10 | A pure quadrupole transition has the analogous special full-polarization condition for `a2=5/7` and `a4=-12/7`, associated with maximum alignment before a `2 -> 0` transition. | method-boundary | direct | p.455, Eq. (9) and following paragraph | false |
| J02-11 | The paper discusses high-polarization calibration choices including particle-induced reactions, alpha decay, Coulomb excitation and selected 227Th -> 223Ra gamma rays; it stresses that known a priori polarization is preferable to relying only on a low-polarization angular-distribution inference. | calibration-method | direct | pp.455-457, Secs.5-6 and Table 1 | false |
| J02-12 | Relative efficiency can be checked with a geometry in which `P(0)=0` and `A=0`, or with two detector configurations related by a 90-degree rotation so that crystal/electronics differences cancel in a product of count ratios. | calibration-method | direct | p.458, Sec.7, Eqs. (10)-(12) | false |
| J02-13 | The special `\|P\|=1` cases are not a general in-beam assumption: finite detector size, large solid-angle coverage, low-energy efficiency and unobserved feeding can make calibration and relative-efficiency corrections non-trivial. | method-boundary | direct | pp.452, 458-459, Secs.1, 7-8 | false |

## Physical and Methodological Boundaries

- `P` is a property of the emitted gamma-ray angular distribution; `A` is a count asymmetry in a particular detector geometry; `Q` is the detector response/sensitivity at a given energy and accepted Compton-scatter phase space.
- The `|P|=1` examples are special alignment and transition cases. They must not be promoted to a universal property of ordinary in-beam transitions.
- The angular-distribution coefficients `a2` and `a4` describe nuclear alignment and transition geometry; they are not detector sensitivity coefficients.
- A calibration reaction or source transition supplies a reference polarization. It does not remove the need to report detector geometry, scatter-angle acceptance, efficiency and statistical uncertainty.

## Competing Interpretations and Limitations

- The special full-polarization conditions are calibration limits, not a general in-beam assumption.
- Sensitivity estimates inherit uncertainties from the reference polarization, count statistics, detector geometry and accepted Compton-scatter phase space.
- A mixed-transition sign or `delta` convention must be read with the Rose-Brink phase convention used in the paper.

## Extracted Pages

- Pages 1-2: motivation, Compton geometry and definitions of physical polarization and asymmetry.
- Pages 3-4: pure-E2 calibration formula, a2/a4 coefficients and `19F` numerical example.
- Pages 4-5: mixed-transition Rose-Brink expression and pure dipole/quadrupole limits.
- Pages 5-7: high-polarization calibration reactions and `223Ra` table.
- Pages 8-9: relative-efficiency correction and conclusions for low-energy strip/tracking detectors.

## Related Wiki Pages

- Concepts: [[gamma-ray-linear-polarization]], [[magnetic-substate-population]], [[spin-alignment]]
- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]], [[angular-distribution]]
- Observables: [[experimental-asymmetry]], [[polarization-sensitivity]], [[angular-distribution-coefficient]], [[multipole-mixing-ratio]]
- Project: [[gamma-ray-linear-polarization-in-nuclear-spectroscopy]]

## Human Review Triage

P0 review completed: J02-3 (p.453, Eqs.2-3), J02-5 (p.454, Eqs.4-6), J02-8 (pp.454-455, Eq.7), and J02-9/J02-10 (p.455, special full-polarization conditions) were checked against the displayed equations and sign conventions.

The user-reviewed source has no remaining claim-level `needs_review: true` items. The P0/P1 items above were checked; the special full-polarization examples remain bounded to their stated alignment and transition conditions.

## Project Relation

This source is the formalism and calibration anchor for [[gamma-ray-linear-polarization-in-nuclear-spectroscopy]]. It supplies the definitions used to compare later Clover, tracking-array and CdTe Compton measurements, while leaving detector-specific sensitivity and nuclear alignment as separate evidence layers.


## 2026-10-19 Codex追加：校准态、零强度与相对效率边界

以下为本session对本地八页原件的新self-audit，不继承旧人审结论；原frontmatter与全部旧页面前缀逐字节保留，新claims均needs_review。已读Sections1–8、References、Fig.1、Table1及Eqs.(1)–(12)，并视觉核p453–455/457–458。原PDF SHA256不变，原八页不因旧ExtractedPages的页数摘要扩大为九页。

| ID | 新核查陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| J02-14 | p455 Eq9的m0 pure2→0 E2给W=(15/2)x²(1−x²)、Q=W，x=cosθ。非零强度处P=+1，但θ90°也有I=Q=0，P未定义；p455/458文字只列0/180°例外不足以覆盖这个节点，不把约去公共因子的极限充作节点偏振。 | Codex-node-domain-audit | exact-polynomial-and-independent-helicity-check | p455 Eq9及其后m0文字；p458 Sec7；本追加W/Q公式 | true |
| J02-15 | p457–458视觉确认0→2→0中间态文字写w(±2)=.5，却并列a2=5/14/a4=8/7。pointfirstγ物理helicity±1的独立CG/density trace给w(±1)=.5，与所列系数/P90=+1相符；w(±2)则给a2=−5/7/a4=−2/7、P90=−1。隔离为printed population/coefficient不闭合，未把它归为正式corrigendum或原实验重测。 | Codex-printed-state-consistency-audit | visual-source-and-two-calculation-routes | p457末段至p458首段；本追加population对照 | true |
| J02-16 | p456的onlym0/±1 family满足P90=1仅在有光子的p0<1；W90=5(1−p0)/4，p0=1为节点。p0=.4给P60=3/5；不能把某角fullP与各角constantP、0→2→0与4→2→0门制备等同。 | calibration-family-boundary | source-and-exact-calculation | p456 Sec5 family；p455Eq9；本追加family公式 | true |
| J02-17 | p458 Eq10–12的90°交换法给R=sqrt(Na0 Nb0/(Na90 Nb90))，A=(1−R)/(1+R)；仅在两orientation的物理A与对应效率比可因子分离且稳定时消除效率。若比值产品残留κ，则Ahat=tanh(atanhA−lnκ/4)，不能宣称所有系统误差无条件消除。 | relative-efficiency-design-boundary | original-equations-and-declared-model | p458 Eqs10–12；本追加cross-ratio模型 | true |
| J02-18 | 对四独立Poisson峰面积，一阶VarA=(1−A²)²Σ1/Ni/16；一般应gᵀΣg，gi=−(1−A²)si/(4Ni)、s=(+1,−1,+1,−1)。共享背景/同事件/校准需实际Σ，零或负netarea不能使用本log近似。 | conditional-statistical-derivation | derivative-and-PSD-controls | p458 Eq10–12；本追加误差公式；designresult | true |
| J02-19 | p454的19F P=.23(.06)/A=.077(.008)来自Ref7旧实验；1000/857与1000/493是作者假设计数。按独立Poisson得到A相对σ约30.05%/7.17%；由舍入A/P及假定独立得到Q=.3348、σ=.0940，非新实验Q或已恢复A–P Cov。 | reported-versus-hypothetical-input | source-and-conditional-arithmetic | p454 Sec3 casea/b；Refs7；本追加计数复算 | true |
| J02-20 | Table1的两个314.78keV分别属于母态376.28(7/2−→7/2+)和445.00(9/2+→9/2+、M1)，所列理论P90为−.94/+.96。Eγ本身不能识别校准reference，须同α门/母态/response；实验a2/a4转录自1998Ref12，P列为本文理论，非新增独立采集。 | transition-and-data-lineage-boundary | direct-Table1-and-caption | p457 Table1 parent376.28/445.00 rows；p456Sec6/Ref12 | true |
| J02-21 | 假定两314.78分量同响应/共同轴、f为接受后第一分量光子份额，则P_eff=.96−1.90f，f=48/95时为0；目标−.94中声明5%错分量给−.845、若误用纯reference则Q低估约10.1%。这是污染设计，不是实测含量、谱峰分解或actualQ。 | conditional-unresolved-reference-design | Stokes-mixture-arithmetic | p457 Table1两314.78理论P；本追加混合公式 | true |

### 不可先约去的零强度

这里`W`以角平均1归一，`Q=I_parallel−I_perp`为光子Stokes分量，不是polarimeter Q。对2→0 pureE2，独立Racah和helicity trace给：

| 布居 | a2 | a4 | W90 | P90 |
| --- | --- | --- | --- | --- |
| m0=1 | 5/7 | −12/7 | 0 | undefined |
| w(+1)=w(−1)=.5 | 5/14 | 8/7 | 5/4 | +1 |
| w(+2)=w(−2)=.5 | −5/7 | −2/7 | 5/4 | −1 |

m0的`W=(15/2)x²(1−x²)`和`Q=W`在x=0、±1同时零。数值trigonometric残差约10^-32不构成信号；程序先保存原W/Q节点，再在定义域内化简P。两计算路线a2/a4及九角W/Q误差≤7.50×10^-16。字面w±2与其后所列系数不合，不能靠换δ号、EM标签或旧review状态将其消掉；原图/原文/旧claims保持。

### Cross-ratio何时真正消效率

按原Eq10–11顺序四峰为`(Na0[A1],Na90[A2],Nb0[A2],Nb90[A1])`。声明模型：`Na0=Ta ε1(1−A)`、`Na90=Ta ε2(1+A)`、`Nb0=Tb ε2(1−A)`、`Nb90=Tb ε1(1+A)`；相同A/response才有原产品。曝光Ta/Tb可不同；角门、偏振参考面、interaction selection、能窗/背景方法仍须匹配。

设计输入A=.2、Ta/Tb=5000/7000、ε1/ε2=.8/.4给期望峰面积3200/2400/2240/6720。单orientation裸不对称为−.142857，而cross-ratio回到.2，四独立Poisson一阶σ=.008734。共享纯乘性曝光rank1 Cov控制抵消；这不代表共享background也抵消。效率比产品漂移κ=1.1给Ahat=.1770204，偏差大于此例两倍统计σ；未将它说成实际装置漂移。

一般`VarA=gᵀΣg`；只有独立Poisson才可代入`Σ=diag(N)`。实验netpeak area、sharedfit/subtraction与Qcalibration需实际Cov；设计程序对零输入拒绝log近似，不加伪计数或clip。边界处应另用声明的原count likelihood，不将此一阶近似当exact CI。

### 同能标reference仍需母态门

两314.78的`P_eff=f*(−.94)+(1−f)*.96`仅是相同响应下的密度矩阵混合。f必须是相应接受后的光子数权重，不能直接用a2、未修强度或母态branch替代；若response不同，应先对每分量的I/Q与响应积分。没有新的数据证明实际峰未分开/污染5%；这里标出单能标匹配会丢失的必要身份。

Ref12书目已外核为G.D.Jones/P.A.Butler/T.H.Hoare/P.M.Jones，*EPJ A*2,129–141(1998)，DOI10.1007/s100500050101，题名*A study of223Ra populated byα-decay*；在取得正文前不补原α门或fitCov。2002重列表与1998原实验不计两次独立数据。

### 续接与证据状态

`supports`source中的高P校准/旋转法思想；`revises`其实际使用中的节点与布居文字合同；`limits`跨父态/响应裸迁reference和宣称所有系统项消除。新结论只为Codex self-audit，未清needs_review或更改原human-reviewed前缀。

[新审计脚本](../../system/scripts/day16_jones2002_calibration_audit.py)、[冻结合同/数值结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/jones2002-calibration-audit-result.json)；[双314.78设计](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/jones2002-ra223-doublet-design-result.json)。原件与依赖hash、主动回忆/完整八页阅读和视觉记录在同run回执。[[compton-polarimetry]]、[[linear-polarization-asymmetry]]和[[co60-gate-role-response-benchmark]]保存可复用边界；这些outputs是执行证据，知识判断在本source。


### 1998原实验已读后的版本与companion补充

| ID | 新核查陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| J02-22 | Ref12原件现已完整读13页/9图3表。1998 Table1与本Table1的experimental列同源，本篇36行对应theory/P以point/RB模型闭合；原1998部分theory列不同。不能把2002理论P列称独立测P，也不以重放新拟原δ。 | upstream-primary-and-version-crosswalk | original-source-comparison-and-Codex-model | Ref12；本Table1；J98p132Table1 | true |
| J02-23 | 原113.159γ峰含174.58/174.62 E1/E2重叠，作者另用α–eL/eM选择赋11/2+；γ/total/subshell权重不同。342.84 J9/2+及Table2多数δ符号另附模型/系统学条件，不能由本校准表标签抹掉。 | companion-and-assignment-boundary | direct-upstream-primary | J98Sec4.2/4.5；Fig3；Table2符号说明 | true |

[[jones-1998-ra223-alpha-gamma-correlations]] J98-1–13保存原装置/phase/Qk/误差/两314.78、113.159companion与47行复算。比对只做同层：1998实验角系数、1998theory、2002theory/P、当前point计算分别保留。原文件/旧人审prefix均不改；新增J02-22/23仍needs_review。
