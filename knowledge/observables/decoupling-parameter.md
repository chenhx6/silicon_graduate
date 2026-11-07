---
type: observable
title: 解耦参数（a）
aliases: [decoupling parameter, Coriolis decoupling parameter, a-parameter]
created: 2026-11-06
updated: 2026-11-06
status: active
review_status: unreviewed
observable_kind: band-structure-parameter
symbol: a
units: dimensionless
tags: [nilsson-model, coriolis, decoupling, signature-splitting, stephens-simon]
---

# 解耦参数（Decoupling Parameter, $a$）

## Definition

在奇 $A$ 变形核中，$K = 1/2$ 能带具有非常特殊的自旋劈裂结构。由于核对称轴上的单核子内禀角动量投影仅为 $1/2$，垂直于对称轴旋转的集体核芯通过科里奥利力（Coriolis force）直接翻转粒子自旋（$\Delta K = \pm 1$），从而在相同哈密顿量中产生直接的一阶对角能量修正项。该项的微观无量纲强度系数即为解耦参数 $a$。

## Formula and Energy Spectrum

在轴对称强耦合极限下，$K = 1/2$ 转动带的激发能谱严格遵循 Bohr-Mottelson 公式：
$$E(I) = E_0 + A \left[ I(I+1) + a (-1)^{I+1/2} (I + 1/2) \right]$$
其中 $A = \frac{\hbar^2}{2\mathcal{J}}$ 为转动惯量常数，$a$ 为解耦参数。

### 旋称劈裂量（Signature Splitting）
相邻奇偶自旋态之间的有效能级差受到 $a$ 的直接调制：
- 当 $a > 0$ 时，自旋 $I = 3/2, 7/2, 11/2, \dots$（$\alpha = -1/2$）能级相对压低；
- 当 $a < 0$ 时，自旋 $I = 1/2, 5/2, 9/2, \dots$（$\alpha = +1/2$）能级相对压低。

### 单粒子微观表达式（Nilsson 极限）
在变形单粒子基底 $|\Omega = 1/2\rangle = \sum_j c_j |j, 1/2\rangle$ 下，解耦参数由核子角动量升降算符微观决定：
$$a = -\langle \Omega = 1/2 | j_+ | \Omega = -1/2 \rangle = \sum_j (-1)^{j-1/2} (j + 1/2) |c_j|^2$$

对于未受微观组态混合的高 $j$ 纯单粒子极限轨道（Pure High-$j$ State）：
$$a_{\text{pure}} = (-1)^{j-1/2} (j + 1/2)$$
- 对于 $1g_{9/2}$ 轨道：$a_{\text{pure}} = +(9/2 + 1/2) = +5$；
- 对于 $1h_{11/2}$ 轨道：$a_{\text{pure}} = -(11/2 + 1/2) = -6$；
- 对于 $1i_{13/2}$ 轨道：$a_{\text{pure}} = +(13/2 + 1/2) = +7$。

## Stephens-Simon 彻底退耦带机制（Decoupled Band）

当 $|a| \approx j+1/2 \gg 1$ 时（例如 $h_{11/2}$ 轨道的 $a \approx -6$），奇核子的角动量完全从形变核芯的对称轴上“解耦”，转而牢固地与转动轴（$x$ 轴）对齐。这导致能级序列的间距完全退化为偶偶核芯基态带的能量间距（Stephens-Simon 退耦带）：
$$E(I = j+2) - E(I = j) \approx E(2_1^+)_{\text{core}}$$
这一机制是解释 A~130 区域奇 La、Ce、Pr 核中特征性 $\Delta I = 2$ 退耦转动带的微观物理基石。
