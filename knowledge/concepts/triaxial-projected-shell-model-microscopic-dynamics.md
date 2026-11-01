---
type: concept
title: "三轴投影壳模型（TPSM）微观多体动力学与角动量投影理论"
aliases: [三轴投影壳模型, TPSM模型, 3D角动量投影, 带图理论, Band Diagram, 微观摆动计算]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [tpsm, angular-momentum-projection, band-diagram, pairing-plus-quadrupole, triaxiality, wobbling-motion, chiral-doublet-bands]
---

# 三轴投影壳模型（TPSM）微观多体动力学与角动量投影理论

## 1. 理论渊源：打破轴对称性与对称性精确恢复

在低能核结构微观模型体系中，传统大尺度球形壳模型（LSSM）在处理中重质量变形核（如 $A\approx 130$ 质量区）的高自旋态时，面临着千亿维配置空间的指数爆炸难题；而自洽推转平均场（TAC/CSM）虽然能在大形变下求解，但其内禀波函数打破了三维空间旋转对称性，导致角动量不是守恒量，无法直接输出具有确定自旋和宇称的离散实验室物理跃迁。

由 J. A. Sheikh 和 K. Hara 发展的**投影壳模型（Projected Shell Model, PSM）**及其三轴推广——**三轴投影壳模型（Triaxial Projected Shell Model, TPSM）**（详见 C. M. Petrache 主编《Chirality and Wobbling in Atomic Nuclei》第 12 与 14 章），通过**微观三维角动量严格投影技术（3D Angular Momentum Projection）**，在有限紧凑的多准粒子截断空间内，完美兼顾了原子核宏观大形变与严格的微观量子数守恒（自旋 $I$、宇称 $\pi$、电荷与微观粒子对关联）。

---

## 2. TPSM 哈密顿量与多准粒子投影基底

### (1) 配对加四极-四极相互作用（PQQ）微观哈密顿量
TPSM 采用可严格求解长程形变与短程配对竞争的标准微观多体能量算符：
$$\hat{H} = \hat{H}_0 - \frac{1}{2} \chi \sum_\mu \hat{Q}_{2\mu}^\dagger \hat{Q}_{2\mu} - G_M \hat{P}^\dagger \hat{P} - G_Q \sum_\mu \hat{P}_{2\mu}^\dagger \hat{P}_{2\mu}$$
其中：
- $\hat{H}_0$ 为球形单粒子壳层能量项；
- 第二项为长程质子-中子四极-四极相互作用（Quadrupole-Quadrupole Force, $Q\cdot Q$），直接驱动原子核产生宏观四极形变 $\epsilon_2$ 与三轴非对称角 $\gamma$；
- 第三项为单极对关联（Monopole Pairing, $G_M$），描述时间反演共轭核子对的超流配对；
- 第四项为四极对关联（Quadrupole Pairing, $G_Q$），描述高角动量准粒子旋转对剪切对关联的修正。

### (2) 三轴变形 Nilsson-BCS 真空态
通过在三轴形变外场中求解准粒子自洽方程，构造三轴变形 BCS 真空基态 $|\Phi(\epsilon_2, \gamma)\rangle$。在该真空中，三轴形变参数化定义为：
$$H_{\text{sp}} = H_0 - \frac{2}{3} \hbar\omega_0 \left[ \epsilon_2 \cos\gamma \cdot Y_{20} + \frac{\epsilon_2 \sin\gamma}{\sqrt{2}} (Y_{22} + Y_{2-2}) \right]$$
在此真空上通过 Bogoliubov 准粒子创生算符 $a_k^\dagger$ 构造多准粒子基底集合 $\{ |\Phi_\kappa\rangle \}$：
- 偶偶核基态：真空态 $|\Phi_0\rangle$；
- 两准粒子对齐态：$a_{\nu_1}^\dagger a_{\nu_2}^\dagger |\Phi_0\rangle$（两准中子），$a_{\pi_1}^\dagger a_{\pi_2}^\dagger |\Phi_0\rangle$（两准质子）；
- 四准粒子对齐态：$a_{\pi_1}^\dagger a_{\pi_2}^\dagger a_{\nu_1}^\dagger a_{\nu_2}^\dagger |\Phi_0\rangle$。

