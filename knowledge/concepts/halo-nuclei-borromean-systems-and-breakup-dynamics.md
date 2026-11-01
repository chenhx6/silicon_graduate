---
type: concept
title: "中子晕核（Halo Nuclei）、Borromean三体体系与破裂反应动量分布动力学"
aliases: [中子晕核, 晕核, Borromean核, 质子晕, 软E1巨共振, 破裂动量分布, Hansen-Jonson模型, Tanihata相互作用截面]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [halo-nuclei, borromean-systems, breakup-reactions, momentum-distribution, soft-e1-resonance, glauber-theory, drip-line]
---

# 中子晕核（Halo Nuclei）、Borromean三体体系与破裂反应动量分布动力学

## 1. 物理全景：滴线量子隧穿与极端弥散空间核结构

在远离 $\beta$ 稳定线的极其丰中子极限区（中子滴线附近），原子核的最后单核子或双核子结合能急剧趋近于零（$S_n, S_{2n} \ll 1\text{ MeV}$）。

根据 A. Bohr & B. R. Mottelson《Nuclear Structure》、K. Heyde《Basic Ideas in Nuclear Physics》（第 15 章）、C. A. Bertulani《Introduction to Nuclear Reactions》（第 11 章）与叶沿林等《原子核物理（修订版）》（第 10 章）：
1. **量子隧穿与空间延伸**：
   对于弱束缚中子，由于中子不带电（库仑势垒 $V_C = 0$），若其价轨道占据轨道角动量 $l=0$ 的 $s$ 波轨道，**离心势垒亦严格为零**（$V_{\text{cent}} = \frac{l(l+1)\hbar^2}{2\mu r^2} = 0$）。此时单粒子波函数不受任何经典转折点阻挡，波函数在径向呈渐近自由隧穿指数衰减：
   $$\psi(r) \propto \frac{e^{-\kappa r}}{r}, \quad \kappa = \frac{\sqrt{2\mu S_n}}{\hbar}$$
   当分离能 $S_n \to 0$ 时，衰减长度 $1/\kappa \to \infty$，形成延伸范围远超经典核芯半径、密度极低弥散的**中子晕（Neutron Halo）**！
2. **宇称反转与壳演化**：
   典型单中子晕核 $^{11}\text{Be}$（$S_n = 504\text{ keV}$）基态打破了经典幻数壳层排布，原本应处于负宇称 $1p_{1/2}$ 轨道的第七个中子由于微观核力张量力与形变极化跃迁至正宇称 $2s_{1/2}$ 轨道，基态自旋宇称为 $J^\pi = 1/2^+$。纯粹的 $l=0$ 使得其均方根核物质半径扩展至近 $7\text{ fm}$，可与稳定区铅核 $^{208}\text{Pb}$ 的大小比拟！
3. **Borromean 拓扑三体体系**：
   典型双中子晕核 $^{11}\text{Li}$（$S_{2n} = 369\text{ keV}$）与 $^{6}\text{He}$（$S_{2n} = 975\text{ keV}$）展现出惊人的 Borromean 环链拓扑特性：
   - 体系任何两个两体子系统均不能自束缚（$n\text{-}n$ 无束缚态，$^{10}\text{Li}$ 和 $^{5}\text{He}$ 均为非束缚共振态）；
   - 但三体系统通过中子-核芯相互作用与微弱的中子对空间配对关联（Pairing Correlation）形成稳定的束缚态体系；任意去掉一个组成部分，剩余两个粒子立刻解体！

---

## 2. 破裂反应动量分布：Serber 近似与 Hansen-Jonson 渐近标度律

### (1) 突发近似（Sudden Approximation）与动量映射
在高能外周反应（如 $E_{\text{lab}} \sim 400 \sim 800\text{ MeV/u}$）下，晕核穿过靶核时，强核作用将晕中子剥离（Breakup），而核芯碎块（Core Fragment，如 $^{11}\text{Li}$ 反应中的 $^{9}\text{Li}$）在极短时间内飞出靶区。

