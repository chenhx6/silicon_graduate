# Public summary input

`ba129_same_parent_A4.csv` is a normalized two-row transcription of the
evaluated public ENSDF objects `129056001` and `129056013` (2014 evaluation
version). It contains the two transitions from the same 643.6-keV
\(13/2^-\) level that are needed for the conditional rank-4 companion-line
test:

- the 364.7-keV line, labelled 365 keV in the modern \(^{129}\)Ba discussion,
  is treated as an \(M1+E2\) target;
- the 461.6-keV line is the evaluated \(E2\) companion reference.

The values are public evaluated summary coefficients, not recovered event
counts or a new measurement. The source objects, raw text files, hashes and
locators are recorded in the Wiki source page
`knowledge/sources/nndc-2014-129ba-365-coefficient-records.md`. The article
analysis deliberately does not claim that the two rows share identical
postselection, finite-acceptance correction, higher-multipole purity or
covariance; those are the conditions being audited.

The CSV is therefore suitable for redistribution as a normalized analysis
fixture once the manuscript's final license and archive decision is made.

## Version-sensitive input

`input-contract.json` binds the canonical coefficients to the actual archived
ENSDF text and its exact line locators. It also binds a separate error-scale
scenario to publisher FULL JSON of Gizon1977. The latter OCR suggests larger
margins for three entries. The scan table is still unavailable, so evaluated
means and signs are deliberately retained and the alternate scales are not
advertised as corrected primary measurements. The two scenarios are never
pooled as independent experiments.

The CSV now carries `parent_id`; loaders reject duplicate rows, different
parents or spins, unsupported multipole hypotheses, nonfinite numbers and
nonpositive errors. A zero reference A4 is rejected by the ratio diagnostic;
the coefficient-space formalism itself does not require division by it.
