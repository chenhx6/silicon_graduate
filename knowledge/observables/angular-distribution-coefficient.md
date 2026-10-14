---
type: observable
title: 角分布系数
aliases: [angular distribution coefficient, angular-distribution coefficient, A2, A4, Legendre coefficient]
created: 2026-07-08
updated: 2026-10-15
status: ai-draft
review_status: unreviewed
observable_kind: gamma-angular-distribution-observable
symbol: A2, A4
units: dimensionless
tags: [angular-distribution, mixing-ratio, alignment, pado-support]
---

# 角分布系数（Angular-Distribution Coefficient）

## Definition

γ 射线角分布常写为 Legendre expansion。对 stretched E2 case，[[draper-1970-gaussian-substate-side-feeding]] 使用 `W(θ)=1+A2P2(cosθ)+A4P4(cosθ)`，其中 `A2` 与 `A4` 是待解释或拟合的角分布系数。

Diamond 1966 uses the same Legendre form for stretched-E2 cascades and compares measured `A4`--`A2` points with a Gaussian `m=0` alignment reference. The reported deviations are part of the evidence boundary: a Gaussian can organize a calibration comparison without being an exact residual-population law.

## Dependence

`A2/A4` 不是单纯的 transition label。它们依赖 emitting level 的 magnetic-substate population、spin sequence、multipolarity/mixing ratio、feeding history 和 detector/analysis treatment。

## Relevance to P-ADO

在 P-ADO mixing-ratio extraction 中，`A2/A4` 或等效角分布响应与 polarization observables 一起约束 `δ`。如果 alignment 或 substate population 参数被强行固定，`δ` 的 branch selection 和置信区间可能被系统性影响。

## How It Is Obtained

由不同探测角度的 efficiency-corrected γ-ray intensities 拟合 Legendre polynomial expansion 得到。

## Diagnostic Use

用于约束 transition multipolarity、mixing ratio 和 emitting level alignment/population assumptions。

## Model Dependence

系数依赖 spin sequence、multipolarity/mixing ratio、magnetic-substate population、feeding history 和 detector/analysis corrections。

## Failure Modes and Ambiguities

alignment 未知、side feeding 未处理、Doppler broadening、弱峰污染或不同实验条件混用都可导致错误的 `δ` branch 或过窄误差。

## Sources

- [[draper-1970-gaussian-substate-side-feeding]]
- [[zobel-1980-magnetic-substate-distributions]]
- [[zobel-1983-energy-projectile-alignment]]
- [[diamond-1966-nuclear-alignment-heavy-ion-reactions]]


## 拟合系数、核取向与最大辐射系数的层级

[[zobel-1983-energy-projectile-alignment]] Z83-1（printed p.389，Eq.(1) 与 Eq.(2)）明确区分归一辐射强度中的 `A_k^exp` 与核取向系数 `α_k`：`A_k^exp=α_k A_k^max(I_i,I_f,δ)`。以下 β 表达是本任务为说明拟合归一而选择的参数化，不是源文新增公式或 GF 源码。

| 量 | 本节定义 | 应保存的条件/误差 |
| --- | --- | --- |
| β0、β2、β4 | 未归一拟合 `I(θ)=β0+β2P2+β4P4`；与I同单位 | 三参数 Cov，β0不能默认为无误差 |
| A2exp、A4exp | `A_k^exp=β_k/β0`；`W=1+Σ A_k^exp P_k` | 归一 Jacobian 与β0交叉项 |
| c_k=A_k^max | 同spin sequence、multipolarity、δ约定下的最大取向参考辐射系数 | 参考取向、δ符号及其不确定度；不是所有核的固定数 |
| α2、α4 | `α_k=A_k^exp/c_k`；核取向张量相对该参考的比值 | c非零、同initial level、feeding/布居假设；不等于Gaussian宽度 |
| detector attenuation / acceptance | 探测立体角与选择响应的量 | 阵列/门/校正约定；与核α分别保存 |

前述源文的“maximum alignment”指定参考布居，不是可无条件套用的数值上界。更换spin、δ、参考张量或conditional gate会改变问题；c_k=0时该阶不能通过除法识别α_k。有限几何可在适用的单γ响应下引入自己的衰减因子；一般γγ门须使用[[angular-correlation]]的joint response，不能把门响应一律并入核α。[[attenuation-coefficient]]已有核α、探测几何因子与超精细Gk的区分，本轮核对后保留其既有定义。

### 条件转换与Cov的坐标不变性

原表数据是 Z83-11 / printed p.392 Table1 的958.0-keV、13/2+→9/2+、alpha11.3-MeV列：α=(.973,.803)，quoted statistical errors=(.037,.090)。Z83-12 / p.393保留其统计相关性但未给数值Cov。

本任务沿[[angular-distribution]]“角采样与归一化下的Cov可识别性”的CG/Legendre推导，固定pure E2、point response与complete-alignment参考，取 c=(40/91,−216/1001)。条件转换得到 Aexp=(.427692308,−.173274725)，对应marginal errors=(.016263736,.019420579)。这些是由源表与声明模型算出的量，不是新取得的原文实测表列或真实joint fit。

固定c且D=diag(c2,c4)时：

\[
\Sigma_A=D\Sigma_\alpha D^{\mathsf T},\qquad
\rho_A=\operatorname{sign}(c_2c_4)\rho_\alpha,\qquad
r_A^{\mathsf T}\Sigma_A^{-1}r_A
=r_\alpha^{\mathsf T}\Sigma_\alpha^{-1}r_\alpha .
\]

选择ρ_α=+.6仅作坐标控制，ρ_A=−.6；chosen comparison α=(.90,.72)在两坐标中的Mahalanobis平方都为3.999519931。该数没有实验显著性含义；真正ρ仍未知。相关符号改变不会改变正确转换后的物理相容性。

把α直接写入W的反事实，在0/90度给(2.776,.814625)，正确条件转换给(1.254417582,.721175824)。两式均有球平均1、全角域均为正；所以归一/非负不能替代变量语义和来源定位。

### 归一与模型参数误差

对 a_k=β_k/β0，delta-method梯度含 `∂a_k/∂β0=−a_k/β0` 和 `∂a_k/∂β_k=1/β0`。共同整体scale在归一后一阶取消，不同角度、不同run、β0的cross covariance仍须保留。若c(δ)也不固定，还要对 `(α,δ)` 或其它joint nuisance传播；仅用固定D不会包含δ或acceptance系统误差。局部线性传播也不保证弱β0、非Gaussian likelihood或离散spin假设的区间覆盖。

复算脚本：[day14_angular_coefficient_conventions.py](../../system/scripts/day14_angular_coefficient_conventions.py)。17项检查覆盖独立CG系数、Cov/逆变换、联合距离不变、ratio Jacobian、scale/归一cross项、全域语义反例与chosen c误差控制。全部自设ρ、β covariance、comparison和c-error仅为L2练习，不补作者GF矩阵、193Bi response或新σ/I。此为Day14中的Day15无学分知识预习；正式周考21/24保持，源页继承人审范围不扩。
