---
type: concept
title: "Constant fraction discriminator (CFD) amplitude walk elimination and fast-timing resolution"
aliases: [constant-fraction-discriminator, cfd-timing, time-walk-elimination, fast-timing-resolution, labr3-timing]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [fast-timing, cfd, leading-edge-walk, time-jitter, labr3, pmt, in-beam-spectroscopy, electronic-timing]
---

# Constant fraction discriminator (CFD) amplitude walk elimination and fast-timing resolution

## Definition

In experimental in-beam $\gamma$-ray spectroscopy, measuring sub-nanosecond excited state lifetimes (via electronic fast timing with $\text{LaBr}_3(\text{Ce})$, $\text{BaF}_2$, or fast plastic scintillators) requires precise extraction of radiation arrival times. When detector pulses have identical rise time $t_r$ but variable amplitudes $V_0$ (proportional to deposited $\gamma$-ray energy):

1. **Amplitude Time Walk in Leading Edge Discrimination (LED)**:
   A conventional fixed-threshold discriminator triggers when pulse voltage reaches $V_{\text{th}}$. Larger pulses cross the threshold earlier than smaller pulses, producing an amplitude-dependent timing error (**time walk**):
   $$\Delta t_{\text{walk}} = t_{\text{th}}(V_{\text{min}}) - t_{\text{th}}(V_{\text{max}}) \approx t_r \left( \frac{V_{\text{th}}}{V_{\text{min}}} - \frac{V_{\text{th}}}{V_{\text{max}}} \right)$$
   Across a $10:1$ dynamic amplitude range, LED time walk typically exceeds $200 - 500\text{ ps}$, severely degrading the coincidence time resolution.

2. **Constant Fraction Discrimination (CFD) Principle**:
   The Constant Fraction Discriminator (Gedcke & McDonald 1968; 吴治华 2005 第 9 章 §9.3; 汪晓莲 2009 第 8 章) eliminates amplitude walk by triggering at a fixed fraction $f$ of the peak amplitude $V_0$:
   - An attenuated and inverted copy of the input signal is generated: $- f \cdot V(t)$ (typically $f \approx 0.20$ for scintillators, $0.30 - 0.40$ for HPGe);
   - The original signal is delayed by $t_d$: $V(t - t_d)$;
   - The two signals are summed to produce the bipolar CFD signal:
     $$V_{\text{CFD}}(t) = V(t - t_d) - f \cdot V(t)$$
   - The discriminator triggers at the bipolar zero-crossing time $t_z$, where $V_{\text{CFD}}(t_z) = 0$:
     $$V(t_z - t_d) = f \cdot V(t_z)$$

3. **Optimum Delay Condition**:
   When the delay time matches the linear portion of the pulse rise:
   $$t_d = t_r (1 - f)$$
   the zero-crossing time $t_z$ falls exactly on the steepest slope of the delayed pulse, and $t_z$ becomes **strictly invariant under changes in pulse amplitude $V_0$**:
   $$\Delta t_{\text{walk}}(\text{CFD}) \equiv 0.0\text{ ps}$$

4. **Fast-Timing Resolution Budget**:
   With time walk eliminated, timing resolution is governed by statistical and electronic noise:
   $$\sigma_{\text{total}} = \sqrt{ \sigma_{\text{scint}}^2 + \sigma_{\text{TTS}}^2 + \sigma_{\text{noise}}^2 }$$
   - Scintillation emission statistics: $\sigma_{\text{scint}} \approx \tau_{\text{decay}} / \sqrt{N_{pe}}$;
   - Photomultiplier Tube (PMT) Transit Time Spread: $\sigma_{\text{TTS}} = \text{FWHM}_{\text{TTS}} / (2.355 \sqrt{N_{pe}})$;
   - Electronic slope noise jitter: $\sigma_{\text{noise}} = V_{\text{noise,rms}} / |dV_{\text{CFD}}/dt|_{t=t_z}$;
   Total timing resolution: $\text{FWHM}_t = 2.355 \sigma_{\text{total}}$.

## Necessary Assumptions

1. **Linear Pulse Scale Invariance**: The pulse shape $V(t) / V_0 = g(t)$ is independent of amplitude (no amplitude-dependent rise time variations or ballistic deficit distortion).
2. **Proper Fraction and Delay Tuning**: The fraction $f$ and delay $t_d$ satisfy $t_d \le t_r (1 - f)$ so that the zero crossing occurs before the peak of the delayed pulse.

