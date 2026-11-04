# Glossary: W. D. Hamilton 核谱学电磁相互作用专业术语规范

本术语表汇编 W. D. Hamilton《The Electromagnetic Interaction in Nuclear Spectroscopy》（North-Holland，1975）中的核心专业术语、中英文对照及严密物理定义，为辐射多极性、角分布、角关联与线偏振分析提供统一权威术语标准。

---

## 1. 统计取向与核态张量 (Nuclear Orientation and Statistical Tensors)

- **Statistical Tensor (统计张量 $\rho_{kq}(I)$ / 状态密度矩阵)**: 描述具有自旋 $I$ 的量子系综在空间各磁子态 $m$ 上布居概率分布与相干相位的张量算符展开系数。
- **Orientation Parameter (轴对称取向参数 $B_k(I)$)**: 在轴对称（无方位角偏倚，使得非对角相干项 $\rho_{kq \ne 0} = 0$）核反应或极化系统中，描述磁子态布居偏离球对称各向同性程度的偶数阶无量纲张量：$B_k(I) = \sqrt{2I+1} \sum_m (-1)^{I-m} \langle I m I -m | k 0 \rangle P(m)$。
- **Spin Alignment Width ($\sigma/I$, 自旋取向高斯分布宽度)**: 在重离子熔合反应中描述磁子态高斯布居 $P(m) \propto \exp(-m^2/2\sigma^2)$ 弥散度的特征比值；通常在束反应中 $\sigma/I \a0.28 - 0.35$。
- **Complete Alignment (完全取向极限)**: 所有自旋严格对齐在反应平面垂直轴（即 $m=0$ 纯态占据，$P(m) = \delta_{m0}$）的理论极限状态。
- **Cascade Deorientation Factor (级联去取向系数 $U_k(I_a I_b L)$)**: 描述未被实验探测器观测到的中间级联跃迁由于发射光子带走随机角动量导致子能级取向张量发生幅度衰减的纯几何缩放因子。

---

## 2. 角分布与几何系数 (Directional Distributions and Angular Coefficients)

- **Directional Distribution (方向角分布 $W(\theta)$)**: 轴对称对齐核态发射的单个 $\gamma$ 光子在空间相对于束流轴夹角 $\theta$ 的相对微分角发射几率分布：$W(\theta) = 1 + A_2 P_2(\cos\theta) + A_4 P_4(\cos\theta)$。
- **Legendre Polynomials (勒让德多项式 $P_k(\cos\theta)$)**: 角分布函数正交基底，$P_2(x) = \frac{1}{2}(3x^2 - 1)$，$P_4(x) = \frac{1}{8}(35x^4 - 30x^2 + 3)$。
- **Ferentz-Rosenzweig Coefficient ($F_k(L L' I_f I_i)$, 几何 $F$ 系数)**: 连接初始自旋 $I_i$、终态自旋 $I_f$ 与两辐射多极阶数 $L, L'$ 的纯角动量 Racah 几何重耦合系数。
- **Multipole Mixing Ratio ($\delta(L'/L)$, 多极混合比)**: 高一阶多极跃迁矩阵元与最低多极跃迁矩阵元在幅值与相对代数符号上的比值：$\delta \equiv \langle I_f || \mathcal{M}_{L'} || I_i \rangle / \langle I_f || \mathcal{M}_L || I_i \rangle$。
- **Dual-Root Degeneracy (双根退化 / 混合比双值多解)**: 由于角分布各向异性系数 $A_2$ 是关于 $\delta$ 的二次有理分式，一个实测 $A_2$ 值通常严格对应两个数学等价的解根（小根 $\delta_1 \approx 0$ 与大根 $\delta_2 \sim 3 - 8$）。

---

## 3. 方向角关联与符合比值 (Directional Correlations and DCO)

- **Directional Correlation (方向角关联 / 符合角分布)**: 两个或多个相继发射的级联 $\gamma$ 光子在空间不同探测角度被同时符合探测时的联合概率分布函数 $W(\theta_1, \theta_2, \Delta\phi)$。
- **DCO Ratio (定向态方向角关联比值 $R_{\text{DCO}}$)**: 在大探测器阵列中，探测器 1 置于特定角度 $\theta_1$ 与探测器 2 置于 $\theta_2$ 之间，反转门控探测器所测得的双重符合峰面积强度比值。
- **Stretched Transition (拉伸跃迁)**: 角动量变化量严格等于辐射多极阶数（$\Delta I = I_i - I_f = L$）的电磁跃迁（如 $\Delta I = 2$ 的拉伸 $E2$ 或 $\Delta I = 1$ 的拉伸 $E1/M1$）。
- **Non-Stretched Transition (非拉伸跃迁)**: 自旋变化量小于多极阶数（如 $\Delta I = 0$ 的非拉伸偶极跃迁或四极跃迁）。

---

## 4. 康普顿线偏振度测量 (Compton Linear Polarimetry)

- **Linear Polarization ($P(\theta)$, 康普顿线偏振度)**: $\gamma$ 光子电矢量平行于反应平面振动的强度与垂直于反应平面强度的相对归一化不对称度：$P(\theta) = \frac{W(\theta, \psi=90^\circ) - W(\theta, \psi=0^\circ)}{W(\theta, \psi=90^\circ) + W(\theta, \psi=0^\circ)}$。
- **Electric/Magnetic Parity Selection (电/磁宇称正负号选择法则)**: 在固定角度 $\theta = 90^\circ$ 处，电性跃迁（$EL$）的理论线偏振度 $P(90^\circ) > 0$（正偏振），而磁性跃迁（$ML$）的理论线偏振度 $P(90^\circ) < 0$（负偏振）；该符号反转是排他性甄别跃迁宇称变化的决定性物理判据。
- **Compton Scattering Asymmetry ($A_{\text{asym}}$, 散射不对称度)**: 康普顿偏振仪或分段 Clover 探测器内部相邻晶体垂直散射计数 $N_\perp$ 与平行散射计数 $N_\parallel$ 的相对差值：$A_{\text{asym}} = \frac{N_\perp - a_{\text{geom}} N_\parallel}{N_\perp + a_{\text{geom}} N_\parallel}$。
- **Polarization Sensitivity ($Q(E_\gamma)$, 偏振灵敏度)**: 偏振探测器在能量 $E_\gamma$ 处将 $100\%$ 完全线偏振入射光子转化为实测散射不对称度的响应效率因子（满足 $A_{\text{asym}} = Q \cdot P$）。

---

## 5. 内转换电子与微观电磁矩阵元 (Internal Conversion and Multipoles)

- **Internal Conversion Coefficient ($\alpha_i$, 内转换系数)**: 原子核发生激发态退激时发射轨道内转换电子的几率与发射自由光子的几率之比：$\alpha_i = \lambda_{e, i} / \lambda_\gamma$。
- **Subshell Ratio (子壳层比值 $\alpha_K / \alpha_L$, $L_1/L_2/L_3$)**: 电子在不同原子轨道子壳层被发射的相对比值，对跃迁多极阶数 $L$ 与宇称具有独特的微观敏感性。
- **Electric Monopole ($E0$ 跃迁)**: 不带出任何轨道角动量（$\Delta I = 0, \Delta \pi = \text{no}$）的核跃迁，单光子发射严格禁戒，只能通过纯内转换电子发射或电子-正电子对产生发生。
