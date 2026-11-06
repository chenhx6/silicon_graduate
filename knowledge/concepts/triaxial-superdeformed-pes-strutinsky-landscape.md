---
type: concept
title: "Triaxial superdeformed 3D (beta_2, gamma, beta_4) potential energy surface, macroscopic-microscopic Strutinsky shell corrections and secondary well stabilization"
aliases: [tsd-pes-strutinsky, triaxial-pes-landscape, strutinsky-tsd-engine, high-spin-tsd-stabilization, 163lu-pes]
created: 2026-11-04
updated: 2026-11-06
status: ai-draft
review_status: unreviewed
tags: [triaxiality, superdeformation, potential-energy-surface, pes, strutinsky-method, high-spin, 163lu, 130ba]
---

# 三轴超形变势能面：壳结构极小与动力学稳定性分开检验

## Definition

宏观–微观方法将平滑能量与壳结构、配对等修正分开。给定模型中可以寻找正常形变与大形变局部极小，并比较相对能量和路径上的势垒；这不自动构成实验形状、异能态或摆动／手征模式的确认。

[[book-bohr-mottelson-nuclear-structure-vol2]] BM2-10（PDF620／printed598及PDF627／printed605）明确指出，总体平滑能量部分会影响壳能局部极小能否成为形状异能态。BM2-8、13的更正也撤回了没有核素输入、输出及原书定位的TSD退激与固定PES数字。

## Necessary Assumptions

在明确的固定I近似下，可组织为

\[
E(q;I)=E_{\rm macro}(q)+\delta E_{\rm shell}(q)
+\delta E_{\rm pair}(q;I)+E_{\rm rot}(q;I).
\]

每项必须有独立定义，并检查是否已在推转微观能量中计入转动贡献，避免重复计数。单轴转子式 \(E_{\rm rot}=\hbar^2I(I+1)/(2\mathcal J)\) 仅是指定近似；固定频率的Routhian使用不同的约束。

本地`triaxial_superdeformed_pes_strutinsky_engine.py`给定液滴多项式、经验惯量与Gaussian势谷。它没有从单粒子能谱执行Strutinsky平滑，也没有自洽求配对或量子态。因此代码中的shell correction只能指示意势谷。其固定beta4切片及二维网格，不是对全部rank4自由度的三维自洽极小化。

## Discriminating Observables

真实TSD解释需结合组态、转动顺排、电磁矩阵元、跃迁四极矩和退激路径等数据。即使模型中存在有势垒的局部极小，寿命还涉及惯量、耦合、态密度与隧穿／统计混合；仅凭势垒高度不能推出退激被阻止。

## Supporting Evidence

当前页没有建立具体核素的定量PES证据链。旧页列出的beta/gamma区间、25–40hbar阈值、65hbar²/MeV惯量、10–15MeV降能及确定势垒／极小数值，均撤回其原书结果或已验证核素计算的身份。它们不能由末尾增加“fixture”标签而继续作为科学结论。

```bash
python3 system/scripts/analysis/nuclear_analyzer.py tsdpes --preset 163Lu_TSD_potential_energy_surface
```

预设名是保留的演示入口。输出只描述所给参数化与网格；`has_secondary_tsd_well`等兼容字段表示程序搜索到的候选极小，不是对实际核素的稳定性裁决。

## Counter-evidence and Competing Interpretations

Gaussian势谷本身可预设多阱结构。网格边界、局部选择、形变阈值及选定路径会影响所谓势垒；路径上的峰值未证明是全维最小鞍点。局部极小也不保证有可辨量子态。模型下较大惯量降低固定I转动能的趋势不能生成普适阈值或固定降能。

## Our Current Position

本页保留可追溯的一般分解、约束和演示实现说明，撤回来源不明的核素数字及稳定性判决。不新增微观PES计算或参数拟合。

## Sources

- [[book-bohr-mottelson-nuclear-structure-vol2]]：BM2-8、10、13及其更正边界。
- `system/scripts/analysis/triaxial_superdeformed_pes_strutinsky_engine.py`：固定参数化的演示代码。
