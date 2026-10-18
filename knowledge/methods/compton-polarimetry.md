---
type: method
title: "Gamma-Ray Compton Polarimetry"
aliases: [Compton polarimetry, gamma-ray Compton polarimeter]
created: 2026-07-13
updated: 2026-10-19
status: active
review_status: unreviewed
method_type: gamma-ray-polarimetry
tags: [compton-scattering, linear-polarization, detector-response, parity]
---

# Gamma-Ray Compton Polarimetry

## Purpose

Compton polarimetry infers the linear polarization of gamma rays from the azimuthal dependence of Compton-scattering events. The scattering plane is correlated with the incident electric-field direction through the Klein-Nishina cross section.

## Inputs and Assumptions

- Calibrated energy and position information for the scatter and absorber interactions.
- A defined azimuth convention, accepted Compton-scatter angle range, detector response and background treatment.
- A reference polarization or validated response simulation when converting a modulation to `P`.

## Core Chain

1. Select events with a reconstructible scatter and absorber interaction.
2. Form an azimuthal distribution or detector-pair count asymmetry.
3. Correct or model detector geometry, efficiency, background and accepted Compton-scatter angles.
4. Relate the measured modulation to physical polarization with a calibrated sensitivity `Q` or a simulated detector response.

The analyzing power is a Compton-scattering property and depends on photon energy and scatter angle. It is not the same as nuclear angular-distribution alignment.

## Detector Implementations

- Clover and segmented HPGe arrays provide compact Compton event selections.
- GRETINA/AGATA tracking arrays provide many interaction positions and a continuous angular phase space, but still require response and ordering treatment.
- Go 2024 demonstrates a twenty-layer position-sensitive CdTe camera for a 847-keV calibration line. Its likelihood and Geant4/ComptonSoft chain is a detector demonstration, not a universal replacement for HPGe arrays.

## What It Can Establish

With calibration and response control, Compton polarimetry can constrain the linear polarization and electromagnetic character of selected gamma-ray transitions.

## What It Cannot Establish Alone

It cannot by itself fix nuclear alignment, choose a unique mixing-ratio branch, or establish a nuclear-structure interpretation without the transition and population context.

## Boundaries

Physical `P`, measured `A`, sensitivity `Q`, modulation factor `Q'`, and efficiency `epsilon` must be reported separately. A detector simulation characterizes response; it does not establish a nuclear-structure interpretation by itself.

[[zheng-2013-linear-polarization-91ru]] gives a clover-specific in-beam example: the measured asymmetry uses adjacent-crystal horizontal/vertical scatters, `A=([aN⊥]−N∥)/([aN⊥]+N∥)`, and the EXOGAM sensitivity is fitted as `Q=Q_point(p0+p1Eγ)` from known pure E2 transitions. The reported figure of merit is detector- and energy-dependent; the source does not define a universal `Q` or asymmetry sign outside its geometry and convention.

[[garciaraffi-1997-monte-carlo-compton-polarimeters]] adds the response-simulation layer: modified GEANT3/Stokes tracking reproduces five-coaxial, four-coaxial and CLOVER `Q(E)` values to roughly 10% for the tested geometries. Multiple-scatter polarization propagation is essential; first-scatter-only treatment underestimates `Q` in the four-crystal test. The quoted `Q` and `M=εQ²` remain geometry/threshold/window specific.

[[bass-1972-two-crystal-compton-polarimeter]] provides an early symmetric two-crystal coincidence/anticoincidence design; its `R(E,E_th)` and efficiency trade-off are explicit detector-response quantities.

[[klein-nishina-1929-compton-scattering]] is the free-electron relativistic response foundation; it does not include polarization, finite geometry or detector sensitivity.

[[vonderwerth-1995-compton-polarimeters]] supplies POLALI/MINIPOLA modular detector designs and the kinematic-gate/sensitivity/efficiency figure-of-merit trade-off.

[[schmid-1998-gammasphere-polarization]] supplies the segmented-Gammasphere confined/shared asymmetry and Monte Carlo `Q(E)` validation, including high-background `197Pb` parity application limits.

[[droste-1999-ppco-polarization]] extends CLOVER polarimetry to PPCO two-γ correlations; alignment and both detector sensitivities remain explicit inputs.

[[starosta-1999-pdco-experimental-test]] provides the complementary single-transition PDCO validation: `A=QP`, a detector-specific `Q(E)` calibration and four polarimeter/gamma-detector geometries are combined with `R_DCO`. Its `490 keV` case remains E2 versus ΔI=0 M1/E2 ambiguous, and integrated-mode `P` is qualitative unless solid-angle and efficiency corrections are known.

2026-10-17原件补核：ST99-6的Q拟合是`Q0[.31(2)+7(2)×10^-5 E_keV]`，旧Wiki10^-4已纠正。NORDBALL79°单CLOVER标定向EUROGAM所选18polarimeters移用，不提供完整gate/pair response；四组P与integrated P也非独立新采集。[[st99-pdco-calibration-table-replay]]保存全部13行式7重算、未闭合行、NDF和chosenCov排序反例；不把printed边际误差当实际完整Sigma。647的共同E1类别不独立唯一固定11−。

