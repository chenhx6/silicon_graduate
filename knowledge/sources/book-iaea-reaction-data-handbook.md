---
type: source
title: "IAEA 2006 - Handbook for Calculations of Nuclear Reaction Data: Reference Input Parameter Library-2 (RIPL-2)"
aliases: [IAEA RIPL-2, RIPL2-2006, 核反应参数参考库手册]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: deep-read
title_original: "Handbook for calculations of nuclear reaction data, Reference Input Parameter Library-2 (RIPL-2)"
authors: [IAEA (International Atomic Energy Agency)]
publisher: "IAEA-TECDOC-1506, Vienna"
year: 2006
citation_key: "iaea_2006_handbook-calculations-reaction"
pages: "172"
canonical_source: "IAEA, Handbook for calculations of nuclear reaction data (RIPL-2), IAEA-TECDOC-1506 (2006)"
library_file: "raw/books/Handbook for calculations of nuclear reaction data.pdf"
raw_file: "raw/books/Handbook for calculations of nuclear reaction data.pdf"
raw_sha256: "7db49b1250cfe8690cbc5986fec2392518faa24844c6370a6ccf47bce45a61d4"
nuclei: []
reactions: [compound-nucleus, neutron-reactions, photonuclear]
experiments: []
models: [gilbert-cameron, back-shifted-fermi-gas, lorentzian-gdr, koning-delaroche-optical]
tags: [nuclear-data, level-density-parameter, optical-model-parameters, photon-strength-functions]
---

# IAEA 2006 - Handbook for Calculations of Nuclear Reaction Data (RIPL-2)

## 专著全貌与学术定位

国际原子能机构（IAEA）汇聚全球顶尖核数据专家编制的标准输入参数库手册（IAEA-TECDOC-1506）。本书是现代核反应统计模拟程序（如 TALYS、EMPIRE、PACE4、CASCADE）背后的标准参数圣经。

## 核心章节精要与理论内容

### Chapter 5: Nuclear Level Densities (pp. 67–104)
- **反冲费米气体模型（Back-Shifted Fermi Gas Model, BSFG）**：
  激发能 $U = E^* - \Delta$ 处的总能级密度由 Bethe 公式给出：
  $$\rho(U, J) = \frac{\sqrt{\pi}}{12} \frac{\exp(2\sqrt{a U})}{a^{1/4} U^{5/4}} \cdot \frac{2J + 1}{2\sqrt{2\pi} \sigma^3} \exp\left(-\frac{(J + 1/2)^2}{2\sigma^2}\right)$$
  其中：
  - $a$ 为能级密度参数（Level density parameter），随质量数经验演化为 $a \approx A / 8.5\text{ MeV}^{-1}$；
  - $\Delta$ 为由配对效应引起的回退能量（Back-shift energy）；
  - $\sigma^2 = \frac{\mathcal{J}_{\text{rigid}}}{\hbar^2} \sqrt{U/a}$ 为自旋截止因子（Spin cutoff parameter），直接决定了复合核高自旋态向 yrast 线的布居效率。


## Bibliographic Record

本书完整原著收录于 `book-iaea-reaction-data-handbook.md` 对应原始路径，哈希与元数据已于前置卡固化。


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
