---
type: concept
title: "In-beam gamma-gamma gated coincidence matrix background-subtracted multiplet deconvolution and peak area covariance"
aliases: [gated-matrix-multiplet-fitting, coincidence-peak-deconvolution, multiplet-covariance, in-beam-peak-overlap, radware-gated-deconvolution]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [in-beam-spectroscopy, gamma-gamma-coincidence, multiplet-fitting, peak-deconvolution, covariance-matrix, background-subtraction]
---

# In-beam gamma-gamma gated coincidence matrix background-subtracted multiplet deconvolution and peak area covariance

## Definition and Phenomenological Origin

In in-beam $\gamma$-ray spectroscopy using multi-detector HPGe arrays (e.g. Gammasphere, AGATA, Clover arrays), coincidence data are sorted into a symmetric two-dimensional matrix $M(E_1, E_2)$.

Based on 吴治华《原子核物理实验方法》第 10 章 §10.2–10.3 (pp. 250–265), 汪晓莲《粒子探测技术》第 5 章, 朱永生《实验物理中的概率和统计》第 8–9 章, and D. C. Radford (NIM A 361, 297, 1995):
1. When placing an energy gate on transition $\gamma_1$, the projected coincident spectrum contains both genuine coincidence peaks and underlying Compton scattering continuum.
2. Subtracting adjacent left ($B_L$) and right ($B_R$) background windows produces the net gated spectrum:
   $$S(E) = P_G(E) - f_L B_L(E) - f_R B_R(E)$$
   with variance propagated via Poisson counting statistics:
   $$\sigma^2_S(E) = P_G(E) + f_L^2 B_L(E) + f_R^2 B_R(E)$$
3. Transitions connecting rotational levels often appear as close **multiplets** (e.g. doublets separated by $\Delta E \le 1.5 - 3.5\text{ keV}$, comparable to the detector $\text{FWHM} \sim 2.0 - 2.5\text{ keV}$).
   Standard independent peak fitting fails because the peak areas are strongly coupled.

---

## Mathematical Formalism: Coupled Multiplet Lineshape & Area Covariance

### 1. Composite Model Function
The composite profile is parameterized by $K$ Gaussians sharing the detector's local energy resolution width $\sigma = \text{FWHM}(E) / 2.355$ plus a residual background:
$$F(E) = \sum_{j=1}^K \frac{A_j}{\sqrt{2\pi}\sigma} \exp\left( -\frac{(E - E_j)^2}{2\sigma^2} \right) + b_0 + b_1 (E - E_{\text{center}})$$

### 2. Weighted Non-Linear Optimization & Full Covariance Matrix
Fitting the parameter vector $\mathbf{p} = [A_1, E_1, \dots, A_K, E_K, \sigma, b_0, b_1]$ via weighted least squares minimizes:
$$\chi^2 = \sum_i \frac{[S(E_i) - F(E_i; \mathbf{p})]^2}{\sigma_S^2(E_i)}$$
The parameter covariance matrix $\mathbf{V} = (\mathbf{J}^T \mathbf{W} \mathbf{J})^{-1}$ yields the mutual correlation coefficient between overlapping peak areas:
$$\rho(A_i, A_j) = \frac{V_{A_i, A_j}}{\sqrt{V_{A_i, A_i} V_{A_j, A_j}}}$$

When separation $D = \Delta E / \text{FWHM} < 2.0$, $\rho(A_1, A_2)$ is strongly negative ($\rho \sim -0.50 \text{ to } -0.90$).
Ignoring this covariance when evaluating branching ratios $I_1 / I_2$ or total feeding sums $I_1 + I_2$ introduces large unphysical uncertainties.

---

## Executable Analysis Tool: `gatedmult`

The Python analysis suite integrates `in_beam_gated_matrix_multiplet_deconvolution_fitter.py`, accessible via:

```bash
# Benchmark 1: 133Ce wobbling candidate close doublet (638.2 and 641.4 keV)
python3 system/scripts/analysis/nuclear_analyzer.py gatedmult --preset 133Ce_wobbling_candidate_doublet

# Benchmark 2: 130Ba overlapping in-beam triplet (455.0, 458.5, and 464.0 keV)
python3 system/scripts/analysis/nuclear_analyzer.py gatedmult --preset 130Ba_two_quasiparticle_triplet

# Benchmark 3: Isolated single calibration peak (1332.5 keV)
python3 system/scripts/analysis/nuclear_analyzer.py gatedmult --preset isolated_single_peak_benchmark
```

### Benchmark Validation
1. **$^{133}\text{Ce}$ Doublet**:
   $\Delta E = 3.20\text{ keV}$, $\text{FWHM} = 2.146\text{ keV}$ ($D = 1.49\times\text{FWHM}$, severely overlapping).
   Deconvoluted areas: Peak 1 ($638.20\text{ keV}$) = $12544.5 \pm 61.8$ ($0.36\%$ from truth $12500$); Peak 2 ($641.40\text{ keV}$) = $8455.6 \pm 51.8$ ($0.66\%$ from truth $8400$).
   Reduced $\chi^2/\text{ndf} = 1.08$.
2. **$^{130}\text{Ba}$ Triplet**:
   Resolves 3 overlapping peaks within $9\text{ keV}$ span with accuracy better than $0.8\%$.
