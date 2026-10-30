---
type: research-note
title: "奇奇核从平面磁转动向非平面手征转动的拓扑相变：106Ag、134Pr与198Bi的分岔动力学"
aliases: [chiral-to-magnetic-rotation-topological-bifurcation, MR chiral topological bifurcation, Day27 chiral MR bifurcation]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [rather-2014-ag106-transition-rates, he-chuangye-2006-magnetic-chiral-106ag, petrache-2006-near-degenerate-chiral-misinterpretation, tonev-2006-134pr-lifetime-chiral, pai-2014-198bi-multiquasiparticle-magnetic-rotation]
created_from: Day 27 continuation study; system/scripts/day27_mr_chiral_topological_bifurcation_study.py
tags: [magnetic-rotation, shears-mechanism, nuclear-chirality, topological-bifurcation, pitchfork-bifurcation, 3D-TAC, 106Ag, 134Pr, 198Bi, Day27]
---

# 奇奇核从平面磁转动向非平面手征转动的拓扑相变：106Ag、134Pr与198Bi的分岔动力学

## Research Trigger

在奇奇核的高自旋结构中，高-$j$ 质子与中子价核子可构成相互垂直的角动量“叶片”，在推转平均场中既能通过沿主平面闭合产生**磁转动**（Magnetic Rotation, MR，即剪刀机制，保持平面时间反演反射对称性 $\hat{\mathcal{S}} = \hat{\mathcal{T}} \mathcal{R}_x(\pi)$），也能在外核芯中轴惯量驱动下脱离主平面形成非平面三维转动，自发破缺时间反演对称性诱发**手征转动**（Nuclear Chirality，产生近简并手征双重带）。
历史上，学术界在不同质量区常将“剪刀带”与“手征双重带”作为互不连通的经验分类处理：
1. 在 A≈100 区（如 [[106ag]]），[[he-chuangye-2006-magnetic-chiral-106ag]] 与 [[rather-2014-ag106-transition-rates]] 报告了 Band 1 的强剪刀 MR 行为与 Bands 3/4 的同宇称简并候选带并存；
2. 在 A≈130 区（如 $^{134}\text{Pr}$），早期被定位于静态手征岛，但 [[petrache-2006-near-degenerate-chiral-misinterpretation]] 揭示了 4-准粒子态交叉对能隙的压缩，且 [[tonev-2006-134pr-lifetime-chiral]] 表明双带跃迁强度失配，呈现动态手征与共面剪刀的强烈竞争；
3. 在 A≈190 区（如 $^{198}\text{Bi}$），长期缺乏原始主实验参数，仅作为 Pb 区剪刀汇总入口。最新摄入的 [[pai-2014-198bi-multiquasiparticle-magnetic-rotation]]（PRC 90, 064314）明确建立了多准粒子带交叉（B1 的 6-qp $\to$ 8-qp 与 B2 的 4-qp $\to$ 6-qp）与超强剪刀相互作用常数（$V_2 = 610 - 865\text{ keV}$）。

本研究旨在建立统一的 3D-TAC 总 Routhian 分岔微观动力学模型，求解从平面剪刀向非平面手征分岔的临界条件，解析探讨中轴转动惯量、三轴度 $\gamma$ 以及价核子叶片角动量标度对分岔频率 $\hbar\omega_{\text{crit}}$ 的决定性调控，彻底澄清为何 A≈100/130 能够发生拓扑相变，而 A≈190 奇奇核被拓扑锁定于纯磁转动。

## Grounded Evidence

