---
name: modern-nuclear-shell-model
description: "MDPI 权威专著《The Nuclear Shell Model 70 Years after Its Advent》（Gargano 等编）：现代微观壳模型前沿、Otsuka 单极张量力驱动壳演化、Gamow 复能连续谱壳模型、MCSM/QVSM 大组态空间算法、低能库仑激发与有效电荷、N=40 反转岛核子去除、100Sn 邻区高自旋 Seniority 谱学、同位旋破坏 MED/TED 与 0vbb 双贝塔微观核矩阵元。"
---

<!-- argument-hint: [formalism, nucleus, observable, or article-topic] -->

# 现代原子核壳模型：诞生 70 年前沿与进展（Gargano、De Gregorio、Lenzi 主编）

**主编者**：Angela Gargano, Giovanni De Gregorio, Silvia Monica Lenzi（INFN 那不勒斯分部 / 帕多瓦大学） | **出版社**：MDPI (2023) | **页数**：334 PDF 页（14 篇特邀前沿专论合集）
**本地原件**：`raw/books/The Nuclear Shell Model 70 Years after Its Advent Achievements and Prospects_Gargano, Gregorio, Lenzi.pdf` (SHA-256 `1b2418417419c343d2a35684a7d3dc7136ad0bc340d609eecbd028830b55eec1`)

本技能提炼纪念原子核壳模型（Mayer & Jensen 诺奖理论）诞生 70 周年权威特邀前沿专著的核心物理思想与计算范式，系统整合世界顶尖壳模型理论家（Otsuka、Brown、Talmi、Stuchbery、Utsuno、Shimizu、Górska、Gade、Smirnova、Horoi、Martínez-Pinedo 等）在单极张量力驱动壳演化、复动量平面 Gamow 连续谱壳模型、大规模量子蒙特卡罗（MCSM/QVSM）、低能库仑激发与微观有效电荷、极端丰中子反转岛、$^{100}\text{Sn}$ 闭壳近区高自旋 Seniority 谱学、同位旋对称性破缺（MED/TED）以及无中微子双贝塔衰变微观核矩阵元（NME）的最新突破，为核结构与反应动力学提供现代第一性微观壳模型法典。

## How to Use This Skill

- **单极相互作用与壳演化**：询问 `单极张量力`、`有效单粒子能量ESPE`、`Otsuka壳演化机制`、`新幻数出现与传统幻数淬灭`、`Type-II壳演化`；
- **滴线连续谱与弱束缚核**：询问 `滴线结合能双差分`、`Gamow壳模型GSM`、`Berggren复能基底`、`共振态与连续谱耦合`、`28O与晕核`；
- **大尺度计算算法 (MCSM / QVSM)**：询问 `Lanczos对角化`、`蒙特卡罗壳模型MCSM`、`能量方差外推`、`准粒子真空壳模型QVSM`；
- **微观有效电荷与库仑激发**：询问 `微观极化有效电荷`、`E2求和规则与四极不变量`、`低能库仑激发矩阵元确定`、`14C加莫夫-泰勒跃迁相消`；
- **反转岛与反应截面**：询问 `N=40反转岛`、`准粒子阻塞`、`单核子敲出反应谱因子`、`形变侵入组态`；
- **$^{100}\text{Sn}$ 邻区高自旋与异能态**：询问 `100Sn闭壳近区高自旋谱学`、`g9/2壳层Seniority异能态`、`质子滴线奇异衰变`；
- **同位旋破缺与对称性能级差**：询问 `同位旋对称性破缺ISB`、`镜像能级差MED`、`三重大多重态能级差TED`、`超允许费米衰变内转换修正delta_C`；
- **双贝塔衰变与天体物理**：询问 `0vbb无中微子双贝塔核矩阵元NME`、`短程关联SRC`、`核天体弱反应率`、`超新星电子俘获`。

---

## Core Frameworks and Mental Models

