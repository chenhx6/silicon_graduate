---
type: source
title: "Use of DCO Ratios for Spin Determination in gamma-gamma Coincidence Measurements"
aliases: [Kramer-Flecken 1989 DCO, Kramer-Flecken 1989 use of DCO ratios, DCO spin determination OSIRIS]
created: 2026-07-12
updated: 2026-10-17
status: ai-draft
review_status: human-reviewed
source_type: experiment-method-article
reading_depth: read
title_original: "Use of DCO Ratios for Spin Determination in gamma-gamma Coincidence Measurements"
authors: [A. Kramer-Flecken, T. Morek, R. M. Lieder, W. Gast, G. Hebbinghaus, H. M. Jager, W. Urban]
journal: Nuclear Instruments and Methods in Physics Research Section A
year: 1989
volume: 275
number: 2
pages: 333--339
doi: 10.1016/0168-9002(89)90706-7
language: en
canonical_source: doi:10.1016/0168-9002(89)90706-7
citation_key: kramer-flecken_1989_UseDCO
raw_file: "raw/papers/1989_Krämer-Flecken et al_Use of DCO ratios for spin determination in γ-γ coincidence measurements.pdf"
raw_sha256: 30CDF474DB5FBFAA6A27F6D2E0D11EA39BBB61A05C8153E740F2F3DCCA52220F
nuclei: []
reactions: []
observables: [multipole-mixing-ratio]
methods: [dco-ratio, angular-correlation, spin-parity-assignment]
tags: [dco, angular-correlation, spin-assignment, geometry, alignment, gamma-spectroscopy]
---

# Kramer-Flecken et al. (1989): Use of DCO Ratios

## 2026-10-17使用更正：实验DCO分式

**当前使用以KF89-9为准。** 原件printed334的理论式与实验式彼此一致；旧Wiki KF89-1把实验强度分式转写成了倒数。正确原式是`I_(theta1)^gamma2(Gate_(theta2)^gamma1) / I_(theta2)^gamma2(Gate_(theta1)^gamma1)`：gamma1为门、gamma2为待测线，W的第一角参数是门角。不能把原文只当一个无标签的theta交换式使用。

原有page级`human-reviewed`及KF89-1–8的flag/文字保留原审核历史，**不扩张到本次更正**；KF89-1的旧实验分式已被本节明确supersede，不能继续单独引用。新KF89-9–14及本节是Codex原件self-audit、`needs_review: true`，不是人审记录。原PDF身份/哈希不变。

同理，原件low-spin边界I≤6与旧摘要I<6、width措辞及generic mixed pair的适用条件分别由KF89-13/14注明；不要用旧审核标签抹掉本次明确的原件边界。

## Bibliographic Record

A. Kramer-Flecken et al., *Nuclear Instruments and Methods in Physics Research Section A* **275**(2), 333--339 (1989), DOI `10.1016/0168-9002(89)90706-7`, citation key `kramer-flecken_1989_UseDCO`.

The BibTeX key matches uniquely by title, year and DOI. Local file size is `450640` bytes; local timestamp `2025-01-09 10:22:20`; SHA-256 is recorded above.

## Scope and Reading Depth

The full seven-page article was read from the PDF text layer. Key checks covered the DCO formalism in Sec.2, geometry/systematics in Figs.1--4 and Table 1, the OSIRIS array description in Sec.3, and the `178W` spin-assignment application in Sec.4.

This is a `method-ingest + theory-ingest` source. It is both a method paper and an experimental demonstration on `178W`; for the current Wiki its main contribution is the DCO-ratio definition, geometry dependence, alignment dependence, and multi-solution boundary.

## Summary

The paper formalizes directional correlations from oriented states (DCO) as a practical reduction of gamma-gamma angular-correlation information in large detector arrays. It defines the gated intensity ratio, studies its dependence on detector geometry, alignment width, spins, multipolarities, and dipole-quadrupole mixing ratios, and shows with OSIRIS calculations that a single measured DCO ratio may map to several different spin/mixing-ratio solutions.

Its practical message is balanced: DCO is powerful for weak or unresolved transitions in multidetector arrays, but it does not uniquely determine spin or `delta` in all cases and should be combined with additional information such as intensities or angular distributions.

## Experimental or Theoretical Setup

