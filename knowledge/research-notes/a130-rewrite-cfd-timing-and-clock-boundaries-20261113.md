---
type: research-note
title: "A130数字定时研学：CFD算子映射、相位插值收敛与时钟协方差边界"
aliases: [A130 CFD timing and clock boundaries]
created: 2026-11-13
updated: 2026-11-13
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "第5章5.4节已核稿LaTeX迁移与数字定时模型追溯"
promotion_target: ""
evidence_sources: [wu-hongyi-2020-general-purpose-digital-daq-thesis, doctoral-r1-g32-lipschutz-2016-pixie16-ddas-timing, doctoral-r1-g32-hennig-2007-pixie16-multi-chassis-sync]
tags: [A130, digital-daq, CFD, timing-resolution, sampling-phase, covariance, lifetime-response]
---

# 算法零交叉、采样网格收敛与仪器寿命卷积的边界

## Research Trigger

在束 $\gamma$ 谱学和快符合实验中，时间标记用于判定相继信号是否属于同一次退激事件。
正文第 5.4 节初稿推导了恒比定时（CFD）与线性过零插值，但存在若干易混淆的边界：
把编码对应的名义时间步长当成物理时间分辨率、把离散 20 相位样本的最大误差当成连续全区间的全局上界、
忽略不同文献中延迟相减算子的符号与参数定义差异，以及混淆瞬发仪器响应函数 $R(t)$ 与核能级寿命 $\tau$。
本页归纳数字定时、同步抖动与寿命卷积的可复用物理方法与数据边界，防止模型结果被外推为通用硬件指标。

## Grounded Evidence

- [[wu-hongyi-2020-general-purpose-digital-daq-thesis]]：
  PDF 35–38（印刷 23–26）给出了前沿定时、幅度走动以及 CFD 算子式 (1.22) $x[n] - a x[n-k]$ 与图 1.27；
  PDF 104–109（印刷 92–97）记录了采样周期与脉冲前沿比值下的相位依赖测试。
- [[doctoral-r1-g32-lipschutz-2016-pixie16-ddas-timing]]：
  PDF 1–4 给出了 Pixie-16 模块上的 DDAS CFD 算法式 (2)–(6) 及优化参数；式 (3) 采用 $\mathrm{FF}[n] - w \mathrm{FF}[n-D]$，
  给出了四点三次多项式插值与 PMT 分路半采样周期延迟测试（$2\,\mathrm{ns}$ 延迟于 $4\,\mathrm{ns}$ 采样周期）。
- [[doctoral-r1-g32-hennig-2007-pixie16-multi-chassis-sync]]：
  PDF 1–4 第 3–4 节及图 3–5 讨论了 SeGA 系统多机箱同步方案，报告了同机箱 33 通道分路测试（相对参考通道分布 $\mathrm{FWHM} < 300\,\mathrm{ps}$）
  与示波器跨机箱时钟包络最坏偏差（约 $1.5\,\mathrm{ns}$）。

计算模型与数据路由：
- 任务规范模型脚本：`system/scripts/doctoral_g32_digital_pulse_response.py`（SHA-256: `bd70a7db208b62443a93c8258e18194e4d18f096a7e1160f2ed958fa0855e618`）
- 模拟收敛性产物：`outputs/l4/20261108-digital-pulse-response/sampling_convergence.csv`（SHA-256: `fcbc5a3ebf68e5ef8f0cb5dabfc1be09484d4f99757f9f2f9db6909225469222`）
  四行已核基线数据包含：
  - $T_s = 10.0\,\mathrm{ns}$：参考延迟 $t_{\mathrm{ref}} = 157.122270\,\mathrm{ns}$，20 相位点最大绝对误差 $0.256608\,\mathrm{ns}$；
  - $T_s = 5.0\,\mathrm{ns}$：参考延迟 $t_{\mathrm{ref}} = 159.653642\,\mathrm{ns}$，20 相位点最大绝对误差 $0.129692\,\mathrm{ns}$；
  - $T_s = 2.5\,\mathrm{ns}$：参考延迟 $t_{\mathrm{ref}} = 160.844638\,\mathrm{ns}$，20 相位点最大绝对误差 $0.013737\,\mathrm{ns}$；
  - $T_s = 1.25\,\mathrm{ns}$：参考延迟 $t_{\mathrm{ref}} = 161.471599\,\mathrm{ns}$，20 相位点最大绝对误差 $0.005997\,\mathrm{ns}$。

## Provisional Reasoning

### 1. CFD 算子定义、符号约定与跨文献映射

本任务模型采用的 CFD 序列定义为：
$$
C[n] = F[n-d] - f F[n], \quad (0 < f < 1).
$$
其选取的过零分支为主脉冲到达后的第一个上升穿越：$C[n] < 0 \le C[n+1]$，两点线性内插零点为：
$$
\widehat{t}_{\mathrm{zc}} = n T_s - \frac{C[n]}{C[n+1] - C[n]} T_s.
$$
文献中的实现形式与本式存在符号和参数映射差异：
- 吴鸿毅论文式 (1.22) 为 $Y_a[n] = F[n] - a F[n-d]$；
- Lipschutz 式 (3) 展开后为 $\mathrm{FF}[n] - w \mathrm{FF}[n-d]$。

