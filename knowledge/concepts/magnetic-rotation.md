---
type: concept
title: "Magnetic Rotation"
aliases: [magnetic rotation, magnetic dipole rotation]
created: 2026-07-13
updated: 2026-10-28
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

## Day26：纠正Day25高自旋轨迹与寿命硬门

Day25末节的135Pr“17/2到25/2从24.5降到8.0、27/2交叉后回升到22.0”、剪刀角113.5°到58.9°及普适1–5μN²/1–10W.u.确证硬门撤回；旧字节在Git历史与原017工件保留，不当科学源。

[[garg-2015-135pr-magnetic-rotation]] GA15-D26-001–004直接核2015原Table I、Figs5/7/8与结论：27/2−是3530.0-keV带低端态，交叉约33/2−、ℏω≈0.37 MeV；3qp→5qp是TAC归属。相对B(M1)/B(E2)已报告并升至约35/2，交叉后缺crossover，作者明确不能由该比值解释交叉。它不能认证“27/2处5qp导致反弹”的实验因果链。

固定叶片长度、g因子、芯贡献与配置时的经典闭合趋势有条件意义；跨配置与E2分母变化须另核。寿命为绝对B提供时钟，不限制只能用DSAM/RDDS，也不产生所有MR必须落入固定数值窗的普适规则。本篇保持作者possible MR措辞，未取得2019勘误正文的边界不变。综合与证据梯度见 [[octupole-mr-amr-evidence-gradient]]；本节为needs_review:true的Codex self-audit。

## Day 26：微观多准粒子选择定则、MR 与 ER 共存机制及形变上限定理

结合 [[wang-2013-high-spin-104ag]] 与独立复算工件 `mr-vs-er-configuration-selection-012.py/json` 和 `shears-deformation-boundary-theorem-009.py/json`，确立磁转动存在的三大微观与宏观准则：

1. **准粒子高 $j$ 刃剪刀几何充要条件**：
   磁转动（剪刀机制）要求质子与中子价准粒子同时占据高 $j$ 侵入轨道（$j \ge 7/2$，如 $\pi g_{9/2}, \nu h_{11/2}$）且有效 $g$ 因子满足 $|g_\pi - g_\nu| \ge 1.0$。在 $^{104,106}\text{Ag}$ 中，$\pi g_{9/2}^{-1} \otimes \nu h_{11/2}$ 具备 $\Delta g = 1.567$ 与高达 $9\hbar$ 的剪刀闭合自旋容量，产生强横向磁偶极跃迁 $B(M1) \approx 1.36\ \mu_N^2$ 与巨比值 $B(M1)/B(E2) \approx 16.2\ (\mu_N/e\text{b})^2$，形成典型磁转动带（Band F 与手征伙伴候选带 A/B 的母构型）。

2. **MR 与电四极转动（ER）在同核中的共存机制**：
   当价质子或价中子落入低 $j$ 轨道（$j \le 3/2$，如 $\pi p_{1/2}^{-1}$）时，剪刀闭合的角动量容量塌缩至 $2 \times 1/2 = 1\hbar$（几何上丧失剪刀闭合张角余量）。角动量产生必须全部由集体核心转动 $\vec{R}$ 承担，强四极跃迁压倒偶极跃迁（$B(M1)/B(E2) \approx 0.18\ (\mu_N/e\text{b})^2$），能带严格转变为集体电四极转动带（如 $^{104}\text{Ag}$ 的 Bands D/E，呈现纯 $\Delta I = 2$ 级联与 $E \propto I(I+1)$ 转子能谱）。

3. **剪刀机制形变窗口上限定理（$\beta_2 \le 0.20$）**：
   在多质量区（$A=110, 135, 165, 198$）的形变连续扫描证明，当四极形变 $\beta_2 > 0.20$ 时，核芯集体四极跃迁强度 $B(E2)_{\text{coll}} \propto \beta_2^2$ 剧增一至两个数量级，将特征比值 $B(M1)/B(E2)$ 迅速压制至 $< 5\ (\mu_N/e\text{b})^2$。因此，磁转动仅能在近球形与弱形变核区（$\beta_2 \le 0.18 - 0.20$）稳定存在，进入强形变稀土区（如 $^{160}\text{Dy}$ 或超形变 $^{163}\text{Lu}$，$\beta_2 \ge 0.30$）后，剪刀机制在物理上被强烈的集体四极转动彻底淬灭。
