# Actinide beta4--octupole coupling and parity tunnelling

This worker is a transparent reduced model for the `224,226Ra` and
`226,228Th` context. It addresses three linked diagnostics:

1. a symmetry constrained `V(beta3,beta4; beta2)` surface in the requested
   `beta2=0.15--0.20` window;
2. a beta4 dependent two-level surrogate for the
   `pi f7/2 <-> pi i13/2` and `nu g9/2 <-> nu j15/2` Delta-l=Delta-j=3 pairs;
3. exact finite-difference and WKB estimates of the lowest even/odd beta3
   collective splitting along the beta4-minimized path and at fixed beta4.

The values are model inputs and model outputs. They are not a self-consistent
Woods--Saxon/Nilsson, HFB, GCM, or EDF calculation, and no beta4 value is
claimed as an experimental measurement for the four target nuclei.

## Run

```bash
python3 beta4_octupole_tunneling.py
```

The script writes:

| File | Content |
| --- | --- |
| `parameters.json` | standalone parameter manifest and grid definitions |
| `results.json` | formulas, parameters, summaries, checks, and evidence boundary |
| `pes_grid.csv` | full `(beta2,beta3,beta4)` energy grid |
| `mep_path.csv` | beta4-minimized path for every beta3 grid point |
| `fixed_beta4_scan.csv` | barrier, beta3 minimum, exact splitting and WKB scan |
| `mep_parity_splitting.csv` | parity result on the beta4-minimized path |
| `orbital_beta4_scan.csv` | pair spacing, overlap proxy, avoided-crossing mixing |
| `sensitivity_summary.csv` | positive-beta4 slopes and reference values |
| `schrodinger_grid_convergence.csv` | 321/641/1281 point grid check |
| `*.png` | optional PES, splitting, and orbital-response plots |

## Model contract

Reflection sends `beta3 -> -beta3` while leaving `beta2` and `beta4` unchanged.
The lowest allowed local coupling used here is therefore
`-G234 beta2 beta3^2 beta4`; the sign of `G234` is a convention/parameter and
is not fixed by symmetry. With `G234>0`, positive beta4 lowers the beta3
quadratic coefficient at fixed beta4. Minimizing beta4 instead gives

```text
k4 beta4 + u4 beta4^3 = G234 beta2 beta3^2,
```

so the MEP has positive beta4 at finite beta3. A zero-coupling run recovers
beta4=0, and the saved checks verify reflection symmetry and sign reversal.

For an orbital pair `a,b`, the surrogate uses

```text
H_tau = [[epsilon_a, kappa3 beta3 O_tau],
         [kappa3 beta3 O_tau, epsilon_b]],
delta_tau = epsilon_b-epsilon_a,
O_tau = O0 [1 + eta2(beta2-0.175) + eta4 beta4].
```

The eigenvalue gap is
`sqrt(delta_tau^2 + 4(kappa3 beta3 O_tau)^2)`, and the reported mixing
probability is the lower-state two-level admixture. Positive beta4 was chosen
to reduce `|delta_tau|` and increase the overlap proxy for both representative
pairs; a different Woods--Saxon/Nilsson parameterization can give a different
sign or size.

The collective Hamiltonian is

```text
H3 = -(hbar^2/2B33) d^2/d beta3^2 + V_MEP(beta3).
```

The exact result uses a symmetric three-point finite-difference Hamiltonian and
classifies the first two eigenvectors by beta3 reflection. WKB uses the same
ground-state energy and the central forbidden interval. `H2_OVER_2B33` is an
effective dimensionless-coordinate kinetic coefficient; its numerical value is
not a measured collective mass.

## Representative output

At `beta2=0.175`, moving the fixed beta4 slice from `0` to `+0.04` gives:

| quantity | beta4=0 | beta4=+0.04 |
| --- | ---: | ---: |
| `beta3_min` | 0.20795 | 0.21331 |
| `V_barrier` (MeV) | 0.15417 | 0.17603 |
| exact `Delta E(odd-even)` (MeV) | `1.109e-7` | `2.528e-8` |
| WKB `Delta E` (MeV) | `1.074e-7` | `2.411e-8` |

Thus this chosen positive-beta4 coupling raises the central barrier by about
14% and lowers the model parity splitting by about 77%; the minimum shifts
outward by about 2.6%. On the beta4-minimized path the same beta2 slice has
`beta3_min=0.21015`, `beta4*=0.01187`, `V_barrier=0.15733 MeV`, and exact
`Delta E=8.30e-8 MeV`. The 321/641/1281 grid values of that splitting differ by
less than 0.3%.

At the same beta2, evaluating each orbital pair at its fixed-beta4 minimum
gives:

| pair | quantity | beta4=0 | beta4=+0.04 |
| --- | --- | ---: | ---: |
| `pi f7/2--pi i13/2` | `delta_epsilon` (MeV) | 0.260 | 0.156 |
|  | overlap proxy | 0.920 | 0.986 |
|  | mixing probability | 0.378 | 0.432 |
| `nu g9/2--nu j15/2` | `delta_epsilon` (MeV) | 0.180 | 0.112 |
|  | overlap proxy | 0.970 | 1.020 |
|  | mixing probability | 0.426 | 0.457 |

The bare opposite-parity spacing shrinks while the finite-beta3 avoided-crossing
gap grows because the off-diagonal octupole matrix element also grows. This is
the intended microscopic mechanism in the surrogate, not a claim that the
adiabatic spacing in a production calculation must grow for positive beta4.

## Evidence boundary

The long-lived interpretation and source locators are in
[`knowledge/research-notes/actinide-hexadecapole-octupole-coupling-and-tunneling-splitting.md`](../../../../../knowledge/research-notes/actinide-hexadecapole-octupole-coupling-and-tunneling-splitting.md).
Existing local evidence identifies the `Delta l=Delta j=3` orbital mechanism
and strong-octupole context, while Gaffney's `224Ra` Coulomb-excitation result
and the Gogny Ra/Th mapping retain the static-versus-soft interpretation
boundary. The model output cannot supply a beta4-resolved experimental PES,
pairing response, angular-momentum projection, or a measured absolute
`0+--0-` energy in any target nucleus.
