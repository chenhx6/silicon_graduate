---
type: research-note
title: "A≈130 三轴论文包审计：旧稿只能作为素材与失败案例"
aliases: [a130 triaxial writing package audit, legacy manuscript audit 20261105]
created: 2026-11-05
updated: 2026-11-05
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [a130-single-point-paper-133ce-response-aware-identifiability]
created_from: "Full-library audit and subagent read-only review of raw/writing/gpt/a130-triaxial"
scope: a130/writing-package/data-provenance/claim-calibration
nuclei: [135pr, 135nd, 134pr, 131ce, 133ce]
tags: [a130, manuscript-audit, provenance, evidence-boundary, paper-candidate]
---

# A≈130 三轴论文包审计：旧稿只能作为素材与失败案例

## Audit decision

`raw/writing/gpt/a130-triaxial/` 不作为新稿的正文模板、事实源或结论源。
它保留为素材库、失败案例和数据 provenance 线索。新论文必须使用独立 topic
目录，并从 `knowledge/sources/`、原始材料和可复现分析重新建立 claim ledger。

## Blocking findings

### 稿件状态不一致

`main.pdf` 与 `paper.pdf` 的字节身份相同，实际由 `paper.typ` 生成；它不是
`main.tex` 的编译结果。`main.tex`、`paper.typ` 和 PDF 因此不是同一稿件。当前
环境也没有完成 RevTeX 编译验证，不能把现有 PDF 称为已验证投稿稿。

### 同一 `135Pr` claim 存在多套数值

`data/table1_135pr_experiment_benchmark.csv`、`main.tex`、`paper.typ`、
`generate_figures.py` 和 `fig2_*profile_likelihood_curve.csv` 使用不同的
能量、`a_2`、偏振值和 mixing-ratio roots。它们不能同时作为一条证据链。
正文给出的 `11.1 sigma` 也不能由当前图件和公式一致重建。

安全的知识结论只能是：公开 `135Pr` 资料存在分支、偏振定义和响应处理差异，
需要共同响应与协方差审计；旧稿的数值显著性不继承到新论文。

### Figure 3 不是 partner-resolved 实验比较

`table2_chiral_benchmark_135nd_134pr.csv` 的 `band` 列只有 `Band1`，绘图
代码也只读取一条带，再叠加理论曲线。因此它不能证明两条实验伙伴带之间的
`S_M1`、带内 `B(E2)` 或 interband minimum。

### Figure 4 不是可复现的 Nilsson/Strutinsky 计算

图件读取预先存在的插值 CSV，没有从 `table3` 产生，也没有实现其声称的
Nilsson、Strutinsky、QTR 或 Routhian 计算。它可作为研究假设图，不能作为
微观计算结果。

### P-ADO 表的 source identity 错位

旧稿中的 Zobel 表将反应、核素和页码写成与已归档 source 不一致的版本。
因此 Figure 5 不能作为 Zobel 原始数据重绘。P-ADO 共享 alignment 是有价值的
研究种子，但必须先从原文表格重新建 manifest、校准反应身份和误差结构。

### `figures/made/data/` 不能自我重建

绘图脚本读取辅助 CSV，但不生成这些 CSV；删除它们后不能得到同一份中间数据。
它们只能被视为历史缓存，不能称为可复现 producer output。

## Reusable material

1. “角分布 mixing-ratio 双根必须由独立观测量仲裁”是可复用的方法学问题；
2. P-ADO alignment 随 projectile、能量和 feeding 条件变化是可检验的 EPJA 候选；
3. `131Ce/133Ce` 可作为真正结合 iThemba 数据的核结构论文方向；
4. 三轴转子相空间图可作教学性示意，但不构成 A≈130 新结果。

## New-paper routing

当前优先级改为：

1. `133Ce` response-aware collective-mode identifiability（核结构价值高，
   依赖私有数据和 response closure，目标 PRC/EPJA）；
2. P-ADO shared-alignment null test（方法学清晰，目标 EPJA，依赖正确重建
   Zobel 原始表和 coverage 校准）；
3. `135Pr` common-response branch audit（公开争议明确，但缺 raw response/
   covariance，暂不写强排除）。

这些候选不能合并成一篇 omnibus paper。

## Self-audit boundary

本页是 Codex self-audit；没有把旧稿数字或本审计推断写成已通过 paper
evidence gate 的结论。所有旧稿 claim 在新文章使用前仍需回到直接 source、
locator、适用条件和用户定向审核。

## Research Trigger

用户要求把旧 A≈130 写作包作为素材审计，并从全库温故知新中筛选一个可以
单独成文的创新点。

## Grounded Evidence

本审计使用旧稿源码、CSV、绘图脚本、现有 source/project 页面和直接归档的
Matta、Lv、Zobel、133Ce、135Nd 等来源。旧稿文件身份和数字冲突只在本地
文件层面审计，不把旧稿的人工整理表当作原始实验数据。

## Provisional Reasoning

旧稿最有价值的部分是它暴露了一个可发表的问题：不同实验响应和派生量被
放在同一解释框架后，模式结论会被不一致的输入放大。该推断仍需由新文章的
可复现 profile/coverage 分析验证。

## Assumptions

旧稿文件仍作为历史工作包保留；本审计不重写其原始内容，也不把旧稿 PDF、
人工整理 CSV 或图件缓存提升为独立实验来源。

## Competing Explanations

旧稿中的不一致可能来自版本漂移、人工抄录、相同实验谱系的重复计数、图件
缓存与正文不同步、或真正的物理解释分歧。只有回到原始 source/locator 才能
区分这些原因。

## Transfer Conditions

本审计结论只适用于当前 `raw/writing/gpt/a130-triaxial/` 包及其已核对的
source lineage；不能把旧稿的错误模式自动迁移到新 P-ADO 或 `133Ce` 分析。

## Failure Conditions

若无法回到原始 source、定位数据来源、确认版本身份或区分实验事实与模型结果，
相关 claim 保持 withdrawn/conditional，不进入新稿。

## Falsification or Reverse Tests

新稿必须重新读取原始 Table/图/能级位置，重建数据 manifest，并用独立响应、
holdout 或 pseudo-experiment 检查 claim。若新计算不能重现 source identity 或
结果依赖未声明的 hard-coded 数值，候选路线停止。

## Open Questions

- 旧稿中哪些人工整理表可以由原始 source 逐行重建？
- P-ADO shared-alignment 候选是否能通过 coverage 和 family 分层形成新结果？
- South Africa `133Ce` 数据是否最终能闭合到公开、可复算的 response-aware L4？

## Human Review

本页是 Codex self-audit，未发生用户 paper-level claim review。

## Promotion or Rejection History

2026-11-05：旧稿被降格为素材与失败案例；P-ADO alignment-response 作为当前
公开数据 primary 论文候选，`133Ce` response-aware identifiability 保留为
secondary candidate。