[[droste-1996-pdco-formalism]] is the formal precursor: one statistical-tensor expression covers DCO, PDCO and PPCO, with explicit detector-plane, emission-angle, deorientation and Gaussian-alignment terms.

[[jones-1995-clover-compton-calibration]] is the early four-crystal EUROGAM calibration: `P`, count asymmetry `A` and sensitivity `Q=A/P` are kept separate, with `Q` falling from `0.34(9)` at 197 keV to `0.121(5)` at 1368 keV for a 60-keV threshold. The fit and threshold are geometry-specific.

[[miller-2007-sega-polarization]] extends the response map to side-irradiated SeGA: a `249Cf` α–γ calibration gives `Q≈0.14(2)` near 350 keV and `FM≈5.9×10^-6`. The side orientation, geometric asymmetry and finite-angle correction are part of the calibration identity.

[[aoki-1975-geli-summing-polarimeters]] is an early simultaneous-angle Ge(Li) design: a central scatterer and four analyzers measure `φ=0°,30°,60°,90°` without rotation; majority anticoincidence reduces Compton background, while the ring-reflector summing spectrometer trades efficiency for a flat low background and a practical ≈300-keV threshold.

## Jones1995：标定系数、偏振误差与阈值信息

[[jones-1995-clover-compton-calibration]] JO95-5纠正原有C转录：Eq4是`Q=Q′(B+CE_MeV)`，`B=.29±.03`、`C=0.0±.003 MeV^-1`，不是C中心值.003。换成keV时C sigma为3×10^-6；未给Cov(B,C)，不将边际误差独立拼成曲线置信带。C=0只使Q/Q′为常数，不让Q本身与能量无关。

JO95-6的P并非从一个假定Gaussian sigma直接给定：以70%coaxial在五角度测angular distribution、CLOVER addback作monitor，用STAG拟合子态布居并做finite-angle修正；A/a由另一配置的90°/0°CLOVER及pair-trigger取得。AD与polarimetry有共同normalization/response依赖，不能只把P写成无误差外部标尺。

### 已归一pureE2系数到名义P90

在**pureE2、point90°、同一已归一angular coefficients**条件下，不需要另猜Gaussian布居即可写

$$P_{90}=\frac{\frac32a_2+\frac58a_4}{1-\frac12a_2+\frac38a_4}.$$

这里a2/a4是W/其constant的实际系数，不是maximum coefficients、核attenuation alpha或几何a。由[[droste-1996-pdco-formalism]] Eq4/8/12，pureE2的H2=−sqrt6、H4=sqrt(5/2)；`−H_k d^k_(0,2)(pi/2)`正好为3/2、5/8。比值中的共同归一抵消。mixed multipoles、finite acceptance及非轴对称输入不可直接套此式；2+→0+的triangle/parity强制E2，但5/2→1/2的相容central值不独立排除M3。

令D=1−a2/2+3a4/8，则

$$g_2=\frac{1.5+.875a_4}{D^2},\qquad
g_4=\frac{.625-.875a_2}{D^2},\qquad
\operatorname{Var}_{\rm local}P=g^T\Sigma_{a_2a_4}g.$$

未知Cov不能自动取零。只固定两边际sigma时，local sigmaP必在`[||g2|s2−|g4|s4|, |g2|s2+|g4|s4]`内；这是线性化与nominal printed sigmas的条件界，不是confidence region或原STAG误差预算。

| JO95 Table2核/keV | 印P(sigma) | 名义point P | 独立a2/a4时sigmaP | 任意两系数Cov的local sigma范围 |
| --- | --- | ---: | ---: | --- |
| 19F197 | .23(.06) | .231608 | .074248 | .046982–.093905 |
| 109Ag415 | .39(.04) | .382772 | .030015 | .008607–.041565 |
| 107Ag423 | .45(.04) | .452416 | .062732 | .044657–.076658 |
| 56Fe845 | .53(.03) | .530864 | .068686 | .044353–.086420 |
| 24Mg1368 | .99(.04) | .986696 | .013941 | .001561–.019654 |

central values接近原表，但部分印sigma不在这个nominal local范围内，Mg尤为清楚。误差末位舍入、原finite-angle/normalization、STAG recipe、额外预算及非线性处理未重放，不能把此诊断升格为作者错误，也不能反推一个不存在的实际Cov。五行A/原表P的Q中央复算及仅A/P局部传播另保存；Q、P、angular coefficients是同链派生列，不增独立证据。

### Qprime识别与跨标定的受限比较

