---
type: model
title: 准粒子-声子模型（QPM）
aliases: [QPM, quasiparticle phonon model, Soloviev phonon model]
created: 2026-11-06
updated: 2026-11-06
status: active
review_status: unreviewed
model_family: microscopic-vibrational-model
degrees_of_freedom: [quasiparticles, random-phase-phonons]
parameters: [woods-saxon-potential, pairing-monopole, separable-multipole-forces]
tags: [phonons, octupole-vibration, giant-resonance, scissors-mode, qrpa]
---

# 准粒子-声子模型（Quasiparticle-Phonon Model, QPM）

## Purpose

准粒子-声子模型由 V. G. Soloviev 及杜布纳学派创立，用于微观描述中重原子核从低激发离散振动态到高激发巨共振态的精细结构。QPM 特别擅长处理八极振动态（$3^-$ 状态与八极软核）、磁偶极剪刀模式（Scissors Mode）以及电偶极（$E1$）光核吸收截面中的微观声子劈裂机制。

## Hamiltonian or Core Formalism

哈密顿量由单粒子平均场、单极配对力以及可分离多极/自旋-多极残余相互作用组成：
$$H = H_{\text{sp}} + H_{\text{pair}} + H_M + H_{SM}$$

在 Bogoliubov 变换引入准粒子后，构建准粒子无规相位近似（QRPA）声子产生算符：
$$Q^\dagger_{\lambda \mu i} = \frac{1}{2} \sum_{j j'} \left[ \psi^{\lambda i}_{j j'} [\alpha^\dagger_j \times \alpha^\dagger_{j'}]^{(\lambda)}_\mu - \varphi^{\lambda i}_{j j'} [\alpha_{\tilde{j}} \times \alpha_{\tilde{j}'}]^{(\lambda)}_\mu \right]$$

### 广义波函数展开
偶偶核波函数不仅包含单声子态，还显式包含两声子和三声子耦合组态：
$$| \Psi_\nu(J M) \rangle = \left\{ \sum_i R_i(J) Q^\dagger_{J M i} + \sum_{\lambda_1 i_1 \lambda_2 i_2} P^{\lambda_1 i_1}_{\lambda_2 i_2}(J) [Q^\dagger_{\lambda_1 i_1} \times Q^\dagger_{\lambda_2 i_2}]^{(J)}_M + \dots \right\} | 0 \rangle_{\text{ph}}$$

准粒子-声子相互作用将简单的 QRPA 纯单声子态强度碎裂（Fragmentation）到复杂的两声子乃至连续谱背景态中。

## Application to Octupole and Rare Decays

1. **八极集体态（$3_1^-$）**：微观计算表明，八极声子主要由 $\Delta l = 3, \Delta j = 3$ 轨道对相干驱动，QPM 能定量给出 $B(E3; 3_1^- \to 0_1^+)$ 的集体增强倍数（达 20–50 W.u.）；
2. **双八极双声子态（Two-Phonon Octupole Quartet）**：预测 $[3^- \otimes 3^-]$ 产生的 $0^+, 2^+, 4^+, 6^+$ 四重态的非谐振能量劈裂与电磁衰变分支；
3. **低能矮电偶极共振（Pygmy Dipole Resonance, PDR）**：精确区分中子皮多余中子振动引发的软 $E1$ 模式与巨偶极共振（GDR）尾部。

## Boundary and Failure Domain

- **大四极变形转动带受限**：QPM 以球形或轴对称准粒子为基底，对强三轴非轴对称高自旋转动带（如 wobbling 与手征双带）的描述显著劣于粒子-转子模型（PRM）和倾斜轴推转模型（TAC）；
- **微观相互作用可分离近似**：为了数值可解性，QPM 普遍采用多极可分离相互作用（Separable Forces），略去了真实两体有效相互作用中复杂的多体张量非局域关联。
