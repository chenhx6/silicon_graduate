---
type: research-note
title: "A130数字实现参考：统一记号、数据头与证据入口"
aliases: [A130 digital implementation reference]
created: 2026-11-13
updated: 2026-11-14
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "父对附录E和5.5实际原图与离散递推的增量核验"
promotion_target: ""
evidence_sources: [wu-hongyi-2020-general-purpose-digital-daq-thesis, wolff-1982-poisson-arrivals-see-time-averages]
tags: [A130, digital-daq, trapezoidal-filter, CFD, FIFO-buffer, live-time]
---

# 数字实现参考与统一入口

## Research Trigger

早期实现笔记把连续时间近似写成精确离散参数，且把死时间附录误作FIFO策略原件。这里保留关键记号与修正依据；完整递推、有限控制和读图结果集中在[[a130-rewrite-digital-appendix-consistency-20261113]]，避免维护两份不一致公式。

## Grounded Evidence

[[wu-hongyi-2020-general-purpose-digital-daq-thesis]]的143物理页授权版：PDF55/印43 Fig2.8支持该版本事件字域，PDF55–56/印43–44讨论标准固件和作者定制固件在波形缓存满时的不同保存策略。PDF127–128/印115–116讨论死时间模型，不能用于证明FIFO策略。原件路径与SHA回source；该图不证明未知新固件具有相同协议。

[[wolff-1982-poisson-arrivals-see-time-averages]]的PDF2–5/印223–226支持所述PASTA条件。到达前状态、参考测度及长期极限须一并说明，不能由独立单道活时间直接推出联合符合接受概率。

## Provisional Reasoning

对正文所用因果指数输入和组合梯形递推，精确记号是
\[
\alpha=e^{-T_s/\tau_d},\qquad
M=\frac{\alpha}{1-\alpha}=\frac{1}{\exp(T_s/\tau_d)-1}.
\]
$M\simeq\tau_d/T_s$只在小采样比下作领先近似，不应同时当成精确恒等式。单独极零补偿阶跃和组合梯形输出的残余尾形需要按各自传递函数分析。

定义估计时间减真实过零时间的误差，并在非零斜率、光滑局域曲线和小采样步长条件下，割线插值领先误差为
\[
\widehat t-t_0=-\frac{T_s^2}{2}\phi(1-\phi)
\frac{C''(t_0)}{C'(t_0)}+O(T_s^3).
\]
它是确定性插值误差；实际时间分辨还受噪声、参考通道和同步影响。不同CFD算子只有连同输入、延迟、比例因子及过零方向一起变换才可比较。

## Assumptions

上述公式仅对应正文声明的LTI递推、输入和误差符号。事件字域和缓存策略仅对应实际读过的固件版本；算法控制不等于FPGA或未知用户装置验证。

## Competing Explanations

能量或符合产额变化可以来自成形取幅、基线、堆积判弃、整事件丢失及软件门选。波形被省略与整事件未保存具有不同观测后果，需用事件头、计数器及相应参考过程辨别。

## Transfer Conditions

迁移至其它模块前需核具体字协议、ADC/FPGA实现、递推初值及真实时钟/门控。数学模型可复用，固件字段和实验性能不能按型号相似直接外推。

## Failure Conditions

用$M\simeq\tau_d/T_s$替代精确关系；把CFD编码步长称为真实分辨率；用错误附录页说明FIFO；把共同busy下两道接受度当独立；把未执行的控制写成通过。

## Falsification or Reverse Tests

已执行的五项有限控制、实际producer路径和数值结果回[[a130-rewrite-digital-appendix-consistency-20261113]]。本页不新增或虚报额外数值实验。

## Open Questions

真实固件的饱和、定点误差、holdoff与高水位阈值，只有取得对应实现或可验证测试时再作定量分析。

## Human Review

本次为Agent原件/公式自审，没有记录人工审核事件。

## Promotion or Rejection History

2026-11-14：撤回旧稿的精确参数、插值误差符号和FIFO定位错误；移除被字符串转义破坏的数学文本，合并到已核的统一数字附录入口。历史错误稿只留任务审计快照，不作事实来源。
