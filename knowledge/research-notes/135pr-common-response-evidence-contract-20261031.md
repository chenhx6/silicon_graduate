---
type: research-note
title: "`135Pr` common-response evidence audit 的最小统计合同"
aliases: [135Pr common response contract, 135Pr branch profile and holdout contract]
created: 2026-10-31
updated: 2026-10-31
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [matta-2015-transverse-wobbling-135pr, lv-2022-evidence-against-wobbling-135pr, sensharma-2019-two-phonon-wobbling-135pr, sensharma-2026-evolution-chirality-transverse-wobbling-135pr, chen-2026-bayesian-inertia-wobbling-135pr]
created_from: "2026-10-31 P1 contract audit"
promotion_target: "post-30-day-nuclear-structure-paper-prospectus"
scope: 135pr/common-response/branch-identifiability/statistical-design
nuclei: [135pr]
observables: [transition-energy, angular-distribution, polarization, rac, mixing-ratio, b-e2, b-m1, lifetime]
tags: [135pr, common-response, branch-profile, holdout, covariance, l3, l4-readiness]
---

# `135Pr` common-response evidence audit 的最小统计合同

## Research Trigger

`135Pr` 的大、小 `δ` 分支来自不同 acquisition、响应和谱系，需要先冻结共同响应合同。

## Grounded Evidence

本页使用 `M15-*`、`L22-*`、`SH26-*` 和 `CH26-B1`–`CH26-B7` 的 source claims。

## Research Question

在统一的 transition identity、响应、门条件、校准和联合协方差合同下，Matta 的大
`|δ|` 分支、Lv 的 `P–R_ac` 小 `|δ|` 分支以及 Sensharma 对旧角分布的条件
`χ²` 偏好，能否支持唯一的 wobbling、tilted precession、signature-partner 或
configuration-mixing 排序？

当前答案只能保持为开放问题。公开材料足以冻结分析设计，不能声称已经完成共同
raw-data 重分析或机制终局裁决。

## Evidence and Lineage

| Dataset | Atomic evidence | Current role | Missing input |
|---|---|---|---|
| Matta 2015 | `M15-3/M15-4/M15-8/M15-10` | Gammasphere angular-distribution 大 `|δ|` 与 INGA `A` | 逐角净峰、响应、`a(E)/Q(E)`、背景和联合 `Σ` |
| Lv 2022 | `L22-3/L22-4/L22-11` | 独立 JUROGAM II `P–R_ac` 小 `|δ|` 分支 | `P–R_ac` 联合协方差、逐门 counts、response 和 feeding |
| Sensharma 2019/2026 | `SH19-*`；`SH26-8/SH26-13/SH26-15` | DGS 连接线和固定 `σ/I=.2` 的条件结果 | event/run ledger、完整 nuisance profile、拟合代码和 Cov |
| Chen 2026 | `CH26-B1`–`CH26-B7` | energy-conditioned model layer | full likelihood、priors、posterior samples、固定 EM 输入和 competing-model evidence |

Matta 与 Sensharma 共享或部分复用 Gammasphere/DGS 谱系，不能按论文数量加权。
Lv 保留为独立 event pool，但其校准和理论解释仍单独记录。`A`、`A_p`、`P` 不是
同一观测量；`δ`、`f_E2`、相对强度和派生 `B` 值也不能重复计票。

## Core Transition Ledger

首轮只冻结三条同时出现在争议链中的连接线：

| Label | State identity | Inclusion rule |
|---|---|---|
| `747` | `17/2− → 15/2−` | 核心 line block；逐实验能量别名保留 |
| `813` | `21/2− → 19/2−` | 核心 line block；作为敏感性 holdout |
| `450` | `19/2− → 17/2−` | 核心 line block；第二外部检查 |

`754/755`、`550/551`、`517/519` 和 `571/571.7 keV` 只有在逐线身份、门条件和
response 对齐后才可加入。近似能量不能自动绑定母态、末态或实验版本。

## Data Contract

实验观测向量应按身份分块：

$$
D=(D_E,D_{\rm AD},D_{\rm pol},D_{R_{ac}},D_I).
$$

- `D_E`：逐态能量、母态/末态、`Jπ`、能量误差和能级协方差；
- `D_AD`：逐角环或角组的净峰 counts，不能只使用图上曲线；
- `D_pol`：`N_\parallel`、`N_\perp`、Compton 门、背景和校准参数；
- `D_Rac`：far/near counts、共同 gate、normalizer 和角度组；
- `D_I`：仅在分支、母态、门和效率定义相同后纳入。

分支参数使用有界角变量：

$$
\xi_j=\arctan(\delta_j),\qquad \delta_j=\tan(\xi_j),
$$

并保留 signed `δ`。离散分支指标可定义为

$$
z_j=
\begin{cases}
S,&|\delta_j|<1,\\
L,&|\delta_j|>1.
\end{cases}
$$

`f_E2=δ²/(1+δ²)` 只是派生变换，丢失干涉符号，不能代替原始 angular-distribution
或 polarization response。

每个 acquisition 使用自己的 nuisance vector：

$$
\eta_d=(\sigma/I,f_{\rm feed},a_0,a_1,Q_0,Q_1,\eta_{ac},
\epsilon_{\rm ring},b_{\rm bg},c_{\rm gate},\rho_{\rm overlap}).
$$

`σ/I`、feeding、background、gate acceptance 和 normalization 默认不跨阵列共享。
同一 acquisition 内可共享校准 nuisance；Matta、Sensharma 和 Lv 不可直接借用
彼此的 `a(E)` 或 `Q(E)`。

