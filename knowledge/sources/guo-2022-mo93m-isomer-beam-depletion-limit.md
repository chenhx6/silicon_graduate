---
type: source
title: "Probing 93mMo Isomer Depletion with an Isomer Beam"
aliases: [Guo 2022 Mo93m isomer beam, Guo 2022 PRL null-limit]
created: 2026-11-07
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: experiment-article
reading_depth: deep-read
title_original: "Probing 93mMo Isomer Depletion with an Isomer Beam"
authors: [S. Guo, B. Ding, X. H. Zhou, Y. B. Wu, J. G. Wang, S. W. Xu, Y. D. Fang, C. M. Petrache, E. A. Lawrie, Y. H. Qiang, Y. Y. Yang, H. J. Ong, J. B. Ma, J. L. Chen, F. Fang, Y. H. Yu, B. F. Lv, F. F. Zeng, Q. B. Zeng, H. Huang, Z. H. Jia, C. X. Jia, W. Liang, Y. Li, N. W. Huang, L. J. Liu, Y. Zheng, W. Q. Zhang, A. Rohilla, Z. Bai, S. L. Jin, K. Wang, F. F. Duan, G. Yang, J. H. Li, J. H. Xu, G. S. Li, M. L. Liu, Z. Liu, Z. G. Gan, M. Wang, Y. H. Zhang]
journal: Physical Review Letters
year: 2022
volume: 128
pages: 242502
doi: 10.1103/PhysRevLett.128.242502
language: en
canonical_source: doi:10.1103/PhysRevLett.128.242502
raw_file: "raw/papers/isomer/isomer_application/nuclear battery/2022_Guo et al_Probing Mo 93 m Isomer Depletion with an Isomer Beam.pdf"
raw_sha256: ec3d4f308c1083124d5c8be87417c39ec2804f9568ba6f7901d84d15c7b24652
archive_required: true
nuclei: [93mo, 92zr, 91zr, 90zr]
reactions: ["12C(86Kr,5n)93mMo"]
observables: [isomer-depletion-upper-limit, isomer-decay-yields, coincident-gamma-spectra]
methods: [secondary-isomer-beam-line, ribll-hirfl-csr, implantation-gamma-coincidence, anti-compton-clover-array]
tags: [mo93m, isomer-beam, ribll, null-limit, neec-refutation-under-beam-foil, experimental-control]
---

# Guo et al. (2022): Probing \(^{93\text{m}}\)Mo Isomer Depletion with an Isomer Beam

## Bibliographic Record

S. Guo, B. Ding, X. H. Zhou, Y. B. Wu, J. G. Wang, S. W. Xu, Y. D. Fang, C. M. Petrache, E. A. Lawrie, Y. H. Qiang, Y. Y. Yang, H. J. Ong, J. B. Ma, J. L. Chen, F. Fang, et al., "Probing \(^{93\text{m}}\)Mo Isomer Depletion with an Isomer Beam," *Physical Review Letters* **128**, 242502 (2022), DOI: `10.1103/PhysRevLett.128.242502`. Primary PDF is 6 pages, SHA-256: `ec3d4f308c1083124d5c8be87417c39ec2804f9568ba6f7901d84d15c7b24652`.

## Scope and Reading Depth

The 6-page Letter was read completely. Locators examined: secondary beamline RIBLL layout (PDF p. 2 / printed p. 242502-2, Fig. 1), HPGe \(\gamma\)-ray spectra and 268-keV fit inset (PDF p. 3 / printed p. 242502-3, Fig. 2a--c), upper limit formulas Eqs. (1)--(3) and Table I coefficients (PDF p. 3--4 / printed p. 242502-3--4), and relativistic theory comparison (PDF p. 4 / printed p. 242502-4, Eqs. 4--5).

## Summary

The authors re-investigate \(^{93\text{m}}\)Mo isomer depletion using a secondary isomer beam at HIRFL-CSR / RIBLL to isolate stopping from primary reaction backgrounds. Selecting \(^{93\text{m}}\text{Mo}^{36+}\) ions at 460 MeV, they observe 570 counts in the 266.5--269.5 keV window against an estimated Compton background of 596 counts, with no statistically significant peak above background. With \(1.763(1) \times 10^6\) spontaneous isomer decay photons detected at 263 keV during beam-on, an upper limit \(P_{\text{max}} \approx 2 \times 10^{-5}\) is extracted using the \(3\sigma\) background lower bound.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GU22-1 | Delivers 460-MeV 93mMo36+ ions through 35-m RIBLL beamline (purity ~0.6%), isolating stopping foil from prompt reaction gamma-rays. | experimental-design | direct experimental report | printed p.242502-2, Fig. 1 | true |
| GU22-2 | In 266.5-269.5 keV window, observes 570 counts vs estimated 596 Compton background counts (3-sigma lower limit 523 counts; no significant peak). | experimental-null-result | direct measurement | printed p.242502-3, Fig. 2c inset | true |
| GU22-3 | Detects 1.763(1)e6 263-keV isomer decay photons during beam-on; extracts upper bound of ~50 peak counts using 3-sigma background lower bound and 95% Gaussian fraction. | quantitative-limit | derived value | printed p.242502-3--4, Eqs. (1)--(3) | true |
| GU22-4 | Establishes upper limit P_max ~ 2e-5 (factor of 500 below Chiara 2018), consistent with relativistic atomic theory (~2.3e-12 at 460 MeV). | quantitative-limit | derived experimental bound | printed p.242502-3--4, Table I | true |

