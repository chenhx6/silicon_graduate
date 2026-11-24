---
type: source
title: "Piekarewicz 2004 - Unmasking the nuclear matter equation of state"
aliases: [Piekarewicz 2004 equation of state, ISGMR neutron skin, PIE04]
created: 2026-10-30
updated: 2026-11-22
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Unmasking the nuclear matter equation of state"
authors: [J. Piekarewicz]
journal: Physical Review C
year: 2004
volume: 69
issue: 4
pages: "041301(R)"
doi: "10.1103/PhysRevC.69.041301"
canonical_source: "https://doi.org/10.1103/PhysRevC.69.041301"
citation_key: piekarewicz2004unmasking
raw_file: "raw/papers/gpt/learning-daily/20261031-OPEN-RESEARCH-source-recovery/PhysRevC.69.041301.pdf"
raw_sha256: 885b59e7151a44b531f945dac490fe95151f1712b72b82608f85e47a65f674f8
nuclei: [90zr, 208pb]
reactions: []
experiments: []
models: [relativistic-mean-field, continuum-rpa, NL3-family]
observables: [ISGMR-strength-distribution, IVGDR-strength-distribution, symmetric-matter-incompressibility, neutron-skin]
methods: [continuum-RPA, resonance-centroid-comparison]
tags: [giant-monopole-resonance, neutron-skin, incompressibility, equation-of-state, Day27]
---

# Unmasking the nuclear matter equation of state

## Bibliographic Record

PRC 69, 041301(R) (2004), DOI `10.1103/PhysRevC.69.041301`.

## Scope and Reading Depth

刊版 PDF1–5 对应印刷 041301-1 至 041301-5。核对模型定义、Table I、Figs. 1–4、产生约束的联合比较和末页参考文献。实验质心和峰值来自文中所引来源。

## Summary

论文用相对论平均场和连续谱 RPA 计算 90Zr 与 208Pb 的等标量巨单极响应，以及 208Pb 的等矢量巨偶极响应。作者比较模型中能量质心对对称能密度依赖的敏感性，再按既有实验约束模型。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PIE04-1 | Table I 比较五组 NL3 变体。90Zr 计算质心约 18.62–18.77 MeV，对所选等矢参数不敏感。208Pb 的计算质心约 14.32–14.91 MeV，模型变化更显著。 | model-result | direct-to-model | PDF3 Table I and PDF4 Figs. 1–2 | false |
| PIE04-2 | Table I 把实验质心写为90Zr 的17.89(20) MeV、208Pb 的14.24(11) MeV，来自本文 Ref. [12]。计算质心采用不同核的指定能窗。 | cited-experimental-values | secondary-in-this-article | PDF3 Table I caption and experiment rows | false |
| PIE04-3 | 作者用 \(E_{\rm ISGMR}\propto\sqrt K\) 缩放估计，把原模型的对称物质不可压缩性 271 MeV 调整为 \(248\pm8\) MeV。原文指出完整调整需要重新标定模型。 | model-conditioned-inference | derived | PDF4, preceding discussion of Fig. 4 | false |
| PIE04-4 | 208Pb 的 ISGMR 质心和 IVGDR 峰值在该模型族中共同约束中子皮。作者据此给出约 \(R_n-R_p\lesssim 0.22\) fm 的推断。 | model-conditioned-inference | derived | PDF4 Fig. 4 and summary | false |

## Competing Interpretations and Limitations

计算结果限于所选模型族、能量窗口和缩放近似。旧条目中的富中子 Sn 软单极态、中子皮与核芯反相压缩、定量 \(K_\tau\) 等判断缺少本篇证据，已从本篇来源记录撤回。

## Extracted Pages

- [[soft-monopole-mode-and-ktau-divergence]] 记录历史模型练习与本篇来源的边界。
