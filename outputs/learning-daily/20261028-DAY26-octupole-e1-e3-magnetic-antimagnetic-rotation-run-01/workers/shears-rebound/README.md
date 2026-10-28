# 135Pr shears reopening worker

This worker contains a transparent geometry and crossing proxy for the
135Pr negative-parity MR question. It is not a TAC or TAC-RMF implementation.

## Run

```bash
python3 shears_rebound_model.py
```

The command writes `shears_rebound_model_results.json`.

## Evidence anchors

- `knowledge/sources/garg-2015-135pr-magnetic-rotation.md`: 135Pr Band 3, hybrid TAC 3qp/5qp comparison, crossing near 0.37 MeV and 33/2−, Fig.7 relative strength trend, no lifetime.
- `knowledge/sources/garg-2019-135pr-polarization-erratum.md`: corrected 747.5/813.3-keV polarization asymmetries and mixed M1+E2 assignments.
- `knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md`: neighboring 137Pr comparison with the same nominal pi(h11/2)(g7/2)^2 nu(h11/2)^-2 5qp route.
- `knowledge/research-notes/pr135-shears-dynamics-bandcrossing-rebound.md`: evidence matrix, derivation, TAC/CDFT boundary and self-audit.

All strengths in the JSON are normalized. No absolute B(M1), B(E2), or
experimental J^(2) is inferred.
