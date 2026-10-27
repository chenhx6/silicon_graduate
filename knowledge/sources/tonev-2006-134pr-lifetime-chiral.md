---
type: source
title: "Tonev2006：134Pr跃迁几率与手征检验原实验"
aliases: [Tonev 2006 134Pr transition probabilities, 134Pr PRL 96 052501]
created: 2026-10-27
updated: 2026-10-27
status: ai-draft
review_status: unreviewed
source_type: experimental-lifetime-paper
reading_depth: deep-read
title_original: "Transition Probabilities in 134Pr: A Test for Chirality in Nuclear Systems"
authors: ["D. Tonev", "G. de Angelis", "P. Petkov", "A. Dewald", "S. Brant", "S. Frauendorf", "D. L. Balabanski", "P. Pejovic", "D. Bazzacco", "P. Bednarczyk", "F. Camera", "A. Fitzler", "A. Gadea", "S. Lenzi", "S. Lunardi", "N. Marginean", "O. Möller", "D. R. Napoli", "A. Paleni", "C. M. Petrache", "G. Prete", "K. O. Zell", "Y. H. Zhang", "Jing-ye Zhang", "Q. Zhong", "D. Curien"]
year: 2006
journal: Physical Review Letters
volume: 96
issue: 5
pages: "052501"
doi: 10.1103/PhysRevLett.96.052501
canonical_source: https://doi.org/10.1103/PhysRevLett.96.052501
citation_key: ""
raw_file: raw/papers/2006_Tonev_134Pr_Transition_Probabilities.pdf
raw_sha256: eac94a5ff8402144aa66b003fbafada85e180126941063eb5bfc62be5b20d134
raw_storage_status: public-staging-not-archived
actual_body_file: tmp/day24-tonev134pr-primary-090/body.pdf
nuclei: [134Pr]
reactions: [119Sn-19F-4n-134Pr]
experiments: [euroball-iv-rdds-dsam-134Pr-2006]
models: [tqptr, ibffm, dynamic-chirality]
methods: [recoil-distance, dsam, differential-decay-curve, compton-polarimetry]
observables: [mean-lifetime, B(E2), B(M1), level-scheme]
tags: [134Pr-chirality, dynamic-chirality, lifetime-measurement, companion-matrix]
---

# 134Pr所研究双带的静态极限受到限制，动态解释仍保持条件性

## Bibliographic Record

