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
authors: [Mohammad Nakhostin, "吴鸿毅 (译)"]
publisher: "John Wiley & Sons 原版 / 北京大学技术物理系吴鸿毅翻译"
year: 2020
pages: "427"
isbn: "978-1-119-02604-4"
canonical_source: "M. Nakhostin, Signal Processing for Radiation Detectors, Wiley (2017); 吴鸿毅 译 (2020)"
raw_storage_status: archived-local
archive_required: true
library_file: "raw/books/翻译版-SignalProcessingforRadiationDetectors.pdf"
raw_file: "raw/books/翻译版-SignalProcessingforRadiationDetectors.pdf"
raw_sha256: "85e38c7aeb0121faed84cb0b2d8bb03e3e9c80e65dab84c8aad3893bc1399f99"
nuclei: []
reactions: []
experiments: []
models: [shockley-ramo-theorem, trapezoidal-filter, pole-zero-cancellation, digital-cfd]
tags: [books, digital-signal-processing, pulse-shaping, hpge-readout, baseline-restoration, pileup-rejection]
---

# Mohammad Nakhostin (吴鸿毅译) 2020 - 辐射探测器信号处理

## Bibliographic Record

- **书名**：辐射探测器信号处理（Signal Processing for Radiation Detectors）
- **原著**：Mohammad Nakhostin（英国萨里大学）
- **主译**：吴鸿毅（北京大学核物理与核技术国家重点实验室）
- **原版出版**：John Wiley & Sons, Inc., 2017 年 10 月第 1 版，ISBN 978-1-119-02604-4。
- **中文译本**：2020 年在北京大学用于核谱学教学与前沿核实验数据采集处理培训。
- **全书规模**：427 物理 PDF 页（译本与原版各章页码保持完全对应）。
- **本地原件**：`raw/books/翻译版-SignalProcessingforRadiationDetectors.pdf`
- **原件 SHA-256**：`85e38c7aeb0121faed84cb0b2d8bb03e3e9c80e65dab84c8aad3893bc1399f99`

## Scope and Reading Depth

本来源登记状态定为 `skimmed`，明确界定本轮针对数字脉冲成形、Shockley-Ramo 定理、弹道亏损与极零相消的重点查验范围：
- **已核查章节**：
  - 封面、译者序与目录（PDF pp. 1–10）；
  - 第 1 章 信号生成机制（印刷 pp. 11–70 / PDF pp. 11–70）：Shockley-Ramo 定理、加权场 $E_w$ 与电子/空穴漂移感应电流；
  - 第 4 章 能量测量与脉冲成形（印刷 pp. 169–226 / PDF pp. 169–226）：CR-(RC)$^n$ 模拟滤波器、弹道亏损机制、梯形滤波平顶与死时间/堆积机制；
  - 第 10 章 数字化辐射测量系统（印刷 pp. 375–420 / PDF pp. 375–420）：Jordanov 递归离散差分梯形算法、移动平均基线恢复与数字恒比定时。
- **未核查内容**：第 2–3 章前置放大器晶体管电路、第 5–9 章时间测量与位置敏感探测器电路细节。

## Summary

本书是全面论述辐射探测器信号处理与现代数字脉冲处理（Digital Pulse Processing, DPP）的权威专著。全书从微观电荷感应物理出发，推导了前置放大器输出波形特征、极零相消（PZC）、滤波成形噪声最优化，以及基于 FPGA 的梯形滤波算法与基线跟踪技术。在在束实验数据采集与离线分析中，本书为消除弹道亏损、编写梯形滤波程序及数字恒比定时算法提供了直接的数学物理依据。

## Key Results

