# CRMF Dirac-current proxy

This worker provides a reproducible two-dimensional proxy for the spatial-current bookkeeping requested for magnetic rotation in `199Pb` and `135Pr`.

It is not a CRMF solver. It does not solve the three-dimensional Dirac-Hartree equations, meson propagators, pairing, angular-momentum projection, or an explicit negative-energy Dirac sea. The core term is a linear-response counter-flow surrogate; the sea column is a clearly labelled 6% sensitivity residual.

## Run

```bash
python3 crmf_dirac_currents.py
```

The script uses only the Python standard library. Grid size and spatial extent can be changed with `--grid` and `--extent`.

## Model contract

The current is decomposed as

```text
j_D = j_valence + delta(j_core) + delta(j_sea, proxy)
```

The local field is represented by a divergence-free stream function, `j_x = d_z psi` and `j_z = -d_x psi`. Two displaced high-j loops represent the shears current. A broadened opposite-sign response represents core counter-flow. As the shears angle closes, the field is continuously mixed into a regularized cylindrical stream, giving a diagnostic termination limit.

The effective M1 proxy is

```text
B(M1) = 3/(8 pi) [g_delta j_p j_n sin(theta) / I]^2
B(M1)_eff = (g_eff/g_free)^2 B(M1)_free
```

The values are model results and sensitivity diagnostics. They are not absolute experimental strengths or published CRMF outputs.

## Files

- `crmf_dirac_currents.py`: source code and parameter definitions.
- `crmf_current_summary.csv`: frequency-by-frequency angular-momentum, topology, effective-g and M1 summary.
- `current_slices.csv`: valence, core, sea-proxy and total current components plus vorticity on the spatial slices.
- `results.json`: manifest, equations and summary rows.
- `topology_landscape.svg`: dependency-free plot of the effective-g scan.

The durable interpretation and evidence boundaries are in [`knowledge/research-notes/crmf-dirac-currents-and-core-counter-rotation.md`](../../../../../knowledge/research-notes/crmf-dirac-currents-and-core-counter-rotation.md).
