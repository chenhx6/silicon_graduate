---
type: source
title: "Impact of Nuclear Mass Uncertainties on the r Process"
aliases: [Martin 2016 r-process mass uncertainties, Martin 2016 PRL]
created: 2026-11-07
updated: 2026-11-27
status: active
review_status: unreviewed
source_type: journal-article-theory
reading_depth: deep-read
title_original: "Impact of Nuclear Mass Uncertainties on the r Process"
authors: [D. Martin, A. Arcones, W. Nazarewicz, E. Olsen]
journal: Physical Review Letters
year: 2016
volume: 116
pages: 121101
doi: 10.1103/PhysRevLett.116.121101
language: en
canonical_source: doi:10.1103/PhysRevLett.116.121101
citation_key:
raw_file: "raw/papers/isomer/isomer_application/nuclear_astrophysics/2016_Martin et al_Impact of Nuclear Mass Uncertainties on the r Process.pdf"
raw_sha256: bcc1be2537c180ae5197cad0574b85402e34112e6c1ec6dd9625a7000123605b
alternate_version_file: "raw/papers/isomer/isomer_application/nuclear_astrophysics/2016_Martin et al_Impact of Nuclear Mass Uncertainties on the r Process 1.pdf"
alternate_version_sha256: c9045474ae93257657a0d20716a33d5bbc3417d77556ed57db4b8df83c226c09
alternate_version_identity: "CHORUS accepted author manuscript (7 pages, 1,708,925 bytes)"
archive_required: true
nuclei: [128pd, 130cd, 132sn, 134sn, 195pt]
reactions: [neutron-capture, photodissociation, r-process-network]
experiments: []
models: [nuclear-density-functional-theory, skyrme-edf, talys-statistical-model, reaction-network]
observables: [neutron-separation-energy, r-process-abundance, reaction-rate]
methods: [dft-mass-modeling, talys-cross-sections, r-process-simulations]
tags: [r-process, mass-uncertainties, skyrme-edf, astromer, shell-closure, nuclear-astrophysics]
---

# Martin 等（2016）：原子核质量不确定度对快速中子俘获过程（r 过程）的影响

## Bibliographic Record

The paper was published in *Physical Review Letters* 116, 121101 (2016), received 10 December 2015, published 25 March 2016 (DOI: 10.1103/PhysRevLett.116.121101). The published 6-page PDF is retained at `raw/papers/isomer/isomer_application/nuclear_astrophysics/2016_Martin et al_Impact of Nuclear Mass Uncertainties on the r Process.pdf` with SHA-256 `bcc1be2537c180ae5197cad0574b85402e34112e6c1ec6dd9625a7000123605b` (794,047 bytes). The CHORUS accepted author manuscript (7 pages) is preserved in the same directory as `... 1.pdf` with SHA-256 `c9045474ae93257657a0d20716a33d5bbc3417d77556ed57db4b8df83c226c09` (1,708,925 bytes). `archive_required: true` is preserved.

## Scope and Reading Depth

The published 6-page paper was read in full, including text, figures 1–3, and equations. The study computes $r$-process nucleosynthesis yields in realistic astrophysical trajectories (neutron star mergers and magneto-rotational jet-like supernovae) using neutron capture and photodissociation rates based on nuclear density functional theory (DFT) with six Skyrme energy density functionals (EDFs: SkM*, SkP, SLy4, SV-min, UNEDF0, UNEDF1).

## Summary

