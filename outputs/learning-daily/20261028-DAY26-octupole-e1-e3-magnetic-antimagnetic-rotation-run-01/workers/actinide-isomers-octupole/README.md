# Actinide isomer K-mixing and octupole selection-rule worker

Run from this directory with:

```text
python3 actinide_isomer_k_mixing.py
```

The script writes `k_mixing_scan.csv`, `results.json`, and `chart_data.json`.
It diagonalizes a finite intrinsic-K basis and scans beta3 from 0 to 0.20 for
four transverse-mixing scales `eps_K`. E1, E2, M1, and E3 strengths and rates
are normalized sensitivity outputs. Radiation constants use E_gamma in MeV
and rates in s^-1; internal conversion is omitted.

The model keeps a necessary symmetry boundary explicit: an axial beta3 Y30
field breaks reflection symmetry but commutes with the axial rotation
generator, so beta3 alone does not mix K. `eps_K` represents Coriolis,
triaxial mu!=0, or octupole-phonon coupling and must be nonzero for the
bypass channel. The output is a toy model, not an EDF calculation, not a fit
to 225Ra, and not a prediction of 229Th or 234U lifetimes.

The 225Ra reference line is the evaluated 31.50-keV E1 with B(E1)=0.00081(20)
W.u. from `knowledge/sources/nndc-2009-ra225-adopted-parity-doublet.md`.
The worker intentionally does not infer a total lifetime from that value
because internal conversion and the complete branching scheme are required.

Current NNDC NuDat adopted-level pages provide the comparison anchors used in
the note: 229Th has a 5/2+ ground state and a 3/2+ state at 8.355733554 eV
(same parity), while 234U has a 6- K=6 bandhead at 1421.275(45) keV with
T1/2=33.5(20) microseconds. These values are context anchors, not inputs to
the toy scan.
