# AMR core quadrupole drive and non-harmonic shears torque

This directory contains a deterministic two-coordinate surrogate for an
antimagnetic-rotation band.  It is intended to expose the feedback between a
shears angle `theta` and a polarizable core deformation `beta2`.

## Model

At fixed total spin `I` the minimized laboratory energy is

```text
E(theta,beta; I) = V_s cos(theta)^2
                  + 1/2 C (beta-beta0)^2
                  + [I - I_qp(theta)]^2 / [2 J_core(beta)]
I_qp(theta) = j_p + 2 j_h cos(theta)
J_core(beta) = J0 + (dJ/dbeta)(beta-beta0)
```

The conjugate frequency is `omega=(I-I_qp)/J_core`.  The stationary equations
give the useful checks

```text
tau_shears = -dV_shears/dtheta = V_s sin(2 theta)
F_quad,elastic = -dE_core/d beta = -C (beta-beta0)
F_quad,drive = 1/2 (dJ/dbeta) omega^2
```

Thus the positive drive shifts `beta` upward while the larger `J_core` lowers
the frequency needed for a fixed residual angular momentum.  The reported
`tau_retarding` is the difference between the closing torque computed with
`J_core(beta0)` and that computed with the polarized `J_core(beta)` at the same
`I`; it is a model diagnostic, not a separately measured torque.

For the transition-strength diagnostic, effective coherent amplitudes are used:

```text
B(E2) = [Q_shears sin^2(theta) + Q_core(beta)]^2
Q_core(beta) = beta (e b)
```

`Q_shears` and `Q_core` are amplitude parameters.  Their squared terms are
reported separately, but the experimental B(E2) does not uniquely determine
that partition because the cross term and phase are unmeasured here.

## Files and execution

- `amr_core_drive_model.py`: standard-library Python implementation and model metadata.
- `amr_core_drive_trajectory.csv`: 57 fixed-spin minima sorted by conjugate omega.
- `amr_core_drive_stiffness_scan.csv`: five core-stiffness scans, 145 rows.
- `amr_core_drive_chart_data.json`: plotting-ready trajectory and scan payload.
- `amr_core_drive_results.json`: equations, parameters, limits and SHA-256 hashes.

Run from this directory:

```bash
python3 amr_core_drive_model.py
```

The baseline gives `beta2=0.1133 -> 0.1534`, `B(E2)=0.1354 ->
0.0660 e^2 b^2`, and a positive retarding-torque diagnostic over the
high-spin part of the trajectory.  These are outputs of the surrogate, not a
fit or a new experimental extraction.

## Evidence boundary

Roy et al. 2011 directly reports the 110Cd 16+–24+ lifetimes and
`B(E2)=0.14(1), 0.12(2), 0.11(2), 0.09(3), 0.06(2) e^2 b^2` (PDF p.324,
Table 1).  The same paper uses a particle-plus-rotor interpretation with
`J_m=19.5 hbar^2/MeV` (PDF pp.325–326).  Rather et al. 2014 locally provides
the AMR geometry and `sin^4(theta)` law on its first page; the remaining
pages and any point-by-point 104Pd table are not treated as verified here.

The model therefore supports a mechanism-level comparison only.  It does not
claim that centrifugal force proves a spontaneous static deformation, that a
single B(E2) measurement separates core and shears amplitudes, or that the
same parameters apply unchanged to 102,104Pd and 106,108,110Cd.