Jones只用文字描述Q′来自KN point scatterer、psi0/90和scatter90°，未印显式代数式。**若**识别成[[starosta-1999-pdco-experimental-test]] Eq6的`Q0=(1+x)/(1+x+x²)`，x=E/511keV，则JO95 B=.29/C=0在1368keV给Q=.098337，而Table2印.121(5)；这没有闭合normalization/fit weighting/unrounded producer，不能宣布原曲线完全重放或自行修改B。

在同一有条件的Q′识别下，490keV JO95/ST99 central曲线分别.197360/.234314，比例1.187241。它们的校准targets、measurement geometry/threshold/selection不同，实际curve Cov及具体device identity未核；这个差值不是统计矛盾或某一个器件systematic原因的认定。ST99提threshold/collimator为可能解释，不是经本任务证明的因果。

### 计数型figure of merit的使用条件

JO95-7原Eq5是`F=Q²(Nperp+Nparallel)`，其中N是当次接受的计数，不是source报告的21%/125%相对NaI photopeak efficiency，也不自动等于其它array的absolute epsilonQ²。Fig5是同采集的离线threshold scan，点间共享事件，不能把所有点误差独立使用或仅看图指定普适最佳threshold。

在a=1、known Q、无背景且条件总N固定的二项模型，`Pr(perp)=(1+QP)/2`，Fisher信息为`NQ²/(1−Q²P²)`。source F是小asymmetry时的统计信息近似；未知Q/a、背景、selection和shared calibration会降低或改变信息。这个推导不填造原Fig5计数、cut Cov或新的优化结果。

[冻结输入](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-jo95-calibration-input.json) SHA-256 `c3d74a1088d3cb691571aa72a64b74d833b03180192d78fcae99abfc25163f66`，[脚本](../../system/scripts/day16_jo95_calibration_audit.py)与[完整结果](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-jo95-calibration-audit.json)核source/input/code hash；H与Jacobian独立差分核验通过。source JO95-8/9保留条件边界，未取得STAG、actualSigma、finite-response或事件；当前只L2核算/L3设计。

## Simpson1983：效率分母与共享sector模式

[[simpson-1983-sectored-geli-compton-polarimeter]] S83-8/10/11给出更具体的count/response边界。其Eq7保留

$$\epsilon_c(E)=\left[\frac{N_\parallel+N_\perp}{2N_s}\right]_{\theta=0}\epsilon_s(E),
\qquad F_\epsilon=Q^2\epsilon_c.$$

Ns为single-crystal计数率，epsilon_s为absolute singles效率。若**就在此theta0、相同selection/曝光T和singles归一**下记`Phi_ref=Ns/epsilon_s`，纯代数给

$$F_{\rm count}=Q^2T(N_\parallel+N_\perp)
=2T\Phi_{\rm ref}F_\epsilon.$$

不能漏掉2、曝光和normalization，或把Phi_ref自动认成总4π photon emission rate。Jones的90°数据还需匹配角分布/曝光，才可比count-F。S83的1.9%是对指定NaI reference的relative efficiency，不能当absolute epsilon_c；Fig2 stat<1%同时有最多10%source-strength systematics，Fig5/6 stat<2%也不提供完整Cov（S83-15）。

### 同事件进入两个计数时须保留Cov

对`A=(aN_perp−N_parallel)/(aN_perp+N_parallel)`，令D为分母，在known a条件的局部传播为

$$\operatorname{Var}A=\frac{4a^2}{D^4}\left[
N_\parallel^2\operatorname{Var}N_\perp+
N_\perp^2\operatorname{Var}N_\parallel-
2N_\perp N_\parallel\operatorname{Cov}(N_\perp,N_\parallel)\right].$$

若a也拟合，还需`dA/da=2N_perp N_parallel/D²`及与counts的cross-Cov；P=A/Q再加入Q/calibration依赖。不能只从一条总多重性直方图或共同ADC推断它们独立。

原Table1的60Co1.33MeV数据给n=1/2/3/≥4约38/42/18/2%，双sector约75%相邻。它与Table2 polarized calibration不是同一采集。下面只用该nominal aggregate检验统计可识别性，不从中估原beam实验实际Cov。

按原Eq6的quadrants `(1,2),(3,4),(5,6),(7,8)`，本任务**选择**每orientation一个Boolean计数：V为两竖直quadrant对的OR，H为两水平对的OR。实际硬件是否双填、互斥、加权或优先路由未得；本选择不是原producer认证。另**选择**相同marginals pH=pV=.25，以加强“连两边计数均值也相同”的检验，不把.25写成观测。

在全部255个非空bit patterns上，对source aggregate和chosen means作正概率LP：pHV可在0–.20；再加全部8个cyclic rotations对称，仍可在.0375–.17125。显式极端mask分布、非负/约束残差与primal–dual证书均保存。它们是统计可行witness，**未证明为真实Compton transport可实现的response**；结论限于这些汇总输入不能唯一恢复chosen routing下的joint overlap。

