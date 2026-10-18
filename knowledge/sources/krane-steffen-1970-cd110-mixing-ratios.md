---
type: source
title: "Krane and Steffen 1970 - E2/M1 mixing ratios in 110Cd"
aliases: [Krane Steffen 1970 Cd110 mixing ratios]
created: 2026-09-21
updated: 2026-10-17
status: ai-draft
review_status: unreviewed
source_type: experiment-and-formalism
reading_depth: deep-read
title_original: "Determination of the E2/M1 Multipole Mixing Ratios of the Gamma Transitions in Cd110"
authors: [K. S. Krane, R. M. Steffen]
journal: "Physical Review C"
year: 1970
volume: 2
pages: "724-734"
doi: "10.1103/PhysRevC.2.724"
citation_key: Krane_1970
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "Krane & Steffen, Phys. Rev. C 2, 724-734 (1970)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1970_Krane et al_Determination of the E2M1 Multipole Mixing Ratios of the Gamma Transitions in Cd110.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1970_Krane et al_Determination of the E2M1 Multipole Mixing Ratios of the Gamma Transitions in Cd110.pdf"
raw_sha256: "ab82cb483425ba984a8c30b35f118b4713e186d53899fcbbba6a19dd444377f1"
nuclei: [110Cd, 110Ag]
reactions: [110Ag-beta-decay]
experiments: [two-GeLi-directional-correlation]
models: [vibrational-model, extra-pair-model, Rose-Brink, Biedenharn]
observables: [E2-M1-mixing-ratio, directional-correlation, gamma-width, quadrupole-moment]
methods: [gamma-gamma-directional-correlation, high-resolution-GeLi]
tags: [110Cd, mixing-ratio, angular-correlation, vibrational-nucleus]
---

# E2/M1 mixing ratios in `110Cd`

## Bibliographic Record

