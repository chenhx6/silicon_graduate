---
type: concept
title: "巨共振同位旋分支：几何系数与动力学强度分开"
aliases: [同位旋分支与Lane势边界]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [isospin, giant-resonance, lane-potential, model-boundary]
---

# 巨共振同位旋分支：几何系数与动力学强度分开

## Definition

在近似同位旋守恒、基态 T=Tz=(N−Z)/2≥0，且作用为 q=0 的秩一同位旋算符时，角动量加法允许 T'=T 或 T+1；T−1 被 M=T 的下限排除。若 T=0，则**只允许 T'=1**，不能说 N=Z 核一定有两条等强度分支。

## Necessary Assumptions

把同位旋秩、末态同位旋变化量和电磁多极阶数分开：秩一算符不等于每个跃迁必有 ΔT=1。真实核还可能有库仑混合。光核 q=0 响应、核子散射中 t=1/2 弹核耦合与电荷交换 q=±1 不是同一套分支。

Wigner–Eckart 关系包含几何 Clebsch–Gordan 系数，也包含不同末态的**约化矩阵元及其规范因子**。只知道几何系数，不能得到全部巨共振的实验强度百分比。

## Discriminating Observables

需识别对应激发算符、基态/末态同位旋、各通道实验截面、对其它多极分量的分解及模型输运因素。要提取 Lane 势，须声明光学势中系数及 t·T 的规范，不能将约定不同的 V1 数值直接互换。

## Supporting Evidence

同位旋三角条件与 q=0 加法是代数重构。[[book-bohr-mottelson-nuclear-structure]] 第一卷对称性/角动量附录是后续逐式学习入口，但本轮未读完这些附录，具体巨共振动力学数值没有获得原式核验，`needs_review: true`。

此前程序用人为给定的 V1 和经验质心，先假设高分支份额 1/(T+1)，再倒推出峰位。该程序输出的“Pb 高分支 4.3%、能差 7.19 MeV”是这套假设的结果，不是测量，也不是由泡利阻塞独立算得。其声称的修正强度比甚至未被实现，不能当作定量微观证据。

## Counter-evidence and Competing Interpretations

旧推导先定义 t=1/2，再把末态写为 T 与 T+1，混淆了 t=1/2 散射耦合的 T±1/2 和秩一激发的 T、T+1。与此同时，同位旋守恒的相互作用本来就可以令不同总 T 有不同能量；出现同位旋分支能差不自动证明电荷无关性破缺。

## Our Current Position

撤回原“Lane 劈裂定理给出无模型精确峰位和分支比”的认证。`isg` 只可作为带明示边界的历史示意参数化；实际强度/峰位与 Pauli blocking 的数值判断应待算符、原式和实验材料闭合。

## Sources

- [[book-bohr-mottelson-nuclear-structure]]：对称性及角动量原件入口。
- [[giant-dipole-resonance-lorentzian-and-trk-sum-rule]]：GDR 积分与形变演示的不同边界。

## Evolution Log

2026-11-02：纠正 N=Z 分支数、算符秩与 ΔT 混用、CG 几何即实验强度、以及分裂即电荷无关性破缺等表述。未补造外部数值或来源 locator。
