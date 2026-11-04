---
type: concept
title: "库仑激发动力学、重取向效应与Kumar四极形变不变量"
aliases: [库仑激发理论, 重取向效应, Kumar四极不变量, Coulex截面, 静态四极矩Qs]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [coulomb-excitation, reorientation-effect, kumar-invariants, static-quadrupole-moment, triaxiality, gamma-softness]
---

# 库仑激发动力学、重取向效应与Kumar四极形变不变量

## Definition

### 物理全景：纯电磁探针下的核形状测绘

在原子核低激发态研究中，强相互作用引起的核反应往往伴随复杂的光学势、核子重叠与不可避免的模型依赖性。而**库仑激发（Coulomb Excitation, Coulex）**将入射带电粒子的质心系碰撞能量严格控制在库仑势垒以下（即满足安全距离判据，通常外缘接触距离 $d_{\text{min}} \ge R_p + R_t + 5\text{ fm}$），彻底隔绝了强核相互作用的核势干扰。

根据 A. Bohr & B. R. Mottelson《Nuclear Structure》Vol. II 与 K. Alder & A. Winther《Electromagnetic Excitation》（1975）：
1. **电磁相互作用纯粹性**：反应截面完全由经典电动力学与微观多极跃迁矩阵元严格决定；
2. **对角与非对角矩阵元全息提取**：不仅能高精度测量跨态跃迁强度 $B(E2; 0_1^+ \to 2_1^+)$，而且能够通过**重取向效应（Reorientation Effect）**直接测定激发态自身的**静态电四极矩（Static Quadrupole Moment, $Q_s(2_1^+)$）**，从而在无模型依赖前提下判定原子核是拉长形还是扁长形；
3. **Kumar 四极不变量（Kumar Invariants）**：通过求迹构建旋转坐标系与实验室系严格守恒的张量不变量，彻底解耦核形状涨落（$\gamma$ 软度）与刚性三轴形变。

---

## Necessary Assumptions

### 库仑激发二阶微扰与重取向效应（Reorientation Effect）

### (1) 一阶微扰激发几率
在半经典近似下，带电粒子沿双曲线轨道运动，一阶 $E2$ 激发几率为：
$$P_{0 \to 2}^{(1)} = \left(\frac{Z_p e}{\hbar v a}\right)^2 \cdot B(E2; 0_1^+ \to 2_1^+) \cdot df_{E2}(\theta, \xi)$$
其中 $a = \frac{Z_p Z_t e^2}{m_0 v^2}$ 为对心碰撞半距离，$\xi = \frac{\Delta E}{\hbar} \frac{a}{v}$ 为绝热参数（Adiabaticity parameter）。

### (2) 二阶微扰干涉与重取向效应
在强电场作用下，激发到 $2_1^+$ 态的原子核受到入射核电荷的强烈电场梯度作用。若该激发态具有非零内禀四极形变，其自身的自旋磁子能级发生二次重排。二阶微扰总几率为：
$$P_{0 \to 2} = P_{0 \to 2}^{(1)} \left[ 1 + c(E, \theta) \cdot \langle 2_1^+ || \mathcal{M}(E2) || 2_1^+ \rangle \right]$$
其中对角矩阵元与实验可观测的**静态电四极矩 $Q_s(2_1^+)$** 直接成正比：
$$Q_s(2_1^+) = \sqrt{\frac{16\pi}{5}} \frac{C_{2 2 2 0}^{2 2}}{\sqrt{5}} \langle 2_1^+ || \mathcal{M}(E2) || 2_1^+ \rangle \approx 0.758 \langle 2_1^+ || \mathcal{M}(E2) || 2_1^+ \rangle$$

**极性判决法则（拉长 vs 扁长）**：
- 若测量出**$Q_s(2_1^+) < 0$**：对应**拉长形变（Prolate shape）**；
- 若测量出**$Q_s(2_1^+) > 0$**：对应**扁长形变（Oblate shape）**；
- 若测量出**$Q_s(2_1^+) \approx 0$**：对应**三轴最大非对称核（Triaxial with $\gamma \approx 30^\circ$）**或球形振动核！

---

## Discriminating Observables

### 特征谱学观测量

## Supporting Evidence

### Kumar 四极形变不变量（Kumar Invariants）数学理论

在具有大振幅软振动的过渡区核（如 $A\approx 130$ 质量区）中，单凭固定形变模型（如纯拉长或纯三轴）无法描述波函数随形状的广泛分布。Krishna Kumar（1972）提出利用电四极张量算符 $\mathcal{M}(E2)$ 的零阶张量标量积，构造全局不变量：

### (1) 二阶不变量 $Q^2$（总形变平方）
$$q_2 \equiv \sqrt{5} \langle 0_1^+ | [\mathcal{M}(E2) \times \mathcal{M}(E2)]_0 | 0_1^+ \rangle = \sum_i \langle 0_1^+ || \mathcal{M}(E2) || 2_i^+ \rangle \langle 2_i^+ || \mathcal{M}(E2) || 0_1^+ \rangle$$
$$Q^2 = \left( \frac{3 Z}{4\pi} R_0^2 \right)^2 \langle \beta^2 \rangle$$
该求和由所有中间 $2^+$ 态的跃迁几率耗尽，直接给出基态全四极形变均方根值 $\sqrt{\langle \beta^2 \rangle}$。

### (2) 三阶不变量 $Q^3 \cos(3\delta)$（非对称偏斜度）
$$q_3 \equiv -\sqrt{\frac{35}{2}} \langle 0_1^+ | [ [\mathcal{M}(E2) \times \mathcal{M}(E2)]_2 \times \mathcal{M}(E2)]_0 | 0_1^+ \rangle = \left( \frac{3 Z}{4\pi} R_0^2 \right)^3 \langle \beta^3 \cos(3\gamma) \rangle$$
由此定义等效非对称角参数 $\delta$（对应微观形变角 $\gamma$）：
$$\cos(3\delta) \equiv \frac{q_3}{(q_2)^{3/2}}$$

**无模型依赖的三轴与形状共存判据**：
1. $\cos(3\delta) = +1.0 \implies \delta = 0^\circ$（纯拉长核）；
2. $\cos(3\delta) = -1.0 \implies \delta = 60^\circ$（纯扁长核）；
3. $\cos(3\delta) \approx 0.0 \implies \delta \approx 30^\circ$（**最大三轴非对称形变**）；
4. **$\gamma$ 刚性 vs $\gamma$ 软度判定**：
   计算高阶涨落方差 $\sigma_\gamma^2 = \langle \cos^2(3\delta) \rangle - \langle \cos(3\delta) \rangle^2$。若方差接近零，为三轴刚性转子（如 Davydov-Filipov 模型）；若方差很大，为大振幅 $\gamma$ 软核（Jean-Wilets 软核模型）。

## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。


## Sources

- [[triaxial-collective-modes-unified-theory-and-spectroscopy]]
- [[nuclear-spectroscopy-and-structure-master-field-manual]]
