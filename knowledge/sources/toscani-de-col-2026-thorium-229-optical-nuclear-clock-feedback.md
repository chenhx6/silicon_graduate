---
type: source
title: "A thorium-229 optical nuclear clock with feedback loop"
aliases: ["toscani-de-col-2026-thorium-229-optical-nuclear-clock-feedback", "L. Toscani De Col 2026"]
created: 2026-11-07
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: experiment-article
reading_depth: deep-read
title_original: "A thorium-229 optical nuclear clock with feedback loop"
authors: ["L. Toscani De Col", "T. Riebner", "I. Morawetz", "F. Schneider", "N. Sempelmann", "J. Schlachet-Lépinay", "F. Schaden", "M. Bartokos", "G. A. Kazakov", "K. Beeks", "B. Gerstenecker", "M. Pimon", "S. Lahs", "A. Hellerschmied", "T. Lercher", "H. Denker", "J. Premper", "A. Niessner", "M. Matus", "M. Čížek", "O. Číp", "V. Lal", "G. Zitzer", "V. Petrov", "J. Tiedau", "M. V. Okhapkin", "E. Peik", "T. Schumm"]
journal: "Nature"
year: 2026
volume: "658"
pages: "897--902"
doi: "10.1038/s41586-026-11084-4"
canonical_source: "doi:10.1038/s41586-026-11084-4"
raw_file: "raw/papers/isomer/isomer_application/nuclear_clock/2026_Toscani De Col et al_A thorium-229 optical nuclear clock with feedback loop.pdf"
raw_sha256: "dd965aab469469930f7d2d70b736ab61f334a65f436912df2600e6ff88968a61"
archive_required: true
nuclei: ["229th"]
observables: []
methods: []
tags: ["229th", "isomer", "nuclear-clock", "vuv-spectroscopy"]
---

# A thorium-229 optical nuclear clock with feedback loop

## Bibliographic Record

- **Citation**: L. Toscani De Col, T. Riebner, I. Morawetz, F. Schneider, N. Sempelmann et al., *Nature* **658**, 897--902 (2026). DOI: `10.1038/s41586-026-11084-4`.
- **Local Raw File**: `raw/papers/isomer/isomer_application/nuclear_clock/2026_Toscani De Col et al_A thorium-229 optical nuclear clock with feedback loop.pdf`
- **File SHA-256**: `dd965aab469469930f7d2d70b736ab61f334a65f436912df2600e6ff88968a61`
- **Physical Page Count**: 10 pages.

## Scope and Reading Depth

本次对象为frontmatter指定的本地PDF，页数及实际读取范围见本轮clock逐文件台账。关键主张依下表原页定位；未在该PDF中实际检查的独立SI、原始计数和装置文件不自动包含在核验范围。

## Summary

Toscani De Col et al. (Nature Vol. 658, pp. 897-902, 22 October 2026) realized a closed-loop optical nuclear clock by stabilizing a continuous-wave 148 nm laser to the 229Th 5/2 -> 3/2 nuclear transition in a millimeter-sized room-temperature CaF2 crystal using rapid absorption feedback (10 Hz modulation). The subharmonic was continuously compared against PTB's 171Yb+ single-ion optical clock, demonstrating a shot-noise-limited Allan deviation instability of 3 x 10^-12 / sqrt(tau/s), approaching 10^-15 at 1 day (ttot = 23 h). A linear drift rate of (2 ± 4) x 10^-14 day^-1 was measured, and dark matter search limits were set on photon (d_e) and strong interaction (d_mhat, d_g) couplings.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| T26-1 | Closed-loop nuclear clock demonstrated shot-noise-limited fractional frequency instability Allan deviation of sigma_y(tau) = 3 x 10^-12 / sqrt(tau/s), reaching ~10^-15 at 1 day. | observed-fact | direct | p. 897, Abstract; p. 898, Fig. 2 | true |
| T26-2 | Continuous comparison with PTB 171Yb+ clock constrained linear frequency drift rate to (2 ± 4) x 10^-14 day^-1 over 23 hours. | observed-fact | direct | p. 897, Abstract; p. 899, Fig. 3 | true |
| T26-3 | Lomb-Scargle periodogram analysis of 23-hour clock beat data set experimental exclusion limits on ultralight dark matter couplings d_e, d_mhat, and d_g. | observed-fact | direct | p. 897, Abstract; p. 900, Fig. 4 | true |

## Competing Interpretations and Limitations