- K. S. Krane & R. M. Steffen, *Phys. Rev. C* **2**, 724–734 (1970), DOI `10.1103/PhysRevC.2.724`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1970_Krane et al_Determination of the E2M1 Multipole Mixing Ratios of the Gamma Transitions in Cd110.pdf`。

## Scope and Reading Depth

- PDF pp.724–734 fully read: `110Ag→110Cd` level structure, Ge(Li) 1–2/1–3/1–4 directional correlations, 25-correlation fit, explicitly defined reduced operators, convention conversion, all mixed-transition δ values and vibrational/extra-pair discussion.
- Not covered: raw coincidence matrices and later model calculations.

## Key Results

- High-resolution two-Ge(Li) directional correlations and coincidence gating determine a consistent set of 25 cascade correlations. Compton background was explicitly investigated and shown to bias directional-correlation coefficients if untreated (PDF pp.724–727).
- The reported E2/M1 amplitude ratios are `δ(447)=−0.45(20)`, `δ(620)=−0.80(50)`, `δ(678)=−0.25(20)`, `δ(687)=−1.1(+.8/−.4)`, `δ(707)=−1.0(3)`, `δ(818)=−1.20(15)`, `δ(1384)=−0.37(3)`, `δ(1505)=−0.55(10)`; the paper also gives corresponding Bohr–Mottelson multipole-moment ratios (printed724 abstract and printed733 TableIII). The previously unreadable 687-keV interval was resolved by this session's enlarged original, not by symmetrizing an error.
- The formalism defines δ using reduced emission matrix elements with the initial state on the right and maps them explicitly to Rose–Brink and Biedenharn conventions. This resolves sign/order ambiguity before comparing the 25 fits (PDF pp.726–728, Eqs.3–14).
- The measured nonzero M1 admixtures and crossover E2 transitions challenge a pure harmonic-vibration picture of `110Cd`; the authors discuss extra-pair/anharmonic and microscopic quadrupole–pairing interpretations (PDF pp.724–726).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KS70-1 | A consistent set of E2/M1 δ values is obtained from 25 Ge(Li) directional correlations after Compton-background control. | mixing-ratio-result | direct | PDF pp.724–728, abstract | true |
| KS70-2 | Explicit operator/state-order definitions and conversion to Rose–Brink/Biedenharn conventions are necessary for δ sign comparison. | convention-boundary | direct | PDF pp.726–728, Eqs.3–14 | false |
| KS70-3 | Nonzero M1 admixtures and crossover E2 decay challenge a pure harmonic-vibration description of `110Cd`. | structure-interpretation | mixed | PDF pp.724–726 | true |
| KS70-4 | Directional-correlation coefficients require explicit Compton-background and detector-response checks. | method-boundary | direct | PDF pp.724–725 | false |
| KS70-5 | Eq9以初态在右的radiative emission RME的E2/M1比定义delta，并给delta=(sqrt3/10)k Delta_BM；natural units中的m在正文明确为electron mass。TableIII的BM矩比和Fig5的M1 percentages是同一delta的派生量，不增独立观测。 | definition-unit-and-dependency | direct | printed727 Eq4/9；printed732 Eq20/单位说明；printed733 TableIII/Fig5 | true |
| KS70-6 | 相同KS emission delta用于两photon时，第一条orientation B有负线性干涉项、第二条distribution A有正干涉项；未观测中间跃迁的U只含multipole intensities、无干涉，不能由U或delta平方确定符号。 | role-and-interference-boundary | direct | printed727 Eq7–11；printed728 Eq13–15 | true |
| KS70-7 | Eq12所称BR是Biedenharn–Rose1953（Ref29），并给gamma1处delta_KS=−delta_BR、gamma2处delta_KS=+delta_BR；Rose–Brink1967是另一个Ref30，Eq5对其初态在左的T矩元另有L-dependent相位/归一。不能混用二者缩写。 | convention-identity | direct | printed727 Eq5/12与上下文；printed734 Refs29/30 | true |
| KS70-8 | 源文用几何校正后的A_lambda,lambda=(A'_lambda,lambda/A'_00)/(Qbar_lambda(gamma1)Qbar_lambda(gamma2))；这些Qbar是有限geometry因子，不是polarimeterQ或ADO f，能量独立性只在其测量范围/装置下检验。 | response-convention | direct | printed728 Eq18/19；printed729 calibration说明 | true |
| KS70-9 | 937–885强线的直接A22=.055±.010偏离pure6→4→2期望.102；作者用约10%Compton污染解释，background-corrected谱法给.098±.010。强峰不能保证background不改角系数，未给两结果Cov时不重算显著性。 | experimental-counterexample | direct-and-self-audit | printed730 Compton例；printed731 Fig4及正文 | true |
| KS70-10 | TableII的818–658 direct corrected(A22,A44)=(.375±.050,.180±.050)；TableI的658门818行是(.481±.082,.155±.112)。两配置分开，TableIII最终delta818=−1.20±.15是network summary，不能再当独立数据和前述系数重复拟合。 | published-data-and-dependency | direct-and-self-audit | printed732 TableI gamma9/gamma3门；printed733 TableII/III | true |
| KS70-11 | 放大原件读得nominal687（TableIII能量686.6）的delta=−1.1^(+.8/−.4)，natural Delta=−4.7^(+3.4/−1.7)。保留不对称误差，旧扫描歧义在此局部解决，原claims的review flags不清除。 | source-reading-resolution | direct | printed724 abstract；printed733 TableIII | true |
| KS70-12 | Parent在abstract/Fig5是110mAg，文中采用253day历史半衰期；658/764/937门有90/135/180三角，885门只有90/180且只提取anisotropy。不能把全部表列强行当同样two-coefficient/full-Cov观测。 | measurement-identity-boundary | direct | printed724 abstract；printed729 source；printed730 angles；printed733 Fig5 | true |
| KS70-13 | Eq5的每L因子为(-1)^(Ii−If+L) sqrt((2Ii+1)/(2pi)) / sqrt(2L+1)。把Rose–Brink Eq3.39的normalized a_RB定义代入，同一transition的ratio得到delta_KS(Lprime/L)=(-1)^(Lprime−L) delta_RB；相邻E2/M1为负号。该桥是两篇原式的代数核对，不是新的实验结果。 | cross-source-convention-derivation | direct-and-self-audit | printed727 Eq5/9；companion RB67-6的printed319 Eq3.39 | true |

## Summary

Krane and Steffen demonstrate how a complete high-resolution directional-correlation network can determine a mutually consistent set of E2/M1 mixing ratios. The source is an important convention and background-control anchor for later δ tables, while its anharmonic-vibration interpretation remains model dependent.

## Competing Interpretations and Limitations

- Some δ uncertainties are broad/asymmetric and branch solutions depend on the adopted spin sequence and convention. The 687-keV asymmetric interval is now locally resolved as `−1.1(+.8/−.4)` by the original image; this does not recover the fit likelihood or joint covariance and does not change the old review flags.
- Pure-vibration, displaced-oscillator and extra-pair models can reproduce different subsets of level energies, moments and transition strengths; δ data alone do not select a unique microscopic Hamiltonian.
- Ge(Li) Compton background and unresolved coincidence contributions can distort A coefficients; high-resolution gating is part of the measurement identity.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| KS70-AR-1 | Correlation chain | Cascade identity/background correction → directional-correlation coefficients → reduced-matrix-element fit → δ set across transitions. | PDF pp.724–728 | self-checking |
| KS70-AR-2 | Convention chain | Emission matrix elements (initial state right) → Rose–Brink/Biedenharn map → comparable δ signs. | PDF Sec.III, Eqs.3–14 | self-checking |
| KS70-AR-3 | Model boundary | δ/M1 admixtures constrain vibration/extra-pair models but do not uniquely determine shape or collectivity. | PDF Sec.I and discussion | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[multipole-mixing-ratio]], [[angular-correlation]], [[angular-distribution]], [[rose-brink-1967-phase-defined-angular-distributions]] and the `110Cd` γ-vibration comparator.
- New reusable rule: a directional-correlation δ value is only portable with its operator convention, cascade order, background correction and spin sequence.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `KS70-P0-1`: Preserve Compton-background, convention and spin-sequence boundaries; do not merge the printed δ values with Rose–Brink or Hamilton values without conversion.

## Extracted Pages

- Methods/observables: [[multipole-mixing-ratio]], [[angular-correlation]], [[angular-distribution]]。

## 2026-10-17原件复核：发射约定、实际数据与精度边界

本次primed来源前回忆先冻结，随后重核raw SHA-256 `ab82cb483425ba984a8c30b35f118b4713e186d53899fcbbba6a19dd444377f1`，完整读11页（printed724–734），放大Eq3–19、TableI–III/abstract，查Fig1–5与实验/讨论主线。旧KS70-1–4的flags和page review不改，新KS70-5–12 true。没有取得原event spectra、完整fit Cov或25-correlation likelihood；纸中253day是历史source身份，不作当前评价寿命。

### 同BM定义下的两文振幅桥

本节以t_KS表示发射RME（不是source的去取向U_lambda）。KS70 Eq4a以`C_L i^L M(EL)`给electric t_KS，Eq4b以`−C_L i^(L−1) M(ML)`给magnetic t_KS，其中`C_L=k^L sqrt((L+1)/L)/(2L+1)!!`。必须保留Eq4b前的负号；它与i幂合成i^(L+1)。在同一BM算符、state order、units及同一transition下，[[droste-1996-pdco-formalism]] Eq5因此为

\[
a_{D96}(TL)=\sqrt{8\pi k/(2I_i+1)}\,t_{KS70}(TL).
\]

共同positive normalization在同gamma的multipole ratio中抵消，故本例的`d_D96=a(E2)/a(M1)=delta_KS`。这与本任务probe→source的relative-basis负号是不同操作，不能误说两篇delta相反。两文共享BM理论定义，符合是一项定义/实现核对，不是新的独立实验。

Eq5对Rose–Brink的**literal T_RB matrix ratio**给`delta_KS=−sqrt(3/5) [<Ii||T_E2||If>_RB/<Ii||T_M1||If>_RB]`。本run随后定向原图核[[rose-brink-1967-phase-defined-angular-distributions]] RB67-6的Eq3.39，确认其每个振幅已除sqrt(2L+1)，所以同一E2/M1跃迁确为`delta_KS=−delta_RB`。这里的负号来自Eq5的L-dependent factor，不能把裸T比本身当delta。Rose–Brink初态在左在此仍指**发射**，不能仅凭bra/ket位置把它叫作实际吸收。Eq12的Biedenharn–Rose转换又依赖gamma1/gamma2角色，两个BR/RB来源不是同一篇。

### 实际818–658系数与derived列

Fig5对应818.0keV的`2+(1475.7)→2+(657.7)`，gamma3/657.7（nominal658）是`2+→0+` pureE2参考；source无取向，角度是两gamma的opening angle，不是beam-oriented DCO的交换探测器比。[[dco-pdco-ambiguity-worksheet]]保存该**已校正**TableII单A22的条件反演及A44比较；不将其造作raw RDCO或原文global delta重拟合。

TableIII的15行中8行为finite mixed ratio，7个pureE2限值保留∞（在文中dipole/quadrupole截断内）；M1百分比、natural Delta与eb/muN Delta都是同一delta的派生表，不独立计入likelihood。本任务按声明单位常数核8行，中央值/百分比与印刷精度一致；但若把所有尾随零都视为有效位，620.2keV的`delta error .50 → Delta_(eb/muN) error .95`严格rounding检验不闭合。原件已放大确认这两个数，未改数据/扩大容差；source没给其error rounding recipe或unrounded estimates，保留精度边界，不据此宣布原误差错误或给出新CI。

885门只有两角的coverage、quoted errors主要受Compton background subtraction影响（printed731约5%说明），以及normalized coefficients/geometry correction共享的Cov均需保留。TableI/II与global delta相容性不能靠把所有derived列当独立测量来加强。

## Day16恢复批次：完整相关网络与1505-keV参考角色

本批来源前primed假设已冻结，随后重新核原件全部主线，重点放大printed732 TableI、733 TableII/Fig5及727–728 Eq10/11/17。以15个gamma编号和箭头端点重建选定网络；9个图示能级含无本表连接的tentative1473.2-keV0+，不是新完整评价。冻结输入`DAY16-KS70-NETWORK-1505-ROLE-REFERENCE-01`保留Fig5和TableIII的energy写法差别，不把图上整数/小数当新的测量精度。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| KS70-14 | TableI可逐格读出31个有向target/gate条目，按无向gamma对去重为26对；TableII四行均为已在TableI出现的gamma对。此count与abstract的25correlations口径未恢复，既不擅改作者数字，也不当作26/35个独立实验；885门只有两角的边界仍在。 | printed-network-identity-and-counting-boundary | direct-and-task-enumeration | printed732 TableI；printed733 TableII；printed724 abstract | true |
| KS70-15 | gamma14=1505：Fig5的3+(2162.2)→2+(657.7)；下游gamma3=658是2+→0+，上游gamma8=764是5+(2926.6)→3+。TableII分别给1505–658的A22=−.403(.014)/A44=−.027(.020)及764–1505的−.184(.024)/−.031(.037)；同target的first/second角色要分别用Eq10/11，不能机械倒数或仅翻δ。 | measured-reference-role-identity | direct | printed733 TableII/Fig5；printed727 Eq10/11 | true |
| KS70-16 | TableI同1505/658行A22=−.471(.010)，与TableII−.403(.014)中央差−.068，两个字面一倍quoted-margin区间不交；源文仍称总体内部相容。此处保存印刷差异，不虚构联合Cov/totalbudget或宣称原实验矛盾、哪种处理必然正确。 | direct-indirect-response-countercheck | direct-and-task-arithmetic | printed732 TableI gamma14/gamma3；printed733 TableII firstrow；printed731 internal-consistency discussion | true |
| KS70-17 | 图示764到658有764–620–885–658、764–687–818–658、764–1505–658三条路径；707到658也有经678/885、744/818或1562的三路。未额外指定branch/gate时endpoint相关是路径加权和，不能任选一条未观测U链；当前输入无这些path weights。 | cascade-path-and-branch-boundary | direct-graph-and-derived | printed733 Fig5；printed728 Eq17；printed732 TableI gamma3/gamma8与gamma6/gamma3 | true |
| KS70-18 | 放大Fig5确认2162.2等能级与所印620.2/686.8/763.9/1505.0不能全以0.1keV内的能差闭合，最大字面残差.5keV；TableIII还用686.6/1504.9等值。以箭头/编号/spin映射身份，保留两个energy层，不改原值、不补能量误差或重评能级。 | printed-drawing-precision-boundary | direct-and-task-arithmetic | printed733 Fig5/TableIII | true |

新[计算程序](../../system/scripts/day16_ks70_network_reference_audit.py)使用先前已证明的KS70=D96发射坐标，复用同一F/CG底层，**不算独立producer实现**。同target1505的两种角色用不同二次型，TableII单A22给δ≈−3.45050或−.483082；在上游参考的A22预测分别约−.08660/−.20632，后一值落在其字面quoted区间。全部四项TableII marginalboxes交得δ约[−.495802,−.454731]，只是固定spin/已校正系数/截断的必要条件区间，不是新实验δ或CI，作者summary−.55(.10)不再作独立拟合输入。

同样条件套TableI四项时无一倍margin共同交，不能强称四个central或marginalboxes都已被同δ复现。其764/1505 A44中央−.047在此模型全δ范围[−.01360544,0]外，quotedbox上端−.014也略低于该下界；这是一项打印输入/声明条件的未闭合，非统计排除源的全实验结果。缺原counts/background/response与完整Σ，不自由调误差、分支或相位补闭合。

首run在任何反演前因图示能差0.11keV守卫失败；放大原图确认这是源所印数值，并非OCR错读。最终保留能差residual ledger而不把drawing当精密能量fit；相同冻结数据未修改。two-role directphoton/F核对误差1.12e−15以内，只证明本任务代数相容。决定`supports`用上/下游匹配reference和多rank共同约束；`limits`仅凭“25consistent”摘要恢复全likelihood或忽略direct/indirect口径。新claims true；所有旧flags/review保留。

### 相同条件下的外部C++实现检查

本日随后实际构建[[alpaca-2023-v105-angular-correlation-code]]的固定2023代码对象，AC23-5/6给first/last角色映射和独立GSL数字路径核验。无取向1505两路径、单一764–687–818中间marginal及polarizedcontrols与本任务trace相容，支持当前条件forwardmodel的实现。它未提供TableI/II的actualresponse/Σ或fullnetworkbranchweights，因此不把上面的印刷差异消除，也不将codeagreement当另一项110Cd测量。
