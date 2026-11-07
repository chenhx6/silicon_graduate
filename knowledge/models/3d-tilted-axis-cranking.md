---
type: model
title: 三维倾斜轴推转模型（3D-TAC）
aliases: [3D-TAC, 3D tilted axis cranking, three-dimensional cranking, aplanar cranking]
created: 2026-11-06
updated: 2026-11-06
status: active
review_status: unreviewed
model_family: self-consistent-cranking-model
degrees_of_freedom: [single-particle, rotational-orientation-angles]
parameters: [deformation-beta, deformation-gamma, rotational-frequency, tilt-angles-theta-phi]
tags: [chirality, aplanar-rotation, triaxiality, spontaneous-symmetry-breaking]
---

# 三维倾斜轴推转模型（3D Tilted Axis Cranking, 3D-TAC）

## Purpose

三维倾斜轴推转模型由 Frauendorf 与孟杰等人（1997）发展，用于在微观自洽平均场框架下描述原子核在三维欧几里得空间中的**非平面（Aplanar）倾斜轴转动**。它是微观解释原子核手征对称性自发破缺（Nuclear Chirality）与手征双重带（M$\chi$D）的最核心自洽微观理论。

## Hamiltonian or Core Formalism

在随动三轴内禀坐标系（主轴为 $x, y, z$）中，转动角速度矢量 $\vec{\omega}$ 在球坐标下由极角 $\theta$ 和方位角 $\phi$ 参数化：
$$\vec{\omega} = \omega (\sin\theta \cos\phi\, \vec{e}_x + \sin\theta \sin\phi\, \vec{e}_y + \cos\theta\, \vec{e}_z)$$

对应的推转 Routhian 单粒子哈密顿量为：
$$h' = h_{\text{def}} - \vec{\omega} \cdot \vec{j} = h_{\text{def}} - \omega (j_x \sin\theta \cos\phi + j_y \sin\theta \sin\phi + j_z \cos\theta)$$

体系总能量或总 Routhian 是角度 $(\theta, \phi)$ 的函数：
$$E(\theta, \phi; J) = \langle \Phi(\theta, \phi) | H | \Phi(\theta, \phi) \rangle$$
约束条件为总角动量模长匹配 $\langle \vec{J} \rangle^2 = J(J+1)$。

## Physical Mechanism for Chirality

在三轴奇奇核中（典型构型如 $\pi h_{11/2} \otimes \nu h_{11/2}^{-1}$）：
1. 质子准粒子（处于壳层底部，表现为粒子型）沿内禀短轴（$s$ 轴，通常取为 $x$ 轴）取向；
2. 中子准粒子（处于壳层顶部，表现为空穴型）沿内禀长轴（$l$ 轴，通常取为 $z$ 轴）取向；
3. 三轴变形核芯由于中间轴（$m$ 轴，通常取为 $y$ 轴）具有最大转动惯量（$\mathcal{J}_m$），转动角动量倾向于沿中间轴；
4. 质子、中子与核芯转动三个矢量相互垂直，构成**空间三面体（Chiral Trihedron）**。

当总角动量脱离任何主平面（即 $\theta \ne 0, \pi/2$ 且 $\phi \ne 0, \pi/2$）时，体系在时间反演 $\mathcal{T}$ 与空间转动 $\mathcal{R}(\pi)$ 的联合操作下具有手征性，自发破缺为互为镜像对称的左手系与右手系，能量极小在势能面 $E(\theta, \phi)$ 上表现为两个简并的非平面极小点。

## Degrees of Freedom and Assumptions

- **自由度**：准粒子在变形平均场中的独立运动，以及角动量矢量在内禀系中的空间指向取向 $(\theta, \phi)$；
- **关键假设**：角动量矢量在内禀系中具有明确的半经典取向；假设高自旋下转动自由度与内禀激发解耦。

## Boundary and Failure Domain

- **经典破缺 vs 量子穿透**：3D-TAC 是平均场半经典模型，只能预测非平面势能面极小的出现（自发破缺），但**不能给出有限核中左手与右手简并态之间的量子隧穿能量劈裂 $\Delta E(I)$**；
- **静态近似局限**：在势垒较低或低自旋平面相向手征相过渡区，必须引入三维转动投影（3D-AMP）或倾斜轴推转加无规相位近似（TAC+RPA），否则无法计算实验室系下的实验室多极电磁跃迁率 $B(M1)$ 与 $B(E2)$。
