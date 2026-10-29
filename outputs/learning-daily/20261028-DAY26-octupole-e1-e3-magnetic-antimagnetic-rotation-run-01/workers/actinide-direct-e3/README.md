# Odd-A actinide direct E3 angular-coupling work package

This directory contains a transparent strong-coupling calculation for direct
electric-octupole transitions between opposite-parity bands. It evaluates the
CG geometry for `Delta I = 0, +/-1, +/-2, +/-3`, the `K=1/2` octupole
decoupling factor, and the relative `Delta I=+3/-3` direction geometry.

The input `Q30=1000 e fm^3` is illustrative. It is not an experimental value
for `223,225Ra` or `225,227Ac`. The work package therefore provides a model
network and reproducible angular factors, not an experimental claim of direct
odd-A actinide `B(E3)` measurements. The evidence boundary and source links
are recorded in the companion research note:

`knowledge/research-notes/odd-a-actinide-parity-doublet-direct-e3-transitions-angular-coupling.md`

## Run

```bash
python3 direct_e3_angular_coupling.py
```

Generated files:

- `direct_e3_network.csv`: transition rows for `223,225Ra` and `225,227Ac`;
- `cg_geometry_matrix.csv`: CG and CG-squared values;
- `delta3_direction_comparison.csv`: `+3/-3` geometry ratios;
- `khalf_interference_curve.csv`: `K=1/2` alternating interference factors;
- `direct_e3_results.json`: metadata and all rows in one JSON object.

The script uses only the Python standard library. Its finite factorial formula
for CG coefficients is included in the source so the numerical convention is
visible and does not depend on a hidden package.
