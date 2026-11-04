---
name: bohr-mottelson-nuclear-structure
description: "A. Bohr & B. R. Mottelson, Nuclear Structure (Vols. I & II): foundational quantum nuclear-structure principles, time-reversal invariance, single-particle motion, deformed shell model, rotational and vibrational spectra, Coriolis decoupling, and transition sum rules."
---

<!-- argument-hint: [topic, framework, observable, or volume/chapter number] -->

# Nuclear Structure (A. Bohr & B. R. Mottelson, Vols. I & II)

**Authors**: Aage Bohr and Ben R. Mottelson | **Publisher**: W. A. Benjamin, Inc. (1969, 1975) / World Scientific
**Source PDFs**:
- Vol. I: `raw/books/nuclear structure Ⅰ_Bohr, Mottelson.pdf` (SHA-256 `a31a158e0aff2ec6734d46f5aea5eb42dbebb82280835774f49350dd6f8c79df`)
- Vol. II: `raw/books/nuclear structure Ⅱ_Bohr, Mottelson.pdf` (SHA-256 `46015a1401bcbdd40d4fd7267a1b066b4aef662050dcf35693e4e3a10a6d417a`)

This project-local skill turns Bohr and Mottelson's monumental two-volume masterpiece into an active, on-demand reasoning engine and reference toolkit for nuclear structure research.

## How to Use This Skill

- **Without arguments**: Load the core frameworks, mental models, and chapter indices.
- **By topic**: Ask about `time-reversal`, `Kramers degeneracy`, `Nilsson asymptotic quantum numbers`, `Alaga rules`, `Mikhailov plot`, `Coriolis decoupling`, `incompressibility`, or `gK - gR extraction`; loads the relevant chapter cards and primary equations.
- **By chapter**: Ask for `vol1-ch01`, `vol1-ch02`, `vol1-ch03`, `vol2-ch04`, `vol2-ch05`, or `vol2-ch06`.
- **Distinguish evidence levels**: Maintain the strict boundary between symmetry/exact algebraic theorems (e.g. Kramers degeneracy, Alaga branching limits), model calculations (Nilsson, pairing, RPA), and empirical experimental data.

---

## Core Frameworks and Mental Models

1. **Symmetry and Invariance as the First Principle (Vol. I Ch. 1)**:
   Nuclear phenomena must be formulated first through their invariance groups:
   - Anti-unitary time-reversal operator $\mathcal{T} = U K_0$ with $\mathcal{T}^2 = (-1)^{2j} = -1$ for half-integer fermion systems, proving **Kramers degeneracy** (every single-particle orbital in a time-reversal-invariant deformed field is at least twofold degenerate $|\Omega\rangle, |-\Omega\rangle$);
   - Isospin invariance and charge symmetry yielding the **Morpurgo $E1$ selection rule** ($\Delta T = 0$ transitions in self-conjugate $N=Z$ nuclei are strictly forbidden due to effective charge cancellation);
   - Rotational signature $\mathcal{R}_x(\pi) = e^{-i \pi I_x}$ with quantum number $r = (-1)^I$ or $\alpha = I \bmod 2$.

2. **Fermi Gas, Symmetry Energy, and Incompressibility (Vol. I Ch. 2)**:
   Nuclear matter as a saturated degenerate Fermi liquid:
   - Fermi momentum $k_F \a1.36\text{ fm}^{-1}$, Fermi energy $\epsilon_F \approx 38.5\text{ MeV}$, nuclear radius parameter $r_0 \a1.2\text{ fm}$;
   - Kinetic contribution to the symmetry energy coefficient $b_$C_$C_{\text{sym}}$ \a30\text{ MeV}$;
   - Compression modulus of nuclear matter $K_\infty \approx 200 - 250\text{ MeV}$, governing the breathing mode (ISGMR) energy systematics $E_0 \a80 A^{-1/3}\text{ MeV}$.

3. **Adiabatic Separation of Collective and Intrinsic Degrees of Freedom (Vol. II Ch. 4)**:
   In well-deformed nuclei, the fast intrinsic single-particle motion decouples from the slow collective rotation:
   $$\Psi_{IMK} = \sqrt{\frac{2I+1}{16\pi^2 (1 + \delta_{K0})}} \left[ D_{MK}^I(\theta_i) \chi_K + (-1)^{I+K} D_{M,-K}^I(\theta_i) \mathcal{T} \chi_K \right]$$
   Rotational energies follow the leading $I(I+1)$ pattern with signature-dependent Newby/Gallagher-Moszkowski shifts in $K=1/2$ and $K=0$ bands.

