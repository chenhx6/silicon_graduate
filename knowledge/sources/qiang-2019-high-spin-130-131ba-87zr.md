---
type: source
title: "强赟华 2019 博士论文：130,131Ba 高自旋态及 87Zr 低位能级寿命"
aliases: [强赟华2019博士论文, Qiang Yunhua 2019 Ba Zr thesis]
created: 2026-09-05
updated: 2026-09-05
status: ai-draft
review_status: unreviewed
source_type: phd-thesis-experiment
reading_depth: deep-read
title_original: "Study of high spin states in 130,131Ba and lifetime measurement of low-lying states in 87Zr"
authors: [强赟华]
advisor: [刘翔, 周小红]
journal: "兰州大学博士学位论文"
year: 2019
volume:
pages: 92
doi:
arxiv:
language: zh
canonical_source: "强赟华. 130,131Ba高自旋态研究及87Zr低位能级寿命测量[D]. 兰州大学, 2019."
zotero_item_key:
citation_key: ""
zotero_uri:
library_file: "raw/papers/degree dissertation/A强赟华博士论文-兰大.pdf"
raw_file: "raw/papers/degree dissertation/A强赟华博士论文-兰大.pdf"
raw_sha256: "CCFAEFF6D5A86C308440ACC218391070C46290C6133FA7104FE83ECE11E73EBF"
nuclei: [130ba, 131ba, 87zr]
reactions: ["122Sn(13C,xn)130,131Ba", "87Nb beta-plus decay to 87Zr"]
experiments: [galileo-131ba-c13-65mev]
models: [cranked-shell-model, particle-rotor-model, shell-model]
observables: [angular-correlation, g-factor, lifetime, bm1-be2-ratio, signature-splitting]
methods: [gamma-gamma-coincidence, gamma-gamma-gamma-coincidence, beta-gamma-delayed-coincidence]
tags: [a130, high-spin, barium-isotopes, chiral-doublet-bands, k-isomer, t-band, lifetime, phd-thesis]
---

# 强赟华 2019：`130,131Ba` 高自旋态及 `87Zr` 低位能级寿命

## Bibliographic Record

强赟华，*Study of high spin states in 130,131Ba and lifetime measurement of low-lying states in 87Zr*，兰州大学博士学位论文，2019，92 页。原始 PDF SHA-256 为 `CCFAEFF6D5A86C308440ACC218391070C46290C6133FA7104FE83ECE11E73EBF`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: 摘要、目录、第 2–5 章理论/实验/数据处理、第 5 章 `130,131Ba` 结果与讨论，以及第 6 章总结；核对 K-isomer、t-band、S-band、MχD、E1 关联、角关联、g 因子和 `87Zr` 寿命结果。
- Not covered: 底层电子学线路的逐元件复现、未列入论文主线的全部参考文献原文。
- Coverage caveats: `130,131Ba` 的组态和形变多依赖系统学、推转壳模型或粒子-转子模型；并非全部为直接形变测量。

## Paper Question and Scientific Motivation

作者希望扩展 `130,131Ba` 的高自旋能级纲图，检验 `N=74/75` 同中子素中的 K-isomer、带交叉、t-band、S-band 与手征双重带系统学，并用 `87Zr` 低位寿命检验奇 A/偶偶核芯的集体性（Abstract；Chapters 1 and 6）。

## Method and Design Logic

`122Sn(13C,xn)` 在 65 MeV 下布居 `130,131Ba`，用 GALILEO、EUCLIDES 和 Neutron Wall 记录 γγγ 与粒子-γ 符合；`87Zr` 由 `87Nb` β+ 衰变布居，以 β-γ 延迟符合测量寿命（Abstract；Chapter 3）。能级纲图先由符合、角关联和分支建立，再用 CSM、粒子-转子模型和壳模型进行组态解释（Chapters 4–5）。

## Key Evidence and Reasoning Chain

1. 符合关系扩展 `130,131Ba` 能级纲图并提供候选带结构（Ch.5）。
2. 分支比、混合比和角关联约束 K-isomer 带及部分跃迁多极性（Ch.5.1–5.2）。
3. alignment、signature splitting 与邻核系统学用于组态映射（Ch.5.1–5.2）。
4. β-γ 延迟符合给出 `87Zr` 第一激发态寿命，再转换为 `B(E2)`/`B(M1)`（Ch.5.3）。
5. MχD、t-band 和形变结论由实验结构与模型比较联合支持，不能脱离模型写成直接形状观测。

## Summary

论文报告 `130Ba` 的 Kπ=8− 同核异能态带、Kπ=8+ t-band、两个 S-band、负宇称带和四准粒子带；报告 `131Ba` 共 19 条带，其中 9 条为本工作新识别，并提出一对负宇称、两对正宇称 MχD 及正负宇称之间的 E1 八极关联。`87Zr` 的 `7/2+` 第一激发态寿命测为 `1017(16) ps`。这些结果为 A≈130 的形变、组态和手征候选提供了高信息量来源，但关键解释仍需保留模型依赖和竞争解释。

