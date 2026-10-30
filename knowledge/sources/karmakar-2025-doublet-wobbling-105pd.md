---
type: source
title: "Karmakar et al. 2025 - Evidence of a doublet wobbling excitation mode in 105Pd"
aliases: [Karmakar 2025 105Pd doublet wobbling, doublet wobbling 105Pd, KAR25]
created: 2026-10-30
updated: 2026-10-30
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Evidence of a doublet wobbling excitation mode in 105Pd"
authors: [A. Karmakar, P. Datta, N. Rather, S. Pal, R. Palit, A. Goswami, G. H. Bhat, J. A. Sheikh, S. Jehangir, S. Chattopadhyay, S. Frauendorf]
journal: Physical Review C
year: 2025
volume: 112
issue: 3
pages: "034323"
doi: "10.1103/46gk-nqsh"
canonical_source: "https://doi.org/10.1103/46gk-nqsh"
citation_key: karmakar2025doublet105pd
arxiv: "2403.08235"
nuclei: [105pd]
reactions: ["96Zr(13C,4n)105Pd @ 63 MeV"]
experiments: [INGA-TIFR]
models: [triaxial-projected-shell-model, particle-rotor-model]
observables: [multipole-mixing-ratio, wobbling-energy, interband-e2-strengths, bm1-be2-ratio, angular-distribution-dco]
methods: [dco-ratio, linear-polarization, gamma-gamma-coincidence, tpsm-diagonalization]
tags: [experiment-ingest, doublet-wobbling, transverse-wobbling, one-neutron, tpsm, A100, 105Pd, Day27]
---

# Evidence of a doublet wobbling excitation mode in `105Pd`

## Bibliographic Record

PRC 112, 034323 (2025), DOI `10.1103/46gk-nqsh`; arXiv:2403.08235v2.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: High-statistics Indian National Gamma Array (INGA) at TIFR measurement of $^{105}\text{Pd}$ via $^{96}\text{Zr}(^{13}\text{C},4n)$ at 63 MeV; Directional Correlation from Oriented states (DCO) and polarization asymmetry measurements; extraction of multipole mixing ratios $\delta(E2/M1)$; Triaxial Projected Shell Model (TPSM) calculations with full configuration space; resolution of the two-phonon vs doublet one-phonon controversy.
- Not covered: Lifetimes directly measured via DSAM (uses extracted branching and mixing ratios relative to intra-band transitions).
- Coverage caveats: Clarifies that band 3 (previously labelled band C in Timar 2019) is not an $n_w=2$ two-phonon wobbler, but rather a doublet one-phonon ($n_w=1$) wobbling excitation built on an excited quasineutron state with $j_s=7/2$ instead of $j_s=11/2$.

## Key Findings and Claims

| Claim ID | Claim Summary | Evidence Type | Direct/Derived | Locator | Review Flag |
|---|---|---|---|---|---|
| KAR25-1 | INGA-TIFR 实验测定 $^{105}\text{Pd}$ 包含四个负宇称带：Band 1（yrast，$\alpha=-1/2$），Band 2（$\alpha=+1/2$），Band 3（$\alpha=-1/2$）与 Band 4（$\alpha=+1/2$），跨带跃迁均展现出强烈的 E2 混合比 $|\delta| > 1.5$ 与正偏振度。 | experimental-result | direct | Sec. III, Table I | false |
| KAR25-2 | Band 2 向 Band 1 的跃迁展现出随自旋下降的摆动能量 $E_{\text{wob}}(I) = 750 \to 450\text{ keV}$ 与增强的带间 $B(E2)/B(E2)_{\text{in}} \approx 0.40 - 0.70$，确立为基于基态构型（$j_s=11/2$）的一声子横向摆动模式 Mode 1。 | experimental-result | direct | Sec. IV, Fig. 5 | false |
| KAR25-3 | Band 4 向 Band 3 同样展现出完整的带间跃迁阶梯，能量特征与跃迁比完全符合一声子横向摆动特征（$B(E2)/B(E2)_{\text{in}} \approx 0.35 - 0.65$），确立为基于第二准中子取向构型（$j_s=7/2$）的第二声子横向摆动模式 Mode 2。 | experimental-result | direct | Sec. IV, Fig. 6 | false |
| KAR25-4 | TPSM 微观波函数投影计算证明，Band 3 的内禀角动量在短轴上的投影仅为 $j_s \approx 7/2$，排除了 Timár 2019 提出的 $n_w=2$ 两声子解释，确立该核为核结构中首个被证实的“双重横向摆动（Doublet Wobbling）”体系。 | model-result | direct | Sec. V, Fig. 8, Table II | false |
| KAR25-5 | 针对 Nomura 2022 基于 IBFM 的 M1 主导质疑与 Lawrie 2020 的 TiP 假说，高精度 DCO 与偏振测量完全排除了小 $|\delta|$ 解，证实带间 $B(E2)$ 真实增强，消除了 A≈100 摆动模式存在的长期争议。 | author-interpretation | direct | Sec. VI, Discussion | false |

## Cross-Mass-Region Transferability Significance

1. **A≈100 对决 A≈130/160 机制差异**：在 $^{163}\text{Lu}$（A≈160）中，强拉长超形变（$\beta_2 \approx 0.40$）与 $i_{13/2}$ 质子的大角动量支持理想的谐振子式 $n_w = 0, 1, 2$ 多声子激发；而在 $^{105}\text{Pd}$（A≈100，$\beta_2 \approx 0.23, \gamma \approx 23^\circ$）中，三轴软度与准中子 $h_{11/2}$ 的非主轴取向自由度使得体系优先激发第二对齐取向（$j_s = 7/2$），从而形成两个平行的 $n_w = 1$ 双重摆动带，而非高阶多声子态。
2. **实验判据的严谨性**：确立了在没有多声子 $n_w=2 \to n_w=1 \to n_w=0$ 阶梯电四极辐射连续测定前，不可草率将能量接近 $2\hbar\omega_w$ 的伴带定性为两声子态。
