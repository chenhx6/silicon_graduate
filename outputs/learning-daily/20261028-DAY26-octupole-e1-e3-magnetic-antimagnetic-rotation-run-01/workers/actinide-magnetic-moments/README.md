# Actinide parity-doublet magnetic moments: reproducible toy model

Run:

```bash
python3 nilsson_octupole_magnetic_moments.py
```

The script diagonalizes a four-orbital `K=1/2` neutron Hamiltonian with
explicit `Δl=Δj=3` octupole couplings. It writes
`nilsson_octupole_magnetic_moments.csv` and
`nilsson_octupole_magnetic_moments.json`. The CSV is the graph-ready table:
each row gives `beta3`, branch identity, parity weights, `g_K`, the
parity-sensitive `b0` proxy, and two rotor magnetic-moment formulas.

The calculation is intentionally a sensitivity model. It does not claim a
self-consistent Nilsson, Woods–Saxon, blocked-HFB, QRPA, or GCM result. The
orbital energies and couplings are explicit toy inputs and can be replaced by
a production single-particle basis. The `b0` column is a stretched-basis
proxy with a stated phase convention; it must not be read as an experimental
decoupling parameter. The `225Ra` static moment is an external benchmark,
`mu = -0.7338(15) mu_N`, and is not fitted.

The effective neutron spin factor is `g_s^eff/g_s^free = 0.70`; the JSON
metadata records this choice. The range `0.65–0.75` discussed in the research
note is a model sensitivity range, not a new experimental determination.
