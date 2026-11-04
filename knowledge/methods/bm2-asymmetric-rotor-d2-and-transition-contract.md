---
type: method
title: "Bohr–Mottelson Vol. II：非轴对称转子的 D2 对称性、轨迹与 E2 连接"
aliases: [BM-II D2 asymmetric rotor, Regge trajectories asymmetric rotor, non-axial rotor transition contract]
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
method_type: "asymmetric-rotor-symmetry-and-transitions"
scope: "Selected rendered verification of BM-II §4-5a-e, PDF pp. 197, 199, 201, 205, 207, 209, 211-218"
confidence: "high for the displayed equations and selected-page boundaries"
tags: [bohr-mottelson, asymmetric-rotor, d2-symmetry, regge-trajectories, e2-transitions, triaxiality]
sources: [book-bohr-mottelson-nuclear-structure-vol2]
---

# Bohr–Mottelson Vol. II：非轴对称转子的 D2 对称性、轨迹与 E2 连接

## Purpose

非轴对称转子没有轴对称转子的严格 \(K\) 守恒量。BM-II §4-5e 的页面把这一点
具体化为：

```text
D2 对称性块
-> K 与相位分量混合
-> 非轴对称能级轨迹
-> yrast/高能极限的近似单轴运动
-> E2 强级联与较弱跨轨迹连接
```

## Inputs and Assumptions

- 三个主轴的转动参数按 \(A_1<A_2<A_3\) 标记；
- 对偶偶核保留 \(D_2\) 对称性量子数和相位约束；
- 在给定 \(I\) 的 \(\vert K\rangle\) 表象中，非轴对称项连接 \(K\) 与 \(K+2\)；
- 高自旋极限可以用 yrast 或最高能量附近的渐近展开，但有限 \(I\) 需要矩阵对角化；
- “轨迹编号 \(K\)”在非轴对称情形是解的排序/延拓标签，不等同于轴对称极限中
  的严格内禀 \(K\) 量子数。

## What It Can Establish

### General finite-spin Hamiltonian and \(D_2\)

For a time-reversal-invariant non-axial intrinsic state, BM-II writes the leading rotor
Hamiltonian as
\[
H_{\rm rot}=\sum_{k=1}^3 A_k I_k^2,\qquad
A_k=\frac{\hbar^2}{2\mathcal J_k}.
\]
With intrinsic \(D_2\) symmetry, rotations by \(\pi\) about the three principal axes
produce commuting symmetry blocks for even-\(A\) systems. The state labels \(r_k\) constrain
which \(K\)-components can mix. For odd-\(A\) systems the intrinsic states are Kramers
doublets and the particle-rotor Hamiltonian becomes a matrix in the conjugate intrinsic
space.

When two moments of inertia are nearly equal, the spectrum can be organized approximately
by a \(K\)-like label and an effective \(\Delta K=2\) coupling. BM-II explicitly warns that
observed higher-order rotational coefficients need not be explained by a small static
asymmetry alone; couplings to other modes can have similar effects.

BM-II PDF p. 195 的矩阵元结构可写成对角项和 \(K\leftrightarrow K+2\) 的非对角项；
其 \(D_2\) 关系把相位量子数、\(r_i\) 和 \(I,K\) 的奇偶结构联系起来。对固定
惯量比，能量本征值可以视为连续 \(I\) 参数的轨迹；物理整数/半整数自旋态来自
满足共同对称性量子数的轨迹交点。

在 \(A_3\) 为最大或最小惯量参数的情形，渐近递推根为实数并可选出离散本征值；
中间轴表象的递推根可落在单位圆上，解析延拓表现为连续谱结构。这是数学轨迹
分析的条件性结果，不能直接当作实验连续能谱。

在高自旋 yrast 区，原书把不同轨迹解释为：

- 沿同一 \(n\) 轨迹的强 E2 转动序列；
- 连接不同 \(n\) 轨迹的较弱 E2 过渡；
- 在轴对称极限恢复熟悉的 \(K\) 标签和转动带图像。

## Discriminating Observables

- 对同一母态的带内/跨轨迹 \(B(E2)\) 比；
- 轨迹能量随 \(I\) 的排序和 avoided/crossing 结构；
- \(D_2\) 对称性允许的自旋、相位和 signature；
- 主轴约定下 \(Q_0,Q_2\) 对 E2 矩阵元的贡献；
- 与粒子-转子、QTR/TAC 或 TPSM 计算在未用于拟合的连接跃迁上的比较。

## What It Cannot Establish Alone

一个 \(K\)-like 能级标签、等间隔能级或强 E2 带内跃迁不能单独证明静态三轴形变、
wobbling phonon、TiP 或 chirality。BM-II 选段是转子模型 benchmark；实验模式判断
还需要有限自旋、准粒子、feeding、寿命、偏振和完整响应。

## Counter-evidence and Competing Interpretations

- 非轴对称转子的轨迹交点和能级混合可能与多带 Coriolis 混合、\(\gamma\) 振动或
  configuration mixing 产生类似能级模式；
- 在 \(I\) 不够大或惯量接近简并时，谐近似失效，强度比例不应使用高自旋公式；
- 不同文献把 \(1,2,3\) 轴标成 \(s,m,l\) 的顺序可能相反，必须先转换 \(A_k\) 和
  \(\mathcal J_k\)；
- E2 连接弱并不自动代表实验不可见；效率、门条件、feeding 和统计误差同样影响
 观测强度。

## Model Dependence

```text
finite asymmetric rotor matrix
-> D2 blocks and eigenstates
-> high-I asymptotic expansion
-> E2 operator in Q0/Q2 convention
-> detector-corrected transition observables
```

任何实际核素计算都需要声明采用的是完整有限矩阵、谐近似、冻结准粒子粒子-转子
还是其它模型。

纯有限自旋 benchmark 已实现于
`system/scripts/analysis/bm2_asymmetric_rotor_matrix_diagonalizer.py`：它在完整
\(\vert I,K\rangle\) 表象中对角化，并返回 trace check、能级和轴约定；该模块与奇
\(A\) PTRM 代码分开，避免把纯转子与粒子-转子哈密顿量混用。

## Limitations and Missing Evidence

本页核对 BM-II §4-5a–e 的选定页面（PDF pp. 197, 199, 201, 205, 207, 209, 211–218）；
未完成第 4 章全部非轴对称转子例题、
Regge 图完整复现、附录和现代有限自旋 QTR 比较。当前没有把该页转成自动模式分类器。

## Sources

- [[book-bohr-mottelson-nuclear-structure-vol2]]
- [[bm2-high-spin-asymmetric-rotor-e2-contract]]
- [[bm2-particle-rotor-adiabatic-coriolis-contract]]
- [[nuclear-chirality-and-wobbling-triaxial-foundations]]
- [[tanabe-top-on-top-algebraic-wobbling-contract]]：Tanabe 在 Petrache 专著 Ch.4 详尽澄清了 BM-II 式 (4-282) 与图 4-33 在惯量排序与 κ 对应上的印刷错误，并建立了保持 D2 对称性的 Top-on-Top 代数次领头阶展开。
