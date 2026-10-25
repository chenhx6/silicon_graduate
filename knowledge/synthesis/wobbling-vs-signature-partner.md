---
type: synthesis
title: Wobbling 与 signature partner 的判别
aliases: []
created: 2026-07-01
updated: 2026-10-25
status: active
review_status: human-reviewed
scope: odd-a-normal-deformed-a130
confidence: medium
high_confirmed_by:
high_confirmed_date:
sources: [chakraborty-2023-131xe-wobbling-origin, frauendorf-2024-wobbling-review, lv-2022-evidence-against-wobbling-135pr, matta-2015-transverse-wobbling-135pr, garg-2015-135pr-magnetic-rotation, lawrie-2020-tilted-precession-wobbling]
tags: [wobbling, signature, evidence-matrix, a130]
---

# Wobbling 与 Signature Partner 的判别

## Agent active summary — Day22

当前使用Day22 checkpoint095/098的逐量比较；Day23仅无学分预习。[[lv-2022-evidence-against-wobbling-135pr]] L22-D22-R095-1提供逐线小δ测量；[[agarwal-2007-137pr-magnetic-rotation-bandcrossing]] AG07-D22-R098-1提供独立MR比值/模型对照，不能由一条M1占优线唯一归属SP、TiP或剪刀。 本段是Codex self-audit导航，新增内容needs_review: true，不扩张原有human-reviewed范围，也不替代source locator。

## Question and Scope

在正常形变奇 A 核，如何区分 [[wobbling-motion]] 与普通 [[signature-partner-bands]]？`131Xe` 作为当前反例案例。

## Evidence Matrix

| 主张 | 支持证据 | 反证/限制 | 替代解释 | 来源独立性 | 置信度 |
|---|---|---|---|---|---|
| wobbling 相邻 phonon 带间应有集体增强 E2 | 2024 综述结论及引用实验 | mixing ratio 测量困难 | signature partner M1 连接 | 综述，待回溯原始文献 | medium |
| signature partner 连接 ΔI=1 主要 M1 | `131Xe` DCO/δ | 弱跃迁误差 | 小幅集体 E2 混合 | 单一实验 | medium |
| 大 signature splitting 支持三轴性 | `131Xe` 系统学与模型 | 组态/Coriolis 也影响 | 非 wobbling 三轴带 | 单一实验+模型 | low |
| 三轴形变不保证 wobbling | `131Xe` 有三轴模型支持但无 E2 wobbling 信号 | 三轴性本身也模型依赖 | 未找到正确 wobbling band | 单一实验 | medium |

## Synthesis

判别优先级应是：

1. 可靠的 ΔI=1 mixing ratio 与绝对/相对 E2 强度；
2. 带的组态和自旋对应；
3. wobbling energy 与角动量几何；
4. signature splitting 和能量/Routhian 系统学。

能量相似或 wobbling energy 单独升降不能取代电磁跃迁证据。`131Xe` 新 yrare 序列的低 δ 支持普通 unfavoured signature partner；另一条 yrast 13/2- 序列仍应保持未解释。

## Counter-evidence

- 2024 综述认为正常形变核中的 TW/LW 有若干确认案例；
- `131Xe` 只说明该序列不是 wobbling，不说明整个核绝不可能存在 wobbling。

## Model Dependence

TPRM γ 和转动惯量可调；TPSM 基底截断和形变输入也影响结果。模型再现能量不能替代跃迁测量。

## Confidence Notes

判别框架 medium；`131Xe` yrare 序列作为 unfavoured partner 为 medium 候选，等待用户和原始数据复核。

## Limitations and Missing Evidence

- 缺 `131Xe` 关键态寿命和绝对 B(E2)；
- 缺 135Pr/133Ba/127Xe 等 wobbling 原始实验的并列复核；
- 需要检查 δ 的多解、符号和系统误差。

## Sources

- [[chakraborty-2023-131xe-wobbling-origin]]
- [[frauendorf-2024-wobbling-review]]
- [[lv-2022-evidence-against-wobbling-135pr]]
- [[matta-2015-transverse-wobbling-135pr]]
- [[garg-2015-135pr-magnetic-rotation]]
- [[lawrie-2020-tilted-precession-wobbling]]

## Evolution Log

- 2026-07-01：建立以电磁跃迁优先的判别流程。
- 2026-07-01（human review）：用户完成轻度科学校准，整体评价良好；框架升级为 human-reviewed，不升级为 verified。

## Day22 checkpoint095：机制比较的适用边界

135Pr不能只按一条小δ/弱正P被唯一判为TiP。[[lv-2022-evidence-against-wobbling-135pr]] L22-D22-R095-1–3报告的是逐线联合测量并在其QTR输入下解释；[[matta-2015-transverse-wobbling-135pr]] M15-D22-R095-1/2和[[sensharma-2026-evolution-chirality-transverse-wobbling-135pr]] SH26-D22-R095-1保留大δ支持链及不同MoI选择。SP/TiP/剪刀的识别需共同组态、连接身份、相对与绝对强度及模型几何；不采用“80–90% M1→TiP”“固定低W.u.→剪刀”的通用硬门。

旧Day22数值规则/黄金基准未完成原件对账，保存历史后移出活跃综合。参见[[signature-tip-shears-discrimination-contract]]的新逐项程序；Day23只预习、无学分。needs_review: true。

## Day22 checkpoint098：Day23无学分预习的独立磁转动对照

| 对照 | 原实验约束 | 解释与限制 |
|---|---|---|
| 137Pr，AG07-D22-R098-1/2 | INGA DCO/IPDCO与弱E2支路；给B(M1)/B(E2)，无τ | 比值先升后降；TAC提出3qp/5qp交叉与叶片重开。43/2打印强度重建不闭合，保留逐门输入缺口 |
| 108In，CHI01-D22-R098-1/2 | 另一核/阵列的DSAM与branch/ICC给绝对B(M1)，含对齐处回升 | 约3.05是18+/19+打印中央比，不是新联合CI；stopping系统量未含在原误差中 |

两条独立实验链提高的是“相对比/绝对强度/组态演化”辨别能力，不能把108In寿命迁入137Pr，或把一条小δ直接标成磁转动。原子出处见[[agarwal-2007-137pr-magnetic-rotation-bandcrossing]] AG07-D22-R098-1/2与[[chiara-2001-108-110in-shears-band-lifetimes]] CHI01-D22-R098-1/2。needs_review: true；Day23仍无学分。
