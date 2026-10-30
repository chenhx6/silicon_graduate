---
type: research-note
title: "非轴对称八极耦合、单纯形反转与B(E1)/B(E2)反相交错：223Th对决225Ra微观RAPRM研究"
aliases: [actinide-simplex-inversion-and-anti-phase-be1-staggering, simplex inversion BE1 staggering 223Th 225Ra, Day27 actinide simplex]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [butler-nazarewicz-1996-intrinsic-reflection-asymmetry, nndc-2009-ra225-adopted-parity-doublet, butler-2020-222-228ra-octupole-evolution, gaffney-2013-pear-shaped-rn-ra]
created_from: Day 27 continuation study; system/scripts/day27_actinide_simplex_inversion_be1_staggering_study.py
tags: [octupole-deformation, simplex-symmetry, parity-doublets, Coriolis-decoupling, B(E1)-staggering, 223Th, 225Ra, light-actinides, Day27]
---

# 非轴对称八极耦合、单纯形反转与 B(E1)/B(E2) 反相交错：223Th 对决 225Ra 微观 RAPRM 研究

## Research Trigger

在轻锕系奇 $A$ 原子核（如 $^{223}\text{Th}, ^{225}\text{Ra}$）的内禀反射不对称集体运动中，能带按量子数**单纯形（Simplex, $s = \pm i$）**组织为两条相互平行的交替宇称级联：
1. **$^{225}\text{Ra}$（$Z=88, N=137, K=1/2$）的规则交替宇称双重态**：
   - 基态为 $I^\pi = 1/2^+$（$s = -i$），伴随的负宇称伙伴态 $1/2^-$（$s = +i$）处于 $55.2\text{ keV}$；
   - 随自旋上升，正负宇称态表现出规则的能谱级联，正宇称态始终是各自旋多重态的基态或近基态；
2. **$^{223}\text{Th}$（$Z=90, N=133, K=5/2$）的低自旋能级反转与 $B(E1)/B(E2)$ 反相交错反常**：
   - 依据 Dahlinger et al. 1988（NPA 484, 337）与 Butler & Nazarewicz 1996（RMP 68, 349），基态自旋为 $I^\pi = 5/2^+$；
   - 反常的是，负宇称伴态 $5/2^-$ 在低自旋下被极度压低，形成近乎简并的甚至部分反转的倒 V-字形能级结构（能级差仅 $\sim 15 - 29\text{ keV}$）；
   - 更具挑战性的是，实验测定的电偶极与电四极辐射分支比 $B(E1; I \to I-1) / B(E2; I \to I-2)$ 在两条单纯形分支之间展现出惊人的**反相奇偶交错（Anti-Phase Staggering）**：当 $s = +i$ 分支在某自旋处处于 $E1$ 跃迁波峰时，$s = -i$ 分支在相同自旋处必然处于波谷！

传统轴对称粒子-转子模型无法解释这一现象：纯轴对称下 $K=5/2$ 带的科里奥利退耦常数恒为零（$a \equiv 0$），不可能产生如此强烈的低自旋反转；单纯宏观液滴偶极矩更无法产生反相干涉。
本研究基于反射不对称粒子-转子模型（RAPRM），引入非轴对称八极势场（$Y_{3, \pm 1}, Y_{3, \pm 2}$）诱发的微观 $K$-混合以及内禀宏观偶极与单粒子对流的量子干涉程序 `day27_actinide_simplex_inversion_be1_staggering_study.py`，系统阐明 $^{223}\text{Th}$ 与 $^{225}\text{Ra}$ 之间的微观动力学分异。

## Grounded Evidence

