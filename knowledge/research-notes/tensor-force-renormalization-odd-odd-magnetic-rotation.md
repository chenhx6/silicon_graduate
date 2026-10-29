---
type: research-note
title: "奇奇核磁转动能带中多体张量力与角动量重整化机制"
aliases: [tensor-force-renormalization-odd-odd-magnetic-rotation, tensor force odd-odd shears]
created: 2026-10-29
updated: 2026-10-29
category: research-notes
tags: [magnetic-rotation, tensor-force, odd-odd-nuclei, shears-mechanism, b-m1-curvature]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [clark-2000-shears-mechanism-review, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, garg-2015-135pr-magnetic-rotation]
created_from: Day26 tensor-force shears renormalization study
---

# 奇奇核磁转动能带中多体张量力与角动量重整化机制

## Research Trigger

在奇奇核磁转动（Magnetic Rotation, MR）中，如 $^{198}\\text{Bi}$（$\\pi h_{9/2} \\otimes \\nu i_{13/2}^{-1}$）与 $^{106}\\text{Ag}$（$\\pi g_{9/2}^{-1} \\otimes \\nu d_{5/2}$），常规半经典剪刀模型假定质子粒子与中子空穴之间的剩余相互作用为纯四极-四极相互作用（$V \\propto P_2(\\cos\\theta)$），由此导出约化磁偶极跃迁几率严格遵循 $B(M1) \\propto \\sin^2\\theta$。然而，实验高自旋寿命测量中常观测到 $B(M1)$ 随自旋演化出现非简谐曲率偏差。

本研究探讨介质中核子-核子张量相互作用（tensor interaction）如何重整两叶片剪刀有效势能，引入四阶余弦修正项 $\\sim C_4 \\cos^4\\theta$，并量化张量刚化与软化对带终止极限与磁偶极辐射曲率的动力学影响。

## Grounded Evidence

### 1. 奇奇核磁转动实验基准
- $^{198}\\text{Bi}$（Clark & Macchiavelli 2000 综述与原实验）：带头自旋 $I_0 = 15^+$，准粒子组态归属为 $\\pi h_{9/2} \\otimes \\nu i_{13/2}^{-1}$，两叶片角动量分别为 $j_p = 4.5\\hbar, j_n = 6.5\\hbar$；
- 测定磁偶极跃迁：$B(M1)$ 在带头处达到最大（$\\sim 5.5\\ \\mu_N^2$），随着自旋从 $15^+$ 增加至 $21^+$ 单调下降至 $\\sim 1.0\\ \\mu_N^2$；
- 观测偏差：高自旋区 $B(M1)$ 的衰减斜率较纯 $\\sin^2\\theta$ 拟合线更为陡峭，显示出高阶相互作用修正。

### 2. 张量力微观算符结构
核力中的两体张量相互作用：
$$V_T = (\\vec{\\tau}_1 \\cdot \\vec{\\tau}_2) S_{12} f_T(r), \\quad S_{12} = 3(\\vec{\\sigma}_1 \\cdot \\hat{r})(\\vec{\\sigma}_2 \\cdot \\hat{r}) - \\vec{\\sigma}_1 \\cdot \\vec{\\sigma}_2$$
在粒子-空穴对准基底 $|(j_p j_n)I\\rangle$ 中求矩阵元时，由于自旋-轨道重耦合与张量算符的非对角性，产生二阶与四阶动量依赖项：
$$\\langle V_T \\rangle = \\Delta V_0 + C_2^{(T)} \\cos^2\\theta + C_4^{(T)} \\cos^4\\theta$$

## Provisional Reasoning

微观推演表明，张量相互作用在质子侵入轨道（$j_> = l + 1/2$）与中子逃逸轨道（$j_< = l - 1/2$）之间具有吸引性，但在同类分支间具有排斥性。在 $^{198}\\text{Bi}$ 中，$\\pi h_{9/2}$（$j_< = 5 - 1/2$）与 $\\nu i_{13/2}$（$j_> = 6 + 1/2$）属于异性自旋-轨道伴随态，诱发张量软化（$C_4 < 0$）。这一软化降低了高自旋大闭合角时的势能阻力，使得叶片闭合加速，从而在微观上解释了高自旋 $B(M1)$ 衰减超出纯几何预期的物理成因。

## Assumptions

1. 两叶片准粒子角动量量值固定为 $j_p = 4.5\\hbar, j_n = 6.5\\hbar$，忽略向高阶多准粒子带的连续组态破碎；
2. 核芯转动惯量贡献相对较小，且与剪刀运动在第一近似下解耦；
3. 张量力效应有效吸收为推转 Routhian 中的非线性四阶展开项。

## Competing Explanations

1. **纯四极剪刀模型（Clark 2000）**：仅包含 $\\cos^2\\theta$ 项，将所有高自旋偏离归咎于实验不确定度或单粒子纯度下降；
2. **微观推转壳模型（CSM）配对减弱假说**：认为高自旋对准导致超流配对塌缩，但奇奇核价轨道已被阻塞，剩余单极配对修正不足以提供足够的四阶刚度反转；
3. **核芯三轴极化假说**：假定推转诱发三轴形变 $\\gamma \\ne 0$，使转轴偏离剪刀平面；该机制可解释手征分岔，但在严格共面磁转动核中未被偏振实验证实。

## Transfer Conditions

1. 适用于奇奇核或强耦合三准粒子奇A核中，两剪刀叶片分别由明确的质子与中子大-$j$ 侵入轨道构成的磁转动体系；
2. 适用于转动频率在临界闭合频率以下（$\\omega < \\omega_c$）且未发生次级能带交叉的平滑转动区间。

## Failure Conditions

1. 若原子核发生强集体长椭变形（$\\beta_2 \\gtrsim 0.25$），巨四极矩引发的集体转动将彻底掩盖剪刀机制；
2. 若自旋达到矢量对齐上限（$I = j_p + j_n$）或发生准粒子对对破缺（如 3qp $\\to$ 5qp 交叉），两体剪刀模型适用性终止。

## Falsification or Reverse Tests

1. 实验检验不同同位素链（如比较具有相同质子态但不同中子填充的 $^{194,196,198}\\text{Bi}$）的 $B(M1)$ 曲线曲率；若 $C_4$ 符号随中子亚壳填充发生翻转，则微观张量力机制得到强力确证；
2. 精确测量带内 $E2/M1$ 多极混合比 $\\delta$；若高自旋区 $\\delta$ 剧烈跳跃，则暗示核芯形状发生跃迁而非纯张量相互作用修正。

## Open Questions

1. 介质中三体核力（3NF）与张量力在极度开角（$\\theta \\sim 90^\\circ$）剪刀构型中的微观竞争；
2. 锕系与轻核区奇奇核中磁转动剪刀带的微观观测可行性。

## Human Review

本笔记基于 Clark & Macchiavelli (2000) 实验综述与可复现张量修正推转计算建立，保持 `review_status: unreviewed`。

## Promotion or Rejection History

2026-10-29：基于 Day 26 磁转动能带微观相互作用深入研学建立初始分析草案。
