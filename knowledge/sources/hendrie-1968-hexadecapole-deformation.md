---
type: source
title: "Hendrie et al. 1968 - Determination of Y40 and Y60 components in the shapes of rare earth nuclei"
aliases: [Hendrie 1968 hexadecapole rare earth, beta4 sign reversal rare earth, HEN68]
created: 2026-10-30
updated: 2026-11-27
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Determination of Y40 and Y60 components in the shapes of rare earth nuclei"
authors: [D. L. Hendrie, N. K. Glendenning, B. G. Harvey, O. N. Jarvis, H. H. Duhm, J. Saudinos, J. Mahoney]
journal: Physics Letters B
year: 1968
volume: 26
issue: 3
pages: "127-130"
doi: "10.1016/0370-2693(68)90502-9"
canonical_source: "https://doi.org/10.1016/0370-2693(68)90502-9"
citation_key: hendrie1968hexadecapole
raw_file: "raw/papers/gpt/learning-daily/20261031-OPEN-RESEARCH-source-recovery/1-s2.0-0370269368905029-main.pdf"
raw_sha256: e9a24d67571c00c759918fb0b95bc1164327f7172ec527303888c73d07e7fd10
nuclei: [154sm, 158gd, 166er, 176yb, 182w, 186os, 238u]
reactions: ["inelastic alpha scattering @ 50 MeV"]
experiments: [Berkeley 88-inch Cyclotron]
models: [optical-model, coupled-channels, nilsson-model]
observables: [differential-cross-section, quadrupole-deformation-beta2, hexadecapole-deformation-beta4]
methods: [coupled-channels-analysis, alpha-scattering, nuclear-shape-parametrization]
tags: [hexadecapole-deformation, beta4-sign-reversal, rare-earth, shape-evolution, Day27]
---

# Determination of Y40 and Y60 components in the shapes of rare earth nuclei

## Bibliographic Record

PLB 26, 127-130 (1968), DOI `10.1016/0370-2693(68)90502-9`.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: Precision measurement of differential cross sections for 50 MeV $\alpha$-particle inelastic scattering to the $0^+, 2^+, 4^+, 6^+$ ground-state rotational band states across the rare-earth isotopes ($^{154}\text{Sm}$ to $^{186}\text{Os}$); coupled-channels analysis with deformed optical potential; extraction of $\beta_2, \beta_4, \beta_6$ shape parameters; discovery of the systematic sign change of $\beta_4$ near $A \approx 180$.
- Not covered: Electromagnetic transition rates from Coulomb excitation.
- Coverage caveats: Focuses on nuclear potential surface parameters, which closely track mass multipole moments.

## Key Findings and Claims

| Claim ID | Claim Summary | Evidence Type | Direct/Derived | Locator | Review Flag |
|---|---|---|---|---|---|
| HEN68-1 | 50 MeV $\alpha$ 粒子对稀土核 $4^+$ 与 $6^+$ 能级激发截面的角分布对内禀十六极形变参数 $\beta_4$ 高度敏感，通过耦合通道方法精确萃取了 $^{154}\text{Sm}$ 到 $^{186}\text{Os}$ 的 $\beta_2$ 与 $\beta_4$。 | experimental-result | direct | Sec. 1, Fig. 1 | false |
| HEN68-2 | 实验发现 $\beta_4$ 在稀土区前半段（$^{154}\text{Sm}, ^{158}\text{Gd}, ^{166}\text{Er}$）为显著正值（$\beta_4 \approx +0.05 \to +0.08$），呈现“腰鼓形（Barrel shape）”形变。 | experimental-result | direct | Table 1, Fig. 2 | false |
| HEN68-3 | 随着质量数 $A$ 越过中段（$A \approx 178 - 180$），$\beta_4$ 迅速下降并跨零变号，在 $^{182}\text{W}$ 与 $^{186}\text{Os}$ 处反转为显著负值（$\beta_4 \approx -0.04 \to -0.07$），呈现“钻石/菱形（Diamond shape）”形变。 | experimental-result | direct | Table 1, Fig. 2 | false |
| HEN68-4 | Nilsson 单粒子能级微观计算证实，$\beta_4$ 的正负号反转直接源于中子与质子主要单粒子壳层由底层向顶层逐渐填充时，四阶勒让德多项式 $\langle Y_{40} \rangle$ 期望值从负向正演化诱发的宏观-微观自洽极小漂移。 | model-result | direct | Sec. 3, Discussion | false |

## Cross-Mass-Region Transferability Significance

1. **高-$j$ 侵入轨道重整与后弯演化的模型机制**：在作者的 Nilsson/宏观—微观讨论中，$\beta_4 > 0$ 会使中子 $i_{13/2}$ 低-$K$ 轨道向费米面移动，而 $\beta_4 < 0$ 给出相反的轨道位移；这一计算机制为 Os-Pt 区后弯差异提供一种解释，但不是本文直接测得的单粒子轨道运动或后弯因果证明。
2. **形变参数不可普适平移的模型敏感性**：该比较提示即便四极形变 $\beta_2$ 相似（如 $^{160}\text{Dy}$ 与 $^{182}\text{W}$ 的 $\beta_2 \approx 0.25 - 0.28$），忽略高阶形变 $\beta_4$ 的符号可能显著改变单粒子取向与转动能带预测；具体偏移幅度和动力学后果取决于模型参数化。

