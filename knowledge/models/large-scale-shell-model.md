---
type: model
title: 大规模微观壳模型（LSSM）
aliases: [LSSM, large-scale shell model, exact shell model, ANTOINE, NuShellX, KSHELL]
created: 2026-11-06
updated: 2026-11-06
status: active
review_status: unreviewed
model_family: configuration-interaction-model
degrees_of_freedom: [valence-nucleons, m-scheme-slater-determinants]
parameters: [single-particle-energies, two-body-effective-matrix-elements]
tags: [shell-model, m-scheme, lanczos, tensor-force, shell-evolution]
---

# 大规模微观壳模型（Large-Scale Shell Model, LSSM）

## Purpose

大规模组态相互作用微观壳模型是低能核结构微观理论的第一性黄金标准。它在选定的价核子模型空间（Model Space）内，利用 Lanczos 迭代算法在包含数亿至百亿维度的 $M$-scheme Slater 行列式基底下精确对角化有效哈密顿量，用于研究原子核结合能、能级谱学、单极张量力驱动的壳演化、Gamow-Teller $\beta$ 衰变强度与无中微子双贝塔衰变（$0\nu\beta\beta$）核矩阵元。

## Hamiltonian or Core Formalism

在价空间中，有效哈密顿量包含单体项与剩余两体有效相互作用（TBME）：
$$H_{\text{eff}} = \sum_i \epsilon_i c^\dagger_i c_i + \frac{1}{4} \sum_{ijkl} \langle ij | V_{\text{eff}} | kl \rangle c^\dagger_i c^\dagger_j c_l c_k$$

### 单极-多极分解与 Otsuka 单极张量相互作用
两体相互作用可以精确分解为球形单极项（Monopole）与多极相互作用项（Multipole）：
$$V_M(j_a, j_b) = \frac{\sum_J (2J+1) \langle j_a j_b | V | j_a j_b \rangle_J}{\sum_J (2J+1)}$$

Otsuka 等人指出，核力的张量分量通过单极项产生强烈的自旋-同位旋依赖：
- 当质子填充 $j_> = l + 1/2$ 轨道时，对中子 $j'_< = l' - 1/2$ 轨道产生强吸引，对中子 $j'_> = l' + 1/2$ 产生排斥；
- 该机制是解释 A~130 区域中质子 $\pi h_{11/2}$ 填充如何引起中子有效单粒子能（ESPE）漂移并驱动形变演化的微观根源。

## Computation Architecture

主流计算平台包括：
- **ANTOINE / NATHAN**（E. Caurier 等）：采用质子-中子分解存储系数；
- **NuShellX**（W. D. M. Rae, B. A. Brown）：支持大规模自动 $J$-投影与跃迁算符计算；
- **KSHELL**（清水则孝等）：高度并行的混合 MPI/OpenMP GPU 加速 Lanczos 求解器；
- **BIGSTICK**（C. W. Johnson 等）：因数分解算法优化存储。

## Boundary and Failure Domain

- **指数墙（Exponential Wall）**：基矢维度随价核子数与轨道数呈组合爆炸式增长。在 A~130 区域，完全开放整个 $50\text{--}82$ 质子与中子主壳（含 $1g_{7/2}, 2d_{5/2}, 2d_{3/2}, 3s_{1/2}, 1h_{11/2}$）对于双奇核或中间形变核超出当代计算机内存极限；
- **必须的有效电荷**：由于高阶组态截断，必须采用经验有效电荷（$e_p \approx 1.5e, e_n \approx 0.5e$）以补偿核芯极化效应；
- **连续谱与滴线弱束缚**：标准 LSSM 假定束缚态谐振子基，在质子或中子滴线区无法自洽描述晕核与共振态。
