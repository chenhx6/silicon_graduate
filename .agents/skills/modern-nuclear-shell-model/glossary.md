# Glossary: 现代原子核壳模型前沿专业术语规范与物理定义

本术语表汇编 MDPI 特邀专论合集《The Nuclear Shell Model 70 Years after Its Advent》（Gargano, De Gregorio, Lenzi 主编，2023）中的核心专业术语、中英文对照及严密物理定义，为现代微观壳模型、壳演化、弱束缚连续谱、大尺度计算与同位旋破坏研究提供统一概念标准。

---

## 1. 单极相互作用与微观壳演化 (Monopole Interaction and Shell Evolution)

- **Monopole Interaction (单极相互作用 $V_{j_1 j_2}^{\text{mono}}$)**: 两体有效相互作用中关于全角动量 $J$ 的角加权平均标量分量，描述轨道 $j_2$ 填充核子时对轨道 $j_1$ 单粒子中心势能的平均拖曳或抬升。
- **Effective Single-Particle Energy (ESPE, 有效单粒子能量)**: 在充满其他核子的多体介质环境中，某一单粒子轨道实际感受到的修正单体能级位置：$\epsilon_{\text{eff}}(j_1) = \epsilon_{\text{bare}}(j_1) + \sum_{j_2} V_{j_1 j_2}^{\text{mono}} n(j_2)$。
- **Tensor Force (张量力)**: 由介子交换（主要为 $\pi$ 与 $\rho$ 介子）诱发的角动量与空间坐标张量耦合核力，算符形式为 $\hat{S}_{12} = 3(\vec{\sigma}_1 \cdot \hat{r})(\vec{\sigma}_2 \cdot \hat{r}) - \vec{\sigma}_1 \cdot \vec{\sigma}_2$；是自旋-轨道反平行轨道（$j_>$ 与 $j'_<$）之间产生超强单极吸引的根本物理起源。
- **Shell Evolution (壳演化)**: 随着中子数或质子数远离稳定线持续填充，单粒子能隙发生连续变化，传统闭壳幻数逐渐淬灭消失，同时产生全新局域幻数的微观现象。
- **Type-II Shell Evolution (第二类壳演化)**: 在同一核素内部，因粒子-空穴跨壳激发自发重构占据数，从而剧烈改变单极相互作用与单粒子能隙、自发诱发形状共存的机制。

---

## 2. 弱束缚系统与连续谱壳模型 (Weak Binding and Continuum Shell Model)

- **Drip Line (滴线)**: 单核子或双核子分离能降为零（$S_n \le 0$ 或 $S_p \le 0$）的强相互作用绝对核稳定性边界。
- **Berggren Completeness (Berggren 复动量平面完备性)**: 在复动量平面上构造包围共振态极点的积分围道，使得分立束缚态、非束缚衰变宽共振态与沿复积分路径的散射连续态构成正交完备基底的广义泛函定理。
- **Gamow Shell Model (GSM, Gamow 壳模型)**: 在 Berggren 复基底上展开包含两体真实核力的复对称非厄米哈密顿量，实现对弱束缚滴线核共振寿命、粒子发射宽度与连续态耦合自洽计算的开放微观多体模型。
- **Complex Energy Eigenvalues (复本征能量 $E = E_r - i \Gamma / 2$)**: 虚部严格直接给出共振态的粒子放射性自发衰变全宽度 $\Gamma$，半衰期满足 $T_{1/2} = \hbar \ln 2 / \Gamma$。

---

## 3. 大尺度微观算力与算法 (Advanced Computational Shell Model)

- **M-Scheme Basis ($M$-表象基底)**: 选取所有满足单粒子磁量子数代数和严格等于总系统磁量子数 $\sum m_i = M$ 的 Slater 行列式正交基矢。
- **Lanczos Algorithm (Lanczos 块三对角化算法)**: 通过构造正交 Krylov 子空间快速提取超大稀疏厄米矩阵极值（最低特征能态）的经典数值代数算法。
- **Monte Carlo Shell Model (MCSM, 蒙特卡罗壳模型)**: Otsuka 等提出基于重要性抽样自适应变分生成最优化四极形变基矢、并在对称流形上进行三维角动量与宇称投影的算法，突破 Slater 行列式维度 $10^{11}$ 的“维数灾难”。
- **Energy Variance Extrapolation (能量方差外推法)**: 利用变分基底能量方差 $\Delta E^2 = \langle H^2 \rangle - \langle H \rangle^2 \to 0$ 时的线性渐近截距，严格无偏反演全截断空间真实本征能量的数值外推技术。
- **Quasi-Particle Vacua Shell Model (QVSM, 准粒子真空壳模型)**: Shimizu 提出将配对准粒子相干真空作为变分试探基矢、实现大模型空间高效角动量投影的大规模微观算法。

