---
type: research-note
title: "110Cd 分支归一化与 Roy B(E2) 中心值边界"
aliases: [Cd110 branch normalization boundary, Day26 Cd branch audit]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [roy-2011-cd110-systematics-antimagnetic, nndc-2012-cd110-hi-xng]
created_from: Day26 fixed-column ENSDF branch audit
promotion_target: antimagnetic-rotation
tags: [110Cd, branch, feeding, normalization, evidence-boundary]
---

# 110Cd 分支归一化与 Roy B(E2) 中心值边界

## Research Trigger

Roy Table 1 的条件寿命公式反推值比打印 B(E2) 中心高约7–11%。新取得的 110048022 HI,XNG 固定栏对象提供了相对分支字段，可用于检查一个明确的分支选择情景。

## Grounded Evidence

18⁺、20⁺、24⁺评价块分别列1224.5、1323.0、1358.0-keV带内E2相对强度；在所读块中没有第二条评价分支。22⁺同时列1314.1-keV RI=2.7(1)和1100-keV RI=1.0(3)，条件分支份额为2.7/(2.7+1.0)=0.7297。评价注释明确 Roy未在符合门确认1100-keV线。原始字段与位置见 [[nndc-2012-cd110-hi-xng]]。

## Provisional Reasoning

如果把22⁺的1100-keV线纳入总分支，1314.1-keV线对应的分支加权强度会下降；但这只影响一个评价对象的条件换算。18⁺、20⁺、24⁺没有同样的第二条评价分支，故不能用22⁺情景解释全部Roy中心差异。不能把该份额直接乘到Roy的0.09(3)，因为Roy明确未确认该线。

## Assumptions

相对强度被当作同一评价块内可加的条件量；没有加入探测效率、内转换、未观测分支、feeding、side feeding或协方差。结果是算术场景，不是新 B(E2)。

## Competing Explanations

中心值差异还可能来自 Roy 的线形拟合、feeding设定、停止本领系统误差、分支选择或打印舍入；现有固定栏对象无法排序这些解释。

## Transfer Conditions

只有同一反应、门条件、分支列表和响应校准同时可得时，评价 RI 才能进入原始 LINESHAPE 重放；不能把评价分支迁移到不同门条件。

## Failure Conditions

若用22⁺1100-keV分支无条件覆盖Roy，或把相对RI当绝对布居/完整branch inventory，结论失效。

## Falsification or Reverse Tests

取得Roy逐门分支、side feeding和响应后，重算每个寿命的 branch-conversion factor；若18⁺、20⁺、24⁺也有未列分支且能统一解释7–11%，更新当前边界，否则保留归一化未定。

## Open Questions

Roy原始LINEShape输入、门控计数、分支选择和停止本领曲线是否存在公开附录或作者更正？评价对象的相对RI是否来自同一门条件？

## Human Review

本页为Codex self-audit，保持 `unreviewed`。

## Promotion or Rejection History

2026-10-28：建立条件分支账本；不修改Roy原表，不把1100-keV评价分支写成实验重放结果。
