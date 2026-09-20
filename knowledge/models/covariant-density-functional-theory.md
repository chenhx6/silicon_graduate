---
type: model
title: 协变密度泛函理论
aliases: [covariant density functional theory, CDFT, constrained CDFT, TAC-CDFT]
created: 2026-07-01
updated: 2026-09-20
status: active
review_status: unreviewed
model_family: self-consistent-mean-field
degrees_of_freedom: [density, deformation, quasiparticle-configuration, rotational-frequency]
parameters: [energy-density-functional, pairing, constraints]
tags: [mean-field, deformation, chirality, high-spin]
---

# 协变密度泛函理论（CDFT）

## Purpose

自洽求解给定核素或组态的密度、形变和能量；加入转动约束后可研究倾斜轴和角动量取向。

## Hamiltonian or Core Formalism

以协变能量密度泛函为基础。当前来源使用 PC-PK1；约束 CDFT 用于组态形变，TAC-CDFT 还包含 `-ω·J` 推转项。

## Degrees of Freedom

密度、四极形变、单粒子占据、配对及转动频率/方向。

## Assumptions

平均场破缺对称性；具体计算可能冻结组态或忽略 pairing。手征双重带的量子隧穿通常仍需 PRM 等恢复。

## Inputs and Parameters

能量密度泛函、基空间、组态约束、pairing 方案和转动频率。

[[ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce]] 使用 PK1 constrained triaxial RMF，为 `133Ce` states a/b 给出组态、`beta/gamma` 与 excitation energies，并把这些形变作为 TPRM 输入。

[[liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br]] 使用 PC-PK1 MDC-CDFT，为 `78Br` 两套 proposed configurations 给出 `beta2/gamma`，并计算 `beta20-beta30` PES；沿 `beta30` 的 softness 支持 octupole correlations，但不是 stable nonzero-`beta30` minimum 的实验测量。

[[peng-chen-2022-chiral-rotation-rhodium-isotopes]] uses PC-PK1 3D-TAC CDFT in ten oscillator shells for `102-107Rh`. Occupations are traced in one configuration family and pairing is omitted; this enables a clean mean-field `omega_crit` trend but produces visible even-`(gd)` discrepancies and no quantum side bands.

[[guo-2022-possible-chiral-multiple-chiral-thallium-isotopes]] uses PK1 adiabatic and configuration-fixed constrained triaxial RMF for `192-200Tl`, with 12 fermion/20 meson shells and no pairing. It selects favorable deformation/configuration minima but contains no cranking orientation or laboratory-frame partner-band calculation.

[[li-2024-144ba-octupole-cdf-3d-lattice]] uses PC-PK1 cranking CDFT on a 3D lattice (1-fm mesh, 30 points per axis) without spatial symmetry restrictions. It obtains `β20≈0.22`, `β30≈0.13` at the ground-state minimum and an average `β30≈0.128` to `I≈24ℏ`; pairing is omitted and parity/total-I restoration is not performed, so parity splitting is outside the calculation.

[[liang-2016-pseudospin-symmetry-review]] supplies the Dirac/RMF symmetry layer: PSS is exact only in the `dΣ/dr=0` limit, while realistic tensor/deformation/continuum terms break the degeneracy; it is not a direct band-assignment rule.

## Predicted Observables

形变极小值、能量、频率、角动量分量及部分带内电磁量。

## Strengths

形变和角动量取向可在给定泛函内自洽产生，适合为粒子-转子模型提供组态和形变输入。

## Known Limitations

不同泛函、pairing 和组态约束会改变结果；模型 γ 不是直接测量；单一平均场不能自动给出左右手量子隧穿。

## Related Models

[[tilted-axis-cranking]]、[[triaxial-particle-rotor-model]]

## Sources

- [[ayangeakaa-2016-133ce-in-beam]]
- [[ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce]]
- [[liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br]]
- [[petrache-2020-137nd-multiple-chiral-bands]]
- [[peng-chen-2022-chiral-rotation-rhodium-isotopes]]
- [[guo-2022-possible-chiral-multiple-chiral-thallium-isotopes]]
- [[li-2024-144ba-octupole-cdf-3d-lattice]]
- [[liang-2016-pseudospin-symmetry-review]]

## Evolution Log

- 2026-07-01：建立 constrained CDFT 与 TAC-CDFT 的共同入口。
- 2026-07-13：加入 Ayangeakaa 2013 的 PK1 constrained-RMF shape/configuration input 与非直接测量边界。
- 2026-07-13：加入 Liu 2016 MDC-CDFT configuration shapes 与 `beta30` softness 边界。
- 2026-08-11: added the Peng-Chen 2022 PC-PK1 3D-TAC isotope-chain example and pairing/side-band limits.
- 2026-08-11: added Guo 2022's PK1 constrained-RMF Tl-isotope screening and separated static minima from rotational chirality.
- 2026-09-20: added Li–Wang 2024 PC-PK1 3D-lattice cranking CDFT and its pairing/parity-projection boundary.
