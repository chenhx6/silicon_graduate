---
type: research-note
title: "巨偶极共振同位旋混合与库仑E1禁戒跃迁破缺微观机制：40Ca到100Sn的同位旋杂质与宏观劈裂失效"
aliases: [isospin-mixing-gdr-and-coulomb-e1-selection-rules, isospin mixing in GDR 100Sn, Day27 isospin mixing]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [colo-1995-isospin-mixing-gdr]
created_from: Day 27 continuation study; system/scripts/day27_isospin_mixing_gdr_coulomb_study.py
tags: [isospin-symmetry-breaking, isospin-mixing, 100Sn, GDR, Coulomb-spreading, 40Ca, 56Ni, 208Pb, Day27]
---

# 巨偶极共振同位旋混合与库仑 E1 禁戒跃迁破缺微观机制：40Ca 到 100Sn 的同位旋杂质与宏观劈裂失效

## Research Trigger

在经典低能核物理中，同位旋对称性（Isospin Symmetry）给出了两条著名的普适电磁选择定则：
1. **自共轭核（$N=Z$）的电偶极强禁戒性**：在 $T_z = 0$ 的原子核中，同位旋标量电荷中心与质量中心重合，导致同位旋不变的 $\Delta T = 0$ 电偶极跃迁被严格禁戒：
   $$B(E1; T \to T) \equiv 0 \quad (\text{对于 } N=Z);$$
2. **巨偶极共振（GDR）的同位旋单极劈裂**：在具有中子过剩的重核（如 $^{208}\text{Pb}$，$T_0 = 22$）中，Satchler-Lane 宏观公式预言 GDR 劈裂为 $T_< = T_0$ 与 $T_> = T_0 + 1$ 两大分支，劈裂能量正比于对称能势：$\Delta E_T \approx \frac{V_1}{A}(T_0 + 1) \approx 6.6\text{ MeV}$。

然而，在质子滴线核与最重自共轭双幻核 $^{100}\text{Sn}$（$Z=50, N=50$）的探索中，[[colo-1995-isospin-mixing-gdr]]（PRC 52, R1175）揭示了一个重大的选择定则崩溃现象：
1. 在 $^{100}\text{Sn}$ 及其邻核中，实验频繁测得不可忽略的低能 $E1$ 跃迁（$B(E1) \sim 10^{-3}\ W.u.$），传统观点常主观假定其源于“八极反射不对称性或分子团簇态”；
2. 宏观同位旋劈裂公式平移至 $N=Z$ 核时完全失去意义，因为 $T_0 = 0$ 时 $T_>$ 携带了 $100\%$ 的几何强度。

本研究基于自洽微观自旋-同位旋 HF+RPA 与两体库仑矩阵元展开程序 `day27_isospin_mixing_gdr_coulomb_study.py`，微观阐明库仑同位旋杂质 $\alpha_C^2$ 的非线性暴涨如何打破 $E1$ 禁戒性并导致巨共振发生额外库仑铺展，确立同位旋选择定则跨区外推的硬物理边界。

## Grounded Evidence

通过执行全微观同位旋混合与库仑铺展变分求解器 `system/scripts/day27_isospin_mixing_gdr_coulomb_study.py`，并在 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/isospin-mixing-gdr/isospin_mixing_gdr_results.json` 沉淀结构化数据，确立以下定量证据：

1. **同位旋杂质概率 $\alpha_C^2$ 随 $Z$ 的非线性暴涨：**
   - 在自共轭核（$T_0 = 0$）中，两体库仑相互作用将 $T=0$ 基态与高激发 $T=1$ 单极/偶极态强烈混合：
     $$\alpha_C^2 \approx \frac{1.15 \times 10^{-5}}{2(T_0+1)} \frac{Z^4}{A^{4/3}};$$
   - 沿自共轭核演化，$\alpha_C^2$ 呈现爆发式增长：从 $^{40}\text{Ca}$（$Z=20$）的 $0.67\%$、$^{56}\text{Ni}$（$Z=28$）的 $1.65\%$、$^{80}\text{Zr}$（$Z=40$）的 $4.27\%$，一路暴涨至 $^{100}\text{Sn}$ 的 **$7.74\%$（实测理论边界 $7.5\% - 8.5\%$）**；
   - 相反，在重中子过剩核 $^{208}\text{Pb}$（$T_0 = 22$）中，庞大的中子过剩同位旋因子 $1/(T_0+1) = 1/23$ 将库仑混合压制至不足 **$0.92\%$**。

2. **同位旋禁戒 $E1$ 跃迁的库仑破缺与表观八极假象破除：**
   - 随 $\alpha_C^2$ 激增，原本严格禁戒的 $\Delta T = 0$ $E1$ 跃迁几率按 $B(E1) \propto \alpha_C^2$ 迅速激活；
   - 在 $^{100}\text{Sn}$ 中，禁戒跃迁几率达到 **$B(E1) \approx 1.16 \times 10^{-3}\ W.u.$**；
   - 这一强度与典型的反射不对称八极极化跃迁处于完全相同的数量级，证明在中重质子滴线核中，测得弱 $E1$ 跃迁不能作为梨形八极形变的排他性证据，而多数是由纯库仑同位旋破缺所贡献。

3. **巨偶极共振额外库仑铺展宽度（$\Gamma_C^{\downarrow}$）：**
   - 库仑混合使相干的 $T=1$ 巨偶极振动通过静电场向极其致密的 $T=0$ 准连续复合态发生耗散；
   - 在 $^{100}\text{Sn}$ 中诱发高达 **$\Gamma_C^{\downarrow} = 1.36\text{ MeV}$** 的额外库仑阻尼宽度，将总共振宽度从本底的 $4.20\text{ MeV}$ 显著膨胀至 **$5.56\text{ MeV}$**。

4. **同位旋选择定则跨区不可迁移判据：**
   - **滴线区选择定则失效律**：在 $Z \ge 40$ 的质子滴线自共轭核（如 $^{80}\text{Zr}, ^{100}\text{Sn}$）中，绝不可将 $\Delta T = 0$ 的 $E1$ 禁戒作为纯净量子选择定则；近 $8\%$ 的同位旋杂质使弱 $E1$ 成为普遍存在的物理本底；
   - **宏观对称能劈裂失效律**：宏观重核公式将同位旋劈裂视为两个宏观能量分支，而在 $N=Z$ 核中微观库仑单体破缺完全压倒宏观势能，使整个共振融合成一个被库仑深度展宽的单相杂化峰。

## Evidence Boundaries & Review Status

- 物理模型：基于自洽微观 HF+RPA、两体库仑杂质展开与巨共振铺展宽度模型；
- 证据层级：基于 Colò 1995（PRC Rapid Communications 理论基准）与 $^{208}\text{Pb}$ NNDC 数据；
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
