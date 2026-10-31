---
type: source
title: "Search for the origin of wobbling motion in the A≈130 region: The case of 131Xe"
aliases: []
created: 2026-07-01
updated: 2026-10-30
status: active
review_status: human-reviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Search for the origin of wobbling motion in the A ≈ 130 region: The case of 131Xe"
authors: [S. Chakraborty, et al.]
journal: Physical Review C
year: 2023
volume: 107
pages: 064318
doi: 10.1103/PhysRevC.107.064318
arxiv: 2311.09713
language: en
canonical_source: doi:10.1103/PhysRevC.107.064318
zotero_item_key: 5WSF5D6P
citation_key: chakraborty_2023_Searchorigin
zotero_uri: zotero://select/library/items/5WSF5D6P
library_file: "E:/zetore reference/高自旋/三轴/进动/理论/2023_Chakraborty et al_Search for the origin of wobbling motion in the A ≈ 130 region.pdf"
raw_file: "raw/papers/2023_Chakraborty et al_Search for the origin of wobbling motion in the A ≈ 130 region The case of Xe 131.pdf"
raw_sha256: 730DB39EB9A5AECD3BBCE1DCE3CB9C32829EB2F4A2062EE31C59DDC4D52BD9FF
nuclei: [131xe, 133ba, 135ce]
reactions: [130te-alpha-3n-131xe]
experiments: [vecc-131xe-alpha-38mev]
models: [triaxial-particle-rotor-model, triaxial-projected-shell-model]
observables: [multipole-mixing-ratio, signature-splitting, bm1-be2-ratio]
methods: [dco-ratio, linear-polarization-asymmetry, gamma-gamma-coincidence]
tags: [a130, wobbling, signature-partner, triaxiality, in-beam-spectroscopy]
---

# Chakraborty 等（2023）：`131Xe` 中 wobbling 起源与 signature partner

## Bibliographic Record

Physical Review C 107, 064318 (2023)，DOI `10.1103/PhysRevC.107.064318`。2026-10-30 对原文件哈希与版式复核：当前本地 PDF 为 8 页期刊排版，页脚 `064318-1` 至 `064318-8`，首页列 published 27 June 2023；此前“arXiv 版本”的描述撤回。arXiv `2311.09713` 是另一个可访问入口，不因标识相同而把本地期刊 PDF 认成预印本。

## Scope and Reading Depth

全文精读；视觉核对 Fig.1 能级纲图、Table I、Figs.4-5 的 mixing ratio 约束和 Fig.11 的 TPSM/TPRM 比较。

## Summary

作者重新分析 `130Te(4He,3nγ)131Xe` 数据，建立一条以 9/2-、13/2-、17/2-、21/2- 为成员的新负宇称序列，并研究其与 νh11/2 yrast 带之间的联系。连接跃迁的 DCO 与角分布表明 E2/M1 mixing 很小，主要是 M1；因此该序列被解释为 νh11/2 带的不利 signature partner，而非 wobbling 带。TPRM 在调整到 `ε2=0.13, γ=33°` 后再现实验能级与 signature splitting。作者同时指出 `131Xe` 可具有三轴形变，但本工作没有发现 wobbling 的实验信号，三轴形变本身并不保证 wobbling 出现。

## Experimental or Theoretical Setup

- 反应：`130Te(4He,3nγ)131Xe`；
- 束流：38 MeV α，VECC K-130 cyclotron；
- 靶：2 mg/cm² enriched `130Te`，600 µg/cm² Mylar backing；
- 阵列：7 个 Compton-suppressed INGA clover HPGe，40°、90°、125°；
- DAQ：Pixie-16，250 MHz，12 bit；
- 排序与分析：IUCPIX、INGASORT、RADWARE；
- 理论：TPSM 对照与本文 TPRM。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| C23-1 | 新序列包含 705、816、930 keV 带内跃迁，并通过 177、882、1055、1176 keV 跃迁连接到 yrast 负宇称带。 | experimental-fact | direct | PDF pp.2-3, Fig.1, Fig.2 | false |
| C23-2 | 671、882、1055、1176 keV 为 dipole，705、766、816、930 keV 为 quadrupole；1055 keV 的 δ 接近 0，671/882 keV 的 δ 分别约 0.03(3)/0.09(8)。 | experimental-fact | direct | PDF pp.3-4, Table I, Figs.4-5 | false |
| C23-3 | 连接跃迁的 E2 成分很小，作者据此排除所建序列的 wobbling 性质，并将其解释为 νh11/2 的不利 signature partner。 | author-interpretation | direct | PDF pp.4-6 | false |
| C23-4 | TPRM 采用 `ε2=0.13, γ=33°, ξ=1` 后较好再现有利/不利 signature partners；这是模型拟合结果。 | model-result | direct | PDF p.7, Fig.11 | false |
| C23-5 | yrare 17/2- 态实验 `B(M1)/B(E2)=1.27(14)` 与 TPRM 1.27 一致；yrast 17/2- 的实验值 2.54(4) 约为模型值两倍。 | experimental-fact | direct | PDF p.7 | false |
| C23-6 | yrare 13/2- 上的带被认为是更合适的不利 signature partner；yrast 13/2- 序列的起源仍是开放问题。 | author-interpretation | direct | PDF p.7 | false |
| C23-7 | 作者结论：本工作未发现 wobbling 实验信号；三轴形变本身可能不足以保证 wobbling。 | author-interpretation | direct | PDF p.8, Summary | false |

