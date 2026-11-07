---
type: "source"
title: "Peng and Chen 2019 - Possible Chiral Doublets in 60Ni"
aliases: ["Peng 2019 60Ni chirality", "Peng 2019 PLB"]
created: "2026-11-07"
updated: "2026-11-07"
status: "active"
archive_required: true
review_status: "unreviewed"
source_type: "journal-article"
reading_depth: "read"
title_original: "Possible chiral doublets in 60Ni"
year: 2019
canonical_source: "https://doi.org/10.1016/j.physletb.2019.04.065"
citation_key: ""
raw_file: "raw/papers/gpt/query/20261107-six-region-transfer/arxiv-1904-12100/source/Ni60.tex"
raw_sha256: "835bbcd55b8d3df189955c5e9cf07933896aa5e98871302f5e77d235f6632360"
tags: ["theory-ingest", "nuclear-chirality", "light-mass-region", "a60", "60ni", "four-quasiparticle"]
authors: ["J. Peng", "Q. B. Chen"]
journal: "Physics Letters B"
volume: 793
pages: "303–307"
doi: "10.1016/j.physletb.2019.04.065"
arxiv: "1904.12100"
---

# 60Ni手征双带的四j壳PRM候选

## Bibliographic Record

J. Peng and Q. B. Chen, Possible chiral doublets in 60Ni, Physics Letters B 793 (2019) 303–307，DOI 10.1016/j.physletb.2019.04.065。
实际底本为arXiv:1904.12100（未独立确认vN；以实际获取时间和本地哈希固定底本）的Ni60.tex，作者源码与图已归档；不等同本轮取得实验原始数据或出版排印PDF。

## Scope and Reading Depth

Worker阅读正文主线，总控回查配置/参数、M4观测范围、RMS与方位分布、静态手征表述及限制。
未独立运行PRM，也未回放其引用的Torres2008数据；没有把源码/图像下载或模型图当成手性直接测量。

## Summary

四j壳PRM用跨壳多准粒子组态解释60Ni的M1/M4带，提供A≈60可存在非共面取向的理论候选。
部分参数据谱选择；M4实验仅到I=13ℏ，作者明确要求补充电磁数据以获得更坚实证据。
因此该文反驳区域性对称禁戒推论，却不直接确证真实60Ni已经静态手征。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PC19-1 | 采用π(f7/2)−1(p3/2)1⊗ν(g9/2)1(f5/2)−1四准粒子配置。 | model-result | direct | Ni60.tex物理行231–232，配置段 | false |
| PC19-2 | 先前TAC-CDFT带头β=.27、γ=19°；PRM固定β=.27、γ=22°、J0=9ℏ²/MeV、ξ=.98以较好描述谱。 | model-result | direct | 行233–243，模型输入段 | false |
| PC19-3 | 对能量和部分电磁数据作比较；实验M4只达到I=13ℏ，更高自旋的M4结果属于预测。 | author-interpretation | direct | 行256–300，Fig.1及电磁比较讨论 | false |
| PC19-4 | 计算中高j粒子/空穴与核芯偏向不同主轴；方位分布在指定自旋出现非共面峰，作者解释为振动—静态手征—再振动演化。 | model-result + author-interpretation | indirect | 行304–413，RMS图与azimuthal图/相关讨论 | false |

## Competing Interpretations and Limitations

γ和惯量等与谱有关，固定形变未包含先前TAC-CDFT的随旋转β变化；
作者指出部分高自旋B(M1)/B(E2)再现存在差异。由模型取向图讨论的静态手征不是独立实验事实。
能量近简并本身不识别所有竞争解释，M4寿命/连接和更高自旋范围仍有价值。

P0：身份和SHA已核对，模型与实验范围区分。P1：配置/参数依赖、M4电磁证据及跨壳驱动的真实可迁移范围。

## Extracted Pages

底本Ni60.tex的主线由worker读取；总控本轮重点复核行231–300、304–413与实际引用的图/讨论。
原实验引用未另取得完整新原件，不将理论文和其复用数据算作两份独立实验。

归档集合的canonical清单：`raw/papers/gpt/query/20261107-six-region-transfer/archive-v1/manifest.json`；父目录初始获取回执原字节保留。
