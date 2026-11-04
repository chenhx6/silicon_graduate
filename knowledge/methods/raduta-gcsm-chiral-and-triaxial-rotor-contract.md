---
type: method
title: "A. A. Raduta 广义相干态模型（GCSM）三轴转子与偶偶核手征对称性方法合同"
aliases: [Raduta-GCSM-contract, Coherent-State-Chirality-contract, GCSM-triaxial-contract]
created: 2026-11-04
updated: 2026-11-04
status: active
review_status: unreviewed
method_type: collective-model-contract
tags: [raduta, coherent-states, gcsm, csm, triaxiality, nuclear-chirality, wobbling, boson-expansion]
topics: [coherent-states, gcsm, triaxiality, nuclear-chirality, wobbling]
sources: [book-raduta-coherent-states, book-petrache-chirality-and-wobbling, book-greiner-nuclear-models]
---

# A. A. Raduta 广义相干态模型（GCSM）三轴转子与偶偶核手征对称性方法合同

## Purpose

本方法合同严格绑定 A. A. Raduta《Nuclear Structure with Coherent States》（Springer 2016）第 4 章与第 10 章（印刷 pp. 75–129, 291–334 / 物理 PDF pp. 82–136, 298–341），
系统形式化非轴对称三轴转子的半经典自旋相干态表示、Holstein-Primakoff 与 Dyson 玻色子展开、倾斜转子相空间轨道量子化，
以及广义相干态模型（Generalized Coherent State Model, GCSM）耦合两准粒子在偶偶核（如 $^{138}\text{Nd}, {}^{130}\text{Ba}$）中诱发宏观手征对称性自发破缺的微观玻色子形式理论（式 10.1.18–10.1.23），
为超越绝热粒子-转子模型（PRM）的三轴集体运动与手征相空间动力学提供严格微观规范。

## Inputs and Assumptions

1. **质子-中子独立四极玻色子场**：分别引入质子与中子四极玻色子创生算符 $b_{p, 2\mu}^\dagger, b_{n, 2\mu}^\dagger$，内禀基态取为投影相干态；
2. **两准粒子微观费米子自由度**：准粒子对（如质子粒子对与中子空穴对）在球形壳层中运动，通过四极-四极相互作用与自旋-自旋力耦合到 GCSM 核芯（式 10.1.18）：
   $$H = H_{\text{GCSM}} + \sum_\alpha \epsilon_a c_\alpha^\dagger c_\alpha - \frac{G}{4} P^\dagger P - \sum_{\tau=p,n} X_{\text{pc}}^{(\tau)} \sum_m q_{2m} [b_{\tau,-m}^\dagger + (-)^m b_{\tau m}] (-)^m - X_{sS} \vec{J}_F \cdot \vec{J}_c$$
3. **角动量三维投影规范**：通过对欧拉角空间严格对易积分算符 $\hat{P}_{MK}^I = \frac{2I+1}{8\pi^2} \int D_{MK}^{I*}(\Omega) \hat{R}(\Omega) d\Omega$，从非轴对称内禀相干态中精确提取实验室系好自旋与好宇称态；
4. **自洽电磁跃迁算符一致性**：电四极算符 $Q_{2m}$ 与磁偶极算符 $\mathcal{M}_{1m}$ 不采用唯象常数截断，而是直接由模型哈密顿量导出正则对易运动方程确定。

## What It Can Establish

1. **偶偶核手征双重带（Chiral Bands in Even-Even Nuclei）的微观微扰基底**：
   - 将两准粒子态 $(a_j^\dagger a_j^\dagger)_J$ 与具有确定非轴对称形变的质子-中子玻色子相干态 $\phi_{J'}^{(1)}$ 矢量耦合（式 10.1.22）：
     $$\Psi_{JI; M}^{(2\text{qp}; J_1)} = N_{JI}^{(2\text{qp}; J_1)} \sum_{J'} C_{J 1 J+1}^{J J' I} \frac{1}{N_{J'}^{(1)}} [ (a_j^\dagger a_j^\dagger)_J |\text{BCS}\rangle \otimes \phi_{J'}^{(1)} ]_{IM}$$
   - 证明质子变形 $d_p$ 与中子变形 $d_n$ 的非对称性导致质子与中子玻色子角动量矢量取向正交，自然形成相互垂直的角动量三脚架几何；
2. **半经典非轴对称转子相空间极值与分离线（Separatrix）**：
   - 经典正则坐标 $(\theta, \phi)$ 上的相空间轨迹由能量守恒方程唯一限制，存在分界周期轨道与渐近发散的分离线：$(1-u)(1-v^2)(v^2-u^2)(v^2-u) = 0$；
   - 严格区分出环绕主惯量轴的小振幅稳态进动（对应量子摆动运动）与跨越势垒的大振幅手征分岔相；
3. **磁偶极 $M1$ 跃迁强度的解析解耦**：
   - 导出内禀磁矩跃迁矩阵元在手征简并点处的退化结构，证明带间 $M1$ 强度直接反映了左手态与右手态在玻色子角动量相空间中的干涉重叠。

## What It Cannot Establish Alone

1. **玻色子截断对超高自旋能带的饱和偏差**：GCSM 基于有限玻色子数展开，在极高自旋区（$I \ge 24\hbar$）会受到玻色子有限数效应的代数挤压，高自旋带交叉回弯需耦合更高阶准粒子截断；
2. **纯唯象形变参数的自洽性**：相干态变形参数 $d_p, d_n$ 通常由低激发能级（$E(2^+)$）拟合确定，不能自动替代微观自洽协变密度泛函（CDFT）的绝对总能极小化计算；
3. **$\gamma$ 势能深度的绝热假定**：相干态模型假定原子核沿基态谷具有固定形变参量，在处理浅势垒大振幅软核振动时需结合五维微观宏观 Bohr 哈密顿量。

## Sources

- [[book-raduta-coherent-states]]：Chapters 4 & 10 (印刷 pp. 75–129, 291–334 / PDF pp. 82–136, 298–341).
- [[book-petrache-chirality-and-wobbling]]：Chapter 8 GCSM for Nuclear Chirality (A. A. Raduta et al.).
- A. A. Raduta et al., Phys. Rev. C 65, 064322 (2002); Phys. Rev. C 69, 064321 (2004).
- [[coherent-state-model-and-semiclassical-triaxiality]]：相干态模型与半经典三轴性.
- [[chiral-geometry-tilted-axis-cranking-and-aplanarity]]：手征几何与倾斜轴推转动力学.
