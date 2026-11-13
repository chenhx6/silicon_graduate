---
type: source
title: "Gysbers 等 2019：从头算多体关联与手征两体流对原子核 β 衰变淬灭的微观解释"
aliases: [Gysbers 2019 Nature Physics, arXiv:1903.00047, gysbers-2019-beta-decay]
created: 2026-11-13
updated: 2026-11-13
status: active
review_status: unreviewed
source_type: preprint-and-journal-article
reading_depth: skimmed
title_original: "Discrepancy between experimental and theoretical beta-decay rates resolved from first principles"
authors: [P. Gysbers, G. Hagen, J. D. Holt, G. R. Jansen, T. D. Morris, P. Navrátil, T. Papenbrock, S. Quaglioni, A. Schwenk, S. R. Stroberg, K. A. Wendt]
journal: Nature Physics
year: 2019
volume: "15"
pages: "428–431"
doi: 10.1038/s41567-019-0450-7
arxiv: 1903.00047v1
language: en
canonical_source: "https://doi.org/10.1038/s41567-019-0450-7; local arXiv:1903.00047v1 preprint"
citation_key: gysbers-2019-ab-initio-beta-decay-quenching
raw_file: raw/papers/gpt/query/20261113-A130-axial-currents/gysbers-2019-arxiv1903.00047v1.pdf
raw_sha256: f11beb0975ed129c8bbd2addcf1485fb25fa248ec375cb804001a17a96e2e25e
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/papers/gpt/query/20261113-A130-axial-currents/manifest.json
actual_read_pages: [1, 2, 3, 4]
actual_read_scope: "第1页题目与Fig.1(空心/实心符号区分1BC与2BC对实验B(GT)的描述)；第2页手征EFT弱两体流(2BC)与高阶组态混合；第3–4页100Sn超允许衰变与从头算耦合道计算方法选读。不代表全20页所有补充材料均已精读。"
nuclei: [100sn, 14c]
reactions: []
experiments: []
models: [chiral-effective-field-theory, no-core-shell-model, valence-space-imsrg, coupled-cluster]
observables: [gamow-teller-strength, beta-decay-half-life]
methods: [ab-initio-chiral-currents, two-body-weak-currents]
tags: [A130, beta-decay, gamow-teller, quenching, two-body-currents, ab-initio, 100sn]
---

# Gysbers 等 2019：从头算多体关联与弱两体流

## Bibliographic Record

P. Gysbers 等 2019 年在 Nature Physics 发表研究（预印本 arXiv:1903.00047v1），题为 *Discrepancy between experimental and theoretical beta-decay rates resolved from first principles*。本地持有原始预印本 PDF（20 页）及 arXiv 记录网页快照。

## Scope and Reading Depth

本记录基于预印本 PDF 第 1–4 页定向选读：
- 第 1 页：题名、作者与 Fig. 1（轻核至 $^{100}\mathrm{Sn}$ 的 $B(GT)$ 强度随质量数演化，空心符号标单一单体流 1BC，实心符号标 1BC+2BC）。
- 第 2 页：手征有效场论弱两体轴矢量流（2BC）的引入及其与三体力相当的微观阶次。
- 第 3–4 页：$^{100}\mathrm{Sn} \to {}^{100}\mathrm{In}$ 强 Gamow-Teller 跃迁的耦合簇计算与讨论。

未精读 Supplementary Information 全部 16 页推导与核力拟合细节。

## Summary

Gysbers 等（2019）基于手征有效场论相互作用与弱电流算符，利用从头算无芯壳模型（NCSM）、价空间 IMSRG 与耦合簇（CC）方法计算从轻核到双闭壳 $^{100}\mathrm{Sn}$ 的 Gamow-Teller $\beta$ 衰变强度。作者在所考察的相互作用与多体截断下同时纳入关联与手征弱两体流（2BC），比较其对强跃迁的影响。PDF 第2页进一步明确：先加入关联还是先加入2BC，会改变对“主要来源”的分配，分配也随相互作用分辨率变化。不能从这项比较归纳出跨框架固定的机制主次顺序。

## Key Results

| ID | 声明与物理内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GYSBERS-1 | 从头算计算中联合纳入大空间粒子-空穴多体关联与手征弱两体流（2BC），在不引入人为唯象淬灭因子的前提下，计算的 Gamow-Teller 衰变强度与实验在所考察核区达到良好一致。 | model-result | direct | PDF p. 1, Fig. 1 & p. 2 | false |
| GYSBERS-2 | 在作者的比较中，先纳入关联或先纳入2BC，得到不同的“主要来源”分配；相对贡献还随EFT相互作用的分辨率变化。这是同一理论比较的归因边界，不是两个可独立相加的实验贡献。 | model-comparison-and-attribution-boundary | direct-original-parent-check | PDF p.2，讨论 resolution scale 与两种纳入顺序的段落；补充Fig.6为作者回指，本轮未逐点复算 | false |
| GYSBERS-3 | 题名“...resolved from first principles”代表原作者在所计算特定核素序列上的理论结论，不能作为全核区所有弱衰变过程（包括不同动量转移与禁戒跃迁）均已完备解决的终极定论。 | scope-boundary | task-deduction | PDF p. 1 title & text boundary | false |

## Competing Interpretations and Limitations

作者结论展示了从头算理论对低能基态到低激发态 Gamow-Teller 跃迁的自洽解释路线。但在远离闭壳的形变核以及高激发态巨共振连续谱分布中，微观模型对核力低能常数选择仍有依赖；不同多体方法在处理大动量转移虚中微子交换时不可机械平移此结论。

## Extracted Pages

选读范围覆盖预印本 PDF 第 1–4 页。核心图表为 Fig. 1（对比单体流 1BC 与全流 1BC+2BC），相关微观关联与弱两体流相容性结论提取至 [[a130-rewrite-axial-operator-scope-20261113]]，作为博士论文第 2.7 节弱算符重整化讨论的理论依据。
