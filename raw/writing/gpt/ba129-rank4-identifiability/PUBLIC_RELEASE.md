# Public release plan

The package is an exploratory local draft. Mathematical checks have passed;
publication-level novelty and experimental closure remain unproven. It is not a
publication authorization and does not grant permission to redistribute
copyrighted source PDFs or unpublished data.

## Candidate release

The candidate release consists of the normalized public summary CSV, the
self-contained analysis script, JSON result, figure generator, regenerable
figure, manuscript source, bibliography and the claim ledger. The exact
inventory and SHA-256 values are in
`sources/public-release-manifest.json`.

## Evidence boundary

The case study uses evaluated public summary coefficients from ENSDF.
`data/input-contract.json` keeps the evaluated and provisional OCR error-scale
scenarios distinct; `analysis/companion_profile.py` profiles both angular ranks
in coefficient space under explicitly chosen covariance matrices. It does
not reconstruct the original 1977/1978/1992 spectra, detector response,
finite-angle corrections, feeding, gate acceptance or coefficient covariance.
The relation is therefore reported as a conditional identifiability gate.

The release excludes publisher full-text JSON, first-page PDFs and authentication
responses. The manuscript must retain the following boundaries:

- the 2024 \(^{129}\)Ba paper's large-root result is an attributed
  reanalysis result, not a new measurement;
- \(f_{E2}\) is a radiative \(M1/E2\) subspace fraction, not an absolute
  \(B(E2)\);
- the same-parent \(A_4\) relation requires matched postselection,
  coefficient conventions, reference purity and a positive, characterized
  \(s_4\);
- quoted marginal error boxes are not joint confidence regions;
- the calculation does not classify wobbling, signature partner or tilted
  precession.

## Release gates

1. Fill final author, affiliation, funding, contribution and conflict
   statements.
2. Select a permanent public archive and license for the normalized data and
   code.
3. Perform paper-use claim review against the archived source locators.
4. Establish sufficient scientific novelty or new physical information beyond
   the already established same-parent reference method.
5. If the paper is upgraded from a methods/readiness paper to an experimental
   reanalysis, obtain the original response, gate, purity and covariance
   inputs and rerun both mixing-ratio branches.
