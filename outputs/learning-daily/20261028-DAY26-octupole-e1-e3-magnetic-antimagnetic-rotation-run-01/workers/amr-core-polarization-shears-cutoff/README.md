# AMR finite-j cutoff and core-polarization response

This worker implements a transparent fixed-total-spin surrogate for the
four-blade antimagnetic-rotation question.  It combines the exact identical
fermion pair limits

```text
pi(g9/2)^-2: Jp = 0, 2, 4, 6, 8
nu(h11/2)^2: Jn = 0, 2, 4, 6, 8, 10
J_val,max = Jp,max + Jn,max = 18 hbar
```

with the requested energy functional.  The effective blade coordinate is
`x = cos(theta/2)`, `J_val = 18*x`, so `j_blade=9` is a coarse-grained
four-blade length.  It is not the single-particle `g9/2` or `h11/2` value.

## Equations

```text
E(I,x) = V_shears(x) + (I - 18*x)^2/(2*J_core)
V_shears(x) = a*x^2 + b*x^4

I(x) = 18*x + (J_core/18) V'_shears(x)
R_core = I - 18*x = J_core*omega
dx/dI = 1 / [18 + (J_core/18) V''_shears(x)]
dtheta/dI = -2*(dx/dI)/sqrt(1-x^2)
J^(2) = J_core + 18^2/V''_shears(x)
```

The last two expressions apply on the interior branch.  Once `I` exceeds
`I(1)`, the finite-j valence sector is pinned at `J_val=18` and additional
spin is carried by the core.  The angle coordinate has a square-root endpoint
singularity at `theta=0`; `d(sin^2(theta/2))/dI` is reported as the regular
closure diagnostic there.

For the E2 diagnostic, the script reports both the pure shears term and a
coherent effective core amplitude:

```text
B_shears_only = Q_shears^2 sin^4(theta/2)
B_total = [Q_core + phase*Q_shears sin^2(theta/2)]^2
```

`Q_shears` and `Q_core` are effective amplitudes in `eb`; the geometric
normalization is absorbed into them.  Thus the core inertia delays the fall of
the shears term, while a nonzero core E2 amplitude produces the residual high-
spin plateau.  A finite `J_core` alone does not create a nonzero floor at
`theta=0`.

## Run

From this directory:

```bash
python3 amr_core_polarization_shears_cutoff.py
```

Files written by the script:

- `amr_core_polarization_trajectory.csv`: 110Cd-like and 104Pd-like half-
  hbar trajectories with angle, valence/core spin, E2 terms, tangent and
  finite-difference `J^(2)` diagnostics.
- `closure_comparison.csv`: pure-shears versus finite-core closure at common
  spins.
- `core_inertia_scan_at_I16.csv`: response to changing `J_core`.
- `finite_j_pair_limits.csv`: allowed same-j pair spins and the 18-hbar cap.
- `parameters.json`: equations, parameters, source locators and boundaries.
- `results.json`: selected rows, checks, and SHA-256 hashes of the artifacts.

The 110Cd-like set uses `J_core=19.5 hbar^2/MeV`, gives `I_sat=26.0167 hbar`,
and carries about `8 hbar` in the core at `I=26`.  Its illustrative total
`B(E2)` is `0.114, 0.102, 0.090, 0.090 e^2 b^2` at `I=22,24,26,28`, while
`J^(2)/B(E2)` from the finite-difference energy is `356.5, 377.6, 285.3`
for `I=22,24,26` and remains in the broad 200--450 diagnostic range over the
selected 110Cd-like points.  These are conditional model outputs, not new
measurements or a microscopic fit.

The 104Pd-like rows only test the same angular-momentum bookkeeping with a
different core inertia and effective E2 scale.  The local Rather 2014 source
is a first-page excerpt, and Zhang 2019 shows that the full PNC configuration
and deformation evolution can be richer than the frozen four-blade subspace.
