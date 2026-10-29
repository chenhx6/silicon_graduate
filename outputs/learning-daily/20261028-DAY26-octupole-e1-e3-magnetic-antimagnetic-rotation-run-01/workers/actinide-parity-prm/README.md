# Quadrupole-octupole PRM worker

This worker implements a transparent finite-difference model for an even-even
quadrupole-octupole rotor. It covers `220,222,224,226,228Ra` and
`222,224,226,228,230Th`.

## Reproduce

From this directory run:

```text
python3 quad_oct_prm.py
```

The script uses Python 3, NumPy, and no repository-local data files. It writes
the following deterministic artifacts:

- `prm_levels.csv`: lowest even and odd parity eigenvalues for each spin;
- `parity_displacement.csv`: finite-difference displacement plus the explicit
  WKB-like convergence surrogate;
- `e1_e2_systematics.csv`: rotor branch strengths, ratios in `fm^-2`, and
  inverted `D0` values;
- `results.json`: equations, parameters, empirical anchors, and all rows;
- `chart_data.json`: compact arrays ready for plotting.

## Model and evidence boundary

The solved Hamiltonian is

`H_I = -(hbar^2/2B33)d^2/d(beta3)^2 + V(beta3) + hbar^2 I(I+1)/(2J(beta3))`,

with a symmetric quartic double well and
`J(beta3)=J0(1+c3 beta3^2)`. The finite-difference eigenvectors are parity
classified and provide the rotor levels. The exponential line in
`parity_displacement.csv` is a clearly labelled WKB-like surrogate; it is
calibrated to the scale examples `224Ra: 174 -> 20 keV` and
`226Th: 194 -> approximately 0 keV`, and is not an EDF/GCM prediction.

The E1/E2 calculation uses
`B(E1)=(3/4pi)D0^2 C1^2` and
`B(E2)=(5/16pi)Q0^2 C2^2`, with all strengths converted to physical
`e^2 fm^(2lambda)` units before inversion. The `224Ra=0.15 e fm` and
`226Ra=0.05 e fm` entries are user-supplied targets for sensitivity testing.
The former conflicts with an existing Wiki audit value near `0.03 e fm`; both
are retained as an explicit review boundary in `results.json` and the linked
research note.

The potential, inertia, and dipole inputs are schematic. Experimental facts
remain in the knowledge source pages; no CSV row should be cited as a new
measurement.
