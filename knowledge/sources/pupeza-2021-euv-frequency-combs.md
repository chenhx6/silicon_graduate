---
type: source
title: "Extreme-ultraviolet frequency combs for precision metrology and attosecond science"
aliases: ["pupeza-2021-euv-frequency-combs", "Ioachim Pupeza 2021"]
created: 2026-11-07
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: review-article
reading_depth: read
title_original: "Extreme-ultraviolet frequency combs for precision metrology and attosecond science"
authors: ["Ioachim Pupeza", "Chao Zhang", "Markus Högner", "Jun Ye"]
journal: "Nature Photonics"
year: 2021
volume: "15"
pages: "175--186"
doi: "10.1038/s41566-020-00741-3"
canonical_source: "doi:10.1038/s41566-020-00741-3"
raw_file: "raw/papers/isomer/isomer_application/nuclear_clock/2021_Pupeza et al_Extreme-ultraviolet frequency combs for precision metrology and attosecond science.pdf"
raw_sha256: "9062593b285102168400fdbc56cd320525b873c74e4263b35a415c9a08e77571"
archive_required: true
nuclei: ["229th"]
observables: []
methods: []
tags: ["229th", "isomer", "nuclear-clock", "vuv-spectroscopy"]
---

# Extreme-ultraviolet frequency combs for precision metrology and attosecond science

## Bibliographic Record

- **Citation**: Ioachim Pupeza, Chao Zhang, Markus Högner, Jun Ye, *Nature Photonics* **15**, 175--186 (2021). DOI: `10.1038/s41566-020-00741-3`.
- **Local Raw File**: `raw/papers/isomer/isomer_application/nuclear_clock/2021_Pupeza et al_Extreme-ultraviolet frequency combs for precision metrology and attosecond science.pdf`
- **File SHA-256**: `9062593b285102168400fdbc56cd320525b873c74e4263b35a415c9a08e77571`
- **Physical Page Count**: 12 pages.

## Scope and Reading Depth

The local primary PDF was examined under reading depth `read`. Main text, figures, tables, and discussions were inspected. Supplementary information was not bundled in this primary PDF file and is not included in this audit.

## Summary

Pupeza, Zhang, Högner, and Ye reviewed cavity-enhanced high-harmonic generation (HHG) for EUV/VUV frequency combs in Nature Photonics. They detailed the generation of coherent 7th-harmonic VUV frequency combs (148 nm) with single-comb-tooth powers from nW to μW, providing the optical technology foundation for direct frequency-comb spectroscopy of 229Th.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PU21-1 | Reviewed cavity-enhanced HHG for generating coherent VUV/EUV frequency combs with Hz-level tooth linewidths. | method-formalism | review synthesis | pp. 175-180, Figs. 1-2 | true |
| PU21-2 | Detailed upconversion architectures enabling 7th harmonic 148 nm coherent radiation for nuclear spectroscopy. | method-formalism | technical review | pp. 181-184, Fig. 4 | true |

## Competing Interpretations and Limitations

Review of laser physics and frequency comb technology; does not report nuclear spectroscopy data directly.

## Extracted Pages

- [[pupeza-2021-euv-frequency-combs]]
- [[nuclear-clock-isomer-learning-and-transfer-20261107]]

## 2026-11-27 — 馆藏原件与覆盖核对

