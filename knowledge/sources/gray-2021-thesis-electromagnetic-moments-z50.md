---
type: source
title: "Gray 2021 - Electromagnetic moments and emerging nuclear collectivity near Z=50"
aliases: [Timothy Gray ANU thesis, 130Sn core B(E2) re-tabulation]
created: 2026-09-29
updated: 2026-09-29
status: active
review_status: unreviewed
source_type: doctoral-thesis
reading_depth: skimmed
citation_key: Gray2021ANU
title_original: "Electromagnetic Moments and Emerging Nuclear Collectivity near Z=50"
authors: [Timothy J. Gray]
institution: Australian National University
year: 2021
doi: 10.25911/yd6j-qk37
language: en
canonical_source: "https://openresearch-repository.anu.edu.au/handle/1885/224114"
raw_file: "raw/papers/gpt/learning-daily/20260928-DAY2-shell-gap-single-particle/gray-2021-anu-thesis-z50-electromagnetic.pdf"
raw_sha256: 3ff5dc98a995e43133b23889900a3b579e57413a4a836e7264b9c870389fe152
related_raw_files: ["raw/papers/gpt/learning-daily/20260928-DAY2-shell-gap-single-particle/radford-2005-130sn-coulex-source.pdf"]
nuclei: [128sn, 130sn]
reactions: []
experiments: []
models: [shell-model]
observables: [b-e2, g-factor]
methods: [doctoral-thesis, literature-synthesis]
tags: [sn130, sn128, b-e2, z50, thesis, source-lineage]
---

# Gray 2021 thesis: 130Sn core B(E2) cross-check

## Bibliographic Record

Timothy J. Gray, Electromagnetic Moments and Emerging Nuclear Collectivity near Z=50, PhD thesis, Australian National University, 2021, DOI 10.25911/yd6j-qk37. The public ANU repository PDF was downloaded from the record’s citation_pdf_url and hash-verified.

## Scope and Reading Depth

Targeted source check of Chapter 3 Table 3.13 and its References [20] and [28], not a full-thesis review. The thesis studies Coulomb excitation of 129Sb and related Z=50-region structure; Table 3.13 cites prior experimental core B(E2) strengths for 128Sn and 130Sn.

## Summary

Gray’s Table 3.13 lists the experimental 130Sn core B(E2) as 5.9(1.3) W.u. The table note points to references [20] and [28]; the reference list identifies [28] as Radford et al., European Physical Journal A 25, Supplement 1, 383–387 (2005), DOI 10.1140/epjad/i2005-06-205-y. This is a dependent re-tabulation of the Radford 130Sn result, not an independent Coulomb-excitation experiment. The 5.9(1.3) W.u. entry agrees with conversion of Radford’s 0.023(5) e2b2 using the standard Weisskopf E2 unit at A=130.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GRAY21-1 | Gray’s Table 3.13 lists the 130Sn core B(E2) as 5.9(1.3) W.u. | secondary-compilation | contextual | Chapter 3, Table 3.13, printed p.75 | true |
| GRAY21-2 | The same table’s source note cites references [20] and [28]; the bibliography identifies [28] as Radford et al. 2005 EPJ A 25 S1, 383–387, DOI 10.1140/epjad/i2005-06-205-y. | source-lineage | contextual | Chapter 3, Table 3.13 note and bibliography, printed p.81 | true |
| GRAY21-3 | Table 3.13 separately lists the 128Sn core B(E2) as 20.9(1.3) W.u., with its cited Allmond et al. 2011 source; this is not an independent dataset from that citation. | secondary-compilation | contextual | Chapter 3, Table 3.13, printed p.75 | true |

## Source Lineage and Independence

The thesis table is a later re-tabulation. Its 130Sn value is traceable to Radford et al. 2005 and must not be counted as an independent measurement. The thesis also treats 128Sn as a core input and cites Allmond et al. 2011 for that value.

## Competing Interpretations and Limitations

This thesis cross-check supports the numerical conversion to 5.9(1.3) W.u.; it does not resolve why the Radford conclusion describes the value as “around 1.4 single-particle units.” The 2005 paper’s B(E2) remains preliminary, and the thesis is dependent on that source.

## Extracted Pages

- Chapter 3, Table 3.13 and its note (printed p.75).
- Bibliography References [20] and [28] (printed p.81).

## Related Knowledge

- [[radford-2005-130sn-coulomb-excitation-126-130sn]]
- [[a130-shell-gap-orbital-observable]]


## 2026-11-22 — Chapter 3 定位与年份复核

馆藏件为 270 页。PDF 1 题名页印 2020，题录沿用 ANU 馆藏登记年 2021，两者分别记录。PDF 69–108 对应印刷 43–82 的 129Sb 库仑激发章节。PDF 101（印 75）式 (3.20) 分开质子项、中子项与干涉交叉项。Table 3.13 把 130Sn 的 5.9(13) W.u. 列为既有核心强度，将其与 129In、131Sb 的壳模型分量并列。PDF 107–108 的引文依赖保留。整卷其余章节待分段核验，未计整件阅读。


## 2026-11-22 — 全件阅读与各实验的证据边界

- PDF 1–26 为题名、摘要和目录，PDF 27–68 为背景和电磁观测方法，PDF 69–108 为 129Sb 库仑激发。PDF 238（印 212）Fig. 7.1 把 129Sb 实验激发强度和 128Sn 的既有核心强度并列，并分列两套壳模型结果。该图与 Table 3.13 的质子、中子和相干项并列使用时，须保留每列的来源。
- PDF 109–170 为 138Xe β 延迟谱。PDF 121（印 95）§4.4.1 看不到清晰的预进动信号，PDF 152–153 从植入和有效超精细场讨论测量灵敏度。PDF 238 把 1866 keV 的 \(2_3^+\) 列为 mixed-symmetry 候选，并指出不同核的形状参数基于壳模型矩阵元及求和规则。该图未提供这些态的新实验绝对 E2 闭合网络。
- PDF 171–200 为 130Sn 异能态 TDPAD。PDF 186 的联合拟合给 \(g=-0.31(2)\)，PDF 189–194 对低计数重分箱、旧 128Sn 结果和统计灵敏度作独立检查。PDF 196 与 239 将 130Sn 结果标为初步。PDF 201–236 为 Cd/Sn 实验，其中 PDF 215–216 的 111Sn 两组分别拟合 \(-0.213(4)\) 和 \(-0.214(4)\)，作者采用 \(-0.214(4)\)。两组共享以 113Sn 取得的场分布（PDF 215 Fig. 6.16，均值 \(-30.2(5)\) T、FWHM 4.0(7) T）。
- PDF 237–242 总结各采集。PDF 243–251 含 Kumar–Cline 附录，PDF 247（印 221）列两阶求和的角动量重耦合。PDF 252–261 和 262–270 是两篇附印作者稿，分别讨论 Cd 的时差超精细校准及 Ge/Ga 在 Fe、Gd 中的场。附印稿的物理页与页眉单独定位，作者所述的相关数据、场假设及再分析沿用各自的实验谱系。

原件题名页印 2020。DOI 题录登记 2021，接受与可用日期均为 2021-02-22。两者记录不同环节。
