---
name: raduta-nuclear-coherent-states
description: "A. A. Raduta《Nuclear Structure with Coherent States》：相干态模型 (CSM) 与广义相干态 (GCSM)、三维角动量投影算符、半经典三轴转子相空间分离线 (Separatrix)、Holstein-Primakoff 玻色子展开、偶偶核手征双重带微观玻色机制与梨形八极宇称四重带。"
---

<!-- argument-hint: [model-formalism, phase-space, observable, or chapter topic] -->

# 相干态核结构理论：半经典三轴动力学、手征带与角动量投影（A. A. Raduta）

**著者**：A. A. Raduta（罗马尼亚国家物理与核工程研究所 / 罗马尼亚科学院资深院士） | **出版社**：Springer International Publishing Switzerland (2016) | **页数**：524 页
**本地原件**：`raw/books/nuclear structure with coherent states_Raduta.pdf` (SHA-256 `98b057e53e323b0f4781060ad5ae4a8c045ac36b32c0650033953360d951aca3`)

本技能提炼国际著名核理论家 A. A. Raduta 教授经典专著《Nuclear Structure with Coherent States》的核心数学物理体系，系统形式化变形玻色子相干态模型（CSM）与广义相干态模型（GCSM）、三维量子角动量投影算符、半经典三轴转子相空间极值与分离线（Separatrix）拓扑、Holstein-Primakoff 与 Dyson 玻色子展开、偶偶核中的微观手征自发对称性破缺，以及梨形八极相干态与手征-八极宇称四重带（Chiral-Parity Quartets），为从半经典非线性动力学跨越到量子多体严格电磁跃迁提供深厚的第一性原理理论框架。

## How to Use This Skill

- **相干态模型与角动量投影**：询问 `相干态模型CSM`、`广义相干态GCSM`、`变形玻色子基底`、`三维角动量投影算符`、`能带投影正规化积分`；
- **半经典相空间与分离线拓扑**：询问 `半经典三轴转子`、`相空间庞加莱截面`、`分离线Separatrix`、`马鞍点稳定性`、`从摆动进动向手征分岔相变`；
- **玻色子角动量展开**：询问 `Holstein-Primakoff展开`、`Dyson展开`、`高自旋大玻色子极限`、`非轴对称非简谐展开`；
- **偶偶核手征双重带**：询问 `GCSM偶偶核手征带`、`质中玻色子非对称耦合`、`退激带间M1跃迁`、`手征双重带角动量投影`；
- **梨形八极相干态与四重带**：询问 `梨形八极相干态`、`反射不对称相干波函数`、`宇称投影`、`手征-八极宇称四重带`；
- **自洽电磁跃迁算符**：询问 `正则对易子构建M1与E2算符`、`自洽跃迁几率`、`内转换E0算符`。

---

## Core Frameworks and Mental Models

1. **变形四极玻色子相干态与三维角动量投影（第 6 章）**：
   - 引入五维四极玻色子创生算符 $b_{2\mu}^\dagger$（$\mu = -2, \dots, +2$），定义具有内禀四极形变参数 $d$ 与非轴对称参数 $\gamma$ 的未正规化内禀相干基态：
     $$|\psi(d, \gamma)\rangle = \exp\left[ d \left( b_{20}^\dagger + \frac{\gamma}{\sqrt{2}} (b_{22}^\dagger + b_{2-2}^\dagger) \right) \right] |0\rangle;$$
   - **Peierls-Yoccoz 三维连续角动量投影算符**：
     $$\hat{P}_{MK}^I = \frac{2I+1}{8\pi^2} \int D_{MK}^{I*}(\Omega) \hat{R}(\Omega) d\Omega;$$
   - 从单一内禀相干态中自洽投影提取出属于基带（Ground band）、$\beta$ 振动带与 $\gamma$ 振动带的严格具有好自旋 $I$、宇称 $\pi=+$ 的正规化纯正交物理态，彻底消除了微观平均场破坏空间转动对称性的伪相干伪态。

2. **半经典三轴转子相空间极值、分离线 (Separatrix) 与量子进动拓扑（第 4 章）**：
   - 在自旋相干态表象下，将三轴刚体哈密顿量映射为经典相空间欧拉角球面配对正则变量 $(p_\phi = I_z, \phi)$ 上的连续 Hamilton 能量函数：
     $$\mathcal{H}(\theta, \phi) = \langle \theta, \phi | \sum_{k=1}^3 \frac{\hat{I}_k^2}{2\mathcal{J}_k} | \theta, \phi \rangle;$$
   - **相空间定点与稳定性定理**：
     1. 沿最大转动惯量主轴（中间形变轴 $m$ 轴）的极值点为全局能量极小稳定定点；
     2. 沿最小转动惯量主轴（长形变轴 $l$ 轴）的极值点为能量极大稳定定点；
     3. 沿中间转动惯量主轴（短形变轴 $s$ 轴）的极值点为非稳定双曲马鞍点（Hyperbolic Saddle Point）；
   - **分离线 (Separatrix) 能量临界条件**：
     当能量达到穿过中间轴马鞍点的临界能量 $2 E \mathcal{J}_s = I^2$ 时，相轨道分界为双渐近闭合双曲线（分离线）；
     - **分离线内部**：封闭相空间环流，对应量子力学围绕稳定轴的小振幅进动微振荡——**摆动运动 (Wobbling Motion)**；
     - **分离线外部**：大振幅跨越对称双阱的旋转大圆，在奇奇核与多准粒子耦合下演变为自发破缺的时间反演**手征双阱轨道 (Chiral Orbitals)**。

