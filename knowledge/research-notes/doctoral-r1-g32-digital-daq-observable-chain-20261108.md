---
type: research-note
title: "吴鸿毅论文起点：数字滤波、定时与核观测量的响应链"
aliases: [G32 digital DAQ observable chain]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [wu-hongyi-2020-general-purpose-digital-daq-thesis, wu-2021-general-purpose-digital-daq-waveform-analysis, doctoral-r1-g32-lipschutz-2016-pixie16-ddas-timing, doctoral-r1-g32-hennig-2007-pixie16-multi-chassis-sync]
created_from: "G32原件研学；总控核吴论文原页并重建数值验证"
promotion_target: ""
tags: [digital-daq, trapezoid-filter, cfd, detector-response, doctoral-foundations]
---

# 从脉冲到能级：电子学怎样进入核结构结论

## Research Trigger

实验技术不能只列HPGe、ADC和FPGA的名字。
需要解释脉冲怎样变成能量和时间、何时事件被保留，以及这些选择怎样影响分支、符合、寿命和角关联。
本页是研究准备，不是论文技术章节；吴论文的装置参数不代表用户个人实验设置。

## Grounded Evidence

| Evidence | source / locator | provenance | limitation |
|---|---|---|---|
| MWD与递归梯形滤波、指数尾校正参数M | [[wu-hongyi-2020-general-purpose-digital-daq-thesis]]，PDF31–32/printed19–20，Eqs1.11–1.18、Figs1.19–1.21 | 总控回读并视觉核PDF32 | 原书对前人算法的叙述；本文程序不是作者固件 |
| 两点插值时间公式与噪声/基线依赖 | 同论文PDF36/printed24 Eq1.21与Fig1.26 | 原文方法 | 无通用最佳阈值/分数，CFD符号随实现定义 |
| 两系统1408keV源测试分辨约.17%，BGO VETO宽300ns | 同论文PDF85–86/printed73–74，Figs3.4–3.5 | 该论文实际设置与测试 | 不给其它系统通用性能；分辨相近不等于事件选择相同 |
| 周期分路输入测试中，100M-14bit一通道约80k/s，全开各通道约20k/s | 同论文PDF111–112/printed99–100 Fig3.46 | 实测吞吐，作者归因旧DSP架构 | 周期同源输入不是Poisson死时间实验，更不是当前全部Pixie模块指标 |
| 相位/插值行为依算法与上升时间 | 同论文PDF106/printed94 Figs3.35–36及讨论 | 作者特定模拟/测试 | 5个采样周期只是该讨论的经验尺度，不能作为普适分界 |
| 本任务理想脉冲、PZC和CFD重放 | `system/scripts/doctoral_g32_digital_pulse_response.py`及相应L4 provenance | 总控重建的模型验证 | 无真实波形、噪声、效率/死时间校准或核寿命拟合 |

吴论文实际143物理页，SHA `925521da71f14eab642aa1dc55ad6c7cc639c4e1a27bb85227786469c5f8949b`。
G32的广泛读取范围与总控上述独立核查分开；2021论文为成果相关来源，不能另计重复实验。
该期刊报告沿用[[wu-2021-general-purpose-digital-daq-waveform-analysis]]的canonical页。
[[doctoral-r1-g32-lipschutz-2016-pixie16-ddas-timing]]把固定延迟分路的电子学测试
与不同LENDA棒的随机到达响应分开；
[[doctoral-r1-g32-hennig-2007-pixie16-multi-chassis-sync]]又区分机箱内波形相对FWHM
与跨机箱示波器时钟包络变化。它们支持方法比较，不能合并成一个通用RMS指标。

## Provisional Reasoning

### 1. 递推式怎样处理指数尾

以输入v[n]、样本索引n、样本周期T_s为约定，采用零初始历史，
\[
d[n]=v[n]-v[n-k]-v[n-\ell]+v[n-k-\ell],\quad
p[n]=p[n-1]+d[n],
\]
\[
r[n]=p[n]+Md[n],\quad s[n]=s[n-1]+r[n],\quad
M=(e^{T_s/\tau_d}-1)^{-1}.
\]
k、ℓ为样本数，ℓ≥k；理想梯形上升kT_s、平顶约(ℓ−k)T_s。
**原文边界：** 吴论文Eq1.14/1.19末项字面印为n[n−k−ℓ]；
此处按四延迟差分的线性时不变结构重建为v，不把校正后的式子伪称逐字原文。

任务推导：对理想\(v[n]=A\alpha^n\)，\(\alpha=e^{-T_s/\tau_d}=M/(M+1)\)，
递推传递函数中的\((M+1)-Mz^{-1}\)消去指数极点，
输出是两个长度k、ℓ矩形序列卷积乘A(M+1)。
故理想平顶高度为\(Ak(M+1)\)，本任务归一应除\(k(M+1)\)，而非旧程序的kM。
这项增益控制已用独立矩形卷积核对，最大误差约2.4×10⁻¹²任意幅度单位。
它是算法控制，不是测得真实电荷量。

### 2. 平顶为什么有用，又为什么不是绝对定理

有限收集过程会让响应依脉冲上升沿变化，延长平顶可降低取幅敏感性，
但需要具体电流形状、PZC、取样位置与归一；不成立“G≥某tc就当且仅当零亏损”的普适命题。
本任务输入\(A(1-e^{-t/\tau_r})e^{-t/\tau_d}\)为无噪声双指数，
τ_r是模型形状参数，并非严格有限的最长电荷收集时间。
τ_r=220ns时，模型零平顶的幅度亏损约8.00%，400ns平顶约2.07%。
有剩余偏差正是该模型的结果，不可称完全消除。

