---
type: concept
title: "原子核旋称反转动力学、能量交错参量与三轴质中残余相互作用"
aliases: [旋称反转, 反常旋称劈裂, 能量交错参量S(I), 三轴pn相互作用, Signature Inversion]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [signature-inversion, signature-splitting, staggering-parameter, triaxiality, pn-interaction, a130-region]
---

# 原子核旋称反转动力学、能量交错参量与三轴质中残余相互作用

## Definition

### 物理全景：科里奥利力经典排序的量子反转

在旋转变形原子核中，绕垂直于对称轴旋转 $180^\circ$ 的空间离散旋转操作 $\mathcal{R}_x(\pi) = \exp(-i\pi \hat{I}_x)$ 构成系统的运动常数。其本征量子数定义为**旋称（Signature, $\alpha$）**：
$$r = \exp(-i\pi \alpha) \implies I = \alpha \pmod 2$$
在单粒子高 $j$ 轨道中，科里奥利力（$-2\vec{\omega} \times \vec{v}$）将核子推向转动轴，使得**有利旋称态（Favored signature: $\alpha_f = \frac{1}{2}(-1)^{j-1/2}$）**与转子同向对齐，其能级在常规轴对称核中总是严格低于**不利旋称态（Unfavored signature: $\alpha_u = \alpha_f + 1$）**。

然而，自 1980 年代以来，在 $A\approx 130$ 质量区的奇奇核与奇中子核（如 $^{126,128}\text{Cs}, {}^{130,132,134}\text{La}, {}^{132,134,136}\text{Pr}$）中，实验上广泛观测到了反常的**旋称反转（Signature Inversion）**现象：
- 在低自旋区（$I \le 15\hbar$），**理论上应该能量更高的不利旋称态反而位于有利旋称态之下（能量倒转！）**；
- 随着转动角速度增加，两能带在某一临界自旋 $I_{\text{inv}}$ 处发生能量交叉，高自旋区恢复为正常的旋称排序。

根据相关推转模型研究，三轴单粒子耦合和价质子-价中子残余相互作用都可影响旋称反转；轴对称模型、三轴模型和残余相互作用的相对贡献需要按具体组态与核素检验。旋称反转是一个有信息量的谱学现象，但不是三轴形变或 $p$-$n$ 相互作用的单独决定性证明。

---

## Necessary Assumptions

### 能量交错参量 $S(I)$ 与实验判定指标

在在束 $\gamma$ 谱学分析中，实验上通过**能量交错参量（Staggering Parameter, $S(I)$）**精确量化旋称劈裂的幅度与符号：

$$S(I) = \frac{E(I) - E(I-1)}{2I}$$

### (1) 物理判决指纹
将 $S(I)$ 对自旋 $I$ 作图：
1. **正常旋称劈裂（Normal Signature）**：
   $S(I)$ 随自旋呈现规则的锯齿状交错振荡，且在偶奇自旋上的取向与单粒子角动量代数预言一致；
2. **旋称反转（Signature Inversion）**：
   在低自旋区，锯齿交错的振荡相位发生严格的**$180^\circ$ 反相（相位反转）**！
3. **临界反转自旋 $I_{\text{inv}}$**：
   在 $I = I_{\text{inv}}$ 处，锯齿振荡振幅收缩至零（发生相交节点），此后高自旋区振荡恢复正常相位。

---

## Discriminating Observables

### 特征谱学观测量

## Supporting Evidence

### 三轴形变与质中相互作用微观驱动机制

### (1) 三轴形变势对单粒子矩阵元的调制
当原子核处于三轴形变（$\gamma \ne 0^\circ$）时，变形单粒子 Nilsson 势在不同主轴上的曲率互不相等。
在推转哈密顿量 $h' = h_{\text{sp}} - \omega j_x$ 中，由于波函数在长轴与短轴之间的非对称投影，科里奥利相互作用的非对角矩阵元受到三轴几何因子 $\cos(\gamma + 30^\circ)$ 的强烈调制：
- 当 $\gamma < 0$（扁长三轴）时，Coriolis 力在特定低 $j$ 轨道上的有效退对齐效应削弱了有利旋称态的对齐能量增益；
- 导致有利旋称态与不利旋称态的单粒子能级在费米面附近发生能级反常靠近。

### (2) 质子-中子残余力（$V_{pn}$）的关键推动
在 $A\approx 130$ 奇奇核中，价质子占据 $\pi h_{11/2}$ 轨道，价中子占据 $\nu h_{11/2}$ 轨道。
当二者通过短程表面 $\delta$ 相互作用（SDI）或四极力耦合时，质子波函数与中子波函数的空间角重叠在不利旋称态构型下比有利旋称态更大！
由此产生的微观相互作用吸引能：
$$\Delta E_{pn} = \langle \alpha_u | V_{pn} | \alpha_u \rangle - \langle \alpha_f | V_{pn} | \alpha_f \rangle < 0$$
在低自旋下，质中残余相互作用的能量降低幅度**压倒了原本微弱的 Coriolis 旋称劈裂能**，强行将不利旋称态拉到有利旋称态下方，形成旋称反转！
高自旋下，集体转动离心力急剧增加（正比于 $I$），Coriolis 力重新占据主导，系统最终恢复正常排序。

---

## 4. 与三轴手征带、横向摆动带的鉴别对账

在 $A\approx 130$ 质量区的同位素分析中，旋称反转与手征双重带、横向摆动经常处于相邻或竞争的激发通道：
1. **与手征双重带的鉴别**：
   - 手征双重带由两条宇称相同、自旋相同且各级完全并行的能带构成，其带间存在特征的交替 $B(M1)$ 强化；
   - 旋称反转带是单一准粒子组态内由于绕轴旋转 $180^\circ$ 离散对称性引起的自旋相差 $1\hbar$ 的交错劈裂；
2. **对 $^{131}\text{Ce}$ 与 $^{133}\text{Ce}$ 的关键启示**：
   在分析 $^{133}\text{Ce}$ 带头 $13/2^-$ 的伴随能带时，应通过能量
   交错参量 $S(I)$ 检查旋称反转的可能性，并结合偏振、寿命、组态和
   响应证据；单独的相位翻转不能严格排除旋称反转或保证手征归属。

## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。


## Sources

- [[triaxial-collective-modes-unified-theory-and-spectroscopy]]
- [[nuclear-spectroscopy-and-structure-master-field-manual]]
