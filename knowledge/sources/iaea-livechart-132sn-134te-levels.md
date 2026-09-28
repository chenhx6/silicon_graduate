---
type: source
title: "IAEA LiveChart/ENSDF adopted levels for 130Sn, 132Sn, 134Sn and 134Te"
aliases: [132Sn LiveChart levels, N=82 Sn-Te level comparison]
created: 2026-09-28
updated: 2026-09-29
status: active
review_status: unreviewed
source_type: evaluated-nuclear-data
reading_depth: skimmed
title_original: "IAEA LiveChart of Nuclides v1 API, ENSDF-derived level records"
journal: IAEA LiveChart of Nuclides
year: 2026
language: en
canonical_source: "https://nds.iaea.org/relnsd/v1/data?fields=levels&nuclides=132Sn&format=json"
raw_file: "raw/papers/gpt/day2-shell-gap-20260928/iaea-levels-132Sn.csv"
raw_sha256: cf9bf7423da89883488a6f2106161d8212e62dd5d4da90651ef1c347e8944f11
related_raw_files: ["raw/papers/gpt/day2-shell-gap-20260928/iaea-levels-130Sn.csv", "raw/papers/gpt/day2-shell-gap-20260928/iaea-levels-134Sn.csv", "raw/papers/gpt/day2-shell-gap-20260928/iaea-levels-134Te.csv", "raw/papers/gpt/day2-shell-gap-20260928/nudat-132Sn-levels.html", "raw/papers/gpt/day2-shell-gap-20260928/nudat-134Te-levels.html"]
retrieved: 2026-09-28
nuclei: [130sn, 132sn, 134sn, 134te]
reactions: []
experiments: [adopted-level-evaluation]
models: []
observables: [excitation-energy, spin-parity]
methods: [evaluated-nuclear-data-query]
tags: [ensdf, livechart, tin, tellurium, n82, shell-closure]
---

# IAEA LiveChart / ENSDF-derived adopted levels

## Bibliographic Record

IAEA LiveChart v1 API level records, retrieved 2026-09-28. The response identifies the ENSDF evaluator and cutoff for each nuclide. Query URLs and raw response snapshots are recorded in this page and local source files.

## Scope and Reading Depth

The four `fields=levels` query responses and two targeted NuDat 3 pages were read for low-lying `2+` levels, assigned uncertainties and available Coulomb-excitation `B(E2)` fields. This is an evaluated-data check, not a full audit of every adopted level or every primary experiment behind these databases.

## Summary

The adopted `E(2+)` systematics distinguish the `N=82` Sn closure from its neighbors, while the `B(E2)` comparison adds a collective-strength observable with explicit evaluation and source-lineage limits.

## Data Record and Query Route

The level rows below were retrieved on 2026-09-28 from the IAEA LiveChart v1 API. The `fields=levels` requests returned CSV records with the listed ENSDF evaluation cutoff, evaluator and extraction date. These are adopted database values, not three new experiments.

