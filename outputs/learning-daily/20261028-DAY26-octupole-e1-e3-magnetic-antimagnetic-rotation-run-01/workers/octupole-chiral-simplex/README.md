# Octupole–chiral signature and simplex model

This folder contains a synthetic, reproducible diagnostic model for a triaxial high-
`j` particle coupled to an octupole double well. It is designed to expose the
interference between a triaxial signature amplitude, an octupole amplitude, and a
spin-dependent Coriolis amplitude. It is not a fit to `78Br`, `130Cs`, or `133Ce`.

Run:

```bash
python3 octupole_chiral_simplex_model.py
```

The run writes:

- `signature-splitting-results.csv`: branch energies, `Delta E_rot`, and `S(I)`;
- `simplex-landscape-results.csv`: quartic-well minima, barriers, WKB gap proxies;
- `octupole-chiral-simplex-results.json`: parameters, algebra checks, and file manifest;
- `signature-splitting.svg` / `.png` and `simplex-restoration.svg` / `.png`.

The discrete-symmetry check records that `P` commutes with `R_x(pi)` and therefore
with `S=P R_x^{-1}(pi)`. A four-state local basis follows from two independent
exchange coordinates (chirality and the sign of `beta_3`); a nonzero commutator
requires an additional antiunitary operation or a different convention.
