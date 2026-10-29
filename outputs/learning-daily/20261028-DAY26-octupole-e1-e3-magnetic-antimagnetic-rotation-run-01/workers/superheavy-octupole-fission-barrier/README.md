# Superheavy octupole fission barrier toy WKB

This directory contains a reproducible two-coordinate sensitivity calculation
for `254No (Z=102,N=152)` and `256Rf (Z=104,N=152)`. The elongation coordinate
`q` is a proxy for the second-saddle path and `beta3` is the axial
reflection-asymmetric coordinate. The reference path is `beta3=0`; the
asymmetric path minimizes an even Landau potential

```text
V(q,beta3) = V_sym(q) + a3(q) beta3^2 + c3 beta3^4,
beta3*(q) = sqrt[-a3(q)/(2 c3)] when a3(q)<0.
```

The action is evaluated as `S/hbar = integral sqrt(2 M(s)[V(s)-E0]) ds`, with
collective masses in `hbar^2/MeV`, and `log10(Tsf/s) = log10[(ln2)/nu] +
2 S/ln(10)` using the explicit assault proxy `nu=1e20 s^-1`.

Run from the repository root:

```bash
python3 outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/superheavy-octupole-fission-barrier/superheavy_octupole_wkb.py
```

The run writes one path CSV per isotope, `scan_summary.json`,
`scan_parameters.json`, and `barrier_and_beta3.svg`. The default grid is 4001
points and `E0=0.80 MeV`.

## Results

| nucleus | `B_f^II` symmetric (MeV) | asymmetric (MeV) | lowering (MeV) | `S_sym` | `S_asym` | `Delta log10(Tsf)` |
|---|---:|---:|---:|---:|---:|---:|
| `254No` | 6.200 | 5.066 | 1.134 | 8.199 | 5.372 | -2.456 |
| `256Rf` | 6.550 | 5.105 | 1.445 | 8.432 | 4.103 | -3.760 |

These values are model outputs. The parameters are intentionally exposed in
the Python file so that EDF barrier heights, a calculated inertia tensor, or a
different zero-point energy can replace the proxies without changing the IO
contract. No claim is made here that either isotope has a measured static
octupole saddle.
