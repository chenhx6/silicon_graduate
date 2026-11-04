---
type: method
title: "Petrache Ch.11：IBFM-2 γ-soft 核芯与混合比模型合同"
aliases: [Petrache Ch.11 IBFM wobbling, IBFM delta mixing-ratio contract]
method_type: "ibfm-experimental-model-comparison"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Petrache ed. Ch.11 PDF pp.239-255, selected formula and result pages"
confidence: "high for displayed IBFM equations and model comparison; conditional for assignments"
tags: [ibfm, gamma-soft, wobbling, mixing-ratio, 135pr, 127xe, b-e2, b-m1]
sources: [book-petrache-chirality-and-wobbling]
---

# Petrache Ch.11：IBFM-2 \(\gamma\)-soft 核芯与混合比模型合同

## Purpose

把 IBFM-2 对低自旋 wobbling 候选的计算结果接入实验混合比分析，同时避免把
模型得到的小 \(\delta\) 或大 \(\delta\) 直接写成实验模式确认。

## Inputs and Assumptions

IBFM-2 哈密顿量写为
\[
\hat H=\hat H_B+\hat H_F+\hat V_{BF},
\]
其中 \(\hat H_B\) 是 IBM-2 质子/中子玻色核芯，\(\hat H_F\) 是未配对费米子，
\(\hat V_{BF}\) 包含动力学四极、交换和单极相互作用。偶偶核芯的 SCMF 能量面
通过映射进入 IBM-2 参数；第 11 章的例子显示多数相关核芯沿 \(\gamma\) 方向较软。

示例单粒子空间主要采用 \(h_{11/2}\) 轨道；奇质子/奇中子核的具体身份必须回到
核素 \(Z,N\) 和原始计算输入核对，不能只照抄章节文字。

## What It Can Establish

### Energies and gamma softness

IBFM-2 可以在给定 IBM-2 核芯、费米子空间和 \(V_{BF}\) 参数下比较低能负宇称能带，
并把实验带与理论带建立映射。能谱再现说明该组模型输入可描述部分低能结构，
不能单独确认 wobbling。

### Mixing ratio

第 11 章使用
\[
\delta
=0.835\,E_\gamma[\mathrm{MeV}]
\frac{\langle I_f\Vert T(E2)\Vert I_i\rangle[e\,b]}
{\langle I_f\Vert T(M1)\Vert I_i\rangle[\mu_N]}.
\]

IBFM-2 的 E2 算符包含玻色核芯贡献；M1 算符包含轨道、自旋、核芯和占据振幅
相关项。因而 \(\delta\) 的大小可能由：

- E2 矩阵元增强；
- M1 矩阵元变小或发生相消；
- \(\gamma\)-soft 核芯波函数；
- 单粒子空间、配对和构型混合

共同决定。大 \(|\delta|\) 不能自动翻译成“大集体 E2”。

### Chapter examples

- \(^{135}\mathrm{Pr}\)：IBFM-2 对相关 B1/B2 到 yrast 连接多给出接近零或
  \(|\delta|<1\) 的结果；章节指出近期小混合比测量与该模型相容，而早期大混合比
  测量代表不同实验分支；
- \(^{127}\mathrm{Xe}\)：低自旋 B2 到 yrast 的大 \(|\delta|\) 可由过小的 M1
  矩阵元产生；章节将其联系到半填充 \(νh_{11/2}\) 和低自旋构型混合；
- \(^{133}\mathrm{La}\)、\(^{105}\mathrm{Pd}\)：模型与实验的 \(\delta\) 比较也依赖
  带映射、轨道身份和实验数据版本。

## Evidence Contract

IBFM 结果与实验比较应保存：

```text
IBFM Hamiltonian/PES -> single-particle space -> V_BF parameters
                    -> wavefunctions -> E2/M1 matrix elements
                    -> signed delta(E2/M1)
                    -> experimental roots, covariance, lifetimes and alternatives
```

实验端必须保留 \(\delta\) 的全部可容许根、角分布/偏振响应、取向参数和效率协方差。
模型与某一根一致只能说明条件性相容，不能把该根变成独立验证。

## What It Cannot Establish Alone

- IBFM-2 的小 \(\delta\) 不能单独证明 signature partner；
- 大 \(\delta\) 不能单独证明 wobbling；
- \(\gamma\)-soft 核芯计算不能单独测量实验 \(\gamma\)-刚性；
- 能谱和 \(\delta\) 同时拟合不等于独立预测，除非定标量和 holdout 观测预先区分；
- 章节中的模型带标签不能替代实验能级、寿命、偏振和原始计数的身份确认。

## Sources and Locators

- PDF pp.239–243 / printed pp.220–224：IBFM-2 哈密顿量、SCMF–IBM 映射和
  \(\gamma\)-soft 势能面；
- PDF pp.244–246 / printed pp.225–227：式 (11.10)–(11.12)、\(^{135}\mathrm{Pr}\)、
  \(^{127}\mathrm{Xe}\) 等混合比；
- PDF pp.247–255 / printed pp.228–236：IBFFM-2、奇奇核和模型电磁性质边界。

## Sources

- [[book-petrache-chirality-and-wobbling]]
- [[petrache-ch5-experimental-wobbling-evidence-contract]]
- [[wobbling-mixing-ratio-phase-and-transition-diagnostics]]
- [[experimental-uncertainty-propagation-and-double-root-triage]]
