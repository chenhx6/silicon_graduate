---
type: research-note
title: "P-ADO 共享 alignment null 的真实表格反证"
aliases: [P-ADO shared alignment null profile, sigma/J shared transfer falsifier]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [zobel-1983-energy-projectile-alignment, yamazaki-1967-aligned-angular-coefficients, ionescu-1981-improved-angular-distribution-analysis-particle-xn]
created_from: Day28 independent L3 continuation
promotion_target: sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction
tags: [pado, alignment, sigma-over-i, covariance, partial-identification, real-table-audit]
---

# P-ADO 共享 alignment null 的真实表格反证

## Research Trigger

已有 P-ADO 资产分别处理 `alpha2→sigma/J`、正 magnetic-substate population 凸包、
选定 covariance worksheet 和 Ionescu 表格审计，但没有直接检验一个危险的迁移假设：
不同 projectile/beam-energy 条件下，同一 `958.0-keV`、`13/2+→9/2+`、纯 E2
跃迁是否可以共享一个 alignment response。

## Grounded Evidence

[[zobel-1983-energy-projectile-alignment]] Zobel 1983 Table 1 的十行公开 fit output 覆盖 `alpha` 束的 11.3、12、15、18、
22 MeV 和 `12C` 束的 32、36、40、44、48 MeV；表格身份与逐行输入见
该 source 的 printed p.392 / PDF p.4 Table 1
及冻结 fixture `outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/zobel83-958-table-fixture.json`。
source 说明这些是 attenuation fit estimates，quoted errors 为 statistical，行内
`alpha2-alpha4` covariance 未提供。

## Provisional Reasoning

对每一行令

$$
y_i=(\alpha_{2,i},\alpha_{4,i}),\quad
\mu(r)=(\alpha_2(J=13/2,r),\alpha_4(J=13/2,r)),
$$

其中 `r=sigma/J` 是共享 nuisance；有限-J 系数约定回链
[[yamazaki-1967-aligned-angular-coefficients]]。缺少行内协方差时，用共同 `rho` 参数化

$$
\Sigma_i(\rho)=
\begin{pmatrix}
s_{2,i}^2 & \rho s_{2,i}s_{4,i}\\
\rho s_{2,i}s_{4,i} & s_{4,i}^2
\end{pmatrix}.
$$

以逐行 Mahalanobis 距离的最大值

$$
D(r,\rho)=\max_i (y_i-\mu(r))^\mathsf{T}\Sigma_i^{-1}(y_i-\mu(r))
$$

检验共享 null；`tau` 只作为声明清楚的共同 covariance inflation sensitivity，
不是 detector calibration 或实验 coverage。

## Real-table Result

可复现入口为 `tmp/day28-pado-research/profile_shared_z83.py`，结果为
`tmp/day28-pado-research/shared-z83-profile.json`：

| 量 | 结果 |
|---|---:|
| 最佳共享 `sigma/J` | `0.2727346222` |
| 最佳共同 `rho` | `0.6369815764` |
| 共同预测 `(alpha2, alpha4)` | `(0.8194195633, 0.5176233469)` |
| 最小逐行最大 Mahalanobis 平方距离 | `17.69642678` |
| 95%二维参考阈值 `q` | `5.99146455` |
| `tau=1` 是否存在共同区间 | 否 |
| 达到95%二维参考域所需 `tau` | `1.71860589` |

最佳共同均值有正 population LP witness；因此失败来自十个 reaction-condition
行不能由一个共享 response 同时解释，而不是最佳均值超出纯量子正 population
可行域。逐行从 `alpha2` 反演的 `sigma/J` 约为 `0.1270–0.3650`，与共享
null 的高残差方向一致。

## Interpretation and Limits

这项结果支持一个可复用的 falsifier：若方法把不同 reaction/projectile/beam-energy
条件的同类 transition 共享为一个 alignment nuisance，应先 profile 共同 `rho`
和共同 `tau`；若 `tau=1` 无解且所需 `tau` 明显大于1，应改用
condition-specific 或 feeding-aware population。

该结果限制的是“跨反应条件复用单一 alignment response”的 null，不否定 P-ADO、
Zobel 的单行 fit、纯 E2 参考或任何 condition-specific 模型。`tau`、共同 `rho`
和95%二维阈值是本任务的统计敏感性合同；没有恢复 source covariance、event counts、
detector efficiency、真实 coverage 或正式 likelihood-ratio。

[[ionescu-1981-improved-angular-distribution-analysis-particle-xn]] Ionescu 1981 的 pure-E2 表格另有作者报告的 global Gaussian 不足与
side-feeding/discrete-feeding 处理；它是必要 companion boundary，不与本轮十行
Zobel 结果合并为独立实验票。若要升级为方法论文，下一步应分别对 `alpha` 与
`12C` family profile，并在取得原始 covariance 后再做 coverage study。

## Assumptions

十行记录的 transition identity、`Ji/Jf`、纯 E2 条件和 `alpha2/alpha4` 定义一致；
quoted marginal errors 可作为表格级边际误差输入；缺失的行内 covariance 由共同
`rho` 做敏感性参数化。`tau` 和二维参考阈值是声明的统计合同，不是实验校准或
coverage estimate。

## Competing Explanations

共同 null 的失败也可能来自 projectile-specific alignment、feeding、response、
误差估计方式或 source 表格的拟合模型，而不是 P-ADO 方法本身失效。Ionescu 的
discrete-feeding 模型、condition-specific population 和真实 detector response
是必须保留的替代解释。

## Transfer Conditions

只有在 transition identity、spin/parity、多极性、误差定义和 reaction-condition
分组一致时，才可复用本 null-test 结构。不能把本轮 `tau` 或共同 `rho` 当作其它
阵列的校准常数，也不能把 table-level rejection 写成实验显著性。

## Failure Conditions

若逐行误差不是可比较的边际误差、source 表格混入不同 transition、误差下界跨零、
或 feeding/response 需要 condition-specific nuisance，当前共同 null 不适用。若
实际 covariance 远超 quoted marginal errors，必须重新定义统计合同。

## Falsification or Reverse Tests

取得原始角分布/逐角计数、response、efficiency、feeding 和完整 covariance；按
projectile family 做预注册 profile，并用 Ionescu 的 feeding-aware model 作负对照。
只有共同 response 在真实 likelihood 和 coverage 检验中仍被排除，才可写成正式方法
结论。

## Open Questions

- `alpha` 与 `12C` 两个 projectile family 各自是否能恢复有限的共享区间？
- `tau≤1.2` 这类容忍范围是否能由独立 calibration 或 source covariance 支持？
- 真实 feeding-aware model 是否解释十行差异，还是需要更细的 reaction-condition response？

## Human Review

本页是 Codex self-audit，`review_status: unreviewed`、`reasoning_status: provisional`；
真实表格计算通过脚本和 JSON 保存，但不等于实验重拟合或用户审核。

## Promotion or Rejection History

2026-10-30：由 Day28 全库复习和 P-ADO 旁线研究产生。结果支持将共享 alignment
迁移假设列为可证伪的开放问题；未升级为投稿结论。
