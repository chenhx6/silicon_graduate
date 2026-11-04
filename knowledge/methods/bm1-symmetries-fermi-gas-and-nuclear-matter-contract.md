---
type: method
title: "Bohr-Mottelson 第一卷：空间时间对称性、费米气体与核物质微观方法合同"
aliases: [BM1 Symmetries and Nuclear Matter Contract, BM1对称性与核物质合同]
created: 2026-11-04
updated: 2026-11-04
status: active
review_status: unreviewed
method_type: single-particle-theory-contract
tags: [bohr-mottelson, single-particle-motion, time-reversal, kramers-degeneracy, isospin-invariance, morpurgo-rule, fermi-gas, lane-potential, woods-saxon]
topics: [symmetries, nuclear-matter, single-particle-potential, isospin]
sources: [book-bohr-mottelson-nuclear-structure, book-bohr-mottelson-nuclear-structure-vol2, book-greiner-nuclear-models]
---

# Bohr-Mottelson 第一卷：空间时间对称性、费米气体与核物质微观方法合同

## Purpose

本方法合同严格绑定 Aage Bohr 与 Ben R. Mottelson 经典巨著《Nuclear Structure, Volume I: Single-Particle Motion》（1969 / 1998 重印版）第 1、2、3 章，
系统形式化原子核空间-时间反演对称性（$\\mathcal{P}, \\mathcal{T}$）与 Kramers 简并定理、强核力同位旋 $SU(2)$ 不变性与 Morpurgo $E1$ 跃迁禁戒定则、均一核物质费米气体模型（Fermi Gas Model）与 Lane 同位旋标量势，以及表面导数型自旋-轨道耦合 Woods-Saxon 单粒子势，
为核结构微观模型、对称性破缺与单核子激发能谱提供权威数学物理基准。

## Inputs and Assumptions

1. **反幺正时间反演算符代数结构**：$\\mathcal{T} = U K_0$，作用于费米子单态满足 $\\mathcal{T}^2 = (-1)^{2j} = -1$；
2. **同位旋标量与矢量分解假设**：电磁多极辐射算符严格按单核子空间-同位旋张量分解为同位旋标量项（$\\Delta T=0$）与同位旋矢量项（$\\Delta T=0, \\pm 1$）；
3. **均一各向同性饱和核物质模型**：核物质在饱和密度 $\\rho_0 \\a0.17\\text{ fm}^{-3}$ 处动能与唯象短程相互作用势能处于平衡；
4. **定域平均场（Woods-Saxon）假设**：核子在内部感受平坦深势阱（$V_0 \\approx 50\\text{ MeV}$），在表面弥散区（$a \\a0.65\\text{ fm}$）感受强自旋-轨道力矩。

## What It Can Establish

1. **Kramers 简并定理与变形场简并基石**：
   $$\\mathcal{T}^2 = -1 \\implies H|\\psi\\rangle = E|\\psi\\rangle \\implies H(\\mathcal{T}|\\psi\\rangle) = E(\\mathcal{T}|\\psi\\rangle)$$
   - 严格证明在无外加磁场或宏观推转（无 Coriolis 力）的任何时间反演不变体系中，半整数自旋体系所有能级必严格双重简并；
   - 证明轴对称/三轴形变场下单粒子轨道必成对出现为对角投影对（$|\\Omega\\rangle$ 与 $|-\\Omega\\rangle$）；
2. **同位旋不变性与 Morpurgo $E1$ 跃迁禁戒定则**：
   $$e_{\\text{IS}}(E1) = \\frac{N - Z}{2A} e \\equiv 0 \\quad (\\text{当 } N = Z)$$
   - 证明在自共轭核（$N = Z$）中，同位旋标量电荷严格为零；
   - 导出 $\\Delta T = 0$ 的电偶极跃迁矩阵元在偶数分波下严格抵消，实验上该类 $E1$ 跃迁几率被剧烈压低 $10^2 \\sim 10^4$ 倍；
3. **均一核物质费米气体参量与 Lane 势**：
   $$k_F = \\left(\\frac{3\\pi^2 \\rho_0}{2}\\right)^{1/3} \\a1.36\\text{ fm}^{-1},\\quad \\epsilon_F \\approx 38.5\\text{ MeV},\\quad \\langle T \\rangle = \\frac{3}{5}\\epsilon_F \\approx 23.1\\text{ MeV}$$
   $$V_p(r) = V_0(r) - \\frac{N-Z}{4A} V_1(r),\\quad V_n(r) = V_0(r) + \\frac{N-Z}{4A} V_1(r)$$
   - 给出对称能系数 $b_{\\text{sym}} \\a30\\text{ MeV}$ 与不可压缩模量 $K_\\infty \\approx 200 - 250\\text{ MeV}$；
   - 证明在中子过剩核中中子势阱深度变浅、质子势阱加深；
4. **表面导数型自旋-轨道耦合与经典幻数起源**：
   $$\\Delta E_{ls} = \\frac{2l+1}{2} V_{ls} r_0^2 \\left\\langle \\frac{1}{r}\\left \vert \\frac{df}{dr}\\right \vert \\right\ \rangle$$
   - 证明能级劈裂与 $(2l+1)$ 成正比，驱动高 $l$ 壳层的最高 $j = l + 1/2$ 独特宇称轨道（$1g_{9/2}, 1h_{11/2}, 1i_{13/2}$）大幅下沉穿入下一主壳，微观确立 28, 50, 82, 126 经典幻数。

## What It Cannot Establish Alone

1. **大振幅四极形变与集体转动态**：本卷局限于球形单粒子运动与微扰极化，宏观转动、三轴形状共存与多声子振动必须由第二卷形式化；
2. **核力张量力（Tensor Force）微观起源**：Woods-Saxon 唯象势无法微观解释单极张量力驱动的滴线区幻数演化（如 $N=20, 28$ 反转岛）；
3. **超流配对凝聚与准粒子准能谱**：未包含 Bogoliubov 准粒子正则变换，必须结合 BCS 理论。

## Sources

- [[book-bohr-mottelson-nuclear-structure]]
- [[book-bohr-mottelson-nuclear-structure-vol2]]
- [[bm1-electromagnetic-multipoles-and-single-particle-contract]]
- [[greiner-asymmetric-rotor-and-rvm-contract]]
