# checkpoint107 primed recall before rare decay and octupole timing synthesis
Same run/session; original 2026-10-22 15:00 Shanghai research deadline. Strongly primed by checkpoints 088–106 and octupole/rare decay synthesis. No blind recall and no independent experimental data.
Core purpose: Connect Day 19 time measurement techniques (Fast Timing, sub-barrier Coulomb excitation stopping integrals) to rare electromagnetic decays and octupole collectivity in knowledge/synthesis/octupole-and-rare-electromagnetic-decay.md:
1. 137Ba competitive double-gamma decay:
   - Fast timing role: sub-ns coincidence gates (LaBr3/CeBr3) suppress random accidentals;
   - Consistency: Walz 2015 2.05(37)e-6 vs Soderstrom 2020 2.62(30)e-6 agree within 1.20 sigma on total branch;
   - Cut sensitivity: symmetric energy-sharing cuts filter out asymmetric E3M1 phase space, causing virtual path inversion.
2. 144,146Ba direct B(E3) Coulomb excitation:
   - Stopping clock is incident beam slowing in target matrix (Nolan Eq 6.2), distinct from recoil stopping;
   - Identical B(E3) = 48 W.u. establishes octupole collectivity while D0 drops by factor 4.3 due to shell-droplet cancellation.
3. 220Rn vs 224Ra pear shapes:
   - Modest Q3 ratio 1.156 (2.15 sigma), but Schiff moment metric Z Q3 Q2 enhanced by 1.72x in 224Ra.
Implement day19_rare_decay_timing_contract107.py.
