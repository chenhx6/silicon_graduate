---
type: research-note
title: "SE21 的 135Pr 对齐校准：张量定义与实际参数层的条件一致性"
aliases: [SE21 alignment calibration consistency]
created: 2026-10-17
updated: 2026-10-17
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [sensharma-2021-wobbling-motion-135pr-187au, yamazaki-1967-aligned-angular-coefficients, rose-brink-1967-phase-defined-angular-distributions, krane-steffen-1970-cd110-mixing-ratios, der-mateosian-sunyar-1974-attenuation-coefficients, der-mateosian-sunyar-1974-angular-coefficients]
created_from: Day15 daily-learning uncredited Day16 preview
promotion_target: angular-distribution
tags: [135pr, alignment, calibration, angular-distribution, positivity, provisional]
---

# 先核准 attenuation 的含义，再用它限定混合比

## Research Trigger

[[sensharma-2021-wobbling-motion-135pr-187au]] SE21-9/10 同时给出了核对齐的定义和实际参考线校准。问题是表列 alpha_exp 是否已能直接当作同一核布居的 rho/B，还是还混有响应、归一或参考跃迁的约定。本页只检验这一条件，不裁决其原实验数据或 wobbling 指认。

## Grounded Evidence

本次实际定向阅读 2021 thesis 的方法、相关校准/角度表，保留其与 Springer2022 书的版本区别：

| 输入 | 原件值与定义 | 精确入口 |
| --- | --- | --- |
| nuclear attenuation | αk=ρk/Bk；半整数 complete reference 为 \|M\|=1/2 | SE21-9，printed41–42/PDF63–64，Eqs2.45/2.49/2.50 |
| Gaussian | P(M)∝exp[−M²/(2σ²)]；σ为指数width | SE21-9，printed42/PDF64，Eq2.51 |
| calibration参考 | 854.3keV，23/2−→19/2−，作者采用pureE2近似 | SE21-10，printed97/Table4.1与printed109/Table4.3 |
| 表列 attenuation | α2=.92(5)，α4=.30(1)，adopted σ/J=.2 | SE21-10，printed97/PDF119，Table4.1 |
| 同线拟合系数 | A2exp=.352(1)，A4exp=−.212(1) | SE21-10，printed109/PDF131，Table4.3 |

原始逐 ring 峰与背景、complete fit covariance、实际校准操作和 production code 未得。表的误差不在本页被重新解释为完整高斯分布或某个联合置信区间。

## Provisional Reasoning

### 按相同 rho/B 定义的精确正布居检查

由 [[yamazaki-1967-aligned-angular-coefficients]] YA67-13 与 SE21 Eq2.45/2.50，对 J=23/2、S=J(J+1)、h=1/2，定义

$$t_2(m)=\frac{3m^2-S}{3h^2-S},\qquad
t_4(m)=\frac{35m^4-(30S-25)m^2+3S^2-6S}
{35h^4-(30S-25)h^2+3S^2-6S}.$$

若 αk=Σm P(m)tk(m)、P≥0 且 ΣP=1，则每个允许 m 都满足

$$7-10t_2(m)+3t_4(m)
=\frac{105(m^2-\tfrac14)(m^2-\tfrac94)}
{3(S-\tfrac34)(S-\tfrac{15}{4})}\ge0.$$

因为允许的半整数 \|m\| 为 1/2、3/2、5/2…，分子逐项非负。由凸性得到必要条件

$$7-10\alpha_2+3\alpha_4\ge0.$$

本 run 用新输入 J=23/2 的逐 m 有理 CG 与独立 Stevens 多项式比较，并用线性规划核对；复用已有通用 helper，没有重跑旧的 67Ga 数据或沿用旧检查数加分。必要式针对任意 positive P，不限 Gaussian。

源 Table4.1 的字面 mean 给 −1.3。将 quoted margins 仅当作 rectangle，其最大值仍为

$$7-10(.92-.05)+3(.30+.01)=-.77.$$

