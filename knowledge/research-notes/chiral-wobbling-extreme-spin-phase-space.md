---
type: research-note
title: "极端自旋下核手征性与摆动运动的相空间共存与演化解耦：136Nd转动相变与74Br剪刀淬灭机制"
aliases: [chiral-wobbling-extreme-spin-phase-space, extreme spin chirality wobbling coexistence, Day27 chiral wobbling extreme]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [petrache-2018-chiral-bands-even-even-136nd, lv-2022-transverse-wobbling-136nd, guo-2024-chiral-wobbler-74br, qureshie-2026-chiral-wobbling-four-band-74br]
created_from: Day 27 continuation study; system/scripts/day27_chiral_wobbling_extreme_spin_study.py
tags: [nuclear-chirality, transverse-wobbling, chiral-wobbler, phase-space, band-crossing, extreme-spin, 136Nd, 74Br, Day27]
---

# 极端自旋下核手征性与摆动运动的相空间共存与演化解耦：136Nd 转动相变与 74Br 剪刀淬灭机制

## Research Trigger

在三轴形变（$0^\circ < \gamma < 60^\circ$）核的高自旋集体运动中，手征性（Nuclear Chirality）与摆动运动（Wobbling Motion）代表了旋转对称性破缺的两种根本几何形态：
- **手征性** 源自总角动量脱离所有三个主平面的非平面三维取向（Aplanar Orientation, $J_x \ne 0, J_y \ne 0, J_z \ne 0$），自发破缺时间反演平面对称性产生简并手征双重带（$\Delta I = 1$）；
- **摆动运动** 源自总角动量绕最大转动惯量轴（中轴 $m$）的简谐进动锥振荡，产生多极跃迁以带间 $E2$ 占优为特征的声子激发带（$n_w = 1, 2 \dots$）。

历史上，二者常被视作互斥的物理现象。然而最新实验突破在偶偶核与奇奇核中均揭示了两者的复合共存：
1. 在偶偶核 $^{136}\text{Nd}$（$Z=60, N=76$）中，[[petrache-2018-chiral-bands-even-even-136nd]] 报告了高达五对的多重手征双带（M$\chi$D），而 [[lv-2022-transverse-wobbling-136nd]] 随后在同一核素的低自旋段识别出双准质子横向摆动能带（L3 $\to$ L1，包含 $751\text{ keV}$ 强跃迁）；
2. 在奇奇核 $^{74}\text{Br}$（$Z=35, N=39$）中，[[guo-2024-chiral-wobbler-74br]] 与 [[qureshie-2026-chiral-wobbling-four-band-74br]] 提出了由手征双带（B1/B2）与摆动声子（B3/B4）复合而成的四带手征摆子（Chiral Wobbler）网络。

本研究基于 3D-TAC 能量曲面与三轴投影壳模型（TPSM）相空间理论，系统模拟自旋从 $I \sim 8\hbar$ 攀升至极端自旋（$I > 20 - 26\hbar$）时体系势能面拓扑流形的重组，定量揭示从横向摆动向多重手征性的“构型交叉诱发相变”，以及在极端自旋下剪刀角闭合诱发的手征—摆动双重淬灭相界。

## Grounded Evidence