Martin et al. performed the first systematic evaluation of mass-model uncertainty bands in $r$-process nucleosynthesis using microscopic DFT mass inputs from six Skyrme functionals. For each functional, Maxwellian-averaged $(n,\gamma)$ and $(\gamma,n)$ rates were computed with the TALYS statistical model code and input into a comprehensive reaction network. The authors found that systematic abundance uncertainty bands are strongly correlated and non-uniform across mass number $A$:
1. The $A \approx 130$ second peak is constrained by fission recycling in neutron star mergers, but displays significant mass sensitivity around shell closures ($N=82$) where nuclei transition between deformed and spherical shapes.
2. The pre-peak and post-peak abundances and the $A \approx 195$ third peak are directly governed by the fine trends in two-neutron separation energy $S_{2n}$ and single-neutron separation energy $S_n$, because photodissociation rates scale exponentially as $\lambda_{(\gamma,n)} \propto \exp(-S_n / kT)$.
3. The paper establishes that microphysics uncertainties at magic shell gaps ($N=82$ and $N=126$) leave immediate imprints on the freeze-out path and final elemental distributions.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MAR16-1 | Using six microscopically optimized Skyrme EDFs (SkM*, SkP, SLy4, SV-min, UNEDF0, UNEDF1), the authors compute correlated systematic uncertainty bands for $r$-process abundances in neutron star mergers and jet-like supernovae. | model-calculation | direct | PDF p. 1–2, Abstract, Fig. 1 | false |
| MAR16-2 | The abundance uncertainty bands are non-uniform across mass number $A$, contrasting with random mass variations, because DFT forces maintain physical correlations between binding energies of neighboring isotopes. | author-interpretation | direct | PDF p. 2, text col. 2, Fig. 1 | false |
| MAR16-3 | Freeze-out abundances and the formation of peaks at $A \sim 130$ ($N=82$) and $A \sim 195$ ($N=126$) directly correlate with local variations in two-neutron separation energies $S_{2n}$ along isotopic chains. | model-calculation | direct | PDF p. 2–4, Fig. 2 | false |
| MAR16-4 | Photodissociation rates $\lambda_{(\gamma,n)}$ depend exponentially on neutron separation energies $S_n$, amplifying small mass model variations ($300–500\text{ keV}$) into orders-of-magnitude rate shifts during $(n,\gamma) \rightleftharpoons (\gamma,n)$ equilibrium. | derived-observable | direct | PDF p. 2, col. 1, Eq. context | false |
## Competing Interpretations and Limitations

### Mass Model Variations and Isomer Equilibrium Assumptions
In standard $r$-process networks (including those used in Martin 2016), each isotopic species is assumed to occupy its ground state or to maintain instantaneous thermal Boltzmann equilibrium with all low-lying excited states. However, in nuclei near the $N=82$ waiting point (e.g. $^{128}\text{Pd}$ $8^+$, $^{126}\text{Pd}$ $5^-/7^-$, $^{131}\text{In}$ $1/2^-$, and predicted isomers such as $^{129}\text{Pd}$ $19/2^-$):
1. When isomer de-excitation is hindered by large spin differences ($\Delta J \ge 3$ or $K$-forbiddenness) and low transition energies, thermal coupling requires photo-excitation through intermediate "doorway" states.
2. If thermalization timescales are slower than expansion and $\beta$-decay timescales, the isomer and ground state act as decoupled "astromers" with distinct neutron-capture cross sections and beta-decay half-lives.
3. As demonstrated by Martin 2016's sensitivity to $S_n$, if an isomer has an effective neutron separation energy $S_n^{\text{iso}} = S_n^{\text{g.s.}} - E_x$, its photodissociation rate is enhanced, which can alter local reaction paths during freeze-out.

## Source Self-Audit

- Audit date: 2026-11-07 by Codex research agent (self-audit, not human-reviewed).
- File lineage check: identified published PRL version (6 pages, 794,047 bytes, SHA `bcc1be25...`) vs CHORUS accepted manuscript (7 pages, 1,708,925 bytes, SHA `c9045474...`).
- Consistency check: verified that six Skyrme EDFs are SkM*, SkP, SLy4, SV-min, UNEDF0, and UNEDF1 matching Ref. [42] (Erler et al. Nature 2012).

## Extracted Pages

- PDF p. 1 (121101-1): Motivation; astrophysical sites (NS mergers vs jet-like SNe); Skyrme EDF selection; abstract.
- PDF p. 2 (121101-2): Reaction network description; TALYS statistical rate calculations; Fig. 1 abundance uncertainty bands.
- PDF p. 3 (121101-3): Fig. 2 analysis of $S_{2n}$ trends along isotopic chains and comparison of freeze-out vs final abundances for SkM*, SLy4, and UNEDF0.
- PDF p. 4 (121101-4): Microscopic origin of abundance troughs and peaks; discussion of deformation transitions around $N=82$ and $N=126$.
- PDF p. 5 (121101-5): Sensitivity of jet-like SNe vs NS mergers; fission recycling impact on $A \sim 130$.
- PDF p. 6 (121101-6): Conclusions and references (1–66).

## 2026-11-27 — 馆藏原件与覆盖核对

