# Cheatsheet: A. A. Raduta 相干态核结构理论速查卡

半经典相空间分离线、Holstein-Primakoff 展开、CSM 角动量投影与偶偶手征带速查卡。

---

## 1. 半经典三轴转子相空间极值点与分离线方程速查卡

设三主轴转动惯量按形状轴排序为：$\mathcal{J}_m > \mathcal{J}_s > \mathcal{J}_l$（中间形变轴为最大惯量轴，短轴为中间惯量轴，长轴为最小惯量轴）。

| 经典相空间定点类别 | 对应物理主轴 | 正则坐标 $(p_\phi = I_z, \phi)$ | 经典能量 $E$ | 局部动力学稳定性 | 量子力学对应激发模式 |
|---|---|---|---|---|---|
| **极小值椭圆定点** | 中间轴 ($m$ 轴) | $I_z = \pm I, \phi = 0$ | $E_{\min} = \frac{I^2}{2 \mathcal{J}_m}$ | **李雅普诺夫稳定** | 稳定主轴进动 (量子基准态) |
| **极大值椭圆定点** | 长轴 ($l$ 轴) | $I_z = 0, \phi = 90^\circ$ | $E_m_{\max} = \frac{I^2}{2 \mathcal{J}_l}$ | **李雅普诺夫稳定** | 高能量环流进动态 |
| **双曲马鞍点 (Saddle)** | 短轴 ($s$ 轴) | $I_z = 0, \phi = 0^\circ$ | **$E_n_{\text{crit}} = \frac{I^2}{2 \mathcal{J}_s}$** | **非稳定 (渐近轨道)** | **分离线 (Separatrix) 临界鞍点** |

---

## 2. Holstein-Primakoff 玻色子展开在高自旋摆动中的展开公式

取最大转动惯量轴为量子化 $z$ 轴，自旋算符展开为单模玻色子 $a, a^\dagger$：

$$I_z = I - a^\dagger a, \quad I_+ = \sqrt{2I - a^\dagger a} \cdot a, \quad I_- = a^\dagger \sqrt{2I - a^\dagger a}$$

1. **二阶谐振子项（零阶小振幅简谐摆动近似）**：
   $$\hat{H}_2 = E_0(I) + \hbar\omega_w \left( a^\dagger a + \frac{1}{2} \right), \quad \hbar\omega_w = I \sqrt{\left(\frac{1}{\mathcal{J}_x} - \frac{1}{\mathcal{J}_z}\right)\left(\frac{1}{\mathcal{J}_y} - \frac{1}{\mathcal{J}_z}\right)}$$
2. **四阶非简谐微扰项（非线性声子相互作用）**：
   $$\hat{H}_4 = V_4 a^\dagger a^\dagger a a + V_{4}' (a^\dagger a^\dagger + a a), \quad V_4 = -\frac{\hbar\omega_w}{4 I} \left[ 1 + \frac{(\mathcal{J}_x - \mathcal{J}_y)^2}{2(\mathcal{J}_x - \mathcal{J}_z)(\mathcal{J}_y - \mathcal{J}_z)} \right]$$
   - 展开适用条件：多声子数满足 $n_w \ll 2I$；当 $n_w$ 接近分离线时，四次项引起摆动声子能量强烈下弯软化。

---

## 3. CSM 相干态模型三维角动量投影核心公式卡

$$|\psi(d)\rangle = \exp[d (b_{20}^\dagger - b_{20})] |0\rangle = e^{-d^2/2} \sum_{n=0}^\infty \frac{d^n}{\sqrt{n!}} |n, 0\rangle$$

1. **连续角动量投影正规化积分核**：
   $$N_I^2(d) = (2I+1) e^{-d^2} \int_0^1 P_I(x) \exp\left[ d^2 P_2(x) \right] dx$$
2. **三条集体能带波函数微观构建**：
   - **基态带 (Ground Band)**：$|\phi_M^I(g)\rangle = \frac{1}{N_I^{(g)}} \hat{P}_{M0}^I |\psi(d)\rangle$；
   - **$\beta$ 振动带 ($\beta$ Band)**：$|\phi_M^I(\beta)\rangle = \frac{1}{N_I^{(\beta)}} \hat{P}_{M0}^I \left[ \hat{\Omega}_\beta^\dagger |\psi(d)\rangle \right]$；
   - **$\gamma$ 振动带 ($\gamma$ Band)**：$|\phi_M^I(\gamma)\rangle = \frac{1}{N_I^{(\gamma)}} \hat{P}_{M2}^I \left[ b_{22}^\dagger |\psi(d)\rangle \right]$。

---

## 4. GCSM 偶偶核手征双重带关键判据卡

由质子四极玻色子 $\vec{J}_\pi$、中子四极玻色子 $\vec{J}_\nu$ 与破对两准粒子费米子对 $\vec{J}_f$ 构成正交手征三面体：

| 手征观测特征项 | 偶偶核手征双重带表现 | 竞争假模式（形状共存或带交叉）表现 |
|---|---|---|
| **自旋宇称序列** | 孪生两带均为正宇称：$I^\pi = 10^+, 12^+, 14^+, \dots$ | 宇称相反或自旋交错不匹配 |
| **带间能量裂距 $\Delta E(I)$** | 在中自旋区呈现深极小（$\Delta E \le 50 - 150\text{ keV}$） | 随自旋单调发散或交叉后急剧增大 |
| **带间磁偶极跃迁 $B(M1; I \to I)$** | **显著集体增强：$B(M1) \a0.1 - 0.5\ \mu_N^2$** | 强烈阻碍：$B(M1) \ll 0.01\ \mu_N^2$ |
| **$S_{M1}(I)$ 奇偶交错参量** | 孪生两带内部 $S_{M1}(I)$ 呈现严格同相振荡 | 反相交错或无交错振荡 |
| **转动惯量 $\mathcal{J}^{(2)}$ 相似度** | 两带动力学转动惯量高度重合（偏差 $< 10\%$） | 两带转动惯量截然不同 |

---

## 5. 典型手征-八极宇称四重带核素微观参数速查表

| 核素 | 支配微观准粒子组态 | 宇称四重带能级范围 | 带间 $B(E1)$ 跃迁强度 | 物理机制与微观结构 |
|---|---|---|---|---|
| **$^{130}\text{Cs}$** | $\pi h_{11/2} \otimes \nu h_{11/2} \otimes \text{Octupole } 3^-$ | $I = 10^\pm \sim 18^\pm$ | $B(E1) \sim 10^{-3} - 10^{-2}\text{ W.u.}$ | 手征对称性破缺与八极振动声子强相干耦合 |
| **$^{132}\text{Cs}$** | $\pi h_{11/2} \otimes \nu h_{11/2}$ 软八极相干核芯 | $I = 9^\pm \sim 16^\pm$ | $B(E1) \sim 5 \times 10^{-3}\text{ W.u.}$ | 跨宇称电偶极网络强化 |
| **$^{78}\text{Br}$** | $\pi g_{9/2} \otimes \nu g_{9/2}$ 与动态反射不对称 | $I = 8^\pm \sim 14^\pm$ | $B(E1) \sim 10^{-3}\text{ W.u.}$ | $A \sim 80$ 手征岛中的手征-八极宇称四重带标杆 |
