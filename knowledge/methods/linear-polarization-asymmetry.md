---
type: method
title: 线偏振不对称分析
aliases: [linear polarization asymmetry, polarization asymmetry, Delta asym]
created: 2026-07-01
updated: 2026-10-17
status: active
review_status: unreviewed
method_type: gamma-ray-polarimetry
tags: [multipolarity, electric-magnetic-character]
---

# 线偏振不对称分析（Linear Polarization Asymmetry）

## Purpose

利用分段 HPGe/Clover 的 Compton 散射方位分布判断跃迁的电或磁性质。

## Inputs and Assumptions

探测器偏振灵敏度、非对称校正、符合门和足够统计；还需spin/geometry、核取向或其约束、门/背景与未分峰component条件。

## Procedure

比较垂直/平行于反应平面的散射计数并构造不对称量。

## What It Can Establish

为电/磁性质提供不同于DCO的互补约束；两者共享事件、门或标定时，不能自动视为统计独立或两条独立实验。

## What It Cannot Establish Alone

弱跃迁的不确定度可能过大，不能可靠提取小 E2 admixture。

未分峰的共同asymmetry不能自动分配成逐线性质；若无相应取向、geometry和spin条件，符号本身也不能独自给出electric/magnetic或绝对Jπ。

## Conventions and Systematics

不对称量符号依实验定义，必须引用原文校准。

[[bark-2024-investigations-nuclear-chirality-ithembalabs]] 的 Eq.(5) 把 `A_p` 分子与分母都印成同一个 minus-form expression，代数上会恒等于 1，并与紧随其后的 `A_p=Q(Eγ)P(θ)` 不相容。该公式作为 source error 隔离，不据此修改本页定义；AFRODITE-specific sign/efficiency convention 应回到原始 calibration source。

不要把所有“asymmetry”默认理解为同一种 in-beam clover Compton polarimetry。[[rusev-2009-multipole-mixing-ratios-11b]] 测量的是 linearly polarized photon beam 激发后，发射 gamma rays 在水平/垂直平面的 azimuthal asymmetry；它与 clover Compton scattering asymmetry 共享“偏振相关”这一物理思想，但实验量和系统项不同。

[[lauritsen-2025-gamma-angular-formalism-tracking-arrays]] treats tracking-array linear polarization as a continuous-angle response-function problem. For in-beam single-gamma polarization, its Eq.35 expands the angular-distribution expression with a `P_pm cos(2 zeta)` term and includes mixed transitions. Its `152Dy` 432-keV example shows why angular distribution, DCO and linear polarization may all be needed to resolve `M1/E2` versus `E1/M2` ambiguity.

[[zheng-2013-linear-polarization-91ru]] provides a clover implementation boundary: EXOGAM `90°` clovers use adjacent-crystal Compton scatters, an unpolarized `152Eu` normalization `a(Eγ)`, and known pure E2 transitions to fit `Q(Eγ)`. The experiment uses `A=QP` together with `R_DCO`; the sign and magnitude separate stretched electric/magnetic and nonstretched cases under the stated geometry. Its `91Ru` assignments remain conditional on the assumed `(9/2+)` ground state, so a clean asymmetry does not remove level-scheme assumptions by itself.

[[garciaraffi-1997-monte-carlo-compton-polarimeters]] shows why `Q` calibration is not a universal constant: geometry, thresholds, scatter-angle windows and polarization transport through multiple scatters must be reproduced before a simulated or measured asymmetry is converted to physical `P`.

[[twin-1970-polarization-angular-correlation-40k]] is an early joint-analysis example: Compton polarization provides parity/multipole sensitivity only after `a2/a4` angular distributions constrain spin and population; polarization alone can admit several spin/parity fits.

[[wadsworth-1977-61ni-levels]] extends the same Rose–Brink/three-GeLi method to a `61Ni` level scheme and demonstrates that polarization, angular distributions and DSAM must be kept as separate evidence layers.

[[falkoff-1948-polarization-correlation]] supplies an early successive-γ polarization-correlation sign formalism; it is not the same detector-level asymmetry as modern segmented-clover analyses.

[[starosta-1999-pdco-experimental-test]] demonstrates the PDCO joint observable in EUROGAM-II: the CLOVER asymmetry is converted with `Q(E)` and combined with a geometry-dependent `R_DCO`. The study explicitly retains an E2 versus mixed M1/E2 branch for the 490-keV transition, showing why polarization plus DCO is narrowing evidence rather than an automatic unique assignment.

[[jones-1995-clover-compton-calibration]] defines the detector-level separation used in later CLOVER work: angular-distribution fitting supplies `P`, adjacent-crystal counts supply `A`, and the calibration is `Q=A/P`. Its 197–1368 keV response and 60-keV threshold should not be copied to another array without recalibration.

## Formalism Boundary

