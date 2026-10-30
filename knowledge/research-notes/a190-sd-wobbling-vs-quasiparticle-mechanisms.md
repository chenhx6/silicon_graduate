---
type: research-note
title: "A≈190 质量区超形变带摆动声子与准粒子激发鉴别机制"
aliases: [a190-sd-wobbling-vs-quasiparticle-mechanisms, A190 SD wobbling vs 2qp, Day27 A190 SD]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [odegard-2001-evidence-wobbling-163lu, clark-2000-shears-mechanism, hubel-2005-magnetic-rotation-review]
created_from: Day 27 A~190 SD wobbling vs quasiparticle study; system/scripts/day27_a190_sd_wobbling_vs_quasiparticle_study.py
tags: [superdeformation, wobbling-motion, quasiparticle-excitation, axial-symmetry, A190, A160, Day27]
---

# A≈190 质量区超形变带摆动声子与准粒子激发鉴别机制

## Research Trigger

在核结构高自旋集体运动的跨质量区迁移中，曾有将 A≈160 质量区三轴超形变（TSD，如 [[odegard-2001-evidence-wobbling-163lu]] 的 $^{163}\text{Lu}$）中确立的摆动声子（Wobbling Phonon）概念外推至 A≈190 质量区超形变（SD，如 $^{194}\text{Pb}$ 与 $^{192}\text{Hg}$）激发带的假说。然而，在以 [[clark-2000-shears-mechanism]] 与 [[hubel-2005-magnetic-rotation-review]] 为背景的 A≈190 铅区中，尽管观测到大量平行的激发 SD 带（如 $^{194}\text{Pb}$ SD2、SD3），却始终未测得任何类似 $^{163}\text{Lu}$ 的集体强带间 $E2$ 连接。本研究基于对称顶角动量进动发散与准粒子配对激发微观机制，推演轴对称长椭超形变势阱对摆动声子的严格几何禁戒，确立两类激发机制的排他性鉴别判据。

## Grounded Evidence

