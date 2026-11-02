---
type: concept
title: "Grodzins product rule, quadrupole deformation beta_2 inversion and superfluid moment of inertia pairing reduction"
aliases: [grodzins-product-rule, beta2-deformation-inversion, intrinsic-quadrupole-moment, superfluid-moi-pairing-reduction]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [nuclear-structure, deformation, grodzins-rule, beta2, quadrupole-moments, b-e2, superfluidity, pairing-reduction]
---

# Grodzins product rule, quadrupole deformation beta_2 inversion and superfluid moment of inertia pairing reduction

## Definition

In low-energy collective nuclear structure, the electric quadrupole transition probability $B(E2; 0_1^+ \to 2_1^+)$ and the first excited state energy $E(2_1^+)$ in even-even nuclei provide direct macroscopic measures of nuclear deformation, shell structure, and superfluid pairing:

1. **Quadrupole Deformation Parameter $\beta_2$ Inversion**:
   Under the Bohr collective model (卢希庭 2000 第 8 章 §8.4; Bohr & Mottelson Vol. II §4-2; Raman et al. 2001), the nuclear radius expands as $R(\theta, \phi) = R_0 [1 + \beta_2 Y_{20}(\theta)]$. The reduced transition probability $B(E2; 0_1^+ \to 2_1^+)$ (in $e^2\text{b}^2$) directly yields the quadrupole deformation parameter $\beta_2$:
   $$\beta_2 = \frac{4\pi}{3 Z R_0^2} \sqrt{\frac{B(E2; 0_1^+ \to 2_1^+)}{e^2}}$$
   where $R_0 = 1.2 A^{1/3}\text{ fm}$, and $B(E2)$ is converted to $e^2\text{fm}^4$ ($1\ e^2\text{b}^2 = 10^4\ e^2\text{fm}^4$).

2. **Intrinsic and Spectroscopic Quadrupole Moments ($Q_0$ and $Q_s$)**:
   In the body-fixed intrinsic coordinate frame, the intrinsic quadrupole moment $Q_0$ measures the permanent mass/charge asymmetry:
   $$Q_0 = \sqrt{\frac{16\pi}{5} \frac{B(E2; 0^+ \to 2^+)}{e^2}} \approx \frac{3}{\sqrt{5\pi}} Z R_0^2 \beta_2 (1 + 0.16\beta_2)$$
   The spectroscopic quadrupole moment $Q_s(2_1^+)$ measured in the laboratory frame by Coulomb excitation reorientation:
   $$Q_s(2_1^+) = -\frac{2}{7} Q_0$$
   - Negative $Q_s(2^+) < 0 \iff$ Prolate deformed ellipsoid ($\beta_2 > 0$);
   - Positive $Q_s(2^+) > 0 \iff$ Oblate deformed ellipsoid ($\beta_2 < 0$).

3. **Grodzins Empirical Product Rule**:
   Lee Grodzins (1962) and S. Raman et al. (2001) established that the product $E(2_1^+) \cdot B(E2; 0_1^+ \to 2_1^+)$ across all even-even nuclei satisfies an empirical scaling law:
   $$E(2_1^+) \cdot B(E2; 0_1^+ \to 2_1^+) = (2.57 \pm 0.45) \times Z^2 A^{-2/3} \text{ keV}\cdot e^2\text{b}^2$$
   The dimensionless Grodzins ratio:
   $$\mathcal{G} = \frac{E(2_1^+) \cdot B(E2; 0_1^+ \to 2_1^+)}{2.57 \times Z^2 A^{-2/3}}$$
   - $\mathcal{G} \approx 0.8 - 1.2$: Normal collective rotor or vibrator obeying global systematics;
   - $\mathcal{G} \gg 1.5$: Spherical magic shell closure ($^{132}\text{Sn}, ^{208}\text{Pb}$) where $E(2^+)$ is anomalously high;
   - $\mathcal{G} \ll 0.7$: Superdeformed bandhead or soft transitional collectivity.

4. **Superfluid Pairing Reduction of the Moment of Inertia**:
   - The experimental moment of inertia: $\mathcal{J}_{\text{exp}} = \frac{3\hbar^2}{E(2_1^+)}$;
   - The classical rigid-sphere moment of inertia:
     $$\mathcal{J}_{\text{rig}} = \frac{2}{5} M_u A R_0^2 (1 + 0.31\beta_2)$$
   - The superfluid reduction ratio:
     $$\frac{\mathcal{J}_{\text{exp}}}{\mathcal{J}_{\text{rig}}} \approx 0.30 - 0.55$$
   As emphasized by Bohr & Mottelson, the fact that experimental moments of inertia are quenched by $50\%$ relative to the rigid rotor is the historical proof of BCS pairing superfluidity in deformed atomic nuclei.

## Necessary Assumptions

1. **Axially Symmetric Quadrupole Deformation**: Primary deformation is prolate or oblate quadrupole ($\lambda=2$), with hexadecapole ($\beta_4$) and triaxial ($\gamma$) treated as secondary perturbations.
2. **$K=0$ Rotational Bandhead**: The ground state bandhead has $K=0$, satisfying the adiabatic rotational Clebsch-Gordan coupling $\langle 2 0 2 0 \mid 0 0 \rangle = 1/\sqrt{5}$.

