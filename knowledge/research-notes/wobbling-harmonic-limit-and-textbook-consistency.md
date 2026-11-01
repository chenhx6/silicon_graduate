---
type: research-note
title: "摆动谐近似的涨落尺度、角度平方与教材一致性检查"
aliases: [摆动近似适用域自审]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: reflect
evidence_sources: [book-bohr-mottelson-nuclear-structure-vol2, book-petrache-chirality-and-wobbling]
promotion_target:
tags: [wobbling, harmonic-approximation, triaxiality, textbook-consistency]
---

# 摆动谐近似：把“高自旋”转成可检查的误差尺度

## 问题与保留理由

低自旋摆动争议同时涉及观测、模型和术语。若只记住一个固定自旋下限，后续模型筛选可能把近似条件变成普适排除规则。本条保存可复算的推导、教材间疑点和会改变判断的条件；不以此裁决任何实际核的摆动指认。

## 直接来源与本任务推导

直接来源：[[book-bohr-mottelson-nuclear-structure-vol2]] §4-5e，PDF 212–214 / pp. 190–192，Eqs. 4-296–4-307。本轮同时核对公式图像。令自旋 I 以 ħ 为单位，A_k=ħ²/(2ℑ_k)，参考转轴为最大惯量轴 1。固定 I 的能量曲面在该轴附近有两个正曲率，对应 A2−A1、A3−A1。

玻色展开为

\[
H'=\alpha(c^\dagger c+\tfrac12)
 +\tfrac{\beta}{2}(c^{\dagger2}+c^2),\quad
\alpha=I(A_2+A_3-2A_1),\quad\beta=I(A_2-A_3).
\]

正则变换保持 x²−y²=1，频率满足

\[
\hbar\omega=\sqrt{\alpha^2-\beta^2}
=2I\sqrt{(A_3-A_1)(A_2-A_1)}.
\]

原书 Eq. 4-306–4-307 要求横向涨落远小于 I²。将它重写成诊断量是**本任务代数重构**：

\[
C=\frac{A_2+A_3-2A_1}{2\sqrt{(A_3-A_1)(A_2-A_1)}}\ge1,
\qquad
\varepsilon=\frac{(2n_w+1)C}{I}\ll1.
\]

在同一领先阶近似下 ε≈⟨I2²+I3²⟩/I²≈⟨sin²θ⟩。因此角度尺度关联的是**正弦平方**。这里 I²≈I(I+1) 也是高自旋近似的一部分；不宣称低自旋数值精确。

## 可复算的人工参数例

取 ℑ1,ℑ2,ℑ3=(30,10,5) ħ²/MeV，n_w=1。它们是人为模型参数，**不是目标核拟合或实验测量**。

| I | ε（领先阶模型） | 解释 |
| --- | --- | --- |
| 8 | 0.41505 | 小参数不小，不能信任谐近似的精密预测 |
| 17 | 0.19532 | 仍须比较完整量子解；不是任意 10° 门槛的自动通行证 |
| 40 | 0.08301 | 相对更接近展开极限，误差仍依赖所求观测量 |

```python
import math
A1, A2, A3 = 1 / 60, 1 / 20, 1 / 10  # MeV
C = (A2 + A3 - 2*A1) / (2*math.sqrt((A3-A1)*(A2-A1)))
for I in (8, 17, 40):
    print(I, 3*C/I)
```

## 两处不可混并的检查

1. [[book-petrache-chirality-and-wobbling]] Ch. 5 PDF 119 / p. 100，Eq. 5.1 写 I2²+I3²=I²sin²θ，但随后的 Eq. 5.2–5.3 使用 sinθ 而非 sin²θ，并以 10° 给出一/二声子的约 17/28 自旋估算。本轮按 BM Eq. 4-307 重构，发现该角度步骤**存在待核的平方一致性问题**。不能在未解释该步骤前把 17ħ/28ħ 写成严格普适阈值。该疑点也不使整章的实验测量自动失效。
2. 原书 Ch. 2 PDF 45–46 / pp. 26–27 在能量极大、最小惯量轴附近也讨论经典稳定进动，并区分中间**惯量**轴不稳定的 separatrix。形状几何的“中轴 m”与惯量大小排序的“中间轴”不是同一个词义。纯自由刚体绕极小惯量轴也可稳定，不可把“yrast 偏好最大惯量轴”改成“所有其它主轴转动都不稳定”。核多体惯量与经典刚体形状惯量也不应默认等同。

## 反向检验、替代解释与下一步

- 量纲：C 与 ε 无量纲；频率表达中的 A 为能量。
- 轴对称横向极限 A2=A3>A1：C=1，ε=(2n_w+1)/I。
- 接近 A2=A1：谐频率趋零且 C 发散；频率低不能同时被当成模式特别清晰的证据。
- 完整量子转子、PTR 波函数或自旋相干分布可直接计算 ⟨I2²+I3²⟩，检验展开误差随 I 的实际变化。这是下一项计算，而不是要求实验者先接受 10° 的人为阈值。
- γ 软核、TiP 或其它耦合模式可以产生不同涨落尺度；须分别建立波函数与观测响应，不能以纯转子的 ε 直接证伪它们。

## Promotion or Rejection History

2026-11-02，provisional：完成 BM 原式与局部代数 self-audit；角度平方疑点保留 `needs_review: true`，待比对原作者推导或勘误。没有新的真实核数据结论，不晋升为实验判据，不标 human-reviewed。
