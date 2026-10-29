# 144,146Ba E1/E3 SCCM orbital audit

This bounded worker artifact audits the published Bucher 2016/2017 values and the author-level SCCM explanation. It does not run Gogny HFB/SCCM and leaves orbital-resolved dipole kernels as missing data.

## Results

- `144Ba` E3 matrix element report interval: `[0.42, 0.82] e b^(3/2)`.
- `146Ba` E3 matrix element report interval: `[0.45, 0.79] e b^(3/2)`.
- Matrix-element overlap: `[0.45, 0.79]`, Jaccard overlap `0.85`.
- Reported `B(E3;3−→0+)` intervals: `[14,73]` and `[19,69]` W.u.; overlap `[19,69]` W.u., Jaccard `0.8475`.
- `146Ba` SCCM E1 matrix element: `0.00474 e b^(1/2)`; experiment: `0.000223(+10/−8) e b^(1/2)`. Central amplitude ratio: `21.26`; squared strength ratio: about `451.8`.
- Reported neutron orbital parentages and occupancies in `146Ba`: `νh9/2 (K=3/2−, v²=0.40)`, `νf7/2 (K=5/2−, v²=0.27)`, `νi13/2 (K=1/2+, v²=0.20)`. The cited paper gives a collective near cancellation, not independent signed per-orbital dipole contributions.

The E3 intervals are reported asymmetric error ranges. The cited papers do not provide a common formal confidence level or full covariance, so the artifact does not label them formal confidence intervals.
