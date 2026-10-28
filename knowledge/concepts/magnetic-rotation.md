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
- [[pr135-shears-dynamics-bandcrossing-rebound]]

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

## Day26：微观电流、剪刀与集体转动的条件模型（017纠错）

前版把 $j\ge7/2$、$|g_\pi-g_\nu|\ge1$、$\beta_2\le0.20$、固定 $B(M1)/B(E2)$ 数值和低-$j$ 必然纯 ER 写成充要条件或定理；这些认证撤回。它们至多是指定组态与模型参数下的例子，不能作为跨核素相界。[[hubel-2005-magnetic-rotation-review]] 的实验判据需要寿命、组态及静态矩联合对账；[[he-chuangye-2006-magnetic-chiral-106ag]] 的候选归属又受 [[rather-2014-ag106-transition-rates]] 的不同组态解释约束。先前 012/009 工件只可复算其输入，不能证明普适性。本段为 Codex 条件推导，`needs_review: true`。

在推转平均场 $\delta\langle H-\boldsymbol\omega\cdot\mathbf J-\sum_q\lambda_qN_q\rangle=0$ 下，规范协变的轨道流由单体密度矩阵给出：

$$\mathbf j_q(\mathbf r)=\left.\frac{\hbar}{2mi}(\nabla_{\mathbf r}-\nabla_{\mathbf r'})\rho_q(\mathbf r,\mathbf r')\right|_{\mathbf r'=\mathbf r}-\frac{e_q}{m}\mathbf A(\mathbf r)\rho_q(\mathbf r,\mathbf r).$$

若研究磁化流，还应按所用有效磁矩算符加入 $\nabla\times\mathbf M$；核子质量、有效质量及交换流约定必须与具体 EDF 一致。非零局部 $\mathbf j$ 是时间奇量，单独 $\mathcal T$ 不可能保持。取 $x$ 为剪刀平面 $yz$ 的法向时，平面解可以保持反幺正 $\mathcal S_x=\mathcal R_x(\pi)\mathcal T$；某个 $\mathcal R_z(\pi)$ 是否破缺须由实际占据和自洽密度检验。017 工件的单涡旋示例满足 $\mathcal S_x$ 且破缺单独 $\mathcal T$、$\mathcal R_z(\pi)$，这是构造例而非所有 MR 的对称性定理。

固定叶片长度和有效磁矩时，$\mathbf I=\mathbf j_\pi+\mathbf j_\nu+\mathbf R$、$\boldsymbol\mu=g_\pi\mathbf j_\pi+g_\nu\mathbf j_\nu+g_R\mathbf R$，$B(M1)\propto|\boldsymbol\mu_\perp|^2$。芯对齐、配对、组态重排或电荷四极矩变化会改变 $B(M1)/B(E2)$；$B(E2)\propto\beta_2^2$ 只在固定几何和电荷归一的简化集体模型中成立。因此 MR、手征候选与常规电转动在同核并存是能带/组态层面的检验问题，不能由单一 $\beta_2$ 或 $j$ 阈值裁定。参见 [[octupole-mr-amr-evidence-gradient]] 与 017 工件。