## Experimental or Theoretical Setup

- `122Sn(13C,5n)130Ba` 与 `122Sn(13C,4n)131Ba`，束流能量 65 MeV。
- GALILEO + EUCLIDES + Neutron Wall；源论文将该装置与 `131Ba` 的既有实验页关联，但 `130Ba` 5n 通道需在后续实验页中单独标明。
- `87Nb` β+ 衰变与 SHANS/β-γ 延迟符合寿命测量。
- CSM、粒子-转子模型、壳模型；gK/gR、signature splitting、E1 links、lifetime 和 `B(E2)` 为主要观测/派生量。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | source_independence | locator | needs_review |
|---|---|---|---|---|---|---|
| QY19-1 | 65 MeV `13C` + `122Sn` 反应和 GALILEO/EUCLIDES/Neutron Wall 符合测量显著扩展了 `130,131Ba` 的高自旋纲图。 | experimental-fact | direct | multiple-dependent | Abstract；Ch.3；Ch.5 | true |
| QY19-2 | `130Ba` 中首次观察到建立在 Kπ=8−、T1/2=9.5 ms 同核异能态上的转动结构；分支/混合比提取的 gK、gR 与 `ν7/2+[404]⊗9/2−[514]` 预期相容。 | experimental-fact + author-interpretation | direct | multiple-dependent | Abstract；Ch.5.1；Ch.6 pp.75–76 | true |
| QY19-3 | 建立在 `130Ba` 8+、2979 keV 能级上的带被作者解释为 A≈130 首例 t-band，候选组态为 `ν7/2−[523]⊗9/2−[514]`。 | author-interpretation | indirect | multiple-dependent | Ch.5.1；Ch.6 p.75 | true |
| QY19-4 | `130Ba` 两个 S-band 的大 signature splitting 被作者用于区分质子长椭与中子扁椭激发，并报告四准粒子带和负宇称带。 | author-interpretation | indirect | multiple-dependent | Abstract；Ch.5.1；Ch.6 | true |
| QY19-5 | `131Ba` 观察到 19 条转动带、其中 9 条新建；作者提出一对负宇称和两对正宇称 MχD。 | experimental-fact + author-interpretation | direct | multiple-dependent | Abstract；Ch.5.2；Ch.6 p.75 | true |
| QY19-6 | `131Ba` 正负宇称带之间的 E1 跃迁被作者解释为八极关联；带 3–6 的近简并还被提出可能涉及赝自旋与手征的共同破缺。 | experimental-criterion + author-interpretation | indirect | multiple-dependent | Ch.5.2；Ch.6 p.75 | true |
| QY19-7 | `87Zr` 第一激发态 `7/2+` 的寿命为 `1017(16) ps`，由此得到的 `B(E2;7/2+→9/2+)` 与 `N=47` 系统学和 `86Zr` 核芯集体性相近。 | experimental-fact | direct | single | Abstract；Ch.5.3；Ch.6 p.76 | true |
| QY19-8 | `130Ba`/`131Ba` 的组态、形变和 MχD 结论依赖角关联、分支、邻核系统学及模型；不能仅凭本论文宣称直接测得 γ 形状或已证明手征。 | analytical-boundary | inferred | multiple-dependent | Ch.5–6；缺少绝对形变/完整矩阵元 | true |

## Nuclear Structure Information

- `130Ba`：Kπ=8− isomer band、8+ t-band、两个 S-band、负宇称和四准粒子候选。
- `131Ba`：19 条带、MχD 候选和跨宇称 E1 network；与现有 GALILEO `131Ba` 来源属于同一实验谱系，不能重复计为独立数据集。
- `87Zr`：低位 `7/2+` 寿命和奇 A/偶偶核芯集体性比较。

## Authors' Interpretation

作者以 alignment、signature splitting、分支/混合比、邻核系统学与 CSM/粒子-转子模型联合解释 t-band、S-band、K-mixing、MχD 和八极关联。MχD 与 t-band 均应保留为作者解释/模型支持层。

## Model Results

- Kπ=8− 组态与 gK/gR 的粒子-转子模型比较。
- `130Ba` t-band 和 S-band 的组态、长椭/扁椭形变解释来自 CSM/系统学。
- `131Ba` 带的 MχD、赝自旋与八极关联依赖邻核和模型映射。
- `87Zr` 的 `B(E2)` 趋势在壳模型框架下作定性解释。

## Competing Interpretations and Limitations

