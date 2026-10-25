---
type: method
title: 自旋压缩态图
aliases: [spin squeezed state map, SSS map]
created: 2026-07-01
updated: 2026-07-01
status: active
review_status: unreviewed
method_type: angular-momentum-wavefunction-visualization
tags: [wobbling, angular-momentum]
---

# 自旋压缩态图（Spin-Squeezed-State Map）

## Purpose

将有限自旋空间中的波函数映射为更接近一维角变量概率密度的表示，用于分析 wobbling 和 flip 模式。

## Inputs and Assumptions

模型波函数、轴与角变量约定。

## Procedure

在自旋压缩态基底中投影并比较势阱所包围的主轴。

## What It Can Establish

辅助分类 TW/LW/FM，并观察波函数节点和多峰结构。

## What It Cannot Establish Alone

过完备表示存在一定可视化歧义；结论需与能量和电磁跃迁一致。

## Conventions and Systematics

需保留作者使用的坐标、相位和归一化。

## Examples

[[frauendorf-2024-wobbling-review]] 将 SSS 作为 SCS 的补充。

## Sources

- [[frauendorf-2024-wobbling-review]]
- [[chen-2022-study-wobbling-spin-coherent-state-maps]]

## Evolution Log

- 2026-07-01：由 2024 综述建立。
## Day22 SSS定义纠错（checkpoint093）

旧045将本表示直接等同于Bogoliubov压缩本征态，并给出了互为倒数的惯量比等式，认证撤回。局部HFA振子的压缩参数可以是另一项分析，但不能替代review中SSS的定义。

[[frauendorf-2024-wobbling-review]] F24-D22-R093-1的SSS是有限K空间密度矩阵的角表示：

    P(φ) = (1/2π) ΣKK′ exp[−i(K−K′)φ] ρKK′。

生成态为均匀K振幅(2I+1)^−1/2ΣK|IIK⟩，再绕3轴旋转。它不是K=0投影态。I和轴/φ约定须固定，且∫P(φ)dφ=Trρ=1。

### 局域生成态的有限Fourier核

任务解析控制：D=2I+1，ρKK′=1/D时，P(φ)=sin²(Dφ/2)/[2πD sin²(φ/2)]，在φ=0取连续极限D/(2π)，首零点φ=2π/D。若ρ在K基底对角，P恒为1/(2π)。这些是该表示的归一/基底局域性，不是某核的实测压缩或γ刚度。

SSS的角分辨和SCS的球面模糊范围不同；同一模型态换表示可更清楚呈现节点，但没有新增独立物理数据。选模仍需能谱/矩阵元及竞争解释，不能单凭图像窄峰或M1份额唯一改判。hfa-sss-controls-093.json用任意I=11/2作归一/正性/首零点控制，不代表163Lu的拟合。