- [`130Sn` levels](https://nds.iaea.org/relnsd/v1/data?fields=levels&nuclides=130Sn&format=json)
- [`132Sn` levels](https://nds.iaea.org/relnsd/v1/data?fields=levels&nuclides=132Sn&format=json)
- [`134Sn` levels](https://nds.iaea.org/relnsd/v1/data?fields=levels&nuclides=134Sn&format=json)
- [`134Te` levels](https://nds.iaea.org/relnsd/v1/data?fields=levels&nuclides=134Te&format=json)
- Cross-interface check: [NNDC NuDat 3 adopted levels for `132Sn`](https://www.nndc.bnl.gov/nudat3/getdataset.jsp?nucleus=132SN&unc=nds). It lists the same `4041.20-keV`, `2+` level; NuDat and LiveChart are not independent evidence because both expose evaluated level data.
- Direct Coulomb-excitation follow-up: [[varner-2005-coulomb-excitation-132-134sn]] and the [ENSDF `132Sn` Coulomb-excitation subfile](https://www.nndc.bnl.gov/ensnds/132/Sn/coulex.pdf).
- `134Te` Coulomb-excitation evaluation: [NuDat 3 adopted levels](https://www.nndc.bnl.gov/nudat3/getdataset.jsp?nucleus=134TE&unc=nds) and its [ENSDF Coulomb-excitation subfile](https://www.nndc.bnl.gov/ensnds/134/Te/coulex.pdf); the adopted primary citation is `2003Ba01`, DOI `10.1016/S0370-2693(02)03066-6`.

## Key Results

### Adopted low-lying level records

| ID | Adopted level | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| LC130SN-1 | `130Sn` (`Z=50`, `N=80`) level index 1 is at `1221.26(5) keV` with tentative `(2+)` assignment. | experimental-fact | direct | IAEA LiveChart `130Sn` levels, row `idx=1` | true |
| LC132SN-1 | `132Sn` (`Z=50`, `N=82`) first `2+` level is at `4041.2(15) keV`. | experimental-fact | direct | IAEA LiveChart `132Sn` levels, row `idx=1` | true |
| LC134SN-1 | `134Sn` (`Z=50`, `N=84`) first `2+` level is at `725.6 keV`; the returned record has no energy uncertainty. | experimental-fact | direct | IAEA LiveChart `134Sn` levels, row `idx=1` | true |
| LC134TE-1 | `134Te` (`Z=52`, `N=82`) first `2+` level is at `1279.11(10) keV`. | experimental-fact | direct | IAEA LiveChart `134Te` levels, row `idx=1` | true |
| NUDAT132SN-1 | NNDC NuDat 3 lists the `132Sn` adopted `2+` level at `4041.20 keV`, consistent with LiveChart to displayed precision. | experimental-fact | contextual | NuDat 3 `132SN` adopted-level table, `2+` row | true |
| NUDAT132SN-2 | NuDat 3 labels the 4041.1-keV `2+→0+` transition as `B(E2)(W.u.)=5.5 15`. | derived-observable | contextual | NuDat 3 `132SN` gamma table, 4041.1-keV row | true |
| NUDAT132SN-3 | NuDat 3's adopted-level row for `132Sn` lists `B(E2)=0.11 3`; the unit is not shown on that row, while Varner et al. give `e²b²` in the primary article. | derived-observable | contextual | NuDat 3 `132SN` adopted-level table, 4041.20-keV row | true |
| NUDAT134TE-1 | NuDat 3 labels the `1279.01-keV` `2+→0+` transition as `B(E2)(W.u.)=6.3 20`. | derived-observable | contextual | NuDat 3 `134TE` gamma table, 1279.01-keV row | true |
| NUDAT134TE-2 | The `134Te` adopted-level row lists `B(E2)=0.13 4`, attributed to Coulomb-excitation reference `2003Ba01`; the row does not print the unit. | derived-observable | contextual | NuDat 3 `134TE` adopted-level table, 1279.11-keV row | true |
| NUDAT134TE-1 | NuDat 3 labels the `1279.01-keV` `2+→0+` transition as `B(E2)(W.u.)=6.3 20`. | derived-observable | contextual | NuDat 3 `134TE` gamma table, 1279.01-keV row | true |
| NUDAT134TE-2 | The `134Te` adopted-level row lists `B(E2)=0.13 4`, attributed to Coulomb-excitation reference `2003Ba01`; the NuDat row does not print the unit. | derived-observable | contextual | NuDat 3 `134TE` adopted-level table, 1279.11-keV row | true |

## Competing Interpretations and Limitations

The isotope comparisons `130Sn`–`132Sn`–`134Sn` hold `Z=50` fixed; the `130Sn` spin assignment is tentative. The `132Sn`–`134Te` isotone comparison holds `N=82` fixed and changes `Z` from 50 to 52. A high `E(2+)` is a shell-closure signature, not a direct measurement of a single-particle gap. The `132Sn` and `134Te` adopted strengths are similar in W.u. to their quoted precision despite the large `E(2+)` difference. `134Te` primary full text was not available from the publisher endpoint in this run; its ENSDF citation and database locator are retained without treating the database view as an independent measurement. NuDat 3's 130Sn 1221.24-keV tentative (2+) row has no printed B(E2) or multipolarity field; this is a database coverage gap, not evidence that no measurement exists. Radford et al. 2005 directly report a preliminary 130Sn B(E2)=0.023(5) e2b2 (Table 1); see [[radford-2005-130sn-coulomb-excitation-126-130sn]]. The NuDat 132Sn gamma-table value 5.5(15) W.u. and adopted-level field 0.11(3) without unit are distinct displayed fields whose source lineage still needs audit. The cited Raman et al. 2001 evaluation is marked closed in OpenAlex with no repository full text.

## Extracted Pages

- IAEA LiveChart `130Sn`, `132Sn`, `134Sn` and `134Te` `levels` response files are retained under the day-specific raw source bundle.
- NuDat 3 `132Sn` and `134Te` adopted-level HTML pages are same-ENSDF interface checks, not independent experiments.

## Related Knowledge

- [[a130-shell-gap-orbital-observable]]
- [[ame2020-sn132-mass-curvature]]
