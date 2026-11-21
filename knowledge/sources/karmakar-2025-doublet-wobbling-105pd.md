---
type: source
title: "Karmakar et al. 2025 - Evidence of a doublet wobbling excitation mode in 105Pd"
aliases: [Karmakar 2025 105Pd doublet wobbling, doublet wobbling 105Pd, KAR25]
created: 2026-10-30
updated: 2026-11-21
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
archive_required: true
arxiv: "2403.08235"
nuclei: [105pd]
reactions: ["96Zr(13C,4n)105Pd @ 63 MeV"]
experiments: [INGA-TIFR]
models: [triaxial-projected-shell-model, particle-rotor-model]
observables: [multipole-mixing-ratio, wobbling-energy, interband-e2-strengths, bm1-be2-ratio, angular-distribution-dco]
methods: [dco-ratio, linear-polarization, gamma-gamma-coincidence, tpsm-diagonalization]
tags: [experiment-ingest, doublet-wobbling, transverse-wobbling, one-neutron, tpsm, A100, 105Pd, Day27]
---

# Evidence of a doublet wobbling excitation mode in 105Pd

## Bibliographic Record

*Phys. Rev. C* **112**, 034323 (2025)，DOI `10.1103/46gk-nqsh`。阅读底本为 APS 刊版。

## Scope and Reading Depth

已核对刊版 14 页，包括实验、模型与附录 A/B。Tables I–II 及其关联门和读图条件按原刊追溯。

## Summary

本篇报道与 [[timar-2019-transverse-wobbling-105pd]] 不同的 TIFR INGA 采集。两文的 991、1034、994 keV 连接分别标为 Karmakar 的 Band 3→1 和 Timár 的 B→A。2025 年增加 Band 4→2 的两条低能连接，并用 TPSM 提出两组一声子摆动候选。带号以各文的能级与跃迁对应为准。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KAR25-1 | 数据来自 63 MeV 的 \(^{96}\mathrm{Zr}(^{13}\mathrm C,4n)\) 反应。作者用 1100-keV E2 和 1331-keV E1 的 \(R_{\rm DCO}\) 定出 \(\sigma/J=0.31(3)\)，按 40°/90° 与 157°/90° 两套矩阵计算不同响应。 | method-result | direct | PDF 2–4, Sec. II, Table I | false |
| KAR25-2 | 991.1、1033.8、993.8 keV 属 Band 3→1，Table II 给大正 \(\delta=1.9^{+0.4}_{-0.5}, 2.2^{+0.5}_{-0.4}, 2.4^{+0.8}_{-0.5}\)，以及 \(B(E2)_{\rm out}/B(E2)_{\rm in}=0.49(15),0.39(10),0.57(17)\)。Fig. 5 的偏振误差较大，作者结合 DCO 与偏振曲线判断。 | experimental-analysis | direct | PDF 4–7, Fig. 5, Table II | false |
| KAR25-3 | Band 4→2 的 253.6、299.6 keV 相同中心 \(\delta\simeq 0.3\)，表给 E2 相对强度比 \(1.23(75),1.45(98)\)。没有相应的实测偏振。低能跃迁可在小 E2 份额下仍给较大的相对 \(B(E2)\)。 | experimental-analysis | direct | PDF 6–7, Table II, PDF 12 Summary | false |
| KAR25-4 | Band 4↔3 的 \(\Delta I=1\) 支路以 M1 为主。作者把 Band 4 解释为短轴投影约 \(7/2\) 的另一准中子构型，并将 Band 2 解释为其一声子摆动；Band 3 则配对 Band 1。 | author-interpretation | direct | PDF 7 Table II and discussion, PDF 12 Summary | false |
| KAR25-5 | TPSM 用 \(\epsilon=0.26,\epsilon'=0.11\)，附录 A 用等效扇区重排量子化轴。附录 B 根据计算强度估计未见的 Band 2→4 连接。 | model-result | direct | PDF 7, Eqs. (1)–(3); PDF 12–13, Appendices A/B and Table III | false |

## Competing Interpretations and Limitations

Band 4→2 两条线的大小解来自 DCO 曲线。作者以大解导致异常大的相对 E2 强度为由选用较小分支，这一处没有独立偏振裁决。两条比值也共享已选混合支和同母态带内参照。Band 2→4 的未观测支路及 Band 4→2 的绝对偏振仍限制第二组结构的实验判定。关于双组一声子和双声子的区分，应把跨带支路、相对 E2 强度和模型的短轴投影分别追溯。

## Extracted Pages

PDF 1–4 核对文献身份、装置、门和 Table I；PDF 5–7 核对 Fig. 5、Table II、TPSM 输入；PDF 8–12 核对带对应、模型分解和结论；PDF 12–14 核对附录、未见支路估计及引文。
