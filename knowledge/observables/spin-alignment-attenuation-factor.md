---
type: observable
title: 自旋取向衰减因子
aliases: [spin-alignment attenuation factor, alignment attenuation factor, alpha2, alpha4]
created: 2026-07-09
updated: 2026-10-17
status: ai-draft
review_status: human-reviewed
observable_kind: angular-distribution-derived-alignment-observable
symbol: alpha2, alpha4
units: dimensionless
tags: [alignment, angular-distribution, pado-support]
---

# 自旋取向衰减因子 (Spin-Alignment Attenuation Factor)

## Definition

在 [[ekstrom-1979-spin-alignment-attenuation-a61-a67]] 中，`alpha_k(Ji) = p_k(Ji) / p_k^ca(Ji)` 表示实际初态 statistical tensor 相对 complete alignment 情形的衰减因子。该文重点讨论 `alpha2` 与 `alpha4`。

## How It Is Obtained

当 `Ji`、`Jf`、multipolarity 以及必要时的 `delta` 已知时，可由测得的 angular-distribution coefficients `A2/A4` 反推 `alpha2/alpha4`。Ekstrom 1979 特意选用 pure-E2 transitions，以避免 `delta` 不确定度污染这一反推。

## Boundary Against Similar Symbols

- `alpha2/alpha4` 不是 Gaussian width `sigma`。
- 它们也不是 Ionescu 1981 Fig.3 中的 `rho2/rho4` statistical-tensor factors。
- 它们也不是 Zobel 1980/1983 使用的 attenuation-coefficient notation 的简单改名版本。
- 它们当然更不是用户代码里的 `sigma/I`。

## Why It Matters Here

这类 observable 直接把“实验角分布有多强的各向异性”与“初态 alignment 实际保留了多少”联系起来，因此是 source-level alignment evidence 与项目层 `sigma/I` 写作动机之间的重要桥梁。

## Important Limitation from Ekstrom 1979

Ekstrom 1979 的 relevant boundary 不是“某个固定 excitation-energy threshold”本身，而是：

- simple Gaussian magnetic-substate population can be too restrictive for the compiled data;
- when unmodeled gamma feeding becomes appreciable and the reaction energy lies sufficiently above the relevant particle-emission threshold, direct-population alignment estimates can become unreliable.

对其中的 energy wording 还必须保持 source-local boundary：

- `E ≳ 2 MeV` only belongs to the Fig.5 `62Ni(alpha,n)65Zn` example;
- for `(alpha,p)`, the effective above-threshold scale is lowered by the proton Coulomb barrier by about `2-3 MeV`;
- 因此它不能被重写成 universal numeric threshold。

## Diagnostic Use

- 用 pure-E2 transitions 反推 alignment retention
- 检查 model-predicted alignment 是否与实验兼容
- 为后续 mixing-ratio analysis 提供受限的 alignment input

## Model Dependence

把 `A2/A4` 反推成 `alpha2/alpha4` 需要已知或受控的 `Ji`、`Jf`、multipolarity，以及必要时的 `delta`。若 feeding history 被忽略，或 direct-population assumption 本身不成立，则 model-derived attenuation estimate 会偏离真实情况。

## Failure Modes and Ambiguities

- 忽略 gamma feeding 会使 direct-population estimate 失真。
- 不同 source 的 attenuation notation 不能直接互换。
- 若 transition assignment 本身不稳，`alpha2/alpha4` 的物理解释也会随之变弱。

## Sources

- [[ekstrom-1979-spin-alignment-attenuation-a61-a67]]
- [[ionescu-1981-improved-angular-distribution-analysis-particle-xn]]
- [[zobel-1980-magnetic-substate-distributions]]

## 2026-10-17条件校准检查：先核实验alpha的参数层

本节仅Codex self-audit，原human-reviewed范围保持，不覆盖新增应用。[[sensharma-2021-wobbling-motion-135pr-187au]] SE21-9/10明定half-integer参考与alpha=rho/B，但其Table4.1的135Pr(.92,.30)若直接作同一J=23/2核布居的两个tensor，违反必要式7−10alpha2+3alpha4≥0；字面quoted-margin矩形也未进入可行域。[[se21-alignment-calibration-consistency]]保存新输入、精确CG/Farkas及独立LP控制。

该结果限制的是直接迁移alpha_exp的假设，不是原始数据错误或某个模式的裁决。非Gaussian positiveP不能独自修复同定义的失配；实际reference E2/M3、gate/geometry、归一操作或参数层变换尚需闭合。sigma/J=.2的source Gaussian给(.894266,.689096)，不是表列pair的共同拟合；width指数参数与finite-J population RMS也分开。Source原flags/Review状态和其它notation边界均保留。

[[sensharma-2021-wobbling-motion-135pr-187au]] SE21-16/17与[[se21-alignment-calibration-consistency]]的后续scope控制显示：同一真实nuclear alpha不变，混合reference经错误pureE2反演可给违反核正性必要式的apparent alpha。该控制是本任务模型反例，不是源报告的新delta或实际calibration原因；原文negative-ratio配置在声明point条件下仍未闭合两表。此新增段也不属于历史human-reviewed范围。
