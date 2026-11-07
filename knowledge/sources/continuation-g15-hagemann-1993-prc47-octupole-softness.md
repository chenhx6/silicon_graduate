---
type: source
title: "Hagemann等1993：奇A稀土核E1跃迁与八极软度系统学及微观模型（PRC全文11页）"
aliases: ["Hagemann 1993 PRC octupole softness", "Phys. Rev. C 47 2008", "10.1103/PhysRevC.47.2008"]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: read
title_original: "Electric-dipole transitions and octupole softness in odd-A rare-earth nuclei"
authors: ["G. B. Hagemann", "I. Hamamoto", "W. Satuła"]
journal: Physical Review C
year: 1993
volume: 47
pages: 2008-2018
doi: 10.1103/PhysRevC.47.2008
canonical_source: "https://doi.org/10.1103/PhysRevC.47.2008"
citation_key:
raw_file: raw/papers/gpt/query/20261107-continuation-G15/Hagemann-1993-PRC-47-2008.pdf
raw_sha256: cc286cb71fc568db818ff926cfce70e9842af79a1438f9eccd10f4536bb60cb4
raw_storage_status: fully-archived-local
archive_required: true
nuclei: ["157ho", "165tm", "167tm", "169lu", "171lu", "173lu", "163er", "163yb", "165yb", "167yb", "177hf"]
models: ["particle-rotor-model", "nilsson-potential", "rpa-microscopic-octupole", "pauli-blocking", "quasiparticle-vibration"]
observables: ["B(E1)", "effective-charge", "b0-b1-parameters", "2qp-blocking-deltab"]
tags: ["e1-transitions", "octupole-softness", "rpa", "pauli-blocking", "effective-e1-operator", "rare-earth", "fulltext-read"]
---

# Hagemann1993：稀土E1的经验极化与微观估计

## Bibliographic Record

G.B.Hagemann、I.Hamamoto、W.Satuła，PRC47,2008–2018(1993)，
DOI10.1103/PhysRevC.47.2008。实际11页出版PDF已归档，前言延续1989模型工作。

## Scope and Reading Depth

G15提取全文/表；Terra独立回读pp2011–2013的算符、模式求和和局限，
核图pp2017 Eq8；总控复核对应关键段。未重现作者RPA/PRM生产计算或全部实验来源。

## Key Results

| ID | 实际内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HG93-1 | 文章比较稀土奇A核的E1，用有效参数表征所采用模型中的八极软度贡献 | model-comparison | direct | p2008摘要及正文 | false |
| HG93-2 | 内禀E1为eeff rY1ν + e bν r³Y3ν，并给bν的RPA模矩阵元/能量求和表达 | author-derivation | direct | p2011 Eqs4–5 | false |
| HG93-3 | 绝对b的微观估计受质心、IS/IV及质中子径向分布等影响，作者未获得全部定量一致 | author-interpretation | direct | p2013及p2018结论 | false |
| HG93-4 | Eq8的两耦合量约为−4.8×10^-5与+1.58×10^-5 MeV fm^-6 | model-input | direct | p2017 Eq8，Terra核图 | false |
| HG93-5 | 文章讨论较早程序修正及重新调整的参数；版本与参数不能混用 | methodological-history | direct | p2012 TableIII及p2013 Fig7邻文 | false |

## Model and Parameter Boundary

bν的模式求和包含能量、八极矩阵元及偶极响应；它不是仅由β2、β3或一个CG系数给定。
本文的微观相消/阻塞示例不能证明所有核和所有方法都无法估计绝对极化。
本文旧记号的耦合定义也不能擅换成2026的κsc或认为只差通用常数。
负/正κ的物理解释须保留作者势和张量归一，而不是只凭符号口称吸引/排斥。

## Transfer and Competing Explanations

强E1的解释必须同时检查配对、Coriolis、单粒子空间、有效电荷及波函数。
原文对低能稀土跃迁使用的静态极化假设，只给102Ru问题一个需要检验的来源，
不能仅凭5MeV相对最低3−能量，就判定2026参数化不合法。
轴向K破缺后可能产生混合，其强弱与剩余对称性依赖实际模型；不是所有K分量必显著。
相关推导和修订见[[continuation-t02-ru102-covariant-effective-e1-20261107]]。

## Agent Self-audit Triage

G15草案曾把p2017 Eq8两数误写为10^-3，本轮独立核图纠正为10^-5，原PDF不变。
同时撤回共同拟合必强共线、旋转D1与单一[Q2⊗O3]1普遍等价等推断。
未验证的书目key留空，不创建假BibTeX身份。


## Summary

本页记录该原件实际提供的实验/模型信息与读取边界；核心数据/公式沿用上文原表locator，不作为新实验或作者代码复现。


## Competing Interpretations and Limitations

模型参数和解释不等于实验直接测量；原文未报告不等于严格为零或全球不存在。局部比较不能排除全部模型族，适用条件与缺失响应沿用本页记录。


## Extracted Pages

实际读取的PDF/出版页、XML原文段及表号见Scope和逐项locator；全文文件可用不代表全部图点/转引原件或生产实现已核。