3. **玻色子角动量展开：Holstein-Primakoff 与 Dyson 表象（第 4 章 §4.2）**：
   - 在高自旋渐近极限下（$I \gg 1$），总角动量算符沿短轴或中轴强烈对齐：
   - **Holstein-Primakoff 展开**：
     $$\hat{I}_3 = I - a^\dagger a, \quad \hat{I}_+ = \sqrt{2I - a^\dagger a} \cdot a, \quad \hat{I}_- = a^\dagger \sqrt{2I - a^\dagger a};$$
   - 将非线性转动算符代入三轴哈密顿量，通过级数展开直接解构零阶谐振子频率、一阶四次非简谐相互作用以及玻色子高阶自能修正，给出摆动声子能量随自旋下降或上升的纯解析微分方程。

4. **广义相干态模型 (GCSM) 处理偶偶核手征双重带（第 10 章 §10.1）**：
   - 传统倾斜轴推转（3D-TAC）主要局限于奇奇核两粒子模型，难以处理偶偶核无非满壳未配对核子时的手征对称性；
   - **GCSM 偶偶手征机制**：
     1. 显式引入质子四极玻色子 $b_{p, 2\mu}^\dagger$ 与中子四极玻色子 $b_{n, 2\mu}^\dagger$，两者具有非同轴的相互倾斜内禀主轴；
     2. 耦合两准粒子费米子对（如中子对 $\nu(h_{11/2})^2$ 或质子对 $\pi(h_{11/2})^2$）；
     3. 质子玻色子角动量、中子玻色子角动量与费米子准粒子角动量三者在空间相互正交相互垂直，构成三维内禀手征三面体；
   - 经过角动量与宇称投影后，从单一微观哈密顿量自洽导出偶偶核中具有相同正宇称、近简并、且伴随强带间 $M1$ 跃迁的孪生手征双重带（式 10.1.18–10.1.23）。

5. **梨形八极相干态与手征-八极宇称四重带（第 7 章）**：
   - 引入八极玻色子创生算符 $b_{3\mu}^\dagger$（$\mu = -3, \dots, +3$），构建同时具备四极拉伸形变 $\beta_2$ 与反射不对称八极形变 $\beta_3$ 的相干基底：
     $$|\psi_{\text{oct}}\rangle = \exp\left[ d_2 b_{20}^\dagger + d_3 b_{30}^\dagger \right] |0\rangle;$$
   - **双重对称性破缺（Dual Symmetry Breaking）**：
     系统同时自发破坏时间反演手征对称性（空间手征三面体左/右对偶）与空间反演宇称对称性（梨形反射上下对偶），产生四重简并极小；
     经过三维角动量投影 $\hat{P}^I$ 与正负宇称投影 $\hat{P}^\pm = \frac{1}{2}(1 \pm \hat{\mathcal{P}})$，严格分裂出由**四条旋转能带组成的手征-八极宇称四重带（Chiral-Parity Quartets）**：包含两对相同自旋、相反宇称（$I^+$ 与 $I^-$）的手征双重带，带间被巨大的集体增强电偶极 $E1$ 跃迁与强磁偶极 $M1$ 跃迁紧密交织。

---

## Chapter Index

| # | 章节主题 | 核心数学方法与核结构前沿应用 |
|---|---|---|
| [ch04-sep](chapters/ch04-semiclassical-triaxial-rotors-and-separatrix.md) | 半经典三轴转子相空间与分离线拓扑 | 正则角坐标、庞加莱截面、分离线临界条件 $2E\mathcal{J}_s = I^2$ 与摆动/手征分岔 |
| [ch04-boson](chapters/ch04-boson-expansions-holstein-primakoff.md) | 玻色子展开技术：Holstein-Primakoff 与 Dyson | 高自旋展开、对易代数保真映射、非简谐四次恢复力与摆动非简谐声子谱 |
| [ch06](chapters/ch06-coherent-state-model-and-3d-projection.md) | 相干态模型 (CSM) 与三维角动量投影 | 五维四极相干态、Peierls-Yoccoz 积分核、基带/$\beta$/$\gamma$ 带投影正规化 |
| [ch07](chapters/ch07-pear-shaped-octupole-coherent-states.md) | 梨形八极相干态与手征-八极宇称四重带 | 八极玻色子基底、反射不对称破缺、正负宇称交错带与手征-八极四重带 |
| [ch08](chapters/ch08-quasiparticle-coupling-to-csm-core.md) | 准粒子微观费米子与 CSM 玻色子核芯耦合 | 费米子-玻色子正交混合哈密顿量、高-$j$ 独宇称轨道解耦与多准粒子带头 |
| [ch10](chapters/ch10-gcsm-even-even-chiral-doublet-bands.md) | 广义相干态 (GCSM) 偶偶核手征双重带 | 质中玻色子非同轴手征几何、全对称与反对称态带间 $M1$ 跃迁与投影自洽 |

## Supporting Reference Files

- [glossary.md](glossary.md) — 广义相干态、相空间分离线、Holstein-Primakoff 展开与八极手征四重带专业术语定义。
- [patterns.md](patterns.md) — 5 大半经典相空间分析、角动量投影与玻色展开推演范式。
- [cheatsheet.md](cheatsheet.md) — 相空间分离线能量常数卡、Holstein-Primakoff 代数表与 GCSM 跃迁算符速查卡。

---

## Scope & Limits

本技能提供相干态投影微观玻色理论、半经典相空间分离线拓扑与多极自洽跃迁算符的严格数学物理基础。对于自洽微观协变密度泛函狄拉克时域演化（TD-CDFT），配合 `chirality-and-wobbling-atomic-nuclei`；对于大探测器阵列方向角关联（DCO）与康普顿线偏振实验数据反演，配合 `hamilton-nuclear-spectroscopy`；对于重离子熔合蒸发最佳束能窗口，配合 `heavy-ion-nuclear-reactions`。