## Discriminating Observables

1. **Deformation Parameter Magnitude**:
   - $\beta_2 \ge 0.30$: Highly deformed or superdeformed rotor (e.g. $^{154}\text{Sm}$ with $\beta_2 = 0.34$);
   - $0.20 \le \beta_2 < 0.30$: Well-deformed rare earth or actinide rotor;
   - $0.10 \le \beta_2 < 0.20$: Transitional $A \sim 130$ nucleus (e.g. $^{134}\text{Ce}$ with $\beta_2 = 0.17$);
   - $\beta_2 < 0.10$: Near-spherical or vibrational shell-closure nucleus ($^{132}\text{Sn}$ with $\beta_2 = 0.02$).
2. **Prolate vs Oblate Asymmetry ($Q_s$)**:
   Direct measurement of $Q_s(2_1^+)$ via Coulomb excitation fixes the sign of deformation.
3. **$\mathcal{J}_{\text{exp}} / \mathcal{J}_{\text{rig}}$ Superfluid Fraction**:
   Directly measures the strength of nucleon-nucleon pairing correlations $\Delta_{\text{pair}}$, recovering the rigid limit ($\mathcal{J} \to \mathcal{J}_{\text{rig}}$) only at high spin after the Coriolis anti-pairing (CAP) backbending transition.

## Supporting Evidence

1. **$^{154}\text{Sm}$ Well-Deformed Prolate Rotor Benchmark**:
   - $Z=62, A=154, E(2^+) = 82.0\text{ keV}, B(E2) = 4.35\text{ e}^2\text{b}^2$;
   - Inverted deformation: $\beta_2 = 0.3406$ (matches Raman 2001 evaluated $\beta_2 = 0.341$);
   - $Q_0 = 6.613\text{ e}\cdot\text{b}$, $Q_s(2^+) = -1.889\text{ e}\cdot\text{b}$ (prolate!);
   - Grodzins product: $E(2^+) \cdot B(E2) = 356.7\text{ keV}\cdot e^2\text{b}^2$ vs theoretical $343.9\text{ keV}\cdot e^2\text{b}^2 \implies \mathcal{G} = 1.037$ (matches to $3.7\%$);
   - Moment of inertia: $\mathcal{J}_{\text{exp}} = 36.59\ \hbar^2/\text{MeV}$ vs $\mathcal{J}_{\text{rig}} = 67.40\ \hbar^2/\text{MeV} \implies \mathcal{J}_{\text{exp}} / \mathcal{J}_{\text{rig}} = 0.543$.
2. **$^{132}\text{Sn}$ Doubly Magic Benchmark**:
   - $Z=50, A=132, E(2^+) = 4041.0\text{ keV}, B(E2) = 0.011\text{ e}^2\text{b}^2$;
   - Inverted deformation: $\beta_2 = 0.0235$ (near-spherical);
   - $\mathcal{J}_{\text{exp}} / \mathcal{J}_{\text{rig}} = 0.016 \ll 1.0$, confirming absence of collective rotation.

## Counter-evidence and Competing Interpretations

1. **Triaxiality and Effective $\gamma$ Softness**:
   For triaxial nuclei ($\gamma \ne 0^\circ$), the simple prolate formula slightly overestimates $\beta_2$ because $B(E2)$ is shared between $K=0$ and $K=2$ bands. Microscopic analysis requires Kumar quadrupole invariants $\langle Q^2 \rangle$ and $\langle Q^3 \cos 3\delta \rangle$ (Module 14).
2. **Departures from Grodzins Scaling at Shell Closures**:
   Grodzins scaling fails dramatically near doubly closed shells ($Z=50, 82; N=82, 126$), where $E(2^+)$ is dominated by two-quasiparticle seniority excitations rather than collective rotation.

## Our Current Position

In this wiki, quadrupole deformation parameters $\beta_2$, intrinsic/spectroscopic quadrupole moments ($Q_0, Q_s$), Grodzins product rules, and superfluid pairing moment of inertia reductions are analyzed using Module 104 (`grodzins_deformation_beta2_quadrupole_inverter.py`, CLI subcommand `grodzins`). The module benchmarks well-deformed rare earths against doubly magic shell closures with exact evaluated Raman (2001) systematics.

## Sources

- [[book-lu-nuclear-physics-chinese]]: 卢希庭, 江栋兴, 叶沿林, 《原子核物理（修订版）》, 原子能出版社 (2000), 第8章 核结构模型 §8.4 (形变核转动能谱与形变参量, 印刷 pp. 205–212 / PDF pp. 215–222).
- [[book-bohr-mottelson-nuclear-structure-vol2]]: A. Bohr and B. R. Mottelson, *Nuclear Structure*, Vol. II, §4-2 (pp. 31–38).
- Grodzins, L., *A systematics of the properties of the lowest 2+ states in even-even nuclei*, Phys. Lett. 2, 88 (1962).
- Raman, S., Nestor, C. W., Jr., Tikkanen, P., *Transition probability from the ground to the first-excited 2+ state of even-even nuclides*, At. Data Nucl. Data Tables 78, 1 (2001).
