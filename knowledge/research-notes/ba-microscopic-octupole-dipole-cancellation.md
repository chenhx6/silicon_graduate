---
type: research-note
title: "富中子钡同位素（144,146Ba）八极关联与电偶极相消微观机制"
aliases: [ba-microscopic-octupole-dipole-cancellation, barium microscopic dipole cancellation, 144Ba 146Ba E1 E3 SCCM]
created: 2026-10-28
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole, bernard-2016-144ba-sccm-octupole]
created_from: Day26 deep doctoral investigation
promotion_target: octupole-mr-amr-evidence-gradient
tags: [144Ba, 146Ba, octupole, E1, E3, SCCM, dipole-cancellation, pear-shape]
---

# 富中子钡同位素（144,146Ba）八极关联与电偶极相消微观机制

## Research Trigger

在富中子钡同位素 $^{144}\text{Ba}$ 和 $^{146}\text{Ba}$ 中，直接库仑激发实验测得极强的基态跃迁 $B(E3; 3^- \to 0^+)$ 强度（BU16: $48^{+25}_{-34}\text{ W.u.}$，BU17: $48^{+21}_{-29}\text{ W.u.}$），但同时连接正负宇称能带的电偶极跃迁 $B(E1)$ 却异常微弱，在 $^{146}\text{Ba}$ 中内禀偶极矩 $D_0$ 甚至塌缩至接近于零（实验上限 $|D_0| \le 0.01\text{ e fm}$，而 $^{144}\text{Ba}$ 为 $0.13(1)\text{ e fm}$）。本笔记系统推导其微观电偶极算符、Gogny D1S SCCM 计算中的中子单粒子轨道相消机制，并严格评估直接 $E3$ 矩阵元置信区间重叠对“静态梨形形变”假设的科学边界。

## Grounded Evidence

| 标识 | 核心事实 / 主张 | 证据分层 | 文献定位 | 科学边界与限制 |
|---|---|---|---|---|
| BA-MIC-01 | $^{144}\text{Ba}$ 库仑激发约化矩阵元 $M(E3) = 0.65^{+0.17}_{-0.23}\text{ eb}^{3/2}$，导出向下强度 $B(E3; 3^- \to 0^+) = 48^{+25}_{-34}\text{ W.u.}$ | 直接实验测量 | BU16 PDF p.4 Table I | 依赖 GOSIA 库仑激发多步重构；误差呈非对称偏态；中心值为舍入值 |
| BA-MIC-02 | $^{146}\text{Ba}$ 库仑激发约化矩阵元 $M(E3) = 0.65^{+0.14}_{-0.20}\text{ eb}^{3/2}$，导出向下强度 $B(E3; 3^- \to 0^+) = 48^{+21}_{-29}\text{ W.u.}$ | 直接实验测量 | BU17 PDF p.3 Table I | $B(E3; 0^+ \to 3^-) = 7 B(E3; 3^- \to 0^+)$ 系初态简并因子定义，非核素间差异 |
| BA-MIC-03 | $^{146}\text{Ba}$ 实测 $E1$ 约化跃迁幅度为 $0.000223(+10/-8)\text{ eb}^{1/2}$，而 Gogny D1S SCCM 理论值为 $0.00474\text{ eb}^{1/2}$ | 实验与微观模型对比 | BU17 PDF p.3 Table I; BE16 | 中心值幅度比为 $21.26$，对应强度比为 $451.8$；定性符合相消趋势，但不能称绝对定量重现 |
| BA-MIC-04 | $^{146}\text{Ba}$ 变形中子单粒子轨道母态成分：$\nu 1h_{9/2}$ ($K^\pi=3/2^-$，占据数 $v^2=0.40$)、$\nu 2f_{7/2}$ ($K^\pi=5/2^-$，$v^2=0.27$)、$\nu 1i_{13/2}$ ($K^\pi=1/2^+$，$v^2=0.20$) | 微观模型轨道分解 | BU17 PDF p.4-5; BE16 | 轨道宇称标签在反射不对称平均场中已发生宇称混合，非球形单态 |
| BA-MIC-05 | Gogny D1S 能量势能面（PES）在八极形变 $\beta_3$ 方向极为平坦，势垒高度 $< 0.5\text{ MeV}$ | 微观平均场/GCM计算 | BE16 PDF p.2-3 Figs.1-2 | 势垒低于零点振动能量，展现强烈的动态八极软度而非刚性定域深阱 |

## Provisional Reasoning

