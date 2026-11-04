---
name: hamilton-nuclear-spectroscopy
description: "W. D. Hamilton《The Electromagnetic Interaction in Nuclear Spectroscopy》：在束 γ 谱学角分布理论、统计取向张量 B_k(I)、几何 F_k 系数、未观测级联去取向 U_k 系数、方向角关联 DCO 比值、康普顿线偏振度 P(theta) 测量、多极混合比 delta 双根二次有理展开与网格似然反演。"
---

<!-- argument-hint: [formalism, formula, observable, or chapter topic] -->

# 核谱学电磁相互作用（W. D. Hamilton 经典权威专著）

**编著者**：W. D. Hamilton (editor)（苏塞克斯大学数学与物理科学学院） | **出版社**：North-Holland Publishing Company / American Elsevier (1975) | **页数**：956 页
**本地原件**：`raw/books/The Electromagnetic Interaction In Nuclear Spectroscopy.pdf` (SHA-256 `93b32a8debb66ad036229d860ad56f0434dc49b56edd32f1628af1d71a21ae00`)

本技能提炼国际在束 $\gamma$ 谱学界公认的“电磁相互作用圣经”——W. D. Hamilton 编著经典专著的核心数学物理表象，系统形式化轴对称取向统计张量 $B_k(I)$、角分布与角关联 $F_k$ 几何系数、未观测中间跃迁去取向 $U_k$ 级联连乘定理、方向角关联 DCO 阵列比值、康普顿线偏振度 $P(\theta)$ 宇称选择定则，以及多极混合比 $\delta(E2/M1)$ 的二次有理方程双根退化与网格极小化拟合，为在束核谱学能级纲图构建、跃迁多极性指认与手征/摆动模式实验判决提供严密的代数几何与实验分析支撑。

## How to Use This Skill

- **方向角分布与各向异性**：询问 `方向角分布公式`、`统计取向张量B_k`、`自旋取向宽度sigma/I`、`F_k几何系数`、`各向异性系数A_2与A_4`；
- **未观测级联与去取向**：询问 `去取向系数U_k`、`未观测跃迁衰减`、`6j符号展开`、`级联连乘定理`；
- **方向角关联 (DCO / ADO)**：询问 `方向角关联函数`、`DCO比值理论值`、`不同自旋跃迁序列DCO指纹`、`大探测器阵列几何矩阵`；
- **康普顿线偏振度 (Linear Polarization)**：询问 `康普顿线偏振公式`、`电磁多极性宇称判据`、`散射不对称度A_asym`、`偏振灵敏度Q(E)`、`Clover阵列偏振测量`；
- **多极混合比 $\delta$ 与双根仲裁**：询问 `混合比二次有理方程`、`双根退化机理`、`arctan(delta)网格似然扫描`、`偏振破除双根简并`；
- **内转换系数与微观矩阵元**：询问 `内转换子壳层比值`、`E0单极跃迁内转换`、`Weisskopf单粒子单位`、`Alaga强度定则`。

---

## Core Frameworks and Mental Models