将各式统一作用于相同快滤波输入 $F$ 时，有：
$$
Y_a[n] = F[n] - a F[n-d], \qquad C[n] = -f Y_{1/f}[n].
$$
要使过零点严格重合，必须满足 $a = 1/f$ 或 $w = 1/f$，并注意到整体负因子 $-f$ 反转了穿越方向（由下降穿越变为上升穿越）。
Lipschutz 实验优化所得参数为线性 $w = 5/8$、三次 $w = 1/8$；这些 $w < 1$ 的参数不是本模型 $f$ 的倒数（本模型 $f = 0.4 \implies 1/f = 2.5 > 1$）。
因此，不同硬件/固件方案的定时参数不能通过简单的字母对齐直接互换，必须依据各自算子定义独立校准定时点。

### 2. 幅度不变性成立的物理前提与局部噪声抖动

对于同形状、同到达相位的信号序列 $F[n] = A g[n]$（$A > 0$），由于差分与比例相减均为线性操作，$C[n] = A C_g[n]$。
在线性内插式中幅度因子 $A$ 在分子与分母中精确对消：
$$
\widehat{t}_{\mathrm{zc}} = n T_s - \frac{A C_g[n]}{A [C_g[n+1] - C_g[n]]} T_s = n T_s - \frac{C_g[n]}{C_g[n+1] - C_g[n]} T_s.
$$
幅度不变性成立的前提条件为：
1. 信号前沿在不同能量沉积下保持理想同形（无空间收集时间起伏与等离子体延迟畸变）；
2. 整个电子学链路完全在线性区工作，无放大饱和或截幅；
3. 无叠加噪声，且选中的离散样本跨度 $[n, n+1]$ 不随幅度改变。

