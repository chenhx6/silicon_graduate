---
type: method
title: "Nakhostin 辐射探测器数字信号处理、脉冲成形与时差算法方法合同"
aliases: [Nakhostin Digital Pulse Processing Contract, 探测器数字信号处理方法合同]
created: 2026-11-04
updated: 2026-11-04
status: active
review_status: unreviewed
method_type: digital-signal-processing-contract
tags: [digital-signal-processing, trapezoidal-filter, jordanov-algorithm, mwd, baseline-restoration, digital-cfd, enc-noise, pileup-rejection]
topics: [digital-pulse-processing, hpge-detectors, fast-timing, pileup-rejection]
sources: [book-nakhostin-signal-processing-detectors, book-wu-nuclear-experiment-methods, book-wang-particle-detection]
---

# Nakhostin 辐射探测器数字信号处理、脉冲成形与时差算法方法合同

## Purpose

本方法合同严格绑定 Mohammad Nakhostin 专著 *Signal Processing for Radiation Detectors*（Wiley 2017 / 吴鸿毅译 2020）第 1、3、4、7、10 章，
系统形式化 Shockley-Ramo 电荷感应定理与弹道亏损微观机制、Jordanov 递归离散差分梯形滤波算法、数字化移动窗口反褶积（MWD）与自适应基线恢复（BLR）、数字恒比定时（Digital CFD）过零点插值算法，以及前放等效噪声电荷（ENC）解析模型与最优成形时间 $\\tau_{\\text{opt}}$，
为在束核谱学探测系统数字化数据采集（DPP/DAQ）、FPGA 实时在线成形与高计数率能谱分辨率恢复提供标准算法合同。

## Inputs and Assumptions

1. **Shockley-Ramo 加权场假设**：电荷移动产生的感应电流正比于电荷速度与静态加权电场点积 $i(t) = q \\vec{v}(t) \\cdot \\vec{E}_w$；
2. **离散均匀时域采样**：模拟电荷脉冲经闪速 ADC 在固定周期 $T_s$（如 $10\\text{ ns}$ 对应 $100\\text{ MSPS}$）下数字化为无丢点序列 $v[n]$；
3. **前放单指数衰减响应**：电荷灵敏前置放大器输出波形前沿具有收集时间 $t_c$，后沿满足单指数放电 $e^{-t/\\tau_{\\text{pre}}}$；
4. **噪声源独立相加假设**：并联电流白噪声、串联电压白噪声与 $1/f$ 闪烁噪声互相统计独立。

## What It Can Establish

1. **Shockley-Ramo 电荷感应与弹道亏损根除准则**：
   $$i(t) = q \\vec{v}(t) \\cdot \\vec{E}_w(\\vec{r}(t)),\\quad Q = \\int i(t)dt$$
   - 证明大体积 HPGe 探测器不同位置收集时间差异（$\\Delta t_c \\sim 100 - 300\\text{ ns}$）导致模拟成形产生严重弹道亏损；
   - 证明设计平顶宽度满足 $T_{\\text{flat}} \\ge t_{c, \\max}$ 的梯形滤波器可在波形中心完全消除弹道亏损；
2. **Jordanov 离散有限差分递归梯形滤波算法**：
   $$d^k[n] = v[n] - v[n-k]$$
   $$p[n] = p[n-1] + d^k[n] - d^k[n-l]$$
   $$s[n] = s[n-1] + p[n] + M d^k[n] - M d^k[n-l]$$
   - 其中数字极零补偿因子 $M = 1 / (e^{T_s/\\tau_{\\text{pre}}} - 1)$；
   - 证明全算法仅含加减法与整型累加，在 FPGA 上可零浮点开销实现实时能谱成形；
3. **移动窗口反褶积（MWD）与高计数率自适应基线恢复**：
   $$v_{\\text{MWD}}[n] = (v[n] - v[n - M_{\\text{win}}]) + \\frac{1}{\\tau_{\\text{decay}}} \\sum_{i = n - M_{\\text{win}} + 1}^n v[i]$$
   - 将无限长指数拖尾反褶积为宽度严格有限的矩形脉冲，并在脉冲触发时冻结基线滑动更新，彻底消除高计数率（$>50\\text{ kHz}$）下的脉冲堆积展宽；
4. **数字恒比定时（Digital CFD）亚采样周期插值**：
   $$c[n] = x[n] - f \\cdot x[n - D],\\quad t_{\\text{zero}} = \\left( n_0 + \\frac{-c[n_0]}{c[n_0+1] - c[n_0]} \\right) T_s$$
   - 理论证明差分过零点时刻独立于脉冲振幅，消除确定性时间游走（Walk），在 $100\\text{ MHz}$ 采样下实现 $\\sigma_t \\le 200\\text{ ps}$ 的亚纳秒时间分辨率；
5. **等效噪声电荷（ENC）最优化**：
   $$\\text{ENC}^2 = a \\tau + \\frac{b C_{\\text{tot}}^2}{\\tau} + c \\implies \\tau_{\\text{opt}} = C_{\\text{tot}}\\sqrt{\\frac{b}{a}}$$
   - 给出大电容同轴 HPGe 探测器最佳成形时间（$4 - 8\\ \\mu\\text{s}$）与快速闪烁探测器（$50 - 200\\text{ ns}$）的定量理论界据。

## What It Cannot Establish Alone

1. **半导体晶格中子辐照空穴俘获**：数字成形无法恢复由于强中子损伤深能级陷阱造成的载流子永久性丢失，需结合电荷收集模拟补偿（如启发式前沿上升时间修正）；
2. **探测器死区与真实灵敏体积比率**：算法处理输入电信号，不能替代由高精度准直源测定的锗晶体死层（Dead layer）几何测量；
3. **极端多粒子重叠波形拓扑盲区**：当两个脉冲到达时间间隔小于输入信号固有上升时间（$\\Delta t < t_r \\sim 30\\text{ ns}$）时，数字快成形通道无法分辨两个独立前沿，必然被误判为单事件。

## Sources

- [[book-nakhostin-signal-processing-detectors]]
- [[book-wu-nuclear-experiment-methods]]
- [[book-wang-particle-detection]]
- [[nuclear-detector-spectroscopy-wu-vs-wang-reconciliation]]
