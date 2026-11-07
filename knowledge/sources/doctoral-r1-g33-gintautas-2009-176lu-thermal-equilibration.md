---
type: source
title: 'Gintautas 2009: 176Lu via K-mixing thermal equilibration in the s-process'
aliases: [Gintautas 2009 176Lu thermal equilibration, Gintautas 2009 PRC 80 015806]
created: 2026-11-08
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: article
reading_depth: read
title_original: Thermal equilibration of 176Lu via K mixing
authors: [V. Gintautas, A. E. Champagne, F. G. Kondev, R. Longland]
journal: Physical Review C
year: 2009
volume: 80
pages: 015806
doi: 10.1103/PhysRevC.80.015806
arxiv: 0804.0223v1
language: en
canonical_source: https://doi.org/10.1103/PhysRevC.80.015806
citation_key: ''
raw_file: raw/papers/gpt/query/20261108-foundations-G33/gintautas-2009-176lu-thermal-equilibration.pdf
raw_sha256: abb6c1656b00e5db22c1c4ea19f54dbdc3b9557d7a8665945a7c0400492770d8
archive_required: true
nuclei: [176lu, 176hf, 177lu, 177hf, 180ta]
reactions: ['175Lu(n,gamma)176Lu', '176Lu(gamma,gamma'')176Lu']
observables: [stellar-half-life, equilibration-timescale, transition-rates, k-mixing-matrix-element]
methods: [two-cluster-master-equation, detailed-balance, coriolis-k-mixing, quasi-steady-state-elimination]
tags: [astromer, 176lu, thermal-isomer-network, k-mixing, s-process-thermometer]
---

# Gintautas等：176Lu的K混合与热交换网络

## Bibliographic Record

V. Gintautas、A.E. Champagne、F.G. Kondev、R. Longland，*Thermal equilibration of 176Lu via K mixing*，
PRC80,015806(2009)，DOI `10.1103/PhysRevC.80.015806`。
实际底本arXiv0804.0223v1，9物理页，提交2008-04-01；内部Dated2018与之不同，原因未查明。
路径与SHA见frontmatter，最终期刊版未逐字对照。

## Scope and Reading Depth

G33读模型、路径及热率主线；总控独立核PDF1–2、4–5的参数、Table I、Fig3、Eqs16–27。
没有原始实验数据、全网络producer或后续2026能级评价。
文中引用的能级/寿命与模型假设分开，不声称所有引用均已独立原读。

## Summary

作者研究低K与高K长期组分通过中间态交换的速度，
并探索约725keV两个7⁻态K混合的可能作用。
快带内平衡与慢跨簇交换可以分离；这需要实际路径与反应时间尺度，不能只看基态—异能态能隙。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GI09-1 | 文中采用176Lu7⁻长寿命基态、122.9keV1⁻异能态与838.6keV5⁻桥接路径 | adopted-level-structure | direct-original | PDF1–2 §I–II | false |
| GI09-2 | 724.7与725.2keV同7⁻态的K混合为模型建议；V未知，依517eV观测间隔的两态关系作参数扫描，上界258.5eV | model-hypothesis-and-input | direct-original | PDF2–4 Fig2、Eqs16–17、Table I | false |
| GI09-3 | Fig3的T9=.25、混合概率9.40×10⁻³%、仅g初始及无β损失算例：簇内约.1/1ns，跨簇约10⁵s | controlled-model-result | direct-original | PDF4–5 Fig3及说明 | false |
| GI09-4 | 带内热权重进入两个有效方程；含β破坏时用整个率矩阵本征值讨论有效寿命和交换 | model-method | direct-original | PDF5 Eqs18–27 | false |

## Competing Interpretations and Limitations

未知V与计算的分宽不是测量。直接母态ΔK不是每个分支的禁戒度ν；
须按各跃迁L、三角条件和K差检查，不能写“7单位K差就是ν=7”或普适100每度。
簇总布居、带头布居与单能级详细平衡须按各自定义处理。
有破坏/生产或变温时，一个固定热化温度及1/(两率和)不足以概括全部演化。
725keV路线是否有新实验需另查，原文未知不自动成为2026仍未发现。

## Extracted Pages

[[doctoral-r1-g33-thermal-isomer-network-20261108]]给成对EM、簇权重及开放两簇矩阵的任务重建。

## Agent Self-audit Triage

P0：原件身份/9页与条件算例已核；P1为V、部分分支、最终出版差分及实际天体输入。
