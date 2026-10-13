---
type: method
title: γ-γ 符合分析
aliases: [gamma-gamma coincidence, γγ coincidence, coincidence spectroscopy]
created: 2026-07-01
updated: 2026-10-14
status: active
review_status: unreviewed
method_type: gamma-ray-spectroscopy
tags: [level-scheme, in-beam-spectroscopy]
---

# γ-γ 符合分析（Gamma-Gamma Coincidence）

## Purpose

通过跃迁之间的符合关系建立能级纲图、级联和分支。

## Inputs and Assumptions

时间戳事件、能量刻度、符合窗、本底和双峰处理。

## Procedure

构造对称/非对称矩阵或更高维立方体，在已知或新跃迁上设门并检查互相符合与反符合。

## What It Can Establish

跃迁级联关系、能级放置和双峰分解的支持证据。

## What It Cannot Establish Alone

不能独立给出自旋宇称或电磁性质。

## Conventions and Systematics

必须记录门能量、污染峰、随机符合和效率。

## Examples

`131Xe` 中 930 keV 门同时观察 816/1055 keV，支持二者来自同一 1862 keV 态；880/882 keV 双峰通过不同门的峰心差异处理。

### Day12 gate-and-background audit: `137mBa`

对弱双光子/γ级联信号，单看 `E1+E2` 接近能级差并不足以证明有两束独立光子：一束 γ 在探测器间 Compton 散射也能留下相同能量和；无关 singles 偶合可形成随机和峰；相邻能级 cascade 也可能给相近总能量。可复用的门控次序如下。

| 步骤 | 门与对照 | 检查目标 | 当前可保留的边界 |
|---|---|---|---|
| 1. 定义事件 | 建立时间戳 `γ-γ` 矩阵；用已知 prompt cascade 标定本实验 prompt-time window，若研究异构态衰变则另定义 delayed window | 确认两个能量来自同一触发/时间关联，避免把 source lifetime 当作探测窗 | 时间窗必须按该阵列的 time resolution 和 trigger 设计，不能搬用其它实验数值 |
| 2. 估计 random | 用同一谱区的 off-time sideband，按时间窗宽和 live time 缩放后相减 | 估算无关 singles 偶然进入同一符合窗的背景 | sideband 形状、窗口比例、峰区污染及误差传播都需保留 |
| 3. 抑制 Compton / cosmic | 记录 lead/反符合条件、事件 multiplicity、`|E1−E2|` cut；对候选能量和检验单 γ 在两个探测器间散射的预测 | 区分真正的双 γ 对与单 γ 多探测器能量沉积、宇宙线诱发的多重事件 | 几何和 cut 会改变接受度；必须用响应或效率修正并做 cut variation |
| 4. 检验级联 | 对两个单光子能区分别开门并看反向 projection；检查已知中间能级、能量和、互符合/反符合及时间谱 | 排除经已知中间能级的 sequential cascade 和错误能级归属 | 弱线仍可能和未观测路径、双线或目标核/靶污染峰重叠 |
| 5. 做独立维度交叉核验 | 比较多个探测器角组/不同角度、时间分布、sum-energy 与 individual-energy 或 energy-sharing 分布 | 防止单一投影、单一 gate 或一种本底模板主导解释 | 角关联、能量共享或模型分解可消除部分退化，仍需保留统计和模型不确定度 |

`137mBa` 提供了可核验的实例。Walz 的五个 LaBr₃ 探测器在 `72°/144°` 组测量；72° 数据用 `|Δt|≤1.2 ns` 作 prompt gate、`20≤|Δt|≤76 ns` 估计 random，并在能量和谱施加 `|E1−E2|<300 keV`；144° 用 `<250 keV`。lead 降低 Compton 贡献；对 sum-energy 峰再看时间谱，真实候选峰在 `Δt=0` 附近、FWHM 约 1 ns，而单光子 Compton 散射预期在约 `±0.8 ns` 出现延迟峰。连续的单光子能量谱和级联能级信息用于反驳经 283.5-keV `1/2+` 态的顺序衰变（[W15-2](../sources/walz-2015-competitive-double-gamma-137ba.md)，[W15-AR-1](../sources/walz-2015-competitive-double-gamma-137ba.md)，PDF pp.406–408, Figs.1–3）。

门宽的算术核对：prompt 区 `|Δt|≤1.2 ns` 总宽 `2.4 ns`；图示 off-time 两侧区 `20≤|Δt|≤76 ns` 总宽 `2×(76−20)=112 ns`。若偶然符合率在 sideband 与 prompt 区近似平坦，则 prompt 区 random 估计的归一化因子为 `2.4/112≈0.0214`。这只是窗口宽度比例，不是论文分支比或新的 background count；正式计数还需要实际 sideband 峰面积、峰拟合、效率和协方差。能源和门宽/角度门的差异也不能混成同一个接受度修正。

另一个能级闭合反例说明总和门的局限：`137mBa` 的 `661.66-keV` isomer 若顺序经过 `283.5-keV` 中间态，另一光子能量约为 `661.66−283.5=378.16 keV`，两条跃迁的能量和仍为 `661.66 keV`。所以 sum peak 本身不能区分 simultaneous two-photon emission 和 cascade；要反向开门检查各自单光子谱、时间结构、multiplicity 与角关联。Walz 报告候选事件中的单光子能量连续、没有集中在这两个级联线能量上，并用时间与角分布作附加控制（[W15-2](../sources/walz-2015-competitive-double-gamma-137ba.md)，PDF p.407, Fig.2）。