Operates on a room-temperature solid crystal where transition linewidth is ~100 kHz. Dark matter coupling limits depend on theoretical sensitivity models (K_alpha, K_q); systematic shifts in the solid-state host must be controlled for longer integration times.

## Extracted Pages

- [[toscani-de-col-2026-thorium-229-optical-nuclear-clock-feedback]]
- [[nuclear-clock-isomer-learning-and-transfer-20261107]]

## 2026-11-27 — 馆藏原件与覆盖核对

- 物理第1–2页（印刷897–898），首页、引言、Experimental set-up、Clock operation 开头与图1。
- 物理第3–6页（印刷899–902），Clock operation 续、Clock performance、暗物质约束、改进展望、图2–4、Online content 与参考文献1–59。
- 物理第7–8页，Methods、数据可用性、参考文献60–69与文末声明。
- 物理第9–10页，扩展数据图1–2的图注及可提取图中文字。
- 本次获取的具体覆盖：逐页读完物理第1–10页所供文本，包括论文正文、Methods、参考文献、图1–4及扩展数据图1–2的图注。图像和版面均待核。建议接受既有条目的同版书目，修正关键主张和定位并完成关键图核后再验收既有深读条目。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A20-1 | 作者用室温 Th:CaF₂ 的 148 nm 核吸收误差信号闭环校正钟激光，并与 BEV 的 ¹⁷¹Yb⁺ 单离子钟比较。论文报告两种核反馈积分时间，分别为20 s和30 min，并在连续运行中达到低 10⁻¹⁴ 量级的重叠 Allan 偏差。 | 实验报告 | source-reported | 物理第2页（印刷898）图1a、b及装置正文，物理第3页（印刷899）图2与 Clock performance。图2的长平均时间端点待图核。 | true |
| A20-2 | 对 T = 20 s、总长约23 h的频率比数据作线性拟合，得到漂移斜率 (2 ± 4) × 10⁻¹⁴ d⁻¹，与零相容。 | 实验数据拟合 | source-reported | 物理第4页（印刷900）Constraining dark matter couplings 末段。物理第5页图4a使用同批数据，物理第8页 Methods 给出采集起止时刻。 | true |
| A20-3 | 四个晶体位置的五次测量中，线心最大差约1.7 kHz，高于约0.13 kHz的预期统计散布。回到同一位置的第2、4次扫描所得线心相容。 | 实验观测 | source-reported | 物理第3页（印刷899）Clock performance，物理第4页（印刷900）图3a及图3b内嵌表。扫描编号与数值待图核。 | true |
| A20-4 | 在所设超轻标量暗物质模型下，作者将频率比的振荡幅度上限转为光子、QCD尺度及轻夸克质量耦合 d_e、d_g 和 d_{m_q} 的排除带，并用 10³、10⁴、10⁵ 三组钍核灵敏度展示模型依赖。 | 模型依赖推断 | source-reported | 物理第4页（印刷900）耦合换算正文，物理第5页（印刷901）图4b–d，物理第7–8页 Methods。排除带标签与换算式待核。 | true |

暗物质分析用约23 h拍频数据，每循环抽取一点。Lomb–Scargle 谱无峰超过经多重搜索校正的5%全局检测阈值。作者另用模拟求各频点的局部95%振幅排除线。耦合换算采用局域暗物质密度0.4 GeV cm⁻³、随机涨落修正及核灵敏度假设。见物理第4–5、7–8页。

- 将摘要和 T26-2 的“PTB ¹⁷¹Yb⁺ 钟”改为“经光纤链路连接的 BEV ¹⁷¹Yb⁺ 单离子钟”。10 Hz 是吸收或误差信号探测的调制频率，核反馈积分时间记为 T = 20 s 或30 min，见物理第2–3、7页。
- T26-1 改引物理第3页（印刷899）图2。将 3 × 10⁻¹²(τ/s)⁻¹ᐟ² 标为散粒噪声趋势，该式代入一天约为 10⁻¹⁴。单列摘要中“接近 10⁻¹⁵”的措辞，待核图2末端后确定可入库的实测值。
- T26-2 改引物理第4页（印刷900）暗物质约束末段。图3记录晶体位置相关线心，图4a对应约23 h的搜振荡数据。
- T26-3 改引物理第5页（印刷901）图4和物理第8页 Methods。采用 d_{m_q}，区分全局5%阈值、逐频点局部95%振幅上限及模型依赖的耦合排除带。图4a图注的否定措辞以第8页所述“排除高于上限的振荡”为准。
