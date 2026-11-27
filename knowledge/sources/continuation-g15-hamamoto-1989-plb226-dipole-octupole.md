---
type: source
title: "Hamamoto等1989：变形稀土核偶极跃迁与八极振动耦合理论（PLB全文5页）"
aliases: ["Hamamoto 1989 PLB dipole-octupole", "Phys. Lett. B 226 17", "10.1016/0370-2693(89)90280-3"]
created: 2026-11-07
updated: 2026-11-27
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: read
title_original: "Electric-dipole transitions in deformed rare-earth nuclei"
authors: ["I. Hamamoto", "J. Höller", "X. Z. Zhang"]
journal: Physics Letters B
year: 1989
volume: 226
pages: 17-21
doi: 10.1016/0370-2693(89)90280-3
canonical_source: "https://doi.org/10.1016/0370-2693(89)90280-3"
citation_key:
raw_file: raw/papers/gpt/query/20261107-continuation-G15/Hamamoto-1989-PLB-226-17.pdf
raw_sha256: 5b31944f6183f1e66fcd9863d584f7221f52d0cbb18da8d79eaa6d545af30a98
raw_storage_status: fully-archived-local
archive_required: true
nuclei: ["177hf", "169lu"]
models: ["particle-rotor-model", "nilsson-potential", "bcs-pairing", "particle-vibration-coupling"]
observables: ["B(E1)", "E1-matrix-elements", "spin-alignment-dependence", "b0-b1-parameters"]
tags: ["e1-transitions", "octupole-vibration", "dipole-octupole-coupling", "effective-e1-operator", "rare-earth", "177hf", "169lu", "coriolis-coupling", "fulltext-read"]
---

# Hamamoto1989：稀土E1跃迁的八极极化有效算符

## Bibliographic Record

I.Hamamoto、J.Höller、X.Z.Zhang，PLB226,17–21(1989)，
DOI10.1016/0370-2693(89)90280-3。实际5页PDF与Elsevier XML已归档。
取得HTTP全文不等于获得公开再分发授权，PDF保留本地。

## Scope and Reading Depth

G15提取全文；总控核读首页与静态极化/算符段，Terra独立回读pp17–20，
尤其p19 Eqs2–3和Fig2。未重跑作者PRM、BCS或拟合，也未逐篇读取全部被引实验。

## Key Results

| ID | 可核查内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| H89-1 | 文章以177Hf的低能E1为例，比较包含Coriolis耦合的单准粒子描述及八极极化扩展 | model-comparison | direct | pp17–20、Fig1 | false |
| H89-2 | 明确写实验室E1与内禀分量的Wigner D1旋转关系 | author-derivation | direct | p19 Eq2 | false |
| H89-3 | 内禀算符为eeff rY1ν + e bν r³Y3ν；八极项电荷因子是e | author-derivation | direct | p19 Eq3 | false |
| H89-4 | 推导使用粒子—八极振动微扰，并讨论本例跃迁能相对八极模较低的静态极化条件 | model-assumption | direct | p19、Fig2 | false |
| H89-5 | b0和b±1携带模式/极化信息，以数据调整；不是纯几何CG系数 | author-interpretation | direct | pp19–20 | false |

## Conditions and Competing Explanations

轴对称参考下的良好K与指定rank1直接耦合限制所讨论的模式；它不是所有八极激发的禁戒。
Coriolis、配对、单粒子波函数及E1屏蔽都影响作者的比较，不能把一个强E1解释为静态β3测量。
本文静态近似的适用条件属于本文低能稀土算例，不能直接以102Ru的最低3−能量
判断约5MeV QRPA响应必然失效或必然有效。

## History and Transfer

1993后续文[[continuation-g15-hagemann-1993-prc47-octupole-softness]]讨论了旧程序修正，
使用拟合数值时须核对版本；本页不把1989与1993参数静默混合。
[[continuation-g15-effective-e1-origin-20261107]]和
[[continuation-t02-ru102-covariant-effective-e1-20261107]]区分原文旋转表示与本任务协变构造。
旧文e·b与2026的eeff·b不同，不可直接比较b数值而不检查电荷/算符约定。

## Agent Self-audit Triage

原件身份与哈希已核。撤回worker关于三轴全K解禁、协变唯一性与普适静态失效的推论。
未重现原作者计算；来源中的拟合是模型结果，不是独立测得的介质常数。


