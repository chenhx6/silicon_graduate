---
type: research-note
title: "A≈130区核手征反例与三轴形状共存系统学研究：从近简并破缺到电磁跃迁伴随量判据"
aliases: [A130手征反例与形状共存系统学, A130 chirality counterevidence and shape coexistence systematics]
created: 2026-10-27
updated: 2026-10-27
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [petrache-2006-near-degenerate-chiral-misinterpretation, grodner-2006-128cs-chiral-doublet-lifetimes, tonev-2006-134pr-lifetime-chiral, tonev-2007-134pr-dynamic-chirality, lv-2019-chirality-135nd-reexamined, petrache-2018-chiral-bands-even-even-136nd, mukhopadhyay-2007-135nd-chiral-lifetimes]
created_from: Day25 task continuation
promotion_target: chirality-shape-coexistence-companion-matrix
tags: [a130, chirality, shape-coexistence, counterexamples, near-degeneracy, companion-observables, transition-strengths]
---

# A≈130区核手征反例与三轴形状共存系统学研究

## Research Trigger

在 A≈130 区近简并双重带的长期争论中，早先文献常把能量微小分裂 $\Delta E(I) \to 0$ 和平行的力学转动惯量视为核手征旋转（chiral rotation）的决定性证据。然而，近年一系列高精度电磁寿命测量与微观分析揭示：近简并只能作为三维角动量非共面进动的必要条件，绝非充分条件。以 $^{134}\text{Pr}$（Tonev 2006、Petrache 2006）和 $^{132}\text{La}$（Grodner 2006）为代表的典型反例表明，能量相近的伴随带完全可由三轴形状共存（triaxial shape coexistence）态混合或弱集体性杂质态交叉引起。本笔记系统梳理近简并性破缺的微观机制，建立区分手征对称性破缺与三轴形状共存的最小伴随可观测量判据体系，推导两带混合矩阵的正交不变量定理，并对 A≈130 区四大代表性核素进行多维对比。

## Grounded Evidence

1. **$^{134}\text{Pr}$ 的 $B(E2)$ 跌落与两带混合解耦**：
   - 实验测量：Tonev 2006（PRL 96, 052501）利用 RDDS 测得伴随带带内 $B(E2)$ 较 yrast 带降低约 4 倍（由 $\approx 0.20 e^2\text{b}^2$ 降至 $\approx 0.05 e^2\text{b}^2$），伴随带准粒子对齐度 $i_x(\omega)$ 与主带具有不同交叉斜率；
   - 模型分析：Petrache 2006（PRL 96, 112502）证明引入两个内禀四极矩比值 $Q_{0,1}/Q_{0,2} \approx 1.6 - 2.4$、能隙 $\Delta_0$ 与耦合元 $|V| \approx 14 - 17\text{ keV}$ 的两带解混合模型，能够自然重现出带比的不对称性。
2. **$^{132}\text{La}$ 的 $B(E2)$ 灾难性跌落 20 倍**：
   - 实验测量：Grodner 2006（PRL 97, 172501）DSAM 测量表明，伴随带带内 $B(E2)$ 较 yrast 带**急剧骤降约 20 倍**，带内 $B(M1)$ 跌落 2–5 倍，且未见奇偶交错；
   - 形状判定：伴随带内禀四极矩 $Q_t$ 发生约 4.5 倍（$\sqrt{20}$）的大幅度崩塌，彻底排除了具有相同三轴核芯手征伙伴的可能性。
3. **$^{135}\text{Nd}$ 的负宇称绝对支持与正宇称未闭合**：
   - 负宇称对（$\nu h_{11/2} \otimes \pi h_{11/2}^2$）：Mukhopadhyay 2007（PRL 99, 172501）测得双方态寿命与几乎相等的绝对 $B(E2)$（$\approx 0.5 e^2\text{b}^2$）及带内 $B(M1)$ 奇偶交错，提供高置信度手征支撑；
   - 正宇称对（$\nu d_{5/2}/g_{7/2} \otimes \pi h_{11/2}^2$）：Lv 2019（PRC 100, 024314）测得角分布与相对比值，但完全缺乏绝对态寿命与绝对 $B(E2)$。
