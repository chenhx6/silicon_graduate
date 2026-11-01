---
type: research-note
title: "131Ce and 133Ce unified triaxial collective modes, Fermi surface evolution, and isotone systematics"
aliases: [131Ce 133Ce unified collective modes, Ce odd-A triaxial evolution, N=75 isotone systematics]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [
  alwaleedi-2013-band-structures-131ce,
  wakudyanaye-2022-triaxiality-rotational-bands-133ce,
  ding-2021-131ba-133ce-signature-splitting,
  userdata-133ce-southafrica-dataset,
  nuclearmap-jcnp-pc-pk1
]
created_from: "Candidate 6 post-30-day paper prospectus investigation"
promotion_target: "post-30-day-nuclear-structure-paper-prospectus"
scope: odd-A-cerium/triaxial-collective-modes/fermi-surface-shift/isotone-chain
nuclei: [131ce, 133ce, 132ce, 134ce, 131ba, 135nd]
observables: [routhian, alignment, signature-splitting, signature-inversion, mixing-ratio, be2-ratio, bm1-ratio, triaxiality-gamma]
tags: [131ce, 133ce, triaxiality, collective-modes, signature-partner, wobbling-falsification, gamma-vibration, tilted-precession, isotone-systematics]
---

# `131Ce` and `133Ce` unified triaxial collective modes, Fermi surface evolution, and isotone systematics

## Executive Summary & Research Context

This research note completes the scientific synthesis for **Candidate 6** of the post-30-day research prospectus: *“131Ce/133Ce collective-mode identifiability: Differentiating unfavored signature partner, wobbling, tilted precession, and $\gamma$-vibrational coupling in odd-$A$ Ce isotopes.”*

By integrating the CIAE HI-13 beam experiment on $^{131}\text{Ce}$ ($N=73$, [[alwaleedi-2013-band-structures-131ce]]), the iThemba LABS PR295 experiment on $^{133}\text{Ce}$ ($N=75$, [[wakudyanaye-2022-triaxiality-rotational-bands-133ce]], Ding Bing et al. 2022 [[ding-2021-131ba-133ce-signature-splitting]], and the private workbook layer [[userdata-133ce-southafrica-dataset]]), and microscopic covariant density functional theory priors from NuclearMap ([[nuclearmap-jcnp-pc-pk1]]), we resolve the structural evolution across the $N=74$ triaxial core $^{132}\text{Ce}$ ($\beta_2 \approx 0.22\text{--}0.24, \gamma \approx 17^\circ\text{--}20^\circ$).

### Key Scientific Conclusions
1. **Microscopic Fermi Surface Shift ($N=73 \to N=75$)**:
   - In $^{131}\text{Ce}$ ($N=73$), the neutron Fermi level resides in the lower-middle $\nu h_{11/2}$ subshell near $[523]7/2^-$. Band 4 is established as a **$\gamma$-vibrational phonon coupled to the $\nu h_{11/2}$ quasiparticle** ($\gamma \otimes e$), with bandhead $I^\pi = 15/2^-$ at $972\text{ keV}$ above the $9/2^-$ isomer, decaying via high-energy linking transitions ($994, 1108\text{ keV}$).
   - In $^{133}\text{Ce}$ ($N=75$), adding two neutrons pushes the Fermi level to the top of the $\nu h_{11/2}$ shell (orbitals $[514]9/2^-$ and $[505]11/2^-$). The valence hole exerts an oblate-driving shape polarization competing against the prolate-driving core protons, stabilizing triaxiality ($\gamma \approx 18^\circ$). Band 4 is an **unfavored signature partner** possessing a $2\hbar$ long-axis rotation component (tilted precession, TiP), with bandhead $I^\pi = 13/2^-$ at $512\text{ keV}$, decaying via low-energy transitions ($465, 582, 625\text{ keV}$).
