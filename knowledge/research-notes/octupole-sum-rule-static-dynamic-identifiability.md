---
type: research-note
title: "E3 完备性、非能权和规则与静态/动态八极形状可辨识性"
aliases: [octupole E3 sum rule localization, Day26 Butler 2020 static dynamic octupole]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [butler-2020-222-228ra-octupole-evolution, gaffney-2013-pear-shaped-rn-ra, bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole]
created_from: Day26 direct reading of Butler 2020 and E3 closure analysis 027
promotion_target: octupole-and-rare-electromagnetic-decay
tags: [octupole, E3, sum-rule, static-shape, octupole-vibration, identifiability]
---

# E3 完备性与静态/动态八极形状可辨识性

## Research Trigger

单一大 $B(E3;3^-\to0^+)$ 只能证明一个强跃迁。Butler *et al.* 2020 对 `222Ra` 与 `228Ra` 给出多条 E3 矩阵元，提供了比较静态梨形与八极振动的更高信息量实验合同。本笔记把该合同与闭合关系、非能权和规则及高阶形状涨落边界分开保存；脚本 027 只算表列矩阵元的部分和，不宣称完整 sum rule。

## Grounded Evidence

[[butler-2020-222-228ra-octupole-evolution]] 的实际正文为 PRL PDF 1–6；arXiv v1 PDF 1–16 还包含附加页 7–16 的能级图、代表性 GOSIA 产额、E2 系统学和 E1 Table II。PRL PDF p.3 Table I 给 `222Ra` 的 E3 中心矩阵元 `0+→3−=1.13(9)`, `2+→1−=0.85(24)`, `2+→3−=−0.9(5)`, `2+→5−=1.79(20)`, 以及若干标星耦合项；`228Ra` 给 `0+→3−=0.87(15)`, `2+→1−=1.36(23)*`, `2+→3−=−0.06(+0.23/−0.16)*`, `2+→5−=1.71(23)*`, `4+→1−=0.4(+0.7/−1.1)*`。星号项由较低矩阵元按旋转关系耦合，非完全独立。

PRL PDF p.4 Fig.4 与正文显示，`222,224,226Ra` 多条转换导出的 $Q_3$ 近似恒定；`228Ra` 的 `2+→3−` 和 `1−→4+` 近零。作者在 PRL p.1 摘要、p.5 讨论中把这组模式解释为 `222Ra` 的稳定八极形状与 `228Ra` 的八极振动，同时承认 `222,224,226Ra` 的近基态能级行为受配对影响，旋转对齐八极声子仍可提供不要求永久梨形的解释。

[[gaffney-2013-pear-shaped-rn-ra]] Table 1/2 提供 `220Rn`、`224Ra` 的 E3 矩阵元和 $Q_3$；该实验的多条 Q3、E2/E3 系统学是 `224Ra` 与 `220Rn` 的早期跨核对照。[[bucher-2016-144ba-direct-octupole]] 与 [[bucher-2017-146ba-direct-octupole]] 提供 `144,146Ba` 的直接 `0+↔3−` E3，约 `48 W.u.`，但只有选定基态 E3 的单条直接强度，不能单独完成多态形状辨识。

## Provisional Reasoning

### 0+ 的非能权 E3 闭合关系

设 $M_{3\mu}=e\sum_i r_i^3Y_{3\mu}(\hat r_i)$，初态为 $|0^+\rangle$。在完整的负宇称 $3^-_f$ 本征态集合上，非能权和为

$$m_0(E3;0^+)=\sum_f B(E3;0^+\to3^-_f)=\sum_{f,\mu}|\langle3^-_f,\mu|M_{3\mu}|0^+\rangle|^2=\sum_\mu\langle0^+|M_{3\mu}^{\dagger}M_{3\mu}|0^+\rangle,$$

其中采用 $B(E3;0\to3)=|\langle3\|M(E3)\|0\rangle|^2$ 的约化矩阵元约定。因每一项非负，单条已测 `0+→3−` 只给 $m_0$ 的下界（若该矩阵元、方向和单位转换均正确）；它不能给出未观测高阶 $3^-$ 态的剩余强度。实验表中不同初始自旋的 E3 行不能直接相加成这个 `0+` sum，因为它们属于不同初态的闭合关系。

