---
type: method
title: "Grodner：126,128Cs 非手征到手征构型转变、电磁选择定则与 g 因子直接测定合同"
aliases: [Grodner Cs chirality, 126Cs 128Cs chiral transition, 2x2 mixing picture, S-symmetry B(M1) staggering, g-factor direct chirality probe]
method_type: "chiral-transition-and-spectroscopic-observables-contract"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Chirality and Wobbling in Atomic Nuclei Ch.7, PDF pp.156-166, full chapter reading"
confidence: "high for formalisms and reported experimental data; conditional for preliminary plunger limits"
tags: [nuclear-chirality, cs-isotopes, 126cs, 128cs, 2x2-mixing, s-symmetry, b-m1-staggering, rdds-plunger, g-factor, aplanarity]
sources: [book-petrache-chirality-and-wobbling]
---

# Grodner：126,128Cs 非手征到手征构型转变、电磁选择定则与 g 因子直接测定合同

## Purpose

本方法合同基于 Ernest Grodner 在专著《Chirality and Wobbling in Atomic Nuclei》第 7 章中的系统论述，
针对低能核结构与奇奇核手征双重带前沿，解决手征双带从带头低自旋“非手征（共面）构型”向高自旋“手征（非共面）构型”
动态转变的物理机制与实验判定标准，特别聚焦于 A≈130 质量区经典候选核 \(^{126,128}\mathrm{Cs}\)：

1. 建立核手征性的 \(2\times2\) 混合代数图景，严格区分手征双重带能级劈裂的两个独立微观机制：穿隧效应（Tunneling）与非正交归一因子（内禀态重叠 \(\langle L \vert R \rangle \ne 0\)）；
2. 澄清能级简并判据在真实核素中的局限性：实验上并未普遍观察到“劈裂随自旋增大急剧减小并平坦化”的理想趋势（图 7.1）；
3. 导出包含左右手态交叉跃迁的带内与带间电磁跃迁几率，确立稳定手征对称下伙伴带电磁强度的对称性；
4. 阐述 \(S\) 对称性（四极形变 \(\alpha\) 宇称反转 + 奇中子与奇质子占有置换）对 \(B(M1)\) 奇偶交错（Staggering）的支配机制，以及在 \(^{128}\mathrm{Cs}\) 低自旋区（\(I < 15\hbar\)）出现的“一单带交错消失、另一带交错加剧”的不对称性微观成因；
5. 结合普朗吉（Plunger）反冲距离法（RDDS）测得的 \(^{128}\mathrm{Cs}\) 低自旋态寿命，确定交错断裂的自旋边界；
6. 确立旋磁因子（\(g\) 因子）作为三自旋张角与非共面体积（Aplanarity）直接实验探针的微观原理，依据 \(^{128}\mathrm{Cs}\) 异能态带头（\(I=9^+, T_{1/2}=56\text{ ns}\)）的 \(g\) 因子实测值，证明低自旋带头处于近共面非手征态，确立了 \(9\hbar \le I \le 14\hbar\) 转变区的存在。

## Inputs and Assumptions

### 2x2 mixing picture and chiral symmetry operator

核手征性属于阿贝尔 \(\mathbb{Z}_2\) 对称群。手征变换算符定义为绕垂直轴转动 \(180^\circ\) 与时间反演的复合操作：

\[
\mathcal{O} = \mathcal{R}_y \mathcal{T} , \quad \mathcal{O}^2 = 1 .
\]

由于包含反幺正算符 \(\mathcal{T}\)，核手征性是建立在核转动与奇核子角动量动力学之上的运动型对称性。
在奇奇核中，角动量由三部分构成：未配对质子 \(\vec j_p\)、未配对中子 \(\vec j_n\) 与甚至核芯转动 \(\vec j_R\)。
描述空间手征取向的无量纲标度为混合自旋标量三重积（Aplanarity 因子）：

\[
\sigma = \frac{(\vec j_p \times \vec j_n)\cdot \vec j_R}{|\vec j_p| |\vec j_n| |\vec j_R|} .
\]

左手内禀态 \(|\sigma = L\rangle\) 与右手内禀态 \(|\sigma = R\rangle\) 满足变换关系：\(\mathcal{R}_y\mathcal{T}\vert L\rangle = \vert R\rangle\)。
由于对易关系 \([\mathcal{R}_y\mathcal{T}, I^2] = 0\) 和 \([\mathcal{R}_y\mathcal{T}, I_z] = 0\)，投影到总自旋 \(I\) 与手征宇称 \(\chi = \pm\) 的真实实验可观测态为：