独立 LP 对 mean 和这个 rectangle 都返回 infeasible。这是定义条件下的集合不相交，不是实验显著性检验。没有联合 coverage，未知 covariance 也不被补成零。

在 α2=.92 时，必要 α4≥11/15≈.733333；在 α4=.30 时，必要 α2≤.79。这些是该条件模型的必要阈值，不能替换成对实验系数的新建议值。

### 单参数 Gaussian 也不闭合

| source-defined 条件计算 | α2 | α4 |
| --- | ---: | ---: |
| adopted σ/J=.2 | .894266 | .689096 |
| 只匹配 α2=.92，得到 σ/J=.175284 | .920000 | .756606 |
| 只匹配 α4=.30，得到 σ/J=.350794 | .673420 | .300000 |

这三行不是重新测得的 σ。采用 width=2.3 时，有限离散布居的 RMS=2.299995；数值接近不改变两者在一般有限 J、窄 width 下的不同定义。半整数 σ→0 应取 \|M\|=1/2 的极限，不能直接计算零除指数。

### 同一参考线的第二张表也须经过转换

为避免只凭一份张量实现作判断，另取 complete reference 的 M=±1/2，用 doubled-spin CG 算 pureE2 的 photon-mass μ 分布：

$$p_{\mu=-2,\ldots,2}
=(15/322,\ 40/161,\ 66/161,\ 40/161,\ 15/322).$$

在 [[rose-brink-1967-phase-defined-angular-distributions]] RB67-11 的横向光子基底下，纯 E2 的 μ=0、\|μ\|=1、\|μ\|=2 的 (A2,A4) 分别为
(5/7,−12/7)、(5/14,8/7)、(−5/7,−2/7)。
它们给本参考的

$$A_{2,\max}=65/161,\qquad A_{4,\max}=-26/161.$$

用 Eq2.51 的 Gaussian 作完整 CG 求和，与 αkAk,max 独立闭合，得到 (.361039,−.111283)。若将 Table4.3 的 .352/−.212 当作这个 pure-point convention 下的系数相除，得到 (.871877,1.312769)，并不是 Table4.1 的 (.92,.30)。

这里没有把仅验证过整数 spin 的混合光子计算核用于半整数；本段是明确的 doubled-spin、single-pure-E2 检查。也没有拟合实际 E2/M3 干涉、detector acceptance 或门条件。它增加了“必须先核参数层”的证据，不定位作者实现中的原因。

![相同张量定义下的条件校准域](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-se21-alignment-region.svg)

图中绿色为 positive-P 凸包、蓝线为 source-defined Gaussian family，方块标 adopted .2；橙色点及横纵 margins 为源 Table4.1。误差棒没有被赋联合置信水平，图的 nuclear-only 约定与 unresolved gate/response 条件已显式标注。

## 1974 primary 的定向复核

[[der-mateosian-sunyar-1974-attenuation-coefficients]] DA74-5–7 的原Eq4–6采用同一个rho/B、half-integer reference与2sigma²指数。printed400 TableII J23/2 .2的原数.894266/.689096、printed405 AppendixB .40373/−.16149在末位舍入内确认本页计算，未发现可用不同sigma命名消除条件失配的依据。论文称half-width，仍须按其指数，不自动转成HWHM。

[[der-mateosian-sunyar-1974-angular-coefficients]] DMS74-5–7是相邻的另一个work；其Ji6→5例题使用negative delta列，source-native程序正负控制复现了作者的maximum/attenuation/partial coefficients。两篇与Yamazaki共享theory谱系，并不是独立采集或SE21真实程序的副本。当前最需要的仍是SE21 actual alpha_exp提取层，不能把primary理论表匹配当作找到了实验错误。

## Competing Explanations

