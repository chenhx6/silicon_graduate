---
type: method
title: "Talmi：\(^{14}\mathrm C\) 长寿命的壳模型 GT 相消合同"
aliases: [Talmi 14C shell model, Gamow-Teller cancellation shell-model contract]
method_type: "shell-model-beta-decay"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Nuclear Shell Model 70 Years article 1, PDF pp.14-21 / article pp.1-8"
confidence: "high for the article's displayed model derivation; conditional for broader 14C explanations"
tags: [shell-model, beta-decay, gamow-teller, tensor-force, effective-interaction, 14c]
sources: [book-nuclear-shell-model-70-years]
---

# Talmi：\(^{14}\mathrm C\) 长寿命的壳模型 GT 相消合同

## Purpose

用一个可追溯的小型壳模型例子连接：

```text
有效相互作用 -> 壳模型波函数 -> GT 矩阵元相消
             -> 镜像 beta 衰变 -> 实验寿命/模型空间边界
```

这个例子适合训练“能级拟合、波函数结构、弱跃迁矩阵元和实验事实必须分开”的分析习惯。

## Inputs and Assumptions

- \(^{14}\mathrm C\) 的 \(J=0,T=1\) 基态在简化 \(p^{-2}\) 空间中由
  \({}^{1}S_0\) 和 \({}^{3}P_0\) 组合：
  \[
  |\Psi_{0}\rangle=x|{}^{1}S_0\rangle+y|{}^{3}P_0\rangle;
  \]
- \(^{14}\mathrm N\) 的 \(J=1,T=0\) 基态在同一简化空间中写成
  \[
  |\Psi_{1}\rangle
  =\alpha|{}^{3}S_1\rangle
  +\beta|{}^{1}P_1\rangle
  +\gamma|{}^{3}D_1\rangle;
  \]
- 允许 GT 衰变的自旋算符只连接相应径向部分，文章给出
  \[
  M_{\mathrm{GT}}
  =\sqrt6\left(x\alpha-\frac{y\beta}{\sqrt3}\right).
  \]

## What It Can Establish

当张量力改变 \(^{14}\mathrm N\) 波函数中的 \(\alpha,\beta\) 相对符号和大小时，
GT 振幅可以发生强烈相消。Talmi 的简化数值示例给出近似相等的 \(\alpha,\beta\)
时矩阵元接近零，并用 \(^{14}\mathrm O\) 镜像衰变说明 Coulomb/质子—中子差异
会改变相消程度。

文章还展示了一个 \(J=0\) 壳模型子空间矩阵：自旋–轨道项和张量力共同决定混合
系数；小的波函数组分变化即可显著改变一个本来很小的弱衰变矩阵元。这是实验
核结构分析中“弱跃迁对模型空间和相位非常敏感”的直接示例。

## Experimental and Model Boundary

- \(^{14}\mathrm C\) 的实测长半衰期是实验事实；简化壳模型中的“接近零”是模型
  机制，不等于完整理论已经解释全部数据；
- 文章回顾 Cohen–Kurath 有效相互作用、张量力、较高壳层混合和无芯壳模型等
  不同路线；
- \(^{14}\mathrm C\) 小矩阵元不适合用单一“淬灭因子”概括；
- 镜像 \(^{14}\mathrm O\) 衰变是重要交叉约束，但实验和 Coulomb 结构必须单独核对；
- 小的构型混合、三体力或更大模型空间可能改变相消，不能从一个简化矩阵外推
  到所有弱衰变。

## What It Cannot Establish Alone

- 不能由 \(M_{\mathrm{GT}}\approx0\) 单独确定张量力的唯一强度；
- 不能把一个能级拟合良好的有效相互作用自动视为对弱跃迁的无偏预测；
- 不能把 \(^{14}\mathrm C\) 的特殊相消直接迁移到 A≈130 核的 GT、M1 或 E2 分析；
- 不能忽略有效算符、模型空间、三体力和实验分支/半衰期不确定度。

## Verification

2026-11-03：

- 核对合集 PDF physical pp.14–21，对应文章正文 pp.1–8；
- 页面图像核对了壳模型混合矩阵、波函数系数和 GT 相消式；
- raw SHA-256、合集文章边界和正文定位已登记在
  `knowledge/sources/book-nuclear-shell-model-70-years.md`；
- 该文章完成了一个有界小单元，合集其它 13 篇仍保持 queued。

## Sources

- [[book-nuclear-shell-model-70-years]]
- [[stuchbery-wood-shell-model-effective-charge-collectivity-contract]]
- [[casten-shell-model-pairing-and-collectivity-foundations]]
- [[beta-decay-phase-space-log-ft-and-cvc-unitarity]]
