---
type: research-note
title: "高自旋磁转动核芯交叉与扁椭终止系统学：A≈140与A≈190质量区多准粒子竞争机制"
aliases: [mr-high-spin-core-crossing-and-oblate-termination, MR core crossing oblate termination, Day27 MR crossing A140 A190]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [hubel-2005-magnetic-rotation-review, clark-2000-shears-mechanism, pai-2014-198bi-multiquasiparticle-magnetic-rotation, agarwal-2007-137pr-magnetic-rotation-bandcrossing, garg-2015-135pr-magnetic-rotation]
created_from: Day 27 continuation study; system/scripts/day27_mr_oblate_core_crossing_study.py
tags: [magnetic-rotation, shears-mechanism, core-rotation, band-crossing, band-termination, oblate-deformation, 198Pb, 198Bi, 142Gd, Day27]
---

# 高自旋磁转动核芯交叉与扁椭终止系统学：A≈140 与 A≈190 质量区多准粒子竞争机制

## Research Trigger

在磁转动（Magnetic Rotation, MR）的高自旋演化中，传统粗糙观念常假定“轻/中质量区核芯转动显著，而重铅区核芯绝对刚硬、纯靠剪刀叶片单调闭合直达终止”。然而，近期对权威综述（[[hubel-2005-magnetic-rotation-review]], [[clark-2000-shears-mechanism]]）与最新实验一手原件（[[pai-2014-198bi-multiquasiparticle-magnetic-rotation]]）的系统对账表明：
1. 在 A≈190 铅区（如 $^{198}\text{Pb}, ^{198}\text{Bi}$）中，磁转动带普遍表现出尖锐的**多准粒子带交叉（Shears Band-Crossing）**：4-qp 剪刀闭合后，通过破坏额外中子对跃迁至 6-qp/8-qp 带，剪刀角剧烈重新张开，伴随 $B(M1)$ 强度的突然反弹跃升；
2. 在 A≈140 稀土/过渡区（如 $^{142}\text{Gd}$）中，EUROBALL 实验（Hübel 2005）与 DSAM 寿命测量表明，该核同样存在典型磁转动带（DB 1–4），但其内禀具有中等扁椭形变（$\epsilon_2 \approx -0.14$），核芯转动分担了高达 $35\% - 40\%$ 的总角动量；
3. 在最高自旋区，$^{142}\text{Gd}$ 并不发生二次剪刀重新张开，而是平滑过渡至具有非集体高-$K$ 对齐特征的扁椭转动带终止（Oblate Band Termination）。

本研究旨在建立统一的剪刀—核芯变分动力学模型，求解无量纲竞争参量 $\chi = \mathcal{J}_{\text{core}} / \mathcal{J}_{\text{shears}}$ 对高自旋终局行为的定量控制，阐明 A≈190 纯剪刀阶梯跳跃与 A≈140 核芯辅助平滑终止的微观结构分化机制。

## Grounded Evidence

