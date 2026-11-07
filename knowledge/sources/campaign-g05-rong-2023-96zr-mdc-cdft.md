---
type: source
title: "Rong et al. 2023: 96Zr八极关联与对称性恢复MDC-CDFT微观分析（PLB）"
aliases: ["Rong 2023 PLB 96Zr octupole", "arXiv:2201.02114", "PLB 840 137896"]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Anatomy of octupole correlations in 96Zr with a symmetry-restored multidimensionally-constrained covariant density functional theory"
authors: ["Yu-Ting Rong", "Xian-Ye Wu", "Bing-Nan Lu", "Jiang-Ming Yao"]
journal: Physics Letters B
year: 2023
volume: 840
pages: 137896
doi: 10.1016/j.physletb.2023.137896
arxiv: "2201.02114"
canonical_source: "https://doi.org/10.1016/j.physletb.2023.137896"
citation_key: ""
raw_file: raw/papers/gpt/query/20261107-campaign-G05/arxiv-2201.02114.pdf
raw_sha256: 8efe9c1878d87afa98726c9af2441381bc8afd5b7cc6718bb27f0eda394ba685
raw_storage_status: fully-archived-local
archive_required: true
nuclei: ["96zr"]
tags: ["octupole-correlation", "symmetry-restoration", "cdft", "mdc-rhb", "a100", "n56"]
---

# Rong等：96Zr八极关联、投影势面与形状混合边界

## Bibliographic Record

Y.-T. Rong, X.-Y. Wu, B.-N. Lu, J.-M. Yao，PLB840,137896(2023)，
DOI10.1016/j.physletb.2023.137896。本地实际底本arXiv:2201.02114v2，10物理页。
题名与SHA见元数据；不能把作者预印本称作已逐字对照的出版版。

## Scope and Reading Depth

### Covered scope

正文主线与Figs1–4/Table1；总控回查PDF4–7，Terra与G11核对投影方案/表行。
文献列表与参考原文独立，不能说已逐篇读完被引论文。

### Not covered

未运行RHB/角动量宇称投影生产程序，也未恢复全部输入与Cov。
原文尚未包含完整GCM形状混合；不能把其投影最低点称作已计算的完整GCM波函数。

## Key Results

| ID | 实际模型内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| R23-1 | 一维β30/β32的指定平均场切线在球形处最低，投影0+后出现非零极小；不能从这些切线推出所有方案的全局平均场极小全为零 | model-result | direct | PDF4 Fig1(c,d)及正文 | false |
| R23-2 | 四极面很软；名义对力有β20=.21与−.19的两个极小，调整对力可移动最低点。另有投影三轴分支 | model-result | direct | PDF4 Fig1(a,b)；PDF5 Table1(a) | false |
| R23-3 | 轴向反射不对称方案Table1(b)：0+极小(β20,β30)=(.01,.23)；3−为(.03,.24)、Ex=4.90MeV；1−为(.21,.22)、Ex=7.09MeV | model-result | direct | PDF5 Table1；PDF6 | false |
| R23-4 | 同列(.22,.12;4.65MeV)属于2+，(.25,.11;5.94MeV)属于4+；旧草案错配成3−与1−，已纠正 | model-result | direct | PDF5 Table1(b) | false |
| R23-5 | 固定0+的内禀形变(.01,.23)，以同一形变投影态计算B(E3;3−→0+)=20.68×10³ e²fm⁶；作者对比所引Iskra2019的23(2)×10³ | model-result + secondary-experiment-report | direct-model + indirect-experiment | PDF6 | false |
| R23-6 | Fig4以质子p3/2–g9/2、中子d5/2–h11/2附近轨道讨论微观八极驱动 | model-result | direct | PDF7 Fig4及正文 | false |

## Summary

该文的增量是多种对称性约束与投影下PES/能谱的具体比较。
投影极小、平均场坐标、实验室八极期望与完整形状混合波函数是不同对象。
不能把β30=.23称为直接实测rms振幅，亦不能由此排他裁决静态/动态。

## Competing Interpretations and Limitations

Table1各列的对称性、配对及粒子数恢复实现不同，须带列比较，不能当独立实验。
论文采用PAV；投影能谱与实测仍有差异，作者认为进一步形状混合重要。
某个B(E3)接近所引数据不表示能谱或全部矩阵元均已拟合成功。
PDF6说明E3计算忽略初末态形状随自旋的移动，不能略去这一近似。
RHIC形变参数的比较是模型相关，不能仅因数值接近称已验证碰撞反演机制。

## Knowledge Impact and Learning Decision

`revises + provisional research-note`：[[campaign-g05-a100-softness-octupole-20261107]]。
新的可追查缺口是Iskra2019修订E3原实验，不把Rong的转引写成已读实验结果。

## Agent Self-audit Triage

P0: none identified in registered original identity。
P1：总控/Terra/G11纠正10页身份、Table1行/列串读，撤回所有平均场严格零、
本工作已含GCM、实验量与投影坐标等同及无来源势垒判据。

## Extracted Pages

本地作者v2共10页；重点原件定位PDF4–7，原字节未改变。
