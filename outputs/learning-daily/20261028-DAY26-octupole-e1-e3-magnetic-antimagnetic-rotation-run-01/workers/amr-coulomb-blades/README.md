# AMR proton-blade Coulomb diagnostic

This directory contains a reproducible two-angle Routhian calculation for a
four-blade antimagnetic-rotation geometry. It compares a no-Coulomb baseline
with a finite-density direct proton-proton Coulomb term.

Run from the repository root:

```bash
python3 outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-coulomb-blades/amr_coulomb_blades.py
```

The script writes `amr_coulomb_blades_results.csv` and
`amr_coulomb_blades_results.json`. The Routhian uses `j_p=9/2`, `j_n=11/2`,
`V_pn=0.55 MeV`, `V_nn=0.50 MeV`, `I_core=19.5 MeV^-1`, and a 0.25 degree
angle mesh. The Coulomb term is

`V_C = kappa e^2 / sqrt(a^2 + (2 r sin(theta_p))^2)`.

The `a -> 0` point-particle limit diverges at closure. A finite orbital width
regularises the direct matrix element, as required for a quantum wavefunction.
With the illustrative `a=2.0 fm` parameter, the endpoint proton angle is in
the 10--15 degree range. This is a provisional calibrated result, not a
first-principles prediction or an experimental measurement. The `B(E2)`
output includes an explicitly imposed `B_core=0.06 e2 b2` proxy so that the
effect of angle asymmetry can be separated from the core contribution.
