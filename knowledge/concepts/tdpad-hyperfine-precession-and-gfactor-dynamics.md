---
type: concept
title: "时间差分扰动角分布（TDPAD）、核超精细进动与三矢量g因子动力学"
aliases: [TDPAD, 时间差分扰动角分布, 核g因子, 拉莫尔进动, 电四极相互作用, 超精细磁场, 三矢量磁矩叠加, 128Cs手征g因子]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [tdpad, g-factor, larmor-precession, hyperfine-interaction, quadrupole-interaction, chiral-geometry, planar-aplanar, magnetic-moment]
---

# 时间差分扰动角分布（TDPAD）、核超精细进动与三矢量g因子动力学

## 1. 物理全景：纳秒至微秒异能态的核电磁矩在束直接精密测量

在低能核物理与高自旋在束 $\gamma$ 谱学中，虽然跃迁几率（$B(M1), B(E2)$）反映了初末态之间的微观矩阵元，但**唯有静态电四极矩 $Q_s$ 与静态磁偶极矩 $\mu$（即朗德 $g$ 因子）能够提供核态内禀波函数几何构型与单粒子角动量对齐方向的直接、绝对测量**！

对于寿命在纳秒至微秒区间（$\tau \sim 5\text{ ns} \sim 100\ \mu\text{s}$）的同质异能态（Isomers），**时间差分扰动角分布法（Time-Differential Perturbed Angular Distribution, TDPAD）**是国际核物理界最核心的精密测量技术。

根据 W. D. Hamilton《The Electromagnetic Interaction in Nuclear Spectroscopy》（第 13–14 章）、E. Grodner et al. (Phys. Rev. Lett. 120, 022502, 2018) 与 M. Ionescu-Bujor et al. (Nucl. Phys. A 643, 459, 1998)：
1. **反冲核取向与外加磁场下的进动**：
   重离子熔合蒸发反应将角动量垂直对齐于反应平面（$m=0$ 优势布居，产生取向张量 $B_k$）。反冲核注入无辐射损伤的宿主晶格中，置于垂直于反应平面的强外磁场 $B_{\text{ext}}$ 下。核磁矩与磁场发生塞曼相互作用，驱动取向核绕磁场轴发生经典的**拉莫尔进动（Larmor Precession）**，其角频率为：
   $$\omega_L = -\frac{g \mu_N B}{\hbar}$$
2. **双倍拉莫尔调制频率定理**：
   由于定向核发射的电四极或偶极 $\gamma$ 辐射具有空间二重反对称性（角分布主导项为 $P_2(\cos \theta)$），核旋转半周（$\pi$）即可恢复空间几何等效，因此实测角分布谱以**双倍拉莫尔频率（$\omega_{\text{prec}} = 2\omega_L$）**发生周期性正弦调制！

---

## 2. TDPAD 实验可观测量：四重时间对象与各向异性比值 $R(t)$

### (1) 四重独立时间实体的严格解耦
在分析 TDPAD 实验时，必须严格区分四类本质不同的时间常数，严禁混淆：
1. **核能级粒子数寿命 $\tau_{\text{pop}}$**：核态自发衰变的内禀寿命，主导探测器总计数的单指数衰减因子 $\exp(-t / \tau_{\text{pop}})$；
2. **自旋取向弛豫时间 $\tau_{\text{relax}}$**：晶格微观随机超精细微扰引起的自旋退取向时间，主导调制包络的阻尼；
3. **进动调制周期 $T_{\text{prec}} = \pi / \omega_L$**：外加磁场或电场梯度驱动的微观物理进动周期；
4. **脉冲束流与探测器时间分辨 $\text{FWHM}_{\text{PRF}}$**：决定测量短寿命（$\tau < 10\text{ ns}$）的起始时间卷积窗口。

### (2) 各向异性调制比值 $R(t)$ 的数学自洽性
为完全消去统计分母中的共同粒子数衰减项 $\exp(-t / \tau_{\text{pop}})$，实验上在与束流成 $\theta_1 = +135^\circ$ 与 $\theta_2 = -135^\circ$（或 $0^\circ$ 与 $90^\circ$）放置两组或四组探测器，构造无量纲归一化比值：
$$R(t) = \frac{N(t, +135^\circ) - N(t, -135^\circ)}{N(t, +135^\circ) + N(t, -135^\circ)}$$
利用含时扰动角分布公式展开：
$$R(t) \approx \frac{3 A_2 B_2}{4 + A_2 B_2} \sin(2\omega_L t) \cdot \exp\left( -\frac{t}{\tau_{\text{relax}}} \right)$$
由此，实验通过对 $R(t)$ 进行最小二乘拟合，即可**独立于核寿命 $\tau_{\text{pop}}$，以极高的统计精度直接解出进动频率 $\omega_L$ 与 $g$ 因子**！

---

## 3. 三矢量磁矩叠加模型与手征核几何判据（Grodner 2018）

在奇奇核与三轴奇 $A$ 核中，朗德 $g$ 因子对单粒子轨道与集体转动矢量的空间拓扑具有极其敏感的指向性。

