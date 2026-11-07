---
type: source
title: 'Gosselin 2010: Stellar plasma electronic process modifications of K-isomers in 176Lu and 180Ta'
aliases: [Gosselin 2010 plasma isomers, Gosselin 2010 PRC 81 055808]
created: 2026-11-08
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: article
reading_depth: read
title_original: 'Modification of nuclear transitions in stellar plasma by electronic processes: K isomers in 176Lu and 180Ta under s-process conditions'
authors: [G. Gosselin, P. Morel, P. Mohr]
journal: Physical Review C
year: 2010
volume: 81
pages: 055808
doi: 10.1103/PhysRevC.81.055808
arxiv: 1005.2151v1
language: en
canonical_source: https://doi.org/10.1103/PhysRevC.81.055808
citation_key: ''
raw_file: raw/papers/gpt/query/20261108-foundations-G33/gosselin-2010-176lu-180ta-plasma-transitions.pdf
raw_sha256: ee1165a0508ddbab27d648f5a02e47e4ecc6c97ebe0f6ea53efb818b93c932fa
archive_required: true
nuclei: [176lu, 180ta]
reactions: ['176Lu(gamma,gamma'')176Lu', '180Ta(gamma,gamma'')180Ta']
observables: [internal-conversion-coefficient, neec-rate, transition-width, integrated-cross-section]
methods: [average-atom-plasma-model, neec-enhancement, detailed-balance, dirac-fock-screening]
tags: [plasma-atomic-physics, neec, internal-conversion, 176lu, 180ta, astromer]
---

# Gosselin等：单跃迁电子增强与整体异能态交换

## Bibliographic Record

G. Gosselin、P. Morel、P. Mohr，*Modification of nuclear transitions in stellar plasma by electronic processes: K isomers in 176Lu and 180Ta under s-process conditions*，
PRC81,055808(2010)，DOI `10.1103/PhysRevC.81.055808`。
实际arXiv1005.2151v1、10物理页，提交2010-05-12；内部Dated2018的原因未查明。
路径与原件哈希见frontmatter。

## Scope and Reading Depth

G33研学主线；总控独立核PDF1–3/5的摘要、桥接结构、率定义和电子机制。
未运行等离子体/网络代码、未逐项重算所有图或取得所有引用的原始实验。
读到的单支路与整体率是不同对象，不以摘要中的一个增强因子代替全模型。

## Summary

作者在指定s过程等离子体条件下研究NEEC、电子散射、NEET等对单条跃迁的影响，
并另算通过中间态的low-K/high-K整体率。
其关键结果是局部可明显增强，整体却仍可受另一侧瓶颈控制。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GO10-1 | 电子环境可能改变低能核跃迁及IC/逆过程；NEEC是本文较重要的单跃迁增强机制 | model-result | direct-original | PDF1摘要/引言及§III | false |
| GO10-2 | 作者算例中180Ta一条低能跃迁可增强约10倍，但Lu/Ta整体跨K率及所讨论s过程核合成基本不变 | model-result-with-network-boundary | direct-original | PDF1摘要，§IV–V | false |
| GO10-3 | 中间态两侧部分宽度共同决定有效桥接截面，单侧增强不能独立决定整体变化 | model-mechanism | direct-original | §II桥接率/积分截面定义 | false |

## Competing Interpretations and Limitations

低于100keV的明显作用及更高能区较弱作用属于作者环境中的趋势，非自然界的硬开关。
不能无说明把实验室中性原子总寿命/转换系数原样套入电离环境。
成对EM反向关系与开放网络的总布居/破坏不同；若环境非LTE，须重建一致的电子/光子率。
此文没有证明所有NEEC机制都无观测效应，也未提供所有天体的存活丰度。

## Extracted Pages

[[doctoral-r1-g33-thermal-isomer-network-20261108]]将本反例与高K路径、快态消去及整体本征时间联系。

## Agent Self-audit Triage

P0：版本/题录与局部—整体结论已核；P1为原代码、网络分支误差与其它环境未重放。
