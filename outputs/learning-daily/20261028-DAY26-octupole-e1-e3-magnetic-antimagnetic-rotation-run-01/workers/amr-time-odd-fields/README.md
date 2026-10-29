# AMR CRMF time-odd-field proxy

This worker is a reduced-unit, two-dimensional diagnostic for the local spatial Dirac current, the induced omega/rho/photon vector fields, the time-odd Dirac interaction, and four-blade antimagnetic-rotation response. It is not a self-consistent three-dimensional CRMF calculation: no covariant parameter set, pairing solver, blocked orbital basis, angular-momentum projection, or fitted meson propagator is used.

Run from this directory with:

```bash
python3 amr_time_odd_fields.py
```

The script uses NumPy and writes:

- `local_fields.csv`: the 45-degree baryon current, reduced vector field, and vorticity on the x-z grid;
- `level_shifts.csv`: time-odd-off/on reduced shifts for proton g9/2, neutron h11/2, comparator levels, and spin-orbit proxies;
- `scissors_potential.csv`: the phenomenological four-blade stiffness scan;
- `j2_cd_systematics.csv`: finite-difference `J^(2)` values from the locally stored Cd transition-energy ledger;
- `j2_time_odd_proxy.csv`: the explicitly model-dependent time-odd response scenario for 106,108,110Cd;
- `results.json`: equations, symmetry diagnostics, parameter boundary, source locators, and summary values;
- `time_odd_fields.svg`: dependency-free potential plot.

At 45 degrees the paired blade moments cancel to numerical precision while the local current and vector field remain nonzero. The default stiffness ansatz gives 16.95–20.28% enhancement across the angle scan; the 15/20/25% values in `results.json` are a sensitivity scan, not a published CRMF result. The Cd `J^(2)` changes are response proxies and must not be subtracted from the experimental energies as if they were an observable decomposition.

The durable evidence and scientific limits are recorded in [`knowledge/research-notes/amr-relativistic-time-odd-fields-and-spin-orbit-splitting.md`](../../../../../knowledge/research-notes/amr-relativistic-time-odd-fields-and-spin-orbit-splitting.md).
