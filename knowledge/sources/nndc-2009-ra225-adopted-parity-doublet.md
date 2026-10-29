---
type: source
title: "NNDC 225Ra Adopted：低能宇称伙伴与31.50-keV E1"
aliases: [NNDC225Ra parity doublet adopted, Ra225 31.50 keV E1]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data
reading_depth: skimmed
title_original: "225RA ADOPTED LEVELS, GAMMAS"
authors: [A. K. Jain, R. Raut, J. K. Tuli]
journal: Nuclear Data Sheets
year: 2009
volume: 110
pages: "1409"
citation_key: NNDC225RaAdopted2009
citation_key_origin: ENSDF-header-local-key
canonical_source: "NNDC ENSDF 225088001,225RA, ADOPTED LEVELS GAMMAS"
source_url: "https://www.nndc.bnl.gov/ensdf/"
data_version: "2009-05 listing; H header NDS 110, 1409 (2009), CUT 1-Dec-2008; H err update 11-Mar-2013"
raw_storage_status: "official-response-archived-as-retrieved-html-wrapper"
raw_file: "raw/data/day26-20261028/225ra-adopted-225088001-016.html"
raw_sha256: "93ce30628f3f24d08bc1e69c47d2c96e739748868fd03407ddbede9e4732e31e"
nuclei: [225Ra]
observables: [level-energy, spin-parity, B(E1), B(E2), half-life]
methods: [ENSDF-evaluated-fixed-column]
tags: [parity-doublet, odd-A, octupole, evaluated-data, source-lineage]
---

# $^{225}$Ra 的评价能级与 E1 记录

## Bibliographic Record

NNDC `DatasetFetchServlet` 以 `nuc=225Ra&searchType=quick&datasource=ensdf` 返回 `225088001,225RA` Adopted；再以 `EnsdfDispatcherServlet` 的 `dbclass=ensdf&page-source=singular&datasetcheck=225088001,225RA&chooseit=ENSDF text format` 获取固定栏文本。H 行给出 Jain、Raut、Tuli，*Nuclear Data Sheets* **110**, 1409 (2009)，cutoff 2008-12-01；另有 Singh 2013-03-11 RI 更正。本页取固定栏对象，不将 2013 年更正当新独立实验。

## Scope and Reading Depth

定向读取本对象头部及 0–120.36 keV 的 L/G/B 记录与伴随 Jπ、T、来源注释。未逐条读取其余能级，也未取得原论文 1985Is03、1983Ah03、1970Tr04 的完整实验正文。评价对象是二手核数据汇编，数值来源层级须与原实验区分。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| NR225-1 | Adopted A 带列 $0.0\,(1/2^+)$、$25.41(2)\,(5/2^+)$、$42.77(3)\,(3/2^+)$、$111.60(5)\,(7/2^+)$ keV；B 带列 $31.56(3)\,(3/2^-)$、$55.16(6)\,(1/2^-)$、$69.36(6)\,(7/2^-)$、$120.36(6)\,(5/2^-)$ keV。括号为 ENSDF 末位不确定度；其中 $1/2^-$、$7/2^-$ 指认带括号。 | evaluated-level-data | direct-evaluated-object | `225088001` L 0.0–120.36; band tags A/B | true |
| NR225-4 | 评价基态记录静态磁偶极矩 `MOMM1=-0.7338(15) μ_N`，并注明来自激光谱学（1987Ar20、1983Ah03）；该数值属于评价对象，不能与双重态 `B(M1)` 混同。 | evaluated-static-moment | direct-evaluated-object | 归档 ENSDF L71–81 | true |
| NR225-2 | $31.56$ keV 的 $3/2^-\to1/2^+$ 31.50-keV E1 支线给 $B(E1)=0.00081(20)$ W.u.；评价注释引用 1985Is03 寿命及该跃迁 E1 类型。 | evaluated-transition-strength | direct-evaluated-object | 归档 ENSDF 第 90–95 行：L31.56、G31.50、其后 B 行的 BE1W 字段；L T/J comments | true |
| NR225-3 | 同自旋 A/B 能量中心差 $E_- -E_+$：$I=1/2$ 为 $+55.16$ keV（负宇称指认暂定），$I=3/2$ 为 $-11.21$ keV，$I=5/2$ 为 $+94.95$ keV，$I=7/2$ 为 $-42.24$ keV（负宇称指认暂定）。这些仅为评价能级差；Coriolis、不同转动惯量和组态混合均可能参与，不是单一八极隧穿常数。 | derived-from-evaluated-levels | evaluated-object-arithmetic | NR225-1 paired A/B L lines | true |

## Summary

评价数据支撑 $^{225}$Ra 低能 A/B 伙伴的逐自旋比较，也直接限制笼统的“极小劈裂 $<50$ keV”：此表中两项中心差满足，一项约 55 keV、一项约 95 keV。评价 E1 中心值 $8.1\times10^{-4}$ W.u.，低于泛称的 $10^{-3}$–$10^{-2}$ W.u. 范围，显示区间不能无条件覆盖所有支线。它属于评价量；核素内禀 $D_0$ 仍需声明转子 $K$ 与单位约定才能从该单线反推。

## Competing Interpretations and Limitations

评价 Jπ 指认有实/括号之别，且能级中心差随 $I$ 交替变号；不可将同自旋差直接写成正的八极隧穿间隔。该 E1 支线源于寿命与多极性评价，不是本次重新分析原始计数或转换系数。只比较不同初态的 B(E1) 与 B(E2) 不构成同一跃迁强度比。原实验来源与评价依赖关系需继续追踪。

## Knowledge Impact and Learning Decision

`supports` 225Ra 低能伙伴能级的条件系统学；`limits` 单一正劈裂和泛用 E1 数量级；在原实验获取前保留 evaluated 标签。

## Extracted Pages

- [[odd-a-parity-doublet-blocking-audit]]：评价能级差、E1 几何换算与原实验待核验边界。

## Sources

- [[gaffney-2013-pear-shaped-rn-ra]]：偶偶 $^{224}$Ra 的独立库仑激发；其所引 odd-A 间隔不是本评价的独立复测。
- [[butler-nazarewicz-1996-intrinsic-reflection-asymmetry]]：反射不对称理论综述，不作为本表数值来源。
