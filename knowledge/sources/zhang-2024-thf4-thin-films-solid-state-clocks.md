---
type: source
title: "229ThF4 thin films for solid-state nuclear clocks"
aliases: ["zhang-2024-thf4-thin-films-solid-state-clocks", "Chuankun Zhang 2024"]
created: 2026-11-07
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: experiment-article
reading_depth: deep-read
title_original: "229ThF4 thin films for solid-state nuclear clocks"
authors: ["Chuankun Zhang", "Lars von der Wense", "Jack F. Doyle", "Jacob S. Higgins", "Tian Ooi", "Hans U. Friebel", "Jun Ye", "R. Elwell", "J. E. S. Terhune", "H. W. T. Morgan", "A. N. Alexandrova", "H. B. Tran Tan", "Andrei Derevianko", "Eric R. Hudson"]
journal: "Nature"
year: 2024
volume: "636"
pages: "603--608"
doi: "10.1038/s41586-024-08256-5"
canonical_source: "doi:10.1038/s41586-024-08256-5"
raw_file: "raw/papers/isomer/isomer_application/nuclear_clock/2024_Zhang et al_229ThF4 thin films for solid-state nuclear clocks.pdf"
raw_sha256: "7cf04907243399a4e20bc0959649c92bcb6379997366694561c6f9e699eb1b78"
archive_required: true
nuclei: ["229th"]
observables: []
methods: []
tags: ["229th", "isomer", "nuclear-clock", "vuv-spectroscopy"]
---

# 229ThF4 thin films for solid-state nuclear clocks

## Bibliographic Record

- **Citation**: Chuankun Zhang, Lars von der Wense, Jack F. Doyle, Jacob S. Higgins, Tian Ooi et al., *Nature* **636**, 603--608 (2024). DOI: `10.1038/s41586-024-08256-5`.
- **Local Raw File**: `raw/papers/isomer/isomer_application/nuclear_clock/2024_Zhang et al_229ThF4 thin films for solid-state nuclear clocks.pdf`
- **File SHA-256**: `7cf04907243399a4e20bc0959649c92bcb6379997366694561c6f9e699eb1b78`
- **Physical Page Count**: 10 pages.

## Scope and Reading Depth

本次对象为frontmatter指定的本地PDF，页数及实际读取范围见本轮clock逐文件台账。关键主张依下表原页定位；未在该PDF中实际检查的独立SI、原始计数和装置文件不自动包含在核验范围。

## Summary

Zhang et al. demonstrated the growth of 229ThF4 thin films by physical vapor deposition (PVD) consuming only micrograms of 229Th. Using a VUV frequency comb, they directly observed laser excitation of the nuclear transition in the thin films, demonstrating a high-density (10^22 cm^-3) solid-state platform compatible with nanophotonics.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ZT24-1 | Fabricated 229ThF4 thin films by PVD consuming microgram amounts of 229Th with nuclear density ~10^22 cm^-3. | method-formalism | direct | pp. 603-605, Fig. 1 | true |
| ZT24-2 | Observed laser excitation of the 229Th nuclear transition in 229ThF4 thin films using a VUV frequency comb. | observed-fact | direct | pp. 605-607, Figs. 2-3 | true |

## Competing Interpretations and Limitations

Thin film samples exhibit broader transition linewidths than low-concentration doped single crystals due to inhomogeneous film strain and local field variations.

## Extracted Pages

- [[zhang-2024-thf4-thin-films-solid-state-clocks]]
- [[nuclear-clock-isomer-learning-and-transfer-20261107]]

## 2026-11-27 — 馆藏原件与覆盖核对

