# Octupole--chiral static magnetic moments and K=1/2 decoupling

This worker is a synthetic forward model for a four-state local basis
`(chi,p) = (+,+), (-,+), (-,-), (+,-)`.  It scans spin `I`, octupole mixing
`beta3`, and an effective octupole barrier depth.  The model reports the core
term `g_R I`, intrinsic quasiparticle term, parity-dependent K=1/2 decoupling
term, chiral/parity terms, and the `chi*p` interference term separately.

## Run

```text
python3 octupole_chiral_magnetic_moments.py
```

The script requires NumPy.  Matplotlib is optional; if present it writes an
SVG plot.  All generated values are model outputs in `mu_N` and MeV, not
measurements of `78Br` or `133Ce`.

## Files

- `octupole_chiral_magnetic_moments.py`: model, scan, checks, and output writer.
- `magnetic_moment_network.csv`: one row per local state, spin, `beta3`, and barrier.
- `magnetic_moment_network.json`: parameters, records, state ordering, and checks.
- `magnetic_moment_plot_data.csv`: compact plotting data for the reference slice.
- `magnetic_moment_network.svg`: reference-slice plot when Matplotlib is available.

## Algebra and limits

For the stated order, the local diagonal moments satisfy

`(mu1 - mu2) + (mu3 - mu4) = 4 mu_chi_p`.

Thus `mu1 - mu2 = -(mu3 - mu4)` only when the chi--parity interference
coefficient vanishes.  The K=1/2 convention used by the script is

`E_dec = A_rot b0^p (-1)^(I+1/2) (I+1/2)`

with `b0^p = b0_base + p b0_mix sin(2 theta)` and
`theta = 0.5 atan(2 beta3 v_oct / delta_eps)`.  The magnetic decoupling term is
an explicitly labelled phenomenological proxy, not a universal identity.