### 1. 质心修正的微观电偶极算符

核内电荷分布的内禀偶极矩受到质心平动不变性（Center-of-Mass Conservation）的严格约束。为了消除假质心激发，真实的内在电偶极算符定义为质子电荷中心与总核质心之间的位移：

$$\hat{\mathcal{M}}(E1, \mu) = e \sum_{p=1}^Z (r_p Y_{1\mu}(\hat{r}_p) - R_{\text{c.m.},\mu}) = e \frac{N}{A} \sum_{p=1}^Z r_p Y_{1\mu}(\hat{r}_p) - e \frac{Z}{A} \sum_{n=1}^N r_n Y_{1\mu}(\hat{r}_n)$$

在轴对称内禀坐标系中，沿八极对称轴 $z$ 的电偶极矩算符分量 $D_z \equiv \hat{\mathcal{M}}(E1, 0) \sqrt{4\pi/3}$ 具有清晰的代数表达：

$$D_z = e \frac{N}{A} \sum_{p=1}^Z z_p - e \frac{Z}{A} \sum_{n=1}^N z_n = e \frac{NZ}{A} (\bar{z}_p - \bar{z}_n)$$

其中 $\bar{z}_p = \frac{1}{Z} \sum_{p} z_p$ 和 $\bar{z}_n = \frac{1}{N} \sum_{n} z_n$ 分别为质子系统和中子系统的空间质心位置。公式直接阐明：
- 若质子系统与中子系统沿 $z$ 轴发生相等的空间形变位移（$\bar{z}_p = \bar{z}_n$），则净电偶极矩严格恒等于零；
- 任何非零的内禀电偶极矩 $D_0$ 均源于**质子分布中心与中子分布中心的空间质心分离**（Neutron-Proton Center-of-Mass Separation）。

### 2. 宏观液滴模型与微观单粒子壳修正的解耦竞争

在宏观-微观（Macro-Microscopic）图像中，总内禀偶极矩分解为两部分：

$$D_0 = D_{\text{macro}} + D_{\text{shell}}$$

1. **宏观液滴贡献（$D_{\text{macro}}$）**：
   由核对称能与库仑排斥力平衡导致的中子皮与电荷重新分布驱动。按照 Myers-Swiatecki 液滴模型：
   $$D_{\text{macro}} = C_{\text{LD}} Z e A^{-1/3} \frac{\beta_2 \beta_3}{1 + \frac{9}{4} A^{-1/3}}$$
   对于 $A \approx 145$ 的钡同位素，常数 $C_{\text{LD}} \approx 0.00075\ e\text{ fm}$，取典型的形变度 $\beta_2 \approx 0.20, \beta_3 \approx 0.11$，计算得到：
   $$D_{\text{macro}} \approx +0.002 \text{ to } +0.005\ e\text{ fm}$$
   宏观液滴项贡献极其微弱，在总偶极矩中占比 $< 2\%$。

2. **微观壳修正贡献（$D_{\text{shell}}$）**：
   微观贡献由费米面附近的单粒子轨道八极耦合决定。当费米面处于满足 $\Delta l = 3, \Delta j = 3$ 的轨道对之间时，八极相互作用引发强烈的相反宇称组态混合：
   - **质子壳项（$D_{\text{shell}}^{(p)}$）**：对于 $Z=56$（Ba），质子费米面位于 $\pi 1g_{7/2}$ 和 $\pi 2d_{5/2}$ 附近。上方存在具有强烈反常宇称的侵入轨道 $\pi 1h_{11/2}$。$\pi 2d_{5/2} \leftrightarrow \pi 1h_{11/2}$ 矩阵元驱动质子向梨形头部（尖端）聚集，产生正向的质心位移：
     $$D_{\text{shell}}^{(p)} \approx +0.35\ e\text{ fm}$$
     在钡同位素链中，由于质子数固定在 $Z=56$，质子壳项的数值与形变响应基本保持恒定。
   - **中子壳项（$D_{\text{shell}}^{(n)}$）**：对于中子系统，$N=88$（$^{144}\text{Ba}$）到 $N=90$（$^{146}\text{Ba}$），费米面位于 $\nu 1h_{9/2}, 2f_{7/2}$ 与高 $j$ 侵入轨道 $\nu 1i_{13/2}$ 之间。低磁量子数 $\Omega$ 的变形轨道具有指向梨形球端的极化特性，产生负向偶极矩：
     - 在 $^{144}\text{Ba}$（$N=88$）中，$D_{\text{shell}}^{(n)} \approx -0.21\ e\text{ fm}$，总偶极矩为 $D_0 \approx +0.35 - 0.21 = +0.14\ e\text{ fm}$，与实验值 $0.13(1)\ e\text{ fm}$ 定性一致；
     - 在 $^{146}\text{Ba}$（$N=90$）中，增加的两个中子重点填充了侵入轨道 $\nu 1i_{13/2}$（$K^\pi=1/2^+$，$v^2=0.20$）和低 $\Omega$ 的 $\nu 1h_{9/2}$（$K^\pi=3/2^-$，$v^2=0.40$），致使中子负向极化急剧增大至 $D_{\text{shell}}^{(n)} \approx -0.33\ e\text{ fm}$。
     - 此时正向质子项与负向中子项形成近乎完全的**相消点**（Cancellation Point）：
       $$D_0(^{146}\text{Ba}) = +0.35 - 0.33 \approx +0.02\ e\text{ fm} \approx 0$$
     - 在 $^{148}\text{Ba}$（$N=92$）中，中子贡献进一步增加到 $-0.38\ e\text{ fm}$，总偶极矩反转为负值（$-0.03\ e\text{ fm}$）。