## Nuclear Structure Information

### `131Xe` 负宇称相关序列

- favored νh11/2 序列：11/2- 164 keV、15/2- 806 keV、19/2- 1616 keV、23/2- 2518 keV、27/2- 3181 keV、29/2- 4061 keV；
- 新建的 yrare 序列：9/2- 341 keV、13/2- 1046 keV、17/2- 1862 keV、21/2- 2792 keV；作者指认为 unfavoured signature partner；
- 另一条 yrast 13/2- 835 keV 起始序列延伸到 17/2- 1601 keV 等态，其物理起源在本文中未解决。

## Authors' Interpretation

低 E2 admixture 是区分普通 signature partner 与 wobbling band 的关键。较大的 signature splitting 可支持 γ deformation，但不能单独证明 wobbling。

## Model Results

- TPSM 能再现 signature splitting，但部分相邻能级差偏离实验；
- TPRM 对 γ 参数高度敏感，调整参数后再现能级；
- 模型成功不等于模型参数代表唯一势能面。

## Analytical Reconstruction

本文的证据链是“新负宇称序列与连接关系 → DCO/角分布约束的低 `delta` mixing → 小 E2 成分 → signature-partner 而非 wobbling 的作者解释 → TPRM/TPSM 模型比较”。其中能级、跃迁和 mixing-ratio 属于实验层；signature-partner 指认、TPRM 参数和三轴解释分别属于作者解释或模型结果。三轴形变可能存在，但不能由此单独推出 wobbling。

## Competing Interpretations and Limitations

- 部分 mixing ratio 由弱跃迁和有限角度 DCO 约束，需复核完整误差传播；
- TPRM 的 γ=33° 是模型输入/拟合，不是直接测量的刚性 γ；
- 对 135Ce wobbling 的讨论是预测性案例，不是本文的新实验确认；
- 本地 Zotero 数据库中还存在一个以 PDF 文件名为标题的附件条目，正式 Zotero item 使用 key `5WSF5D6P`。

## Project Relation

本页是 [[low-spin-wobbling-controversies]] 中 `131Xe` 的反例/边界 source：它把“三轴形变存在”与“观测到 wobbling”分开，并提供低-E2、M1-dominated signature-partner 解释的对照。它不替代 `135Pr`、`187Au` 的争议性原始证据，也不把 TPRM/TPSM 的再现升级为唯一实验结论。

## Human Review Record

- 2026-07-03：既有 claim-review round 记录了用户对 `C23-2`、`C23-5` 的定位与数值复核，并将 C23 claim-level 待审状态清除；当前 `C23-1..C23-7` 均为 `needs_review: false`。
- 2026-07-15：本批次仅更新 citation key、raw filename 和 SHA-256；未重新改写或重新裁决 C23 科学 claims。
- 2026-07-16：用户审核并通过本轮 C23 source page 的 claims、claim kind、locator、证据边界、project relation 和 P0/P1；页面继续保持 `human-reviewed`。

## Human Review Triage

### P0

P0: none remaining. The user completed the current ingest review of C23-1 through C23-7 and accepted the source/project evidence boundaries.

### P1

P1: none remaining for this ingest review.

### P2

- **C23-1/C23-6/C23-7**, PDF pp.2-8: retain the boundary between the observed sequence, the proposed unfavoured signature partner and the unresolved yrast `13/2-` origin; verify cross-links before synthesis reuse.

### P3

- Metadata and traceability: canonical citation key `chakraborty_2023_Searchorigin`, current raw filename and SHA-256 are aligned; no duplicate source is required.

## Extracted Pages

