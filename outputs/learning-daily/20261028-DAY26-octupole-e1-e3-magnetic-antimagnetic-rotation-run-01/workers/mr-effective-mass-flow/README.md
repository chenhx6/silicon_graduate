# Quasiparticle Effective Mass and Rotational Flow Back-Reaction in Magnetic Rotation

## Overview

Investigates how in-medium effective mass $m^*/m \\in [0.65, 1.00]$ (Skyrme, Gogny, CDFT) and rotational non-inertial flow back-reactions modify shears restoring potentials and dynamical moments of inertia $J^{(2)}$ in magnetic rotators ($^{198}\\text{Bi}$, $^{135}\\text{Pr}$).

## Key Files

- `mr_effective_mass_flow_model.py`: Calculates self-consistent Routhians with effective-mass-renormalized stiffness $C_{\\text{eff}}(m^*)$ and flow back-reaction currents $\\Delta J_{\\text{back}}(\\omega)$.
- `mr_effective_mass_flow_results.json`: Full numerical dataset across rotational frequencies $\\hbar\\omega = 0.08 \\to 0.44\\text{ MeV}$.
- `mr_effective_mass_flow_results.csv`: Flat tabular dataset for systematic model comparison.

## Scientific Findings

1. **Stiffness Inversion with Effective Mass**:
   Because the single-particle level density scales as $g(\\epsilon_F) \\propto m^*$, the effective shears stiffness scales inversely as $C_{\\text{shears}} \\propto 1/m^*$. Relativistic effective masses ($m^*/m \\approx 0.65$) harden the shears potential by $\\sim 50\\%$, significantly delaying premature blade closure compared to bare-mass calculations.
2. **Rotational Flow Back-Reaction**:
   Coriolis counter-currents $\\delta\\vec{v}(\\vec{r})$ partially cancel the apparent shears alignment, providing a natural in-medium quenching mechanism for the total spin buildup.
