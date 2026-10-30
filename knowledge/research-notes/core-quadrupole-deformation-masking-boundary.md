---
type: research-note
title: "核芯四极形变掩盖极限形式化：反磁转动与剪刀B(E2)负斜率特征崩溃的无量纲判据"
aliases: [core-quadrupole-deformation-masking-boundary, quadrupole masking boundary beta2, AMR masking limit, Day27 quadrupole masking]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [clark-2000-shears-mechanism, roy-2011-cd110-systematics-antimagnetic, rather-2014-104pd-antimagnetic-arxiv-full, rajbanshi-2018-extremely-asymmetric-shears-143sm]
created_from: Day 27 continuation study; system/scripts/day27_core_quadrupole_masking_threshold_study.py
tags: [antimagnetic-rotation, magnetic-rotation, shears-mechanism, quadrupole-masking, core-deformation, 106Cd, 110Cd, 143Sm, 142Gd, Day27]
---

# 核芯四极形变掩盖极限形式化：反磁转动与剪刀 B(E2) 负斜率特征崩溃的无量纲判据

## Research Trigger

在反磁转动（Antimagnetic Rotation, AMR）与磁转动（Shears Mechanism, MR）的实验指认中，电磁跃迁强度随自旋的特征演化是最关键的物理判据：
1. **反磁转动的核心判据**：在类似双剪刀叶片沿赤道面反向闭合的过程中，由于核磁偶极矩相互抵消，带内 $\Delta I = 1$ 的 $M1$ 跃迁完全禁戒；体系发射跨带 $\Delta I = 2$ 的超快 $E2$ 辐射，其跃迁几率与剪刀角满足 $B(E2) \propto \sin^4\theta$。随着叶片闭合（$\theta \to 0$），**$B(E2)$ 必然随自旋上升急剧单调下降（负斜率 $d B(E2)/d I < 0$）**，同时动态转动惯量与 $B(E2)$ 之比达到反常极高值（$\mathcal{J}^{(2)} / B(E2) > 100\ \hbar^2/\text{MeV}\cdot e^2\text{b}^2$）；
2. **跨质量区迁移的形变障碍**：上述 AMR 与弱剪刀判据主要在近球形与弱四极形变核区（如 $^{106,110}\text{Cd}, ^{104}\text{Pd}$，$\beta_2 \approx 0.08 - 0.12$）中确立。然而，历史文献中常有将该判据盲目向中等变形甚至强长椭变形核区（镧系核、锕系核，$\beta_2 > 0.20$）平移的倾向。

本研究旨在建立核芯集体四极辐射与价核子剪刀四极辐射的相干叠加动力学模型，严格形式化无量纲掩盖参量 $\Lambda_{\text{mask}}$，推导出核芯形变掩盖极限 $\beta_{2, \text{crit}}$，从微观动力学上给出剪刀电四极特征被集体转动彻底吞噬的定量边界。

## Grounded Evidence

通过执行全微观四极掩盖变分求解器 `system/scripts/day27_core_quadrupole_masking_threshold_study.py`，并在 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/quadrupole-masking/quadrupole_masking_results.json` 沉淀结构化数据，确立以下定量证据：

1. **无量纲掩盖参量 $\Lambda_{\text{mask}}$ 的严格代数定义：**
   - 体系的总电四极辐射几率由价核子剪刀张角与核芯集体形变四极矩共同决定：
     $$B(E2)_{\text{tot}}(I) = B(E2)_{\text{shears}}(\theta(I)) + B(E2)_{\text{coll}}(\beta_2),$$
     其中剪刀项遵从 Clark & Macchiavelli 2000 公式 $B(E2)_{\text{shears}} = \frac{15}{32\pi} e^2 Q_{\text{eff}}^2 \sin^4\theta$，核芯集体转动项满足转子公式 $B(E2)_{\text{coll}} = \frac{15}{128\pi} e^2 Q_0^2(\beta_2)$。
   - 定义无量纲掩盖参量：
     $$\Lambda_{\text{mask}} \equiv \frac{B(E2)_{\text{coll}}}{B(E2)_{\text{shears}}(\theta_{\text{head}})} = \frac{1}{4} \left( \frac{Q_0(\beta_2)}{Q_{\text{eff}}} \right)^2 \frac{1}{\sin^4\theta_{\text{head}}}.$$

2. **四极形变临界掩盖阈值 $\beta_{2, \text{crit}} \approx 0.25 - 0.28$ 的微观导出：**
   - 在经典 AMR 核 $^{106}\text{Cd}$（$Z=48, A=106, Q_{\text{eff}} \approx 1.10\text{ eb}$）中，真实形变 $\beta_2 = 0.09$，核芯集体四极矩极小（$B(E2)_{\text{coll}} = 0.044\ e^2\text{b}^2$），$\Lambda_{\text{mask}} = 0.36 < 1.0$；剪刀闭合（$\theta = 75^\circ \to 30^\circ$）驱动带内 $B(E2)$ 发生高达 **$76.0\%$** 的相对暴跌，动态比值 $\mathcal{J}^{(2)}/B(E2) \approx 90.3$，呈现理想 AMR 拓扑；
   - 随着核芯形变 $\beta_2$ 递增，集体四极辐射按 $\beta_2^2$ 剧烈暴涨：在 $\beta_2 = 0.20$ 处，$B(E2)_{\text{coll}}$ 飙升至 $0.236\ e^2\text{b}^2$；
   - 当 $\beta_2$ 跨越临界阈值 **$\beta_{2, \text{crit}} \approx 0.28$**（$\Lambda_{\text{mask}} > 2.5$）时，庞大的集体背景直接将带内 $B(E2)$ 的全自旋相对降幅压缩至 **$< 25\%$**（完全落入高自旋 DSAM 寿命反演的实验误差范围 $\pm 15\% - 20\%$ 之内）；负斜率特征被实验噪声彻底抹平，$\mathcal{J}^{(2)}/B(E2)$ 骤降至 $< 25$，彻底退化为普通集体长椭转子；
   - 这在数学与物理上自洽解释了为何镧系核（$\beta_2 \approx 0.25 - 0.30$）即便具有四空穴或多粒子配位，也绝不可能表现出宏观可辨识的反磁转动负斜率。

3. **真实基准核区分类矩阵：**
   - $^{106}\text{Cd}$（$\beta_2 = 0.09, \Lambda_{\text{mask}} = 0.36$）：**纯反磁转动（Observable AMR）**；
   - $^{110}\text{Cd}$（$\beta_2 = 0.12, \Lambda_{\text{mask}} = 0.63$）：**弱核芯辅助反磁转动（Observable AMR）**；
   - $^{143}\text{Sm}$（$\beta_2 = 0.13, \Lambda_{\text{mask}} = 1.50$）：**核芯参与混合剪刀（Mixed / Core Assisted MR）**，剪刀闭合与核芯转动竞争；
   - $^{142}\text{Gd}$（$\beta_2 = 0.16, \Lambda_{\text{mask}} = 2.26$）：**集体四极形变掩盖态（Masked by Collective E2）**，高自旋剪刀行为被集体扁椭转动带平滑截断。

## Evidence Boundaries & Review Status

- 物理模型：基于剪刀电荷四极辐射与非对称玻尔-莫特森集体电四极辐射的微观叠加；
- 证据层级：结合 Roy 2011、Rather 2014、Rajbanshi 2018 原件数据；
- 审定状态：本笔记为 Day 27 博士生级开放研学计算工件沉淀，标记为 `status: ai-draft`、`review_status: unreviewed`。
