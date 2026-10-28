---
type: research-note
title: "Butler 2020 E1/E2/E3 单位、相位与多跃迁边界"
aliases: [Butler E1 E3 ledger, Day26 Butler 032]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [butler-2020-222-228ra-octupole-evolution]
created_from: Day26 Butler Table I/II unit and direction audit
promotion_target: octupole-and-rare-electromagnetic-decay
tags: [octupole, E1, E2, E3, Q3, phase-convention, GOSIA]
---

# Butler 2020 E1/E2/E3 单位、相位与多跃迁边界

## Research Trigger

Butler 2020 的正文 Table I 与 arXiv 附加 Table II 同时给出 E1、E2、E3 矩阵元、内禀矩和星号耦合。需要把拟合矩阵元、转子派生量、初态简并因子和相位约定分开，避免把有量纲的 E3/E1 比写成无量纲强度或把 Q3 近似恒定夸大为严格统计结论。

## Grounded Evidence

PRL PDF p.3 Table I 的单位表头为 (e b^{\lambda/2})，即 E2 为 (e b)、E3 为 (e b^{3/2})；arXiv PDF p.16 Table II 的 E1 为 (e b^{1/2})，Q1 为 (e fm)。Table I 注释说明 E3 星号项与高阶矩阵元耦合；`222Ra` 的星号包括 `4+→1−`, `4+→3−`, `4+→5−`, `4+→7−`，`228Ra` 的星号包括 `2+→1−`, `2+→3−`, `2+→5−`, `4+→1−`。Table II 注释说明 E1 符号依据 (Q_1/Q_3) 相对符号的旋转模型假设。

`228Ra 2+→3−` E3 中心为 (-0.06^{+0.23}_{-0.16},e b^{3/2})，打印一标准差区间为 ([-0.22,0.17])，跨过零；对应 (Q_3=150^{+360}_{-500},e fm^3) 区间也跨零。该检查使用打印区间，不做新拟合。

## Provisional Reasoning

### 有量纲 E3/E1 比

因为 (b^{3/2}/b^{1/2}=b)，同一状态对的中心值比 (M(E3)/M(E1)) 单位为 (b)。例如 `222Ra 2+→1−` 为 (0.85/(-0.0114)=-74.56,b)，`228Ra 2+→3−` 为 ((-0.06)/(-0.009)=6.67,b)。这些是矩阵元幅度比，不是 (B(E3)/B(E1))；若要比较 B，还需各自实际初态简并因子和单位平方。对于 `0+→3−` 与 `0+→1−` 的 ground-band scale 比，末态不同，不能称同一跃迁的多极比。

### 初态简并与星号

标准约定为 (B(E\lambda;J_i\to J_f)=|M_{fi}|^2/(2J_i+1))。Table 行的 bra-ket 方向必须结合正文箭头核对；不能把表中第一列自旋机械当 (J_i)。星号项通过旋转关系耦合，因此在做多跃迁统计或散布估计时应单独标注，不能把它们视为与无星号项独立抽样。

### 222Ra 的“近常数”边界

Butler PRL p.4 Fig.4 与文字称 `222,224,226Ra` 的 Q3 跨转换近似恒定；但 Table I 打印的 `222Ra` 每条 Q3 为 `3030, 2000, 2100, 3100, 4400, 5500, 3200, 4600 e fm³`，无星号前四条范围 `2000–3100`，星号项更高且受耦合。故“近常数”应保留为作者的 rotor-like 解释和图样层判断，不升级为所有中心值相等或独立统计检验。

## Assumptions

本笔记只使用 Butler 2020 已归档正文与 arXiv 附加 Table II 的打印中心和不对称区间；E1 符号沿用作者的旋转模型相位约定。没有重建 GOSIA 协方差、释放星号耦合或重新拟合。

## Competing Explanations

近零 E3 可支持八极振动图样，也可能受态混合、相位、有限灵敏度或耦合参数影响；多条 Q3 近似恒定支持静态梨形的 rotor-like 描述，但配对、对齐八极声子与模型约束仍是竞争解释。E1/E3 幅度比本身不选择这些机制。

## Transfer Conditions

跨核比较须统一 E1/E2/E3 单位、跃迁方向、初态简并、相位约定、星号耦合和 Q 转换。不能把 `228Ra` 近零中心直接当精确零，也不能把 `222Ra` 的 Q3 散布当独立样本方差。

## Failure Conditions

若将 (M(E3)/M(E1)) 当无量纲、把幅度比当 B 比、忽略 (2J_i+1)、或把星号项当独立测量，结论会产生单位和统计错误。

## Falsification or Reverse Tests

释放所有星号耦合并使用联合协方差，重新检验 `222Ra` 的 Q3 平坦度；对 `228Ra 2+→3−` 取得更高灵敏度和独立相位约束，检验其区间是否仍跨零。若 E1 符号改变，所有 signed E3/E1 比需重算，绝对值比也须保留单位 (b)。

## Open Questions

完整 GOSIA covariance 是否会改变近常数 Q3 的统计判断？`228Ra` 近零 E3 的显著性在释放耦合后是多少？能否取得同一初态和相位约定下的绝对 E1/E3 联合矩阵元？

## Human Review

本页为 Codex 基于 Butler 正文与附加 Table II 的 self-audit，`review_status: unreviewed`；没有用户人工审核记录。

## Promotion or Rejection History

2026-10-28：建立 provisional 单位和可辨识性边界；待协方差和释放耦合分析后再评估晋升。
