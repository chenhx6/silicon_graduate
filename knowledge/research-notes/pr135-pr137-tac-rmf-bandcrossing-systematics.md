---
type: research-note
title: "135Pr 与 137Pr：TAC-RMF/CDFT 视角下的磁转动带交叉与配对阻塞"
aliases: [135Pr 137Pr TAC RMF band crossing]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [garg-2015-135pr-magnetic-rotation, agarwal-2007-137pr-magnetic-rotation-bandcrossing, lv-2025-136pr-tac-covariant-density-functional, covariant-density-functional-theory]
created_from: Day26 targeted primary-source and reduced TAC-RMF response study
promotion_target: magnetic-rotation-and-tac-cdft
tags: [135Pr, 137Pr, magnetic-rotation, band-crossing, TAC, CDFT, RMF, pairing, blocking]
---

# 135Pr 与 137Pr：TAC-RMF/CDFT 视角下的磁转动带交叉与配对阻塞

## Research Trigger

本轮任务是核验 135Pr（N=76）与 137Pr（N=78）负宇称高自旋 ΔI=1 带的交叉位置，比较

    3qp: π h11/2 ⊗ ν(h11/2)^−2
    → 5qp: π h11/2 (g7/2)^2 ⊗ ν(h11/2)^−2

并把实验/杂化 TAC 结果放进 PC-PK1 类 TAC-CDFT 的自洽语言中。需要先划清范围：Garg 2015 和 Agarwal 2007 是实验加 hybrid TAC/壳模型解释；本地可直接核验的现代 PC-PK1 TAC-CDFT 原件是 136Pr 的 Lv 等 2025，而不是 135/137Pr。因此本页的数值工件是“约化 TAC-RMF/CDFT 响应模型”，用于重现角度、组态混合和流场响应的逻辑，不冒充 135/137Pr 的 PC-PK1 自洽求解。

## Grounded Evidence

### 1. 实验和作者模型结果

| 对象 | 直接报告或作者解释 | 定位 | 证据层 |
|---|---|---|---|
| 135Pr | 负宇称 ΔI=1 带有 M1 主导链接和 crossover E2；作者用 3qp 下段与 5qp 上段解释能量/对齐交叉。 | Garg 2015, PDF pp.1–9；source 页 GA15-1/2，[[garg-2015-135pr-magnetic-rotation]]:48 | 实验 + 作者模型 |
| 135Pr 交叉 | ħω≈0.37 MeV、I≈33/2−。Garg 的比较图把 137Pr 放在约 0.42 MeV、35/2−。 | Garg 2015, PDF p.8, Fig.6/结论段 | 作者模型/比较 |
| 137Pr | Band 2 扩展到 47/2−，DCO/IPDCO 支持 M1 带，并首次报告弱 crossover E2；B(M1)/B(E2) 在 37/2− 为 62.1(12.0)，在 41/2− 为 17.2(2.9)。 | Agarwal 2007, Table I、Figs.4/7，PDF pp.4–7；[[agarwal-2007-137pr-magnetic-rotation-bandcrossing]]:68-75 | 实验派生比值 |
| 137Pr 交叉 | 作者把 3qp/5qp 交叉与 back-bending 联系起来；低自旋接近 3qp，高自旋接近 5qp，35/2–37/2 为混合区。 | Agarwal 2007, Sec.IV, PDF pp.6–7；source 页 AG07-7/8 | 作者模型解释 |
| 137Pr 频率边界 | Agarwal 正文称实验 back-bending 约 0.48 MeV；Garg 2015 的跨核比较称约 0.42 MeV。二者采用的频率重建/图读法未在本轮统一。 | Agarwal 2007, PDF p.6；Garg 2015, PDF p.8 | 冲突保留 |
| 135Pr 绝对强度 | Garg 2015 没有本带 lifetime，不能提取绝对 B(M1)；交叉后 crossover 缺失，不能由 B(M1)/B(E2) 追踪反弹。 | Garg 2015, PDF pp.7–8；source 页 GA15-3、GA15-14 | 直接限制 |

### 2. CDFT 方法锚点和适用边界

PC-PK1 TAC-CDFT 的形式为能量密度泛函平均场加 −ω·J 推转项；模型自由度包含密度、形变、占据、配对和转频/方向。Lv 2025 的 136Pr 计算使用 PC-PK1、10 个谐振子主壳和 Bogoliubov 配对，但不做粒子数投影或总角动量投影（LV25-4，PDF p.9；[[lv-2025-136pr-tac-covariant-density-functional]]:72）。D1 在约 0.35 MeV 附近的 J 突跳被作者与 pairing collapse 联系，并明确提到粒子数投影可能改变该跳变，但本工作没有实施（LV25-13，PDF p.10；同页:81）。