若这个统计模型的source-event yield为Poisson lambda，则Cov(NH,NV)=lambda pHV；若总事件数固定N，则为N(pHV−pH pV)。在a=1、pH=pV=p、局部A传播下，两种情况下均有`Var(A)×yield=(p−pHV)/(2p²)`。cyclic模型两极端给1.70和.63；naive independent Poisson会给2.00。这里yield不是4π photon rate；没有actualQ，**不能**将其解释为真实P精度改善或实际paper误差修正。

真正可解除歧义的下一输入是：同calibration/gate/threshold的逐事件完整sector mask、core energy/time/eventID、H/V权重与互斥策略，和background/a/Q共同误差预算。S83-13的低能单sector照射发现约5%反向电耦合脉冲，说明需保留电子串扰negative control。S83-14又说明，1369keV校准F随threshold近似平坦，不妨碍弱峰高背景在更高threshold下受益；peak/total的改变不是普适Q或epsilon。

### 已知P与Qprime的伴随来源边界

S83 Table2的known P由Ref6（4430keV由Ref1）采用，未在本次取得这些原文重做；Fe在3.43MeV beam下P=.57(.01)不能无条件替代Jones 3.0MeV下的P=.53(.03)。相同transition并不固定布居/alignment和P。S83的158Er应用又用naturalMo Coulomb excitation复校，不把三者统计独立性混为一谈。

全文直接伴随复核没有补出Jones所缺Q′显式式或B/C producer recipe，因此JO95-9保持open；不靠再拟合B/C或堆历史response曲线消除这个归一缺口。原S83 Pt只写元素未给质量数，本次删去旧Wiki192Pt；不从记忆补另一个同位素。

[冻结输入](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-s83-pattern-input.json) SHA-256 `71401a867ac26cb29d70c7be67f6aa435286aa1163754169c4404a251fcbfaca`，[脚本](../../system/scripts/day15_s83_pattern_identifiability.py)、[LP结果/证书](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-s83-pattern-identifiability.json)与S83-11保持同一chosen模型。此bounded exercise的stop contract已满足；actual sector/Cov/transport缺口仍保留。

## Sources

- [[jones-2002-calibration-compton-polarimeters]]
- [[simpson-1983-sectored-geli-compton-polarimeter]]
- [[garciaraffi-1995-nonorthogonal-compton-polarimeter]]
- [[butler-1973-three-geli-compton-polarimeter]]
- [[logan-1974-generalized-polarimeter-merit]]
- [[go-2024-demonstration-nuclear-gamma-ray-polarimetry-cdte]]
- [[longfellow-2026-gretina-energy-ordering-polarization]]
- [[lauritsen-2025-gamma-angular-formalism-tracking-arrays]]
- [[zheng-2013-linear-polarization-91ru]]
- [[garciaraffi-1997-monte-carlo-compton-polarimeters]]
- [[bass-1972-two-crystal-compton-polarimeter]]
- [[klein-nishina-1929-compton-scattering]]
- [[vonderwerth-1995-compton-polarimeters]]
- [[schmid-1998-gammasphere-polarization]]
- [[droste-1999-ppco-polarization]]
- [[jones-1995-clover-compton-calibration]] JO95-5/6/7/8/9/10。
- [[starosta-1999-pdco-experimental-test]] ST99-6/7/8/13。
- [[droste-1996-pdco-formalism]] DR96-8/9；pureE2的H与分析轴约定。


## Gammasphere双分段的P/A/Q与actual峰面积

[[schmid-1998-gammasphere-polarization]] SG98-4–12在不可旋转的两分段Ge中定义confined C/shared S，并以unpolarized source的eta=Su/Cu修正：

\[
A(C,S,\eta)=\frac{\eta C-S}{\sqrt\eta(C+S)}=Q P.
\]

它不是genericclover平行/垂直的同一计数公式。C包括两侧confined总和，其中一侧在sideADC的zerochannel；该zero是已触发fullphotopeak但sidechannel未过threshold，不是无效事件。按原定义改变cut后需重定eta/Q。

| 层 | 本篇实际对象 | 必要独立输入/条件 |
| --- | --- | --- |
| physical P | 反应平面内/外electricfield分量差和比；给定gamma方向、spin/purity/population与gate | calibration的P由已知pureE2和a2/a4推得，不是从同一A除已校Q作独立验证 |
| measured A | 上式的C/S及eta，不是(C−S)/(C+S) | 真实peakfit/背景、energy/threshold、两侧zero与同detectorselection |
| response eta | unpolarized152Eu的S/C，可能需energy interpolation | 同cut/threshold/arrayweights；不能借Fig9的130keV实例认证Fig10的60keV样本 |
| sensitivity Q | calibration A/P；actual约.043/.047/.052于1368/847/415keV | 与A共享校准依赖，实际fitCov；geometry/threshold不变才可迁移 |
| efficiency/F | 双分段epsilon是photopeak；传统四方向epsilon_c为coincidence | nearA0、knowneta/Q、统计主导时F≈epsilonQ²；高背景拟峰系统项需另核 |

