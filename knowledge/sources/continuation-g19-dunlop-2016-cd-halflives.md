---
type: source
title: "Half-lives of neutron-rich Cd128–130"
aliases: [Dunlop2016, Dunlop 2016 PRC, 128-130Cd half-lives GRIFFIN]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Half-lives of neutron-rich Cd128–130"
authors: [R. Dunlop, V. Bildstein, I. Dillmann, A. Jungclaus, C. E. Svensson, C. Andreoiu, G. C. Ball, N. Bernier, H. Bidaman, P. Boubel, C. Burbadge, R. Caballero-Folch, M. R. Dunlop, L. J. Evitts, F. Garcia, A. B. Garnsworthy, P. E. Garrett, G. Hackman, S. Hallam, J. Henderson, S. Ilyushkin, D. Kisliuk, R. Krücken, J. Lassen, R. Li, E. MacConnachie, A. D. MacLean, E. McGee, M. Moukaddam, B. Olaizola, E. Padilla-Rodal, J. Park, O. Paetkau, C. M. Petrache, J. L. Pore, A. J. Radich, P. Ruotsalainen, J. Smallcombe, J. K. Smith, S. L. Tabor, A. Teigelhöfer, J. Turko, T. Zidar]
journal: "Physical Review C"
year: 2016
volume: 93
pages: "062801(R)"
doi: "10.1103/PhysRevC.93.062801"
language: en
canonical_source: "doi:10.1103/PhysRevC.93.062801"
citation_key:
raw_file: "raw/papers/gpt/query/20261107-continuation-G19/Dunlop_2016_PRC_93_062801_128-130Cd_halflives.pdf"
raw_sha256: cee8422b6079264ff7e541a0bc8d6882798d54a4a2861d4388200cf74ca4405c
archive_required: true
nuclei: [128cd, 129cd, 130cd, 132sn]
reactions: [480mev-proton-induced-fission-ucx]
experiments: [triumf-isac-griffin-sceptar]
models: [df3-cqrpa, rhb-rqrpa, shell-model]
observables: [beta-decay-half-life, r-process-waiting-point, gamow-teller-quenching]
methods: [beta-delayed-gamma-timing, hpge-clover-spectrometry, isomer-separation]
tags: [cadmium-isotopes, isomer-half-lives, r-process-waiting-point, gt-quenching, 129cd, 130cd, griffin-spectrometer]
---

# Dunlop2016：GRIFFIN测定128-130Cd半衰期与GT淬灭因子标定

## Bibliographic Record

R. Dunlop et al., Physical Review C 93, 062801(R) (2016)，DOI: 10.1103/PhysRevC.93.062801。
实际本地原件：arXiv:1711.05621v1，6物理页，SHA-256: `cee8422b6079264ff7e541a0bc8d6882798d54a4a2861d4388200cf74ca4405c`。

## Scope and Reading Depth

### Covered scope

通读6页全文：
1. 实验测定：利用TRIUMF-ISAC高纯锗阵列GRIFFIN精确测定中子富集镉同位素半衰期：
   - $^{128}\text{Cd}$：$T_{1/2} = 246.2(21)\,\text{ms}$
   - $^{129}\text{Cd}(11/2^-)$：$T_{1/2} = 147(3)\,\text{ms}$（剔除 $995\,\text{keV}$ 交叉馈送与 $1354\,\text{keV}$ 女儿污染）
   - $^{129}\text{Cd}(3/2^+)$：$T_{1/2} = 157(8)\,\text{ms}$（与Taprogge 2015的 $146(8)\,\text{ms}$ 一致，加权均值 $151.5(57)\,\text{ms}$）
   - $^{130}\text{Cd}(0^+)$：$T_{1/2} = 126(4)\,\text{ms}$（确证Lorusso 2015 EURICA值 $127(2)\,\text{ms}$，否定历史长寿命 $162(7)\,\text{ms}$）
2. 唯象淬灭标定机制：
   - 文献中 $q=0.66 \to 0.75$ 的标度调节（第4页右栏及引文[9,10,12]）具体针对大尺度壳模型（LSSM, Zhi 2013, Cuenca-Garcia 2007, Lorusso 2015）对 $N=82$ 等待点核的计算；早期为拟合 $^{130}\text{Cd}$ 旧长寿命（$162(7)\,\text{ms}$）取 $q=0.66$，确认 $126(4)\,\text{ms}$ 后在壳模型中上调至 $q=0.75$；
   - 全局微观模型 DF3+CQRPA（Borzov 2008）与 RHB+RQRPA（Marketin 2016）在 Fig. 7 中作为对比，略微系统性高估绝对寿命，但未在本文中实施 $q=0.66 \to 0.75$ 的针对性重调，不能将该壳模型经验拟合套用于所有泛函/QRPA 模型；
   - 这一调整表明文献中的 $q=0.75$ 是针对特定等待点核寿命反演拟合的经验参数，不能当作独立测定的普适第一性物理常数。

### Not covered

不包含 $^{129}\text{Cd}$ 逐能级分支比的完整纲图推导（由后续Saito 2020文章详述）。

## Key Findings and Data

1. **澄清历史分歧**：
   本次GRIFFIN结果与Arndt等早期ISOLDE报告的两倍寿命差异不相容（历史报告 $11/2^-$ 为 $104(6)\,\text{ms}$、$3/2^+$ 为 $242(8)\,\text{ms}$），本次两个母态的半衰期接近（$147(3)\,\text{ms}$ vs $157(8)\,\text{ms}$）。
2. **$q=0.75$ 的唯象起源**：
   $q=0.75$ 在天体r-process等待点模型中作为唯象输入，用来缩短计算寿命；若直接把 $q=0.75$ 当作从原子核微观弱相互作用基本第一性原理测定的通用常数，属于物理循环论证。



## Parent version and scope audit

实际读取版本为arXiv1711.05621v1，发表身份为PRC93,062801(R)(2016)。
总控回读实际PDF5：q=.66→.75讨论LSSM对130Cd较短寿命的标定，
不能归给同页Fig7比较的DF3/RHB；新结果不是独立普适gA测量。


## Summary

本页记录该原件实际提供的实验/模型信息与读取边界；核心数据/公式沿用上文原表locator，不作为新实验或作者代码复现。


## Competing Interpretations and Limitations

模型参数和解释不等于实验直接测量；原文未报告不等于严格为零或全球不存在。局部比较不能排除全部模型族，适用条件与缺失响应沿用本页记录。


## Extracted Pages

实际读取的PDF/出版页、XML原文段及表号见Scope和逐项locator；全文文件可用不代表全部图点/转引原件或生产实现已核。


## Key Results

| ID | 内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DU16-1 | 129Cd两母态半衰期147(3)、157(8)ms | experimental-fact | direct | arXiv1711.05621v1 PDF4 TableI | false |
| DU16-2 | q=.66→.75讨论LSSM对130Cd较短寿命的标定 | model-calibration | direct | 同版本PDF5讨论；不归给DF3/RHB | false |