在存在小随机噪声时，若无噪声波形在过零点 $t_\times$ 的时间斜率为 $\bar{C}'(t_\times) \ne 0$，引起的定时抖动可表示为：
$$
\sigma_t \simeq \frac{\sigma_C}{|\bar{C}'(t_\times)|},
$$
其中 $\sigma_C$ 为经过快滤波、延迟与相减操作后在过零附近的有效幅度噪声标准差，包含采样点自相关传播，不能直接用原始 ADC 采样单点噪声替代。

### 3. 采样相位依赖、插值收敛与 20 相位样本局限

脉冲到达时间相对 ADC 网格的相对相位为 $\phi = t_0 \bmod T_s \in [0, T_s)$。
因为连续 CFD 曲线在过零附近存在非零曲率，连接离散采样点的直线并不与真实曲线重合，产生依赖于相位的系统插值误差。
表 5.2 数据表明，减小 $T_s$ 能显著压制插值误差（由 $10\,\mathrm{ns}$ 下的约 $0.257\,\mathrm{ns}$ 下降至 $1.25\,\mathrm{ns}$ 下的约 $0.006\,\mathrm{ns}$）。

但必须记录以下方法学边界：
1. **样本离散性限制**：模拟表中的最大绝对误差仅覆盖等间距扫描的 20 个离散相位点（$\phi/T_s = 0, 0.05, \dots, 0.95$），它反映了算法在离散点集上的分散特征，不能作为全连续相位区间 $[0, T_s)$ 内解析意义上的严格数学上界；
2. **多项式插值的局限性**：高阶多项式插值（如 Lipschutz 四点三次多项式）仅约束 4 个采样节点上的函数值，节点之间的真实物理曲线仍不可知；高阶插值可能放大高频噪声或引入多根，需配套穿越方向与单调性校验。

### 4. 编码分度与物理时间分辨率的区别

设数字系统的时间戳粗计数周期为 $T_{\mathrm{tick}}$，内部采用 $b$ 位有效二进制细位作均匀分数内插，则时间戳的数字步长为：
$$
\delta t_{\mathrm{code}} = \frac{T_{\mathrm{tick}}}{2^b}.
$$
这是数字系统的字格式与编码量化单位（LSB）。
真实实验的时间分辨率由探测器电荷收集涨落、光电转换统计、电子学热噪声抖动、时钟漂移及有限采样插值误差综合决定。
仅在算法或字结构中增加存储位宽 $b$（例如将时间戳低位扩展至 16 位），只能减小数值舍入误差，绝对不会物理缩窄实测时间谱的 FWHM。

### 5. 阵列多通道同步、共同抖动与时钟协方差

多探测器符合测量测定的是相对时间差 $\Delta t = t_1 - t_2$。在两通道时间测量方差存在时，差值的方差满足：
$$
\mathrm{Var}(\Delta t) = \mathrm{Var}(t_1) + \mathrm{Var}(t_2) - 2\mathrm{Cov}(t_1, t_2).
$$
- 同一测试脉冲的分路测量可能保留共享噪声或漂移的相关项；若 $\mathrm{Cov}(t_1, t_2) > 0$，差值谱可以更窄，不能未经协方差检查便套用两路独立噪声的 $\sqrt{2}$ 换算；
- 独立高斯噪声通道下，若两路分辨相同，则 $\mathrm{FWHM}_{\Delta t} = \sqrt{2} \mathrm{FWHM}_t$；
- 跨机箱同步中示波器累积的时钟包络最坏偏差（如 Hennig 测得的约 $1.5\,\mathrm{ns}$）包含探头失真与非高斯系统偏移，属于包络极值，不能直接等同于统计标准差或高斯 FWHM。

### 6. 仪器瞬发响应与核能级衰变寿命卷积的区别

在慢符合或寿命提取中，测得的时间差谱 $S(t)$ 是核衰变等待时间分布与仪器响应函数的时间卷积：
$$
S(t) = A_{\mathrm{sig}} \int_0^\infty \frac{e^{-u/\tau}}{\tau} R(t - t_{\mathrm{off}} - u) \, \mathrm{d}u + B(t),
$$
其中：
- $\tau$ 为被测能级的真实平均寿命；
- $R(t)$ 为系统的瞬发时间响应函数（包含探测器输运、走动与电子学抖动，单位为 $\mathrm{s}^{-1}$，且 $\int R(t)\mathrm{d}t = 1$）；
- $t_{\mathrm{off}}$ 为通道间几何与电路延迟偏移；
- $B(t)$ 为偶然符合本底。

时间谱的展宽是由核寿命 $\tau$ 与仪器响应 $R(t)$ 共同贡献的：
- 仪器响应函数的 FWHM 反映的是电子学与探测器的瞬发定时分散度；
- 能级平均寿命 $\tau$ 反映的是原子核处于不稳定激发态的本征存活时间；
- 单一时间谱的 FWHM 与平均寿命 $\tau$ 没有通用相等关系，也不构成寿命能否提取的绝对下限；当系统响应 $R(t)$ 经过精确标定且统计量充足时，通过解卷积分析（Deconvolution）或重心位移法可测定远小于仪器 FWHM 的核寿命。

## Assumptions

- 脉冲波形由理想无噪声双指数模型给出，不计入探测器空间电离位置差异引起的电荷收集时间非均匀性；
- CFD 线性插值假定过零前后相邻两点近似处于局部线性区间；
- 寿命卷积公式假定能级为瞬时直接布居，忽略复杂的多级级联 feeding 过程。

## Competing Explanations

时间谱形状的非对称展宽与拖尾可能由以下竞争机制引起，不可武断归因于单一因素：
1. 原子核激发态存在有限的微观衰变寿命 $\tau$；
2. 探测器晶体内部深层与表层载流子漂移时间差异带来的电荷收集拖尾；
3. 未完全校准的脉冲幅度走动（Time Walk）；
4. 电子学时钟漂移、低频温漂或多机箱同步相位晃动；
5. 随机偶然符合与连续 $\gamma$ 本底。

## Transfer Conditions

- 规范方法与参数映射用于正文第 5.4 节（`Tex/Sections/sec-5-4.tex`）以及后续第 5.5 节数据获取系统活时间分析；
- 寿命卷积表达式与物理量定义作为第 5.8 节与第 5.10 节在束寿命谱学测量的理论模型基础；
- 与前置知识页 [[a130-rewrite-digital-pulse-gain-and-data-boundaries-20261108]] 形成快慢通道双滤波方法学闭环。

## Failure Conditions

把编码名义步长直接当成物理时间分辨、把离散 20 相位点最大误差外推为连续全局界、
无条件沿用同源分路正协方差套算独立通道差谱、在脉冲非同形或饱和时套用线性幅度不变性，
或在存在显著级联 feeding 时将时间差谱直接当单指数寿命处理，均会导致推论失效。

## Falsification or Reverse Tests

已核对 `outputs/l4/20261108-digital-pulse-response/sampling_convergence.csv` 与既有 producer 脚本 `system/scripts/doctoral_g32_digital_pulse_response.py` 的数据一致性，完成算子符号、跨文献映射与量纲核查。
本次纠正属于模型边界审计与文献符号对齐，未做新的全连续相位数值积分，未跑新蒙特卡罗模拟，亦未做新的硬件探测器时间分辨测量。
正文第 5.4 节修订仍须以相应 LaTeX 台账与正文逐行核验，不以本页建立自动等同于实验通过。

## Open Questions

实际阵列多通道时钟相对漂移的真实协方差矩阵、复杂退激级联的真实 feeding 时间分布、
探测器电离位置涨落引入的波形形变以及在线固件触发判弃逻辑的综合活时间损失，仍依赖具体的实验装置与实测标定数据。

## Human Review

本页由 G79 及总控在 LaTeX 迁移与科学审计中完成代数、符号与数据边界自审，无新增用户人工审核记录。

## Promotion or Rejection History

- 2026-11-13：伴随第 5 章 5.4 节已核稿迁移建立本页，撤回将编码名义步长等同于物理时间分辨、将 20 离散相位极值当成全区间全局上界、以及将分路测试正协方差普适化为所有独立阵列特征的断言。
