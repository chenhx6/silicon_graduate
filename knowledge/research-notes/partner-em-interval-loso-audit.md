---
type: research-note
title: "伙伴带 B(E2) 的协方差无关逐自旋留出审计"
aliases: [partner EM interval LOSO audit, partner-resolved B(E2) interval test]
created: 2026-10-31
updated: 2026-10-31
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [mukhopadhyay-2007-135nd-chiral-vibration-static, tonev-2007-134pr-dynamic-chirality, rather-2014-ag106-transition-rates]
created_from: "Day28 independent candidate-method worker"
promotion_target: "post-30-day-nuclear-structure-paper-prospectus"
scope: partner-em/b-e2/partial-identification/lineage
nuclei: [135nd, 134pr, 106ag]
observables: [b-e2, lifetime, transition-strength]
tags: [partner-bands, b-e2, partial-identification, leave-one-spin-out, covariance-boundary]
---

# 伙伴带 `B(E2)` 的协方差无关逐自旋留出审计

## Research Trigger

跨核素伙伴带比较容易把相似的 `B(E2)` 中心值误写成模式判据。本页测试一个明确的数据合同：同一项目内各自旋的 `B(E2)_partner/B(E2)_reference` 是否可以由一个共同尺度解释；结果只针对这个合同，不裁决手征、形状或组态。

## Grounded Evidence

| case | input | source locator | boundary |
|---|---|---|---|
| `135Nd` MU07 D5/D6 | 五个重叠自旋的 `B(E2)` 中心值和印刷边际误差 | [[mukhopadhyay-2007-135nd-chiral-vibration-static]] `MU07-1`, `MU07-11` | DSAM/branch joint covariance 和逐线 identity 未公开 |
| `134Pr` Tonev07 Band1/Band2 | `I=14–17` 的 Table II `B(E2)` 中心值和边际误差 | [[tonev-2007-134pr-dynamic-chirality]] `TO07-D24-002`, `TO07-D24-008` | raw file 未归档；shared lifetime/branch covariance 未提供 |
| `106Ag` Rather14 | `I=14–17` 的 partner/main `B(E2)` 中心值 | [[rather-2014-ag106-transition-rates]] `RA14-5`, `RA14-12` | 冻结输入没有逐行 `B(E2)` 误差，不能进入区间拒绝 |

## Provisional Reasoning

对每行定义

$$
r_i = \frac{B(E2)_{\mathrm{partner},i}}{B(E2)_{\mathrm{reference},i}}.
$$

若两项均为正，把打印误差当作边际误差盒而不是独立高斯标准差，则

$$
r_i \in \left[
\frac{B_p-\sigma_p}{B_r+\sigma_r},
\frac{B_p+\sigma_p}{B_r-\sigma_r}
\right].
$$

轮流留出自旋 `k`，以其余区间的交集作为训练允许集。只有训练交集非空且与留出区间完全不相交，才允许写 `reject_common_scale_for_holdout`。训练交集为空、误差缺失或 source identity 未闭合时，结果为 `unidentifiable / not executable`。

实际运行入口为 `tmp/day28-em-candidates/loso_partner_em_interval.py`，结果为 `tmp/day28-em-candidates/loso_partner_em_interval.json`，脚本退出码为 `0`。

| case | executable | rejected holdouts | result |
|---|---:|---|---|
| `135Nd` MU07 D5/D6 | yes | none | 所有留出区间与训练共同尺度相交 |
| `134Pr` Tonev07 Band1/Band2 | yes | none | 中心值变化明显，但保守误差盒过宽 |
| `106Ag` Rather14 | no | not applicable | 缺逐行误差，只能作中心值控制 |

## Assumptions

各行的 parent/reference 与 partner state identity 已由来源表绑定；打印误差只用于保守区间显示；不假定协方差为零，不把误差盒写成置信区间，不将不同论文或同实验不同版本计为独立实验。

## Competing Explanations

共同尺度的未拒绝可能来自误差盒过宽、共享 DSAM/lifetime 分母、branch/feeding covariance 或真实的近似尺度相似。它不能单独说明手征、形状共存或组态解释正确。

## Transfer Conditions

只有在跃迁方向、state identity、同一 `B(E2)` 定义、误差语义和 source lineage 均明确时，才能迁移到其它伙伴带。没有逐行误差时只能保留中心值控制，不得强行补区间。

## Failure Conditions

若训练交集为空、误差下界跨零、source body 未归档且身份不稳定、或同一行混入不同 parent/branch，当前审计不能生成拒绝结论。若获得真实 joint covariance，必须用联合模型重做主结果。

## Falsification or Reverse Tests

取得逐线 branch、响应和 joint covariance 后，比较误差盒结果与真实 likelihood/coverage。若真实共同模型在协方差合同下排除某些 holdout，才能升级为数据分析结果；若共同尺度恢复，应撤回任何表格级拒绝措辞。

## Open Questions

- `106Ag` 能否取得逐行 `B(E2)` 误差或原始 DSAM covariance？
- `134Pr` 的 raw archive 与共同 lifetime/branch covariance 能否恢复？
- 135Nd 的图点、Table I 行和具体跃迁能否在同一 line ledger 中闭合？
- 该方法与外部 partial-identification/interval-validation 文献相比是否具有足够方法学新颖性？

## Human Review

本页是 Codex self-audit，`review_status: unreviewed`、`reasoning_status: provisional`。结果是可复现的条件数据合同审计，不是实验 covariance 重建、置信区间、手征证明或否证。

## Knowledge Impact and Learning Decision

`limits`：135Nd 与 134Pr 的公开误差盒不能硬拒绝共同 `B(E2)` 尺度；106Ag 当前不可执行。

`supports`：把“中心值变化明显”和“在公开不确定度下可证伪”分开，为 30 天后论文 prospectus 提供安全的最小分析形态。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-10-31 | Day28 bounded candidate exercise | none | provisional | frozen published tables executed with interval boxes and lineage gating | [[post-30-day-nuclear-structure-paper-prospectus]] |
