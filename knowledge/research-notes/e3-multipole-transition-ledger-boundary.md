---
type: research-note
title: "跨核 E3 多跃迁账本与和规则边界"
aliases: [E3 multipole transition ledger, Day26 E3 unit and degeneracy audit]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [butler-2020-222-228ra-octupole-evolution, bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole, gaffney-2013-pear-shaped-rn-ra]
created_from: Day26 E3 transition ledger and 027 partial-sum audit
promotion_target: octupole-and-rare-electromagnetic-decay
tags: [octupole, E3, transition-matrix, Q3, sum-rule, evidence-gradient]
---

# 跨核 E3 多跃迁账本与和规则边界

## Research Trigger

027 的平方和把不同初始自旋的 Butler E3 行放在一起，并将首列自旋作为 B(E3) 简并因子，不能当作 (0^+) 闭合和。新账本逐条保留矩阵元、单位、转子 (Q_3)、星号耦合和 locator，明确哪些可比较、哪些不能相加。

## Grounded Evidence

`144Ba` 的 `0+↔3−` 矩阵元为 `0.65(+0.17/−0.23) e b^(3/2)`、向下 `B(E3)=48(+25/−34) W.u.`，转子约定下 `Q3=1.73(+0.45/−0.62)×10^3 e fm^3`（Bucher 2016 PDF p.4 Table I/text）。`146Ba` 对应中心值为 `0.65(+0.14/−0.20) e b^(3/2)`、`48(+21/−29) W.u.`（Bucher 2017 PDF p.3 Table I/text）。

Gaffney 2013 PDF p.3 Table 1 给 `220Rn` 的 `0+↔3−` E3 矩阵元 `810(50) e fm^3`、`B=33(4) W.u.`，给 `224Ra` `940(30) e fm^3`、`B=42(3) W.u.`；PDF p.4 Table 2 给相应 `Q3=2180(130)` 和 `2520(90) e fm^3`。`940(30)` 是约化矩阵元，不能与 `Q3=2520(90)` 混作同一量。

Butler 2020 PDF p.3 Table I 给 `222Ra` `0+→3−=1.13(9)`、`Q3=3030(240)` 和旋转模型聚合 `Q3=3120(190)`；`228Ra` 为 `0.87(15)`、`2300(400)` 和 `2230(290)`。同表 `222Ra` 的高自旋 E3 行中 `4+→1−`, `4+→3−`, `4+→5−`, `4+→7−` 标星；`228Ra` 的 `2+→1−`, `2+→3−`, `2+→5−`, `4+→1−` 标星。原文 p.3 说明标星矩阵元通过旋转关系与更高阶矩阵元耦合，因而不是完全独立。

## Provisional Reasoning

### 单位与简并因子

`e b^(3/2)` 转为 `e fm^3` 的因子为 (1000)。对实际初态 (J_i)，

$$B(E3;J_i\to J_f)=|M_{fi}|^2/(2J_i+1).$$

但表格的 bra-ket 行向和正文的箭头必须先核对；不要仅按视觉上的第一列自旋套分母。对 `0+↔3−`，同一个约化矩阵元的向上/向下 B 相差 (2J+1=7)；因此 `B(E3;3−→0+)` 与 `B(E3;0+→3−)` 不能混写。跨不同 (J_i) 的矩阵元平方也不能直接组成一个 (0^+) 的和规则。

### 非能权和的正确对象

完整 (0^+) 闭合和为

$$m_0(E3;0^+)=\sum_f B(E3;0^+\to3^-_f).$$

单一已测 `0+→3−` 只贡献其中一个非负项，是下界候选；表列 `2+`、`4+` 行属于不同初态闭合关系。能量加权和 (m_1=\frac12\langle0|[M^\dagger,[H,M]]|0\rangle) 还需要哈密顿量或完整能级/矩阵元网络，本账本未计算。

### 证据梯度

从单条 Ba E3 到 Gaffney 的 `Rn/Ra` 多条矩阵元，再到 Butler 的 `222/228Ra` 星号标注网络，信息量逐步增加。多条转子换算 (Q_3) 的近似恒定可检验 rotor-like 一致性；`228Ra` 特定近零链提供振动图样反证。它们仍受 GOSIA 耦合、相位、配对、未观测高态和转子转换约定影响，不能转成无模型静态密度或形状概率。

## Assumptions

账本只使用已归档 source 页面和其中明确 locator 的中心值。不同实验的系统误差不合并；星号项不当作独立样本；未从打印区间反演新的协方差或置信度。

## Competing Explanations

近恒定 (Q_3) 可支持静态局域反射不对称，也可能由旋转耦合和有限态空间模拟；近零 E3 链支持八极振动图样，但不排除组态混合、对齐八极声子或未观测通道。单一大 E3 不足以在这些解释间作排他判决。

## Transfer Conditions

跨核比较必须统一 E3 单位、跃迁方向、初态简并因子、轴对称 (Q_3) 转换和星号耦合状态。Ba 的单条 E3 不能直接套用 Butler 的多跃迁平坦度判据。

## Failure Conditions

若把不同初态矩阵元平方相加、把表中矩阵元和 (Q_3) 混作同一量，或把旋转耦合项当独立实验，账本会产生虚假的 sum rule 或统计显著性。

## Falsification or Reverse Tests

对每一条跃迁重新核对 bra-ket 方向和 (2J_i+1) 分母；释放 Butler 星号耦合并使用完整协方差，检验近恒定 (Q_3) 是否仍成立。若释放耦合后平坦度消失，静态解释应降级为模型条件结果。

## Open Questions

能否取得完整 `0+` 到所有 `3−` 的高能 E3 强度及协方差，从而给出真正的 (m_0)？能否用同一相位约定和 Hamiltonian 计算 (m_1)？Ba 是否有足够多的独立 E3 链进行同样检验？

## Human Review

本页是 Codex 对已归档 source 和 027 工件的 self-audit，`review_status: unreviewed`；未发生用户人工审核。

## Promotion or Rejection History

2026-10-28：建立 provisional 账本边界；待完整多态网络和协方差取得后再评估晋升。