能量加权和

$$m_1(E3;0^+)=\sum_f(E_f-E_0)B(E3;0^+\to3^-_f)=\frac12\sum_\mu\langle0^+|[M_{3\mu}^{\dagger},[H,M_{3\mu}]]|0^+\rangle$$

需要哈密顿量、能级和算符交换子；Butler Table I 没有提供 closure-complete `m1`，因此不能从几条 GOSIA 矩阵元推出普适能量加权规则。对高阶形状涨落，$m_0$ 是算符平方的二阶统计量；要区分静态局域形状与动态软度，还需要势能面/集体惯量、能级分布和至少多条有相位约束的跃迁核。

### 多态图样为何增加可辨识性

轴对称 $K=0$ 转子若具有近似固定内禀 $Q_3$，不同 $I^+\leftrightarrow I'^-$ E3 矩阵元除 Clebsch–Gordan 因子外应共享同一 $Q_3$；因此将多个矩阵元转成 $Q_3(I,I')$ 并检查跨自旋平坦度，比单条 `0+→3−` 多一个刚性检验。Butler 的 `222Ra` 图样满足作者的 rotor-like 解释，而 `228Ra` 的特定 `2+→3−` 近零项与 `148Nd` 对照支持振动图像。

这仍不是密度图像或唯一势能面解。旋转关系可能已经作为 GOSIA 约束进入星号项；相对 E3 相位、未观测高态、配对与旋转对齐声子都影响反演。高阶形状涨落若要在实验上被约束，至少需要：多个 $I^+\to(I+1)^-$ 与 $I^+\to(I+3)^-$ 矩阵元、相对相位/符号、能级与寿命、独立 E2 集体性，以及对激发态和高阶多极耦合的协方差。

## Assumptions

脚本 027 使用 Butler Table I 的打印中心值；所有平方均为部分、非能权的矩阵元平方，未把不同初态的行伪装成单一 `0+` 闭合和。Q3 比较采用论文给出的 rotor conversion，仅作图样诊断。实验误差、GOSIA 协方差和高能态未在脚本中重建。

## Competing Explanations

多条近恒定 Q3 支持稳定梨形或局域反射不对称，但也可能由有限态空间的旋转耦合和对齐八极声子产生；近零 E3 支持振动图样，却不自动排除组态混合、K 混合或未观测通道。E3 大小与 $\beta_3$ 静态值之间仍有模型映射。

## Transfer Conditions

Butler 的 `222/228Ra` E3 完备性判据只能在相近的态标记、相同 GOSIA 约定、可比的初末态覆盖和明确星号耦合边界下迁移到 `224/226Ra` 或 `144/146Ba`。Ba 的单条直接 E3 不足以套用 Ra 的多态 Q3 平坦度判据。

## Failure Conditions

若高阶 E3 条目主要由旋转关系固定、相对相位未知、负宇称带有未观测强混合或数据仅给绝对矩阵元，Q3 平坦度不能视为独立静态证据。若遗漏高能 $3^-$ 强度，部分 `m0` 不能作为完整集体强度。

## Falsification or Reverse Tests

对同一核同时拟合 rotor、软振动和对齐八极声子模型，释放星号耦合并保留完整协方差；检查它们能否共同重现实测 E3 绝对值、相对相位、E2/能级和附加 $I$ 跃迁。若 rotor 只能靠逐项重设 $Q_3$ 才拟合，而振动模型预测的关键近零/增强图样被独立跃迁否定，则相应解释应降级。

## Open Questions

`222Ra` 的高阶 E3 星号矩阵元在释放旋转耦合后仍保持 Q3 平坦吗？`228Ra` 的近零 `2+→3−` 是否由完整协方差显著支持？从 `m0` 到能量加权 `m1` 需要哪些高能负宇称态和激发能？Ba 是否能取得同样的多态 E3 网络？

## Human Review

本页为 Codex 基于 Butler 正文及 arXiv 附加页的 self-audit，`review_status: unreviewed`，未有用户人工审核。

## Promotion or Rejection History

2026-10-28：建立 provisional 研究笔记；待完整协方差、更多 E3 态和跨模型联合拟合后评估是否晋升。
