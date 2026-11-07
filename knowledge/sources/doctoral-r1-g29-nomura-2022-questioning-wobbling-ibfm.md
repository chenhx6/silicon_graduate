---
type: source
title: 'Nomura & Petrache 2022: 相互作用玻色子-费米子模型探索γ软核低自旋带性质'
aliases: [Nomura Petrache 2022 PRC, IBFM wobbling questioning, 10.1103/PhysRevC.105.024320]
created: 2026-11-08
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: read
title_original: Questioning the wobbling interpretation of low-spin bands in γ-soft nuclei within the interacting boson-fermion model
authors: [K. Nomura, C. M. Petrache]
journal: Physical Review C
year: 2022
volume: 105
pages: '024320'
doi: 10.1103/PhysRevC.105.024320
arxiv: 2106.15384v3
canonical_source: https://doi.org/10.1103/PhysRevC.105.024320
citation_key: ''
raw_file: raw/papers/gpt/query/20261108-foundations-G29/nomura-2022-questioning-wobbling-ibfm.pdf
raw_sha256: 127e2f814f743ead8129e84f293ea6a554d83acbd8e50e441e971fa011ee7b06
raw_storage_status: archived-local
archive_required: true
learning_candidate: true
nuclei: [135pr, 133la, 127xe, 105pd]
models: [IBFM, mapped-IBM-2, Gogny-D1M, DD-PC1]
observables: [mixing-ratio, b(e2), b(m1), energy-staggering]
methods: [boson-fermion-mapping, potential-energy-surface-mapping, electromagnetic-transition-analysis]
tags: [wobbling-counter-evidence, ibfm, gamma-softness, a130, mixing-ratio, gamma-vibration]
---

# Nomura & Petrache2022：低自旋带的替代IBFM解释

## Bibliographic Record

K. Nomura、C.M. Petrache，*Questioning the wobbling interpretation of low-spin bands in γ-soft nuclei within the interacting boson-fermion model*，PRC105,024320(2022)，DOI `10.1103/PhysRevC.105.024320`。
实际底本arXiv2106.15384v3，12物理页；旧稿“10页”错误已更正。

## Scope and Reading Depth

G29研读；总控独立核PDF1–4、9–10，重点模型构造/拟合、Table I–II及M1/E2分解。
未重新运行IBFM，无实验原始数据；137/135等不同实验引用不能按作者相同就计独立。
本工作算例135Pr、133La、127Xe、105Pd，不是130Ba两费米子模型。

## Summary

作者用映射IBM-2核芯与奇费米子耦合，对若干低自旋候选带给替代解释。
其能谱与EM可比较，但PES映射没有固定所有耦合/磁响应参数。
与旧/新实验混合比的差别须逐核逐带说明，不能写整个A130的普适否定。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| NP22-1 | 核芯用GognyD1M(132Ba/128Xe)或DD-PC1(134Ce/106Pd)；IBM-2加单h₁₁/₂费米子/空穴空间 | model-construction | direct-original | PDF2 Fig1、Eqs.1–2及正文 | false |
| NP22-2 | IBM参数按PES映射；质中形变设相等，某些Majorana项不向该PES增加独立贡献，因此不能单靠该映射确定其强度 | identifiability-and-assumption | direct-original | PDF3 Eq3后 | false |
| NP22-3 | Γ₀、Λ₀、A₀耦合用各奇核低能能级拟合；Table I另列eB/gB与占据输入 | fitted-model-input | direct-original | PDF4 Eq6后及Table I | false |
| NP22-4 | 对135Pr21/2连接，IBFMδ=−0.368，Table II同时列旧实验−1.54(9)与新−0.37⁺⁰·¹⁰₋₀·¹⁴ | model-versus-cited-experiments | direct-original | PDF9 Table II，Eγ约813keV行 | false |
| NP22-5 | 并非表内每项都\|δ\|<1：127Xe13/2行模型−5.699；作者分解指出该点M1很小，导致δ偏大 | table-specific-exception-and-operator | direct-original | PDF9 Table II及§III.D | false |

摘要/结论的“consistent small”是作者总体措辞，不能覆盖Table II例外。
大δ可能来自M1分母小，不自动说明绝对E2集体增强。

## Competing Interpretations and Limitations

磁算符、核芯映射与费米子空间有条件；引入不同耦合和其它轨道可能改变结果。
γ软核芯不自动意味着每条激发带就是纯K=2形状声子；三轴情形K也未必是好量子数。
本文提供替代计算，未证明所有奇A/偶偶候选均被排除，更未证明130Ba真实机制。
旧稿的“作者自我证伪历史”、统一1MeV软度线与未作扫描的稳健性断言已撤回。

## Extracted Pages

见[[doctoral-r1-g29-a130-core-orientation-20261108]]；与130Ba只作方法比较，
不能把一费米子核芯模型当作其两准粒子逐态计算。

## Agent Self-audit Triage

P0：版本、页数、IBM-2/两类EDF与Table II已核。
P1：算符有效参数/模型空间、不同实验根分支和完整Cov仍须具体比较；未重跑代码。
