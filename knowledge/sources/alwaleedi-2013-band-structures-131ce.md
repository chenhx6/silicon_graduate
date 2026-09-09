---
type: source
title: Band Structures of 131Ce
aliases: [Alwaleedi 2013 131Ce thesis]
created: 2026-07-27
updated: 2026-09-05
status: active
review_status: unreviewed
source_type: phd-thesis-experiment
reading_depth: deep-read
title_original: Band Structures of 131Ce
authors: [Mohammed Abdullah Alwaleedi]
journal:
year: 2013
volume:
pages: 97
doi: 10.17638/00015073
arxiv:
language: en
canonical_source: doi:10.17638/00015073
zotero_item_key:
citation_key: mohammedabdullahalwaleedi_2013_Bandstructures
zotero_uri:
library_file:
raw_file: raw/papers/degree dissertation/Band structures of 131Ce.pdf
raw_sha256: B50C22877418DE560F06002588BB46D34F5BA670C6880E30A89D1509C79AD8C1
nuclei: [131ce]
reactions: [100Mo(36S,5n)131Ce]
experiments: [atlas-gammasphere-131ce-s36-165mev]
models: [cranked-shell-model, woods-saxon-model]
observables: [angular-intensity-ratio, bm1-be2-ratio, moments-of-inertia, signature-splitting]
methods: [gamma-gamma-coincidence, angular-distribution]
tags: [a130, high-spin, band-crossing, configuration-assignment, phd-thesis]
---

# Alwaleedi 2013: Band Structures of 131Ce

## Bibliographic Record

Mohammed Abdullah Alwaleedi，*Band Structures of 131Ce*，University of Liverpool / Oliver Lodge Laboratory，博士学位论文，2013，97 页，DOI `10.17638/00015073`。引用键为 mohammedabdullahalwaleedi_2013_Bandstructures。原始 PDF SHA-256 为 B50C22877418DE560F06002588BB46D34F5BA670C6880E30A89D1509C79AD8C1。

## Scope and Reading Depth

- Completed reading_depth: deep-read。
- Covered scope: 全文 97 页；实验与 angular intensity ratio 方法；Figure 4.1、Tables 4.1–4.7；crossings、alignments、configuration assignments、Tables 5.1–5.4、Figure 5.5 和 B(M1)/B(E2) 推导。
- Coverage caveat: 当前环境缺少 PyMuPDF，标准 preparation bundle 未成功生成；采用 chapter/section/figure/table/equation locator，关键实验页、Figure 4.1 和 Table 5.3 已由 Poppler 渲染并视觉复核。
- Not covered: 本数据集没有寿命、绝对 B(E2)、线偏振或直接形变测量。
- 2026-09-05 re-read: 复核 Abstract、Chapter 4 Figure 4.1/Tables 4.1–4.7、Chapter 5 Tables 5.1–5.4/Figure 5.5；确认 Bands 1–7、`δ=0`、Band 2 parity conflict 和 Band 5 duplicated `e⊗AEFG` mapping 与现有 source 记录一致，未发现需要改变 claim wording 的新证据。

## Paper Question and Scientific Motivation

论文旨在扩展 131Ce 高自旋能级纲图，并用 alignment、band crossing、准粒子 Routhian 和跃迁分支比解释各带组态及随转动频率发生的结构变化（Abstract；Chapters 4–5）。

## Method and Design Logic

通过 100Mo(36S,5nγ)131Ce 反应布居高自旋态，以 Gammasphere 多重 γ–γ 符合建立和扩展能级纲图；angular intensity ratios 约束跃迁多极性及自旋宇称；随后比较实验 alignment、crossing frequency、Woods–Saxon/准粒子图和半经典 B(M1)/B(E2) 计算，形成组态指认（Chapters 3–5）。

## Key Evidence and Reasoning Chain

1. 符合关系与相对强度建立 Bands 1–7 和 linking transitions（Figure 4.1；Tables 4.1–4.7）。
2. angular intensity ratios 支持主要跃迁的 dipole/quadrupole 分类，从而约束 spin/parity（Chapter 3；Chapter 4 tables）。
3. crossing frequencies 与 alignment gains 对照准粒子轨道，缩小可能组态（Figures 5.1–5.4；Tables 5.1–5.3）。
4. 假定 δ=0 后由分支强度计算实验 B(M1)/B(E2)，再与半经典模型比较（Equations 5.6–5.7；Table 5.4；Figure 5.5）。
5. 组态和形变结论是实验谱学与模型比较的联合解释，不是直接形变测量。