根据量子力学突发近似与 Serber 模型，出射核芯碎块在入射粒子静止坐标系下的动量分布严格反映了**碰撞瞬间该核子在内禀束缚基态波函数的傅里叶动量空间分布**：
$$\frac{d\sigma}{d^3 p} \propto |\tilde{\psi}(\vec{p})|^2 = \left| \frac{1}{(2\pi\hbar)^{3/2}} \int e^{-i \vec{p}\cdot\vec{r}/\hbar} \psi(\vec{r}) d^3 r \right|^2$$

### (2) Hansen-Jonson 洛伦兹平方动量分布（Hansen & Jonson 1987）
对于由渐近 Yukawa 尾 $\psi(r) = C \frac{e^{-\kappa r}}{r}$ 统治的弱束缚 $s$ 波中子，其三维傅里叶变换具有解析显式解：
$$\tilde{\psi}(\vec{p}) = \frac{C\sqrt{2/\pi}}{p^2 + \hbar^2 \kappa^2}$$
由此，投影到束流方向的一维纵向动量分布（Longitudinal Momentum Distribution）呈现经典的**洛伦兹平方（Lorentzian-squared）线形**：
$$\frac{d\sigma}{dp_z} \propto \frac{1}{(p_z^2 + \alpha^2)^2}, \quad \alpha = \hbar \kappa = \sqrt{2\mu S_n}$$

对该分布求全宽半高（Full Width at Half Maximum, FWHM）：
$$\Gamma_{\text{FWHM}} = 2 \sqrt{\sqrt{2} - 1} \cdot \alpha = 2 \sqrt{\sqrt{2} - 1} \cdot \sqrt{2\mu S_n} \approx 1.287 \cdot \sqrt{2\mu S_n}$$

**实验标志性指纹**：
- **普通核碎块费米运动（Goldhaber 统计模型）**：
  普通核内强束缚核子的动量分布由费米动量 $p_F \approx 250\text{ MeV}/c$ 决定，碎块动量分布宽度为：
  $$\sigma_G = \sigma_0 \sqrt{\frac{A_F (A_P - A_F)}{A_P - 1}}, \quad \sigma_0 \approx \frac{p_F}{\sqrt{5}} \approx 90\text{ MeV}/c$$
  对于普通重离子剥离反应，碎块分布半高宽通常在 $\Gamma \sim 150 \sim 200\text{ MeV}/c$；
- **晕中子极窄动量宽度**：
  由于不确定性原理 $\Delta p \cdot \Delta x \sim \hbar$，空间极度弥散（$\Delta x \gg R_0$）必然对应极窄的动量宽度！实验测得 $^{11}\text{Li} \to {}^9\text{Li}$ 破裂反应中，核芯横向/纵向动量半高宽仅为 **$\Gamma_{\text{FWHM}} \approx 45 \sim 48\text{ MeV}/c$**，直接从动量空间证实了中子晕的存在！

---

## 3. 巨电偶极软模式（Soft E1 Dipole Mode）与结团求和定则

在稳定核中，巨偶极共振（GDR）发生在 $E_x \sim 15 \sim 25\text{ MeV}$，表现为全体质子流与全体中子流的反相宏观体振动。

而在晕核中出现独特的**低能软偶极共振（Soft E1 / Pigmy Dipole Mode）**：
1. **质心解耦与偶极跃迁算符**：
   定义体系总质心坐标系下核芯与价晕中子的相对位矢 $\vec{r} = \vec{r}_{\text{halo}} - \vec{R}_{\text{core}}$。由于中子不带电荷，核芯（带电量 $Z_c$、质量数 $A_c$）与晕中子（带电量 $0$、质量数 $A_h$）的相对运动产生的有效电偶极算符为：
   $$\mathcal{M}(E1, \mu) = e_{\text{eff}} r Y_{1\mu}, \quad e_{\text{eff}} = e \frac{Z_c A_h}{A_{\text{total}}}$$
