---
type: source
title: "93mMo Isomer Depletion via Beam-Based Nuclear Excitation by Electron Capture"
aliases: [Wu 2019 Mo93m NEEC theory, Wu 2019 9-orders-discrepancy]
created: 2026-11-07
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: theory-article
reading_depth: deep-read
title_original: "93mMo Isomer Depletion via Beam-Based Nuclear Excitation by Electron Capture"
authors: [Yuanbin Wu, Christoph H. Keitel, Adriana Pálffy]
journal: Physical Review Letters
year: 2019
volume: 122
pages: 212501
doi: 10.1103/PhysRevLett.122.212501
language: en
canonical_source: doi:10.1103/PhysRevLett.122.212501
raw_file: "raw/papers/isomer/isomer_application/nuclear battery/2019_Wu et al_Mo 93 m Isomer Depletion via Beam-Based Nuclear Excitation by Electron Capture.pdf"
raw_sha256: 65a948a1144b2745a83cf0888fba24fa2fcdd79aa786faed6723f768641daf45
archive_required: true
nuclei: [93mo]
reactions: []
observables: [neec-resonance-strength, partial-capture-probabilities, stopping-power, charge-state-distribution]
methods: [multiconfigurational-dirac-fock, grasp92, casp-code, lorentz-profile-integration]
tags: [mo93m, neec, theory-discrepancy, stopping-power, charge-state-evolution, isomer-depletion]
---

# Wu et al. (2019): \(^{93\text{m}}\)Mo Isomer Depletion via Beam-Based Nuclear Excitation by Electron Capture

## Bibliographic Record

Yuanbin Wu, Christoph H. Keitel, and Adriana Pálffy, "\(^{93\text{m}}\)Mo Isomer Depletion via Beam-Based Nuclear Excitation by Electron Capture," *Physical Review Letters* **122**, 212501 (2019), DOI: `10.1103/PhysRevLett.122.212501`. Primary PDF is 6 pages, SHA-256: `65a948a1144b2745a83cf0888fba24fa2fcdd79aa786faed6723f768641daf45`.

## Scope and Reading Depth

The 6-page Letter was read completely. Reading covers formulation of beam-target NEEC stopping integrals (PDF p. 2 / printed p. 212501-2, Eqs. 1--3), stopping-power models and empirical charge-state distributions (PDF p. 3 / printed p. 212501-3, Fig. 2), mapping of 648 recombination channels (PDF p. 3 / printed p. 212501-3, Fig. 3), and Table I total probabilities and Table II shell-by-shell breakdown (PDF p. 4 / printed p. 212501-4).

## Summary

The authors calculate the theoretical probability of beam-based NEEC for \(^{93\text{m}}\)Mo slowing down in solid carbon. Modeling 648 atomic recombination channels across charge states \(\text{Mo}^{14+}\) to \(\text{Mo}^{42+}\) with MCDF wavefunctions and CasP stopping power, they find a total depletion probability \(P \approx 2.58 \times 10^{-11}\). This stands in conflict by approximately nine orders of magnitude with the experimental value of \(1.0(3)\%\) reported by Chiara et al. (Nature 2018).

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| W19-1 | Calculates total NEEC depletion probability for 93mMo in solid carbon as P = (2.26 to 2.73)e-11 across 648 recombination channels. | model-calculation | derived value | printed p.212501-2--4, Table I | true |
| W19-2 | Demonstrates a 9-orders-of-magnitude discrepancy between relativistic atomic theory (~2.6e-11) and the Chiara 2018 report (1.0e-2). | theoretical-challenge | comparative analysis | printed p.212501-1, 4 | true |
| W19-3 | Identifies physical quenching of L-shell capture (P_L ~ 1.5e-19) due to charge-state cooling to q_bar ~ 20-25 during stopping in carbon. | physical-mechanism | theoretical model | printed p.212501-4, Table II | true |
| W19-4 | Shows that M-shell (P_M ~ 1.53e-11) and N-shell (P_N ~ 7.54e-12) dominate the total stopping-target NEEC probability. | model-calculation | derived value | printed p.212501-4, Table II | true |

## Competing Interpretations and Limitations