## Summary

论文报告两条新的强耦合带 Bands 4 和 7，并扩展既有 Bands 1、2、6。作者用若干中子 Nilsson 轨道与质子、中子对齐组态解释 Bands 1–7，并用 spin-dependent core polarization/non-axial deformation 讨论 crossing 后的结构。证据最直接支持 signature/configuration coupling、准粒子 crossing 和组态依赖的转动响应；不足以单独确立 wobbling、chirality 或 shape coexistence。

## Experimental or Theoretical Setup

- 165 MeV 36S 束流，平均束流强度约 5 pnA，由 ATLAS 提供。
- 两张富集 100Mo 靶，每张约 600 µg/cm²。
- Gammasphere 使用 101 个 Compton-suppressed HPGe 探测器。
- 共记录约 `3×10^9` 个 fold ≥7 的 prompt γ coincidence events。
- 数据整理为符合矩阵/立方体和用于 angular intensity ratios 的角度分组谱。
- Woods–Saxon/TRS 讨论采用 β2=0.218、β4=-0.023、γ=0°；这些是模型输入/极小值，不是实验直接测得的形变。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AW13-1 | 新建立强耦合 Bands 4 和 7，并扩展 Bands 1、2、6；完整关系见 Bands 1–7 能级纲图。 | observed-fact | direct | Abstract; Chapter 4; Figure 4.1; Tables 4.1–4.7 | true |
| AW13-2 | Band 1 被扩展到更高自旋，并通过新连接跃迁与 Band 4 建立结构关系。 | experimental-assignment | direct | Chapter 4, Bands 1 and 4; Figure 4.1 | true |
| AW13-3 | Band 2 的正宇称序列被扩展，作者用 alignment 与 crossing 行为讨论低-j 正宇称中子轨道。Figure 4.1、Tables 4.5–4.6 和 Section 5.2.2 相互一致。 | experimental-assignment | direct | Figure 4.1; Tables 4.5–4.6; Section 5.2.2 | true |
| AW13-4 | 作者把 Band 4 指认为与 γ 振动耦合的 e/f 序列，把 Band 7 指认为 a/b⊗AE；这是组态解释。 | author-interpretation | direct | Chapter 5; Table 5.3 | true |
| AW13-5 | Table 5.1 给出 Band 1 两个 signature 的 crossing frequencies 0.329、0.367 MeV/ℏ，Band 2 两个 signature 均为 0.316 MeV/ℏ。 | model-assisted-measurement | direct | Table 5.1 | true |
| AW13-6 | Woods–Saxon/TRS 计算采用或得到 β2=0.218、β4=-0.023、γ=0° 的轴对称形变背景。 | model-result | direct | Chapter 5, Woods–Saxon/TRS discussion | true |
| AW13-7 | 作者认为 alignment 后行为提示 spin-dependent core polarization，并允许非轴形变在更高自旋处变得重要。 | author-interpretation | direct | Chapter 5, crossing/alignment discussion | true |
| AW13-8 | Table 5.3 将 Bands 1–7 映射为 e/f⊗EF、a/b⊗EF、c/d、γ⊗e/f、e/f⊗AE(→AEFG)、efg/feh 和 a/b⊗AE 等组态。 | author-interpretation | direct | Table 5.3 | true |
| AW13-9 | 实验 B(M1)/B(E2) 由分支强度和 γ 能量计算，并明确假定 E2/M1 mixing ratio δ=0；不是绝对 B(M1) 或 B(E2)。对同一分支数据，`R(δ)=R(0)/(1+δ²)`。 | derived-observable | direct | Equations 5.6–5.7; Section 5.3; Table 5.4 | true |
| AW13-10 | 作者认为 Figure 5.5 中实验与半经典理论比值的总体一致性加强了组态指认。 | author-interpretation | direct | Figure 5.5 and discussion | true |
| AW13-11 | 本数据集没有寿命、绝对 B(E2)、线偏振或直接 γ 刚性测量，不能仅凭本论文裁决 wobbling、chirality、shape coexistence 或 γ-soft/γ-rigid。 | analytical-boundary | inferred | Dataset/method inventory across Chapters 3–5 | true |
| AW13-12 | Table 5.3 排版原文把 Band 5 两个 signature 分量的高自旋端都写成 `e⊗AEFG`：`e⊗AE → e⊗AEFG` 与 `f⊗AE → e⊗AEFG`；180 dpi 页面视觉复核确认这不是文本提取误差。 | observed-fact | direct | Table 5.3, thesis p.80 | false |
| AW13-13 | 2026-08-11 用户审核决定按 Table 5.3 原文保留上述两条映射，不以 signature 连续性把第二行改写为 `f⊗AEFG`。重复的高自旋 `e⊗AEFG` 标签在物理上如何对应两个低自旋 signature 分量仍未解决，需独立来源或作者勘误才能重映射。 | analytical-boundary | inferred | Table 5.2; Table 5.3; Section 5.2.2 Band 5; user review 2026-08-11 | false |

