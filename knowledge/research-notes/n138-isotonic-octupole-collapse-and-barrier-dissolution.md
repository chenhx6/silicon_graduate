---
type: research-note
title: "N=138同中子链八极形变猝灭与势垒融化微观机制：从226Ra刚性梨形转子到230U谐振八极振动"
aliases: [n138-isotonic-octupole-collapse-and-barrier-dissolution, N=138 octupole collapse 226Ra 230U, Day27 N=138 octupole]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [butler-2020-222-228ra-octupole-evolution, gaffney-2013-pear-shaped-rn-ra, butler-nazarewicz-1996-intrinsic-reflection-asymmetry]
created_from: Day 27 continuation study; system/scripts/day27_n138_octupole_collapse_rn_ra_th_u_study.py
tags: [octupole-deformation, N=138, pear-shape, double-well-barrier, alternating-parity, 224Rn, 226Ra, 228Th, 230U, Day27]
---

# N=138 同中子链八极形变猝灭与势垒融化微观机制：从 226Ra 刚性梨形转子到 230U 谐振八极振动

## Research Trigger

在轻锕系原子核的反射不对称结构中，$N \approx 134 - 138$ 是核图上八极关联最强烈的经典岛区。然而，沿固定中子数 **$N = 138$** 同中子链的系统学演化展现出令人瞩目的反常突变：
1. **$^{226}\text{Ra}$（$Z=88$）的刚性梨形旋转**：[[butler-2020-222-228ra-octupole-evolution]]（PRL 124, 042503）与 Coulomb 激发实验证实，$^{226}\text{Ra}$ 具有极大的内禀八极矩（$Q_3 \approx 1050\ e\text{ fm}^3$）与极低的负宇称带头（$E(1^-) = 253.7\text{ keV}$），表现出理想交替宇称转动带与深双阱势垒；
2. **$^{230}\text{U}$（$Z=92$）的突发性八极塌缩**：仅增加 4 个质子到达铀同位素 $^{230}\text{U}$，内禀反射不对称性突然崩溃；负宇称 $1^-$ 态能量急剧飙升至 **$634.9\text{ keV}$**，内禀八极矩腰斩，交替宇称能级级联完全解体，原子核退化为普通的四极长椭转子加高能八极表面振动态。

传统唯象宏观液滴模型无法解释为何同中子数下仅改变质子数 $Z=88 \to 92$ 就会诱发如此剧烈的相变。
本研究基于 Nilsson-Strutinsky 壳修正与粒子-空穴八极极化率模型 `day27_n138_octupole_collapse_rn_ra_th_u_study.py`，微观阐释导致八极势垒融化的双驱动机制：质子八极易感性猝灭与四极核芯拉长稀释效应。

## Grounded Evidence