因此，本任务不能把 136Pr 的 PC-PK1 输出平移成 135/137Pr 的已发表计算，也不能把模型形变/占据写成实验测量。Lv 2025 是方法学近邻与失败边界，而不是目标核的直接证据。

## Provisional Reasoning

### 1. 倾角自洽条件

在旋转系中取 h(ω,θ) = h0 − ωx Jx − ωz Jz，ωx = ω sin θ，ωz = ω cos θ，故 θJ = atan2(ωx,ωz)。对每个 blocked configuration（3qp、5qp），应同时迭代密度、配对张量、形变和 θ，使 ∂E′/∂θ = 0，其中 E′ = E − ωx〈Jx〉 − ωz〈Jz〉。

实际 CDFT 中 E、〈Jk〉、配对场和单粒子占据都来自同一 PC-PK1 迭代。现有 135/137Pr 文献没有提供这些输入，因此工件采用显式的刚度项和二维 θ 网格，仅验证方程链和响应方向。

### 2. 交叉和对齐增益

用两态 Routhian H = (E′3 W; W E′5)，W=0.12 MeV，得到 5qp 混合概率 P5(ω)。工件把源比较点固定为 135Pr 的 0.37 MeV 与 137Pr 的 0.42 MeV，使用能量偏移透明地把未混合两支在该点相交。输出的中间混合结果为：

| 核素 | 文献比较点 | 工件中 P5≈0.5 | θJ | Jp | Jn |
|---|---:|---:|---:|---:|---:|
| 135Pr | 0.37 MeV, 33/2− | 0.370 MeV | 35.0° | 8.50ħ | 10.00ħ |
| 137Pr | 0.42 MeV, 35/2− | 0.420 MeV | 38.9° | 8.27ħ | 8.15ħ |

这些角动量和倾角是约化模型输出，不是论文测量值。137Pr 的 Jn 较低来自脚本中显式的中子阻塞/占据调制场景；它不能单独证明真实核的中子费米面位置。

### 3. 配对阻塞与“较高中子费米面”说法

137Pr 比 135Pr 多两个中子（N=78 对 N=76）。在给定单粒子轨道排序中，增加中子数通常使化学势向上移动，但“较高中子费米面导致更强阻塞”不是 Garg/Agarwal 的直接测量，也不是当前文献给出的 135/137Pr PC-PK1 结果。合理的微观条件链是：

1. λn 上移使费米面附近 ν h11/2 Nilsson 分支的 uk、vk 改变；
2. 被阻塞的准粒子使时间反演配对通道减少，Δn(ω) 和 Ek=sqrt((εk−λn)^2+Δn^2) 随频率变化；
3. E′3−E′5 的斜率改变，故 crossing 频率和 Δi 改变；
4. 只有在给出 blocked orbital、u/v、Δn(ω) 和密度迭代后，才能把该链升级为 137Pr 的 CDFT 结论。

脚本把 Δn=0.764 MeV（135Pr 近邻 Garg 输入）和 Δn=0.650 MeV（137Pr Agarwal hybrid TAC 输入）作为来源锚点，但没有把二者解释为同一 PC-PK1 泛函下的精确配对场。更高 N 的费米面偏移设置为 +0.20 MeV 只是敏感性输入。

### 4. 质子/中子流场重排

在自洽 CDFT 中，时间奇密度给出 species-resolved current jq(r)（q=p,n），并满足 〈Jk〉q = ∫d3r [r×jq(r)]k。3qp→5qp 后新增的是 (g7/2)2 质子对，故最直接的预期是 jp(r) 的横向分量增强/重排；中子空穴的 blocked h11/2 占据与配对场变化则使 jn(r) 的方向和幅度响应更加依赖 N。

脚本输出 pr_tac_rmf_current_proxy.csv，在交叉前后用同一 θJ、Jp、Jn 生成二维高斯矢量场，以便检查积分矩与角度响应。该文件是可复现诊断场，不是 CDFT 的 jq(r) 原始网格。

## Assumptions

- Garg 2015 的 0.37 MeV/33/2− 与 137Pr 的 0.42 MeV/35/2−被作为跨核比较锚点；Agarwal 2007 的 0.48 MeV 表述保留为独立来源，不强行统一。
- 3qp/5qp 轨道标签采用两篇论文原文；没有替换成 ν i13/2−2 或其它未报告配置。
- 约化模型用 W=0.12 MeV、角度刚度和有效对齐分量作为透明的演示输入；它们不是 PC-PK1 参数。
- +0.20 MeV 的 137Pr 中子化学势偏移是反事实敏感性控制；真实值须由同一泛函、同一基底和 blocked HFB/TAC 计算得到。
- current proxy 只用于展示 p/n 流场的相对重排，不用于反演绝对磁矩、B(M1) 或 B(E2)。

## Competing Explanations

