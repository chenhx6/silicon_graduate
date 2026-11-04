---
type: method
title: "Zhang 等：过渡核玻尔哈密顿量、γ 振动模型与 MχD/多重摆动微观合同"
aliases: [Zhang gamma vibrational model, Bohr Hamiltonian with gamma-stable potential, CPS E5 X5 Z5 T5, gamma vibration MchiD, wobbling vs gamma vibration discrimination]
method_type: "collective-bohr-hamiltonian-gamma-vibration-contract"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Chirality and Wobbling in Atomic Nuclei Ch.17, PDF pp.323-337, full chapter reading"
confidence: "high for formalisms, calculated curves, and reported data; conditional for model parameter choices"
tags: [bohr-hamiltonian, critical-point-symmetries, gamma-vibration, mchid, wobbling, collective-model, gamma-softness, transitional-nuclei]
sources: [book-petrache-chirality-and-wobbling]
---

# Zhang 等：过渡核玻尔哈密顿量、γ 振动模型与 MχD/多重摆动微观合同

## Purpose

本方法合同基于张宇、姜宏弟、亓斌在专著《Chirality and Wobbling in Atomic Nuclei》第 17 章的系统研究，
解决低能核结构中粒子转子模型（PRM）将核芯 \(\beta\) 与 \(\gamma\) 形变完全冻结为刚性参数的理论局限，
从包含动态形变自由度的完整玻尔哈密顿量（Bohr Hamiltonian）及临界点对称性（CPS：E(5), X(5), Z(5), T(5)）出发，
通过“核芯–粒子耦合机制”建立具有 \(\gamma\) 稳定谐振势能的集体微观模型，并在以下重大理论争议与实验判据中确立分析规范：

