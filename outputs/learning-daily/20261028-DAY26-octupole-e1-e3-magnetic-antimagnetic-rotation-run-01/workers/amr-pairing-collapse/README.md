# AMR pairing-collapse and J2 control

This worker contains a standard-library-only conditional model for the
frequency dependence of residual proton/neutron pairing after a blocked
two-proton-hole plus two-neutron-particle AMR configuration. It is a
mechanism control, not a full 110Cd/104Pd PNC-CSM, HFB, EDF, or projected
laboratory-frame calculation.

Run:

```bash
python3 amr_pairing_collapse.py
```

The script solves the finite-temperature cranked BCS gap equation on active
residual levels, writes the gap and J2 scans, and records the source ledger.
The core response is deliberately explicit: the mean-field gap scan places
the collapse near 0.50 MeV, while a finite-width susceptibility kernel maps
the softening to `J_core=19.5 -> 45.0 hbar^2/MeV`. This produces a model J2
maximum of about 70.8 hbar^2/MeV at 0.52 MeV and then returns toward the
unpaired baseline. The mapping is the model hypothesis being tested.

Files:

- `amr_pairing_collapse.py`: equations, parameters, solver and SVG writer.
- `pairing_gap_scan.csv`: proton/neutron gaps, blocking metadata and core response.
- `j2_curve.csv`: paired and no-pairing I(omega), J2(omega), and gaps.
- `experimental_ledger.csv`: Roy 2011 110Cd lifetime/B(E2)/Egamma values and Rather 2014 104Pd derived J2 values.
- `results.json`: equations, numerical summary and evidence boundaries.
- `pairing_j2_control.svg`: dependency-free chart of the control curves.

The 110Cd ledger keeps the negative 20--22 finite-difference proxy produced
by the printed 1323 -> 1314 keV sequence. Roy 2011 does not provide a direct
J2 table, so the model peak must not be cited as a measured 110Cd value.
Rather 2014 reports J2/B(E2); multiplying by its B(E2) table gives the
derived 104Pd peak near 63.5 hbar^2/MeV at I=20.
