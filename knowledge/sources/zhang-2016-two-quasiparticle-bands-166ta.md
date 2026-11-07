---
type: "source"
title: "Zhang 2016 - Two-Quasiparticle Bands in Doubly-Odd 166Ta"
aliases: ["Zhang 2016 166Ta", "Zhang 2016 SCPMA"]
created: "2026-11-07"
updated: "2026-11-07"
status: "active"
archive_required: true
review_status: "unreviewed"
source_type: "journal-article"
reading_depth: "read"
title_original: "Investigation of the two-quasiparticle bands in the doubly-odd nucleus 166Ta using a particle-number conserving cranked shell model"
year: 2016
canonical_source: "https://doi.org/10.1007/s11433-016-0088-2"
citation_key: ""
raw_file: "raw/papers/gpt/query/20261107-six-region-transfer/arxiv-1606-00573/source/166Ta.tex"
raw_sha256: "81fb0e20b64b6bfb770636b0c9eef3ae6648103d5c2112d749bcac34f0b09e88"
tags: ["theory-ingest", "rare-earth-region", "a160", "doubly-odd", "axial-symmetry-boundary"]
authors: ["Zhen-Hua Zhang"]
journal: "Science China Physics, Mechanics & Astronomy"
volume: 59
pages: "682012"
doi: "10.1007/s11433-016-0088-2"
arxiv: "1606.00573"
---

# 166Ta的轴对称PNC-CSM：可解释的转动与未检验的三轴自由度

## Bibliographic Record

Z.-H. Zhang，Investigation of the two-quasiparticle bands in the doubly-odd nucleus 166Ta using a particle-number conserving cranked shell model；2016，DOI 10.1007/s11433-016-0088-2。
实际阅读底本为arXiv:1606.00573（未独立确认vN；以实际获取时间和本地哈希固定底本）的166Ta.tex；出版信息由归档metadata记录核对，未将预印稿称为出版排印版。

## Scope and Reading Depth

Worker阅读正文主线；总控定向复核Abstract、§II PNC-CSM formalism、§III输入及组态段落。
本轮没有独立重算CMPC、复现原作者图或对全部EPS图逐点取数。
定位使用实际TeX的section/公式label，替换早期草稿不正确的估计行号。

## Summary

轴对称推转场中用粒子数守恒方法处理配对/阻塞，对166Ta四条两准粒子带的惯量和顺排作解释。
作者沿用并微调Nilsson输入；此文没有通过变化γ来检验三轴稳定性，更不证明整个稀土区无手征。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ZH16-1 | 模型明确从轴对称核的Hamiltonian出发，推转项为−ωJx，并在截断Fock空间对角化配对Hamiltonian。 | model-result | direct | §II，Eq.label eq:H_CSM及其后CMPC段落 | false |
| ZH16-2 | ε2=0.192、ε4=−0.0045取邻近偶偶Hf/W平均；还调整中子μ6及π1/2−[541]位置。 | model-result | direct | §III开头，Fig.1 caption | false |
| ZH16-3 | 质子N=4,5和中子N=5,6壳的CMPC截断；各约1000维，Gp=.34、Gn=.46 MeV为该空间对应有效配对输入。 | model-result | direct | §III Fig.1前的输入段落 | false |
| ZH16-4 | 采用的Band1组态为π9/2−[514]⊗ν1/2+[660]，Band2为π9/2−[514]⊗ν5/2−[523]；Band3/4分别以π5/2+[402]/π1/2+[411]配ν1/2+[660]。 | model-result | direct | §III Fig.2讨论及四组明确列式 | false |
| ZH16-5 | 与实验惯量/顺排比较支持指定组态；未观测GM伙伴的惯量/顺排属于预测。 | author-interpretation | indirect | Abstract、§III Fig.2及GM伙伴讨论 | false |

## Competing Interpretations and Limitations

已假设轴对称的Hamiltonian不提供关于真实核γ稳定性的独立测量；
“本模型没有非共面自由度”不能改写成“真实166Ta或A≈160普通形变态均无手征”。
参数由参考值和谱学信息选择，模型与实验的吻合不是新的独立采集。
ε与β的定义须保持，未作未经原件规定的普适换算。

P0：本地原件和哈希已核对，无未隔离身份问题。P1：配对截断、单粒子输入与实验组态的依赖，以及未纳入三轴自由度的模型边界。

## Extracted Pages

原文TeX的Abstract、§II、§III与总结由worker读取；本轮总控复核上述claim对应段落。
未新增确证核素/带实体，不将该模型作为手征搜索阴性结果。

归档集合的canonical清单：`raw/papers/gpt/query/20261107-six-region-transfer/archive-v1/manifest.json`；父目录初始获取回执原字节保留。