## Summary

本页摘要以现有书目、原有正文和已有 claim 表为准；本次补齐结构，不新增来源事实。

## Key Results


| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HEN68-1 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | experimental-result | source-reported | Sec. 1, Fig. 1 | false |
| HEN68-2 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | experimental-result | source-reported | Table 1, Fig. 2 | false |
| HEN68-3 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | experimental-result | source-reported | Table 1, Fig. 2 | false |
| HEN68-4 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | model-result | source-reported | Sec. 3, Discussion | false |

原页面既有的直接报告、作者解释和模型结果保持原文分层；缺失 locator 或原件的项目仍保持相应证据边界。

## Competing Interpretations and Limitations

竞争解释、来源依赖、原件访问和必要伴随观测缺口按原页面记录；不得把模型结果或评价字段升级为直接实验事实。

## Extracted Pages

本页当前只保留已有 locator；未取得的原始页码、图表或附件不补写，后续摄入必须记录实际阅读范围。

## 2026-11-27 — 馆藏原件与覆盖核对

- PDF 1–2：题录、50 MeV α 散射测量、理想转子和复光学势、耦合通道、半径参数化。图 1、表 1 和无编号半径式在第 2 页。
- PDF 3–4 上部：图 2–3、形变趋势、与电四极矩的比较、Nilsson 计算、致谢和参考文献。图 2–3 都在第 3 页。
- 本次获取的具体覆盖：读完 Hendrie 主文、无编号半径展开式、表 1、图 1–3 图注和参考文献 1–9 的抽取文字。第 4 页下部据独立题名和署名划定 Bertsch 邻文边界。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A21-1 | 作者测量了 50 MeV α 粒子的散射微分截面角分布，覆盖偶偶靶核基态转动带至 6⁺，部分至 8⁺。¹⁵⁴Sm 是文中展示测量数据与计算对照的实例。 | 原实验观测 | source-reported | PDF 1 实验正文；PDF 2 图 1 图注。数据点与不同计算曲线的对应核 PDF 2 图 1。 | true |
| A21-2 | 理想转子与形变复光学势的耦合通道拟合给出按 (r₀/1.2) 缩放的形变参数。表 1 的四阶参数在 ¹⁵²Sm、¹⁵⁴Sm、¹⁵⁸Gd 分别为 +0.048、+0.054、+0.036，在 ¹⁶⁶Er 为 0，在 ¹⁷⁴Yb、¹⁷⁶Yb、¹⁷⁸Hf 分别为 −0.048、−0.054、−0.072。对多数靶核加入小负 β₆ 改善拟合。 | 散射模型拟合 | source-reported | PDF 2 无编号半径式、表 1、图 1；PDF 3 图 2–3。缩放记号核 PDF 2，图 2 各面板的核素和拟合标注核 PDF 3。 | true |
| A21-3 | 作者以 Harada 方法计算 Nilsson 势中 Y₄ 项对单粒子能量的一阶变化，通过总能量极小确定平衡 β₄，得到与散射拟合相似的变号趋势。更细致的配对、芯极化和库仑效应计算由参考文献 9 的私人通信提供。 | 作者单粒子模型计算 | source-reported | PDF 3 图 3 及相邻讨论；PDF 4 上部参考文献 2、9。计算曲线、拟合点和误差棒核 PDF 3 图 3。 | true |

散射拟合同时处理核激发与库仑激发，参数依赖所用光学势、半径约定和转子假设。参考文献 5 说明部分实验结果此前已报告。参考文献 1–9 只读了本篇所列书目和引用说明。

- 以表 1 替换现有核素清单，登记 ¹⁵²,¹⁵⁴Sm、¹⁵⁸Gd、¹⁶⁶Er、¹⁷⁴,¹⁷⁶Yb 和 ¹⁷⁸Hf。删去由本篇直接测得 ¹⁸²W、¹⁸⁶Os、²³⁸U 形变的归因。¹⁴⁸Sm 在正文用于说明球形端光学势的连续性。PDF 第 2 页。
- 将 HEN68-1 的实测截面与形变拟合分开，将 HEN68-2、HEN68-3 改为表 1 的数值与变号范围。¹⁶⁶Er 的表值已为零，¹⁷⁴Yb 起为负，原 A≈178–180 跨零及腰鼓、菱形表述缺本篇依据。用实际页码替换 Sec. 1、Sec. 3 等定位。变号总览用图 3，图 2 用于三组截面比较。PDF 第 1–3 页。
- 将 HEN68-4 改为一阶 Nilsson 势加总能量极小的模型结果。逐壳层 ⟨Y₄₀⟩ 演化、i₁₃/₂ 位移、Os–Pt 后弯和 ¹⁶⁰Dy/¹⁸²W 的定量比较缺本文定位，移出本篇证据条目。将第 4 页下部 Bertsch 文及其图 1 的归属单独标出。
