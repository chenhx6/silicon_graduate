---
type: source
title: "Afanasjev & Abusara 2010：转动核的时间奇场与核磁性"
aliases: [Afanasjev Abusara 2010 nuclear magnetism, rotating time-odd CDFT]
created: 2026-11-08
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: journal-article-theory
reading_depth: skimmed
title_original: "Time-odd mean fields in covariant density functional theory: Rotating systems"
authors: [A. V. Afanasjev, H. Abusara]
journal: Physical Review C
year: 2010
volume: "82"
pages: "034329"
doi: 10.1103/PhysRevC.82.034329
arxiv: 1010.1801v1
language: en
canonical_source: https://doi.org/10.1103/PhysRevC.82.034329
citation_key: ""
raw_file: raw/papers/gpt/query/20261108-r2-g40-time-odd-rotation/afanasjev-2010-time-odd-cdft-rotating-prc82-034329.pdf
raw_sha256: 4a15adacc5f8101bdf0eb2370aed191138217f64fde5c142b26e5eb0823e5b51
raw_storage_status: archived-local
archive_required: true
nuclei: [194pb, 152dy]
reactions: []
experiments: []
models: [cranked-relativistic-mean-field, cranked-relativistic-hartree-bogoliubov]
observables: [moments-of-inertia, alignment, band-crossing, intrinsic-current]
methods: [self-consistent-cranking, nuclear-magnetism-switch]
tags: [doctoral-foundations, time-odd-fields, nuclear-magnetism, high-spin]
---

# 自洽电流改变转动响应，但“核磁性”不是一个实测 M1 数字

## Bibliographic Record

实际底本 `1010.1801v1` 为 **22 个物理页**，页边为 2010-10-09，
内部 Dated 2018-11-09 不据此另立 2018 年研究。
DOI 题名核对遇一次 Crossref 429，保留实际响应并作有界重试。
同目录另有 Afanasjev–Ring 2000 的伴随原件；不因其被下载就计为本页独立证据。

## Scope and Reading Depth

- Completed reading_depth: skimmed，选段理论/机制阅读。
- Covered scope: pp. 1–5 的理论设置、NM/WNM 定义和带交叉；
  pp. 6–9 的惯量与刚体/电流比较；总结、相关 Figs. 1–8。
- Not covered: 全部高自旋组态、终止/旋称分离图的逐项核验、
  原程序重放、所有参数组数值，以及 2000 伴随作的全部推导。

## Paper Question and Scientific Motivation

在指定 CDFT 介子耦合参数化中研究时间奇场对转动观测量的影响。
大多数计算采用忽略配对的 CRMF，以便分离部分效应；
少数带交叉例子用 CRHB、Gogny D1S 配对和 LN。
这些计算的适用条件不能合并成一个通用于低自旋软核的结论。

## Method and Design Logic

NM 与 WNM 对同一核组态分别自洽求解；WNM 关闭空间矢量介子场及相应耦合，
但保留 Coriolis 项。因此 WNM 中仍可有 Coriolis 诱导电流。
NM−WNM 是指定理论干预的差，包含由干预造成的自洽重排，
不是独立实验测得的纯场贡献。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AA10-1 | Coriolis 项和磁矢量势是不同来源；不能把 WNM 说成完全没有转动电流。 | model-result | direct | pp. 2–4, Eqs. (2)–(20) 及方案定义 | false |
| AA10-2 | 本文百分比定义为 \((O_{\rm NM}-O_{\rm WNM})/O_{\rm NM}\times100\%\)，分母不是 WNM。 | model-result | direct | p. 4, Eq. (18) | false |
| AA10-3 | 在指定未配对 194Pb SD 组态中，计算交叉频率由 WNM 的 0.465 降到 NM 的 0.345 MeV；不是实测频率变化。 | model-result | direct | pp. 4–5, Fig. 1 及正文 | false |
| AA10-4 | 含配对的 194Pb 示例中，中子交叉另为 0.485→0.415 MeV；它与未配对质子单粒子交叉不是同一个数字或同一种比较。 | model-result | direct | p. 5, Fig. 2 及正文 | false |
| AA10-5 | SD/HD 指定计算的惯量可接近刚体参考值，但其内禀电流仍有非刚体分布；标量惯量接近不能识别完整流场。 | model-result | direct | pp. 8–9, Figs. 6–8 及 Sec. V | false |

## Summary

时间奇响应可以改变单粒子顺排、交叉和沿带惯量；其效应依组态与频率而变。
“相同质量区”“接近刚体惯量”和“相同内禀流场”是三个不同判断。
本来源给出的是指定平均场模型的计算与已发表实验的比较，没有直接测量核内电流。

## Competing Interpretations and Limitations

Lorentz 约束联系同一矢量通道的时间/空间耦合，不表示 σ、ω、ρ 的耦合常数
全都相同。本文范围以非线性 σ 自耦合参数组为主，不代表所有现代 CDFT 泛函。
电流图也不是流场拓扑不变量或 M1 矩阵元的直接测量。
用带交叉约束时间奇场，还须同时处理配对、组态、形变和态跟踪。
禁止把 Eq. (18) 的贡献份额直接叫作相对 WNM 的同数值增长率。

## Knowledge Impact and Learning Decision

methodological-bridge：[[doctoral-r2-collective-inertia-response-crosswalk-20261108]]；
limits：配对消失必然产生理想刚体流、一个固定增强系数适用于所有组态的设想。
没有重新宣称某个绝对 M1/δ 数字已经唯一判定了时间奇耦合。

## Agent Self-audit Triage

P0：核查了模型干预、百分比分母、配对/未配对交叉的不同身份及 22 页底本。
P1：参数组、频率、组态和刚体参照的限制保留；其余未逐图核验的初稿数字不进入本页。
P2/P3：空 citation key 保留；原件和源码留本地，未运行外来程序。

## Extracted Pages

- 可复用方法与比较合同：[[doctoral-r2-collective-inertia-response-crosswalk-20261108]]。
- 具体案例、真实表与边界：[[doctoral-r2-inertia-evidence-and-band-reconstruction-20261108]]。
- 当前不另建能带或实验页；本来源中的实核数值与模型条件按上文保留，
  不将理论参数登记成新的测量。
