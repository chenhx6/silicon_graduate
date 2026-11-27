---
type: source
title: "Gade et al. 2025 - In-beam spectroscopy reveals competing nuclear shapes in 62Cr"
aliases: [Gade 2025 62Cr shape coexistence]
created: 2026-09-20
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-model
reading_depth: skimmed
title_original: "In-beam spectroscopy reveals competing nuclear shapes in the rare isotope 62Cr"
authors: [Alexandra Gade, Brenden Longfellow, Robert V. F. Janssens, Duc D. Dao, Frédéric Nowacki, Jeffrey A. Tostevin, et al.]
journal: "Nature Physics"
year: 2025
volume: 21
pages: "37-42"
doi: "10.1038/s41567-024-02680-0"
citation_key: Gade_2024
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "https://doi.org/10.1038/s41567-024-02680-0"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/形变/2025_Gade et al_In-beam spectroscopy reveals competing nuclear shapes in the rare isotope 62Cr.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/形变/2025_Gade et al_In-beam spectroscopy reveals competing nuclear shapes in the rare isotope 62Cr.pdf"
raw_sha256: "80ada48de9df6bddc15b9de79ad6e6d77fc4a6822264d8d7ebdf23762c12203e"
nuclei: [62Cr, 64Fe]
reactions: [64Fe-two-proton-knockout-9Be]
experiments: [FRIB-GRETINA-S800]
models: [large-scale-shell-model-LNPS, discrete-nonorthogonal-shell-model]
observables: [0plus-shape-coexistence, gamma-spectrum, momentum-distribution, B(E2), shell-occupancy]
methods: [in-beam-gamma-spectroscopy, knockout-momentum-distribution]
tags: [62Cr, shape-coexistence, N40-island-inversion, FRIB, GRETINA]
---

# In-beam spectroscopy reveals competing nuclear shapes in 62Cr

## Bibliographic Record

