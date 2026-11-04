# 第 5 章：$\alpha$ 衰变动力学与 Gamow 势垒穿透理论

**来源专著**：卢希庭《原子核物理（修订版）》（原子能出版社 2000）
**对应页码**：印刷 pp. 113–128 / 扫描 PDF pp. 123–138

---

## 1. 核心理论推导与数学方程

### 1.1 $\alpha$ 衰变能与 Geiger-Nuttall 定律
- 衰变能计算（质量亏损）：
  $$Q_\alpha = [M(A, Z) - M(A-4, Z-2) - M_\alpha] c^2;$$
- $\alpha$ 粒子的出射动能（反冲核动能修正）：
  $$E_\alpha = \frac{A - 4}{A} Q_\alpha.$$
- **Geiger-Nuttall 经验定律**：衰变常数对数与动能平方根成反比：
  $$\log \lambda = A - \frac{B}{\sqrt{E_\alpha}}.$$
  动能仅仅改变一倍（$4\text{ MeV} \to 8\text{ MeV}$），半衰期跨越惊人的 24 个数量级（$10^{10}\text{ 年} \to 10^{-7}\text{ 秒}$），这是量子隧道穿透几率对能垒高度极度敏感的典型宏观表现。

### 1.2 Gamow 量子势垒穿透理论（WKB 近似）
- **物理图像**：$\alpha$ 粒子预先在核内以一定几率形成（预形成因子 $P_\alpha \sim 0.1 - 1.0$），在半径为 $R$ 的核势阱内以频率 $\nu_0 = v / (2R) \sim 10^{21}\text{ s}^{-1}$ 频繁碰撞核表面势垒。
- **库仑势垒与经典转折点**：
  $$V_C(r) = \frac{2 (Z - 2) e^2}{4\pi\varepsilon_0 r}, \quad b = \frac{2 (Z - 2) e^2}{4\pi\varepsilon_0 Q_\alpha}.$$
- **WKB 穿透几率积分**：
  $$P = \exp\left( - 2 \int_R^b \sqrt{\frac{2M_\alpha}{\hbar^2} [V_C(r) - Q_\alpha]} dr \right) \approx \exp\left( - 2 \gamma_G \right),$$
  其中 Gamow 因子为：
  $$\gamma_G = \sqrt{\frac{2M_\alpha Q_\alpha}{\hbar^2}} \int_R^b \sqrt{\frac{b}{r} - 1} dr = \frac{2(Z-2)e^2}{\hbar v} \left( \arccos\sqrt{\frac{R}{b}} - \sqrt{\frac{R}{b}\left(1 - \frac{R}{b}\right)} \right).$$
  在 $R \ll b$ 的超长半衰期近似下：
  $$\lambda = \nu_0 \cdot P \approx \nu_0 \exp\left[ - \frac{4\pi (Z-2)e^2}{\hbar v} + 8 \sqrt{\frac{(Z-2)e^2 M_\alpha R}{\hbar^2}} \right].$$
  严格从薛定谔方程解析推导出了 Geiger-Nuttall 定律。

### 1.3 离心势垒与角动量阻碍因子
若 $\alpha$ 粒子出射带有轨道角动量 $L > 0$，势垒叠加离心势项 $V_L(r) = \frac{\hbar^2 L(L+1)}{2 M_\alpha r^2}$，穿透几率被进一步压低。阻碍因子定义为：
$$HF = \frac{T_{1/2}^{\text{exp}}}{T_{1/2}^{\text{theo}}(L=0)}.$$
$HF \a1$ 对应基态到基态的允许跃迁（$0^+ \to 0^+$）；$HF \gg 1$ 强烈预示出射粒子带有角动量改变或涉及破对非单粒子态。
