---
type: concept
title: "Nuclear seniority scheme, fractional parentage B(E2) cancellation and half-filled shell isomers"
aliases: [seniority-scheme-isomers, half-filled-shell-cancellation, seniority-quantum-number, racah-seniority-b-e2]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [shell-model, seniority-scheme, high-j-orbitals, nuclear-isomers, b-e2-cancellation, half-filled-shell, fractional-parentage]
---

# Nuclear seniority scheme, fractional parentage B(E2) cancellation and half-filled shell isomers

## Definition

In spherical and near-spherical nuclei with identical valence nucleons in a single high-$j$ shell ($j \ge 7/2$, such as $1g_{9/2}, 1h_{11/2}, 1i_{13/2}$), the short-range nuclear attractive force is dominated by the pairing interaction. Giulio Racah (1943) introduced the **Seniority Quantum Number ($v$)** to classify many-particle wave functions:
- $v$ represents the number of nucleons that are not coupled into $J=0$ paired states.
- For an even number of nucleons $n$ in a $j^n$ configuration:
  * Ground state has $v = 0$ ($J = 0^+$);
  * Lowest excited states have seniority $v = 2$, with even total angular momenta $J = 2, 4, 6, \dots, (2j - 1)$.

Using fractional parentage coefficients and second quantization (Bohr & Mottelson Vol. I §3-4; Heyde Ch. 8), the reduced electric quadrupole transition probability $B(E2)$ between states belonging to the **same seniority** ($v \to v$, $\Delta v = 0$) scales with particle number $n$ as:
$$B(E2; j^n, v, J \to v, J') = \left[ \frac{2j + 1 - 2n}{2j + 1 - 2v} \right]^2 B(E2; j^v, v, J \to v, J')$$
Notice the linear parentage factor:
$$F_{\text{seniority}}(j, n) = \frac{2j + 1 - 2n}{2j + 1 - 2v}$$
When the high-$j$ shell is exactly **half-filled**:
$$n_{\text{half}} = \frac{2j + 1}{2} = j + \frac{1}{2}$$
(e.g. $n = 6$ for $h_{11/2}$, $n = 5$ for $g_{9/2}$, $n = 7$ for $i_{13/2}$), the numerator vanishes identically:
$$F_{\text{seniority}}(j, n_{\text{half}}) \equiv 0 \implies B(E2; j^{n_{\text{half}}}, v=2 \to v=2) \equiv 0.0$$
Because the dominant collective $E2$ de-excitation channel is canceled by particle-hole symmetry, the highest-spin state of the $v=2$ multiplet ($J_{\text{max}} = 2j - 1$) cannot decay rapidly. Its electromagnetic transition rate drops by orders of magnitude, generating a **Seniority Isomer** with half-life reaching microseconds, milliseconds, or longer.

## Necessary Assumptions

1. **Pure Single-$j$ Shell Occupancy**: Valence nucleons occupy a unique-parity high-$j$ shell, well separated from neighboring orbital subshells by the spin-orbit splitting.
2. **Pairing-Dominated Effective Interaction**: Two-body matrix elements preserve seniority as a good quantum number (pure Surface Delta Interaction or short-range pairing force).
3. **$\Delta v = 0$ Transition Selection**: The de-exciting transition occurs between states of the same seniority ($v=2 \to v=2$); transitions that break or change pairs ($\Delta v = 2$) are governed by different operator matrix elements.

## Discriminating Observables

1. **Parabolic U-Shaped $B(E2)$ Scaling**:
   Across an isotopic or isotonic chain filling a single $j$-shell, the $B(E2; J \to J-2)$ transition probability exhibits a characteristic parabolic dependence on particle number $n$:
   $$B(E2) \propto (2j + 1 - 2n)^2$$
   Maximum at 2 particles ($n=2$) and 2 holes ($n=2j-1$), dropping to a sharp minimum at mid-shell ($n = j + 1/2$).
2. **Isomer Half-Life Peak at Mid-Shell**:
   The half-life of the $J = 2j - 1$ state reaches a dramatic maximum at mid-shell, where experimental hindrance factors $HF = T_{1/2}(n) / T_{1/2}(n=2)$ exceed $10^2 - 10^5$.
