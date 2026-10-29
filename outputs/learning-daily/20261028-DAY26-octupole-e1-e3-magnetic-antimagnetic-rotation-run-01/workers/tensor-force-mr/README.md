# Tensor-Force Renormalization in Odd-Odd Magnetic Rotators

## Overview

Investigates the role of in-medium nuclear tensor interactions in renormalizing the effective shears restoring potential in odd-odd magnetic rotators (e.g. $^{198}\\text{Bi}$, $^{106}\\text{Ag}$).

## Key Files

- `tensor_force_shears_model.py`: Solves Routhian minimization with quartic tensor-force potential $V_{\\text{eff}}(\\theta) = \\frac{1}{2} C_2 \\cos^2\\theta + \\frac{1}{4} C_4 \\cos^4\\theta$.
- `bi198_tensor_shears_results.json`: Calculated benchmark data comparing standard quadrupole, tensor stiffening ($C_4 > 0$), and tensor softening ($C_4 < 0$).
- `bi198_tensor_shears_results.csv`: Flat table format of rotational frequency, shears angle, spin, $B(M1)$, $B(E2)$, and $J^{(2)}$.

## Scientific Findings

1. **Non-linear Quartic Correction**:
   The nuclear tensor force produces an effective quartic angle coupling $\\sim C_4 \\cos^4\\theta$ between valence proton and neutron single-particle currents.
2. **Curvature Deviation in B(M1)**:
   Tensor softening ($C_4 < 0$) produces an accelerated downward curvature in $B(M1; I \\to I-1)$ as the band approaches termination, providing a quantitative explanation for deviations from simple $\\sin^2\\theta$ geometric fits.
