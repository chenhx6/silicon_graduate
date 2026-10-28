---
type: research-note
title: "奇 A 宇称伙伴能量窗与带标签边界"
aliases: [parity doublet energy window boundary, odd-A nearest-level pairing trap]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [nndc-2009-ra225-adopted-parity-doublet, nndc-2022-ac225-adopted-parity-doublet]
created_from: Day26 unit036 energy-window candidate audit
promotion_target: octupole-correlation
tags: [octupole, parity-doublet, odd-A, energy-window, band-assignment, evidence-boundary]
---

# 奇 A 宇称伙伴能量窗与带标签边界

## Research Trigger

最近异宇称能级经常被误读为宇称双重态。对 $^{225}$Ra/$^{225}$Ac 已归档评价能级施加 50、100、200 keV 能量窗，量化候选数如何随窗宽膨胀，并检查 A–D 带标签能否真正选出配对。

## Grounded Evidence

输入为 Unit030 的固定栏 ENSDF level 列表：Ra `225088001`、Ac `225089001`。算法对相同数值 $J$ 的所有 $J^-$–$J^+$ Cartesian pairs 计算 $|E_-−E_+|$，保留在窗口内的全部组合。50/100/200 keV 候选数分别为：Ra 3/8/15，Ac 6/9/11。带标签完整候选计数仅排除 `?` 标签，不等于实验带连接证明。

## Provisional Reasoning

能量窗由 50 keV 放宽至 200 keV 时，Ra 候选数增加五倍，Ac 增加约 1.8 倍；这种增长来自多个同自旋状态和不同带的笛卡尔组合。Ra 的 5/2 D–E 组合仅差 23.95 keV，但不能替代低能 A/B；Ac 的 5/2 A–B 与 C–D 分别差 34.78 和 34.83 keV，最近值几乎无法选带。故最近能级算法只能输出诊断排序，不能选择物理双重带。

## Assumptions

只使用评价表给出的数值 J、宇称、能量和带标签；不引入未列的带连接、寿命或波函数。窗口端点采用闭区间 $|\Delta E|\le W$。

## Competing Explanations

近简并可能来自静态反射不对称、八极振动、粒子–芯耦合、Coriolis 混合或偶然能级靠近。不同带的相同 Jπ 也可能由不同 Nilsson 轨道或组态混合产生。

## Transfer Conditions

能量窗计数可迁移为数据审计方法；具体窗口大小、带标签可信度、Jπ 确定性和近简并解释不能跨核素直接迁移。

## Failure Conditions

若把最近 pair 当作唯一物理 pair、把带标签当作波函数重叠证明，或对 200-keV 候选列表只报告最小差值，审计会产生选择偏差。若忽略括号 Jπ 和未分配带，候选数也不再可追溯。

## Falsification or Reverse Tests

用原实验的 γ–γ 连接、寿命、E1/E2/E3 分支和组态指认逐一淘汰 Cartesian candidates；若唯一保留的 pair 仍无法同时重现电磁观测量，则最近能级假说被反驳。

## Open Questions

两核是否有足够的原实验带连接和微观波函数信息，能把 50-keV 内候选从评价 level list 晋升为同构型宇称双重态？当前资料不足。

## Human Review

本页为 Codex source self-audit，保持 unreviewed；候选计数不提升为实验或模型认证。

## Promotion or Rejection History

2026-10-28：建立 50/100/200-keV 窗口计数，记录最近能级误导示例和 A–D 带标签约束边界。

## Next Actions

获取原始 γ–γ/寿命资料，建立带成员连接图后再对候选 pair 做物理筛选。

## Sources

- [[nndc-2009-ra225-adopted-parity-doublet]]
- [[nndc-2022-ac225-adopted-parity-doublet]]
- `parity-doublet-energy-window-036.json`（本单元逐候选输出）
