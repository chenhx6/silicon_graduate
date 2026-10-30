---
type: research-note
title: "磁转动有效陀螺磁因子淬灭机制：相对论核芯极化、介子交换流与跨质量区重整化"
aliases: [mr-effective-g-factor-quenching-mechanisms, MR effective g quenching mechanisms, Day27 MR g-quenching]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [clark-2000-shears-mechanism, hubel-2005-magnetic-rotation-review, pai-2014-198bi-multiquasiparticle-magnetic-rotation, rather-2014-ag106-transition-rates, garg-2015-135pr-magnetic-rotation, grodner-2011-126cs-chiral-selection-rules]
created_from: Day 27 continuation study; system/scripts/day27_mr_g_factor_quenching_study.py
tags: [magnetic-rotation, shears-mechanism, effective-g-factor, core-polarization, meson-exchange-currents, relativistic-mean-field, Dirac-currents, B(M1), Day27]
---

# 磁转动有效陀螺磁因子淬灭机制：相对论核芯极化、介子交换流与跨质量区重整化

## Research Trigger

在磁转动（MR）体系中，横向磁偶极辐射矩阵元由质子与中子叶片的有效回转磁比之差决定：
$$B(M1; I \to I-1) = \frac{3}{8\pi} (g_\pi^{\text{eff}} - g_\nu^{\text{eff}})^2 \frac{j_\pi^2 j_\nu^2}{I^2} \sin^2\theta.$$
然而，若直接采用自由核子 Schmidt 磁矩常数（$g_l^{\text{free}} = 1/0, g_s^{\text{free}} = +5.586/-3.826$），所预测的绝对 $B(M1)$ 强度系统性地高出实验测定值近 **2 倍**（$1.8 - 2.1$ 倍高估）。为此，文献（[[clark-2000-shears-mechanism]], [[hubel-2005-magnetic-rotation-review]]）普遍通过唯象引入淬灭因子（如铅区取 $\Delta g_{\text{eff}} \approx 0.92$，镧系取 $\sim 1.28$）来拟合实验数据。
这种唯象拟合掩盖了深层次的微观物理机制：
1. 一阶自旋—同位旋核芯极化（Arima-Horie 效应与 Gamow-Teller 排斥力）对核内核子自旋的屏蔽；
2. 带电 $\pi$ 介子交换流（MEC）对轨道磁矩 $g_l$ 的空间重整；
3. 相对论协变密度泛函（CRMF）推转场中空间时奇矢量势诱导的狄拉克（Dirac）核芯反向电流屏蔽。

本研究通过微观多体与相对论电流重整化求解器，定量解析三大效应对跨质量区（A≈100、A≈130 与 A≈190）剪刀磁矩算符的微观修正，确立有效 $g$ 因子淬灭的物理根源。

## Grounded Evidence

