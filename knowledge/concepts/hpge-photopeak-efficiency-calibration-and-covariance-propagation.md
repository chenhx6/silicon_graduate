---
type: concept
title: "HPGe and Clover detector photopeak efficiency curve weighted least squares calibration and rigorous covariance error propagation"
aliases: [efficiency-calibration, photopeak-efficiency, covariance-propagation, radford-efficiency, efficiency-error-overestimation]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [gamma-spectroscopy, efficiency-calibration, hpge-detectors, clover-detectors, weighted-least-squares, covariance-matrix, error-propagation]
---

# HPGe and Clover detector photopeak efficiency curve weighted least squares calibration and rigorous covariance error propagation

## Definition and Physical Motivation

In in-beam $\gamma$-ray spectroscopy and radioactivity measurements, determining absolute and relative transition intensities, branching ratios $I_\gamma$, internal conversion coefficients $\alpha_K$, and multipole mixing ratios requires knowledge of the detector photopeak efficiency curve $\varepsilon(E_\gamma)$ across $E_\gamma \sim 80\text{ keV} - 3.5\text{ MeV}$.

Based on 吴治华《原子核物理实验方法》第 10 章 §10.4 (pp. 265–275), 汪晓莲《粒子探测技术》第 5 章, 朱永生《实验物理中的概率和统计》第 3 章 §3.4 & 第 6–7 章, and D. C. Radford (NIM A 361, 297, 1995):
1. Standard multi-$\gamma$ calibration sources ($^{152}\text{Eu}, {}^{133}\text{Ba}, {}^{60}\text{Co}$) provide discrete calibration data points $(E_i, \varepsilon_i \pm \sigma_i)$ with high precision.
2. For coaxial HPGe and Clover detectors, efficiency curves in the photoelectric/Compton-dominated regime are parameterized in logarithmic polynomial space:
   $$\ln\varepsilon(E) = \sum_{k=0}^M a_k \cdot \left[ \ln\left( \frac{E}{E_0} \right) \right]^k$$
   where $E_0 = 1000\text{ keV}$ is an energy scaling reference ensuring a well-conditioned normal matrix.

---

## Mathematical Formalism: WLS & Parameter Covariance

### 1. Weighted Least Squares Inversion
Defining $y_i = \ln\varepsilon_i$ with uncertainty $\sigma_{y_i} = \sigma_{\varepsilon_i} / \varepsilon_i$, the weight matrix is diagonal:
$$\mathbf{W} = \text{diag}\left( \frac{1}{\sigma_{y_i}^2} \right)$$
The design matrix $\mathbf{X}$ has elements $X_{ik} = [\ln(E_i/E_0)]^k$.
The optimal polynomial parameter vector $\hat{\mathbf{a}}$ is solved via:
$$\hat{\mathbf{a}} = (\mathbf{X}^T \mathbf{W} \mathbf{X})^{-1} \mathbf{X}^T \mathbf{W} \mathbf{y}$$
The parameter covariance matrix is the inverse of the normal matrix:
$$\mathbf{V}_a = (\mathbf{X}^T \mathbf{W} \mathbf{X})^{-1}$$

### 2. Strong Negative Correlations
Adjacent polynomial coefficients exhibit strong anti-correlations:
$$\rho_{ij} = \frac{V_{a, ij}}{\sqrt{V_{a, ii} V_{a, jj}}} \sim -0.70 \text{ to } -0.99$$
When a lower-order coefficient $a_k$ fluctuates upward, the higher-order coefficient $a_{k+1}$ must adjust downward to maintain the curve through the calibration data points.

### 3. Rigorous Error Propagation vs Naive Error Fallacy
At any in-beam transition energy $E$, the Jacobian vector is $\mathbf{j}(E) = [1, \ln(E/E_0), \dots, (\ln(E/E_0))^M]^T$.
The **exact variance** of the interpolated efficiency is:
$$\sigma_{\ln\varepsilon}^2(E) = \mathbf{j}(E)^T \mathbf{V}_a \mathbf{j}(E) = \sum_{i=0}^M \sum_{j=0}^M j_i(E) j_j(E) V_{a, ij}$$
$$\sigma_\varepsilon(E) = \varepsilon(E) \cdot \sqrt{\sigma_{\ln\varepsilon}^2(E)}$$

**The Naive Error Fallacy**:
If experimentalists ignore the off-diagonal covariance elements ($V_{a, ij}$ for $i \ne j$) and simply sum the individual term variances:
$$\sigma_{\text{naive}}^2 = \sum_{k=0}^M j_k(E)^2 V_{a, kk}$$
the cancellation between anti-correlated terms is lost, causing the calculated efficiency uncertainty to be **artificially inflated by $200\% - 600\%$**!

---

## Executable Analysis Tool: `effcov`

The Python analysis suite integrates `hpge_efficiency_curve_covariance_fitter.py`, accessible via:

```bash
# Benchmark 1: Clover HPGe 152Eu calibration & query specific in-beam lines (409 keV, 638 keV)
python3 system/scripts/analysis/nuclear_analyzer.py effcov --preset clover_detector_152Eu_calibration --query-E 409,638,1332

# Benchmark 2: Broadband coaxial HPGe 133Ba + 152Eu + 60Co mixed source
python3 system/scripts/analysis/nuclear_analyzer.py effcov --preset broadband_coaxial_hpge_mixed_source --query-E 511,898,1274
```

### Benchmark Validation
1. **Clover HPGe $^{152}\text{Eu}$**:
   Fit achieves reduced $\chi^2/\text{ndf} = 0.41$ (excellent fit quality).
   At $E_\gamma = 409.0\text{ keV}$, rigorous propagated efficiency is $\varepsilon = 0.011819 \pm 0.000124$ ($1.05\%$ relative uncertainty).
   The naive variance sum yields an unphysical error $\pm 0.000742$, overestimating the uncertainty by a factor of $\times 5.99$!
2. **Consistency Across Energy Range**:
   Provides accurate efficiency interpolation and reliable $1\sigma$ error boundaries for level-scheme intensity balance calculations.