### 真实432-keV行：同名asymmetry不能互换

SG98 Table3给197Pb432 line：C=30934±402、S=4449±125、eta=.163±.003。依原Eq15中央值A=.04152823。直接(C−S)/(C+S)约.7485，另一个balanced-denominator `(etaC−S)/(etaC+S)`约.06250，都不是这篇Q所校准的A，不能沿用原Q换算P。source列A=.041(.011)、P=.75(.20)；其Q取normalizedMC/calibrationcurve，未给精确curve coefficients，不从圆整A/P造出新的独立Q。

源Table3的误差来自DAMM多peak/background拟合，不能令Var(C)=C、Var(S)=S来覆盖这些误差。对n=C+S，A的梯度为

\[
\partial_C A=\frac{(1+\eta)S}{\sqrt\eta n^2},\quad
\partial_S A=-\frac{(1+\eta)C}{\sqrt\eta n^2},\quad
\partial_\eta A=\frac{\eta C+S}{2\eta^{3/2}n}.
\]

完整P=A/Q传播用`gPᵀΣ(C,S,eta,Q)gP`。若只为诊断把quoted C/S errors当独立，432行σA≈.00980；eta error另给敏感性.00611；换sqrt(area)仅得.00508。这些不是作者full error budget的重建，不能擅自把两项quadrature称新实验error。C/S拟合与eta/Q校准可有共同Cov；Q从Acal/Pcal得，Acal–Q的依赖尤其不能忽略。

对无背景、固定n、knowneta的**声明二项模型**，`pC=(1+sqrteta A)/(1+eta)`，exactconditional

\[
\mathrm{Var}(A\mid n)=\frac{1+(\eta-1)A/\sqrt\eta-A^2}{n}.
\]

nearA0才回到1/n及F形式；sourceEq17是独立Poisson层的相应误差式，不是对任意净peakareas与systematics的保证。这个推导不生成新counts或替换源fiterrors。

### 原表closure与高背景反证

实际七行Table3重算中，六行按C/S整数、eta/A最后位舍入盒相容；294-keV的eta.061/C16622/S1226给A=−.0481061，而印−.045，当前printingbox未闭合。要强求印刷中央值需eta≈.0617505，这个target反推值不被当独立标定，更没有修改输入。缺unrounded producer、原逐detectoraggregation/threshold/peakledger；原因未决，未宣称原文错误或重新拟合P。 反推eta仍落在reported .061±.001的测量边界内，A差也远小于quoted .019；这是printcentral复现边界，不是实验数据矛盾或新的校准结果。

源作者本身指出inband P的离散和部分>约36%的幅值受高背景peakfitting限制，并用AD的相近形状反查。约36%属于其purehighspin-dipole/maximumalignment比较，不是任何conditionalgamma的通用上限；不能把超界中央值夹到.36，也不能拿这些P精度去做无Cov的δ强拟合。其符号pattern对E1link/负宇称的支持保留为作者有条件解释。

两种calibration反应、同197Pb数据的不同处理、alternate44pagepreprint/16page期刊版都不自动增加独立实验。实际197Pb为12台80–100度、60keV side threshold、约270/271-keV bandgate；精确energy/gate选择应回原谱，不能仅凭近似label匹配其它measurement。

复算[day16_sg98_polarimetry_preview.py](../../system/scripts/day16_sg98_polarimetry_preview.py)的冻结input/actualtableaudit保存七行、原errors、梯度与printingfailures；这是本日恰好Day17无学分知识preview，不重记formal17。下一高信息输入是matchingeta/Q与background/fitCov和event/cut ledger，而非任意加counts或Q插值调参。


## EXOGAM已知E2校准：比值误差与回代依赖

[[zheng-2013-linear-polarization-91ru]] Z13-7/9/10/11的原Eq.(4)与Table I给Q=A/P。必须把“中央值可以复算”和“同一误差预算可复现”分开：11项中央值在printing rounding下相容；若括号σ是同一比值的marginal标准差，一阶局部传播须满足

\[
\left|\frac{\sigma_A}{P}-\frac{A\sigma_P}{P^2}\right|
\le\sigma_Q\le
\frac{\sigma_A}{P}+\frac{A\sigma_P}{P^2}.
\]

这是Cov正半定/Cauchy–Schwarz的必要界，不是独立误差假设。原316-keV项A=.17(.02)、P=.513(.002)、Q=.331(.008)的名义下界约.03769，已高于.008；即宽松允许所有中央值/误差末位各半位，保守下界.02755仍高于.0085。586、974、1054也保留这种条件不闭合；823的名义不闭合不能通过宽松rounding检查，故不将其列为稳健排除。原σ定义/producer缺失，不据此宣布原实验错误或重估P/δ。

