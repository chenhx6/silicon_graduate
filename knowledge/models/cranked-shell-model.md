---
type: model
title: 推转壳模型
aliases: [cranked shell model, CSM]
created: 2026-07-01
updated: 2026-09-30
status: active
review_status: unreviewed
model_family: rotating-shell-model
degrees_of_freedom: [quasiparticle-orbitals, pairing, rotational-frequency, deformation]
parameters: [beta2, gamma, pairing, rotational-frequency]
tags: [signature, coriolis, high-spin]
---

# 推转壳模型（Cranked Shell Model）

## Purpose

研究旋转频率下准粒子 Routhian、alignment、带交叉与 signature splitting。

## Hamiltonian or Core Formalism

形变单粒子场加推转项和 pairing；具体基底、参数化及是否粒子数守恒必须按来源说明。[[babra-2019-deformation-change-136sm]] 还结合准粒子 Routhian 与总 Routhian 面（TRS）追踪带交叉和竞争形变极小。

## Degrees of Freedom

准粒子轨道、signature、pairing、形变和转动频率。

## Assumptions

平均场及给定形变近似；当前 `131Ba/133Ce` 来源用它分析 `νg7/2[404]7/2+` 两支 signature 的 γ 灵敏度。

## Inputs and Parameters

β2、γ、β4、pairing、转动频率和轨道占据。Babra 2019 的准粒子交叉示例采用 `β2=0.25, β4=0.02, γ=-15°`，TRS 则在 `(β2,γ)` 平面逐频率对 `β4` 极小化。

## Predicted Observables

quasiparticle Routhian、alignment、交叉频率与 signature splitting。

[[frauendorf-2018-beyond-unified-model]] uses the cranked-shell model as a fast configuration-classification layer: diabatic Routhians, alignment and crossings organize multi-band spectra, while the review warns that high-K configurations can be misplaced in simple Routhian diagrams and that quantum mixing requires more complete models.

## Strengths

可直接展示 γ=0 与非零 γ 时 signature branches 的能量响应。

## Known Limitations

单独改变 γ 不能涵盖近邻低-j 轨道混合的全部效应；模型趋势不能把 S(I) 变成 γ 的唯一反演。准粒子交叉频率和 TRS 极小还依赖 Woods-Saxon、配对及宏观-微观能量设置；多个竞争极小存在时，有限寿命数据未必能唯一选形状。

### `131Xe` 的 Woods–Saxon TRS 案例（2026-09-30）

[[banik-2020-131xe-multiple-band-structures]] 使用 Woods–Saxon 单粒子能级与 Strutinsky 壳修正，在 `β₂–γ` 网格计算总 Routhian 面，并逐频率对 `β₄` 极小化（BNK20-6, BNK20-7）。对负宇称 1-qp `B1`，最低点从低频的 γ-soft 区域移动到 `ℏω≈0.21–0.26 MeV` 的三轴区域，再在更高频出现两个极小；对 3-qp `B4/B4(a)`，模型给出宽 γ-soft 区。它说明高自旋形变可随频率和组态变化；`γ` 与 `β₂` 都是 TRS 模型输出，不能当作直接形状测量，也不可与 TPSM/TPRM 的固定输入不加约定地平均。

### `131Xe` Woods–Saxon TRS 频率演化（2026-09-30）

[[banik-2020-131xe-multiple-band-structures]] 用 Woods–Saxon 单粒子势和 Strutinsky 壳修正，在 `β₂–γ` 网格计算 TRS，并逐频率对 `β₄` 极小化（BNK20-6, BNK20-7）。负宇称 1-qp `B1` 的 TRS 极小从低频 γ-soft 区域移到 `ℏω≈0.21–0.26 MeV` 的约 `γ=−26°`，再在更高频出现两个极小；3-qp `B4/B4(a)` 的极小位于宽 γ-soft 区。此例说明 TRS 能描述转频与组态依赖的形状响应；它是 Woods–Saxon/Strutinsky macroscopic-microscopic calculation，不应误标成 Nilsson-only CNS、自洽 HFB 解或直接形状测量。

## Related Models

[[cranked-nilsson-strutinsky-model]]、[[triaxial-particle-rotor-model]]

## Sources

- [[ding-2021-131ba-133ce-signature-splitting]]
- [[babra-2019-deformation-change-136sm]]
- [[banik-2020-131xe-multiple-band-structures]]
- [[banik-2020-131xe-multiple-band-structures]]
- [[frauendorf-2018-beyond-unified-model]]

## Evolution Log

- 2026-07-01：由 N=75 g7/2 signature-splitting 分析建立。
- 2026-07-05：加入 `136Sm` 准粒子交叉与 TRS 多极小的高自旋形变演化用途。
- 2026-09-20：加入 review-level Routhian/configuration-classification and quantum-mixing boundary。
- 2026-09-30：加入 `131Xe` Woods–Saxon TRS 的转频依赖与模型输出边界。
- 2026-09-30：加入 `131Xe` 的 Woods–Saxon/Strutinsky TRS 频率依赖例子，并将能面极小与实验形状测量、固定 TPSM 输入区分。
