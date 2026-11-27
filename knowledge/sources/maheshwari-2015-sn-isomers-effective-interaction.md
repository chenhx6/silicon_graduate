---
type: source
title: "Maheshwari等2015：Sn异能态与RCDB有效相互作用"
aliases: [Maheshwari Jain Srivastava 2015 Sn, arXiv1502.02859]
created: 2026-11-07
updated: 2026-11-27
status: active
review_status: unreviewed
source_type: theory-article
reading_depth: read
title_original: "6+ isomers in neutron-rich Sn-isotopes beyond N=82 and effective interaction"
authors: [Bhoomika Maheshwari, Ashok Kumar Jain, P. C. Srivastava]
journal: Physical Review C
year: 2015
volume: 91
pages: 024321
doi: 10.1103/PhysRevC.91.024321
arxiv: 1502.02859v1
canonical_source: "doi:10.1103/PhysRevC.91.024321"
citation_key:
raw_file: raw/papers/gpt/query/20261107-round2-sn136-seniority/maheshwari-2015-6-isomers-sn-effective-interaction.pdf
raw_sha256: 9265e5f2542c1959831a17597d7cbfceccbc2a06a5bf58fd2ccd2ded5b4f6049
archive_required: true
nuclei: [134sn, 136sn, 138sn]
tags: [seniority, effective-interaction, configuration-mixing, neutron-rich]
---

# RCDB与136Sn的seniority混合

## Bibliographic Record

B. Maheshwari, A. K. Jain, P. C. Srivastava, PRC91,024321(2015)。
本地实际读取底本为arXiv:1502.02859v1、5物理页；未把作者稿等同逐字核对后的出版版。

## Scope and Reading Depth

读取摘要、模型空间、Figs.1–4及结论，Fig.1已渲染核对；未运行NuShell。
原实验取自Simpson及被引其它论文，不是本篇新测量。

## Key Results

| ID | 模型及数据内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MJ15-1 | 132Sn核芯外用六条中子轨道2f7/2、3p3/2、1h9/2、3p1/2、2f5/2、1i13/2，采用eν=0.65e。 | model-input | direct | PDF p.2, Calculations | false |
| MJ15-2 | RCDB到RCDBMO将指定νf7/2²对角与非对角TBME减少25keV，136Sn的6+→4+₁从14.5增为22.0e²fm⁴，对比实验24(4)。 | model-result + experimental-reference | direct | PDF pp.2–3, Fig.1 | false |
| MJ15-3 | 同时6+→4+₂从53.1变为46.4，4+₁→2+₁从28.0变为95.3e²fm⁴，提示联合分支可比单值提供更多约束。 | model-result | direct | PDF pp.3–4, Fig.1 | false |
| MJ15-4 | Fig.1中136Sn的RCDB能量为6+=1373、4+₂=1331keV；RCDBMO为1353、1290keV。差为42、63keV，均属计算而非已测新旁路。 | model-result | direct figure | PDF p.2, Fig.1 | false |

## Summary

这篇多轨道有效两体计算提供强度的竞争解释；与一个B(E2)相容不等于所有观测已被唯一解释。
不把25keV经验修改直接叫作显式价空间三体矩阵元。

## Competing Interpretations and Limitations

真实核的单j近似不精确，跨轨道组态与有效算符可以改变中壳节点。
作者的模型比较不认证“三体力不存在”；也不证明任意基本三核力都已被正规序两体项替代。
Fig.1最左134Sn的6+计算能量1255/1264keV不能误放成136Sn的4+₂能量。

## Extracted Pages

5页预印本。特别核查p.2 Fig.1及pp.3–4的B值/能级变化；
实际核的大空间对角化与协方差未重放。

## 2026-11-27 — 馆藏原件与覆盖核对

- 物理第1–2页，题头、摘要、I引言、II计算和III结果开头，含图1能级与B(E2)图注。
- 物理第3–4页，III结果与讨论，含物理第3页图2及ESPE式(1)–(2)，物理第4页图3跃迁强度和图4轨道占据。
- 物理第5页，IV结论、致谢及参考文献1–17。
- 本次获取的具体覆盖：已审读物理第1–5页抽取文本，包括模型输入、图1–4图注及可辨数值、式(1)–(2)及其说明、结论和参考文献。建议接受既有同版v1的五页文字覆盖。图中列归属及期刊版覆盖须分别按相应原页核验。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A18-1 | NuShell计算以¹³²Sn为惰性核芯，价中子空间含2f₇/₂、3p₃/₂、1h₉/₂、3p₁/₂、2f₅/₂和1i₁₃/₂六条轨道，有效中子电荷取0.65e。RCDBMO把作者指定的νf₇/₂²相关对角和非对角两体矩阵元各降低25 keV。 | 本文模型输入 | source-reported | 物理第1–2页II Calculations，物理第3页III开头重述。 | true |
| A18-2 | 本文用于比较的¹³⁶Sn和¹³⁸Sn的B(E2; 6⁺→4₁⁺)实验值分别为24(4)和16(4) e²fm⁴，均引自Simpson等。 | 外引实验观测 | source-reported | 物理第3页¹³⁶Sn数值段、物理第4页¹³⁸Sn数值段，图1、图3及参考文献2。 | true |
| A18-3 | ¹³⁶Sn由RCDB改为RCDBMO后，B(E2; 6⁺→4₁⁺)从14.5升至22.0，B(E2; 6⁺→4₂⁺)从53.1降至46.4，B(E2; 4₁⁺→2₁⁺)从28.0升至95.3，单位均为e²fm⁴。图1的6⁺与4₂⁺计算能量在RCDB下为1373与1331 keV，在RCDBMO下为1353与1290 keV，相差42和63 keV。能量列归属待核物理第2页。 | 本文模型结果 | source-reported | 物理第2页图1中央¹³⁶Sn分组，物理第3–4页数值讨论。 | true |
| A18-4 | 作者将¹³⁶Sn的非零中壳E2强度和修改后的分支变化归因于两个4⁺态之间的v = 2与v = 4混合，并认为¹³⁴Sn和¹³⁸Sn的相关yrast态更接近纯v = 2。图4给出所比较轨道的计算占据，具体图线归属待核物理第4页。 | 作者的seniority混合解释 | source-reported | 物理第3页中壳选择规则与强度讨论，物理第4页图4及相邻文字，物理第5页结论。 | true |

本件为壳模型计算。图1的¹³⁴Sn实验数据引自参考文献4–6，¹³⁶,¹³⁸Sn引自Simpson等的参考文献2。图3误差棒和数据的图注单列参考文献2、4。参考文献2也提供经约150 keV调整的另一有效相互作用计算作为比较。

- 书目同时保留arXiv v1底本、边栏2015年日期及题头2021年日期差异，期刊文章号024321单列。当前阅读页数记为v1的5个物理页。
- 保留图1既有列归属订正。1255和1264 keV归入¹³⁴Sn的两个6⁺计算列，¹³⁶Sn的4₂⁺计算值归入中央分组的1331和1290 keV。
- 物理第3页式(1)–(2)的抽取中轨道下标重复，转录求和指标、可能的撇号及矩阵元括号前查原页。物理第2页振子参数的ℏ字形抽取为~，引用公式前核字。
