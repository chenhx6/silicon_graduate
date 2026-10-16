---
type: source
title: "Chakraborty：129Ba 365-keV混合比重分析，arXiv v3（2024）"
aliases: [arXiv 2108.05313v3, 129Ba 365 mixing comment]
created: 2026-10-17
updated: 2026-10-17
status: ai-draft
review_status: unreviewed
source_type: preprint-reanalysis
reading_depth: deep-read
title_original: "On the multipole mixing ratio of the 365 keV gamma-transition in 129Ba"
authors: [S. Chakraborty]
year: 2024
arxiv_id: "2108.05313"
data_version: "v3, 9-Apr-2024; initial submission11-Aug-2021"
canonical_source: "https://arxiv.org/abs/2108.05313v3"
citation_key: Chakraborty2024Ba129DeltaV3
citation_key_origin: agent-local-paper-label-pending-reference-manager
raw_file: "raw/papers/gpt/day15-20261016/chakraborty-arxiv2108.05313v3-c8c0accfc9d2.pdf"
raw_sha256: "c8c0accfc9d21e91ebf9ea201287b44047b6e2aca48fc4d1cc765799a160005d"
nuclei: [129ba]
reactions: []
observables: [angular-distribution-coefficient, linear-polarization, multipole-mixing-ratio]
methods: [legacy-data-reanalysis]
tags: [a130, mixing-ratio, source-version, reanalysis, covariance-boundary]
---

# 365keV：一次旧数据重分析，不是新采集

## Bibliographic Record

S. Chakraborty，[arXiv:2108.05313v3](https://arxiv.org/abs/2108.05313v3)，单页comment/reanalysis；原PDF页边明确标**9 Apr 2024**。arXiv metadata给首次提交2021-08-11，v2（2021-08-13）历史标withdrawn，v3日期2024-04-09。本次只读v3，不把早期年份/withdrawal标记自动套到v3内容，也不推断撤回原因。页面未给journal DOI，本Wiki不替它指定PRC DOI。

它与四作者[[chakraborty-2024-possibility-wobbling-129ba]]是两个不同题名/长度的对象，具有相同primary数据和高度重叠的365keV论证；没有由此证明二者是逐字preprint/VoR关系。原文只引J. Gizon等PRC17,596(1978)和127Xe2020工作。

## Scope and Reading Depth

- 单页全文、Fig1的A22/A44曲线、Fig2的平面轨迹/χ²曲线、误差、旧结果与新结果、两条references及页边version均实际阅读和视觉核验。
- 本篇没有提供1977/1978 raw spectra、完整系数修正/取向输入、原polarimeter响应或Cov。Gizon1978 body目前未取得；其题名/作者/DOI已由Crossref/HAL核，不能称primary精读。
- 不以摘要片段为证据；本文主张与计算的证据身份为后续作者重分析，不新增独立实验。

## Summary

v3重新讨论365keV 13/2−→11/2−的旧A22/A44/P，作者由联合系数图/χ²选择δ≈−2.0(2)，报radiative E2约80(4)%。−.84至−.79在本文是历史采用区间，不能当新分析值。原作者曾因angular distribution排除almostpureE2区域的理由受到本篇重新检查；本篇没有发布一套新测量。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| C365-1 | 实读版本为v3/9-Apr-2024、一页；初次2021日期和v2 withdrawal仅是版本史，不等于v3正文年份/撤回原因。 | source-version-identity | direct | p1 margin arXiv2108.05313v3；arXivsubmissionhistory | true |
| C365-2 | 作者引用365keV A22=−.70(.03)、A44=.16(.05)、P=.072(.068)，并回顾旧AD/P/采用区间；这些是旧数据的secondary引述，不是2024新实验。 | quoted-legacy-observables | direct-secondary | p1 leftcolumn openingparagraphs | true |
| C365-3 | 单A22可给约−2.0(.2)/−.33(.03)，A44可给约±1.3(.7)；作者用A22/A44联合图和χ²报δ≈−2.0(.2)、80(4)%E2。 | author-reanalysis-result | direct | p1 Figs1/2 andrightcolumn firstparagraph | true |
| C365-4 | −.84至−.79为历史采用区间；本篇重新检查旧工作“angular distribution排除almostpureE2”的论证，不应把历史值与新作者结果混为同一个采用。 | attribution-boundary | direct | p1 leftcolumn textaboveFig1；rightcolumn | true |
| C365-5 | 用127Xe483keV δ≈−2.1/81%E2作同中子素比较，不是129Ba另一次独立measurement，也不单独建立集体模式。 | cross-nucleus-comparison-boundary | direct-and-self-audit | p1 rightcolumn lasttwoparagraphs；Ref2 | true |
| C365-6 | 本页未列明完整A22/A44取向/finitegeometry修正层、χ²Cov/归一及P响应；未把作者图线改成actualconfidence或将自选reference当其producer。 | reproducibility-boundary | direct-scope-audit | p1 fullmainline/Figs1/2 | true |
| C365-7 | 本篇与CH24的365输入和论证共享Gizon数据；多版本/多图/后续PRC引用不增加该实验的独立样本数。 | evidence-dependence | cross-source-synthesis | p1 Ref1/Figs1/2；CH24printed024324-2/3 | true |

## Competing Interpretations and Limitations

作者的large-E2解须与旧作者的解、原coeff层/phase、alignment和sharedCov区别。[[ba129-365-mixing-reference-boundary]]的明确chosen最大取向参考内部通过F/photon检查却没有复现这些图线；这只说明该reference不能直接代替原analysis输入，不构成对任一作者的代码错误裁决。

两篇现代文本的共享数据不是两个独立支持；scalarP很接近零且其角度/校准定义尚未在primary核定。本次没有给新的experimentalδ/CI/absolute strength或wobbling结论。

## Extracted Pages

- [[ba129-365-mixing-reference-boundary]]：原文归属更正、两类coeff/reference与uncertainty输入合同。
- [[129ba]]及[[chakraborty-2024-possibility-wobbling-129ba]]：只更新数值来源，不升级模式。
