---
type: method
title: "Hamilton 核谱学角分布、DCO、去取向与 Compton 线偏振方法合同"
aliases: [Hamilton-angular-distribution-contract, DCO-polarization-contract, gamma-correlation-Hamilton-contract]
created: 2026-11-04
updated: 2026-11-04
status: active
review_status: unreviewed
method_type: nuclear-spectroscopy-angular-correlation
tags: [hamilton, angular-distribution, dco, ado, linear-polarization, compton-polarimeter, deorientation, mixing-ratio]
topics: [angular-distribution, dco, linear-polarization, deorientation, experimental-statistics]
sources: [book-hamilton-electromagnetic-interaction, book-wu-nuclear-experiment-methods, book-zhu-probability-statistics-in-physics]
---

# Hamilton 核谱学角分布、DCO、去取向与 Compton 线偏振方法合同

## Purpose

本方法合同绑定 W. D. Hamilton 编《The Electromagnetic Interaction in Nuclear Spectroscopy》（North-Holland 1975）第 12、15 章的选段核验：
定向核态统计张量与角分布/方向角关联、DCO 几何、未观测级联去取向系数、Compton 线偏振相关以及实验误差和固有多解边界。
它服务于在束核谱学中的 $J^\pi$、多极性、混合比 $\delta$ 和摆动候选判别，并要求把理论系数、探测器响应、背景、统计误差和相位约定分开处理。

## Inputs and Assumptions

1. **轴对称定向输入**：在非极化束流、出射粒子未观测或具有绕束流轴圆柱对称的探测几何下，初态定向可由统计张量 $B_k(I_i)$ 描述；反应机制或库仑激发计算提供其取值。
2. **角分布模型**：
   $$W(\theta)=1+A_2P_2(\cos\theta)+A_4P_4(\cos\theta),$$
   其中 $A_k$ 由初态定向张量与跃迁多极几何系数 $R_k(LL'I_iI_f)$ 共同决定。
3. **DCO 几何**：两条级联 $\gamma$ 射线的方向由实验室系中 $(\theta,\phi)$ 指定；DCO 系数依赖探测器固定角度、级联顺序、自旋和多极性，不能只写成一个与几何无关的常数。
4. **Compton 极化响应**：线偏振由相差 $90^\circ$ 的散射计数估计，极化灵敏度 $Q(E_\gamma)$ 与散射体、吸收体、散射角和效率共同决定。

## What It Can Establish

1. **DCO 角关联的几何化表达**：当某一探测器方向固定在 $90^\circ$、$180^\circ$ 或特定环角时，广义方向角关联可化为剩余角度的 Legendre 展开，为 ADO/DCO 比值建立可复核的几何输入。
2. **线偏振与电磁多极性的独立约束**：Hamilton Eq. (15.9) 的偏振角分布含有依赖电/磁辐射的相位因子；在固定相位、极性和几何约定下，偏振可与 DCO 联合区分 $M1$ 与 $E2$ 候选。
3. **Compton 极化测量的响应公式**：
   $$P_\mathrm{exp}(\theta)=\frac{N_\perp-a_\mathrm{geom}N_\parallel}{Q(E_\gamma)[N_\perp+a_\mathrm{geom}N_\parallel]},$$
   其中 $a_\mathrm{geom}$ 由无偏振标准线校准，$Q$ 不能被默认设为理想值。
4. **统计和系统误差预算**：角分布拟合中的净峰计数应包含峰、本底和随机扣除的方差；相对效率、束流能量、靶厚、各向异性和未知定向参数会引入系统误差。Hamilton 给出的示例表明即使每个角度约有千计数，$a_2/a_4$ 误差仍可能达到数个百分点。
5. **固定混合比扫描而非盲目非线性拟合**：由于混合比出现在非线性项中，实践上可对 $\arctan\delta$ 网格扫描，在每个网格点线性拟合定向参数，再比较 $\chi^2$ 或等价统计量。

## What It Cannot Establish Alone

1. **单一角分布不能自动消除双根**：不同 $(J,\delta)$ 组合可能给出相同或近似相同的角分布系数；必须结合线偏振、内转换、寿命、绝对 $B(E2)$/$B(M1)$ 或其它独立观测量。
2. **偏振正负号不是跨实验的无条件标签**：$P$ 的正负依赖散射平面、极性定义、相位约定、$Q$ 校准和背景扣除；不能脱离实验 convention 直接把正号写成 $E2$、负号写成 $M1$。
3. **低统计增加不能保证模型多解消失**：即使将实验时间增加数倍，若不同假设在理论角分布上本征简并，统计误差变小也不能凭空产生独立信息。
4. **定向参数不能被理论默认值替代**：反应机制、feeding 和去取向效应若未约束，固定 $\sigma/I$ 或固定高斯 $m$ 子态分布会把模型不确定性误写成混合比精度。

## Sources

- [[book-hamilton-electromagnetic-interaction]]：Ch. 12, PDF p. 532, 559；Ch. 15, PDF pp. 727–737。
- [[book-wu-nuclear-experiment-methods]]：在束角分布、DCO 与 Compton 极化实验方法。
- [[book-zhu-probability-statistics-in-physics]]：误差传播、非线性拟合与双根判决。
- [[behnke-hep-statistics-and-unfolding-contract]]：区间覆盖、系统误差与展开边界。
- [[experimental-statistics-and-dual-root-determination]]：多极混合比双根与正交实验裁判。