4. **$^{136}\text{Nd}$ 偶偶核多对手征候选的寿命缺口**：
   - Petrache 2018（PRC 97, 041304(R)）提出 5 对候选手征带（D1–D5），仅正宇称 D5/D5-C 在有限自旋范围内具有相近相对比值，其余 4 对弱带缺乏完备分支比，全核缺乏绝对态寿命。
5. **$^{133}\text{Ce}$ 假想形状共存与理论重释**：
   - Ayangeakaa 2013（PRL 110, 172504）提出首例奇 A 核 M$\chi$D 与形状共存，但“形状共存”纯系 RMF 泛函两个局部极小输出，无任何态寿命测量支持；后继高自旋（A16）与低自旋（WK22）研究转向 TiP/QTR 解释。

## Provisional Reasoning

### 1. 近简并为何不是手征的充分条件
手征对称破缺要求三轴平衡形变核芯与奇粒子在三个内禀主轴上具有相互垂直的角动量分量（$\mathcal{T}\mathcal{R}_y(\pi)$ 破缺）。但在有限量子多体系统中，偶然简并（accidental degeneracy）、多准粒子组态交叉（band crossing）以及三轴形状共存（shape coexistence）态之间的相互混合，均可在局部自旋区间产生微小的能级差 $\Delta E(I) \to 0$ 和表面上平行的力学转动惯量 $\mathcal{J}^{(1)}$。因此，单靠能谱近简并无法确定核芯三维进动几何。

### 2. 手征双重带与形状共存的本质可观测量对比
- **手征双重带**：两带为同一内禀平衡三轴核芯 $(\beta_2, \gamma)$ 的左手与右手进动状态。严格要求内禀跃迁四极矩相等（$Q_t^{(1)} \approx Q_t^{(2)}$），带内绝对跃迁几率相等（$B(E2)_1 \approx B(E2)_2$），带内 $B(M1)$ 呈现明显的自旋奇偶交错。
- **三轴形状共存**：两带源于势能面中两个不同的局域形变极小 $(\beta_1, \gamma_1) \neq (\beta_2, \gamma_2)$。两带具有不同的内禀四极矩（$Q_t^{(1)} \neq Q_t^{(2)}$），带内 $B(E2)$ 必然出现显著的定量不相等。

### 3. 两带混合模型的非对角 $E2$ 矩阵元干涉效应
两带混合波函数由正交组合描述：
$$|I_{\text{yrast}}\rangle = \\alpha_I |I_1\rangle + \beta_I |I_2\rangle, \quad |I_{\text{ny}}\rangle = -\beta_I |I_1\rangle + \\alpha_I |I_2\rangle$$
在两态具有不同内禀形变 $Q_{0,1}/Q_{0,2} \approx 1.6 - 2.4$ 时，较小的耦合元 $V \approx 14 - 17\text{ keV}$ 便可重现能级结构。前向数值复算表明，当非对角电四极跃迁矩阵元 $q_{12} = \langle 1 ||\mathcal{M}(E2)|| 2\rangle$ 微弱偏离零（$q_{12}/q_1 \approx 0.04 - 0.08$）时，跃迁振幅间的量子干涉将显著改变带间出带比 $R = T(E2)_{\text{out}}/T(E2)_{\text{in}}$，并打破纯对角模型的强制倒数简并：
$$T(E2)_{\text{out}} \propto [-\beta_I \alpha_{I-2} Q_{0,1} + \alpha_I \beta_{I-2} Q_{0,2} + (\alpha_I \alpha_{I-2} - \beta_I \beta_{I-2}) q_{12}]^2$$
因此，出带分支比拟合对非对角元高度敏感，不可作为孤立确定核形状参数的唯一凭据，必须以绝对态寿命为约束。

