---
type: research-note
title: "MR有效g因子淬灭、M1重正化与剪刀强度反演边界"
aliases: [MR effective g quenching, shears effective magnetic operator, M1 core polarization]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [clark-2000-shears-mechanism, hubel-2005-magnetic-rotation-review, agarwal-2007-137pr-magnetic-rotation-bandcrossing, garg-2015-135pr-magnetic-rotation, rather-2014-ag106-transition-rates]
created_from: Day26 independent MR effective-operator and cross-region strength audit
promotion_target: magnetic-rotation
tags: [magnetic-rotation, shears, M1, effective-g-factor, quenching, core-polarization, giant-resonance, Gamow-Teller, Pb, Pr, 106Ag]
---

# MR有效 $g$ 因子淬灭、M1重正化与剪刀强度反演边界

## Research Trigger

任务要求从MR的 $B(M1)$ 反演 $g_p^{\rm eff}-g_n^{\rm eff}$，并把自由核子 $g_s$ 的淬灭、M1巨共振/剪刀模、Gamow–Teller极化和核芯自旋极化统一起来。审计后的结论是：只有在配置、叶片角、绝对寿命和电磁算符都固定时，$B(M1)$才给出一个条件有效 $\Delta g$；它不能自动给出普适的自由核子淬灭因子。

## Grounded Evidence

| 区域/来源 | 可用强度或 $g$ 信息 | 反演边界 |
|---|---|---|
| Pb区 $^{198,199}$Pb | Clark 2000以198/199Pb寿命数据配合半经典角度曲线，取 $g_{\rm eff}=g_\pi-g_\nu\approx0.92$；Schmidt配置估计约1.17。Hübel重述该区强B(M1)随剪刀闭合下降 | [[clark-2000-shears-mechanism]] pp.15–18；[[hubel-2005-magnetic-rotation-review]] pp.25–26,58–59。0.92是模型拟合的有效差，不是纯$g_s$淬灭测量 |
| $^{193}$Pb控制 | 29/2−带头静态 $g_{\rm exp}=0.68(3)$，配置加法估计 $0.71(4)$；Hübel称其支持配置及近正交耦合 | [[hubel-2005-magnetic-rotation-review]] pp.33–35。静态总$g$约束平行磁矩，不能单独等价于$g_\pi-g_\nu$ |
| $^{135}$Pr | Garg 2015未测Band 3寿命，只有由相对分支/能量得到的$B(M1)/B(E2)$；不能分离绝对$B(M1)$和$B(E2)$，更不能经验反演$\Delta g$ | [[garg-2015-135pr-magnetic-rotation]] pp.7–8；原文明确说无寿命不能提取$B(M1)$ |
| $^{137}$Pr | Agarwal 2007 Table I/Fig.7的$B(M1)/B(E2)$来自相对强度，假设$\delta^2$可忽略；无绝对寿命。故不能从62.1(12.0)、17.2(2.9)等比值给$\Delta g$ | [[agarwal-2007-137pr-magnetic-rotation-bandcrossing]] pp.4–7 |
| $^{106}$Ag | Rather 2014 Table I确有逐态绝对$B(M1)$，例如主带I=15为0.45、I=17为1.12，partner相应数据包含2.02和0.69等；但两带构型、叶片角、side/top feeding和完整响应并未给出足以作唯一剪刀反演的合同 | [[rather-2014-ag106-transition-rates]] pp.4–11；文中TPSM用同一$\epsilon=.15,\gamma=30^\circ$而取不同准粒子$K$，说明相同E2不能唯一锁定叶片几何 |

Pb区 $g_{\rm eff}=0.92$ 与1.17的比值约0.79，但只能作为“有效算符整体尺度”的数量级提示；不能写成核内 $g_s^{\rm eff}=0.79g_s^{\rm free}$。$g_l$、轨道/自旋组成、空穴符号、核心磁化和波函数混合都进入同一个差值。

## Provisional Reasoning

### 1. 剪刀模型的条件反演

取总角动量 $\mathbf I=\mathbf j_p+\mathbf j_n$，磁偶极算符

$$\boldsymbol\mu=\mu_N\left(g_p^{\rm eff}\mathbf j_p+g_n^{\rm eff}\mathbf j_n\right).$$