通过执行全微观 $N=138$ 同中子链八极演化求解器 `system/scripts/day27_n138_octupole_collapse_rn_ra_th_u_study.py`，并在 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/n138-octupole-collapse/n138_octupole_collapse_results.json` 沉淀结构化数据，确立以下定量证据：

1. **质子 $\Delta j = \Delta l = 3$ 八极共振驱动项的微观猝灭：**
   - 轻锕系区八极形变的核心微观驱动力源自穿过费米面的质子正常宇称轨道 $\pi f_{7/2}$ 与侵入轨道 $\pi i_{13/2}$ 之间的强烈微观多极偶极相互作用；
   - 在 $Z = 88$（$^{226}\text{Ra}$）中，质子费米面精确坐落于 $\pi f_{7/2} - \pi i_{13/2}$ 壳隙的正中央，配对相干因子 $(u_p v_{p'} + v_p u_{p'})^2$ 达到最大值 $1.0$，诱发极强的相对质子八极易感性（$\chi_3^p \equiv 1.0$）；
   - 当质子数增加至 $Z = 92$（$^{230}\text{U}$）时，4 个额外价质子强行填入 $\pi i_{13/2}$ 低 $\Omega$ 轨道（$[660]1/2, [651]3/2$），费米面显著上移并远离主八极能隙；微观相干因子被剧烈削弱，质子八极易感性暴跌至 **$\chi_3^p \approx 0.142$（衰减逾 $7$ 倍）**，使八极自洽平均场彻底丧失了克服单极重力恢复力的微观驱动。

2. **四极长椭拉长引起的八极几何稀释（$\beta_2$ Dilution）：**
   - 伴随价质子增加，中子-质子四极相互作用驱动基态四极形变显著递增：从 $^{224}\text{Rn}$（$\beta_2 = 0.140$）、$^{226}\text{Ra}$（$\beta_2 = 0.165$）持续扩张至 $^{230}\text{U}$ 的 **$\beta_2 = 0.235$**；
   - 强烈的四极椭球拉伸导致球形单粒子轨道发生剧烈的 $K$-分裂，原本高度简并的 $\Delta K = 0$ 八极相干矩阵元被空间发散的各个本征态撕裂稀释（稀释因子高达 $1.8$ 倍），协同加速了八极势阱的瓦解。

3. **势能面双阱势垒融化与 $1^-$ 能级跃变：**
   - $^{226}\text{Ra}$：双阱势能面在 $\beta_3 = \pm 0.135$ 处具有深达 **$V_{\text{barrier}} = 1.25\text{ MeV}$** 的内禀八极反演势垒；较厚的势垒抑制了宇称反转隧穿，导出极低的基态宇称双重态跃迁能量 $E(1^-)_{\text{calc}} = 182.3\text{ keV}$（实测 $253.7\text{ keV}$），内禀八极矩高达 $Q_3 = 1052.6\ e\text{ fm}^3$（实测 $1050\ e\text{ fm}^3$），为典型的**刚性梨形转子**；
   - $^{228}\text{Th}$：势垒高度骤降至 $0.08\text{ MeV}$，处于微弱软八极双阱向单阱过渡区（$E(1^-) = 328.0\text{ keV}$）；
   - $^{230}\text{U}$：势能面双阱势垒完全归零（**$V_{\text{barrier}} \equiv 0.0\text{ MeV}$**），平衡形变退化至 $\beta_3 = 0.0$；势能面转化为高刚度的简谐单阱，宇称反转态蜕变为高能八极振动声子，$E(1^-)$ 陡升至 **$660.5\text{ keV}$（实测 $634.9\text{ keV}$）**，内禀八极矩缩减至 $520\ e\text{ fm}^3$，在微观动力学上严密闭合了轻锕系八极猝灭的机制链条。

## Evidence Boundaries & Review Status

- 物理模型：结合 Nilsson-Strutinsky 壳修正能、八极配对易感性与一维 WKB 隧穿双阱模型；
- 证据层级：基于 Butler 2020、Gaffney 2013 及 NNDC adopted levels 实验谱学；
- 审定状态：本笔记为 Day 27 博士生级开放研学计算工件沉淀，标记为 `status: ai-draft`、`review_status: unreviewed`。

## Provisional Reasoning

本页原有内容的机制判断保持 provisional；模型结果、作者解释与本任务综合不升级为实验事实。

## Assumptions

- 仅在原有来源、质量区和方法适用条件成立时使用本页判断。
- 缺失的响应、协方差或伴随观测不由本页补造。

## Competing Explanations

- 竞争解释包括组态重排、门条件/响应效应、统计碎片化和模型约定差异；当前页面不把单一机制写成排他结论。

## Transfer Conditions

- 向其它核素或质量区迁移前，必须重新核对直接来源、观测量、谱系、响应和独立性。

## Failure Conditions

- 原始输入、locator、响应、协方差或必要伴随观测缺失时，本页只能作为 L3/readiness boundary 使用。

## Falsification or Reverse Tests

- 若受控的反向检验、独立实验或共同响应使关键预测域不相交，应降低或撤回本页的 provisional 判断。

## Open Questions

- 需要补齐原始数据/响应/协方差、独立 holdout 和竞争解释的可区分预测。

## Human Review

本页为 Codex self-audit；`review_status: unreviewed`，未设置 `human-reviewed`，未清除任何 claim 的 `needs_review`。

## Promotion or Rejection History

| Date | event | previous state | new state | reason |
|---|---|---|---|---|
| 2026-10-31 | schema boundary completion | incomplete structure | provisional | required governance sections added without changing scientific claims |
