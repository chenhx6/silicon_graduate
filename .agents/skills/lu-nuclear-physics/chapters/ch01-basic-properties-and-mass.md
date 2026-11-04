# 第 1 章：原子核的基本性质、质量与结合能公式

**来源专著**：卢希庭《原子核物理（修订版）》（原子能出版社 2000）
**对应页码**：印刷 pp. 1–35 / 扫描 PDF pp. 11–45

---

## 1. 核心理论推导与物理模型

### 1.1 原子核的电荷、半径与密度分布
- **电荷数与中子数**：核素符号记为 ${}_Z^A X_N$，质量数 $A = Z + N$；
- **核电荷半径与物质半径**：由高能电子弹性散射与介子原子 X 射线精确测定，电荷分布服从两参数 Fermi 分布（Saxon-Woods 形状）：
  $$\rho(r) = \frac{\rho_0}{1 + \exp\left(\frac{r - R}{a}\right)},$$
  其中半密度半径 $R = r_0 A^{1/3}$（$r_0 \a1.07 - 1.12\text{ fm}$ 为方均根等效半径常数），弥散度表层厚度 $t \approx 4.4 a \approx 2.4\text{ fm}$；
- **核物质密度饱和性**：原子核中心核物质密度约为 $\rho_0 \a0.16\text{ nucleons/fm}^3 = 2.7 \times 10^{14}\text{ g/cm}^3$，不随质量数 $A$ 改变，证明核力具有强饱和性。

### 1.2 原子质量、结合能与分离能
- **原子核质量亏损**：
  $$\Delta M = Z M_H + (A - Z) M_n - M(A, Z);$$
- **总核结合能**：$B(A, Z) = \Delta M \cdot c^2$；
- **平均核子结合能（比结合能）**：$\epsilon = B(A, Z) / A$。轻核区比结合能陡峭上升并伴随 $\alpha$ 聚团峰（如 $^{4}\text{He}, {}^{12}\text{C}, {}^{16}\text{O}$）；在铁区（$^{56}\text{Fe}, {}^{62}\text{Ni}$）达到最高极值 $\sim 8.8\text{ MeV}$；随后因长程库仑排斥累积，重核区缓慢下降至 $\sim 7.5\text{ MeV}$（裂变产能的物理根源）。

### 1.3 Bethe-Weizsäcker 半经验质量公式（液滴模型）
卢希庭教材推导的 SEMF 标准形式为：
$$B(A, Z) = a_v A - a_s A^{2/3} - a_c \frac{Z(Z-1)}{A^{1/3}} - a_$C_{\text{sym}}$ \frac{(A - 2Z)^2}{A} + \delta(A, Z),$$
参数取值：$a_v = 15.56\text{ MeV}$，$a_s = 17.23\text{ MeV}$，$a_c = 0.697\text{ MeV}$，$a_$C_{\text{sym}}$ = 23.285\text{ MeV}$，$a_p = 12.0\text{ MeV}$。

### 1.4 $\beta$ 稳定谷中心电荷方程
对于固定奇数 $A$，原子核质量是 $Z$ 的单条抛物线；由极大结合能条件 $\partial B / \partial Z = 0$：
$$- \frac{a_c}{A^{1/3}} (2Z - 1) + 4 a_$C_{\text{sym}}$ \frac{A - 2Z}{A} = 0 \implies Z_{\text{stable}} = \frac{A}{2 + \frac{a_c}{2 a_$C_{\text{sym}}$} A^{2/3}} \approx \frac{A}{2 + 0.015 A^{2/3}}.$$
- 当 $Z < Z_{\text{stable}}$ 时，核素位于稳定谷左侧（中子过剩），发生 $\beta^-$ 衰变；
- 当 $Z > Z_{\text{stable}}$ 时，核素位于稳定谷右侧（质子过剩），发生 $\beta^+$ 衰变或轨道电子俘获（EC）。
