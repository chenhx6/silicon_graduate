---
type: source
title: "Kumar et al. 2023 — 磁转动与反磁转动结构综述（arXiv 2303.00499）"
aliases: [Kumar 2023 AMR review, 2303.00499]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
source_type: review
reading_depth: read
title_original: "Review of magnetic- and antimagnetic-rotational structures in nuclei"
authors: [Sushil Kumar, Sukhjeet Singh, Balraj Singh, Amita, Ashok Kumar Jain]
journal: "Atomic Data and Nuclear Data Tables (prepublication arXiv version)"
year: 2023
pages: "105 PDF pages"
doi: ""
citation_key: Kumar2023_AMR_review_arXiv
citation_key_origin: arxiv
citation_key_verified: 2026-10-29
canonical_source: "arXiv:2303.00499"
raw_file: "raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/kumar-2023-amr-review-arxiv2303.00499.pdf"
raw_sha256: "1af5160c1055852abcc151c2588af5cbd99649fd394471d246de451de78f54dd"
nuclei: [100Pd, 101Pd, 102Pd, 103Pd, 104Pd, 105Pd, 106Cd, 107Cd, 108Cd, 109Cd, 110Cd]
models: [review-of-experimental-and-theoretical-AMR]
observables: [BE2, BM1, J2, level-lifetime, configuration]
methods: [literature-review, ENSDF, XUNDL, NSR]
tags: [antimagnetic-rotation, Pd-systematics, Cd-systematics, evidence-boundary]
---

# Kumar 等：AMR 结构综述与 Pd 质量区证据边界

## Bibliographic Record

Sushil Kumar 等，*Review of magnetic- and antimagnetic-rotational structures in nuclei*，arXiv:2303.00499。实际载荷为105页PDF，SHA-256为`1af5160c1055852abcc151c2588af5cbd99649fd394471d246de451de78f54dd`。文稿摘要说明其文献截止日为2025年3月31日；因此这里记录的是综述版本及其截止范围，不将其当作已经核验的期刊终稿。

## Scope and Reading Depth

实际读取全文文本及Pd/Cd相关章节、Table 3说明和参考文献。该综述汇总40条AMR结构、28个核，并指出Pd、Cd、In区域共有29条候选/已报告AMR带。综述同时强调许多带缺乏寿命、B(E2)或B(M1)数据，部分归属仍属tentative。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KU23-01 | 综述将Cd与Pd视为AMR研究最成熟的质量区之一，但指出firm evidence仍稀少，许多带缺寿命和电磁强度。 | review-synthesis | direct-review | PDF pp8–10, abstract | true |
| KU23-02 | Pd相关参考链明确包括100Pd、101Pd、102Pd、103Pd与104Pd；本综述的Pd参考与Table 3未列出106Pd或108Pd的AMR带。 | review-scope-absence | direct-review | PDF pp99–101, Table 3 references | true |
| KU23-03 | 100Pd的AMR归属仅有少数寿命点，102Pd等若干案例在综述中被标为较不确定；因此“Pd同位素均有确立AMR”不能成立。 | review-qualification | direct-review | PDF pp9–10, Table 3 notes | true |
| KU23-04 | 综述给出的AMR一般识别线索包括弱且随自旋下降的B(E2)、较大的J(2)/B(E2)，但这些是经验特征汇总，不是无条件的数值硬门。 | review-synthesis | direct-review | PDF p9 | true |
| KU23-05 | Pd的理论参考发展到104Pd及奇A 103/105Pd等；未见同一综述中106/108Pd的对应理论链。 | review-scope-absence | direct-review | PDF pp100–105 | true |

## Summary

截至综述截止范围，104Pd是偶偶Pd中有直接DSAM E2证据并被作者称为AMR的关键实例；106Pd、108Pd不能因Z=46和g9/2空穴壳层相似就自动当作已建立AMR。对于这两个核，应将结论标为“本次综述未核验到AMR归属”，而不是绝对不存在。

## Extracted Pages

- [[amr-global-nuclide-distribution-configuration-confidence-audit]]

- [[amr-pd-four-hole-geometry-evolution-audit]]
- [[antimagnetic-rotation]]

## Competing Interpretations and Limitations

综述的“未列出”是范围和检索结果边界，不是对全世界文献的不存在证明。综述表格整合了原始实验和模型，重复引用不等于独立证据；Pd个别带可能有高自旋谱学但没有AMR所需寿命和E2趋势。

## Knowledge Impact and Learning Decision

该页为Pd跨同位素比较提供文献范围边界：104Pd可继续做原件模型审计，106/108Pd需先建立原始高自旋和寿命来源，不能凭四空穴几何外推实验归属。

## Human Review

Codex review self-audit；保持`unreviewed`。

## Review Status

综述全文已读；原始Pd 106/108实验资料仍未建立独立来源链。
