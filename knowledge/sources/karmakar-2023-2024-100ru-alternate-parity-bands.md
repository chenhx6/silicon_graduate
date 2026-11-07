---
type: source
title: "Karmakar et al. 2023-2024：100Ru交替宇称转动带与七条交错E1跃迁在束谱学（PRC）"
aliases: ["Karmakar 2024 PRC 100Ru spectroscopy", "arXiv:2306.07670", "PRC 109 054312", "Possibility of stable octupole deformation in 100Ru"]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: read
title_original: "Rotation of pear-shaped 100Ru nucleus (arXiv:2306.07670v1) / Possibility of stable octupole deformation in 100Ru (PRC 109, 054312)"
authors: ["A. Karmakar", "P. Datta", "Soumik Bhattacharya", "Shabir Dar", "S. Bhattacharyya", "G. Mukherjee", "H. Pai", "S. Basu", "S. Nandi", "S. S. Nayak", "Sneha Das", "R. Raut", "S. S. Ghugre", "Sajad Ali", "R. Banik", "W. Shaikh", "S. Chattopadhyay"]
journal: Physical Review C
year: 2024
volume: 109
pages: 054312
doi: 10.1103/PhysRevC.109.054312
arxiv: "2306.07670"
canonical_source: "https://doi.org/10.1103/PhysRevC.109.054312"
citation_key: ""
raw_file: raw/papers/gpt/query/20261107-a100-octupole-lifetimes/arxiv-2306.07670v1.pdf
raw_sha256: 100429e395e521e28039fb46170aabc5d481c623c43537f7ced7642f1e14a60c
raw_storage_status: fully-archived-local
archive_required: true
nuclei: ["100ru"]
tags: ["in-beam-gamma-spectroscopy", "alternate-parity-bands", "interleaved-e1", "octupole-correlations", "a100"]
---

# 100Ru交替宇称带在束谱学：七条交错E1跃迁、相对B(E1)/B(E2)与版本题名演化

## Bibliographic Record

A. Karmakar et al., Physical Review C **109**, 054312 (published 2024-05-08), DOI: 10.1103/PhysRevC.109.054312。
预印本先行版本为 arXiv:2306.07670v1 (2023-06-13)。
底本为合法获取的官方预印本全文及其完整源码：
1. PDF全文：`raw/papers/gpt/query/20261107-a100-octupole-lifetimes/arxiv-2306.07670v1.pdf` (SHA-256: `100429e395e521e28039fb46170aabc5d481c623c43537f7ced7642f1e14a60c`，共 13 页)；
2. LaTeX源码及补充材料：`raw/papers/gpt/query/20261107-a100-octupole-lifetimes/arxiv-2306.07670v1.src.tar.gz` (解包源文件 `arxiv.tex`，含正文与 Supplementary Information 全文共 461 源码行，包含 Table I, II 及分支比分析)。

## Scope and Reading Depth

对官方预印本及补充材料全文（正文及 SI 共 13 页，含图 1–7 与表 1–2）进行了全量逐行深度阅读。重点核查：
1. 题名演化：从预印本激进断言 *Rotation of pear-shaped $^{100}$Ru nucleus*（梨形核转动）到期刊发表审慎软化为 *Possibility of stable octupole deformation in $^{100}$Ru*（稳定八极形变可能性）的历史演进与学术分寸；
2. 实验设置：反应系统为 $50\text{ MeV}$ $\alpha + {}^{100}\text{Mo}$ **$2\text{ mg/cm}^2$ 薄靶**（与后续厚靶实验不同采集），使用 INGA 11 台 Clover 阵列采集 $5 \times 10^9$ 符合事件，RADWARE 能级纲目构建；
3. 识别的 10 条新跃迁，特别是连接 Band 2 与 Band 3 的 7 条交错 E1 跃迁的光强、DCO 角关联比值与 iPDCO 线偏振测量；
4. 相对分支比 $I(E1)/I(E2)$ 与跃迁几率比 $B(E1)/B(E2)$ 随自旋的演化规律；
5. 转动惯量 $\mathcal{J}^{(1)}$ 与宇称劈裂指数 $S(I)$ 的定量行为；
6. 界定本篇（薄靶纯谱学相对比值）与后续寿命篇（PRC 110, L051302，厚靶 DSAM 绝对寿命）的依赖与分工，杜绝预印本与期刊重复计证。

## Key Results