---

## 4. 极化电荷、转移与同位旋对称性 (Effective Charges, Transfer and ISB)

- **Core Polarization Effective Charge (核芯极化有效电荷 $e_{\text{eff}}$)**: 考虑巨四极共振（GQR）在模型空间外 $2\hbar\omega$ 虚激发贡献后，将价空间价核子电荷人为重整化以匹配真实微观 $B(E2)$ 的有效标度量（质子 $e_{\text{eff}}^\pi \a1.3 - 1.5 e$，中子感生电荷 $e_{\text{eff}}^\nu \a0.5 - 0.7 e$）。
- **Kumar Quadrupole Invariants (Kumar 四极不变量 $\langle Q^2 \rangle, \langle Q^3 \cos(3\delta) \rangle$)**: 通过多步低能库仑激发测定所有相互连接的 $E2$ 矩阵元循环乘积构建的物理量，无模型依赖地直接给出核基态均方四极形变量与三轴非对称刚度。
- **Mirror Energy Difference (MED, 镜像能级差)**: 互为镜像的同位旋多重态核（如 $T_z = -1/2$ 与 $T_z = +1/2$）在相同自旋 $J$ 处的激发能量差分：$\text{MED}(J) = E_x(J, T_z = -T) - E_x(J, T_z = +T)$。
- **Triplet Energy Difference (TED, 三重大能级差)**: 同位旋三重态（$T=1$）中心核与两翼核构成的二阶能量差分：$\text{TED}(J) = E_x(J, T_z=-1) + E_x(J, T_z=+1) - 2 E_x(J, T_z=0)$，对微观电荷对称性破坏核力（CSB）与电荷无关性破坏核力（CIB）极其敏感。
- **Isospin-Mixing Correction ($\delta_C$, 超允许费米衰变内转换修正)**: 描述由于库仑势导致母态与子态同位旋波函数空间重叠不完全相等的微扰百分比修正，是高精度检验电弱相互作用 CKM 矩阵首行么正性（$|V_{ud}|^2 + |V_{us}|^2 + |V_{ub}|^2 \equiv 1$）的关键微观参数。

---

## 5. 双贝塔衰变与核天体物理 (Double Beta Decay and Nuclear Astrophysics)

- **Neutrinoless Double Beta Decay ($0\nu\beta\beta$, 无中微子双贝塔衰变)**: 原子核自发释放两个电子且不发射任何中微子的轻子数破坏假想弱电衰变（$\Delta L = 2$），一旦被实验证实直接确立中微子为 Majorana 费米子。
- **Nuclear Matrix Element (NME, $0\nu\beta\beta$ 微观核矩阵元 $M_{0\nu}$)**: 包含了费米、加莫夫-泰勒与张量弱电流算符在超前向中间虚态完备基底上求和的微观算符期望值：$M_{0\nu} = M_{0\nu}^{\text{GT}} - \left(\frac{g_V}{g_A}\right)^2 M_{0\nu}^F + M_{0\nu}^T$。
- **Closure Approximation (闭合近似)**: 鉴于中间虚态能量远小于交换的虚马约拉纳中微子特征动量（$q \sim 100 - 200\text{ MeV}$），将中间态能量取平均值后应用正交完备性将双步跃迁折叠为两核子有效算符期望值的理论方法。
- **Short-Range Correlations (SRC, 短程关联修正)**: 考虑由于核力硬芯强斥力导致核子在极近距离（$r < 0.5\text{ fm}$）无法重叠的 Jastrow 关联波函数修正。
- **Axial-Vector Quenching ($g_A$ 淬灭)**: 核介质多体关联与非核子自由度（$\Delta$ 等同位旋激发）导致弱相互作用轴矢量耦合常数相较自由中子值（$g_A = 1.27$）发生有效减缩的现象。
