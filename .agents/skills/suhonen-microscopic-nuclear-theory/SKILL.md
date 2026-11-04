---
name: suhonen-microscopic-nuclear-theory
description: Jouni Suhonen《From Nucleons to Nucleus》：微观核结构理论、角动量 Racah 代数与不可约球张量算符、Wigner-Eckart 定理标准相位约定、微观电磁跃迁算符、表面 delta 相互作用 (SDI)、BCS 配对准粒子平均场、准粒子随机相位近似 (QRPA) 与质中 pnQRPA Ikeda 求和规则。
---

<!-- argument-hint: [operator, racah, bcs, qrpa, pnqrpa, transition, or sum-rule] -->

# Jouni Suhonen 微观核结构理论与准粒子代数技能

本技能形式化芬兰于韦斯屈莱大学 Jouni Suhonen 教授权威专著《From Nucleons to Nucleus: Concepts of Microscopic Nuclear Theory》（Springer 2007，654 页，SHA-256 `4d4b799b...`）的微观核结构理论体系。
作为低能核物理微观理论与代数重耦合的核心法典，本技能为商业大模型提供从核子—核力微观算符、Racah 张量代数、BCS 准粒子平均场、QRPA 集体响应到 $\beta$ 衰变与电磁跃迁约化矩阵元的高精度数学物理规范。

---

## 核心微观核结构理论框架

### 1. 角动量代数与不可约球张量算符（Chapters 1–4）
- **不可约球张量算符定义**：
  Rank 为 $k$ 的不可约球张量算符 $T_q^{(k)}$（$q = -k, \dots, +k$）满足角动量对易关系：
  $$[J_z, T_q^{(k)}] = q T_q^{(k)}, \quad [J_\pm, T_q^{(k)}] = \sqrt{k(k+1) - q(q \pm 1)} T_{q \pm 1}^{(k)}$$
- **Wigner-Eckart 定理严格相位约定**：
  Suhonen 采用与 Edmonds、Bohr-Mottelson 完全自洽的标准相位定义：
  $$\langle j_f m_f | T_q^{(k)} | j_i m_i \rangle = (-1)^{2k} \frac{C_{j_i m_i k q}^{j_f m_f}}{\sqrt{2 j_f + 1}} \langle j_f || T^{(k)} || j_i \rangle = (-1)^{j_f - m_f} \begin{pmatrix} j_f & k & j_i \\ -m_f & q & m_i \end{pmatrix} \langle j_f || T^{(k)} || j_i \rangle$$
  其中约化矩阵元 $\langle j_f || T^{(k)} || j_i \rangle$ 独立于磁量子数 $m_i, m_f, q$。
- **张量积与重耦合（$6j$ 与 $9j$ 符号）**：
  两张量算符的耦合算符 $[P^{(k_1)} \otimes Q^{(k_2)}]^{(K)}$ 在耦合双体态间的约化矩阵元：
  $$\langle (j_1 j_2) J || [P^{(k_1)} \otimes Q^{(k_2)}]^{(K)} || (j_1' j_2') J' \rangle = \hat{J} \hat{J}' \hat{K} \begin{Bmatrix} j_1 & j_2 & J \\ j_1' & j_2' & J' \\ k_1 & k_2 & K \end{Bmatrix} \langle j_1 || P^{(k_1)} || j_1' \rangle \langle j_2 || Q^{(k_2)} || j_2' \rangle$$
  其中符号记法 $\hat{x} \equiv \sqrt{2x + 1}$。

---

### 2. 微观电磁多极跃迁算符与单粒子矩阵元（Chapters 6–7）
- **电多极算符（$E\lambda$）**：
  $$\mathcal{M}(E\lambda \mu) = \sum_{k=1}^A e_k r_k^\lambda Y_{\lambda \mu}(\hat{r}_k)$$
  单粒子约化矩阵元：
  $$\langle n_f l_f j_f || \mathcal{M}(E\lambda) || n_i l_i j_i \rangle = \frac{e_{\text{eff}}}{\sqrt{4\pi}} (-1)^{j_i + \lambda - 1/2} \frac{1 + (-1)^{l_f + l_i + \lambda}}{2} \hat{j}_f \hat{j}_i \hat{\lambda} \begin{pmatrix} j_f & \lambda & j_i \\ 1/2 & 0 & -1/2 \end{pmatrix} \langle n_f l_f | r^\lambda | n_i l_i \rangle$$
