---
type: source
title: "Gamma-Ray Linear Polarization and Angular Distribution Formulas in Terms of Phase-Defined Reduced Matrix Elements"
aliases: ["Taras 1971 phase-defined mixing ratios", "Taras polarization angular distribution formulas"]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: theory
reading_depth: deep-read
title_original: "Gamma-Ray Linear Polarization and Angular Distribution Formulas in Terms of Phase-Defined Reduced Matrix Elements"
authors: ["P. Taras"]
journal: "Canadian Journal of Physics"
year: 1971
volume: 49
issue: 3
pages: "328-351"
doi: "10.1139/p71-039"
language: en
canonical_source: "Taras, P. Gamma-Ray Linear Polarization and Angular Distribution Formulas in Terms of Phase-Defined Reduced Matrix Elements. Can. J. Phys. 49, 328-351 (1971)."
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1971_Taras_Gamma-Ray Linear Polarization and Angular Distribution Formulas in Terms of Phase-Defined Reduced Ma.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1971_Taras_Gamma-Ray Linear Polarization and Angular Distribution Formulas in Terms of Phase-Defined Reduced Ma.pdf"
raw_sha256: "151e8a5274e3f9f510f3884a0e5e20a0ca8c9d883d609fe18ab7b4fb669e8a5d"
nuclei: ["35Cl", "19F", "26Mg", "28Si"]
models: ["Rose-Brink-formalism"]
observables: ["linear-polarization", "angular-distribution", "multipole-mixing-ratio", "statistical-tensor"]
methods: ["angular-distribution", "linear-polarization-asymmetry", "multipole-mixing-ratio"]
tags: [phase-defined-matrix-elements, mixing-ratio-sign, angular-distribution, gamma-polarization, statistical-tensor]
---

# Gamma-Ray Linear Polarization and Angular Distribution Formulas in Terms of Phase-Defined Reduced Matrix Elements

## Bibliographic Record

- 作者：P. Taras。
- 期刊：*Canadian Journal of Physics* 49(3), 328-351 (1971)。DOI：`10.1139/p71-039`。
- 原始文件：`raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1971_Taras_Gamma-Ray Linear Polarization and Angular Distribution Formulas in Terms of Phase-Defined Reduced Ma.pdf`；SHA-256：`151e8a5274e3f9f510f3884a0e5e20a0ca8c9d883d609fe18ab7b4fb669e8a5d`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: PDF pp.328-351 全文；phase-defined Rose-Brink matrix elements、statistical tensors/population parameters、angular-distribution Z coefficients、mixed-multipole formulas、linear-polarization relation、Litherland-Ferguson methods I/II、particle-gamma capture and particle-X-gamma capture cases、finite counter size and application discussion均已阅读。
- Not covered: 引用论文全文和原文 Appendix 表格的逐项数字转录。
- Coverage caveats: 公式 PDF 部分为 OCR/扫描层；论文级公式转引需回页面核对相位和系数索引。本文的重点是 phase convention consistency，不是某一核素的最终实验结论。

## Paper Question and Scientific Motivation

- 论文解决的核心问题是：如何把 γ 角分布、线偏振和 multipole mixing ratio `δ` 统一写在 Rose-Brink phase-defined reduced matrix-element convention 下，使 `δ` 的大小和符号可与核模型预测一致比较（摘要；PDF pp.328-329）。
- 作者强调，若不同实验使用不一致的 reduced-matrix-element phase convention，混合比符号会被错误解释，并可能导致错误的 polarization 参数。

## Method and Design Logic

- 初态是沿束流轴取向的 aligned state；磁子态 population `P(m)` 与 statistical tensors `p_k0` 通过 Clebsch-Gordan 变换互换。alignment condition 使奇 k tensors 消失（PDF p.329，式 (4)-(5)）。
- 角分布写成 statistical tensors、Z coefficients 和 phase-defined reduced matrix elements 的组合；混合跃迁的干涉项保留 `δ` 的相位和符号（PDF pp.329-334，式 (2)-(21)）。
- 论文分别处理 unobserved-particle angular distributions、Litherland-Ferguson particle-gamma angular correlations、particle-gamma capture 和 particle-X-gamma capture，并讨论有限粒子计数器对 population parameters 的限制（PDF §§3.2-3.5）。

## Key Evidence and Reasoning Chain

1. 线偏振和角分布共享同一 phase-defined reduced matrix elements；因此从两类数据提取的 `δ` 必须使用同一相位 convention（PDF pp.328-329）。
2. Dipole-quadrupole mixtures 只出现到 `P4(cosθ)`，公式可同时用于 M1/E2 与 E1/M2；quadrupole-octupole mixtures 则加入相应更高 Legendre terms（PDF pp.333-334）。
3. 某些反应方法只允许有限 `m` populations，能唯一确定 statistical tensors；在不利情况下只有 `a2/a0`、`a4/a0` 两个系数，任意 `δ` 可能都能拟合，必须引入偏振或额外约束（PDF pp.334-335）。
4. 作者用一个近期 γ polarization measurement 展示 phase-consistent formulas 如何识别异常 inhibited transition；“预期 transition probability”不能替代直接 parity/polarization measurement（PDF pp.328-329）。

## Summary

Taras 1971 是 γ 角分布、线偏振和混合比符号一致性的基础方法来源。它把 aligned-state population、statistical tensors、Rose-Brink phase-defined matrix elements、Z coefficients 和 polarization formulas 放进同一套约定，并明确区分不同反应几何和有限 counter-size 的适用条件。对本 Wiki，最重要的边界是：`δ` 的符号不是脱离 phase convention 的可移植标签；仅有两个角分布系数通常不能唯一选定混合比分支。

