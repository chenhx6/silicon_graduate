---
type: project
title: "P-ADO 中反应条件依赖的 alignment response 与 mixing-ratio 可识别性"
aliases: [P-ADO alignment response dependence paper, shared sigma over J null test]
created: 2026-11-05
updated: 2026-11-05
status: active
review_status: unreviewed
project_stage: active-L3-public-data-L4
publication_status: local-draft
confidentiality: public-benchmark-with-source-boundary
nuclei: [67ga]
tags: [pado, alignment, sigma-over-j, mixing-ratio, a130-methodology, epja-candidate]
---

# P-ADO 中反应条件依赖的 alignment response 与 mixing-ratio 可识别性

## Research Question

对于同一个 `^{67}Ga` 的 `958.0-keV`, `13/2^+ -> 9/2^+` 纯 `E2`
参考跃迁，来自不同 projectile 和 beam-energy 条件的
`(alpha_2, alpha_4)` 是否能共享一个 `r = sigma/J` alignment response？

这个问题直接对应 A≈130 在束谱学中的 mixing-ratio 提取风险：若把跨反应、
跨能量或不同 feeding history 的 `r` 当作同一个 nuisance，角分布/ADO
反演的 `delta(E2/M1)` 会继承一个未被观测量约束的系统偏差。

## Single innovation

用 reaction-condition-aware profile likelihood 对 shared `r` null 做可复现
反证，并把以下层次分开：

- shared `r`；
- projectile-family-specific `r`；
- energy-dependent `r(E)`；
- direct/cascade feeding 的替代解释；
- 未知的 row-internal `alpha_2-alpha_4` covariance。

文章只讲这一个方法学创新。Zobel 表格不是 A≈130 新实验；它是对 A≈130
wobbling/chirality/TiP 证据链中 alignment nuisance 的公开校准基准。

## Grounded evidence

- [[zobel-1983-energy-projectile-alignment]]：原始 `^{67}Ga` 反应、Table 1、
  `alpha2/alpha4` fit outputs、statistical-error 和 covariance boundary；
- [[pado-shared-alignment-null-profile]]：现有 provisional max-Mahalanobis
  shared-null 结果；
- [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]：alignment
  nuisance 迁移和 mixing-ratio 传播边界；
- [[angular-distribution]]：`W(theta)`、F 系数和 P-ADO 条件；
- [[experimental-wobbling-evidence-strength-map]]：wobbling 识别中 response、
  mixing-ratio 和寿命的证据层。

## Current numerical baseline

在当前 table-level 合同、`rho=0`、`J=13/2` 下：

- all ten rows shared-null `tau_req = 2.1556`;
- alpha family shared-null `tau_req = 2.1556`;
- `12C` family shared-null `tau_req = 0.7417`;
- allowing common `rho` changes the sensitivity but does not make the alpha-family
  null robust over the explored interval `rho in [-0.8, 0.8]`.

这些数字是 Codex self-audit 的 profile result，不是原文作者报告的实验显著性、
coverage-calibrated p-value 或正式 likelihood-ratio test。

新建的 profile likelihood 结果（`raw/writing/gpt/pado-alignment-response-dependence/analysis/results/alignment-profile.json`）进一步给出：

- shared model: `r0=0.280146`, `AIC=32.0415`, `BIC=33.0372`,
  `Dmax^2=31.2643`;
- family model: `r_alpha=0.288714`, `r_12C=0.275782`,
  `AIC=32.6274`, `BIC=34.6188`;
- energy model: `r0=0.278525`, slope `0.005280` per 10 MeV,
  `AIC=32.6339`, `BIC=34.6253`.

在 `rho=0` 的 Gaussian table-level sensitivity下，额外参数没有获得 AIC/BIC
支持；这使文章主张保持为“shared-null incompatibility and calibration boundary”，
而不是声称 family-specific 或 energy-dependent model 已被数据唯一选中。

用 shared-null `r=0.28`、`rho=0`、固定随机种子 `20261105` 的 1000 次
parametric pseudo-experiments，最大 row-wise `D^2` 小于单行二维
`q95=5.9915` 的比例为 `0.654`，经验 95% 分位数为 `10.0142`。这表明
单行二维阈值不能直接当作十行 maximum statistic 的 family-wise 95% threshold；
该结果是声明过的 toy coverage 检查，不是实验 p-value。

## Planned tests

1. Rebuild the ten-row fixture from the original Table 1 and correct reaction/
   nucleus/page provenance.
2. Fit shared, family-specific and energy-dependent alignment models with a
   profiled common covariance parameter.
3. Run parametric pseudo-experiments under each null to measure false-rejection and
   coverage under missing covariance.
4. Compare maximum Mahalanobis, Gaussian profile likelihood and robust covariance
   sensitivity; keep the contracts separate.
5. Propagate condition-specific `r` into a toy `delta`/ADO inversion to demonstrate
   the practical effect on A≈130 mode identification without claiming a new
   A≈130 measurement.

## Stop conditions

- Original Table 1 identity, row errors or transition mapping cannot be reproduced;
- a source covariance or feeding model changes the conclusion over a reasonable
  sensitivity range;
- pseudo-experiment coverage is not calibrated;
- the result only repeats the source's qualitative warning without a new quantitative
  test;
- the manuscript would need to state that P-ADO is universally invalid.

## Paper status

`active-L3-public-data-L4`: the source and table are archived, but the new model,
coverage study, claim-specific evidence gate and journal fit are still pending.
No experimental fact, user-data result or final paper conclusion has been admitted.
## Current Hypotheses

`H_shared` 假设所有条件共享一个 `r=sigma/J`；`H_family` 允许
projectile-family-specific response；`H_energy` 允许一个显式 beam-energy
slope。direct/cascade feeding mixture 是物理替代解释，不由表格本身自动识别。

## Evidence Available

公开 Zobel 1983 Table 1、source-level locator、现有 max-Mahalanobis
profile 和本工作包的 Gaussian profile/coverage outputs 已存在。source covariance、
raw event counts、detector response 和真实 feeding model 尚未提供。

## Risks and Blockers

- missing row-internal covariance may change likelihood and coverage;
- the table is a fitted summary, not an event-level reanalysis;
- a family or energy model is not selected by the current AIC/BIC values;
- a publication claim requires a predeclared coverage-calibrated test.

## Next Actions

1. Complete family-wise coverage and covariance sensitivity;
2. add a feeding-aware negative-control model;
3. freeze the EPJA claim-to-source map and Data Availability Statement;
4. run a final manuscript self-audit before any paper-level user review.