以printed11个Q为独立输入的声明拟合是p0=.38616115、p1=7.39668×10^-5/keV、χ²=9.98029；作者.39(.02)、.00006(.00003)及Fig.5标签11不改。这些数并非原协方差/拟合配方的认证。Q_i本就来自A_i/P_i，以相同A_i/Qfit(E_i)回到P_i只检查样本内残差；应保留Cov(A_i,Qfit)与跨点calibration Cov。更多反应道或更多回代处理不自动增加独立标定。

复核原件和[冻结input/计算](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/z13-calibration-audit.json)的目的是定位缺哪一层误差。应取得matching Compton净计数/门/背景、a与Q拟合Cov、A2/A4联合Cov/未舍入参数后才作实验error-budget或δ联合拟合；当前仍是Day16下的partial17知识预习，无正式17学分。


### FOM比较要与同能量同response的Q配对

[[zheng-2013-linear-polarization-91ru]] Z13-13的1368-keV文字点给F比4.4、Q=.135(.005)对.121(.005)。在同对象F=Q²epsilon_c假设下，Q²比仅1.244792，条件epsilon比3.534727；这不是独立效率测量，更不等于物理偏振P提高。该能量超出Table I列到1264-keV的校准点，印刷curve外推给.160078而文字另报.135；缺selection/parameter及cross-Cov，保留中央差，不用外推替换原比较点或判实验冲突。原F未给误差，不从同数据反推epsilon再当独立companion证明F。


## GRETINA：半因子、reference角色与真实cut tradeoff

[[morse-2022-gretina-polarization-sensitivity]] M22-4/5/6/8/9/11与[[longfellow-2026-gretina-energy-ordering-polarization]] L26-23/24给实际calibration链。两篇都用A0=Q Pbar/2；同P/同响应下改成A0=Qnew Pbar须同时Qnew=Q/2，不能固定Q删半因子。若声明uniform reference、无background、knownQ的连续p(ξ|P)=[1−κQP cos2ξ]/(2π)，则P=0的Fisher information/yield为κ²Q²epsilon/2。因此同observable可在Q²epsilon数值改变四倍时保持同一information；跨instrument比较还需epsilon/estimator合同。这是条件统计推导，不是原实验beamtime测量。

Morse的6-quad tracking与L26的12-quad energy-order/noaddback不同；L26 Eq19曲线来自同一tuning后的模拟GRETA500–2000四点，不是本run实测多能Q。作者说调到σ100≈7mm可匹配A0，却使sim apparentP90降至约.85、实验约1，并明确7mm不是实测分辨率。这个必要companion不闭合应与曲线一起保存，不用一个matched A0认证整套response。

原cut表真实中央值：Ft≤.1使Q提高到.314，但F只余baseline的.25、F/Q² impliedepsilon仅余.0974。ψ60–80°的相应比例.3922/.2113。没有Q–F Cov，不再造epsilon error；更高Q是否有利必须连同选择损失和目标likelihood检查。

[[lauritsen-2025-gamma-angular-formalism-tracking-arrays]] L25-30的Q=.33(.04)来自1173 coincidence polarizing 60Co1333，measured/ideal amplitudes .016/.048。未加γγ条件的source singles可为unpolarized reference；同源γ在coincidence条件下却能polarize，不能只按能量或核素名当同一reference。其Q也不能未经gates/角响应/归一转换直接替代Morse .196。

详细matched transition/plane/phase/数据独立性账见[[gretina-25na1041-polarization-response-contract]]。源A2=0可用未相除系数连续计算P，actual intensity=0则P undefined；两种0/0边界须分开。两点energy-ordering的Compton plane换序不变不代表reaction plane/Doppler方向不变，≥3hit与其它拓扑也需实际response。


### 角覆盖平均、event平均与Q重标必须一致

[[longfellow-2026-gretina-energy-ordering-polarization]] L26-27–29实际公开Fig4的218点coverage与2908点P曲线重放，按图示CθP/Cθ给约.377923/.543870，正文写about.35/.53；原approx不是精确误差声明，未取得实际kernel/未舍入producer，因此只记录重放未闭合。Cθ若是counts per θ-bin就用dθ；改用cosθ要1/sinθ Jacobian，不能再随意乘sin。图形提取不等于rawresponse。

在声明factorized kernel下，event-weighted平均为∫CθWlabP/∫CθWlab，与sourcecoverage平均∫CθP/∫Cθ不同。更一般harmonic涉及〈Sigma P〉，不自动等于〈Sigma〉〈P〉；缺joint θ/ψ/point/ξ kernel时，分别平均不能恢复其相关。统计fitCov与这种响应measure中的相关是不同对象。

经验Q本来由A/(κPbar)校准，换平均定义须同时换Q。若true A=κq Pbar_event，则Q_C=q Pbar_event/Pbar_C；校准核与目标核只有相同weighting-ratio才会在transfer时抵消。把target换成更合A的平均却固定旧Q不是独立response修正。

