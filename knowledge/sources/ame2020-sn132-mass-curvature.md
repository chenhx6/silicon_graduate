---
type: source
title: "AME2020 Sn mass records around N=82"
aliases: [AME2020 Sn masses, N=82 tin mass curvature]
created: 2026-09-28
updated: 2026-09-29
status: active
review_status: unreviewed
source_type: evaluated-nuclear-data
reading_depth: skimmed
citation_key: Wang2021AME2020
title_original: "The AME 2020 atomic mass evaluation (II). Tables, graphs and references"
authors: [M. Wang, W. J. Huang, F. G. Kondev, G. Audi, S. Naimi]
journal: Chinese Physics C
year: 2021
volume: 45
issue: 3
pages: 030003
doi: 10.1088/1674-1137/abddaf
language: en
canonical_source: doi:10.1088/1674-1137/abddaf
raw_file: "raw/papers/gpt/day2-shell-gap-20260928/ame2020-mass_1.mas20.txt"
raw_sha256: e8599c6d7f724fac91934e59f1b9de8fb8f63e820f4b39456b790665ed2a3307
data_url: "https://www-nds.iaea.org/amdc/ame2020/mass_1.mas20.txt"
data_sha256: e8599c6d7f724fac91934e59f1b9de8fb8f63e820f4b39456b790665ed2a3307
data_bytes: 472648
rct1_url: "https://www-nds.iaea.org/amdc/ame2020/rct1.mas20.txt"
rct1_sha256: e6ba1d2256f90053464c48e24d44691828dc49820ce64054aa418d834cc18e90
rct1_bytes: 511515
related_raw_file: "raw/papers/gpt/day2-shell-gap-20260928/ame2020-rct1.mas20.txt"
nuclei: [130sn, 131sn, 132sn, 133sn, 134sn]
reactions: []
experiments: [mass-evaluation]
models: [atomic-mass-evaluation]
observables: [mass-excess, one-neutron-separation-energy, two-neutron-separation-energy]
methods: [least-squares-mass-evaluation]
tags: [ame2020, tin, n82, shell-closure, mass-curvature]
---

# AME2020: `130Sn`, `132Sn` and `134Sn` mass data

## Bibliographic Record

The official AME2020 files `mass_1.mas20.txt` and `rct1.mas20.txt` are served at the [IAEA Atomic Mass Data Center](https://www-nds.iaea.org/amdc/ame2020/mass_1.mas20.txt) and [reaction/separation-energy table](https://www-nds.iaea.org/amdc/ame2020/rct1.mas20.txt). Their headers date the unrounded files to 3 March 2021; `mass_1` contains atomic masses and `rct1` contains separation energies. Both headers state that `#` marks estimated (non-experimental) values and cite Wang et al., *Chinese Physics C* **45**, 030003 (2021), DOI `10.1088/1674-1137/abddaf`.

The payloads retrieved on 2026-09-28 were `mass_1` (472,648 bytes; SHA-256 `e8599c6d7f724fac91934e59f1b9de8fb8f63e820f4b39456b790665ed2a3307`) and `rct1` (511,515 bytes; SHA-256 `e6ba1d2256f90053464c48e24d44691828dc49820ce64054aa418d834cc18e90`). Both verified files are retained under `raw/papers/gpt/day2-shell-gap-20260928/`; URLs, retrieval date, hashes and exact row locators preserve the verification route.

## Scope and Reading Depth

This page records only the evaluated ground-state mass excesses for the three Sn isotopes needed for a second-difference check across `N=82`. It does not reproduce the full AME evaluation, its input-reaction network or a mass covariance matrix.

## Summary

The AME2020 `mass_1` mass-excess rows and matching `rct1` two-neutron separation energies support a reproducible `N=82` Sn-chain second difference. Both files belong to one evaluation, and neither provides the covariance matrix needed for a fully correlated uncertainty on that difference.

## Key Results

### AME2020 shell-gap mass-curvature records

| ID | Evaluated record | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AME20-N-1 | AME2020 neutron mass excess is 8071.31806 ± 0.00044 keV. | evaluated-mass | direct | mass_1.mas20.txt, neutron row, mass-excess and uncertainty columns | true |
| AME20-131SN-1 | 131Sn (Z=50, N=81) mass excess is −77264.579 ± 3.621 keV. | evaluated-mass | direct | mass_1.mas20.txt, 131Sn row, mass-excess and uncertainty columns | true |
| AME20-133SN-1 | 133Sn (Z=50, N=83) mass excess is −70873.890 ± 1.904 keV. | evaluated-mass | direct | mass_1.mas20.txt, 133Sn row, mass-excess and uncertainty columns | true |
| AME20-130SN-1 | `130Sn` (`Z=50`, `N=80`) mass excess is `−80132.217 ± 1.873 keV`. | experimental-fact | direct | `mass_1.mas20.txt`, `130Sn` row, mass-excess and uncertainty columns | true |
| AME20-132SN-1 | `132Sn` (`Z=50`, `N=82`) mass excess is `−76546.554 ± 1.976 keV`. | experimental-fact | direct | `mass_1.mas20.txt`, `132Sn` row, mass-excess and uncertainty columns | true |
| AME20-134SN-1 | `134Sn` (`Z=50`, `N=84`) mass excess is `−66433.759 ± 3.167 keV`. | experimental-fact | direct | `mass_1.mas20.txt`, `134Sn` row, mass-excess and uncertainty columns | true |
| AME20-RCT1-132SN-1 | AME2020 gives `S₂n(132Sn)=12556.9730 ± 2.7224 keV`. | experimental-fact | direct | `rct1.mas20.txt`, `132Sn` row, `S(2n)` and uncertainty columns | true |
| AME20-RCT1-134SN-1 | AME2020 gives `S₂n(134Sn)=6029.8413 ± 3.7328 keV`. | experimental-fact | direct | `rct1.mas20.txt`, `134Sn` row, `S(2n)` and uncertainty columns | true |

## Competing Interpretations and Limitations

These are evaluated masses, not three independent measurements performed by the AME authors. The 2020 evaluation combines the available mass network. The `mass_1` and `rct1` values reproduce one another through the standard finite-difference formula; this is an internal consistency check of one evaluation, not an independent dataset. The retrieved tables do not provide the covariance between these fitted masses or adjacent `S₂n` values; any propagated uncertainty for a finite difference must state its covariance assumption. The `134Sn` mass row has an `x` qualifier in a separate qualifier column; the mass-excess value itself has no `#` estimated-value mark. This page preserves the qualifier without assigning it an unverified meaning.

The derived `δ₂n` is a mass-curvature indicator across the neutron shell closure. It includes pairing and smooth mass-surface contributions and is not identical to a single-particle orbital spacing.

## Extracted Pages

- `mass_1.mas20.txt`: `130Sn`, `132Sn`, `134Sn` rows and file legend.
- `rct1.mas20.txt`: `S(2n)` entries for `132Sn` and `134Sn`.

## Related Knowledge

- [[a130-shell-gap-orbital-observable]]
- [[shell-effects-and-deformation]]
