# checkpoint106 primed recall before shape observable timing contract synthesis
Same run/session; original 2026-10-22 15:00 Shanghai research deadline. Strongly primed by checkpoints 088–105 and shape observable matrix history. No blind recall and no independent experimental data.
Core purpose: Connect Day 19 time measurement techniques (DSAM, RDDS, Fast Timing, TDPAD) to the shape-sensitive observable matrix in knowledge/synthesis/shape-observable-matrix.md:
1. Establish the physical clock classification for nuclear shape observables:
   - Transition quadrupole moment Qt / beta2: relies on transition rates 1/tau from DSAM, RDDS, or Fast Timing;
   - Spectroscopic quadrupole moment Q_spec: relies on TDPAD quadrupole interaction frequency nu_Q in lattice EFG;
   - Magnetic g-factor: relies on TDPAD Larmor precession frequency omega_L in external B;
   - Octupole collectivity B(E3): relies on sub-barrier Coulomb excitation yield integrating incident beam stopping.
2. Quantify the 3-regime hierarchy in 131Ce across 5 orders of magnitude in time:
   - Regime 1: TDPAD 9/2- isomer (tau = 127 ns, Qs = 0.92 eb, beta2 ~ 0.094);
   - Regime 2: Plunger/DSAM normal band (tau = 1.235 ps, Qt = 2.26-2.72 eb, beta2 ~ 0.125-0.150);
   - Regime 3: Fast DSAM high-deformation band (tau < 0.2 ps, Q0 = 7.3 eb, beta2 ~ 0.38).
3. Apply the 8-item minimal calibration checklist to eliminate cross-observable confusion between Qs and Qt.
Implement day19_shape_observable_timing_contract106.py.
