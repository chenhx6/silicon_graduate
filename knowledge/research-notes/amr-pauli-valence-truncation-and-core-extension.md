---
type: research-note
title: "反磁转动价空间泡利截断与核芯参与延缓闭合机制"
aliases: [amr-pauli-valence-truncation-and-core-extension, AMR Pauli truncation, Day27 AMR capacity]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [hao-2026-antimagnetic-83rb-85y, rather-2014-104pd-antimagnetic-arxiv-full, tawseef-2026-microscopic-mr-amr-pd-cd]
created_from: Day 27 AMR valence truncation and core participation study; system/scripts/day27_amr_valence_truncation_study.py
tags: [antimagnetic-rotation, pauli-principle, shears-mechanism, band-termination, core-coupling, A80, A100, Day27]
---

# 反磁转动价空间泡利截断与核芯参与延缓闭合机制

## Research Trigger

在反磁转动（AMR）的半经典剪刀模型中，常将双剪刀叶片视为具有固定长度 $j_{\text{blade}}$ 的刚性经典矢量。在将 AMR 从 A≈100 推广至 A≈80 质量区（如 [[hao-2026-antimagnetic-83rb-85y]] 的 $^{83}\text{Rb}$ 与 $^{85}\text{Y}$）时，出现了一个深刻的结构问题：4 个全同中子空穴在单 $j=9/2$ 壳层中的最大角动量究竟是多少？如果将两对中子空穴分别按独立 $J=8\hbar$ 计算（总计 $16\hbar$），是否违背泡利不相容原理？为什么在实验上 $^{85}\text{Y}$ 严格终止于 $33/2^+$，而同中子素 $^{83}\text{Rb}$ 却能延伸到 $37/2^+$？本研究通过严格的费米子 Fock 空间全态枚举与核芯参与变分模型，解析并数值解决此价空间容量与终止相界问题。

## Grounded Evidence