- **磁多极算符（$M\lambda$）**：
  $$\mathcal{M}(M\lambda \mu) = \mu_N \sum_{k=1}^A \left[ \frac{2}{\lambda+1} g_l^{(k)} \vec{l}_k + g_s^{(k)} \vec{s}_k \right] \cdot \nabla_k [r_k^\lambda Y_{\lambda \mu}(\hat{r}_k)]$$
  对于 $M1$ 跃迁算符：
  $$\mathcal{M}(M1 \mu) = \sqrt{\frac{3}{4\pi}} \mu_N [g_l \vec{l} + g_s \vec{s}]_\mu$$
- **跃迁概率 $B(\sigma\lambda)$ 与单粒子 Weisskopf 单位**：
  $$B(\sigma\lambda; I_i \to I_f) = \frac{1}{2I_i + 1} |\langle I_f || \mathcal{M}(\sigma\lambda) || I_i \rangle|^2$$
  $$B_{\text{sp}}(E\lambda) = \frac{(1.2)^\lambda}{4\pi} \left( \frac{3}{\lambda+3} \right)^2 A^{2\lambda/3}\ [e^2\text{ fm}^{2\lambda}]$$
  $$B_{\text{sp}}(M\lambda) = \frac{10}{\pi} (1.2)^{\lambda-1} \left( \frac{3}{\lambda+2} \right)^2 A^{(2\lambda-2)/3}\ [\mu_N^2\text{ fm}^{2\lambda-2}]$$

---

### 3. 表面 Delta 相互作用与两体剩余相互作用（Chapter 8）
- **SDI 势形式**：
  $$V_{\text{SDI}}(1, 2) = -4\pi V_0 \delta(\vec{r}_1 - \vec{r}_2) \delta(r_1 - R_0)$$
  假定核内相互作用主要发生在核表面，所有单粒子径向波函数在表面具有相同取值 $R_{nl}(R_0) = \text{const}$。
- **反对称化耦合两粒子矩阵元解析解**：
  $$\langle j_a j_b; J T | V_{\text{SDI}} | j_c j_d; J T \rangle = -\frac{V_0}{2(1 + \delta_{ab})^{1/2}(1 + \delta_{cd})^{1/2}} (-1)^{l_a + l_c} \hat{j}_a \hat{j}_b \hat{j}_c \hat{j}_d \sum_L \hat{L}^2 \begin{pmatrix} j_a & j_c & L \\ 1/2 & -1/2 & 0 \end{pmatrix} \begin{pmatrix} j_b & j_d & L \\ 1/2 & -1/2 & 0 \end{pmatrix} [1 - (-1)^{J + T} (-1)^{j_c + j_d}]$$
  提供了无自由参数的紧凑两体剩余相互作用基准，完全避免了经验矩阵元的任意性。

---

### 4. BCS 准粒子平均场与配对理论（Chapters 13–14）
- **Bogoliubov-Valatin 变换与时间反演准粒子算符**：
  $$a_{j m}^\dagger = u_j c_{j m}^\dagger - (-1)^{j-m} v_j c_{j, -m}$$
  $$a_{j m} = u_j c_{j m} - (-1)^{j-m} v_j c_{j, -m}^\dagger$$
  正规化条件：$u_j^2 + v_j^2 = 1$。
