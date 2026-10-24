---
type: source
title: "In-beam spectroscopy of medium- and high-spin states in 133Ce"
aliases: []
created: 2026-07-01
updated: 2026-07-02
status: active
review_status: human-reviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "In-beam spectroscopy of medium- and high-spin states in 133Ce"
authors: [A. D. Ayangeakaa, et al.]
journal: Physical Review C
year: 2016
volume: 93
pages: 054317
doi: 10.1103/PhysRevC.93.054317
arxiv:
language: en
canonical_source: doi:10.1103/PhysRevC.93.054317
zotero_item_key:
citation_key: ayangeakaa_2016_Inbeamspectroscopy
zotero_uri:
library_file:
raw_file: "raw/papers/2016_Ayangeakaa et al_In-beam spectroscopy of medium- and high-spin states in Ce 133.pdf"
raw_sha256: F2C9BA6A17D231356A0D40E69752E802F0560C56882C0EFE57852D2E16B91E6E
nuclei: [133ce]
reactions: [116cd-ne22-5n-133ce]
experiments: [atlas-133ce-ne22-112mev]
models: [cranked-nilsson-strutinsky-model, covariant-density-functional-theory, tilted-axis-cranking]
observables: [signature-splitting]
methods: [gamma-gamma-coincidence, two-point-angular-correlation-ratio]
tags: [a130, high-spin, triaxiality, in-beam-spectroscopy, gammasphere]
---

# Ayangeakaa 等（2016）：`133Ce` 中高自旋谱学

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

Physical Review C 93, 054317 (2016)，DOI `10.1103/PhysRevC.93.054317`。Zotero `Wiki Inbox` 的 Better BibTeX 导出给出 citation key `ayangeakaa_2016_Inbeamspectroscopy`。

## Scope and Reading Depth

全文精读；视觉核对 Figs.1-2 的能级纲图、Figs.7-10 的能量和 alignment 系统学、Fig.11 的 TAC-CDFT 比较及 pp.18-19 总结。论文覆盖的带很多，本轮只抽取可长期复用的实验地图、模型边界和核素级结论，不逐条转录全部 γ 跃迁。

## Summary

作者利用 `116Cd(22Ne,5n)133Ce` 和 Gammasphere 扩展 `133Ce` 能级纲图至约 22.8 MeV、最高自旋 93/2，识别 11 条四极序列和两条新偶极带，并把此前未与低能级连接的高自旋三轴带接入已知能级。CNS 和 TAC-CDFT 计算支持中高自旋区存在显著三轴形变和不同转轴取向，但具体组态与 γ 值均具有模型依赖。

## Experimental or Theoretical Setup

- 反应：`116Cd(22Ne,5n)133Ce`；
- 束流：112 MeV `22Ne`，Argonne ATLAS；
- 靶：1.48 mg/cm² 富集 `116Cd`；两次实验分别采用 Al/Au 夹层和 Au backing；
- 阵列：Gammasphere，分别有 101 和 88 个有效 Compton-suppressed HPGe；
- 数据：合计 `4.1×10^9` 个 fold≥4 prompt coincidence events；
- 分析：三维、四维 γ 符合；角分布和两点角关联比 `R_ac`；
- 理论：cranked Nilsson-Strutinsky（CNS）及 band D3 的 TAC-CDFT。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| A16-1 | 能级纲图延伸至约 22.8 MeV 和自旋 93/2；共讨论 11 条四极带及 9 条偶极带，其中 D8、D9 和 Q1-Q3、Q11 为新识别序列。 | experimental-fact | direct | PDF p.1 abstract; pp.2-13, Figs.1-2 | false |
| A16-2 | 新连接跃迁把此前高自旋 Q 带接入低能结构，从而约束其激发能、自旋和宇称；部分弱带头指认仍依赖理论比较。 | experimental-fact | direct | PDF pp.2-13, Table I | false |
| A16-3 | CNS 对 D3、D6、D8、D9 的计算与实验能量通常在约 ±0.5 MeV 内一致，并给出随自旋 `ε2≈0.22→0.18`、`γ≈+24°` 的三轴解。 | model-result | direct | PDF p.15, Fig.9 | false |
| A16-4 | 旧的 Q5/Q7 近简并及 signature-partner 解释在新连接关系下不再成立。 | author-interpretation | direct | PDF pp.16-17, Fig.10 | false |
| A16-5 | TAC-CDFT 对 D3 的中等自旋能量和频率给出较好描述，但低、自旋端不收敛且未计算全部偶极带。 | model-result | direct | PDF p.18, Fig.11 | false |
| A16-6 | 作者认为整体结果强烈支持 `133Ce` 中高自旋区的显著三轴形变以及绕不同主轴或倾斜轴转动。 | author-interpretation | indirect | PDF pp.18-19, Summary | false |

## Nuclear Structure Information

- `133Ce` 为 `Z=58, N=75` 奇中子核；
- 低能区预计为较小形变，文中给出 `ε2≈0.15-0.20` 的尺度；
- D 带表现为小 signature splitting 的 ΔI=1 序列；作者指出这提示倾斜轴不稳定性，但不等同于已经证明静态手征；
- 多条 Q 带随自旋发生组态或三轴最低点变化，不能用一个固定 γ 形状概括全核。

## Authors' Interpretation

中高自旋 `133Ce` 展现多准粒子组态竞争、显著三轴性以及绕不同轴的集体转动。D3 的 TAC-CDFT 结果与非典型的 B(M1) 趋势使手征几何或手征振动“不能排除”，措辞并非确认。

## Model Results

- CNS 忽略配对，主要适用于中高自旋；
- D3 的 TAC-CDFT 使用 PC-PK1，计算中同样忽略 pairing；
- 计算形变是指定组态与模型下的极小值，不是直接测量；
- 某些 Q 带需要随自旋改变组态或在正负 γ 极小值之间切换。

## Competing Interpretations and Limitations

- 论文的 MχD 说明主要回引同一数据集的早期工作，当前来源不是该指认的完整独立复核；
- 弱跃迁的自旋宇称部分依赖理论解释；
- CNS/TAC-CDFT 的参数和组态匹配存在非唯一性；
- 小 signature splitting、三轴解或能量再现都不能单独证明手征双重带。

## Extracted Pages

- Nuclei: [[133ce]]
- Experiment: [[atlas-133ce-ne22-112mev]]
- Concepts: [[triaxial-deformation]], [[chiral-doublet-bands]], [[signature-partner-bands]]
- Models: [[cranked-nilsson-strutinsky-model]], [[covariant-density-functional-theory]], [[tilted-axis-cranking]]
- Observables: [[signature-splitting]]
- Methods: [[gamma-gamma-coincidence]], [[two-point-angular-correlation-ratio]]

## Personal Notes

这篇论文适合作为 `133Ce` 的“谱学地图”，但不宜把其所有模型组态一次性固化成确定知识。后续应按具体研究问题回到 Table I 和 Figs.1-2 建立单带页。

## Day 21周考对比：133Ce高自旋谱学演化与手征模式措辞弱化（Checkpoint 004）

## Day21 checkpoint057：2016全谱拓扑演化与模式确定性收缩审计

124纠正：Q5/Q7的旧解释和D3等手征讨论不是同一对带；不得用一句措辞改变声明原2013全部MChD被撤回。旧全文见superseded-124，不声称本轮新读这些原件全文。原review与原始claims/flags保持。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| A16-D21-1 | superseded：124撤回本条新科学认证；改用本页A16-4的有限范围。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |
| A16-D21-R57-1 | superseded：124撤回本条新科学认证；改用本页A16-4的有限范围。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |
