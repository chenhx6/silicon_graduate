---
type: method
title: "吴治华实验方法选段：死时间、HPGe 能谱与 RDM/DSAM 输入契约"
aliases: [Wu experimental methods contract, deadtime HPGe RDM DSAM, 吴治华实验接口]
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
method_type: "experimental-nuclear-spectroscopy"
scope: "Bounded page-level audit of Wu Ch. 1, 5, 10 and 15"
confidence: "high for the listed scanned-page formulas and workflow boundaries"
tags: [wu-experiment-methods, dead-time, hpge, gamma-spectroscopy, efficiency, rdm, dsam]
sources: [book-wu-nuclear-experiment-methods, book-wang-particle-detection, book-nakhostin-signal-processing-detectors]
---

# 吴治华实验方法选段：死时间、HPGe 能谱与 RDM/DSAM 输入契约

## Purpose

把吴治华《原子核物理实验方法》第三版中直接服务于实验核谱学的数据处理内容，
整理为后续 Python 分析的输入和边界契约：

```text
真实事件率 -> 死时间/堆积校正 -> HPGe 能量与效率
    -> γ-γ 符合矩阵与本底扣除
    -> RDM/DSAM 寿命 -> B(E2)、Qt 与形变
```

## Inputs and Assumptions

- 明确输入率和记录率的符号，不把不同教材的 \(m,n\) 约定混用；
- 死时间公式首先是平稳泊松单通道近似，多道 ADC、缓冲、幅度相关转换时间需要额外标定；
- HPGe 能量刻度和效率刻度必须分别拟合，峰位、峰面积、分辨率和几何效率不能混成一个参数；
- 二维符合本底扣除要记录峰门、左右本底门、门宽和协方差；
- RDM 和 DSAM 的寿命输出依赖反冲速度、阻止本领、侧馈、峰面积/线形和探测器响应。

## Definition

### 死时间

以下采用“\(m\) 为真实输入率、\(n\) 为记录率”的约定：

- 不可扩展型/非麻痹型：
  \[
  n=\frac{m}{1+m\tau_N};
  \]
- 可扩展型/麻痹型：
  \[
  n=m e^{-m\tau_P}.
  \]

可扩展型在 \(m=1/\tau_P\) 处达到
\[
n_m_m_{\max}=\frac{1}{e\tau_P}.
\]
当观测率低于该极大值时，逆问题可能有两个真实输入率根；改变束流通量或
使用独立 pulser/活时间记录才能消除二义性。

### HPGe 能谱接口

能量刻度应使用参考峰拟合
\[
E=a_0+a_1x+a_2x^2+\cdots,
\]
并独立记录峰宽随能量的参数化。效率刻度则是另一条函数
\(\varepsilon_{\mathrm{FE}}(E_\gamma)\)，需要说明源几何、晶体距离、级联相加、
死层吸收和内转换分支。

### RDM 与 DSAM

RDM/Plunger 通过改变靶—阻挡箔距离 \(d\)，利用未移位/移位峰面积变化获得寿命，
主要覆盖约 ps 到 ns 区间。DSAM 利用反冲核在衬底中的连续减速和多普勒位移，
主要覆盖 fs 到 ps 区间；它需要 stopping power、散射角、侧馈和角度响应。

## Discriminating Observables

| 环节 | 必须保存的量 | 失败模式 |
|---|---|---|
| 死时间 | 输入/记录率、\(\tau\)、模型类型、双根状态 | 把高率饱和支当作唯一输入率 |
| 能量刻度 | 峰中心、参考线、残差、FWHM | 用效率曲线替代能量刻度 |
| 效率 | 全能峰效率、总效率、几何距离、相加修正 | 未校正级联相加就比较分支 |
| 符合谱 | 峰门、左右本底门、门宽、协方差 | 负本底或门宽比例错误 |
| RDM | \(d\)、反冲速度、移位/未移位面积、侧馈 | 用单指数替代多级联/侧馈 |
| DSAM | \(F(\tau)\)、停止截面、散射角、线形、侧馈 | 把阻止模型误差写成形变演化 |

## Evidence Matrix

| Wu 页面 | 已核对内容 | Wiki 接口 |
|---|---|---|
| PDF pp. 30–33 / printed pp. 22–25 | 事件间隔、非麻痹/麻痹死时间、双根曲线 | `detector_deadtime_pileup_correction_calculator.py` |
| PDF p. 152 / printed p. 144 | 半导体探测器与辐射损伤章节入口 | HPGe 电荷收集/缺陷边界 |
| PDF p. 265 / printed p. 257 | 能量刻度和 \(\gamma\) 强度测量章节入口 | 峰拟合、能量/效率分离 |
| PDF p. 273 / printed p. 265 | 探测效率、谱线响应和探测器比较 | HPGe efficiency/covariance |
| PDF p. 283 / printed p. 275 | BGO/能谱测量段 | Compton suppression 与加和边界 |
| PDF p. 430 / printed p. 422 | 核寿命测量章节、直接测量与短寿命方法 | RDM/DSAM 方法选择 |

## What It Can Establish

这张契约可以建立：

- 死时间模型选择和计数率反演的数学边界；
- HPGe 能量、分辨率、全能峰效率和几何响应的分层输入；
- γ-γ 门控本底扣除所需的门宽和归一化信息；
- RDM/DSAM 的寿命量级、响应模型和侧馈输入要求；
- 从寿命到 \(B(E2)\)、\(Q_t\) 的实验分析链条。

## What It Cannot Establish Alone

它不能单独给出真实阵列的效率、BGO 抑制比、阻止本领、侧馈时间或某个核素的
寿命结果；也不能把理想公式当作实测响应。具体实验必须保留原始谱、校准源、
门条件、响应函数和协方差。

## Supporting Evidence

- 吴治华第三版第 1 章 §1.5：PDF pp. 30–33 / printed pp. 22–25；
- 第 5 章半导体探测器：PDF pp. 152–156 / printed pp. 144–148；
- 第 10 章 \(\gamma\) 强度、能量与效率：PDF pp. 265–303 / printed pp. 257–295；
- 第 15 章核寿命测量：PDF pp. 429–460 / printed pp. 421–452；
- 以上页码均来自本地扫描原件，关键页面已渲染核对。

## Counter-evidence

- 不可扩展/可扩展死时间是理想单通道模型，多道数据采集系统可能需要级联或排队模型；
- BGO 抑制和全能峰效率随能量、几何和阈值变化，不能使用一个全局常数；
- RDM 的指数关系会被侧馈、阻挡箔厚度和反冲速度分布改变；
- DSAM 的 stopping power、散射角和侧馈模型可能在 \(Q_t\) 自旋系统学中产生相关偏差。

## Model Dependence

Wu 的公式提供实验流程骨架；现代分析还需要数字波形、Geant4/响应模拟、ZBL/LSS
阻止本领、联合峰拟合和完整误差传播。代码输出必须标识模型类型和未建模响应。

## Limitations and Missing Evidence

本页只覆盖四个选段，未完成 Wu 第 2、3、11–14 章的完整阅读。当前仍缺少具体
实验阵列的晶体几何、效率协方差、真实死时间记录、RDM/DSAM 原始谱和侧馈网络，
因此不能由本页生成核素级寿命或形变结论。

## Sources

- [[book-wu-nuclear-experiment-methods]]
- [[reconciliation-of-detector-dead-time-and-pulse-pileup]]
- [[in-beam-coincidence-matrix-and-level-scheme-construction]]
- [[dsam-doppler-shift-attenuation-and-picosecond-lifetime-inversion]]