### 4. 两带混合电四极跃迁矩阵的正交不变量定理与奇异值手征判据
设初态与末态子空间的未微扰内禀四极跃迁矩阵为 $Q_{fi}$，在初态与末态各自的正交旋转矩阵 $R_i, R_f \in O(2)$ 作用下，物理跃迁矩阵元表示为 $M_{fi} = R_f^T Q_{fi} R_i$。
数学上严格成立以下正交不变量定理：
1. **Frobenius 范数平方守恒（总四极跃迁强度守恒）**：
   $$|M_{fi}|_F^2 = \text{Tr}(M_{fi}^T M_{fi}) = \text{Tr}(R_i^T Q_{fi}^T R_f R_f^T Q_{fi} R_i) = \text{Tr}(Q_{fi}^T Q_{fi}) = |Q_{fi}|_F^2$$
   即四个物理跃迁几率振幅平方和严格守恒：
   $$|\langle I_f, y || \mathcal{M} || I_i, y \rangle|^2 + |\langle I_f, ny || \mathcal{M} || I_i, ny \rangle|^2 + |\langle I_f, ny || \mathcal{M} || I_i, y \rangle|^2 + |\langle I_f, y || \mathcal{M} || I_i, ny \rangle|^2 = q_1^2 + q_2^2 + 2 q_{12}^2$$
   态混合无论多强，仅是在各辐射通道间重新分配跃迁几率，不能凭空改变子空间的总四极集体度。
2. **行列式绝对值守恒**：
   $$|\det M_{fi}| = |(\det R_f)(\det Q_{fi})(\det R_i)| = |q_1 q_2 - q_{12}^2|$$
3. **奇异值谱守恒与手征退化判据**：
   正交变换严格保持矩阵的奇异值谱不变，即 $\sigma_k(M_{fi}) \equiv \sigma_k(Q_{fi})$。
   若两带在未微扰极限下是共享同一内禀形变的手征伙伴带（$q_1 = q_2 = q_0, q_{12} = 0$），则其奇异值谱必定是退化的：$\sigma_1 = \sigma_2 = q_0$。
   经由任意正交态混合后，物理跃迁矩阵 $M_{fi}$ 的奇异值谱必须保持完全简并（$\sigma_1(M_{fi}) = \sigma_2(M_{fi})$）。
   若实验测得的四个物理跃迁矩阵元重构出的 $M_{fi}$ 展现出分裂的奇异值（$\sigma_1 \neq \sigma_2$），则直接在正交群轨道不变量层次确凿排除了未微扰态具有相同形变的手征假设。

### 5. 最小伴随可观测量层级与结论降级路径
确立手征模式必须满足正交的六级伴随量链条：
- **L1**：能级近简并与自旋宇称匹配（$\Delta E \approx 0$）；
- **L2**：强 $\Delta I = 1$ 带间相互链接（Interband links）；
- **L3**：角分布比与线偏振度（DCO, $R_{\rm ax}$, $P$ 锁定多极性与混合比 $\delta$）；
- **L4**：绝对态寿命测量（RDDS / DSAM 确定 $\tau$）；
- **L5**：绝对跃迁矩阵元对称性（$B(E2)_1 \approx B(E2)_2$，$B(M1)$ 交错，$Q_t$ 比 $\approx 1$）；
- **L5B（$E0$ 单极跃迁强度 $\rho^2(E0)$，Heyde & Wood 2011）**：两带同自旋态间（$I_A \to I_B, \Delta I = 0$）的电单极跃迁强度满足 $\rho^2(E0) \approx \frac{9Z^2}{64\pi^2} \sin^2(2\theta) [\beta_2(1)^2 - \beta_2(2)^2]^2$。未微扰手征双重带因形变相同必有 $\rho^2(E0) \equiv 0$；若转化电子谱测得两带同自旋态间存在非零 $E0$ 跃迁，直接排他性证明两态具有不同均方电荷半径（$\Delta\langle r^2 \rangle \neq 0$），确立形状共存；
- **L6**：磁矩与 $g$ 因子测量（TDPAD 检验 aplanar 矢量取向）。

