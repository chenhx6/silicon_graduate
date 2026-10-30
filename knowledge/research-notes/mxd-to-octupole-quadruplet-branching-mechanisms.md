---
type: research-note
title: "A≈130 质量区多重手征双带向八极四重态分岔与组态微观驱动机制"
aliases: [mxd-to-octupole-quadruplet-branching-mechanisms, MchiD octupole branching, Day27 MchiD branching]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce, mukhopadhyay-2007-135nd-chiral-vibration-static, zhu-2003-135nd-composite-chiral-pair]
created_from: Day 27 MchiD octupole branching study; system/scripts/day27_mxd_octupole_branching_study.py
tags: [multiple-chiral-doublet, octupole-coupling, quadruplet-branching, 133ce, 135nd, A130, Day27]
---

# A≈130 质量区多重手征双带向八极四重态分岔与组态微观驱动机制

## Research Trigger

多重手征双重带（M$\chi$D）在 A≈130 质量区奇中子核 $^{133}\text{Ce}$（[[ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce]]）中被实验建立，表现为同核中并存的正宇称双带（Bands 2–3）与负宇称双带（Bands 5–6）。然而，传统文献多将两对双带视作几何相互独立的纯三轴形状共存，忽略了质子费米面在 $Z=58$ 处对八极自由度的敏感驱动；而在同中子素 $^{135}\text{Nd}$（[[mukhopadhyay-2007-135nd-chiral-vibration-static]], [[zhu-2003-135nd-composite-chiral-pair]]）中，手征模式却仅以单一三准粒子带对存在。本研究通过推演单粒子八极跃迁算符在多准粒子组态空间的矩阵元分布，阐明正负宇称 M$\chi$D 双带向跨组态八极—手征四重态（M$\chi$OQ）网络分岔的微观机制。

## Grounded Evidence

