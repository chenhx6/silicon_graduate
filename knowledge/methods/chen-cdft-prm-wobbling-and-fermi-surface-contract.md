---
type: method
title: "Chen 等：CDFT+PRM 微观摆动运动、费米面演化与偶偶核两准粒子摆动合同"
aliases: [Chen CDFT PRM wobbling, TW and LW Fermi surface evolution, 130Ba two-quasiparticle wobbling, N=59 isotone wobbling, spin coherent state probability distribution]
method_type: "triaxial-wobbling-cdft-prm-microscopic-contract"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Chirality and Wobbling in Atomic Nuclei Ch.10, PDF pp.222-238, full chapter reading"
confidence: "high for formalisms, calculated curves, and reported data; conditional for model parameter choices"
tags: [wobbling, transverse-wobbling, longitudinal-wobbling, cdft-prm, fermi-surface, 130ba, n59-isotones, multiphonon-wobbling, spin-coherent-state]
sources: [book-petrache-chirality-and-wobbling]
---

# Chen 等：CDFT+PRM 微观摆动运动、费米面演化与偶偶核两准粒子摆动合同

## Purpose

本方法合同基于陈启博、戴华明、李英芝在专著《Chirality and Wobbling in Atomic Nuclei》第 10 章的系统研究，
解决低能核结构中摆动运动（Wobbling motion）微观机制与唯象模型之间的参数鸿沟：
通过将自洽相对论/协变密度泛函理论（CDFT）与严格恢复实验室转动对称性的粒子转子模型（PRM）无缝结合（CDFT+PRM），
由微观限制三轴形变能面计算直接导出核芯形变参数 \((\beta, \gamma)\) 与单粒子能级，摆脱传统 PRM 对形变的人工唯象拟合，
并在以下核心课题中建立定量的微观分析合同：

1. **费米面位置对摆动模式（TW 与 LW）的决定性控制律**：定量揭示价准粒子沿变形单 \(j\) 壳层从底部（DALs 粒子）、中部（FAL）到顶部（DALl 空穴）演化时，双带能量差 \(\Delta E(I)\) 与电磁跃迁比率的特征演变；
2. **形变参数对摆动稳定性的敏感性**：四极形变 \(\beta\) 与三轴形变 \(\gamma\) 对横向摆动临界拐点自旋、失稳区（\(\Delta E < 0\)）及向纵向摆动转变的动力学制约；
3. **多极混合比 \(\delta(E2/M1)\) 的准粒子符号定理**：准质子与准中子横向摆动跃迁混合比符号相反的微观起源；
4. **\(A\approx100\) 质量区 \(N=59\) 同中子素链摆动系统学**：以 \(^{105}\mathrm{Pd}\)（已证实首个中子 TW）为基准，利用约束 CDFT 预言 \(^{97}\mathrm{Sr}, {}^{99}\mathrm{Zr}\) 的中子横向摆动带；
5. **偶偶核两准粒子摆动第一例：\(^{130}\mathrm{Ba}\) 微观剖析**：基于 PC-PK1 泛函确定 \(\pi h_{11/2}^2\) 组态（\(\beta=0.24, \gamma=21.5^\circ\)），并通过自旋相干态（SCS）二维角几率分布 \(P(\theta, \phi)\) 严格验证多声子摆动（\(n=0,1,2,3\)）的波函数节点拓扑特征。

## Inputs and Assumptions

### CDFT+PRM integrated Hamiltonian

在实验室系中，总角动量 \(\vec I\) 为守恒好量子数。PRM 将体系分解为三轴转子与价准粒子：

\[
\hat H_{\rm PRM} = \hat H_{\rm coll} + \hat H_{\rm intr} , \quad
\hat H_{\rm coll} = \sum_{k=1}^3 \frac{(I_k - j_k)^2}{2\mathcal{J}_k} ,
\]

式中 \(\mathcal{J}_k\) 为三个惯性主轴的转动惯量；单 \(j\) 壳层内禀哈密顿量为：

\[
\hat h_p = \frac{1}{2} C \left\{ \cos\gamma \left[ j_3^2 - \frac{j(j+1)}{3} \right] + \frac{\sin\gamma}{2\sqrt{3}} (j_+^2 + j_-^2) \right\} ,
\]

其中耦合强度 \(C = \frac{123}{8}\sqrt{\frac{5}{\pi}}\frac{2N_{\rm osc}+3}{j(j+1)} A^{-1/3}\beta\)。
BCS 配对能量取为 \(\epsilon_\nu = \sqrt{(e_\nu - \lambda)^2 + \Delta^2}\)，并在单粒子跃迁矩阵元中乘入配对因子 \(u_\mu u_\nu + v_\mu v_\nu\)。

