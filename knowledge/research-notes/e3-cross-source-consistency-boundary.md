---
type: research-note
title: "Day26 E3 跨来源一致性与剩余边界"
aliases: [E3 cross-source consistency, Day26 E3 convergence audit 038]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole, bernard-2016-144ba-sccm-octupole, gaffney-2013-pear-shaped-rn-ra, butler-2020-222-228ra-octupole-evolution]
created_from: Day26 read-only cross-source and artifact consistency audit 038
promotion_target: octupole-and-rare-electromagnetic-decay
tags: [octupole, E3, consistency, evidence-boundary, sum-rule]
---

# Day26 E3 跨来源一致性与剩余边界

## Research Trigger

Day26 已产生多个 E3 账本和模型工件，需要确认单位、误差、跃迁方向、初态简并、星号耦合和“近常数”措辞没有互相冲突。本页只记录收敛审计，不新增实验事实。

## Grounded Evidence

已审计 source：Bucher 2016/2017、Bernard 2016、Gaffney 2013、Butler 2020；已审计 artifact：018、027、029、032、035。Bucher/Butler 的 E3 矩阵元用 (e b^{3/2})，Gaffney 用 (e fm^3)；(1b^{3/2}=1000fm^3)。Gaffney `940(30)` 是 E3 约化矩阵元，`2520(90)` 是 (Q_3)。Bernard `0.460/25 W.u.` 是模型计算，不与 Bucher 的实验值冲突。Butler 星号项确实是旋转耦合项，非完全独立。

## Provisional Reasoning

### 方向与简并

(B(E3;J_i\to J_f)=|M|^2/(2J_i+1))。035 按打印箭头给出条件正向/反向 B；029/035 明确 027 的首列分母代理不能当认证 B 和。不同 (J_i) 的矩阵元不能相加成 (0^+) closure；单条 (0^+\to3^-) 只对应其自身闭合和的一项。

### Butler 图样

`228Ra 2+→3−` 的中心和一标准差区间跨零，未做新拟合。`222Ra` 的“Q3 近常数”是 Butler Fig.4 和作者文字中的 rotor-like 解释；表中无星号值仍有约 `2000–3100 e fm³` 散布，星号项延伸到更大值并受耦合，因此不能写成精确或独立统计恒定。

### 018 逻辑边界

018 已补入 E1/E3 联立解 (R=219.84fm,w=4.46\times10^{-5})。因此“单一未极化通道无法同时解释”只在核尺度局域 (R) 与共同跃迁权重的条件下成立；(w) 不等于 (S_\alpha)。

## Assumptions

一致性审计使用各 source/ledger 的打印中心值和已声明约定，不恢复 GOSIA covariance，不释放星号耦合，不把不同实验误差合并。

## Competing Explanations

静态梨形、动态八极振动、对齐八极声子、组态混合和模型耦合都仍可解释部分 E3 图样。单位和简并因子一致不构成结构解释的排他证据。

## Transfer Conditions

跨核使用前必须重新核对单位、bra-ket 方向、初态自旋、星号耦合和 (Q_3) 转换。Ba 单条 E3 不可直接迁移 Butler 多跃迁平坦度判据。

## Failure Conditions

将 (M^2) 当作所有方向相同的 B、将部分平方和当完整 closure、将 Gaffney 的矩阵元当 (Q_3)，或将 Butler 的质量解释写成独立统计认证，都会越过证据边界。

## Falsification or Reverse Tests

释放 Butler 星号项并使用联合 covariance；分别按固定 (J_i) 重建 B 和 closure。对 018 的点团簇模型限制 (R) 在核尺度范围内，并由独立通道观测约束共同权重。

## Open Questions

完整多态 E3 网络和 covariance 是否会改变 Q3 平坦度判断？能否获得真正的 (0^+) closure (m_0) 与 energy-weighted (m_1)？

## Human Review

本页是 Codex read-only self-audit，`review_status: unreviewed`；无用户人工审核。

## Promotion or Rejection History

2026-10-28：建立 provisional 跨来源一致性边界；无 fatal contradiction，保留上述开放问题。
