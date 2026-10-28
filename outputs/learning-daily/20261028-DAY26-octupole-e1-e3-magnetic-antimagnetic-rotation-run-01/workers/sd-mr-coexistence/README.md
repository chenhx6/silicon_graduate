# A≈190 Pb SD/MR two-well comparison

`sd_mr_doublewell.py` is a deliberately transparent scale model. It produces:

- `deformation_pes.csv`: a quartic two-minimum potential in `beta2`;
- `sd_mr_observables.csv`: rotor E2, shears M1, and illustrative `J^(2)` tracks;
- `sd_mr_model_summary.json`: equations, inputs, source boundary, and consistency checks.

Run from this directory:

```bash
python3 sd_mr_doublewell.py
```

The code is not a self-consistent HFB, TAC, or GCM calculation. Its purpose is
to make the topology and observable contrast auditable, while keeping measured
values and illustrative controls separate. In particular, `Q_t≈20 eb` from the
Pb SD lifetime work and `beta2=0.50` are retained as separate inputs because the
standard liquid-drop conversion in the script gives `Q0≈14.7 eb` for beta2=0.50.
