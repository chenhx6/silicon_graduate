---
type: concept
title: 退取向
aliases: [deorientation, spin deorientation, nuclear-spin deorientation, orientation attenuation]
created: 2026-07-09
updated: 2026-07-09
status: ai-draft
review_status: unreviewed
concept_type: gamma-angular-distribution-foundation
confidence: low
high_confirmed_by:
high_confirmed_date:
tags: [alignment, angular-distribution, attenuation, pado-support]
---

# 退取向（Deorientation）

## Definition

退取向（deorientation）指初始核自旋取向或取向排列在粒子蒸发、γ 级联、寿命演化或外场扰动中逐步减弱的过程。它影响 emitting level 的 magnetic-substate population，因此会改变 γ 射线角分布或角关联中的 alignment/attenuation 因子。

## Source-Level Meaning

[[cejnar-1996-spin-deorientation-alpha-2n-gamma]] 在 compound-nucleus `(α,2nγ)` 反应中计算 feeding flow 与 orientation flow，并用 deorientation coefficient `Uλ(Ji L Jf)` 描述每次粒子或 γ 发射对取向参数的衰减。

[[radeck-2012-deorientation-lifetime-98ru-rdds]] 在 inverse Coulomb excitation + RDDS 实验中把 deorientation 归因于 recoil in vacuum 时 nuclear spin 与 electron spin 的 hyperfine interaction，并用 time-dependent attenuation factor `Gk(t/d)` 修正 particle-γ angular correlations。

## Boundary

- deorientation 是核自旋取向随反应或衰变历史改变的物理/统计过程，不等同于探测器有限立体角造成的 solid-angle attenuation。
- deorientation coefficient、attenuation coefficient `αK/Gk`、Gaussian width `σ`、`σ/I` 或 `σ/J` 是相关但不相同的描述层。
- RDDS / Coulomb-excitation 中的 hyperfine deorientation 不应直接改写成 fusion-evaporation side-feeding `σ/I` 主证据。
- 从 deorientation calculation 得到的 side-feeding Gaussian 参数必须保留 reaction、projectile energy、feeding route 和 model assumptions，不能当作通用常数。

## Relevance to P-ADO

P-ADO 或 angular-distribution / polarization fitting 若固定一个 alignment-width 参数，实际等于固定了 emitting state 的退取向历史或其近似表示。Cejnar 1996 支持的谨慎表述是：`σ` 区间可以由反应特定的 deorientation calculation 约束，但这种约束依赖 reaction condition 和 feeding route。

## Necessary Assumptions

To use deorientation in a fit or project argument, identify the reaction mechanism, feeding path, lifetime or recoil-time scale, and the local meaning of any attenuation coefficient. Detector solid-angle corrections must be kept separate from nuclear deorientation.

## Discriminating Observables

Relevant observables include angular-distribution coefficients, particle-gamma or gamma-gamma angular correlations, time- or distance-dependent attenuation factors, reference transitions with known multipolarity, and condition-matched polarization data.

## Supporting Evidence

[[cejnar-1996-spin-deorientation-alpha-2n-gamma]] supports reaction-route deorientation calculations for `(alpha,2n gamma)` reactions. [[radeck-2012-deorientation-lifetime-98ru-rdds]] supports time-dependent hyperfine deorientation corrections in inverse Coulomb excitation + RDDS.

## Counter-evidence and Competing Interpretations

The same angular change can sometimes be represented by different layers: side-feeding Gaussian width, attenuation coefficients, time-dependent deorientation, detector response, or mixing-ratio changes. These representations should not be collapsed without source-specific mapping.

## Our Current Position

Deorientation is a necessary background concept for P-ADO `sigma/I` uncertainty, but current sources do not justify a universal deorientation or Gaussian-width constant. The concept remains low-confidence until mapped to the user's actual reaction and code notation.

## Sources

- [[cejnar-1996-spin-deorientation-alpha-2n-gamma]]
- [[radeck-2012-deorientation-lifetime-98ru-rdds]]

## 未观测γ与全部衰变的条件权重

[[martin-1987-ensdf-mixing-ratio-phase-conventions]] MA87-3原Eq9指出：对完全未观测的两multipolebranch，U所用qtot=δgamma²(1+alpha_Lprime)/(1+alpha_L)，alpha是totalICC。若明确postselect其光子通道，才按相应gamma条件权重传播；只检测一shellelectron又是另一对象。混合U无干涉、U0=1，但不同multipole/atomicconversion可影响强度权重。

[[internal-conversion-analysis]]的新168.71W例保持qgamma与qtot分开，并保留trace、pure/equalICC和rank2/4控制。这不是hyperfineGk或任意sigma重设，也不模拟电子轨迹。不同candidate的radiativeq自由时，可抵消ICC因子而保全所有Uk，因此原manual所说paritysensitivity不能自动升级为唯一parity测量。