- {"from": 1, "to": 3, "sections": "首页、引言、微型 PVD 与靶表征；第2页图1，第3页图2及核激光谱方法"}
- {"from": 4, "to": 6, "sections": "光谱与寿命结果、淬灭讨论、图3和式(1)的钟性能模型、展望；第5–6页文献[1]–[58]"}
- {"from": 7, "to": 9, "sections": "Methods 中的折射率、检测、薄膜性质、DFT、淬灭、Zeeman 式(2)、转化与钟稳定度估算；第9页数据声明、文献[59]–[72]及出版附加信息"}
- {"from": 10, "to": 10, "sections": "Extended Data Table 1 的表题；表身缺抽"}
- 本次获取的具体覆盖：通读物理第1–9页的正文、图注、Methods、文献与附加信息。物理第10页只抽出 Extended Data Table 1 的表题，表身不可读。出版版正文及方法的文本覆盖完整，扩展表数值与各图图像待核。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A19-1 | 微型物理气相沉积以微克量 ²²⁹Th 材料制备薄膜靶。代表性小靶的 AFM 尺寸约为直径 50 μm、厚 30 nm，α 谱给出约 3 Bq；用于核光谱的两套大面积靶各约 21 kBq。 | experimental-observation | source-reported | PDF 第2页图1(a–c)、第3页靶表征与核激光谱正文、第7页 Methods；AFM 轮廓及 α 谱积分区待核第2页。 | true |
| A19-2 | 以氙气中两台脉冲染料激光共振增强四波混频产生的 VUV 光激发薄膜，记录到归于 ²²⁹Th 核异能跃迁的荧光。MgF₂ 与 Al₂O₃ 样品频率分别为 2020406.8(4)stat(30)sys 和 2020409.1(7)stat(30)sys GHz，衰减寿命分别为 153(9)stat(7)sys 和 150(15)stat(5)sys s。 | experimental-observation | source-reported | PDF 第2页结果概述、第3页核激光谱方法和图2(b,c)、第4页结果正文；频扫、衰减、衬底图例和归一化待核第3页。 | true |
| A19-3 | 根据荧光计数、靶密度和厚度、约 2 μJ 的脉冲能量及探测效率，作者估计两种靶参与窄核荧光的发射体比例均为 2(1) × 10⁻³。 | experimental-inference | source-reported | PDF 第4页荧光强度讨论、第7页探测效率及背景 Methods。 | true |
| A19-4 | 无缺陷单斜 ThF₄ 晶体模型给出两类不等价 Th 位点及约 1–7 kHz 的 Zeeman 限制线宽。假定 100 nm 膜、1 μW 窄线宽探测光且淬灭受到抑制，预测两类位点的钟分数不稳定度在 1 s 时均约为 5 × 10⁻¹⁷。 | model-calculation | source-reported | PDF 第4页图3和式(1)、第5页预测正文、第7–9页 Methods、第10页 Extended Data Table 1。第4页图示和第10页逐跃迁线宽待核。 | true |

薄膜跃迁归属援引文献[1]–[3]的晶体结果。发射体比例依赖光线追迹、光电倍增管量子效率及约 0.7% 的实验系统探测效率估计。性能预测采用晶体 DFT 的电场梯度、核矩参数和随机核偶极场模拟，稳定度模型另假设 1% 的系统探测效率。约 10²² cm⁻³ 可由第7页所用 6.3 g cm⁻³ 的材料密度和名义化学式换算，应标为材料数密度估计。

- 将 VUV 频率梳改为脉冲染料激光在氙气中的共振增强四波混频，定位 PDF 第3页。频率梳属于该文文献[3]所述的既往晶体实验。薄膜实测图定位第3页图2，第4页图3改归理论预测。
- 将薄膜谱线较宽且由应变和局域场造成的表述，替换为第4页所报的激光带宽主导结果。本文薄膜的表观谱线比所列 ²²⁹Th:LiSrAlF₆ 对照更窄，作者将其归因于采集期间较少的激光漂移。应变、界面、无序及杂质可标为可能的淬灭或非均匀展宽因素。
- 分别记录小靶的约 3 Bq 和光谱靶的各约 21 kBq。第2页图1(d,e)使用另制表征样品，其中透射面板所用膜约 1 μm 厚。将旧条目自链式页面清单替换为有物理页码的覆盖记录。
- PDF 第3页图2的 Nγ 和角度标注抽取变形，以图注可辨内容定位并回看原图。第4页式(1)与第8页式(2)的算符和 η 分母待核，且两页文本分别给出 Qg = 3.149(4) eb 与 3.149(3) eb，应保留差异待核。第8页折射率反推式及第8–9页稳定度、信噪比公式存在根号或上下标丢失；1 s 性能值可引第5页清楚的正文。
- PDF 第10页保留了扩展表题，表内跃迁标签、位点和逐行线宽缺抽。逐行数值须回看该页。
