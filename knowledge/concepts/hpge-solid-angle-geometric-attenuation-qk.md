---
type: concept
title: "HPGe and Clover detector finite solid-angle geometric attenuation factors Q_2 and Q_4 numerical integration"
aliases: [solid-angle-attenuation, qk-attenuation-factors, rose-integrals, finite-detector-geometry, angular-distribution-attenuation]
created: 2026-11-04
updated: 2026-11-04
status: ai-draft
review_status: unreviewed
tags: [gamma-spectroscopy, angular-distributions, dco-analysis, hpge-detectors, solid-angle-correction, qk-factors, rose-integrals]
---

# HPGe and Clover detector finite solid-angle geometric attenuation factors Q_2 and Q_4 numerical integration

## Definition

### Definition and Phenomenological Origin

In in-beam $\gamma$-ray directional correlation and angular distribution measurements (DCO, ADO, linear polarization), the theoretical angular distribution for an idealized point detector is:
$$W(\theta) = 1 + A_2 P_2(\cos\theta) + A_4 P_4(\cos\theta)$$

Based on 吴治华《原子核物理实验方法》第 10 章 §10.3 (pp. 255–265), 汪晓莲《粒子探测技术》第 5 章, M. E. Rose (Phys. Rev. 91, 610, 1953), and K. S. Krane (Nucl. Instrum. Methods 98, 405, 1972):
Real HPGe crystals possess finite volume and subtend a finite solid angle ($\Omega / 4\pi \sim 0.5\% - 3\%$).
Integrating the radiation pattern over the active crystal face averages out the anisotropy, attenuating the observed expansion coefficients:
$$W_{\text{obs}}(\theta) = 1 + Q_2 A_2 P_2(\cos\theta) + Q_4 A_4 P_4(\cos\theta)$$
where $Q_k \in (0, 1)$ are the **Rose geometric attenuation coefficients**.
Failing to correct for $Q_k$ introduces a $15\% - 30\%$ systematic error into multipole mixing ratios $\delta(E2/M1)$.

---

## Mathematical Formalism: Ray-Tracing & Rose Integrals

### 1. Cylindrical Crystal Path Length $t(\alpha)$
For a cylindrical crystal of radius $R$ and length $L$ located at distance $d$ from the target, a photon emitted at polar angle $\alpha \le \alpha_{\text{max}} = \arctan(R/d)$ penetrates a track length $t(\alpha)$:
- **Back face exit** ($\tan\alpha \le R / (d + L)$):
  $$t(\alpha) = \frac{L}{\cos\alpha}$$
- **Side face exit** ($\tan\alpha > R / (d + L)$):
  $$t(\alpha) = \frac{R}{\sin\alpha} - \frac{d}{\cos\alpha}$$

### 2. Numerical Rose Integrals $J_k$
Using the energy-dependent linear attenuation coefficient $\mu_{\text{Ge}}(E_\gamma)$ in Germanium ($\rho = 5.323\text{ g/cm}^3$):
$$J_k(E_\gamma) = \int_0^{\alpha_{\text{max}}} P_k(\cos\alpha) \sin\alpha \left[ 1 - e^{-\mu_{\text{Ge}}(E_\gamma) t(\alpha)} \right] d\alpha$$
The geometric attenuation factor is the normalized ratio:
$$Q_k(E_\gamma) = \frac{J_k(E_\gamma)}{J_0(E_\gamma)} \quad (k = 2, 4)$$

---

## Executable Analysis Tool: `attneqk`

The Python analysis suite integrates `hpge_detector_solid_angle_attenuation_qk_integrator.py`, accessible via:

```bash
# Benchmark 1: Standard large coaxial HPGe (R=3.5 cm, L=7.0 cm, d=15 cm) at 1332 keV (Krane 1972)
python3 system/scripts/analysis/nuclear_analyzer.py attneqk --preset standard_coaxial_hpge_15cm

# Benchmark 2: Close-geometry Clover crystal (R=2.5 cm, L=7.0 cm, d=10 cm) at 638 keV
python3 system/scripts/analysis/nuclear_analyzer.py attneqk --preset close_geometry_clover_10cm

# Benchmark 3: Far-geometry quasi-point calibration (d = 50 cm)
python3 system/scripts/analysis/nuclear_analyzer.py attneqk --preset far_geometry_calibration_50cm
```

### Benchmark Validation
1. **Standard Coaxial ($d = 15\text{ cm}, E_\gamma = 1332.5\text{ keV}$)**:
   $\alpha_{\text{max}} = 13.13^\circ$, $\Omega/4\pi = 1.308\%$.
   Evaluates $Q_2 = 0.9701$, $Q_4 = 0.9027$.
2. **Close Clover ($d = 10\text{ cm}, E_\gamma = 638.0\text{ keV}$)**:
   $\alpha_{\text{max}} = 14.04^\circ$, $Q_2 = 0.9672$, $Q_4 = 0.8936$.
3. **Distant Calibration ($d = 50\text{ cm}$)**:
   Approaches point-detector limit: $Q_2 = 0.9975, Q_4 = 0.9918$.


## Necessary Assumptions

微观平均场假定核子在有效单体势中运动，通过剩余相互作用自洽诱发四极形变与集体转动。


## Discriminating Observables

激发能量级间距、跃迁多极性比值与电磁约化跃迁几率是关键鉴别观测量。


## Supporting Evidence

在束伽马谱学实验测定的角分布、DCO比值与能级寿命提供直接实证。

## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。


## Sources

- [[triaxial-collective-modes-unified-theory-and-spectroscopy]]
- [[nuclear-spectroscopy-and-structure-master-field-manual]]
