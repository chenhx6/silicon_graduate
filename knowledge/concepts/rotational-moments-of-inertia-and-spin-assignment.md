---
type: concept
title: "原子核运动学与动力学转动惯量（J1与J2）及未知能带自旋反演算法"
aliases: [转动惯量J1与J2, 运动学转动惯量, 动力学转动惯量, 自旋反演算法, 悬挂带自旋确定]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [moments-of-inertia, kinematical-moi, dynamical-moi, spin-assignment, floating-bands, superdeformation]
---

# 原子核运动学与动力学转动惯量（J1与J2）及未知能带自旋反演算法

## 1. 物理测量全景：微观自旋与宏观转动的桥梁

在低能高自旋实验核谱学中，实验探测器阵列记录的最直接量是级联退激的 $\gamma$ 射线能量。根据 A. Bohr & B. R. Mottelson《Nuclear Structure》Vol. II 与高自旋物理学，如何从分立的跃迁能量差中提取原子核转动响应，依赖于两个内涵截然不同的转动惯量定义：

1. **运动学转动惯量（Kinematical Moment of Inertia, $\mathcal{J}^{(1)}$）**；
2. **动力学转动惯量（Dynamical Moment of Inertia, $\mathcal{J}^{(2)}$）**。

二者的微观演化与差异，是判断核超流配对塌缩、准粒子回弯对齐、超形变（Superdeformation, SD）以及在未建立跨带连接线（悬挂能带，Floating bands）时反演确定绝对能级自旋的最强有力数学物理武器。

---

## 2. $\mathcal{J}^{(1)}$ 与 $\mathcal{J}^{(2)}$ 的严格微积分定义与物理诠释

### (1) 运动学转动惯量 $\mathcal{J}^{(1)}$（一阶导数）
定义为总角动量在转动轴上的投影 $I_x$ 与旋转角速度 $\omega$ 的静态比值：
$$\mathcal{J}^{(1)}(\omega) \equiv \hbar \frac{I_x}{\omega} = \hbar^2 \frac{I_x}{\frac{dE}{dI_x}}$$
在常规轴对称或三轴转动带中，对于连续级联四极跃迁（$\Delta I = 2$），跃迁能量为 $E_\gamma(I \to I-2) \approx 2\hbar\omega$。取中点自旋 $I_m = I - 1$：
$$\mathcal{J}^{(1)}(I_m) \approx \hbar^2 \frac{2I - 1}{E_\gamma(I \to I-2)}$$

**物理特征**：
- 包含微观价核子的对齐角动量贡献（$I_x = I_{\text{core}} + i_x$）；
- 计算必须依赖于**已经确切知道该能级的绝对自旋 $I$**！若自旋未知，无法计算 $\mathcal{J}^{(1)}$。

### (2) 动力学转动惯量 $\mathcal{J}^{(2)}$（二阶导数）
定义为角动量对转动角速度的变化率（响应导数）：
$$\mathcal{J}^{(2)}(\omega) \equiv \hbar \frac{dI_x}{d\omega} = \hbar^2 \left( \frac{d^2 E}{dI_x^2} \right)^{-1}$$
在离散实验能级中，通过前后两条相邻级联 $\gamma$ 射线的能量差 $\Delta E_\gamma$ 计算：
$$\Delta E_\gamma = E_\gamma(I+2 \to I) - E_\gamma(I \to I-2)$$
$$\mathcal{J}^{(2)} \approx \frac{4\hbar^2}{\Delta E_\gamma}$$

**物理特征（核心优势）**：
- **完全无需知道绝对自旋 $I$**！仅凭纯能谱测定的两条 $\gamma$ 线间距即可严格提取；
- 反映了转动势能曲面的曲率以及转动对微观组态重构的抵抗刚性；
- 在无粒子对解耦的刚体极限下，$\mathcal{J}^{(2)} = \mathcal{J}^{(1)} = \mathcal{J}_{\text{rigid}}$；
- 在常规配对超流核中，随频率增加配对被弱化，$\mathcal{J}^{(2)} > \mathcal{J}^{(1)}$；
- 在发生回弯对齐（Backbending）处，能级间距骤缩（$\Delta E_\gamma \to 0$），$\mathcal{J}^{(2)}$ 展现剧烈的尖锐峰值甚至发散！

---

## 3. 悬挂能带的未知自旋反演算法（Spin Assignment Protocol）

在束内重离子实验中，常常会发现一条漂亮的规则四极转动能带，但其底端向已知低自旋基带的退激路径极其分散微弱，未能在二维符合矩阵中找到连接线（称为“悬挂能带，Floating band”）。此时能带能级的绝对自旋 $I$ 悬空未知。

### Draper-Wu 自旋反演积分模型：
由于动力学惯量无需自旋即可计算，利用微分关系 $dI_x = \frac{1}{\hbar} \mathcal{J}^{(2)}(\omega) d\omega$，积分得到角动量展开：
$$I_x(\omega) = \frac{1}{\hbar} \int_{\omega_0}^\omega \mathcal{J}^{(2)}(\omega') d\omega' + i_0$$
将转动惯量在未回弯区间按 Harris 展开代入：$\mathcal{J}^{(2)}(\omega) = \mathcal{J}_0 + 3 \mathcal{J}_1 \omega^2$。

积分反演公式为：
$$I(I+1) - K^2 \approx \left[ \mathcal{J}_0 \omega + \mathcal{J}_1 \omega^3 + i_0 \right]^2$$

**算法执行准则**：
1. 取试验带头自旋初猜值 $I_{\text{trial}} = I_0, I_0 + 1, I_0 + 2, \dots$（半整数或整数）；
2. 对每组候选自旋计算试验运动学转动惯量 $\mathcal{J}^{(1)}_{\text{trial}}(\omega)$；
3. 检验微观自洽性：在未回弯频率区，真实的能带必须满足 $\mathcal{J}^{(2)} \ge \mathcal{J}^{(1)}$ 且二者在大形变极限下渐近收敛；
4. 寻找使 $\sum [\mathcal{J}^{(1)}_{\text{trial}}(\omega) - \mathcal{J}_{\text{model}}(\omega)]^2$ 最小的离散实数解，即可**以 $\pm 1\hbar$ 的极高置信度锁定未知悬挂带的带头真实自旋**！
