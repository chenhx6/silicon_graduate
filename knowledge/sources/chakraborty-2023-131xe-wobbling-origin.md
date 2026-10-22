---
type: source
title: "Search for the origin of wobbling motion in the A≈130 region: The case of 131Xe"
aliases: []
created: 2026-07-01
updated: 2026-07-16
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

Physical Review C 107, 064318 (2023)，DOI `10.1103/PhysRevC.107.064318`。本地 PDF 为 8 页 arXiv 版本。

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

This source is page-level `human-reviewed`; `C23-1..C23-7` remain `needs_review: false`. Paper-level reuse must still return to the cited transition and model-comparison locators and does not turn TPRM/TPSM agreement into an independent observation.

## Personal Notes

这篇文献非常适合做“反证模板”：它并不否定 `131Xe` 三轴性，而是把“存在三轴形变”和“观测到 wobbling”明确拆开。

## Day19量化审计：131Xe纯M1连接线、摇摆零对照基准与软核色散机制

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_xe131_wobbling_null_control_audit.py` 的 9 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/xe131-wobbling-null-control-result-047.json`，系统核准了 Chakraborty 2023（PRC 107, 064318）关于 $^{131}\text{Xe}$ 摇摆模式零对照（Null Control）的量化事实：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| C23-D19-1 | Chakraborty 2023 重新分析 $^{130}\text{Te}(\alpha, 3n\gamma)^{131}\text{Xe}$ 数据，测定 yrare 侧带到 yrast 负宇称带的三条 $\Delta I = 1$ 连接跃迁（671、882、1055 keV）的多极混合比：$\delta = 0.03(3), 0.09(8), 0.00(2)$，其 $E2$ 份额分别仅为 $0.09\%, 0.80\%, 0.00\%$（磁偶极 $M1$ 份额全部超过 $99.2\%$），断然排除了摇摆激发所必须的集体增强 $E2$ 特征（$|\delta| > 1$），确立该带为不利旋称伙伴带（$\alpha = -1/2$）；同时测得 $17/2^-$ 态 $B(M1)/B(E2)$ 比值在有利带与不利带之间呈现 $2.0$ 倍的旋称交错（$2.54 \text{ vs } 1.27\ (\mu_N/e\text{b})^2$），与三轴粒子—转子模型（$\gamma = 33^\circ$）精确吻合。该测量构成了 A≈130 区域判定低自旋摇摆的黄金“零对照基准”：确立了三轴形变（$\gamma \sim 30^\circ$）仅为摇摆出现的必要条件而非充分条件；在偶偶核芯具有平坦 $\gamma$-软势能面（$^{130}\text{Xe}$ 的 $S(4,3,2) = -0.642 < 0$）的物理体系中，弱三轴转动无法提供谐振进动刚度，体系必然色散为常规的单粒子旋称伙伴带。 | quantitative-benchmark-and-criterion | direct-and-derived | PRC 107, 064318 pp.2-8; Table I, Figs.4-5,11; xe131-wobbling-null-control-result-047.json | true |
