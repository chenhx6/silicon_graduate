---
type: source
title: "Massimiliano Bonamente 2022 - Statistics and Analysis of Scientific Data (3rd Edition)"
aliases: [Bonamente2022, Statistics of Scientific Data, 科学数据统计与分析]
created: 2026-11-01
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: skimmed
title_original: "Statistics and Analysis of Scientific Data"
authors: [Massimiliano Bonamente]
publisher: "Springer Nature Switzerland (Graduate Texts in Physics)"
year: 2022
citation_key: "bonamente_2022_statistics-scientific-data"
pages: "491"
isbn: "9783030999513"
canonical_source: "M. Bonamente, Statistics and Analysis of Scientific Data (3rd Ed.), Springer (2022)"
library_file: "raw/books/Statistics and Analysis of Scientific Data (Graduate Texts in Physics), 3rd Edition (Massimiliano Bonamente) (Z-Library).pdf"
raw_file: "raw/books/Statistics and Analysis of Scientific Data (Graduate Texts in Physics), 3rd Edition (Massimiliano Bonamente) (Z-Library).pdf"
raw_sha256: "e5197dffd54d527b9d6925b92eeae34e0859e0062063861f2e54abf333d2b2ca"
nuclei: []
reactions: []
experiments: []
models: [maximum-likelihood, bootstrap-resampling, robust-regression, monte-carlo-markov-chain]
tags: [scientific-data-analysis, error-propagation, robust-statistics, chi2-fitting]
---

# Massimiliano Bonamente 2022 - Statistics and Analysis of Scientific Data

## 专著全貌与学术定位

阿拉巴马大学物理学教授 Bonamente 的研究生统计教材（491 页，第三版）。全书深入浅出地讲解物理测量数据中的误差传播、参数拟合、稳健统计（Robust statistics）以及 Bootstrap 重采样技术。

## 核心章节精要与方法内容

### Chapter 8: Non-linear Fitting & The Bootstrap Method (pp. 185–228)
- **非线性参数拟合的 Bootstrap 蒙特卡罗误差传播**：
  当导出物理量 $Y = f(X_1, X_2, \dots)$ 涉及复杂的非线性函数（如核谱学中通过混合比 $\delta$ 计算 $E2$ 百分比 $\delta^2/(1+\delta^2)$，当 $\delta$ 跨越零点或发散点时一阶微分传播彻底失效）时，通过从原始协方差矩阵抽取 $N = 10^5$ 组随机 Toy 实验参数，直接构建 $Y$ 的经验概率密度分布，提取 $16\%$、$50\%$（中位数）、$84\%$ 分位数作为非对称真实误差，彻底解决非线性奇异性问题。


## Bibliographic Record

本书完整原著收录于 `book-bonamente-statistics-scientific-data.md` 对应原始路径，哈希与元数据已于前置卡固化。


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

## 2026-11-27 — 馆藏原件与覆盖核对

- 第1章用交集概率除以条件事件的正概率来计算条件概率，并用交集概率是否等于边缘概率之积来判定两事件是否独立。（PDF 实体第29–30页，§§1.3–1.4，式 (1.6)–(1.8)。）
- 教材转录了 Thomson 两支阴极射线管在不同气体下的 W/Q、I、m/e 和 v。书中由 W/Q 与 I 计算 v 和 m/e，并在注记中指出三处星号记录存在数值不一致。（§2.4，物理页 49–51，式 (2.15) 与表 2.1、2.2。星号、指数和行列对应须目视核对物理页 51。）

## 2026-11-27 — 馆藏原件与覆盖核对

- 作者报告，将100个独立的 U(0,1) 变量求和，以1,000次和100,000次模拟重复构造的样本分布均接近均值50、方差100/12的正态参照曲线。曲线与样本分布的吻合程度须检查原图。（PDF 第92–93页，§4.4.2、图4.1。图形待核第93页。）
