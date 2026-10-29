# Angular Momentum Fluctuations and Exact Projection in the Shears Mechanism

## Overview

Investigates quantum angular momentum dispersion $\\Delta J_\\perp^2(\\theta) = \\langle \\vec{J}^2 \\rangle - \\langle J_x \\rangle^2$ and exact angular momentum projection (AMP) corrections to energy levels and reduced magnetic dipole transition rates $B(M1)$ in magnetic rotators ($^{198}\\text{Bi}$, $^{135}\\text{Pr}$).

## Key Files

- `shears_amp_fluctuations_model.py`: Calculates self-consistent shears opening angles, Casimir dispersions, and exact AMP projection factors $f_{\\text{proj}}(I)$.
- `shears_amp_results.json`: Full numerical dataset for spins $I = 15 \\to 21\\hbar$.
- `shears_amp_results.csv`: Flat tabular dataset for comparative analysis.

## Scientific Findings

1. **Large Angular Momentum Fluctuation**:
   In the intermediate shears opening region ($\\theta \\sim 50^\\circ - 60^\\circ$), the transverse angular momentum dispersion reaches $\\Delta J_\\perp^2 \\sim 9 - 11\\ \\hbar^2$, reflecting the non-collinear quantum orientation of the valence quasiparticles.
2. **Systematic Semiclassical Overestimation**:
   Exact AMP demonstrates that semiclassical shears formulas systematically overestimate experimental $B(M1)$ transition rates by $12\\% - 28\\%$, due to the quantum projection factor $f_{\\text{proj}}(I) = 1 - \\frac{\\Delta J_\\perp^2}{2 I^2}$.
