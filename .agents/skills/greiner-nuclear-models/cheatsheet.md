# Cheatsheet: Greiner 核模型与集体转动公式速查卡

Davydov-Filippov 能级与分支比表、RVM 转动振动公式、Wilets-Jean 软核与巨共振和则速查卡。

---

## 1. Davydov-Filippov 模型随 $\gamma$ 形变角演化速查表

| 三轴形变角 $\gamma$ | $\sin^2(3\gamma)$ | 能量比 $R_{22/21} = \frac{E(2_2^+)}{E(2_1^+)}$ | $R_{4/2} = \frac{E(4_1^+)}{E(2_1^+)}$ | 分支比 $\frac{B(E2; 2_2^+ \to 0_1^+)}{B(E2; 2_2^+ \to 2_1^+)}$ | 物理极限图像 |
|---|---|---|---|---|---|
| **$0^\circ$** | $0.000$ | $+\infty$ (准 $\gamma$ 带无限抬升) | $3.333$ | $0.0000$ | 轴对称长椭转子极限 (Prolate) |
| **$5^\circ$** | $0.067$ | $28.85$ | $3.328$ | $0.0107$ | 极微弱非轴对称扰动 |
| **$10^\circ$** | $0.250$ | $8.00$ | $3.273$ | $0.0435$ | 弱三轴形变 |
| **$15^\circ$** | $0.500$ | $4.24$ | $3.155$ | $0.0952$ | 中度三轴形变 |
| **$20^\circ$** | $0.750$ | $2.91$ | $2.986$ | $0.1500$ | 强三轴形变 |
| **$25^\circ$** | $0.933$ | $2.26$ | $2.802$ | $0.1738$ | 极强三轴形变 |
| **$30^\circ$** | $1.000$ | **$2.000$ (理论极小值)** | **$2.667$** | **$0.1750$ ($7/40$, 理论极小值)** | **极大三轴不对称极限 (Maximal Triaxiality)** |

---

## 2. Davydov-Filippov 模型高自旋解析能级公式

基底为对称化 Wigner 函数 $|IMK\rangle_$C_{\text{sym}}$$，能量以 $\epsilon_0 = \frac{\hbar^2}{4 B \beta^2}$ 为自然单位：

1. **$I=2^+$ 能级（二重分裂）**：
   $$E(2_1^+, 2_2^+) = \frac{9 \epsilon_0}{\sin^2(3\gamma)} \left[ 1 \mp \sqrt{1 - \frac{8}{9}\sin^2(3\gamma)} \right]$$
2. **$I=3^+$ 能级（单态）**：
   $$E(3_1^+) = \frac{18 \epsilon_0}{\sin^2(3\gamma)} \equiv E(2_1^+) + E(2_2^+) \quad (\text{严格求和恒等式})$$
3. **$I=4^+$ 能级（三重分裂）**：
   本征能量满足三次代数特征方程：
   $$E^3 - \frac{120 \epsilon_0}{\sin^2(3\gamma)} E^2 + \left[ \frac{3600}{\sin^4(3\gamma)} - \frac{2304}{\sin^2(3\gamma)} \right] \epsilon_0^2 E - \frac{28800 \epsilon_0^3}{\sin^4(3\gamma)} \cos^2(3\gamma) = 0$$

---

## 3. Faessler-Greiner 转动振动模型 (RVM) 能级公式卡

围绕轴对称长椭基态平衡形变 $(\beta_0, \gamma=0)$，小振幅拉格朗日展开给出解析能谱：

$$E(I, K, n_\beta, n_\gamma) = \left( n_\beta + \frac{1}{2} \right) \hbar\omega_\beta + \left( 2 n_\gamma + 1 + \frac{1}{2}|K| \right) \hbar\omega_\gamma + \frac{\hbar^2}{2\mathcal{J}_0} \left[ I(I+1) - K^2 \right]$$