1. **超越刚性转子假定**：将 \(\beta\) 刚性但具备平衡三轴度 \(\gamma_e\) 的 \(\gamma\) 振动动力学引入奇奇核与奇 \(A\) 核多体哈密顿量，实现转动与 \(\gamma\) 振动自由度的绝热代数分离；
2. **多重手征双重带（M\(\chi\)D）的全新物理机制：\(\gamma\) 振动声子多重态（图 17.1–17.2）**：打破“M\(\chi\)D 只能由不同多准粒子构型产生”的传统狭隘认知，证明在同一粒子–空穴构型（\(\pi h_{11/2} \otimes \nu h_{11/2}^{-1}\)）上，基于核芯 \(\gamma\) 振动激发（\(n_{\gamma'} = 0, 1, 2, \dots\)）即可天然产生多套具有高度镜像电磁对称性的手征双重能带；
3. **奇 \(A\) 核多重转动–摆动双重带（Multiple Wobbling Bands，图 17.3–17.4）**：阐明单准粒子与三轴核芯耦合时，核芯 \(\gamma\) 振动激发可自然派生出一组多重转动–摆动双重带序列（\(n_{\gamma'} = 0, 1, 2\) 叠加 \(n_\omega = 0, 1\)）；
4. **摆动运动（Wobbling）与 \(\gamma\) 振动（\(\gamma\)-vibration）的竞争判决与鉴别法典**：针对 A≈130 质量区（如 \(^{135}\mathrm{Pr}, {}^{130}\mathrm{Ba}, {}^{187}\mathrm{Au}\)）中伴随带究竟属于“三轴横向/纵向摆动”还是“奇核子耦合的 \(\gamma\) 振动带”这一长期核心论争，从微观矩阵元层面揭示两者的电磁相似性与能谱鉴别特征。

## Inputs and Assumptions

### Critical Point Symmetries (CPS) in the Bohr Hamiltonian

经典五维玻尔哈密顿量：

\[
\hat H_{\rm Bohr} = -\frac{\hbar^2}{2B} \left[ \frac{1}{\beta^4}\frac{\partial}{\partial\beta}\beta^4\frac{\partial}{\partial\beta} + \frac{1}{\beta^2\sin3\gamma}\frac{\partial}{\partial\gamma}\sin3\gamma\frac{\partial}{\partial\gamma} - \frac{1}{4\beta^2}\sum_{k=1}^3 \frac{L_k^2}{\sin^2(\gamma-\frac{2}{3}k\pi)} \right] + V(\beta, \gamma) .
\]

不同势阱形式定义了形状相变临界点基准：

- **E(5)**：球形到 \(\gamma\) 不稳定（\(U(5)\leftrightarrow O(6)\)）相变，\(V(\beta,\gamma) = V(\beta)\)（\(\beta\) 无限深方势阱，与 \(\gamma\) 无关），波函数由球贝塞尔函数解析给出；
- **X(5)**：球形到长椭（\(U(5)\leftrightarrow SU(3)\)）相变，\(\beta\) 为方势阱，\(V(\gamma) = \frac{1}{2}a^2\gamma^2\) 局域于 \(\gamma=0^\circ\) 附近小振动；
- **Z(5)**：长椭到扁椭三轴相变，\(V(\gamma) = \frac{1}{2}c(\gamma - \pi/6)^2\)，势能极小锁定于最大三轴度 \(\gamma = 30^\circ\)；
- **T(5)**：普遍三轴相变，势能形式取为 \(V(\gamma) = \frac{1}{2}c(\gamma - \gamma_e)^2\)，平衡三轴度可在 \(0 \le \gamma_e \le \pi/3\) 间自由取值。

### Core-particle coupling with a gamma-stable potential

奇奇核总哈密顿量取为：\(\hat H = \hat H_c + \hat H_p + \hat H_n\)，总角动量 \(\vec I = \vec L + \vec j_p + \vec j_n\)。
在 \(\beta\) 刚性但 \(\gamma\) 稳定的核芯近似下：

\[
\hat H_c = -\frac{\hbar^2}{2B\beta^2}\frac{1}{\sin3\gamma}\frac{\partial}{\partial\gamma}\sin3\gamma\frac{\partial}{\partial\gamma} + \frac{\hbar^2}{8B\beta^2}\sum_{k=1}^3 \frac{L_k^2}{\sin^2(\gamma-\frac{2}{3}k\pi)} + V(\gamma) ,
\]

其中核芯势能取为谐振子形式：

\[
V(\gamma) = \frac{\bar c}{4B\beta^2}(\gamma - \gamma_e)^2 .
\]

价准粒子哈密顿量采用单 \(j\) 壳层三轴势场表达式式 (17.46)，耦合系数 \(C_\sigma = \pm \frac{195}{2j_\sigma(j_\sigma+1)} A^{-1/3}\beta\)。
在绝热近似下，转动项与单粒子项在平衡点 \(\gamma \approx \gamma_e\) 展开，体系波函数严格分离为转动–内禀部分与 \(\gamma\) 振动部分：

\[
\Psi = f(\gamma') \phi(\theta_i, a_p, a_n) , \quad \gamma' = \gamma - \gamma_e .
\]

## What It Can Establish

### 1. 转动与 \(\gamma\) 振动的代数本征分解

体系总能量本征值解析表述为：

\[
E(s, I, n_{\gamma'}) = E_0 + A' n_{\gamma'} + B' r_s^I ,
\]

其中：

- \(n_{\gamma'} = 0, 1, 2, \dots\) 为一维厄米多项式描述的 \(\gamma\) 振动谐振子量子数；
- \(s = 1, 2, 3, \dots\) 为角动量本征值方程（形式与 PRM 矩阵对角化完全一致）在给定 \(I, M\) 下的能级排序量子数；
- 该公式严格表明：在绝热近似下，**核芯的 \(\gamma\) 振动激发主要平移带头激发能（由 \(A' n_{\gamma'}\) 决定），而完整保留了各带内基于三轴转动的相对激发能谱与电磁跃迁特征**。

### 2. \(\gamma\) 振动诱发的 M\(\chi\)D 新机制（图 17.1 与图 17.2）

在 \(\pi h_{11/2} \otimes \nu h_{11/2}^{-1}\) 且 \(\gamma_e = 30^\circ\) 条件下：

- 零声子态 \(n_{\gamma'} = 0\) 上的 \(s=1, 2\) 构成了经典基态手征双重带（在 \(I \ge 11\hbar\) 以上展现出高度近简并）；
- 激发声子态 \(n_{\gamma'} = 1, 2, \dots\) 上的 \(s=1, 2\) 能级带直接复现了与基带完全全同的转动能谱与近简并特征（图 17.1）；
- 理论证明，在绝热近似下，同一 \(s\) 的能带其带内 \(B(E2)\) 与 \(B(M1)\) 跃迁完全独立于 \(\gamma\) 振动量子数 \(n_{\gamma'}\)（图 17.2）：带内 \(B(E2)\) 随自旋上升单调增大，带内 \(B(M1)\) 展现出特征的先降后起伏行为；
- **物理结论**：这在理论上确立了 M\(\chi\)D 的第三种产生机制——基于单一准粒子构型耦合核芯的大振幅 \(\gamma\) 振动，为实验上寻找具有相同组态的多重手征带提供了微观依据。

### 3. 奇 \(A\) 核多重转动–摆动双重带（图 17.3 与图 17.4）

当单质子（如 \(\pi h_{11/2}\)）与 \(\gamma\) 稳定三轴核芯（\(\gamma_e = 30^\circ\)）耦合时：

- 零声子态 \(n_{\gamma'} = 0\) 产生主转动带（\(n_\omega = 0\)）与单声子摆动伙伴带（\(n_\omega = 1\)）；
- 激发声子态 \(n_{\gamma'} = 1, 2\) 衍生出平行的激发双重带序列，构成了“多重转动–摆动双重带”；
- 在流体动力学转动惯量下，摆动能 \(E_{\rm wob}(I)\) 在 \(I > 19/2\hbar\) 随自旋上升，表现为纵向摆动（LW）特征；
- 跨带连接跃迁具有强集体四极特性（\(B(E2)_{\rm out}/B(E2)_{\rm in} \sim 0.3\)–\(0.8\)），而 \(B(M1)\) 相对比值受到压制。

### 4. 摆动模式（Wobbling）与 \(\gamma\) 振动（\(\gamma\)-vibration）的微观辨识法典

本章从深层代数结构上厘清了两者长期困扰实验谱学的交叠与区分标志：

1. **电磁跃迁特征的表面重叠性**：
   - 奇 \(A\) 核中单一高 \(j\) 准粒子耦合到 \(\gamma\) 振动核芯所产生的激发带，向基态带退激时**同样以 \(\Delta I=1\) 的强集体 \(E2\) 跃迁为主导**（\(B(E2)_{\rm out}/B(E2)_{\rm in} \sim 0.5\)）；
   - 这表明：**单纯观测到跨带强集体 \(E2\) 跃迁，不足以排他性确立刚性三轴摆动运动**，它完全可能来自软核体系中的单声子 \(\gamma\) 振动耦合！
2. **区分两者的决定性结构判据**：
   - **多声子阶梯结构**：纯粹的多声子谐振摆动运动要求能带间距呈现近乎等间距排列（\(n_\omega = 0, 1, 2\)），且跃迁比率满足严格的振幅加倍关系 \(B(E2; n_\omega=2 \to 1) \approx 2 \times B(E2; n_\omega=1 \to 0)\)；
   - **带头物理本质**：\(\gamma\) 振动激发在实验能谱中会引入独立的带头能隙（在过渡核区典型为 \(0.8\)–\(1.5\text{ MeV}\)），其微观波函数是沿 \(\gamma\) 坐标振动的波包，对偶偶核芯具有清晰的 \(K=2\) 投影声子特征；
   - **\(\gamma\) 软度与交错指数**：在偶偶核芯中，若基准 \(\gamma\) 带的奇偶自旋交错指数 \(S(I) = \frac{[E(I)-E(I-1)] - [E(I-1)-E(I-2)]}{E(2_1^+)}\) 呈现大振幅交错且奇自旋偏低，核芯属于非轴对称刚性三轴；若交错微弱或反向，核芯属于大振幅 \(\gamma\) 软核，此时奇 \(A\) 伴随带更应理解为四极振动与转动的动力学耦合，而非纯纯经典刚体摆动。

## Experimental and Spectroscopic Analysis Contract

在开展 A≈130 区域奇 \(A\) 与奇奇核摆动/手征带的实验指认时，必须严格执行以下判据合同：

1. **严禁仅凭单对能带的跨带强 E2 跃迁直接宣布发现摆动运动**：
   必须全面评估核芯的 \(\gamma\) 软度；若相邻偶偶核的 \(2_2^+\) 能级偏低（低于或接近 \(4_1^+\) 能量）且 \(S(J)\) 符合 \(\gamma\) 软核特征，必须在论文中同时给出“四极 \(\gamma\) 振动声子耦合说”作为首要竞争解释；
2. **M\(\chi\)D 机制归类三原则**：
   当在同一核内发现两对以上手征双带时，必须通过在束谱学区分其物理机制：
   - **机制 I（多准粒子组态型）**：两对双带基于完全不同的单粒子壳层占据（如 2-qp vs 4-qp，具有不同带头自旋宇称）；
   - **机制 II（形状共存型）**：基于相同组态但在不同形变极小（不同 \((\beta, \gamma)\)）中局域；
   - **机制 III（\(\gamma\) 振动声子型）**：双带基于相同组态，且高激发双带展现出与基准双带高度全同的相对转动结构，带头能量间隔对应核芯 \(\gamma\) 声子能量；
3. **多声子比率检验**：若主张多声子摆动，必须定量测量 \(B(E2; 2 \to 1)\) 与 \(B(E2; 1 \to 0)\) 之比，并排查跨两声子直跃 \(B(E2; 2 \to 0)\) 的抑制上限。

## What It Cannot Establish Alone

- 简化的谐振势 \(V(\gamma) = \frac{\bar c}{4B\beta^2}(\gamma - \gamma_e)^2\) 属于近似模型势，无法替代全自洽微观能量泛函计算得出的真实非对称或平底大振幅 \(\gamma\) 势能曲面；
- 绝热近似将转动与 \(\gamma\) 振动严格解耦，忽略了高转速下 Coriolis 力引起的转动–振动动态耦合及离心拉伸效应；
- 模型假设 \(\beta\) 刚性，在强 \(\beta\)-\(\gamma\) 耦合区（如临界点核）必须采用完全可分离的数值求解器。

## Knowledge Impact and Learning Decision

张宇等人的第 17 章为全库的三轴形变前沿研究补上了最关键的一块理论拼图：
它将临界点对称性（E(5), X(5), Z(5), T(5)）与玻尔集体哈密顿量引入手征与摆动领域，
首创了由 \(\gamma\) 振动声子激发产生 M\(\chi\)D 与多重摆动带的物理机制，
并在微观层面为判定真实的横向/纵向摆动运动与核芯 \(\gamma\) 振动耦合带提供了界限清晰的分析判据。

本单元完成第 17 章全文、公式推导及图 17.1–17.4 的系统精读与核验。

## Evidence and Locators

- Ch.17 pp.304–305 / physical PDF pp.323–324：Bohr 哈密顿量与 PRM 局限、临界点对称性发展背景；
- Ch.17 pp.305–309 / physical PDF pp.324–328：经典 CPS 求解（E(5) 式 17.2–17.8、X(5) 式 17.9–17.20、Z(5) 式 17.21–17.30、T(5) 式 17.31–17.41）；
- Ch.17 pp.309–312 / physical PDF pp.328–331：奇体系 \(\gamma\) 振动模型哈密顿量式 (17.42)–(17.47)、绝热变量分离式 (17.48)–(17.51)、转动方程与 \(\gamma\) 振动方程求解式 (17.52)–(17.57)、总能公式式 (17.58)、电磁跃迁算符式 (17.59)–(17.62)；
- Ch.17 pp.312–314 / physical PDF pp.331–333：奇奇核 M\(\chi\)D 图 17.1 能级谱与图 17.2 在带 \(B(E2)/B(M1)\) 跃迁；
- Ch.17 pp.314–316 / physical PDF pp.333–335：奇 \(A\) 核多重摆动带图 17.3 能级谱与图 17.4 摆动能及 \(B(E2)_{\rm out}/B(E2)_{\rm in}\) 比值；
- Ch.17 pp.315–316 / physical PDF pp.334–335：摆动与 \(\gamma\) 振动竞争判决、M\(\chi\)D 机制归类与总结；
- 已渲染核对 PDF pp.324、326、328、329、330、331、332、333、334。

## Sources

- [[book-petrache-chirality-and-wobbling]]
- [[collective-quadrupole-pes-and-gamma-softness]]
- [[chen-cdft-prm-wobbling-and-fermi-surface-contract]]
- [[sheikh-tpsm-wobbling-and-triaxial-projection-contract]]
- [[multiple-chiral-doublets-and-chiral-parity-quartets]]
- [[multiphonon-wobbling-and-anharmonicity-dynamics]]
- [[odd-a-wobbling-mode-stability-and-bifurcation]]