The three new method sources make the detector-layer separation explicit: Jones 2002 defines physical polarization `P`, experimental count asymmetry `A` and detector sensitivity `Q`; Go 2024 extracts a polarization from normalized measured/simulated azimuthal distributions; Longfellow 2026 uses `A0=1/2 Q Pbar` after integrating GRETINA coverage. These are related observables, not interchangeable names for the same quantity.

The special `|P|=1` cases in Jones 2002 require particular alignment and pure transitions. Longfellow's Appendix further shows that the sign of `A0` alone cannot generally identify electric or magnetic character for mixed transitions. Use [[gamma-ray-linear-polarization]], [[experimental-asymmetry]] and [[polarization-sensitivity]] for the separate evidence layers.

### 135Pr的A与P跨表闭合

[[135pr-mixing-branch-input-contract]]按M15-16、[[lv-2022-evidence-against-wobbling-135pr]] L22-16/17与HE15-10核对：Matta TableI是INGA不对称度A，Lv主文是P而SI Table1另列Ap。同一次Lv数据满足P=Ap/Q；采用的Q来自Herzan2015，但a(E)使用Lv自己的calibration，不一并复制Herzan的a。独立原件的Q中央系数使三线Ap→P及误差尺度在印刷精度内闭合；这是身份核验，不新增独立偏振实验或完整error-budget认证。

同页的G Sigma_cal G^T给共享截距/斜率的条件敏感性；原calibration Cov与P–Rac overlap未知，不能把该chosen模型当实验Σ。源P区间跨零不禁止联合分析，也不支持仅按符号选择大模delta。无INGA自己的Q/response时，不把其A=.047/.054直接同JUROGAM的P=.04/−.03作数值冲突检验。

## Examples

`131Xe` 论文明确指出弱连接跃迁的偏振误差较大，因此主要依赖角关联/角分布约束 δ。

[[matta-2015-transverse-wobbling-135pr]] 用 INGA clover 得到 747.0、812.8 keV transitions 的正 asymmetry，并以 593.9 keV signature-partner link 的负 asymmetry 作 M1 对照。只有统计足够的 transitions 才报告可靠结果。

[[guo-2022-low-spin-wobbling-187au]] 用 clover 相邻晶体中垂直/平行方向的 Compton scattering，与 `R_ac` 联合约束 376/462 keV links。该文同时强调：偏振通常只利用相邻晶体，统计误差可能很大；选 mixing-ratio branch 时必须使用偏振幅度与可信不确定度，不能只看正负号。

[[rusev-2009-multipole-mixing-ratios-11b]] 则给出另一种边界：即使 measured asymmetry 很干净，predicted asymmetry versus `delta` 仍可能给出两支解。该文对 `11B` 选择较小 `|delta|` branch，是因为大 `|delta|` branch 会对应异常大的 `E2` admixture，而不是因为 asymmetry 本身已经唯一选解。

[[liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br]] 用两个 90° AFRODITE clovers 作 Compton polarimeters，并与 [[angular-distribution]] 中的 ADO ratio 联合约束 `78Br` linking transitions；其 Fig.3 采用正值为 electric、负值为 magnetic 的本文约定。

## Sources

- [[herzan-2015-193bi-spectroscopy]] HE15-9/10：共同393/394观测与clover实际a(E)/Q(E)；[[nndc-2017-193bi-level-scheme-evaluation]] N193-5保留Q及(E2)/negativePOL矛盾。
- [[rose-brink-1967-phase-defined-angular-distributions]] RB67-2/11：population与photon helicity的相干差/和；下方模型是任务重构，不是作者实验。

## 未分峰偏振的联合命题与选择条件

[[herzan-2015-193bi-spectroscopy]] HE15-9的393.4/394.0-keV doublet报告共同Rexp=1.26(16)、A=−0.076(11)。它不是两条independent polarization measurements。N193-5只保留multipolarity字段Q（quadrupole），不能把此Q与detector sensitivity `Q_sens(Eγ)`混成一个量。

若两component使用相同a，真计数已去除背景且非负，令`z_j=aN⊥,j+N∥,j`，则`A_shared=Σz_j A_j/Σz_j`。这是count-level convex mixture；共享事件不破坏均值恒等式，统计Σ仍须另算。共同negative A能限制“两条在该选择下都A_j≥0”的joint命题，却不能指定哪一条为负。自设pair(−.20,+.10)或(+.10,−.20)，配合不同正权重都可给−.076；这些权重不是原表的Iγ，也不是新fit。

HE15-10的a(E)在0.6keV跨度的差仅3.24×10⁻5；若common energy取该区间内，对两个本来非负的component，最多引入约−1.484×10⁻5的合成floor，远小于−.076。用原a(393.7)=1.0917402和报告A反推条件raw N⊥/N∥≈.786575，若仅靠重标a把mean推至0，需要a≈1.271334（增加16.45%）。这是固定count ratio下的校准敏感性，不是指控真实calibration错误，未把原.011当完整Gaussian误差或重新报告source significance。

