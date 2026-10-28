# TAC frequency/unit sensitivity audit 031

**Scope.** Conditional arithmetic from Olbratowski 2002 v1 Eqs. (2)–(7), compared with Starosta 2001 Table I. No HF or 3D-TAC rerun was performed. Day27 remains an uncredited preview.

## Source quantities

| Quantity | Value | Status |
|---|---:|---|
| Experimental 132La doublet displacement | ≈0.37 MeV | Starosta Fig. 3, PDF p. 3 |
| Starosta 132La 3D-TAC barrier | 12 keV | Table I, PDF p. 4 |
| Olbratowski frozen-gyro ℏωc | 0.514639 MeV | conditional arithmetic from Eqs. 6–7 |
| Olbratowski HF aplanar onset | 0.6 MeV | source model result, PDF p. 3 |
| Olbratowski planar threshold ℏωthr | 1.282267 MeV | Eq. 5, different branch |

These values are different observables or model outputs. None is a measured critical frequency.

## Unit audit

With (s) in ℏ and (J) in ℏ²/MeV, (s/(J_m-J_k)) has units MeV/ℏ. Therefore (ℏomega_c) is in MeV and (I_c=J_momega_c) is in ℏ. The latter is a continuous classical length, not an experimental quantum-spin threshold.

## Local sensitivity

Baseline input: (J_s,J_m,J_l=(8.5,31,20),ℏ^2/mathrm{MeV}), (s_s,s_l=(5.43,5.00),ℏ). A ±10% one-parameter scan gives:

| Perturbed input | −10% ℏωc (MeV) | +10% ℏωc (MeV) |
|---|---:|---:|
| (J_s) | 0.510578 | 0.519150 |
| (J_m) | 0.692040 | 0.413205 |
| (J_l) | 0.454060 | 0.605709 |
| (s_s) | 0.503773 | 0.526388 |
| (s_l) | 0.474971 | 0.555195 |

Within this conditional scan, (J_m) dominates the local frequency response. This is a sensitivity result for the frozen model, not an uncertainty on the original HF calculation.

## Gamma convention

Starosta uses (gamma=32^circ) in a hybrid potential; Olbratowski reports approximately (gamma=45^circ) for its HF solution. Under an illustrative irrotational relation (J_kproptosin^2(gamma-2pi k/3)), the unscaled triplets are ((0.280814,0.998782,0.220404)) at (32^circ) and ((0.500000,0.933013,0.066987)) at (45^circ). Axis permutation and scale are unspecified, so these values cannot be mapped onto either source’s (J_s,J_m,J_l).

See the full machine-readable rows in `tac-frequency-unit-sensitivity-031.json` and the source-grounded note in `knowledge/research-notes/tac-frequency-unit-boundary.md`.
