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
raw_file: "raw/papers/gpt/learning-daily/20261031-OPEN-RESEARCH-source-recovery/46gk-nqsh.pdf"
raw_sha256: 12f37107ee755ff38ed1351d6044c6b90b08433e4a2834357afaac32ce773610
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
| KAR25-2 | Band 2 向 Band 1 的跃迁展现出随自旋下降的摆动能量 $E_{\text{wob}}(I) = 750 \to 450\text{ keV}$ 与增强的带间 $B(E2)/B(E2)_{\text{in}} \approx 0.40 - 0.70$；作者据此将其解释为基于基态构型（$j_s=11/2$）的一声子横向摆动模式 Mode 1。 | experimental-result | direct | Sec. IV, Fig. 5 | false |
| KAR25-3 | Band 4 向 Band 3 展现带间跃迁阶梯和相近的跃迁比；作者将其解释为基于第二准中子取向构型（$j_s=7/2$）的另一一声子横向摆动分支 Mode 2。 | experimental-result | direct | Sec. IV, Fig. 6 | false |
| KAR25-4 | TPSM 波函数投影给出 Band 3 的短轴角动量投影接近 $j_s \approx 7/2$，并使作者的 doublet-wobbling assignment 相比 `n_w=2` 解释更有利；这是模型支持，不是独立几何测量。 | model-result | direct | Sec. V, Fig. 8, Table II | false |
| KAR25-5 | 作者用 DCO、偏振和相对强度讨论小 `|δ|` 解、IBFM M1 主导解释与 TiP 假说；这些结果限制了竞争解释，但没有在缺少绝对寿命/完整响应协方差时完全排除所有替代机制。 | author-interpretation | direct | Sec. VI, Discussion | false |

## Cross-Mass-Region Transferability Significance

1. **A≈100 对决 A≈130/160 的模型机制差异**：作者在 $^{105}\text{Pd}$ 的三轴软度和准中子取向框架中提出两个平行 `n_w=1` 分支；这提供可检验的配置机制比较，不能单独作为跨质量区模式定律。
2. **实验判据的谨慎使用**：本文支持在没有完整多声子阶梯、绝对寿命和共同 response/covariance 时，不应仅凭能量接近 `2ℏω_w` 就把伴带定性为两声子态。

## Summary

本页摘要以现有书目、原有正文和已有 claim 表为准；本次补齐结构，不新增来源事实。

## Key Results


| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KAR25-1 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | \delta | source-reported | experimental-result | direct |
| KAR25-2 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | experimental-result | source-reported | Sec. IV, Fig. 5 | false |
| KAR25-3 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | experimental-result | source-reported | Sec. IV, Fig. 6 | false |
| KAR25-4 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | model-result | source-reported | Sec. V, Fig. 8, Table II | false |
| KAR25-5 | 对应上方 “Key Findings and Claims” 的同号条目；本表只提供治理字段索引。 | δ | source-reported | author-interpretation | direct |

原页面既有的直接报告、作者解释和模型结果保持原文分层；缺失 locator 或原件的项目仍保持相应证据边界。

## Competing Interpretations and Limitations

竞争解释、来源依赖、原件访问和必要伴随观测缺口按原页面记录；不得把模型结果或评价字段升级为直接实验事实。

## Extracted Pages

本页当前只保留已有 locator；未取得的原始页码、图表或附件不补写，后续摄入必须记录实际阅读范围。