- Nuclei: [[131xe]]
- Bands: [[131xe-nu-h11-2-favored-sequence]], [[131xe-negative-parity-yrare-sequence]], [[131xe-negative-parity-yrast-13-2-sequence]]
- Experiment: [[vecc-131xe-alpha-38mev]]
- Concepts: [[wobbling-motion]], [[signature-partner-bands]], [[triaxial-deformation]]
- Models: [[triaxial-particle-rotor-model]], [[triaxial-projected-shell-model]]
- Observables: [[multipole-mixing-ratio]], [[signature-splitting]], [[bm1-be2-ratio]]
- Methods: [[dco-ratio]], [[linear-polarization-asymmetry]], [[gamma-gamma-coincidence]]
- Synthesis: [[wobbling-vs-signature-partner]]

## Review Status

This source is page-level `human-reviewed`; `C23-1..C23-7` remain `needs_review: false`. Paper-level reuse must still return to the cited transition and model-comparison locators and does not turn TPRM/TPSM agreement into an independent observation. Day28 的新增核验和旧断言撤回属于 Codex self-audit，不扩展既有人审范围；新增 `C23-D28-*` 均保留 `needs_review: true`。

## Personal Notes

这篇文献非常适合做“反证模板”：它并不否定 `131Xe` 三轴性，而是把“存在三轴形变”和“观测到 wobbling”明确拆开。

## Day19量化审计：131Xe纯M1连接线、摇摆零对照基准与软核色散机制

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


