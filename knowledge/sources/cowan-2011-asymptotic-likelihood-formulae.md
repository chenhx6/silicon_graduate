---
type: source
title: "Asymptotic formulae for likelihood-based tests of new physics"
title_original: "Asymptotic formulae for likelihood-based tests of new physics"
aliases: [cowan-2011-asymptotic-likelihood-formulae]
created: 2026-11-27
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: preprint
reading_depth: read
authors: ["Glen Cowan", "Kyle Cranmer", "Eilam Gross", "Ofer Vitells"]
tags: [nuclear-structure, local-literature-archive]
year: 2011
arxiv: 1007.1727v3
doi: "10.1140/epjc/s10052-011-1554-0"
canonical_source: "doi:10.1140/epjc/s10052-011-1554-0"
raw_file: "raw/papers/gpt/learning-daily/20261102-poisson-audit/cowan-et-al-1007.1727v3.pdf"
raw_sha256: "618783cfea3355b83423609bde70a4b085762353ffc4386cda2621de295df6dd"
raw_storage_status: archived-local
archive_required: true
---

# Asymptotic formulae for likelihood-based tests of new physics

## Bibliographic Record

Glen Cowan, Kyle Cranmer, Eilam Gross and Ofer Vitells, Asymptotic formulae for likelihood-based tests of new physics, arXiv:1007.1727v3 [physics.data-an], 2013-06-24.

物理第 1 页印有 arXiv:1007.1727v3 和 2013 年 6 月 24 日。该日期为预印本版本日期，所给文本未列期刊出版年或本文 DOI。目录第 424 行。启动器核验的归档文件为 raw/papers/gpt/learning-daily/20261102-poisson-audit/cowan-et-al-1007.1727v3.pdf，401434 字节，SHA-256 为 618783cfea3355b83423609bde70a4b085762353ffc4386cda2621de295df6dd。

## Scope and Reading Depth

- {"start_page": 1, "end_page": 8, "sections": "首页、摘要、§1–2 与 §3 开头。图 1 在第 6 页。"}
- {"start_page": 9, "end_page": 22, "sections": "§3.1–3.8 渐近分布与 Asimov 构造，§4 灵敏度、联合通道及误差带，§5 开头。图 2 在第 20 页。"}
- {"start_page": 23, "end_page": 29, "sections": "§5.1 计数算例、§5.1.1 已知背景算例、§5.2 形状分析及 §6 开头。图 3–4 在第 24 页，图 5–6 在第 25 页，图 7–8 在第 27 页，图 9–10 在第 28 页，图 11–12 在第 29 页。"}
- {"start_page": 30, "end_page": 32, "sections": "§6 续、§7 结论、致谢及参考文献 [1]–[18]。"}
- 本次获取的具体覆盖：逐页审核物理第 1–32 页的抽取文本，覆盖 §1–7、图 1–12 的图注、致谢及参考文献 [1]–[18]。图像尚待目检，数值模拟未复算。所给材料没有既有同版笔记可供对照，建议登记本次全文文本覆盖，暂不认定既有覆盖。

## Summary

在单参数 Wald 近似下，有效信号强度估计量近似服从正态分布。背景零假设下，发现统计量 q₀ 的渐近分布由零点质量与一自由度 χ² 分布各占一半组成。按文中的尾概率约定，发现显著度为 √q₀。

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A21-1 | 在单参数 Wald 近似下，有效信号强度估计量近似服从正态分布。背景零假设下，发现统计量 q₀ 的渐近分布由零点质量与一自由度 χ² 分布各占一半组成。按文中的尾概率约定，发现显著度为 √q₀。 | 渐近推导 | source-reported | 物理第 7 页式 (12)，第 9 页式 (17)–(20)，第 14–15 页式 (47)–(53)。 | true |
| A21-2 | Asimov 样本以假定参数下的期望计数填充信号区与控制区。在文中近似下，可用对应的 Asimov 统计量估计中位发现显著度及背景假设下的中位排除显著度，并由估计量的正态分位数估计上限的统计波动带。 | 统计方法 | source-reported | 物理第 10–12 页式 (24)–(32)，第 20 页式 (79)–(81)，第 21–22 页式 (85)–(89)。 | true |
| A21-3 | 作者报告，在 τ=1、名义发现显著度为 4 的双泊松算例中，b 大于约 4 时，渐近显著度与蒙特卡洛所给显著度的差异小于约 10%。作者还报告，在 s 与 b 都很低时，Asimov 的 q₀ 中位数近似会变差。 | 作者报告的模拟比较 | source-reported | 物理第 23–24 页 §5.1 与式 (90)–(93)。图 3、图 4 的尾部及低计数比较待在物理第 24 页目检。 | true |
| A21-4 | 对背景均值 b 已知的单泊松计数，名义信号下的 Asimov 中位发现显著度近似为 √{2[(s+b) ln(1+s/b)−s]}。s/√b 是 s/b 很小时的一阶近似。 | 模型特例 | source-reported | 物理第 26 页 §5.1.1 式 (94)–(98)。 | true |

## Competing Interpretations and Limitations

抽样分布推导依赖 Wilks [1] 与 Wald [2] 的大样本结果、似然模型和对干扰参数的约束。对照依据是作者生成的蒙特卡洛样本。参考文献 [1]–[18] 仅审核本文所列书目及引用位置。

- 泊松计数与形状算例用于验证统计近似。形状算例以 Rayleigh 背景和已知宽度、逐点指定峰位的高斯信号建模。第 27–29 页的逐质量点排除上限不支持全局发现显著度，第 27 页将别处效应指向 [14]。
- 渐近结果依赖有效样本量及模型设定。第 3、9、30 页明确限制了对模型失配和极小样本的外推。第 19 页提及 CLs 比率，并将该步骤交给 [12]。
- 第 29–30 页的 RooStats 内容记录该预印本所述的实现状态。

## Extracted Pages

- {"start_page": 1, "end_page": 8, "sections": "首页、摘要、§1–2 与 §3 开头。图 1 在第 6 页。"}
- {"start_page": 9, "end_page": 22, "sections": "§3.1–3.8 渐近分布与 Asimov 构造，§4 灵敏度、联合通道及误差带，§5 开头。图 2 在第 20 页。"}
- {"start_page": 23, "end_page": 29, "sections": "§5.1 计数算例、§5.1.1 已知背景算例、§5.2 形状分析及 §6 开头。图 3–4 在第 24 页，图 5–6 在第 25 页，图 7–8 在第 27 页，图 9–10 在第 28 页，图 11–12 在第 29 页。"}
- {"start_page": 30, "end_page": 32, "sections": "§6 续、§7 结论、致谢及参考文献 [1]–[18]。"}