2. **结团 Thomas-Reiche-Kuhn (TRK) 偶极求和定则**：
   相对运动耗散的非能量加权与能量加权求和定则：
   $$S_{\text{cluster}}(E1) = \int \frac{dB(E1)}{dE_x} dE_x = \frac{9}{4\pi} e^2 \left( \frac{Z_c A_h}{A_{\text{total}}} \right)^2 \langle r^2 \rangle$$
   由于晕核内禀均方根距离 $\langle r^2 \rangle$ 极大，在极其低下的激发能区（$E_x \sim 1.0 \sim 1.5\text{ MeV}$）就耗尽了高达数个 $e^2 \text{fm}^2$ 的极强 $B(E1)$ 跃迁强度！
3. **相对论库仑激发（Coulomb Dissociation）**：
   在穿过高 $Z$ 靶（如 $^{208}\text{Pb}$）的超强虚光子场时，极易发生相对论库仑激发解离，提供反向推算天体物理辐射俘获截面（如 $^7\text{Be}(p, \gamma)^8\text{B}$ 太阳中微子核反应）的高灵敏度钥匙。

---

## 4. Glauber 多重散射模型与均方根物质半径反演

1985 年，Tanihata（谷畑良尚）在劳伦斯伯克利实验室（LBL）测得 $^{11}\text{Li}$ 的相互作用截面 $\sigma_I$ 比同位素链异常跃升逾 $30\%$。

在 Glauber 光学极限近似（Optical Limit Approximation, OLA）下：
1. **靶核与入射粒子几何重叠 S 矩阵**：
   $$S(b) = \exp\left[ -\bar{\sigma}_{NN} \int d^2 s \rho_P(s) \rho_T(|\vec{b} - \vec{s}|) \right]$$
   其中 $\bar{\sigma}_{NN}$ 为核子-核子平均同位旋平均总截面，$\rho_P$ 与 $\rho_T$ 分别为投射核与靶核的厚度积分密度剖面。
2. **总反应截面方程**：
   $$\sigma_R = 2\pi \int_0^\infty b \, db \left[ 1 - |S(b)|^2 \right]$$
3. **核物质均方根半径反演**：
   通过调节二参数费米分布（2pF）或高斯+指数尾密度分布的均方根物质半径 $R_m$，拟合测得的 $\sigma_R$，精确解得 $^{11}\text{Li}$ 的核物质半径高达 **$R_m = 3.12 \pm 0.16\text{ fm}$**（而正常核芯仅约 $2.45\text{ fm}$），彻底确立了中子晕的新物理形态。

---

## 5. Python 算法设计与实验分析器规范

本 Wiki 在 `system/scripts/analysis/halo_breakup_momentum_calculator.py` 中实现了完整的晕核破裂动力学分析器：
1. **Hansen-Jonson 动量宽度正演**：从单/双核子分离能计算 $\Gamma_{\text{FWHM}}$；
2. **反演弱结合能**：从实测碎块窄动量分布反演价中子分离能 $S_n$；
3. **Goldhaber 统计模型基准计算**：评估正常费米运动碎块动量展宽，提供晕效应检验背景；
4. **结团 TRK 软 E1 强度求和定则**：定量评估低能软偶极激发的 $B(E1)$ 跃迁强度上限；
5. **Glauber 光学截面标度反演**：从反应截面差分反演核物质半径增量 $\Delta R_{\text{rms}}$。

---

## 6. 权威文献与理论溯源

1. **Tanihata, I. et al.** (1985). Measurements of interaction cross sections and nuclear radii in the light p-shell region. *Phys. Rev. Lett.*, 55(24), 2676-2679.
2. **Hansen, P. G. & Jonson, B.** (1987). The neutron halo of extremely neutron-rich nuclei. *Europhys. Lett.*, 4(4), 409-414.
3. **Jonson, B.** (2004). Light exotic nuclei. *Phys. Rep.*, 389(4), 137-246.
4. **Bertulani, C. A. & Danielewicz, P.** (2004). *Introduction to Nuclear Reactions*, Chapter 11 (Breakup of halo nuclei). CRC Press.
5. **Heyde, K.** (2004). *Basic Ideas and Concepts in Nuclear Physics* (3rd Edition), Chapter 15 (Weakly bound quantum systems and exotic nuclei). CRC Press.
6. **叶沿林、卢希庭、江栋兴** (2000). 《原子核物理（修订版）》第 10 章：放射性核束物理与晕核. 原子能出版社.
