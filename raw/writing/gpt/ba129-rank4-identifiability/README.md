# Same-parent consistency checks for the 365-keV transition in 129Ba

Status: **exploratory draft; scientific novelty and experimental closure unproven**.
The package applies an established same-parent reference principle to a specific
legacy-data question. The earlier description of the rank-4 relation as a new
identification method was too strong and has been withdrawn.

The exact relation `A4_target = -(8/3) f_E2 s4 A4_reference` constrains a
product. An independently calibrated nonzero response ratio is needed to infer
`|delta|`; rank four alone does not recover its sign. A separate rank-2 check
and a joint coefficient-space calculation are now included.

The evaluated central values remain a useful diagnostic. Under chosen diagonal
covariance and `s2=s4=1`, the small-minus-large profile-distance contrast is only
`0.0135634`. The branch ordering reverses in the stated correlation sensitivity
family. No experimental root, p-value, confidence interval or collective-mode
assignment is reported.

The original 1977 article's publisher FULL JSON is now available locally, but
its scanned Table 1 remains unavailable. OCR suggests different error scales
from the evaluation; these are retained as a separate sensitivity scenario.
That scenario removes the earlier two-margin rank-4 box non-overlap. The 1978
full text, original yields, covariance and response calibration remain open.

## Reproduce

See `analysis/README.md`. Canonical public summary data and the analysis
contract are in `data/`. Essential calculation outputs are in
`analysis/results/`. Regenerable plotting tables are in `figures/made/data/`.
The manuscript is `main.tex`, with its local compiled `main.pdf`.

`analysis/validate_case.py` checks the exact algebra with standard Wigner
symbols and a separate photon-amplitude calculation, compares projected
residuals with direct GLS, checks numerical refinement and rejects incorrect
parent/row/multipole inputs. These are mathematical and implementation checks,
not publication or experimental certification.

The primary-source archive is documented by the Wiki source page
`knowledge/sources/gizon-1977-ba129-angular-distribution-primary.md`.
Publisher text, PDFs, authentication responses and private data are excluded
from the candidate release.