## Competing Interpretations and Limitations

Guo 2022 strengthens counterevidence against the 1% claim under its specific stopping conditions (460-MeV ions in carbon foil). It does not represent a unique forensic reconstruction of the 2018 ATLAS target environment, nor does it disprove NEEC as a physical process, because the theoretical NEEC rate in carbon (\(\sim 10^{-11}\)) remains far below the \(2 \times 10^{-5}\) sensitivity threshold.

## Extracted Pages

- mo93m
- isomer-beam
- ribll
- neec

## 2026-11-27 — 馆藏原件与覆盖核对

- {"from": 1, "to": 2, "sections": ["刊头、引言、反应和RIBLL次级束输运", "图1装置图注、探测器与采数"]}
- {"from": 3, "to": 4, "sections": ["图2图注和植入符合分析", "268 keV窗口计数、上限推导式（1）–（3）、表I、理论式（4）–（5）"]}
- {"from": 5, "to": 6, "sections": ["理论计算结果及比较、结论、致谢", "参考文献1–39"]}
- 本次获取的具体覆盖：通读全部6个物理页的正文、图注、公式解释、表I及书目。PDF第3页的抽取保留图2图注及面板号，谱线和插图须看原图。建议接收修订后的同版文字覆盖，图像、表格印刷符号和公式排印待复核。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A18-1 | 实验以559 MeV的⁸⁶Kr束轰击碳靶，经 ¹²C(⁸⁶Kr,5n) 产生反冲核。约35 m的RIBLL次级束线将选择的460 MeV、36+离子送至远端，⁹³ᵐMo纯度估计约0.6%。离子在20 μm碳箔和塑料探测器中减速，最终停于塑料探测器。 | 实验条件 | source-reported | PDF第2页（242502-2）图1、图注及装置正文。实际传输长度见该页正文。 | true |
| A18-2 | 在50 ns植入符合门下，266.5–269.5 keV窗口记录570个计数，低于约596个计数的估计康普顿背景。作者报告未见可辨识的268 keV峰。 | 实验结果 | source-reported | PDF第3页（242502-3）图2c插图、末段，第4页（242502-4）开头。插图的峰形、拟合与背景待目视核对。 | true |
| A18-3 | 作者以523个计数的3σ背景下界及3 keV窗口覆盖约95%高斯峰面积的假定，估计268 keV峰面积上限约50个计数。以束开时263 keV峰的 1.763(1)×10⁶ 计数和随后18.4小时束关时的 2.78(1)×10⁵ 计数估算植入异能态数，结合探测修正得到激发概率上限约 2×10⁻⁵。 | 实验派生上限 | source-reported | PDF第3页（242502-3）图2c及正文，第4页（242502-4）式（1）–（3）、表I。谱图及公式、表格排印待目视核对。 | true |
| A18-4 | 作者计算碳中460 MeV入射反冲离子的 NEEC 概率为 2.3×10⁻¹²，假设840 MeV入射反冲离子时为 2.8×10⁻¹¹。两项均为电荷态分布、电子动量分布和停止功率模型下的结果。 | 模型计算 | source-reported | PDF第4页（242502-4）式（4）–（5）及理论输入，第5页（242502-5）开头给出结果。公式根号和指标待原页核对。 | true |

实验上限依赖背景下界和假定峰形，并使用相对效率、内转换、塑料探测阈值、符合门接受度及死时间或堆积修正。理论计算采用参考文献[24]的648个通道强度、参考文献[25]的冲量近似、碳电子康普顿轮廓、经验电荷态分布及 CasP 停止功率。

- 将既有上限定位细化为PDF第3页图2c和第4页式（1）–（3）、表I。式（1）–（5）均印于第4页，模型数值在第5页。补入束关263 keV计数及其半衰期外推。
- 把约95%写成假定高斯峰落入3 keV窗口的面积份额，把3σ明确归于背景下界。将“在碳箔中停止”改为“经碳箔减速后最终停于塑料探测器”。
- PDF第4页抽取中的式（2）分数与指数、式（4）–（5）求和积分及根号、表I首行效率比符号和内转换系数的希腊字母均须查原页后再逐字符转录。PDF第2页图1示意中的自旋轴标注抽取不全，照录前须核该页。
- 已读正文和图2图注明确支持索引中的⁹²Zr。既有索引中的⁹¹Zr、⁹⁰Zr须由PDF第3页图2原图标注核实后再保留。