- alpha_exp 的实际提取可能还包含不同的 reference、有限响应、归一或表记操作；必须取得该层定义才能把它转换为 ρ/B。
- 854.3 参考的原文还报告小 E2/M3 成分。少量高阶辐射强度仍可能通过线性干涉影响较小的 A4，不能只因 δ² 小便认证 exact pureE2。当前未计算这项实际干涉或认定它解释了差异。
- quasi-isotropic gates、方向依赖 postselection、逐 ring 效率或背景处理可能使拟合系数不对应同一 unconditional nuclear density；这些不是本页已经定位的故障。
- 仅把 Gaussian 换成其它非高斯 positive P，不能消除同一 ρ/B 定义下的必要式失配。应先审定义和响应层，再讨论 feeding 形状。

## 有界反证：参考线的小 M3 分量

这部分按 [[sensharma-2021-wobbling-motion-135pr-187au]] SE21-12 的两个 source 配置，保持 J=23/2→19/2、sigma/J=.2、axisymmetric diagonal Gaussian 和 point single-gamma geometry，只加入 E2/M3 两个真实辐射振幅。未包含实际 γγ gate/acceptance、Doppler/aberration、背景或 Cov；也不通过新拟合改变源 δ 或 σ。

模型用 SE21 Eq2.42/43 的 generalized F 与独立 RB 直接光子振幅两路。Nuclear CG 与 Racah 6j 全部以 doubled integers 计算；photon μ=Mi−Mf 与 helicity λ=±1 分开。归一化混合振幅的总辐射率对每个 M 都为一。[[krane-steffen-1970-cd110-mixing-ratios]] KS70-13 与 [[rose-brink-1967-phase-defined-angular-distributions]] RB67-6/11 给出 adjacent-rank 的 native/RB 坐标映射，改坐标时振幅和系数矩阵同时变换，观测量保持。

在该约定下，δ 为高阶 M3 对低阶 E2 的辐射振幅比。Gamma fraction δ²/(1+δ²) 只是强度份额，角系数还有线性干涉：

$$A_k(\delta)=\frac{a_k+2b_k\delta+c_k\delta^2}{1+\delta^2}.$$

Primary pureE2、D/Q作者例题、pureM3极限、uniform isotropy、theta镜像、逐M归一均通过；source-F与直接振幅最大差约1.0×10⁻14，12/16-node quadrature差约1.05×10⁻14。这些是两条实现路线及物理控制，不是两场独立实验。该实现仅检查过这里的J=6→5 D/Q与23/2→19/2参考案例，不认证任意half-spin joint response。

| 源配置与 native δ | M3辐射份额 | 模型 A2 | 模型 A4 | 模型 A6 |
| --- | ---: | ---: | ---: | ---: |
| below659.8 gate，−.04 | .1597% | .313673 | −.147476 | .00026676 |
| singles，−.06 | .3587% | .289881 | −.165429 | .00059901 |

PureE2的模型A4为−.111283。因此很小的高阶强度仍能通过振幅干涉明显改变A4，不能只看百分比判断它可忽略。源 two configurations 分开保留，不能把它们当成同一条件下的独立重复。

将源 δ±误差只当作字面参数区间，gated [−.05,−.03] 的 A4像为 [−.156469,−.138456]；singles [−.07,−.05] 的像为 [−.174351,−.156469]。这些不是置信区间；在当前固定 point/Gaussian 模型内未到 Table4.3 的 −.212，不能说这项机制已经解释了该表。

另把 source TableA.2 的七个 average angles 当作点，使用**自选等权、无噪声**的 free-scale/P2/P4 projection 检验遗漏 P6。gated/singles 的 A4移位仅−2.28×10⁻5/−5.13×10⁻5；这不是实际 ring weights、有限角接受或实验 Cov 的重放，不能当成实际系统误差上限。

### 计算后的 scope 反例

真实核布居不因参考 γ 的混合比改变，仍给 alpha=(.894266,.689096)，必要式值为+.124626。保持所有operators固定，另选**物理相位控制** δ=+.04；若把它的辐射系数误除 pureE2 maximum 系数，会得到

