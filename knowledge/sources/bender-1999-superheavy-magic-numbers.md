---
type: source
title: "Bender et al. 1999 - Shell structure of superheavy nuclei in self-consistent mean-field models"
aliases: [Bender 1999 superheavy shell structure, superheavy magic numbers RMF Skyrme, BEN99]
created: 2026-10-30
updated: 2026-11-27
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Shell structure of superheavy nuclei in self-consistent mean-field models"
authors: [M. Bender, K. Rutz, P.-G. Reinhard, J. A. Maruhn, W. Greiner]
journal: Physical Review C
year: 1999
volume: 60
issue: 3
pages: "034304"
doi: "10.1103/PhysRevC.60.034304"
canonical_source: "https://doi.org/10.1103/PhysRevC.60.034304"
citation_key: bender1999superheavy
raw_file: "raw/papers/gpt/learning-daily/20261031-OPEN-RESEARCH-source-recovery/PhysRevC.60.034304.pdf"
raw_sha256: f345e34d1e3e6c99012b0abc16d0dda87744ba47d480fab0c6b2897bd1ad6d3f
nuclei: [16o, 132sn, 208pb, 298114, 292120, 310126]
reactions: []
experiments: []
models: [relativistic-mean-field, skyrme-hartree-fock, folded-yukawa, bcs-pairing]
observables: [single-particle-energies, shell-gaps, spin-orbit-splitting, charge-density-distributions, two-proton-separation-energies]
methods: [self-consistent-mean-field, density-gradient-analysis, central-depression-evaluation]
tags: [superheavy-elements, magic-numbers, spin-orbit-quenching, island-of-stability, central-depression, Day27]
---

# Shell structure of superheavy nuclei in self-consistent mean-field models

## Bibliographic Record

PRC 60, 034304 (1999), DOI `10.1103/PhysRevC.60.034304`.

## Scope and Reading Depth

- Covered scope: 20 页 APS 出版版。已核球形自洽平均场的模型清单与对照、已知核单粒子谱、超重核壳隙、密度及自旋轨道势、结论、附录主线和关键引文。原件重核包括 Table I、Figs. 1–16、附录 Tables II–IV 的定位与相关说明。
- Coverage caveats: 本文提供依参数化与核子数而异的球形闭壳预测。邻近奇质量核提取的实验单粒子谱用于约束模型。未复算泛函、能谱、结合能或配对参数，未读尽所有引文，熔合蒸发动力学在论文覆盖之外。

## Summary

