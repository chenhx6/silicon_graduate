---
type: source
title: Crider等2016：68,70Ni寿命与分支比测定及形状共存两态混合模型分析
aliases: [Crider 2016 68Ni shape coexistence, Crider 2016 PLB, 10.1016/j.physletb.2016.10.020]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: Shape coexistence from lifetime and branching-ratio measurements in 68,70Ni
authors: [B. P. Crider, C. J. Prokop, S. N. Liddick, M. Al-Shudifat, A. D. Ayangeakaa, M. P. Carpenter, J. J. Carroll, J. Chen, C. J. Chiara, H. M. David, A. C. Dombos, S. Go, R. Grzywacz, J. Harker, R. V. F. Janssens, N. Larson, T. Lauritsen, R. Lewis, S. J. Quinn, F. Recchia, A. Spyrou, S. Suchyta, W. B. Walters, S. Zhu]
journal: Physics Letters B
year: 2016
volume: 763
pages: 108-113
doi: 10.1016/j.physletb.2016.10.020
arxiv: null
language: en
canonical_source: https://doi.org/10.1016/j.physletb.2016.10.020
zotero_item_key: null
citation_key: ''
zotero_uri: null
library_file: null
raw_file: raw/papers/gpt/query/20261108-foundations-G26/crider-2016-68ni-shape-coexistence.pdf
raw_sha256: 923ce537b505cecd49cdf75901bdd1be76896da0326ce29e8b049f10143d4b28
nuclei: [68Ni, 70Ni]
reactions: ['9Be(76Ge, X) fragmentation at 130 MeV/u', 68Fe(beta-)68Co(beta-)68Ni, 70Co(beta-)70Ni]
experiments: [NSCL-A1900-SeGA-LaBr3]
models: [LNPS-SM, MCSM-A3DA, two-level-mixing-model]
observables: [t1/2, branching-ratio, B(E2), rho2(E0), delta-r2, Q0]
methods: [electronic-fast-timing, beta-gamma-coincidence, GeDSSD-implantation]
tags: [shape-coexistence, a60, 68ni, e0-transition, e2-transition, two-state-mixing, doctoral-foundations]
archive_required: true
---

# Crider2016：先区分新测、采用量与两态模型

## Bibliographic Record

B. P. Crider等，*Shape coexistence from lifetime and branching-ratio measurements in 68,70Ni*，
PLB763,108–113(2016)，DOI `10.1016/j.physletb.2016.10.020`。
底本为六物理页出版PDF，原件路径/哈希见frontmatter。

## Scope and Reading Depth

G26读取主文；总控本轮独立核PDF2–5/printed109–112，尤其Table1、Fig1–3与两态分析。
已读实验链、寿命/分支、条件形状抽取与理论比较；没有事件级数据、完整Cov或作者计算代码。
参考文献所引Suchyta等并未因此全部重新原读；其量标为本文采用。

## Summary

新测68Ni的0₃半衰期与弱430keV分支，将绝对EM信息补入构型混合问题。
作者在限定两态模型中求混合度，再结合采用的E0强度求半径差与轴向内禀Q。
这条推断链不能压缩成“直接测到0⁺椭球”。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CR16-1 | 68Ni0₃的t₁/₂=0.57(5)ns；70Ni候选(0₂)的t₁/₂=1.65⁺⁰·³⁰₋₀·₂₅ns | reported-experiment | direct-original | PDF2、PDF4 Table1 | false |
| CR16-2 | 430keV的2₁→0₂分支为0.12(3)%；结合采用的2₁半衰期0.31(5)ps得到B=147(46)e²fm⁴，向0₁为52.5(84) | experiment-with-adopted-input | direct-original | PDF2末、PDF4 Table1及脚注b | false |
| CR16-3 | 0₂能量1604keV，0₃为2511keV；其球/扁/长形状与组态联系来自模型比较 | state-identity-and-model-attribution | direct-original | PDF2首、PDF4 Fig3及模型段 | false |
| CR16-4 | 两态模型给cos²θ=0.74(7)；采用ρ²=0.0076(4)后得半径差0.17(2)fm²；轴向等附加假设下\|Q₀\|=93(5)efm² | conditional-model-extraction | direct-original | PDF3/printed110右栏 | false |
| CR16-5 | 原文所引A3DA/LNPS对68Ni0₃半衰期预测108ns/1.5ns，与0.57(5)ns不同 | cited-model-comparison | direct-original-comparison | PDF4/printed111 | false |

寿命实验用像素快塑闪及LaBr3/SeGA，弱分支实验另用GeDSSD和SeGA。
两次实验的共同采用量仍须保留依赖；0₃→0₁/0₂的E0为上限，不是零值。

## Competing Interpretations and Limitations

两态抽取忽略更高态与未混合交叉矩阵元；单体E0算符在任意构型基底并非自动对角。
内禀Q绝对值不能决定形变正负，0⁺的实验室Qs恒零。
能量或一个强度的符合不能消除模型对其它寿命的偏差；原文模型比较只代表其2016范围。
“基态球形”是内禀表示/模型语言，不自动意味着无四极关联或无量子涨落。

## Extracted Pages

持久推理与迁移问题见[[doctoral-r1-g26-a60-collectivity-20261108]]。
本页不把该实验当高自旋60Ni或其它核芯的直接测量。

## Agent Self-audit Triage

P0：原件身份/哈希已核；旧稿1770keV与混合实验装置等误写已纠正。
P1：未重读采用量的全部原始来源、没有完整Cov/事件重放；两态和轴向映射为条件模型。
没有发生用户逐项审核，不以历史review标签赋予事实资格。
