---
type: "source"
title: "Jehangir et al. 2020 - High-Spin Doublet Band Structures in Odd-Odd 194-200Tl Isotopes"
aliases: ["Jehangir 2020 194-200Tl", "Jehangir 2020 EPJA"]
created: "2026-11-07"
updated: "2026-11-07"
status: "active"
archive_required: true
review_status: "unreviewed"
source_type: "journal-article"
reading_depth: "read"
title_original: "High-Spin Doublet Band Structures in odd-odd 194-200Tl isotopes"
year: 2020
canonical_source: "https://doi.org/10.1140/epja/s10050-020-00206-9"
citation_key: ""
raw_file: "raw/papers/gpt/query/20261107-six-region-transfer/arxiv-2007-12347/source/194_200Tl_v21.tex"
raw_sha256: "8b1cb723cdd74da061061156e81cf4627051c6696f4d22edabbd5e8b27cdbf14"
tags: ["theory-ingest", "nuclear-chirality", "a190", "thallium-isotopes", "four-quasiparticle"]
authors: ["S. Jehangir", "I. Maqbool", "G. H. Bhat", "J. A. Sheikh", "R. Palit", "N. Rather"]
journal: "The European Physical Journal A"
volume: 56
pages: "206"
doi: "10.1140/epja/s10050-020-00206-9"
arxiv: "2007.12347"
---

# 194–200Tl双带的TPSM比较：候选、模型限制与观测缺口

## Bibliographic Record

S. Jehangir et al., High-Spin Doublet Band Structures in odd-odd 194–200Tl isotopes，2020，DOI 10.1140/epja/s10050-020-00206-9。
底本为归档arXiv:2007.12347（未独立确认vN；以实际获取时间和本地哈希固定底本）源码194_200Tl_v21.tex。新下载的是作者源码，未称为期刊出版排印PDF。

## Scope and Reading Depth

Worker读取正文主线；总控复核Abstract、§II Hamiltonian与实际生效的Table label Tab:Tcr、§III电磁比较及手征讨论。
未复现TPSM，没有原作者波函数/完整协方差，也没有把TeX注释中的旧表格行当作现行输入。

## Summary

作者扩展奇奇核TPSM基，包含两准粒子之上的四准粒子结构，比较Tl同位素双带。
194Tl的实验/模型差值支持候选解释，198Tl有模型候选，196/200Tl的失配有模型限制；
原文明确要求进一步研究，不提供全球已确证的手征终止界。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| JE20-1 | 基空间由1p⊗1n扩展到额外两中子或两质子准粒子，描述带交叉后结构。 | model-result | direct | Abstract、§II，Eq.label intrinsic | false |
| JE20-2 | Hamiltonian含单粒子、Q·Q、单极配对与四极配对；BCS给准粒子真空，进行三维角动量投影。 | model-result | direct | §II，Eq.label Hamilt及其前后段落 | false |
| JE20-3 | 现行Table Tab:Tcr对194/196/198/200Tl依次给β=.178/.168/.157/.157、γ=30°/29°/31°/34°。 | model-result | direct | TeX未注释的Table Tab:Tcr；源码物理行375–391 | false |
| JE20-4 | 194Tl带交叉后实验/模型δE趋小；其它同位素的侧带未在交叉后建立，198Tl的手征可能性在该段主要来自模型预测。 | author-interpretation | indirect | §III，figDeltaE讨论，源码物理行765–809 | false |
| JE20-5 | 196/200Tl计算差值远离零，但作者提醒可能是模型伪象；200Tl高自旋B(M1)/B(E2)失配可能与固定平均场有关。 | author-interpretation | direct | §III，fig1m1e2/fig2m1e2及figDeltaE讨论；行670–710、800–809 | false |

表中γ不同于源码被百分号注释掉的旧行35/36/30/33等值；不得混用。
本Hamiltonian没有本文早期生成草稿所称的十六极相互作用或精确粒子数投影。

## Competing Interpretations and Limitations

四准粒子配置/能量吻合和计算的电磁相似性提供模型支持，不是直接测得三维手性。
固定形变是输入；200Tl只有很短侧带，模型失配不能证明N=126附近的实测模式终止。
也不凭β正负或γ≈30°把所有构型强称“扁椭”；轴序、形变和算符约定需从同一来源确认。

P0：原件身份/哈希已核验，早期注释行/输入混用和虚构作用项已纠正。
P1：实验交叉后侧带、伙伴分辨绝对强度与可变平均场仍缺；当前保留模型依赖及反证。

## Extracted Pages

实际读取底本的§II、Table Tab:Tcr、§III和总结见Scope；总控对上述claim逐项回查。
不把模型预测的交叉后198Tl侧带或计算矩阵元记为新观测。

归档集合的canonical清单：`raw/papers/gpt/query/20261107-six-region-transfer/archive-v1/manifest.json`；父目录初始获取回执原字节保留。