3. **Particle-Hole Symmetry**:
   Configurations with $n$ particles and $(2j+1-n)$ holes possess identical $B(E2)$ transition rates and seniority level energy spacings.

## Supporting Evidence

1. **Tin Region $1h_{11/2}$ Seniority Isomers ($j = 11/2$, Shell Capacity 12)**:
   - For $h_{11/2}$, $n_{\text{half}} = 6$ neutrons ($^{122}\text{Sn}$).
   - In $^{130}\text{Sn}$ ($n=10$, 2 holes in $h_{11/2}$): $10^+$ isomer at $2434\text{ keV}$ decays via $65\text{ keV}$ $E2$ transition with $T_{1/2} = 1.61\ \mu\text{s}$.
   - In $^{134}\text{Te}$ ($n=2$, 2 protons in $h_{11/2}$ outside $Z=50$): $6^+$ isomer at $2391\text{ keV}$ ($T_{1/2} = 164\text{ ns}$).
   - As $n \to 6$, the $B(E2; 10^+ \to 8^+)$ strength drops toward zero, confirming the $(12 - 2n)^2$ cancellation.
2. **Lead Region $1h_{9/2}$ Seniority Isomers ($j = 9/2$, Capacity 10)**:
   - In $^{210}\text{Po}$ ($Z=84, N=126$, 2 valence protons in $h_{9/2}$): $8^+$ state at $1557\text{ keV}$ decays via $84\text{ keV}$ $E2$ transition ($8^+ \to 6^+$) with $T_{1/2} = 110\text{ ns}$.
3. **$N=50$ Region $1g_{9/2}$ Seniority Isomers ($j = 9/2$, Capacity 10)**:
   - In $^{94}\text{Ru}$ ($Z=44, N=50$, 4 proton holes in $g_{9/2}$): $8^+$ isomer at $2644\text{ keV}$ has $T_{1/2} = 71\ \mu\text{s}$, driven by the $(10 - 2n)^2 = (10 - 8)^2 = 4$ reduction.

## Counter-evidence and Competing Interpretations

1. **Core Polarization & Finite Residual $B(E2)$**:
   In actual nuclei, experimental $B(E2)$ values at mid-shell do not vanish to absolute zero (typically residual $B(E2) \sim 0.01 - 0.1\text{ W.u.}$). As discussed in Bohr & Mottelson Vol. I §3-4, this residual collectivity arises from core polarization (effective nucleon charges $e_{\text{eff}} = e_p + \delta e$) and configuration mixing with neighboring subshells ($s_{1/2}, d_{3/2}, d_{5/2}$) that slightly break pure seniority $v=2$.
2. **Shape Coexistence vs Seniority Traps**:
   Not all high-spin isomers are seniority isomers; shape isomers (superdeformed secondary minima) and $K$-isomers (axial deformation selection rules $\Delta K > \lambda$) occur through different symmetry mechanisms. Seniority isomers are uniquely identified by spherical shell-model orbitals and characteristic $(2j+1-2n)^2$ parabolae.

## Our Current Position

In this wiki, seniority scheme energy multiplets, fractional parentage $B(E2)$ scaling, half-filled shell cancellations, and isomer hindrance factors are calculated using Module 102 (`seniority_scheme_half_filled_isomer_calculator.py`, CLI subcommand `seniority`). The suite verifies exact single-$j$ cancellation at $n = j + 1/2$ and evaluates realistic Weisskopf hindrance factors across $1g_{9/2}, 1h_{11/2}, 1h_{9/2}, 1i_{13/2}$ subshells.

## Sources

- [[book-bohr-mottelson-nuclear-structure]]: A. Bohr and B. R. Mottelson, *Nuclear Structure*, Vol. I, §3-4 (pp. 314–332).
- [[book-jain-nuclear-isomers]]: A. K. Jain, B. Maheshwari, A. Goel, *Nuclear Isomers: A Primer*, Springer (2021), Ch. 3 & Ch. 5.
- [[book-heyde-nuclear-physics-concepts]]: K. L. G. Heyde, *Basic Ideas and Concepts in Nuclear Physics*, Ch. 8 (The Nuclear Shell Model).
- Racah, G., *Theory of Complex Spectra. III*, Phys. Rev. 63, 367 (1943).
