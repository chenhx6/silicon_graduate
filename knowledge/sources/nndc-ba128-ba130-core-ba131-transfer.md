---
type: source
title: "NNDC：128,130Ba核芯与130Ba(d,p)131Ba记录"
aliases: [Ba128 Ba130 core ENSDF controls, Ba131 addition-channel readiness]
created: 2026-11-05
updated: 2026-11-06
status: ai-draft
review_status: unreviewed
source_type: evaluated-data-collection
reading_depth: skimmed
title_original: "128Ba and 130Ba Adopted Levels, Gammas; 130Ba Coulomb Excitation; 130Ba(d,p)131Ba"
authors: [NNDC ENSDF, Balraj Singh, Zoltan Elekes, Janos Timar, Yu. Khazov, I. Mitropolsky, A. Rodionov]
year: 2026
canonical_source: "ENSDF Ba128/Ba130 adopted, Ba130 Coulomb and Ba131(d,p): source snapshot 20261105"
citation_key: NNDCBaCoreSnapshot20261105
citation_key_origin: task-source-snapshot
raw_file: raw/papers/gpt/query/20261105-ba129-core-constraints/manifest.json
raw_sha256: 4aa6e4e1e746fea3a1444d5399d5343254fedce09b53e82f98bb23a1b6a330c0
archive_required: true
nuclei: [128ba, 129ba, 130ba, 131ba]
observables: [energy-spectrum, BE2, spectroscopic-quadrupole-moment, g-factor, spectroscopic-strength]
tags: [a130, core-constraint, ensdf, transfer, evaluation-lineage]
---

# 邻偶核输入和加中子资料的实际边界

## Bibliographic Record

2026-11-05取得的是旧评价的当前服务器快照，不能称为2026实验。

| 别名 | 集合内原件 | 评价版本和文献截止 |
| --- | --- | --- |
| B128 | `nndc128-adopted-text.ens`；对应20页PDF | 201510/15NDS，Elekes–Timar，NDS129,191(2015)；2015-02-28 |
| B130 | `nndc130-adopted-text.ens`；对应13页PDF | 200107/01NDS，Singh，NDS93,33(2001)；2001-05-11 |
| C130 | `nndc130-coulomb-text.ens` | 同一2001评价，库仑激发对象 |
| P131 | `nndc131-dp-text.ens` | 200612/06NDS，Khazov等，NDS107,2715(2006)；2006-07-17 |

网页响应原字节保留为`.response.html`；文本是其唯一`pre`元素的内容，
另存并登记派生关系、SHA-256及POST参数。下文行号计入文件首空行。
PDF与文本是同一评价的不同输出，不是独立数据。

## Scope and Reading Depth

核对两份adopted的首页低能表及选定记录、全部C130和P131对象。
两份首页关键能量、括号及寿命已视觉核验。未重读全部高自旋表；
未取得1989Bu07、1970Vo04等实验正文，不外推评价摘要为原实验复算。

## Summary

低自旋核芯能级可检验恒定惯量假设。130Ba电磁尺度有可用的B(E2)和g因子，
但Q有两分支，且库仑对象的寿命由B(E2)导出。131Ba加中子对象没有明确l=5
强度，不能补成h11/2加/移除联合约束。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| BC-1 | 128Ba的2_1、2_2、3_1能量为284.00(8)、884.50(12)、1324.37(14)keV；γ带奇/偶自旋分别标A/B。 | evaluated-data | evaluated-record-visually-checked | B128 L48/60/83；band注L19–20；PDFp.1 | true |
| BC-2 | 130Ba对应能量为357.38(8)、908.02(8)、1361.06(9)keV；最后态保留Jπ=`3(+)`，两γ带态标N。 | evaluated-data | evaluated-record-visually-checked | B130 L43/69/80；band注L35；PDFp.1 | true |
| BC-3 | 130Ba B(E2;0→2_1)=1.163(11)e²b²，为constructive/destructive两值1.167(11)/1.159(12)的评价平均；g(2_1)=0.35(3)来自另一1980采集。 | evaluated-EM-and-lineage | evaluated-record | C130 L18–22、L19；B130PDFp.1 | true |
| BC-4 | Q(2_1)两支为−1.02(16)与−0.09(16)eb，依赖重取向干涉和2_2→2_1主E2假设；不能择一称唯一形状。 | ambiguity-and-method | evaluated-record | C130 L23–26；B130PDFp.1 | true |
| BC-5 | C130的40.7(4)ps是由B(E2)导出的半衰期；adopted41.8(12)ps还包含RDDS输入，不能与该B(E2)重复当独立观测。 | dependence-and-quantity | evaluated-record | C130 L17/27；B130 L43及该态注，PDFp.1 | true |
| BC-6 | P131含46个L记录，已给l仅0–3或其括号形式，没有明确l=5强度；原采集1970Vo04为12-MeV(d,p)，评价列DWBA的S′。 | dataset-coverage | evaluated-record-plus-count | P131 L2–8及全部46个L记录 | true |

## Competing Interpretations and Limitations

B128/B130能级由多种采集评价得到，完整协方差未给。3(+)的括号不移除。
P131的空l/S′字段不是零强度或上限；2006截止对象也不是截至2026的穷尽文献调查。
核芯与奇核可能有形状极化、配对和有效算符差异，不能直接锁定同一惯量。

## Extracted Pages

- [[ba129-core-and-pairing-validity]]
- [[ba129-model-input-and-holdout-contract]]
- [[paired-single-j-positive-bcs-rotor]]

## Human Review

Codex来源核查与定向计算；未声明human-reviewed。