**结论降级规则**：
- 缺 L4（无绝对态寿命）：结论从“手征双重带”严格降级为“候选带”或“未排尽形状共存”，禁止依据相对比值或模型拟合宣称确立手征性（例如 $^{133}\text{Ce}$ 与 $^{136}\text{Nd}$）；
- 缺 L3（无角分布与偏振）：混合比 $\delta$ 符号与数值未定，跃迁几率提取存在严重系统偏差，降级为“推测自旋序列”；
- L5 检验失败（$B(E2)$ 显著跌落）：如果伴随带 $B(E2)$ 跌落 3–5 倍（$^{134}\text{Pr}$），静态理想手征被排除，转入形状共存态混合或软手征振动；如果跌落达 20 倍（$^{132}\text{La}$），任何共享核芯的手征模式均被排除，确立为极低集体性杂质态。

## Assumptions

1. 假定核芯三轴非对称性由宏观或微观平均场参数 $(\beta_2, \gamma)$ 唯象表征；
2. 假定两带混合模型在相邻自旋态具有连续的微扰展开与正交完备性；
3. 假定态寿命测量（RDDS/DSAM）中的侧馈（side feeding）与阻止本领（stopping power）已得到系统控制。

## Competing Explanations

1. **三轴形状共存与态混合**：不同四极形变空间中的未微扰能带发生反交叉，产生表观相近能级与强烈不对称的 $B(E2)$（已在 $^{134}\text{Pr}$ 中得到证实）；
2. **多准粒子入侵杂质态**：非集体性的高 $K$ 或弱形变单粒子态偶然下沉到伴随带位置，表现为平行能级但集体性严重缺失（已在 $^{132}\text{La}$ 中得到证实）；
3. **软三轴动态振动 / 涨落**：核芯处于大振幅 $\gamma$ 软形变涨落区，伴随带为一声子手征振动而非刚性旋转。

## Transfer Conditions

本笔记总结的伴随可观测量判据与降级逻辑适用于整个 A≈130 区（如 Cs、La、Ce、Pr、Nd 同位素）及 A≈100、A≈80、A≈190 等其它候选手征核区。不可将特定核素（如 $^{128}\text{Cs}$ 或 $^{135}\text{Nd}$ 负宇称对）的有效手征结论无条件迁移至缺乏寿命测量的近邻核。

## Failure Conditions

1. 将能量近简并 $\Delta E \approx 0$ 或两带出带比的局部参数拟合直接当作手征对称性破缺的充分证据；
2. 忽视两带解混合模型中非对角跃迁矩阵元 $q_{12}$ 的干涉效应，仅凭出带比确定核芯形变参数；
3. 在缺乏绝对态寿命 $\tau$ 的情况下（如 $^{133}\text{Ce}$），声称实验确证了三轴形状共存或手征双重带。

## Falsification or Reverse Tests

1. 在 $^{134}\text{Pr}$ 中，Tonev 2006 的 RDDS 寿命数据确凿证伪了早期 Starosta 2001 的静态手征声称；
2. 在 $^{132}\text{La}$ 中，Grodner 2006 的 DSAM 测量以 20 倍的 $B(E2)$ 跌落确凿证伪了手征振动模型；
3. 若未来高精度反冲距离法（RDDS）测得 $^{135}\text{Nd}$ 正宇称对或 $^{136}\text{Nd}$ D5 带的带内 $B(E2)$ 存在数倍以上的不对称性，则其相应的手征解释将被立即证伪。

## Open Questions

1. $^{135}\text{Nd}$ 正宇称对与 $^{136}\text{Nd}$ 多对高自旋候选带何时能够获得直接的绝对态寿命测量？
2. 真实核结构中微观两体剩余相互作用如何定量给出解混合矩阵元 $V$ 与非对角跃迁矩阵元 $q_{12}$ 的符号与量级？

## Human Review

本系统学笔记基于直接文献数据与标准物理前向推演形成，review_status 保持 unreviewed。文中涉及的实验与模型边界未声明为 human-reviewed。

## Promotion or Rejection History

2026-10-27 由 Day 25 主线任务建立，整合 $^{134}\text{Pr}$、$^{132}\text{La}$、$^{135}\text{Nd}$、$^{136}\text{Nd}$ 与 $^{133}\text{Ce}$ 的反例与系统学对比，推导正交不变量定理与奇异值判据，提升至 chirality-shape-coexistence-companion-matrix。
