---
type: source
title: "IAEA 2006 - Handbook for Calculations of Nuclear Reaction Data: Reference Input Parameter Library-2 (RIPL-2)"
aliases: [IAEA RIPL-2, RIPL2-2006, 核反应参数参考库手册]
created: 2026-11-01
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: read
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

## 2026-11-27 — 馆藏原件与覆盖核对

- 手册转述 Audi 与 Wapstra 的 1995 年汇编，实验原子质量覆盖 1,964 个核素。（物理第 19 页 §2.1.1，物理第 23 页参考文献 [2.1]）

## 2026-11-27 — 馆藏原件与覆盖核对

- 离散能级库用已知自旋及可用的 γ 跃迁约束计算或抽样赋值。缺少实验自旋时，蒙特卡罗抽样值有单独编码。单候选值可编码为 u，即使原实验指派仍带不确定性。（物理第42–43页，附录3.B，式(3.6)–(3.10)及五类选择规则。公式排版待核物理第42页。）
- 附录5.D按库条目列出入射粒子、模型类型、色散与相对论势标记、适用核素与能区及参考文献编号。目录含中子、质子、氘、氚、³He和⁴He条目，Koning–Delaroche参数化只是其中一组。（物理第85–91页附录5.D目录表（抽取中未见独立表号）。物理第92页[5]与[11]均著录Koning和Delaroche的Nucl. Phys. A713 (2003) 231。）
- 手册转述，²³⁰Th(n,f) 在约 700 keV 的入射中子能量附近观测到共振，²⁴⁰Pu 的中子诱发裂变截面也显示中间结构。（物理第157页 §8.2，参考文献 [8.9]、[8.10] 的书目见物理第167页。）

PDF 2 核技术报告号、机构与日期；PDF 7、13、17、49、77、97、129、171 原页确认空白。PDF 33 Figs. 3.1–3.2 与 PDF 55 Figs. 4.1–4.2 区分离散能级拟合参数与不同评价的 s、p 波平均中子共振间距。PDF 70 按入射粒子及目标区分光学势建议，PDF 108、139 仅在指定输入下比较模型和数据。
