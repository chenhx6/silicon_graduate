---
type: source
title: "Wang等2020：131Ba多手征双重带的赝自旋对称性与八极关联RAT-PRM模型（PRC全文6页）"
aliases: ["Wang 2020 PRC 131Ba RAT-PRM", "Phys. Rev. C 102 024313", "10.1103/PhysRevC.102.024313", "arXiv:2008.02414"]
created: 2026-11-07
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: read
title_original: "Pseudospin symmetry and octupole correlations for multiple chiral doublets in 131Ba"
authors: ["Y. P. Wang", "Y. Y. Wang", "J. Meng"]
journal: Physical Review C
year: 2020
volume: 102
pages: 024313
doi: 10.1103/PhysRevC.102.024313
canonical_source: "https://doi.org/10.1103/PhysRevC.102.024313"
citation_key:
raw_file: raw/papers/gpt/query/20261107-continuation-G21/Wang-2020-PRC-102-024313-131Ba.pdf
raw_sha256: 5aca0762a20dd6683d2547c9a7c2266d8cbf6b40fb8a01c431a2b4c78aa65247
raw_storage_status: fully-archived-local
archive_required: true
learning_candidate: true
learning_topic: chiral-octupole-correlation-a130-transfer
nuclei: ["131ba"]
models: ["rat-prm", "reflection-asymmetric-triaxial-rotor", "cdft-pc-pk1", "pseudospin-symmetry", "azimuthal-plots"]
observables: ["energy-spectra", "S(I)", "B(M1)/B(E2)", "B(E1)/B(E2)", "azimuthal-angles-theta-phi"]
tags: ["131ba", "pseudospin-chiral-quartet", "octupole-correlations", "rat-prm", "cdft", "mchid", "a130", "fulltext-read"]
---

# Wang2020：131Ba的RAT-PRM与赝自旋/手征关联

## Bibliographic Record

Y.P.Wang、Y.Y.Wang、J.Meng，PRC102,024313(2020)，DOI10.1103/PhysRevC.102.024313。
实际6页出版PDF及哈希见元数据。

## Scope and Reading Depth

G21读取全文模型/图表；总控回读PDF2 Eqs2–8和Numerical Details。
未重放波函数/代码、数字化全部图点或读取其全部转引实验。

## Summary

这是一篇三准粒子反射不对称三轴粒子—转子模型论文，
对131Ba既有候选带作理论比较，不是本次新寿命/绝对强度测量。

## Key Results

| ID | 实际内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WA20-1 | 核芯Hamiltonian含转动和宇称劈裂项，使用好宇称/角动量对称化基底 | model-derivation | direct | PDF2 Eqs2–8 | false |
| WA20-2 | β2=.22、γ27.1°采自指定CDFT，β3=.02为本RAT-PRM选用值 | model-input | direct | PDF2 Numerical Details | false |
| WA20-3 | J0=19ℏ²/MeV、E(0−)=2.1MeV按谱调整；Δ采用12/√A经验式 | model-input | direct | PDF2 Numerical Details | false |
| WA20-4 | 比较D3–D8能谱、相对电磁数据及方位角分布 | model-comparison | direct | PDF3–5 Figs2–8 | false |
| WA20-5 | 赝自旋伙伴及非共面取向是所用模型中的解释/概率图，非直接几何或静态形变测量 | model-interpretation | direct | PDF4–5讨论 | false |

## Competing Interpretations and Limitations

该论文讨论的候选高自旋网络未由本文新增绝对寿命；不能说整个131Ba核素无寿命。
β3、E(0−)和占据是模型输入，不证明唯一参数或静态八极存在/不存在。
正负宇称名义组态不同也不构成一般宇称投影伙伴的数学禁戒。
原实验设备/事件数如只转引，不作为本篇已独立核实。

## Extracted Pages

出版PDF1–6已可读；总控重点PDF2，G21其余模型读取范围见记录；作者生产实现未重现。