- **BCS 能隙方程与化学势 $\lambda$ 方程**：
  $$\Delta_a = \frac{1}{2} \sum_b \frac{G \hat{j}_b}{\hat{j}_a} \frac{\Delta_b}{E_b}, \quad \text{其中 } E_a = \sqrt{(\varepsilon_a - \lambda)^2 + \Delta_a^2}$$
  粒子数守恒条件：
  $$\langle \text{BCS} | \hat{N} | \text{BCS} \rangle = \sum_a (2j_a + 1) v_a^2 = N$$
  占据几率与非占几率：
  $$v_a^2 = \frac{1}{2} \left[ 1 - \frac{\varepsilon_a - \lambda}{E_a} \right], \quad u_a^2 = \frac{1}{2} \left[ 1 + \frac{\varepsilon_a - \lambda}{E_a} \right]$$
- **准粒子表象下的电磁跃迁约化矩阵元**：
  两准粒子态间电多极跃迁带有相消因子 $(u_a u_b - v_a v_b)$，而磁多极跃迁带有相加因子 $(u_a u_b + v_a v_b)$：
  $$\langle a b; J || \mathcal{M}(E\lambda) || \text{BCS} \rangle = \frac{1}{\sqrt{1 + \delta_{ab}}} (u_a v_b + v_a u_b) \langle a || \mathcal{M}(E\lambda) || b \rangle$$
  $$\langle a || \mathcal{M}(E\lambda) || b \rangle_{\text{1qp}} = (u_a u_b - v_a v_b) \langle a || \mathcal{M}(E\lambda) || b \rangle_{\text{sp}}$$
  $$\langle a || \mathcal{M}(M\lambda) || b \rangle_{\text{1qp}} = (u_a u_b + v_a v_b) \langle a || \mathcal{M}(M\lambda) || b \rangle_{\text{sp}}$$

---

### 5. 准粒子随机相位近似 (QRPA) 与同位旋 pnQRPA（Chapters 18–19）
- **QRPA 声子激发算符**：
  $$Q_\omega^\dagger = \sum_{a \le b} [X_{ab}^\omega A^\dagger(ab; J M) - Y_{ab}^\omega \tilde{A}(ab; J M)]$$
  其中准粒子对产生算符 $A^\dagger(ab; J M) \equiv [a_a^\dagger \otimes a_b^\dagger]_{JM}$。
- **QRPA 运动方程与超矩阵结构**：
  $$\begin{pmatrix} A & B \\ -B^* & -A^* \end{pmatrix} \begin{pmatrix} X^\omega \\ Y^\omega \end{pmatrix} = \hbar\omega \begin{pmatrix} X^\omega \\ Y^\omega \end{pmatrix}$$
  正规化条件：$\sum_{a \le b} [|X_{ab}^\omega|^2 - |Y_{ab}^\omega|^2] = 1$。
- **质中 QRPA (pnQRPA) 与 Ikeda 严格求和规则**：
  pnQRPA 描述母核向奇奇子核的荷电多极激发（$\beta^-$ 与 $\beta^+$ 通道）。
  Gamow-Teller 算符 $\beta_\mp = \sum_k \tau_\mp^{(k)} \vec{\sigma}_k$。
  **Ikeda 求和规则**基于对易关系的微观精确恒等式：
  $$S_- - S_+ \equiv \sum_f B(\text{GT}^-; i \to f) - \sum_{f'} B(\text{GT}^+; i \to f') = 3(N - Z)$$
  该式在任意单核子局域势和完整多粒子希尔伯特空间中均严格成立，不受粒子-粒子相互作用参数 $g_{\text{pp}}$ 影响，构成了微观核物理弱相互作用的黄金基准。
- **$g_{\text{pp}}$ 相消机制与 $2\nu\beta\beta$ 衰变矩阵元**：
  粒子-粒子道相互作用参数 $g_{\text{pp}}$ 随强度增加产生两准粒子基态关联，导致 $\beta^+$ 振幅与 $2\nu\beta\beta$ 跃迁矩阵元 $M^{2\nu}$ 发生剧烈相消抑制；当 $g_{\text{pp}} \to g_{\text{pp}}^n_{\text{crit}}$ 时，QRPA 发生集体破缺相变。