## Nuclear Structure Information

- Bands 1–7 的来源编号只在本论文语境中使用；与其它 131Ce 文献对齐时必须依赖 bandhead、parity、signature、linking transitions 和组态，不能只按编号合并。
- Band 1 与 Band 4 围绕负宇称 νh11/2 类轨道及其耦合展开；Band 2 与 Band 7 涉及正宇称低-j 中子轨道和对齐质子对。
- crossing frequency 与 alignment 是组态约束量，但模型轨道标签和形变依赖 Woods–Saxon 参数化。

### Working parity map

用户依据 Figure 4.1 提出本轮 provisional working assignment：Bands 2、3、5 为正宇称，Bands 1、4、6、7 为负宇称。该判断已与 Figure 4.1、Tables 4.1–4.7 及 Chapter 5 的带讨论交叉核验，整体一致；它是 claim-level 人工判断，不把整页升级为 `human-reviewed`。Table 5.1 中 Band 2 的负宇称单元仍按原样保留为来源内部冲突。

## Authors' Interpretation

作者用强耦合 Nilsson 轨道、质子/中子对齐和 core polarization 统一解释 Bands 1–7，并认为更高自旋处可能需要非轴形变。论文没有把这些带正式指认为 wobbling 或 chiral partners。

## Model Results

- Table 5.2 给出中子 a/b=[404]7/2+ (g7/2)、e/f=[514]9/2− (h11/2)、g/h=[541]1/2− (h9/2)，以及质子 A/B=[413]5/2+ (g7/2)、E/F=[550]1/2− (h11/2)。
- Table 5.3 的 band-configuration map 是作者综合 alignment、crossing 和 Routhian 比较后的指认。
- Table 5.4 与 Figure 5.5 的 B(M1)/B(E2) 比较依赖 g factors、alignment 参数和 δ=0 假设。

## Competing Interpretations and Limitations

- Table 5.1 原表把 Band 2 标为负宇称，而 Figure 4.1、Tables 4.5–4.6 和 Section 5.2.2 均支持正宇称；当前分类为来源内部冲突、`probable typo`。原表记录不得改写，crossing frequency 可用，但该 parity 单元不用于正式宇称结论。
- Band 5 的 Table 5.3 原文给出 `e⊗AE → e⊗AEFG` 与 `f⊗AE → e⊗AEFG`；页面视觉复核已排除 OCR/文本提取误差。2026-08-11 用户审核决定忠实保留这两条映射，不引入 `f⊗AEFG` 修正；重复高自旋标签与 signature 连续性之间的张力保持为未解决来源边界。
- B(M1)/B(E2) 必须始终携带 δ=0 假设。由 Equations 5.6–5.7，`R(δ)=R(0)/(1+δ²)`；若 `|δ|≤0.5`，δ=0 结果相对真实值最多高估 25%，而两者差值相对 δ=0 结果最多为 20%。δ 的符号不改变这项幅值修正，但仍影响偏振和相位判断。
- 轴对称 TRS 极小值和高自旋非轴 core polarization 不等价于已经测得 γ-soft 或 rigid-triaxial 势面。
- 近简并、signature splitting 或相似 alignment 可由普通 signature partners、组态混合、粒子—芯耦合及不同集体模式产生，需要额外电磁和形变 observable 区分。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-1 | Core reconstruction | 最稳健的重构是组态耦合与准粒子 crossing 的谱学地图，不是某种新集体模式的发现。 | Figure 4.1; Tables 5.1–5.3 | unreviewed |
| AR-2 | Assumptions and dependencies | 组态依赖 Woods–Saxon/TRS 和 alignment；跃迁比依赖 δ=0 及半经典参数。 | Equations 5.6–5.7; Tables 5.2–5.4 | unreviewed |
| AR-3 | Transfer conditions | 可作 131Ce 后续研究的纲图基线，但跨论文 band identity 必须重新映射。 | Figure 4.1 and band text | unreviewed |
| AR-4 | Failure conditions | 若寿命、偏振或 mixing ratio 显示不同电磁性质，现有解释排序应改变。 | Missing-observable inventory | unreviewed |
| AR-5 | Reverse/falsification test | 用绝对/相对跃迁强度、偏振、精确 δ 和形变敏感量检验竞争解释。 | Chapter 5 limits; AW13-9–11 | unreviewed |
| AR-6 | Research-question decision | 进入 L3：与 133Ce 及必要邻核对照，寻找裁决集体模式的最小 observable 集。 | AW13-11; A≈130 projects | active-L3 |
| AR-7 | Band 5 signature-preserving reconstruction | withdrawn：Agent 曾依据 signature 连续性提出把第二行重构为 `f⊗AEFG`；2026-08-11 用户审核要求按原表 `f⊗AE → e⊗AEFG` 使用，因此该重构不再作为 working mapping。只有独立来源或作者勘误才能重新开启标签修正。 | Tables 5.2–5.3; Section 5.2.2 Band 5; user review 2026-08-11 | withdrawn-by-human-review |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: 133Ce 和邻近 A≈130 核中，γ-softness、signature splitting、chirality 与 wobbling 存在竞争解释。
- Effect of this source: supports and limits。
- Reason: 补全 131Ce 的实验带结构与组态基线，同时暴露电磁跃迁和形变判据缺口。
- Persistence decision: 新建 source、nucleus、experiment 页面并进入 L3 project；不机械为 Bands 1–7 全部建页。
- Review state: 页面整体仍为 `unreviewed`；2026-08-11 用户仅完成 AW13-12/AW13-13 的 claim-level review。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| foundational-background | [[131ce]] | 提供 131Ce 的结构基线。 |
| methodological-bridge | [[bm1-be2-ratio]] | 展示由 branching ratios 推导比值时 δ=0 的关键假设。 |
| competing-interpretation | [[wobbling-vs-signature-partner]] | 能谱和组态证据优先支持普通 signature/configuration coupling，未提供 wobbling 所需带间 E2 证据。 |
| limits | [[gamma-soft-vs-gamma-rigid-diagnostics]] | TRS 形变点不能单独裁决 γ 势的刚/软性质。 |