Bender 等比较七套 Skyrme–Hartree–Fock 参数组与四套 RMF 参数组，并给 folded-Yukawa 单粒子势作非自洽对照。Table I 列无限核物质的 E/A、ρ₀、K∞、m*/m、a_sym 与 κ，部分量用于拟合约束。RMF 的 m*/m 列中，括号外为 k=0 的值，括号内为费米面值。本文的球形双幻候选包括 ²⁹⁸114、²⁹²120、³¹⁰126。作者结合已知核自旋轨道劈裂基准和超重区计算，判断 Z=120、N=172 最有支持。该判断依赖球形模型与所选参数组。**定位**　PDF pp. 1–4、7–15。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| BEN99-1 | 在 ²⁹²120，Fig. 10 比较多套模型的中子、质子及总径向密度与自旋轨道势。SkP 为明显中心凹陷的例外。正文所讨论的深凹陷计算中心密度约为核物质值的 2/3。Fig. 12 的 SkI3 球形扫描显示凹陷在 Z≈120、N<184 一带显著。作者关联费米面附近轨道占据与自洽密度反馈，库仑作用亦影响质子径向分布。 | model-result | source-reported | PDF p. 2 左栏，pp. 11–13 §V.E、Figs. 10–12 | false |
| BEN99-2 | 球形自旋轨道劈裂依赖径向波函数与物种相关的自旋轨道场的重叠。SkI3 的 ²⁹²120 示例中，质子 3p、中子 3d 与内外异号势区均有重叠，劈裂可近乎抵消。质子 2f、中子 2g 主要采样表面区，保留较通常的劈裂。若干 RMF 参数组的 3p 次序反转。 | model-result | source-reported | PDF pp. 4–5 §III、Eqs. (2)–(8)，pp. 11–12 Figs. 9–11，p. 14 §V.G、Fig. 16 | false |
| BEN99-3 | 自洽参数组为 SkM*、SkP、SLy6、SLy7、SkI1、SkI3、SkI4 和 NL3、NL-Z、NL-Z2、NL-VT1。SkI4 给 Z=114 球形闭壳，其所需的较大质子 2f 劈裂受已知核劈裂偏差制约。本文各 RMF 参数组给 Z=120，SkI3 也给该候选。N=172 的中子壳隙对 3d 劈裂敏感，见于 RMF 和 SkI3 的计算。SkP、SkM* 在 N≈184 处给 Z=126 闭壳。N=184 的强度依参数和质子数变化；在 ²⁹⁸114，NL3 的主要 N=184 闭壳消失。 | model-result | source-reported | PDF p. 3 Table I，pp. 8–10 §§V.C–D、Figs. 3–8，pp. 11–14 §§V.E–F、Figs. 9–15，p. 15 §VI | false |
| BEN99-4 | ²⁰⁸Pb 的实验参照能级来自近邻奇质量核，本论文用它检验球形谱与自旋轨道外推。壳隙指标 δ₂q 是偶偶核结合能的二阶差分，近闭壳时可近似联系费米能的变化；离开闭壳时配对削弱这个联系。作者指出壳结构差异会影响近基态的势能面及裂变预言。本文的量化结论限于所计算的球形能谱、壳隙与密度。 | model-scope | source-reported | PDF p. 2 引言，pp. 5–8 §§IV、V.A–B、Eqs. (9)–(12)、Figs. 1–2，p. 15 §VI | false |

## Competing Interpretations and Limitations

- 参数组共用已知核拟合或比较数据，²⁰⁸Pb 参与本文各参数组的拟合。Fig. 1 的邻核实验数据回链 [66]。Fig. 2 的劈裂与空穴/粒子能比较用于检验外推，参数间共享的输入应保留。
- Fig. 10 的 folded-Yukawa 波函数密度也可见较弱的凹陷。该势由预设形状产生，缺少密度对势的自洽反馈。超重区参数排序取决于有效质量、同位旋自旋轨道项及径向密度三者。定位 PDF pp. 11–14 §§V.E–G，p. 18 Appendix A.4。
- 逐值引用 Table I 的 SkI3 有效质量时用表列 0.577，并记 §IV 和 Table IV 分别给出 0.574。Fig. 16 的质子空符号据图例为 2f，p. 14 左栏相邻正文有一处写作 3f，同页右栏与图例为 2f。重建必须注明所用标签和数值来源。

## Extracted Pages

- PDF pp. 1–4，摘要、框架与 Table I。SHF 与 RMF 参数组见 p. 3；p. 17 Tables II–III 给耦合参数。
- PDF pp. 5–6，径向劈裂、有效质量与平均能级密度、S₂q 和 δ₂q，Eqs. (5)–(12)。
- PDF pp. 7–8，Fig. 1 为 ²⁰⁸Pb 单粒子谱，Fig. 2 为已知核自旋轨道劈裂相对误差，Fig. 3 为 Z=114 同位素链 δ₂p。
- PDF pp. 9–11，Fig. 4 为 ²⁹⁸114 单粒子谱，Figs. 5–8 为 Z=120 的 δ₂p 与费米面附近质子谱，Fig. 9 为 ²⁹²120 单粒子谱。
- PDF pp. 11–14，Figs. 10–12 为 ²⁹²120 及邻区密度、径向自旋轨道场与积分核，Fig. 13 为 N=172 同中子素的 SkI3 中子谱，Figs. 14–15 为 Z=126 的 δ₂p 与 ³¹⁰126 单粒子谱，Fig. 16 为按 2ℓ+1 归一的劈裂。
- PDF pp. 15–20，§VI 总结与 Appendix A，含 Skyrme 泛函、RMF 拉氏量、零程 BCS 配对 Table IV、folded-Yukawa 对照及参考文献。
