---
type: concept
title: "In-beam true coincidence summing (TCS) corrections and close-geometry efficiency calibration"
aliases: [true-coincidence-summing, tcs-correction, summing-out-correction, summing-in-peak, close-geometry-spectroscopy]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [in-beam-spectroscopy, true-coincidence-summing, tcs, peak-to-total-ratio, close-geometry, efficiency-calibration, cascade-corrections]
---

# In-beam true coincidence summing (TCS) corrections and close-geometry efficiency calibration

## Definition

### Definition and Phenomenological Origin

In in-beam $\gamma$-ray spectroscopy, experiments increasingly deploy compact, close-geometry High-Purity Germanium (HPGe) arrays (such as Clover detectors or mini-arrays placed at distances $d \sim 5 - 15\text{ cm}$ from the target) to maximize geometric solid angle coverage ($\Omega / 4\pi \sim 1\% - 5\%$ per crystal).

When a cascade of $\gamma$-rays is emitted in prompt sequence ($I_1 \xrightarrow{\gamma_1} I_2 \xrightarrow{\gamma_2} I_3$) within the charge-collection resolving time ($\sim 100 - 300\text{ ns}$):
1. **Summing-Out Effect (Photopeak Loss)**:
   Photon $\gamma_1$ deposits its full energy $E_1$ in the crystal, while the cascade partner $\gamma_2$ simultaneously interacts in the same crystal (via Compton scattering or photoelectric absorption). The combined charge pulse corresponds to $E_1 + \Delta E_2 > E_1$.
   **Result**: The event is removed from the photopeak of $\gamma_1$, causing measured net peak counts to be systematically suppressed by $10\% - 25\%$!
2. **Summing-In Effect (Spurious Sum Peak)**:
   Both $\gamma_1$ and $\gamma_2$ deposit their full energies simultaneously in the crystal, synthesizing an artificial virtual photopeak at $E_{\text{sum}} = E_1 + E_2$ (e.g. the $2505.7\text{ keV}$ sum peak in $^{60}\text{Co}$).

Based on 吴治华《原子核物理实验方法》第 10 章 §10.5 (pp. 275–285), 汪晓莲等《粒子探测技术》第 5 章, and K. Debertin & R. G. Helmer (1988):
Ignoring TCS leads to distorted level-scheme branching ratios, erroneous internal conversion coefficients, and false side-feeding yields!

---

## Mathematical TCS Correction Formalism

### 1. Analytical Summing-Out Attenuation
For transition $\gamma_1$ feeding $\gamma_2$ with internal conversion coefficient $\alpha_{\text{tot}, 2}$:
$$N_1^{\text{obs}} = N_0 \cdot b_1 \cdot \varepsilon_p(E_1) \cdot \left[ 1 - \alpha_{\text{tot}, 2} \right] \cdot \left[ 1 - \varepsilon_t(E_2) W(\theta=0) \right]$$
where:
- $\varepsilon_p(E_1)$ = full-energy photopeak efficiency;
- $\varepsilon_t(E_2)$ = total interaction efficiency (photoelectric + Compton + pair creation);
- $W(\theta=0)$ = directional correlation factor at zero relative angle.

The summing-out correction factor $C_{\text{out}}(E_1)$ is:
$$C_{\text{out}}(E_1) = \frac{N_1^{\text{true}}}{N_1^{\text{obs}}} = \frac{1}{1 - \varepsilon_t(E_2) W(\theta=0)}$$

### 2. Peak-to-Total ($P/T$) Ratio Relation
The total efficiency $\varepsilon_t(E)$ is related to the photopeak efficiency through the detector's Peak-to-Total ratio:
$$\varepsilon_t(E) = \frac{\varepsilon_p(E)}{P/T(E)}$$
In typical HPGe crystals, $P/T \approx 0.20 - 0.30$ at $1\text{ MeV}$, meaning total interaction efficiency is $3 - 5$ times higher than photopeak efficiency!

### 3. Virtual Summing-In Peak Count Rate
$$N_{\text{sum-in}}(E_1 + E_2) = N_0 \cdot b_1 b_2 \cdot \varepsilon_p(E_1) \varepsilon_p(E_2) \cdot W(\theta=0)$$

---

## Canonical Experimental Benchmarks

1. **$^{60}\text{Co}$ Close-Geometry Calibration ($1173.2\text{ keV} \to 1332.5\text{ keV}$, $d = 10\text{ cm}$)**:
   - $\varepsilon_p(1173) = 2.50\%, \varepsilon_t(1332) = 11.00\% \implies C_{\text{out}}(1173) = 1.1236$ ($+12.4\%$ correction needed);
   - $\varepsilon_p(1332) = 2.20\%, \varepsilon_t(1173) = 11.36\% \implies C_{\text{out}}(1332) = 1.1282$ ($+12.8\%$ correction needed);
   - Virtual sum peak at $2505.7\text{ keV}$ produces $550$ false counts per $10^6$ decays.
2. **$^{134}\text{Ce}$ In-Beam Yrast Cascade ($4_1^+ \xrightarrow{638} 2_1^+ \xrightarrow{409} 0^+$)**:
   - High close-geometry efficiency produces $\sim 15\%$ summing-out loss, successfully rectified by the TCS engine.

---


## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。

## Sources

### 参考文献与交叉引用


- **Wu Zhihua (吴治华)**: *Methods of Nuclear Physics Experiments* (《原子核物理实验方法》), Fudan University Press (1995), Chapter 10 §10.5 (Coincidence Summing in Spectrometry), pp. 275–285.
- **Wang Xiaolian (汪晓莲) et al.**: *Particle Detection Technology* (《粒子探测技术》), USTC Press (2009), Chapter 5.
- **Debertin, K. & Helmer, R. G.**: *Gamma- and X-Ray Spectrometry with Semiconductor Detectors*, North-Holland (1988).


## Necessary Assumptions

微观平均场假定核子在有效单体势中运动，通过剩余相互作用自洽诱发四极形变与集体转动。


## Discriminating Observables

激发能量级间距、跃迁多极性比值与电磁约化跃迁几率是关键鉴别观测量。


## Supporting Evidence

在束伽马谱学实验测定的角分布、DCO比值与能级寿命提供直接实证。
