---
type: research-note
title: "离散对称、电流场与实验可观测量的边界"
aliases: [discrete symmetry current boundary, TAC current observables]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, starosta-2001-n75-chiral-vibrations, olbratowski-2002-critical-frequency-preprint]
created_from: Day26 discrete-symmetry audit 034
promotion_target: tilted-axis-cranking
tags: [time-reversal, discrete-symmetry, current-density, good-I, tac, observables]
---

# 离散对称、电流场与实验可观测量的边界

> 034 为 Day26 条件审计；Day27 仅无学分预习，不推进课程状态，也不打开 Day28。017 的流场使用任意单位，不能视作核 EDF/HFB 结果。

## Research Trigger

需要把 (\mathcal T)、(\mathcal R_z(\pi)) 和 (\mathcal S_y=\mathcal T\mathcal R_y(\pi)) 对内禀电流的作用写清楚，并区分三类对象：定向的 cranked intrinsic field、角动量投影后的 good-(I) 实验室态，以及真正可测的能级和电磁跃迁。局部 (\mathbf j(\mathbf r)) 的对称残差不能直接认证 MR、AMR 或手征。

## Grounded Evidence

- Frauendorf 2001 F01-5/F01-8/F01-9（PDF pp.473–476、484–485）区分旋转平均场的内禀离散对称、左右手 aplanar 解、实验室对称恢复，以及 TAC 与 PRM 的量子边界。TAC 本身不恢复 good total (I)，也不计算左右手隧穿劈裂。
- Starosta 2001（PDF pp.1–4，Fig.1、Fig.3、Table I）使用由时间反演与 180° 旋转组成的手征算符；其 (^{132}\mathrm{La}) sideband 位移和 3D-TAC 表格是模型/实验系统学，不是局部电流测量。
- Olbratowski 2002 v1（PDF pp.1–4，Eqs.2–7、Figs.4–6）给出 (I=\hat J\omega+s)、平面/非平面经典分支及 Skyrme-HF 结果。其 (\hbar\omega_c=0.514639) MeV 是冻结参数算术，HF 非平面分支从约 0.6 MeV 出现；二者都不是实验临界频率。

## Provisional Reasoning

对时间奇电流，变换规则写作

$$
\mathcal T\mathbf j(\mathbf r)=-\mathbf j(\mathbf r),\quad
\mathcal R_z(\pi)\mathbf j(\mathbf r)=R_z(\pi)\mathbf j(R_z^{-1}\mathbf r),
$$

$$
\mathcal S_y\mathbf j(\mathbf r)=\mathcal T\mathcal R_y(\pi)\mathbf j(\mathbf r)
=-R_y(\pi)\mathbf j(R_y^{-1}\mathbf r).
$$

若完整内禀场满足 (\mathcal S_y\mathbf j=\mathbf j)，它可以保持非零局部流；若同时要求单独 (\mathcal T\mathbf j=\mathbf j)，则时间奇性强制该场为零。相反，(\mathcal S_y) 不变并不意味着局部磁化或磁矩处处为零。

017 高斯 MR 涡旋在其选定坐标下有非零 (T) 与 (R_z(\pi)) 残差，而 (T R_z(\pi)) 残差为零；AMR 双反向涡旋也有非零局部场和 (R_z(\pi)T) 残差为零。对 (T R_y(\pi))，该具体玩具场的残差为非零，说明轴标签和构造不能从名称自动推断。表格中的局部残差只检验一个人为给定的向量场，不能替换自洽占据、密度、算符和能带证据。

一个 good-(I) 实验室态来自角动量投影或量子化模型；其 (J^2) 与实验室投影量子数是好量子数，但不等同于带有固定经典方向的 intrinsic (\mathbf j(\mathbf r))。因此内禀电流是平均场序参量/模型对象，实验可观测量来自能级、(S(I))、alignment、(B(M1))、(B(E2))、分支和带间连接。

## Assumptions

017 的残差使用 (0.35) 间距的对称笛卡尔网格、任意高斯涡旋宽度和 arbitrary-current units；积分“磁矩”仅是 (\frac12\int\mathbf r\times\mathbf j\,d^3r) 的诊断量。没有把该诊断量标定为 (\mu_N)，没有求解 EDF/HFB，也没有进行角动量投影。

## Competing Explanations

相同的 (\Delta I=1/2) 能带模式可能来自手征、磁转动、旋称伙伴、平面/轴向分支、形状共存或组态混合。AMR 中横向磁矩抵消的模型图像不排除局部流、纵向磁矩或其它跨带跃迁。Frauendorf 2001 的 TAC/PRM 边界和 Olbratowski Fig.6 的 planar/axial-long 替代都要求保留这些竞争解释。

## Transfer Conditions

迁移到真实核时，必须给出 body-axis convention、密度矩阵/配对、时间奇 EDF 项、有效磁矩算符、占据和角动量投影方案。离散对称残差可以作为数值自检，但只有与逐带实验跃迁和量子模型同时闭合时才有模式判别价值。(R_z(\pi))、(R_y(\pi)) 的轴标签不能脱离源文 convention 互换。

## Failure Conditions

若以 (\mathbf j(\mathbf r)\neq0) 直接声称实验 MR，或以积分磁矩为零直接声称 AMR；若把 intrinsic (T) 破缺写成 laboratory good-(I) 态必然有定向流；若把 (S_y) 不变误写成每一点 (\mathbf j=0)，结论均失效。局部场残差也不能取代 lifetime、absolute (B(M1)/B(E2))、branching、alignment 或 competing-model 检验。

## Falsification or Reverse Tests

在固定 EDF、组态与轴 convention 下，分别施加 (T)、(R_z(\pi))、(T R_y(\pi)) 到完整密度和 current，检查残差是否随网格、基组和 self-consistency 收敛；再进行 good-(I) 投影并计算 (S(I))、(B(M1))、(B(E2)) 和带间矩阵元。若不同内禀场给出相同投影观测量，局部流拓扑不能被当作唯一模式证据。

## Open Questions

真实 3D-TAC/HFB 密度的时间奇项和配对如何改变这些残差？在 (^{132}\mathrm{La}) 中，投影后的量子态能否同时重现约 0.37 MeV 带位移、Starosta 的 12 keV 内禀势垒和 Olbratowski 的 planar/axial-long 替代？哪些实验绝对电磁矩对左右手相干最敏感？

## Human Review

本页是 Codex 的 source/claim self-audit，未提升 `human-reviewed`。017 残差、变换轴和 good-(I) 解释均需在论文级使用时按原件和实际数值实现定向复核。

## Promotion or Rejection History

2026-10-28：建立 034 离散对称审计；明确非零 (T)-odd intrinsic current、(S_y) 反幺正补偿、good-(I) 实验室态和局部残差的边界。撤回用 toy (\mathbf j(\mathbf r)) 直接认证 MR/AMR/chirality 的写法。Day27 保持无学分预习。
