# 第 15 章：激发态微观寿命测量：RDM (DDCM) 与 DSAM 方法学

**来源专著**：吴治华《原子核物理实验方法》（第三版，原子能出版社 2005）
**对应页码**：印刷 pp. 421–452 / 扫描 PDF pp. 429–460 (§15.3 反冲距离多普勒法与 §15.4 多普勒频移衰减法)

---

## 1. 反冲距离多普勒法（RDM / Plunger）与差分衰变曲线法（DDCM）

### 1.1 传统 RDM 原理（$1\text{ ps} - 1\text{ ns}$）
- 重离子反应产生的高自旋复合核以速度 $v \sim 0.01 - 0.05\ c$ 冲出超薄自支撑靶箔；
- 在距靶 $d$ 处放置一片高 $Z$ 减速/阻止箔（Stopper，如 $10\text{ mg/cm}^2$ Au 或 Ta）；
- **双峰结构**：
  - 在飞行途中衰变的核子发射的 $\gamma$ 射线产生多普勒频移：$E_u = E_0 (1 + \beta \cos\theta)$（移动峰 Unshifted/Shifted）；
  - 在进入阻止箔完全停阻后衰变的核子发射无频移 $\gamma$ 射线：$E_s = E_0$（停止峰 Stopped）；
- 移动峰与停止峰的强度比：
  $$R(d) = \frac{I_u(d)}{I_u(d) + I_s(d)} = \exp\left(-\frac{d}{v \tau}\right).$$

### 1.2 差分衰变曲线法（DDCM）的数学飞跃
传统拟合严重受制于前级未知复杂级联侧馈（Side-feeding）的时间卷积。A. Dewald 等提出差分衰变曲线法（DDCM）：
由核能级布居速率平衡方程：
$$\frac{d N_i(t)}{dt} = -\frac{N_i(t)}{\tau_i} + \sum_j \lambda_{ji} N_j(t),$$
将时间变量变换为空间距离变量 $t = d/v$。在选定直接布居跃迁为门（Gated on directly feeding transition $B$）的条件下，侧馈项严格为零：
$$\tau(d) = \frac{I_s^A(d)}{v \cdot \frac{d}{dd} I_u^A(d)} = \frac{I_s^A(d)}{v \cdot \left| \frac{d I_s^A(d)}{dd} \right|}.$$
- **DDCM 核心优势**：在一条平坦的有效测量区域（Plateau region）内，寿命可以直接通过停止峰面积及其空间微商解析反演出来，彻底摆脱了复杂的级联多参数拟合！

---

## 2. 多普勒频移衰减法（DSAM，$\sim 10\text{ fs} - 2\text{ ps}$）

### 2.1 物理图像：离子在固体介质中的连续放慢
- 采用厚衬底靶（靶材直接真空压制在 $10 - 20\text{ mg/cm}^2$ 金或铅衬底上）；
- 反冲核产生后在衬底点阵中经历连续减速，速度从初速度 $v_0$ 衰减到零，总减速时间为 $t_{\text{stop}} \sim 1.0 - 1.5\text{ ps}$；
- 若核态平均寿命 $\tau < t_{\text{stop}}$，不同时刻衰变的核在不同速度 $v(t)$ 下发射 $\gamma$ 射线，探测器测得的谱线在基频 $E_0$ 与最大移动能量 $E_0(1 + \beta_0 \cos\theta)$ 之间形成连续延伸的**多普勒线形（Doppler Lineshape）**。

### 2.2 阻止本领与质心衰减因子 $F(\tau)$
- 反冲核受到的总阻止本领为电子阻止（Bethe-Bloch 机制，小角散射为主）与核阻止（Lindhard-Scharff-Schiøtt / ZBL 机制，弹性能核碰撞导致反冲轨迹偏折）：
  $$-\frac{dE}{dx} = \left(\frac{dE}{dx}\right)_e + \left(\frac{dE}{dx}\right)_n = S_e(v) + S_n(v).$$
- 平均多普勒频移因子：
  $$F(\tau) = \frac{\langle \Delta E \rangle}{\Delta E_m_{\max}} = \frac{\langle v(t) \cos\phi \rangle}{v_0} = \frac{1}{v_0 \tau} \int_0^\infty v(t) \overline{\cos\phi(t)} e^{-t/\tau} dt.$$
  通过测定各角度探头峰位漂移与线形不对称度，直接反演超短寿命 $\tau$，用于绝对跃迁几率 $B(E2)$、过渡四极矩 $Q_t$ 及核形变参数 $\beta_2$ 的绝对标定。
