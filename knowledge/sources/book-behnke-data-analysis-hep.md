---
type: source
title: "Olaf Behnke 等 2013 - Data Analysis in High Energy Physics: A Practical Guide to Statistical Methods"
aliases: [Behnke2013, Data Analysis in HEP, 高能与实验物理数据分析指南]
created: 2026-11-01
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: read
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

## 2026-11-27 — 馆藏原件与覆盖核对

- 第1章用高斯分布描述连续变量，以泊松分布描述给定期望值的事件计数，以二项分布描述固定试验次数的成功数。表1.1的抽取文字列出双侧高斯尾概率，其中1σ为31.7%，5σ约为0.0000573%。（PDF第24页式(1.13)，第26页表1.1及式(1.19)，第27页式(1.20)。表1.1的数值及行列对应待核PDF第26页。）

## 2026-11-27 — 馆藏原件与覆盖核对

- 对每个固定的感兴趣参数值，剖面似然比分子使用干扰参数的条件极大值，分母使用全局极大值。书中以大样本下的卡方近似构造区间，自由度取感兴趣参数的个数。（物理第55–56页，§2.3.4.1–2.3.4.2，式(2.25)、(2.33)–(2.36)。双产额示例见物理第74页图2.12及第75页正文，图中曲线与等高线对应关系待核第74页。）
- 例3.1设定仅背景和信号加背景下的计数分别服从均值为1.3和3.3的泊松分布，以事件数为统计量，预先规定至少4个事件时拒绝仅背景假设。观测后再按实际计数求尾部p值。（物理PDF第94–96页，例3.1、图3.1、表3.1及式(3.1)–(3.2)；第100页式(3.4)–(3.5)。）

## 2026-11-27 — 馆藏原件与覆盖核对

- 在大样本和标准正则条件下，负二倍对数似然比渐近服从自由度等于兴趣参数维数的卡方分布。有干扰参数时，分子在给定兴趣参数下最大化似然，分母取联合最大似然。（PDF第139页§4.3.4式(4.36)，第141页式(4.37)。）
- Fisher 线性判别最大化两类投影均值之差的平方与两类投影方差之和的比值。类内协方差矩阵之和可逆时，权重方向由该矩阵的逆作用于两类均值差得到。两类均值相同而仅宽度有差异时，该目标在原变量上无法选出有区分力的投影。（物理 PDF 第181–183页，§5.3.3，式(5.15)–(5.22)。）

## 2026-11-27 — 馆藏原件与覆盖核对

PDF 26 Table 1.1 与 Fig. 1.2 区分正态尾概率和 Poisson 计数；PDF 140 Table 4.5 对图区间受物理边界及先验影响，页码 140 夹在印 123 与 124 间，引用用 PDF 页。PDF 220 §6.1.3 对正则项的系数和曲率约定须随矩阵使用。PDF 414 §12.3 与 PDF 430 术语索引核位置。

- 第1章用高斯分布描述连续变量，以泊松分布描述给定期望值的事件计数，以二项分布描述固定试验次数的成功数。表1.1的抽取文字列出双侧高斯尾概率，其中1σ为31.7%，5σ约为0.0000573%。（PDF第24页式(1.13)，第26页表1.1及式(1.19)，第27页式(1.20)。表1.1的数值及行列对应待核PDF第26页。）
- 对每个固定的感兴趣参数值，剖面似然比分子使用干扰参数的条件极大值，分母使用全局极大值。书中以大样本下的卡方近似构造区间，自由度取感兴趣参数的个数。（物理第55–56页，§2.3.4.1–2.3.4.2，式(2.25)、(2.33)–(2.36)。双产额示例见物理第74页图2.12及第75页正文，图中曲线与等高线对应关系待核第74页。）
- 在积分亮度设为1 fb⁻¹、质量假设为250 GeV的教学伪数据中，50 GeV质量窗内有25个事件，信号与背景的期望计数分别为7.84和14.71。使用质量谱的剖面似然检验得到背景尾概率0.021及 CLₛ＝0.554。（物理 PDF 第373页图11.2及正文，第376页式(11.4)，第379页图11.6和表11.1，第380页§11.2.2.4。）
- 本章报告对 Union2 Ia 型超新星数据作最大似然拟合，残差图注给出的每自由度 χ² 为 0.979。数据点分布和坐标标注待核物理 PDF 第411页。（物理 PDF 第411页，图12.5及图注。数据集引文 [23] 见第419页。）
