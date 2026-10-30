# Qi09 independent representation audit — worker qi-review-005

Scope: `system/scripts/day24_qi09_projection_grid.py`, the fixed official-author EPS/TeX files, the stored arXiv v1 PDF, existing `qi09-projection-grid-003.json`, and QI09-D24-001–003 plus project-map lines 167–173. No shared canonical file was changed. No PostScript, TeX or author program was executed. The independent Python calculation reads literal numeric records and the existing PDF through PyMuPDF; it does not import or call the reviewed script.

## Severity-ranked result

- Critical: **0 identified** in the assigned scope.
- Important: **0 identified** in the assigned scope.
- Minor correction requests: **0**. The implementation is deliberately specific to three content hashes; its limited PostScript parser must remain scoped that way. The following are verification boundaries, not defects already demonstrated in this fixed input.

1. **Conditional representation arithmetic, not producer uncertainty.** Reviewed script lines 40–45 and 82–89 correctly calculate a coordinate-rounding envelope under an explicit independent ±0.5 drawing-unit assumption. The source does not establish Origin's original quantization algorithm, probability covariance, physical uncertainty or a confidence interval. Existing script limits at 116–120 and source claim QI09-D24-002 retain that distinction. The bounds are conservative corner extrema of `0.3 * (n*y0 - sum(yj))/(y0-yend)` with positive denominator, allowing shared baseline/endpoint errors and separate marker ordinate errors. Every marker ordinate can take the same extremal sign for the sum, so replacing its total error by ±n/2 is valid under that declared box model.
2. **The parser is not a general PostScript interpreter.** Script lines 22–37 do not implement graphics-state stacks, transformations, path-clearing/filling/closing, text programs or clipping. For the actual fixed EPS, an independent restricted-state audit traced the literal numeric `gs/gr`, `sw/rgb`, `sc/tr/ro/concat`, and temporary marker matrix sequences. The data markers are unaffected by the ignored text/font geometry and all 690 are independently recovered with the same attributes. Examples: EPS lines 1350–1354 establish the drawing transformation; lines 1517–1529 show two marker paths and the temporary `mtx cmtx mtx smtx` stroke matrix; the latter changes the stroke CTM after path construction and is restored by `smtx`. The independent state and temporary-matrix stacks both end at depth zero. A different EPS would require renewed operator/state inspection, even if marker counts coincidentally matched; the existing fixed SHA checks at script 48–51 prevent silently accepting such a different file.
3. **No producer folding, interpolation or phase reconstruction.** `paper.tex` 403–419 provides the one-axis marginal formula and gamma-sector substitutions; 421–459 supplies the author's Ki=0/Ks=0 language and model interpretation. The plot alone cannot identify how the producer combined signed-K components, binned/smoothed values, or assigned phases. Its positive-half-integer samples and unit-sum compatibility do not establish a unique folding convention. The existing QI09-D24-002 and project-map 171–173 already preserve this boundary. Nothing here independently re-solves the PRM or proves/excludes static chirality or two-dimensional tunneling.

## Direct numeric checks

| Check | Independently observed |
|---|---|
| PDF SHA256 | `248546abd4a1d1597bf9ddf39cfffd5f09604802704204f0ff61647bbdb19346` |
| Fig5 EPS SHA256 | `728a1b079695dbef66aa9caf3730df372180848ca95ccb9b10af66af66b7b8a0` |
| TeX SHA256 | `aaab1da6ab07275330e7d37bf25eabc41d74e1ae3992da205154452eb75aab76` |
| Author archive | 187831 bytes; SHA256 `9e3e5149acc47b3c6a82b922f95726b66032dcaa3df0694afc10fab3584c4707`; exactly 12 regular files with safe flat names: paper.tex, elsarticle.cls, ten EPS files |
| Data-mark counts | 690 zero-width line markers: 345 red + 345 blue |
| Series | 36: l/i/s × A/B × six spins; per axis/band counts 23,21,20,19,17,15 for 45/2,41/2,39/2,37/2,33/2,29/2 |
| K grid | All 36 series consistent with `.5,1.5,...,I`; maximum absolute grid residual `0.06684643769514675 K` (l/B, I=39/2) |
| Drawn probability sums | `[0.9915441176470589, 1.004059040590406]`; matches existing JSON to <1e-12 |
| Conditional rounding envelopes | All 36 contain 1; union of envelope extremes `[0.9683823529411764,1.02619926199262]` |
| PDF color/order identity | All 690 markers match one-to-one in source draw order and RGB identity |
| PDF marker-center affine residual | `0.002493573465017107 pt` maximum; affine fixed by three black-frame points, without data-marker fitting |
| PDF individual-endpoint affine residual | `0.0025510226229243926 pt` maximum, also below the script's 0.005 pt representation tolerance |
| Existing control count | 117 entries, all true in stored result; independent check does not treat that count as 117 independent scientific evidences |

