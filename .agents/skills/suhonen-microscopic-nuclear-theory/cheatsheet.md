# Jouni Suhonen 微观核理论数学物理速查卡

### 1. 常用 3j 与 6j 符号恒等式
- 正交归一关系：
  $$\sum_{m_1 m_2} (2j_3 + 1) \begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix} \begin{pmatrix} j_1 & j_2 & j_3' \\ m_1 & m_2 & m_3' \end{pmatrix} = \delta_{j_3 j_3'} \delta_{m_3 m_3'}$$
- 交换对称性：
  $$\begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix} = (-1)^{j_1 + j_2 + j_3} \begin{pmatrix} j_2 & j_1 & j_3 \\ m_2 & m_1 & m_3 \end{pmatrix} = \begin{pmatrix} j_2 & j_3 & j_1 \\ m_2 & m_3 & m_1 \end{pmatrix}$$
- 零动量自旋球谐 $3j$ 符号：
  $$\begin{pmatrix} j & j & 0 \\ m & -m & 0 \end{pmatrix} = \frac{(-1)^{j-m}}{\sqrt{2j + 1}}$$

---

### 2. 单粒子 Weisskopf 单位数值速查表（$A$ 为核子数）

| 多极类型 | Weisskopf 估算值 $B_{\text{sp}}(\sigma\lambda)$ | 典型量级 ($A=130$) |
|---|---|---|
| $E1$ | $6.446 \times 10^{-4} A^{2/3}\ [e^2\text{ fm}^2]$ | $0.0165\ [e^2\text{ fm}^2]$ |
| $E2$ | $5.940 \times 10^{-2} A^{4/3}\ [e^2\text{ fm}^4]$ | $38.2\ [e^2\text{ fm}^4]$ |
| $E3$ | $5.940 \times 10^{-2} A^2\ [e^2\text{ fm}^6]$ | $1003.8\ [e^2\text{ fm}^6]$ |
| $M1$ | $1.790\ [\mu_N^2]$ | $1.790\ [\mu_N^2]$ |
| $M2$ | $1.650 A^{2/3}\ [\mu_N^2\text{ fm}^2]$ | $42.3\ [\mu_N^2\text{ fm}^2]$ |

---

### 3. 核子自由 $g$ 因子与标准淬灭因子
- 质子自由 $g$ 因子：$g_l^p = 1.0, \quad g_s^p = +5.586$
- 中子自由 $g$ 因子：$g_l^n = 0.0, \quad g_s^n = -3.826$
- 实验标准淬灭因子：$g_s^{\text{eff}} = 0.70 \times g_s^{\text{free}}$（高阶组态混合与 $\Delta(1232)$ 极化效应）
- 轴矢量弱相互作用常数：$g_A^{\text{free}} = 1.27$，核内淬灭值 $g_A^{\text{eff}} \a0.8 - 1.0$

---

### 4. BCS 准粒子跃迁干涉因子表

| 激发过程 | 电多极跃迁 ($E\lambda$) | 磁多极跃迁 ($M\lambda$) | 物理效应 |
|---|---|---|---|
| 基态 $\to$ 2qp 态 | $(u_a v_b + v_a u_b)$ | $(u_a v_b - v_a u_b)$ | 电跃迁相加相干增强（E2 集体振动机制） |
| 1qp $\to$ 1qp 态 | $(u_a u_b - v_a v_b)$ | $(u_a u_b + v_a v_b)$ | 电跃迁费米面相消；磁跃迁稳健无相消 |
| 2qp 湮灭 $\to$ 基态 | $(v_a u_b + u_a v_b)$ | $(v_a u_b - u_a v_b)$ | 逆过程与激发过程满足微观时间反演共轭 |
