---
type: concept
title: "Odd-odd triaxial nuclei chiral minimum energy path (MEP) and instanton quantum tunneling action solver"
aliases: [chiral-mep, instanton-tunneling, chiral-tunneling-splitting, large-amplitude-chiral-motion, odd-odd-chiral-tunneling]
created: 2026-11-04
updated: 2026-11-04
status: ai-draft
review_status: unreviewed
tags: [triaxiality, chirality, instanton, minimum-energy-path, neb, string-method, quantum-tunneling, 134pr, 128cs]
---

# Odd-odd triaxial nuclei chiral minimum energy path (MEP) and instanton quantum tunneling action solver

## Definition and Physical Mechanism

In odd-odd triaxial nuclei with $A \sim 130$ (e.g., $^{134}\text{Pr}$, $^{128}\text{Cs}$) and $A \sim 100$ (e.g., $^{106}\text{Ag}$), nuclear chirality arises from the mutually orthogonal coupling of three angular momentum vectors:
1. High-$j$ valence proton particle $\vec{j}_p$ (aligned along the nuclear short axis $s$, $\theta = \pi/2, \phi = 0$);
2. High-$j$ valence neutron hole $\vec{j}_n$ (aligned along the nuclear long axis $l$, $\theta = 0$);
3. Collective core rotation $\vec{R}$ (preferentially aligned along the intermediate axis $i$, $\theta = \pi/2, \phi = \pi/2$, possessing the largest moment of inertia $\mathcal{J}_i > \mathcal{J}_s, \mathcal{J}_l$ in irrotational/hydrodynamic and rigid triaxiality).

In the 3D Tilted Axis Cranking (TAC) mean-field description, the total angular momentum $\vec{J} = \vec{R} + \vec{j}_p + \vec{j}_n$ is specified by spherical orientation angles $(\theta, \phi)$ in the intrinsic frame:
$$J_s = I \sin\theta \cos\phi, \quad J_i = I \sin\theta \sin\phi, \quad J_l = I \cos\theta$$

For total spin $I > I_{\text{crit}}$, the classical rotational Routhian develops two symmetric degenerate minima:
- $(\theta_0, +\phi_0)$: Right-handed chiral geometry;
- $(\theta_0, -\phi_0)$: Left-handed chiral geometry.

The two chiral wells are separated by a planar barrier with a saddle point at $\phi = 0$.
Quantum mechanically, chiral symmetry is restored by quantum tunneling between the two wells, which lifts the two-fold degeneracy into chiral doublet bands (yrast and sideband) separated by an energy splitting $\Delta E_{\text{tunnel}}(I)$.

---

## Minimum Energy Path (MEP) and Instanton Formalism

Connecting the two wells $(\theta_0, -\phi_0) \to (\theta_0, +\phi_0)$ via a straight 1D line along $\phi$ is an oversimplification. Because the proton particle and neutron hole have different Coriolis alignments along the $s$ and $l$ axes, the potential surface $V(\theta, \phi)$ and effective mass tensor $B_{\mu\nu}(\theta, \phi)$ bend the true Minimum Energy Path (MEP) across the 2D surface.

Along the MEP parameterized by normalized arc length $s$, the Euclidean action (Instanton Action) is given by:
$$S_{\text{inst}} = \int_{\text{MEP}} \sqrt{2 B_{\text{eff}}(s) \cdot \max(0, V(s) - V_{\text{min}})}\, ds$$
where:
- $B_{\text{eff}} \approx \mathcal{J}_i / (2 \sin^2\theta_0)$ is the collective inertia for azimuthal rotation;
- $V(s)$ is the potential energy along the MEP relaxed via the String Method / Nudged Elastic Band (NEB);
- $\hbar\omega_0$ is the zero-point small-amplitude chiral vibrational frequency at the well minimum ($\hbar\omega_0 = \sqrt{C_\phi / B_{\text{eff}}}$).

The semiclassical chiral tunneling energy splitting is then:
$$\Delta E_{\text{tunnel}} = \frac{\hbar\omega_0}{\pi} \exp\left( - \frac{S_{\text{inst}}}{\hbar} \right)$$

### Physical Regimes:
1. **Chiral Vibration ($I \approx I_{\text{crit}}$)**:
   The barrier height is shallow ($\Delta V \le 20\text{ keV}$), the instanton action is small ($S_{\text{inst}} < 1\hbar$), and the energy splitting is large ($\Delta E \approx 30 - 200\text{ keV}$).
2. **Static Chirality ($I \gg I_{\text{crit}}$)**:
   The barrier deepens ($\Delta V > 250 - 500\text{ keV}$), the instanton action grows ($S_{\text{inst}} > 4 - 7\hbar$), exponentially suppressing tunneling. The doublet bands become nearly degenerate ($\Delta E \le 0.5 - 2\text{ keV}$).

---

## Executable Analysis Tool: `chirmep`

The Python analysis suite integrates `odd_odd_chiral_mep_instanton_tunneling_solver.py`, accessible via CLI:

```bash
# 1. 134Pr static chiral tunneling benchmark at I=17hbar
python3 system/scripts/analysis/nuclear_analyzer.py chirmep --preset 134Pr_chiral_mep_instanton

# 2. 134Pr chiral vibration near critical spin I=13hbar
python3 system/scripts/analysis/nuclear_analyzer.py chirmep --preset 134Pr_chiral_vibration

# 3. 128Cs classic chiral doublet band at I=16hbar
python3 system/scripts/analysis/nuclear_analyzer.py chirmep --preset 128Cs_chiral_doublet
```

---

## Literature and Textbook Provenance

- **Chirality and Wobbling in Atomic Nuclei** (CRC Press 2025), Chapter 2 (S. Frauendorf), Chapter 10 (Q. B. Chen, J. M. Yao, P. Ring).
- **Chen, Frauendorf, Sun**, Phys. Rev. C 96, 051303(R) (2017): *Collective Hamiltonian for chiral modes in nuclei*.
- **Frauendorf & Meng**, Nucl. Phys. A 617, 131 (1997): *Tilted axis cranking and chiral symmetry breaking*.
- **Bohr & Mottelson**, *Nuclear Structure*, Vol. II, §4-2.
