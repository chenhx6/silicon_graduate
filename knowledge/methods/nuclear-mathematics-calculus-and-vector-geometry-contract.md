---
type: method
title: "核物理微积分几何、矢量代数与连续流体力学方法合同"
aliases: [Nuclear-mathematics-contract, Vector-geometry-calculus-contract, Tongji-math-physics-contract]
created: 2026-11-04
updated: 2026-11-04
status: active
review_status: unreviewed
method_type: mathematical-physics-contract
tags: [higher-mathematics, vector-algebra, scalar-triple-product, lagrange-multipliers, volume-integrals, stokes-theorem, irrotational-flow]
topics: [vector-algebra, multivariable-calculus, surface-integrals, stokes-theorem, irrotational-flow]
sources: [book-tongji-higher-mathematics-vol2, book-bohr-mottelson-nuclear-structure-vol2, book-greiner-nuclear-models]
---

# 核物理微积分几何、矢量代数与连续流体力学方法合同

## Purpose

本方法合同严格绑定同济大学数学系《高等数学（第七版下册）》（高等教育出版社 2014）第 8–11 章（物理 PDF pp. 8–257），
系统形式化矢量标量三重积在空间角动量三面体手征体积度规中的行列式定义（式 8.12）、
Lagrange 条件极值乘子法在约束形变自洽势能曲面极小化搜索中的应用（式 9.28）、
球坐标三重积分在四极电四极矩 $Q_0$ 与均方根半径微积分反演中的算法、
以及基于斯托克斯定理（Stokes Theorem）在无旋流条件 $\nabla \times \vec{v} = 0$ 下微观推导 Bohr-Mottelson 液体流转动惯量 $\mathcal{J}_k(\beta, \gamma)$，
为低能核结构集体模型、手征几何分析与势能面计算提供严密的第一性微积分数学基础。

## Inputs and Assumptions

1. **三维欧氏空间笛卡尔与曲线正交坐标系**：内禀主轴坐标系取为右手正交笛卡尔标架 $(x, y, z)$，球坐标变换满足 $x = r \sin\theta \cos\phi, y = r \sin\theta \sin\phi, z = r \cos\theta$；
2. **表面边界单值闭合假设**：核表面半径 $R(\theta, \phi) = R_0 [1 + \sum \alpha_{\lambda\mu} Y_{\lambda\mu}^*]$ 为连续二阶可微函数，围成凸体积；
3. **连续核物质流体假设**：核电荷流与质量流在宏观尺度近似为不可压缩连续流体（$\nabla \cdot \vec{v} = 0$）；
4. **光滑势能泛函极小化条件**：势能曲面 $E(\beta, \gamma, \dots)$ 在参数网格内连续二阶可导，Hessian 矩阵正定确立稳定平衡形变。

## What It Can Establish

1. **手征三维角动量体积度规的严格行列式定义（式 8.12）**：
   $$\mathcal{V} = \vec{j}_p \cdot (\vec{j}_n \times \vec{R}) = \begin{vmatrix} j_{px} & j_{py} & j_{pz} \\ j_{nx} & j_{ny} & j_{nz} \\ R_x & R_y & R_z \end{vmatrix}$$
   - 行列式值为正对应右手三面体，值为负对应左手三面体，值为零严格对应角动量共面退化（Planar degenerate state）；
   - 证明空间旋转不变性：任意正交坐标旋转矩阵 $\mathbf{O} \in SO(3)$ 保持 $\det(\mathbf{O}) = +1$，手征体积度规 $\mathcal{V}$ 在全空间旋转下严格保持标量不变性；
2. **受约束微观泛函的 Lagrange 乘子法方程（式 9.28）**：
   $$\frac{\partial}{\partial q_i} \left[ E(q_1, \dots, q_n) - \lambda_Q \langle \hat{Q}_{20} \rangle - \lambda_\gamma \langle \hat{Q}_{22} \rangle \right] = 0$$
   给出了微观约束推转自洽场中提取固定形变网格点 $(\beta_2, \gamma)$ 能量的微积分极值保证；
3. **电四极矩 $Q_{20}$ 与质量转动惯量重积分转换**：
   $$Q_0 = \frac{1}{e} \iiint \rho(r, \theta, \phi) (2z^2 - x^2 - y^2) dV = \sqrt{\frac{16\pi}{5}} \int_0^{2\pi} d\phi \int_0^\pi \sin\theta d\theta \int_0^{R(\theta,\phi)} \rho_0 r^4 Y_{20}(\theta, \phi) dr$$
   精确给出展开到二阶的形变几何系数 $Q_0 \approx \frac{3}{\sqrt{5\pi}} Z R_0^2 \beta_2 [1 + 0.16 \beta_2]$；
4. **基于斯托克斯公式推导无旋流转动惯量定理**：
   - 无旋流条件 $\nabla \times \vec{v} = 0 \implies \vec{v} = \nabla \Phi$，连续性方程 $\nabla^2 \Phi = 0$；
   - 结合表面运动边界条件 $v_n = \dot{R}(\theta, \phi)$ 求解速度势 $\Phi$；
   - 积分全流体动能 $T = \frac{1}{2} \rho_0 \iiint (\nabla\Phi)^2 dV = \frac{1}{2} \sum \mathcal{J}_k \Omega_k^2$，微观形式严格导出 Bohr 四极流体惯量：
     $$\mathcal{J}_k = 4 B \beta^2 \sin^2\left(\gamma - k \frac{2\pi}{3}\right) \quad (k = 1, 2, 3)$$

## What It Cannot Establish Alone

1. **不可描述微观壳效应引发的惯量反常**：流体无旋流公式预测惯量严格正比于 $\beta^2$，比实验刚体测量值低估近 2–3 倍，必须结合微观 BCS 准粒子配对因子的 Inglis cranking 公式进行重整化；
2. **费米子交换能与反对称泡利原理**：经典微积分对质点质量元 $dm = \rho dV$ 积分，无法反映同一相空间量子态中同类费米子由于泡利阻塞带来的排斥动能；
3. **大振幅隧穿过程中的非经典几何路径**：经典微积分极小化仅适用于寻找局域稳态，在穿越手征势垒或裂变势垒的穿隧动作中，必须借助虚时间欧氏空间瞬子（Instanton）积分。

## Sources

- [[book-tongji-higher-mathematics-vol2]]：第八章 §2，第九章 §8，第十章 §3–4，第十一章 §6–7.
- [[book-bohr-mottelson-nuclear-structure-vol2]]：App. 6B 液体无旋流转动惯量推导.
- [[chiral-geometry-tilted-axis-cranking-and-aplanarity]]：手征角动量几何与体积度规.
- [[cranked-triaxial-shape-coexistence-pes]]：推转三轴形变共存势能面.
