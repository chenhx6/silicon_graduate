---
type: research-note
title: "MR/AMR 跨来源一致性与定位边界审计"
aliases: [MR AMR cross-source consistency, magnetic antimagnetic consistency audit]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [roy-2011-cd110-systematics-antimagnetic, garg-2015-135pr-magnetic-rotation, agarwal-2007-137pr-magnetic-rotation-bandcrossing, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, hubel-2005-magnetic-rotation-review]
created_from: Day26 cross-source consistency audit 040
promotion_target: magnetic-rotation
tags: [magnetic-rotation, antimagnetic-rotation, consistency-audit, provenance, observables]
---

# MR/AMR 跨来源一致性与定位边界审计

> 040 是只读收敛审计；Day27 仍为无学分预习，不打开 Day28。本文只新增审计记录，不修改被审计的共享页或来源页。

## Research Trigger

017–037 已建立 MR/AMR 的电流、分岔、离散对称和可观测量边界。本审计检查这些工件与 Roy、Garg、Agarwal、Frauendorf、Hübel 原件记录之间是否出现单位、时间反演、局部电流、数值或 locator 矛盾。

## Grounded Evidence

1. **单位与比值**：Frauendorf F01-D26-003 将 (J^{(2)}/B(E2)) 写成有单位的 (mathrm{MeV}^{-1}(eb)^{-2})（在 (hbar=1) 约定下）；Roy RO11-4/source audit 给出源特定范围。037、AMR 概念页和证据笔记都撤回无量纲及普适 (ge100) 硬门。
2. **MR 相对比值**：Garg GA15-3/GA15-14 和 Agarwal AG07-5/6、AG07-D22-R098-1 都保留相对 (B(M1)/B(E2)) 与缺少绝对寿命的边界。037 矩阵没有把比值升级为绝对强度。
3. **T 与局部流**：017/034 JSON 明确玩具流为 arbitrary units；概念页和 034 笔记都说明 (\mathbf j) 是时间奇量、反幺正组合可补偿时间反演符号，而局部残差不能认证模式。
4. **TAC 与实验室量**：Frauendorf F01-5/F01-8/F01-9 及 024/031/034 笔记均区分内禀 TAC、good-(I) 恢复和实验跃迁；031 把 0.514639、0.6、12 keV 与 0.37 MeV 分开。

## Provisional Reasoning

一致性结果分为：

- **通过**：物理边界和证据等级在不同页面之间一致；包括 (T)-odd 电流、TAC/good-(I) 区分、Garg/Agarwal 相对比值限制、037 观测量矩阵和 031 四种频率/能隙量的分层。
- **带警告通过**：(J^{(2)}/B(E2)) 单位与来源特定范围一致，但旧页仍保留历史撤回数字的审计段落；这些段落明确标为撤回/不作科学源，不能重新引用。
- **定位已核**：归档 Roy PDF 第3个PDF页顶部印刷页码为324，Table 1在该页；017工件原写p.323已更正为p.324。p.323仍用于实验线形描述。

没有发现会改变当前 MR/AMR 物理边界的内部矛盾。定位冲突只影响引用导航和 locator 可信度。

## Assumptions

审计以当前 source 页 claim_kind、locator、needs_review 和 artifact JSON 为准；没有重新读取所有 raw PDF，也没有把同一实验的综述、论文和模型当独立实验。历史 superseded 工件可以显示旧算术，但不改变当前知识页的撤回状态。

## Competing Explanations

若某条页面只保留 (B(M1)/B(E2))、规则能谱、弱 E2 或局部电流残差，它仍可能对应普通弱集体、终止、signature、组态混合、手征或 wobbling。040 未把这些竞争解释压成单一模式。

## Transfer Conditions

审计结论可迁移的是单位、证据分层和“相对比值不等于绝对强度”的方法边界。Roy 的 (B(E2)) 数列、Agarwal 的比值、Garg 的 possible-MR 语句和 017 的 toy 残差都必须保留原核素、原实验、原模型和原 locator。

## Failure Conditions

若把旧 superseded 数值重新写入当前证据；把有单位比值写成无量纲阈值；把 toy (\mathbf j(\mathbf r)) 当实核流；把 TAC (omega_c) 当实测频率；或在未解决 Roy 页码冲突时给出确定 page-only 引文，审计结论失效。

## Falsification or Reverse Tests

重新核对 Roy PDF 的 printed page、PDF page label 和 Table 1 位置；再把 017、037 中的 source locator 统一到同一页码 convention。对任意物理矛盾，回到原件 claim、source lineage、单位和误差，而不是依靠 artifact 的可运行算术反证实验。

## Open Questions

Agarwal/Garg 的后续勘误是否改变表格 locator 或相对比值？真实自洽 current density 和 good-(I) EM 网络能否为 toy 对称残差提供可复现替代？

## Human Review

本页为 Codex source/claim self-audit，未提升 `human-reviewed`。Roy locator 冲突需在正式引用前定向核对；其余一致性结论不替代逐条原件复核。

## Promotion or Rejection History

2026-10-28：完成 MR/AMR 040 只读交叉审计。保留 (J^{(2)}/B(E2)) 的单位边界、T-odd 电流与 TAC/good-(I) 区分、相对比值和 toy 限制；完成 Roy Table 1 的 p.324 归档PDF页码核对并更正017工件；保留p.323作为线形段定位。Day27 保持无学分预习。
