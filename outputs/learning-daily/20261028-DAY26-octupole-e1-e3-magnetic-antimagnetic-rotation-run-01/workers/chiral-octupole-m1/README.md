# Chiral octupole M1 selection-rule toy model

This worker implements the four-state basis
`(|L,+>, |R,+>, |L,->, |R,->)` and the projected labels `(chi,p)`. It is a
symmetry and bookkeeping model, not a fit to `78Br`, `131Ba`, `134Pr`, or any
other nucleus.

## Physics contract

The magnetic dipole operator is represented as

`T(M1) = sqrt(3/(4*pi)) mu_N [g_l l + g_s s + g_R R]`.

In the projected basis the reduced toy operator is
`M1 = m_chi sigma_x(chi) tensor identity(p)`. It is parity even and time
reversal odd. Therefore same-parity chiral-partner M1 transitions are allowed
for `Delta I=1`, while cross-parity M1 matrix elements are exactly zero when
the Hamiltonian preserves parity.

The optional `h_parity` term is an explicit parity impurity. It demonstrates
how a small cross-parity M1 amplitude can appear after parity mixing. The
parity-preserving tunnelings `t_chi`, `t_pi`, and `t_chi_pi` alone do not
produce that amplitude. The expected scaling is
`B(M1)_cross/B(M1)_same ~ |eta_i+eta_f|^2`, with `eta` the parity admixture.

The polar-current diagnostic uses
`C = 1 - |m_L+m_R|/(|m_L|+|m_R|)`. It is a defined toy residual-current
measure, not a model-independent theorem about every microscopic current
density.

## Files

- `chiral_octupole_m1_selection_rules.py`: standalone standard-library Python
  generator.
- `m1_selection_rules_results.json`: operator contract, strict zero check,
  transition networks, and barrier scan.
- `m1_transition_network.csv`: `I=10 -> 9` M1 network with `h_parity=0.10`
  keV, including same-parity and impurity branches.
- `barrier_scan.csv` and `barrier_scan.json`: 7 x 7 scan in chiral and
  octupole barrier heights, with `B(M1)` ratio and current cancellation.
- `cross_to_same_m1_heatmap.svg`: dependency-free chart of the barrier scan.

## Reproduce

```bash
python3 chiral_octupole_m1_selection_rules.py
```

The strict symmetry check in the JSON reports zero cross-parity amplitude at
`h_parity=0`. All energies, g factors, geometric factors, barriers, and
current residuals are synthetic and should not be quoted as measured values.
