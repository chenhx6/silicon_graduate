# AMR critical frequency and Landau damping

This worker contains a conditional particle-plus-rotor calculation and a
separable RPA response proxy for a soft scissors mode. It is intended to make
the assumptions, parameter dependence, and evidence boundaries executable.

## Run

```bash
python3 amr_critical_frequency.py
```

The script writes four files:

- `critical_frequency_scan.csv`: scans `V_pinu`, `j_pi`, `j_nu`, and
  `J_core`; the intrinsic result is
  `hbar*omega_c = 3 V_pinu / (2 j_pi)` and the closure spin is
  `I_c = j_nu + 2 j_pi + J_core omega_c`.
- `isotope_systematics.csv`: model rows for 106,108,110Cd and 104Pd, plus an
  explicit missing-evidence row for 102Pd.
- `landau_damping_scan.csv`: one- and two-phonon softening, RPA response, and
  golden-rule width `Gamma = 2 pi g^2 rho_ph(2 Omega_s)`.
- `amr_critical_frequency_results.json`: equations, inputs, evidence ledger,
  and scope warnings.

## Scope

The analytic Hamiltonian is

`E(I,c) = (I - j_nu - 2 j_pi c)^2/(2 J_core) + V_pinu P2(c)`.

The familiar `c = omega/omega_c` relation is the intrinsic shear result. In
this minimal model `j_nu` and `J_core` set the spin offset and the spin at
closure, rather than changing the intrinsic critical frequency. A formula
that puts all four quantities into one universal `omega_c` requires an
additional convention or a microscopic response model and is not source
independent.

With Roy's `omega = omega_rot - omega_sh` convention, the closure frequency
defined from the total-spin rotor term is instead approximately
`hbar*omega_lab,c = (j_nu + 2*j_pi + 1/2)/J_core`; `V_pinu` cancels in that
definition. This is why the note keeps intrinsic and laboratory frequency
conventions separate.

The RPA spectrum uses a small, declared particle-hole list and finite `eta`.
Its rising near-critical width demonstrates Landau phase-space broadening;
it is not a fitted lifetime or a microscopic prediction for a Cd/Pd isotope.

## Evidence anchors

- Roy et al. 2011: local source page `knowledge/sources/roy-2011-cd110-systematics-antimagnetic.md`, printed pp. 323--326 and Table 1.
- Rather et al. 2014: local source page `knowledge/sources/rather-2014-104pd-antimagnetic-arxiv-full.md`, Table 1 and model pp. 4--6.
- Frauendorf 2001: local source page `knowledge/sources/frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei.md`.
