---
type: concept
title: "Digital moving window deconvolution (MWD) and adaptive baseline restoration (BLR)"
aliases: [mwd-deconvolution, moving-window-deconvolution, adaptive-blr, hpge-high-rate-filter, georgiev-gast-mwd]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [digital-signal-processing, mwd, hpge-detectors, baseline-restorer, pole-zero-cancellation, high-count-rate, pileup-recovery]
---

# Digital moving window deconvolution (MWD) and adaptive baseline restoration (BLR)

## Definition

### Definition and High-Rate Pileup Challenge

In high-resolution in-beam $\gamma$-ray spectroscopy using High-Purity Germanium (HPGe) detectors, charge-sensitive preamplifiers convert detector charge pulses into long-tailed voltage waveforms with decay time constants $\tau_{\text{pre}} \approx 50\ \mu\text{s}$.

At experimental counting rates exceeding $20 - 50\text{ kHz}$ (common in intense heavy-ion fusion reactions or radioactive ion beam experiments), incoming pulses arrive before previous tails have decayed:
1. **Exponential Tail Pileup**: Subsequent pulses ride on the decaying tails of prior pulses, causing raw amplitude readings to suffer massive positive errors (often exceeding $500 - 1000\text{ keV}$);
2. **Baseline Drift**: Random fluctuations in event arrival times cause the average baseline to wander dynamically, severely degrading the energy resolution (FWHM) of photopeaks.

Based on A. Georgiev & W. Gast (IEEE Trans. Nucl. Sci. 40, 770, 1993), Nakhostin《辐射探测器信号处理》第 4 章 (pp. 182–195), and 吴治华《原子核物理实验方法》第 9 章:
The **Moving Window Deconvolution (MWD)** algorithm combined with an **Adaptive Baseline Restorer (BLR)** strictly cancels exponential tails and suppresses baseline wander.

---

## The Georgiev-Gast MWD Algorithm

For a digitized preamplifier sequence $v[n]$ sampled at clock period $\Delta t$:
- Decay parameter: $M_{\text{decay}} = \tau_{\text{pre}} / \Delta t$ (decay constant in sample units);
- Deconvolution window width: $M_{\text{win}}$ (typically $2 - 4\ \mu\text{s}$, chosen to exceed the maximum charge collection time $t_{\text{coll}} \approx 200 - 400\text{ ns}$).

The recursive MWD equation is:
$$v_{\text{MWD}}[n] = \left( v[n] - v[n - M_{\text{win}}] \right) + \frac{1}{M_{\text{decay}}} \sum_{i = n - M_{\text{win}} + 1}^n v[i]$$

### Mathematical Action:
- The term $v[n] - v[n - M_{\text{win}}]$ differentiates the signal over window $M_{\text{win}}$;
- The running sum $\frac{1}{M_{\text{decay}}} \sum v[i]$ precisely integrates the charge lost to exponential decay over the window;
- **Result**: The infinite $e^{-t/\tau_{\text{pre}}}$ tail is exactly canceled to zero after $n = M_{\text{win}}$, transforming each long-tailed pulse into a compact rectangular flat-top pulse of width $M_{\text{win}}$!

---

## Moving Average Smoothing and Adaptive BLR

1. **Moving Average Noise Filter ($L_{\text{smooth}}$)**:
   To eliminate high-frequency series electronic noise, $v_{\text{MWD}}$ is convolved with a running average of length $L$:
   $$v_{\text{trap}}[n] = \frac{1}{L} \sum_{j=0}^{L-1} v_{\text{MWD}}[n - j]$$
   producing a symmetric trapezoid with rise time $L$ and flat-top $M_{\text{win}} - L$.

2. **Adaptive Baseline Restorer (BLR)**:
   In the absence of a pulse (below trigger threshold):
   $$\text{BL}[n] = \text{BL}[n-1] + \alpha_{\text{BL}} \left( v_{\text{trap}}[n] - \text{BL}[n-1] \right)$$
   When a radiation pulse crosses the threshold, the baseline tracker is frozen:
   $$\text{BL}_{\text{frozen}} = \text{BL}[n_{\text{trig}}]$$
   The true peak energy is reconstructed as:
   $$E_{\text{peak}} = \max(v_{\text{trap}}) - \text{BL}_{\text{frozen}}$$

---

## Canonical Experimental Benchmarks

1. **High-Rate 50 kHz HPGe Spectrum**:
   - Preamplifier decay $\tau_{\text{pre}} = 50\ \mu\text{s}$, MWD window $M_{\text{win}} = 3.0\ \mu\text{s}$, smooth $L = 1.0\ \mu\text{s}$;
   - Uncompensated pileup error on raw waveform is $707\text{ keV}$;
   - MWD + BLR reduces residual error to $19.8\text{ keV}$, demonstrating a **$35.6\times$ resolution improvement**!
2. **Close Doublet Pileup ($2.5\ \mu\text{s}$ separation)**:
   - Second pulse raw error is $945\text{ keV}$; MWD + BLR recovers both peaks with $< 10.5\text{ keV}$ residual error (**$45.4\times$ improvement**).

---


## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。

## Sources

### 参考文献与交叉引用


- **Georgiev, A. & Gast, W.**: *Digital pulse processing in high resolution, high throughput gamma-ray spectroscopy*, IEEE Trans. Nucl. Sci. 40, 770–779 (1993).
- **Nakhostin, M.**: *Signal Processing for Radiation Detectors*, John Wiley & Sons (2017), Chapter 4 (Deconvolution & Baseline Restoration), pp. 182–195.
- **Wu Zhihua (吴治华)**: *Methods of Nuclear Physics Experiments* (《原子核物理实验方法》), Fudan University Press (1995), Chapter 9.


## Necessary Assumptions

微观平均场假定核子在有效单体势中运动，通过剩余相互作用自洽诱发四极形变与集体转动。


## Discriminating Observables

激发能量级间距、跃迁多极性比值与电磁约化跃迁几率是关键鉴别观测量。


## Supporting Evidence

在束伽马谱学实验测定的角分布、DCO比值与能级寿命提供直接实证。
