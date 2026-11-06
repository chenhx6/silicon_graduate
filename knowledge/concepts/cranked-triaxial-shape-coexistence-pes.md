---
type: concept
title: "Cranked Strutinsky triaxial shape coexistence potential energy surface (PES) and spin-induced yrast shape transitions"
aliases: [shape-coexistence-pes, cranked-strutinsky, triaxial-oblate-coexistence, yrast-shape-crossing, 130ba-pes]
created: 2026-11-04
updated: 2026-11-06
status: ai-draft
review_status: unreviewed
tags: [triaxiality, shape-coexistence, cranked-strutinsky, pes, potential-energy-surface, 130ba, 76kr, 186pb]
---

# 推转形状共存势能面：固定频率与固定自旋的边界

## Definition

形状共存研究比较不同组态、形变和量子态的能量及电磁连接。势能面上的多个局部极小是模型信息；仅由极小或两支曲线相交，不能确认实验形状共存、一阶相变、摆动或手征模式。

[[book-bohr-mottelson-nuclear-structure-vol2]] 的 BM2-10 指出，壳结构能的局部极小是否成为形状异能态还取决于平滑能量部分（PDF620／printed598及PDF627／printed605）。BM2-13已撤回旧页未绑定核素、输入、输出的极小坐标与交叉频率。

对一个给定形状、单轴、常惯量的示意转子，固定角频率的消元给出 Routhian：

\[
E'(q;\omega)=E_0(q)-\tfrac12\mathcal J_x(q)\omega^2.
\]

这里 \(q\) 表示形变；若用 \(u=\hbar\omega\) 的数值单位MeV、\(\widetilde{\mathcal J}=\mathcal J/\hbar^2\) 的单位MeV⁻¹，则转动项为 \(-\widetilde{\mathcal J}u^2/2\)。它不是固定自旋的总能量。相应单轴转子在固定无量纲自旋I下采用 \(E_I(q)=E_0(q)+\hbar^2I(I+1)/(2\mathcal J_x(q))\)，其适用近似和量子修正必须另行说明。

同一频率下不同形状通常有不同角动量；固定频率交叉不能直接等同于同一I的yrast换支。需要一致的角动量约束或Legendre变换、组态追踪和带混合处理。

## Necessary Assumptions

`cranked_triaxial_shape_coexistence_pes_engine.py` 是指定多项式背景、Gaussian形变势谷及惯量函数的演示。它不从单粒子谱求Strutinsky平滑能，也不求HFB自洽场。惯量的形变幂律和势谷深度属于输入假设；不能由函数命名取得原书或真实核素认证。

## Discriminating Observables

实际应用需同一核素的组态与能带身份、相对激发能、转动顺排以及具有共同定标的绝对E2／静态矩。多组态混合可以形成回避交叉，能量接近不唯一确定形状。该示意势能面没有计算这些实验响应。

## Supporting Evidence

当前来源支持平滑能与壳结构竞争的一般物理图像。旧页列出的固定beta/gamma极小、惯量区间及0.236/0.262/0.232交叉数值，未建立原件或可追溯核素计算链，已撤回其物理结果身份。没有把旧命令注释当成测量或验证。

保留CLI接口供演示复算：

```bash
python3 system/scripts/analysis/nuclear_analyzer.py coexpes --preset 130Ba_triaxial_oblate_coexistence
```

该旧预设名是兼容标识；程序已将预设标为`synthetic_model_benchmark`。输出只描述输入曲面上的模型交叉。

## Counter-evidence and Competing Interpretations

极小可以由人为势谷直接产生；改变势谷、惯量或限制区间可能改变交叉。有限网格／局部优化不保证找到所有极小和全局鞍点。真实系统还可涉及配对、组态换支和隧穿；本模块未建立相变阶数或模式稳定性。

## Our Current Position

保留条件模型定义与数值演示入口，撤回未建证据链的核素数字和实验确认身份。本轮传播已有BM-II归属更正，不新增PES计算、参数拟合或真实核结构判定。

## Sources

- [[book-bohr-mottelson-nuclear-structure-vol2]]：BM2-10、BM2-13及其精确页码。
- `system/scripts/analysis/cranked_triaxial_shape_coexistence_pes_engine.py`：本地演示实现，不是外部物理证据。