\[
|IM, \chi = +\rangle = \frac{1}{\sqrt{2}N_+} (\vert IM, L\rangle + \vert IM, R\rangle) , \quad
|IM, \chi = -\rangle = \frac{i}{\sqrt{2}N_-} (\vert IM, L\rangle - \vert IM, R\rangle) .
\]

### Antiunitary property and complex conjugation

由于时间反演算符 \(\mathcal{T}\) 是反幺正算符，反转矩阵元中的手征取向等价于取复共轭：

\[
\langle IM, L  \vert \hat H  \vert IM, L \rangle = \langle IM, R  \vert \hat H  \vert IM, R \rangle^* , \quad
\langle IM, L  \vert \hat H  \vert IM, R \rangle = \langle IM, R  \vert \hat H  \vert IM, L \rangle^* .
\]

归一化条件 \(\langle IM, \pm  \vert IM, \pm\rangle = 1\) 决定了归一因子 \(N_\pm\)：

\[
N_+^2 = \text{Re}\langle L \vert L \rangle + \text{Re}\langle L \vert R\rangle , \quad
N_-^2 = \text{Re}\langle L \vert L \rangle - \text{Re}\langle L \vert R\rangle .
\]

## What It Can Establish

### 1. 手征双重带能级劈裂的双机制源泉

手征对称双重带成员的能量本征值为：

\[
E_+ = \frac{\text{Re}\langle L \vert \hat H \vert L \rangle + \text{Re}\langle L \vert \hat H \vert R \rangle}{N_+^2} , \quad
E_- = \frac{\text{Re}\langle L \vert \hat H \vert L \rangle - \text{Re}\langle L \vert \hat H \vert R \rangle}{N_-^2} .
\]

能级能量差 \(\Delta E(I) = E_- - E_+\) 表明，双重带分裂存在两个根本不同的物理诱因：

1. **左右手势阱间的量子穿隧效应**：由非角对角耦合项 \(\text{Re}\langle L \vert \hat H \vert R  \rangle\) 驱动；
2. **内禀态有限重叠导致的归一因子差异**：即使在穿隧完全消失（即满足条件 \(N_+^2 E_+ = N_-^2 E_-\)）的极限下，只要左右手波函数在空间并非严格分离（\(\text{Re}\langle L \vert R \rangle \ne 0\)），由于 \(N_+ \ne N_-\)，双重态之间**仍然保持有限的能量劈裂**！

### 2. 实验能级劈裂与传统“简并”假设的系统性偏差（图 7.1）

传统简易模型假设手征双带能级差随自旋增大急剧减小并在高自旋区完全稳定（简并）。
Grodner 汇总了 9 个代表性奇奇核候选（\(^{128}\mathrm{Cs}, {}^{126}\mathrm{Cs}, {}^{100}\mathrm{Tc}, {}^{132}\mathrm{La}, {}^{130}\mathrm{La}, {}^{104}\mathrm{Rh}, {}^{136}\mathrm{Pm}, {}^{134}\mathrm{Pr}, {}^{106}\mathrm{Ag}\)）的实测能谱（图 7.1）：

- 几乎所有核均**未出现**理想的“大劈裂急剧减小并进入平坦稳定区”的行为；
- 在 Cs 同位素中，能级差沿整个转动带几乎保持恒定（\(\sim 400\text{ keV}\)）；
- 在其他部分核中，观察到随自旋单调下降但无高自旋稳定平台，更可能归因于两条带主转动惯量的微小差异，而非理想手征静止恢复。

### 3. 带内与带间电磁跃迁几率的代数展开

利用与哈密顿量完全相同的对易子关系 \([\hat T(\text{EM}), \mathcal{R}_y\mathcal{T}] = 0\)，可精确导出双带间的电磁矩阵元：

- **带内跃迁（\(\chi=\pm \to \chi=\pm\)）**：
  \[
  \langle I_2, \pm || \hat T(\text{EM}) || I_1, \pm\rangle = \frac{\text{Re}\langle  I_2, L \vert| \hat T |\vert  I_1, L\rangle \pm \text{Re}\langle  I_2, L \vert| \hat T |\vert  I_1, R\rangle}{N_{I2\pm} N_{I1\pm}} ;
  \]
- **带间跃迁（\(\chi=\pm \to \chi=\mp\)）**：
  \[
  \langle I_2, \pm || \hat T(\text{EM}) || I_1, \mp\rangle = -\frac{\text{Im}\langle  I_2, L \vert| \hat T |\vert  I_1, L\rangle \pm \text{Im}\langle  I_2, L \vert| \hat T |\vert  I_1, R\rangle}{2 N_{I2\pm} N_{I1\mp}} .
  \]

