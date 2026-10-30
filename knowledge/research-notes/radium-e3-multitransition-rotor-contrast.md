---
type: research-note
title: "222,228Ra 多跃迁 E3 与转子预言对比：临界连接、相位与耦合边界"
aliases: [Radium E3 rotor contrast, Butler 2020 critical E3 links]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
confidence: medium
evidence_sources: [butler-2020-222-228ra-octupole-evolution, gaffney-2013-pear-shaped-rn-ra]
created_from: Day27 continued octupole reading and conditional contrast study
promotion_target: ""
tags: [octupole, E3, 222Ra, 228Ra, rotor-model, identifiability]
---

# 关键 E3 连接如何区分转子图样与振动反例

## Research Trigger

单一大 B(E3;0+→3−) 不能区分静态梨形形变与动态八极关联。Butler 2020 Table I 给出了 222Ra 与 228Ra 的多条 E3 约化矩阵元。本笔记检验：固定 K=0 轴对称转子关系时，哪条关键连接与转子预言差异最明显，以及这一对比受到哪些耦合与协方差限制。

## Grounded Evidence

[[butler-2020-222-228ra-octupole-evolution]] PRL PDF p.3 Table I 给出实验测得的约化矩阵元（单位 e b^(3/2)）：
- 222Ra：⟨0+||E3||3−⟩=1.13(9)，⟨2+||E3||3−⟩=−0.9(5)（该项为自由变分参数，未标星号）；
- 228Ra：⟨0+||E3||3−⟩=0.87(15)，⟨2+||E3||3−⟩=−0.06(+0.23/−0.16)*（标星号，原文明确说明通过旋转关系与更高阶矩阵元耦合，不完全独立）。

同表采用共同相对相位约定：222Ra 取 Q1 与 Q3 同号，228Ra 取异号。

## Rotor Model Contrast

在 K=0 轴对称刚性转子极限下，由同一内禀 Q30 决定的两个矩阵元满足

\[
\frac{\langle2^+\Vert E3\Vert3^-\rangle}{\langle0^+\Vert E3\Vert3^-\rangle}
=-\sqrt{\frac{4}{3}}\approx -1.1547.
\]

若由基态 ⟨0+||E3||3−⟩ 预言 ⟨2+||E3||3−⟩：
- 222Ra：转子预言值为 −1.305 e b^(3/2)，实测中心值为 −0.9，差量为 +0.405 e b^(3/2)。按原表单误差端点构成的包络区间为 [−0.199, +1.009]，包含零。
- 228Ra：转子预言值为 −1.005 e b^(3/2)，实测中心值为 −0.06，差量为 +0.945 e b^(3/2)。按原表单误差端点构成的包络区间为 [+0.611, +1.348]，明显偏离转子比值。

## Provisional Reasoning

228Ra 的 ⟨2+||E3||3−⟩ 近零值构成了偏离刚性转子预言的灵敏指标，支持作者的八极振动与转动对齐声子解释。与此形成对照，222Ra 的 ⟨2+||E3||3−⟩ 维持较大的负值，与转子预言相容。

这证明多跃迁网络比单一基态 E3 具有更高的可辨识性；但不能将该对比直接写成统计假设检验的 p 值或模型后验比。

## Assumptions

1. 转子预言严格采用 K=0 轴对称极限；
2. 相位约定沿用原文表格相对符号；
3. 不假设未报告的参数间协方差，仅做输入端点包络核对。

## Competing Explanations

近零矩阵元除八极振动外，也可能受到 K 混合、高激发态组态混合或未观测通道耦合的影响；接近转子预言的矩阵元也可能由有限维基底中的声子凝聚模拟。

## Transfer Conditions

对比仅适用于相同相角定义、相同 GOSIA 拟合条件下的多步库仑激发数据集；不能将 Ra 的多跃迁平坦度判据直接套用到仅有单条基态 E3 的核素（如 144,146Ba）。

## Failure Conditions

1. 若 228Ra 标星矩阵元在释放高自旋耦合后中心值大幅偏移，本对比需重新评估；
2. 若忽略 E1 与 E3 相对相位的不确定性，符号定义将失效；
3. 若把输入端点包络误当成联配置信椭圆，推断将不可靠。

## Falsification or Reverse Tests

运行可复现对比脚本：
```bash
python3 system/scripts/day27_e3_rotor_contrast.py --output-dir outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/e3-contrast
```
检查在假设相关系数从 −1 到 +1 变化时，222Ra 差量标准差在 [0.396, 0.604] 范围内受控。

## Open Questions

在完整 GOSIA 输出矩阵元协方差不可得的情况下，能否通过释放星号耦合的重拟合直接检验 228Ra 近零连接的稳健性？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

本页为 Codex 基于已归档正文及附加材料的 self-audit，保持 `review_status: unreviewed`。

## Promotion or Rejection History

- 2026-10-29：基于 Butler 2020 实际矩阵元建立转子预言对比与耦合边界。

## Agent self-audit triage

P0: none identified。数值已由独立脚本验证，未把标星耦合项冒充独立实验值。P1：原件完整协方差与高阶矩阵元未得，结论限于表列输入对比。P2/P3：保持引用和元数据规范。