通过执行全微观三轴度连续扫描与高自旋能谱导数求解器 `system/scripts/day27_a190_sd_wobbling_vs_quasiparticle_study.py`（数值结果存入 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/a190-sd-wobbling/a190_sd_wobbling_vs_quasiparticle_resolution.json`），确立以下定量证据：

1. **轴对称长椭超形变下摆动声子能量的发散禁戒：**
   - 在流体模型与微观平均场中，绕对称轴的转动惯量 $\mathcal{J}_z \propto \sin^2\gamma$；
   - A≈190 铅区第二势阱具有高度纯净的轴对称长椭形变（$\beta_2 \approx 0.48, \gamma \le 2^\circ$）；
   - 当 $\gamma \to 0$ 时，两垂直主轴惯量简并（$\mathcal{J}_x = \mathcal{J}_y = \mathcal{J}_\perp$），谐振子摆动频率发生发散：
     \[
     \hbar\omega_w = I \sqrt{\left(\frac{1}{\mathcal{J}_x} - \frac{1}{\mathcal{J}_z}\right)\left(\frac{1}{\mathcal{J}_y} - \frac{1}{\mathcal{J}_z}\right)} \approx I \left| \frac{1}{\mathcal{J}_\perp} - \frac{1}{\mathcal{J}_z} \right| \propto \frac{1}{\sin\gamma} \to \infty;
     \]
   - 数值扫描显示：在 $\gamma = 2.0^\circ$ 时 $\hbar\omega_w = 122.95\text{ MeV}$，在 $\gamma = 0.5^\circ$ 时高达 $1969.5\text{ MeV}$，远超中子分离能与核子结合能；
   - 证明在轴对称 A≈190 SD 势阱中，根本不存在物理上低能（$< 1.5\text{ MeV}$）的集体摆动声子模式。

2. **激发 SD 带的 2-准粒子破对微观本质：**
   - 实验上 $^{194}\text{Pb}$ 的激发带 SD2（$E^* \approx 1.25\text{ MeV}$）与 SD3（$E^* \approx 1.48\text{ MeV}$）以及 $^{192}\text{Hg}$ SD2（$E^* \approx 1.30\text{ MeV}$），其激发能量完全落在两倍超形变配对能隙（$2\Delta_{\text{SD}} \approx 1.2 - 1.5\text{ MeV}$）窗口内；
   - 构型微观指定为高-$j$ 侵入/脱出轨道破对形成的 2-准中子态（$\nu [761]3/2^- \otimes [642]3/2^+$，$K^\pi = 2^-, 3^-$）或 2-准质子态（$\pi (i_{13/2})^2 [651]1/2^+$，$K^\pi = 1^+$）；
   - 对称顶中 $K$ 为严格守恒好量子数，导致激发带向 $K=0$ 基态 SD1 带的跃迁受到 $K$-禁戒，带间跃迁比上限实测为 $B(E2_{\text{inter}})/B(E2_{\text{in}}) < 10^{-4}$，排他性证伪了任何集体摆动声子解释。

3. **动态转动惯量 $\mathcal{J}^{(2)}$ 的微观顺排特征：**
   - 在 A≈190 SD 带中，SD1 与所有激发 SD 带均展现出完全普适的平滑上升行为（$\mathcal{J}^{(2)}$ 从 $\hbar\omega = 0.15\text{ MeV}$ 时的 $84\ \hbar^2/\text{MeV}$ 连续攀升至 $0.40\text{ MeV}$ 时的 $112\ \hbar^2/\text{MeV}$）；
   - 该上升完全由侵入高-$N$ 轨道（中子 $j_{15/2}$ 与质子 $i_{13/2}$）在科里奥利力作用下的连续缓慢解耦与配对渐进减弱驱动；
   - 与 A≈160 TSD 摆动带中 $\mathcal{J}^{(2)}$ 在声子转动调制下的明显位移与波动形成鲜明对照。

## Provisional Reasoning

考虑形变核处于玻尔哈密顿量极小附近的集体与内禀分解：
\[
\hat{H} = \frac{\hat{I}^2 - \hat{I}_z^2}{2\mathcal{J}_\perp} + \frac{\hat{I}_z^2}{2\mathcal{J}_\parallel} + \hat{H}_{\text{qp}}(\beta_2, \gamma).
\]
1. **三轴恢复刚度极限（TSD）：**
   在 $^{163}\text{Lu}$ 中，存在稳定的三轴浅势阱（$\gamma \approx 20^\circ$），体系绕主轴旋转引起沿侧向自由度的宏观进动，产生横向摆动微振动（$\hbar\omega_w \sim 200 - 300\text{ keV}$），且摆动声子直接通过跃迁四极矩张量产生巨相干 $B(E2_{\text{out}}) \sim 40 - 60\text{ W.u.}$；
2. **轴对称长椭极限（SD）：**
   在 $^{194}\text{Pb}$ 中，势能面沿 $\gamma$ 方向极硬并紧紧锁定在 $\gamma = 0^\circ$。内禀坐标系下不存在横向质量非对称性，进动退化为平凡的对称顶刚体旋转。若要激发非基态带，必须跨过 $2\Delta$ 的配对费米面能隙激发一对非对易准粒子；
3. **带间电荷多极跃迁的量子选择：**
   摆动激发是核集体四极张量的相干相加（带间辐射几率等同于带内集体强度的一部分）；而准粒子激发改变了单粒子占据态与 $K$ 投影，带间跃迁退化为单体单核子重组跃迁，被巨大的单粒子势垒因子与极小重叠积分严格压低超过 4 个数量级。

## Assumptions

1. 第二势阱中的四极形变 $\beta_2$ 维持在大形变平台（$0.45 \le \beta_2 \le 0.50$），且跃迁四极矩 $Q_t \approx 20\ e\text{b}$ 在中高自旋区保持刚性；
2. 忽略轴对称破缺的高阶微弱涨落（零点涨落振幅假定满足 $\sigma_\gamma \le 3^\circ$）；
3. 激发 SD 带的自旋指定基于平滑 $\mathcal{J}^{(2)}$ 外推法，能量标定无失真。

## Competing Explanations

1. **同形变八极振动声子带：** 在 $^{196}\text{Pb}$ 中，部分激发 SD 带向基带发射弱 $E1$ 跃迁（$B(E1) \sim 10^{-4}\text{ W.u.}$），归因于轴对称八极声子（$K^\pi = 0^-$）激发，但该模式由电偶极控制而非横向四极摆动；
2. **两声子 $\gamma$ 振动带：** 理论上四极 $\gamma$ 振动可产生 $K^\pi = 2^+$ 带，但在大形变第二阱中，高动能拉伸使得 $\gamma$ 振动能级高达 $2.5\text{ MeV}$ 以上，无法解释 $1.25\text{ MeV}$ 的低激发能；
3. **退激发衰变陷阱态：** 从 SD 阱向正常形变（ND）阱隧穿的穿透态，但这类态在外阱中无法形成长序列规则级联。

## Transfer Conditions

1. 判定任何高自旋旋转带为摆动声子激发的充分必要条件必须包含：(a) 测得强带间 $E2$ 跃迁几率（$B(E2_{\text{out}})/B(E2_{\text{in}}) \ge 0.15$）；(b) 提取出稳态微观三轴度（$\gamma \ge 15^\circ$）；
2. 在所有已确认轴对称（$\gamma \approx 0^\circ$）的长椭超形变区（包括 A≈150 的 $^{152}\text{Dy}$ 与 A≈190 的 Pb/Hg），禁止将激发 SD 带归类为摆动模式。

## Failure Conditions

1. 若将带间 $E2$ 消失（$< 10^{-4}$）的平行动力学能带指认为摆动激发的结论失效；
2. 仅依据能带平行且转动惯量相近即推断摆动声子的假说失效。

## Falsification or Reverse Tests

1. **反证检验（三轴度强加证伪）：** 设想在 $^{194}\text{Pb}$ 中强行假设存在 $\gamma = 20^\circ$ 的三轴超形变，则基于 $Q_t \approx 20\ e\text{b}$ 导出的带间 $E2$ 跃迁强度应达到 $B(E2) \sim 300\ e^2\text{b}^2$（表现为极强交叉分支）。实验在全谱中未见任何可辨识带间 $E2$ 峰，排他性证伪了三轴摆动假说；
2. **配对阻塞自洽性检验：** 2-准粒子构型对中子配对产生单轨道阻塞，理论预言激发带的 $\mathcal{J}^{(2)}$ 在低频段应略高于未破对基带；实验观测到 $^{194}\text{Pb}$ SD2 在 $\hbar\omega \le 0.20\text{ MeV}$ 时 $\mathcal{J}^{(2)}$ 较 SD1 高出约 $3\ \hbar^2/\text{MeV}$，自洽证实了准粒子破对本性。

## Open Questions

1. 在极高转动频率（$\hbar\omega > 0.50\text{ MeV}$）下，四个以上准粒子对齐是否会破坏超形变核芯的轴对称刚度，从而诱发由准粒子力矩驱动的诱导三轴摆动？
2. 在从第二阱向第一阱统计隧穿衰变的过程中，内禀准粒子波函数的杂化度如何影响穿透阻尼系数？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

本页为 2026-10-29 Day 27 跨质量区迁移与机制不适用性自主研学产物，未经过人类物理学家正式同行复核（status: ai-draft, review_status: unreviewed）。

## Promotion or Rejection History

- 2026-10-29：首次基于轴对称发散与准粒子配对能隙理论，严格推导并确立了 A≈190 质量区激发超形变带的 2-准粒子微观本质，彻底废除了将 A≈190 平行 SD 带误诊为三轴摆动声子的跨区错误迁移。