若核芯磁矩平行于 $\mathbf I$、两叶片和配置固定，则横向分量可写为

$$|\mu_\perp|=|\Delta g_{\rm eff}|\frac{j_pj_n}{I}|\sin\theta|,
\qquad \Delta g_{\rm eff}=g_p^{\rm eff}-g_n^{\rm eff}.$$

于是

$$B(M1;I\to I-1)=\frac{3}{8\pi}\Delta g_{\rm eff}^2\left(\frac{j_pj_n}{I}\right)^2\sin^2\theta,$$

以及条件反演

$$|\Delta g_{\rm eff}|=\sqrt{\frac{8\pi B(M1)}{3}}\frac{I}{j_pj_n|\sin\theta|}.$$

用Clark的角度约定也可写为

$$B(M1)=\frac{3}{8\pi}g_{\rm eff}^2j_p^2\sin^2\theta_p,$$

其中 $\theta_p$ 是质子叶片相对总角动量的角，不是两叶片夹角 $\theta$。把这两个角混用会产生系统性错误。

反演的可识别条件至少包括：绝对寿命、分支和内转换处理；初末态构型与叶片长度；每个自旋的角度；M1/E2混合比；芯磁矩和有效算符。缺任一项，结果只是模型条件下的 $\Delta g$。

### 2. 自由算符与介质中有效算符

单体M1算符可写成

$$\hat T(M1)=\sqrt{\frac{3}{4\pi}}\mu_N\sum_{\tau=p,n}\left[g_l^\tau\mathbf l_\tau+g_s^\tau\mathbf s_\tau\right].$$

自由值为 $g_l^p=1,g_l^n=0,g_s^p=5.586,g_s^n=-3.826$。有限模型空间中通常使用

$$g_s^{\rm eff}=q_sg_s^{\rm free},\qquad g_l^{\rm eff}=g_l^{\rm free}+\delta g_l,$$

并可能加入

$$\delta g_p\,[Y_2\otimes\sigma]_{J=1}$$

以及两体电流/介子交换项。$q_s\sim0.7$–$0.8$是许多壳模型和GT/M1经验分析的常见量级，但不是所有质量区、算符和跃迁的统一常数。现代大空间计算中，剩余相关、连续性和两体电流会改变所需的表观淬灭，某些M1系统给出的整体$g$尺度可接近0.8–0.9；这正是Pb区0.92/1.17≈0.79不能直接命名为$q_s$的原因。

微观来源可分为四层：

1. **模型空间外的粒子–空穴极化**：外部壳层激发通过核心极化修正单体M1矩阵元，产生$\delta g_l,\delta g_s$与新的张量结构；
2. **长程相关和配置混合**：TAC/壳模型截断的波函数把强度错误地压入少数叶片，重建后$B(M1)$可增可减；
3. **两体电磁流**：交换电流和短程电流不能总等价成一个常数$q_s$，尤其在不同动量转移和不同自旋/轨道跃迁之间；
4. **空穴与芯极化符号**：中子空穴的有效贡献带有相对于粒子不同的角动量/磁矩耦合，$g_p-g_n$不能只用两自由核子Schmidt值相减。

### 3. M1巨共振、剪刀模与GT的关系

低能轨道剪刀模和高能M1自旋翻转巨共振是同为$J^\pi=1^+$的不同响应区：

- 轨道剪刀模主要是质子与中子轨道角动量的相对振荡，M1算符的轨道等矢/等矢组合占主导；
- 自旋M1巨共振主要是自旋翻转的粒子–空穴响应，能量更高，强度可被淬灭、碎片化并转移到复杂配置；
- MR带内M1是低能、特定多准粒子波函数的跃迁，不等于把巨共振总强度压缩成一个“剩余磁矩”。积分M1强度和低能MR强度之间没有逐态一一对应。

Gamow–Teller算符为

$$\hat O_{GT}=g_A\sum_k\boldsymbol\sigma(k)\tau_\pm(k),$$

它是自旋–同位旋算符；M1的等矢/等旋自旋部分可在同位旋对称极限下与GT响应存在类比，但M1还含轨道项、不同同位旋组合和电磁两体流。因此GT强度缺失不能直接转成MR的$g_p-g_n$淬灭，最多提示自旋–同位旋相关和模型空间外强度转移的规模。