在稳定手征状态下（大非共面度，\(\langle L \vert R \rangle \approx 0\)，且 \(\text{Re}\langle  L\vert|\hat T|\vert R\rangle \approx 0\)），跃迁完全由内禀态本征部分支配，两带对应的带内 \(B(M1), B(E2)\) 以及带间正反向跃迁表现出高度镜像对称。

### 4. S 对称性破缺与 B(M1) 奇偶交错的不对称断裂（图 7.2）

- **\(S\) 对称性本质**：由 Prochniak 于 2011 年推广到 \(\gamma\) 软核的微观对称性，包含四极形变 \(\alpha\) 宇称反转与同壳层奇质子–奇中子粒子/空穴构型置换；
- **交错成因**：当核哈密顿量关于 \(S\) 对称不变时，带内 \(B(M1)\) 展现出特征的奇偶交错现象；
- **\(^{128}\mathrm{Cs}\) 低自旋区异常机制**：
  - 在 \(^{126}\mathrm{Cs}\) 中，\(14\hbar \le I \le 21\hbar\) 全区两带均保持优良的双带 \(B(M1)\) 交错；
  - 在 \(^{128}\mathrm{Cs}\) 中，高自旋区（\(I \ge 15\hbar\)）两带交错对称；但进入 \(I < 15\hbar\) 的低自旋区时，伴随带交错急剧加剧，而主带交错却完全消失！
  - 代数机制：向带头回溯时，核芯角动量 \(j_R\) 减小，系统进入非手征过渡区，交叉矩阵元 \(\text{Re}\langle  L\vert|\text{EM}|\vert R\rangle\) 变为非零。主带中本征项与交叉项反相相消导致交错消失，而伴随带中同相相加导致交错畸变放大；
  - **结论**：这一不对称性实验证实，在进入带头非手征构型时，\(S\) 对称性依然有效，而核手征性本身已开始消解。

### 5. 普朗吉 RDDS 寿命实验确立交错消失边界（图 7.3）

利用重离子反冲距离法（RDDS）测定 \(^{128}\mathrm{Cs}\) 的 \(10^+, 11^+, 12^+\) 态能级寿命：

- 若 \(B(M1)\) 交错按高自旋规律外推，\(10^+\) 态寿命应大于 \(60\text{ ps}\)，\(12^+\) 态大于 \(5\text{ ps}\)，\(11^+\) 态小于 \(1.5\text{ ps}\)；
- 华沙 HIL 与波兰 NCBJ 的实测表明，\(10^+\) 态真实寿命仅为 \(9 \pm 5\text{ ps}\)；
- 证明在 \(I \le 10\hbar\) 处，\(B(M1)\) 交错已经完全断裂，确立了非手征向手征构型演化的低自旋界限。

### 6. 旋磁因子（g 因子）作为非共面度的直接实验探针

相较于能级差与 \(B(M1)\) 这类间接效应，旋磁因子 \(g\) 是唯一直接度量非共面体积的物理量：

1. 奇质子（\(g_p\)）、奇中子（\(g_n\)）与核芯（\(g_R\)）具有完全不同的旋磁比，且总磁矩不受波函数左右手叠加相消影响；
2. \(g\) 因子直接敏感于三自旋张角所张成的立体角体积；
3. \(^{128}\mathrm{Cs}\) 带头 \(I=9^+\) 异能态（\(T_{1/2}=56\text{ ns}\)）的精密核进动测量显示：其角动量不能由单纯纯纯质子–中子准粒子对齐形成，必须包含相当份额的核芯转动 \(j_R\)，且三个角动量处于**近共面几何（Near-planar configuration）**；
4. 这在物理上最终确证了 \(^{128}\mathrm{Cs}\) 的 \(9^+\) 带头是严格非手征的，系统在 \(9\hbar \le I \le 14\hbar\) 之间经历了从平面非手征向非平面立体手征的动态构型演化。

## Experimental and Chiral Analysis Contract

在开展 A≈130 区域奇奇核与中重核手征双带的实验判决时，必须遵守以下合同规则：

