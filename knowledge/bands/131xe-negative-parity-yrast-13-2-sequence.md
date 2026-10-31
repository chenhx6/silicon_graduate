---
type: band
title: ¹³¹Xe yrast 13/2- 起始序列
aliases: [131Xe 13/2- 835 keV sequence, 131Xe unresolved negative-parity sequence]
created: 2026-07-01
updated: 2026-10-30
status: active
review_status: human-reviewed
nucleus: 131xe
band_label: yrast-13-2-negative-parity-sequence
parity: "negative 13/2− anchor; 1600.9-keV node unresolved"
signature:
spin_range: "13/2− anchor; upper 1600.9-keV node unresolved"
configuration_status: unresolved
interpretation_status: open-question
tags: [negative-parity, unresolved-band]
---

# ¹³¹Xe Yrast 13/2- 起始序列

## Stable Identity

以 835 keV 的 yrast 13/2− 态为起点，在 Fig.1 中通过 766 keV quadrupole 跃迁连接到1601-keV节点；2023列为17/2−，2020版本列为17/2+，节点宇称保持未决。

## Level and Transition Data

当前首轮摄入可确认：

- 13/2-：834.6 keV；
- 1600.9-keV节点：2023列17/2−，2020列17/2+；
- 1600.9-keV节点 → 13/2−：766.5 keV，R_DCO=1.15(20)；
- 13/2- → 11/2-：670.6 keV，δ=0.03(3)。

## Spin-Parity Evidence

来自 2023 Table I 和 Fig.1，仍需回溯更早实验。Day28回核发现同一1600.9-keV节点在2020文献中标为17/2+、794.8-keV E1，而2023改列17/2−；新766.5-keV符合放置支持级联，但偏振栏为空，不能单独闭合electric/magnetic宇称判别。该版本冲突保留为 `needs_review: true`，不静默选择一方。

## Configuration Assignment

未解决。

## Proposed Interpretation

2023 作者明确指出其起源仍是开放问题，不将其写成 wobbling 或 signature partner。

## Discriminating Observables

yrast 17/2- 的实验 `B(M1)/B(E2)=2.54(4)` 约为 TPRM 预测的两倍。

## Competing Interpretations

可能涉及不同组态、准 γ 耦合或其他集体结构；当前知识库无足够来源排序。

## Sources

- [[chakraborty-2023-131xe-wobbling-origin]]
- [[banik-2020-131xe-multiple-band-structures]]
- [[131xe-1601-parity-version-boundary]]

## Day28 Evidence Boundary

- 2020的795-keV E1在图注、Table I脚注和B3门分析中多次出现；这削弱“单行排印错误”的解释，但不证明正宇称正确。
- 2023 Table I的766.5-keV行没有偏振观测；DCO quadrupole与符合关系不能独自重定1601-keV态宇称。
- 794.6-keV ENSDF记录、历史EKC和Kaya2018的独立再观测仍属于外部版本线索或评估边界，不能作为本页已亲验的早期primary宇称测量。
- Day28新增内容均保持 `needs_review: true`；本页既有`human-reviewed`只描述历史页面审核，不把本次版本边界升级为已解决事实。

## Evolution Log

- 2026-07-01（1 source）：建立开放问题页，避免被误并入 unfavoured partner。
- 2026-07-01（human review）：用户完成轻度科学校准，认可保持“起源未解决”的表述。