两个采集的总分支比可作一项有限的一致性检查：Walz `2.05(37)×10⁻6`，Söderström `2.62(30)×10⁻6`；若只为比较而假定两组报告误差彼此独立，差值 `0.57×10⁻6` 对应 `sqrt(0.37²+0.30²)=0.48×10⁻6`，约 `1.2σ`。这支持两个独立实验观察到相容的总分支规模，不裁决双光子虚跃迁的多极路径。Söderström 的 branch count 是独立采集；但其 Fig.5 联合 energy-sharing fit 也纳入 Walz 数据点，不能把该联合拟合当成完全独立的路径复核（[W15-1](../sources/walz-2015-competitive-double-gamma-137ba.md)，[SO20-1](../sources/soderstrom-2020-137ba-competitive-gamma.md)，[SO20-AR-3](../sources/soderstrom-2020-137ba-competitive-gamma.md)）。

Söderström 的十一只 CeBr₃ 阵列用 `Δt≤655 ps` 定义 prompt window（以 `152Sm` 的已知 cascade 标定），`20–820 ns` 作 random sideband，并结合 multiplicity-two 和 cosmic-ray energy-difference cut。其独立数据中 661.6-keV 总和峰的计数在不同 cuts 下会改变，说明 cut 是测量接受度的一部分，不能只报告最后峰高。该实验报告 `8.7σ` 的分支确认，并用两光子 energy-sharing 分布补上 Walz 的角分布信息：Walz 的原始结论偏向 `Aqq`，Söderström 数据的 energy-sharing 支持较大的 `E3M1` 项；现有拟合仍保留 `α` 符号/模型差异（[SO20-1](../sources/soderstrom-2020-137ba-competitive-gamma.md)，[SO20-2](../sources/soderstrom-2020-137ba-competitive-gamma.md)，[SO20-AR-1](../sources/soderstrom-2020-137ba-competitive-gamma.md)，PDF pp.3–5, Figs.2–5, Table 1）。

**独立性与未解项：** 两篇文章使用不同的探测阵列和独立采集；Söderström 的自身分支计数是独立复测，但 Fig.5 的合并能量共享拟合也纳入 Walz 数据点，因此该联合拟合不能作为完全独立的多极路径复核。`137Ba` 的延迟 isomer tagging 是另一类时间选择，可参看 `193Bi` 的 delayed γ/electron coincidence（[HE15-2](../sources/herzan-2015-193bi-spectroscopy.md)）。由于可复查的事件级数据与完整响应/协方差不可得，本 audit 不独立重拟合 Walz/Söderström 的残余 Compton、random scaling 或 `α` 分支；Walz 与 Söderström 对虚跃迁路径的解释差异作为尚存开放歧义保留。

## Joint pair acceptance 与 event mixing stage

[[ljungvall-2020-agata-ganil-performance]] LG20-10直接比较source-normalizer的构建顺序：混合两个uncorrelated events的interaction points后tracking，才能包含close-pair clustering损失；tracking后只混两条γ不能无条件作为joint response。LG20-11的knownsource coefficients支持此特定验证，仍共享source/PSA/calibration，不成为独立spin赋值。

LG20-12保留in-beam低peak/background及共同alignment的限制。[[tracking-array]]的明确toy证明独立events若共有单γbeam-axis density `1+A2P2`，cross-event pair-angle density仍含 `A2²/5 P2`；不是isotropic，也不是same-cascade量子关联的新测量。对energy/PID/FOM门后coincidence强度或angular fits，应记录mix stage、population/occupancy、accepted/unaccepted counts与normalizer covariance。没有acceptance的angle bins不能用除法补回。

## Sources

- [[assie-2021-mugast-agata-vamos]] AS21-2/11/12：particle–γ–heavy tag的event stage与feeding entrypoint；强背景抑制和relativecurve不补齐absolutebeam normalization。

[[schirmer-1984-double-gamma-40ca-90zr]] demonstrates a rare two-photon branch: delayed proton-gated events, Crystal-Ball multiplicity, Eq.(1) PAF kinematics, energy/angle cuts and polarization-assisted angular-correlation fitting are all needed to separate simultaneous photons from annihilation/Compton backgrounds. This is a two-photon-decay case, not a generic cascade-DCO recipe.

- [[chakraborty-2023-131xe-wobbling-origin]]
- [[walz-2015-competitive-double-gamma-137ba]]
- [[soderstrom-2020-137ba-competitive-gamma]]
- [[herzan-2015-193bi-spectroscopy]]

## Evolution Log

- 2026-07-01：记录 `131Xe` 级联建立实例。
- 2026-10-12：补入 `137mBa` prompt/random/Compton/sequence gate audit；source-specific cuts 不跨实验复用。

## Gate predicates and spectral-origin control

[[senyigit-2014-agata-neutron-rejection]] SY14-4/6/7提供methodcounterexamples：γTOFgate并不确定targetisotope；detector/environmentγ可残留。gate组合须记录accept/reject、AND/OR、signed/absoluteangle、strict/equality边界、units、reference样本和executedversion。preprintbodyORgood与conclusion反向OR条件不是逻辑互补；未确认actualpredicate，不把文献summary转成生产代码。

不同stage的rejectpercent也不可相加：Table4的1040peak57%再28%中心值对应1−.43×.72≈69.04%overallreduction。这是source-tablearithmetic与背景设计，不是本方法对任意γγgate的efficiency。见[[doppler-correction]]、sourceSY14-5/8，保留jointcount/normalizationcovariance缺口。
