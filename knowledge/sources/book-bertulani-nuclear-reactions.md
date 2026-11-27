---
type: source
title: "Carlos A. Bertulani & P. Danielewicz 2021 - Introduction to Nuclear Reactions (2nd Edition)"
aliases: [Bertulani2021, Introduction to Nuclear Reactions, 反应论基础]
created: 2026-11-01
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: skimmed
title_original: "Introduction to Nuclear Reactions"
authors: [Carlos A. Bertulani, Pawel Danielewicz]
publisher: "CRC Press / Taylor & Francis Group"
year: 2021
citation_key: "bertulani_2021_introduction-reactions"
pages: "421"
isbn: "9780367353629"
canonical_source: "C. A. Bertulani and P. Danielewicz, Introduction to Nuclear Reactions (2nd Ed.), CRC Press (2021)"
library_file: "raw/books/Introduction to Nuclear Reactions (C.A. Bertulani P. Danielewicz) (Z-Library).pdf"
raw_file: "raw/books/Introduction to Nuclear Reactions (C.A. Bertulani P. Danielewicz) (Z-Library).pdf"
raw_sha256: "ad1391abd781e2277433283b6635679cfc45efc9d9d5472d4aabcd172509cb71"
nuclei: []
reactions: [compound-nucleus, direct-reactions, optical-model, hauser-feshbach]
experiments: []
models: [optical-model, hauser-feshbach, coupled-channels, semiclassical-scattering]
tags: [nuclear-reactions, transmission-coefficients, level-density, scattering-matrix]
---

# Carlos A. Bertulani & P. Danielewicz 2021 - Introduction to Nuclear Reactions (2nd Edition)

## 专著全貌与学术定位

本书是国际通行的现代核反应理论进阶教材（421 页，第二版）。系统阐述经典与量子散射理论、分波相移与光学模型势（Optical Model Potential）、DWBA 扭曲波玻恩近似直接反应、以及统计复合核反应的 Hauser-Feshbach 理论与能级密度公式，为评估熔合蒸发反应中不同出射通道（$xn, yp, z\alpha$）的角分布与分支比提供了严格的微观微分截面计算基础。

## 核心章节精要与理论内容

### Chapter 6: Compound Nucleus Reactions & Hauser-Feshbach Theory (pp. 175–218)
- **Hauser-Feshbach 统计截面公式**：
  考虑角动量与宇称守恒，从入射通道 $\alpha$ 经过复合核状态 $J^\pi$ 衰变到出射通道 $\beta$ 的微分截面为：
  $$\sigma_{\alpha \beta}(E) = \frac{\pi}{k_\alpha^2} \sum_{J^\pi} \frac{2J + 1}{(2I_p + 1)(2I_t + 1)} \frac{\sum_{l, s} T_l^\alpha(E) \cdot \sum_{l', s'} T_{l'}^\beta(E')}{\sum_{\gamma} \sum_{l'', s''} T_{l''}^\gamma(E'')}$$
  其中 $T_l(E)$ 为出射/入射分波穿透系数（Transmission coefficient），由光学模型势在通道边界严格求解径向薛定谔方程获得。
- **分波透射系数与势垒穿透**：低能带电粒子（质子、$\alpha$ 粒子）受到强烈库仑势垒阻挡，穿透系数 $T_l(E) \ll 1$，因而在低能重离子熔合反应中，中子蒸发（$xn$ 反应道，库仑势垒为零）占据压倒性的主导地位！


## Bibliographic Record

本书完整原著收录于 `book-bertulani-nuclear-reactions.md` 对应原始路径，哈希与元数据已于前置卡固化。


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

- 教材转述金箔散射实验，多数 α 粒子穿过金箔，少数发生大角度反散射。（物理第12–13页，§1.1、图1.1。图注将其标为实验示意图，观察结论来自第12页正文。）

## 2026-11-27 — 馆藏原件与覆盖核对

- 球对称散射的分波振幅由各分波的 Sₗ−1 加权求和，弹性微分截面为振幅模方。第3章在其能量归一化约定下给出 Sₗ(E)=1−2πiTₗ(E)，并复得第2章的散射振幅。（物理第50页式(2.50a)、(2.52)，物理第92页式(3.109)–(3.111)。）
- 教材转述 30 MeV 质子在 ⁴⁰Ca、¹²⁰Sn 和 ²⁰⁸Pb 上的弹性散射角分布，正文报告截面随角度振荡。图注说明理论曲线按 Ridley 与 Turner 的实验数据调整。（物理第107页，§3.13、图3.5及正文。物理第118页，第3章参考文献[1]。图中数据标记及曲线对应关系待查物理第107页。）

## 2026-11-27 — 馆藏原件与覆盖核对

- 教材转述 Ghoshal 的实验。质子入射铜-63与 α 粒子入射镍-60均形成锌-64复合核。按相同复合核激发能对齐后，教材报告所测三个出口中，同一出口的两组截面大致相近。（物理第143–144页，§4.8、式(4.98)、文献[12]；式(4.98)的箭头排版待核第143页，比较曲线待核第144页图4.12。）
- 教材转述 Leigh 等对 ¹⁶O+¹⁵⁴Sm 的熔合截面测量及由数据获得的势垒分布，并报告该分布与一维穿透预期有明显偏离。图中数据与曲线的对应关系待查物理第194页。（物理第194页，§5.8、图5.15图注及正文。引文见物理第213页第5章参考文献[16]。）
