---
type: concept
title: "原子核形状共存、四极形变突变与电单极（E0）跃迁动力学"
aliases: [形状共存, E0跃迁, 双态混合模型, 电单极强度rho2, Shape Coexistence, E0 Transitions]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [shape-coexistence, e0-transitions, two-state-mixing, monopole-strength, internal-conversion, a130-region]
---

# 原子核形状共存、四极形变突变与电单极（E0）跃迁动力学

## Definition

### 物理全景：核多体系统的宏观形状简并

在原子核低激发能谱中，宏观几何形状通常由价核子组态所决定的势能曲面全局极小值决定。然而，在特定核区（如中子/质子闭壳与次闭壳附近，包括铅区 $Z\approx 82$、氪-锶-锆区 $A\approx 70 \sim 100$、以及本 Wiki 重点关注的钡-铈-钕区 $A\approx 130$），原子核常常在几乎相同的激发能下（甚至在基态附近）展现**两种或三种截然不同的宏观平衡形貌**——**形状共存（Shape Coexistence）**。

根据 K. Heyde & J. L. Wood（Rev. Mod. Phys. 83, 1467, 2011）与 A. Bohr & B. R. Mottelson《Nuclear Structure》Vol. II：
1. **微观驱动机制**：长程质子-中子四极-四极相互作用（$Q_\pi \cdot Q_\nu$）使得质子或中子跨越单粒子壳隙激发的多粒子-多空穴入侵组态（Intruder states, 如 $2p\text{-}2h, 4p\text{-}4h$）能量急剧大幅下移，与正常的准球形或弱变形基态发生偶合简并；
2. **电单极（$E0$）跃迁的独占地位**：不同形状态之间的混合与脱激由于初末态空间角动量相同（最典型为 $0_2^+ \to 0_1^+$），单光子发射由于角动量守恒被严格禁戒，使得**电单极（$E0$）内转换电子跃迁成为探针形状共存与微观波函数混合的最直接指纹**！

---

## Necessary Assumptions

### 电单极跃迁（$E0$ Transitions）微观理论

### (1) 单极跃迁算符与选择定则
电单极跃迁算符由核内带电质子电荷半径平方的单体算符定义：
$$\hat{T}(E0) = \sum_{k=1}^Z e \cdot r_k^2$$
- **选择定则**：$\Delta I = 0$，$\pi_i = \pi_f$（宇称严格守恒，但 $0 \to 0$ 严格禁戒单光子辐射）；
- **退激途径**：
  1. **内转换电子（Internal Conversion Electron, ICE）**：近核 $K, L, M$ 壳层电子与核电荷分布直接重叠发生无辐射跃迁，电子被电磁单极场直接弹出原子；
  2. **正负电子对产生（Internal Pair Creation, IPC）**：当能级差 $\Delta E = E_i - E_f > 2 m_e c^2 = 1022\text{ keV}$ 时，真空中自发产生相对运动的 $e^+ e^-$ 对。

### (2) 减缩电单极强度参数 $\rho^2(E0)$
为消除原子物理结合能与相空间因子的影响，Church & Weneser 定义了无量纲的减缩电单极强度：
$$\rho(E0) \equiv \frac{\langle I_f || \sum_{k=1}^Z r_k^2 || I_i \rangle}{R_0^2}$$
$$\rho^2(E0) = \frac{1}{R_0^4} |\langle I_f || \sum_{k=1}^Z r_k^2 || I_i \rangle|^2$$
其中标称核半径取 $R_0 = 1.2 A^{1/3}\text{ fm}$。

跃迁速率与单极强度由原子转换因子 $\Omega(E0)$ 严格连接：
$$W(E0) = \frac{1}{\tau(E0)} = \rho^2(E0) \cdot \Omega_K(E0)$$
（$\Omega_K(E0)$ 为可由 Dirac-Fock 相对论原子物理高精度计算的电单极电子因子）。
通常实验测得的强度以千分之一单位表示：$\rho^2(E0) \times 10^3$。

---

## Discriminating Observables

### 特征谱学观测量

## Supporting Evidence

### 双态混合模型（Two-State Mixing Model）与形变反演

当原子核在基态附近存在两个未微扰的纯形状态：
- 态 $|1\rangle$：未微扰能量 $e_1$，平衡四极形变 $\beta_1$（如较小形变或球形）；
- 态 $|2\rangle$：未微扰能量 $e_2$，平衡四极形变 $\beta_2$（如较大形变拉长态）。

二者通过微观二体剩余相互作用矩阵元 $V_{\text{mix}} = \langle 1 | \hat{H} | 2 \rangle$ 发生组态混合。物理本征态为：
$$|0_1^+\rangle = \cos\theta |1\rangle + \sin\theta |2\rangle$$
$$|0_2^+\rangle = -\sin\theta |1\rangle + \cos\theta |2\rangle$$
其中混合角由能隙与耦合矩阵元决定：$\tan(2\theta) = \frac{2 V_{\text{mix}}}{e_1 - e_2}$。

### 形状共存 $\rho^2(E0)$ 解析反演定理：
$$\rho^2(E0; 0_2^+ \to 0_1^+) = \sin^2(2\theta) \cdot \left( \frac{3 Z}{4\pi} \right)^2 \cdot (\beta_1^2 - \beta_2^2)^2$$

**物理精要与判据法典**：
1. **若形变无差异（$\beta_1 \approx \beta_2$）**：即便发生完全混合（$\theta = 45^\circ$），$\rho^2(E0) \approx 0$；
2. **若无组态混合（$V_{\text{mix}} = 0 \implies \theta = 0^\circ$）**：即便两态形变差异巨大，$\rho^2(E0) \equiv 0$；
3. **强 $\rho^2(E0)$ 现象（$\rho^2(E0) \times 10^3 > 10$）的充要条件**：**体系必须同时具备“显著的宏观形变跨度（$|\beta_1^2 - \beta_2^2| \gg 0$）”与“有限强度的微观波函数重叠混合（$\sin^2(2\theta) > 0$）”**！

---

## 4. 在 $A\approx 130$ 三轴手征与摆动能带中的重要启示

在 $A\approx 130$ 质量区的同位素链中（如 $^{130}\text{Ba}, {}^{132,134}\text{Ce}, {}^{134,136}\text{Nd}$）：
1. **三轴形状共存与多重手征带（M$\chi$D 类型 II）**：
   当原子核在长椭三轴势阱与扁椭三轴势阱之间共存时，外层奇核子在这两个不同形变核芯上分别构造成手征双重带；
2. **能带退激脱落（Decay-out）中的 $E0$ 甄别**：
   当高自旋变形带（如高形变带 HD 或三轴带）向低自旋正常形变基态带退激时，常伴随多条异常强的转换电子线；利用本指南的模型，可精确提取带间微观穿透势垒阻碍因子，排除虚假高自旋分支。

## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。


## Sources

- [[triaxial-collective-modes-unified-theory-and-spectroscopy]]
- [[nuclear-spectroscopy-and-structure-master-field-manual]]