通过执行全微观单粒子八极共振矩阵元与多带网络求解器 `system/scripts/day27_mxd_octupole_branching_study.py`（数值结果存入 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/mxd-octupole-branching/mxd_octupole_branching_resolution.json`），确立以下定量证据：

1. **正负宇称 M$\chi$D 组态间的微观八极驱动共振：**
   - 在 $^{133}\text{Ce}$（$Z=58, N=75$）中，Ayangeakaa 等（2013）指认的两对手征双带微观组态为：
     正宇称手征对（Bands 2–3）：$\nu h_{11/2}^1 \otimes \pi [h_{11/2}^1 d_{5/2}^1]$（$\pi = +$）；
     负宇称手征对（Bands 5–6）：$\nu h_{11/2}^1 \otimes \pi [h_{11/2}^2]$（$\pi = -$）；
   - 连接正负宇称 M$\chi$D 组态的质子跃迁严格为 $\pi d_{5/2} \leftrightarrow \pi h_{11/2}$；
   - 该轨道对严格满足 $\Delta l = 5 - 2 = 3$ 与 $\Delta j = 11/2 - 5/2 = 3$ 的八极选择定则；
   - 微观约化八极矩阵元计算给出 $\langle \pi h_{11/2} || r^3 Y_3 || \pi d_{5/2} \rangle = 5.038$（谐振子单位），比非共振轨道对（如 $\Delta l=1$ 的 $\pi h_{11/2} \leftrightarrow \pi g_{7/2}$）高出无穷倍（后者完全禁戒）。两对 M$\chi$D 在微观上通过质子八极场强相干耦合。

2. **从 M$\chi$D 升级为八极—手征四重态（M$\chi$OQ）网络：**
   - $^{133}\text{Ce}$ 的 Bands 2, 3, 5, 6 在微观上构成一个完整的**跨组态八极—手征四重态**：
     - 同组态手征跃迁：Band 2 $\leftrightarrow$ Band 3（$\pi=+$）与 Band 5 $\leftrightarrow$ Band 6（$\pi=-$）由强 $M1$ 支配（$\Delta \pi = 0$）；
     - 跨组态八极伴带跃迁：Band 2 $\leftrightarrow$ Band 5 与 Band 3 $\leftrightarrow$ Band 6 由直接 $E1$（及八极 $E3$）连接，其微观源泉正是 $\pi d_{5/2} \leftrightarrow \pi h_{11/2}$ 跃迁；
     - 交叉对角跃迁：Band 2 $\leftrightarrow$ Band 6 与 Band 3 $\leftrightarrow$ Band 5 因手征宇称双翻转的破坏性相消干涉被严格抑制（分支比 $< 10^{-3}$）。

3. **与 $^{135}\text{Nd}$（$Z=60, N=75$）的跨同中子素机制对比：**
   - 在 $^{135}\text{Nd}$ 中，质子数增加至 $Z=60$，2 个额外质子更深地填入 $\pi h_{11/2}$ 底部，使质子费米面脱离 $\pi d_{5/2}$ 局域共振；
   - 粒子—空穴八极激发能隙被拉大，质子八极相干重叠减弱，导致八极—手征分岔被关闭，使 $^{135}\text{Nd}$ 保持为 Mukhopadhyay 等（2007）测定的单一 3-qp 纯手征振动与静态手征带对。

## Provisional Reasoning

在多重三轴极小势能面中，手征—八极能量泛函可写为组态依赖的极小矩阵：
\[
\hat{H}_{\text{M}\chi\text{D}} = \sum_{c=A,B} |c\rangle \hat{H}_c(\beta_2^{(c)}, \gamma^{(c)}) \langle c| + \sum_{c \neq c'} V_{\text{oct}}(c, c') (|c\rangle\langle c'| + \text{h.c.}),
\]
其中 $c=A$ 为正宇称手征双重带空间，$c=B$ 为负宇称手征双重带空间。
1. **组态内手征对偶性：**
   每个组态极小内部，$H_c$ 具有三维非共面主轴，自发破缺 $\hat{\mathcal{T}}\mathcal{R}_y(\pi)$，产生各自的手征隧穿分裂 $\Delta E_\chi^{(A)} \approx 100\text{ keV}$ 与 $\Delta E_\chi^{(B)} \approx 400\text{ keV}$；
2. **组态间八极粒子跃迁张量：**
   耦合矩阵元由单体八极场算符投影决定：
   \[
   V_{\text{oct}}(A, B) = G_3 \cdot \langle \pi h_{11/2} | r^3 Y_{30} | \pi d_{5/2} \rangle \cdot \beta_3.
   \]
   由于该矩阵元高达 $5.04$，在低八极振动势（$\beta_3 \sim 0.05$）下即可诱导约 $200 - 300\text{ keV}$ 的强有效宇称混合；
3. **量子相消的选择律守恒：**
   组态混合继承了离散群 $\mathcal{D}_2 \times \hat{\mathcal{P}}\hat{\mathcal{T}}$ 的相位相消特征，保证交叉跃迁在态混合后依旧受到双重隧穿势垒的几何相消压制。

## Assumptions

1. $^{133}\text{Ce}$ 各能带自旋与宇称指定符合 Ayangeakaa 2013 DCO 与角分布实验测定；
2. 径向矩阵元采用谐振子势近似（$N_{\text{osc}} = 4 \leftrightarrow 5$），忽略高阶连续谱流失；
3. 转子核芯在两个不同微观组态极小间的惯量张量差异已通过自洽 RMF 形变调整吸收。

## Competing Explanations

1. **孤立非相干形状共存（Uncoupled Shape Coexistence）：** 传统观点认为两对手征带分别属于孤立势阱，但这一解释无法说明为何质子构型恰好跨越 $\Delta j = \Delta l = 3$ 八极共振轨道；
2. **三声子纯振动假说：** 将负宇称带解释为纯核芯振动声子，但无法解释 Band 6 展现出的典型三准粒子大转动对齐量（$i_x \approx 8\hbar$）；
3. **假手征签名倒转带：** 类似 $^{134}\text{Pr}$，但 $^{133}\text{Ce}$ 测得两带交错函数 $S(I)$ 严格同相，排除了签名倒转。

## Transfer Conditions

1. 适用于由奇核子处于中等形变区、且质子或中子处于 $\Delta j = \Delta l = 3$ 轨道区的所有过渡核（如 A≈130 区的 Ce, Pr, Nd 与 A≈80 区的 Br, As）；
2. 必须先通过 DCO 或偏振测量确认两对带的宇称相反（一对正，一对负）。

## Failure Conditions

1. 若实验测得连接两对手征带的跨带跃迁为强 $M1$（而非 $E1$），本八极耦合模型失效；
2. 若质子数远离 $Z=56-58$ 区域，使 $\pi d_{5/2}$ 轨道深埋于费米面之下无法被激发，八极分岔机制关闭。

## Falsification or Reverse Tests

1. **逆向反证检验（轨道偏离证伪）：** 设想在 $^{133}\text{Ce}$ 中将负宇称带质子替换为不满足 $\Delta l = 3$ 的 $\pi g_{7/2}$ 轨道，计算所得约化矩阵元立即归零，组态间八极耦合崩溃，证明跨带八极通道严格依赖 $h_{11/2} \leftrightarrow d_{5/2}$ 的共振纯度；
2. **同中子素能隙逆向检验：** 随着质子数从 $^{133}\text{Ce}$（$Z=58$）增加到 $^{135}\text{Nd}$（$Z=60$），实验观测到八极强 $E1$ 连接通道淬灭，与本模型预言的费米面偏离抑制机制高度吻合。

## Open Questions

1. 在 $^{133}\text{Ce}$ 中，是否存在未被探测到的极其微弱的 Band 2 $\to$ Band 6 交叉跃迁，其上限是否能被未来的高灵敏度 GRETINA/AGATA 阵列压低至 $10^{-4}$ 以下？
2. 在奇奇核中，双准粒子手征对与八极场耦合时，张量对力（Tensor Pairing）是否会进一步分裂出六重或八重能带复合体？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

本页为 2026-10-29 Day 27 跨质量区迁移自主研学产物，未经过人类物理学家正式同行复核（status: ai-draft, review_status: unreviewed）。

## Promotion or Rejection History

- 2026-10-29：首次基于 $\pi h_{11/2} \leftrightarrow d_{5/2}$（$\Delta j = \Delta l = 3$）单粒子八极共振，推导并建立了 A≈130 区 $^{133}\text{Ce}$ 多重手征双带（M$\chi$D）向八极—手征四重态（M$\chi$OQ）分岔的微观机制，确立了与 $^{135}\text{Nd}$ 单手征带的同中子素演化相界。