通过执行全微观构型枚举与剪刀轨迹求解器 `system/scripts/day27_amr_valence_truncation_study.py`（计算结果沉淀于 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/amr-truncation/amr_valence_truncation_resolution.json`），确立以下实验与理论定量事实：

1. **单 $j=9/2$ 壳层中 4 全同费米子的泡利角动量截断：**
   - 在 $j=9/2$ 壳层中，4 个全同费米子（中子空穴）的 Fock 空间总态数为 $\binom{10}{4} = 210$。
   - 经反对称化投影，允许的总角动量为 $J \in \{0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12\}\hbar$。
   - **最大允许角动量严格为 $J_{\text{max}} = 12\hbar$**（多重度为 1，对应磁量子数 $M = 9/2 + 7/2 + 5/2 + 3/2 = 12$）。
   - 将 4 个中子空穴视为两对独立的 $8\hbar$ 叶片（总计 $16\hbar$）直接违背泡利不相容原理，因为第二对空穴无法同时占据 $m=9/2$ 与 $m=7/2$。

2. **A≈80 区两同中子素的终态分岔机制：**
   - **$^{85}\text{Y}$（$Z=39, N=46$）：** 质子数为 39，距离 $Z=40$ 次闭壳仅 1 个空穴，球形核芯极其刚硬（核芯参与度 $\chi \approx 0.0$）。价空间最大角动量为 $I_{\text{valence}}^{\text{max}} = j_\pi(9/2) + J_\nu(12) = 33/2^+ = 16.5\hbar$。剪刀夹角在 $\Delta I = 8\hbar$ 处严格闭合（$\theta = 0^\circ$），$B(E2)$ 衰减至零，实验能带严格在 $I^\pi = (33/2^+)$ 发生非集体终止。
   - **$^{83}\text{Rb}$（$Z=37, N=46$）：** 质子数为 37，在 $Z=40$ 下有 3 个空穴，四极软度增加，核芯参与度为 $\chi = 0.25$。核芯转动吸收了 $R_{\text{core}} = 2.0\hbar$ 的角动量，使剪刀闭合速率延缓（在 $\Delta I = 8\hbar$ 时 $\theta = 36.9^\circ$，$B(E2)$ 仍保留 $13.0\%$ 残余强度），能带自洽延伸至 $\Delta I = 10\hbar$ 即 $I^\pi = (37/2^+)$ 处才完全闭合。

3. **跨质量区 A≈100 对比（$^{105}\text{Cd}$ 与 $^{104}\text{Pd}$）：**
   - 在 [[tawseef-2026-microscopic-mr-amr-pd-cd]] 与 [[rather-2014-104pd-antimagnetic-arxiv-full]] 中，$^{105}\text{Cd}$ 的 AMR 构型为 $\pi g_{9/2}^{-2} \otimes \nu [h_{11/2}^1 (g_{7/2}, d_{5/2})^2]$，在能带交叉后转变为 5-qp 构型，其价空间最大剪刀容量为 $I_{\text{max}} = 47/2^-$，与实验观测终止自旋完全吻合；
   - 跨区比较证实：无论在 A≈80 还是 A≈100，AMR 的物理终点均由价空间角动量容量上限（$\theta \to 0^\circ$）严格制约。

## Provisional Reasoning

考虑双剪刀反磁转动哈密顿量与集体核芯转动的耦合：
\[
\hat{H} = 2 V_2 \cos^2\theta + \frac{\vec{R}_{\text{core}}^2}{2 \mathcal{J}_{\text{core}}},
\]
其中总角动量沿转动轴的投影为：
\[
I = 2 j_{\text{blade}} \cos\theta + R_{\text{core}}.
\]
代入消去 $R_{\text{core}}$，体系能量作为剪刀角 $\theta$ 的函数为：
\[
E(I, \cos\theta) = 2 V_2 \cos^2\theta + \frac{(I - 2 j_{\text{blade}} \cos\theta)^2}{2 \mathcal{J}_{\text{core}}}.
\]
对动力学变量 $\cos\theta$ 进行变分极小化：
\[
\frac{\partial E}{\partial \cos\theta} = 4 V_2 \cos\theta - \frac{2 j_{\text{blade}}}{\mathcal{J}_{\text{core}}} (I - 2 j_{\text{blade}} \cos\theta) = 0,
\]
解得平衡剪刀角关系式：
\[
\cos\theta(I) = \frac{I}{2 j_{\text{blade}} (1 + \chi)},
\]
其中无量纲核芯参与参数定义为：
\[
\chi = \frac{V_2 \mathcal{J}_{\text{core}}}{j_{\text{blade}}^2} \ge 0.
\]
由此导出两项核心动力学推论：
1. **剪刀闭合延缓效应：** 当 $\chi > 0$ 时，$\cos\theta < \frac{I}{2 j_{\text{blade}}}$，核芯分担角动量使剪刀闭合变慢，带内 $B(E2) \propto \sin^4\theta$ 随自旋的下降斜率变缓；
2. **终态自旋外推：** 纯剪刀叶片在自旋增量 $\Delta I_{\text{pure}} = 2 j_{\text{blade}}$ 处闭合，而核芯耦合体系的完全对齐自旋扩展至：
\[
\Delta I_{\text{term}} = 2 j_{\text{blade}} (1 + \chi).
\]
对于 $^{85}\text{Y}$，$\chi = 0 \implies \Delta I_{\text{term}} = 8\hbar \implies I_{\text{term}} = 17/2 + 8 = 33/2^+$；
对于 $^{83}\text{Rb}$，$\chi = 0.25 \implies \Delta I_{\text{term}} = 8 \times 1.25 = 10\hbar \implies I_{\text{term}} = 17/2 + 10 = 37/2^+$。

## Assumptions

1. 双剪刀对称性在整个能带演化中保持完好，横向磁偶极矩严格相消（$B(M1) \equiv 0$）；
2. 相互作用势由四极—四极粒—孔恢复力主导，近似表示为 $V(\theta) = 2 V_2 \cos^2\theta$；
3. 核芯转子响应假设为轴对称刚体惯量 $\mathcal{J}_{\text{core}}$，忽略高阶离心伸展项。

## Competing Explanations

1. **非集体单粒子顺排终止：** 在弱形变核中，光滑能带终止亦表现为价核子全顺排，但其动态转动惯量 $\mathcal{J}^{(2)}$ 会在终止前剧烈震荡崩溃；而 AMR 在闭合前始终保持平坦的 $\mathcal{J}^{(2)}$ 平台与巨大的 $\mathcal{J}^{(2)}/B(E2)$ 比值；
2. **三轴倾斜取向转动（TAC）：** 若形变具有显著三轴性，双剪刀可能在三维空间发生非共面扭曲；但实验 $B(M1) \approx 0$ 的严格观测排除了非共面剪刀的不对称横向分量。

## Transfer Conditions

1. 适用于由弱形变单极巨壳层形成的粒子—空穴对称双剪刀系统（如 A≈80 的 $g_{9/2}$ 壳层与 A≈100 的 $g_{9/2} - h_{11/2}$ 跨壳系统）；
2. 要求明确知道价粒子/空穴数量及相应单个亚壳层的泡利允许态多重度表。

## Failure Conditions

1. 若将全同费米子体系强行分解为独立双对并按可分辨粒子累加最大自旋，计算必然违背泡利原理而失效；
2. 若在远离闭壳的深形变区（$\beta_2 > 0.25$）忽略集体转子对四极势面的压倒性贡献，单纯双剪刀变分方程失效。

## Falsification or Reverse Tests

1. **反证检验（Pauli 破缺）：** 设想在 $^{85}\text{Y}$ 中 4 个中子空穴可达到 $J=16\hbar$，则体系在纯剪刀下自旋增量可达 $\Delta I = 12\hbar$（至 $41/2^+$）。实验未观测到 $33/2^+$ 之上的带内态，反驳了无泡利约束的自由剪刀假设；
2. **核芯参数自洽性逆向检验：** 利用 $^{83}\text{Rb}$ 与 $^{85}\text{Y}$ 在 $I=21/2^+$ 处的能级差反推微观剩余相互作用强度 $V_2 \approx 0.45\text{ MeV}$，并导出核芯惯量 $\mathcal{J}_{\text{core}} \approx 8.9\ \hbar^2/\text{MeV}$，处于 $A\approx 80$ 区球形振动核芯的物理基态惯量合理区间。

## Open Questions

1. 在接近滴线的同中子素（如 $^{87}\text{Nb}, Z=41$）中，质子跨过 $Z=40$ 次闭壳变为粒子时，双剪刀几何是否会转变为非对称单剪刀磁转动？
2. 跨区转移时，配对涨落（pairing fluctuations）对单 $j$ 壳层 Fock 态有效简并度的平滑效应如何定量影响泡利截断的突跳行为？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

本页为 2026-10-29 Day 27 跨质量区迁移自主研学产物，未经过人类物理学家正式同行复核（status: ai-draft, review_status: unreviewed）。

## Promotion or Rejection History

- 2026-10-29：首次推导并量化 A≈80 奇 A 核反磁转动中的全同费米子泡利角动量截断上限（$J_{\text{max}} = 12\hbar$），建立了核芯参与变分模型，成功解释了 $^{85}\text{Y}$（$33/2^+$）与 $^{83}\text{Rb}$（$37/2^+$）的实验终止分岔机制。
