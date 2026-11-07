---
type: source
title: 'Hennig等 2007: Pixie-16数字数据获取模块多机箱时钟与触发背板同步技术（NIM B）'
aliases: [Hennig 2007 Pixie-16 sync, 'arXiv:nucl-ex/0701016', NIM B 261 1000]
created: 2026-11-08
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: read
title_original: Clock and Trigger Synchronization between Several Chassis of Digital Data Acquisition Modules
authors: [W. Hennig, H. Tan, M. Walby, P. Grudberg, A. Fallu-Labruyere, W. K. Warburton, C. Vaman, K. Starosta, D. Miller]
journal: Nuclear Instruments and Methods in Physics Research Section B
year: 2007
volume: 261
pages: 1000-1004
doi: 10.1016/j.nimb.2007.04.181
arxiv: nucl-ex/0701016
canonical_source: https://doi.org/10.1016/j.nimb.2007.04.181
citation_key: ''
raw_file: raw/papers/gpt/query/20261108-foundations-G32/hennig-2007-pixie16-clock-trigger-sync.pdf
raw_sha256: e077cdcfd462610a80467024aac3446a562e2e4eaffbc813578a0b9bb86e0449
raw_storage_status: fully-archived-local
archive_required: true
nuclei: []
reactions: []
experiments: [pixie-16-pxi-chassis-sync]
models: []
observables: [clock-jitter, trigger-distribution, synchronization-stability]
methods: [digital-data-acquisition, pxi-backplane-star-trigger, clock-distribution, fpga-trigger-bus]
tags: [digital-daq, pixie-16, clock-synchronization, trigger-distribution, pxi-crate]
---

# Hennig2007：多机箱时钟与触发的实际测试边界

## Bibliographic Record

*Clock and trigger synchronization between several chassis of digital data acquisition modules*，NIMB261,1000–1004(2007)，正确DOI `10.1016/j.nimb.2007.04.181`。
总控按Crossref原响应及本地PDF首页核作者。旧`.04.148`属于CR-39刻蚀论文，与本文无关，已撤回。
实际底本为arXiv入口取得的7物理页预印本，非5页期刊排版；vN未独立核定，字节由SHA固定。
题录响应已追加归档至G32集合，PDF原字节保持不变。

## Scope and Reading Depth

G32研学；总控独立核PDF1、3–4的设置、Fig3/4/5讨论和结论，未复现硬件测试。
不声称已读期刊最终版或核准2026全部模块性能。

## Summary

四机箱SeGA DDAS的同步目标、机箱内波形时间测试和跨机箱示波器时钟变化测试不同。
峰位偏差、FWHM和长期最大变化不能合并成一个“RMS抖动”。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HE07-1 | 设计用于四PXI机箱、超过600个SeGA通道；摘要目标为同步波形抖动小于1ns | design-target | direct-original | PDF1摘要/引言 | false |
| HE07-2 | 同机箱三模块33通道分路脉冲，700组波形；各相对时间分布FWHM小于300ps，峰位可有固定线缆偏移 | reported-test | direct-original | PDF3 §3 Fig3讨论 | false |
| HE07-3 | 跨机箱模块时钟示波器最大变化约1.5ns，受探头反射/失真影响，是最坏情况估计；文末计划后续同步波形测试 | reported-test-and-boundary | direct-original | PDF3 Fig4讨论、PDF4结论 | false |

## Competing Interpretations and Limitations

“<20ps RMS”与“最多8机箱已验证”不受本次原读支持，已删除。
跨机箱示波器最大包络变化不是同机箱脉冲时间FWHM，也不是所有模块的绝对同步保证。
作者版本与测试时间是2007，不能作为今日硬件推荐或用户装置指标。

## Extracted Pages

[[doctoral-r1-g32-digital-daq-observable-chain-20261108]]保留事件采样相位、相对时钟及响应链区分。

## Agent Self-audit Triage

P0：错误DOI/作者列表及实际页数已从原件与注册题录更正。
P1：vN及期刊最终版未独立比较；未复现硬件或全范围扩展测试。
