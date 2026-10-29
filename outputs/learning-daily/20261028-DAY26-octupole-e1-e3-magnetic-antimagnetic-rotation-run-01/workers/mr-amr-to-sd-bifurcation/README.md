# Shears Mechanism to Superdeformation Bifurcation Model

## Overview

Investigates the high-spin topological competition between shears closing in a weakly deformed core (Well 1, $\\beta_2 \\sim 0.12$) and collective crossing into a superdeformed rotational well (Well 2, $\\beta_2 \\sim 0.56$) in $^{194}\\text{Pb}$.

## Key Files

- `shears_to_sd_bifurcation.py`: Self-consistent two-well energy minimization and WKB barrier penetration calculator.
- `pb194_bifurcation_results.json`: Numerical outputs covering spins $I = 12 \\to 44\\hbar$.
- `pb194_bifurcation_results.csv`: Tabulated values of $E_{\\text{ND}}$, $E_{\\text{SD}}$, shears angle, $B(M1)$, $B(E2)$, and $J^{(2)}$.

## Scientific Findings

1. **Yrast Crossing at High Spin**:
   In $^{194}\\text{Pb}$, the MR shears band forms the yrast state from $I=12\\hbar$ up to $I=28\\hbar$. At $I \\approx 30\\hbar$, the huge moment of inertia of the superdeformed minimum ($J_{\\text{SD}} \\sim 91\\ \\hbar^2/\\text{MeV}$) overcomes the $4.5\\text{ MeV}$ bandhead excitation energy, causing the SD band to become the true yrast state.
2. **Observable Signature Jumps**:
   The transition from Well 1 to Well 2 is marked by a discontinuous jump in $B(E2)$ from $\\sim 0.05\\ e^2\\text{b}^2$ to $\\sim 1.85\\ e^2\\text{b}^2$ ($37\\times$ increase) and a complete quenching of $M1$ transitions.
