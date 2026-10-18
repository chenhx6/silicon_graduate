---
type: source
title: "In-Beam Angular Distribution and Linear Polarization Measurements with GRETINA Using a Simple Energy-Ordering Approach"
aliases: [Longfellow 2026 GRETINA polarization, GRETINA energy-ordering polarimetry]
created: 2026-07-13
updated: 2026-07-13
status: active
review_status: human-reviewed
source_type: in-beam-method-article
reading_depth: deep-read
title_original: "In-Beam Angular Distribution and Linear Polarization Measurements with GRETINA Using a Simple Energy-Ordering Approach"
authors: ["B. Longfellow", "P. C. Bender", "C. Mueller-Gatermann", "D. Seweryniak", "T. Beck", "et al."]
journal: Nuclear Instruments and Methods in Physics Research A
year: 2026
volume: 1082
pages: 170932
doi: 10.1016/j.nima.2025.170932
language: en
canonical_source: doi:10.1016/j.nima.2025.170932
citation_key: longfellow_2026_Inbeamangular
raw_file: "raw/papers/2026_Longfellow et al_In-beam angular distribution and linear polarization measurements with GRETINA using a simple energy.pdf"
raw_sha256: FB3B4F5E4DCE6A436BB569B64AF1914C6B673561374D7867A3D906AEF7090DF1
nuclei: [25mg, 25na, 22ne]
reactions: ["18O + 9Be fusion-evaporation"]
observables: [angular-distribution-coefficient, gamma-ray-linear-polarization, experimental-asymmetry, polarization-sensitivity, multipole-mixing-ratio]
methods: [tracking-array, compton-polarimetry, angular-distribution, linear-polarization-asymmetry, doppler-correction, lorentz-boost-correction]
tags: [gretina, in-beam, energy-ordering, lorentz-boost, aberration, rose-brink, gaussian-alignment]
---

# Longfellow et al. (2026): GRETINA In-Beam Angular Distribution and Polarization

## Bibliographic Record

B. Longfellow et al., *Nuclear Instruments and Methods in Physics Research A* **1082**, 170932 (2026; online 2025), DOI `10.1016/j.nima.2025.170932`, citation key `longfellow_2026_Inbeamangular`.

The title, author list, DOI, volume and article number match the BibTeX record uniquely. The full ten-page PDF was read, including the formalism in Sec.2 and Eqs.(1)-(19), the ATLAS/GRETINA setup, angular-distribution and polarization sections, Tables 1-3, Figs.1-7, the summary and appendix.

## Scope and Reading Depth

This is an `in-beam-method-ingest + tracking-array-ingest + relativistic-correction-ingest` source. It tests GRETINA as a Compton polarimeter in a fusion-evaporation experiment using a pragmatic energy-ordering rule for interaction points. It is a method characterization with known or literature-established transitions, not a universal proof that energy ordering is better than full tracking.

## Summary

Longfellow et al. combine laboratory-frame angular distributions with GRETINA Compton-plane asymmetries in a fusion-evaporation experiment. The formalism keeps transition mixing, Gaussian magnetic-substate alignment, detector sensitivity, Lorentz angle aberration and event-by-event Doppler energy correction as separate terms.

## Experimental Setup

- A 55-MeV `18O` beam on a 1.152 mg/cm2 `9Be` target was used at the ATLAS facility. GRETINA had twelve quad modules (48 36-fold segmented HPGe crystals; 47 used at high voltage), with groups at laboratory angles 90, 122 and 148 degrees. The Fragment Mass Analyzer selected reaction products (p.3, Sec.3, Fig.1).
- The reaction products included `25Mg`, `25Na` and `22Ne`. The paper analyzes stretched electric quadrupole, stretched electric dipole and mixed magnetic-dipole/electric-quadrupole transitions with both Delta-J=0 and Delta-J=1.
- GRETINA was treated as independent crystals with no addback for this analysis. Interaction points were ordered by energy rather than selected with a full tracking figure of merit; the highest-energy point was taken as the first interaction point.

