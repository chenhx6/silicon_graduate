---
type: project
title: "A≈130 thesis evidence matrix"
aliases: [A130 thesis evidence matrix, A≈130 博士论文证据矩阵]
created: 2026-09-22
updated: 2026-09-23
status: active
review_status: unreviewed
project_stage: seed
confidentiality: private
nuclei: [127i, 128i, 131ce]
tags: [a130, thesis-pipeline, evidence-matrix, collective-modes, durable-learning]
---

# A≈130 thesis evidence matrix

本页是 A≈130 三轴形变与集体激发模式博士论文管线的长期知识资产。它保存可复用的证据矩阵行，不保存每日运行过程；日报和 run receipt 位于 `outputs/learning-daily/`。

## Research Question

哪些 A≈130 能级、跃迁和模式解释已经有可复核的观测支撑，哪些仍需要 mixing ratio、偏振、寿命、绝对跃迁强度或带间连接才能进入博士论文证据链？

## Current Hypotheses

- 能量和符合关系可以稳定约束能级放置，但不能单独确定 `J^π`、组态或集体模式。
- ADO/DCO/偏振、寿命和绝对电磁强度需要组合使用，才能区分 signature/configuration coupling、γ-soft response、wobbling、chirality 和 shape coexistence。
- source lineage 和实验独立性必须与物理证据分开记录。

## Purpose and status

本矩阵用于把“实验直接观测 → assignment handle → 解释边界 → 必要伴随观测 → source lineage”固定下来，供后续 Q&A、L3 研究、综合和论文写作使用。

当前内容来自 Day 1 baseline exercise，属于 Codex self-audit / `unreviewed` 训练资产，不是人工审核后的 claim registry。

## Evidence matrix

| Candidate | Direct observables | Assignment handles | Interpretation boundary | Necessary next observables | Source lineage |
|---|---|---|---|---|---|
| `127I` high-spin scheme | γ energies, coincidence/intensity balance, energy sums, `R_ADO`; Ding thesis Fig. 5.1–5.2 and Tables 5.1 (PDF pp.58–62; printed pp.50–54) | ADO plus sequence/systematics; labels remain source assignments | Energy closure supports placement, not unique `J^π`, configuration, or collective mode; ADO is geometry-specific | transition-level mixing ratio, polarization, lifetimes and absolute `B(E2)/B(M1)` | [[ding-2012-phd-thesis-127-128i-high-spin]]; single Ding experimental lineage |
| `128I` coupled structures | γ placements around the 167.4-keV `(6−)` isomer, `R_ADO`, model comparison; Fig. 6.2 and Tables 6.1, PDF pp.75–81 (printed pp.67–73) | ADO, coincidence, shell-model/NPA comparison | Reversed `6−/7−` ordering and ambiguous `8−` configuration limit a unique structural reading; no clear chiral doublet | conversion coefficients, polarization/mixing ratios, lifetimes and stronger linking constraints | [[ding-2012-phd-thesis-127-128i-high-spin]]; dependent thesis/Wiki derivatives |
| `131Ce` continuity contract | Current Wiki question highlights missing `δ`, polarization, partner-resolved absolute strengths and links | Existing source/project evidence only; no new L3/L4 analysis in Day 1 | Signature/configuration, γ-soft, wobbling, chirality and shape coexistence remain competing explanations | complete transition properties, absolute strengths, linking transitions, and if applicable g-factor/transfer observables | [[131ce-collective-mode-discrimination]]; multiple dependent lineages |

## Evidence Available

当前矩阵行来自 Ding 2012 原始 thesis source、`131Ce` project evidence map 和相关方法页；每行保留直接观测、assignment handle、解释边界、必要观测与 source lineage。矩阵不替代 source/raw locator。

## Risks and Blockers

- thesis/journal/shared-dataset lineages 不能重复计为独立实验；
- ADO 数值依赖阵列几何、alignment、feeding 和效率校准；
- source 页仍可能 `unreviewed` 或 `needs_review`；
- 当前没有用户数据、响应、协方差和代码包，不能进入 L4。

## Decision rule retained

A new line or energy-sum closure may strengthen placement. It cannot by itself promote parity, configuration, triaxiality, wobbling, chirality or shape coexistence. Any future L4 route requires a complete data/response/covariance/code package and the applicable manual gate.

## Next matrix increments

- Add Day 2 shell-gap/orbital evidence while keeping experimental observables separate from model results.
- Add A≈130 source rows only after title/DOI, raw or public-full-text identity, locator and source-independence checks.
- Link each row to at least one nucleus/band page, one method/model page, and one competing source or project where applicable.

## Next Actions

1. 接入 Day 3 的 mean-field/model-choice 证据，但保持模型输出与实验事实分层。
2. 为 `131Ce/133Ce` 补充外部原始文献和必要的 `δ`/偏振/寿命/绝对强度行。
3. 每次扩展前核对 DOI、raw/public-full-text identity、locator 和 source independence。
