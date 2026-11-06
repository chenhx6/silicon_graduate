# Focused manuscript revision — 6 November 2026

The current `main.pdf` is a 12-page revised EPJ A candidate. It integrates
the completed rigid-charge control and the separate isomer applicability test,
with independent replay packages for those calculations and the source-energy
comparison. It has not been submitted.

The central claim remains singular: a diagnostic converged within one
intermediate-spin channel can respond strongly to angular coupling, so its
evolution alone does not establish a change of intrinsic charge geometry.

## What changed and why

- The rigid-charge 20° counterexample is now the first Results subsection.
  Its operator identities establish fixed geometry independently of the
  initial eigenstate. The separate IBFM intervention then resolves the
  redistribution of static strength and signed cubic paths.
- The chain table now carries q2 as well as coverage and ratios. The
  redundant chain-trend figure was removed from the main text, while its
  original file remains available. Three core figures carry the argument.
- All five conditional calibration branches remain in the appendix.
  Their conclusion-changing implications, including complete-ratio domain
  failures, remain in the main text.
- The conditional 137Ba isomer failure is explicit in the Discussion.
  All 28 strengths,14 photon-rate sums and84 branches remain in the data.
  Model energies, mapping uncertainty and the lifetime/B(E2) dependence
  are stated; this is neither a full-IBFM rejection nor an author-error claim.
- The135/137Ba displayed source-spectrum comparison is summarized in Methods.
  The absence of19/2 source points and author electromagnetic reconstruction
  is preserved.
- The book citation now describes the actually consulted1998 World Scientific
  reissue. Its publisher/location and original1975 edition were checked
  against local PDF p6.

The previous text/PDF is preserved in `previous-text/`, with hashes in
`baseline.json`. The original 45-file data manifest is unchanged. New files
are separately registered in `data/revision-v2/manifest.json`.

## Completed verification

The three standalone replays use unchanged scientific producers or declared
adapters. They do not need the original Wiki for their numerical comparisons.
Re-extraction of the source figure still requires its actual original; this
was not silently claimed as a package-only verification.

| Replay | Scope | Comparison |
|---|---|---|
| Rigid-charge control | Five field strengths,20 proxies,full q2/q3 and independent controls | All compared values agree; maximum numerical difference0 |
| Isomer check | Four energy mappings,28 strengths,14 sums,84 branches | All compared values agree; both CSVs byte-identical |
| Source spectrum | Twelve frozen source points and kernel energies | JSON/CSV byte-identical; source differences1.896/3.128keV retained |

The actual receipts are in the packages and in
`outputs/l4/20261106-odd-ba-manuscript-revision/`.
The independent editorial/scientific review has no unresolved must-fix within
its text-level scope. It did not independently rerun the calculations; those
are verified separately above. A missing plus sign in an intermediate
Hamiltonian transcription was corrected before finalization, without a code
or data change.

All 12 PDF pages were rendered and visually inspected. Overfull boxes,
undefined references and missing characters are absent. Narrow-column
underfull warnings remain recorded and were visually checked.
See `latex-check.json`; approximate before/after prose counts and three-figure
allocation are in `word-count.json` and `argument-map.md`.

## Remaining boundary

The manuscript supports a bounded model-mechanism contribution. It does not
establish actual Ba intrinsic shapes, rigidity, collective-mode assignments,
the original authors' electromagnetic calculation, or a first-in-literature
general theorem. Internal review and reproducibility do not predict acceptance.

Human author identities, affiliations, contributions and final accountability
statements are still placeholders. The permanent public data/code destination
has not been assigned. These are unresolved submission items, not tasks to
fill with invented details. The full-library research goal also remains
unfinished.


Final bounded closeout: the three-source original-text comparison is complete. General geometry/inertia separation is explicitly credited in the main Discussion. The candidate remains incremental and is not certified for priority or journal-level significance. See ../final-evidence-closure.md. The associated Mikhailov/CAP/PES corrections are outside the article producers. The broader library mission remains incomplete and is not counted as achieved by this closeout.