- MχD 的近简并、共同组态和 E1 关联不足以单独证明静态手征或稳定八极形变；需 absolute strengths、lifetime、偏振和几何信息。
- t-band 的“倾斜轴顺排”是作者的结构解释，不能与直接测得的三轴形变混同。
- `87Zr` 的集体性结论是寿命到 `B(E2)` 的模型辅助转换，需核对分支、寿命定义和误差传播。
- 该论文与 Guo 2020、Ding 2021 共用/复用 GALILEO `131Ba` 实验谱系；后续证据计数标为 `multiple-dependent`。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-QY19-1 | Core reconstruction | 来源最强贡献是将 `130Ba` 的 K-isomer/t/S-band 与 `131Ba` MχD 放入同一 A≈130 实验谱学框架。 | Ch.5–6 | unreviewed |
| AR-QY19-2 | Assumptions and dependencies | 组态和形变依赖 systematics、CSM/PRM；MχD 依赖 shared GALILEO data lineage。 | Ch.5.1–5.2 | unreviewed |
| AR-QY19-3 | Transfer conditions | 可用于 A≈130 带结构、signature 和 E1/手征候选比较，不可直接外推 γ-rigid 或 stable octupole。 | QY19-4–8 | unreviewed |
| AR-QY19-4 | Failure conditions | 若原始 branching、偏振或绝对矩阵元不支持共同组态，MχD/t-band 排序需降级。 | Ch.5；缺少 observables | unreviewed |
| AR-QY19-5 | Reverse/falsification test | 对 MχD 检查 partner-band absolute strengths、E1/E2 ratios、lifetimes 和 angular-momentum geometry。 | Ch.5.2；existing MχD evidence map | unreviewed |
| AR-QY19-6 | Research-question decision | 接入 A≈130 collective-mode evidence map，重点区分 K-mixing、t-band、chirality 与 octupole correlation。 | QY19-3–6 | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: 已有 `131Ba` 的 GALILEO MχD/赝自旋来源，但缺少同一论文对 `130Ba` K-isomer/t/S-band 和 `87Zr` lifetime 的完整串联。
- Effect of this source: supports and extends；同时 limits 对 MχD、t-band 和形变结论的证据强度。
- Reason: 增加 A≈130 的 K-isomer、t-band、MχD、E1 与寿命证据，并明确共享实验依赖。
- Persistence decision: 新建 source；更新 `131Ba` 来源关系；`130Ba`/`87Zr` 是否建立独立核素页留待内容核对后最小化决定。
- Review state: 页面 `unreviewed`；QY19-2、QY19-3、QY19-5、QY19-6、QY19-7 保留 claim-level review。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[131ba]] | 提供同一 GALILEO `131Ba` 实验谱系的博士论文层证据。 |
| competing-interpretation | [[nuclear-chirality-and-multiple-chiral-doublet-bands]] | MχD 与 E1 八极关联是作者候选解释，需与已有 `131Ba`/`78Br` 证据分层。 |
| methodological-bridge | [[angular-correlation]] | 以角关联、分支比和混合比约束带结构与多极性。 |
| competing-interpretation | [[wobbling-vs-signature-partner]] | t-band/signature splitting 不能自动转译为 wobbling。 |

## Human Review Triage

### P0

- QY19-5/QY19-6：核对 `131Ba` 一负两正 MχD 的带号、E1 links、跃迁方向和“八极关联”措辞；风险是把作者候选解释写成已证实手征/八极形变。
- QY19-3：核对 `130Ba` 8+、2979 keV t-band 的带头、组态和“首例”范围；风险是把 t-band 模型解释误写成直接形变事实。

### P1

- QY19-2：复核 Kπ=8− isomer 半衰期、gK/gR、Nilsson 组态和误差。
- QY19-7：复核 `87Zr` 1017(16) ps 及 `B(E2)/B(M1)` 转换、分支和误差传播。
- QY19-8：与 Guo 2020、Ding 2021 做 shared-dataset independence audit。

### P2/P3

- 补齐 `130Ba`/`87Zr` 的轻量核素入口和 citation key；不改变 claim 状态。

## Extracted Pages

- Nuclei: [[131ba]]；`130Ba`、`87Zr` 暂不机械新建。
- Bands: Kπ=8−、t-band、S-band 和 MχD 先保留在 source 内。
- Experiments: [[galileo-131ba-c13-65mev]]（共享装置/谱系）。
- Concepts/observables: [[nuclear-chirality]], [[multiple-chiral-doublet-bands]], [[signature-splitting]], [[angular-correlation]], [[g-factor-measurement]], [[lifetime]]。

## Non-source Notes and Follow-up

本论文是 `131Ba` GALILEO 数据的博士论文层复述/扩展，后续计数不得与 `guo-2020-pseudospin-chiral-quartet-131ba`、`ding-2021-131ba-133ce-signature-splitting` 当作独立实验重复加权。
