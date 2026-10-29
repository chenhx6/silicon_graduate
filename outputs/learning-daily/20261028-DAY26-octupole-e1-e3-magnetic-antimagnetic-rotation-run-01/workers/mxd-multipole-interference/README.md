# Multipole Operator Matrix Elements and Transition Interference in MxD Octupole Nuclei

## Overview

Investigates algebraic quantum interference in electromagnetic transition multipole operators ($E1, M1, E2, E3$) across chiral-octupole quadruplets in nuclei with multiple chiral doublets (M$\\chi$D) and octupole softness ($^{78}\\text{Br}$, $^{133}\\text{Ce}$, $^{135}\\text{Nd}$).

## Key Files

- `mxd_multipole_interference_model.py`: Diagonalizes the $4 \\times 4$ composite chiral-parity Hamiltonian and projects multipole transition matrices.
- `mxd_interference_results.json`: Full numerical dataset of quadruplet eigenvalues, splittings, and reduced transition rates.
- `mxd_interference_results.csv`: Tabulated dataset covering ranges of chiral tunneling $t_\\chi$ and parity tunneling $t_\\pi$.

## Scientific Findings

1. **Strict Algebraic Selection Rules**:
   Electric dipole transitions ($T(E1)$) strictly couple opposite-parity states ($\\Delta\\pi = -1$) while conserving the chiral symmetry channel, whereas magnetic dipole transitions ($T(M1)$) connect opposite-chirality partner states while preserving parity.
2. **Interference Quenching and Branching Ratios**:
   Cross-tunneling matrix elements ($t_{\\chi\\pi}$) break the naive uncoupled selection rules, creating destructive interference that completely suppresses transitions into one of the partner bands ($B(E1; 0 \\to 3) \\approx 0$), resulting in orders-of-magnitude branching ratio anomalies.
