---
type: observable
title: 内禀电偶极矩（|D_0|）
aliases: [intrinsic electric dipole moment, D0, octupole dipole moment]
created: 2026-11-06
updated: 2026-11-06
status: active
review_status: unreviewed
observable_kind: intrinsic-electromagnetic-moment
symbol: |D_0|
units: e*fm
tags: [octupole, reflection-asymmetry, e1-transition, parity-doublets]
---

# 内禀电偶极矩（Intrinsic Electric Dipole Moment, $|D_0|$）

## Definition

在具有静态八极形变（梨形形变，$\beta_3 \ne 0$）或动态八极关联的原子核内禀坐标系中，质子电荷质心与中子质量质心之间的空间分离所诱发的宏观电偶极矩。它是实验判定原子核空间反射对称性（宇称 $\mathcal{P}$）是否发生自发破缺的最关键物理观测量。

## Formula and Extraction Method

在交替宇称带（Alternating Parity Bands）中，高激发态既通过带内电四极（$E2$）跃迁退激，也通过跨带偶极（$E1$）跃迁退激。实验上通过测量分支强度比 $I_\gamma(E1)/I_\gamma(E2)$，提取约化跃迁几率比值：
$$\frac{B(E1; I \to I-1)}{B(E2; I \to I-2)} = \frac{I_\gamma(E1)}{I_\gamma(E2)} \cdot \left( \frac{E_\gamma(E2)}{E_\gamma(E1)} \right)^5 \cdot \frac{1 + \alpha(E2)}{1 + \alpha(E1)}$$

基于转子模型（Rotor Model）几何矩阵元，内禀电偶极矩 $|D_0|$ 与内禀电四极矩 $Q_0$ 的代数比值为：
$$\frac{B(E1; I \to I-1)}{B(E2; I \to I-2)} = \frac{8}{5} \frac{\langle I 0 1 0 | I-1 0 \rangle^2}{\langle I 0 2 0 | I-2 0 \rangle^2} \frac{D_0^2}{Q_0^2} = \frac{8}{5} \frac{2I-1}{I-1} \frac{D_0^2}{Q_0^2}$$

由此得到内禀电偶极矩提取公式：
$$|D_0| = \sqrt{ \frac{5}{8} \frac{I-1}{2I-1} \cdot Q_0^2 \cdot \frac{B(E1)}{B(E2)} }$$

## Physical Mechanisms: Macroscopic vs. Microscopic

1. **宏观液滴模型（LDM）极化效应**：经典均匀液滴因电荷再分布产生极小负偶极矩；
2. **微观壳效应（Shell Correction）**：费米面附近具有强八极耦合的轨道对（如质子 $1d_{5/2} \leftrightarrow 1h_{11/2}$ 与中子 $2f_{7/2} \leftrightarrow 1i_{13/2}$）诱发的非对称核子空间波函数重组，往往在 $A \sim 140\text{--}150$ 钡-铈区产生异常巨大的内禀电偶极矩（$|D_0| \sim 0.1 \sim 0.4\text{ }e\cdot\text{fm}$）；
3. **与巨偶极共振（GDR）的相干混合**：低能内禀八极态通过剩余库仑和同位旋相互作用与高能等矢巨偶极共振尾部相干杂化。

## Boundary and Interpretation Caveats

- **$D_0$ 的符号不确定度**：由于分支比仅依赖跃迁几率模方，实验直接测量的永远是 $|D_0|$。若要测定符号，必须借助库仑激发中 $E1$ 与高阶多极矩阵元之间的量子干涉效应；
- **不能孤立推断刚性八极形变**：仅有较大的 $|D_0|$ 并不足以严格证明基态具有静态梨形形变，大振幅八极振动（Octupole Vibration）同样可以导致瞬时增强的 $E1$ 跃迁；必须同时配合交替宇称能级交错参数 $\Delta E(I) \to 0$ 与绝对 $B(E3)$ 测量。
