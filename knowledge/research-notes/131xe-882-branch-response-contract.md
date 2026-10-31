---
type: research-note
title: "131Xe 882-keV混合比分支的联合响应合同"
aliases: [131Xe 882 branch response contract]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [chakraborty-2023-131xe-wobbling-origin, rose-brink-1967-phase-defined-angular-distributions, krane-steffen-1970-cd110-mixing-ratios]
created_from: "Day28 bounded response-contract worker and source audit"
promotion_target: "131xe-low-spin-partner-crosswalk"
tags: [131xe, mixing-ratio, angular-correlation, polarization, l4-readiness]
---

# 131Xe 882-keV混合比分支的联合响应合同

## Research Trigger

[[131xe-low-spin-partner-crosswalk]]保留了Fig.5中881.8-keV线的小δ与负δ大解并存的边界。本页把“什么数据足以选根”写成可执行的输入合同，不把设计条件冒充已有实验结果。

## Grounded Evidence

| Evidence | source / locator | provenance | limitation |
|---|---|---|---|
| 881.8-keV线为1046.0-keV 13/2−→11/2−，RDCO=0.64(11)，偏振栏为空 | [[chakraborty-2023-131xe-wobbling-origin]] C23-D28-9 | Table I, printed064318-3 | 表只称stretched-E2 gates，未列实际角对和响应 |
| Fig.5给小解δ=0.09(8)，负δ区尚有第二交点 | 同source C23-D28-3、C23-D28-9 | Fig.5, printed064318-4 | 视觉交点不提供另一根精确值、权重或置信度 |
| 相干M1/E2角分布、线偏振、级联布居和δ约定依赖统计张量、接受度与相位合同 | [[rose-brink-1967-phase-defined-angular-distributions]] RB67-11、RB67-D23-001、RB67-D23-003；[[krane-steffen-1970-cd110-mixing-ratios]] KS70-2、KS70-6 | printed316/318/319及KS70 Eqs.3–15 | 原方法论不提供本装置的实际响应系数 |

## Provisional Reasoning

### 目标和输入边界

目标跃迁的信号bin可在实M1/E2、线性响应的限定下写成

\[
q_i(\delta,\eta)=\frac{a_i(\eta)+2b_i(\eta)\delta+c_i(\eta)\delta^2}{1+\delta^2},
\qquad
\mu_i=Y_gq_i+B_i+\lambda_gT_{880,i}.
\]

系数必须由实际clover/crystal、角对、有限几何、取向/feeding、效率和相位约定积分得到；不能用三个名义探测角替代。880.1-keV双线应作为逐门污染组分，不能把其峰面积忽略或假设为固定常数。

最少真实输入包括：逐门峰形和sideband背景、能量漂移与双线分辨、所有角对和级联顺序、实际探测器接受度/成对效率、上游取向与feeding、882的parallel/perpendicular scatter-bin计数、未偏振校准`a(E)`与分析响应`Qeff`或完整Stokes响应、ANGCOR版本与输入、共享校准协方差。若使用压缩的RDCO/asymmetry，必须提供联合Σ，不能把原计数和派生比值重复放入似然。

### 两分支的条件分离

任一同选样ratio可写为

\[
X(\delta,\eta)=\frac{a+2b\delta+c\delta^2}{A+2B\delta+C\delta^2}.
\]

对于小、大分支代表值`δs`、`δl`，在同一η且分母为正时，

\[
X_s-X_l=
\frac{(\delta_s-\delta_l)\{2(bA-aB)+(\delta_s+\delta_l)(cA-aC)+2\delta_s\delta_l(cB-bC)\}}{D_sD_l}.
\]

花括号可以为零，所以“δ不同”本身不保证某个偏振或角分布比值能选根。真实比较应构造基线数据允许的分支可行集合`F_b`，再把新观测和其误差集合映射为预测集合`P_b`。若一个标量观测的包络满足`U_small<L_large`或反向不交，则是充分分离条件；包络相交不能证明完整非凸集合相交。

局部近似下，先白化两分支均值差`Δ`，再剔除共享nuisance方向`H`，可用

\[
d_{\rm prof}^2=z^\mathsf{T}[I-H(H^\mathsf{T}H+\Lambda)^\dagger H^\mathsf{T}]z,
\qquad z=V^{-1/2}\Delta.
\]

这里`V`、`H`和校准约束精度`Λ`必须来自真实数据；没有它们不报告σ、likelihood ratio或“最优偏振精度”。

### Companion选择和不可迁移控制

预先在可实现的偏振/角bin候选中最大化两分支经nuisance剖面后的最坏距离。704.6-keV的13/2−→9/2−竞争退激可作为同一1046-keV母态的取向参考，但它不能与882作双符合，且其E2纯度和响应必须独立约束。671属于另一母态，1055属于另一跃迁和历史AD条件；两者的符号/asymmetry不能直接替代882观测。

## Assumptions

采用实M1/E2振幅作设计参数化；高阶多极只在明确误差界内省略；门选样和校准数据在各假设内共享；污染、背景、效率、取向和相位均作为联合模型参数或受约束的输入；所有响应协方差保持PSD。

## Competing Explanations

大解可能是RDCO有限响应下的真实分支，也可能被双线污染、取向/feeding、角对选择或相位约定改变。新偏振若与两分支预测集合重叠，结论仍可能是数据不足，而不是某一物理模式获胜。小δ中心值不能单独升级为signature partner的排他证据。

## Transfer Conditions

合同可迁移到其它有混合比双解的γγ角分布问题，前提是保留逐bin计数、共享响应、污染路径、统计张量和联合校准；不能把抽象系数或本核的名义角度直接移到其它阵列。

## Failure Conditions

880污染无界、偏振轴符号未知、`Qeff`为零或未标定、ratio分母接近零、分支差落在nuisance切空间、门选不一致、未建模高阶多极/复相位、或重复使用共享事件和校准数据，都会使分离判断失效。必要的物理约束（偏振绝对值≤1、密度矩阵PSD且trace=1、非负信号bin）不能单独保证可辨识。

## Falsification or Reverse Tests

若在真实共同响应和基线可行集合下所有候选companion的经剖面预测集合均相交，则“存在一个仅凭该观测稳健选根的最小设计”被否定，应继续获取原始计数或改变观测。若集合不交，也只能支持该特定响应合同下的分支排除，不自动证明wobbling或signature partner。

## Open Questions

真实881/880峰形、实际角对、取向和偏振校准是否保存？C23使用的ANGCOR输入与δ符号如何映射到RB/KSW？704.6参考线是否具有足够统计量和已核E2纯度？这些缺口使本页保持L4 readiness而非事件级L4结果。

## Human Review

- Review scope: worker解析合同与父任务C23图表抽查。
- Decision: provisional；未发生human review。
- Complete unresolved P0/P1 inventory: 科学P1为真实逐门响应、880污染和联合协方差；不生成代理计数、根值或显著性。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-10-30 | 882双分支响应合同 | worker output | provisional research-note | 论文图表确认双解边界；输入缺口禁止事件级重拟合 | [[131xe-low-spin-partner-crosswalk]] |

复现入口：[worker分析](../../outputs/learning-daily/20261030-DAY28-independent-l3-research-week-four-exam-run-01/workers/882-contract/note.md)、[机器输入合同](../../outputs/learning-daily/20261030-DAY28-independent-l3-research-week-four-exam-run-01/workers/882-contract/input-contract.json)、[验证回执](../../outputs/learning-daily/20261030-DAY28-independent-l3-research-week-four-exam-run-01/workers/882-contract/verification.json)。
