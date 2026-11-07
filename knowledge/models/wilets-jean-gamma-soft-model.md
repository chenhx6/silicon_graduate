---
type: model
title: Wilets-Jean 伽马不稳定模型
aliases: [Wilets-Jean model, gamma-unstable model, O(5) limit, gamma-soft rotor]
created: 2026-11-06
updated: 2026-11-06
status: active
review_status: unreviewed
model_family: collective-bohr-hamiltonian
degrees_of_freedom: [collective-beta, collective-gamma, euler-angles]
parameters: [beta-stiffness, mass-parameter]
tags: [gamma-softness, o5-symmetry, o6-ibm, davydov-comparison, triaxiality]
---

# Wilets-Jean 伽马不稳定模型（Wilets-Jean $\gamma$-Unstable Model）

## Purpose

由 L. Wilets 与 M. Jean 于 1956 年提出，该模型是研究原子核**完全 $\gamma$ 不稳定（$\gamma$-Softness / $\gamma$-Unstable）**动力学的经典宏观集体模型。它在五维 Bohr 哈密顿量中假定集体势能完全独立于不对称度参数 $\gamma$（即在内禀形状平面上具有完美的圆对称势阱），代表着集体模型中具有五维转动对称性 $O(5)$ 的严格解析极限，对应于相互作用玻色子模型（IBM-1）的 $O(6)$ 动力学对称性。

## Hamiltonian or Core Formalism

在 Bohr-Mottelson 坐标下，当势能仅为 $\beta$ 的函数 $V(\beta, \gamma) = V(\beta)$ 时，微观集体哈密顿量为：
$$H = -\frac{\hbar^2}{2B} \left[ \frac{1}{\beta^4} \frac{\partial}{\partial \beta} \beta^4 \frac{\partial}{\partial \beta} + \frac{1}{\beta^2} \Lambda^2 \right] + V(\beta)$$
其中 $\Lambda^2$ 为五维角动量卡西米尔（Casimir）算符：
$$\Lambda^2 = -\frac{1}{\sin 3\gamma} \frac{\partial}{\partial \gamma} \sin 3\gamma \frac{\partial}{\partial \gamma} + \sum_{k=1}^3 \frac{I'_k^2}{4 \sin^2(\gamma - \frac{2\pi}{3}k)}$$

$\Lambda^2$ 的本征值为 $\tau(\tau+3)$，其中 $\tau = 0, 1, 2, \dots$ 为 $O(5)$ 高度对称性量子数（常称作 Seniority 玻色子类似物）。

## Energy Multiplets and Decay Rules

能级结构完全按 $\tau$ 多重态聚集：
- $\tau = 0$：基态 $0_1^+$；
- $\tau = 1$：单重态 $2_1^+$；
- $\tau = 2$：双重态 $(4_1^+, 2_2^+)$，能量严格简并：$E(4_1^+) = E(2_2^+)$；
- $\tau = 3$：三重态 $(6_1^+, 4_2^+, 3_1^+)$，能量严格简并且满足：$E(3_1^+) \approx E(4_1^+) + E(2_1^+)$；
- $\tau = 4$：包含 $(8_1^+, 6_2^+, 5_1^+, 4_3^+, 2_3^+)$。

### 电磁跃迁选择定则
由于电四极算符 $T(E2) \propto \beta$ 表现为 $\tau$ 改变 1 的张量，导致严格的跃迁禁戒定则：
$$\Delta \tau = \pm 1$$
这决定了：
- 允许跨带跃迁：$B(E2; 2_2^+ \to 2_1^+) > 0$；
- 严格禁戒跃迁：$B(E2; 2_2^+ \to 0_1^+) \equiv 0$（因为 $\Delta \tau = 2$ 禁戒）。

## Critical Diagnostic: Wilets-Jean vs. Davydov Rigid Rotor

在实验能谱上区分究竟是**大振幅 $\gamma$ 涨落的软核（Wilets-Jean）**还是**具有稳定三轴形变的刚性转子（Davydov-Filippov）**，核心判据如下：

| 物理量 / 检验指标 | Wilets-Jean $\gamma$-软核极限 | Davydov 刚性三轴转子（$\gamma = 30^\circ$） |
| :--- | :--- | :--- |
| **能量相对位置** | $E(2_2^+) \approx E(4_1^+)$ | $E(2_2^+) \approx E(4_1^+)$ |
| **三态能量求和恒等式** | $E(2_1^+) + E(2_2^+) \ne E(3_1^+)$ | **$E(2_1^+) + E(2_2^+) \equiv E(3_1^+)$（严格求和守恒）** |
| **交叉 $E2$ 衰变分支** | $B(E2; 2_2^+ \to 0_1^+) \equiv 0$ | $B(E2; 2_2^+ \to 0_1^+) \ne 0$（有限小分支） |
| **四极不变量方差** | $\sigma^2(\cos 3\gamma) = \langle \cos^2 3\gamma \rangle \approx 0.5$（大涨落） | $\sigma^2(\cos 3\gamma) \to 0$（严格局域在 $\gamma_0$） |

## Boundary and Failure Domain

- **不适用于稳定长椭或扁椭转子**：当核由于微观壳效应在特定 $\gamma$ 处（如 $\gamma = 0^\circ$ 或 $20^\circ$）具有深能量极小时，$V(\gamma)$ 不能略去，哈密顿量退化为转动-振动耦合模型（RVM）或刚性转子；
- **无法产生手征双重带与摆动运动**：$\gamma$-软核由于内禀轴定义模糊且具有大振幅动力学涨落，无法维持稳定的刚性三维角动量几何三脚架，因此不能产生真正的横向摆动运动与稳定的手征进动。
