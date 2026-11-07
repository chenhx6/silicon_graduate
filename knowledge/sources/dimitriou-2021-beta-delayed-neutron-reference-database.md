---
type: source
title: "Dimitriou 等 2021：β 缓发中子参考数据库与测量方法"
aliases: [IAEA 2021 delayed neutron database]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
source_type: evaluated-data-review
reading_depth: skimmed
title_original: "Development of a Reference Database for Beta-Delayed Neutron Emission"
authors: [P. Dimitriou, I. Dillmann, B. Singh, et al.]
journal: Nuclear Data Sheets
year: 2021
volume: "173"
pages: "144–238"
doi: "10.1016/j.nds.2021.04.006"
arxiv: "2102.01165v1"
citation_key:
canonical_source: "doi:10.1016/j.nds.2021.04.006"
raw_file: "raw/papers/gpt/query/20261108-r3-g52-beta-delayed-particles/dimitriou-2021-iaea-beta-delayed-neutron-database.pdf"
raw_sha256: "ca0b475131704e33f6732163ef996467e630fbea88898dba73cc9f66e7f5684f"
archive_required: true
nuclei: []
tags: [doctoral-foundations, beta-delayed-neutron, efficiency, multiplicity, gamma-competition]
---

# β 强度、粒子通道与探测计数之间的三层关系

## Bibliographic Record

官方Crossref核定卷页DOI。本地为96物理页arXiv v1；
不能把期刊95页跨度当本地PDF页数。

## Scope and Reading Depth

G52定向学习；总控核PDF4–11的定义与效率、17–18的评价/近似、
21与24的模型比较，以及84–85的结论。其余核素表、谱评价和全部96页未逐条审核。
不把2020截止的数据数目称为2026全世界现状。

## Summary

IAEA协调评价系统区分缓发中子分支、多重度、谱与测量响应，并比较β结构和通道竞争。评价不等于独立的新测量。

## Key Results

| claim | claim_kind | evidence_level | locator | boundary |
|---|---|---|---|---|
| P1n为恰发一个中子的衰变数除以母态衰变数 | evaluated-definition | located-review | PDF4, Eq.(1) | 不等于平均中子数 |
| 简化βn计数公式要求β效率可相消，实际应取通道相关效率平均 | measurement-method | located-review | PDF6–7, Eqs.(2)–(4), Figs.2–3 | 不能将平均乘积无条件改为平均之积 |
| 多中子发射会迁移到较低探测多重度，须处理效率及偶然符合 | measurement-method | located-review | PDF6–7 | 不用单一εn消除全部响应 |
| TAGS提供独特约束，但中子相互作用的模拟与验证重要 | review-method-comparison | located-review | PDF11, Sec.II.C.1 | 不是所有βn实验唯一合格仪器 |
| GT/FF、Q值、复杂组态和通道竞争共同影响Pn与半衰期 | review-model-comparison | located-review | PDF21,24,84–85 | 不从Pn单独归因形变或壳隙淬灭 |

## Competing Interpretations and Limitations

sharp cutoff、统计Hauser–Feshbach及逐态处理有不同输入/适用域。
评价建议与原始测量不是相互独立的证据。未经本轮核的Cd能级排序、
固定FF比例或任意质量偏差效应不从worker报告移入。

## Extracted Pages

- [[doctoral-r3-weak-operators-and-delayed-particles-20261108]]