## Key Results

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| L26-1 | The paper characterizes GRETINA's angular-distribution and linear-polarization performance in a fusion-evaporation experiment using a simple energy-ordering approach for interaction points. | author-interpretation/method | direct | Abstract; pp.2-3, Secs.1-3 | false |
| L26-2 | In the center-of-mass frame the angular distribution is `W(theta)=sum a_lambda P_lambda(cos theta)` over even lambda (Eq.1). For an in-beam source, the laboratory expression includes a Lorentz transformation and a common forward-compression solid-angle factor `(1-beta^2)/(beta cos(theta_lab)-1)^2` (Eq.2). | method/formalism | direct | p.2, Eqs.(1)-(2) | false |
| L26-3 | The aberration relation used to map the laboratory angle to the center-of-mass angle is `cos(theta)=(cos(theta_lab)-beta)/(1-beta cos(theta_lab))`, with `beta=v/c` for the emitting nucleus. | method/formalism | direct | p.2, text below Eq.(2) | false |
| L26-4 | The coefficients are expanded as `a_lambda=A_lambda B_lambda Q_lambda`: transition geometry and mixing enter `A_lambda`, magnetic-substate population enters statistical tensors `B_lambda`, and finite detector solid-angle attenuation enters `Q_lambda`. Fusion-evaporation populations are modeled as a Gaussian in magnetic-substate `m` with width `sigma` (Eq.6). | method/formalism | direct | pp.2-3, Eqs.(3)-(6) | false |
| L26-5 | The direction-polarization correlation is written in `W_pol(theta,phi)` with associated Legendre polynomials and a parity/higher-multipole sign factor (Eq.7). The paper defines physical polarization as a ratio of `W_pol` at phi=0 and 90 degrees (Eq.9), and gives mixed quadrupole-dipole and pure multipole forms (Eqs.10-13). | method/formalism | direct | pp.2-3, Eqs.(7)-(13) | false |
| L26-6 | In the laboratory-frame polarization ratio, the forward-compression solid-angle factor is common to numerator and denominator and cancels, but the aberration angle transformation remains inside the angular and polarization functions. | method/formalism/boundary | direct | p.3, text immediately after Eq.(13) | false |
| L26-7 | The Compton-scattering cross section is given by Klein-Nishina (Eq.14), with analyzing power Sigma(psi) in Eq.(15). After integrating over the array's theta_lab and Compton-angle coverage, the paper defines average polarization `Pbar`, sensitivity `Q` and the measured asymmetry `A0=1/2 Q Pbar` in `W_C(xi)=N(1-A0 cos(2xi))` (Eqs.16-17). | method/formalism | direct | pp.2-3, Eqs.(14)-(17) | false |
| L26-8 | The Doppler-energy relation `E_gamma=E_gamma,lab (1-beta cos(theta_lab))/sqrt(1-beta^2)` (Eq.18) is applied event by event using the first interaction-point direction. This energy correction is separate from the Lorentz angular aberration in Eq.2, although both use the same beta and event geometry. | method/formalism | direct | p.3, Sec.3 and Eq.(18) | false |
| L26-9 | The in-beam angular distributions are normalized with isotropic 56Co and 152Eu source data and background subtraction. The authors report a Lorentz-boost effect ranging from about 0% to -9% between theta=pi/2 and pi for the velocities in this experiment. | observed-fact/method-boundary | direct | p.3, Sec.4 | false |
| L26-10 | For the polarization analysis, events with at least two interaction points summing to the Doppler-corrected full-energy peak are retained. The first and second points are assigned by energy ordering and define the Compton-scattering plane and xi angle. | method/formalism | direct | pp.5-6, Sec.5 and Fig.3 caption | false |
| L26-11 | Under the present conditions, including events with more than two interaction points increased the 1275-keV `22Ne` statistics by nearly a factor of two and produced higher asymmetry sensitivity than exactly-two-point events; this is a present-setup result, not a universal ranking against full tracking. | observed-fact/method-boundary | direct | p.5, discussion of Fig.3 | false |
| L26-12 | The measured asymmetries for transitions in `25Mg`, `25Na` and `22Ne` are compared with predictions from measured `a2/a4`, array coverage and the energy-dependent GRETINA sensitivity `Q(Egamma)` (Eq.19); signs and magnitudes are reported as mutually consistent within uncertainties. | observed-fact/author-interpretation | direct | pp.6-7, Table 2 and Eq.(19) | false |
| L26-13 | For the 1041-keV `25Na` transition, angular distributions permit mixing-angle solutions near `delta=0` and `delta=-0.85` in the Rose-Brink convention. The predicted polarization asymmetry favors `delta=0` for the adopted alignment and sensitivity, while the paper notes that a different `sigma` or `Q` would change the prediction. | experimental-criterion | direct | p.7, discussion below Table 2 | false |
| L26-14 | The appendix shows that Gaussian width `sigma/Ji` attenuates `a4` more strongly than `a2` (Fig.6). For mixed transitions, the signs of `a2`, `a4` and the polarization component `P0` depend on Delta-J, parity and mixing; the sign of `A0` alone cannot generally identify electric versus magnetic character. | method-boundary/experimental-criterion | direct | pp.7-8, Figs.6-7, Table 3 and Appendix | false |
| L26-15 | In the small-mixing limit, a pure E2 transition and an E1+M2 mixed transition with Delta-J=0 can share the same positive sign of `A0`; therefore angular-distribution signs and polarization-asymmetry signs must be interpreted jointly with multipolarity, mixing and alignment information. | method-boundary | direct | p.8, Appendix and Table 3 | false |
| L26-16 | The summary reports that the measured angular distributions and polarization asymmetries are consistent with the theoretical formalism and known transition assignments, and that simple energy ordering yields useful characterization under the stated experimental conditions. | author-interpretation | direct | p.7, Sec.6 | false |

