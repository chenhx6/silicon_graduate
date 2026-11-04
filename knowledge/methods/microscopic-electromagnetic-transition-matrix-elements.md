---
type: method
method_type: experimental-analysis-contract
title: "微观核物理代数与电磁跃迁矩阵元推导全指南"
aliases: [电磁跃迁微观推导, Suhonen张量代数指南, Wigner-Eckart定理核跃迁, 单粒子跃迁几率计算]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
tags: [tensor-algebra, wigner-eckart-theorem, electromagnetic-transitions, suhonen-methods, bcs-quasiparticles]
---

# 微观核物理代数与电磁跃迁矩阵元推导全指南

## Purpose

### 理论渊源与微观推导基石

低能核结构实验的核心可观测量（如激发态半衰期 $T_{1/2}$、多极混合比 $\delta$、角分布系数 $a_2$）最终都要归结为原子核波函数之间的**电磁跃迁约化矩阵元（Reduced Transition Matrix Elements）**。

根据 Jouni Suhonen 经典著作《From Nucleons to Nucleus: Concepts of Microscopic Nuclear Theory》（Springer 2007）与 Kris Heyde《Basic Ideas and Concepts in Nuclear Physics》，本指南系统给出从角动量 Racah 代数、不可约球张量算符、Wigner-Eckart 定理，到单粒子与多体 BCS 准粒子电磁跃迁几率计算的标准数学物理框架。

---

## Inputs and Assumptions

### 角动量代数与 Wigner-Eckart 定理严格约定

### (1) 不可约球张量算符（Irreducible Spherical Tensor Operators）
阶数为 $\lambda$ 的不可约球张量算符集合 $\{ T_{\lambda \mu} \}$（$\mu = -\lambda, -\lambda+1, \dots, \lambda$）满足与总角动量算符 $\vec{J}$ 的标准对易关系：
$$[J_z, T_{\lambda \mu}] = \mu T_{\lambda \mu}$$
$$[J_\pm, T_{\lambda \mu}] = \sqrt{\lambda(\lambda+1) - \mu(\mu \pm 1)} T_{\lambda, \mu \pm 1}$$

### (2) Wigner-Eckart 定理（Suhonen / Rose 相位约定）
任何不可约球张量算符在角动量本征态之间的矩阵元可以严格因式分解为几何因子（Clebsch-Gordan 系数）与内禀物理结构（约化矩阵元 $\langle j_f || T_\lambda || j_i \rangle$）：
$$\langle j_f m_f | T_{\lambda \mu} | j_i m_i \rangle = (-1)^{2\lambda} \frac{C_{j_i m_i \lambda \mu}^{j_f m_f}}{\sqrt{2 j_f + 1}} \langle j_f || T_\lambda || j_i \rangle$$
其中 $C_{j_i m_i \lambda \mu}^{j_f m_f} \equiv \langle j_i m_i \lambda \mu | j_f m_f \rangle$ 为 Clebsch-Gordan 系数。

**极重要反模式警示**：
不同学派教材中约化矩阵元的定义相差一个 $\sqrt{2j_f + 1}$ 因子（如 Edmonds 约定 vs Brink-Satchler 约定）。在编写 Python 或 C++ 计算代码时，必须统一锁定 Suhonen 约定，确保初末态交换对称性：
$$\langle j_i || T_\lambda || j_f \rangle = (-1)^{j_i - j_f} \langle j_f || T_\lambda^\dagger || j_i \rangle^*$$

---

## What It Can Establish

### 理论判据与可观测量

## What It Cannot Establish Alone

### 电多极（$E\lambda$）与磁多极（$M\lambda$）单粒子算符显式表达

### (1) 电多极跃迁算符 $\mathcal{M}(E\lambda, \mu)$
$$\mathcal{M}(E\lambda, \mu) = e_{\text{eff}} r^\lambda Y_{\lambda \mu}(\hat{r})$$
- **有效电荷（Effective Charge）**：
  由于核芯极化（Core Polarization）效应，价核子在核介质中的有效电荷偏离自由值：
  - 质子有效电荷：$e_{\text{eff}}(p) \approx (1 + \chi_p) e \approx 1.5 e$；
  - 中子有效电荷：$e_{\text{eff}}(n) \approx \chi_n e \approx 0.5 e$。
- **单粒子轨道约化矩阵元**：
  $$\langle n_f l_f j_f || \mathcal{M}(E\lambda) || n_i l_i j_i \rangle = e_{\text{eff}} \langle n_f l_f | r^\lambda | n_i l_i \rangle \cdot (-1)^{j_i + \lambda - 1/2} \frac{1 + (-1)^{l_f + l_i + \lambda}}{2} \sqrt{\frac{(2j_f + 1)(2\lambda + 1)(2j_i + 1)}{4\pi}} \begin{pmatrix} j_f & \lambda & j_i \\ 1/2 & 0 & -1/2 \end{pmatrix}$$

