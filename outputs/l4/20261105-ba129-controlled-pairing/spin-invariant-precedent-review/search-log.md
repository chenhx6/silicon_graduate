# Search coverage and limits

This is a source-definition/precedent audit, not a systematic review or novelty certificate.
The task/collection date is 2026-11-06. The host UTC acquisition interval is recorded
per artifact in the new raw manifest and falls on 2026-11-05. These differing dates
are retained explicitly.

Local search came first:

```bash
rg --files --no-ignore raw/papers | rg -i '(nomura|cline|werner|kumar|henderson|quadrupole|invariant|pietralla|jolos)'
rg -n -i '021301|Nomura.*2017|Werner.*2000|finite.spin|nonzero.spin|non.zero.spin' knowledge/sources knowledge/models knowledge/methods knowledge/concepts -g '*.md'
rg -n -C 14 'q_2|q_3|Werner|Cline|five|band.head' raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.tex raw/papers/gpt/query/20261105-nomura2017-input-audit/arxiv-v2-v4.bbl
```

The existing Nomura2017, Cline1986 and Henderson2020 source pages located actual
originals. Source-page historical review/staging labels were not treated as scientific
authority. PDF identity and formulas were checked against the originals. Page images
were inspected for Nomura2017 p.11, Cline p.698 and Nomura2018 p.9. Additional reading
locations are listed in `source-inventory.json`.

Representative exact web queries used during this audit:

```text
"Werner" "021301" "2000" quadrupole
"Nomura" "014304" "2017" "erratum"
"quadrupole" "invariants" "non-zero spin"
"shape invariants" "Nomura" "J+2"
"014304" "2017" "Nomura" "Comment"
"q-invariants" "J+2"
"q-invariants" "J + 2"
"Signatures of shape phase transitions in odd-mass nuclei" arxiv
"Prolate-to-oblate shape phase transitions in neutron-rich odd-mass nuclei" arxiv
"Triaxiality and the determination" "five observables" arxiv
"quadrupole shape invariants" "finite spin"
"quadrupole invariants" "half-integer"
"Nomura" "014304" "6j"
"Shape-phase transitions in odd-mass" "invariants" "correction"
"Shape-phase transitions in odd-mass" "Erratum"
"Shape-phase transitions in odd-mass" "Comment"
"Nomura" "2017" "invariants" "truncation"
"triaxial projected shell model" "shape invariants"
"Microscopic investigation of E2 matrix elements" nuclei arxiv
"Structure of 128,129,130Xe"
"Unexpected transitional paths" Erratum pdf
"s10050-021-00591-9"
"Shape transitions in odd-mass" "064316" arxiv
```

Source-specific follow-up used author-deposited arXiv copies, the author manuscript
in an institutional repository, journal/publisher pages and Crossref. Some broad
queries produced unrelated material; only identified relevant originals support the
report. The related Bose–Fermi erratum was acquired in full and excluded as a formula
correction because it concerns a funding number.

The Nomura2017 correction check comprises:

- publisher landing page;
- both publisher citing-index pages, yielding 34 unique citing DOI records;
- current Crossref relation/update metadata;
- arXiv version history;
- targeted full-text follow-up on the closest method and same-region papers.

`citation-screen.json` contains the citing-record titles/DOIs and index origins.
Title screening is explicitly distinguished from full-text reading. Index completeness,
unindexed comments, author correspondence and unpublished code are not established.
There is no inference from a query miss or an empty metadata relation to novelty.

The download helpers and `download-batch1.json` through `download-batch6.json`
retain the requested endpoints. The raw manifest records successful bytes,
resolved URLs, size, SHA-256, actual UTC, access scope and failed attempts. Its
contents and the existing original sources are verified by `finalize_evidence.py`.
It does not install software, inspect get-paper, run a fit or change model code.
