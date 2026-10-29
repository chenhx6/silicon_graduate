# Octupole induced IVGDR splitting and low energy E1 EWSR

This worker is a reproducible phenomenological scan for the research note
`knowledge/research-notes/octupole-gdr-splitting-and-low-energy-e1-ewsr-boundary.md`.
It is deliberately smaller than a self-consistent QRPA/RPA calculation.  The
model keeps the usual axial `K=0,1` IVGDR branches, adds a beta3 dependent
two-level doorway mixing to each branch, evaluates the exact center-of-mass
corrected intrinsic dipole identity, and partitions the E1 TRK sum rule.

## Run

```text
python3 octupole_gdr_e1_model.py
```

The script writes `gdr_splitting_scan.csv`, `response_curve.csv`,
`e1_ewsr_partition.csv`, and `results.json` in this directory.  The first CSV
contains the beta3 scan from 0 to 0.20 for `144Ba`, `146Ba`, `224Ra`, and
`226Th`; the second contains normalized Lorentzian response curves at each
listed nucleus's nominal beta3; the third gives the EWSR fraction ledger.

## Equations and interpretation

The exact translationally invariant identity used by the script is

`D0 = e*N*Z/A*(<z_p>-<z_n>)`.

The displacement closure used for sensitivity scans is labelled as a model
assumption in the source code and JSON.  It is not a measurement of a local
proton-neutron displacement.  The E1 sum rule is the requested

`S(E1) = (9/(4*pi))*(hbar^2*e^2/(2m))*(N*Z/A)*(1+kappa)`

with `kappa=0.20`.  For a `K=0` rotor conversion, `B(E1)=3*D0^2/(4*pi)` is used only
to show the equivalent dipole scale required for 0.1%, 0.3%, and 1% of the
sum rule.  For comparison, the Bucher 2017 `146Ba` Table I amplitude
`0.000223 eb^(1/2)` gives `B=4.9729e-6 e^2 fm^2` and a toy low-state share
`8.49e-9` at 1.05 MeV.  This is far below 0.1%; an integrated pygmy band and
one static E1 transition must not be conflated.

## Evidence boundary

Butler and Nazarewicz (1996) support the distinction between cancellation
sensitive E1 moments, collective E3 observables, static reflection asymmetry,
and octupole softness.  Bucher et al. (2016, 2017) provide direct Ba E3 data
and the SCCM occupancy/cancellation interpretation.  Neither source reports
the present GDR scan for Ba, Ra, or Th.  A measured multi-component IVGDR
decomposition would require an energy resolved E1 response and a
self-consistent QRPA/RPA or equivalent calculation; coherent low-energy
interference additionally requires a common final state and a relative phase.
