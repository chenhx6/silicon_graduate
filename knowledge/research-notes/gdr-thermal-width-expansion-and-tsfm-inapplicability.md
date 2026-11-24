---
type: research-note
title: "巨偶极共振（GDR）热展宽相变与TSFM模型跨区不适用性：配对塌缩临界温度对决双幻核208Pb碰撞阻尼刚性"
aliases: [gdr-thermal-width-expansion-and-tsfm-inapplicability, GDR thermal width expansion TSFM, Day27 GDR thermal width]
created: 2026-10-30
updated: 2026-11-22
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [pandit-2012-gdr-thermal-width-critical-behavior]
created_from: Day 27 continuation study; system/scripts/day27_gdr_thermal_width_tsfm_study.py
tags: [giant-dipole-resonance, thermal-width, shape-fluctuations, TSFM, pairing-collapse, 119Sb, 120Sn, 208Pb, Day27]
---

# 巨偶极共振（GDR）热展宽相变与 TSFM 模型跨区不适用性：配对塌缩临界温度对决双幻核 208Pb 碰撞阻尼刚性

## Research Trigger

比较热 GDR 宽度随温度和自旋的变化，并检验模型能否跨核素外推。

## Grounded Evidence

[[pandit-2012-gdr-thermal-width-critical-behavior]] PDF2–3 报告 201Tl 和 63Cu 的谱拟合宽度，119Sb、120Sn、208Pb 的点来自以前的实验。PDF4 Fig. 3 把热形变涨落与 GDR 诱发形变比较，Eq. (1) 用经验 \(T_c(A)\) 描述低温平台。PDF5 留有对该机制的进一步检验需求。

## Evidence Boundaries & Review Status

Day 27 的 `system/scripts/day27_gdr_thermal_width_tsfm_study.py` 是历史模型练习。先前本页把计算中指定的配对隙、势能面刚度和碰撞展宽归成 Pandit 原文确立的实验机制。2026-11-22 回源后撤回这项归属。继续用该工件时应查脚本的独立输入和原件，区分模型结果与谱拟合结果。

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