## Relativistic Correction Boundary

The source supports the following chain without collapsing distinct corrections:

1. The angular distribution is first defined in the center-of-mass frame (Eq.1).
2. The laboratory angular distribution uses the aberration map in L26-3 and the forward-compression solid-angle factor in L26-2.
3. The same common factor appears in the polarization numerator and denominator and cancels in the ratio, but the transformed angle still changes the functions being evaluated (L26-6).
4. Direction-polarization correlation is evaluated with laboratory event directions and Compton-plane geometry through `xi` (L26-5, L26-7 and L26-10).
5. Doppler energy correction is a separate event-by-event transformation (Eq.18), needed to place interaction events in the correct full-energy peak and not a substitute for the angular transformation.
6. The reported 0 to -9% boost effect shows why a small `beta` should not be silently equated with a zero correction in this analysis; the numerical significance remains experiment- and angle-dependent.

## Competing Interpretations and Limitations

- Agreement with known transition assignments validates the method under the stated setup; it does not make energy ordering universally equivalent to full tracking.
- Polarization signs and angular-distribution coefficients remain dependent on Delta-J, parity, mixing ratio, alignment width, response coverage and sign convention.
- The reported boost range is an experiment-specific result and should not be transferred without recalculating the angular acceptance and residue velocity.

## Extracted Pages

- Pages 1-3: angular-distribution/polarization formalism, Rose-Brink mixing, statistical tensors and Lorentz transformation.
- Pages 3-4: ATLAS/GRETINA setup, Doppler-energy equation, source normalization and angular distributions.
- Pages 5-7: energy-ordered Compton events, measured/predicted asymmetries and GRETINA sensitivity.
- Pages 7-8: Gaussian-width and mixing-angle appendix, sign ambiguity and Table 3.

## Related Wiki Pages

