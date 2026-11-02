---
type: concept
title: "In-beam high-rate pulser injection live-time calibration, cascaded pileup-ADC dead-time compensation and compound error propagation"
aliases: [pulser-injection-live-time, live-time-correction, cascaded-dead-time, pileup-loss-compensation, pulser-clock-discrepancy]
created: 2026-11-04
updated: 2026-11-04
status: ai-draft
review_status: unreviewed
tags: [gamma-spectroscopy, in-beam-spectroscopy, dead-time, live-time, pulser-injection, pileup-loss, absolute-intensity]
---

# In-beam high-rate pulser injection live-time calibration, cascaded pileup-ADC dead-time compensation and compound error propagation

## Definition and Phenomenological Origin

In in-beam $\gamma$-ray experiments with high-intensity accelerator beams (detector rates reaching $20 - 80\text{ kHz}$), event loss occurs through three distinct, cascaded physical stages:
1. **Fast Preamplifier/Shaper Pileup Rejection**: Pulses arriving within the shaping/inspection time are rejected or distorted into the continuum;
2. **ADC Conversion Dead Time**: Fixed or amplitude-dependent processing time (Wilkinson or pipelined flash ADCs);
3. **DAQ Event-Builder Busy Time**: Computer buffer overflows and disk writing latency.

Based on 吴治华《原子核物理实验方法》第 8 章 §8.4 (pp. 210–225), 汪晓莲《粒子探测技术》第 8 章 §8.2, 朱永生《实验物理中的概率和统计》第 4 章, and E. De Filippo et al. (NIM A 438, 397, 1999):
Standard hardware live-time clocks (LTC) gate a reference clock using the ADC/DAQ "busy" signal. However, LTC is **completely blind to analog pileup losses** occurring in the preamplifier and shaping amplifier!
Relying solely on hardware clocks leads to systematic underestimations of cross sections and absolute transition rates by $5\% - 20\%$.

---

## Mathematical Formalism: Pulser Injection Method & Compound Variance

### 1. The Pulser Monitor Principle
A high-stability pulse generator injects periodic charge pulses at known frequency $f_{\text{pulser}}$ directly into the detector preamplifier test input throughout the run duration $T_{\text{real}}$:
$$N_{\text{injected}} = f_{\text{pulser}} \cdot T_{\text{real}}$$
The recorded pulser peak area in the spectrum is $N_{\text{recorded}}$.
The **effective live-time fraction** accounting for all cascaded losses is:
$$\text{LT} = \frac{N_{\text{recorded}}}{N_{\text{injected}}}$$
with binomial sampling variance:
$$\sigma_{\text{LT}} = \sqrt{ \frac{\text{LT}(1 - \text{LT})}{N_{\text{injected}}} }$$

### 2. Physical Transition Peak Area Correction
For an observed net peak area $A_{\text{meas}} \pm \sigma_{A_{\text{meas}}}$:
$$A_{\text{true}} = \frac{A_{\text{meas}}}{\text{LT}}$$
The compound relative uncertainty (combining Poisson peak counting with binomial pulser monitoring) is:
$$\frac{\sigma_{A_{\text{true}}}}{A_{\text{true}}} = \sqrt{ \left( \frac{\sigma_{A_{\text{meas}}}}{A_{\text{meas}}} \right)^2 + \left( \frac{\sigma_{\text{LT}}}{\text{LT}} \right)^2 }$$

### 3. Diagnosis of Unmonitored Analog Pileup
Comparing the pulser live time against the hardware clock live time $\text{LT}_{\text{hardware}}$ isolates the unmonitored analog pileup loss fraction:
$$f_{\text{pileup}} = \frac{\text{LT}_{\text{hardware}} - \text{LT}_{\text{pulser}}}{\text{LT}_{\text{hardware}}}$$

---

## Executable Analysis Tool: `pulserlt`

The Python analysis suite integrates `in_beam_pulser_injection_live_time_corrector.py`, accessible via:

```bash
# Benchmark 1: High-rate (45 kHz) in-beam 130Ba run (reveals 8.08% unmonitored pileup loss)
python3 system/scripts/analysis/nuclear_analyzer.py pulserlt --preset in_beam_high_rate_clover_130Ba

# Benchmark 2: Moderate-rate (12 kHz) in-beam run (LT ~ 0.925)
python3 system/scripts/analysis/nuclear_analyzer.py pulserlt --preset moderate_rate_germanium_array

# Benchmark 3: Pure low-rate radioactive source calibration (LT ~ 0.988)
python3 system/scripts/analysis/nuclear_analyzer.py pulserlt --preset pure_low_rate_calibration
```

### Benchmark Validation: $^{130}\text{Ba}$ High-Rate In-Beam Run
- Real run duration: $T = 7200\text{ s}$, $f_{\text{pulser}} = 50.0\text{ Hz} \implies N_{\text{injected}} = 360000$ pulses;
- Recorded pulser counts: $N_{\text{recorded}} = 278640 \implies \text{LT} = 0.7740 \pm 0.0007$ ($22.60\%$ total dead-time loss);
- Hardware clock recorded $\text{LT}_{\text{hardware}} = 0.8420$, failing to detect $8.08\%$ analog pileup loss (`HIGH_ANALOG_PILEUP_LOSS`);
- Transition peak at $328.0\text{ keV}$ is corrected from $84500$ to true yield $109173.1 \pm 425.0$ counts.