1. **轴对称定向态统计张量 $B_k(I)$ 与方向角分布展开（第 12 章）**：
   - 空间激发态的磁子态布居 $P(m)$ 在轴对称熔合蒸发碰撞中满足高斯分布：$P(m) \propto \exp\left(-\frac{m^2}{2\sigma^2}\right)$；
   - **统计取向张量 (Orientation Tensor $B_k(I)$)**：
     $$B_k(I) = \sqrt{2I+1} \sum_{m=-I}^I (-1)^{I-m} \langle I m I -m | k 0 \rangle P(m), \quad B_0(I) \equiv 1;$$
     由于宇称守恒与轴对称正负 $m$ 对称性，奇数阶张量严格为零：$B_1 = B_3 = \dots = 0$；
   - **方向角分布函数**（相对于束流轴角 $\theta$）：
     $$W(\theta) = 1 + A_2 P_2(\cos\theta) + A_4 P_4(\cos\theta),$$
     其中各向异性系数严格分解为初态统计取向度与电磁跃迁几何因子的乘积：
     $$A_k(I_i \to I_f) = B_k(I_i) \cdot R_k(L, L', I_i, I_f).$$

2. **$F_k$ 几何系数与多极混合比 $\delta$ 的二次有理展开（第 12 章式 12.247–12.253）**：
   - 对于包含最低多极 $L$ 与高一阶多极 $L' = L+1$（如 $M1 + E2$ 或 $E1 + M2$）的混合跃迁，跃迁几何因子为：
     $$R_k(L L' I_i I_f) = \frac{F_k(L L I_f I_i) + 2 \delta F_k(L L' I_f I_i) + \delta^2 F_k(L' L' I_f I_i)}{1 + \delta^2},$$
     其中 $F_k$ 系数为 Ferentz-Rosenzweig 纯几何 Racah 代数系数：
     $$F_k(L L' I_f I_i) = (-1)^{I_f - I_i - 1} \sqrt{(2I_i+1)(2L+1)(2L'+1)} \langle L 1 L' -1 | k 0 \rangle W(I_i I_i L L'; k I_f);$$
   - **Krane-Steffen 相位约定**：$\delta(L'/L) \equiv \frac{\langle I_f || \vec{j} \cdot \vec{A}_{L'}^{(\text{e.m.})} || I_i \rangle}{\langle I_f || \vec{j} \cdot \vec{A}_L^{(\text{e.m.})} || I_i \rangle}$；
   - **双根退化（Dual-Root Degeneracy）**：由于方程对 $\delta$ 是二次分式，实测 $A_2$ 值代入后通常导出**两个数学完全等价的实数解根**（$\delta_1 \approx 0$ 与 $\delta_2 \sim 3 - 8$），单靠未极化角分布无法甄别，必须引入线偏振或转换系数仲裁！

3. **未观测中间跃迁去取向 $U_k$ 级联连乘定理（第 12 章式 12.207–12.213）**：
   - 在级联衰变链中，若初始对齐核态经过若干次未被探测器观测到的中间跃迁 $I_0 \xrightarrow{\gamma_{\text{unobs}}} I_1 \xrightarrow{\gamma_{\text{unobs}}} I_2 \dots \xrightarrow{\gamma_{\text{obs}}} I_f$：
   - 每次未观测跃迁会部分抹平磁子态对齐度，引入去取向系数 $U_k$：
     $$U_k(I_a I_b L) = (-1)^{I_a + I_b + L + k} \sqrt{(2I_a+1)(2I_b+1)} W(I_a I_a I_b I_b; k L);$$
   - **级联连乘守恒律**：第 $n$ 级观测态的有效统计取向张量等于初态张量按所有中间未观测级联的 $U_k$ 因子依次连乘：
     $$B_k(I_n) = B_k(I_0) \cdot \prod_{j=1}^n U_k(I_{j-1} I_j L_j), \quad (U_0 \equiv 1).$$

4. **方向角关联与 DCO 阵列几何比值（第 14 章）**：
   - 两探测器分别放置在相对于束流轴角 $(\theta_1, \theta_2)$ 且相对方位角为 $\Delta\phi$ 时，符合发射两个 $\gamma$ 光子的空间双重角关联函数：
     $$W(\theta_1, \theta_2, \Delta\phi) = \sum_{k_1, k_2, k} A_{k_1 k_2}^k H_{k_1 k_2}^k(\theta_1, \theta_2, \Delta\phi);$$
   - **DCO 符合比值 (Directional Correlation from Oriented States)**：
     在两特定特征角度（如前向/后向角 $\theta_1 = 30^\circ$ 与垂直角 $\theta_2 = 90^\circ$）门控下：
     $$R_{\text{DCO}} = \frac{I_{\gamma 1}(\text{at } \theta_1, \text{gated by } \gamma_2 \text{ at } \theta_2)}{I_{\gamma 1}(\text{at } \theta_2, \text{gated by } \gamma_2 \text{ at } \theta_1)};$$
   - **经验跃迁指纹**（门控在纯四极拉伸跃迁 $\Delta I = 2, E2$ 上）：
     - 纯拉伸四极跃迁（$\Delta I = 2, E2$）：$R_{\text{DCO}} \a1.00$；
     - 纯偶极跃迁（$\Delta I = 1, D$ 或 $\Delta I = 0, D$）：$R_{\text{DCO}} \a0.55 - 0.65$；
     - 包含大混合比 $\delta$ 的多极混合跃迁：$R_{\text{DCO}}$ 可偏移至 $0.8 - 1.5$ 范围。

