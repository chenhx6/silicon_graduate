---
type: concept
title: "In-beam charged particle Delta E - E telescope PID and Goulding power-law geometric correction"
aliases: [particle-identification, delta-e-telescope, goulding-pid, charged-particle-pid, bethe-bloch-pid]
created: 2026-11-04
updated: 2026-11-04
status: ai-draft
review_status: unreviewed
tags: [in-beam-spectroscopy, charged-particles, particle-identification, telescope, bethe-bloch, goulding]
---

# In-beam charged particle Delta E - E telescope PID and Goulding power-law geometric correction

## Physical Principle & In-Beam Reaction Channel Selection

In heavy-ion fusion-evaporation reactions, compound nuclei de-excite via competing light charged particle evaporation (protons $p$, deuterons $d$, tritons $t$, $\alpha$ particles) and neutrons ($xn$) before emitting $\gamma$-ray cascades. Identifying evaporated particles with high efficiency and purity is essential to isolate weak exotic channels (e.g., $2p, 3p, \alpha p, \alpha 2n$ leading to neutron-deficient $A \sim 130$ and $N \approx Z$ isotopes).

A $\Delta E - E$ telescope combines a thin transmission detector (thickness $T_0 \approx 50 - 150\ \mu\text{m}$) and a thick stopping detector ($T_{\text{stop}} \ge 1000\ \mu\text{m}$).
Based on Bethe-Bloch energy loss, the non-relativistic range-energy relationship is:
$$R(E) = a \cdot E^\mu$$
where $\mu \approx 1.73$ for silicon detectors, and $a \propto \frac{1}{m^{\mu-1} z^2}$.

---

## Goulding Modified Power-Law Transformation & Geometric Correction

For a particle incident at angle $\theta_{\text{inc}}$ relative to the detector surface normal, the effective transmission path length is:
$$T_{\text{eff}} = \frac{T_0}{\cos\theta_{\text{inc}}}$$

The classic Goulding Particle Identification (PID) parameter is:
$$PI = \frac{(E_{\text{tot}} + E_0)^\mu - (E_{\text{res}} + E_0)^\mu}{T_{\text{eff}}}$$
where $E_{\text{tot}} = \Delta E + E_{\text{res}}$, and $E_0 \approx 0.5 - 1.0\text{ MeV}$ compensates for pulse-height defects, plasma recombination, and low-velocity stopping deviations.

### Theoretical PID Invariant:
$$PI(m, z) \propto m^{\mu-1} z^2$$
Relative to protons ($m=1, z=1$):
- Proton ($^1\text{H}$): $PI_{\text{rel}} = 1.000$
- Deuteron ($^2\text{H}$): $PI_{\text{rel}} = 2^{0.73} = 1.659$
- Triton ($^3\text{H}$): $PI_{\text{rel}} = 3^{0.73} = 2.232$
- Helium-3 ($^3\text{He}$): $PI_{\text{rel}} = 4 \times 3^{0.73} = 8.928$
- Alpha ($^4\text{He}$): $PI_{\text{rel}} = 4 \times 4^{0.73} = 11.006$

Clean channel gating requires a Figure of Merit (FOM) between adjacent peaks:
$$FOM = \frac{|\langle PI_2 \rangle - \langle PI_1 \rangle|}{\text{FWHM}_1 + \text{FWHM}_2} \ge 1.0 - 1.2$$

---

## Executable Analysis Tool: `pidtele`

The Python analysis suite integrates `in_beam_charged_particle_pid_delta_e_telescope_inverter.py`, accessible via CLI:

```bash
# 1. Silicon Microball in-beam telescope at theta=45 deg
python3 system/scripts/analysis/nuclear_analyzer.py pidtele --preset silicon_telescope_heavy_ion_in_beam

# 2. Gas-silicon hybrid telescope
python3 system/scripts/analysis/nuclear_analyzer.py pidtele --preset gas_silicon_hybrid_telescope
```

---

## Literature and Textbook Provenance

- **吴治华**, 《原子核物理实验方法》 (第三版), 第 4 章 §4.4 (pp. 95–110).
- **汪晓莲, 李澄, 绍明, 陈宏芳**, 《粒子探测技术》, 第 3 章 §3.2 (pp. 75–95).
- **K. Heyde**, *Basic Ideas and Concepts in Nuclear Physics* (3rd Ed.), Chapter 4.
- **F. S. Goulding & B. G. Harvey**, Ann. Rev. Nucl. Sci. 25, 167 (1975).
