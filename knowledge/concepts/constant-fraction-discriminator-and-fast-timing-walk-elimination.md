---
type: concept
title: "Constant fraction discriminator (CFD) amplitude walk elimination and fast-timing resolution"
aliases: [constant-fraction-discriminator, cfd-timing, time-walk-elimination, fast-timing-resolution, labr3-timing]
created: 2026-11-03
updated: 2026-11-20
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

3. **Conditional Amplitude Invariance**:
   For ideal self-similar pulses $V(t)=V_0g(t)$, the amplitude cancels from the zero-crossing equation. This does not require a universal optimum delay. For a linear ramp while both terms remain on the rise,
   $$t_z=t_d/(1-f),\qquad 0<t_d<(1-f)t_r.$$
   Equality places the crossing at the original pulse peak, not a generally optimal operating point. Shape changes, noise and discriminator response can leave residual walk; zero in a toy calculation is not zero walk in a detector.

4. **Fast-Timing Resolution Budget**:
   With time walk eliminated, timing resolution is governed by statistical and electronic noise:
   $$\sigma_{\text{total}} = \sqrt{ \sigma_{\text{scint}}^2 + \sigma_{\text{TTS}}^2 + \sigma_{\text{noise}}^2 }$$
   - Scintillation emission statistics: $\sigma_{\text{scint}} \approx \tau_{\text{decay}} / \sqrt{N_{pe}}$;
   - Photomultiplier Tube (PMT) Transit Time Spread: $\sigma_{\text{TTS}} = \text{FWHM}_{\text{TTS}} / (2.355 \sqrt{N_{pe}})$;
   - Electronic slope noise jitter: $\sigma_{\text{noise}} = V_{\text{noise,rms}} / |dV_{\text{CFD}}/dt|_{t=t_z}$;
   Total timing resolution: $\text{FWHM}_t = 2.355 \sigma_{\text{total}}$.

## Necessary Assumptions

1. **Linear Pulse Scale Invariance**: The pulse shape $V(t) / V_0 = g(t)$ is independent of amplitude (no amplitude-dependent rise time variations or ballistic deficit distortion).
2. **Proper Fraction and Delay Tuning**: The ramp inequality above belongs to that waveform model. Actual fractions, delays and calibration depend on detector pulse shapes and electronics, not a single universal setting.

## Discriminating Observables

1. **Suppression of Amplitude Time Walk**:
   Measure the residual timing centroid versus energy and event class after discrimination. CFD can suppress amplitude walk without producing a perfectly flat real calibration curve.
2. **Sub-Nanosecond Prompt Coincidence FWHM**:
   Prompt resolution and lifetime precision depend on energy, statistics, calibration, feeding and gates. A coincidence FWHM alone does not establish a universal minimum measurable lifetime.
3. **Walk Reduction Factor**:
   Report the measured residual and its uncertainty, not a universal reduction ratio or a numerical zero as proof of exact elimination.

## Supporting Evidence

[[smith-2017-109ru-109tc-fast-timing-thesis]] PDF55-60 describes actual CFD electronics but still requires separate beta and LaBr3 walk calibrations. In that calibration, below 400 keV, full-energy and Compton events have different timing responses. This is direct evidence against equating installed CFD with calibration-free timing, not a contradiction of ideal amplitude cancellation.

The historical simulations below were not rerun or certified as experimental detector performance in this batch. The timing-budget formulas above are an idealized parameterization, not a complete measured resolution model.

1. **Simulation Across 10:1 Dynamic Amplitude Range ($V_0 = 0.5\text{ V} \to 5.0\text{ V}, t_r = 2.0\text{ ns}, f = 0.20$)**:
   - Historical chosen delay (not a validated optimum): $t_d = 2.0 \times (1 - 0.2) = 1.60\text{ ns}$;
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

The historical implementation reference is Module 103 (`constant_fraction_discriminator_fast_timing_calculator.py`, CLI subcommand `cfd`); it was not executed in this learning batch. Do not adopt its toy fraction/delay as a universally validated experimental protocol. Actual pulse classes, residual walk, prompt response and background gates require calibration.

An explicitly illustrative check uses $g(t)=1-\exp(-t/t_r)$ and gives $t_z=t_r\ln[(\exp(t_d/t_r)-f)/(1-f)]$. With arbitrary $f=0.2$, $t_d=0.4$ns, changing $t_r$ from1ns to2ns shifts the root by about9.44ps. This is a waveform-model counterexample to universal zero walk, not Smith detector inputs or a prediction of its residual.

## Sources

- [[smith-2017-109ru-109tc-fast-timing-thesis]]: actual CFD, walk calibration and event-class dependence; PDF55-60.

- [[book-wu-nuclear-experiment-methods]]: 吴治华, 《原子核物理实验方法（第三版）》, 原子能出版社 (2005), 第9章 时间测量与定时方法 §9.3, 印刷 pp. 235–256 / PDF pp. 243–264.
- [[book-wang-particle-detection]]: 汪晓莲, 李澄, 绍明, 陈宏芳, 《粒子探测技术》, 中国科学技术大学出版社 (2009), 第8章 电子学定时与脉冲成形, 印刷 pp. 310–335.
- Gedcke, D. A., McDonald, W. J., *A constant fraction of pulse height trigger for optimum time resolution*, Nucl. Instrum. Methods 58, 253 (1968).
