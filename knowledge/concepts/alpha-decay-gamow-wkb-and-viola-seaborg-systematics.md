---
type: concept
title: "Alpha decay Gamow quantum tunneling, centrifugal barrier and Viola-Seaborg systematics"
aliases: [alpha-decay-gamow-wkb, alpha-decay-penetration, gamow-factor, viola-seaborg-systematics]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [alpha-decay, quantum-tunneling, gamow-factor, wkb-approximation, viola-seaborg, hindrance-factor, nuclear-decay]
---

# Alpha decay Gamow quantum tunneling, centrifugal barrier and Viola-Seaborg systematics

## Definition

Alpha decay ($\alpha$ 衰变) is the spontaneous quantum emission of a $^4\text{He}$ nucleus ($Z=2, N=2, A=4$) from an unstable parent nucleus $(Z, A)$ to a daughter nucleus $(Z-2, A-4)$:
$$(Z, A) \to (Z-2, A-4) + \alpha + Q_\alpha$$
Because the total decay energy $Q_\alpha$ (typically $4 - 9\text{ MeV}$ in heavy nuclei) is substantially lower than the Coulomb barrier height $V_C(R_0) \approx 20 - 30\text{ MeV}$, the decay is strictly forbidden in classical mechanics. In quantum mechanics, it proceeds via wave-packet quantum tunneling through the combined Coulomb and centrifugal potential barrier.

The decay constant $\lambda$ and half-life $T_{1/2} = \ln 2 / \lambda$ are governed by:
$$\lambda = \nu \cdot P(L) \cdot S_\alpha$$
where:
1. $\nu = v_{\text{in}} / (2 R_0) \approx 10^{21} - 10^{22}\text{ s}^{-1}$ is the internal assault frequency of the $\alpha$ particle against the nuclear surface ($v_{\text{in}} = \sqrt{2(Q_\alpha + V_0)/m_\alpha}$ with well depth $V_0 \approx 25\text{ MeV}$ and touching radius $R_0 = r_0 [ (A-4)^{1/3} + 4^{1/3} ]$);
2. $P(L) = \exp[-2 G(L)]$ is the WKB barrier penetration probability, with action integral:
   $$2 G(L) = \frac{2}{\hbar} \int_{R_0}^{R_c(L)} \sqrt{2\mu [ V_{\text{eff}}(r) - Q_\alpha ]} \, dr$$
   where $\mu = \frac{m_\alpha m_d}{m_\alpha + m_d}$ is the reduced mass, $V_{\text{eff}}(r) = \frac{2(Z-2)e^2}{4\pi\varepsilon_0 r} + \frac{\hbar^2 L(L+1)}{2\mu r^2}$, and $R_c(L)$ is the classical turning point where $V_{\text{eff}}(R_c) = Q_\alpha$.
3. $S_\alpha$ is the $\alpha$ preformation factor ($0 < S_\alpha \le 1$), representing the overlap probability of four valence nucleons forming a correlated $^4\text{He}$ cluster on the nuclear surface.

For $L = 0$ s-wave tunneling through a pure Coulomb potential, the Gamow action integral integrates analytically to:
$$2 G_0 = \frac{8(Z-2)\alpha_{\text{em}}}{v/c} \left[ \arccos\sqrt{x_0} - \sqrt{x_0(1 - x_0)} \right]$$
where $v/c = \sqrt{2 Q_\alpha / \mu}$, $\alpha_{\text{em}} \approx 1/137.036$, and $x_0 = R_0 / R_c(0) = \frac{R_0 Q_\alpha}{2(Z-2)e^2}$.

## Necessary Assumptions

1. **Preformation and Two-Body Separation**: The parent nucleus can be treated as a composite system of a daughter nucleus and a preformed $\alpha$ cluster interacting via an effective central potential $V_{\text{eff}}(r)$.
2. **WKB Semiclassical Penetration**: Semiclassical WKB approximation requires that the de Broglie wavelength varies slowly compared to the potential scale ($|\frac{d\lambda}{dr}| \ll 1$), which holds well except near the isolated classical turning point $R_c$.
3. **Spherical Barrier and Neglect of Higher Multipolarity**: The analytical Gamow formula assumes a spherical Coulomb field. In deformed nuclei ($\beta_2, \beta_4 \ne 0$), anisotropic Coulomb and nuclear field multipoles couple different partial waves $L$.
4. **Sharp Nuclear Surface**: The nuclear touching radius is parameterized by $R_0 = r_0 [ (A-4)^{1/3} + 4^{1/3} ]$ with $r_0 \approx 1.20 - 1.25\text{ fm}$. Finite diffuseness (Woods-Saxon skin) slightly lowers the peak of the barrier.

## Discriminating Observables

1. **Geiger-Nuttall Law and Exponential Sensitivity**:
   The logarithm of the decay constant $\log_{10} \lambda$ or half-life $\log_{10} T_{1/2}$ scales linearly with $Q_\alpha^{-1/2}$ for isotopic chains:
   $$\log_{10} T_{1/2} = A(Z) Q_\alpha^{-1/2} + B(Z)$$
   A factor of 2 change in $Q_\alpha$ (e.g. $4.27\text{ MeV}$ in $^{238}\text{U}$ to $8.95\text{ MeV}$ in $^{212}\text{Po}$) drives an astounding 24 orders of magnitude change in half-life ($1.4 \times 10^{17}\text{ s}$ down to $3 \times 10^{-7}\text{ s}$).
