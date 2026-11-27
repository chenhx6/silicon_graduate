---
type: source
title: "Novel Approach to 93mMo Isomer Depletion: Nuclear Excitation by Electron Capture in Resonant Transfer Process"
aliases: [Rzadkiewicz 2021 Mo93m NEEC-RT, Rzadkiewicz 2021 Compton profile NEEC]
created: 2026-11-07
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: theory-article
reading_depth: deep-read
title_original: "Novel Approach to 93mMo Isomer Depletion: Nuclear Excitation by Electron Capture in Resonant Transfer Process"
authors: [J. Rzadkiewicz, M. Polasik, K. Słabkowska, Ł. Syrocki, J. J. Carroll, C. J. Chiara]
journal: Physical Review Letters
year: 2021
volume: 127
pages: 042501
doi: 10.1103/PhysRevLett.127.042501
language: en
canonical_source: doi:10.1103/PhysRevLett.127.042501
raw_file: "raw/papers/isomer/isomer_application/nuclear battery/2021_Rzadkiewicz et al_Novel Approach to Mo 93 m Isomer Depletion Nuclear Excitation by Electron Capture in Resonant Trans.pdf"
raw_sha256: 9d295acd2c1706088b1c8d10ae0a097af2b34dc3f338598a984a8a69a5481860
archive_required: true
nuclei: [93mo]
reactions: []
observables: [neec-rt-cross-section, depletion-function, l-shell-enhancement, total-depletion-probability]
methods: [impulse-approximation, target-electron-compton-profile, dirac-fock-icc-scaling, casp-stopping]
tags: [mo93m, neec-rt, compton-profile, resonant-transfer-excitation, l-shell-restoration, theory-gap]
---

# Rzadkiewicz et al. (2021): Novel Approach to \(^{93\text{m}}\)Mo Isomer Depletion: Nuclear Excitation by Electron Capture in Resonant Transfer Process

## Bibliographic Record

J. Rzadkiewicz, M. Polasik, K. Słabkowska, Ł. Syrocki, J. J. Carroll, and C. J. Chiara, "Novel Approach to \(^{93\text{m}}\)Mo Isomer Depletion: Nuclear Excitation by Electron Capture in Resonant Transfer Process," *Physical Review Letters* **127**, 042501 (2021), DOI: `10.1103/PhysRevLett.127.042501`. Primary PDF is 6 pages, SHA-256: `9d295acd2c1706088b1c8d10ae0a097af2b34dc3f338598a984a8a69a5481860`.

## Scope and Reading Depth

The 6-page Letter was read completely. Reading scope covers formulation of NEEC in Resonant Transfer (NEEC-RT) within the impulse approximation (PDF p. 2 / printed p. 042501-2, Eqs. 1--2), target electron Compton profiles (PDF p. 3 / printed p. 042501-3, Eqs. 3--4), partial cross-section curves (PDF p. 4 / printed p. 042501-4, Fig. 3), charge-state evolution and depletion functions (PDF p. 4 / printed p. 042501-4, Figs. 4 and 5), and Table I probabilities (PDF p. 5 / printed p. 042501-5).

## Summary

The authors formulate NEEC in Resonant Transfer (NEEC-RT) by folding microscopic resonance strengths with the momentum distribution (Compton profile) of bound target electrons in carbon. While this momentum broadening restores the L-shell depletion probability by 7 to 8 orders of magnitude (from \(1.5 \times 10^{-19}\) to \(1.49 \times 10^{-11}\)), the total depletion probability increases only to \(6.98 \times 10^{-11}\). This demonstrates that target electronic momentum effects cannot bridge the 8-order gap to the 1% claim.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| R21-1 | Formulates NEEC-RT by folding atomic resonance strengths with target electron Compton profile within the impulse approximation. | theoretical-proposal | theoretical derivation | printed p.042501-2--3, Eqs. (1)--(4) | true |
| R21-2 | Compton profile momentum spread increases L-shell depletion probability by 7-8 orders of magnitude (to P_L = 1.49e-11). | model-calculation | derived value | printed p.042501-4--5, Table I | true |
| R21-3 | Total stopping depletion probability increases only to P_tot = 6.98e-11, leaving an 8-orders-of-magnitude discrepancy with the 1% claim. | quantitative-limit | derived value | printed p.042501-5, Table I | true |
| R21-4 | Proves that atomic momentum broadening redistributes phase space without increasing energy-integrated cross sections by orders of magnitude. | model-calculation | physical conclusion | printed p.042501-5 | true |