### Coordinate and symmetry conventions

1. **惯量轴与主轴约定**：惯量排序通常满足 \(\mathcal{J}_m > \mathcal{J}_s > \mathcal{J}_l\)（\(m\) 为中间轴，\(s\) 为短轴，\(l\) 为长轴）；
2. **代数对称性**：在三轴 \(D_2\) 对称性下，强耦合基底系数满足 \(C_{-K,-k}^{(\nu)} = (-1)^{I-j} C_{K,k}^{(\nu)}\)；且哈密顿量在变换 \(\gamma \to 60^\circ - \gamma\) 与 \(\lambda = e_\nu \to e_{7-\nu}\) 下保持严格不变。

## What It Can Establish

### 1. 费米面驱动的横向向纵向摆动演化律（图 10.2 与图 10.3）

通过系统平移费米面 \(\lambda = e_1 \to e_6\)（\(h_{11/2}\) 壳层），计算双带能量差 \(\Delta E(I) = E_{B2}(I) - \frac{1}{2}[E_{B1}(I+1) + E_{B1}(I-1)]\)：

- **DALs 粒子构型（底壳，\(\lambda = e_1\)）**：角动量沿短轴取向，低自旋区 \(\Delta E(I)\) 随自旋下降，表现出典型**横向摆动（TW）**特征；当自旋超过临界值 \(I_{\rm crit}\)（在 \(\gamma=30^\circ\) 下为 \(21/2\hbar\)）后，\(\Delta E(I)\) 拐弯上升，转变为纵向摆动（LW），与 \(^{135}\mathrm{Pr}\) 实验高度一致；
- **DALl 空穴构型（顶壳，\(\lambda = e_6\)）**：角动量沿长轴取向，同样展现低自旋 \(\Delta E(I)\) 下降的 TW 特征，并在高自旋转变；在 \(\gamma=30^\circ\) 下其能谱与粒子构型由于群对称性完全镜像对称；
- **FAL 准粒子构型（中壳，\(\lambda = e_2\) 至 \(e_5\)）**：\(\Delta E(I)\) 从最低自旋开始即随 \(I\) 单调上升，表现为纯粹的**纵向摆动（LW）**模式（如 \(^{187}\mathrm{Au}\) 中基态处于 \(h_{9/2}\) 壳层第二能级）；
- **电磁集体跃迁指纹**：对于 DALs 粒子与 DALl 空穴构型，跨带跃迁比 \(B(E2)_{\rm out}/B(E2)_{\rm in} \ge 0.5\)，证实三轴核电荷分布相对于总角动量矢量的集体摆荡；该比值随自旋按 \(1/\sqrt{I}\)（摆动振幅）逐渐衰减。

### 2. 形变参数 \(\beta\) 与 \(\gamma\) 对摆动稳定性的动力学相图

- **四极形变 \(\beta\) 效应**：增大 \(\beta\) 使奇准粒子与三轴势场耦合加深，增强低自旋区的 TW 特征，并将转变临界自旋 \(I_{\rm crit}\) 往高自旋方向推移；
- **三轴度 \(\gamma\) 效应**：当 \(\gamma\) 从 \(20^\circ, 30^\circ\) 增大至 \(40^\circ\) 时，\(h_{11/2}\) 构型的 TW 彻底消失，全自旋区退化为 LW；
- **失稳判据**：在特定参数区若出现 \(\Delta E(I) < 0\)，标志着摆动集体模式在该自旋处发生失稳（Bifurcation 或转向倾斜进动 TiP）。

### 3. 混合比 \(\delta(E2/M1)\) 符号与准粒子电荷反转定理

跨带 \(\Delta I=1\) 连接跃迁的电磁多极混合比 \(\delta = \frac{\langle E2_{\rm out}\rangle}{\langle M1_{\rm out}\rangle}\)：

- **准中子构型**：由于中子内禀反常磁矩与转子回旋比差值 \(g_n - g_R < 0\)（\(g_n \approx -0.21, g_R \a\a\approx pprox Z/A > 0\)），M1 振幅反向，理论计算给出严格的 **\(\delta > 0\)**；
- **准质子构型**：由于质子 \(g_p - g_R > 0\)（\(g_p > 0\)），理论计算给出 **\(\delta < 0\)**；
- 这一微观符号定理构成了利用束内 \(\gamma\) 谱学角关联（DCO）与偏振测量判定摆动带准粒子性质的判据。

### 4. A≈100 区 \(N=59\) 同中子素横向摆动系统学（图 10.4–10.6）