2. **Viola-Seaborg Systematics**:
   With Sobiczewski parameterization, the half-life of ground-state decays across heavy and superheavy nuclei ($Z \ge 82$) is parameterized by:
   $$\log_{10} T_{1/2}(\text{s}) = \frac{a Z + b}{\sqrt{Q_\alpha}} + (c Z + d) + h_{\text{log}}$$
   where $a = 1.66175, b = -8.5166, c = -0.20228, d = -33.9069$, and $h_{\text{log}}$ accounts for odd-nucleon blocking hindrance ($h = 0$ for e-e, $0.772$ for odd-Z, $0.605$ for odd-N, $1.066$ for odd-odd).
3. **Hindrance Factor (HF)**:
   $$HF = \frac{T_{1/2}^{\text{exp}}}{T_{1/2}^{\text{WKB}}(L=0, S_\alpha=1)}$$
   - $HF \sim 1 - 4$: Favored / unhindered transition (e.g. $0^+ \to 0^+$ ground-to-ground or decay between identical single-particle Nilsson orbitals).
   - $HF \sim 10 - 100$: Moderately hindered transition ($L > 0$ centrifugal barrier or modest structural rearrangement).
   - $HF > 100 - 10^4$: Strongly hindered transition (parity flip $\Delta \pi$, large spin change $\Delta I = L$, shape change, or isomer decay).

## Supporting Evidence

1. **$^{212}\text{Po} \to {}^{208}\text{Pb} + \alpha$ Ground-State Benchmark**:
   - $Q_\alpha = 8.954\text{ MeV}$, $E_\alpha = 8.785\text{ MeV}$, $E_{\text{recoil}} = 168.9\text{ keV}$.
   - WKB calculation yields $2G_0 = 30.961$, $P = 3.58 \times 10^{-14}$, $T_{1/2}^{\text{WKB}} = 8.99\text{ ns}$.
   - Viola-Seaborg prediction gives $T_{1/2}^{\text{VS}} = 8.01 \times 10^{-8}\text{ s}$.
   - Experimental half-life $T_{1/2}^{\text{exp}} = 299\text{ ns}$ yields $HF = 33.3$, corresponding to preformation factor $S_\alpha \approx 0.030$.
2. **$^{238}\text{U} \to {}^{234}\text{Th} + \alpha$ Long-Lived Benchmark**:
   - $Q_\alpha = 4.270\text{ MeV}$, $E_\alpha = 4.198\text{ MeV}$.
   - WKB calculation yields $2G_0 = 86.378$, $P = 3.07 \times 10^{-38}$, $T_{1/2}^{\text{WKB}} = 1.17 \times 10^{16}\text{ s}$ ($3.7 \times 10^8\text{ yr}$).
   - Viola-Seaborg prediction gives $T_{1/2}^{\text{VS}} = 2.22 \times 10^{17}\text{ s}$ ($7.0 \times 10^9\text{ yr}$), matching the experimental half-life $T_{1/2}^{\text{exp}} = 1.41 \times 10^{17}\text{ s}$ ($4.47 \times 10^9\text{ yr}$) with $HF = 12.1$ ($S_\alpha \approx 0.083$).
3. **Superheavy Nucleus $^{294}\text{Og}$ ($Z=118$)**:
   - $Q_\alpha = 11.81\text{ MeV}$, $T_{1/2}^{\text{exp}} = 0.70\text{ ms}$.
   - Viola-Seaborg predicts $T_{1/2}^{\text{VS}} = 0.64\text{ ms}$, in near-perfect agreement with experimental decay times.

## Counter-evidence and Competing Interpretations

1. **Failure of Pure Point-Charge Coulomb Potential**:
   Near the nuclear touching radius $R_0$, the attractive nuclear proximity / folding potential significantly reduces the barrier peak compared to $2 Z_d e^2 / R_0$. Simple sharp-cutoff WKB models overestimate barrier height and must be calibrated using effective preformation factors or microscopic cluster models.
2. **Microscopic $\alpha$ Preformation vs Semiclassical Factorization**:
   The factorization $\lambda = \nu P S_\alpha$ treats $S_\alpha$ as a constant scalar. In microscopic shell-model and relativistic energy density functional (EDF) calculations, preformation is computed from the four-nucleon overlap integral of BCS quasiparticle wave functions, showing sharp shell closures at $N=126$ and $Z=82$.
3. **Centrifugal Barrier vs Deformed Coulomb Coupling**:
   In deformed nuclei, transitions with $L \ne 0$ (such as $0^+ \to 2^+, 4^+$ in rotational bands) cannot be modeled purely by adding $\hbar^2 L(L+1)/(2\mu r^2)$; they require coupled-channel Schrodinger penetration with quadrupole deformation $\beta_2$.

## Our Current Position

In this wiki, $\alpha$ decay calculations are performed using the exact WKB penetration and Viola-Seaborg engine in `alpha_decay_gamow_wkb_calculator.py` (CLI subcommand `alpha`, Module 95). The suite calculates both the exact analytical $L=0$ Gamow integral and numerical Simpson integration for $L > 0$ centrifugal barriers. Unhindered WKB half-lives and experimental hindrance factors are reported alongside Viola-Seaborg systematics without heuristic truncation.

## Sources

- [[book-lu-nuclear-physics-chinese]]: 卢希庭, 江栋兴, 叶沿林, 《原子核物理（修订版）》, 原子能出版社 (2000), 第5章 $\alpha$ 衰变, 印刷 pp. 113–128 / PDF pp. 123–138.
- Gamow, G., *Zur Quantentheorie des Atomkernes*, Z. Phys. 51, 204 (1928).
- Viola, V. E., Seaborg, G. T., *Nuclear systematics of the heavy elements - II. Lifetimes for alpha, beta, and spontaneous fission decay*, J. Inorg. Nucl. Chem. 28, 741 (1966).
- Sobiczewski, A., Gareev, F. A., Kalinkin, B. N., *Closed shells for Z > 82 and N > 126 in a diffuse potential well*, Phys. Lett. 22, 500 (1966).