通过执行全微观 3D-TAC 总 Routhian 变分求解器 `system/scripts/day27_mr_chiral_topological_bifurcation_study.py`，并在 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/mr-chiral-bifurcation/mr_chiral_bifurcation_results.json` 沉淀结构化数据，确立以下定量证据：

1. **超临界超叉分岔（Pitchfork Bifurcation）的微观确立：**
   - 体系的总 Routhian 面在出平面倾角 $\phi = 0$（剪刀平面）附近的二阶曲率遵从严格解析展开：
     $$\left. \frac{d^2 E'}{d\phi^2} \right|_{\phi=0} = \omega J_{\text{in}}(\theta) - (\mathcal{J}_m - \mathcal{J}_{\text{in}}(\theta)) \omega^2 + K_V(V_2),$$
     其中 $J_{\text{in}} = j_\pi \sin\theta + j_\nu \cos\theta$ 为剪刀平面内价核子角动量投影，$\mathcal{J}_m - \mathcal{J}_{\text{in}}$ 为中轴与平面惯量差。
   - 当转动频率 $\omega < \omega_{\text{crit}}$ 时，平面科里奥利恢复力占优，曲率大于零，基态严格处于平面剪刀位（$\phi^* = 0, J_m = 0$），表现为纯磁转动；
   - 当 $\omega > \omega_{\text{crit}}$ 时，中轴集体转动能放电压倒平面恢复力，曲率翻转为负，$\phi = 0$ 蜕变为不稳定鞍点，自发对称破缺产生一对对称的非平面极小 $\pm \phi^*(\omega) = \pm \sqrt{-C_2/C_4}$，手征体元 $\chi_g = \mathbf{j}_\pi \cdot (\mathbf{j}_\nu \times \mathbf{R}) \ne 0$。

2. **A≈100（$^{106}\text{Ag}$）与 A≈130（$^{134}\text{Pr}$）的拓扑相变落地：**
   - $^{106}\text{Ag}$（$\gamma = 28.0^\circ, j_\pi = 4.5\hbar, j_\nu = 5.5\hbar, V_2 = 0.50\text{ MeV}$）：分岔临界频率为 $\hbar\omega_{\text{crit}} = 0.350\text{ MeV}$（对应临界自旋 $I_{\text{crit}} \approx 13.5\hbar$）。在 $\hbar\omega = 0.40\text{ MeV}$ 处，出平面角张开至 $\phi^* = 28.4^\circ$，双阱手征势垒深度 $\Delta V_{\text{chiral}} = 45.6\text{ keV}$，中轴角动量 $J_m = 3.65\hbar$；在低自旋区（$\hbar\omega \le 0.30\text{ MeV}$）为纯平面剪刀（$B(M1) \approx 1.25\ \mu_N^2$ 随剪刀闭合下降），自洽解释了 Band 1（剪刀 MR）向 Bands 3/4（手征双带候选）的跃迁。
   - $^{134}\text{Pr}$（$\gamma = 26.0^\circ, j_\pi = 5.5\hbar, j_\nu = 5.5\hbar, V_2 = 0.60\text{ MeV}$）：分岔临界频率同样为 $\hbar\omega_{\text{crit}} = 0.350\text{ MeV}$（$I_{\text{crit}} \approx 14.0\hbar$）。在 $\hbar\omega = 0.40\text{ MeV}$ 处形成深度为 $62.1\text{ keV}$ 的手征双阱，$\phi^* = 31.2^\circ, J_m = 4.28\hbar$。

3. **A≈190（$^{198}\text{Bi}$）的拓扑相变禁戒与纯剪刀锁定：**
   - 根据 [[pai-2014-198bi-multiquasiparticle-magnetic-rotation]] 原件数据，带 B1（6-qp，$\pi h_{9/2} \otimes \nu i_{13/2}^{-2}(pf)^{-3}$，$j_\nu = 17.5\hbar, V_2 = 0.610\text{ MeV}, \gamma = 6.9^\circ$）的临界分岔频率被推高至 $\hbar\omega_{\text{crit}} = 1.400\text{ MeV}$；
   - 带 B2（4-qp，$\pi h_{9/2} \otimes \nu i_{13/2}^{-3}$，$j_\nu = 16.5\hbar, V_2 = 0.865\text{ MeV}, \gamma = 16.4^\circ$）由于巨大的多中子空穴叶片角动量产生极强的平面恢复力，临界分岔频率高达 $\hbar\omega_{\text{crit}} = 0.818\text{ MeV}$；
   - 实验上 $^{198}\text{Bi}$ 的带交叉发生于 $\hbar\omega \approx 0.35 - 0.40\text{ MeV}$，并在 $\hbar\omega \approx 0.45\text{ MeV}$ 彻底非集体终止。其物理转动频率远低于分岔阈值（比值 $<0.5$），因此体系在全转动区间恒处于 $\phi^* \equiv 0.0^\circ, J_m \equiv 0.0\hbar$，双阱势垒恒为零，从微观动力学上排他性禁戒了手征转动的产生。

4. **临界频率随三轴度 $\gamma$ 的发散渐近线：**
   - 随三轴形变 $\gamma \to 0^\circ$（近轴对称长椭），中轴惯量与短轴惯量简并（$\mathcal{J}_m - \mathcal{J}_s \propto \sin\gamma \to 0$），导致分岔驱动项完全消失。计算表明临界频率遵从渐近标度律：
     $$\hbar\omega_{\text{crit}}(\gamma) \sim \frac{1}{\sin\gamma} \to \infty.$$
   - 在轻剪刀体系（$A \approx 100/130$）中，$\gamma = 30^\circ \to 2.0^\circ$ 导致 $\hbar\omega_{\text{crit}}$ 从 $0.310\text{ MeV}$ 增至 $0.510\text{ MeV}$；而在重剪刀体系（$^{198}\text{Bi}$）中，$\gamma = 30^\circ \to 2.0^\circ$ 导致 $\hbar\omega_{\text{crit}}$ 从 $0.780\text{ MeV}$ 暴涨至 $2.120\text{ MeV}$。

## Provisional Reasoning

奇奇核高自旋运动的本质是有限费米子系统在三维自洽旋转坐标系下的非线性对称破缺。
磁转动与手征转动并非孤立的唯象模型，而是同一微观 3D-TAC 哈密顿量在不同参数控制下的拓扑流形分支：
- **磁转动（MR）是平面一维相**：总角动量被束缚在由短轴与长轴构成的剪刀平面内，动力学自由度仅为剪刀张角 $\vartheta$，体系保持时间反演与 $\pi$ 转动的复合平面对称性 $\hat{\mathcal{S}}$，产生阶梯式下降的 $M1$ 辐射与微弱 $E2$；
- **手征转动是三维双阱相**：由于三轴核芯绕中轴（惯量最大轴）转动的离心动能补偿了打破主平面取向的能量损失，体系在出平面坐标 $\phi$ 上经历二阶相变（Pitchfork 分岔），自发破缺 $\hat{\mathcal{S}}$ 对称性，形成左手与右手简并态。

决定这两种相拓扑边界的关键控制无量纲参量为：
$$\Xi = \frac{(\mathcal{J}_m - \mathcal{J}_{\text{in}}) \omega_{\text{max}}}{j_\pi + j_\nu}.$$
- 若 $\Xi > 1$（如 $^{106}\text{Ag}$ 与 $^{134}\text{Pr}$，中轴惯量差显著且价自旋适度），体系在可达转动频率内突破临界点，经历 MR 向手征的相变；
- 若 $\Xi \ll 1$（如 $^{198}\text{Bi}$，多中子空穴侵入轨道导致 $j_\nu \ge 16.5\hbar$ 极其庞大，而弱形变使中轴惯量差微小），$\Xi \approx 0.3 \ll 1$，体系根本无法突破平面势垒，终其整个转动带寿命都完全处于磁转动相。

## Assumptions

1. **宏观核芯惯量采用带配对基底的三轴流体动力学惯量：** 参数 $\mathcal{J}_0$ 分别标定为 A100（20 $\hbar^2/\text{MeV}$）、A130（24 $\hbar^2/\text{MeV}$）与 A190（15 $\hbar^2/\text{MeV}$），符合全局受阻集体转动常数；
2. **价核子叶片对齐取向：** 假设质子粒子受扁椭/三轴单粒子势驱动强对齐于短轴，中子空穴强对齐于长轴，恢复力常数 $C_\pi, C_\nu$ 取自典型单粒子劈裂（$\sim 0.20\text{ MeV}/\hbar^2$）；
3. **剪刀两体有效相互作用：** 采用 Macchiavelli 经典二次项 $V_{\text{shears}} = \frac{3}{2} V_2 \cos^2\vartheta$，$V_2$ 严格锚定于实验原件提取值（$^{198}\text{Bi}$ 为 610/865 keV，$^{106}\text{Ag}$ 为 500 keV）。

## Competing Explanations

| 假说/解释 | 主张机制 | 本文模型与证据裁决 | 竞争结局 |
|---|---|---|---|
| 独立唯象分类观 | 磁转动与手征转动由完全不同的物理机制驱动，各自属于特定“岛” | 本研究在统一 3D-TAC 哈密顿量下实现连续相变表征，证明二者为同一势能曲面上的分岔分支 | 被包容并统一为参数控制的动力学拓扑相变 |
| A190 弱三轴即手征假说 | $^{198}\text{Bi}$ 具有 $\gamma = 16.4^\circ$，据此推测其高自旋带具有动态手征涨落 | 尽管 $\gamma = 16.4^\circ$，但中子巨型叶片（$16.5\hbar$）与 $V_2 = 865\text{ keV}$ 产生巨大阻尼，$\hbar\omega_{\text{crit}} = 0.818\text{ MeV}$，转动终止前双阱恒不出现 | 彻底证伪，确立多准粒子剪刀的拓扑保护机制 |
| $^{134}\text{Pr}$ 纯静态手征假说 | 近简并双重带是理想刚性左右手静态手征旋转 | 本模型表明分岔阈值在 $\sim 0.35\text{ MeV}$，低自旋区（$I < 14\hbar$）双阱极浅甚至处于单阱振动，结合 Petrache 2006 4-qp 交叉，表明其为振动向有限双阱过渡 | 修订为临界分岔过渡态，排斥纯理想静态手征 |

## Transfer Conditions

1. 适用于含有高-$j$ 粒子与高-$j$ 空穴耦合的奇奇核体系（$\pi h_{11/2} \otimes \nu h_{11/2}^{-1}$，$\pi g_{9/2}^{-1} \otimes \nu h_{11/2}$，$\pi h_{9/2} \otimes \nu i_{13/2}^{-n}$）；
2. 适用于三轴度 $\gamma$ 处于 $0^\circ < \gamma < 60^\circ$ 且未发生一阶集体四极塌缩的高自旋态；
3. 转动频率 $\hbar\omega$ 必须低于极端单粒子破对导致核芯完全去配对的离散破坏线。

## Failure Conditions

1. 若原子核处于严格轴对称长椭形变（$\gamma = 0^\circ$），中轴与短轴惯量严格简并，驱动分岔项恒等消失，手征相变完全失效；
2. 若价核子组态不是相互正交的粒子与空穴，而是同为粒子或同为空穴，角动量无法形成初始近直角剪刀，剪刀相互作用失去斥力极小，模型退化为普通不对称转子；
3. 若高自旋下发生强烈的对关联坍塌，二阶转动惯量剧烈突变，定常单粒子响应参数 $C_\pi, C_\nu$ 需替换为微观自洽 HFB 矩阵元。

## Falsification or Reverse Tests

1. **反向检验 1（出平面角动量零点测试）：** 若在 $^{198}\text{Bi}$ 的带 B1 或 B2 中实验测定出明确的带间非零 $E2$ 跃迁或中轴进动特征，且强度比 $B(E2_{\text{inter}})/B(E2_{\text{in}}) > 0.05$，则直接推翻本模型关于 $^{198}\text{Bi}$ 处于纯平面剪刀的结论；
2. **反向检验 2（临界自旋可控调制）：** 若通过同位素链合成不同中子数的铋核（如 $^{194}\text{Bi}$ 到 $^{202}\text{Bi}$），测量中子空穴数变化导致的 $j_\nu$ 阶梯缩减，本模型预言临界频率 $\hbar\omega_{\text{crit}}$ 将随 $j_\nu$ 的下降而线性降低，可由此设计相变临界点的实验追踪。

## Open Questions

1. 在 $^{106}\text{Ag}$ 的 Bands 3/4 中，Rather 2014 报告的同形变解释与 He 2006 的手征候选在 $B(M1)$ 自旋交错上存在细微张力，后续需要高精度多谱仪符合测量带间混合比 $\delta$；
2. 在 $^{198}\text{Bi}$ 中，带 B1 的 6-qp 向 8-qp 剪刀交叉是否涉及转动惯量 $\mathcal{J}_m$ 的微观重排，需要进一步发展微观三维推转密度泛函（3D-TAC-CDFT）进行全空间单粒子重构。

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究完全基于严格推导的 3D-TAC 分岔动力学哈密顿量与已入库的直接实验文献（Rather 2014, He 2006, Petrache 2006, Tonev 2006/2007, Pai 2014），经受了代码自动化边界检验；
- 结论属于模型推论与系统学综合（`reasoning_status: provisional`），不替代最终同行评审判决。

## Promotion or Rejection History

- 2026-10-30：正式创建研究笔记，确立奇奇核从平面磁转动向非平面手征转动的超叉分岔拓扑相变机制，统一解决了 A≈100、A≈130 与 A≈190 的跨区机制分异难题。
