---
type: method
title: γ 射线角分布分析
aliases: [angular distribution, gamma-ray angular distribution, gamma angular distribution, in-beam angular distribution, ADO]
created: 2026-07-08
updated: 2026-09-21
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

## Relation to Other Methods

Angular distribution 可与 [[multipole-mixing-ratio]]、[[dco-ratio]] 和线偏振共同约束 `δ`。不同实验几何、beam energy、projectile 或 target condition 下得到的角分布参数不能无条件混用。

ADO（angular distribution from oriented states）ratio 是有限角组实现：在相同 gate 下比较不同探测器角组的归一化强度，并用本实验已知 multipolarities 标定 dipole/quadrupole 区域。[[liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br]] 的 AFRODITE 几何给出 stretched quadrupole 约 1.1、pure stretched dipole 约 0.7；这些阈值不得跨阵列复用。

[[zheng-2002-ado-coincidence-angular-anisotropy]] 给出符合模式下 ADO 的显式效率修正：`R_ADO(γ1)=[I^S/I^L]/[ε_S(γ1)/ε_L(γ1)]`，并将其写为待测 γ 的角分布比乘以门控 γ 和探测器响应共同决定的 `f_ADO`。在 `145Tb` 的 12 套 BGO-HPGe、约 `±32°/±58°/90°` 三角度组中，门控能量 `100–1500 keV` 的 `f_ADO` 最大偏差约为四极门 `5.2%`、偶极门 `3.2%`；该来源报告的纯四极约 `R_ADO=1.25`、纯偶极约 `0.75` 只能作为本阵列的局部标定，不能替代新阵列的参考线验证。

## Tracking-Array Formalism

[[lauritsen-2025-gamma-angular-formalism-tracking-arrays]] gives a modern tracking-array notation for in-beam angular distributions: `omega(theta)=A0+alpha2 A2 P2(cos theta)+alpha4 A4 P4(cos theta)+...`. In that local formula, `Amax_k` contains the spin sequence, multipolarities and mixing ratio `delta`, while `alpha_k(J)` is the nuclear alignment/deorientation attenuation calculated from magnetic-substate population `Pm(J)`. The same source usually parameterizes `Pm(J)` as a Gaussian with normalized width `sigma/J`.

This `alpha_k` must not be merged with detector solid-angle attenuation. Lauritsen 2025 uses detector attenuation in the source-correlation formalism and nuclear alignment attenuation in the in-beam angular-distribution formalism; the local definition controls the meaning.

## What It Can Establish

在 alignment 或 population model 足够受控时，角分布可约束 transition multipolarity、mixing ratio 和 attenuation/alignment 参数。

[[rose-brink-1967-phase-defined-angular-distributions]] gives the phase-consistent foundation: the general distribution uses alignment tensors `B_K`, geometry/multipole coefficients `R_K` and reduced interaction-multipole matrix elements. The familiar even-`K` formula requires cylindrical alignment and definite parity; mixed-parity or polarized initial states require the general expression.

[[der-mateosian-sunyar-1974-angular-coefficients]] supplies practical `A_2/A_4` tables through `J=26` (integer) and `51/2` (half-integer). The worked example solves `σ/J` and δ jointly, and explicitly warns that angular-distribution and γγ-correlation δ signs may differ under their respective conventions.

[[yamazaki-1967-aligned-angular-coefficients]] is the earlier coefficient-table backbone: it defines complete-alignment `B_k`, `F_k` and cascade `U_k` tensors for integral and half-integral spins, then applies Gaussian magnetic-substate attenuation. Its explicit angular-distribution/γγ-correlation δ-sign warning is retained as a convention boundary, not merged into a detector calibration.

## What It Cannot Establish Alone

仅凭两个角分布系数通常不能同时唯一确定 `α2`、`α4` 与 `δ`；弱峰、短寿命、Doppler broadening 和 feeding ambiguity 会增加多解风险。

## Practice-Level Boundary

[[chiara-2012-cu65-cu67-core-coupled-protons]] adds a practical spectroscopy example: the angular-distribution calculation for `65Cu` used an assumed `sigma/I = 0.5` because it reproduced known transitions, and the fitted `delta` of one `1115 keV` line changed when the assumed alignment width changed.

[[summary-2013-bases-spin-parity-assignments]] adds reference-guide background that high-spin assignment heuristics are often quoted with a typical orientation parameter, here `σ/I = 0.3`, but that guide-level value is not by itself a demonstrated universal Gaussian prior.

Angular-distribution evidence is one of the standard inputs collected on [[spin-parity-assignment]] pages.

Liu 2016 将 ADO 与 linear polarization 联合用于 `78Br` linking transitions，并由 404.3 keV line 的 `R_ADO=0.79` 与负 polarization 支持 `M1/E2` 及相对 spin revision。

## Sources

[[twin-1970-polarization-angular-correlation-40k]] combines near-threshold `a2/a4` angular distributions, γγ correlations and Compton polarization; it shows that joint fits can resolve δ branches that a single angular distribution cannot.

- [[draper-1970-gaussian-substate-side-feeding]]
- [[zobel-1980-magnetic-substate-distributions]]
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