4. **Nilsson Deformed Mean Field and Asymptotic Quantum Numbers (Vol. II Ch. 5)**:
   Anisotropic harmonic oscillator with spin-orbit ($\vec{l}\cdot\vec{s}$) and centrifugal ($\vec{l}^2$) terms:
   - Deformed single-particle states classified by $[N n_z \Lambda \Omega]$;
   - Wave function parity $\pi = (-1)^N$;
   - Large deformation limit: $\Sigma = \Omega - \Lambda = \pm 1/2$, leading to characteristic selection rules in single-nucleon transfer and electromagnetic transitions.

5. **Coriolis Coupling, High-$j$ Alignment, and Decoupled Bands (Vol. II Ch. 4 & 5)**:
   The Coriolis perturbation Hamiltonian:
   $$H_{\text{cor}} = - \frac{\hbar^2}{\mathcal{J}} \left( I_+ j_- + I_- j_+ \right)$$
   - Strongly mixes $\Delta K = \pm 1$ bands;
   - Maximally affects high-$j$, low-$\Omega$ unique-parity intruder orbitals (e.g. $i_{13/2}, h_{11/2}, g_{9/2}$);
   - In $K=1/2$ bands, the diagonal Coriolis matrix element produces the decoupling parameter $a$:
     $$E(I) = \frac{\hbar^2}{2\mathcal{J}} \left[ I(I+1) + a (-1)^{I+1/2} (I + 1/2) \right]$$
     When $a = -(2j+1)$, the favored signature states form a decoupled rotational band mimicking the ground-state band of the even-even core.

6. **Electromagnetic Transition Alaga Rules and Mikhailov Perturbations (Vol. II Ch. 4)**:
   In the adiabatic limit, reduced transition probabilities are governed by geometrical Clebsch-Gordan coefficients (Alaga rules):
   $$B(E\lambda; I_i K_i \to I_f K_f) = \langle I_i K_i \lambda \Delta K | I_f K_f \rangle^2 |M_{\text{intr}}|^2$$
   Non-adiabatic Coriolis mixing is parameterized by Mikhailov plots:
   $$\frac{M(E2; I_i K_i \to I_f K_f)}{\langle I_i K_i 2 \Delta K | I_f K_f \rangle} = M_0 + M_1 \left[ I_f(I_f+1) - I_i(I_i+1) \right]$$
   Enabling the extraction of the unperturbed intrinsic moment $M_0$ and the interband mixing amplitude $M_1$.

7. **Microscopic Collectivity and Vibrational Sum Rules (Vol. II Ch. 6)**:
   Multipole surface vibrations ($\lambda = 2$ quadrupole, $\lambda = 3$ octupole) described via RPA/quasiparticle-phonon coupling:
   - Energy-Weighted Sum Rule (EWSR) exhaustion fraction serves as the litmus test for collective phonon vs single-particle states;
   - Particle-vibration coupling renormalizes single-particle masses and generates effective charges $e_{\text{eff}} = e_{\text{bare}} + \delta e_{\text{pol}}$.

---

## Chapter Index

| Volume & Chapter | Title | Core Frameworks & Applications |
|---|---|---|
| [vol1-ch01](chapters/vol1-ch01-symmetries-and-conservation-laws.md) | Symmetries and Conservation Laws | Time-reversal, Kramers degeneracy, isospin, Morpurgo E1 rule |
| [vol1-ch02](chapters/vol1-ch02-independent-particle-motion.md) | Independent-Particle Motion | Fermi gas, nuclear matter, incompressibility, Woods-Saxon |
| [vol1-ch03](chapters/vol1-ch03-single-particle-configurations.md) | Single-Particle Configurations | Fractional parentage, seniority, pairing gap, particle-hole |
| [vol2-ch04](chapters/vol2-ch04-rotational-spectra.md) | Rotational Spectra | Rotor-intrinsic separation, moments of inertia, Alaga rules, Mikhailov |
| [vol2-ch05](chapters/vol2-ch05-one-particle-motion-in-nonspherical-nuclei.md) | One-Particle Motion in Deformed Nuclei | Nilsson model, asymptotic $[N n_z \Lambda \Omega]$, Coriolis decoupling, backbending |
| [vol2-ch06](chapters/vol2-ch06-vibrational-spectra.md) | Vibrational Spectra | Quadrupole/octupole collective phonons, RPA, EWSR sum rules |

## Supporting Reference Files

- [glossary.md](glossary.md) — Comprehensive terminology crosswalk (English/Chinese) and notation conventions.
- [patterns.md](patterns.md) — Reusable reasoning patterns for nuclear structure spectroscopy and data analysis.
- [cheatsheet.md](cheatsheet.md) — Rapid calculation recipes, Alaga ratio tables, and formula cards.

---

## Scope & Limits

This skill represents the authoritative theoretical framework of the Bohr-Mottelson unified model. For experimental detector signal processing, refer to `in-beam-gamma-spectroscopy`; for simplified two-state mixing and $N_p N_n$ systematics, refer to `casten-nuclear-structure`; for triaxial non-axial chiral geometry, refer to `nuclear-triaxial-chirality-wobbling`.