## Competing Interpretations and Limitations

The study demonstrates that target electron momentum profiles alter the shell-by-shell breakdown, but confirms that beam-foil collision theory remains orders of magnitude below the 1% observation, reinforcing the need for experimental verification under clean conditions.

## Extracted Pages

- neec-rt
- compton-profile
- mo93m

## 2026-11-27 — 馆藏原件与覆盖核对

- {"pdf_pages": "1–2", "sections": "前序束流实验及理论差距、NEEC-RT 定义和脉冲近似。第2页图1、式(1)–(2)。"}
- {"pdf_pages": "3–4", "sections": "内转换系数、康普顿轮廓及电荷态与阻止积分。第3页图2、式(3)–(4)，第4页图3–5、式(5)。"}
- {"pdf_pages": "5–6", "sections": "第5页表I、对照重算、结论及附记。参考文献[1]–[51]跨第5–6页。"}
- 本次获取的具体覆盖：逐页审读 PDF 物理第1–6页的抽取文字，覆盖前序实验、模型推导、积分结果、讨论、附记和参考文献。图1–5与表I均有抽取题注，原图曲线和表I版面待查。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A20-1 | 论文转述 Chiara 等以 γ 射线符合关系报告的 ¹²C 靶内 ⁹³ᵐMo 耗减概率 0.010(3)。将耗减归因于 NEEC 是该前序实验的解释。 | 转述的实验结果及其归因 | source-reported | PDF 第1–2页实验叙述、第5页表I Experiment 行、第6页引文[26]。第5页实验行的列归属和脚注待核。 | true |
| A20-2 | 模型在脉冲近似下，以 ¹²C 靶束缚电子的纵向动量康普顿轮廓加权 NEEC 共振强度，构造随弹核能量连续变化的 NEEC-RT 截面。能级示意采用异能态上方 4.85 keV 的耗减态。 | 理论模型 | source-reported | PDF 第2页图1和式(1)–(2)，第3页图2和式(3)–(4)，第4页图3。截面分组及曲线对应待查第4页。 | true |
| A20-3 | 表I中，本工作的 L 壳耗减概率为 1.49×10⁻¹¹，较 Wu 两套重组模型的 5.68×10⁻¹⁸ 和 1.48×10⁻¹⁹ 分别提高约六和八个数量级。作者用本组共振强度另做重组对照，认为康普顿轮廓带来的显著增强集中在 L 壳。 | 模型计算与同文对照 | source-reported | PDF 第4页图3–5和式(5)，第5页表I及其下方对照讨论。查第4页图5和第5页表I的壳层及模型行。 | true |
| A20-4 | 所算 L、M、N 壳总耗减概率为 6.98×10⁻¹¹，约为表列 Wu 两组模型总值的三倍，距前序实验中心值仍约八个数量级。 | 模型计算及与实验报告的比较 | source-reported | PDF 第4页式(5)，第5页表I的 Total 列及结论。核查第5页表格对齐。 | true |

模型采用[34]的核跃迁输入、Dirac–Fock 内转换系数与空穴修正、[44]的碳电子康普顿轮廓、[46–47]的平衡电荷态参数化和[48–49]的 CASP 阻止计算。实验与旧理论基线分别来自[26]和[28]。

- 将摘要和 R21-2 的 7–8 个数量级改为原文的约 6–8 个数量级，并注明两套 Wu 基线。将约写的 1.5×10⁻¹⁹ 改为表I的 1.48×10⁻¹⁹，补录另一基线 5.68×10⁻¹⁸。
- R21-4 改为模型限定的结论。康普顿轮廓展宽了截面对弹核能量的分布，L 壳在电荷态加权及阻止积分中的贡献显著增加，而 L、M、N 壳总耗减概率仅小幅上升。删除对一般能量积分截面的证明性断言。
- PDF 第1–2页的核自旋上标、第2页式(1)–(2)的根号和上下标、第3页式(3)–(4)的积分界及质量比，以及第4页式(5)的积分界、求和下标与阻止项均有字形错排。逐式引录前查对应原页。第3页图2的三维坐标文字破碎，第5页表I首行模型名和脚注在抽取中脱离数字行。
