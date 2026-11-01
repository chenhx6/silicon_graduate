---
type: concept
title: "巨偶极共振、TRK 积分与形变反演的模型条件"
aliases: [GDR与TRK模型条件]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [gdr, trk, deformation, model-boundary]
---

# 巨偶极共振、TRK 积分与形变反演的模型条件

## Definition

电偶极集体响应常用质子、中子密度相对振荡的图像讨论。TRK 的能量加权 E1 强度和对光吸收截面的积分有关，但二者是不同的量，不能把“截面积分不再乘 E”写成原始跃迁强度求和不加权。

当前计算器的经典量为 59.74 NZ/A MeV·mb。增强因子 κ 是外部模型输入；不能把默认 0.25 写成该核的实验测量，或把全部增强唯一归因于介子交换流。

## Necessary Assumptions

`gdr` 使用一个轴对称拉长椭球的**示意参数化**：给定 β2 → 轴比 → 频率比，并人为采用 1:2 强度权重和设定宽度。它不是一般三轴三峰计算，也未包含温度、展宽机制、有限窗口积分和其它多极/非共振背景。

在 β2=0 时两个中心相同。若以 208Pb 搭配 β2=0.30 演示，表示给双幻质量数强加一个人为形变输入，不能说观测到了 208Pb 的基态双峰形变。默认参数、平均质心标度和宽度均非核素实验表。

## Discriminating Observables

真实反演至少需光吸收谱、能量/效率校准、截面误差、探测响应、可用能区及 competing fit。应联合比较单峰/双峰/三峰与其它宽度机制，传播峰位、宽度、面积及 κ 的相关不确定度。体积守恒几何和形变定义也需统一。

## Supporting Evidence

现有数值程序只验证了**自身参数化的正反变换**与量纲。`calculate_trk_sum_rule`、`calculate_deformed_gdr_splitting` 和 `invert_beta2_from_gdr_peaks` 没有独立实验基准认证；此前输出的 2967.5、3709.3 等是参数模型结果，不是本任务实测结果。

经典书路线是 [[book-bohr-mottelson-nuclear-structure-vol2]] 第 6 章的振动与求和规则。但本轮实际只重读该卷 §4-5e；GDR 所在页的原式与 Danos 引文仍须补读，`needs_review: true`。不能用概览 source 的存在来伪造逐式核验。

## Counter-evidence and Competing Interpretations

- 一条展宽峰不保证球形；双峰也可能受其它结构与响应影响。
- 三轴形变一般需要三个轴向模；双洛伦兹假设不能自动覆盖它。
- 反演同一个正演公式得到相同 β2 是代数一致性，不是优于 0.001 的真实测量精度。
- 单一强度积分和有限能区覆盖不能无条件分离全部交换/相互作用贡献。

## Our Current Position

本工具暂作为演示和公式复查入口。未通过实际谱图、独立参考实现及来源公式的科学验证，不用于给目标核设定精密基态形变。

## Sources

- [[book-bohr-mottelson-nuclear-structure]]：书籍入口；GDR 章节尚待逐页核验。
- [[book-bohr-mottelson-nuclear-structure-vol2]]：已登记第二卷原件与本轮实际阅读边界。

## Evolution Log

2026-11-02：撤回旧“实测输出”“精确测得 κ=0.25”“三轴双峰通用公式”“反演误差<0.001”与生产级认证。保留程序和可复算演示，科学校准待完成。