### 3. CFD无幅游走的条件及数字插值

在本任务约定下\(C[n]=F[n-d]-fF[n]\)，F为快滤波，d为延迟样本数、f为分数。
两点过零插值为
\[
t_{zc}=t_n-C_nT_s/(C_{n+1}-C_n).
\]
同形状、无线性饱和、无噪声的正幅度缩放会让C整体缩放，过零点不变。
真实时间游走可以来自形状、阈值、噪声、基线、饱和、采样/插值等，
不能断言低能事件必有一个固定方向或固定幂律游走。

事件相对本地采样网格的相位，与两个模块时钟的相对偏差/抖动是不同变量。
本任务扫描事件相位，用相同解析脉冲及同一有限延迟/求和算符求连续过零参考，
再与采样线性插值比较，撤回旧程序没有推导来源的657.2238ns硬编码。
T_s从10ns减到1.25ns时，所采相位点的最大插值误差从.2566ns降到.0060ns。
固定形状幅度扫描的时间戳展宽为数值0；该控制不模拟真实噪声或声称实验可达该分辨。

### 4. 多级选择如何传到物理量

源强度N_γ经探测器响应、触发、反康、堆积/忙和离线符合窗后才形成计数。
若效率依E、角度、计数率和另一通道状态，简单除一条单能效率曲线不一定足够。
窄时间窗还可能对不同能量/通道的prompt峰接收不同部分，影响分支或DCO。
寿命分析同时依赖能量相关时间响应、feeding、背景及拟合模型。

一个校准思路是联合扫描门宽、回放时间—能量响应并以独立源/脉冲监测触发和live。
但宽窗平台也可能受随机符合/背景影响，不能看见平台就认定唯一是时间游走。
反向校准能限制仪器解释，仍需检查ICC、态身份、feeding和核矩阵元模型。

理想Poisson瘫痪模型\(R_{out}=R_{in}e^{-R_{in}\tau}\)只是一个模型；
多通道公共busy、FIFO/DSP吞吐和相关事件不自动满足它。
两通道live校正只有在独立时才可分解成η_iη_j；一般需要联合η_ij。
电子学改进提高多少核事件，必须用实际数据，而非虚构固定效率倍数。

## Assumptions

- 模型所有幅度任意、时间ns，无随机噪声、无真实硬件固件/校准输入。
- PZC和CFD定义始终一致；不同原文可能采用等价的符号/延迟约定。
- ADC量化误差Δ²/12需均匀误差假设；不把它当所有脉冲的精确噪声。
- 用户的ADC位数/采样率、固件、滤波、阈值、时钟、记录模式及live均未在本任务获得。

## Competing Explanations

弱线可能来自小矩阵元、ICC、feeding/态指定，也可能来自阈值/符合选择。
宽时间尾既可能是寿命，也可能是响应、背景或堆积。
这些必须在同一响应/误差合同中比较；不能先把异常全归电子学或全归新核模式。

## Transfer Conditions

在不同阵列/核区迁移的是标定与前向响应方法，不是吴论文的300ns门或80k/s指标。
需保存实际探头/模块型号、固件版本、采样/滤波单位、参数文件、源刻度、live与触发拓扑。
相关实测输入没有取得前，不生成用户实验机时、事件产额或多极性阈值。

## Failure Conditions

波形饱和、基线漂移、取样/滤波索引不一致、公共忙被误当独立、
硬编码“真实时间”或先验假定零死时间，会使相应校准或toy演示失效。
没有联合响应时，不能从相对计数损失唯一归因矩阵元变化。

## Falsification or Reverse Tests

脚本实际7项控制通过：理想指数与独立卷积、增益、幅度不变性、整样本平移、
解析参考根残差、采样加密、平顶缓解但保留残差。
CSV使用LF，provenance有实际UTC、代码/输出哈希与库版本。
真实实验另需源/脉冲输入、能量/计数率扫描、随机符合和联合live检查；toy不代替这些。

## Open Questions

- **idea：** 某条弱带间线对门宽/时间校正的变化，能否区分仪器接收与核衰变强度？
  assumption为有原始时间戳和触发效率；竞争解释为随机符合、feeding与ICC。
  预测须由实际响应模型产生，不设固定低能阈值或任意效应百分比。
  若联合校准后仪器解释不足，再比较核模型，不把剩余偏差自动称新机制。
- **idea：** 多通道公共busy相关是否影响角度组的符合归一？
  先实测η_ij与η_iη_j差异，再预测DCO/分支变化；
  竞争解释为几何效率、取向和背景。无实际相关损失则结束该路线。
- 尚未取得用户数据/硬件配置；这些是候选研究合同，不是已发现的实验问题。

## Human Review

- Review scope: G32研学、总控回原页与独立算法重建；无用户逐项审核。
- Decision: provisional，来源事实与本任务模型分开。
- Complete unresolved P0/P1 inventory: 代码硬编码参考/虚构时间已修；P1为真实用户响应、
  联合live与原始波形未取得，不自动成为用户待办。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-11-08 | 总控核原页并重放 | worker draft | provisional | 撤回平顶iff、通用游走/死时间阈值，纠正PZC增益并用解析根代硬编码 | doctoral-nuclear-structure-foundations |