真实cut .044/.028的gain1.5714在声明knownresponse/uniformξ/无背景且固定角形状的共同偏振幅度模型中需retained fraction>.40496才提高counting information。sourceC图积分约.19669不是实际Compton-selected count retention，不能拿图形就判原cut优劣或给束流时间。此例的完整identity/readiness保留在[[gretina-25na1041-polarization-response-contract]]，不将22Ne的C迁给25Na1041。

### 数据库POL字段要回到原文A0/P定义

[[nndc-2025-a25-mixing-reference-records]] N25-4/5/10实际核了2026Lo01的Na/Mg XUNDL。Na1041的POL=.043(.008)转录L26的A0；该实验定义A0=Q Pbar/2，所以不能直接把POL放进physical-P栏。XUNDL的编译、原paper表与多种处理仍是同一采集，不是三次独立偏振证据。

target/gamma identity还要保留版本：25Na1041在当前Adopted为3459.4→2418.3，XUNDL用3459→2419；Mg XUNDL原G3971不能静默改成Adopted3970.3。官方PDF的靶厚度µg与primary mg相差1000，也限制从转录对象直接构建response。可复用的身份与MR谱系写在[[gretina-25na1041-polarization-response-contract]]；尚未取得actualresponse、jointCov或新的独立选根证据。

### 统计张量到Stokes：纯标定通过不认证任意mixed路径

[[ucgretina-2021-polarized-emission-code]] UC21-1–9固定公开代码并实际抽取编译。POL编译门、nuclear angular correlation与polarized EM开关分开；Reaction的P(m)→rho保留全部rank，ITDecay在衰变更新前取parent tensor。仅计算出W或启用alignment，不证明光子Stokes与Compton分析已一致启用。

原Stokes表达式中Cplus/Cminus×F在禁戒CG处可字面0/0；本run的mixed k0和pureM1 k4失败控制显示：norm有限正而P1/P2为NaN。独立helicitytrace给物理有限值；同1→1 pureM1与mixedlabel δ0的norm相同、代码却一过一失败。应保持原失败，解析约去公共CG后再作另名验证；不能遇NaN置0、截断rho或把calibrator pureE2通过当作任意mixed producer认证。

Morse spin2→0 pureE2控制确实通过，这限制对其原标定的归因；当前只有内核/明示helpers，未取得其exactbinary、geometry、macro、后处理或actualresponse/Cov。若同一selection经reference校正后的ξ acceptance均匀且只留cos2项，源码KN核对无偏振电子给A0=〈Sigma P〉（该声明jointkernel下），若另用Morse的A0=Q Pbar/2，则Q=2〈Sigma P〉/Pbar；只有附加factorization才可写2〈Sigma〉。Stokes的2φ轴旋转、经验Q半因子与finiteangularattenuation是三种不同的因子。

### 非轴对称输入需核同一tensor的两个收缩核

[[ucgretina-2021-polarized-emission-code]] UC21-10–13保存实际对照。Cplus/Cminus×F的公共CG应解析消去，不能浮点0/0后置0；有限H只解决这层数值表达，不自动修复所有Stokes。源码角采样使用P_k^κ的dκ0合同，Stokes归一使用d0κ，二者对奇κ差(−1)^κ；相同PSD tensor的角采样I与独立trace匹配，但Stokes归一核不匹配。轴对称κ0 benchmark看不见这一条件。

另外，原literal pureM1 1→0且只含偶κ的coherent态，I/Q/V过而U反号，CG比全有限，隔离了另一个linear-analyser相位问题。eθ/eφ轴、Jones U=2ReJθφ和Compton消费端−U sin2Φ必须一起核，不能仅把拟合cos2振幅正负当完整Stokes验证。声明511keV/90°散射的K45/K135对照是点模型，不是阵列计数或Q标定。真实I=0时保留P undefined；单个helper极限猜测未观察则如实撤回。

### 有限fullq设计与数据响应仍是两层

[[ucgretina-2021-polarized-emission-code]] UC21-14–16把Jones代数、fullq d_(q,m)收缩与有限H放在同一合同中，另名计算IQUV；Q+iU=−2tau_plusminus*的conjugation决定虚部符号。18个声明case/540点（12个新PSD矩阵事前冻结）与独立photontrace闭合，Rz/纯极限/nonPSD/truezeroI控制也过。这个数学证据没有把原public代码修成已验证producer，也没有补actualgeometry、interactionorder、后处理、background与共享Cov。

使用时先保存density/EM/nativeδ/轴与Stokes定义，再将光子密度矩阵通过matching response作用到实际事件/参考归一。单emitter正性只保证该模型的光子域；Q、计数FOM、实验branch CI及gatedreference仍须各自真实输入。新的数值零门不是能量阈值，absδ很大也仍是含小干涉的有限值。

### 源能谱实际运行后的三层检查