| ID | 陈述与物理内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| NAK-1 | Shockley-Ramo 电荷感应定理：输出瞬态电流为 $i(t) = q \vec{v}(t) \cdot \vec{E}_w(\vec{r}(t))$，其中加权电场 $\vec{E}_w$ 仅取决于电极几何与无电荷条件下的边界电位；载流子在耗尽区漂移全程持续产生感应信号，总电荷 $Q = \int i(t)dt$。 | model-result | direct | 第 1 章 §1.2, 印刷 pp. 15–22 / PDF pp. 15–22, 式 (1.4) | false |
| NAK-2 | 极零相消（Pole-Zero Cancellation）：前置放大器长衰减时间常数 $\tau_{\text{pre}}$（典型 $50\ \mu\text{s}$）在微分成形时产生低能下冲拖尾；通过引入补偿电阻零点 $R_{pz} C_{diff} = \tau_{\text{pre}}$，使传递函数中的前放极点与成形零点精确抵消，彻底消除高计数率下的基线位移与峰展宽。 | method/formalism | direct | 第 4 章 §4.2, 印刷 pp. 175–182 / PDF pp. 175–182, 图 4.6 | false |
| NAK-3 | 弹道亏损（Ballistic Deficit）与平顶成形：当模拟滤波器的达峰时间短于载流子漂移收集时间（$t_c \sim 100-300\text{ ns}$）时，峰值幅度因电荷收集未完全而发生损失；引入梯形滤波器的平顶（Flat Top $FT \ge t_c^{\max}$）可使电荷收集时间涨落下的信号幅度保持不变，彻底根除弹道亏损。 | model-result | direct | 第 4 章 §4.3, 印刷 pp. 185–194 / PDF pp. 185–194, 图 4.22 | false |
| NAK-4 | Jordanov 离散递归梯形滤波算法：输入离散采样序列 $v[n]$，梯形上升步长 $k$、平顶步长 $m$，数字极零补偿因子 $M = 1 / (e^{T_s/\tau_{\text{pre}}} - 1)$，通过双级有限差分递归方程 $s[n] = s[n-1] + p[n] + M d^k[n]$ 实现零乘法开销的快速实时成形。 | method/formalism | direct | 第 10 章 §10.2, 印刷 pp. 380–388 / PDF pp. 380–388, 式 (10.12)–(10.16) | false |
| NAK-5 | 数字化脉冲形状鉴别（PSD）与双门电荷比较法（CCM）：利用闪烁体单重态快成分（$\sim 3.2\text{ ns}$）与三重态慢成分（$\sim 270\text{ ns}$）电荷比值区分快中子与 $\gamma$ 射线；推导短门最佳积分时间 $T_{\text{short}} \approx 15 - 20\text{ ns}$，并建立光电子泊松涨落下分离优值因子 $\text{FOM}(E) = \text{FOM}_0 \sqrt{E / E_0}$ 的能量依赖模型。 | method/formalism | direct | 第 4 章 §4.5, 印刷 pp. 205–218 / PDF pp. 205–218 | false |
| NAK-6 | 数字化移动窗口反褶积（MWD）与自适应基线恢复（BLR）：基于 Georgiev-Gast 递推算法 $v_{\text{MWD}}[n] = (v[n] - v[n-M]) + \frac{1}{M_{\text{decay}}}\sum v[i]$，将前放无限长指数尾部精确抵消为有限矩形阶梯；结合滑动平均滤波与实时自适应基线跟踪冻结算法，根除高计数率（$> 50\text{ kHz}$）下的脉冲堆积与低频基线漂移，恢复本征 Fano 能量分辨率。 | method/formalism | direct | 第 4 章 §4.4, 印刷 pp. 182–195 / PDF pp. 182–195 | false |

## Competing Interpretations and Limitations

- **平顶宽度与噪声性能权衡**：虽然增加梯形滤波器的平顶时间 $FT$ 可以彻底消除大同轴 HPGe 探测器的弹道亏损，但过长的平顶会增加串联电压噪声（白噪声）的积累时间并恶化基线波动，同时增加脉冲堆积几率；必须在弹道亏损抑制与能量分辨率/通过率之间进行实验折衷标定。
- **译本排印勘误记录**：译本 PDF 第 216 页图 4.47 邻近文字中关于麻痹型死时间的公式印为 $m = m e^{-n\tau}$，系原稿排印符号混淆；根据输入输出定义应为 $m = n e^{-n\tau}$。

## Extracted Pages

- 印刷 pp. 15–25（PDF pp. 15–25）：Shockley-Ramo 定理、加权势与半导体感应电流。
- 印刷 pp. 175–194（PDF pp. 175–194）：模拟成形、极零相消与弹道亏损产生机理。
- 印刷 pp. 215–218（PDF pp. 215–218）：串联级联死时间、整形时间与 ADC 处理通道比较。
- 印刷 pp. 380–395（PDF pp. 380–395）：数字梯形滤波器离散递归算法与 FPGA 实现。
