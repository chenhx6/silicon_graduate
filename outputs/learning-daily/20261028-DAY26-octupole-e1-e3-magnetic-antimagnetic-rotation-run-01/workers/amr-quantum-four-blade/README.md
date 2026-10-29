# AMR Quantum Four-Blade Cranking and Core Polarization

## Overview

This directory provides the microscopic cranking and core-polarization model for Antimagnetic Rotation (AMR) in $^{110}\text{Cd}$ and $^{104}\text{Pd}$.

## Key Files

- `quantum_four_blade_amr.py`: Python script solving self-consistent Routhian minimization for four-blade shears angles $(\theta_\pi, \theta_\nu)$ and core quadrupole deformation $\beta_2$.
- `cd110_amr_quantum_cranking.json`: Calculated benchmark data compared directly to Roy et al. (Phys. Lett. B 697, 275 (2011)).
- `cd110_amr_quantum_cranking.csv`: Tabulated values of rotational frequency, blade angles, $B(E2)$, $B(M1)$, $J^{(2)}$, and $J^{(2)}/B(E2)$.

## Key Physical Findings

1. **Strict M1 Cancellation**:
   The four blades obey $\mathcal{R}_y(\pi)\mathcal{T}$ and $\mathcal{R}_z(\pi)\mathcal{T}$ space-time reflection symmetry, yielding exact zero transverse magnetic dipole moment:
   $$\vec{\mu}_\perp \equiv 0 \implies B(M1) \equiv 0$$
2. **B(E2) Plateau at Band Termination**:
   Pure geometric shears predict $B(E2) \propto \sin^4\theta \to 0$ when blades close. However, microscopic core polarization generates an enduring collective platform ($B(E2)_{\text{core}} \approx 0.06-0.09\ e^2\text{b}^2$), matching experimental observations in $^{110}\text{Cd}$ ($0.06(2)\ e^2\text{b}^2$ at $I=24^+$) and $^{104}\text{Pd}$ ($0.02(1)\ e^2\text{b}^2$).
3. **Giant Dynamic Ratio**:
   The ratio $J^{(2)}/B(E2)$ remains within the characteristic $245 - 619\ \hbar^2\text{MeV}^{-1}(e^2\text{b}^2)^{-1}$ range, providing a definitive discriminant against normal collective rotation ($\sim 10-30$).