- Concepts: [[gamma-ray-linear-polarization]], [[magnetic-substate-population]], [[spin-alignment]]
- Methods: [[tracking-array]], [[compton-polarimetry]], [[angular-distribution]], [[linear-polarization-asymmetry]], [[doppler-correction]], [[lorentz-boost-correction]]
- Observables: [[angular-distribution-coefficient]], [[experimental-asymmetry]], [[polarization-sensitivity]], [[multipole-mixing-ratio]]
- Project: [[gamma-ray-linear-polarization-in-nuclear-spectroscopy]]

## Human Review Triage

P0 review completed: L26-2/L26-3 (Eqs.1-2 and aberration/Jacobian), L26-5/L26-6 (polarization transformation and cancellation of the common factor), L26-7/L26-8 (Q/Pbar/A0 and Doppler-energy distinction), and L26-14/L26-15 (sigma/J and sign ambiguity) were checked as the relativistic and P/A/Q evidence chain for this project.

The user-reviewed source has no remaining claim-level `needs_review: true` items. Formula-level, numerical and sign-sensitive claims were checked against the cited equations, tables, figures and appendix; the separation between Lorentz angular correction, Doppler energy correction and energy ordering remains explicit.

## Project Relation

This source is the in-beam tracking-array and relativistic-correction branch of [[gamma-ray-linear-polarization-in-nuclear-spectroscopy]]. It connects Jones's P/A/Q calibration language and Go's detector-response inference to a GRETINA analysis in which angular aberration, Doppler correction, alignment width, mixing ratio and Compton geometry are explicitly separated.


## DAY16无学分预习增量：数据身份与新约定自审

2026-10-18本session完整重读10页（主线1–8、references9–10），视觉核Figs.1–7、Tables1–3/Eqs.(1)–(19)。**上方整段旧页面、L26-1–16及原human-review文字逐字节保留；旧审阅范围不覆盖本段新增claims。** 下列均needs_review；特别是L26-15的旧例句须同时核L26-19，不把旧flag当作新物理判据的审阅。

