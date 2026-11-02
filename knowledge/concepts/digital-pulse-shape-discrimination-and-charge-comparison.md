---
type: concept
title: "Digital pulse shape discrimination (PSD), charge comparison and neutron-gamma FOM"
aliases: [digital-psd, charge-comparison-method, ccm-psd, neutron-gamma-discrimination, figure-of-merit-fom]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [detector-physics, digital-signal-processing, organic-scintillators, pulse-shape-discrimination, charge-comparison, figure-of-merit, neutron-detection]
---

# Digital pulse shape discrimination (PSD), charge comparison and neutron-gamma FOM

## Physical Origin: Scintillation Decay and Ionization Density ($dE/dx$)

In experimental in-beam $\gamma$-ray spectroscopy and reaction channel selection (e.g. discriminating prompt evaporation neutrons from $\gamma$-rays in liquid scintillators like BC-501A, EJ-301, or organic crystals like Stilbene), particle identification relies on the **linear energy transfer ($dE/dx$) dependence of fluorescence decay**:

Based on Nakhostin《辐射探测器信号处理》第 4 章 (pp. 110–145), 汪晓莲等《粒子探测技术》第 4, 8 章, and G. F. Knoll (Radiation Detection and Measurement, Ch. 8, 15):

1. **Double Exponential Scintillation Decay**:
   The light pulse consists of a finite rise time and two fluorescence decay channels:
   $$v(t) = V_0 \left[ 1 - e^{-t / \tau_{\text{rise}}} \right] \left[ (1 - f_{\text{slow}}) e^{-t / \tau_{\text{fast}}} + f_{\text{slow}} e^{-t / \tau_{\text{slow}}} \right]$$
   - **Fast Component ($\tau_{\text{fast}} \approx 3.2\text{ ns}$)**: Prompt radiative transition from excited singlet states ($S_1 \to S_0$);
   - **Slow Component ($\tau_{\text{slow}} \approx 200 - 300\text{ ns}$)**: Delayed emission originating from the annihilation collision of two mobile triplet molecules ($T_1 + T_1 \to S_1^* + S_0 \to \gamma + S_0$).

2. **$dE/dx$ Discrimination**:
   - **Gamma Rays (Compton electrons, low $dE/dx$)**: Low local ionization density suppresses triplet-triplet encounters, resulting in a small slow fraction ($f_{\text{slow}} \approx 8\% - 15\%$);
   - **Fast Neutrons (Recoil protons, high $dE/dx$)**: Dense ionization track produces dense triplet populations, resulting in a significantly enhanced slow tail ($f_{\text{slow}} \approx 28\% - 38\%$).

---

## Digital Charge Comparison Method (CCM)

For a digitized waveform $v_i$ sampled at clock period $\Delta t$:
1. **Short-Gate Integration**:
   $$Q_{\text{short}} = \sum_{i=0}^{N_{\text{short}}} v_i \Delta t \quad (T_{\text{short}} \approx 15 - 30\text{ ns})$$
   capturing predominantly the prompt fast peak.
2. **Long-Gate Integration**:
   $$Q_{\text{long}} = \sum_{i=0}^{N_{\text{long}}} v_i \Delta t \quad (T_{\text{long}} \approx 300 - 450\text{ ns})$$
   integrating the total emitted scintillation charge.
3. **PSD Parameter Definition**:
   $$\text{PSD} = \frac{Q_{\text{tail}}}{Q_{\text{long}}} = \frac{Q_{\text{long}} - Q_{\text{short}}}{Q_{\text{long}}} = 1.0 - \frac{Q_{\text{short}}}{Q_{\text{long}}}$$

---

## Figure of Merit (FOM) and Gate Optimization

### 1. Optimal Short-Gate Width
The separation distance $\Delta\text{PSD}(T_{\text{short}}) = \text{PSD}_n - \text{PSD}_\gamma$ peaks sharply when $T_{\text{short}}$ coincides with the point where the fast singlet component has decayed to $< 1\%$ of its initial value ($\sim 4 \tau_{\text{fast}} \approx 15 - 20\text{ ns}$).

### 2. Figure of Merit (FOM)
The experimental discrimination quality is defined by the peak separation divided by the sum of full-widths at half-maximum:
$$\text{FOM} = \frac{|\mu_n - \mu_\gamma|}{\text{FWHM}_n + \text{FWHM}_\gamma} = \frac{|\mu_n - \mu_\gamma|}{2.355(\sigma_n + \sigma_\gamma)}$$
- $\text{FOM} < 1.0$: Inadequate discrimination, severe neutron/$\gamma$ spillover;
- $\text{FOM} \ge 1.27$: Standard $3\sigma$ Gaussian separation ($> 99.7\%$ purity);
- $\text{FOM} \ge 1.50$: Excellent, contamination-free in-beam particle identification.

### 3. Light Output Energy Threshold Systematics
Because photon detection follows Poisson photoelectron statistics, pulse-to-pulse variance scales as $\sigma \propto 1 / \sqrt{E_{ee}}$:
$$\text{FOM}(E_{ee}) = \text{FOM}_0 \sqrt{\frac{E_{ee}}{E_0}}$$
At low electron-equivalent energies ($E_{ee} \le 100\text{ keVee}$), Poisson fluctuations broaden both peaks, necessitating higher discrimination thresholds or digital pulse-fitting deconvolution.

---

## Canonical Experimental Benchmarks

- **EJ-301 / BC-501A Liquid Scintillator**:
  - $\tau_{\text{rise}} = 1.5\text{ ns}, \tau_{\text{fast}} = 3.2\text{ ns}, \tau_{\text{slow}} = 270.0\text{ ns}$, $f_{\text{slow},\gamma} = 12\%, f_{\text{slow},n} = 32\%$;
  - Optimal $T_{\text{short}} = 15.0\text{ ns}$ with $T_{\text{long}} = 350.0\text{ ns}$;
  - $\text{FOM} = 1.45$ at $500\text{ keVee}$ ($> 3\sigma$ separation), increasing to $2.25$ at $1.2\text{ MeVee}$.
- **Stilbene Crystal**:
  - High light yield yields $\text{FOM} = 1.75$ at $500\text{ keVee}$ and excellent separation down to $200\text{ keVee}$.

---

## Primary Source References

- **Nakhostin, M.**: *Signal Processing for Radiation Detectors*, John Wiley & Sons (2017) / 科学出版社中译本, Chapter 4 (Digital Pulse Processing & Particle Identification), pp. 110–145.
- **Wang Xiaolian (汪晓莲) et al.**: *Particle Detection Technology* (《粒子探测技术》), USTC Press (2009), Chapters 4 & 8.
- **Knoll, G. F.**: *Radiation Detection and Measurement*, 4th ed., John Wiley & Sons (2010), Chapters 8 & 15.
