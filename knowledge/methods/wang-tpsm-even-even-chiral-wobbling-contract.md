---
type: method
title: "Wang：三轴投影壳模型（TPSM）偶偶核多重手征与两准粒子摆动合同"
aliases: [Wang TPSM even-even chirality wobbling, 136Nd even-even MchiD, 130Ba 2qp wobbling TPSM, K-plot and azimuthal plot, chiral vibration to static transition]
method_type: "even-even-tpsm-chiral-wobbling-contract"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Chirality and Wobbling in Atomic Nuclei Ch.14, PDF pp.292-301, full chapter reading"
confidence: "high for formalisms, calculated curves, and reported data; conditional for model parameter choices"
tags: [tpsm, even-even-nuclei, 136nd, 130ba, mchid, two-quasiparticle-wobbling, k-plot, azimuthal-plot, chiral-vibration, static-chirality]
sources: [book-petrache-chirality-and-wobbling]
---

# Wang：三轴投影壳模型（TPSM）偶偶核多重手征与两准粒子摆动合同

## Purpose

本方法合同基于王亚坤在专著《Chirality and Wobbling in Atomic Nuclei》第 14 章的系统论述，
针对低能核物理中非轴对称三轴集体运动的两大前沿——偶偶核多重手征双重带（M\(\chi\)D）与偶偶核两准粒子摆动运动（Wobbling motion），
解决传统唯象模型无法微观描述内禀波函数空间几何取向的瓶颈，
确立基于三维严格角动量投影壳模型（TPSM）、Pfaffian 算法以及集体波函数空间分布（\(K\) 截面图与方位角投影图 Azimuthal plot）的微观分析合同，
特别聚焦于 A≈130 质量区两个标志性偶偶核基准：

1. **\(^{136}\mathrm{Nd}\) 偶偶核五对手征候选带的微观动力学机制**：在包含高达 6 准粒子态的投影空间中，系统再现各双重带能级谱与 \(B(M1)/B(E2)\) 比值，微观揭示从低自旋“手征振动（Chiral vibration）”向高自旋“静态手征转动（Static chirality）”的相变过程；
2. **\(K\) 截面图与方位角分布图（Azimuthal plot）的几何量化**：利用集体波函数在主轴坐标系下的展开，在二维 \((\theta, \varphi)\) 球面上直视角动量空间取向几率密度分布，严格定义共面与非共面取向；
3. **偶偶核 \(^{130}\mathrm{Ba}\) 两准粒子横向摆动微观解构**：基于 \(\pi h_{11/2}^2\) 两准粒子构型，解释为何在偶偶核中跨带 \(\Delta I=1\) 的 \(B(M1)\) 跃迁未如奇 \(A\) 核那样被强烈压制，而是与 \(B(E2)\) 相当的微观机理；
4. **摆动模式的方位角节点拓扑验证**：通过方位角几率分布 \(P(\theta, \varphi)\) 证明零声子态（\(n=0\)）在短轴呈现单峰，而一单声子态（\(n=1\)）在短轴出现严格零点（节点）并分裂为对称双峰，微观确证角动量绕短轴进动的横向摆动几何。

## Inputs and Assumptions

### Pairing-plus-quadrupole TPSM Hamiltonian

在包含单粒子能量、自洽四极–四极相互作用、单极配对和四极配对的微观哈密顿量下：

\[
\hat H = \hat H_0 - \frac{\chi}{2}\sum_\mu \hat Q_{2\mu}^\dagger \hat Q_{2\mu} - G_M \hat P^\dagger \hat P - G_Q \sum_\mu \hat P_{2\mu}^\dagger \hat P_{2\mu} .
\]

对偶偶核，内禀构型空间扩展至最高 6 准粒子态（式 14.3），包括 0-qp 真空、2-qp（中子对、质子对）、4-qp（2 质子 + 2 中子，4 中子，4 质子）及 6-qp 态。
利用三维角动量投影算符 \(\hat P^I_{MK} = \frac{2I+1}{8\pi^2}\int d\Omega D^{I*}_{MK}(\Omega)\hat R(\Omega)\) 恢复好角动量 \(I\) 与 \(M\)，并借助高效的 Pfaffian 算法求解 Hill–Wheeler 广义本征方程：

\[
\sum_{K' \kappa'} \left\{ \langle \Phi_\kappa  \vert \hat H \hat P^I_{KK'}  \vert \Phi_{\kappa'} \rangle - E_\sigma^I \langle \Phi_\kappa  \vert \hat P^I_{KK'}  \vert \Phi_{\kappa'} \rangle \right\} f_{K'\kappa'}^{I\sigma} = 0 .
\]

### K-plot and Azimuthal plot definitions

由于投影基底非正交，展开系数 \(f_{K\kappa}^{I\sigma}\) 不能直接作为几率。定义正交归一化的集体波函数：

