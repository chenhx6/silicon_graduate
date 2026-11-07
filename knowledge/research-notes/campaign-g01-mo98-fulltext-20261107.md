---
type: research-note
title: "98Mo出版正文：相对E3/E2、E1/E2与静态形状的可辨识性"
aliases: [98Mo octupole fulltext appraisal, campaign-g01-mo98-fulltext]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [karmakar-2025-2026-98mo-octupole-preview, bucher-2017-146ba-direct-octupole, mach-1990-96zr]
created_from: project
promotion_target:
tags: [98mo, octupole, a100, e3, identifiability]
---

# 98Mo：正文补齐后，哪些结论改变

## Research Trigger

用户提供8页出版正文，关闭了此前只有首页/两页会刊的访问缺口。
问题转为：三条E3指定与相对分支支持何种八极关联，是否足以区分振动、
高自旋反射不对称旋转和组态重排？出处为
[[karmakar-2025-2026-98mo-octupole-preview]]，实际版本与哈希见该source。

## Grounded Evidence

| 线或母态 | 原文报告 | locator | claim_kind |
|---|---|---|---|
| 1833.3(5) keV | 2620.4-keV 5−→787.2-keV 2+；相对Iγ=.24(9)；DCO、偏振为空 | PDF4 Table1；PDF3 Fig1标1833.2 | experimental-fact |
| 1585.8(6) keV | 3095.4-keV 7−→1509.6-keV 4+；相对Iγ=.74(16)；DCO、偏振为空 | PDF4 Table1 | experimental-fact |
| 已知2017.3(3) keV | 3−→0+，本研究与前两线合计讨论三条E3 | PDF4 Table1 | experimental-fact |
| 5− E3/E2 | B比66.05±27.01 fm²；100Ru对应17.39±4.84 fm² | PDF6 Table2 | experimental-fact, branch-derived |
| 7− E3/E2 | B比153.81±33.31 fm²；100Ru对应36.97±11.45 fm² | PDF6 Table2 | experimental-fact, branch-derived |
| 5−/7−/9− E1/E2 | 98Mo依次5.17(.38)、3.76(.21)、64.52(8.30)，单位10^-8 fm^-2 | PDF7 Table3 | experimental-fact, branch-derived |
| 直接寿命 | 本文说低自旋高能线未见可用线形，缺直接寿命；未给绝对B(E3)或B(E1) | PDF5 Sec4 | experimental-fact |
| 高自旋网络 | 作者未观察到要求的交错E1网络，归因统计不足；S(I)高自旋未消失 | PDF6–7 Fig7及结论 | experimental-fact + author-interpretation |

Iγ以787.2-keV线=100归一，是相对光子强度，不是单母态归一分支概率。
Table1的a表示本次新测量，并不把所有标a线都变成新发现。
1833.2/1833.3的图表差保留，不人为合并为新的精度。

## Provisional Reasoning

两条新线按已指定态对，E3是最低允许多极性；更高的M4等并非由三角/宇称定则严格禁止。
因此“作者指定E3”和“弱线独立测出E3多极性”要分开。Table1没有它们直接DCO/偏振。

作者将低自旋解释为八极振动，将I≥9的结构讨论为可能的永久八极形状旋转；
这两种解释不能扩展成整个98Mo在全部自旋的唯一形状。
尤其小E1不是排除静态八极的充分条件，146Ba的强E3与小E1提供相关反例
（[[bucher-2017-146ba-direct-octupole]] TableI及Figs3–5）。

Table2约四倍的是E3/E2比，不是绝对E3四倍。Table3的9−/7−打印中心比
为17.16（98Mo）和4.63（100Ru），不是两核都相对7−增强十五倍。
跨母态的完整协方差未知，这些是中心值算术，不赋予显著性。

## Assumptions

比值采用论文多极性和效率/分支处理。原表误差、另约4%的效率系统误差及
未提供的协方差分开；本轮没有从原始计数重拟合。J(1)是运动学惯量，
不是J(2)动态惯量；本轮没有数字化Fig5/7，不补精确惯量或临界交点。

## Competing Explanations

本任务提出的竞争路线是组态重排/带混合改变电磁矩阵元。
相对E1/E2上升可由分子、分母或两者变化造成，尚无共同Hamiltonian拟合来选择。
不将具体νh11/2配对、质子组态、固定K禁戒或一至两个数量级的E2下降写成实测机制。
作者双声子5−解释也属于需要矩阵元/共同模型约束的候选。

## Transfer Conditions

96Zr的直接低自旋B(E3)、98Mo的相对E3/E2和100Ru的高自旋绝对E1是三种证据。
N=56使同中子素比较有价值，但不能用一个核的绝对强度标定另一个核，
也不能从102Ru的低自旋NRF E1响应直接认定98Mo高自旋的同一内禀模式。

## Falsification or Reverse Tests

最有信息增益的是5−/7−/9−母态的寿命、完整分支/转换与原始误差，
用于共同提取绝对E1、E2、E3：先检验比值增大是否伴随E2下降。
再以保留统计/背景/效率的搜索检验高自旋交错E1网络；未见须有可报告上限，
不能以固定事件数作为充分灵敏度。对弱线进一步测角分布/偏振与符合关系，
检查错放置或未分辨峰；按当前自旋指定，M2/E2本来就不是该ΔJ=3的允许直接多极。

## Failure Conditions

无绝对矩阵元或共同输入竞争模型时，不宣布静态形状、排他性振动或确定组态。
不存在普适的15–30/40–50 W.u.、D0或10^10事件认证门槛；
探测器与寿命方法须按实际时间尺度、feeding、停止和响应确定。

## Open Questions

能否用同一组参数解释能谱、绝对电磁与交错连接？
现有原始计数、联合Cov和寿命未在本次正文中取得；未由此声称从未测过或不能获取。

## Human Review

这是Gemini精读与总控原表核查，无新增human-reviewed事件。
P0: none identified in registered file identity。P1：多极性、相对/绝对强度、
小E1形状推断及未见信号灵敏度均保留上述限制。

## Promotion or Rejection History

2026-11-07：用新出版正文替换获取边界。总控撤回worker草案的固定强度/事件数门槛、
唯一E3、固定组态、纯跃迁无混合和无依据的精确Ic；访问缺口关闭不等于物理解释闭合。
