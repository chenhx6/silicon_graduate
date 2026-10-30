---
type: research-note
title: "跨谱仪系统误差：实际测量合同、偏振校准与寿命输入边界"
aliases: [cross-instrument-systematics-and-methodological-degeneracy, Spectrometer systematics Day 27]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [garg-2015-135pr-magnetic-rotation, garg-2019-135pr-polarization-erratum, roy-2011-cd110-systematics-antimagnetic, rather-2014-104pd-antimagnetic-arxiv-full, odegard-2001-evidence-wobbling-163lu]
created_from: Day 27 spectrometer-systematics worker; cross-instrument systematics and pseudo-degeneracy modeling
tags: [spectrometer, gammasphere, euroball, agata, jurogam, polarimetry, dsam, rdds, systematic-errors, pseudo-degeneracy]
---

# 跨谱仪比较必须绑定实际测量

## Research Trigger

Day27 原稿为各阵列给统一 Q(662keV) 和寿命误差排名，并把 135Pr 勘误解释为从错误纯 M1 到另一机制的裁决。这些量没有逐配置/选事例合同。续研撤回原通用精度表、固定 2% 失效线及把 80fs 侧馈送当真实实验结果的说法。

## Grounded Evidence

[[garg-2019-135pr-polarization-erratum]] 原 PDF pp.1–2、Table I 直接给出：747.5keV 的 A 从 −0.05(3) 修正为 +0.03(3)，813.3keV 从 −0.20(8) 修正为 +0.04(3)；两线均列 M1+E2，没有给 δ 或绝对寿命。813.3keV 母态 Ei=2204.4keV、21/2−→19/2−；747.5keV 母态 Ei=1478.2keV、17/2−→15/2−。这些身份优先于“MR文章中的线”这一不精确标签。

[[garg-2015-135pr-magnetic-rotation]] §III.B/C 区分低自旋侧带连接和高自旋 possible-MR 级联；原稿把低自旋 813keV 连接当成 MR 带内跃迁的推理撤回。[[sensharma-2026-evolution-chirality-transverse-wobbling-135pr]] SH26-2/3/8/12 区分 DB2→DB1 小 δ 新连接与旧 side→yrast 大 δ 争议；不得相互替换。

## Assumptions

在固定的散射方向和正 Q 约定下，

\[
A=\frac{aN_\perp-N_\parallel}{aN_\perp+N_\parallel},\qquad P=A/Q.
\]

a 是几何计数校准，Q 是选定散射事件、探测结构与分析门对应的灵敏度。数组名称不是 Q 的充分定义。A、P、δ、E2 光子份额 δ²/(1+δ²)、绝对 B(E2) 分属不同推断层。

对固定散射计数比 r=Nparallel/Nperp，有

\[
\frac{\partial A}{\partial\ln a}=\frac{1-A^2}{2}.
\]

因此近零 A 的 2% 校准扰动会给约 0.01 的绝对 A 变化；它是否改变结论取决于原计数、Q、不确定度、取向和混合分支，没有统一“2%即失效”门槛。这是公式的条件微分，不是重分析实验。

## Provisional Reasoning

勘误给新 a(E)=1.01229+1.17083×10⁻⁶ E(keV)。在明确保持原散射计数比不变的条件下，将旧 a=0.93、旧 A=−0.20 代入可得 r=1.395，再用新 a(813.3)只能得到 A约−0.159，不能得到报告的+0.04。这只表明“固定计数且仅改 a”的简化重放不足；不据此断定未公开的重提取、探测器选择或背景处理发生了何种错误。原始逐探测器计数和处理合同仍缺。

## Lifetime and Detector Comparisons