### 纯E2的取向反例与joint R/A必要域

RB67-11/2在printed p.316 / PDF11把线偏振强度写成helicity λ=±1 amplitudes的coherent difference/sum，并以substate population加权；本轮原图/hash再核。这里`mγ=Mi−Mf∈[−2,2]`是多极场的magnetic projection，不能与helicity λ混用。

本任务用pureE2 transverse field `∇ΩY_(2,mγ)`与独立Wigner-rotation/helicity路线复核W和N（linear numerator），所有kernel一致；对任一mγ，W的angular average为1，isotropic初态给W=1、N=0。点角157.6°/75.5°、共同conditional selection、轴对称diagonal population、同一positive Q_sens、无背景与有限接受度的极限中，各非负mγ权重给一个pureE2 **outer set**；不是每个vertex都可由指定J的核布居实现。

Gaussian σ/J=.3的自设15/2→11/2、19/2→15/2 pureE2分别给(R,A)≈(1.4402,+.1325)、(1.4177,+.1260)；自设aligned |Mi|=Ji同样pureE2却给R≈.2704、A≈−.2280。这说明A sign依赖population。后者虽然negative，但不能同时解释原R≈1.26。

在这个松弛的pureE2 outer set中，固定R=1.26时A范围为+.03325到+.09507。一条可直接复核的necessary inequality为`A≥0.264123 R−0.299545`；所有six vertices满足它，报告mean的margin为−.10925。中心值和逐坐标2×printed-error sensitivity box在集合之外；3×box有可行点。这些boxes不是joint confidence regions；未知R/A/标定Σ、finite acceptance与实际gating都未重放，不能将其写成实验排除概率。

若允许不同effective selection/population，单独R和单独A都能由合法核CG权重匹配；它们却不再是一套共同forward model。magnetic quadrupole模型可通过EM duality反转N而保留W，在松弛核CG模型中包含该joint mean；它需要opposite endpoint parities，不能原封不动保留原same-parity暂定纲图，也不提供某条线的M2赋值。Higher multipoles、背景/门/geometry失效和parity-anchor变化均应继续保留，不强行选解释。

![共同R/A的声明模型必要域](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/shared-E2-response-region.svg)

图中source shared estimate与chosen模型点分开；灰红误差框只是敏感性范围。可复算[day14_shared_polarization_limits.py](../../system/scripts/day14_shared_polarization_limits.py)与[结果回执](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/shared-polarization-limits.json)，70项数学/独立kernel/LP/CG检查通过。核模型假设、公式、结果与失败条件在本knowledge页，outputs不是唯一事实副本。

### 必要伴随观测与判断边界

- 先核DCO/POL是否使用相同transition identity、gate/事件选择与兼容的effective population；仅仅“同一acquisition”不够。
- 在实际angular acceptance和clover threshold/geometry上重放response，使用matched-gate known-transition controls、a/Q完整Σ与相关背景；one-angle ratio不能代替full response。
- 逐component偏振/转换和spin/parity锚点才可能定位究竟哪条性质/π需要重审；Gamma Iγ不是polarimetric z_j权重，τ/δ也不由共同A生成。

Self-audit：`supports`shared observable对joint假设的条件约束；`limits`按符号给每条M2、忽略取向或把point model当experiment。N193-5的Q与原review flags保留；没有新的human-review或193Bi/A≈130模式排名。

- [[chakraborty-2023-131xe-wobbling-origin]]
- [[matta-2015-transverse-wobbling-135pr]]
- [[guo-2022-low-spin-wobbling-187au]]
- [[rusev-2009-multipole-mixing-ratios-11b]]
- [[simpson-1983-sectored-geli-compton-polarimeter]]
- [[garciaraffi-1995-nonorthogonal-compton-polarimeter]]
- [[taras-1971-phase-defined-polarization-formulas]]
- [[butler-1973-three-geli-compton-polarimeter]]
- [[lauritsen-2025-gamma-angular-formalism-tracking-arrays]]
- [[liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br]]
- [[zheng-2013-linear-polarization-91ru]]
- [[bark-2024-investigations-nuclear-chirality-ithembalabs]]
- [[garciaraffi-1997-monte-carlo-compton-polarimeters]]

## Evolution Log

- 2026-07-01：记录与 DCO 的互补及统计限制。
- 2026-07-03：加入 `135Pr` electric/M1 同核素偏振对照。
- 2026-07-04：加入 Guo 2022 的联合 `P-R_ac` 选解与偏振误差低估风险。
- 2026-07-12：加入 Rusev 2009 的 polarized-photon asymmetry 技术与双解边界。
- 2026-07-13：加入 Liu 2016 AFRODITE ADO+polarization linking-transition 案例。
- 2026-08-11：记录 Bark 2024 Eq.(5) 的 algebraic source error；禁止传播为 polarimeter formula。