D. Tonev等，*Physical Review Letters* **96**, 052501 (2006)，DOI [10.1103/PhysRevLett.96.052501](https://doi.org/10.1103/PhysRevLett.96.052501)；received 2005-07-04、published 2006-02-09。本篇为Euroball IV在Vivitron开展的119Sn(19F,4n)134Pr寿命测量原实验，也是[[petrache-2006-near-degenerate-chiral-misinterpretation]] (PE06) Ref. [9] 的寿命来源。

090经APS官方直接PDF链接取得完整5页、347,475 bytes，SHA见frontmatter。落地页无补充材料链接，SI记为未识别。

## Scope and Reading Depth

全文5页、Figs.1–3、Table I以及所有方法/讨论均已读及视觉核。正文明确说明分支比和偏振系数的详细分析留待后续论文（Ref. [15]，待发表）；本篇未提供完整的逐线数值分支比表、内转换系数处理或协方差矩阵。未运行模型producer，未重拟衰变曲线。

## Summary

本文结合RDDS与DSAM测定134Pr双带共14个能级的平均寿命τ。在能级近简并区（I=14+–19+），Band 1的带内B(E2)是Band 2的2到3倍，且两带B(M1)平滑、无奇偶交错。刚性三轴核芯模型（TQPTR）在接近静态极限时预报两带B(E2)趋近且B(M1)强交错，与实验严重不符；允许形状涨落的IBFFM模型再现了实验趋势。作者结论明确：实验结果**不支持静态手征（static chirality）**，若存在手征性，它主要具有**动态手征（dynamic chirality）**特征，或表现为准粒子与核形状自由度的耦合。

## Experimental Setup and DDCM Method

反应119Sn(19F,4n)134Pr在Vivitron加速器上进行，探测阵列为Euroball IV加BGO内球，触发要求Ge cluster/clover≥3且BGO内球≥3。

1. **RDDS**：87 MeV，0.5 mg/cm² 119Sn蒸在1.8 mg/cm² 181Ta背衬，反冲速度v=0.98(2)%c，在6.0 mg/cm² Au中停止；20个距离（电接触至2500 μm），微分衰变曲线法（DDCM）拟合门控移动/未移动成分。
2. **DSAM**：83 MeV，0.7 mg/cm² 119Sn在9.5 mg/cm² 181Ta厚背衬；DESASTOP模拟减速，DDCM线形分析。

Clover环作为Compton偏振计，结合DCO确认ΔI=1以M1为主（E2极小）、ΔI=2为E2。正文说明分支比/偏振系数细节留待Ref. [15]（待发表），未列数值分支/ICC/Cov。

## Key Results

全部新claims needs_review: true。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| TO06-D24-001 | 119Sn(19F,4n)134Pr在Euroball IV结合内球进行RDDS (87 MeV) 与 DSAM (83 MeV) 测量，首次测定两带13个态的平均寿命τ。 | direct-experimental-method | direct-original | PDF1–2 / 052501-1–2 | true |
| TO06-D24-002 | Table I给出Band 1 (10+–18+) 与 Band 2 (13+–17+) 的平均寿命τ（ps）；10+1为4.93(15) ps，与Klemme 1999相符；14+1/15+2两方法相符，表中列统计更高的DSAM值。 | measured-lifetime-ledger | direct-original | PDF3 / 052501-3 Table I | true |
| TO06-D24-003 | 近简并区Band 1带内B(E2)是Band 2的2–3倍；两带B(M1)平缓无奇偶交错。实验不支持静态手征，所比较TQPTR计算的EM预报严重失配。 | transition-strength-behavior | direct-original-plus-model | PDF3–4 Fig3 and discussion | true |
| TO06-D24-004 | 包含核形状涨落的IBFFM模型成功再现带内B(E2)的2–3倍差异、平坦B(E2)走势，并消除了B(M1)交错。 | competing-model-success | model-result | PDF3–4 Fig3 and discussion | true |
| TO06-D24-005 | 作者结论明确为“不支持静态手征”；动态手征或准粒子与核形状自由度的耦合是兼容解释；不能将本文简述为对所有手征模式的绝对否定。 | author-interpretation-and-boundary | direct-original | PDF4 conclusion | true |
| TO06-D24-006 | 分支比和偏振系数细节留待Ref. [15]（待发表）；本文未提供逐线数值分支比表、ICC或协方差矩阵。 | data-completeness-boundary | direct-original | PDF3 text | true |
| TO06-D24-007 | PE06的Ref. [9]引用本篇Tonev 2006用于寿命和带内B定性对比；其解混合模型的分支比引自Starosta待发表论文（Ref. [11]），与Tonev Ref. [15]的引用对象不同；实际事件/标定/Cov独立性未由书目差异证明。PE06是分析，非新实验。 | source-lineage-and-dependence | cross-source-comparison | PDF5 Ref. [15]; PE06 Refs. [9, 11] | true |

## Table I Lifetime Ledger

|带|态 \(I^\pi\)|平均寿命 \(\tau\) (ps)|方法|
|---|---|---:|---|
|Band 1|\(10^+_1\)|4.93(15)|RDDS|
|Band 1|\(11^+_1\)|1.614(326)|RDDS|
|Band 1|\(12^+_1\)|1.425(130)|RDDS|
|Band 1|\(13^+_1\)|0.904(50)|RDDS|
|Band 1|\(14^+_1\)|0.882(147)|DSAM|
|Band 1|\(15^+_1\)|0.608(68)|DSAM|
|Band 1|\(16^+_1\)|0.562(47)|DSAM|
|Band 1|\(17^+_1\)|0.422(30)|DSAM|
|Band 1|\(18^+_1\)|0.249(10)|DSAM|
|Band 2|\(13^+_2\)|1.443(50)|RDDS（按共用方法栏）|
|Band 2|\(14^+_2\)|1.280(50)|RDDS（按共用方法栏）|
|Band 2|\(15^+_2\)|0.887(47)|DSAM|
|Band 2|\(16^+_2\)|0.824(52)|DSAM|
|Band 2|\(17^+_2\)|0.353(49)|DSAM|

## Competing Interpretations and Limitations

本实验确立了134Pr在近简并区的带内跃迁几率不对称（2–3倍），给出了静态三轴手征图像的决定性反证；但它并不排除动态手征或形状涨落下的手征残留。由于缺少完整数值分支比表和逐线协方差矩阵，这些数据不能直接重建高精度的绝对带间B(M1)/B(E2)或闭环相干矩阵元。PE06的两带解混合Q比2.0(4)虽然利用了本篇寿命的不对称性作为定性参照，但其具体混合振幅依赖另一篇待发表工作（Starosta Ref. [11]）的分支比。

## Extracted Pages

- [[chirality-shape-coexistence-companion-matrix]]：Day25 134Pr行直接对应本源实验跃迁几率。
- [[petrache-2006-near-degenerate-chiral-misinterpretation]]：PE06两带解混合模型所引用的寿命 primary。


Day24 self-link: [[tonev-2006-134pr-lifetime-chiral]]