## Provisional Reasoning

`ξ=arctan(δ)`、逐 acquisition nuisance 和 profile likelihood 是分析设计，不是
已完成的实验重分析。

## Likelihood and Falsifier

取得 raw counts 后首选 count-level likelihood：

$$
n_{djr}\sim{\rm Poisson}\left[\mu_{djr}(\delta_j,\eta_d,A,M)\right],
$$

其中

$$
\mu_{djr}=\int\epsilon_{dr}(E)R_{dr}(\theta,E)
W(\theta;\delta_j,\sigma_d,f_{\rm feed})\,d\theta+B_{djr}.
$$

若只能取得 summary，才退回：

$$
y_d\sim{\cal N}\left[\mu_d(\delta,\eta),
\Sigma_{\rm stat}+G_{\rm cal}\Sigma_{\rm cal}G_{\rm cal}^{T}
\Sigma_{\rm gate}+\Sigma_{\rm overlap}\right],
$$

并把 Gaussian 假设标为设计假设，而不是实验事实。

每个 branch pattern 先 profile nuisance：

$$
H_b^{\rm prof}=\min_\eta[-2\log L(D\mid\delta,z=b,\eta)].
$$

降低某一分支权重必须同时满足：

1. state identity 和 response contract 相同；
2. background、feeding、alignment、calibration 和 Cov 已 profile；
3. 核心三线的联合 predictive region 不覆盖观测；
4. 通过 bootstrap 或等价覆盖率校准；
5. 结果对 `ρ_overlap`、`σ/I` 和校准协方差稳定。

单线 central `δ`、偏振符号或固定切片的 `Δχ²` 不能单独构成排他证伪。

## Assumptions

raw counts、response 或联合协方差缺失时，不假造 Gaussian covariance，也不把图像
读数升级为事件级数据。

## Competing Explanations

相同的能级、混合比或相对强度趋势也可能来自 tilted precession、signature partner、
configuration mixing 或 response/feeding 处理差异。

## Leave-EM-Out Holdout

训练层只使用预先冻结的能量向量 `D_E` 和 state identity；不得使用 `δ`、`P`、
`A`、`R_ac`、relative E2 ratio 或寿命来选择模型。

- 主 holdout：Lv 独立 JUROGAM 的 `747.3-keV P–R_ac` block；
- 敏感性 holdout：`813.2-keV P–R_ac` block；
- `450.2 keV` 作为第二外部检查，但三条线不计为三次独立实验。

Chen 2026 的 posterior stability只能作为 energy-conditioned model layer，不能
写成 wobbling 相对 TiP/signature-partner 的 Bayes factor。若两个模型的 holdout
predictive regions 重叠，结论是当前公开数据不能区分；若两个模型均不能通过
holdout，结论是模型失配。

## Transfer Conditions

本合同可迁移到其它低自旋 wobbling 争议，前提是重新冻结 transition identity、
response、校准、feeding、Cov 和独立 holdout；本页数值不能直接迁移到其它核素。

## Failure Conditions

若 line identity、event/run lineage、响应或协方差无法闭合，研究停止在 L3 evidence
audit；若 holdout 与训练层共享同一观测量，停止模型间排名。

## Falsification or Reverse Tests

若某一 branch pattern 的联合 predictive region 稳定排除观测，且排除对 overlap、
`σ/I` 和 calibration covariance 不敏感，才可降低该分支权重；若预测区间重叠，反向
结论是当前公开数据不能区分机制。

## Readiness and Stop Rule

没有逐角/逐 gate counts、response、event/run lineage 和联合 Cov 时，P1 停在
L3 public-summary evidence audit。取得 raw/response/Cov 但没有独立 holdout 时，
最多形成方法学稿；只有完整 response/Cov、独立 holdout 和对 nuisance/lineage
敏感性稳定，才可进入完整模型比较。

当前不得声称：

- 已完成 Matta–Lv–Sensharma 统一 raw-data 重分析；
- 已解决大根/小根冲突或排除所有 wobbling；
- 三篇支持链论文代表三次独立实验；
- `A` 可直接转换为 `P`；
- `δ` 或 `f_E2` 等于绝对 `B(E2)`、`B(M1)` 或寿命；
- Chen 2026 摘要级 Bayesian 结果已复现或已提供模型间排他证据。

## Knowledge Impact and Learning Decision

`supports`: 现有 P1 候选已经从“论文题目”推进为一份可在真实输入到达后直接
执行的统计和数据合同。

`limits`: 该页没有生成 synthetic data、没有重拟合公开图像、没有计算 Bayes
factor，也没有改变 `135Pr` 的实验模式判断。

`revises`: 后续所有 P1 数值工作必须先通过 transition identity、lineage、
response、Cov 和 holdout 五道门；重复中心值算术不增加独立信息。

## Open Questions

- 能否取得 Matta、Sensharma 和 Lv 的逐角/逐门 counts、response 与联合 Cov？
- shared Gammasphere/DGS 数据的 event/run overlap 能否量化？
- Lv `747.3-keV P–R_ac` holdout 能否独立检验模型？
- Chen 2026 的 likelihood、prior 和 posterior diagnostics 是否会公开？

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-10-31 | P1 common-response contract audit | none | provisional L3 contract | branch conflict is documented; raw response/Cov and holdout are missing | [[post-30-day-nuclear-structure-paper-prospectus]] |

## Human Review

本页是 Codex self-audit，`review_status: unreviewed`、`reasoning_status: provisional`。
