---
type: concept
title: "In-beam Doppler Shift Attenuation Method (DSAM) ZBL universal stopping power and intrinsic level lifetime inversion"
aliases: [dsam-zbl, dsam-lifetime, zbl-stopping, blaugrund-multiple-scattering, centroid-shift-factor]
created: 2026-11-04
updated: 2026-11-04
status: ai-draft
review_status: unreviewed
tags: [in-beam-spectroscopy, dsam, lifetime, zbl-stopping, blaugrund, quadrupole-moment, 130ba, 134ce]
---

# In-beam Doppler Shift Attenuation Method (DSAM) ZBL universal stopping power and intrinsic level lifetime inversion

## Physical Principle & In-Beam Experimental Setup

In heavy-ion in-beam $\gamma$-ray spectroscopy, the Doppler Shift Attenuation Method (DSAM) is the primary technique for extracting short nuclear state lifetimes in the femtosecond-to-picosecond domain ($0.02\text{ ps} \le \tau \le 2.0\text{ ps}$), which are typical for high-spin states of rotational bands, wobbling modes, and chiral doublets.

In a typical in-beam experiment (e.g. $^{100}\text{Mo}(^{36}\text{S}, 4n)^{132}\text{Ce}$ or $^{114}\text{Cd}(^{20}\text{Ne}, 4n)^{130}\text{Ba}$), compound nucleus recoils are produced with initial recoil velocity $\beta_0 = v_0 / c \approx 0.015 - 0.035$ and injected into a thick backing medium (Au, Pb, Cu, Ta).
As the recoils slow down over a stopping time $t_{\text{stop}} \approx 1.5 - 2.5\text{ ps}$, $\gamma$-rays are emitted with Doppler-shifted energy:
$$E_\gamma(\theta, t) = E_0 \left[ 1 + \frac{v(t)}{c} \cos\theta \right]$$

The centroid Doppler shift attenuation factor $F(\tau)$ is measured at forward/backward angles:
$$F(\tau) = \frac{\Delta E_{\text{exp}}}{\Delta E_{\text{max}}} = \frac{\langle v(t) \cos\phi(t) \rangle}{v_0} = \frac{1}{v_0 \tau} \int_0^{t_{\text{stop}}} v(t) \langle \cos\phi \rangle(t) e^{-t/\tau} dt$$

---

## Pedagogical Controversy: LSS vs. ZBL Electronic Stopping

1. **吴治华《原子核物理实验方法》第 15 章 §15.3 & 卢希庭《原子核物理》第 6 章**:
   - Both classic Chinese textbooks utilize the Lindhard-Scharff-Schiøtt (LSS) theory:
     $$S_e(v) = k_{\text{LSS}} \cdot \frac{v}{v_0}$$
   - *Limitation*: LSS assumes a degenerate electron gas and treats the ion as a point charge, neglecting $Z_1, Z_2$ shell oscillations and effective charge recombination at low velocities ($v < v_{\text{Bohr}} Z_1^{2/3}$).
   - In heavy-ion stopping ($Z \sim 50-70$ in Au), LSS underestimates electronic stopping power by $15\% - 30\%$, leading to systematically overestimated stopping times and a $20\% - 30\%$ underestimation of nuclear lifetimes $\tau$ (which artificially inflates deduced $B(E2)$ values and transition quadrupole moments $Q_0$).

2. **Modern ZBL Stopping & Blaugrund Formalism**:
   - Uses parameterized universal nuclear stopping $S_n(E)$ and calibrated electronic stopping $S_e(v)$ (Ziegler, Biersack & Littmark 1985 / SRIM).
   - Accounts for nuclear multiple scattering via Blaugrund angular attenuation:
     $$\langle \cos\phi \rangle(t) = \exp\left[ - \frac{M_{\text{stopper}}}{2 M_{\text{recoil}}} \int_0^t \frac{S_n(t')}{E(t')} dt' \right]$$
   - Corrects for unobserved feeder transitions through effective side-feeding delay $\tau_{\text{sf}}$:
     $$\tau_{\text{level}} = \tau_{\text{apparent}} - \tau_{\text{sf}}$$

---

## Electromagnetic Collectivity Extraction

From the inverted intrinsic level lifetime $\tau$, the reduced transition probability $B(E2)$ and transition quadrupole moment $Q_0$ are obtained:
$$\frac{1}{\tau} = 8.508 \times 10^{12} \cdot E_\gamma^5(\text{MeV}) \cdot B(E2; I \to I-2, e^2\text{b}^2)$$
$$Q_0 = \sqrt{\frac{B(E2)}{\frac{5}{16\pi} e^2 \langle I 0 2 0 | I-2 0 \rangle^2}}$$

---

## Executable Analysis Tool: `dsamzbl`

The Python analysis suite integrates `in_beam_dsam_zbl_stopping_lifetime_inverter.py`, accessible via CLI:

```bash
# 1. 130Ba 8+ state in gold (Au) backing
python3 system/scripts/analysis/nuclear_analyzer.py dsamzbl --preset 130Ba_8plus_in_Au_backing

# 2. 134Ce 12+ high-spin state in lead (Pb) backing
python3 system/scripts/analysis/nuclear_analyzer.py dsamzbl --preset 134Ce_12plus_in_Pb_backing

# 3. 164Yb 14+ band-crossing state in copper (Cu) backing
python3 system/scripts/analysis/nuclear_analyzer.py dsamzbl --preset 164Yb_14plus_in_Cu_backing
```

---

## Literature and Textbook Provenance

- **吴治华**, 《原子核物理实验方法》 (第三版), 第 15 章 §15.3.
- **卢希庭**, 《原子核物理》 (修订版), 第 6 章 §6.4.
- **J. F. Ziegler, J. P. Biersack, U. Littmark**, *The Stopping and Range of Ions in Solids* (Pergamon 1985).
- **A. E. Blaugrund**, Nucl. Phys. 88, 501 (1966).
- **Bohr & Mottelson**, *Nuclear Structure*, Vol. I, p. 382.
