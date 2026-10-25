---
type: method
title: 核摆动运动的分层鉴别规范
aliases: [minimal wobbling identification protocol, wobbling verification protocol, wobbling falsification protocol]
created: 2026-10-24
updated: 2026-10-25
status: ai-draft
review_status: unreviewed
method_type: experimental-and-theoretical-criteria-protocol
tags: [wobbling, mixing-ratio, phonon, model-boundary]
---

# 核摆动运动的分层鉴别规范

## Purpose

checkpoint091撤回旧“五重数值硬门”及全核区终审。当前规范将实验辨识、几何分类与声子有效域分别检验；具体短卡见[[wobbling-criteria-card]]，四列逐线练习见[[wobbling-geometry-phonon-observable-contract]]。

## Inputs and Assumptions

明确核素/带/跃迁身份、spin和主轴约定；同母态强度与内转换、寿命、δ相位、偏振响应/取向/门条件。模型固定的形变和惯量必须与实测区分。

## 逐项程序

1. 建立符合与能级身份，分开独立采集、同批数据重分析与模型复引。
2. 比较完整角分布/角关联和偏振响应，保留δ竞争解。偏振符号或单纯χ²最低值不能自动替代置信域比较；具体置信水平须来自实际似然。
3. 同一母态计算out/in B比，报告Eγ幂次、混合份额与分支/响应不确定度。没有寿命时，不写绝对B值；相对比仍有实验检验力。
4. 在明示Hamiltonian下检验取向、惯量排序、局部稳定性及HFA有效域；SCS图是波函数表示。F14冻结近似也有非零M1，故不设M1恒零或统一E2份额必要门。
5. 多声子另检验能量与矩阵元阶梯，允许明确量化的非谐性/混合，并与signature/TiP/其他振动或组态交叉作共同观测比较。缺少证据时记未定，不记反机制已证实。

## 跨质量区七大典型核素协议评估全景表

旧表的排他终审撤回，保留此定位说明纠错。163Lu、135Pr、187Au、105Pd、133La、133Ba、131Xe必须各自回原实验，不能共用统一W.u.、δ、R/j门限。本次直接核130Ba/136Nd的两准粒子反例说明旧协议本身过强，不代表这两核的新模式确证。

## 十一核全景定性裁决矩阵（Ten-Nuclei + One-Null-Control Protocol Verdict Matrix）

历史扩展记录；旧名称及其18核替代表不再作为“全部候选”的穷尽分母或确证百分比。原自选样本含163Lu、161Lu、165Lu、167Lu、167Ta、135Pr、187Au、136Nd、74Br、130Ba、105Pd、133La、127Xe、133Ba、151Eu、183Au、129Ba、131Xe。未逐核核验者保持未定；不从来源缺失反推物理不存在。

| 本次直接核对象 | 原文支持 | 实际限制 | 当前处理 |
|---|---|---|---|
| 130Ba S1/S1′ | 约25% E2份额仍被作者结合相对强度和PRM几何解释为TW | AD大δ未完全排除；惯量按能量拟合；复用前序谱学 | 保留支持解释和模型边界，撤回剪刀态终审 |
| 136Nd L1/L3 | 751线约19% E2、相对rE2=.36(.17)与模型比较支持作者TW | 仅一条可分析；算符参数由单点固定；本篇无所称DSAM绝对塌缩 | 保留候选与可证伪外推，撤回11倍塌缩改判 |

## 未来实验判决与谱仪设施指标（Future Facility and Measurement Roadmap）

优先测另一条干净连接线或伙伴态寿命，检验未用该点定标的模型预测。束流小时、偏振符号→模式一一判决、Q(E)与计数率须来自实际设施/反应/效率/污染模型；旧3–4天或16.3h等不得当成本规范已核设施承诺。本规范不改变Day21原实验设计记录，但本轮未对其重新认证。

## What It Can Establish

给出可追溯证据缺口和模型比较问题，避免混合光子份额、相对B与绝对集体性。

## What It Cannot Establish Alone

不能从M1占优、S(4)符号或相近alignment唯一改判；不能证明全核区只有163Lu，也不替代原始响应/协方差或完整多准粒子求解。

## Sources

- [[frauendorf-2014-transverse-wobbling]] F14-D22-R091-1、F14-D22-R091-2。
- [[hamamoto-2003-quantized-wobbling-excitations-alignments]] H03-D22-R091-1。
- [[chen-2019-transverse-wobbling-even-even]] CH19-D22-R091-1、CH19-D22-R091-2。
- [[lv-2022-transverse-wobbling-136nd]] LV22-D22-R091-1、LV22-D22-R091-2。

## 原定位纠错

WOB-METH-075-1的全图谱率和排他判决撤回。所有本轮推断保持needs_review: true，不设置human-reviewed。

## Day22 checkpoint122：缺测、条件上限和实际响应

[[odegard-2001-evidence-wobbling-163lu]] OD01-D22-R122-1提供具体反例：低能交替连接未给有意义upper limit，不能补成实验零。[[jensen-2002-second-phonon-wobbling-163lu]] JE02-D22-R122-1的rM1上限.012则属于选大δ后的比较；仍不能把共享输入派生量算作独立选根证据。原模型支持与实验限制同时保留。

继承225.8keV方案的16.3/45.3h和P正号排他认证，已按[[lv-2019-chirality-135nd-reexamined]] LV19-D22-R110-3撤回。[[miller-2007-sega-polarization]] MI07-D22-R115-1提供的是任务matched-null计数模型的条件推导，不能填补实际Q、shared response、背景和selected rate；增加统计量也不替代这些输入。needs_review: true。
