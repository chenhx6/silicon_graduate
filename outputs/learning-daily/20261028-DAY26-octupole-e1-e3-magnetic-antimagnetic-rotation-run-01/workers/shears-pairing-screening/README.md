# Pairing Fluctuation Screening of Shears Restoring Constants in MR and AMR

## Overview

Investigates the adiabatic screening of effective shears restoring constants $C_{\\text{shears}}(\\omega)$ by nuclear pairing correlations $\\Delta(\\omega)$ during rotational cranked motion in magnetic and antimagnetic rotators.

## Key Files

- `shears_pairing_screening_model.py`: Calculates pairing collapse curves, screened versus constant shears stiffness, and dynamical moment of inertia $J^{(2)}(\\omega)$.
- `pairing_screening_results.json`: Full numerical dataset across rotational frequencies $\\hbar\\omega = 0.08 \\to 0.44\\text{ MeV}$.
- `pairing_screening_results.csv`: Tabulated values of pairing gap, screened stiffness, shears angles, and $B(M1)$ rates.

## Scientific Findings

1. **Adiabatic Pairing Screening**:
   At low frequencies ($\\hbar\\omega < 0.2\\text{ MeV}$), large superflow pairing correlations ($\\Delta \\sim 1.0\\text{ MeV}$) screen the particle-hole quadrupole interaction, reducing the effective shears restoring constant by $25\\% - 30\\%$ ($C_{\\text{eff}} \\approx 1.35\\text{ MeV}$ vs $C_0 = 1.85\\text{ MeV}$).
2. **Dynamical Shears Hardening**:
   As the pairing gap collapses under Coriolis anti-pairing ($\\Delta \\to 0$), the screening disappears, causing the shears restoring potential to stiffen dynamically, producing a characteristic peak in $J^{(2)}$ and modifying the slope of $B(M1)$ near band termination.