2. **Definitive Falsification of Wobbling in $^{133}\text{Ce}$**:
   - Reconstructing the transition-level apparent wobbling frequency formula $\hbar\omega_w = E_{\gamma,\text{out}} - \frac{1}{2}E_{\gamma,\text{in}}$ reveals massive signature staggering ($>300\text{ keV}$) and drops into unphysical negative territory ($-84.5\text{ keV}$ at $23/2^-$ and $-15.5\text{ keV}$ at $27/2^-$).
   - The connecting transitions are strictly $M1$-dominated: $582\text{ keV}$ ($17/2^- \to 15/2^-$) has $\delta = -0.55$, $M1\% = 76.8\%$, $B(E2)_{\text{out}}/B(E2)_{\text{in}} = 0.063(25)$; $465\text{ keV}$ ($19/2^- \to 17/2^-$) has $\delta = -0.17$, $M1\% = 97.2\%$, $B(E2)_{\text{out}}/B(E2)_{\text{in}} = 0.088(33)$. Both $B(E2)_{\text{out}}/B(E2)_{\text{in}}$ values are $< 0.1$, strictly excluding wobbling ($B(E2)_{\text{out}}/B(E2)_{\text{in}} \sim 0.2\text{--}0.5$).
3. **Common Microscopic Proton Backbend**:
   - Both $^{131}\text{Ce}$ and $^{133}\text{Ce}$ exhibit an identical, sharp band crossing at rotational frequency $\omega_c \approx 0.30\text{--}0.32\text{ MeV}/\hbar$ with alignment gain $\Delta i_x \approx 8.8\text{--}9.0\hbar$, corresponding to the alignment of the first pair of $h_{11/2}$ protons ($(\pi h_{11/2})^2$ $S$-band crossing).
4. **$N=75$ Isotone Chain Systematics ($^{131}\text{Ba} \to {}^{133}\text{Ce} \to {}^{135}\text{Nd}$)**:
   - Triaxiality evolves smoothly from $\gamma$-soft ($^{131}\text{Ba}$, $\gamma \approx 10^\circ\text{--}12^\circ$) to rigid triaxial ($^{133}\text{Ce}$, $\gamma \approx 18^\circ$) to rigid chiral triaxiality ($^{135}\text{Nd}$, $\gamma \approx 21^\circ$), driven by proton addition into the $\pi h_{11/2}$ orbital.

---

## Microscopic Configuration & Nilsson Orbitals

The negative-parity single-neutron orbitals close to the Fermi level in $A \approx 130$ at triaxial quadrupole deformation ($\varepsilon_2 \approx 0.185, \gamma \approx 18^\circ$) are given by the QTR model Hamiltonian (Wakudyanaye 2022, Table 6.6):

| State $| \nu \rangle$ | Nilsson Asymptotic Label $\Omega^\pi [N n_z \Lambda]$ | Single-Particle Energy $\varepsilon$ (MeV) | Main Long-Axis Projections $\Omega_l$ |
|---|---|---|---|
| $|14\rangle$ | $1/2^- [550]$ | 5.657 | $0.783 |11/2, 1/2\rangle + 0.512 |11/2, -1/2\rangle$ |
| $|15\rangle$ | $3/2^- [541]$ | 5.743 | $0.772 |11/2, 3/2\rangle - 0.404 |11/2, -1/2\rangle$ |
| $|16\rangle$ | $5/2^- [532]$ | 5.808 | $-0.864 |11/2, 5/2\rangle + 0.360 |11/2, 1/2\rangle$ |
| $|17\rangle$ | $7/2^- [523]$ | 5.901 | $-0.955 |11/2, 7/2\rangle + 0.192 |11/2, -3/2\rangle$ |
| $|18\rangle$ | $9/2^- [514]$ | 6.036 | $0.981 |11/2, 9/2\rangle - 0.149 |7/2, 5/2\rangle$ |
| $|19\rangle$ | $11/2^- [505]$ | 6.212 | $0.986 |11/2, 11/2\rangle - 0.155 |7/2, -7/2\rangle$ |