- Method context: unpolarized heavy-ion beam, detectors insensitive to gamma polarization, so the full angular-correlation formalism can be simplified for DCO use.
- Initial-state magnetic-substate population is modeled as a Gaussian centered at `m=0` with a width parameter written in the paper as `sigma`; the paper states that `sigma/I` is approximately constant over a wide spin range, but that this empirical rule deviates in the low-spin region `I < 6`.
- Calculations were performed with the DCOMAP code for arbitrary detector geometries and for varying spins/multipolarities/mixing ratios.
- Experimental demonstration uses the OSIRIS array (12 Compton-suppressed Ge detectors) and delayed cascades in `178W`.

## Key Results

KF89-1–8是原2026-07-12审核记录；其中KF89-1的实验分式有上述转写错误。其当前更正见同表KF89-9及页首使用说明，原件没有该上下倒置问题。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KF89-1 | 本文先把理论 DCO ratio 定义为 `R_DCO = W(theta_2,theta_1,phi) / W(theta_1,theta_2,phi)`，并紧接着给出实验上对应的 `R_DCO = I_{theta_2}(Gate_{theta_1}) / I_{theta_1}(Gate_{theta_2})`；交换角度或交换 gate 与被观察跃迁会把 DCO ratio 取倒数。 | method-formalism | direct | p.334, Sec.2 around the definition of `R_DCO` | false |
| KF89-2 | 作者采用以 `m=0` 为中心的 Gaussian magnetic-substate population 描述初态取向，并指出 `sigma/I` 在较宽自旋区间内近似常数，但在低自旋 `I < 6` 区域会偏离这一经验规律。 | method-boundary | direct | p.334, Sec.2 first paragraph | false |
| KF89-3 | DCO 对几何强烈依赖：区分不同 cascades 的效果在一个探测器接近 `0°/180°`、另一个接近 `90°` 时最大；对大阵列，应选择能放大该差异的 detector combinations。 | experimental-criterion | direct | pp.334--335, Fig.2 and text below | false |
| KF89-4 | 实验 DCO ratios 需要做相对效率修正；推荐用能量相近、已知 multipolarity 与 spin 的 cascades 来标定平均修正因子。 | experimental-practice | direct | p.335, Sec.2 paragraph below Fig.2 | false |
| KF89-5 | DCO 依赖初态 alignment：当 `a/I` 很大时，DCO ratio 会趋近 `1`，与放射源无取向情形相符。 | method-boundary | direct | p.335, Fig.3 and surrounding text | false |
| KF89-6 | 在允许 dipole-quadrupole mixing 的情况下，同一个实验 DCO ratio 可对应若干不同的自旋或 mixing-ratio 解；一般而言 `Delta I = ±1` 不能仅靠 DCO 唯一区分，因此单靠 DCO 不能总是给出无歧义自旋指定。 | method-boundary | direct | p.337, top paragraph; Fig.4 discussion | false |
| KF89-7 | 作者总结 DCO method 相对角分布的三项实践优势是：可研究弱跃迁、可处理 multiplets、且不需要 beam-charge normalization。 | author-interpretation | direct | p.337, paragraph below Fig.4 | false |
| KF89-8 | 在 `178W` 的 OSIRIS 示例中，作者结合多条 cascade 的 DCO ratios 与强度信息，把 `3527 keV`、`35 ns` isomer 的自旋定为 `I=14`。 | observed-fact | direct | pp.338--339, Sec.4 and Fig.8 discussion | false |
| KF89-9 | 原文W(theta1,theta2,phi)指在detector1的theta1角用gamma1开门、在detector2的theta2角观测gamma2；故R=W(theta2,theta1)/W(theta1,theta2)=I_theta1^gamma2(Gate_theta2^gamma1)/I_theta2^gamma2(Gate_theta1^gamma1)。旧KF89-1的实验I分式是Wiki倒置转写，本条优先。 | source-transcription-correction | direct-and-self-audit | printed334 Sec2，W定义段与紧接的两个R公式 | true |
| KF89-10 | 本文公式中的gamma1/gamma2是gate/observed标签；Table1又明确各例gating transition为物理级联第二条。两套标签不能不经映射等同“第一/第二次发射”。 | convention-boundary | direct | printed334 Sec2定义段、Table1图注 | true |
| KF89-11 | “两条同L则R=1”不能脱离spin路径：Table1在相同geometry/width下给10→8→7的L2/L2为.66、10→8→8的L2/L2为.57，而stretched10→8→6为1。Fig2的陈述有L=Ii−If的stretched前提。 | calibration-transfer-boundary | direct-and-self-audit | printed334 Table1与Fig2图注；printed335首段 | true |
| KF89-12 | 178W例假设35ns异构体不强烈改变width/I；DCO容许isomer I12或14，作者另用decay-pattern/intensity偏好14。不能把其最终采用值说成一项DCO直接唯一测量，本文未给未见弱branch的完整upper-limit/Cov输入。 | author-assignment-and-boundary | direct-and-self-audit | printed337 Sec4末段；printed339 isomer讨论 | true |
| KF89-13 | 原文称Gaussian的half width sigma，未在本文写明指数式；printed334低spin边界印为I≤6。表中sigma/I值不能仅凭同字母自动转成HWHM或D96Eq19的std。 | width-convention-boundary | direct-and-self-audit | printed334 Sec2首段 | true |
| KF89-14 | 182-keV例以E1/小M2解释generic dipole/quadrupole ratio；不能把本文所有delta都当E2/M1或把平方份额无条件称为E2份额。 | multipole-pair-boundary | direct-and-self-audit | printed339 182-keV讨论 | true |

