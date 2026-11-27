---
type: source
title: "Kumar et al. 2023 — 磁转动与反磁转动结构综述（arXiv 2303.00499）"
aliases: [Kumar 2023 AMR review, 2303.00499]
created: 2026-10-29
updated: 2026-11-27
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

## 2026-11-27 — 馆藏原件与覆盖核对

- {"start": 1, "end": 13, "sections": "题名页、目录、正文第1–6节、表1（第4页）、图1–4图注（第5、7、8、9页）、式(1)（第5页）、致谢及正文参考文献 [1]–[34]。"}
- {"start": 14, "end": 15, "sections": "第7节数据政策与第8节表格说明，含数据来源、括号和未知能量基准的约定。"}
- {"start": 16, "end": 76, "sections": "表2，MR 能级、跃迁及逐带注释。"}
- {"start": 77, "end": 86, "sections": "表3，AMR 能级、E2 强度及逐带注释，Pd 条目集中于第78–80页。"}
- {"start": 87, "end": 98, "sections": "表2参考文献。"}
- {"start": 99, "end": 101, "sections": "表3参考文献。"}
- {"start": 102, "end": 105, "sections": "MR 与 AMR 理论参考文献。"}
- 本次获取的具体覆盖：逐页审读所给物理第1–105页的抽取文本，覆盖正文、表格文本、可提取图注及全部参考文献区段，重点核对表3的 Pd 带条目和引用链。图1至图4均有可读图注，图像、版面及字形未目视核验。管理者需翻检物理第5页图1、第7页图2、第8页图3及第9页图4。建议采信既有记录的同版全文文本覆盖，按本回执修订书目与证据表述，并保留待目视复核状态。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A22-1 | 正文报告收录117个核素的228条 MR 带。按表3的核素标题与带号复点，共28个核素、40条 AMR 带，其中 Pd、Cd、In 分别占8、12、9条。结论报告只有12个核素的15条 AMR 带有寿命数据。 | 综述统计 | source-reported | 物理第3页第1节，第10–11页第6节，第77–86页表3。 | true |
| A22-2 | 综述为 ¹⁰⁴Pd 带1列出16⁺至24⁺各级的 B(E2)，中心值由0.26(3)降至0.07(1) (eb)²。26⁺仅给出 B(E2)>0.02 (eb)² 和平均寿命<0.66 ps。引用这些数值前需目视核对第80页的列对齐和不等号。 | 综述转录的实验结果 | source-reported | 物理第80页表3，¹⁰⁴Pd 带1及注2、5。第99页表3书目 2014Ra11。 | true |
| A22-3 | 双剪刀模型中，两支质子角动量向中子角动量方向合拢，横向磁矩相消。图注将总角动量写为剪刀贡献与核芯转动贡献之和，正文将 π 转动对称性与弱的带内 ΔI=2 E2 跃迁联系起来。矢量方向和公式下标待目视核对第9页。 | 模型解释 | source-reported | 物理第8–9页第4节及第9页图4。 | true |
| A22-4 | ¹⁰²Pd 的 1997Gi10 实验文献将该带解释为规则转动带，2018Ji02 的 TAC-CDFT 研究提出集体转动混合可能的 AMR，表3未列该带寿命或 B(E2)。¹⁰⁴Pd 带1的两质子空穴组态来自半经典粒子转子模型。 | 归属与模型比较 | source-reported | 物理第79页表3 ¹⁰²Pd 带1，第80页表3 ¹⁰⁴Pd 带1注1，第99–100页表3书目。 | true |

本件是汇编综述。第14–15页说明数据通常取自逐带所列原始论文首引，部分能级由 ENSDF 补入或由编者推导，部分 B(M1)/B(E2) 由编者按式(1)计算。XUNDL 和 NSR 辅助补全与检索。同一研究在正文、表后书目或理论书目重复出现时按同一证据链计。

- 将 Wiki 标题及年份字段中的2023明确标为归档标识沿用信息，正式出版年和本文 DOI 留空。期刊字段注明第1页为拟刊声明，单列2025年3月31日的文献截止日。
- 将 KU23-02 和 KU23-05 的范围定位写实。表3第78–80页的 Pd 带条目为 ⁹⁹Pd 至 ¹⁰⁴Pd。¹⁰⁵Pd 出现在第100、105页的理论文献 2022Pa27 题名中。第89页表2书目 1996Po07 已提到 ¹⁰⁸Pd 高自旋谱学。¹⁰⁶Pd、¹⁰⁸Pd 的结论限定为本版表3未收录其 AMR 带，且第102–105页理论书目未见两者的专门 AMR 条目。
- 将 KU23-03 的 ¹⁰⁰Pd 寿命表述分期。第9页的两个寿命点指 Zhu 等2001年研究。第78页表3另列 2020Si20 的两个寿命测值和一个寿命上限。将摘要中的 ¹⁰⁴Pd 方法表述改为综述表3汇编了寿命与 B(E2) 证据，DSAM 方法名待核 2014Ra11 原文。
- 将 KU23-04 的大比值具体写为第9页作者提出的经验参考值 J(2)/B(E2)≥100 ħ² MeV⁻¹ (eb)⁻²。表3中的 ¹⁰⁶Cd 带2–3均有低于该值的低自旋点，见第80–81页。采用该比值时保留逐带趋势、寿命和归属语境。
- 引用 AMR 核素分类时，标明第10页将偶偶核写为12个，而按物理第77–86页表3逐核素归类为13个奇A核、10个偶偶核和5个奇奇核，合计28个。第10页的区域外带数也不宜直接采用，按表3的29条 Pd、Cd、In 带计算，区域外为11条。