$$\widetilde\alpha=(1.009932,.464384),\qquad
7-10\widetilde\alpha_2+3\widetilde\alpha_4=-1.706165.$$

该 reference 的布居、发射率和方向强度均物理有效。失配由错误的纯性反演前提制造，说明不能把 apparent alpha 的核正性失败直接称为“不物理实验数据”。这是在已计算的 opposite-phase control 上追加的数学反例，未对源数据调参；+.04不是原文报告的负号，也不是只改 KS/RB坐标名。同一物理振幅作坐标改写时，所有观测保持。

这并未复现原 Table4.1 的提取过程或证明它的具体原因。对源中报告的负号配置，M3 alone 与当前点模型仍未闭合 Table4.3。按预设停止条件，到此停止用自由参数补齐；producer normalization、reference处理、gate/geometry和Cov仍待实际输入。

[新模型脚本](../../system/scripts/day16_se21_m3_reference.py)、[冻结合同](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-se21-m3-reference-input.json)、[全部矩阵/区间/设计结果](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-se21-m3-reference-model.json)、[运行回执](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-se21-m3-model-receipt.json)保存可复算链；真实实验 L4 仍 not-ready。

## Assumptions

检验采用固定 J=23/2、同一 complete reference、同一核布居与 normalized tensor 定义。source error margins 只作字面矩形。source raw、old claims 和 review flags 不变；结果不进入实验 L4。

## Knowledge Impact and Lifecycle

判断为 limits 直接把 Table4.1 的 alpha_exp 传给后续 δ 的 Gaussian prior；supports 先用同阵列参考控制闭合参数定义。不是对所有 angular-distribution δ、135Pr 数据或某个集体模式的整体否定。

[脚本](../../system/scripts/day16_se21_alignment_audit.py)、[冻结输入](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-se21-alignment-input.json)、[有理证书/LP/CG结果](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-se21-alignment-audit.json) 和[图QA](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-se21-figure-qa.json)保存完整过程；定义、数据、证明及边界已在本页。

## Transfer Conditions

可迁移的是共用定义后检查 coefficient feasibility 的方法。整数 spin 的 reference、缺失 rank4 的低 spin、不同核态或不同 response correction 须另写，不直接复制本例数值或半整数参考。

## Failure Conditions

若作者的 alpha_exp 不是 Eq2.49 的核 ρ/B，或两表已用不同 normalization/geometry 操作，本例不能按同一核布居解释它们。取得该变换并闭合后，应修订本页的具体应用，而保留正性检查方法及历史。

## Falsification or Reverse Tests

优先核 SE21 Ref26 的 attenuation 提取规则和 Ref56 的 σ/J 表，再对照实际所用校准程序；这些引用本身不是已经读到的正文证据。随后需要 854.3 的 singles/相同 below-gate 逐角净峰、背景、效率及其 joint covariance，分别复算 measured A、reference coefficient、geometry factor 和 nuclear α。

## Open Questions

Table4.1 与 Table4.3 的确切归一层能否从 method primary 或实际程序恢复？固定point/Gaussian下的small E2/M3已按上文有界评估，actual gate/response中如何进入alpha提取仍未闭合。完整校准 Cov 是否存在？这些问题由当前研究继续追踪，不自动转成用户待办。

## Human Review

Codex self-audit，仍 unreviewed/provisional；没有新 human-reviewed 或作者代码错误认定。

## Promotion or Rejection History

2026-10-17：Day15窗口内的Day16无学分预习创建，以新原件行作条件检查。图的首次碰撞审计捕捉到 off-viewport polygon stroke；仅裁切显示几何后通过，数值不变。所有原始 PDF 保持，Day16不授卡。

2026-10-17追加：1974 primary定义/表列正负号控制与有界single-gamma M3 forward通过，原定义条件证书保留。新增apparent-alpha scope反例限制对实际数据的因果推断；未通过自由sigma/delta调参解释原两表，不晋升为实验L4或human review。
