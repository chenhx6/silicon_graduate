---
type: model
title: 相互作用玻色子模型
aliases: [interacting boson model, IBM, IBM-1, O(6), boson-number-nonconserving IBM]
created: 2026-07-01
updated: 2026-07-05
status: active
review_status: unreviewed
model_family: algebraic-collective-model
degrees_of_freedom: [s-boson, d-boson]
parameters: [hamiltonian-coefficients, boson-number]
tags: [collective-model, gamma-softness]
---

# 相互作用玻色子模型（Interacting Boson Model）

## Purpose

用 s、d 玻色子代数描述偶偶核低能集体结构。

## Hamiltonian or Core Formalism

一致四极算符的 \(O(6)\)–\(SU(3)\) 路径在 \(H=a_2Q_\chi\cdot Q_\chi+a_1J^2\) 与 \(T(E2)\) 中共用 \(\chi\)。相同 \(J\) 的能级差消去 \(a_1J(J+1)\)，相对跃迁和同自旋能级差之比可在该路径下检验 \(\chi\) 与玻色子数的选择。涉及不同 \(J\) 的能级间隔仍依赖转动项。[[book-casten-nuclear-structure-simple-perspective]]，二版 Eqs. (6.76)–(6.77)、Table 6.14。

[[zamfir-casten-1991-gamma-softness-triaxiality]] 从 O(6) γ-unstable 极限出发，加入三阶 d-boson 项，在 γ=30° 引入弱势能极小。

[[nomura-2017-odd-mass-gamma-soft-shape-transitions]] 将偶偶芯 IBM 与单个奇核子耦合为 IBFM；IBM 参数由 DD-PC1 RHB `(β,γ)` 势能面映射确定，但玻色子-费米子耦合仍逐核拟合。

[[nomura-2021-pairing-triaxial-vibrations-gamma-soft]] 使用 `(sd)^(n0-1) ⊕ (sd)^n0 ⊕ (sd)^(n0+1)` 模型空间和 `s†+s` 耦合显式表示配对振动，并保留三体 d-boson 项描述三轴势与 γ 带。

[[nomura-2022-questioning-wobbling-ibfm]] 使用 proton-neutron IBM（IBM-2）描述四个 γ-soft 偶偶芯，再通过 [[interacting-boson-fermion-model]] 耦合一个奇 `h11/2` 费米子，计算 reported low-spin wobbling candidates 的替代带结构与 E2/M1 observables。

## Degrees of Freedom

成对价核子的 L=0、2 集体自由度；扩展实现可允许相邻玻色子数子空间耦合，或再与一个奇费米子耦合。

## Assumptions

IBM-1 不区分质子/中子玻色子；几何势能面由相干态映射得到。

## Inputs and Parameters

玻色子数与哈密顿量系数；1991 工作用三阶项强度相对 O(6) 尺度连续调节 γ 依赖。2021 工作还以 SCMF `(α,β,γ)` 势能面约束玻色子数守恒/非守恒项，并另按经验转动惯量调整转动项。

## Predicted Observables

低能能级、γ 带 staggering、激发 `0+` 态、B(E2) 及其对 γ 与配对自由度的敏感性。

## Strengths

可在统一代数框架中从 γ-unstable 连续过渡到带有 γ 偏好的势。

## Known Limitations

模型参数与真实微观势能面不一一对应。`s,d` 空间不含较高激发的多准粒子组态；玻色子数非守恒实现未区分质子、 中子配对坐标。IBFM 的粒子-芯耦合若按数据拟合，也会限制独立预测力。

## Related Models

[[gamma-unstable-model]]、[[interacting-boson-fermion-model]]

## Sources

- [[zamfir-casten-1991-gamma-softness-triaxiality]]
- [[nomura-2017-odd-mass-gamma-soft-shape-transitions]]
- [[nomura-2021-pairing-triaxial-vibrations-gamma-soft]]
- [[nomura-2022-questioning-wobbling-ibfm]]

## Evolution Log

- 2026-07-01：记录 O(6)+三阶项的判据用途。
- 2026-07-05：加入 RHB→IBM/IBFM 映射以及玻色子数非守恒的配对-三轴耦合扩展。
- 2026-07-05：链接 Nomura 2022 的 IBM-2 core→IBFM low-spin alternative。