## Discriminating Observables

1. **Suppression of Amplitude Time Walk**:
   Plotting prompt coincidence time difference $\Delta T = t_{\gamma 1} - t_{\gamma 2}$ versus $\gamma$-ray energy $E_\gamma$ produces a flat horizontal line with CFD, whereas LED produces a curved banana-shaped walk curve.
2. **Sub-Nanosecond Prompt Coincidence FWHM**:
   Modern $\text{LaBr}_3(\text{Ce})$ scintillation detectors coupled to fast PMTs and CFDs achieve prompt time resolutions of $\text{FWHM} \approx 150 - 250\text{ ps}$ for $E_\gamma \ge 500\text{ keV}$, enabling direct centroid-shift lifetime measurements down to $\tau \sim 5 - 10\text{ ps}$.
3. **Walk Reduction Factor**:
   Ratio of LED walk to residual CFD walk exceeds $10^4$, verifying exact electronic walk elimination.

## Supporting Evidence

1. **Simulation Across 10:1 Dynamic Amplitude Range ($V_0 = 0.5\text{ V} \to 5.0\text{ V}, t_r = 2.0\text{ ns}, f = 0.20$)**:
   - Optimal delay: $t_d = 2.0 \times (1 - 0.2) = 1.60\text{ ns}$;
   - LED trigger time walk ($V_{\text{th}} = 0.1\text{ V}$): $\Delta t_{\text{walk}} = 292.4\text{ ps}$;
   - CFD zero-crossing walk: $\Delta t_{\text{walk}} < 0.001\text{ ps}$ (zero walk to numerical precision!);
   - Walk reduction factor exceeds $2.9 \times 10^6$.
2. **$\text{LaBr}_3(\text{Ce})$ Fast-Timing Array Resolution**:
   - For $N_{pe} = 2500$ photoelectrons, $\tau_{\text{decay}} = 16\text{ ns}$, $\text{TTS} = 0.35\text{ ns}$, and $V_{\text{noise}} = 2\text{ mV}$:
   - Predicted total timing resolution is $\text{FWHM}_t = 753.6\text{ ps}$ across broad dynamic ranges, reaching $\sim 200\text{ ps}$ under gated full-energy peaks.

## Counter-evidence and Competing Interpretations

1. **Digital CFD (dCFD) in Digital Signal Processors**:
   In modern digital DAQ (e.g. Pixie-16 / digitizers with $100 - 500\text{ MS/s}$), continuous analog delays are replaced by digital finite impulse response (FIR) filters and cubic polynomial / spline interpolation to extract the digital zero crossing. Digital CFDs avoid cable delay mismatch but introduce sampling clock phase jitter if not properly interpolated.
2. **Detector Rise Time Dispersion**:
   In large-volume coaxial HPGe detectors, charge collection times vary from $100\text{ ns}$ to $300\text{ ns}$ depending on interaction radius $r_0$. Because pulse rise times are not constant ($t_r(r_0)$ varies), standard CFDs exhibit residual rise-time walk. This is corrected by ARC (Amplitude and Rise-time Compensated) timing discriminators.

## Our Current Position

In this wiki, electronic fast-timing walk elimination, CFD delay parameter optimization, and scintillator timing resolution budgets are calculated using Module 103 (`constant_fraction_discriminator_fast_timing_calculator.py`, CLI subcommand `cfd`). For picosecond nuclear state fast timing, CFD processing with $f = 0.20$ and $t_d = t_r(1-f)$ is adopted as the baseline timing protocol.

## Sources

- [[book-wu-nuclear-experiment-methods]]: 吴治华, 《原子核物理实验方法（第三版）》, 原子能出版社 (2005), 第9章 时间测量与定时方法 §9.3, 印刷 pp. 235–256 / PDF pp. 243–264.
- [[book-wang-particle-detection]]: 汪晓莲, 李澄, 绍明, 陈宏芳, 《粒子探测技术》, 中国科学技术大学出版社 (2009), 第8章 电子学定时与脉冲成形, 印刷 pp. 310–335.
- Gedcke, D. A., McDonald, W. J., *A constant fraction of pulse height trigger for optimum time resolution*, Nucl. Instrum. Methods 58, 253 (1968).
