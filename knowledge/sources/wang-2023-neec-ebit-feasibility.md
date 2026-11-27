---
type: source
title: "Feasibility study of nuclear excitation by electron capture using an electron beam ion trap"
aliases: [Wang 2023 EBIT NEEC feasibility, Wang 2023 Fudan EBIT NEEC]
created: 2026-11-07
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: theory-article
reading_depth: deep-read
title_original: "Feasibility study of nuclear excitation by electron capture using an electron beam ion trap"
authors: [Yumiao Wang, Zhiguo Ma, Yi Yang, Changbo Fu, Wanbing He, Yugang Ma]
journal: Frontiers in Physics
year: 2023
volume: 11
pages: 1203401
doi: 10.3389/fphy.2023.1203401
language: en
canonical_source: doi:10.3389/fphy.2023.1203401
raw_file: "raw/papers/isomer/isomer_application/nuclear battery/2023_Feasibility study of nuclear excitation by electron capture using an electron beam ion trap.pdf"
raw_sha256: 5f54811a552c6a5bcc01a80b50ac6c7cfe59a96783ccf31a9fd346dfd5941334
archive_required: true
nuclei: [154eu, 157gd, 161dy, 181ta, 231pa, 237np, 63ni, 73ge, 83kr, 99ru, 111cd, 129i, 138la, 169tm, 187os, 201hg]
reactions: []
observables: [neec-resonance-strength, ebit-production-rate, coulomb-excitation-competition]
methods: [ebit-rate-modeling, dirac-fock-binding-energies, two-beam-energy-resonance-matching]
tags: [ebit, neec, highly-charged-ions, coulomb-excitation-background, experimental-feasibility, clean-environment]
---

# Wang et al. (2023): Feasibility study of nuclear excitation by electron capture using an electron beam ion trap

## Bibliographic Record

Yumiao Wang, Zhiguo Ma, Yi Yang, Changbo Fu, Wanbing He, and Yugang Ma, "Feasibility study of nuclear excitation by electron capture using an electron beam ion trap," *Frontiers in Physics* **11**, 1203401 (2023), DOI: `10.3389/fphy.2023.1203401`. Primary PDF is 8 pages, SHA-256: `5f54811a552c6a5bcc01a80b50ac6c7cfe59a96783ccf31a9fd346dfd5941334`.

## Scope and Reading Depth

The 8-page article was read completely. Reading scope covers EBIT operational principles and resonance matching (PDF p. 2 / printed p. 02, Fig. 1), Table 1 resonance strengths \(S_{\text{NEEC}}\) (in \(\text{b}\cdot\text{eV}\)) and beam energies for 16 heavy highly charged ions (PDF p. 4 / printed p. 04), Table 2 production rates \(R_{\text{NEEC}}\) and \(R_{\text{CE}}\) (in \(\text{s}^{-1}\)) under stated EBIT parameters (PDF p. 5 / printed p. 05), and background discrimination via two-beam energy modulation (PDF p. 5--6 / printed p. 05--06).

## Summary

The authors conduct a feasibility study of NEEC in an Electron Beam Ion Trap (EBIT). By trapping highly charged ions in ultra-high vacuum and bombarding them with a monoenergetic electron beam (\(\Delta E_e \sim 50\text{ eV}\)), stopping power losses and Doppler broadening are eliminated. Evaluating 16 candidate isotopes across \(E1, E2\), and \(M1\) transitions, they predict NEEC production rates reaching \(10^{-2}\text{--}10^{-1}\text{ s}^{-1}\), vastly exceeding Coulomb excitation backgrounds.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WA23-1 | Proposes EBIT for clean NEEC detection, eliminating solid-state stopping deceleration, Doppler shifts, and projectile-target nuclear collision backgrounds. | method-proposal | experimental design | printed p.01--03, Fig. 1 | true |
| WA23-2 | Evaluates NEEC resonance strengths S_NEEC (b*eV) for 16 heavy highly charged ions in Table 1 across E1, E2, and M1 transitions. | model-calculation | derived value | printed p.04, Table 1 | true |
| WA23-3 | Under typical EBIT conditions (L=3 cm, ni=1e8 cm-3, Ie=200 mA, Delta Ee=50 eV), Table 2 predicts NEEC rates of 1e-2 to 1e-1 s-1 (e.g., 4.36e-2 s-1 for 161Dy64+). | model-prediction | theoretical prediction | printed p.05, Table 2 | true |
| WA23-4 | Demonstrates that Coulomb excitation background is suppressed by orders of magnitude (R_CE ~ 1e-7 s-1 or strictly zero) at low electron beam energies. | model-calculation | comparative analysis | printed p.05, Table 2 | true |

## Competing Interpretations and Limitations