The probability calibration is independently visible in EPS 1394–1453 (horizontal 0,4,...,24 and ordinate 0.1/0.2/0.3 labels), with ticks in 1454–1516. The baseline at `(292,2466)` and the P=0.3 endpoint `(236,2195)` are repeated as a frame/left-axis pair at 1514–1516; intermediate major ticks occur at `(274,2376)` and `(255,2285)`. The other columns repeat the same labels; the six stacked frames use the same probability scale with integer coordinate rounding. The independent computation solves each 2D K/P basis rather than copying the script's shear-subtraction expression. The largest recovered ordinate is about 0.3022140, so 0.3 is a calibration tick/axis endpoint, not a probability truncation bound.

The original PDF page 16 was rendered and inspected (`pdf-page16.png`). The row labels support the script's 45/2 → 41/2 → 39/2 → 37/2 → 33/2 → 29/2 ordering; the legend confirms red=A, blue=B, and l/i/s column order. Counts cover the full expected positive grid through I within the coordinate residual; there is no drawn literal K=0 marker in these identified series.

## Missing/clipped data checks

- EPS 1335 installs rectangle `[0,0,763.71,1112.77]` before the figure transformations. All data-marker endpoints, transformed from literal path coordinates at path construction, lie within `[97.3430274,307.5771042]`–`[660.4953068,746.4176404]` in EPS point coordinates, inside that clip.
- `paper.tex` 612 uses `bb=0 230 710 800`; all those endpoints also lie inside this explicit figure crop.
- PyMuPDF extended drawing records expose PDF clip rectangle `[120.8400040,65.8699341,517.2160034,643.4129639]`. All data-marker endpoints lie within `[171.3630066,256.0120239]`–`[463.6459961,483.7760010]`, inside the PDF clip and page rectangle.
- These checks rule out clipping of the identified 690 drawn data markers by these three bounds. They cannot prove that the author plotted every original producer datum, or recover an unplotted negative-K distribution. The visible positive grid has the expected complete per-spin sample count.

## Claim-by-claim scope

- **QI09-D24-001:** Stored archive hash, size, twelve regular members, and absence of separate PRM jobs/wavefunction/experimental-data members verified. Historical HTTP 200, response MIME, and official network retrieval provenance were not independently re-requested in this audit. The preserved local bytes and paper identity match the supplied expected versions.
- **QI09-D24-002:** Counts, grouping, half-integer grid, P=0.3 calibration, conditional normalization compatibility, color/order/native PDF identity and absence of clipped identified markers independently verified as above. Interpretation remains limited to representation.
- **QI09-D24-003:** TeX 296–305 fixes beta=.235, gamma=22.4 and numerical J0=29 with energy fitting; 345–354 explicitly preserves underestimated interband E2; 439–459 states the 39/2, 76-keV and subsequent vibrational interpretation; 528 cites Almehed/Frauendorf arXiv0709.0969v1. These are author model statements. A numerical PRM reproduction, experimental phase boundary, or word-for-word Almehed v1/v2 comparison was not performed.

## Files produced

Only files inside `outputs/learning-daily/20261026-DAY24-chirality-vibration-static-partner-bands-run-01/workers/qi-review-005/` were created:

- `independent_audit.py`: independent restricted-state/vector and normalization calculation.
- `independent-results.json`: per-series numbers, clipping bounds and hashes.
- `archive-manifest.json`: archive size/hash and regular-member manifest.
- `pdf-page16.png`: freshly rendered stored-PDF figure page.
- `review.md`: this review.

No Git mutation, run/session creation, learning-credit update, raw/PLAN/Bib change, configuration change, or shared scientific-page edit occurred.