利用约束三轴 CDFT 计算 \(^{95}\mathrm{Kr}, {}^{97}\mathrm{Sr}, {}^{99}\mathrm{Zr}, {}^{101}\mathrm{Mo}, {}^{103}\mathrm{Ru}, {}^{105}\mathrm{Pd}, {}^{107}\mathrm{Cd}\)：

- 除 \(^{107}\mathrm{Cd}\) 外，其余同中子素能面均包含显著的三轴极小（\(\gamma \sim 20^\circ\)–\(38^\circ\)）；
- 证实 \(^{105}\mathrm{Pd}\)（已测得的首个中子 TW 核）源自 \(\beta=0.27, \gamma=24.9^\circ\) 的状态 C；
- **全新候选预言**：\(^{97}\mathrm{Sr}\)（状态 D, \(\beta=0.28, \gamma=30.4^\circ\)）与 \(^{99}\mathrm{Zr}\)（状态 B, \(\beta=0.31, \gamma=23.3^\circ\)）基于 \(\nu h_{11/2}\) 构型计算出强集体性 \(B(E2)_{\rm out}/B(E2)_{\rm in} \ge 0.5\) 与 \(\delta > 0\)，且 \(\Delta E(I)\) 随自旋下降，被确立为 \(A\approx100\) 区高置信度的全新中子横向摆动候选核；
- \(^{101}\mathrm{Mo}\) 表现出多个不同形变的深极小，预言可能存在三轴形状共存与多重摆动模式。

### 5. 偶偶核两准粒子摆动与相空间波函数节点拓扑（\(^{130}\mathrm{Ba}\) 案例，表 10.1 与图 10.7）

在偶偶核 \(^{130}\mathrm{Ba}\) 中，约束 CDFT（PC-PK1 泛函）给出基态以下及激发的两准粒子构型：

