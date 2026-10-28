---
type: source
title: "NNDC Ra–Th团簇衰变评价：14C/20O分支、总半衰期与226Th通道边界"
aliases: [NNDC Ra Th cluster branching, Ra14C Th20O evaluated decay]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data
reading_depth: skimmed
canonical_source: "NNDC ENSDF Adopted 222Ra, 224Ra, 226Ra, 226Th, 228Th; acquired 2026-10-29"
raw_file: "raw/papers/gpt/day26-20261028/nndc-222ra-adopted-cluster-20261029.pdf"
raw_sha256: "3a681f65303cbaa9bba9541dfc439d5155c55f276256121d43652d8dc7004042"
title_original: "ENSDF Adopted Levels, Gammas: 222Ra, 224Ra, 226Ra, 226Th, 228Th"
authors: [NNDC ENSDF evaluators]
year: 2026
source_url: "https://www.nndc.bnl.gov/ensnds/"
raw_storage_status: "official-pdf-archived-new-original"
retrieved: 2026-10-29
nuclei: [222Ra, 224Ra, 226Ra, 226Th, 228Th]
observables: [half-life, cluster-branching-fraction, partial-half-life]
methods: [ENSDF-evaluated-data]
tags: [cluster-radioactivity, branching-ratio, evaluated-data, percentage-conversion]
---

# Ra–Th团簇衰变评价数据

## Bibliographic Record

读取官方 `https://www.nndc.bnl.gov/ensnds/<A>/<Element>/adopted.pdf`，2026年是本页获取时间，不是所有数据的评价年份。222Ra/224Ra/226Ra/226Th/228Th的literature cutoff分别为2023-09-25、2022-03-08、1996-02-01、1996-02-01、2012-12-31。精确URL、文件签名、页数和SHA-256载于 `octupole-cluster-radioactivity-boundary.json`；五份PDF均已逐文件核验后以新增原件归档至raw/papers/gpt/day26-20261028/，主raw_file指向222Ra，其余路径和哈希见审计JSON。

## Scope and Reading Depth

读取各核基态总半衰期、团簇分支、来源NSR码及限值注释：222Ra PDF2，其余核PDF1；226Th仅定向检查该表未给出团簇分支。没有把未列出解释为该通道物理上不可能，也没有宣称系统检索全部核数据后已证明零分支。

## Summary

归集Ra222/224/226的14C和Th228的20O评价分支，严格区分百分数、概率和部分半衰期；226Th未由本轮数据建立20O正测基准。

## Key Results

| ID | 核素与评价字段 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| NCRT-1 | 222Ra：总T1/2=33.6(4) s；%14C=3.0(10)×10^-8，对应无量纲分支b=3.0(10)×10^-10；引用1985Pr01/1985Ho21/1991Hu02。 | evaluated-decay-data | official-evaluated-object | 222Ra Adopted PDF2 ground-state comments | true |
| NCRT-2 | 224Ra：总T1/2=3.6316(23) d；%14C=4.0(10)×10^-9，故b=4.0(10)×10^-11；评价采用1992Ar02并列其他结果。 | evaluated-decay-data | official-evaluated-object | 224Ra Adopted PDF1 ground-state comments | true |
| NCRT-3 | 226Ra：总T1/2=1600(7) y；%14C=3.2(16)×10^-9，故b=3.2(16)×10^-11；评价引用1985Ho21及另一上限。 | evaluated-decay-data | official-evaluated-object | 226Ra Adopted PDF1 ground-state comments | true |
| NCRT-4 | 228Th：总T1/2=1.9116(16) y；%20O=1.13(22)×10^-11，故b=1.13(22)×10^-13；引用1993Bo20。 | evaluated-decay-data | official-evaluated-object | 228Th Adopted PDF1 ground-state comments | true |
| NCRT-5 | 226Th当前取得的Adopted基态记录仅列alpha，不提供20O分支的正测值；不能据此建立已正测的226Th20O实验基准。 | acquired-dataset-boundary | official-evaluated-object | 226Th Adopted PDF1 | true |
| NCRT-6 | 用T_partial=T_total/b、1 y=365.25 d换算，222Ra/224Ra/226Ra的14C部分半衰期中心为1.120×10^11、7.844×10^15、1.578×10^21 s；228Th的20O为5.339×10^20 s。 | arithmetic-derived-from-evaluation | derived | NCRT1–4; source-keyed Python artifact | true |

## Competing Interpretations and Limitations

`%14C`或`%20O`是百分比；转换为概率必须除以100。总半衰期与罕见通道的部分半衰期不能混用。部分衰变记录与total T1/2评价年代相差较大，未取得完整协方差或原始计数似然；一阶误差传播只能作为标度估计。226Th的18O下限来自 [[warda-2011-actinide-cluster-radioactivity-gogny]] Table I的原实验引用链，不由该NNDC表新造出一个分支。

## Knowledge Impact and Learning Decision

为 [[octupole-cluster-radioactivity-preformation-boundary]] 提供真实实验评价锚点；不从分支比直接测得P0、beta3、beta5或beta7。

## Extracted Pages

- [[octupole-cluster-radioactivity-preformation-boundary]]

## Review Status

Codex source self-audit，所有新claim保留needs_review。
