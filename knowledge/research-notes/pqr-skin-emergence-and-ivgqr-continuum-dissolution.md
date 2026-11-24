---
type: research-note
title: "锡链低能四极响应与镍链参数化练习的证据边界"
aliases: [pqr-skin-emergence-and-ivgqr-continuum-dissolution, PQR neutron skin IVGQR damping, Day27 PQR]
created: 2026-10-30
updated: 2026-11-22
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [tsoneva-2011-pqr-skin-nuclei]
created_from: Day 27 continuation study; system/scripts/day27_pqr_skin_and_ivgqr_damping_study.py
tags: [pygmy-quadrupole-resonance, neutron-skin, ISGQR, IVGQR, Landau-damping, 58Ni, 68Ni, 78Ni, Day27]
---

# 锡链低能四极响应与镍链参数化练习的证据边界

## Research Trigger

要判断低能 E2 强度是否由核皮层振动承载，需要比较分质子、中子跃迁密度、强度能区和亚壳演化。跨同位素链迁移还需要独立的核素与反应证据。

## Grounded Evidence

[[tsoneva-2011-pqr-skin-nuclei]] 扫描核定的是 `104–134Sn` 的 HFB–QPM/QRPA 理论研究。刊版 pp.176–178 Figs. 2–5 比较集体 `2+_1` 以上的低能簇、等标量和等矢量响应，以及随能区变化的径向跃迁密度。p.179 讨论皮层核子主导、表面位置和弥散度变化，以及双幻 `132Sn` 的模型例外。Fig. 1 引用实验 `2+_1` 结果作低能核谱约束。

## Evidence Boundaries & Review Status

旧 Day 27 练习对 `58,68,78Ni` 设置经验质量标度、皮厚公式、强度阈值与立方宽度函数。脚本中的观测标志是预设输入，自检比对的是这些公式的阈值。其结果保留在历史工件，镍链 EWSR 份额、线宽、径向节点和所谓完全溶解均撤回为来源结论。原件提供锡链理论背景，镍链的相关实验、四极强度及连续谱模型仍需要各自的直接来源。

## Provisional Reasoning

锡链的皮层解释来自所用多体模型。镍链参数化练习只说明所选公式的行为。

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
| 2026-11-22 | publisher original reconciled | provisional nickel assignment | source attribution withdrawn | archived article studies the tin chain; nickel script is parameterized |