### (1) 三矢量推广加和法则（Generalized Three-Vector Additivity）
对于包含价质子（$\vec{j}_p$）、价中子（$\vec{j}_n$）与偶偶三轴核芯集体转动（$\vec{j}_R$）的耦合体系，总角动量为：
$$\vec{I} = \vec{j}_p + \vec{j}_n + \vec{j}_R$$
系统总磁偶极矩在总角动量轴上的投影给出广义三矢量 $g$ 因子公式：
$$g(I) = g_p \frac{\vec{j}_p \cdot \vec{I}}{I(I+1)} + g_n \frac{\vec{j}_n \cdot \vec{I}}{I(I+1)} + g_R \frac{\vec{j}_R \cdot \vec{I}}{I(I+1)}$$
利用矢量余弦定理展开点积：
$$\vec{j}_p \cdot \vec{I} = \frac{1}{2} \left[ I(I+1) + j_p(j_p+1) - |\vec{j}_n + \vec{j}_R|^2 \right]$$

### (2) 手征三维非共面 vs 共面几何的判决法典
在典型手征核 $^{128}\text{Cs}$（$\pi h_{11/2} \otimes \nu h_{11/2}^{-1}$，带头 $I^\pi = 9^+$，$\tau = 81\text{ ns}$）中：
1. **理想三维手征极限（Aplanar Chirality, $\vec{j}_p \perp \vec{j}_n \perp \vec{j}_R$）**：
   三个矢量相互正交，两两点积为零。代入三矢量公式严格预言理论值为 $g_{\text{aplanar}} \approx +0.50$；
2. **共面极端极限（Coplanar Geometry, 质子对齐共面）**：
   质子与中子角动量展开在同一平面内，理论预言极值为 $g_{\text{planar}} \approx +0.60$；
3. **Grodner 2018 实验裁判事实**：
   TDPAD 实测获得 $g = +0.59 \pm 0.01$！这一高精度测量无可辩驳地落在共面极值区，**直接证伪了低自旋带头处存在静态三维手征的假说，确立了带头为共面手征振动态、直至高自旋（$I \ge 13\hbar$）才动态涌现为三维手征转动的新物理图景**！

---

## 4. 晶格微观微扰：非立方金属中的电四极相互作用（QI）

当反冲核注入非立方对称晶格（如多晶金属白锡 Sn、金属镁 Mg 或金属锌 Zn）时，核不仅感受磁场，还会感受主轴电场梯度（Electric Field Gradient, EFG, $V_{zz}$）。
1. **四极耦合基频**：
   $$\omega_0 = \frac{3 e Q_s V_{zz}}{4 I (2I - 1) \hbar}$$
2. **多晶四极微扰因子 $G_{kk}(t)$**：
   $$G_{22}(t) = s_{20} + \sum_{n=1}^3 s_{2n} \cos(n \omega_0 t)$$
   通过测定四极振荡基频，可绝对反演原子核的静态电四极矩 $|Q_s|$。
3. **单粒子磁矩与集体形变解耦判据**：
   在 $^{129,131}\text{Ce}$ 的 $9/2^-$ 异能态中（Ionescu-Bujor 1998），TDPAD 测得单中子 $g$ 因子差异仅 $2\%$（严格保持 Schmidt 极限量），而电四极矩 $|Q_s|$ 却因两中子填充激增 $43.5\%$，直接实验证实了**磁矩对壳层结构刚性守恒、而四极矩对形变极化极其敏感**的物理图像！

---

## 5. Python 算法设计与实验分析器规范

本 Wiki 在 `system/scripts/analysis/tdpad_hyperfine_precession_calculator.py` 中实现了完整的 TDPAD 分析器：
1. **拉莫尔频率与 $g$ 因子精密互演器**：基于基本物理常数 $\mu_N / \hbar \approx 47.8942\text{ MHz/T}$，计算 $\omega_L$、调制周期 $T_{\text{mod}}$ 与 $g$；
2. **各向异性时间调制谱 $R(t)$ 生成器**：生成包含自旋取向对齐 $A_2 B_2$ 与指数弛豫衰减的理论时间谱；
3. **三矢量广义磁矩加和计算器**：输入 $(\vec{j}_p, \vec{j}_n, \vec{j}_R)$ 与空间夹角，计算任意空间几何构型的理论 $g$ 因子，自动诊断手征空间取向角；
4. **电四极相互作用频率反演器**：从四极微扰振荡基频 $\nu_Q$ 与宿主电场梯度 $V_{zz}$ 提取内禀静态电四极矩 $|Q_s|$。

---

## 6. 权威文献与理论溯源

1. **Hamilton, W. D.** (1975). *The Electromagnetic Interaction in Nuclear Spectroscopy*, Chapters 13 & 14 (Perturbed angular correlations and distributions). North-Holland.
2. **Grodner, E. et al.** (2018). Partner bands in $^{128}\text{Cs}$: Planar versus aplanar geometry from magnetic moment measurements. *Phys. Rev. Lett.*, 120(2), 022502.
3. **Ionescu-Bujor, M. et al.** (1998). Static electromagnetic moments of the $9/2^-$ isomers in $^{129,131}\text{Ce}$ and shape evolution in odd-neutron light Ce isotopes. *Nucl. Phys. A*, 643(4), 459-478.
4. **Gray, T. J. et al.** (2020). Hyperfine magnetic fields and $g$-factor measurements of nuclear isomers. *Phys. Rev. C*, 101(4), 044308.
5. **卢希庭、江栋兴、叶沿林** (2000). 《原子核物理（修订版）》第 3 章：原子核电磁矩与超精细相互作用. 原子能出版社.
