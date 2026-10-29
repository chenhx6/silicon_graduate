# Hyperdeformed actinide third-well worker

This directory contains a deterministic Python 3 reduced model for the `beta2-beta3` energy surface, a one-dimensional parity-tunnelling sensitivity scan, and a qualitative decay-channel diagnostic for `230,232Th` and `232,234,236U`.

Run:

```text
python3 hyperdeformed_actinides.py
```

Outputs:

- `pes_grid.csv`: 2D energy grid for each nucleus. `beta3=0` is the reflection-symmetric constrained path; the relaxed path is obtained by minimizing the quartic beta3 sector.
- `results.json`: third-well locations, path barrier proxies, geometric `Q3`, `D0` proxy, equations and provenance boundary.
- `parity_wkb.csv`: `Delta E` versus `beta3` for an assumed dimensionless collective mass `B=140`. The exponential suppression is conditional on this mass and the quartic potential.
- `decay_competition.csv`: outer-barrier WKB transmission proxies versus excitation above the model third minimum. It intentionally does not report an absolute gamma/fission branching ratio.
- `chart_data.json`: compact arrays for plotting the surfaces, relaxed paths and WKB curves.

## Model boundary

The potential is a transparent reduced Landau-like surface, not a Woods–Saxon, Skyrme, Gogny or covariant EDF calculation. Its isotope coefficients are sensitivity inputs chosen to place the relaxed hyperdeformed minima near `beta2≈0.9` and `beta3≈0.30–0.43`; they are not fitted to the uranium or thorium resonance data.

The geometric octupole conversion uses `Q3=(3/(4*pi))*Z*R^3*beta3` with `R=1.2*A^(1/3) fm`. For the model range it gives roughly `3–4.5 e b^(3/2)`, not `12–16 e b^(3/2)`. A value of `12–16 e b^(3/2)` would require a different convention or a much larger effective deformation and must not be presented as a generic actinide result.

The fission-resonance experiments are indirect evidence. `232U` reports a third-minimum energy near `3.2(2) MeV` in the barrier analysis, while the eight-dimensional `232Th` calculation gives a shallow depth near `0.36 MeV` and highlights a conflict between the uranium inference and realistic calculations. The worker preserves that conflict; it does not resolve it.