1. **严禁仅凭近简并判定手征对称性**：必须区分惯量差导致的偶然近简并与立体非共面转动；即使能级差保持 300–400 keV，只要存在稳定的带间/带内电磁对称性与 \(B(M1)\) 交错，仍可属于有限重叠手征态；
2. **电磁对称性检验**：必须在两带中独立测定绝对 \(B(M1)\) 与 \(B(E2)\)，核验其是否具有相近量级；
3. **\(B(M1)\) 交错与 \(S\) 对称性适用域**：\(B(M1)\) 奇偶交错仅适用于奇质子与奇中子占据相同 \(j\) 壳层（如 \(\pi h_{11/2} \otimes \nu h_{11/2}^{-1}\)）且具有粒子–空穴共轭对称性的体系（如 Cs 同位素与 \(^{136}\mathrm{Nd}\)）；对于非对称壳层占据（如奇 \(A\) 核或跨壳核），不出现交错不构成否定手征性的判据；
4. **带头低自旋断裂区必须开展专用寿命与偏振测量**：不能将高自旋手征几何外推至带头，在 \(I < 14\hbar\) 区间必须通过 RDDS 寿命或束内 \(g\) 因子排查非手征过渡；
5. **归一化重叠因子记录**：理论模型（如 PRM、TAC、TPSM、IBFFM）计算手征态时，应显式输出左右手内禀态重叠 \(\langle L \vert R \rangle\)，明确能量差来自穿隧还是几率非正交。

## What It Cannot Establish Alone

- 简单的 \(2\times2\) 离散两态代数模型无法计算内禀态沿连续手征坐标 \(\sigma\) 的连续波函数分布，必须配合 GCM 或三维 TAC 计算；
- 单个核素的能级差 \(\Delta E(I)\) 不能独立反演左右手态空间重叠大小；
- 带内 \(B(M1)\) 交错虽然强烈支持手征几何，但不能排除轴对称核中特定旋称反转或八极关联造成的偶然交错；
- \(^{128}\mathrm{Cs}\) 的 \(9^+\) 带头共面测量不能自动推广至 \(^{126}\mathrm{Cs}\) 或其他 Cs 同位素，不同同位素的形变硬度与过渡自旋点各有差异。

## Knowledge Impact and Learning Decision

Grodner 的第 7 章是低能核手征领域少有的直接贯通代数对称性、多体波函数重叠微观机制与前沿高精度测量（RDDS 寿命 + 纳秒异能态 \(g\) 因子）的权威实证章节。
它彻底纠正了“手征态必然随自旋增加完全简并”的狭隘教条，为 Wiki 补充了 \(S\) 对称性、两态内禀重叠产生劈裂的机制，以及利用 \(g\) 因子直接测定非共面三轴几何的理论范式。

本单元完成第 7 章全文、公式推导、图 7.1–7.3 及全部参考文献关联的有界核读。

## Evidence and Locators

- Ch.7 pp.137–139 / physical PDF pp.156–158：手征阿贝尔 \(\mathbb{Z}_2\) 对称性、算符 \(\mathcal{R}_y\mathcal{T}\) 对易关系式 (7.1)、\(2\times2\) 混合代数式 (7.2)–(7.4)；
- Ch.7 pp.139–141 / physical PDF pp.158–160：能级劈裂式 (7.5)–(7.7)、穿隧项与非正交归一因子式 (7.8)–(7.10)、图 7.1 全局 9 核能级差实测系统学；
- Ch.7 pp.141–143 / physical PDF pp.160–162：带内式 (7.11) 与带间式 (7.12) 电磁跃迁几率展开、稳定手征对称性；
- Ch.7 pp.143–144 / physical PDF pp.162–163：\(S\) 对称性、\(B(M1)\) 奇偶交错微观机制、图 7.2 \(^{126,128}\mathrm{Cs}\) 低自旋交错不对称性断裂；
- Ch.7 pp.144–146 / physical PDF pp.163–165：华沙 HIL 普朗吉反冲距离法实测（图 7.3）、\(10^+\) 态 \(9\text{ ps}\) 寿命；
- Ch.7 pp.144–146 / physical PDF pp.163–165：\(^{128}\mathrm{Cs}\) 带头 \(I=9^+\)（\(56\text{ ns}\)）\(g\) 因子直接非共面测定；
- 已渲染核对 PDF pp.156、158、160、163、164、165。

## Sources

- [[book-petrache-chirality-and-wobbling]]
- [[petrache-ch3-chiral-geometry-and-selection-boundary]]
- [[petrache-ch5-experimental-wobbling-evidence-contract]]
- [[petrache-ch11-ibfm-mixing-ratio-contract]]
- [[recoil-distance-doppler-shift-plunger-lifetimes]]
- [[global-chiral-doublet-bands-systematics-atlas]]