本节记录历史脚本 `system/scripts/day19_xe131_wobbling_null_control_audit.py` 及输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/xe131-wobbling-null-control-result-047.json` 的旧断言。Day28 回核原文后撤回其科学认证；脚本运行成功不认证输入来自原文，也不认证模式解释。旧脚本与输出仅作历史审计资产，不能作为本 source 的独立证据。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| C23-D19-1 | superseded / withdrawn by Day28 source audit。671-keV 线属于 yrast 13/2−，882/1055-keV 线属于 yrare 序列；原文Fig.4标注 δ1055=0.1(2)，正文描述 approximately zero，旧0.00(2)撤回。两个 17/2− 态是 yrast/yrare，不能直接改称 favored/unfavored 带间交错；作者明确说 yrast 比值约为模型两倍。撤回“全部 M1>99.2%”“精确吻合”“黄金零对照”和由 γ-soft 势推出必然色散/无 wobbling 的旧断言。原文未给出该条声称的 S(4,3,2)=-0.642 或此动力学证明；保留作者的低 E2 / signature-partner 解释层，不扩展为普适排他结论。 | correction-and-evidence-boundary | source-rechecked | C23-D28-2; C23-D28-3; C23-D28-4 | true |

## Day28：逐态身份、δ 分支与旧量化断言纠错

覆盖：本轮通读 8 页期刊主文及参考文献；视觉回核 printed `064318-2` Fig.1、`064318-3` Figs.2–3/Table I、`064318-4` Figs.4–6、`064318-7` Fig.11 和模型比较正文。2020 对照仅按 Fig.3、Table I 与 B1(a)/B5 讨论核验，不声称重跑采集数据或 ANGCOR。原文件 SHA-256 保持 frontmatter 值；网络 Crossref、arXiv 和 APS 只核身份/可访问性。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| C23-D28-1 | Sec.III 在约 341-keV 9/2− 态上建立 705/816/930-keV 级联，并明确 816/1055-keV 线先前已报道；2020 B5 已有 1046 与约 1862-keV 成员。2023 新信息包括 882-keV 双线拆分、930/1176-keV 延伸与 835-keV yrast 13/2− 序列，不能将整个低自旋网络称为第二套独立新实验。 | experimental-report-and-lineage | direct | printed 064318-2; Fig.1; printed 064318-3 Sec.III | true |
| C23-D28-2 | Table I 给 794.8 keV、Elevel=1600.9 keV、17/2−→15/2−，Iγ=12.6(2)、RDCO=0.55(1)、Δasym=+0.03(1)；同能量/观测量在 Banik2020 Table I 对应 17/2+→15/2− E1 标签。2023 新增 766.5-keV 17/2−→13/2− 与 670.6-keV 13/2−→11/2− 连接；需要记录 quantum-label 修订，不能静默合并 E1/M1。 | experimental-report-and-version-boundary | direct | Table I, printed 064318-3; Fig.1 | true |
| C23-D28-3 | Fig.5 标注 δ671=0.03(3)、δ882=0.09(8)；对应曲线与 RDCO 色带在负 δ 区还有交点，因此小解标注不等于 RDCO 单独给出全局唯一解。671-keV 的 Δasym=-0.03(5)，882-keV 偏振栏为空。Fig.4左图明确标注 δ1055=0.1(2)，正文称 approximately zero，右图引用1983年独立角分布作比较；旧0.00(2)不是该印刷标注。本轮初稿漏读图内0.1(2)，已在放大视觉核验后纠正，不保留“仅有近零描述、没有数值误差”的说法。 | experimental-report-and-figure-audit | direct-figure-and-text | Figs.4–5, printed 064318-4; Table I | true |
| C23-D28-4 | 作者给 yrare 17/2− 实验 B(M1)/B(E2)=1.27(14)、模型1.27；另给 yrast 17/2− 实验2.54(4)，明确为模型约两倍。模型 δTPRM=-0.69 不是实验 δ≈0；按 δ²/(1+δ²) 得模型 E2 photon fraction≈32.25%，不能把“low”改写成纯 M1 或与实验逐项精确一致。作者仍将 yrast 13/2− 起源列为开放问题。 | experimental-report-and-model-boundary | direct-and-derived | printed 064318-6; printed 064318-7 before Summary; Fig.11 | true |
| C23-D28-5 | 按 Table I 印刷数字直接作 Eparent−Edaughter−Eγ，1055.1-keV 线得到 +0.8 keV，929.7-keV 线得到 +0.5 keV；这是印刷表的算术残差，非重新拟合或实验错误判决。表注称能级经拟合且旧线部分观测量采用Ref22，缺少联合能量协方差，不能给 χ²/显著性或擅改能量。 | derived-observable-and-readiness-boundary | derived-from-printed-table | Table I, printed 064318-3 | true |
| C23-D28-6 | 用Table I的1055.1/815.6-keV线、强度6.0(2)/1.0(1)，加上Fig.4实际小解δ=0.1(2)，标准同母态公式κ=0.697得B(M1)/B(E2)≈1.27224；仅作强度与δ独立的一阶传播得σ≈0.1433，与作者1.27(14)相容。该表图重算未恢复原始联合likelihood或全部效率系统误差，不算独立实验。 | derived-observable | derived-from-printed-table-and-figure | Table I; Fig.4; printed 064318-6 | true |
| C23-D28-7 | Fig.11最右TPRM列采用ε2=0.13、γ=33°，其17/2−→13/2−、17/2−→15/2−图示跃迁能量分别为799、902 keV；实验列相应为816、1055 keV。正文给模型B(M1)/B(E2)=1.27及对应δTPRM=−0.69，但该段未说明计算δ采用实测还是模型Eγ。不能将模型δ直接代入实测光子强度，再把所得商叫作作者模型预测。 | model-input-convention-boundary | direct-figure-and-text | Fig.11; printed 064318-6 final paragraph; printed 064318-7 first paragraph | true |
| C23-D28-8 | Table I没有单独的多极性列；794.8-keV行的量子标签为17/2−→15/2−，已知线的部分强度/DCO/偏振采用Ref22。766.5-keV行有RDCO=1.15(20)、Iγ≈1.8，但偏振栏为空；正文的quadrupole指认及766门的671/795符合关系不能单独构成该线electric-versus-magnetic性质的重新测定。 | experimental-report-and-parity-readiness | direct-and-inference-boundary | Table I; Fig.3; printed 064318-3 Sec.III | true |
| C23-D28-9 | 881.8-keV线的Table I观测为RDCO=0.64(11)，偏振栏为空；Fig.5的小解δ=0.09(8)之外，曲线与RDCO带在负δ区仍有第二交点。要区分这些分支，必须保留881.8/880.1双线污染、实际门和角对、取向/feeding、成对响应、偏振校准及联合协方差；671的异母态asymmetry和1055的另一跃迁AD不能直接迁移为882的分支裁决。没有这些输入，本轮不报告另一根、权重或显著性。 | response-contract-and-branch-boundary | direct-and-derived-design | Table I, printed 064318-3; Fig.5, printed 064318-4 | true |
| C23-D28-10 | arXiv源文件和期刊Fig.11/TPRM段落直接支持模型骨架 `H=Hcore+Hsp+Hpair`、`ε2=0.13`、`γ=33°`、`ξ=1`，并明确出带 `17/2−→15/2−` 的模型/实验能量为902/1055.1 keV、带内 `17/2−→13/2−` 为799/815.6 keV；公开材料没有给出E2/M1算符、有效电荷、g因子、淬灭或`δTPRM=-0.69`的确切能量输入约定。`B(M1)/B(E2)=1.27`与δ涉及不同强度商，不能仅由两者反推能量。 | model-convention-source-boundary | direct-primary-and-derived-boundary | arXiv `131Xe.tex:265-275`; Fig.11; printed 064318-6/7 | true |

**Knowledge Impact and Learning Decision — revises / limits。** 保留原作者偏好 yrare signature partner、未见 wobbling 信号的有界解释；修正旧强断言与对象混淆。完整逐态对照、可复算公式、反证和 response 缺口由 [[131xe-low-spin-partner-crosswalk]] 承接。本轮没有新增人审事件，没有改 C23-1 至 C23-7 的历史审核字段。
