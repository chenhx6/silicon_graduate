# Glossary: Nuclear Chirality & Wobbling Terminology

Comprehensive crosswalk of specialized terminology in non-axial nuclear structure and collective motion from *Chirality and Wobbling in Atomic Nuclei* (CRC Press, 2025).

---

## 1. Nuclear Chirality Concepts (核手征性概念)

- **Nuclear Chirality (原子核手征性)**: Spontaneous breaking of the discrete time-reversal-rotational symmetry $\mathcal{T}\mathcal{R}_y(\pi)$ in the intrinsic frame of a triaxially deformed nucleus ($\gamma \a30^\circ$) when the valence proton, valence neutron, and core angular momentum vectors form a non-coplanar (aplanar) right- or left-handed triad.
- **Chiral Doublet Bands (手征双重带)**: A pair of $\Delta I = 1$ rotational bands sharing identical single-particle configurations, parity, and deformations, degenerate or near-degenerate in energy ($\Delta E(I) < 100\text{ keV}$), restored in the laboratory frame by quantum tunneling through the planar chiral barrier.
- **Multiple Chiral Doublets ($M\chi D$, 多重手征双重带)**: The coexistence of two or more pairs of chiral doublet bands in the same atomic nucleus, arising from different multi-quasiparticle configurations (Type I), triaxial shape coexistence (Type II), or chiral multi-phonon excitations (Type III).
- **Aplanarity (非共面度)**: A measure of the non-coplanarity of the angular momentum vectors:
  $$A_{\text{chiral}} = \frac{\vec{j}_p \cdot (\vec{j}_n \times \vec{R}_{\text{core}})}{|\vec{j}_p| |\vec{j}_n| |\vec{R}_{\text{core}}|}.$$
  $A_{\text{chiral}} \neq 0$ defines the chiral regime; $A_{\text{chiral}} = 0$ corresponds to planar rotation (achiral).
- **Chiral Parity Quartets (手征-宇称四重带)**: A supermultiplet of four intertwined rotational bands ($\pi = \pm, \text{chiral} = \pm$) arising from simultaneous spontaneous breaking of spatial inversion parity $\mathcal{P}$ (octupole deformation $\beta_3 \neq 0$) and chirality $\mathcal{T}\mathcal{R}_y(\pi)$ (triaxial deformation $\beta_2 \neq 0, \gamma \a30^\circ$).

---

## 2. Wobbling Motion Concepts (摆动运动概念)

- **Nuclear Wobbling Motion (原子核摆动运动)**: Semiclassical precession of the total angular momentum vector $\vec{I}$ around the principal axis of largest moment of inertia in a triaxially deformed nucleus, quantized as harmonic phonon excitations ($n_w = 0, 1, 2, \dots$).
- **Transverse Wobbling (TW, 横向摆动)**: The wobbling mode where the odd high-$j$ quasiparticle aligns its angular momentum along the short principal axis ($s$), while the nucleus collective rotation occurs predominantly around the intermediate axis ($m$). The wobbling frequency $\hbar\omega_w = E(I, n_w=1) - [E(I-1, n_w=0) + E(I+1, n_w=0)]/2$ **decreases monotonically with increasing spin $I$** ($d\hbar\omega_w/dI < 0$).
- **Longitudinal Wobbling (LW, 纵向摆动)**: The wobbling mode where the odd quasiparticle aligns its angular momentum along the same axis as the collective rotation vector (the intermediate axis). The wobbling frequency **increases monotonically with spin $I$** ($d\hbar\omega_w/dI > 0$).
- **Intermediate-Axis Separatrix (中间轴不稳定分离线)**: The topological boundary in the classical angular momentum phase space ($2 E \mathcal{J}_2 = M^2$) separating closed precession orbits around the short axis from those around the long axis.
- **Tilted Axis Precession (TiP, 倾斜轴进动)**: Rotation of the nucleus around a uniform axis tilted into one of the principal planes with signature splitting, characterized by predominantly $M1$ connecting transitions and lacking the collective interband $E2$ enhancement required for wobbling.

---

## 3. Electromagnetic Selection Rules and Diagnostics (电磁选择定则与判据)

- **$S_{M1}(I)$ Staggering Parameter (带内 $M1$ 奇偶交错参量)**:
  $$S_{M1}(I) = \frac{[B(M1; I \to I-1)/B(E2; I \to I-2)]_I}{[B(M1; I-1 \to I-2)/B(E2; I-1 \to I-3)]_{I-1}}.$$
  In true chiral doublets, $S_{M1}(I)$ exhibits **100% in-phase staggering** between Band 1 and Band 2; in signature partner bands, it staggers out-of-phase (anti-phase).
- **Grodner $g$-Factor Equality Law ($g$ 因子严格相等律)**:
  $$g_1(I) \equiv g_2(I).$$
  Because the two partner bands share identical intrinsic particle-hole-core wave functions, their gyromagnetic factors $g = \mu / (\mu_N I)$ must be identical within experimental uncertainty.
- **Hypothesis-Driven Root Selection (HDRS, 假设驱动选根)**: The cognitive and methodological fallacy of adopting the large-$|\delta|$ solution ($\delta \sim -2$) of the directional angular distribution quadratic equation ($a_2(\delta) = a_2^{\text{exp}}$) to claim a wobbling band without measuring linear polarization or conversion coefficients to rule out the small-$|\delta|$ signature partner solution.
