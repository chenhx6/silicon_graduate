---
type: research-note
title: "E3 跃迁方向、初态简并因子与闭合和规则边界"
aliases: [E3 direction degeneracy audit, Day26 E3 B direction 035]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [butler-2020-222-228ra-octupole-evolution]
created_from: Day26 Butler Table I direction and degeneracy audit
promotion_target: octupole-and-rare-electromagnetic-decay
tags: [octupole, E3, B-transition, degeneracy, closure-boundary]
---

# E3 跃迁方向、初态简并因子与闭合和规则边界

## Research Trigger

Butler 2020 Table I 同时列出多个初始自旋的 E3 矩阵元。若把这些行直接平方相加，或不区分正向/反向 (B(E3)) 的初态简并因子，就会把不同闭合关系混成一个强度。此笔记只做方向和分母审计。

## Grounded Evidence

Butler PRL PDF p.3 Table I 的中心 E3 行及星号标记已在 [[butler-2020-222-228ra-octupole-evolution]] 和 029/032 账本中归档。单位为 (e,b^{3/2})。`222Ra` 的无星号行包括 `0+→3−`, `2+→1−`, `2+→3−`, `2+→5−`；星号行包括 `4+→1−`, `4+→3−`, `4+→5−`, `4+→7−`。`228Ra` 的 `0+→3−` 无星号，其他表列 E3 行带星号。

## Provisional Reasoning

对同一厄米多极算符，若约化矩阵元幅度相同，则

$$B(E3;J_i\to J_f)=\frac{|M|^2}{2J_i+1},\qquad B(E3;J_f\to J_i)=\frac{|M|^2}{2J_f+1}.$$

所以反向比为 ((2J_f+1)/(2J_i+1))。例如 `0+↔3−` 的 B 相差 7 倍；`2+↔1−` 的正向/反向比为 (3/5=0.6)；`2+↔3−` 为 (7/5=1.4)。这些是角动量定义关系，不是新的实验测量。

只有 (J_i=0) 的行可以进入 (0^+) 的非能权闭合和 (sum_fB(E3;0^+\to3^-_f))。`2+` 和 `4+` 行必须留在各自初态的和规则中，不能与 `0+` 行相加。星号行还受 GOSIA 旋转关系耦合，不能当独立样本。

## Assumptions

本审计采用 Butler 打印箭头作为条件方向；不依据表格字体单独重建实验衰变方向。只使用中心矩阵元，不恢复不对称误差、协方差或 W.u. 转换。

## Competing Explanations

方向换算的简并因子是定义层结果，不区分静态八极形状、动态振动或对齐声子。那些结构解释需多跃迁 (Q_3)、能级和模型耦合共同判断。

## Transfer Conditions

迁移到其他表格时必须重新核对 bra-ket 顺序、作者箭头、初态自旋和是否给出约化矩阵元。不能把一个文献的行方向默认套给另一个文献。

## Failure Conditions

将 (M^2) 当作所有方向相同的 B，或把不同 (J_i) 的 B 相加为单一 closure，会产生错误的强度和规则结论。

## Falsification or Reverse Tests

对每一行独立计算正向和反向分母，并验证比值 ((2J_f+1)/(2J_i+1))。再按固定初态分组检查闭合和；若混入其他 (J_i)，标记为非闭合部分和。

## Open Questions

完整 (0^+) 到所有 (3^-) 的 E3 强度是否可取得？星号耦合释放后，各初态的和规则协方差如何变化？

## Human Review

本页为 Codex 代数 self-audit，`review_status: unreviewed`；没有用户人工审核。

## Promotion or Rejection History

2026-10-28：建立 provisional 方向和简并因子边界。