## Experimental or Theoretical Setup

- Formalism for aligned nuclei produced by unpolarized particle reactions/capture。
- Cases: particle unobserved, particle-gamma angular correlation, particle-gamma capture and particle-X-gamma capture。
- Quantities: `P(m)`, `p_k0`, `Z_k`, Legendre angular-distribution coefficients, polarization and phase-defined `δ`。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| T71-1 | 混合比 `δ` 必须与 phase-defined reduced matrix elements 使用同一 convention，才能比较符号和核模型预测。 | method-principle | direct | PDF pp.328-329 | false |
| T71-2 | `p_k0` 与磁子态 population `P(m)` 通过 CG 系数变换；alignment 使奇 k tensors 消失。 | formalism | direct | PDF p.329，式 (4)-(5) | false |
| T71-3 | Dipole-quadrupole angular distributions 只包含到 `P4`，并适用于 M1/E2 和 E1/M2。 | formalism | direct | PDF pp.333-334，式 (18)-(19) | false |
| T71-4 | 在 population/geometry 不充分时，只有 `a2/a0`、`a4/a0` 可能无法唯一确定 `δ`；线偏振提供额外约束。 | limitation | direct | PDF pp.334-335 | false |

## Nuclear Structure Information

- 论文不建立单核素能级图；`35Cl`、`19F`、`26Mg`、`28Si` 仅作为方法和示例反应背景。
- 可复用内容是 mixing-ratio / parity / polarization 的证据逻辑，不是这些核素的长期结构页面。

## Authors' Interpretation

- 线偏振对 parity 和 mixing ratio 的价值来自 phase-consistent interference term；错误的 `δ` phase 会直接污染 interpretation。
- 在 population information 不足时，测量 polarization 是减少 angular-distribution 多解的必要方向之一。

## Model Results

- 不提供新的 shell-model spectrum；论文讨论如何把实验 `δ` 与核模型中 phase-defined transition matrix elements 比较。

## Competing Interpretations and Limitations

- 不同 convention、符号定义和角度坐标可产生表面上相反的 `δ` 或 polarization sign；跨来源比较必须先做 convention mapping。
- 有限 detector/particle-counter acceptance 会改变可达到的 population constraints；不能直接把理想公式用于真实阵列。
- 仅有两个 angular-distribution coefficients、未知 alignment 或混合跃迁多解时，偏振本身也需结合 DCO/角分布/寿命等证据。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-T71-1 | Core reconstruction | 该来源的核心贡献是把“混合比符号”从经验标签变为 phase-defined matrix-element convention 下的可比量。 | PDF pp.328-334 | self-checking |
| AR-T71-2 | Assumptions and dependencies | 依赖 alignment、statistical tensors、reaction geometry、counter acceptance 和 multipole convention。 | PDF §§2-3 | self-checking |
| AR-T71-3 | Transfer conditions | 公式可作为 P-ADO/DCO/polarization convention bridge；具体 sign/δ 仍需按 source 的 phase and axis definitions 转换。 | PDF §§2-5 | provisional |
| AR-T71-4 | Failure conditions | 只用少量 angular coefficients、忽略 finite counter size 或混合 branch 会导致 δ 不唯一/符号错误。 | PDF pp.334-335 | active-L3 |
| AR-T71-5 | Reverse/falsification test | 对同一 transition 用 source convention 重算 angular distribution 与 polarization，并与已知 pure E2/M1 reference 比较；若符号无法同时闭合则暂停 claim。 | PDF §§3-5 | candidate-L3 |
| AR-T71-6 | Research-question decision | 作为 mixing-ratio/polarization 方法核心来源接入方法项目，不启动 L4。 | PDF pp.328-351 | completed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki 已有 multipole-mixing-ratio、linear-polarization、ADO/DCO pages，但 phase-defined sign consistency 和 population-tensor conversion 尚未有这篇基础来源。
- Effect of this source: `foundational-background` and `methodological-bridge`。
- Reason: 该来源为后续 ADO/偏振/混合比 claims 提供统一 phase convention 和多解边界。
- Persistence decision: update [[linear-polarization-asymmetry]], [[angular-distribution]] and [[multipole-mixing-ratio]] source lists; no standalone nucleus page。
- Review state: `unreviewed`; formalism claims self-audited by Codex, not human-reviewed。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| foundational-background | [[multipole-mixing-ratio]] | phase-defined matrix elements and sign-consistent δ。 |
| methodological-bridge | [[linear-polarization-asymmetry]] | polarization and angular-distribution formulas share convention and statistical tensors。 |
| methodological-bridge | [[angular-distribution]] | `a2/a0`, `a4/a0`, finite alignment and reaction-method boundaries。 |

## Human Review Triage

### P0

- T71-P0-1：任何跨文献 `δ` 符号、electric/magnetic polarization sign 或 model comparison，必须先核对 phase convention、axis convention 和 `P(m)`/tensor definitions。

### P1

- T71-P1-1：少量 angular coefficients 下的 δ branch ambiguity；不得以单一 polarization sign 宣称唯一 mixing ratio。

### P2/P3

- 24 页公式 OCR/扫描混合；论文写作逐式引用时必须回到视觉页核对系数索引。

## Extracted Pages

- Nuclei: 不创建。
- Bands: 不创建。
- Concepts: phase-defined reduced matrix elements、statistical tensors、mixing-ratio sign。
- Methods: [[angular-distribution]], [[linear-polarization-asymmetry]], [[multipole-mixing-ratio]]。

## Non-source Notes and Follow-up

- 下一步：把 T71 的 phase/sign bridge 与 HS-011 之后的 Taras/Brink/PDCO sources 对照，检查方法页公式的 convention consistency。
