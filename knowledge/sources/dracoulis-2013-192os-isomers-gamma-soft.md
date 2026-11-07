---
type: source
title: "Dracoulis et al. 2013：192Os的异能态、组态依赖形状与γ软性"
aliases: [Isomers and excitation modes in the gamma-soft nucleus 192Os]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Isomers and excitation modes in the gamma-soft nucleus 192Os"
authors: [G. D. Dracoulis, G. J. Lane, A. P. Byrne, H. Watanabe, R. O. Hughes, F. G. Kondev, et al.]
journal: Physics Letters B
year: 2013
volume: 720
pages: 330–335
doi: 10.1016/j.physletb.2013.02.026
language: en
canonical_source: "https://doi.org/10.1016/j.physletb.2013.02.026"
citation_key:
raw_file: raw/papers/gpt/query/20261107-triaxial-isomer-transfer/dracoulis2013-192os.pdf
raw_sha256: 1bf0791250429063541d7ebf241c8e82bf15a4b2705477ef79c2425a2e362412
raw_storage_status: archived-local
archive_required: true
nuclei: [190os, 192os, 194os, 194pt, 196hg]
tags: [isomer, k-mixing, gamma-soft, shape-coexistence, deep-inelastic, a190]
---

# 192Os：寿命、K阻碍与形状必须逐态区分

## Bibliographic Record

G. D. Dracoulis et al., Physics Letters B 720 (2013) 330–335，
DOI 10.1016/j.physletb.2013.02.026；实际使用完整六页出版原件。

## Scope and Reading Depth

完整阅读六页正文、表1、图1–5及结论；表1原页渲染复核。未回放原始符合矩阵，
未独立重算TRS/PES，也未回读所有被引原始实验。前言所引低自旋四极不变量、
190Os既有寿命不是本次新测量。

## Paper Question and Scientific Motivation

过渡区Os具有γ软性，为什么仍有长寿命异能态？作者用高自旋谱学判断
K阻碍、低能跃迁和组态依赖形状各自的作用，而不将“异能态存在”当作轴对称判据
（印刷pp.330–331）。

## Method and Design Logic

ATLAS的136Xe，6.0 MeV/u；脉冲间隔825 ns；186W和192Os厚靶配金背衬，
100台Gammasphere探测器。三重符合、束流时间门和延迟门联合分离通道，
并与角分布、强度平衡/内转换和组态约束PES比较（p.331，Figs.1–4）。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DO13-1 | 表1给192Os的12+、2865-keV态平均寿命τ=2.0(4) ns，20+、4580-keV态τ=295(10) ns。 | experimental-fact | direct | PDF p.2/印刷p.331，Table1；pp.332–333 | false |
| DO13-2 | 192Os的10−、2015-keV异能态沿用既有资料，表1为τ=8.5(14) s；307.0-keV M2的fν=11.2，302.5-keV E3为5.4，47.4-keV E3为7.1。 | experimental-fact | indirect | Table1及p.331、Refs.18–19 | false |
| DO13-3 | 作者明确指出异能态有无及寿命长短本身不能确定K的好坏；长寿命可主要来自高多极性或低跃迁能。 | author-interpretation | direct | pp.330–331、总结pp.334–335 | false |
| DO13-4 | 111.5-keV E2分支9.7(26) W.u.，445.7-keV E2分支4.4(9)×10−2 W.u.；同一母态的不同末态存在很大强度差别。 | experimental-fact | direct | Table1；p.333对12+支路讨论 | false |
| DO13-5 | 新12+/20+结构被解释为扁椭形变下高j顺排；这不是直接测得唯一γ值。 | author-interpretation | indirect | pp.333–334，Figs.3–4 | false |
| DO13-6 | PES对各多准粒子态分别最小化；10−组态在190/192Os偏轴对称长椭，其它组态可偏三轴或扁椭。 | model-result | direct | p.334，Figs.4–5及说明 | false |
| DO13-7 | 194Os低能12+/18+及可能β衰变属于模型预测和后续搜索问题；原文说明现有门条件可能不敏感于某些延迟通道。 | model-result + author-interpretation | direct | pp.334–335，Fig.5 | false |

表中的τ是**平均寿命**，不是半衰期；T1/2=τ ln2。190Os与192Os的
10−长寿命值来自被引既有资料，不能算本实验的新独立复测。

## Summary

高自旋谱学揭示不同顺排结构与长寿命10−带。作者将观察与组态依赖形状、
低能和高多极性衰变共同解释；异能态寿命不单独确定K好坏或静态γ。

## Competing Interpretations and Limitations

原文保留高自旋部分自旋指定的暂定性：部分角分布因去取向近各向同性；
某些E2性质结合平行路径缺失和强度平衡判断。先前668-keV线的192Os放置
在本实验中改归互补产物贡献，提示深非弹性通道不能仅按门中有峰确定核素
（pp.332–333，Fig.2）。

低自旋γ软性、某个高K组态的长椭极小、另一个高自旋态的扁椭顺排可以共存。
论文不支持对整个A≈190区或对192Os全部态赋同一形状。fν不是独立于支路、
算符、组态和能量的“γ测量仪”。

## Knowledge Impact and Learning Decision

`revises`：限制旧综合中“异能态寿命→轴对称”“小fν→唯一三轴性”的反演。
持久化到[[high-spin-isomers-and-decay-modes-systematics]]、
[[universal-triaxial-collective-mechanics-and-cross-region-migration]]、
[[reduced-hindrance-factor]]。与2012Ir论文是邻核比较，不能混为同一核素的复测。

## Agent Self-audit Triage

P0：未发现未隔离的来源身份/哈希问题。P1：τ/T1/2、表1支路强度与fν，
以及PES逐组态最小化均已核对；真实γ分布、未发现预测态的搜索灵敏度及
原始事件级谱仍开放。新假设只进入project，不从本source宣称新核结构发现。

## Extracted Pages

六页出版正文均已阅读；Table1原页复核。新增核素/能带实体未另建，
本轮将证据接入异能态、迁移综合与fν观测量页。
