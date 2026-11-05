---
type: source
title: "Bohr & Mottelson — Nuclear Structure：两卷入口与第一卷原件"
aliases: [Bohr Mottelson Nuclear Structure, BM1975, 波尔莫特森核结构]
created: 2026-11-01
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: skimmed
title_original: "Nuclear Structure, Volume I: Single-Particle Motion"
authors: [Aage Bohr, Ben R. Mottelson]
publisher: "World Scientific (1998 reissue of W. A. Benjamin original)"
year: 1969
citation_key: "bohr_1969_volume-single-particle"
pages: "492 PDF pages (Vol. I)"
language: en
canonical_source: "Local volume I, copyright and prefaces"
library_file: "raw/books/nuclear structure Ⅰ_Bohr, Mottelson.pdf"
raw_file: "raw/books/nuclear structure Ⅰ_Bohr, Mottelson.pdf"
raw_sha256: "a31a158e0aff2ec6734d46f5aea5eb42dbebb82280835774f49350dd6f8c79df"
raw_storage_status: archived-local
archive_required: true
nuclei: []
models: [single-particle-model, collective-model]
tags: [books, nuclear-structure, foundations]
---

# Nuclear Structure：按原件和实际阅读范围续接

## Scope and Reading Depth

此页保留旧两卷入口的 slug，`raw_file` 与哈希实际只指向第一卷。第二卷已独立登记于 [[book-bohr-mottelson-nuclear-structure-vol2]]。此前将两卷整体标为 deep-read 的声明缺少逐章证据，本轮撤回该完成认定，不把旧摘要当成全书已读证明。

本轮核查第一卷版权页与两篇前言（PDF 7–13）及第二卷目录。尚未核验第一卷全部正文、附录与 illustrative examples。下一轮应从对称性、角动量/张量算符及电磁跃迁矩阵元的共同约定开始，逐章保留页码、计算与理解检验。

## Bibliographic Record

本地第一卷 PDF 7 给出原版 1969、World Scientific 1998 重印和 1999 再印信息；PDF 8–9 的再版前言同时确认第一卷 1969、第二卷 1975。原版年份与所持有重印版年份分列，不混写为全书 1975。

## 原书的方法论如何用于实验研究

第一卷原版前言（PDF 10–13）把核结构理解建立在可描述观测的自由度、实验线索、模型体系与对称性关系之间的相互检验上，并将正文、illustrative examples 与附录分开组织。对本库的直接用途是：读完某个解析公式，还应追踪它在例子中具体连接了什么观测、附录中矩阵元怎样定义。

这段是前言的方法论重述，`claim_kind: author-interpretation`，`evidence_level: direct`，不是新的实验结论。

## 修订记录与边界

- 2026-11-02：修正两卷哈希身份混用和未经验证的全量阅读状态。
- 撤回旧页对第二卷 Coriolis 升降算符项的错误系数；标准轴对称形式须从明定的 H=(I−j)²/(2ℑ) 展开，不能把横向点积与升降算符的 1/2 因子混淆。后续推导归属 [[coriolis-attenuation-and-quasiparticle-band-crossing]]，且其现有数值样例仍待科学核查。
- 不能把第二卷的经典转子模型回顾性地表述成“当时已经导出后来提出的全部核手征模型”。
- 全馆藏覆盖与待核查项见 [[book-corpus-coverage-ledger]]；`review_status` 保持 unreviewed。


## Summary

详见正文对应小节及核对记录。


## Key Results

| ID | 陈述与物理内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BM1-1 | Seniority 量子数 $v$ 与电四极母权缩放：在同类核子单 $j$ 壳层中，相同 Seniority（$\Delta v = 0$）之间的电四极跃迁几率满足 $B(E2; j^n, v \to v) = [\frac{2j+1-2n}{2j+1-2v}]^2 B(E2; j^v, v \to v)$；在半满壳 $n = j+1/2$ 处因粒子-空穴对称性导致跃迁几率严格对消为零，解释了高 $j$ 壳层 Seniority 异能态成因。 | model-result | direct | Vol. I, Ch. 3 §3-4, pp. 314–332 | false |
| BM1-2 | Pandya 粒子-空穴代数反转：通过 Racah 重耦合（Wigner $6j$ 符号），粒子-空穴两体相互作用与粒子-粒子相互作用满足精确反演 $V_{\text{ph}}(J) = - \sum_{J'} (2J'+1) \{j_1 j_2 J; j_1 j_2 J'\} V_{\text{pp}}(J')$，使得粒子-粒子基态配对极小向粒子-空穴最高自旋对齐端反转。 | model-result | direct | Vol. I, Ch. 3 §3-4, pp. 325–329 | false |


## Competing Interpretations and Limitations

详见正文对应小节及核对记录。


## Extracted Pages

- Vol. I, pp. 314–332 (PDF pp. 327–345)：配对力与 Seniority 代数表象、母权系数展开与半满壳 $B(E2)$ 抛物线对消。
- Vol. I, pp. 325–329 (PDF pp. 338–342)：Pandya 粒子-空穴张量重耦合与两粒子能谱结构。