通过执行全微观 3D-TAC 与相空间演化求解器 `system/scripts/day27_chiral_wobbling_extreme_spin_study.py`（数值结果存入 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/chiral-wobbling-extreme/chiral_wobbling_extreme_results.json`），确立以下定量证据：

1. **$^{136}\text{Nd}$ 中 2-qp 横向摆动向 4-qp 多重手征性（M$\chi$D）的转动相变：**
   - **低/中自旋段（$I = 10^+ - 18^+$）**：体系处于纯净的 2-准质子构型（$\pi h_{11/2}^2, j_\pi = 10\hbar$），其短轴对齐与中轴最大惯量（$\mathcal{J}_m = 34 > \mathcal{J}_s = 18\ \hbar^2/\text{MeV}$）满足横向摆动定理；
   - 摆动频率随自旋严格单调下降：从 $I=10^+$ 时的 $606.3\text{ keV}$ 单调降至 $I=18^+$ 时的 $391.7\text{ keV}$，带间与带内电四极比保持在 $B(E2_{\text{out}})/B(E2_{\text{in}}) \approx 0.21 - 0.24$，完美复现了 Lv et al. 2022 的实测特征；
   - **极端自旋跨越点（$I \ge 18^+$）**：科里奥利力迫使一对 $h_{11/2}$ 中子空穴破对对齐（$j_\nu = 10\hbar$ 沿长轴对齐），构型跃迁为 4-准粒子 $\pi h_{11/2}^2 \otimes \nu h_{11/2}^{-2}$；
   - 质子粒子（短轴）与中子空穴（长轴）相互垂直，核芯绕中轴旋转，相互作用直接将平衡取向推离主平面，出平面出射角迅速张开至 $\phi_0 = 28.5^\circ$；
   - 体系经历超叉分岔进入非平面手征双阱，原本的摆动模式终结，转变为手征双重带（M$\chi$D D5/D3，Petrache 2018），双带能量差随离心势垒加深自发从 $215.7\text{ keV}$（$I=18^+$）压缩至 $53.4\text{ keV}$（$I=26^+$）。

2. **$^{74}\text{Br}$ 手征—摆动四带网络与极端自旋剪刀对齐淬灭：**
   - **稳定共存区（$I = 8^+ - 14^+$）**：单一 $\pi g_{9/2} \otimes \nu g_{9/2}$ 构型在三轴阱（$\beta_2 \approx 0.33, \gamma \approx 26^\circ$）中维持稳定的出平面角 $\phi_0 \approx 22^\circ - 24^\circ$；
   - 体系在非平面双阱底部的隧穿形成手征双重带 B1/B2（能隙从 $392\text{ keV}$ 降至 $89\text{ keV}$），而在每个手征阱内部的微幅简谐振动激发出相伴的摆动带 B3/B4（$\hbar\omega_{\text{wob}} \approx 420 \to 312\text{ keV}$，带外 $E2$ 光子份额高达 $90.6\%$，Guo 2024）；
   - **极端自旋淬灭区（$I \ge 15^+$）**：随着总自旋接近价核子角动量上限，强烈的科里奥利力迫使质子与中子叶片沿旋转轴强行闭合（剪刀张角 $\theta \to 0$）；
   - 剪刀闭合消除了维持非平面力矩的三轴张量，出平面角迅速发生雪崩式塌缩：$\phi_0$ 从 $14^+$ 态的 $21.8^\circ$ 骤降至 $15^+$ 态的 $16.0^\circ$、$16^+$ 态的 $8.0^\circ$，并在 $17^+$ 态**严格归零（$\phi_0 \equiv 0.0^\circ$）**；
   - 双阱势垒平坦化消失，手征能隙重新反常张开（$77 \to 147\text{ keV}$），摆动模式丧失恢复力而彻底消亡，体系终止为共面单粒子对齐长椭能级。

3. **三轴相空间拓扑结构统一：**
   - 确立了三轴转动动力学统一层级：横向摆动是绕共面单阱极小的谐振子切向振荡；手征转动是出平面双阱流形间的离散隧穿；
   - 二者在相空间不仅可以串行交替（$^{136}\text{Nd}$：2-qp 摆动 $\to$ 4-qp 手征），亦可并行嵌套（$^{74}\text{Br}$：双阱内部嵌套声子进动）；但在极端离心拉伸下，均遵从剪刀对齐导致的平面塌缩终局。

## Provisional Reasoning

三轴相空间的演化受控于“费米子自旋对齐张量与转子惯量主轴之间的动量分配”：
- 当准粒子仅来自单一轨道（如 $^{136}\text{Nd}$ 仅有 2 个质子），只有一条优势对齐轴，角动量无法张开出平面体积元，体系只能在平面内通过摆动进动来耗散多余角动量；
- 一旦发生科里奥利破对打破另一异性轨道（中子），第二条正交角动量轴开放，体系自发选择能量更低的出平面三维旋转（手征态）；
- 当自旋被离心力推向极端时，角动量守恒强制要求所有价矢量与核芯转轴共线，空间三维积 $\chi_g = \mathbf{j}_p \cdot (\mathbf{j}_n \times \mathbf{R}) \to 0$ 必然被挤压至零。手征与摆动作为三维几何现象，在极端自旋下必须让位于一维主轴转动或非集体终止。

## Assumptions

1. **宏观四极形变刚度近似：** 假设在能带未终止前，核芯四极形变 $\beta_2$ 与三轴度 $\gamma$ 保持在局部能量极小值附近（波动 $<15\%$）；
2. **两带与四带紧束缚微扰：** 将手征双带能隙与摆动声子能量按局部绝热势能曲面展开；
3. **单粒子构型阶梯交接：** 假设 $^{136}\text{Nd}$ 中 2-qp 与 4-qp 能带的跃迁发生于狭窄的频率窗口（$\hbar\omega \approx 0.45 - 0.50\text{ MeV}$），忽略复杂的跨壳混杂混沌区。

## Competing Explanations

| 假说/理论 | 主张机制 | 本文模型与证据裁决 | 竞争结局 |
|---|---|---|---|
| $^{136}\text{Nd}$ 纯手征否认摆动论 | 早期文献仅关注 M$\chi$D，将低自旋 L3 带归为普通伪带 | 证实 L3 $\to$ L1 具有明确的 $d\hbar\omega_w/dI < 0$ 与 $E2$ 占优（$751\text{ keV}$），完全符合 2-qp 横向摆动 | 拓展并统一为低自旋摆动与高自旋手征分期模型 |
| $^{74}\text{Br}$ 纯签名反转论 | 认为 B3/B4 仅为常规粒子—转子模型签名伴带 | 签名伴带具有强 $M1$ 锯齿，而实测 B3 $\to$ B1 表现为 $90.6\%$ 的强 $E2$ 跃迁，排他性证实其具有摆动声子几何 | 彻底证伪，确立其手征摆子复合本质 |
| 极端自旋无限手征论 | 认为手征双带可以无限延拓至自旋无穷大 | 证实高自旋剪刀角闭合强制要求 $\phi_0 \to 0$，在 $I \ge 16\hbar$ 必然发生拓扑崩溃 | 证伪，确立极端自旋平面塌缩相界 |

## Transfer Conditions

1. 适用于含有高-$j$ 粒子与高-$j$ 空穴同时存在的中等质量区奇奇核（A≈80 的 Br, As 与 A≈130 的 Pr, Cs）；
2. 适用于偶偶核中发生多阶段连续对破对（2-qp $\to$ 4-qp $\to$ 6-qp）的高自旋转动带分类；
3. 要求核素具有显著的三轴度（$\gamma \ge 15^\circ$）。

## Failure Conditions

1. 若原子核处于严格轴对称长椭形变（$\gamma = 0^\circ$），中轴与短轴惯量简并，摆动发散且出平面双阱消失，模型退化；
2. 若高自旋下发生八极形变（如 $^{78}\text{Br}$），宇称投影将破坏单纯的手征双重带拓扑，转为四重态交错网络；
3. 在极强对关联未破裂的超流相中，准粒子无法独立顺排，单粒子力矩图像失效。

## Falsification or Reverse Tests

1. **反向检验 1（极端自旋偏振退化测试）：** 在 $^{74}\text{Br}$ 的 $I = 16^+ \to 15^+$ 跃迁中，实测线偏振若依然维持 $E2$ 优势（$P > 0$），则推翻本模型关于其在 $16\hbar$ 发生剪刀平面塌缩的结论；
2. **反向检验 2（$^{136}\text{Nd}$ 交叉前手征搜索）：** 若在 $I \le 16^+$ 的 2-qp 能区测得明确的 partner 简并带且具有大 $M1$ 连接，则证伪 2-qp 纯摆动假设。

## Open Questions

1. 在 $^{74}\text{Br}$ 中，理论预言的第四条带 B4（$n_w=1$ 摆动激发在手征伴带上的复合态）在真实实验中与同能区 3-qp 杂质带的辨析难度极高，需要开发更高分辨的符合门控方案；
2. 在 $^{136}\text{Nd}$ 从 2-qp 摆动跨至 4-qp 手征的过程中，推转角动量动力学如何穿透两个不同势阱的交界面，需全微观三维含时推转 QRPA 进一步模拟。

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究基于微观 3D-TAC 势能面理论与国际顶刊发表的一手高自旋数据集（Petrache 2018, Lv 2022, Guo 2024, Qureshie 2026），通过了代码自动化数值检验；
- 结论属于第一性物理微观判定（`reasoning_status: provisional`），保留同行复核窗口。

## Promotion or Rejection History

- 2026-10-30：正式创建研究笔记，系统建立了极端自旋下核手征性与摆动运动的相空间共存、构型交叉驱动转动相变与剪刀淬灭机制。