1. **Otsuka 单极相互作用与张量力驱动壳演化（第 3 & 8 篇专论）**：
   - 传统壳模型假定单粒子能级在核素图上固定不变；现代理论证明两体相互作用单极分量随核子填充发生剧烈重整化：
     $$\Delta \epsilon(j_1) = \sum_{j_2} V_{j_1 j_2}^{\text{mono}} \cdot n(j_2), \quad V_{j_1 j_2}^{\text{mono}} = \frac{\sum_J (2J+1) \langle j_1 j_2 J | V | j_1 j_2 J \rangle}{\sum_J (2J+1)};$$
   - **张量力（Tensor Force, $\pi+\rho$ 介子交换）的特征驱动法则**：
     - 当质子占据 $j_{>} = l + 1/2$ 轨道而中子占据 $j_{<}' = l' - 1/2$ 轨道时（自旋轨道反平行），张量力表现为**强烈吸引**；
     - 当两核子同时占据 $j_{>}$ 与 $j_{>}'$ 时，张量力表现为**相斥**；
   - **机制实证**：在富中子区移除质子导致自旋-轨道能隙急剧塌缩，使得传统幻数（如 $N=8, 20, 28$）消失淬灭，并在远离稳定线处催生全新幻数（如 $N=14, 16, 32, 34$）！

2. **滴线连续谱与复动量平面 Gamow 壳模型（第 4 & 5 篇专论）**：
   - 传统谐振子基底局限于高斯指数束缚空间，完全无法描述弱束缚核在滴线附近的非束缚共振与连续态出射；
   - **Berggren 完备复基底**：
     在复动量 $k$ 平面上构造包围共振极点（Resonant Poles）的围道积分：
     $$\sum_{n} |u_n\rangle \langle \tilde{u}_n| + \int_{L^+} |k\rangle \langle k| dk = \hat{1};$$
   - **Gamow 壳模型（GSM）**：将传统单粒子束缚态、非束缚衰变宽共振态与无限维散射连续态统一在严格厄米对偶的复对称哈密顿量中对角化，成功解析了中子滴线外 $^{28}\text{O}$（$Z=8, N=20$）的非束缚多中子发射机制与 $^{11}\text{Li}$ 弱结合微观基底。

3. **大尺度微观算法：MCSM 蒙特卡罗壳模型与 QVSM（第 6 篇专论）**：
   - 面对跨壳大模型空间 Slater 行列式基底维度超过 $10^{11}$（超出直接 Lanczos 算法极限）的瓶颈：
   - **蒙特卡罗壳模型 (MCSM)**：采用变分基底自适应采样，仅选取数十到数百个具有最优化四极形变的投影基矢，结合**能量方差外推法（Energy Variance Extrapolation）**严格逼近完全全空间对角化能量基准；
   - **准粒子真空壳模型 (QVSM)**：引入配对准粒子相干真空，实现超大空间在自洽四极配对流形上的高精度变分投影。

4. **微观极化有效电荷与两体矩阵元相消（第 1 & 2 篇专论）**：
   - **Talmi $^{14}\text{C}$ 加莫夫-泰勒跃迁相消**：
     $^{14}\text{C}$ 的超长半衰期（$5730\text{ 年}$）曾是核物理之谜；I. Talmi 等证明：微观张量力诱发的极小组态混合振幅，恰好使主组态与侵入组态之间的 Gamow-Teller 矩阵元发生**几乎 $100\%$ 的代数完全相消**（相消率达 $99.99\%$），造成衰变率急剧下降百万倍！
   - **有效电荷与微观极化**：巨四极共振（GQR）的 $2\hbar\omega$ 虚激发促使质子有效电荷 $e_{\text{eff}}^\pi \a1.3 - 1.5 e$，中子感生有效电荷 $e_{\text{eff}}^\nu \a0.5 - 0.7 e$；低能 Coulomb 激发测得的非平庸四极不变量严格确定了三轴形变刚性度 $\langle Q^3 \cos(3\delta) \rangle$。

5. **同位旋对称性破缺 (ISB) 与镜像能级差 (MED/TED)（第 11 & 12 篇专论）**：
   - 强核力在微观上近乎严格满足同位旋旋转不变性；核能谱中可观测的同位旋破坏完全源自微观电磁相互作用与轻夸克质量差（$m_d - m_u$）：
   - **镜像能级差 (MED)**：具有相同自旋 $J$ 的镜像核（$T_z = \pm 1/2$ 或 $\pm 1$）之间的能量差：
     $$\text{MED}(J) = E_x(J, T_z = -T) - E_x(J, T_z = +T);$$
   - **三重能级差 (TED)**：同位旋三重态（$T=1$）中心与两翼的二阶能量差分：
     $$\text{TED}(J) = E_x(J, T_z = -1) + E_x(J, T_z = +1) - 2 E_x(J, T_z = 0);$$
   - 随着自旋上升，高-$j$ 质子对与中子对在 Coriolis 力下先后顺排，导致特定自旋处库仑多极单粒子排斥能发生突变，使得 MED 与 TED 成为精准测定单核子顺排轨道顺序与微观同位旋非守恒核力（INC）的精密探针。