### 新增原件事实与条件复算

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| L26-17 | Fig.1标签实际给25Mg β=.048、25Na .046、22Ne .044；Table1的δ是Eq.(3)的dimensionless amplitude ratio，Fig.7横轴δ从−8到8，不能当atanδ角度。pure E2行的δ=0也不是M1/E2的pureM1端点。 | identity-unit-and-channel | direct | PDF3 Fig.1；PDF5 Table1；PDF8 Fig.7；Eq.(3) | true |
| L26-18 | 25Na1041的9/2+→9/2+给a2fit=.20(.02)、a4fit=.00(.04)，作者AD两候选约δRB=0/−.85；A0fit=.043(.008)，采用Q/布居下pred约.021(.007)/.002，后者未单列误差。作者偏好0并说明σ或Q改变会改预测；无本run可用jointCov或原fit ledger。 | reported-branch-and-readiness | direct/author-interpretation | PDF5 Table1；PDF7 Table2后1041讨论 | true |
| L26-19 | Appendix p7例句称pureE2与E1+M2 ΔJ0 smallmix都positive A0，但Table3同E1+M2行是negative。原Fig.7路径/σ/J=.3按原式计算δ→0时，M1/E2的P90=.726274、E1/M2为−.726274，支持Table3方向。两原文位置保留，未猜官方勘误；L26-15不能再单独作positive E1/M2物理规则。 | source-internal-conflict-and-limit-check | direct-and-Codex-calculation | PDF7 Appendix例句；PDF8 Table3/Fig.7；Eqs.(3)–(11) | true |
| L26-20 | Eq.(4)后“CG在oddλ为0”不是一般CG恒等式：C(1,1;1,−1→1,0)=1/sqrt2非零。本文Eq.(6)的m↔−m对称布居使Bodd=0，仍支持实际aligned设置的even-only展开；不把该解释句当普遍选择规则。 | mathematical-explanation-boundary | direct-and-Codex-calculation | PDF2 Eq.(4)后文字及Eqs.(5)–(6) | true |
| L26-21 | 原Racah/RB系数与D96 native单γ emission kernel在相同spin/state/分析轴下由δnative=−δRB相连；本run的3→2 mixed/pure AD/P对照最大差3.89×10^-16，错误同号混用差达1.5336而pure端点仍过。该桥不是所有cascade role的通用换号。 | phase-role-and-observable-check | conditional-calculation | PDF2 Eqs.(3)–(4)/(9)–(11)；DR96-8/9定义及本run fullkernel对照 | true |
| L26-22 | 要让puredipole与mixedδ→0形式连续，本任务的working bridge区分upper-multipole E/M sign与physical photon parity：tauEM(upper)×(−1)^Lupper=Pi_photon。Morse pure公式用Pi_photon，L25另明定E/M sign。L26未充分独立定义其Pi，本桥是由原式/纯极限/Table3重构的操作合同，不冒称作者已明确给出该定义。 | sign-symbol-contract | Codex-reconstruction | PDF2 Eqs.(7)/(11)–(13)；Table3；M22 Eq.(2)；L25 Eq.(31)/(35) | true |
| L26-23 | Eq.(19)的.131/3.25×10^-4来自Morse原preprint对模拟GRETA500–2000四点的fit，并非本篇实测GRETINA多能标定；当前12quads/energy-order/noaddback与上游6quads/tracking不同，2419/3970等在该模拟范围外。原1368点/tuning也不是独立验证同curve。 | calibration-lineage-and-domain | direct-source-crosswalk | PDF6 Eq.(19)/其前段；M22 PDF10–11 Sec.4.4/Eq.(13) | true |
| L26-24 | 本篇和Morse都定义A0=Q Pbar/2。若同P/同响应下改用A0=Qnew Pbar，须同时Qnew=Q/2；observable不变。L25的Q是自己的measured/ideal folded-curve ratio，有γγ参考/角门；不能直接把.33替.196或固定Q删除半因子来强配1041。 | normalization-and-response-contract | direct-and-Codex-algebra | PDF3 Eq.(17)；PDF6 Eq.(19)；M22 Eq.(8)；L25 Sec.5.4/Table2 | true |
| L26-25 | 声明单Compton+末端photoabsorption的two-hit full-energy事件，最高deposit真为first要求Eprime<E/2，即cosψ<1−511/Elab；≤255.5keV时不可能。换序不改变target/两点组成的unoriented Compton plane，却通常改变beam/first-point reaction plane及Doppler方向。它是kinematic design，不是本实验misorder率或≥3hit性能重测。 | Codex-kinematic-failure-control | conditional-design | PDF3能量排序/Eq.(18)；PDF5 Sec.5；M22 Eq.(4)–(6)/Fig.1 | true |
| L26-26 | Eq.(11)中的(A2prime/A2)a2在A2=0时字面0/0，但若一致采用a2=A2B2Q2，其未相除的A2primeB2Q2可有限。原Fig.7的9/2→9/2、σ/J=.3在δRB=.57787494处a2=0而P90=.43201160。未据此指认作者实际代码失败。 | numerical-representation-boundary | conditional-calculation | PDF2 Eq.(11)；PDF8 Fig.7 | true |

### 真实8行与phase/pure controls

[冻结主表输入](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/l26-primary-input.json)保留8条transition的spin、lower/upper multipoles、δRB、Gaussian宽度、AD与A0原值。以原Eq.(4)的Racah W顺序、Eq.(5)的B和Eq.(6)明确2σ²做中央复算，未调δ/σ去对齐原表；Q_lambda取作者close-to-one的**声明近似1**，不认证actual response。25Na1041中央得a2=.20374746/a4=0，与印刷.20/0口径相容；其alternatives的sigma/完整producer未给，不造另一支新CI。

[程序](../../system/scripts/day16_gretina_convention_audit.py)/[结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/gretina-convention-audit.json)将source-Racah计算和显式photon trace分开，δ/RME名、spins与emission角色固定后才比较。只过pure limits不能确认interference phase。L26-21的单γ桥不替代KS70/D96在first/last cascade中的完整state/operator约定。