\[
g^{I\sigma}(K, \kappa) = \sum_{K'\kappa'} \left(N^I\right)^{1/2}(K, \kappa; K', \kappa') f_{K'\kappa'}^{I\sigma} .
\]

在此基础上构造三维空间取向观测量：

1. **\(K\) 截面图（\(K\) plot）**：给出总角动量在内禀长轴（\(l\)）、中间轴（\(m\equiv i\)）和短轴（\(s\)）上的分量几率分布：
   \[
   p^{I\sigma}(|K|) = \sum_\kappa \left( |g^{I\sigma}(K, \kappa)|^2 + |g^{I\sigma}(-K, \kappa)|^2 \right) ;
   \]
2. **方位角投影图（Azimuthal plot）**：给出角动量矢量在内禀空间方向角 \((\theta, \varphi)\) 上的二维几率密度分布：
   \[
   P(\theta, \varphi) = \sum_\kappa \int_0^{2\pi} d\psi |G^{II}(\psi, \theta, \pi-\varphi, \kappa)|^2 ,
   \]
   其中极角 \(\theta\) 为角动量与长轴夹角，方位角 \(\varphi\) 为其在 \(s-m\) 平面投影与短轴夹角。

## What It Can Establish

### 1. \(^{136}\mathrm{Nd}\) 偶偶核 M\(\chi\)D 与手征振动向静态转动相变（图 14.1–14.3）

在偶偶核 \(^{136}\mathrm{Nd}\) 中，实验观测到 5 对近简并带（D1–D5 及伴随带 D1-C 至 D5-C）：

- **能谱与电磁比率一致性**：TPSM 计算的能谱与实验符合优良（图 14.1），各双重带成员的能级差极小，且 \(B(M1)/B(E2)\) 比值呈现随自旋下降的共同趋势；
- **手征振动阶段（\(I = 15\hbar\)）**：
  - 主带 D1 的方位角分布在 \((\theta = 51^\circ, \varphi = 90^\circ)\) 呈现单峰，角动量局域在 \(s-l\) 主平面内（共面旋转相）；
  - 伴随带 D1-C 在 \(\varphi = 48^\circ\) 与 \(132^\circ\) 呈现关于 \(90^\circ\) 对称的双峰分布；
  - \(K\) 图显示 D1 在中间轴（\(i\) 轴）上的分布峰值位于 \(K_i = 0\hbar\)，而 D1-C 在 \(K_i = 0\hbar\) 处严格为零；
  - 这严格证明了在低自旋端，伴随带是主带的手征振动声子激发态（0 声子 vs 1 声子）；
- **静态手征相变（\(I = 19\hbar\)）**：
  - D1 与 D1-C 的方位角分布均自发分裂为偏离主平面的对称双峰（非共面立体旋转）；
  - 中间轴 \(K\) 图在 \(K_i = 15\hbar\) 处出现显著大几率峰，且两带的 \(K\) 谱完全一致；
  - 严格微观证实系统在自旋驱动下完成了从手征振动向**静态手征转动**的动力学相变；
- 对 D2/D2-C、D4/D4-C、D5/D5-C 展现出相似相变，而 D3/D3-C 则表现出更强的多组态混合与污染。

### 2. 偶偶核两准粒子横向摆动微观机理（\(^{130}\mathrm{Ba}\) 案例，图 14.4–14.7）

