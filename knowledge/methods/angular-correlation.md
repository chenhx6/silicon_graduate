---
type: method
title: γ 射线角关联分析
aliases: [angular correlation, gamma-ray angular correlation, particle-gamma angular correlation, gamma-gamma angular correlation]
created: 2026-07-09
updated: 2026-07-12
status: ai-draft
review_status: unreviewed
method_type: gamma-ray-angular-correlation
tags: [multipolarity, alignment, attenuation, deorientation, pado-support]
---

# γ 射线角关联分析（Gamma-Ray Angular Correlation）

## Purpose

角关联分析（angular correlation）利用先前反应、粒子或 γ 辐射方向与后续 γ 射线方向之间的相关性，约束 nuclear alignment、transition multipolarity、mixing ratio 或退取向效应。

## Inputs and Assumptions

- Coincident particle-gamma or gamma-gamma directions with calibrated detector geometry.
- Known or hypothesized spin sequence, multipolarity and mixing-ratio values.
- A controlled description of initial alignment/orientation and any deorientation corrections.
- Separation of detector finite-solid-angle effects from nuclear alignment/deorientation effects.

## Source-Level Foundation

[[radeck-2012-deorientation-lifetime-98ru-rdds]] 在 inverse Coulomb excitation + RDDS 实验中拟合 distance-dependent particle-γ angular correlations，用未扰动的 Coulomb-excitation angular correlation 与实验相关函数之比提取 time-dependent attenuation factor `Gk(d)`。

## Boundary

- angular correlation 与 [[angular-distribution]] 都使用角度依赖强度，但前者保留两个事件或一个粒子-γ 方向之间的相关性；不能与普通 single-γ angular distribution 静默合并。
- [[kramer-flecken-1989-use-dco-ratios]] 展示了 DCO 是从 gamma-gamma angular correlation 压缩出来的一个 gate-与几何依赖比值，而不是脱离原始 correlation formalism 的普适常数。
- Radeck 2012 的 particle-γ angular correlation correction 属于 inverse Coulomb excitation / RDDS 语境，不是 fusion-evaporation P-ADO 的直接 `σ/I` 来源。
- detector finite-solid-angle factor `Qk` 与 nuclear alignment/deorientation factor `Gk` 是不同系统项。

## Relation to P-ADO

角关联可作为 alignment/deorientation 参数的独立约束或校正来源。它支持 P-ADO 的方法论动机：`δ` 提取不应把 alignment 或 attenuation response 当作无不确定度常数。

## What It Can Establish

Angular correlations can constrain spin sequence, multipolarity, mixing ratio, alignment and time-dependent deorientation when the coincidence geometry and reference response are controlled.

## What It Cannot Establish Alone

Angular correlations do not by themselves define a universal side-feeding Gaussian width or `sigma/I` prior. Their interpretation still depends on reaction mechanism, feeding history, detector response and model assumptions.

## Sources

[[konigshofen-2001-mixing-ratios-130ba]] demonstrates a three-angle low-spin application: efficiency-corrected `W(180°)/W(90°)` and `W(55°)/W(90°)` ratios can yield a unique `δ` for 18 `130Ba` transitions when the spin/parity and pure-E2 reference assumptions hold. The unresolved `4+_3→3+_1` row remains an explicit multi-solution boundary.

[[falkoff-1948-polarization-correlation]] is a historical successive-γ polarization precursor: its `A` coefficient complements, but does not replace, directional-correlation coefficients and requires phase-convention mapping.

[[krane-1973-directional-correlations-oriented-states]] is the generalized DCO foundation, separating orientation parameters, radiation coefficients, finite geometry and multipole conventions from later compressed ratios.

- [[radeck-2012-deorientation-lifetime-98ru-rdds]]
- [[lauritsen-2025-gamma-angular-formalism-tracking-arrays]]
- [[kramer-flecken-1989-use-dco-ratios]]
- [[bargholtz-1987-high-spin-gamma-gamma-directional-correlations]]

[[starosta-1999-pdco-experimental-test]] is a direct high-spin example of the compressed-observable boundary: `R_DCO` constrains the alignment/multipolarity space, while CLOVER polarization adds electric/magnetic sensitivity; the combined fit still leaves a 490-keV E2/M1-E2 branch under the paper's assumptions.

[[james-twin-butler-1974-angular-correlation-statistics]] adds the statistical gate: alignment/model variance enters the design matrix, effective degrees of freedom are `n−rank`, and `arctan δ` confidence contours must retain nonlinear/multibranch topology.