Table3中的符号还需multipole/spin条件；p7的具体E1/M2例与该表相反，不能因原页面曾reviewed而隐藏。这里仅给self-audit增量，旧人工事件/flags不修改，也未将新分析设human-reviewed。

### calibration与companion的匹配边界

Morse已实际取得/读完13页author preprint，见[[morse-2022-gretina-polarization-sensitivity]]。L26的8条数据、两种AD处理和ξ分布是同一fusion acquisition，不按核素/图表数计独立实验。Morse是另一反应/阵列配置的标定；其simulation/tuning/GRETA curve共享输入。L25的source γγ选择又与无偏振source singles不同；是否共享某些原source events未认证。

1041的作者选支可以作为**adopted response下的解释**；没有matched角/point/energy response、AD–A0及a/Q联合Cov，不能将原quoted margins做独立z test或新δ posterior。当前无R_DCO数据；FMA species/峰门与γγ reference gate须区分。案例的durable ledger见[[gretina-25na1041-polarization-response-contract]]。

角coverage的平均P、Compton analyzing-power的平均Q与二者joint平均也不是自动同一对象；实际theta/psi/cut kernel缺失时不能从一条Q(E)补全。本文Fig.4的无cut/有cut A0=.028/.044及Pbar约.35/.53保留作原作者报告，不据此反推一份独立Q标定。


## Fig.4的公开矢量曲线：平均的测度与校准范围

本session从原PDF5直接提取vector SVG，而非从示意图造raw响应：Fig.4 top的黑coverage路径218点、红P路径2908点；坐标用图框/0、π/2、π和y=0/1原刻度锁定。公开PDF/SVG/path的hash、完整coverage坐标在冻结input/结果中保留。均值计算前已经暴露原.35/.53/.028/.044，明确primed重放；未调axis/curve/δ/sigma强配这些目标。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| L26-27 | 原Fig.4 top黑/红路径按“归一source coverage乘P”逐段积分，full/cut给.37792305/.54387018，未按最后印刷位闭合正文约.35/.53。另原Table1第二种fit的sigma/J=.55/Racah模型同红曲线最大差.0002641，printed direct a2=.34/a4=−.12模型最大差.004542。原approx没有声明精确误差，实际selection/kernel/未舍入producer缺失，未判实验错误。 | published-vector-arithmetic | conditional-replay | PDF5 Fig.4 top/caption；PDF6首段.35/.53；PDF5 Table1；Eq.(12) | true |
| L26-28 | 对Fig.4 coverage Cθ与声明factorized point-response，coverage平均CP/C与event平均CWlabP/CWlab不同；direct-AD模型full为.3814275/.3623012，cut约.547017/.546949。改平均须相应重定义经验Q，不能保留同Q来“修正”A0。真实joint θ–ψ/cut/point kernel未给，这不是实际response重建。 | Codex-response-average-and-calibration | conditional-design | PDF2 Eqs.(12)/(16)；PDF3 Eq.(17)前平均说明；PDF5 Fig.4与Sec.5 | true |
| L26-29 | Fig.4 cut1.40–1.75的公开source覆盖积分约余.19669；声明factorized event模型约余.16288。实测A0比.044/.028=1.57143，仅在knownresponse、无背景、同uniform-ξ模型且比较固定角形状的共同偏振幅度scale时，需要保留fraction>.40496才增加counting information。图中C不是实际Compton-selected counts，故不据此宣判真实cut有害或给新束流时间。 | Codex-cut-design-and-missing-input | conditional-design | PDF5 Fig.4；PDF6 cut比较段；Eq.(17) | true |

### 图示算术与物理响应各算哪一个平均

令Cθ是source每θ-bin的coverage直方图（图中纵向overall scale任意），与Wlab相乘前不再额外乘sinθ。正文所描述的算术对应

\[
\overline P_C=\frac{\int C_\theta(\theta)P(\theta)\,d\theta}
{\int C_\theta(\theta)\,d\theta}.
\]