## Human Review Triage

### P0

- AW13-5：Table 5.1 的 Band 2 宇称与 Figure 4.1、Tables 4.5–4.6 及 Section 5.2.2 不一致。视觉复核后降级为 `probable typo`，但保留原始冲突并隔离该 parity 单元；crossing 数值仍可按来源使用。

### P1

- AW13-9：后续引用 B(M1)/B(E2) 时必须携带 δ=0 假设和 `R(δ)=R(0)/(1+δ²)`；`|δ|≤0.5` 的 25%/20% 是两种不同分母的误差口径，不得与 ICC 反演文献中约 25% 的实验误差混同。
- AW13-11：将寿命/绝对 B(E2)、mixing ratio/偏振和形变敏感量作为 L3 裁决 observable。
- AW13-12/AW13-13：2026-08-11 claim-level review 已完成。按原表保留 `e⊗AE → e⊗AEFG` 与 `f⊗AE → e⊗AEFG`，撤回 `f⊗AEFG` reconstruction；标签的物理连续性问题留待独立来源。

### P2/P3

- 校对学校/实验室在最终 BibTeX 导出中的字段组织；source 页已保存重建引用所需的核心元数据。

## Human Review Notes

### 2026-08-11 — Band 5 Table 5.3 mapping

- 用户要求忠实采用原表的 `e⊗AE → e⊗AEFG` 与 `f⊗AE → e⊗AEFG`。
- 用户未接受把第二行改写成 `f⊗AEFG`；该 Agent reconstruction 已撤回。
- 本轮只审核 AW13-12/AW13-13，不升级 source 页面整体状态，也不处理其它 claim-level `needs_review`。

## Human Review Record

- 2026-08-11：AW13-12/AW13-13 claim-level review 完成；原表映射获确认，signature-preserving reconstruction 被撤回。

## Extracted Pages

- Nuclei: [[131ce]]
- Bands: 本轮不拆分；先以来源编号和 bandhead/组态映射保持身份边界。
- Experiments: [[atlas-gammasphere-131ce-s36-165mev]]
- Concepts/observables: [[signature-splitting]], [[bm1-be2-ratio]], [[moments-of-inertia]]

## Non-source Notes and Follow-up

L3 pilot 将独立保存跨来源推理；本页不把后来形成的 wobbling/chirality 分类倒灌为论文作者主张。2026-09-05 复读属于本批次温故知新，不改变页面级 `review_status` 或既有 claim-level 状态。
