---
type: concept
title: "Cranked Strutinsky triaxial shape coexistence potential energy surface (PES) and spin-induced yrast shape transitions"
aliases: [shape-coexistence-pes, cranked-strutinsky, triaxial-oblate-coexistence, yrast-shape-crossing, 130ba-pes]
created: 2026-11-04
updated: 2026-11-04
status: ai-draft
review_status: unreviewed
tags: [triaxiality, shape-coexistence, cranked-strutinsky, pes, potential-energy-surface, 130ba, 76kr, 186pb]
---

# Cranked Strutinsky triaxial shape coexistence potential energy surface (PES) and spin-induced yrast shape transitions

## Phenomenological Definition & Microscopic Origin

In transitional nuclei across multiple mass regions ($A \approx 130$ Ba-Ce; $A \approx 70$ Kr-Se; $A \approx 180$ Pt-Pb), competing shell structures produce **Shape Coexistence**: the presence of multiple local minima on the 2D $(\beta_2, \gamma)$ collective quadrupole potential energy surface.

In the Macroscopic-Microscopic Strutinsky framework under 1D cranking rotation $\omega$:
$$E_{\text{total}}(\beta, \gamma, \omega) = E_{\text{macro}}(\beta, \gamma) + \delta U(\beta, \gamma) - \frac{1}{2}\mathcal{J}_x(\beta, \gamma)\omega^2$$

Where:
1. **Macroscopic Liquid Drop Energy**:
   $$E_{\text{macro}}(\beta, \gamma) = C_2 \beta^2 + C_3 \beta^3 \cos(3\gamma) + C_4 \beta^4$$
   The cubic invariant $C_3 \beta^3 \cos(3\gamma)$ controls the fundamental prolate ($\gamma = 0^\circ$) vs. oblate ($\gamma = 60^\circ$) asymmetry.
2. **Microscopic Strutinsky Shell Correction $\delta U(\beta, \gamma)$**:
   In $A \sim 130$ transitional nuclei ($Z \approx 56, N \approx 74$):
   - Protons occupying low-$\Omega$ levels of the intruder $h_{11/2}$ shell favor positive triaxial deformation ($\gamma \approx 20^\circ - 30^\circ$);
   - Neutrons occupying the upper Fermi surface of the $h_{11/2}$ subshell act as holes, generating an energy minimum near oblate deformation ($\gamma \approx 55^\circ - 60^\circ$).
3. **Cranking Rotational Energy & Dynamic Deformation Gain**:
   $$E_{\text{rot}}(\beta, \gamma, \omega) = - \frac{1}{2} \mathcal{J}_x(\beta, \gamma) \omega^2$$
   The collective moment of inertia along the intermediate rotation axis scales strongly with deformation:
   $$\mathcal{J}_x(\beta, \gamma) = \mathcal{J}_0 \left(\frac{\beta}{\beta_0}\right)^{1.5} \left[ 1 - 0.5 \cos\left(\gamma - \frac{4\pi}{3}\right) \right]$$

---

## Spin-Induced Yrast Shape Transitions

Because the triaxial shape possesses both a larger quadrupole deformation ($\beta \approx 0.24$ vs. $0.16$) and optimal orientation along the intermediate axis ($\gamma \approx 24^\circ$), its effective moment of inertia is significantly larger ($\mathcal{J}_{\text{tri}} \approx 55 - 60\text{ MeV}^{-1}$ vs. $\mathcal{J}_{\text{obl}} \approx 30 - 35\text{ MeV}^{-1}$).

Consequently, as rotational frequency $\omega$ increases:
The rotational energy $- \frac{1}{2}\mathcal{J}_x \omega^2$ lowers the triaxial minimum much faster than the oblate minimum.
At the **critical crossing frequency** $\omega_{\text{cross}}$:
$$\Delta E_{12}(\omega) = E_{\text{oblate}}(\omega) - E_{\text{triaxial}}(\omega) = 0$$
The yrast ground state undergoes a sudden **first-order shape transition** from oblate to triaxial deformation!
This mechanism provides the theoretical foundation for why transitional nuclei exhibit stable triaxial wobbling and chiral bands at high spins, despite possessing oblate or $\gamma$-soft ground states at zero spin.

---

## Executable Analysis Tool: `coexpes`

The Python analysis suite integrates `cranked_triaxial_shape_coexistence_pes_engine.py`, accessible via CLI:

```bash
# 1. 130Ba triaxial-oblate coexistence: shape crossing detected at omega_cross = 0.236 MeV/hbar
python3 system/scripts/analysis/nuclear_analyzer.py coexpes --preset 130Ba_triaxial_oblate_coexistence

# 2. 76Kr prolate-oblate coexistence: shape crossing at omega_cross = 0.262 MeV/hbar
python3 system/scripts/analysis/nuclear_analyzer.py coexpes --preset 76Kr_prolate_oblate_coexistence

# 3. 186Pb triple shape coexistence intruder crossing at omega_cross = 0.232 MeV/hbar
python3 system/scripts/analysis/nuclear_analyzer.py coexpes --preset 186Pb_triple_shape_coexistence
```

---

## Literature and Textbook Provenance

- **Bohr & Mottelson**, *Nuclear Structure*, Vol. II, §4-2, §6-4.
- **W. Greiner & J. A. Maruhn**, *Nuclear Models* (Springer 1996), Chapter 8.
- **S. Frauendorf**, Rev. Mod. Phys. 73, 463 (2001): *Spontaneous symmetry breaking in rotating nuclei*.
- **Petrache et al.**, Phys. Rev. C 99, 044303 (2019): *Diversity of shapes and rotations in 130Ba*.