若改变量x=cosθ，测度须带1/sinθ；本run两种积分结果最大差1.12×10^-16。随意再乘sinθ会把direct-AD的full结果改成.422054，不是同一个average。16/32点Gauss积分与C overall scale×7的控制均通过。零P、constant P和所有positive intensity控制也保持；vertical step对积分测度贡献0。

| 原件/声明模型 | full的source平均 | cut的source平均 | full的声明event平均 | cut的声明event平均 |
| --- | --- | --- | --- | --- |
| 实际公开红P×黑C路径 | .37792305 | .54387018 | 不从两条图补joint response | 同左 |
| printed direct a2=.34/a4=−.12，β=.044 | .38142750 | .54701697 | .36230124 | .54694921 |
| 原sigma/J=.55/纯E2 source-coefficient模型，β=.044 | .37790650 | .54383139 | .35897240 | .54376609 |

这里event平均额外**声明**相同source C可作factorized polarimeter acceptance，Wlab含原aberration/Jacobian：

\[
\overline P_{CW}=\frac{\int C_\theta W_{\rm lab}P\,d\theta}
{\int C_\theta W_{\rm lab}\,d\theta}.
\]

实际polarimetry含≥2points、峰/背景/source除法、可能的θ预归一与非factorized响应；一条1238-source coverage不足以证明这个声明kernel就是原producer。因此原均值不闭合、两平均差与caption“measured coefficients”对红curve的匹配，均保留为**重放边界**，不擅自给原结果原因。两组published模型都是事前固定，未优化参数或声称已恢复未舍入fit。

±.01 page-point的axis/zero独立扰动只检digitization registration，18个保持非负C的corner给direct-AD full约.381352–.381473；9个产生negative C的corner明确拒绝，没有clip或移动baseline。它不是统计error或总图形误差界，也不把prose的“about”当±.005 CI。red cutline自动隔离没有成功；积分门取作者caption/text明确1.40–1.75，未靠反推Pbar选门。

### 一个Q平均不能补回joint kernel

声明η(θ,ψ,ξ)等响应后，实际归一ξ harmonic一般涉及带响应的〈Sigma(ψ)P(θ)〉。分别求Q=〈Sigma〉和Pbar=〈P〉再相乘，除非证明对应measure下独立/可分或采用一致的**有效定义**，不自动等于joint平均；差异可写成同measure下Cov_kernel(Sigma,P)。这是detector weighting中的函数相关，不是fit统计Cov，两者都不能从单Cθ图恢复。

假设只为说明identity，true harmonic为A=κq Pbar_event，则按另一平均标出的经验Q_C=A/(κPbar_C)=q Pbar_event/Pbar_C。换定义后应同时变Q；仅在实际response q本已相同的条件下，从calibrator c迁target t会留下ratio[(P_event/P_C)_t/(P_event/P_C)_c]，只有两ratio相同才抵消。不能只改target的Pbar并固定由另kernel标的Q，来把prediction向A0fit调近。

图中红/黑积分得到的cut/full约1.439；声明event模型约1.515，原作者约.53/.35=1.514、A0比1.571。这种相近不是原producer采用某kernel的证据，不能据接近程度选择或调整模型。对sourceC的cut retention也不能当实测polarimetry yield；下一必要输入是实际Compton θ/ψ/ξ与cut/background/source ledger、matching Qcal与完整Cov。

[218点/axis冻结输入](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/l26-coverage-vector-input.json)、[事前模型合同](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/l26-coverage-averaging-contract.json)、[代码](../../system/scripts/day16_gretina_coverage_average.py)、[完整路径/平均/registration结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/l26-coverage-average-audit.json)。原PDF与上方humanprefix保持，新增claims仍needs_review，无新P/Q测量或正式Day17信用。

这里的cut counting-information条件比较固定P(theta)形状下的共同scale，不直接给混合比delta的likelihood信息。不同delta会改变角形状/强度；matched joint响应/布居及Cov仍需另外处理。