### Structural Consequences of the Fermi Level Position:
- In $^{131}\text{Ce}$ ($N=73$), the chemical potential $\lambda$ lies near $|17\rangle$ ($[523]7/2^-$). The valence neutron is situated in the mid-shell where Coriolis decoupling is moderate. The $\gamma$-soft core couples preferentially via vibrational phonons, generating Band 4 as a collective $\gamma$-vibration ($\gamma \otimes e$).
- In $^{133}\text{Ce}$ ($N=75$), two neutrons are added, placing $\lambda$ directly at $|18\rangle$ ($[514]9/2^-$) and $|19\rangle$ ($[505]11/2^-$). The state has $96\%$ pure $h_{11/2}$ character with $\Omega_l = 9/2$. At the top of the shell, the hole-like quasiparticle aligns along the long nuclear axis, while triaxial rotor rotation introduces $\Delta K = \pm 2$ mixing with $|16\rangle$ ($5/2^-$) and $|14\rangle$ ($1/2^-$), causing extreme Coriolis staggering and signature inversion.

---

## Quantitative Comparative Matrix: $^{131}\text{Ce}$ vs $^{133}\text{Ce}$

The spectroscopic parameters synthesized by `system/scripts/ce131_ce133_unified_collective_modes.py` provide a direct head-to-head comparison:

| Observable / Property | $^{131}\text{Ce}$ ($N=73$, Alwaleedi 2013) | $^{133}\text{Ce}$ ($N=75$, Wakudyanaye 2022 / PR295) | Physical Interpretation |
|---|---|---|---|
| **Yrast Bandhead** | $9/2^-$ isomer ($T_{1/2} = 80\text{ ns}$) | $9/2^-$ ($E_x = 37.2\text{ keV}$) | High-$j$ $\nu h_{11/2}$ bandhead |
| **Excited Band (Band 4) Bandhead** | $15/2^-$ ($E_x = 972\text{ keV}$ above $9/2^-$) | $13/2^-$ ($E_x = 512\text{ keV}$ above $9/2^-$) | $\Delta I = 3$ ($\gamma$-vibration) vs $\Delta I = 2$ ($R_l = 2\hbar$ TiP) |
| **Connecting Transitions** | $994\text{ keV}, 1108\text{ keV}$ | $625\text{ keV}, 582\text{ keV}, 465\text{ keV}$ | High energy (phonon) vs low energy (signature partner) |
| **Connecting Multipolarity** | Quadrupole / Dipole mixed | $77\%\text{--}97\%\ M1$ ($|\delta| \le 0.55$) | Single-particle spin flip vs collective phonon |
| **$B(E2)_{\text{out}}/B(E2)_{\text{in}}$** | Not directly reported (weak branch) | $0.063(25)$ ($582\text{ keV}$), $0.088(33)$ ($465\text{ keV}$) | Definitively $< 0.1$, refuting wobbling |
| **$B(M1)/B(E2)$ ratio** | Small (intraband dominant) | $0.254\ \mu_N^2/(e^2 b^2)$, $0.470\ \mu_N^2/(e^2 b^2)$ | Large single-particle magnetic dipole strength |
| **Signature Staggering $S(I)$** | Small at low spin ($\pm 5\text{ keV}$) | Huge staggering ($>100\text{ keV}$), inverts at $19/2^-\text{--}21/2^-$ | Non-axial Coriolis mixing with $\Omega=1/2$ components |
| **Proton Crossing $\omega_c$** | $0.30\text{ MeV}/\hbar$ ($\Delta i_x = 9.0\hbar$) | $0.32\text{ MeV}/\hbar$ ($\Delta i_x = 8.8\hbar$) | Common $(\pi h_{11/2})^2$ $S$-band alignment |
| **Apparent $\hbar\omega_w$ behavior** | Decreases smoothly ($289 \to 43\text{ keV}$) | Staggers by $>300\text{ keV}$, plunges to $-84.5, -15.5\text{ keV}$ | Non-wobbling signature partner collapse |

---

## $N=75$ Isotone Chain Systematics ($^{131}\text{Ba} \to {}^{133}\text{Ce} \to {}^{135}\text{Nd}$)

The $N=75$ isotone chain represents a prime laboratory for studying the onset of stable nuclear triaxiality:

