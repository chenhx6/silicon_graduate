# Octupole collective mass proxy

This worker is a reproducible two-level avoided-crossing diagnostic. It is
dimensionless and is not a calibrated EDF, QRPA, GCM, or nucleus-specific
ATDHFB calculation. It is intended to expose denominator sensitivity and the
effect of pairing and finite-frequency regularization.

Run from this directory with:

```bash
python3 octupole_mass_tensor.py
```

The script writes:

- `mass_surface.csv`: a `(beta2,beta3)` grid with `B22`, `B23`, and `B33` for bare IB, paired ATDHFB-like, dynamic ATDHFB-like, and a TV response proxy;
- `mass_curves_beta3.csv`: the beta3 cut through the crossing;
- `avoided_crossing_scaling.csv`: coupling `V` scaling at the crossing;
- `large_amplitude_periods.csv`: energy-conservation periods for the symmetric double-well proxy;
- `results.json`: parameters, formula conventions, row counts, and positivity check.

The model uses

```text
H_sp = [[a*x, V], [V, -a*x]],
x = beta3 - 0.105 + 0.25*(beta2 - 0.20),
epsilon = sqrt((a*x)^2 + V^2).
```

The off-diagonal derivative coupling is `F_i = (a V/epsilon) d_i x`. The
bare perturbative-cranking diagnostic is proportional to
`F_i F_j/(E_mu+E_nu)^3`. At the exact crossing and vanishing pairing it scales
as `1/V`; this is the conditional small-denominator singularity. A finite
pairing gap makes `E=sqrt(epsilon^2+Delta^2)` nonzero. The dynamic column uses
the smooth response scale `sqrt((2E)^2+(hbar*omega)^2)`, representing a
finite-frequency/pairing-fluctuation proxy. The `TV_proxy` is simply a 1.25
rescaling and must not be read as a self-consistent Thouless-Valatin result.

The many-body formulas represented by the columns are, in a stated convention,

```text
M_-n,ij = sum_(mu<nu) [F_i* F_j + F_j* F_i] / (E_mu+E_nu)^n,
B_GCM = hbar^2 M_-1^-1 M_-2 M_-1^-1,
B_ATDHFB = hbar^2 M_-1^-1 M_-3 M_-1^-1.
```

The small diagonal term in the toy moment matrices stands for omitted
two-quasiparticle channels and makes the two-coordinate inverse finite. It is
part of the proxy regularization, not microscopic data.