对MR而言，最稳妥的有效算符是带有状态/配置标签的

$$\hat\mu_{\rm eff}=\hat\mu_{\rm one-body}(q_s,\delta g_l)+\hat\mu_{\rm core\,pol}+\hat\mu_{\rm two-body},$$

而不是单一全核常数。若只在一个窄带内使用$g_{\rm eff}$，它是对上述多层修正的投影参数。

### 4. 跨区经验反演裁决

**198/199Pb。** Clark从寿命B(M1)与半经典角度拟合出$g_{\rm eff}\approx0.92$，Schmidt估计约1.17；这给出约0.79的有效差值尺度。该结果与Hübel综述中Pb区强M1随剪刀闭合下降、193Pb带头静态g=0.68(3)和配置计算0.71(4)相一致，构成Pb区最完整的$B(M1)+g$交叉约束，但仍是配置特定的有效参数。

**135/137Pr。** 两篇原件均缺候选MR带的绝对寿命；135Pr作者明确说不能提取绝对B(M1)，137Pr的比值按相对强度和$\delta^2\approx0$派生。即使比值出现峰值，也无法判断是M1增强、E2变弱还是有效g改变；不存在可靠的经验$\Delta g_{\rm eff}$数值。任何把Pr写成$\Delta g=1.42$的数字都只能是未给出绝对寿命/角度核验的模型输入或旧工件，不是本轮实验反演。

**106Ag。** Rather Table I的绝对B(M1)使它比Pr更接近可反演条件，但TPSM给出同一平均场形变下的不同准粒子组态，且强度受feeding与stopping输入影响；没有唯一的$(j_p,j_n,\theta)$，所以不能把0.45、1.12、2.02等B(M1)直接转换为经验$g_p-g_n$。它可用于检验多个候选配置的算符矩阵元，而非给出单一全核淬灭常数。

## Assumptions

剪刀公式假设固定叶片、芯磁矩平行总角动量、单一一体M1算符、绝对跃迁率已知。有效算符讨论区分M1轨道/自旋、GT自旋–同位旋和巨共振响应，不把它们视为同一个实验量。

## Competing Explanations

$B(M1)$偏差可能来自角度错误、构型混合、核心转动、空穴符号、M1/E2混合、侧馈和DSAM停止本领，也可能来自真实两体电流或外部空间极化。表观$g$淬灭不能唯一分解这些机制。

## Transfer Conditions

需要绝对寿命、完整分支/ICC、DCO/偏振、构型和同一TAC/PRM角度，才能在指定自旋上反演$\Delta g_{\rm eff}$。跨核比较必须保持算符、叶片定义和有效$g$约定一致；不能把Pb区0.92移作Pr或Ag输入。

## Failure Conditions

将$g_{\rm eff}/g_{\rm Schmidt}$直接称$q_s$；用GT或M1巨共振总和替代低能MR矩阵元；由Pr相对B比值反演绝对$g$；将Ag的单态B(M1)在未知构型下当作$g_p-g_n$，均越过证据边界。

## Falsification or Reverse Tests

对Pb配置同时拟合静态g、B(M1)和B(E2)，改变$q_s,\delta g_l$及核心项并比较相关似然；对Pr先补同带绝对寿命；对Ag在两个TPSM/TAC配置中保持同一响应输入，检查是否可由构型而非$g$淬灭解释B(M1)反差。若同一配置需要自旋依赖且符号反转的$g$，应优先检查混合和算符遗漏。

## Open Questions

Pb区0.92有效差值中轨道、空穴和核心项的独立分解仍缺；Pr缺绝对寿命；Ag缺Lieder原件及完整协方差；巨共振/GT的总强度如何投影到这些特定低能多准粒子态，不能由现有来源定量回答。

## Human Review

Codex定向来源核验、公式推导和边界审计；页面保持 `review_status: unreviewed`，未获得人工逐项审核。

## Promotion or Rejection History

2026-10-29：建立MR有效磁偶极算符边界。`supports` [[clark-2000-shears-mechanism]] 与 [[hubel-2005-magnetic-rotation-review]] 的Pb区$g$和寿命约束；`limits`将Pb有效$g$尺度、GT淬灭或M1巨共振强度直接移植到Pr/Ag。