### (2) 磁多极跃迁算符 $\mathcal{M}(M\lambda, \mu)$
$$\mathcal{M}(M\lambda, \mu) = \mu_N \left[ g_l \vec{l} + g_s \vec{s} \right] \cdot \nabla [r^\lambda Y_{\lambda \mu}(\hat{r})]$$
- **自由核子 $g$ 因子与介质淬灭（Quenching）**：
  - 自由质子：$g_l(p) = 1$，$g_s(p) = +5.586$；
  - 自由中子：$g_l(n) = 0$，$g_s(n) = -3.826$；
  - 在原子核有限多体介质中，受 $\Delta$-空穴激发和二体介子交换流影响，自旋 $g$ 因子普遍发生约 $20\% \sim 30\%$ 的**自旋淬灭**：
    $$g_s^{\text{eff}} \approx 0.7 \sim 0.8 \times g_s^{\text{free}}$$
- **$M1$ 单粒子约化矩阵元（$\lambda=1$）**：
  $$\langle l_f j_f || \mathcal{M}(M1) || l_i j_i \rangle = \delta_{l_f, l_i} \sqrt{\frac{3}{4\pi}} \mu_N \cdot \left[ g_l \langle j_f || \vec{l} || j_i \rangle + g_s^{\text{eff}} \langle j_f || \vec{s} || j_i \rangle \right]$$

---

## 4. 减缩跃迁几率 $B(\sigma\lambda)$ 与半衰期 $T_{1/2}$ 的解析关联

减缩跃迁几率定义为对初态磁量子数平均、末态磁量子数求和：
$$B(\sigma\lambda; I_i \to I_f) = \frac{1}{2I_i + 1} |\langle I_f || \mathcal{M}(\sigma\lambda) || I_i \rangle|^2$$

跃迁放射几率 $\lambda_{\gamma}(\sigma\lambda)$（单位：$\text{s}^{-1}$）与 $B(\sigma\lambda)$ 严格相关：
$$\lambda_{\gamma}(E1) = 1.587 \times 10^{15} \cdot E_\gamma^3 \cdot B(E1) \quad [E_\gamma\text{ in MeV, } B(E1)\text{ in } e^2\text{fm}^2]$$
$$\lambda_{\gamma}(E2) = 1.225 \times 10^9 \cdot E_\gamma^5 \cdot B(E2) \quad [E_\gamma\text{ in MeV, } B(E2)\text{ in } e^2\text{fm}^4]$$
$$\lambda_{\gamma}(M1) = 1.758 \times 10^{13} \cdot E_\gamma^3 \cdot B(M1) \quad [E_\gamma\text{ in MeV, } B(M1)\text{ in } \mu_N^2]$$

能级的部分 $\gamma$ 半衰期为：$T_{1/2}^\gamma = \frac{\ln 2}{\lambda_\gamma}$。

---

## 5. 多体配对与 BCS 准粒子修正因子

当原子核进入开壳区，单粒子态被配对相互作用涂抹为 Bogoliubov 准粒子态：
$$a_j^\dagger = u_j c_j^\dagger - v_j \tilde{c}_j$$
其中 $v_j^2$ 为轨道占有几率，$u_j^2 + v_j^2 = 1$。
单体算符在单准粒子态之间的跃迁矩阵元乘上特征的 **BCS 配对减缩因子**：
- **对于电跃迁（时间反演宇称相同）**：
  $$\langle qp_f || \mathcal{M}(E\lambda) || qp_i \rangle = (u_i u_f - v_i v_f) \cdot \langle j_f || \mathcal{M}(E\lambda) || j_i \rangle_{\text{sp}}$$
- **对于磁跃迁（时间反演反转）**：
  $$\langle qp_f || \mathcal{M}(M\lambda) || qp_i \rangle = (u_i u_f + v_i v_f) \cdot \langle j_f || \mathcal{M}(M\lambda) || j_i \rangle_{\text{sp}}$$

**物理精要**：
在费米面附近的准粒子态之间，若 $u_i \approx u_f \approx 1/\sqrt{2}, v_i \approx v_f \approx 1/\sqrt{2}$，则电跃迁因子 $(u^2 - v^2) \approx 0$，电跃迁受到剧烈配对阻碍；而磁跃迁因子 $(u^2 + v^2) = 1$，磁跃迁保持畅通！这一配对微观机制解释了为何许多奇 $A$ 核低激发能级间的单准粒子交叉跃迁表现为近纯 $M1$ 辐射。


## Sources

- [[triaxial-collective-modes-unified-theory-and-spectroscopy]]
- [[nuclear-spectroscopy-and-structure-master-field-manual]]