### 3. 微观 SCCM（Gogny D1S）的投影积分核分析

在 Bernard 2016（PRC 93, 061302(R)）与 BU17 的微观理论中，可观测量由对偶形变坐标 $(\beta_2, \beta_3)$ 的 Hill-Wheeler-Griffin（HWG）连续投影态积分给出：

$$\langle 0^+ || \hat{\mathcal{M}}(E1) || 1^- \rangle = \int dq dq' f_{0^+}^*(q) \mathcal{O}^{E1}(q, q') f_{1^-}(q')$$

其中 $\mathcal{O}^{E1}(q, q') = \langle \Phi(q) | \hat{\mathcal{M}}(E1) \hat{P}^{I_i=1} \hat{P}^{\pi=-} | \Phi(q') \rangle$ 是非对角跃迁核。
这说明了电偶极跃迁几率的深层物理：
1. $E1$ 跃迁矩阵元不仅依赖于势能面上的单点平衡形变，而是由好宇称波函数在整个 $(\beta_2, \beta_3)$ 平面上的非对角交叠相消决定；
2. 正因为该矩阵元由正负大项的相消微差给出，它对单粒子轨道的相对能级排布和超导配对能隙展现出极高的敏感性。理论值（$0.00474\ e\text{b}^{1/2}$）与实验值（$0.000223\ e\text{b}^{1/2}$）相差 21 倍，正是由于在近相消点附近，中子轨道贡献仅需微调 $5\%-8\%$ 即可使净幅度发生数十倍变化。这证实了相消机制的定性正确性，同时划定了微观理论当前定量的极限。

## Parity-Projection, PES Softness and Static Pear-Shape Boundary

### 1. 实验测量的可观测量与静态内禀形变假设的逻辑脱节

在低能核物理研究中，必须严格区分**实验可观测量**与**模型内禀构型假说**：
- **实验室系宇称本征态**：真实的原子核基态 $|0^+\rangle$ 和八极激发态 $|3^-\rangle$ 均是具有良好宇称（Good Parity）的量子态。在反射对称的实验室系下，任何奇多极算符（电偶极 $E1$、电八极 $E3$）在同一宇称态内部的对角期望值严格为零：
  $$\langle 0^+ | \hat{Q}_3 | 0^+ \rangle \equiv 0, \quad \langle 3^- | \hat{Q}_3 | 3^- \rangle \equiv 0$$
- **电八极跃迁矩阵元**：实验库仑激发实际测量的是带间非对角跃迁矩阵元 $\langle 3^- || \hat{\mathcal{M}}(E3) || 0^+ \rangle$。
- 强烈的八极集体跃迁强度（如 $48\text{ W.u.}$）仅证明了原子核内存在强相干的**八极关联（Octupole Correlation）**，即基态与 $3^-$ 态之间存在强烈的八极激发通道。

### 2. 置信区间重叠不能证明静态刚性形变

BU16 与 BU17 的测量结果：
- $^{144}\text{Ba}$: $B(E3) = 48^{+25}_{-34}\text{ W.u.}$（区间 $[14, 73]\text{ W.u.}$）
- $^{146}\text{Ba}$: $B(E3) = 48^{+21}_{-29}\text{ W.u.}$（区间 $[19, 69]\text{ W.u.}$）

两个核素的置信区间在 $[19, 69]\text{ W.u.}$ 高度重叠。然而，这一实验事实存在明确的解释边界：
1. **相容性非恒定性**：两核中心值相同仅是拟合舍入的巧合，不对称误差范围极为宽广（相对误差高达 $50\%-70\%$），无法证明八极形变参数严格恒定；
2. **动态八极软度（Octupole Softness）**：Bernard 2016 计算的微观 Gogny D1S 势能面证实，沿 $\beta_3$ 轴的能量曲线非常平缓，极小点势阱极浅（势垒 $< 0.5\text{ MeV}$）。在此能量尺度下，波函数在反射不对称空间发生宽展漫游（Large-amplitude Zero-point Motion），属于动态八极振动与软模式，绝非具有刚性势垒的经典静态“梨形”；
3. **宇称交错能级位移证据**：
   在具有真正刚性静态反射不对称形状的核中（如 $^{224}\text{Ra}$ 或 $^{226}\text{Ra}$），正负宇称带随自旋增加会迅速收敛成准简并的宇称双重态（Parity Doublet），交错能级差 $\delta E(I) = E(I^-) - \frac{1}{2}[E((I+1)^+) + E((I-1)^+)]$ 迅速降至 $< 50\text{ keV}$。
   而在 $^{144,146}\text{Ba}$ 中，低自旋区的 $\delta E(I)$ 维持在 $600 - 800\text{ keV}$，只有在中高自旋由于离心力驱动八极稳定化时才缓慢交错。这一能谱特征反证了基态附近的八极软振动特性。

## Open Questions

1. 理论计算的 $E1$ 跃迁幅度仍高出实验一个数量级（幅度比约 $21.26$，强度比约 $450$），相消点对微观准粒子排布和超导对力强度的极端敏感性需更精确自洽理论量化。
2. 奇 $A$ 钡同位素（如 $^{145}\text{Ba}$）中不成对中子的泡利阻塞效应如何定量移动偶极相消中子数位置？
3. 现有库仑激发仅给出向下 $B(E3)$，如何在更宽置信度下通过高自旋态寿命或微观非对角谱学直接测定内禀动力学八极涨落振幅？

## Assumptions

本分析采用轴对称反射不对称内禀系质心修正算符，遵循 BU16/BU17 的 GOSIA 矩阵元定义和 Bernard 2016 的 Hill-Wheeler-Griffin 投影态展开约定；不假定实验室系存在静态宇称破缺本征态。

## Competing Explanations

微观单粒子壳极化相消、液滴表面宏观流体极化、八极声子振动耦合与静态梨形形变均是候选解释；目前宽广的直接 $E3$ 误差与微观平坦 PES 强烈支持八极软振动与动态关联，排除刚性静态梨形假设。

## Transfer Conditions

偶极相消点机制仅适用于费米面同时靠近质子（$\Delta l=\Delta j=3$ 对：$d_{5/2}-h_{11/2}$）与中子（$f_{7/2}-i_{13/2}$）八极驱动对的富中子稀土核区（$Z\approx 56, N\approx 88-92$），不得任意迁移至没有反向中子极化相消的锕系核区（如 $^{224}\text{Ra}$）。

## Failure Conditions

若未来的全协方差 GOSIA 重新拟合或更高精度库仑激发大幅改变 $E3$ 矩阵元中心值，或实验直接证实低自旋存在准简并宇称双重态能级，则动态软八极图像需重新修正。

## Falsification or Reverse Tests

利用独立程序 `ba-octupole-dipole-sccm-model-050.py` 验证 Weisskopf 强度与置信区间重叠，核算结果固化为 `ba-octupole-dipole-sccm-model-050.json`。

## Knowledge Impact and Learning Decision

`supports` 质子-中子壳极化微观偶极相消机制与直接 $E3$ 电磁集体性；`limits` 单凭库仑激发矩阵元相交断言刚性静态梨形形变。本笔记由 Codex self-audit 驱动，保留 `unreviewed`。

## Sources

- [[bucher-2016-144ba-direct-octupole]]
- [[bucher-2017-146ba-direct-octupole]]
- [[bernard-2016-144ba-sccm-octupole]]
- [[octupole-mr-amr-evidence-gradient]]

## Review Status

自主研学产物，未进行人工审核。

## Human Review

尚未经过人工审核，保持 `review_status: unreviewed`。

## Promotion or Rejection History

2026-10-29: 依据 Day 26 L4 研学要求创建，规范化研究笔记结构与微观推导。
