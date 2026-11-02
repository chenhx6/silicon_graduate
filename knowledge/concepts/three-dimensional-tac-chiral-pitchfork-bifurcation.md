---
type: concept
title: "Three-dimensional tilted axis cranking (3D-TAC) chiral pitchfork bifurcation, aplanar orientation energy surface and tunneling barrier"
aliases: [3d-tac-chiral-bifurcation, pitchfork-bifurcation-chirality, aplanar-orientation-surface, chiral-barrier-inversion, 3d-tac-energy]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [triaxiality, nuclear-chirality, 3d-tac, pitchfork-bifurcation, orientation-energy-surface, spontaneous-symmetry-breaking, 134pr]
---

# Three-dimensional tilted axis cranking (3D-TAC) chiral pitchfork bifurcation, aplanar orientation energy surface and tunneling barrier

## Definition and Phenomenological Origin

In triaxial odd-odd nuclei (e.g. $^{134}\text{Pr}, {}^{128}\text{Cs}$ in the $A \sim 130$ region), spontaneous breaking of time-reversal-rotation symmetry $\mathcal{T}\mathcal{R}_y(\pi)$ produces left-handed and right-handed rotational geometries.

Based on *Chirality and Wobbling in Atomic Nuclei* (CRC Press 2025) Chapter 2 (J. Meng & P. W. Zhao), Chapter 9 (PDF pp. 204–221), P. W. Zhao et al. (Phys. Lett. B 699, 181, 2011), and S. Frauendorf & J. Meng (Nucl. Phys. A 617, 131, 1997):
1. The total angular momentum $\vec{J} = (J_s, J_m, J_l)$ couples:
   - Valence proton particles $j_p$ along the short ($s$) axis;
   - Valence neutron holes $j_n$ along the long ($l$) axis;
   - Collective core rotation $\vec{R}$ along the intermediate ($m$) axis.
2. In spherical polar coordinates:
   $$J_s = J \sin\theta \cos\phi, \quad J_m = J \sin\theta \sin\phi, \quad J_l = J \cos\theta$$
   where $\theta \in [0, \pi]$ is the polar tilt angle and $\phi \in [0, \pi/2]$ is the out-of-plane azimuth ($\phi = 0^\circ$ is planar in the $(s, l)$ frame).

---

## Mathematical Formalism: Quasiclassical Energy Functional & Pitchfork Bifurcation

### 1. Orientation Energy Surface
The rotational energy functional is:
$$E(J, \theta, \phi) = \frac{(J \sin\theta \cos\phi - j_p)^2}{2\mathcal{J}_s} + \frac{(J \sin\theta \sin\phi)^2}{2\mathcal{J}_m} + \frac{(J \cos\theta - j_n)^2}{2\mathcal{J}_l}$$
where $\mathcal{J}_m > \mathcal{J}_s, \mathcal{J}_l$ reflects intermediate-axis rotational dominance.

### 2. Supercritical Pitchfork Bifurcation
- At low spin ($J < J_{\text{crit}}$), the energy minimum lies on the boundary plane:
  $$\phi_{\text{min}} = 0^\circ \quad (\text{Planar Rotation, no chirality})$$
- At the critical spin $J_{\text{crit}}$, the planar minimum becomes a saddle point ($\partial^2 E / \partial \phi^2 < 0$), triggering a **supercritical pitchfork bifurcation**:
  $$J_{\text{crit}} \approx \sqrt{\left( j_p \frac{\mathcal{J}_m}{\mathcal{J}_s} \right)^2 + \left( j_n \frac{\mathcal{J}_m}{\mathcal{J}_l} \right)^2} \cdot \left( 1 + \frac{\mathcal{J}_s}{\mathcal{J}_m} \right)^{-1}$$
  Above $J_{\text{crit}}$, two degenerate aplanar minima emerge at:
  $$\phi_{\text{min}}(J) = \pm \arccos\left( \frac{J_{\text{crit}}}{J} \right) > 0^\circ$$
  All three components $J_s, J_m, J_l \ne 0$, forming aplanar left- and right-handed chiral states!

### 3. Chiral Potential Barrier Height
The potential energy barrier separating the two chiral minima is:
$$\Delta E_{\text{barrier}}(J) = E(J, \theta_{\text{saddle}}, \phi=0) - E(J, \theta_{\text{min}}, \phi_{\text{min}})$$
In finite quantum nuclei, tunneling through this barrier produces the experimentally observed energy splitting $\Delta E(I)$ between partner bands.

---

## Executable Analysis Tool: `tacbifurc`

The Python analysis suite integrates `three_dimensional_tac_chiral_pitchfork_bifurcation_inverter.py`, accessible via:

```bash
# Benchmark 1: 134Pr landmark chiral nucleus (Frauendorf & Meng 1997)
python3 system/scripts/analysis/nuclear_analyzer.py tacbifurc --preset 134Pr_chiral_bifurcation

# Benchmark 2: 128Cs chiral doublet benchmark (Grodner 2006, 2018)
python3 system/scripts/analysis/nuclear_analyzer.py tacbifurc --preset 128Cs_chiral_bifurcation

# Counterexample: Axially symmetric rotor (no bifurcation, barrier = 0)
python3 system/scripts/analysis/nuclear_analyzer.py tacbifurc --preset axial_symmetric_no_bifurcation
```

### Benchmark Validation: $^{134}\text{Pr}$
- At $J = 10\ \hbar$: planar phase ($\phi = 0^\circ$, barrier $\Delta E = 0\text{ keV}$);
- Bifurcation occurs at $J_{\text{crit}} = 12.0\ \hbar$, with out-of-plane angle rising to $\phi = 21.2^\circ$;
- At $J = 16\ \hbar$: mature aplanar chiral phase ($\phi = 50.6^\circ$, barrier $\Delta E = 633.1\text{ keV}$, chiral volume $V = 0.302$).
- Axially symmetric counterexample correctly confirms absence of pitchfork bifurcation.