5. **康普顿线偏振度测量与电磁宇称排他性裁决（第 15 章）**：
   - 测定 $\gamma$ 射线在探测器内发生康普顿散射时垂直于反应平面与平行于反应平面的不对称计数：
     $$A_{\text{asym}}(\theta) = \frac{N_\perp - a_{\text{geom}} N_\parallel}{N_\perp + a_{\text{geom}} N_\parallel};$$
   - **理论偏振度公式**：
     $$P(\theta) = \frac{A_{\text{asym}}(\theta)}{Q(E_\gamma)},$$
     其中 $Q(E_\gamma) \in [0, 1]$ 为偏振仪在能量 $E_\gamma$ 处的康普顿偏振灵敏度；
   - **宇称排他性选择律**：
     对于固定角度（通常 $\theta = 90^\circ$）：
     $$P(90^\circ) = \frac{\pm 2 A_2^{(p)} P_2^{(2)}(0) \pm \dots}{W(90^\circ)};$$
     - **正号对应电性跃迁 ($EL$)**：纯 $E2$ 跃迁的线偏振度 $P(90^\circ) > 0$（强正偏振）；
     - **负号对应磁性跃迁 ($ML$)**：纯 $M1$ 跃迁的线偏振度 $P(90^\circ) < 0$（负偏振）。
     这一正负号的剧烈反转，彻底成为裁决三轴手征伙伴带（$M1$ 主导，$P < 0$）与摆动声子激发（$E2$ 主导，$P > 0$）的最强物理仲裁法典！

---

## Chapter Index

| # | 章节主题 | 核心数学方法与核物理应用 |
|---|---|---|
| [ch11](chapters/ch11-multipole-fields-and-transition-probabilities.md) | 电磁多极场与辐射跃迁几率 | 长波近似麦克斯韦多极场展开、Weisskopf 单粒子单位标度律与约化几率 $B(\sigma L)$ |
| [ch12-dist](chapters/ch12-directional-distributions-and-orientation-tensors.md) | 方向角分布理论与统计取向张量 | 轴对称取向张量 $B_k(I)$、高斯 $m$ 子态分布、几何 $F_k$ 系数与各向异性 $A_2/A_4$ |
| [ch12-deor](chapters/ch12-cascade-deorientation-uk-coefficients.md) | 未观测级联跃迁去取向 $U_k$ 理论 | 统计张量连乘守恒定理、Wigner $6j$ 展开、非观测级联退取向衰减与布居跟踪 |
| [ch14](chapters/ch14-directional-correlations-and-dco-formalism.md) | 方向角关联 (DCO/ADO) 与阵列符合比值 | 双光子相干矩阵元、DCO 实验比值理论计算、大探测器阵列几何布局与多极性指认 |
| [ch15-pol](chapters/ch15-linear-polarization-and-compton-polarimetry.md) | 康普顿线偏振度测量与宇称仲裁 | 康普顿散射截面 Klein-Nishina 公式、不对称度 $A_{\text{asym}}$、偏振灵敏度 $Q(E)$ 与电/磁正负号判据 |
| [ch15-dual](chapters/ch15-mixing-ratio-dual-root-and-profile-fitting.md) | 多极混合比 $\delta$ 双根退化与网格拟合 | 二次有理分式多解性、判别式分析、$\arctan\delta$ 均匀网格似然扫描与偏振联合仲裁 |

## Supporting Reference Files

- [glossary.md](glossary.md) — 核谱学角分布、DCO、线偏振与统计张量专业术语中英双语定义。
- [patterns.md](patterns.md) — 5 大角分布多极性反演、偏振仲裁与双根消解分析范式。
- [cheatsheet.md](cheatsheet.md) — 典型自旋跃迁序列 $A_2/A_4$ 与 $R_{\text{DCO}}$ 速查表、Racah 几何系数卡与偏振灵敏度卡。

---

## Scope & Limits

本技能提供辐射电磁跃迁角分布、角关联、线偏振与多极混合比的严格代数与探测器几何理论。对于探测器硬件死时间、时间晃动与数字成形，配合 `nuclear-experimental-methods`；对于非线性误差传播与参数置信区间估计，配合 `zhu-experimental-statistics`；对于重离子反冲速度多普勒频移，配合 `heavy-ion-nuclear-reactions`。
