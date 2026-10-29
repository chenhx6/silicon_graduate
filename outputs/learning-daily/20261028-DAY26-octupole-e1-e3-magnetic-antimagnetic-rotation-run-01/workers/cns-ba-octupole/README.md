# Reduced CNS Ba octupole worker

This worker evaluates a transparent, CNS-inspired macro-microscopic surrogate for
`144Ba`, `146Ba` and exploratory `148Ba` on a grid in `(beta2, gamma, beta3)`
for `I=0..24 hbar`. It is a numerical sensitivity study, not a self-consistent
Nilsson-Strutinsky or EDF calculation.

## Run

```bash
python3 cns_ba_octupole_model.py
```

The script uses Python 3 standard-library modules. If matplotlib is installed it
also writes the PNG path figure. The complete grid has 337,500 rows (three
nuclei, 25 spins, 20 beta2 values, 9 gamma values and 25 beta3 values).

## Model

The minimized energy is

```text
E = E_LD(beta2,gamma,beta3) + E_shell(beta2,gamma,beta3,I)
    + I(I+1)/(2 J_eff(beta2,beta3)) + E_align(beta3,I).
```

`E_LD` is a local Yukawa-plus-exponential-inspired liquid-drop expansion. The
shell term is a smooth Nilsson shell-coherence surrogate centered on the
`Z=56`, `N=88-90` octupole window. `J_eff` increases with beta2 and beta3, so
the rotational term gives a centrifugal stabilization tendency. The explicit
alignment term and a spin-dependent reduction of shell coherence represent the
competing high-j (`nu h9/2`, `nu i13/2`, `pi h11/2`) alignment mechanism. The
critical-spin parameters are declared in the script and are assumptions, not
fitted observables.

## Files

- `cns_ba_octupole_model.py`: source and parameter manifest.
- `cns_ba_energy_grid.csv`: every grid point and energy component.
- `cns_ba_minima.csv`: optimized `(beta2,gamma,beta3)` path for each isotope and spin.
- `cns_ba_staggering.csv`: model parity displacement `S(I)` for `I>=1`; `I=0` is undefined.
- `cns_ba_results.json`: parameters, grid definition, minima, staggering and source anchors.
- `cns_ba_octupole_paths.png`: beta3 path and parity-displacement plot when matplotlib is available.

The model path peaks around `I=6-10` and then decreases after the prescribed
alignment onset. In the baseline parameters the onset is earlier for `144Ba`
(`I_c=12.5`) than for `146Ba` (`I_c=14.0`), an explicit testable hypothesis
for the N=88 to N=90 shift. The synthetic `S(I)` decreases at low spin and
reopens once alignment has reduced beta3. These trends are model outputs only.

## Evidence boundary

The experimental anchors are Bucher 2016 (`144Ba`) and Bucher 2017 (`146Ba`):
both report direct `B(E3;3- -> 0+)` near 48 W.u., while E1/D0 varies strongly.
The 144Ba spectrum reaches about `10 hbar` in the observed lines and its GOSIA
network extends to `14+`/`15-`; the 146Ba yield network reaches `10 hbar` in
the positive sequence and `9 hbar` in the negative sequence, with observed
E1 decays mainly from `3-` and `5-`. The papers do not provide a complete
absolute E1/lifetime ledger through `I=24`.
Butler and Nazarewicz 1996 supplies the historical high-spin octupole and
parity-displacement framework. The existing Wiki source page for Li and Wang
2024 reports a separate PC-PK1 cranking calculation that keeps `beta30` near
0.128 to about `I=24 hbar` but omits pairing and parity projection. Therefore
the present worker does not claim that alignment-driven quenching is an
established experimental result in Ba.