The calculation relies on the Ground State Assumption (GSA) and equilibrium stopping power. Later theoretical work showed that non-equilibrium excited ion states (Gargiulo 2022) and target electron Compton profiles (Rzadkiewicz 2021) can enhance cross sections, but still leave a multi-order-of-magnitude discrepancy with the 1% report.

## Extracted Pages

- mo93m
- neec
- stopping-power
- charge-state-distributions

## 2026-11-27 — 馆藏原件与覆盖核对

- 物理第1–2页，实验背景、图1的装置与能级图注、268 keV 信号及式(1)–(3)的概率推导。
- 物理第3–4页，原子结构计算、电荷态分布、阻止本领、式(4)、图2–3及表I–II。
- 物理第5–6页，铅靶估算、机制讨论及参考文献[1]–[54]。
- 本次获取的具体覆盖：逐页审读物理第1–6页的抽取文字，覆盖正文、图1–3的图注、表I–II的抽取表项和参考文献表。图面及公式排版待复核。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A20-1 | Wu 等转述 Chiara 等测得触发态 T 向 F 跃迁的 268 keV γ 信号，并由数据提取每个 93mMo 核约 0.01 的耗减概率。按文中给出的单位分支比，该值也对应到达 T 的激发概率。 | 转述实验观测及数据提取 | source-reported | 物理第1页图1图注、物理第2页左栏首段及物理第5页文献[28]。引用图中具体能级标签前须核对物理第1页图1。 | true |
| A20-2 | 碳靶计算覆盖 Mo¹⁴⁺ 至 Mo⁴²⁺ 的 648 个俘获通道，其中 23 个通向相应电子基态，625 个通向电子激发态。表I六组模型给出总概率 2.26×10⁻¹¹ 至 2.73×10⁻¹¹，CasP-q 配电荷态模型(ii)给出 2.58×10⁻¹¹。 | 模型计算 | source-reported | 物理第2页式(1)–(3)，物理第4页图3图注、通道说明及表I。图3分布与表I行列须核对物理第4页。 | true |
| A20-3 | 模型中，L 壳层可有最大的单通道概率，但在对应共振能量下，带 L 壳层空位的高电荷态离子份额很小。加权后 L 壳层总贡献可忽略，M 壳层贡献最大，N、O 壳层亦有贡献。 | 模型机制解释 | source-reported | 物理第2页式(3)，物理第3页图2，物理第4页图3及表II。图2电荷态曲线和表II壳层列须分别核对物理第3、4页。 | true |
| A20-4 | 作者把计算概率与文献[28]的约 0.01 相比，将差距概括为约九个数量级，并据此质疑将所见耗减归因于 NEEC。实际激发机制在文中仍为开放问题。 | 作者解释 | source-reported | 物理第4页表I下方讨论，物理第5页左栏结论。 | true |

计算使用 GRASP92 的多组态 Dirac–Fock 束缚波函数、文献[37]的核跃迁强度 B=3.5 W.u.、文献[40–42]的电荷态拟合及 CasP 和文献[43]的阻止本领。电子矩阵元与已有内转换系数的比较约在 10% 水平。建议在落实下列替换后接受既有同版的整篇文本覆盖，图表深读认定待管理者查图。

- 将图3定位从物理第3页改为第4页（212501-4），与表I、表II同页。
- 将旧稿的实验值 1.0(3)% 改为本篇可核的 0.01（约1%）。括号不确定度须另从文献[28]原件核验。
- 表II须按同一模型引用。CasP-q 配模型(ii)的 L、M、N、O 壳层贡献依次为 1.48×10⁻¹⁹、1.47×10⁻¹¹、7.34×10⁻¹²、3.73×10⁻¹²。旧稿的 M、N 数值来自模型(i)。将固定的平均电荷态 20–25 改为作者给出的共振能量处高电荷态尾部份额极小。
- 将方法栏的笼统 GSA 和单一平衡阻止本领表述改为按初始电荷态加权、区分俘获后的电子基态和激发态、主结果采用 CasP-q，并与平衡 CasP 及半经验模型比较。旧稿的 2021/2022 年后续工作应另引原件。