| 要比较的对象 | 至少需要的输入 | 不能由阵列名称推出的结论 |
| --- | --- | --- |
| 极化 | 同线 spin/门、a(E)、Q(E)、散射角接受度、背景与计数协方差 | 固定的 Q 排名或纯 M1/E2 比例 |
| DSAM | 反冲运动、靶/背衬、阻止本领、线形响应、feeding、效率与门 | 统一的 3–5% 或 10–15% 精度 |
| RDDS | 实际距离、速度、移位/未移位强度、门角色、分辨率与侧馈送 | 柱塞名称对应固定距离或寿命精度 |
| 跨实验联合比较 | 同母末态身份、源谱系、单位、校准与 nuisance 合同 | 论文数等于独立测量数 |

[[roy-2011-cd110-systematics-antimagnetic]] 与 [[rather-2014-104pd-antimagnetic-arxiv-full]] 的寿命和 AMR 推断，应回各自 DSAM/模型条件；没有在本续研中证明它们受到 80fs 假侧馈送支配。旧脚本的 80fs 是合成情景。

### 跨阵列似然合同与多跃迁协方差解（Day 27 Continuation）

详见专门研究笔记 [[cross-array-polarization-likelihood-contract]] 与求解脚本 `system/scripts/day27_cross_array_polarization_likelihood_contract.py`：
1. **谱仪名称精度排名的彻底破除：** 求解表明，具有较低灵敏度（$Q=0.20$）但高曝光量（$N=100\text{k}$）与精密刻度（$\sigma_a/a=0.5\%$）的经典阵列（如 Gammasphere 150h），其 Fisher 信息量（$I_F=56.21$）与贝叶斯因子显著超越高灵敏度（$Q=0.28$）但统计量受限（$N=4\text{k}$）的跟踪阵列（$I_F=5.89$）。实验精度属于全似然合同 $\mathcal{L}(\delta \mid \mathbf{D}, \mathbf{C})$，而非谱仪名称。
2. **多跃迁正协方差：** 共享几何刻度比 $a(E)$ 与灵敏度标定 $Q(E)$ 使同带内跃迁的偏振测量产生高达 $\rho_{12} \approx 0.40$ 的正相关；忽略该协方差会虚假缩小联合误差椭球短轴。
3. **双峰似然与非高斯性：** 在偏振显著性受限时，$\mathcal{L}(\delta)$ 表现为小 $|\delta|$ 与大 $|\delta|$ 的双峰极大值（相对高度 $1.00$ 与 $0.21$）；强行以高斯单峰报道会造成对另一模式分支的假性排除。

## Competing Explanations

保留真实模式变化、同组态混合、错误分支、背景与响应偏差的竞争路线。对同母态的不同 γ 分支，可先使用寿命消去比值检验结构模型；共同校准、弱分支与混合比的相关性仍保留。相同正 A 可以对应不同 δ 分支，必须结合实际角分布与取向输入。

## Promotion or Rejection History

- 2026-10-29 初版将说明性谱仪参数、误差和侧馈送情景写成通用事实。
- 2026-10-29 续研撤回上述认证；保留原工件作为未校准情景，使用实际跃迁和校准合同重新组织问题。

## Agent self-audit triage

P0: none identified after isolation。无未隔离凭据/原件风险。P1：原计数缺失，跨实验 line identity、误差与模型对照未闭合；勘误的已发表修正值与条件重放差异分开记录。P2/P3：未改变 source 的 human-review 状态。

## Transfer Conditions

跨装置比较要绑定实际配置、散射角、选事例、校准、门和背景；同线/同母态关系先于统计合并。

## Failure Conditions

只有阵列名或示意参数时，不能给其统一Q或精度排名；原计数不可得时只报告条件重放。

## Falsification or Reverse Tests

用同一散射计数比检查仅改变a能否重放修正值；若不能，记录所缺计数/背景/探测器选择合同，不推定未公开处理细节。

## Open Questions

原计数和逐探测器选择的哪些变化能重放勘误？在共同响应下，两条δ分支的似然与强度网络能否同时检验？

## Human Review

本轮没有人工审核事件；修订未清除source页已有needs_review。
