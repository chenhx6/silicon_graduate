---
type: research-note
title: "A130数字成形研学：增益、协方差、门宽和模拟表的可追溯性"
aliases: [A130 digital pulse gain and data boundaries]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "冻结G68-v1与总控逐行核canonical producer和CSV"
promotion_target: ""
evidence_sources: [wu-hongyi-2020-general-purpose-digital-daq-thesis, wu-2021-general-purpose-digital-daq-waveform-analysis]
tags: [A130, digital-daq, trapezoid-filter, covariance, reproducibility]
---

# 公式、参数和真实产物必须来自同一条计算链

## Research Trigger

5.3初稿递推与z变换大体正确，却把模拟表中大部分点换成了不符原CSV的数值。
不能以两个已核锚点正确、声称“规范模拟”或格式验证通过认证整张表。
本页保存可复用的量纲、统计和数值边界，旧冻结稿不是科学事实源。

## Grounded Evidence

[[doctoral-r1-g32-digital-daq-observable-chain-20261108]]已绑定吴论文
PDF31–32/印刷19–20的递推、符号歧义及总控算法重建。
本次没有把任务模型冒充吴的固件/实测，也未新增通用硬件性能范围。
原件身份见上述两篇source，属于相关研究谱系而非两个独立探测实验。

数字模型producer为
[`doctoral_g32_digital_pulse_response.py`](../../system/scripts/doctoral_g32_digital_pulse_response.py)，
实际输出为`outputs/l4/20261108-digital-pulse-response/ballistic_deficit_study.csv`，
其既有run-provenance保存输入、版本与产物哈希。
本轮总控直接核CSV选定行及producer的取最大值规则，没有重做用户硬件校准。

## Provisional Reasoning

### 1. 本递推的增益不能靠连续近似替代

在已声明的四延迟差分、双累加、\(M=(e^{T_s/\tau_d}-1)^{-1}\)与零历史下，
理想指数输入的平顶为 \(Ak(M+1)\)。按此算法恢复A须除以k(M+1)。
错除kM的相对增益偏置为

$$
\frac{M+1}{M}-1=e^{T_s/\tau_d}-1.
$$

小参数10⁻⁴给约0.01%，不是0.02%；本模型10ns/50μs=2×10⁻⁴才给约0.0200%。
即使误差较小，也不能混用参数与百分数；实际能量校准还可能吸收共同增益，
不由该算术直接推出现有谱线已偏移多少。

### 2. 数据选取与表内圆整

输入为无噪声双指数 \(A(1-e^{-t/\tau_r})e^{-t/\tau_d}\)，A=1000任意幅度单位、
Tₛ=10ns、τd=50000ns、arrival=500ns、k=200，ℓ分别200/210/240。
幅度估计取所生成离散输出的最大值；亏损为100×(1000−amplitude)/1000。
τr不是严格有限的最长电荷收集时间。选定行按既有CSV给：

| τr/ns | 平顶0ns亏损/% | 平顶100ns亏损/% | 平顶400ns亏损/% |
|---|---:|---:|---:|
| 20 | 0.7144 | 0.0560 | 0.0508 |
| 60 | 2.1990 | 0.6455 | 0.1336 |
| 100 | 3.6594 | 1.7643 | 0.2958 |
| 140 | 5.1099 | 3.0538 | 0.6718 |
| 180 | 6.5583 | 4.4123 | 1.2791 |
| 220 | 8.0030 | 5.7955 | 2.0735 |
| 300 | 10.8680 | 8.5933 | 4.0447 |
| 400 | 14.3807 | 12.0648 | 6.8916 |

100ns列由CSV幅度字段算出，0/400ns列与其亏损字段交叉核对。
正文可按目的减少行数或圆整，不能插值/猜填后仍称原表。
给定模型和取幅下平顶缓解且保留残差，不是所有输入、归一与算法永不能消除亏损的定理。

### 3. 量纲和协方差是公式的一部分

若加权势定义为无量纲，负梯度的加权场维数为长度倒数；
在采用相应符号约定的 \(i=q\,v\cdot E_w\) 中才得到电流维数。
这是量纲检查，不声称本轮精读了Ramo–Shockley历史原作。

基线N点平均只有在采样噪声独立、同方差时才有Var(mean)=σ²/N。
一般式为 \(N^{-2}\sum_{ij}\mathrm{Cov}(v_i,v_j)\)。
对已映射到相同幅度单位的能量估计S与基线B，

$$
\mathrm{Var}(S-B)=\mathrm{Var}(S)+\mathrm{Var}(B)-2\mathrm{Cov}(S,B).
$$

数字滤波、共同样本和共同增益都可能带来相关性；
不能无声明把方差相加或把基线ADC单位直接加到能量平方。

### 4. 时间窗和固件逻辑也需要条件

理想Poisson到达、固定窗T内至少一后到事件的概率为1−exp(−RT)，
仅RT≪1才近似RT。这个概率也不自动等于实际被否决的事件比例。
PUR窗是否等于(k+ℓ)Tₛ及判弃哪一个事件，取决于实现；
缓存、共同busy和多重触发不能由单一成形窗代替。
PZC残差会如何影响后续取幅，还取决于基线估计与减除，
不从某一波形下冲单独推出所有软件实现同方向能量偏差。

## Assumptions

数字表只为声明模型，无噪声、无真实波形、无固件量化/饱和或实验效率输入。
实际Cf/Rf、Fano因子、场强和采样率需要对应原件/硬件，不凭经验补“典型”范围。

## Competing Explanations

峰位、拖尾和弱线计数可受响应、阈值、堆积或核衰变影响；
读到算法机制不证明用户数据已经存在任何一种缺陷。

## Transfer Conditions

迁移的是输入/算法/取幅/归一/接受度合同。
吴论文末项n[...]保留为符号歧义与任务重建；未核作者勘误时不武断归因为排版错误。

## Failure Conditions

只核两锚点却扩成未经计算的表、量纲不同却直接合并方差、
把小窗概率当任意计数率线性定理或把任务模型当固件实测，均破坏推论。

## Falsification or Reverse Tests

以producer、原CSV和run-provenance逐项回放。
当前纠正是数值转录/量纲审计，不将它计作新的探测器实验或新算法发现。
5.3修订稿仍需逐行检查其表、文字与台账，不由本知识页自动认可。

## Open Questions

真实响应与联合接受度仍需用户相应实验数据；本任务不虚构输入补齐。

## Human Review

总控数据与代数核查，没有新增人工审核记录。

## Promotion or Rejection History

- 2026-11-08：撤回与canonical CSV不符的G68表，固定同一计算链和统计条件。