6. **无中微子双贝塔衰变 ($0\nu\beta\beta$) 微观核矩阵元（第 13 篇专论）**：
   - $0\nu\beta\beta$ 衰变半衰期与有效马约拉纳中微子质量的平方反比直接包含微观核矩阵元：$(T_{1/2}^{0\nu})^{-1} = G_{0\nu} g_A^4 |M_{0\nu}|^2 \langle m_{\beta\beta} \rangle^2$；
   - M. Horoi 形式化了基于大规模壳模型的闭合近似（Closure Approximation），系统评估超前向-后向虚态求和、短程关联（SRC: Argonne vs CD-Bonn 势）以及核子形状因子的有限尺寸效应；
   - 确立了区分轴矢量弱耦合常数淬灭（$g_A$ Quenching）与模型空间截断误差的独立物理边界。

---

## Chapter Index

| # | 章节主题 | 核心数学方法与核结构物理应用 |
|---|---|---|
| [ch01](chapters/ch01-monopole-tensor-force-and-shell-evolution.md) | 单极张量力、有效单粒子能量与壳演化 | Monopole 矩阵元分解、张量力自旋-轨道重整化、新幻数 $N=16, 32, 34$ 出现 |
| [ch02](chapters/ch02-dripline-continuum-and-gamow-shell-model.md) | 滴线弱束缚、Berggren 基底与 Gamow 壳模型 | 复能量平面动量围道、宽共振、连续谱耦合、$^{28}\text{O}$ 多中子发射动力学 |
| [ch03](chapters/ch03-computational-algorithms-mcsm-and-qvsm.md) | 大尺度算法：MCSM 蒙特卡罗壳模型与 QVSM | 大空间 Slater 维度突破、形变基矢变分优化、能量方差外推与 QVSM 投影 |
| [ch04](chapters/ch04-effective-charges-and-coulomb-excitation.md) | 微观有效电荷、低能库仑激发与矩阵元相消 | GQR 极化电荷、Talmi $^{14}\text{C}$ GT 矩阵元代数相消与 Coulex 四极不变量 |
| [ch05](chapters/ch05-islands-of-inversion-and-nucleon-removal.md) | 极端丰中子反转岛与单核子敲出反应 | $N=40$ 反转岛、形变侵入组态、单核子去除反应微观动量分布与光谱因子 |
| [ch06](chapters/ch06-sn100-region-high-spin-spectroscopy.md) | $^{100}\text{Sn}$ 闭壳近区高自旋与 Seniority 谱学 | 双闭壳坚硬度、$\pi g_{9/2} \otimes \nu g_{9/2}$ 巨 Gamow-Teller 衰变与 Seniority 异能态 |
| [ch07](chapters/ch07-isospin-symmetry-breaking-med-and-ted.md) | 同位旋对称性破缺、MED/TED 与弱电修正 | 库仑单极/多极能差、镜像能级差 MED、超允许 Fermi 衰变内转换修正 $\delta_C$ |
| [ch08](chapters/ch08-double-beta-decay-and-astrophysics.md) | $0\nu\beta\beta$ 双贝塔衰变微观 NME 与天体物理 | 闭合近似、短程关联 SRC、核矩阵元不确定度评估与超新星电子俘获弱反应率 |

## Supporting Reference Files

- [glossary.md](glossary.md) — 现代微观壳模型、单极力、连续谱、反转岛与双贝塔衰变专业术语中英双语定义。
- [patterns.md](patterns.md) — 5 大壳演化单极漂移、连续谱反演与同位旋破缺分析范式。
- [cheatsheet.md](cheatsheet.md) — 单极张量力对偶矩阵元表、典型反转岛核素常数卡与 $0\nu\beta\beta$ 矩阵元汇总卡。

---

## Scope & Limits

本技能提供原子核微观壳模型全谱系方法、单极演化、连续谱边界与微观核矩阵元的严格理论法典。对于非轴对称三轴转子 Davydov-Filippov 模型求解，配合 `greiner-nuclear-models`；对于宏观玻色子相干态投影与相空间分离线，配合 `raduta-nuclear-coherent-states`；对于重离子束能激发函数与熔合势垒穿透，配合 `heavy-ion-nuclear-reactions`；对于在束角分布与偏振双根仲裁，配合 `hamilton-nuclear-spectroscopy`。
