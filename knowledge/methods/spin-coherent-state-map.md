---
type: method
title: 自旋相干态图
aliases: [spin coherent state map, SCS map, azimuthal plot]
created: 2026-07-01
updated: 2026-07-01
status: active
review_status: unreviewed
method_type: angular-momentum-geometry-visualization
tags: [wobbling, chirality, angular-momentum]
---

# 自旋相干态图（Spin Coherent State Map）

## Purpose

把角动量约化密度矩阵映射为内禀系中取向概率分布，提炼量子态对应的经典进动几何。

## Inputs and Assumptions

模型波函数或约化密度矩阵，以及统一的主轴和角度约定。

## Procedure

在自旋相干态过完备基底中计算 `P(θ,φ)`。

## What It Can Establish

显示 planar/aplanar、wobbling 进动锥、flip 多峰和手征左右手分布。

## What It Cannot Establish Alone

它是模型波函数的表示，不是直接实验图像；有限分辨率来自基底非正交性。

## Conventions and Systematics

需注明 θ、φ 定义、轴排序和概率归一化。

## Examples

[[frauendorf-2024-wobbling-review]] 用 SCS 图区分 TW/LW/FM；1997 手征工作给出其早期几何基础。

## Sources

- [[frauendorf-2024-wobbling-review]]
- [[chen-2022-study-wobbling-spin-coherent-state-maps]]

## Evolution Log

- 2026-07-01：建立角动量几何可视化用途。
## Day22 SCS相位、测度与模式边界（checkpoint093）

原044的未统一体固/实验室相位展开与“当且仅当10–100 W.u.、M1占优必为TiP”认证撤回。[[chen-2022-study-wobbling-spin-coherent-state-maps]] CF22-D22-R093-3给出R†旋转最高投影态的定义，并明确体固总J和通常j的升降/角变量符号关系；跨实现应按该约定重建。

若定义Q(θ,φ)=(2I+1)⟨θφ|ρ|θφ⟩/(4π)为每单位立体角密度，则归一使用dΩ=sinθdθdφ；每单位dθdφ的密度还需乘sinθ。不能把两种绘图测度混用。

特定PTR低spin例子的n=0斑团与n=1环带支持作者TW拓扑解释，但不要求所有有限I态都为严格谐声子。近不稳定区可混合/变形，标签要随波函数与矩阵元检查。图像是模型表示，不能直接作为实测进动锥、核内电荷流或绝对B的证明；较窄SSS表示也不是独立实验压缩（见[[spin-squeezed-state-map]]）。

旧SCS-METH-076-1的25.4倍核素解耦推断继续撤回：未输入实际过渡密度或寿命，不可补造局域电荷流。

## Day22 checkpoint101：相同RMS可以对应不同SCS图

[[chen-2022-study-wobbling-spin-coherent-state-maps]] CF22-D22-R101-1/2先核一页Publisher Erratum替换Fig15，避免错误图参与推断。图上的Iν下标不是直接声子数，也不是实验band编号。

为检验RMS信息，采用该文D2允许的I=4基底`|K=0⟩,(|2⟩+|−2⟩)/√2,(|4⟩+|−4⟩)/√2`。两个人工混合密度的三基权重分别`(23,16,21)/60`和`(17,24,19)/60`，均正、归一，且均有`⟨J1²⟩=⟨J2²⟩=⟨J3²⟩=20/3`。但`⟨J3⁴⟩`为`1408/15`及`1312/15`，SCS密度不同；在θ=π/2、φ=π/4，单位立体角密度约.07703与.05726。积分均为1，六项限定控制通过。

这是三RMS不够重建完整密度的物理正性反例，不表示两者是同一转子Hamiltonian的本征态，不给TW/LW/flip标签，也没有算跨spin过渡密度或B(E2)。本代码Q按dΩ归一；CF22实际圆柱图P=sinθQ按dθdφ归一，不能比较不同测度的峰宽。后续对模型的实验检验应比较它们预测的能谱/跃迁向量，不能把模型密度图当已测三维角动量。needs_review: true。
