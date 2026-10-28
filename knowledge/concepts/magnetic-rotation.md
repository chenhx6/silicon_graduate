---
type: concept
title: "Magnetic Rotation"
aliases: [magnetic rotation, magnetic dipole rotation]
created: 2026-07-13
updated: 2026-07-13
status: ai-draft
review_status: unreviewed
concept_type: high-spin-collective-mode
confidence: low
tags: [magnetic-rotation, shears, high-spin]
---

# Magnetic Rotation

## Definition

Magnetic rotation is a high-spin mode in which a few high-j particle and hole angular momenta form current loops and rotate in a weakly deformed or nearly spherical mass distribution. The dominant radiation is often M1 rather than collective E2.

## Experimental Signatures

The review associates magnetic bands with regular Delta I=1 sequences, large B(M1), weak B(E2), and a decrease of B(M1) as the shears close. These are fingerprints that require configuration and lifetime context.

## Boundary

Small charge deformation or weak E2 strength is not by itself proof of magnetic rotation. The current-distribution anisotropy and the shears mechanism are model interpretations that must be separated from measured transition strengths.

## Necessary Assumptions

- A high-j particle-hole configuration and its angular-momentum geometry are specified.
- Charge deformation and current distribution are treated separately.

## Discriminating Observables

Band regularity, M1/E2 strengths, B(M1) decrease with spin, transition multipolarities and lifetime data are relevant together.

## Supporting Evidence

- [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]
- [[clark-2000-shears-mechanism]]
- [[kumar-2025-review-magnetic-antimagnetic-rotational-structures]]
- [[frauendorf-2018-beyond-unified-model]]
- [[greiner-1966-magnetic-properties-even-nuclei]]
- [[hubel-2005-magnetic-rotation-review]]

[[hubel-2005-magnetic-rotation-review]] consolidates the detector, lifetime and static-moment chain: decreasing `B(M1)` with spin, weak/decreasing `B(E2)`, configuration links, g factors, quadrupole moments and band termination jointly discriminate shears rotation from ordinary core rotation. The review also keeps antimagnetic rotation (cancelled transverse moments, `ΔI=2` and decreasing `B(E2)`) separate, and treats TAC/P2 interaction results as model-dependent rather than universal thresholds.

## Counter-evidence and Competing Interpretations

Weak E2 strength and regular Delta I=1 sequences can also arise from other weakly deformed configurations or band mixing.

## Our Current Position

Treat magnetic rotation as a configuration-dependent interpretation supported by transition systematics, not as a synonym for any dipole band.

## Sources

- [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]
- [[clark-2000-shears-mechanism]]
- [[kumar-2025-review-magnetic-antimagnetic-rotational-structures]]
- [[frauendorf-2018-beyond-unified-model]]
- [[greiner-1966-magnetic-properties-even-nuclei]]

## Review Status

New concept page; review pending.
## Day 25 正式核验：剪刀动力学、高自旋重对齐反例与寿命时钟判据

在 Day 25 研学窗口的深入推演中，结合 [[garg-2015-135pr-magnetic-rotation]]（GA15-D25P-A005-01/02）与本 run 独立分析工件 day26-octupole-mr-quantitative-017.json，确立了磁转动模式的定量剪刀闭合规律与关键证伪边界：

1. **半经典剪刀动力学公式与适用域**：
   在等长刚性双叶模型中，质子叶与中子叶角动量 $j_1 \approx j_2 \approx j$ 构成夹角 $\theta$。总自旋满足 $I = (j_\pi + j_\nu) \cos(\theta/2)$，垂直于总角动量的横向磁偶极矩为 $\mu_\perp = (g_\pi - g_\nu) j \sin(\theta/2)$，导出磁偶极跃迁几率满足特征抛物线跌落：
   $$B(M1) = \frac{3}{8\pi} \mu_\perp^2 = \frac{3}{8\pi} (g_\pi - g_\nu)^2 j^2 \left[1 - \left(\frac{I}{j_\pi + j_\nu}\right)^2\right]$$
   该公式定性描述了固定组态下剪刀闭合引起的 $B(M1)$ 随自旋单调下降趋势。

2. **高自旋组态重对齐与单调陡降硬门的破缺（$^{135}\text{Pr}$ 反例）**：
   在 $^{135}\text{Pr}$ 负宇称高自旋带（组态 $\pi h_{11/2} \otimes \nu h_{11/2}^{-2}$）中，低自旋端（$I=17/2^- \to 25/2^-$）随着剪刀从 $\theta \approx 113.5^\circ$ 闭合至 $58.9^\circ$，$B(M1)/B(E2)$ 实验比值从 $24.5$ 陡降至 $8.0$；然而在 $I \ge 27/2^-\hbar$ 处，由于发生五准粒子（5qp，$\pi h_{11/2}(g_{7/2})^2 \otimes \nu h_{11/2}^{-2}$）能带交叉顺对齐，破坏了原有三准粒子叶片的连续闭合，使得比值反弹上升至 $22.0$（$35/2^-$）。这表明不能将“全自旋区间单调抛物线陡降”作为判定磁转动的排他性硬门，多准粒子重对齐会重构新的横向磁矩。

3. **态寿命 $\tau$ 与绝对跃迁尺度的必要性**：
   相对比值 $B(M1)/B(E2)$ 容易受微弱 $E2$ 跨带线测量误差或绝对收集性整体塌缩的掩盖。只有通过 DSAM/RDDS 测得能态寿命 $\tau$，确立绝对 $B(M1) \sim 1–5\ \mu_N^2$ 与弱四极强度 $B(E2) \sim 1–10\text{ W.u.}$，才能真正将候选带升级为确证的磁转动带。缺乏绝对寿命时，必须严格维持“候选磁转动带（candidate MR band）”的审慎定位。
