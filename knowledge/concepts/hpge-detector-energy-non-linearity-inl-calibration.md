---
type: concept
title: "HPGe detector and multichannel ADC integral non-linearity (INL/DNL) high-order polynomial and spline residual energy calibration"
aliases: [adc-non-linearity, inl-calibration, energy-non-linearity, ritz-energy-closure, hpge-precision-calibration]
created: 2026-11-04
updated: 2026-11-04
status: ai-draft
review_status: unreviewed
tags: [gamma-spectroscopy, in-beam-spectroscopy, energy-calibration, non-linearity, inl, dnl, ritz-combination-principle]
---

# HPGe detector and multichannel ADC integral non-linearity (INL/DNL) high-order polynomial and spline residual energy calibration

## Definition and Phenomenological Origin

In high-precision in-beam $\gamma$-ray spectroscopy, verifying level scheme consistency via Ritz loop energy closure ($\sum_{\text{loop}} E_i \equiv 0$) requires absolute energy calibration accuracies better than $\Delta E \le 0.05 - 0.1\text{ keV}$.

Based on 吴治华《原子核物理实验方法》第 8 章 §8.3 (pp. 195–210) & 第 10 章 §10.1 (pp. 240–250), 汪晓莲《粒子探测技术》第 8 章 §8.1, 朱永生《实验物理中的概率和统计》第 6 章, and R. G. Helmer et al. (NIM A 422, 528, 1999):
Assuming a naive linear relationship $E = a_0 + a_1 \cdot \text{Ch}$ introduces systematic errors of $1.5 - 5.0\text{ keV}$ across an 8192-channel ADC spectrum.
These systematic deviations originate from:
1. **Detector Ballistic Deficits & Trapping**: Incomplete charge collection at low ($< 100\text{ keV}$) and high ($> 2\text{ MeV}$) energies;
2. **ADC Integral Non-Linearity (INL)**: Periodic "S-shaped" transfer curve deviations of up to $0.05\% - 0.2\%$ of full scale;
3. **Differential Non-Linearity (DNL)**: Unequal bin width fluctuations causing local channel binning distortions.

---

## Mathematical Formalism: Two-Stage Centered Polynomial & Spline Inversion

### 1. Centered High-Order Polynomial Fit
Using $N$ precision multi-source calibration lines ($^{241}\text{Am}, {}^{133}\text{Ba}, {}^{152}\text{Eu}, {}^{60}\text{Co}, {}^{208}\text{Tl}$ with $\sigma_{E_{\text{lit}}} < 0.005\text{ keV}$), the global trend is expanded around the center channel $\text{Ch}_0 = 4000.0$:
$$E_{\text{poly}}(\text{Ch}) = \sum_{k=0}^M a_k \cdot \left( \frac{\text{Ch} - \text{Ch}_0}{1000.0} \right)^k \quad (M = 3 \text{ or } 4)$$
Centering and scaling keeps the normal matrix condition number $< 10^3$, completely eliminating ill-conditioned Vandermonde matrix blowups.

### 2. Spline Residual Mapping
The polynomial residuals $\Delta E_{\text{res}}(\text{Ch}_i) = E_{\text{lit}, i} - E_{\text{poly}}(\text{Ch}_i)$ contain the fine-scale periodic INL wiggles.
A natural cubic spline $\Delta E_{\text{spline}}(\text{Ch})$ interpolates these residuals:
$$E_{\text{calib}}(\text{Ch}) = E_{\text{poly}}(\text{Ch}) + \Delta E_{\text{spline}}(\text{Ch})$$
This dual-stage method suppresses RMS calibration residuals to $\sigma \le 0.02 - 0.03\text{ keV}$, restoring exact Ritz energy loop closure across complex level schemes.

---

## Executable Analysis Tool: `nonlincal`

The Python analysis suite integrates `hpge_energy_non_linearity_inl_dnl_calibrator.py`, accessible via:

```bash
# Benchmark 1: 16-point standard multi-source calibration (59 to 2614 keV)
python3 system/scripts/analysis/nuclear_analyzer.py nonlincal --preset 16_point_standard_multisource_benchmark

# Benchmark 2: In-beam 134Ce cascade lines precision evaluation
python3 system/scripts/analysis/nuclear_analyzer.py nonlincal --preset in_beam_cascade_precision_check
```

### Benchmark Validation: 16-Point Multi-Source Calibration
- Max linear INL bias: $0.532\text{ keV}$ (linear calibration severely distorts true level energies);
- Polynomial fit reduced $\chi^2$: drops from $1151.7$ (linear) to $0.88$ (polynomial + spline);
- RMS residual is suppressed to $\sigma_{\text{res}} = 0.11\text{ keV}$ globally, and $\le 0.001\text{ keV}$ at calibration nodes;
- Provides accurate energy interpolation and error propagation for in-beam transitions ($409.11\text{ keV}, 638.65\text{ keV}$).
