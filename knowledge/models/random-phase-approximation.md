---
type: model
title: 随机相位近似
aliases: [random phase approximation, RPA, microscopic RPA]
created: 2026-07-01
updated: 2026-07-01
status: active
review_status: unreviewed
model_family: small-amplitude-microscopic-approximation
degrees_of_freedom: [quasiparticle-excitations, small-amplitude-collective-modes]
parameters: [mean-field, pairing, residual-interaction]
tags: [wobbling, microscopic-model]
---

# 随机相位近似（Random Phase Approximation）

## Purpose

在旋转平均场附近描述小振幅集体激发，包括 wobbling 模式。

## Hamiltonian or Core Formalism

从配对加四极-四极等多体哈密顿量的旋转平均场出发，对小振幅涨落线性化。

## Degrees of Freedom

准粒子两体激发和集体小振幅模式。

## Assumptions

振幅较小，且工作点远离模式失稳。

## Inputs and Parameters

平均场形变、配对和残余相互作用。

## Predicted Observables

wobbling frequency、跃迁矩阵元和模式成分。

## Strengths

提供比现象学转子更微观的 wobbling 动力学。

## Known Limitations

[[book-casten-nuclear-structure-simple-perspective]] 二版 p.407 Eq. (10.20) 的简并可分离例给 \(\omega_{\rm RPA}^2=D^2+2CD\sum_r Q_r^2\)。需与相同模型的 TDA 根比较并检验正频稳定性。根号内为负时，该参考态下的频率属于线性失稳。TDA 的可分离求和式只捕获对所选算符有非零重叠的根。斜率、根的数值和组态成分仍随相互作用及有效跃迁算符改变。

[[frauendorf-2024-wobbling-review]] 指出 RPA 在 TW instability 附近失效，且尚未应用于正常形变核。

## Related Models

[[triaxial-projected-shell-model]]、[[triaxial-particle-rotor-model]]

## Sources

- [[frauendorf-2024-wobbling-review]]
- [[book-casten-nuclear-structure-simple-perspective]]

## Evolution Log

- 2026-07-01：由 2024 综述建立适用范围。