- 交叉频率差可来自不同 ν h11/2 Nilsson 占据（Garg 2015 结论段），也可来自配对场、形变极化、配置混合强度或频率定义差异。
- 137Pr 的 B(M1)/B(E2) 峰后下降是相对分支派生量；没有 lifetime 时不能把它拆成绝对 B(M1) 增大或 B(E2) 减小。
- 3qp/5qp 交叉也可能与普通核芯转动、signature/configuration mixing 或漏观测 crossover 共同造成 back-bending。
- “较高中子费米面→更强配对阻塞”是条件性微观假设；若实际 ν h11/2 分支远离费米面，或粒子数投影平滑了 pairing-collapse，方向和大小都可能改变。

## Transfer Conditions

将该机制迁移到其它 A≈130 奇质量 Pr/Nd 核，至少需要：同一能带的 level identity、blocked orbital、ε2/γ、Δp(ω)/Δn(ω)、Jp/Jn 分量、绝对或相对可靠的寿命/分支，以及统一的 ħω 定义。只有这些对象在同一 TAC-RMF/CDFT 计算中自洽更新，才可比较 Δi 和 dI/dω。

## Failure Conditions

- 把 136Pr 的 PC-PK1 TAC-CDFT 结果写成 135/137Pr 直接计算。
- 把 B(M1)/B(E2) 的比值变化改写成绝对 B(M1) 反弹。
- 把 model β、γ、θ 或 current proxy 当作实验测量。
- 以不同来源的 0.42 与 0.48 MeV 频率未经重建即宣称精确一致。
- 未给 blocked orbital、粒子数、配对方案和收敛标准就声称“137Pr 较高中子费米面已被 CDFT 证明”。

## Falsification or Reverse Tests

1. 取得 135/137Pr 同一实验定义下的 E(I) 和 I(ω)，用同一有限差分重建 crossing；若频率顺序反转，当前阻塞方向假设应撤回。
2. 对同一 PC-PK1/TAC-RHB 输入做 λn、blocked h11/2 和粒子数投影的三组控制；若 crossing 对 λn 不敏感，费米面解释不具辨识度。
3. 输出完整 jp(r)、jn(r)、Δq(ω)、u/v 和配置重叠，并检查交叉前后 ∫r×jq(r)d3r 是否真的呈脚本预测的重排。
4. 对交叉前后做 DSAM/RDDS lifetime 与完整 crossover 分支测量；若绝对 B(M1) 单调衰减且只由 B(E2) 变化解释比值，需撤回“叶片重新张开”的强因果表述。

## Open Questions

- 135Pr 与 137Pr 是否存在同一 PC-PK1 blocked TAC-RHB 输入和公开的 u/v、Δq(ω)、jq(r) 数据？
- Garg 2015 的 0.42 MeV 与 Agarwal 2007 的 0.48 MeV 是否可由同一 E(I)→ω 定义和自旋偏移解释？
- 137Pr N=78 的中子费米面究竟改变了哪个 h11/2 Nilsson 分支的 occupancy，还是主要改变了 proton g7/2 pair 的 crossing slope？
- 交叉处 Δi 能否从绝对 I(ω) 与 Jp/Jn 分解中独立确定，而不是用组态标签差值代替？

## Human Review

本页由 Codex 完成原件定位、方法边界和约化响应自审，保持 review_status: unreviewed。尚无用户逐条裁决；尤其“较高中子费米面导致更强阻塞”仍是待验证的条件性假设。

## Promotion or Rejection History

2026-10-29：建立本页。supports Garg 2015 与 Agarwal 2007 的 3qp/5qp 交叉比较；limits 把比值变化当作绝对磁跃迁强度、把 136Pr PC-PK1 迁移到 135/137Pr，以及未经统一定义合并 0.42/0.48 MeV。约化工件明确标注为 proxy，未晋升为直接 CDFT 结果。

## Reproducible Artifact and Handoff

脚本与输出位于：

- outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/pr-tac-rmf/pr_tac_rmf_bandcrossing.py
- 同目录 pr_tac_rmf_bandcrossing_trajectory.csv：ω、θJ、P5qp、Jp、Jn 轨迹；
- 同目录 pr_tac_rmf_current_proxy.csv：交叉前/后的 jp、jn 二维代理流场；
- 同目录 pr_tac_rmf_bandcrossing_results.json：方程、来源锚点、汇总和限制。

运行命令：

```bash
python3 outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/pr-tac-rmf/pr_tac_rmf_bandcrossing.py
```

当前状态：工件已运行成功，两个核素的模型中间混合点分别为 0.370 和 0.420 MeV；下一步应取得真正 135/137Pr TAC-RMF/TAC-RHB 输入或把本页停留在条件性研究笔记层，不把 proxy 晋升为来源事实。
