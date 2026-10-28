# Planar → aplanar transition worker

This worker is a reproducible classical particle–rotor geometry diagnostic. It
minimizes

```text
E(I) = Σk (Ik − jk)^2/(2 Jk),   |I| = I
```

with `jp=(jp,0,0)`, `jn=(0,0,jn)`, and `Jm > Js,Jl`. The intermediate-axis
component `Im` is the order parameter. In this convention
`R = I − jp − jn`, so `Rm = Im` and
`chi_g = jp · (jn × R) = −jp*jn*Im`.

Run from this directory:

```bash
python3 planar_aplanar_transition.py
```

The command writes `transition_scan.csv` and `transition_scan.json`. With the
stored illustrative parameters (`jp=jn=5.5`, `Js=10`, `Jm=30`, `Jl=15`) the
fixed-spin grid first finds an aplanar minimum at `I=14`; the planar azimuthal
curvature changes sign at the same grid spin. The two mirror minima have zero
energy difference to grid precision.

The numerical values are dimensionless diagnostics in the stated effective
moment convention. They are not fitted values for `106Ag`, `106Cd`, `134Pr` or
`198Bi`, and `mu_perp2_dimensionless` is not an experimental `B(M1)`. The model
does not perform angular-momentum projection, tunnelling, configuration mixing,
DSAM fitting, or detector/feeding modelling. It therefore demonstrates the
geometric bifurcation and its reverse tests, while partner-band evidence still
requires the source-specific electromagnetic data listed in the research note.

Source premises used for the model boundary:

- Frauendorf (2001), printed pp. 475–476 and 484–485: principal-axis, planar
  tilted-axis and aplanar solutions; left/right mean-field restoration.
- Frauendorf (2001), printed pp. 487–488: magnetic and antimagnetic rotation
  observables.
- Frauendorf and Meng (1997), model geometry: dominant intermediate-axis
  inertia for an aplanar chiral solution.
- Clark et al. (2000), printed pp. 11–18 and 30–34: shears angle, `B(M1)`
  evolution and core-rotation/configuration-crossing limits.
