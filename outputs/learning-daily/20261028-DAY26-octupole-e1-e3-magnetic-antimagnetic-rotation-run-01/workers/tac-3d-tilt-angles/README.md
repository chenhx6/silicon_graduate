# 3D Microscopic Cranking Tilt Angles and Axis Ratios in Magnetic Rotation

## Overview

Investigates the self-consistent 3D Tilted Axis Cranking (3D TAC) spatial orientation angles $(\\theta_{\\text{rot}}, \\phi_{\\text{rot}})$ and core axis ratios $(R_x : R_y : R_z)$ during the closing of shears blades in magnetic rotators.

## Key Files

- `tac_3d_tilt_angles_model.py`: Solves 3D Routhian minimization across rotational frequencies $\\hbar\\omega = 0.12 \\to 0.44\\text{ MeV}$.
- `tac_3d_tilt_angles_results.json`: Calculated values of polar tilt, azimuth $\\phi$, out-of-plane curvature $K_\\phi$, axis ratios, and electromagnetic observables.
- `tac_3d_tilt_angles_results.csv`: Flat tabular dataset for systematic comparison.

## Scientific Findings

1. **Planar Stability and Strict Azimuthal Locking**:
   In magnetic rotation, the azimuthal angle is strictly locked at $\\phi_{\\text{rot}} \\equiv 0$, with positive out-of-plane restoring curvature $K_\\phi = \\frac{\\partial^2 R}{\\partial \\phi^2} \\sim 1.3 - 5.1\\text{ MeV}$, proving that pure shears motion is robust against chiral non-planar fluctuations.
2. **Axis Ratio Evolution**:
   As the shears blades close, the effective triaxial deformation shifts mildly by $< 1^\\circ$, while the quadrupole deformation $\\beta_2$ remains stable around $0.12 - 0.13$.
