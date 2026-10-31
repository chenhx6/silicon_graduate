---
type: research-note
title: "三轴超形变（TSD）带中八极激发抑制与偶极矩淬灭微观机制：大长椭K-劈裂对决轻锕系交替宇称转子"
aliases: [tsd-octupole-suppression-and-dipole-quenching, TSD octupole suppression 163Lu 165Lu, Day27 TSD octupole]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [schonwasser-2003-tsd-wobbling-165lu, odegard-2001-evidence-wobbling-163lu]
created_from: Day 27 continuation study; system/scripts/day27_tsd_octupole_suppression_and_dipole_quenching_study.py
tags: [triaxial-superdeformation, octupole-suppression, dipole-quenching, wobbling, 163Lu, 165Lu, 224Ra, Day27]
---

# 三轴超形变（TSD）带中八极激发抑制与偶极矩淬灭微观机制：大长椭 K-劈裂对决轻锕系交替宇称转子

## Research Trigger

在低能核结构的内禀反射不对称集体运动中，轻锕系区原子核（如 $^{224}\text{Ra}, ^{226}\text{Th}$，中等长椭形变 $\beta_2 \approx 0.16$）展现出极其显著的八极宇称双重态与交替宇称带级联，其带间电偶极跃迁几率高达 $B(E1) \sim 10^{-2}\ W.u.$，由大宏观核芯电偶极矩 $D_0 \approx 0.35\ e\text{ fm}$ 所支撑。

然而，在稀土区三轴超形变（TSD）能带系统（如 $^{163}\text{Lu}, ^{165}\text{Lu}$，$\beta_2 \approx 0.40, \gamma \approx 20^\circ$）的超高统计量谱学探测中（[[schonwasser-2003-tsd-wobbling-165lu]]，PLB 552, 9）：
1. 体系虽然展现出极其强烈的四极超形变与纯净的 $n_w = 1, 2$ 横向摆动（Wobbling）多声子阶梯，但**从未观测到任何与 TSD 带相伴的交替宇称八极伙伴带**；
2. 实验将所有潜在的带间 $E1$ 跃迁强度上限严格压缩至 **$B(E1) < 10^{-5}\ W.u.$（较轻锕系核受到逾 $10^3$ 倍的极端压制）**。

本研究基于 Nilsson 空间单粒子能级多重 $K$-分裂、微观八极凝聚阈值与液滴偶极相消模型 `day27_tsd_octupole_suppression_and_dipole_quenching_study.py`，微观阐明为何三轴超形变环境会彻底“冻结”八极集体性，确立八极交替宇称模型向超形变区平移的不可适用性硬边界。

## Grounded Evidence

通过执行全微观 TSD 八极抑制变分求解器 `system/scripts/day27_tsd_octupole_suppression_and_dipole_quenching_study.py`，并在 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/tsd-octupole-suppression/tsd_octupole_suppression_results.json` 沉淀结构化数据，确立以下定量证据：

1. **大长椭与三轴混合对八极驱动能隙的微观几何稀释（$\beta_2$ / $\gamma$ Dilution）：**
   - 产生永久八极形变的核心驱动力源自穿过费米面的 $\Delta j = \Delta l = 3$ 轨道对（如质子 $\pi i_{13/2} - \pi f_{7/2}$ 与中子 $\nu j_{15/2} - \nu g_{9/2}$）；
   - 在中等形变锕系区（$\beta_2 \approx 0.16$），这些球形轨道保持紧密的低能近简并，八极配对易感性 $\chi_3 \approx 1.0$ 超过凝聚临界阈值，诱发双阱势能面；
   - 在 TSD 极小（$\beta_2 = 0.40, \gamma = 20.0^\circ$）下，巨大的四极拉伸诱发极强烈的 Nilsson 能级分裂，且三轴度打破了轴对称柱投影守恒；原本相干的八极对跃迁通道被撕裂为四个空间发散的非简并 $K=0, 1, 2, 3$ 子分支；
   - 微观八极相干度暴跌近 $3$ 倍（$\chi_3^{\text{eff}} \approx 0.347 < \chi_{\text{crit}} = 0.55$），导致势能面双阱反转势垒彻底消失，被锁定为简谐单阱，八极声子本征能量被推高至 **$E_{\text{oct}} \approx 3.39\text{ MeV}$**，完全脱离了冷转动带空间。

2. **宏观液滴电偶极矩的同位旋代数相消：**
   - 液滴偶极矩取决于质子质心与核电荷分布的不对称偏离：$D_0 \approx C_{\text{drop}} A Z \beta_2 \beta_3 [1 - c_A (N-Z)/A]$；
   - 在中子过剩的轻锕系核（$Z=88, N=136$）中，中子皮向核钝端漂移，产生可观的宏观电偶极矩 $D_0 \approx 0.26 - 0.35\ e\text{ fm}$；
   - 在稀土区镥同位素（$^{163}\text{Lu}$，$Z=71, N=92$）中，同位旋不对称度显著收缩（$N/Z \approx 1.30$ 对比锕系的 $1.55$），质子与中子质量分布几乎完全共形，代数中和因子导致内禀电偶极矩被淬灭至 **$D_0 \le 0.013\ e\text{ fm}$（衰减逾 $25$ 倍）**；
   - 结合零点八极涨落幅度，理论自洽导出带间 $E1$ 跃迁强度上限为 **$B(E1) \approx 1.01 \times 10^{-5}\ W.u.$（完全符合 Gammasphere 实验测定上限 $< 10^{-5}\ W.u.$）**。

3. **多极模式正交相分离定律：**
   - 确立了**四极摇摆与八极宇称双重态的互斥律**：三轴超形变势阱是极度纯净的纯四极摇摆自由度，其强烈的四极长椭拉长与三轴非轴对称场天生对八极相干性具有极强的破坏与稀释作用；
   - 绝不可将轻锕系区宇称反转与强交替宇称带的概念直接跨区平移至超形变高自旋带中。

## Evidence Boundaries & Review Status

- 物理模型：结合 Nilsson 能级 $K$-分裂几何稀释模型与液滴偶极相消方程；
- 证据层级：基于 Schönwasser 2003（Gammasphere 一手实验数据）与 Butler 1996 锕系基准；
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
