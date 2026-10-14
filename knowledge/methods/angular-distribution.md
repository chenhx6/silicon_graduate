---
type: method
title: γ 射线角分布分析
aliases: [angular distribution, gamma-ray angular distribution, gamma angular distribution, in-beam angular distribution, ADO]
created: 2026-07-08
updated: 2026-10-15
status: ai-draft
review_status: unreviewed
method_type: gamma-ray-angular-distribution
tags: [multipolarity, mixing-ratio, alignment, pado-support]
---

# γ 射线角分布分析（Gamma-Ray Angular Distribution）

## Purpose

角分布分析利用不同探测角度的 γ 射线强度来约束 transition multipolarity、mixing ratio 和 emitting level orientation/alignment。

## Inputs and Assumptions

- 探测器角度与效率归一化；
- transition spin sequence、multipolarity 和可能的 mixing ratio；
- emitting level 的 magnetic-substate population 或等效 attenuation/alignment 描述；
- feeding path、side feeding、寿命和 Doppler broadening 等系统项。

## Source-Level Foundation

[[draper-1970-gaussian-substate-side-feeding]] 对 stretched E2 transitions 给出 `A2/A4` 与 Gaussian side-feeding substate population 的 exact treatment。[[zobel-1980-magnetic-substate-distributions]] 明确指出若 alignment 已知，角分布可用于 multipolarity and mixing-ratio determination；但只有两个 angular-distribution coefficients 时，同时确定 `α2`、`α4` 和 `δ` 会有歧义。

### Ionescu 1981: `167Tm` feeding-aware angular-distribution test

Ionescu et al. measured pure-E2 angular distributions in `165Ho(α,2n)167Tm`. Their pure-E2 test found that one global Gaussian magnetic-substate distribution failed for the studied `167Tm` data. The proposed fit keeps Gaussian side feeding but adds discrete direct-feeding components, `D_T(m)=D_s(m)+Σ_jD_j(m)`; pure-E2 transitions constrain the population model before mixed `M1+E2` transitions are fitted for `δ` (IO81-4/5/6/8/9). This is a reaction-specific counterexample and analysis workflow, not direct evidence about Ding's `127/128I` spectrum and not a universal rejection of Gaussian models.

## Relation to Other Methods

Angular distribution 可与 [[multipole-mixing-ratio]]、[[dco-ratio]] 和线偏振共同约束 `δ`。不同实验几何、beam energy、projectile 或 target condition 下得到的角分布参数不能无条件混用。

ADO（angular distribution from oriented states）ratio 是有限角组实现：在相同 gate 下比较不同探测器角组的归一化强度，并用本实验已知 multipolarities 标定 dipole/quadrupole 区域。[[liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br]] 的 AFRODITE 几何给出 stretched quadrupole 约 1.1、pure stretched dipole 约 0.7；这些阈值不得跨阵列复用。

[[zheng-2002-ado-coincidence-angular-anisotropy]] 给出符合模式下 ADO 的显式效率修正：`R_ADO(γ1)=[I^S/I^L]/[ε_S(γ1)/ε_L(γ1)]`，并将其写为待测 γ 的角分布比乘以门控 γ 和探测器响应共同决定的 `f_ADO`。在 `145Tb` 的 12 套 BGO-HPGe、约 `±32°/±58°/90°` 三角度组中，门控能量 `100–1500 keV` 的 `f_ADO` 最大偏差约为四极门 `5.2%`、偶极门 `3.2%`；该来源报告的纯四极约 `R_ADO=1.25`、纯偶极约 `0.75` 只能作为本阵列的局部标定，不能替代新阵列的参考线验证。

## Tracking-Array Formalism

[[lauritsen-2025-gamma-angular-formalism-tracking-arrays]] gives a modern tracking-array notation for in-beam angular distributions: `omega(theta)=A0+alpha2 A2 P2(cos theta)+alpha4 A4 P4(cos theta)+...`. In that local formula, `Amax_k` contains the spin sequence, multipolarities and mixing ratio `delta`, while `alpha_k(J)` is the nuclear alignment/deorientation attenuation calculated from magnetic-substate population `Pm(J)`. The same source usually parameterizes `Pm(J)` as a Gaussian with normalized width `sigma/J`.

This `alpha_k` must not be merged with detector solid-angle attenuation. Lauritsen 2025 uses detector attenuation in the source-correlation formalism and nuclear alignment attenuation in the in-beam angular-distribution formalism; the local definition controls the meaning.

## What It Can Establish

在 alignment 或 population model 足够受控时，角分布可约束 transition multipolarity、mixing ratio 和 attenuation/alignment 参数。