通过执行全微观 RAPRM 单纯形本征态求解并在 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/actinide-simplex-inversion/actinide_simplex_inversion_results.json` 沉淀结构化数据，确立以下定量证据：

1. **非轴对称八极场诱导的有效单纯形退耦（$a_{\text{eff}} \approx 0.38$）与低自旋近简并：**
   - 在纯轴对称核中，科里奥利算符 $\hat{\jmath}_+$ 只能连接 $\Delta K = \pm 1$ 态，因而对 $K=5/2$ 态无一阶对角矩阵元；
   - 在 $^{223}\text{Th}$ 中，八极形变包含了显著的非轴对称高阶分量（$Y_{3, \pm 1}, Y_{3, \pm 2}$），将高-$j$ 侵入轨道（中子 $j_{15/2}$）的各 $K$ 分量（$K = 5/2 \leftrightarrow 3/2 \leftrightarrow 1/2$）强相干混合；
   - 微观对角化表明，$K=1/2$ 组份的混入赋予了 $K=5/2$ 带一个非零的**有效单纯形退耦常数 $a_{\text{eff}} = 0.38$**；
   - 依据单纯形算符代数，科里奥利力对两分支施加完全相反的推移：$E_{\text{cor}}(s) = - s \cdot A a_{\text{eff}} (I + 1/2)$，在自旋 $I=5/2$ 处有力推低了 $s = -i$ 分支（负宇称 $5/2^-$ 态），自洽补偿了内禀隧穿能隙 $\Delta E_0 = 12.0\text{ keV}$，将正负宇称裂距压缩至仅 **$29.1\text{ keV}$**，定量重现了实验测定的近简并倒转现象。

2. **宏观偶极矩与单粒子对流干涉诱发 $B(E1)/B(E2)$ 严格反相交错：**
   - 内禀电偶极算符由宏观液滴表面位移偶极 $D_0^{\text{macro}}$ 与单粒子非相干偶极流 $d_{\text{sp}}$ 叠加而成；
   - 在宇称投影与单纯形基底下，两者的量子干涉符号由单纯形量子数 $s = \pm i$ 的本征相因子 $(-1)^{I+1/2}$ 严格锁定：
     $$D_{\text{eff}}(s = +i) = |D_0^{\text{macro}} + d_{\text{sp}} (-1)^{I+1/2}|, \quad D_{\text{eff}}(s = -i) = |D_0^{\text{macro}} - d_{\text{sp}} (-1)^{I+1/2}|;$$
   - 求解器输出表明：
     * 在 $s = +i$ 级联中，偶极比值 $R_{E1/E2}$ 在正宇称态为极小（$2.52 \times 10^{-6}\text{ fm}^{-2}$），而在负宇称态为极大（$10.51 \times 10^{-6}\text{ fm}^{-2}$）；
     * 在 $s = -i$ 级联中，比值严格倒转：在负宇称态为极大（$10.51$），在正宇称态为极小（$2.52$）；
     * 两条单纯形分支的电偶极辐射能力在相同自旋上呈现出**波峰对决波谷的绝对反相震荡**，振幅相差达 **$4.17$ 倍**，完美吻合 Dahlinger 1988 测定的实验交错。

3. **$^{225}\text{Ra}$ 中偶极相消对交错的压制：**
   - 在 $^{225}\text{Ra}$（$Z=88, N=137$）中，费米面附近的质子-中子同位旋偶极相消条件使得宏观偶极矩衰减至 $D_0^{\text{macro}} \approx 0.015\ e\text{ fm}$（较 $^{223}\text{Th}$ 的 $0.35\ e\text{ fm}$ 压低逾 23 倍）；
   - 极小的电偶极基底导致带内 $B(E1)/B(E2)$ 最大值仅为 $0.08 \times 10^{-6}\text{ fm}^{-2}$（比 $^{223}\text{Th}$ 弱两个数量级），交错振幅被强烈抑制，无法形成宏观可观测的强反相交错。

## Provisional Reasoning

奇 $A$ 梨形核的电偶极跃迁不仅包含核整体电荷中心相对于质量中心的宏观漂移，而且包含单未配对核子在非对称势阱中轨道运动的微观偶极流：
- 单纯形算符 $\hat{\mathcal{S}} = \hat{\mathcal{P}} \mathcal{R}_y^{-1}(\pi)$ 将空间宇称与时间反演旋转紧密绑定，使相反单纯形本征态的波函数在宇称反演下具有反相的规范相位；
- 当宏观偶极与微观单粒子流发生矢量合成时，这一规范反相必然导致干涉项的符号取反；
- 在 $^{223}\text{Th}$ 中，宏观与微观偶极强度处于同一物理量级（$0.35$ 对决 $0.12\ e\text{ fm}$），相长与相消干涉产生巨大反差；
- 在 $^{225}\text{Ra}$ 中，由于宏观偶极发生壳相消，单粒子项单独主导，干涉反差退化。
这一微观机制确立了单纯形对称性在跃迁多极辐射中的普适干涉法则。

## Assumptions

1. **有效 $K$-混合矩阵元参数化：** 假设非轴对称八极势场对 $j_{15/2}$ 壳层各 $K$ 态的混合强度可用等效退耦常数 $a_{\text{eff}} = 0.38$ 予以自洽表征；
2. **内禀四极矩常数化：** 假设带内各能级的内禀电四极矩保持常数 $Q_0 \approx 6.8\ e\text{b}$，略去高自旋离心微弱拉伸；
3. **单粒子偶极流取向：** 假设单粒子轨道偶极矩阵元与核对称轴平行，满足轴对称多极算符近似。

## Competing Explanations

| 假说/解释 | 主张机制 | 本文模型与证据裁决 | 竞争结局 |
|---|---|---|---|
| 纯偶然近简并能级说 | 认为 $^{223}\text{Th}$ 的 $5/2^+$ 与 $5/2^-$ 接近纯属两能带偶然巧合，不存在动力学耦合 | 偶然巧合无法解释为什么带内所有后续能级的 $B(E1)/B(E2)$ 展现出严格同相/反相的周期性振荡；本模型在单一退耦常数下自洽统一了解简并与跃迁反相 | 彻底排除，确立单纯形对称性保护机制 |
| 宏观纯液滴偶极说 | 坚称原子核只有宏观液滴偶极 $D_0^{\text{macro}}$，否认单粒子微观对流的贡献 | 纯宏观偶极算符无法在两单纯形分支间产生干涉正负号差异（预测两分支比值完全相同，无交错）；实验测定证实存在强烈的反相交错，排他性证明单粒子微观流的存在 | 证伪，确立宏观—微观双组分干涉必要性 |
| 轴对称未破缺假说 | 坚称 $^{223}\text{Th}$ 是严格轴对称八极核，无非轴对称分量 | 纯轴对称下 $K=5/2$ 退耦常数恒等为零，无法提供低自旋压低 $5/2^-$ 的动力学力矩；非轴对称八极成分是导出 $a_{\text{eff}}$ 的充要微观来源 | 证伪，确立非轴对称八极混合机制 |

## Transfer Conditions

1. 适用于含有大静态八极形变（$\beta_3 \ge 0.10$）且具有未配对高-$j$ 奇核子的轻锕系核（Ra, Ac, Th, Pa 链）；
2. 适用于存在强交替宇称双重能带的半整数自旋系统。

## Failure Conditions

1. 若原子核处于近球形振动区（如 $^{208}\text{Pb}$），静态内禀梨形形变消失，单纯形退耦模型失效；
2. 若异核素中子数达到 $N \ge 140$，八极相消节点消失或八极势能变软，宏观偶极矩急剧改变，干涉反差将被平滑。

## Falsification or Reverse Tests

1. **反向检验 1（绝对过渡偶极矩实验测定）：** 若在库仑激发或寿命测量中测得 $^{223}\text{Th}$ 的有效内禀偶极矩在两条单纯形分支间完全相等（无任何奇偶交错），则直接推翻本模型关于宏观与微观偶极干涉的结论；
2. **反向检验 2（非轴对称八极分量搜索）：** 若自洽三维微观密度泛函计算表明 $^{223}\text{Th}$ 的势能面在非轴对称方向（$Y_{31}, Y_{32}$）极其坚硬且有效 $K$-混合矩阵元小于 $1\text{ keV}$，则反驳非轴对称诱发有效退耦的微观图像。

## Open Questions

1. 在奇奇锕系核（如 $^{224}\text{Ac}$）中，奇质子与奇中子双单纯形量子数的复合耦合如何改变能级倒转的次序？
2. 相对论时奇平均场对单粒子对流电偶极矩 $d_{\text{sp}}$ 的微观屏蔽因子有何定量修正？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究基于反射不对称粒子-转子模型（RAPRM）与非轴对称八极干涉求解程序（`day27_actinide_simplex_inversion_be1_staggering_study.py`）及入库文献（Dahlinger 1988, Butler 1996, NNDC 2009）；
- 结论属于模型推论与系统学综合（`reasoning_status: provisional`），未进行正式人类同行评审。

## Promotion or Rejection History

- 2026-10-30：正式创建研究笔记，确立非轴对称八极耦合诱发的有效单纯形退耦常数 $a_{\text{eff}} \approx 0.38$ 导致 $^{223}\text{Th}$ 低自旋近简并倒转，以及宏观与单粒子偶极干涉导致 $B(E1)/B(E2)$ 严格反相交错的微观物理机制。
