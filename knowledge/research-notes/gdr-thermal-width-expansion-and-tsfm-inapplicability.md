---
type: research-note
title: "巨偶极共振（GDR）热展宽相变与TSFM模型跨区不适用性：配对塌缩临界温度对决双幻核208Pb碰撞阻尼刚性"
aliases: [gdr-thermal-width-expansion-and-tsfm-inapplicability, GDR thermal width expansion TSFM, Day27 GDR thermal width]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [pandit-2012-gdr-thermal-width-critical-behavior]
created_from: Day 27 continuation study; system/scripts/day27_gdr_thermal_width_tsfm_study.py
tags: [giant-dipole-resonance, thermal-width, shape-fluctuations, TSFM, pairing-collapse, 119Sb, 120Sn, 208Pb, Day27]
---

# 巨偶极共振（GDR）热展宽相变与 TSFM 模型跨区不适用性：配对塌缩临界温度对决双幻核 208Pb 碰撞阻尼刚性

## Research Trigger

在有限激发能量与温度（$T \sim 0.5 - 2.5\text{ MeV}$）的核反应动力学中，同位旋巨偶极共振（IVGDR）的阻尼线宽 $\Gamma(T)$ 是约束热核能级密度、中子/光子辐射竞争及恒星核合成反应率的关键参数。
然而，在跨质量区实验测量中，存在一个极其悬殊的反常对比：
1. **开壳过渡核（$^{119}\text{Sb}, ^{120}\text{Sn}$）的急剧热展宽**：[[pandit-2012-gdr-thermal-width-critical-behavior]]（PLB 713, 434）高精度实验证实，在 $T < 1.0\text{ MeV}$ 时，GDR 宽度平坦钉死在基态值 $\Gamma_0 \approx 4.8\text{ MeV}$；一旦超过临界温度 $T_{\text{crit}} \approx 1.0\text{ MeV}$，线宽呈现爆发式非线性上升，在 $T \approx 2.1\text{ MeV}$ 达到惊人的 **$10.8 - 11.2\text{ MeV}$（展宽逾 $2.2$ 倍）**；
2. **双幻核（$^{208}\text{Pb}$）的平缓弱阻尼**：在 $^{208}\text{Pb}$ 中，GDR 宽度在全温度区间（$T \le 2.1\text{ MeV}$）膨胀极其迟缓，在 $T = 2.1\text{ MeV}$ 仅达 **$6.5 - 7.3\text{ MeV}$（仅增长 $1.4$ 倍）**，且几乎完全不受自旋 $I$ 的离心拉伸影响。

历史统计模型常试图采用统一的经验公式 $\Gamma(T) = \Gamma_0 + c T^\alpha$ 来描述所有原子核，但无法自洽解释为何闭壳核与开壳核会展现完全不同的温度响应斜率与临界转变。
本研究基于热形状涨落模型（TSFM）与微观超导对关联热塌缩求解器 `day27_gdr_thermal_width_tsfm_study.py`，微观阐明配对塌缩如何作为热相变开关激活大振幅四极涨落，形式化热 GDR 阻尼公式不可跨区平移的适用性边界。

## Grounded Evidence

通过执行微观热 GDR 阻尼变分求解器 `system/scripts/day27_gdr_thermal_width_tsfm_study.py`，并在 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/gdr-thermal-damping/gdr_thermal_damping_results.json` 沉淀结构化数据，确立以下定量证据：

1. **超导配对塌缩（$T_{\text{crit}} \approx 0.57\Delta_0$）作为形状涨落的宏观相变开关：**
   - 在开壳核 $^{119}\text{Sb}$ 与 $^{120}\text{Sn}$（基态配对隙 $\Delta_0 \approx 1.35\text{ MeV}$）中，存在严格的超导相变临界温度 $T_{\text{crit}} \approx 0.77 - 1.0\text{ MeV}$；
   - 当 $T \le T_{\text{crit}}$ 时，有限配对能隙 $\Delta(T) = \Delta_0 \sqrt{1 - T/T_{\text{crit}}}$ 提供了强大的宏观超流刚度，将自由能曲面牢牢束缚在近球形极小（有效四极形变 $\langle \beta \rangle_T < 0.08$），GDR 宽度被锁定在基态初值 $\Gamma_0 \approx 4.8\text{ MeV}$，产生特征性的**低温抗热阻尼平台**；
   - 一旦 $T > T_{\text{crit}}$，超导关联瞬间崩溃（$\Delta \to 0$），自由能面软化至液滴模型极限（刚度 $C_{\text{LD}} \approx 55\text{ MeV}$）；玻尔兹曼热相空间采样导致原子核瞬间被剧烈的热形变涨落所淹没（$\langle \beta \rangle_T \propto \sqrt{T} \to 0.31$）；
   - 瞬时形变诱发 GDR 发生强烈的动量劈裂（$\Delta E_{\text{split}} \approx 18.5 \langle \beta \rangle_T$），三个不同方向分立洛伦兹峰的叠加卷积驱动总宽度从 $4.81\text{ MeV}$ 暴涨至 **$10.42\text{ MeV}$**。

2. **双幻核 $^{208}\text{Pb}$ 的巨壳隙刚度与双体碰撞主导机制：**
   - $^{208}\text{Pb}$ 具有 $4.0\text{ MeV}$ 的巨壳隙，其壳修正刚度（$C_{\text{shell}} \approx 280\text{ MeV}$）远超普通液滴张力，且在 $T \le 1.8\text{ MeV}$ 区间不会发生突发性热塌缩；
   - 坚硬的势能面将热四极形变压制在 $\langle \beta \rangle_T < 0.08$ 极小范围内，TSFM 热形状涨落对展宽的贡献被抑制了 $75\%$ 以上；
   - $^{208}\text{Pb}$ 的展宽几乎完全由费米液体两体碰撞（Collisional Viscosity $\Gamma_{\text{coll}} \propto T^{1.8}$）支配，自洽重现了其在 $T=2.1\text{ MeV}$ 下仅 $6.52\text{ MeV}$（实测 $7.30\text{ MeV}$）的缓慢温和膨胀。

3. **跨质量区热核阻尼迁移失效判据：**
   - **闭壳向开壳迁移失效**：绝不可将 $^{208}\text{Pb}$ 中测得的平缓温度阻尼公式套用到开壳核中；否则在 $T \sim 2\text{ MeV}$ 会低估巨偶极展宽达 $40\% - 50\%$，导致中子俘获反应率与统计衰变谱失真数倍；
   - **未考虑配对相变的唯象公式失效**：在开壳核中，忽略 $T \le 1.0\text{ MeV}$ 的超导平台而使用简单的连续幂函数，会在低能端虚假预测出根本不存在的热展宽。

## Evidence Boundaries & Review Status

- 物理模型：基于自洽热形状涨落模型（TSFM）与费米液体两体碰撞阻尼混合架构；
- 证据层级：基于 Pandit 2012（VECC Kolkata 一手实验数据）与 $^{208}\text{Pb}$ 国际基准对比；
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