- A. Gade *et al.*, *Nature Physics* **21**, 37–42 (2025), DOI `10.1038/s41567-024-02680-0`。
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/形变/2025_Gade et al_In-beam spectroscopy reveals competing nuclear shapes in the rare isotope 62Cr.pdf`。

## Scope and Reading Depth

- PDF pp.37–42 fully read: FRIB `64Fe` two-proton knockout, S800 particle ID, GRETINA Doppler spectroscopy, γγ/multiplicity, momentum distributions, level scheme, LNPS shell-model and DNO-SM shape interpretation.
- Figure/table audit: Figs.1–4, Extended Data descriptions and shape/configuration discussion.
- Not covered: raw GRETINA event files, full LNPS/DNO-SM code and supplementary source data.

## Key Results

- An excited `0+` state in `62Cr` at about 1.38 MeV is established through a 1,016-keV decay to `2+_1`; competing 933/1,509-keV cascades assign `2+_2`, while momentum distributions constrain spins.
- `62Cr` exhibits competing shapes near the N=40 island of inversion; large-scale LNPS and DNO-SM calculations reproduce level ordering and interpret shape coexistence/axial asymmetry.
- The experiment combines particle ID, Doppler-corrected GRETINA spectra, multiplicity and two-proton knockout momentum widths; no single observable alone establishes shape coexistence.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GA25-1 | A low-lying excited `0+` state in `62Cr` is established by γγ/multiplicity and decay to `2+_1`. | experimental-result | direct | PDF pp.37–40, Figs.1–2 | true |
| GA25-2 | Momentum distributions and γ cascades assign `2+_1`, `4+_1`, `6+_1`, `0+_2`, `2+_2`, `2+_3` structures. | experimental-assignment | mixed | PDF pp.38–41, Fig.3–4 | true |
| GA25-3 | LNPS shell model and DNO-SM reproduce data and interpret competing shapes/axial asymmetry. | model-result | mixed | PDF pp.39–42 | true |

## Summary

Gade *et al.* provide direct FRIB evidence for a low-lying `0+` shape-coexisting state in `62Cr`, combining γ spectroscopy, reaction kinematics and shell-model/DNO-SM interpretation near the N=40 island of inversion.

## Competing Interpretations and Limitations

Shape assignments depend on shell-model interaction, DNO-SM basis, momentum-distribution reaction assumptions and incomplete weak branches; shape coexistence requires the combined evidence chain rather than a single γ line.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| GA25-AR-1 | Evidence chain | particle ID/knockout → γγ/multiplicity → level scheme/momentum J → LSSM/DNO-SM shape interpretation. | PDF Figs.1–4 | self-checking |
| GA25-AR-2 | Transfer condition | 0+ coexistence interpretation requires matched reaction/model and weak-branch sensitivity; no universal N=40 rule. | PDF pp.39–42 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[triaxial-shape-coexistence]] and [[heyde-wood-2011-shape-coexistence-review]] with a modern direct experiment outside A≈130.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `GA25-P0-1`: separate direct `0+`/γ/momentum evidence from model-derived shape labels and DNO-SM axial asymmetry.

## Extracted Pages

- Concepts: [[triaxial-shape-coexistence]], [[gamma-soft-deformation]]。
- Methods: in-beam gamma spectroscopy (source-level).

## 2026-11-27 — 馆藏原件与覆盖核对

- {"start": 1, "end": 3, "sections": "出版身份、引言、实验、62Cr 能级与动量分析。图1为 γ 谱和粒子鉴别，图2为符合与多重性，图3为纵向动量分布"}
- {"start": 4, "end": 6, "sections": "图4符合矩阵与能级纲图、图5计算带结构、图6形变面、表1钙同位素计算、展望与参考文献 [1]–[38]"}
- {"start": 7, "end": 8, "sections": "Methods，包括多普勒校正、S800 重建、反应理论、LSSM、DNO-SM 和 SU3 分析，以及数据和代码声明、参考文献 [39]–[46]"}
- {"start": 9, "end": 10, "sections": "扩展图1–2的 4p4h 与 2p2h 构型图注，图体待查"}
- {"start": 11, "end": 12, "sections": "扩展表1的布居态及截面题注，扩展表2的 B(E2) 题注。两表的表身待查"}
- 本次获取的具体覆盖：审读 PDF 第1–8页可提取的主文、图1–6图注、表1、Methods、可用性声明及参考文献 [1]–[46]。第9–12页读到两幅扩展图和两张扩展表的题注。扩展图图体及扩展表逐行数值未进入提取文本，因此附载材料仅部分可读。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A17-1 | FRIB 的 64Fe 双质子敲出测得 62Cr 包容截面 0.59(4) mb。γ 符合和多重性分析显示，933 keV 线馈入 2⁺₁，与两级联相容。1,016 keV 线馈入 4⁺₁，处于多重性为3及以上的级联。 | 实验观测与符合分析 | source-reported | PDF 第2页图1及能级章节，第3页图2及正文，第4页图4b。第4页图中箭头归属待核。 | true |
| A17-2 | 作者将由 933 keV 线退激的 1,379 keV 态指认为 0⁺₂。折叠分辨率后，0⁺₂ 与 2⁺₂ 的计算动量曲线近乎重叠，933 keV 门下两者的约化 χ² 为 0.6 和 1.0，故指认还依靠级联和 LNPS 比较。728 和 1,016 keV 门的动量比较分别支持 4⁺₁ 和 6⁺₁。1,509 keV 线拟归 2⁺₂→2⁺₁，1,492 keV 线馈入 4⁺₁。2⁺₂ 和 2⁺₃ 为有理论支持的候选。 | 谱学指认及其模型依赖 | source-reported | PDF 第3页图2–3，第4页图4a–b，第7页 Methods 的动量拟合段。待核第4页图4b括号和箭头。 | true |
| A17-3 | LNPS 与 DNO-SM 使用同一有效哈密顿量和价空间。作者将基态带解释为以 4p4h 为主、接近轴对称长椭球，将 0⁺₂ 带与以 2⁺₃ 为带头的候选 γ 带解释为以 2p2h 为主、具有 K 混合并向 γ≈30° 的构型展开。 | 结构模型解释 | source-reported | PDF 第4页图5、第5页图6及第5–6页形状讨论。扩展图1–2的图注见第9–10页，图点与占据细节待查原页。 | true |
| A17-4 | 56、58、60Ca 的侵入轨道占据数、粒子–空穴成分及 seniority 来自计算。表1中 60Ca 的 g₉/₂+d₅/₂ 占据数为 3.4，ν=0 成分为 90%。文中另报钙链计算的 2⁺ 能量范围为 1.5–2.0 MeV，讨论纳入 s₁/₂ 后约 300 keV 的初步下移，展望将 60Ca 的 2⁺₁ 概述为约 1 MeV 量级。 | 壳模型外推 | source-reported | PDF 第5页表1及钙链讨论，第6页展望。 | true |

动量判据依赖从 64Fe 的 0⁺ 基态敲出、直接反应与旁观者假定、LNPS 双核子振幅和实验分辨折叠。拟合允许缩放与小幅平移，省去经验建模的低动量尾。2⁺₁ 受未明馈入限制，未做独占动量分析。弱支未见及漏馈影响部分截面，扩展表1题注特别说明了 0⁺₂ 的例外。

- 将旧 Key Results 的 1,016 keV→2⁺₁ 归属改为 933 keV 对应 1,379 keV 候选 0⁺₂→2⁺₁。1,016 keV 对应 6⁺₁→4⁺₁。拆开旧记录合写的 933/1,509 keV，后者是候选 2⁺₂→2⁺₁，邻近 1,492 keV 线馈入 4⁺₁。定位为 PDF 第2–4页图2–4。
- GA25-2 不应将各自旋写成等强度的动量确认。按图4b保留暂定括号，写清 0⁺₂ 与 2⁺₂ 的动量判别有限，2⁺₂ 无可用于确认的独占动量分析。第3页正文对 6⁺₁ 写为 2,191 keV，第4页图4b抽取为 2,190 keV，统一数值前查第4页原图。
- 将形状结论的定位补为 PDF 第4页图5、第5页图6及第8–10页 SU3 讨论和图注。将 2024 保留为在线发表及引文键所用年份，期刊著录保留 2025。
