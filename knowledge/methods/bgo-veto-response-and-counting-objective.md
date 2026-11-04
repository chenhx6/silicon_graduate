---
type: method
title: "BGO 反符合门：时间接受度、随机否决与计数目标的条件化计算"
aliases: [BGO-veto-count-model]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
method_type: conditional-detector-response
tags: [gamma-spectroscopy, bgo, anti-compton, timing, counting-statistics]
---

# BGO 反符合门与计数目标

## Purpose

对给定几何、阈值、prompt 时间响应和固定测量时长，比较门宽如何改变全能峰
接受率、连续底接受率与所选 ROI 的计数精度。此方法不由 BGO 闪烁衰减时间
直接预测时间分辨，也不由 γ 能量独自预测抑制效率。

## Source and Scope

[[li-2025-imp-dragon-hpge-array]] PDF 2 §2.1 报告指定构型、能窗和源条件下
的抑制性能；PDF 3 §2.3 报告电子学使用 400 ns 否决窗口。PDF 3 已核图像，
原文没有把这个门宽定义成本模型的 prompt 高斯 σ，也没有给出本模型的
完整相关否决概率。400 ns 是来源报告的设置，不能据此宣称所有阵列最佳门宽。

以下公式是本任务在明示假设下的概率重建，不是该论文报告的探测器响应拟合。
P/C、P/T、ROI S/B 是三个不同量；指定能窗的 P/C 不可代入全谱 P/T。

## Inputs and Assumptions

- W 为以零 prompt 均值为中心的**完整**门宽；高斯时间差标准差为 σ_t。
- c、p 分别为无限宽门下对连续底事件、全能峰事件的相关否决概率，
  必须由同一阈值、几何和事件选择下的标定或验证模拟提供。
- R 为相同触发条件下与候选 Ge 事件独立的随机 BGO 触发率。
- f 为否决前指定积分范围内的全能峰比例；S0、B0 是另行指定 ROI 的
  固定时长信号与背景计数，不能由 f 自动确定。

## Conditional Model

高斯 prompt 接受度为

\[
A(W)=\operatorname{erf}\!\left(\frac{W}{2\sqrt2\sigma_t}\right),
\qquad q(W)=e^{-RW}.
\]

计算 q 时 W 必须转成秒。两类接受度为

\[
a_P=(1-pA)q,\qquad a_C=(1-cA)q.
\]

随机否决作用于两类计数，不能只扣全能峰而不扣连续底。在独立、平稳泊松
假设下，随机无触发因子 q 在纯度比

\[
(P/T)'=\frac{f a_P}{f a_P+(1-f)a_C}
\]

中消去，却仍降低绝对计数。这解释了为什么同样的 P/T 改善不保证同样的
测量收益。若类别相关随机率、pile-up 或共同触发使独立性失败，需联合响应。

选定 ROI 后 S=S0 aP、B=B0 aC。代码可优化保留 S，或计数精度代理
Z=S/√(S+B)。后者假设背景估计额外方差可忽略，**不是发现显著性**。
背景来自侧窗/拟合、峰重叠或参数相关时应重新建立似然/方差目标。
两个目标可给出不同最佳门宽，边界点也必须参与比较。

## Coincidence Extension

两相同且独立的探测臂下，全能峰–全能峰计数接受度为 aP²，纯度为 ((P/T)')²。
绝对计数、纯度、Z² 增益不可混称同一个 FOM。共用屏蔽、串扰、级联相关与
随机符合会破坏简单乘积，实验阵列需探测器对的联合响应。

旧接口 `matrix_fom_enhancement` 仅为 `matrix_significance_gain_squared` 的
兼容别名，含义已改；分析代码应使用显式的接受度、计数和 `objective_value`。

## Python and Validation

```bash
python3 system/scripts/analysis/nuclear_analyzer.py bgoveto --json
python3 system/scripts/analysis/nuclear_analyzer.py bgoveto --prompt-sigma 20 --continuum-rejection 0.8 --peak-rejection 0 --rate 350 --signal-counts 1000 --background-counts 4000 --objective significance --json
```

这些默认数字及保留的历史阵列 preset 名均为**合成演示**；没有提供任何阵列的
实测最佳门宽。能量、闪烁衰减、阈值在当前模型中仅作元数据，不隐含标定变更。
`response_provenance` 是调用者标签，代码不验证其真实性。

独立测试检查零门/零率极限、全宽约定、两类共同随机存活、完全否决极限、
ROI S/B 依赖、矩阵计数、输入边界及内点/端点最优；测试仅验证条件模型。

## Limitations and Self-audit

P0 self-audit：撤回原稿以闪烁衰减和经验阈值指数生成响应、只对峰扣随机损失、
把任意平方比称为统计收益的做法。现有原文不足以把输入 σ_t、c、p 标为实测。
P1：取得真实 prompt 时间差分布、能量/几何相关响应与随机率，并核验非高斯尾、
类别响应和背景方差后，才能应用于实验设置。无 human-review 事件。

## What It Can Establish

给定上述响应、计数与独立性假设，可比较不同门宽的条件期望计数和所选代理目标，
并检验随机损失、纯度与统计收益是否在计算中被混用。

## What It Cannot Establish Alone

不能单独给出阵列实测最佳设置、完整运输/DAQ 响应、ROI 背景估计方差，
也不能认证发现显著性或目标核集体模式。

## Sources

- [[li-2025-imp-dragon-hpge-array]]，PDF 2–3，仅作配置、反康普顿与电子学设置背景。
- 本页条件概率和计数公式是明确假设下的任务推导，不把 σ_t、c、p 归为该论文测值。