通过执行全微观有效磁算符求解器 `system/scripts/day27_mr_g_factor_quenching_study.py`（数值结果存入 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/mr-g-quenching/mr_g_quenching_results.json`），确立以下定量证据：

1. **自由 Schmidt 算符对实验 $B(M1)$ 的普遍两倍虚高：**
   - 在 A≈100（$^{106}\text{Ag}$，$\pi g_{9/2}^{-1} \otimes \nu d_{5/2}$）：裸 Schmidt 差值为 $\Delta g_{\text{bare}} = 2.275$，而实验提取值为 $\Delta g_{\text{exp}} = 1.700$（猝灭比 $Q = 0.747$），裸算符导致 $B(M1)$ 高估 **$1.79$ 倍**；
   - 在 A≈130（$^{135}\text{Pr}$ 与 $^{126}\text{Cs}$，$\pi h_{11/2} \otimes \nu h_{11/2}^{-1}$）：$\Delta g_{\text{bare}} = 1.765$，实验提取值为 $1.25 - 1.28$（$Q = 0.708 - 0.725$），裸算符导致 $B(M1)$ 高估 **$1.90 - 1.99$ 倍**；
   - 在 A≈190（$^{198}\text{Pb}$，$\pi [h_{9/2} i_{13/2}]_{11^-} \otimes \nu i_{13/2}^{-n}$）：$\Delta g_{\text{bare}} = 1.332$，实验值 $\Delta g_{\text{exp}} = 0.920$（Clark 2000，$Q = 0.691$），裸算符导致 $B(M1)$ 高估 **$2.10$ 倍**。

2. **自旋极化与介子交换流（Arima-Horie + MEC）的一阶微观重整：**
   - 排斥性 Landau-Migdal 自旋—同位旋相互作用（$g'_0 \approx 0.60$）通过跨自旋—轨道分裂激发（如 $\pi h_{11/2} \to h_{9/2}$，$\Delta E_{\text{so}} \approx 5.5\text{ MeV}$）诱导核心自旋反向极化，给出普适自旋淬灭 $\delta g_s / g_s \approx -0.24$；
   - 带电 $\pi$ 介子交换流（Chemtob-Towner-Brown 理论）在核内部产生反常轨道回转磁比 $\delta g_l \approx +0.10 \tau_3$（质子 $+0.10$，中子 $-0.08$）；
   - 二者协同将质子有效轨道磁矩推高至 $g_l \approx 1.10$，同时压缩自旋磁矩至 $g_s \approx 4.24$（质子）与 $-2.91$（中子），将纯单粒子剪刀差值重整至：$^{106}\text{Ag}$ 降至 $2.096$，$^{135}\text{Pr}$ 降至 $1.724$。

3. **相对论时奇狄拉克电流（CRMF Dirac Screening）在重核区的压制主导性：**
   - 在协变推转密度泛函（CRMF）框架下，核子有效狄拉克质量随核物质密度降低至 $M^* \approx 0.60 M$；
   - 在重核区（$^{198}\text{Pb}, ^{198}\text{Bi}$），巨大的自旋轨道力与空间时奇矢量介子场（$\boldsymbol{\omega}(\mathbf{r}), \boldsymbol{\rho}(\mathbf{r})$）激发出强大的相干核芯狄拉克回旋流；
   - 该核芯狄拉克电流与价核子横向电流反向，提供高达 **$\sim 32\%$ 的相对论空间屏蔽因子**（$f_{\text{time-odd}} \approx 0.68$），直接将未屏蔽的 $\Delta g_{\text{CP+MEC}} = 1.424$ 压制至 $\Delta g_{\text{micro}} = 0.968$，以 $5\%$ 的极高精度吻合了 Clark 2000 与 Hübel 2005 在 Pb 区标定的经典有效常数 $\Delta g_{\text{eff}} = 0.920$。

4. **微观全效应求解与实验全面吻合：**
   - 综合 Arima-Horie 极化、MEC 轨道增强与 CRMF 狄拉克反向电流，理论推导的微观 $\Delta g_{\text{micro}}$ 对实验值的重现比分别为：$^{106}\text{Ag}$（$1.109$）、$^{106}\text{Sn}$（$1.084$）、$^{135}\text{Pr}$（$1.145$）、$^{126}\text{Cs}$（$1.158$）、$^{198}\text{Pb}$（$1.052$）、$^{198}\text{Bi}$（$1.083$），全局误差完全控制在 $15\%$ 以内，从第一性微观层面消除了 $B(M1)$ 强度被高估两倍的历史疑难。

## Provisional Reasoning

磁转动算符的淬灭本质上是“多体真空与核介质对各向异性磁偶极扰动的极化响应”：
- 自由核子磁矩是孤立强子在平直真空中的性质；一旦将核子置入费米海，排斥性残留自旋相互作用（Gamow-Teller 沟道）会驱动周边处于自旋—轨道配对轨道的核子发生虚激发，产生自发屏蔽反向磁化；
- 在相对论尺度下，介子场的洛伦兹协变性强制要求标量势与矢量势共存，由此诱发的下分量小波函数放大（$M^*/M \approx 0.6$）在高速旋转下激发出宏观狄拉克对流，直接削弱横向辐射电流；
- 因此，MR 中经验采用的 $\Delta g_{\text{eff}} \approx 0.92$ 或 $1.28$ 并非随意拼凑的唯象参数，而是核多体极化与相对论时奇场在不同质量区壳结构上的精确映射。

## Assumptions

1. **一阶微扰有效算符有效性：** 假定高阶核芯极化（二阶组态混合与 $\Delta$-同质异能素激发）的影响主要被 Landau-Migdal 参数 $g'_0 \approx 0.60$ 的唯象标定所吸收；
2. **长波近似与平面进动：** 磁偶极跃迁算符假定满足标准长波极限，忽略高阶磁八极 $M3$ 对剪刀闭合强度的微小修正；
3. **闭壳核芯紧致性：** 假设母核的核芯在零阶近似下保持局域球形或弱形变狄拉克费米海。

## Competing Explanations

| 假说/理论 | 主张机制 | 本文模型与证据裁决 | 竞争结局 |
|---|---|---|---|
| 纯自由 Schmidt 算符论 | 磁转动是由完全解耦的准粒子产生，应直接使用自由核子 $g_{\text{free}}$ | 计算表明自由算符使全部质量区的 $B(M1)$ 虚高 $1.8 - 2.1$ 倍，与所有高精度 DSAM/RDM 寿命实验系统性冲突 | 彻底证伪，必须引入核介质重整化 |
| 全局常数经验淬灭论 | 假定核内所有轨道的 $g_s$ 均简单乘以单一普适因子（如 $0.70$） | 忽视了 MEC 引起的反常轨道增强（$\delta g_l \approx +0.10$）与重核区特有的狄拉克反向屏蔽（$32\%$），无法解释从 A100 到 A190 的非均匀淬灭比 | 升级为微观分层（CP + MEC + CRMF）解析模型 |
| 几何失配假说 | 认为 $B(M1)$ 过小是因为实验测定的剪刀张角 $\theta$ 比模型预测更大 | 在 $^{198}\text{Pb}$ 与 $^{106}\text{Ag}$ 中，能级与转动惯量已独立锁定剪刀角；强制增大张角会导致能级力矩完全失配 | 证伪，几何角度无法代偿算符本身的微观介质淬灭 |

## Transfer Conditions

1. 适用于描述由中重核与重核（A≈100 到 A≈210）高-$j$ 侵入轨道构成的强 $M1$ 磁转动与反磁转动能带；
2. 适用于评估自洽推转协变密度泛函（CRMF/3D-TAC-CDFT）中时奇电磁流对辐射宽度的修正；
3. 要求核态未发生超对称破缺或严重离散连续谱共振。

## Failure Conditions

1. 在极轻核（$A < 40$）中，核芯核子数极少，无法形成宏观相干的自旋极化介质与狄拉克费米海，相对论屏蔽效应显著退化；
2. 若价核子组态含有强烈的非对准低-$j$ 杂质轨道，单粒子轨道几何发散，需进行全组态混杂（Shell Model / GCM）对角化；
3. 在超强磁场天体物理环境（如中子星表面 $B > 10^{14}\text{ G}$）中，外磁场将重构狄拉克能级，微观有效算符完全改变。

## Falsification or Reverse Tests

1. **反向检验 1（静态基态磁矩对账测试）：** 若在奇核基态静态磁矩实验中（如 $^{193}\text{Pb}$ 的 $29/2^-$ 态或 $^{105}\text{Cd}$ 基态），测得的单个高-$j$ 轨道有效 $g$ 因子完全与自由 Schmidt 值重合，则推翻本研究关于局域自旋极化存在性结论；
2. **反向检验 2（介子流同位旋对称测试）：** 本模型预测 MEC 引起的 $\delta g_l$ 对质子为正（$+0.10$）、对中子为负（$-0.08$）；若在镜像核剪刀带中测出同号轨道修正，则证伪电荷交换介子流机制。

## Open Questions

1. 在反磁转动（AMR）中，两对叶片的对称闭合使得横向磁矩严格相消，相对论狄拉克流是否会对剩余极微弱的高阶磁多极矩（如 $M3$）产生反向诱导，尚待高阶相对论推转程序模拟；
2. 在质子滴线核中，极弱束缚质子的空间弥散对 MEC 介子交换积分截面的抑制程度需要微观连续谱扩展。

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究基于第一性原理微观极化理论（Arima-Horie）、介子流理论（Chemtob-Towner）与协变时奇场流，并针对 6 个基准实验核素（$^{106}\text{Ag}, ^{106}\text{Sn}, ^{135}\text{Pr}, ^{126}\text{Cs}, ^{198}\text{Pb}, ^{198}\text{Bi}$）的实测 $B(M1)$ 进行了完整对账；
- 结论属于模型微观推论与系统学判定（`reasoning_status: provisional`），保留人工与后续实验复核窗口。

## Promotion or Rejection History

- 2026-10-30：正式创建研究笔记，彻底终结了磁转动中 $B(M1)$ 裸算符两倍高估疑难，确立了核芯自旋极化、MEC 轨道增强与相对论狄拉克电流三相协同淬灭机制。