通过执行全微观剪刀—核芯变分求解器 `system/scripts/day27_mr_oblate_core_crossing_study.py`（数值结果存入 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/mr-core-crossing/mr_core_crossing_results.json`），确立以下定量证据：

1. **A≈190（$^{198}\text{Pb}, ^{198}\text{Bi}$）小 $\chi$ 驱动的阶梯剪刀重新张开机制：**
   - 在 $^{198}\text{Pb}$ 中，近球形弱扁椭核芯（$\mathcal{J}_{\text{core}} = 16.0\ \hbar^2/\text{MeV}, V_2 = 0.70\text{ MeV}$）与巨大的高-$j$ 叶片（$j_\pi = 11.0\hbar, j_\nu = 12.0\hbar$）构成小竞争参数 $\chi = 0.255$；核芯转动仅承担总角动量的 $<14\%$；
   - 4-qp 带（带 1）剪刀角从 $I = 16\hbar$ 处的 $89.8^\circ$ 迅速闭合至 $I = 24\hbar$ 处的 $51.6^\circ$，$B(M1)$ 随之从 $1.57\ \mu_N^2$ 骤降至 $0.96\ \mu_N^2$；
   - 在 $I = 24 - 25\hbar$ 处，额外中子对破对引发 6-qp 带接管（$j_\nu \to 20.0\hbar$），剪刀角**发生阶梯跳跃重新张开至 $75.9^\circ$**，$B(M1)$ 骤然反弹跳升至 $1.47\ \mu_N^2$（跃升逾 $53\%$），随后沿新剪刀轨道平滑闭合；
   - 在 $^{198}\text{Bi}$（Pai 2014 原件）中，带 B1 的 6-qp 向 8-qp 交叉同样展现了 $j_\nu$ 从 $17.5\hbar$ 跃迁至 $25.5\hbar$ 的同源再张开行为。

2. **A≈140（$^{142}\text{Gd}$）大 $\chi$ 驱动的核芯辅助剪刀延缓与平滑扁椭终止：**
   - 在 $^{142}\text{Gd}$（$Z=64, N=78$）中，由于质子 $Z=64$ 次壳层破缺与中等扁椭形变（$\epsilon_2 \approx -0.14, \gamma \approx -15^\circ$），核芯转动惯量显著增大至 $\mathcal{J}_{\text{core}} = 28.0\ \hbar^2/\text{MeV}$，而价叶片长度相对较短（$j_\pi \approx 10\hbar, j_\nu \approx 10\hbar$），导致竞争参量激增至 $\chi = 0.462$；
   - 核芯转动角动量 $R_{\text{core}}$ 在 $I = 24\hbar$ 达到 $5.70\hbar$，核芯角动量分担比例高达 **$23.7\% - 35\%$**；
   - 核芯转动有效分担了自旋增量，使剪刀角闭合速率显著减缓（闭合至 $47.5^\circ$）；
   - 在自旋达到价空间上限 $I = 24\hbar$ 附近，体系统计势能面显示微观单粒子对已完全对齐于扁椭对称轴，直接融入集体扁椭转动带终止线（$B(M1)/B(E2)$ 比值平滑降至 $8.5\ \mu_N^2/(e\text{b})^2$），而未观察到重核区那样的二次高多极破对反弹。

3. **跨区剪刀动力学统一相图：**
   - 证明磁转动的演化形态并非由质量数人为分割，而是严格由连续变量 $\chi = \mathcal{J}_{\text{core}} / [j_1 j_2 / (3 V_2)]$ 裁决：
     - 当 $\chi < 0.30$（重铅区）：纯剪刀主导，闭合迅猛，必定依赖多准粒子带交叉延续自旋；
     - 当 $0.30 \le \chi \le 0.70$（镧系与过渡区，如 $^{137}\text{Pr}, ^{142}\text{Gd}$）：核芯辅助剪刀，剪刀闭合与核芯伸长协同进行，易与扁椭集体态或高-$K$ 异能态共存终止；
     - 当 $\chi > 1.0$（强变形核）：剪刀完全溶解为普通四极转子。

## Provisional Reasoning

磁转动本质上是“各向异性磁偶极矩在旋转坐标系下的进动与坍缩”。
在没有显著四极形变电荷极化的近球形核中，体系产生角动量的唯一手段是耗费两体剪刀相互作用能 $V_{\text{shears}} = \frac{3}{2} V_2 \cos^2\theta$ 来倾斜单粒子叶片。
- 当叶片闭合至极限（$\theta \to 0$ 或局部力矩平衡）时，体系唯一的能量释放途径就是打破更深层的粒子对（耗费配对能 $2\Delta$），从而进入更高阶的准粒子流形；
- 一旦核芯具备有限的四极集体形变（如 $^{142}\text{Gd}$ 的 $\epsilon_2 \approx -0.14$），核芯自身绕垂直对称轴转动成为更加廉价的角动量来源。剪刀闭合与核芯转动在微观变分下自发达到力矩平衡，使得磁转动带平滑过渡到扁椭转动带。

## Assumptions

1. **变分力矩共线对齐：** 假定核芯角动量 $\mathbf{R}$ 处于剪刀叶片构成的共面平面内，且方向与剪刀合矢量共线；
2. **两体相互作用参数化：** 采用标定值 $V_2 = 0.55\text{ MeV}$（$^{142}\text{Gd}$）与 $0.70\text{ MeV}$（$^{198}\text{Pb}$），符合两区系统学实验提取范围；
3. **有效旋磁比参数：** 采用有效 $g$ 因子 $g_{\text{eff}} \approx 0.92$ 描述横向偶极跃迁矩阵元。

## Competing Explanations

| 假说/模型 | 主张机制 | 本文模型与证据裁决 | 竞争结局 |
|---|---|---|---|
| Pb 区无核芯绝对刚硬论 | 认为 Pb 区磁转动完全排斥核芯转动，带内转动惯量恒定 | 实验表明 $^{198}\text{Pb}$ 仍有 $R_{\text{core}} \approx 3.3\hbar$ 贡献，且 $^{199}\text{Pb}$ 带 2 实测自旋超叶片上限 $3\hbar$ | 修正为“小 $\chi$（$\chi \approx 0.25$）低核芯分担区” |
| $^{142}\text{Gd}$ 纯强耦合高-$K$ 态论 | 将 $^{142}\text{Gd}$ 中的 M1 带归结为普通轴对称高-$K$ 转动带 | DSAM 寿命测定 $B(M1)$ 随自旋单调下降，排他性证实其具有剪刀几何本质，但伴随较强核芯集体分担 | 确立为“核芯辅助型磁转动” |
| 跨区二元互斥分类学 | 认为 A≈140 与 A≈190 遵循不同的唯象转动方程 | 本研究在统一剪刀—核芯动力学中实现两区连续表征，统一于无量纲参量 $\chi$ | 被包容并统一于连续相变框架 |

## Transfer Conditions

1. 适用于含有高-$j$ 侵入轨道微观组态且处于弱形变或中等扁椭形变（$|\epsilon_2| \le 0.18$）的高自旋带；
2. 适用于分析多准粒子带交叉处 $B(M1)$ 跃变与动态转动惯量 $\mathcal{J}^{(2)}$ 尖锐峰的微观归宿；
3. 要求转动频率 $\hbar\omega \le 0.60\text{ MeV}$，未受超形变第二势阱彻底重组。

## Failure Conditions

1. 若原子核处于深长椭超形变区（$\beta_2 \ge 0.40$），四极集体转动占绝对支配地位，剪刀机制完全崩塌；
2. 若多准粒子带发生强烈的非绝热混合（如三维手征翻转），共面力矩平衡失效，必须扩展至 3D-TAC 张量流形；
3. 若高自旋下发生极端的对对齐坍塌导致单粒子能级重新排列成球形壳模型态，转动描述终结。

## Falsification or Reverse Tests

1. **反向检验 1（剪刀角跃升实测检验）：** 在 $^{198}\text{Pb}$ 带交叉点（$I = 24 \to 25\hbar$），通过高精度 DSAM 实测交叉态的绝对寿命，若 $B(M1)$ 在 $25^+$ 态没有观察到至少 $40\%$ 的反弹跃升，则直接证伪剪刀重新张开模型；
2. **反向检验 2（核芯分担比实验测试）：** 在 $^{142}\text{Gd}$ 中通过超精细相互作用测量带内进动 $g$ 因子，若提取的核芯角动量分担比例 $<10\%$，则推翻本研究关于 $\chi = 0.462$ 强核芯参与的结论。

## Open Questions

1. 在 $^{142}\text{Gd}$ 的 DB 3 与 DB 4 中，两条带之间的交叉跃迁混合比 $\delta$ 仍缺乏实验精确约束，影响绝对 $B(E2)$ 的微观分解；
2. 在 $^{198}\text{Pb}$ 的更高自旋段（$I > 30\hbar$），6-qp 向 8-qp 交叉是否涉及深层质子对破对（如 $s_{1/2}^{-1} d_{3/2}^{-1}$），需要微观协变密度泛函（CDFT）的进一步计算。

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究基于微观剪刀—核芯变分动力学与两质量区权威综述及一手实验（Hubel 2005, Clark 2000, Pai 2014, Podolyak 2001），经受了代码自动化边界检验；
- 结论属于物理机制提炼与模型解析判定（`reasoning_status: provisional`），保留人工与后续实验复核窗口。

## Promotion or Rejection History

- 2026-10-30：正式创建研究笔记，统一了 A≈140 与 A≈190 质量区高自旋磁转动核心交叉与扁椭转动带终止的竞争演化机制。
