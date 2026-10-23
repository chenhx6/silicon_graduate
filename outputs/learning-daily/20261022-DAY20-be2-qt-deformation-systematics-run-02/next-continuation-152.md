# Day20 checkpoint152 continuation

Read run.json first. Same run/session; original 2026-10-23T15:00+08 cutoff; running day20/completed[]/partial[20,21]/next20. No session/daemon restart, mid-run publication, credit or Day22.

152 executable controls on official unedited SIGMA code (SHA256 9e8cd64b844c75fe49c5b7994f500668284ca7390df45ccb2c2e0fb97ae3af6c) compiled with gfortran -O0 -fcheck=all:
1. Pure axial rigid rotor ladders (rigid_j2, rigid_j4, rigid_j6) converge exactly across all J=0,2,4 intermediate couplings with Q2=1, Q4=1, Q6=1, Q3cos3d=1, cos3d=1, var=0.
2. In amplitude-dispersed axial model (Q=1 and Q=2 equal mix, exact delta=0, true angular variance=0), FINT interpolation underestimates M3 (4.4458 vs 4.5), producing apparent cos(3delta)=1.0122 > 1 and negative variance -0.0245, which is zeroed out to 0.0000 by code lines 185-186. Confirms zero angular variance can be an interpolation artifact.
3. Initial failures preserved: sympy dependency, initial table orientation failure, and initial 151 lint schema errors; all repaired, fresh required-checks-152.json mechanical_valid=True (0error/271warning/4064info, 40 writeback pages).

Next: Synthesize A≈130 state-specific lifetime-strength-deformation evidence map across Singh 2016, Petrache 1998, Li 2004, Ionescu-Bujor 1998, Mukhopadhyay 2007/2008, Babra 2019, Klemme 1999, linking to Day 20 matrix deliverables. Research window active until 15:00; under 90min no new sources/cards; 15:00 stop research then final card/report/writeback/checks/H3/publication.

Resume: codex resume 01a16297-c78b-7083-899c-e3a0ac846a67 -C /workspace/wiki -s danger-full-access -a never
