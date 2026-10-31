---
type: source
title: "Denisov 2013：多维团簇放射性模型、动态形变与惯性边界"
aliases: [Denisov 2013 multidimensional cluster radioactivity]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
source_type: journal-article-theory
reading_depth: skimmed
canonical_source: "Phys. Rev. C 88, 044608 (2013); arXiv:1311.3810v1"
raw_file: "raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/denisov-2013-multidimensional-cluster-arxiv1311.3810v1.pdf"
raw_sha256: "cf00e8012f9100edb443571cbd77c1af14b251dc6a78bb81f1c1e02ef6f181be"
title_original: "Multidimensional model of cluster radioactivity"
authors: [V. Yu. Denisov]
year: 2013
journal: Physical Review C
volume: "88"
pages: "044608"
doi: "10.1103/PhysRevC.88.044608"
source_url: "https://arxiv.org/abs/1311.3810v1"
raw_storage_status: "raw-pdf-archived-new-original"
staging_file: "tmp/day26-cluster/1311.3810.pdf"
staging_sha256: "cf00e8012f9100edb443571cbd77c1af14b251dc6a78bb81f1c1e02ef6f181be"
nuclei: [228Th, 208Pb, 20O, 232U, 236Pu, 242Cm]
observables: [cluster-half-life, action-integral, barrier-height]
methods: [extended-Thomas-Fermi, Skyrme-SkM-star, shell-correction, multidimensional-WKB]
tags: [cluster-radioactivity, dynamical-deformation, preformation, collective-inertia]
---

# 多维团簇放射性模型

## Bibliographic Record

Crossref题名、作者和 DOI 与 arXiv:1311.3810v1 首页相符。实际读取12页、1068033 bytes的预印本；PDF签名和 SHA-256 已核验，已逐文件核验后以新增原件归档至frontmatter所列raw路径，没有覆盖既有文件。

## Scope and Reading Depth

定向阅读PDF1–2、5–10：密度参数化、势能/壳修正、Eqs21–31、惯性和最小作用量路线、228Th比较及局限。没有复算ETF能量、动态轨迹或参数标定。

## Summary

多维动态片段形变与壳修正可改变团簇通道作用量；作者设形成因子S=1，因此半衰期符合不构成独立P0测定。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DE13-1 | 以团簇与子核的距离和动态表面形变为多维坐标，用ETF/Skyrme+壳修正求势能并最小化WKB作用量；动态形变可降低球形片段路径的势垒，但结果同时依赖惯性。 | model-method | direct-original-preprint | PDF1–2, PDF5–8, Eqs16–31 | true |
| DE13-2 | Eq21写T=ln2/[nu S T(Q)]，但作者在实际密度ansatz中设预形成因子S=1；这不是测得所有核中P0=1。 | model-assumption | direct-original-preprint | PDF5–6, Eqs21–24 | true |
| DE13-3 | 惯性使用水动力学值再乘增强因子，部分因子受片段E2数据约束；惯性改变可显著改变作用量及半衰期。 | model-input-and-limit | direct-original-preprint | PDF6–9, Eqs25–31 | true |
| DE13-4 | 228Th→208Pb+20O的计算半衰期约5.0×10^20 s，与本文引用的实验(5.29±1.01)×10^20 s相近；不是新的独立实验。 | model-comparison | direct-original-preprint | PDF9 | true |

## Competing Interpretations and Limitations

该模型把团簇预先包含于密度参数化，设S=1并在路径/惯性中承载内部重排代价。它与采用P0≪1的势垒模型可以描述同一衰变率；P0的分解依赖模型定义。动态表面形变不能被自动等同为某一固定beta3、beta5或beta7；本文不提供单独逐阶的beta5/beta7实验增强倍数。

## Knowledge Impact and Learning Decision

支持形变改变势垒与作用量的机制；限制“成功拟合半衰期就测得P0”及“动态形变必等同于基态八极形变”的解释。综合见 [[octupole-cluster-radioactivity-preformation-boundary]]。

## Extracted Pages

- [[octupole-cluster-radioactivity-preformation-boundary]]

## Review Status

Codex source self-audit，保留needs_review。
