---
type: model
title: 核子配对近似（NPA）
aliases: [NPA, nucleon pair approximation, fermion pair model, Zhao-Arima pair model]
created: 2026-11-06
updated: 2026-11-06
status: active
review_status: unreviewed
model_family: truncated-shell-model
degrees_of_freedom: [fermion-pairs, collective-pairs, broken-pairs]
parameters: [single-particle-energies, pairing-strength, multipole-interaction-strengths]
tags: [shell-model, pair-approximation, transitional-nuclei, configuration-truncation]
---

# 核子配对近似（Nucleon Pair Approximation, NPA）

## Purpose

核子配对近似由 J. Q. Chen、A. Arima、Y. M. Zhao（赵玉民）等学者系统发展，用于在严格保持费米子反对称性与微观 Pauli 原理的前提下，通过将壳模型组态空间截断为少数集体配对基矢，实现中重过渡区原子核低激发态与中高自旋态的大规模微观计算。它在近代物理研究所（IMP）等单位的过渡区核（如 A~130 碘、氙、钡同位素）谱学理论分析中被广泛应用。

## Hamiltonian or Core Formalism

NPA 在标准球形或变形壳模型单粒子基底上构建有确定角动量的费米子对产生算符：
$$A^\dagger(r) = \sum_{j_1 j_2} y(j_1 j_2 r) \frac{1}{\sqrt{1 + \delta_{j_1 j_2}}} [c^\dagger_{j_1} \times c^\dagger_{j_2}]^{(r)}$$
其中常用的集体对包括：
- $S$ 对：$r=0^+$（单极配对，超流基石）；
- $D$ 对：$r=2^+$（四极配对，低能四极振动与转动载体）；
- $G$ 对：$r=4^+$；
- 高自旋非集体破对（Unpaired nucleons）：如奇核中单准粒子或非相干对。

多对基矢表示为：
$$| (r_1 r_2 \dots r_p) J M \rangle = [A^\dagger(r_1) \times A^\dagger(r_2) \times \dots \times A^\dagger(r_p)]^{(J)}_M | 0 \rangle$$

通过费米子对对易代数计算重叠重叠矩阵（Norm matrix）与哈密顿量矩阵元，并进行广义广义特征值问题对角化：
$$H \Psi = E N \Psi$$

## Strengths and Physical Insights

1. **严格费米子属性**：不同于玻色子模型（IBM），NPA 严格保留了费米子对易子中的交换项与 Pauli 阻塞效应；
2. **高阶截断能力**：组态空间维度从完整壳模型的 $10^9 \sim 10^{12}$ 压缩至 $10^3 \sim 10^5$，使得重核区多价核子体系计算成为可能；
3. **准粒子与集体运动无缝过渡**：通过在 $S, D$ 对凝聚背景中引入非集体对（破对），能够自然描述回弯（Backbending）、两准粒子高自旋带及同核异能态。

## Boundary and Failure Domain

- **大形变极限失效**：当核发生强烈长椭球转动（$\beta_2 > 0.3$）或高转速下许多费米子对同时去对对齐时，仅由有限几个集体对展开的基矢完备性不足；
- **计算复杂度**：随着核子对数增加，由于费米子反对称化的严格处理，Wick 定理收缩项数目依然急剧上升，对满壳外 8 个以上价核子的体系需要专门的高性能对乘法算法。