## Nuclear Structure Information

The `178W` application is included as a worked method example rather than a full `178W` structure ingest. The current Wiki uses it mainly to anchor DCO practice and its ambiguities.

## Authors' Interpretation

- DCO ratios are well suited to multidetector-array spectroscopy of weak transitions.
- They can determine spins and dipole-quadrupole mixing ratios in favorable cases.
- They still require complementary information when several calculated branches overlap the same measured ratio.

## Model Results

- DCOMAP calculations quantify the dependence of `R_DCO` on geometry, alignment width, spin sequence, and the mixing ratios of both transitions in a cascade.
- For the OSIRIS geometry `theta_1=90°`, `theta_2=38°`, `phi=18°`, the paper tabulates limiting DCO values for several pure cascades and shows broad multi-solution regions for mixed cascades.

## Competing Interpretations and Limitations

- This paper should not be reduced to the heuristic "`R_DCO ~ 1` quadrupole / `~0.5` dipole"; those numbers are geometry-, gate-, and alignment-dependent.
- The low-spin `sigma/I` deviation is explicitly flagged, so later low-spin work should not inherit a single near-constant alignment-width heuristic without caution.
- The `178W` case uses intensities in addition to DCO; the source itself does not claim that DCO alone always solves the problem.

## Extracted Pages

- Nuclei:
- Bands:
- Concepts:
- Methods: [[dco-ratio]], [[angular-correlation]], [[spin-parity-assignment]]
- Observables: [[multipole-mixing-ratio]]
- Projects: [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]

## Personal Notes

This is one of the clearest sources for the sentence "DCO is compressed angular-correlation information, not a geometry-free universal classifier." It also gives a concrete early warning that low-spin behavior and multi-solution branches can spoil naive reuse of standard thresholds.

## 本次原件核验范围与角色映射

本session的Day16整体primed回忆先于source/raw；补充的Ref1专门预测在读过既有source摘要后、打开raw前冻结，不能称盲测。raw SHA-256重新匹配`30cdf474db5fbfaa6a27f6d2e0d11ea39bbb61a05c8153e740f2f3dcca52220f`；完整读7页text主线，放大printed334公式及printed335多解图。原有`reading_depth: read`/human-review范围不改，额外声明不等于DCOMAP代码取得或本session人审。

令按物理发射先后记为a（上游）、b（下游），联合函数写`W_ab(theta_a,theta_b)`。[[dco-pdco-ambiguity-worksheet]]自己定义的`R*=W_ab(0,90)/W_ab(90,0)`可映射为：

| KF的detector标签 | 待测/门 | 对应比 |
| --- | --- | --- |
| theta1=0、theta2=90 | obs=a、gate=b | R* |
| theta1=90、theta2=0 | obs=a、gate=b | 1/R* |
| theta1=90、theta2=0 | obs=b、gate=a | R* |
| theta1=0、theta2=90 | obs=b、gate=a | 1/R* |

这是原定义的代数标签映射，要求同一corrected joint cells/selection/normalization；不同门后密度或不同pair cuts不能当作机械互反。D96 Fig7只列0/90角组，不在图注重写上述全部gate/detector标签，故数值约.4本身不认证唯一的标签解释；保留worksheet的显式R*定义。

新的corrected source入口已同步到[[dco-ratio]]；本页旧实验转写不再作为该方法的操作定义。KF89-2旧I<6摘要与原件I≤6的差别、half-width用语和generic delta的多极子类型分别保留在KF89-13/14，不能靠字母相同填入原文没有的定义。