| 集体能带类别 | 振动量子数 $(n_\beta, n_\gamma)$ | 角动量投影 $K^\pi$ | 允许自旋序列 $I$ | 带首能量（以基态为零点） |
|---|---|---|---|---|
| **基带 (Ground Band)** | $(0, 0)$ | $0^+$ | $0^+, 2^+, 4^+, 6^+, \dots$ | $0\text{ keV}$ |
| **$\beta$ 振动带 ($\beta$ Band)** | $(1, 0)$ | $0^+$ | $0^+, 2^+, 4^+, 6^+, \dots$ | $\hbar\omega_\beta$ |
| **$\gamma$ 振动带 ($\gamma$ Band)** | $(0, 0)$ | $2^+$ | $2^+, 3^+, 4^+, 5^+, \dots$ | $\hbar\omega_\gamma - \frac{2\hbar^2}{\mathcal{J}_0}$ |
| **双声子 $\gamma\gamma$ 振动带** | $(0, 1)$ | $0^+, 4^+$ | $0^+, 2^+, 4^+ \dots$ 与 $4^+, 5^+, 6^+ \dots$ | $2\hbar\omega_\gamma$ |

- **离心拉伸修正 (Variable Moment of Inertia)**：
  在基带高自旋区，有效转动惯量按四极拉伸修正：$\mathcal{J}_{\text{eff}}(I) \approx \mathcal{J}_0 [1 + 6(\frac{\hbar}{\mathcal{J}_0 \omega_\beta})^2 I(I+1)]$。

---

## 4. 三大集体转动模型核心特征判据对比

| 结构特征与观测量 | 轴对称长椭转子 (Bohr-Mottelson) | 刚性三轴转子 (Davydov-Filippov) | 完全 $\gamma$ 软核 (Wilets-Jean / O(6)) |
|---|---|---|---|
| $R_{4/2} = E(4_1^+)/E(2_1^+)$ | $3.333$ | $2.667 - 3.333$ ($\gamma=30^\circ$ 时为 $2.67$) | **$2.500$** |
| $R_{22/21} = E(2_2^+)/E(2_1^+)$ | $\gg 10$ (极高，不形成低激发带) | **$2.00 - 8.00$** | **$2.00 - 2.50$** |
| $E(3_1^+)$ 与三态和则 | 不满足 | 严格满足 $E(3_1^+) \equiv E(2_1^+) + E(2_2^+)$ | 不满足 (呈现 $E(3_1^+) \approx E(4_1^+)$ 简并) |
| 能级聚集配对形态 | 单一基态转动带 | $(2_\gamma^+, 3_\gamma^+)$、$(4_\gamma^+, 5_\gamma^+)$ 成对聚集 | $(3_\gamma^+, 4_\gamma^+)$、$(5_\gamma^+, 6_\gamma^+)$ 成对聚集 |
| 能级交错指数 $S(J)$ | — | **负交错** (偶数自旋处为深谷) | **正交错** (偶数自旋处为峰值) |
| $0^+ \to 1^+$ 剪刀模式 | 无 (缺少同位旋相对取向) | 存在强 $M1$ 激发 | 减弱或破碎为多重声子态 |

---

## 5. 巨多极共振 (Giant Resonances) 宏观流体动力学常数卡

| 巨共振模式 | 标度律 (GT vs SJ) | 经验中心共振能量 $E_{\text{res}}$ | 典型共振宽度 $\Gamma$ | 能量加权求和规则 (EWSR) 耗尽比例 |
|---|---|---|---|---|
| **等标巨单极共振 (ISGMR)** | 单核子声学压缩波 | $E_{\text{GMR}} \a80 A^{-1/3}\text{ MeV}$ | $3.0 - 4.5\text{ MeV}$ | 耗尽 $100\%$ 单极求和，提取核不可压缩系数 $K_\infty \approx 240\text{ MeV}$ |
| **等矢巨偶极共振 (IVGDR)** | GT: $A^{-1/6}$，SJ: $A^{-1/3}$ | $E_{\text{GDR}} \approx 31.2 A^{-1/3} + 20.6 A^{-1/6}\text{ MeV}$ | $4.0 - 6.0\text{ MeV}$ | 耗尽 $100\% - 120\%$ TRK 求和规则：$\sigma_{\text{TRK}} = 60 \frac{NZ}{A}\text{ MeV}\cdot\text{mb}$ |
| **等标巨四极共振 (ISGQR)** | 表面四极无旋流形变波 | $E_{\text{GQR}} \approx 64 A^{-1/3}\text{ MeV}$ | $3.5 - 5.0\text{ MeV}$ | 耗尽 $100\%$ 能量加权四极求和规则 |