- {"pdf_pages": "1–3", "printed_pages": "175–177", "sections": "首页书目信息、引言、HHG 光源比较、飞秒脉冲谐振增强。图1在物理第2页，图2和式（1）在第3页。"}
- {"pdf_pages": "4–6", "printed_pages": "178–180", "sections": "谐振增强续文、等离子体动力学与转换效率、XUV 输出耦合、频率梳稳定性与相干性开头。图3在物理第5页，图4在第6页。"}
- {"pdf_pages": "7–8", "printed_pages": "181–182", "sections": "相干性续文、XUV 直接频率梳光谱、兆赫兹光电子能谱与阿秒物理开头。图5和式（2）在物理第7页，式（3）在第8页。"}
- {"pdf_pages": "9–10", "printed_pages": "183–184", "sections": "光电子能谱与阿秒物理续文、结论与展望、出版日期及参考文献1–43。图6在物理第9页。"}
- {"pdf_pages": "11–12", "printed_pages": "185–186", "sections": "参考文献44–133、致谢、利益冲突声明及出版附记。"}
- 本次获取的具体覆盖：逐页审读物理第1–12页的抽取文本，覆盖正文、可辨公式、图注、可辨图内标签、参考文献及出版附记。图1–6均有抽取图注，抽取文本中未见编号表格。图像、曲线及公式排版留待管理者查阅原页。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A21-1 | 飞秒增强腔的谐振增强要求种子脉冲的重复周期和逐脉冲载波包络相位滑移与腔往返匹配。相干高次谐波生成后，第 q 阶谐波内的梳齿间隔仍为 ωr，偏移为 qω0 对 ωr 取模。 | 模型与方法 | source-reported | 物理第3页（印刷177）图2及式（1），物理第4页（印刷178）正文。式（1）描述线性腔响应，抽取式的根号与指数须核对物理第3页。 | true |
| A21-2 | 文献36用同一近红外种子驱动两个独立增强腔。主动稳定差分光程后，第17次谐波的两梳相对拍频线宽为62.5 mHz，达到测量分辨率极限。 | 引述实验观测 | source-reported | 物理第7页（印刷181）相干性正文、图5b及左侧插图。插图的稳定条件和分辨率标注须核对该页。 | true |
| A21-3 | 氩实验以 Yb 光纤梳的第13次谐波测量约82 nm的跃迁，到靶功率约10 pW/梳齿，确定了绝对梳模序号，正文报告频率不确定度6 MHz。氙实验以第7次谐波测量约147 nm的跃迁，到靶功率为500 fW/梳齿，有限的重复频率调谐范围只支持给出梳模序号的概率分布，所得频率不确定度为280 MHz。 | 引述实验观测 | source-reported | 物理第7页（印刷181）图5c–e及物理第8页（印刷182）光谱正文和式（3），对应文献40与41。氩的精确频率和图5e插图误差标注须核对物理第7页。 | true |
| A21-4 | 作者将以单根 XUV 梳齿直接探测²²⁹Th核跃迁及发展核光钟列为应用前景，引用文献93作为方案依据。 | 应用展望 | source-reported | 物理第8页（印刷182）XUV 频率梳光谱段末、物理第10页（印刷184）结论与展望，文献93条目在物理第11页（印刷185）。 | true |

现有 Wiki 页的 DOI、归档路径、SHA-256 和卷页与本件相符，建议接受同版归档关联。既有 read 条目的全篇图表覆盖及关键结果暂缓采信，待更正人名和证据定位并完成重点图版复核。本回执的整篇覆盖限于所给逐页文本。

- 将作者字段及引文中的 Chao Zhang、Markus Högner 改为首页所印的 Chuankun Zhang、Maximilian Högner。
- 将 PU21-1 的相干性实验证据定位改为物理第7页（印刷181）图5b及文献36，线宽表述改为第17次谐波的相对拍频达到62.5 mHz的测量分辨率极限。图1用于光源性能比较，图2用于腔增强与谐波梳结构说明。
- 将摘要及 PU21-2 的148 nm核光谱装置表述改为物理第8页所述约147 nm第7次谐波氙原子演示，并将²²⁹Th另列为研究前景。图4位于物理第6页（印刷180），用于说明 XUV 输出耦合。
- 将摘要中的单梳齿 nW 至 μW 功率区间拆为物理第8页的两个量。可用于光谱的源功率为每梳模超过1 nW，讨论双光子方案时所列1–100 μW是每谐波的时间平均功率。原子实验到靶功率采用各自的逐梳齿报告值。
- 将阅读范围记录改为整篇逐页文本及图注已审读，图版待核。氩跃迁先记录为约82 nm，待核清物理第7页图5e抽取标签3,655,454,100 ± 154 MHz与物理第8页正文约3.653 × 10¹⁵ Hz各自所指，以及插图误差和正文6 MHz不确定度的关系，再录精确数值。
