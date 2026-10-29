# Finite-Range Shears Interaction and Rotational Frequency Quenching

## Overview

Investigates the role of nuclear finite force range ($\\mu = 0.8, 1.2, 1.6\\text{ fm}$) versus zero-range contact approximation in governing the closing of shears blades and rotational frequency quenching in magnetic rotation.

## Key Files

- `finite_range_shears_model.py`: Routhian minimization solver comparing finite Gaussian force ranges to contact limits in $^{198}\\text{Bi}$.
- `finite_range_shears_results.json`: Full numerical trajectories across rotational frequencies $\\hbar\\omega = 0.06 \\to 0.42\\text{ MeV}$.
- `finite_range_shears_results.csv`: Tabulated values of shears angle, total spin, $B(M1)$, and dynamical moment of inertia $J^{(2)}$.

## Scientific Findings

1. **Potential Softening and Delayed Closing**:
   In zero-range contact models, the shears potential is strictly quadratic in $\\cos\\theta$, forcing premature blade closing at moderate rotational frequencies. Finite force ranges ($\\mu \\sim 1.2\\text{ fm}$) soften the potential at small angles, delaying closure and preserving finite $B(M1)$ up to higher frequencies.
2. **Frequency Quenching at Band Termination**:
   The saturation of the finite-range interaction derivative $dV/d(\\cos\\theta)$ naturally bounds the rotational frequency $\\hbar\\omega$, reproducing the bandhead-to-termination compression observed in experiments.