The study demonstrates that static ion-trap environments eliminate the backgrounds that compromised beam-foil measurements. Realization requires developing in-trap \(\gamma\)-ray or conversion-electron detection systems with high geometric efficiency at EBIT facilities.

## Extracted Pages

- ebit
- neec
- highly-charged-ions

## 2026-11-27 — 馆藏原件与覆盖核对

- PDF 第 1–3 页，第 1–2 节，引言、NEEC 共振机制、共振强度与内转换系数，图 1、表 1、式（1）–（4）。
- PDF 第 4–5 页，第 2 节末至第 4 节，181Ta 电荷态与俘获亚壳层扫描、双电子束 EBIT 及产率模型，图 2、图 3、式（5）。
- PDF 第 6–8 页，第 4 节末至第 6 节、表 2、背景讨论、数据可用性声明及参考文献 [1]–[58]。
- 本次获取的具体覆盖：通读 PDF 第 1–8 页的抽取文本，覆盖六节正文、图 1–3 的完整图注、表 1–2、式（1）–（5）、文末声明和参考文献。图像、表格列对齐和受损符号待查原页。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A20-1 | 作者提出双电子枪 EBIT，由一束电子产生高电荷态离子，另一束满足俘获共振条件 Eᵣ=Eₙ−Eᵦ，并以核退激信号寻找 NEEC。 | 实验方案 | source-reported | PDF 第 2 页第 2 节、图 1；第 4–5 页第 3 节、图 3。装置图待核第 5 页。 | true |
| A20-2 | 表 1 列出 29 个候选离子条目，覆盖 E1、E2、E3、E4、M1、M2 和 M3。181Ta⁵⁹⁺ 的计算共振强度为 4.34×10⁻³ b·eV，图 2 另列其电荷态和俘获亚壳层的扫描结果。 | 模型计算 | source-reported | PDF 第 3 页表 1；第 4 页图 2 及第 2 节续文。表中离子及图中分布待分别核第 3、4 页。 | true |
| A20-3 | 以 3 cm 阱长、10⁸ cm⁻³ 离子密度、200 mA 束流和 50 eV 能散估计，表 2 有 19 个条目。119Sn⁴⁸⁺ 和 137La⁵³⁺ 的 NEEC 率分别为 0.332 和 0.245 s⁻¹。竞争随核素而变，例如 181Ta⁵⁹⁺ 的 NEEC 和 CE 率分别为 0.0130 和 0.0107 s⁻¹，另有若干行的两束电子能量均低于 CE 阈值。 | 模型预测 | source-reported | PDF 第 5 页第 4 节、式（5）；第 6 页表 2 及相邻正文。各行电荷和指数待核第 6 页。 | true |
| A20-4 | 作者建议用共振峰与平滑 CE 背景的差异、与辐射复合（RR）的角分布差异和离阱观测来辨识信号。多普勒及塞曼效应在所设约 50 eV 能散下被估计为可忽略。 | 作者判断与辨识方案 | source-reported | PDF 第 6–7 页第 5 节。 | true |

式（1）–（5）依赖洛伦兹共振、离子内转换系数的比例外推、窄核能级宽度相对较宽电子束能谱的近似，以及选定单一电荷态。PDF 第 3 页说明中性原子内转换系数用 BrIccFO，结合能取文献 [46] 和 NIST [47]。CE 采用文献 [51] 的半经典计算。

- 将 WA23-2 的表 1 位置改为 PDF 第 3 页（03），16 种改为 29 个离子条目并补齐七类多极性。将 WA23-3、WA23-4 的表 2 改为第 6 页（06），明确 19 个条目。核素索引按两表重建，撤下表中未列的 169Tm、187Os，补入 189Os、57Fe、119Sn、137La 等遗漏项。
- 将笼统的 10⁻²–10⁻¹ s⁻¹ 和 CE 普遍可忽略改为逐离子报告。表 2 中有低于 10⁻² s⁻¹ 的候选，也有高于 0.1 s⁻¹ 的候选。181Ta、83Kr、205Pb、57Fe 和 201Hg 标为两机制均有贡献；零 CE 应限定在双束均低于核激发阈值的相应行。
- 将背景消除和多普勒展宽消除改为特定模型条件下的背景辨识与效应可忽略估计。将 Dirac–Fock 结合能标签改为正文所列数据来源。第 5 页以 b·eV 给出的 181Ta 数值应称共振强度。
- 保留跨表差异并核原版。PDF 第 3 页表 1 的 157Gd 为 64+，第 6 页表 2 和正文为 62+；187Re 的 Eₙ 在表 1 为 206.2473 keV，在表 2 抽取中为 1.5648 keV。第 6 页关于所选核素均稳定的表述与表 1 所列若干有限基态半衰期有冲突。第 7 页对共振强度的概括也应保留表 1 的逐项数值。
