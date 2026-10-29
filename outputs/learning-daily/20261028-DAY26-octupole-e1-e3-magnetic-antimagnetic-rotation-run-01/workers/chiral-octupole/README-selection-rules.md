# Chiral--octupole quadruplet selection-rule worker

This worker adds the discrete-symmetry and dimensionless-criterion layer to
the pre-existing four-state toy model in this directory. It is deliberately a
synthetic model, not a fit to `78Br`, `131Ba`, `134Pr`, or any other nucleus.

## Reproduce

```bash
python3 chiral_octupole_selection_rule_matrix.py
```

The script writes:

- `chiral_octupole_selection_rule_matrix.json`: D2/simplex definitions,
  projected operator basis, selection-rule rows, and numeric diagnostics;
- `chiral_octupole_selection_rule_matrix.csv`: the channel-level selection
  rule matrix;
- `chiral_octupole_dimensionless_criteria.csv`: synthetic
  `B(M1)/B(E1)`, reduced-width, `B(E2)`, and cross-channel suppression
  diagnostics for `I=10..14`.

The dimensionless quantities use fixed multipole-specific Weisskopf
normalizations. Energies and reduced amplitudes are synthetic. The M1/E2
interference number is an angular-distribution/polarization amplitude proxy;
distinct multipoles add incoherently to an unpolarized total gamma width.