```
Proton Number Z:   Z = 56 (131Ba)  ------>  Z = 58 (133Ce)  ------>  Z = 60 (135Nd)
Core Non-axiality: gamma ~ 10-12 deg        gamma ~ 18 deg           gamma ~ 21 deg
Core Rigidity:     gamma-soft rotor         stable triaxial core     rigid triaxial rotor
Collective Modes:  Coriolis signature       Tilted precession (TiP)  Chiral doublet bands
                   splitting in g7/2, h11/2  + signature partner      (pi h11/2 x nu h11/2^-1)
```

1. **$^{131}\text{Ba}$ ($Z=56$)**:
   The two valence protons above the $Z=50$ shell closure occupy the $\pi g_{7/2}/\pi d_{5/2}$ orbitals. The core is relatively $\gamma$-soft ($\gamma \approx 10^\circ\text{--}12^\circ, \varepsilon_2 \approx 0.170$). The positive-parity band built on $\nu g_{7/2}[404]7/2^+$ shows moderate signature splitting driven by Coriolis mixing with nearby $\nu s_{1/2}$ and $\nu d_{3/2}$ orbitals.
2. **$^{133}\text{Ce}$ ($Z=58$)**:
   With four valence protons, protons begin to enter the deformation-driving $\pi h_{11/2}$ subshell. The potential energy surface develops a well-defined triaxial minimum at $\beta_2 \approx 0.22, \gamma \approx 18^\circ$ (NuclearMap PC-PK1). The combination of high triaxiality and the top-of-shell $\nu h_{11/2}[514]9/2^-$ hole produces large signature splitting and signature inversion at $I = 19/2^-\text{--}21/2^-$.
3. **$^{135}\text{Nd}$ ($Z=60$)**:
   With six valence protons, the $\pi h_{11/2}$ shell is substantially populated, driving the triaxial core to $\gamma \approx 21^\circ, \beta_2 \approx 0.20$. At moderate spin, coupling the active valence proton in $\pi h_{11/2}$ with the valence neutron hole in $\nu h_{11/2}^{-1}$ and the collective core rotation creates mutually orthogonal angular momentum vectors, leading to chiral doublet bands (Mukhopadhyay 2007, Lv 2019).

---

## Falsifier Verification & Stopping Criteria Audit

- **Falsifier 1 (Wobbling Multipolarity)**: The connecting lines $582\text{ keV}$ and $465\text{ keV}$ exhibit $|\delta| \le 0.55$, $M1\% \ge 76.8\%$, and $B(E2)_{\text{out}}/B(E2)_{\text{in}} < 0.10$. This conclusively falsifies the single-phonon transverse wobbling hypothesis ($|\delta| > 1, B(E2)_{\text{out}}/B(E2)_{\text{in}} \ge 0.2$).
- **Falsifier 2 (Wobbling Frequency Staggering & Negativity)**: The workbook frequency $\hbar\omega_w = E_{\gamma,\text{out}} - \frac{1}{2}E_{\gamma,\text{in}}$ exhibits signature staggering exceeding $300\text{ keV}$ and plunges to $-84.5\text{ keV}$ ($23/2^-$) and $-15.5\text{ keV}$ ($27/2^-$), which is impossible for harmonic rotor wobbling.
- **Stopping Condition**: Without event-level raw ROOT matrix deconvolution or direct microscopic PES calculations for $^{133}\text{Ce}$, this note maintains `status: ai-draft` and `reasoning_status: provisional`, preserving strict epistemic boundaries.

---

## Artifact & Reproducibility Record
- Synthesis script: `system/scripts/ce131_ce133_unified_collective_modes.py`
- Executable JSON artifact: `outputs/l3/ce-collective-modes/ce131_ce133_collective_modes_synthesis.json`
- Passing audit checks:
  * `check1_133ce_M1_dominant_and_BE2_under_0_1`: **PASS**
  * `check2_apparent_wobbling_formula_collapses`: **PASS**
  * `check3_proton_crossing_aligned_across_isotopes`: **PASS**