## Summary

本页记录该原件实际提供的实验/模型信息与读取边界；核心数据/公式沿用上文原表locator，不作为新实验或作者代码复现。


## Competing Interpretations and Limitations

模型参数和解释不等于实验直接测量；原文未报告不等于严格为零或全球不存在。局部比较不能排除全部模型族，适用条件与缺失响应沿用本页记录。


## Extracted Pages

实际读取的PDF/出版页、XML原文段及表号见Scope和逐项locator；全文文件可用不代表全部图点/转引原件或生产实现已核。

## 2026-11-27 — 馆藏原件与覆盖核对

- 物理第1页（印刷第17页）｜刊头、引言、¹⁷⁷Hf 两条 yrast 带及数据来源。
- 物理第2–3页（印刷第18–19页）｜粒子–转子计算、图1比较、式(1)–(3)、图2微扰示意。
- 物理第4–5页（印刷第20–21页）｜¹⁷⁷Hf 拟合结果、¹⁶⁹Lu 图3预测、候选带对、致谢与参考文献。
- 本次获取的具体覆盖：通读物理第1–5页所给文本，包括正文、图1–3图注、式(1)–(3)可辨部分、致谢及参考文献[1]–[13]。图像、图点及公式的排印细节留待核查。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A21-1 | 作者转引文献[6]的 ¹⁷⁷Hf [624 9/2] → [514 7/2] 带间 E1 数据。对 Iᵢ>9/2 的数据，作者用基带观测值 Q₀=674 fm² 换算绝对 B(E1)；图1以约定相位绘制带符号的跃迁振幅。 | reported-observation | source-reported | 物理第1页引言、第2页图1图注及式(1)、第3页实验数据比较段。图上符号与点位核物理第2页。 | true |
| A21-2 | 含 BCS 配对和 Coriolis 混合的单准中子–转子计算，在 e_eff=−0.15e 且只用式(3)首项时，给出的跃迁强度偏小，自旋依赖也与数据定性不符。加入八极项并调整 b₀、b±₁ 后，作者报告振幅再现有所改善。 | model-comparison | source-reported | 物理第2页模型段及图1、第3页比较段及式(3)、第4页首段。两组计算点与实验点核物理第2页图1。 | true |
| A21-3 | 作者以粒子–八极振动微扰引入 Kᵖ=0⁻、1⁻ 模的贡献。式(2)把内禀分量旋转到实验室系，式(3)的内禀项为 e_eff·rY₁ν 与 e·bν·r³Y₃ν。作者以本例 E1 跃迁能低于300 keV、远低于预期最低八极模能量为由采用静态极化近似。 | author-derivation | source-reported | 物理第3页式(2)–(3)、图2及相邻正文。式(2)的 D 矩阵指标与共轭约定、式(3)的上下标及图2图符核物理第3页。 | true |
| A21-4 | 作者把 ¹⁷⁷Hf 拟合的 bν 用于 ¹⁶⁹Lu [411 1/2] → [541 1/2]，并取质子 e_eff=+0.20e。文中提出 ΔI=±1 的 B(E1) 可能呈现 signature 依赖，留待实验检验。 | model-prediction | source-reported | 物理第4页图3图注及相邻正文、第5页首段。若引用两面板的具体量级或点位，核物理第4页图3的不同纵标。 | true |

¹⁷⁷Hf 的比较依赖文献[6]的数据、作者选用的 Q₀ 与有效电荷，以及配对和 Coriolis 混合。bν 由该数据集调整，综合八极模频率、集体性及其 E1 矩。¹⁶⁹Lu 的预测继承这一参数选择。

- H89-1 的图证定位改为物理第2页图1、第3页比较正文及第4页首段。把图1的观测纵量写为按作者相位约定绘出的跃迁振幅，保留 B(E1) 与振幅的区别。
- H89-2 保留一阶 Wigner D 旋转的含义，物理第3页提取文本不足以逐字符确认指标次序或共轭。H89-3 保留八极项的电荷因子 e，并以同页式(3)核对排印。
- 若补录1989年拟合值，以物理第4页正文的 b₀=+9.53×10⁻³ fm⁻²、b₋₁=b₊₁=+8.36×10⁻⁴ fm⁻² 为文本依据。物理第2页图1内参数的正号及幂次提取失真，引用图内标注前核原页。