[[riley-2021-ucgretina-energy-response]] R21-7/13/14给能谱响应本身的必要反证：同一NSCL十二quad数据按能区取不同有效层参数，.4/.9mm outer分别改善不同低能方面，近photopeak的partial charge collection仍未建模。作者明确今后polarimetry/tracking还需现实segmentation与partial collection；能谱吻合给出的是该source/选区下的约束，Q还须匹配的偏振observable。

本run七quad源MC默认coax/back/outer=1.5/2.5/.9mm虽与其Table2 II相同，阵列、SDK、周边材料与源/门身份仍各自核查。R21 continuum的1172/1173target＋LaBr1332gate，与L25的1333target/1173gate角色相反；Compton continuum不是偏振角分布本身，不能从一个common source名迁Q。约210keV背散射检查只验证机制尺度。

[[ucgretina-2024-geant4-11-source-replay]] UG24-3–11实际构建G411/11.4.2无POL源程序，保留all-empty decay truth和仅process-name兼容后的空槽失败；另名source-only记录副本的有效core/IP在同种子1000history下逐位不变，beta/boost未认证。程序exit0不足以确认truth，整个binary文件SHA不同也不足以判定物理记录改变。

实际geometry companion进一步区分宏语句与有效volume：原decay的preinitialize源框命令下Eu152从Target出发；仅移到initialize后，primary从euTape出发并有有效POLYETHYLENE。新几何recipe的探测记录可以改变，不能和仅记录层改动混作同一不变性要求。源能谱/finite-MC合同见[[gretina-eu152-source-response-replay]]；全阵列几何warning、历史模板与matching Compton Q仍缺。

### 公开源能谱能约束什么：Eu152实际数据的readiness门

[[ucgretina-2012-eu152-public-calibration-data]] UE12-1–11取得NSCL2012七quad的run20源/run7背景ROOT。实际egam1keV/bin，source/background entries约1125万/173万；按宏1800–3000而非README1540门计算，a=13836/30293=.45673918，与printedp0接近，声明finitePoisson背景时σa=.00468656。该数只支持对应window的归一算术，没有MC模板/拟合Cov便不称fullresponse复现。

两个grossROI经同a扣背景会共享Cov：n_i=y_i−a b_i，条件Var≈y_i+a²b_i+b_i²Var(a)，非对角≈b_i b_j Var(a)。实际预选121/1408附近grossROI给crossCov≈1387.57counts²；它既非净Gaussian峰面积，也非已测eventCov。Sumw2N0/defaultsqrtN不证明独立事件；同数据更多hist/拟合不增加独立校准。

公开InBeam例的ξ还有truthIsFEP/同crystal/two-IP选择；isolated selector无序反例必须连同上游GRUT BuildFrom的decompE降序排序反证，不能直接归因原实验。相等最大值和binary版本仍需actualinput核查。两校准ROOT只有energy/labθφhist而无TTree/Comptonξ，不足以识别P或Q；这份七quad数据也不能裸迁到Morse六quad或L26十二quad。unpolarized geometricalreference、polarizedQcalibrator与γγ-gated reference的统计对象要随事件分母保存。


### 60Co校准要保存目标、门和选择定义

UG24-30–34另给可核的相同极限：unpolarized4→2→0 pureE2、point reference不分析其helicity时，first/last P在90°均1/6；同一个P不等于相同能量的KN分析能力或实际arrayQ。小M3/finitegate/response可改变结果，须带条件而非只靠角色名字判断。

同pure模型把各reference平面的正局部P直接平均会得19/189，正确在共同目标轴积分无gate的reference方向却恢复无偏振。Q_J+iU_J的spin2轴旋转需先进入平均；Q_J为光子密度分量，polarimeterQ(E)另定义。这个反证说明scalar Pbar必须依附原分析plane/weight合同，不能任意混合局部轴。

[[co60-gate-role-response-benchmark]]将R21的1173target＋LaBr1332gate、L25的1333target＋1173gate和公开两GRETINA-crystal pair例分别保存。原生nuclear angular correlation可在photon polarized EM关闭时运行；这约束方向分布，不认证target的polarized response。矩阵数值一致也不认证实际post-processing或Q。

UG24-21/27的实际记录控制显示，缺失γ占位和跨晶体prefix back标记会改变相应输入对象。逐晶体back、整event back和prefix不是同一个选择；没有原producer时，不据公开hist名字替原校准分母。

### 60Co参考输入的共同误差分量

[[nndc-2013-ni60-co60-reference-records]] N60-3/5/9/11：1173 MR−.0025(22)的σ=.0022、两评价对象同源；S CC为理论更新而旧comment另含实测评价。pointgate模型在明确phase假设下给Covδ=Jσδ²Jᵀ；角色差的σ≈.0008204，误当独立会得.0023719。此项共享误差并非完整reference/arrayQ calibrationCov，不能用小central差重测δ。真实response还须同target/reference/选择/角/归一匹配，原1980phase正文未取。[[co60-gate-role-response-benchmark]]保留实际branch抽样与同输入MC的内部核验，不能把pair相容性变成实验Q验证。
