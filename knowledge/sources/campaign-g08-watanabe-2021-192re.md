---
type: source
title: "Watanabe et al. 2021 - Beta Decay of the Axially Asymmetric Ground State of 192Re"
aliases: ["Watanabe 2021 192Re", "Watanabe 2021 PLB", "192Re beta decay KISS"]
created: 2026-11-07
updated: 2026-11-07
status: active
archive_required: true
review_status: unreviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Beta decay of the axially asymmetric ground state of 192Re"
year: 2021
canonical_source: "https://doi.org/10.1016/j.physletb.2021.136088"
citation_key: ""
raw_file: "raw/papers/gpt/query/20261107-campaign-G08/watanabe-2021-192re-beta-decay.pdf"
raw_sha256: "58142e4d2335a126f270a3a076d7cc19d1d06c8ca9ed19c0a60adc207d7f9780"
tags: ["experiment-ingest", "beta-decay", "192re", "192os", "gamma-soft", "kiss", "hfodd", "a190"]
authors: ["H. Watanabe", "Y. X. Watanabe", "Y. Hirayama", "A. N. Andreyev", "T. Hashimoto", "F. G. Kondev", "G. J. Lane", "Yu. A. Litvinov", "J. J. Liu", "H. Miyatake", "J. Y. Moon", "A. I. Morales", "M. Mukai", "S. Nishimura", "T. Niwase", "M. Rosenbusch", "P. Schury", "Y. Shi", "M. Wada", "P. M. Walker"]
journal: "Physics Letters B"
volume: 814
pages: "136088"
doi: "10.1016/j.physletb.2021.136088"
nuclei: ["192re", "192os", "191re"]
---

# Watanabe2021：192Re低自旋β布居与结构解释

## Bibliographic Record

H. Watanabe et al., PLB814,136088(2021)，DOI10.1016/j.physletb.2021.136088。
White Rose出版版副本共7物理页，PDF1为库方封面，PDF2–7为六页论文。

## Scope and Reading Depth

### Covered scope

正文、Table1和Fig2的β布居/半衰期及HF解释；总控回查实际PDF2–6。

### Not covered

未取得原始β计数、分支完整Cov和HFODD生产代码。
本文是A192链，不是对A194预测高自旋态的直接搜索。

## Key Results

| ID | 实际内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WA21-1 | KISS测192Re的T1/2=15.1(6)s；由β布居/logft暂定基态Jπ=(0−) | experimental-fact + author-interpretation | direct | PDF4 Fig2/讨论 | false |
| WA21-2 | 作者由总β与已观测馈送差估基态β分支89(2)%；低自旋0+/2+布居与logft支持上述指认 | experimental-fact, intensity-balance-derived | direct | PDF4 Table1/Fig2 | false |
| WA21-3 | 低J母态与给定Qβ/选择定则使高J态布居不利；不等于所有高阶禁戒宽度严格为零 | experimental-criterion | direct-framework + our-inference | PDF4/6；本任务边界 | false |
| WA21-4 | HF+SVI以单核子组态与轴不对称形变解释基态/同位素演化 | model-result | direct | PDF5–6 Tables2–3 | false |

## Experiment and Interpretation Boundary

PDF3实际写136Xe与natural Pt多核子转移，靶厚10.7mg/cm²；
不是worker草案的富集198Pt12.5mg/cm²。装置安装与各探针数据使用仍按原文分开。
(0−)是基于强度/logft的暂定指认，不是本次独立直接自旋测量。
0−→0+按作者讨论为first-forbidden non-unique，不能写“一阶非禁戒”。

## Competing Interpretations and Limitations

基态分支由强度平衡而非逐个直接看见β到基态，依赖未见弱feeding的处理。
低自旋β布居限制说明“不观察高自旋γ”可能有选择性原因，
但本论文不能证明194Os某个预测态不存在、已发现或当前搜索已穷尽。
不得将192Re→192Os与194Os跨质量数混作一份直接负结果。

## Summary

为A192增加一个低自旋布居和暂定Jπ的原实验基准。
其HF形变与更高自旋Os/Ir的PES要逐态比较，不能由一个基态推广整个同位素链。

## Knowledge Impact and Learning Decision

`supports + bounded comparison`，关联[[campaign-g08-a190-shape-isomer-20261107]]。
不由本篇单独提取普适gA或高自旋异能态搜寻概率。

## Agent Self-audit Triage

P0: none identified in PDF identity/hash。P1：总控纠正封面/正文页数、靶信息、
暂定自旋、强度平衡属性和A192/A194区分；撤回“完全不能馈送J≥4”的绝对断言。

## Extracted Pages

PDF2–7；题录/方法与布居/模型的定位已分别列出。
