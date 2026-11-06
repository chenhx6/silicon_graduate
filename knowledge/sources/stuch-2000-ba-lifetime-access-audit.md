---
type: source
title: "Stuch寿命工作：原刊身份、学位论文目录与访问边界"
aliases: [Stuch2000 Ba lifetime source boundary]
created: 2026-11-06
updated: 2026-11-06
status: ai-draft
review_status: unreviewed
source_type: bibliographic-and-access-audit
reading_depth: read
title_original: "Coincidence recoil-distance Doppler-shift lifetime measurements in 129,130Ba with EUROBALL Ge cluster detectors"
authors: [O. Stuch, et al.]
year: 2000
journal: Physical Review C
volume: 61
pages: 044325
doi: 10.1103/PhysRevC.61.044325
canonical_source: https://doi.org/10.1103/PhysRevC.61.044325
citation_key: Stuch2000LifetimeAccessAudit
citation_key_origin: official-NSR-Crossref-DNB-identity
raw_file: raw/papers/gpt/query/20261106-ba129-lifetime-primary-check/manifest.json
raw_sha256: d5527a1047059d9e13b993f072715c9ac91489378dc4b0f4888708baa27a5244
archive_required: true
nuclei: [129ba, 130ba]
methods: [RDDS, DDCM]
tags: [lifetime, access-boundary, bibliography, thesis-locator]
---

# 原刊表格未取得，评价量名保持不变

## Bibliographic Record

官方NSR将2000St07与目标DOI及实验关联。
DNB955612446另登记Oliver Stuch的相关科隆博士论文：
学位年1997、出版年1998，IV+126页。此集合含实际取得物和26份访问回执，
没有原刊全文或论文正文。

## Scope and Reading Depth

读题录、NSR记录和三页论文目录；原刊寿命表、实际门选及误差预算未读。
已有Byrne1992相关分支回到原表核验，不计作Stuch正文。

## Summary

当前资料不能改变ENSDF的半衰期解释。
原刊/学位论文的具体表页已定位，仍需原件核查。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| ST-A1 | DNB955612446标出1997学位、1998出版；目录指寿命汇总p.57、129Ba/125Xe讨论p.83、强度附录p.109。 | bibliographic-location | catalogue-and-original-TOC | 集合DNB SRU及stuch1997-thesis-toc.pdf | true |
| ST-A2 | 1998StZX会议贡献索引只覆盖130Ba，未给全文，不认证129Ba两条寿命。 | source-scope | official-metadata | nndc-stuch-keynumber-records.json | true |
| ST-A3 | 未找到推翻评价量名的原件；129Ba T1/2=6.5(2)、1.0(4)ps继续对应τ=9.38(29)、1.44(58)ps。 | evaluated-data-boundary | existing-evaluation-not-new-primary | 2014reaction ENSDF L143/206；[[nndc-2014-129ba-365-coefficient-records]] | true |

## Competing Interpretations and Limitations

Byrne强度来自86-MeV采集，Stuch RDDS为76MeV；不能借前者的强度平衡
恢复后者的门、距离曲线或侧馈。由假定δ算的CC也不是独立混合测量。
完整路线与核查回执在本轮`lifetime-primary-review/`。

## Extracted Pages

- [[ba129-core-and-pairing-validity]]
- [[ba129-model-input-and-holdout-contract]]
- [[nndc-2014-129ba-365-coefficient-records]]

## Human Review

Codex身份与访问self-audit；未认证原刊寿命提取或human-reviewed。
