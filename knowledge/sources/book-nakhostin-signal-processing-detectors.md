---
type: source
title: "Mohammad Nakhostin (吴鸿毅译) 2020 - 辐射探测器信号处理"
aliases: [吴鸿毅辐射探测器信号处理, Nakhostin 2020 Signal Processing, 数字信号处理探测器]
created: 2026-11-01
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: skimmed
title_original: "Signal Processing for Radiation Detectors"
authors: [Mohammad Nakhostin, 吴鸿毅(译)]
publisher: "内部翻译交流版 / John Wiley & Sons 原版"
year: 2020
pages: "427"
canonical_source: "Mohammad Nakhostin 著, 吴鸿毅 译, 《辐射探测器信号处理》 (2020)"
library_file: "raw/books/翻译版-SignalProcessingforRadiationDetectors.pdf"
raw_file: "raw/books/翻译版-SignalProcessingforRadiationDetectors.pdf"
raw_sha256: "85e38c7aeb0121faed84cb0b2d8bb03e3e9c80e65dab84c8aad3893bc1399f99"
archive_required: true
raw_storage_status: archived-local
nuclei: []
reactions: []
experiments: []
models: [shockley-ramo-theorem, trapezoidal-filter, pole-zero-cancellation, digital-cfd]
topics: [digital-signal-processing, pulse-shaping, hpge-readout, baseline-restoration, pileup-rejection]
---

# Mohammad Nakhostin (吴鸿毅译) 2020 - 辐射探测器信号处理

> 阅读状态修订（2026-11-02）：撤回无逐页记录支持的整书 deep-read。下方旧概述不作为整章已读证据。本轮实际核查范围及需要修订的仪器表述见 [[reconciliation-of-detector-dead-time-and-pulse-pileup]]；仅对所列原件页取得局部阅读记录。


## 专著概况与定位

本书由英国萨里大学 Mohammad Nakhostin 撰写、北京大学在束核谱学与数字核电子学专家吴鸿毅博士翻译，是辐射探测器从传统模拟信号处理全面跨入**现代数字脉冲处理（Digital Pulse Processing, DPP）**领域的代表性专著。对于新一代数字化核物理实验系统（如 Pixie-16、CAEN 数字化仪等获取的在束波形），本书详尽推导了梯形滤波成形、数字极零相消、基线自适应跟踪与数字恒比定时（dCFD）的离散数学算法。

## 核心章节精要与物理内容

### 第 1 章：信号生成机制与 Shockley-Ramo 定理（pp. 11–70）
- **电荷感应机制**：指出探测器输出电流不是电荷到达电极时才产生，而是载流子（电子、空穴）在耗尽区漂移全程中由感应电位诱发的连续电流：
  $$i(t) = q \vec{v}(t) \cdot \vec{E}_w(\vec{r}(t))$$
  其中 $\vec{E}_w$ 为加权电场（Weighting field）。由于 HPGe 中空穴迁移率与电子迁移率不同，载流子产生位置导致电荷收集时间 $t_c$ 呈现 50–300 ns 的涨落。

### 第 4 章：能量测量与模拟/数字滤波成形（pp. 169–226）
- **极零相消（Pole-Zero Cancellation）**：前置放大器输出具有长指数衰减尾部（通常 $\tau_{\text{pre}} \approx 50\text{ }\mu\text{s}$）。若未经相消，高计数率下后续脉冲将骑在前脉冲尾巴上导致严重的基线移位与能量展宽。
- **弹道亏损（Ballistic Deficit）**：当成形滤波器的脉冲上升时间或平顶宽度小于探测器的电荷收集时间 $t_c$ 时，滤波器峰值幅度不能完全反映总感应电荷量，造成能量分辨率急剧恶化。

### 第 10 章：数字化辐射测量系统与离散滤波算法（pp. 375–420）
- **Jordanov 递归梯形滤波器（Trapezoidal Filter）**：
  对于以采样间隔 $T_s$ 离散采样的前放输出序列 $v[n]$，梯形滤波器由上升时间 $k$（步长）和平顶宽度 $m$（步长）定义。递归差分方程为：
  $$d^k[n] = v[n] - v[n-k] - v[n-k-m] + v[n-2k-m]$$
  结合前放衰减时间常数 $M = 1 / (e^{T_s/\tau_{\text{pre}}} - 1)$ 进行数字极零相消：
  $$p[n] = p[n-1] + d^k[n]$$
  $$s[n] = s[n-1] + p[n] + M \cdot d^k[n]$$
  该梯形滤波成形输出在平顶区间完全消除了电荷收集时间涨落造成的弹道亏损，同时极大压制了高频白噪声与低频 $1/f$ 噪声！
- **数字基线恢复（Moving Average Baseline Restoration）**：在无脉冲期间对采样点进行滑动平均，动态跟踪温度漂移引起的漏电流基线变化。
- **数字恒比定时（Digital CFD）**：将输入波形延迟 $D$ 个采样点并乘以衰减比例 $f$，与反向原始信号叠加，寻找严格的数字零点交叉，提取高精度时间标记。

## 对本 Wiki 研究的核心指导价值

1. **实验数据处理底层算法保障**：提供了编写自主 Python 波形处理与能谱分析工具的全部离散差分方程。
2. **实验设置参数调优**：为设置实验机数字化仪的上升时间（Rise time）和平顶时间（Flat top）提供严格准则（平顶必须大于最大电荷收集时间 $t_c$）。
