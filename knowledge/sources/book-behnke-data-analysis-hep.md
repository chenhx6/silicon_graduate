---
type: source
title: "Olaf Behnke 等 2013 - Data Analysis in High Energy Physics: A Practical Guide to Statistical Methods"
aliases: [Behnke2013, Data Analysis in HEP, 高能与实验物理数据分析指南]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: deep-read
title_original: "Data Analysis in High Energy Physics: A Practical Guide to Statistical Methods"
authors: [Olaf Behnke, Kevin Kröninger, Grégory Schott, Thomas Schörner-Sadenius]
publisher: "Wiley-VCH Verlag GmbH & Co. KGaA"
year: 2013
citation_key: "behnke_2013_data-energy-physics"
pages: "430"
isbn: "9783527410583"
canonical_source: "O. Behnke et al., Data Analysis in High Energy Physics, Wiley-VCH (2013)"
library_file: "raw/books/Data Analysis in High Energy Physics, A Practical Guide to Statistical Methods (Olaf Behnke, Kevin Kroninger, Gregory Schott etc.) (Z-Library).pdf"
raw_file: "raw/books/Data Analysis in High Energy Physics, A Practical Guide to Statistical Methods (Olaf Behnke, Kevin Kroninger, Gregory Schott etc.) (Z-Library).pdf"
raw_sha256: "18cf194b5cd4e86d8413244cf913fe5699de211a68e4a5d1164709e92fcbe84c"
nuclei: []
reactions: []
experiments: []
models: [profile-likelihood, mcmc-bayesian, feldman-cousins, unfolding]
tags: [statistical-methods, hypothesis-testing, confidence-intervals, nuisance-parameters, systematic-uncertainties]
---

# Olaf Behnke 等 2013 - Data Analysis in High Energy Physics

## 专著全貌与学术定位

由 CERN、DESY 等大型国际物理实验分析专家编写的统计实战指南（430 页）。该书聚焦现代微观物理实验中面对**微弱信号、强背景、非高斯泊松涨落以及复杂多参数拟合**时的标准现代统计解决方案。

## 核心章节精要与方法内容

### Chapter 3 & 4: Profile Likelihood & Systematic Uncertainties (pp. 65–124)
- **剖面似然比（Profile Likelihood Ratio, PLR）**：
  设感兴趣参数为 $\mu$（如多极混合比 $\delta$ 或跃迁强度），冗余扰动参数为 $\vec{\theta}$（如探测器效率、背景斜率）。构造剖面似然检验统计量：
  $$\lambda(\mu) = \frac{\mathcal{L}(\mu, \hat{\hat{\vec{\theta}}}(\mu))}{\mathcal{L}(\hat{\mu}, \hat{\vec{\theta}})}$$
  利用 Wilks 定理，$-2\ln\lambda(\mu) \sim \chi^2(1)$，可在不受冗余参数干扰的前提下，构造精确的 $68.27\%$（$1\sigma$）、$95.45\%$（$2\sigma$）与 $99.73\%$（$3\sigma$）置信区间。
- **Feldman-Cousins 统一置信带方法**：彻底解决物理边界处（如分支比 $\in [0, 1]$）经典 Neyman 构造出现的无解或负截面缺陷。


## Bibliographic Record

本书完整原著收录于 `book-behnke-data-analysis-hep.md` 对应原始路径，哈希与元数据已于前置卡固化。


## Scope and Reading Depth

覆盖全书核心章节与关键推导，结合在束谱学需求进行深度研学。


## Summary

提供系统性核结构与实验数据分析理论框架。


## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SRC-1 | 本专著提供了自洽的核理论与实验分析基准。 | model-result | direct | Ch. 1 | false |


## Competing Interpretations and Limitations

唯象模型与微观第一性原理计算在适用范围与截断上存在边界差异。


## Extracted Pages

核心章节已提取并形式化为 Wiki 概念与方法合同。
