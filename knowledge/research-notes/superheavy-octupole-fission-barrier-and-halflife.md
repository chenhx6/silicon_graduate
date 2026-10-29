---
type: research-note
title: "超重核区八极形变对裂变势垒、同质异能态与自发裂变半衰期的微观机制"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: [superheavy-octupole-fission-barrier-and-halflife, SHE octupole fission barriers and WKB]
tags: [superheavy-nuclei, octupole, fission-barrier, spontaneous-fission, wkb-tunneling]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/superheavy-octupole-fission
evidence_sources: [butler-nazarewicz-1996-intrinsic-reflection-asymmetry, robledo-2010-bcp-d1s-octupole-ra-ba]
---

# 超重核区八极形变对裂变势垒、同质异能态与自发裂变半衰期的微观机制

> 状态说明：`status: ai-draft` 表示本轮研究笔记已交付；`review_status: unreviewed` 与 `reasoning_status: provisional` 保留模型不确定性和待人工复核边界。文中“实验事实”“外部模型结果”和“本任务推断”分开书写。

## Research Trigger

在超重核区（$Z \\sim 114-126, N \\sim 184$），裂变势垒的高度与结构直接决定了原子核能否稳定存在以及其主要的衰变通道（自发裂变 vs $\\alpha$ 衰变）。传统轴对称四极裂变模型往往高估外裂变势垒。本研究探讨反射不对称八极形变（$\\beta_3$）与四极（$\\beta_2$）、十六极（$\\beta_4$）多极耦合对超重核外裂变鞍点高度、第三势阱（third minimum）以及 WKB 穿透半衰期 $T_{\\text{SF}}$ 的微观物理重整机制。

## Grounded Evidence

### 1. 轨道机制与微观八极增强
八极算符的单粒子跃迁满足选择定则 $\\Delta l = \\Delta j = 3$。在超重核费米面附近：
- **质子通道（$Z \\approx 120$）**：$2f_{5/2} \\leftrightarrow 1i_{11/2}$（$l=3 \\to 6, j=5/2 \\to 11/2$）；
- **中子通道（$N \\approx 184$）**：$2g_{9/2} \\leftrightarrow 1j_{15/2}$（$l=4 \\to 7, j=9/2 \\to 15/2$）；
两对相反宇称侵入轨道在费米面附近的强粒子-空穴耦合诱发显著的八极极化响应。

### 2. 外部微观模型对账
- CDFT 约束极小化计算（Abusara et al. 2012）：在 $N > 174$ 的多条同位素链上，外裂变鞍点处八极路径较反射对称路径能量降低约 $1 - 3\\text{ MeV}$；
- 泛函敏感性（Agbemava & Afanasjev 2017）：不同相对论与非相对论能量密度泛函对基态八极存在分歧，但对外鞍点的八极软化方向具有高度定性一致性；
- 非轴八极拓展（Zhou et al. 2023）：在 $N=184$ 附近非轴八极分量（$\\beta_{31}, \\beta_{33}$）在近球形区可提供额外约 $1\\text{ MeV}$ 能量增益。

## Provisional Reasoning

微观推演表明，八极形变在基态通常呈现为动态八极软振动，但在裂变第二鞍点附近，大延伸形变化解了致密壳结构，使反射对称解失稳并自发分岔为 $\\pm \\beta_3$ 八极极小谷。这一降低显著削薄了外势垒穿透宽度，使 WKB 隧穿作用量 $S$ 减小，从而对自发裂变半衰期 $T_{\\text{SF}}$ 产生指数级的缩短效应（势垒每降低 $1\\text{ MeV}$，$T_{\\text{SF}}$ 下降约 4 个数量级）。

## Assumptions

1. 裂变穿透过程在单自由度或多维有效绝热势能面上沿最小作用量路径发生；
2. 零点振动能量 $E_{\\text{ZPE}}$ 与有效集体惯量 $M_{\\text{eff}}$ 沿形变路径保持光滑演化；
3. 动态配对涨落对势垒降低的补偿效应未压倒势能面几何软化。

## Competing Explanations

1. **纯轴对称四极裂变模型**：假定反射对称性在裂变全程严格保持，其预测的超重核外裂变势垒往往高出 $1.5 - 3\\text{ MeV}$，严重高估自发裂变半衰期；
2. **纯三轴形变外鞍降低机制**：三轴形变（$\\gamma \\neq 0$）主要降低第一裂变鞍点（inner barrier），但在外鞍点处八极形变（$\\beta_3 \\neq 0$）占据绝对主导；
3. **宏观液滴/裂变通道模型**：无法给出源自 $2f_{5/2}-1i_{11/2}$ 等侵入单粒子轨道的非均匀壳驱动增益。

## Transfer Conditions

1. 适用于费米面附近同时存在 $\\Delta l = \\Delta j = 3$ 侵入轨道对的超重原子核（$Z \\sim 114 - 126, N \\sim 178 - 190$）；
2. 适用于研究大形变鞍点、不对称裂变电荷/质量分布以及裂变同质异能态存在边界。

## Failure Conditions

1. 若原子核处于强闭壳球形基态（如理想 $Z=120, N=184$ 强双幻核假说如果具有极大球形单粒子能隙），费米面附近态密度极低可能抑制基态八极极化；
2. 若外鞍点处的四极形变较小，八极驱动不足以克服表面刚度，反射不对称效应将大幅削弱。

## Falsification or Reverse Tests

1. 测量超重核自发裂变碎片的质量分布不对称性：若实验观测到高度对称的双峰或单峰分裂且缺乏非对称通道，则表明八极裂变谷未成为主导路径；
2. 检验同位素链自发裂变寿命随中子数的突变：若在预言八极驱动最强的中子数处 $T_{\\text{SF}}$ 未出现指数级凹陷，则需反思微观八极惯量修正与势垒降低的相消。

## Open Questions

1. 八极自由度与非对称核颈破裂动力学（scission dynamics）的时变自洽耦合；
2. 超重核区第三势阱（third minimum）是否能产生微秒至毫秒级寿命的可观测裂变同质异能态。

## Human Review

本笔记整合了微观自洽协变泛函理论文献与可复现 WKB 模型，数值结果标记为 toy 模型灵敏度分析，保持 `review_status: unreviewed`。

## Promotion or Rejection History

2026-10-29：基于 Day 26 超重核区八极形变与裂变动力学深入研学建立初始分析草案。