[[rose-brink-1967-phase-defined-angular-distributions]] 给出 phase-consistent 基础：一般分布使用布居/取向张量 `B_K`、几何/多极系数 `R_K` 和约化 interaction-multipole matrix elements。轴对称条件使表达式成为 Legendre 展开；初末态宇称确定且不测 γ 偏振、对 helicity 求和时，只含偶 `K`，即使初态有 polarization 也成立。另一项充分条件是 `w(−M)=w(M)`，它使奇 `B_K` 消失；不能仅凭“初态 polarized”就声称出现奇 `K`（RB67-4，printed p.320 / PDF p.15，Eq.3.40/3.41）。

[[der-mateosian-sunyar-1974-angular-coefficients]] supplies practical `A_2/A_4` tables through `J=26` (integer) and `51/2` (half-integer). The worked example solves `σ/J` and δ jointly, and explicitly warns that angular-distribution and γγ-correlation δ signs may differ under their respective conventions.

[[yamazaki-1967-aligned-angular-coefficients]] is the earlier coefficient-table backbone: it defines complete-alignment `B_k`, `F_k` and cascade `U_k` tensors for integral and half-integral spins, then applies Gaussian magnetic-substate attenuation. Its explicit angular-distribution/γγ-correlation δ-sign warning is retained as a convention boundary, not merged into a detector calibration.

## What It Cannot Establish Alone

仅凭两个角分布系数通常不能同时唯一确定 `α2`、`α4` 与 `δ`；弱峰、短寿命、Doppler broadening 和 feeding ambiguity 会增加多解风险。

## Practice-Level Boundary

[[chiara-2012-cu65-cu67-core-coupled-protons]] adds a practical spectroscopy example: the angular-distribution calculation for `65Cu` used an assumed `sigma/I = 0.5` because it reproduced known transitions, and the fitted `delta` of one `1115 keV` line changed when the assumed alignment width changed.

[[summary-2013-bases-spin-parity-assignments]] adds reference-guide background that high-spin assignment heuristics are often quoted with a typical orientation parameter, here `σ/I = 0.3`, but that guide-level value is not by itself a demonstrated universal Gaussian prior.

Angular-distribution evidence is one of the standard inputs collected on [[spin-parity-assignment]] pages.

Liu 2016 将 ADO 与 linear polarization 联合用于 `78Br` linking transitions，并由 404.3 keV line 的 `R_ADO=0.79` 与负 polarization 支持 `M1/E2` 及相对 spin revision。

## ADO计算单：额外输入、self-exclusion与误差

以下是 Day14 运行中恰好下一张 Day15 的无学分预习。原文定义来自 [[zheng-2002-ado-coincidence-angular-anisotropy]] Z02-1/6/7/8；数值、效率、布居和 covariance 均为本任务自设练习，不是 `145Tb` 或 `193Bi` 的实验重分析。

### 原式的方向与组效率

令 `γ1` 为待测线、`γ2` 为门控线，`S/M/L` 为三个角组。Zheng PDF p.2 式1/3/4/5给

\[
R_{\mathrm{ADO}}=\frac{I_S/I_L}{\varepsilon_S(\gamma_1)/\varepsilon_L(\gamma_1)}
=\frac{\omega_1(\theta_S)}{\omega_1(\theta_L)}f_{\mathrm{ADO}},\qquad
f_{\mathrm{ADO}}=\frac{C-\omega_2(\theta_S)\varepsilon_S(\gamma_2)/N_S}
{C-\omega_2(\theta_L)\varepsilon_L(\gamma_2)/N_L},
\]

\[
C=\sum_{g=S,M,L}\omega_2(\theta_g)\varepsilon_g(\gamma_2).
\]

`εg` 是该组效率之和，`1/Ng` 修正不能用同一探测器形成 self-coincidence；不能再把待测线组效率多除一次。若输入只有两个角组计数和 target-energy 效率比，只能求 `R_ADO`；求 `f_ADO` 还需独立的本征角分布比或 Eq4/5 的 gate/geometry 输入。用同一个 `R_ADO` 当本征参考会把 `f=1` 变成恒等式，不能验证修正。

### 单探测器展开及失败控制

在原式所用 `ω1ω2` 分离模型内，定义 `ai=ω1(θi)εi(γ1)`、`bi=ω2(θi)εi(γ2)`、`C=Σj bj`。显式 ordered detector-pair 求和给

\[
I_g=K\sum_{i\in g}a_i(C-b_i)=K A_g(C-\bar b_g),\qquad
A_g=\sum_{i\in g}a_i,\quad
\bar b_g=\frac{\sum_{i\in g}a_i b_i}{A_g}.
\]

组内角响应相同时，`Ag=ω1(θg)εg(γ1)`；组公式进一步以 `ω2(θg)εg(γ2)/Ng` 近似 `b̄g`。同样的组效率总和不保证这一替换成立，因为 self-exclusion 还含两个能量的逐探测器效率乘积。自设 `32°/58°/90°`、每组4台、target组效率 `.04/.06/.05`、gate组效率 `.04/.04/.04`、target/gate `(A2,A4)=(.24,−.07)/(.30,.08)` 时，均匀组内响应给 `f=.974006`；只把S组两个能量的效率各改成 `.002/.002/.002/.034`、保持组总和，则显式 pair 结果为 `.772081`。这是近似失败例，不是原阵列的校准误差。