- {"pdf_pages": "1–2", "sections": "首页书目信息、引言、Objectives、Method、Results 起段。第 2 页图 1 为两种天体情景的丰度与不确定度带。"}
- {"pdf_pages": "3–4", "sections": "Results 续段及 Conclusions 起段。第 3 页图 2 为三个 EDF 的分离能、冻出路径与最终丰度。第 4 页图 3 为分离能、示意反应路径与四极形变。"}
- {"pdf_pages": "5–6", "sections": "第 5 页为结论续段、致谢、作者联络注和文献 [1]–[47]，第 6 页为文献 [48]–[69]。"}
- 本次获取的具体覆盖：顺读物理第 1–6 页的原件提取文本，覆盖正文、三幅图的图注、可提取符号和完整参考文献表。建议接受既有同版的全文文本覆盖。既有 deep-read 中的图形与公式核验待勘误及管理者查图后验收。本次无视觉核验。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A18-1 | 六套 EDF 的丰度分散随质量数而变。在中子星并合计算中，第二峰 A≈130 附近的带较窄，第三峰 A≈195 之前变宽。喷流状超新星在第二峰前后的带较并合情景更宽。太阳系 r 过程丰度有些点落在带外。 | 模型计算及与外部丰度数据对照 | source-reported | 物理第 2 页 Results、图 1(a,b) 图注及第 3 页 Results 开头。曲线、灰带与太阳系标点的相对位置待查第 2 页图 1。 | true |
| A18-2 | 在中子星并合模型中，三个示例 EDF 在 A≈120–140 和 A≈180–200 分别呈现与 N=82 和 N=126 相关的分离能快速变化。第三峰在冻出时的质量数小于最终峰位。 | 模型计算结果 | source-reported | 物理第 3 页图 2 上、下排及 Results 正文。峰位和冻出点对应关系待查同页图形。 | true |
| A18-3 | 作者把第三峰向较大质量数的移动归因于冻出后的中子俘获，指出 β 延迟中子与裂变可补充中子。并合情景的最终第二峰主要由裂变供给，该处较窄的模型间分散与六套计算共用裂变输入有关。 | 原作者对计算结果的解释 | source-reported | 物理第 2 页图 1 旁 Results、第 3 页图 2 旁的冻出讨论、第 4 页关于最终第二峰的段落。 | true |
| A18-4 | 作者以 S₂ₙ/2=1.5 MeV 示意平衡路径，解释 SLy4 的非单调分离能如何使物质在固定 Z 上经历较长的中子俘获序列，对应第三峰前 A≈180 的丰度低谷。UNEDF0 的分离能变化较平缓，作者用不同 EDF 对形状过渡细节的预测解释这种差异。 | 原作者对模型机制的解释 | source-reported | 物理第 3 页图 2(b)、第 4 页图 3(a–d)及相邻正文。示意线、箭头和形变图例待查第 4 页。 | true |

偶偶核质量取自文献 [42] 的六套 Skyrme EDF，奇 A 和奇奇核质量用相邻偶偶核及平均配对能隙估计。物理第 2 页 Method 说明用 TALYS 计算 Maxwell 平均中子俘获率，以含配分函数的细致平衡求光致解离率，再输入文献 [50] 所指反应网络。轨迹来源为文献 [4] 和 [9]。质量表、文献 [42] 的补充材料、TALYS 手册和被引轨迹均只追溯到本文的引用。

- 改正 MAR16-3 及摘要对第二峰的归因。物理第 4 页指出 UNEDF0 在 Z≤40 的极富中子核中预测 N=82 壳闭合减弱，冻出丰度缺第二峰，最终第二峰仍主要来自裂变。图 1–2 的丰度按质量数 A 表示，应将“最终元素分布”改为“最终质量数丰度分布”。
- 改写 MAR16-4 为“光致解离率对分离能呈指数依赖”，定位物理第 2 页 Method。该页提取文本只支持定性陈述。删除归于本文的显式指数公式、300–500 keV 幅度及数量级换算。物理第 4 页的 S₂ₙ/2=1.5 MeV 是图 3 的代表性示意条件。
- 移除本文直接证据栏中的 astromer 热平衡假设、具体异能态、异能态分离能修正及其网络效应。物理第 2 页的热力学平衡假设属于 TALYS 统计模型说明。核素与 astromer 标签如用于专题关联，应标为外部背景。
- 将图 2 定位为物理第 3 页、图 3 定位为第 4 页、结论定位为第 4–5 页、参考文献定位为第 5–6 页 [1]–[69]。第 2–4 页 SkM 后的控制字符按对照条目转写为 SkM*，反应括号及等号乱码在对应页核字。第 4 页图 3 的 Z 标签断字须查原图。第 6 页文献 [48] 的姓氏提取为 Aprahamianan，查该页原字形后再决定是否订正。