---

## 3. 三维角动量投影算符（3D Angular Momentum Projection）

由于三轴变形内禀态 $|\Phi_\kappa\rangle$ 不具备良好的实验室角动量，必须通过三维投影算符从变形波函数中“滤出”具有确定自旋 $I$、实验室分量 $M$ 与内禀投影 $K$ 的严格物理本征基矢：
$$\hat{P}_{MK}^I = \frac{2I + 1}{8\pi^2} \int D_{MK}^{I*}(\alpha, \beta, \gamma) \hat{R}(\alpha, \beta, \gamma) d\Omega$$
其中 $\Omega = (\alpha, \beta, \gamma)$ 为欧拉角，$\hat{R}(\Omega) = e^{-i\alpha \hat{J}_z} e^{-i\beta \hat{J}_y} e^{-i\gamma \hat{J}_z}$ 为三维有限空间转动算符。

投影后的基底物理态记为：
$$|I M, \kappa K\rangle = \hat{P}_{MK}^I |\Phi_\kappa\rangle$$
由于投影态之间通常存在非正交重叠，计算多体矩阵元必须求解广义希尔伯特空间广义本征方程（Hill-Wheeler 方程）：
$$\sum_{\kappa' K'} \left[ \mathcal{H}_{\kappa K, \kappa' K'}^I - E^I \mathcal{N}_{\kappa K, \kappa' K'}^I \right] C_{\kappa' K'}^I = 0$$
其中：
- 重叠范数核：$\mathcal{N}_{\kappa K, \kappa' K'}^I = \langle \Phi_\kappa | \hat{P}_{KK'}^I | \Phi_{\kappa'} \rangle$；
- 能量矩阵核：$\mathcal{H}_{\kappa K, \kappa' K'}^I = \langle \Phi_\kappa | \hat{H} \hat{P}_{KK'}^I | \Phi_{\kappa'} \rangle$。

---

## 4. 带图（Band Diagram）理论与三轴手征/摆动模式显式求解

### (1) 什么是微观“带图（Band Diagram）”？
在进行最终全部组态混合对角化之前，先单独计算每个未微扰的多准粒子投影基底自身随自旋 $I$ 演化的期望能量：
$$E_\kappa(I) = \frac{\langle \Phi_\kappa | \hat{H} \hat{P}_{KK}^I | \Phi_\kappa \rangle}{\langle \Phi_\kappa | \hat{P}_{KK}^I | \Phi_\kappa \rangle}$$
以自旋 $I$ 为横坐标、以投影能量 $E_\kappa(I)$ 为纵坐标绘制的多条平滑能量曲线全景图，称为**带图（Band Diagram）**。

### (2) 带图对微观相变的直观揭示
1. **回弯对齐（Backbending）**：
   真空带（$g$-band）能量随自旋按 $I(I+1)$ 上升；而两准粒子对齐带（$s$-band）由于已经获得了约 $i_x \approx 10\hbar$ 的内禀角动量，其能量曲线斜率较平缓。两线在临界自旋 $I_c$ 处发生几何交叉，直接解释了回弯的微观成因！
2. **三轴摆动模式（Wobbling）**：
   在三轴变形下（$\gamma \approx 30^\circ$），同一单粒子态在不同的 $K$ 投影之间发生强力混杂，$K=0, 2, 4$ 态在自旋投影后展现出系列规则排列的伴随能级，其能量差即对应微观摆动声子能量；
3. **手征双重带（Chiral Doublets）**：
   质子粒子-中子空穴两准粒子态在三维旋转坐标系中形成左右手对称态，经投影后自然在能谱中输出严格对称的孪生手征双重带。
