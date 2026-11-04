---
type: method
title: "Petrache Ch.5：在束 γ 谱学中的 wobbling 实验证据合同"
aliases: [Petrache Ch.5 experimental wobbling, P-DCO wobbling evidence, low-spin wobbling audit]
method_type: "experimental-wobbling-evidence"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Petrache ed. Ch.5 PDF pp.110-126 / printed pp.91-107"
confidence: "high for chapter-level experimental workflow; conditional for nuclear assignments"
tags: [in-beam-gamma, wobbling, P-DCO, polarization, mixing-ratio, lifetime, experimental-analysis]
sources: [book-petrache-chirality-and-wobbling]
---

# Petrache Ch.5：在束 γ 谱学中的 wobbling 实验证据合同

## Purpose

把第 5 章的实验经验转成可执行的在束 \(\gamma\) 谱学审计顺序，服务低能/中高自旋
wobbling、TiP、signature partner 和 \(\gamma\)-vibration 的竞争解释。

## Inputs and Assumptions

实验合同至少应保存：

- 能级、跃迁能量、强度、门条件和随机符合处理；
- 自旋宇称、带内与带间连接、\(\Delta I=1\) 路径；
- 角分布、方向角关联、线偏振和混合比 \(\delta(E2/M1)\)；
- 定向参数/取向方差 \(\sigma/I\) 及其协方差；
- 寿命、侧馈、效率、内转换和绝对/相对 \(B(E2),B(M1)\)；
- 同组态的 \(J^{(2)}\)、对齐 \(i_x\) 与转动频率演化；
- 原始计数、响应校准、门条件和可复现的拟合输入。

第 5 章开头还强调高统计量、峰背比和探测器单元数对高自旋级联与符合关系
的重要性。弱带和弱连接线不能脱离探测效率、峰背比和符合条件直接解释。

## What It Can Establish

### High-spin wobbling workflow

在高自旋、小偏转角区域，\(\gamma\) 谱可以先检查：

1. 候选带是否共享同一准粒子组态和近似相同的转动性质；
2. 是否存在一声子带到正常带的 \(\Delta I=1\) 连接；
3. wobbling 能量是否符合高自旋近似的能级演化；
4. 连接跃迁是否具有相对于 signature partner 更强的集体 E2 分量；
5. 多声子带是否呈现合理的连接网络，而非单条偶然跃迁。

第 5 章给出一个粗略的小振幅估算：若把偏转角限制在约 \(10^\circ\)，一声子和
二声子参考自旋约在 \(I>17\) 与 \(I>28\) 以上。这只是摆动近似的尺度估算，
不是实验硬阈值。

### Low-spin mixing-ratio audit

低自旋候选的关键连接线通常要联合：

- 角分布或方向角关联；
- 线偏振；
- \(\delta(E2/M1)\)；
- \(\sigma/I\) 取向参数；
- 寿命和强度。

第 5 章记录了 P-DCO 方法：将线偏振与定向态方向角关联结合，并用两点角关联比
\(R_{\mathrm{ac}}\) 替代传统 \(R_{\mathrm{DCO}}\) 的部分分析路线。理论角分布和偏振
同时依赖 \(\delta\) 与 \(\sigma/I\)，因此不能把一条偏振符号直接翻译成唯一模式。

### \(^{135}\mathrm{Pr}\) and \(^{187}\mathrm{Au}\)

第 5 章总结了不同实验工作对低自旋连接线得到互相矛盾的 \(\delta\)：

- 大混合比分支支持更强 E2 集体性；
- 小混合比分支提示 M1 主导和 signature-partner/单粒子竞争解释；
- 重新实验使用 P-DCO 及 \(R_{\mathrm{ac}}\) 后，报告了小混合比结果；
- 不同工作之间的差异需要回到原始计数、门条件、取向参数和拟合协方差审计。

因此正确的分析对象是完整似然或至少完整的双根/多根分支，而不是只保留一个
“最接近理论”的 \(\delta\) 根。

### Medium-spin even-even candidates

第 5 章讨论 \(^{130}\mathrm{Ba}\) 和 \(^{136}\mathrm{Nd}\) 的两准粒子候选。其经验教训是：

- 两个准粒子的总角动量可以提高 wobbling 稳定性；
- 可同时比较能谱、能量差、\(B(M1)_{\rm out}/B(E2)_{\rm in}\) 和
  \(B(E2)_{\rm out}/B(E2)_{\rm in}\)；
- 连接线的 M1 分量可能超过 E2，但相对于 signature partner 仍可显示增强的 E2；
- “E2 必须占绝对多数”不是所有构型和质量区的必要条件。

## What It Cannot Establish Alone

- 频率下降、近简并、\(\Delta I=1\) 连接或大 \(|\delta|\) 不能单独确认 wobbling；
- 小 \(|\delta|\) 可以削弱某个 wobbling 解释，但仍需检查组态、寿命、\(\gamma\)-soft
  核和其它单粒子模型；
- 粗略自旋下限不是统计显著性阈值；
- \(R_{\mathrm{ac}}\)、偏振或 DCO 比值的拟合必须保留取向、几何、效率和根分支；
- \(^{130}\mathrm{Ba}\)、\(^{136}\mathrm{Nd}\) 的模型再现是特定 PRM/TPSM/CDFT 输入下的
  结果，不是跨核素的普适判据。

## Reproducibility Contract

每个候选跃迁至少应归档：

```text
raw counts -> calibration/efficiency -> gate definition
           -> angular/polarization response -> nuisance covariance
           -> all delta roots -> lifetime/branching conversion
           -> model comparison and competing interpretations
```

第 5 章明确倡议标准化分析和公开数据，以便在不同实验结果矛盾时交换原始数据、
复现拟合和定位 \(\delta\) 根、取向或响应处理造成的差异。

## Evidence and Locators

- PDF pp.110–111 / printed pp.91–92：高统计、峰背比、阵列符合和实验背景；
- PDF pp.119–123 / printed pp.100–104：低自旋争议、P-DCO、\(R_{\mathrm{ac}}\)、混合比
  和 \(^{135}\mathrm{Pr}\)/\(^{187}\mathrm{Au}\)；
- PDF pp.123–126 / printed pp.104–107：\(^{130}\mathrm{Ba}\)、\(^{136}\mathrm{Nd}\)、
  两准粒子 wobbling 与开放问题；
- PDF p.126 / printed p.107：标准化分析、公开数据和可复现性倡议。

## Sources

- [[book-petrache-chirality-and-wobbling]]
- [[petrache-ch11-ibfm-mixing-ratio-contract]]
- [[experimental-uncertainty-propagation-and-double-root-triage]]
- [[wobbling-mixing-ratio-phase-and-transition-diagnostics]]
- [[wu-experimental-methods-deadtime-hpge-rdm-contract]]
