---
type: source
title: "NNDC/ENSDF：176Lu异能态β衰变2006评价快照（2026-11-13取得）"
aliases: [176Lu isomer beta ENSDF2006, Lu176 beta branch snapshot]
created: 2026-11-13
updated: 2026-11-13
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data
reading_depth: read
title_original: "176LU B- DECAY (3.664 H), ENSDF dataset 200602; 176Lu Adopted Levels, Gammas"
authors: [M. S. Basunia, National Nuclear Data Center]
year: 2006
journal: Nuclear Data Sheets
volume: 107
pages: "791"
doi: ""
canonical_source: "https://www.nndc.bnl.gov/ensnds/176/Lu/adopted.pdf"
citation_key: nndc-176lu-beta-2006-snapshot
raw_file: raw/papers/gpt/query/20261113-A130-lu176-beta-evaluation/manifest.json
raw_sha256: e0e1c858a7e0353c851bcb71a372ccf9b0cf13b54df7fb1222bdffa81cdeba29
archive_required: true
decay_text_file: raw/papers/gpt/query/20261113-A130-lu176-beta-evaluation/176lu-isomer-beta-2006-ensdf-extracted.txt
decay_text_sha256: d9c5116aebb776d24dc0459487180d610a854a2b6119c4f88ddf2ad1a0e61829
nuclei: [176Lu, 176Hf]
models: [evaluated-decay-scheme]
observables: [beta-branching, spin-parity, log-ft, half-life]
methods: [ENSDF-evaluation, gamma-intensity-balance]
tags: [doctoral-thesis, section-4-8, isomer, weak-decay, first-forbidden, evaluated-data]
---

# 176Lu异能态：优势β支路的宇称与评价归一化

## Bibliographic Record

直接HTTP取得的ENSDF衰变数据头为`200602`，
列M. S. Basunia、Nuclear Data Sheets 107, 791 (2006)，文献截止日为2005-09-15。
同时保存NNDC的176Lu Adopted PDF、原始HTML及其`pre`块的本地文本提取。
取得时间为2026-11-13，不代表2026年新评价，也不自动代表该核素最新推荐值。
三个文件的实际大小、SHA和来源地址在集合manifest中。

## Scope and Reading Depth

定向读冻结文本的dataset header、parent、normalization和各level/beta行；
另读本地42页Adopted PDF的物理第1–2页。未逐项重建γ级联、转换电子、
原始测量协方差或全部评价文献；没有重算端点、Q值与log ft。
以下行号均指留档的`176lu-isomer-beta-2006-ensdf-extracted.txt`。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LU176-B-1 | Parent记录为1−、半衰期3.664(19) h；本份衰变表P记录能量为123.0(14) keV。另一个Adopted表给122.845(8) keV，不能当同一精度输入混用。 | evaluated-data | direct-snapshot | 文本19行；Adopted PDF1异能态行 | false |
| LU176-B-2 | 优势β馈入为Hf176的0+基态39(2)%及88.361(9)-keV 2+态61(2)%；表列log ft分别6.85(3)、6.54(2)。 | evaluated-intensity-balance | direct-snapshot | 文本25–38行；Iβ总说明第4行 | false |
| LU176-B-3 | 对1−→0+和1−→2+，宇称改变、ΔJ=1，按最低阶β选择规则属于一级禁戒非唯一型，不能称为允许GT主支。 | selection-rule-inference | task-derived-from-evaluated-spins | LU176-B-1/2；选择规则采用标准良宇称与β多极展开 | false |
| LU176-B-4 | 表中还列1247.62(6)-keV 2−态，β馈入0.00146(4)%；不能把纠错扩大成“所有β分支均禁止允许GT”。 | evaluated-data-plus-selection-boundary | direct-snapshot | 文本60–62行 | false |
| LU176-B-5 | 衰变dataset N行采用BR=1、NB=1；Adopted Lu表另列β−99.905(16)%及ε0.095(16)%。不同归一化约定必须保留。 | normalization-boundary | direct-snapshot | 文本20–23行；Adopted PDF1异能态Comments | false |

39(2)%和61(2)%是本评价表的强度平衡结果，不能作为两组独立、无协方差的直接β计数。
其舍入中心相加为100，不证明所有弱支路和EC已被精确计入。
不要把表内近似BR=1升级为全母态衰变绝对归一化的高精度测量。

## Summary

本次冻结的2006评价表提供了母态与末态自旋宇称、优势β馈入及其评价归一化。
它支持撤回“主要允许GT”的描述，并用最低阶选择规则识别两条优势一级禁戒非唯一支路；
不把所有弱支路归为同类，不从log ft单独决定算符，也不声称取得最新评价或原始测量协方差。

## Competing Interpretations and Limitations

本来源解决的是“主要允许GT”这一错误标签，不通过log ft大小单独判定跃迁类型，
也没有从宇称规则计算出半衰期。一级禁戒率仍涉及各相应算符、相空间、
组态及干涉；不能只给所有分支乘同一个经验GT淬灭因子。

浏览器检索工具显示的同URL摘录与本次直接HTTP保存的快照在个别能量栏有差别；
原因未核，不猜测更新机制或时间。本页数值只引用已哈希的本地字节，
不拼接另一摘录中的parent能量或88-keV能级数值。
Adopted表的Q记录、历史衰变端点及不同精度能量尚未统一核对，不用于本次新能量预算。

评价汇编与[[doctoral-r1-g33-gintautas-2009-176lu-thermal-equilibration]]采用的能级资料存在依赖；
不能把它们数成两次独立的新实验。该理论热化来源的桥态与速率讨论另有自己的条件。

## Extracted Pages

- 冻结ENSDF文本第2–4、19–38、60–62行；Adopted PDF1–2。
- 修正[[a130-rewrite-open-network-and-entry-ensemble-20261113]]中原先未取得分支表的缺口，
  为[[doctoral-nuclear-structure-foundations]]的4.7/4.8提供具体反例。
- 没有新增用户实验或最新评价认证；没有把历史review字段当知识资格。