针对首例偶偶核两准粒子摆动核 \(^{130}\mathrm{Ba}\)（带 \(S1\) 与 \(S1'\)）：

1. **摆动能随自旋下降（TW 特征）**：
   理论计算的摆动能量 \(E_{\rm wob}(I) = E_{n=1}(I) - \frac{1}{2}[E_{n=0}(I+1) + E_{n=0}(I-1)]\) 随自旋升高而单调减小（图 14.4 下面板），与实验数据高度一致，证实其具有横向摆动（TW）动力学特征；
2. **\(B(M1)\) 跃迁不被压制的两准粒子物理机制**：
   - 传统奇 \(A\) 核单粒子摆动中，跨带 \(B(M1)\) 受到极强抑制（与 \(B(E2)\) 之比 \(\ll 0.1\)）；
   - 在 \(^{130}\mathrm{Ba}\) 中，实验与 TPSM 均表明跨带 \(B(M1)_{\rm out}/B(E2)_{\rm in}\) 达到了与 \(B(E2)_{\rm out}/B(E2)_{\rm in}\) 相当的量级（图 14.5）；
   - **微观解释**：摆动带由质子两准粒子组态 \(\pi(h_{11/2})^2\) 构成，双质子对齐极大地放大了内禀磁偶极矩阵元，使得即使在集体摆动框架下，跨带 \(\Delta I=1\) 的 \(M1\) 跃迁依然非常强；
3. **方位角节点拓扑验证摆动轴进动（图 14.6）**：
   - 零声子带（\(n=0\)，偶自旋 \(I=10, 16, 22\hbar\)）：方位角几率 \(P(\theta, \varphi)\) 在 \(\varphi = 90^\circ\) 呈现单个对称峰，角动量紧密沿短轴取向；
   - 一声子带（\(n=1\)，奇自旋 \(I=11, 17, 23\hbar\)）：在 \(\varphi = 90^\circ\) 出现严格的几率极小（零点节点），并在两侧对称偏离（\(\varphi \approx 60^\circ\) 与 \(120^\circ\)）；
   - 这一波函数拓扑直接证明了角动量围绕短轴发生的一维谐振进动（Precession around short axis）。

## Experimental and Spectroscopic Analysis Contract

在采用 TPSM 分析偶偶核多重手征与两准粒子摆动能带时，必须遵循以下合同准则：

1. **内禀组态多重性检查**：偶偶核高自旋带涉及 0-qp、2-qp、4-qp、6-qp 态的剧烈交叉，必须在 TPSM 基底中包含充分的准粒子截断空间，不能将跨带混合引起的能级反常误判为手征消失；
2. **区分手征振动与静态手征**：通过 \(K\) 图与方位角图判别低自旋区是否属于手征振动；只有在双带均展现偏离主平面的非零中间轴投影且出现对称双峰时，方可宣称静态手征转动；
3. **偶偶核摆动不能机械套用 M1 压制判据**：对于多准粒子构型驱动的摆动模式，禁止简单以 \(B(M1)\) 强弱作为否定摆动的依据，必须通过 \(B(E2)\) 的集体增强及方位角节点特征联合确证；
4. **形变参数敏感性**：形变参数 \(\beta\) 直接决定带头激发能，必须依据相邻核库仑激发或微观泛函约束，不可随意漂移参数。

## What It Cannot Establish Alone

- TPSM 使用唯象配对加四极（P+Q）相互作用，模型依赖于单极配对强度 \(G_M\) 与四极配对 \(G_Q\) 的唯象经验拟合；
- 模型空间截断限制了在超高自旋（\(I > 25\hbar\)）下更高准粒子激发（如 8 准粒子）的描述；
- 方位角图 \(P(\theta, \varphi)\) 和 \(K\) 图属于模型波函数重构指标，无法直接在探测器上作为分立能谱观测，必须通过跃迁分支比与寿命间接检验。

## Knowledge Impact and Learning Decision

王亚坤的第 14 章将三轴投影壳模型推向了偶偶核多准粒子前沿：
它系统建立了 \(^{136}\mathrm{Nd}\) 偶偶核 5 对 M\(\chi\)D 带的手征振动向静态转动演化图景，
微观破解了偶偶核 \(^{130}\mathrm{Ba}\) 两准粒子横向摆动中 \(M1\) 跃迁未被压制的物理本质，
并确立了 \(K\) 图与方位角投影图作为三维非共面与摆动进动角动量几何的微观诊断标准。

本单元完成第 14 章全文、公式推导及图 14.1–14.7 的系统精读与核验。

## Evidence and Locators

- Ch.14 pp.273–274 / physical PDF pp.292–293：手征与摆动运动背景、全球实验概况；
- Ch.14 pp.274–276 / physical PDF pp.293–295：P+Q 哈密顿量式 (14.1)、变分式 (14.2)、偶偶核多准粒子基底式 (14.3)、3D 投影式 (14.4)–(14.5)、Hill–Wheeler 广义本征式 (14.6)–(14.7)、集体波函数式 (14.8)、\(K\) 图式 (14.9)、方位角分布图式 (14.10)–(14.11)；
- Ch.14 pp.276–278 / physical PDF pp.295–297：\(^{136}\mathrm{Nd}\) 5 对手征双带能谱与 \(B(M1)/B(E2)\) 图 14.1、\(K\) 图 14.2（\(l, i, s\) 轴分布）、方位角投影图 14.3（手征振动向静态转动相变）；
- Ch.14 pp.279–281 / physical PDF pp.298–300：\(^{130}\mathrm{Ba}\) 偶偶核两准粒子摆动能谱与 \(E_{\rm wob}(I)\) 图 14.4、跃迁比率图 14.5、方位角节点图 14.6、\(K\) 图 14.7；
- Ch.14 pp.281–282 / physical PDF pp.300–301：总结与全微观泛函投影展望；
- 已渲染核对 PDF pp.295、296、297、298、299。

## Sources

- [[book-petrache-chirality-and-wobbling]]
- [[sheikh-tpsm-wobbling-and-triaxial-projection-contract]]
- [[chen-cdft-prm-wobbling-and-fermi-surface-contract]]
- [[multiple-chiral-doublets-and-chiral-parity-quartets]]
- [[multiphonon-wobbling-and-anharmonicity-dynamics]]
- [[chiral-vibrational-tunneling-and-double-well-splitting]]
- [[chiral-geometry-tilted-axis-cranking-and-aplanarity]]