| ID | 实际可核验内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KM23-S1 | 预印本原题为 *Rotation of pear-shaped $^{100}$Ru nucleus*，正式发表时修改为 *Possibility of stable octupole deformation in $^{100}$Ru*，反映出同行评审后对“梨形核转动”断言的证据收敛与谨慎态度。 | source-lineage | direct | arXiv:2306.07670v1 题名 vs PRC 109, 054312 题名 | false |
| KM23-S2 | 实验在 VECC 利用 $50\text{ MeV}$ $\alpha + {}^{100}\text{Mo}$ 薄靶（$2\text{ mg/cm}^2$）反应，使用 INGA 阵列收集 $5 \times 10^9$ 符合事件，构建了 $^{100}\text{Ru}$ 高自旋能级纲目，新确立 10 条 $\gamma$ 跃迁。 | experimental-setup | direct | PDF p.2, 源码行 91；Fig. 1 | false |
| KM23-S3 | 在正宇称解耦带 Band 2（$\nu h_{11/2}^2$ RAL 构型）与负宇称解耦带 Band 3 之间观察到 7 条交错连接的跃迁：$687.1 (12^+ \to 11^-)$、$244.8 (13^- \to 12^+)$、$550.5 (14^+ \to 13^-)$、$485.2 (15^- \to 14^+)$、$515.3 (16^+ \to 15^-)$、$488.2 (17^- \to 16^+)$、$623.3\text{ keV} (18^+ \to 17^-)$。 | experimental-data | direct | PDF p.2, 源码行 101；Fig. 1；SI Table I | false |
| KM23-S4 | $R_{DCO}$（$90^\circ$ 与 $55^\circ$）和 $iPDCO$ 测量证实这 7 条带间跃迁均为纯 E1 性质（M2 混合可忽略），支持 Band 3 为负宇称态赋值。 | experimental-data | direct | PDF p.8 SI, 源码行 315–316；Fig. 4 (dco_pdco_s) | false |
| KM23-S5 | 相对比值 $B(E1)/B(E2)$ 在高自旋交错区（$I \ge 12\hbar$）的加权均值为 $(8.93 \pm 0.87) \times 10^{-8}\text{ fm}^{-2}$，显著高于低自旋振动能级（$5^-, 6^-, 7^-, 8^-, 9^-$）的均值 $(2.26 \pm 0.15) \times 10^{-8}\text{ fm}^{-2}$。各能级具体比值见 SI Table I。 | experimental-data | direct | PDF p.3, 源码行 113；SI Table I & Table II | false |
| KM23-S6 | 转动惯量与宇称劈裂指数显示：在 $\hbar\omega \le 0.5\text{ MeV}$（$12\hbar \le I \le 16\hbar$），两带转动惯量存在微小差异且伴随宇称劈裂；在 $\hbar\omega \ge 0.5\text{ MeV}$（$I \ge 16\hbar$），两带转动惯量完全重合且宇称劈裂指数 $S(I)$ 降为 0；在 $I > 22\hbar$（$\hbar\omega = 0.66\text{ MeV}$）交替宇称结构突然终止。 | experimental-derived | direct | PDF p.3-4, 源码行 127, 138, 140；Fig. 3 (3nuclei_moi_sj) | false |
| KM23-S7 | 本文未开展能级寿命测量，所有跃迁强度仅为由谱仪探测效率与角分布校正（$90^\circ$ 与 $125^\circ$ 比值校正系数 $1.58 \pm 0.06$）得到的相对比值 $I(E1)/I(E2)$ 和 $B(E1)/B(E2)$，未获得绝对跃迁几率。 | experiment-method | direct | PDF p.9 SI, 源码行 335–344；式 (1) | false |

## Summary

本项工作是 $^{100}\text{Ru}$ 高自旋交替宇称带的基础性实验谱学研究。作者利用 $50\text{ MeV}$ $\alpha + {}^{100}\text{Mo}$ 薄靶熔合蒸发反应与 INGA 高纯锗阵列，测定了 Band 2（正宇称）与 Band 3（负宇称）之间的 7 条双向交错 E1 跃迁的光强、DCO 角关联比值及康普顿散射线偏振度，确立了两带交替排列的微观能级结构。
测量的相对跃迁几率比 $B(E1)/B(E2)$ 在高自旋区达到了 $(8.93 \pm 0.87) \times 10^{-8}\text{ fm}^{-2}$，比低自旋振动态显著增强；且在高自旋区（$I \ge 16\hbar$）观测到两带转动惯量趋同和宇称劈裂指数归零的特征。
该工作在预印本阶段曾使用果断的“梨形核转动”标题，但在同行评审正式发表于 PRC 时审慎修正为“稳定八极形变的可能性”，体现了纯能级纲目与相对分支比无法单独确立静态八极形变的科学界限。

## Competing Interpretations and Limitations

1. **相对值不可替代绝对几率**：本文仅给出 $B(E1)/B(E2)$ 比值，缺乏能级寿命测量；若 $B(E2)$ 发生集体性减弱，比值亦可表现为表观增大，因此必须由独立的 DSAM 寿命测量进行绝对校验；
2. **预印本与期刊不可重复计证**：arXiv:2306.07670v1 与 PRC 109, 054312 属于同一批实验数据在不同时期的发表文本，属于单一证据链，不可作为两篇独立文献进行重复统计；
3. **高自旋八极来源假说**：作者将交替宇称结构归因于 $\nu h_{11/2} - \nu d_{5/2}$ 轨道的八极驱动力诱导的双中子转动对准核心极化；但这仍属于作者的唯象推测，尚未排除动态八极振动与转动粒子耦合引起的宇称混合；
4. **与后续厚靶寿命工作的实验分工**：本工作为 $50\text{ MeV}$ 薄靶反应建立精细能级纲目与分支比；后续的厚靶实验（PRC 110, L051302，使用 $45\text{ MeV}$ 束流与厚靶）在此基础上测量能级寿命，两者为不同采集事件，但后者分支比直接依赖本篇输入。

## Knowledge Impact and Learning Decision

1. **建立实验谱学底座**：为理解 $^{100}\text{Ru}$ 的八极关联提供了详尽的跃迁能级、多极性鉴定、分支比与转动惯量演化数据；
2. **界定与后续寿命工作的分工**：明确本文负责建立能级纲目、确立 7 条 E1 跃迁及分支比；而后续的 PRC Letter (KM24) 则负责通过厚靶 DSAM 测量能级寿命、提取绝对 $B(E1)$ 并与 TPSM 模型进行对比；
3. **记录题名演化规范**：在文献志和学术史梳理中，明确记录预印本题名改动的审稿背景，防止误将预印本早期激进断言当作正式发表结论。

## Extracted Pages

阅读了官方 PDF 全文（共 13 页，含正文与 Supplementary Information 全文）以及配套 LaTeX 源码 `arxiv.tex`（全量 461 源码行及全部表格图注）。