若 `bi≥0`，令 `η=max_i bi/C<1`，则 `1−η≤f≤1/(1−η)`，其中还假设上述组内角响应相同且效率修正方向一致。每组4台且组内 gate response 均匀时，`η≤1/4`，必要范围为 `.75≤f≤4/3`；探测器数量增加只在 response 不集中到少数台的条件下使 self-exclusion 变小。论文的38个 unordered hardware pairs 与自设 energy-labelled ordered assignments 的44项是不同计数对象，不能从 `38/16` 直接推标准误差或独立样本数。

### 误差传播与可识别性

自设 `NS=5000`、`NL=4800`、效率比 `e=.80±.016`，另给独立本征参考 `r=1.34±.04`。此处 `NS/NL` 表示计数，勿与上文探测器数量 `N_S/N_L` 混用。得到 `R_ADO=1.302083`、`f=R_ADO/r=.971704`。在两个计数为独立 Poisson、其它输入独立的练习条件下，`σf=.040057`。一般应计算

\[
\sigma_f^2=\nabla f^\mathsf T\Sigma\nabla f,\qquad
\nabla f=f(1/N_S,-1/N_L,-1/e,-1/r).
\]

仅改变自设效率比与参考比相关系数 `ρ=−.8/0/+.8`，`σf` 分别为 `.026508/.040057/.050065`。共享 events、峰拟合/背景、效率与参考共用的校准数据会破坏独立假设；原文 Fig1 的最大计算偏离 `5.2%/3.2%` 不是完整实验 uncertainty 或本练习的 `σf`（Z02-7）。

### 角度采样与Day14的条件桥

等权 `32°/58°/90°` 的 `ΣP2=0`、`ΣP4≈−.01712974`。本任务推得 `31.7175°/58.2825°/90°` 可使两者同时为零；这依赖等权及只考虑K2/K4，作者未声明该阵列据此设计。实际 gate 效率不等、角相关、finite acceptance 或 higher ranks 均需另核。

[[linear-polarization-asymmetry]]“未分峰偏振的联合命题与选择条件”的 common-selection point-response 模型，若只用乘法几何 `f` 把其必要域接到 [[herzan-2015-193bi-spectroscopy]] HE15-9 的 shared mean，至少需 `f≈1.488716`，对应 self-exclusion bound 的必要 `η≥.32828`。这只是跨两项条件模型的任务推导；`145Tb` 的均匀4台组上界不足，不构成 JUROGAM 的实际排除，因为没有其 matched gates、逐台响应、完整 γγ correlation、polarization weighting 或 joint covariance。

复算入口：`system/scripts/day15_ado_preview_worksheet.py`；结果和图位于 `outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/day15-ado-preview-worksheet.json`、`day15-ado-input-uncertainty.svg`。28项 pair-sum/limits/gradient/PSD/不可识别性检查通过；图经PNG视觉核验。这里保存定义、推导、数值和边界，使可复用知识不只留在 outputs。

### 来源谱系与下一项可检验问题

Z02-8明确2002方法文用 Ref3 的 `145Tb` 实验数据，DOI `10.1007/s100500170001` 只核到metadata；不能把方法文与对应实验引用计成独立采集。当前最高信息问题是：原式的 `ω1ω2` 分离响应在什么 gate/acceptance 条件下逼近完整 joint γγ response，怎样用同阵列参考线与换门检验。需要实际 detector-pair acceptance、alignment/feeding、净计数及 covariance；这些输入缺失时保持条件推导与实验事实分层。

## Sources

[[twin-1970-polarization-angular-correlation-40k]] combines near-threshold `a2/a4` angular distributions, γγ correlations and Compton polarization; it shows that joint fits can resolve δ branches that a single angular distribution cannot.

- [[draper-1970-gaussian-substate-side-feeding]]
- [[zobel-1980-magnetic-substate-distributions]]
- [[ionescu-1981-improved-angular-distribution-analysis-particle-xn]]
- [[zobel-1983-energy-projectile-alignment]]
- [[lauritsen-2025-gamma-angular-formalism-tracking-arrays]]
- [[chiara-2012-cu65-cu67-core-coupled-protons]]
- [[summary-2013-bases-spin-parity-assignments]]
- [[liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br]]
- [[zheng-2002-ado-coincidence-angular-anisotropy]]
- [[taras-1971-phase-defined-polarization-formulas]]
- [[taras-1970-particle-gamma-angular-correlations]]

## Evolution Log

- 2026-07-13：加入 Liu 2016 的 AFRODITE ADO calibration 与 ADO+polarization assignment 案例。
- 2026-10-15：Day14内无学分Day15预习，固化Zheng原式、组/单探测器self-exclusion、额外输入与误差练习，并修正RB偶K适用条件；不改review状态或给予Day15学分。