- 激发态 \(a\) 为 \(\pi[g_{7/2}^4 h_{11/2}^2] \otimes \nu[2d_{3/2}^2 h_{11/2}^{-4}]\)，具有三轴形变 \(\beta=0.24, \gamma=21.5^\circ\)，相对基态激发能 \(3.13\text{ MeV}\)（与实验 \(I=10\hbar\) 带头 \(3.79\text{ MeV}\) 吻合）；
- **自旋相干态（SCS）二维角几率分布 \(P(\theta, \phi)\)**：
  - 极角 \(\theta\) 相对于长轴（\(l\) 轴）度量，方位角 \(\phi\) 在 \(s-m\) 主平面内相对于短轴（\(s\) 轴）度量；
  - **基态带 \(S1\)（\(n=0\) 声子）**：几率峰对称集中于 \(\phi=0^\circ\)（短轴取向），代表零声子基态；
  - **一激发带 \(S1'\)（\(n=1\) 声子）**：在 \(\phi=0^\circ\) 出现严格的几率节点（零点），峰值对称分布在两侧，具备奇宇称一维振动的一节点波函数特征；
  - **\(n=2\) 与 \(n=3\) 高阶带**：在 \(\phi\) 空间分别展现 2 个节点与 3 个节点，且 \(12\hbar \le I \le 18\hbar\) 能级差近乎等间距，为偶偶核中存在**两声子与三声子多声子摆动运动**提供了严格的量子力学波函数拓扑铁证；
  - 几率分布在高自旋向 \(\phi=\pm90^\circ\)（中间轴）延展融合，微观揭示了摆动向倾斜轴转动过渡的内在结构。

## Experimental and Spectroscopic Analysis Contract

将 CDFT+PRM 摆动计算用于指导和解释在束 \(\gamma\) 谱学实验时，必须严格遵守以下合同：

1. **形变参数的微观约束**：禁止在 PRM 中随意调整 \((\beta, \gamma)\) 以拟合能级；必须从自洽约束 CDFT 势能面（考虑组态固定）中读取局部极小参数；
2. **区分 TW 与 LW 的实验依据**：
   - 仅当测得能隙 \(\Delta E(I)\) 随自旋下降，且伴随高集体性 \(B(E2)_{\rm out}/B(E2)_{\rm in} \ge 0.5\) 时，方可指认为横向摆动（TW）；
   - 若 \(\Delta E(I)\) 从带头起单调上升，必须首先排查 FAL 中壳准粒子驱动的纵向摆动（LW），而非简单归因于转子拉伸；
3. **剪刀模（Scissors Mode）与 \(B(M1)\) 异常处理**：
   - 纯转子 PRM 预言理想摆动跨带 \(B(M1)\) 趋近于零；
   - 实验若观测到有限或较大的 \(B(M1)_{\rm out}/B(E2)_{\rm in}\)（例如 \(\sim 1\mu_N^2/e^2b^2\)），不能直接否定摆动，应根据质子与中子超流电流反向摆动的剪刀模耦合理查修正；
4. **混合比 \(\delta\) 符号反演准粒子性质**：
   - 实验提取到 \(\delta > 0\) 支持奇中子摆动带（如 \(^{105}\mathrm{Pd}, {}^{97}\mathrm{Sr}, {}^{99}\mathrm{Zr}\)）；
   - 实验提取到 \(\delta < 0\) 支持奇质子摆动带（如 \(^{135}\mathrm{Pr}, {}^{163}\mathrm{Lu}\)）；
5. **偶偶核多声子判据**：对于宣称偶偶核多声子摆动（如 \(^{130}\mathrm{Ba}\)），必须同时提供两声子带的能级等间距、向单声子带的跃迁以及向基态带的 \(\Delta n=2\) 跃迁抑制证据。

## What It Cannot Establish Alone

- 单 \(j\) 壳层 PRM 仅考虑主侵入轨道，在高转速下无法涵盖非纯单壳层混合及芯极化；
- 纯 PRM 计算未显式包含质子–中子剪刀模振动的微观自由度，其计算的 \(B(M1)\) 往往系统偏小；
- 势能面上存在三轴极小并不自动保证该核能形成稳定的摆动带，还取决于零点振动能量（ZPE）与 \(\gamma\) 软度势垒是否容纳准粒子定域；
- SCS 几率分布 \(P(\theta, \phi)\) 属于模型内空间波函数展开，不是实验直接测量谱，必须通过绝对跃迁速率和角分布系数间接映射。

## Knowledge Impact and Learning Decision

陈启博等人的第 10 章代表了当前处理核摆动运动最具自洽性的微观–半微观计算方法（CDFT+PRM）：
它填补了从相对论密度泛函内禀形变到实验室系全量子化角动量谱学之间的理论断层，
系统确立了中壳层 FAL 与底/顶壳层 DAL 准粒子对摆动类型的分类定理，
并开创了偶偶核两准粒子摆动（\(^{130}\mathrm{Ba}\)）与 \(A\approx100\) 质量区中子摆动系统学的理论框架。

本单元完成第 10 章全文、公式推导、表 10.1 及全部图表（图 10.1–10.7）的深入核读。

## Evidence and Locators

- Ch.10 pp.203–205 / physical PDF pp.222–224：Bohr–Mottelson 纯转子摆动、Frauendorf–Dönau TW/LW 分类、全局实验候选分布图 10.1；
- Ch.10 pp.205–206 / physical PDF pp.224–225：PRM 哈密顿量式 (10.1)–(10.2)、单 \(j\) 壳式 (10.3)、BCS 式 (10.4)、强耦合基底式 (10.5)、\(D_2\) 对称化式 (10.6)–(10.7)；
- Ch.10 pp.206–207 / physical PDF pp.225–226：电磁跃迁算符式 (10.8)–(10.13)；
- Ch.10 pp.207–210 / physical PDF pp.226–229：费米面演化定律、能隙公式 (10.14)、图 10.2（\(\lambda=e_1\)–\(e_6\) 能谱与 \(B(E2)/B(M1)\) 比值）、图 10.3（\(\beta,\gamma\) 对拐点与稳定性的影响）；
- Ch.10 pp.210–214 / physical PDF pp.229–233：CDFT+PRM 方案、\(N=59\) 同中子素能面（图 10.4–10.5）、\(^{97}\mathrm{Sr}, {}^{99}\mathrm{Zr}\) 预言（图 10.6）、混合比 \(\delta\) 符号定理式 (10.15)–(10.16)；
- Ch.10 pp.214–216 / physical PDF pp.233–235：\(^{130}\mathrm{Ba}\) 两准粒子摆动、PC-PK1 泛函能面局部极小与形变参数（表 10.1）、自旋相干态 \(P(\theta, \phi)\) 节点图（图 10.7）；
- Ch.10 pp.216–217 / physical PDF pp.235–236：总结与前沿问题；
- 已渲染核对 PDF pp.224、227、229、231、232、233、235、236。

## Sources

- [[book-petrache-chirality-and-wobbling]]
- [[petrache-ch2-frauendorf-topological-wobbling-contract]]
- [[petrache-ch5-experimental-wobbling-evidence-contract]]
- [[lawrie-tip-wobbling-discrimination]]
- [[odd-a-wobbling-mode-stability-and-bifurcation]]
- [[multiphonon-wobbling-and-anharmonicity-dynamics]]
- [[wobbling-model-common-input-and-evidence-boundary]]
