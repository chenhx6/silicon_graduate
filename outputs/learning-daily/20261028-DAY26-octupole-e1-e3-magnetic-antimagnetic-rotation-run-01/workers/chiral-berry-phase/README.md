# Berry phase and quantum geometry of a chiral--octupole quadruplet

This worker is a reproducible, standard Python plus NumPy toy calculation for
the research note
`knowledge/research-notes/octupole-chiral-berry-phase-and-topological-gap.md`.
It is a conditional symmetry model, not a fit to `78Br`, `130Cs`, `133Ce`, or
`135Nd`.

Run from this directory:

```bash
python3 chiral_berry_phase_model.py
```

The script writes:

- `berry_curvature_metric_grid.csv`: trace Berry-curvature tensor and quantum
  metric on an `(hbar*omega, beta2, beta3)` grid;
- `berry_loop_accumulation.csv`: gauge-invariant non-Abelian Wilson-link phase
  along a closed rotation/deformation loop;
- `dynamical_vs_geometric_phase.csv`: direct `-integral E(t)dt/hbar` values for
  several traversal periods, alongside the same period-independent geometric
  Wilson phase;
- `spectrum_topological_perturbation.csv`: declared two-path tunnelling-gap and
  `S(I)` proxy with the loop phase;
- `e1_m1_branch_ratio_proxy.csv`: E1/M1 interference proxy with the correct
  parity selection rules;
- `results.json`, `chart_data.json`, and two standalone SVG chart files.

The localized basis is `|L,+>`, `|R,+>`, `|L,->`, `|R,->`.  The Hamiltonian
uses two Pauli spaces, synthetic tunnelling amplitudes, a cranking term, and a
weak chirality--octupole coupling.  The lowest two eigenstates define the
non-Abelian subspace.  For a projector `P`:

```text
F_mn = i Tr[P (d_m P d_n P - d_n P d_m P)]
g_mn = 1/2 Re Tr[(d_m P)(d_n P)]
```

The loop phase is the determinant phase of the Wilson product, with the sign
corresponding to `A = i U^dagger dU`.  A smooth nonzero curvature is not a
quantized Chern number.  A physical nuclear claim would require a microscopic
cranked EDF/PRM/GCM calculation, an open gap over a closed surface, and
partner-resolved electromagnetic data.  The gap and branch-ratio outputs are
therefore labelled proxies and must not be read as measured values.
