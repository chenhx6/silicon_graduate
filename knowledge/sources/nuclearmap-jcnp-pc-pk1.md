---
type: source
title: "NuclearMap triaxial RHB/5DCH PC-PK1 results"
aliases: [NuclearMap, JCNP nuclear map, PC-PK1 triaxial PES]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
source_type: institutional-model-database
reading_depth: read
title_original: "Triaxial Relativistic Hartree-Bogoliubov Results with the PC-PK1 Density Functional"
authors: ["NuclearMap/JCNP web resource"]
year: 2026
pages: "web pages and nuclide PES images"
language: [en]
canonical_source: "http://nuclearmap.jcnp.org/"
source_url: "http://nuclearmap.jcnp.org/"
citation_key: nuclearmap_jcnp_pc_pk1
raw_file: "raw/figures/gpt/learning-daily/20261101-day29-133ce-nuclearmap-pes/manifest.json"
raw_sha256: "5471a15f6124884c18419cab9d38886bb48254414c2405833f7ca67158676356"
raw_storage_status: archived-local-web-snapshot
archive_required: true
nuclei: [132ce, 134ce]
reactions: []
experiments: []
models: [triaxial-relativistic-hartree-bogoliubov, pc-pk1, five-dimensional-collective-hamiltonian]
observables: [beta2, gamma-deformation, potential-energy-surface, collective-energy]
methods: [constrained-quadrupole-calculation, inglis-belyaev, cranking-approximation, zero-point-motion-correction]
tags: [nuclearmap, triaxiality, 133ce, potential-energy-surface, pc-pk1]
---

# NuclearMap triaxial RHB/5DCH PC-PK1 results

## Bibliographic Record

The NuclearMap web resource provides triaxial relativistic
Hartree–Bogoliubov (RHB) results using the PC-PK1 density functional, with
nuclide-specific potential-energy-surface (PES) images and tabulated/model
fields. The local snapshot and hashes are recorded in
`raw/figures/gpt/learning-daily/20261101-day29-133ce-nuclearmap-pes/manifest.json`.

## Scope and Reading Depth

The theory page and the `Z=58` block of the observation script were read.
The site describes constrained calculations in quadrupole deformation
parameters `β` and `γ`, and a five-dimensional collective Hamiltonian with
vibrational and rotational terms. It states that the moments of inertia use
the Inglis–Belyaev formula, mass parameters use a cranking approximation and
the collective potential includes zero-point-motion subtraction.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| NMAP-1 | The web resource presents PC-PK1 triaxial RHB results and a 5DCH extension in `β`, `γ` and Euler-angle coordinates. | model/database identity | direct-web-snapshot | `raw/figures/gpt/learning-daily/20261101-day29-133ce-nuclearmap-pes/nuclearmap-theory.html`, theory section | true |
| NMAP-2 | The `Z=58`, `N=74` entry gives `132Ce` fields `β=0.22` and `γ=17°` in the local JavaScript data block. | model-result | direct-web-snapshot | `raw/figures/gpt/learning-daily/20261101-day29-133ce-nuclearmap-pes/nuclearmap-obs.js`, `if (Z==58)`, `N==74` | true |
| NMAP-3 | The `Z=58`, `N=76` entry gives `134Ce` fields `β=0.17` and `γ=0°` in the local JavaScript data block. | model-result | direct-web-snapshot | `raw/figures/gpt/learning-daily/20261101-day29-133ce-nuclearmap-pes/nuclearmap-obs.js`, `if (Z==58)`, `N==76` | true |
| NMAP-4 | The inspected site route has a PES image for `132Ce`. | model-figure | direct-web-snapshot | `raw/figures/gpt/learning-daily/20261101-day29-133ce-nuclearmap-pes/132Ce_Z058N074_pes.png` | true |
| NMAP-5 | The inspected site route has a PES image for `134Ce`. | model-figure | direct-web-snapshot | `raw/figures/gpt/learning-daily/20261101-day29-133ce-nuclearmap-pes/134Ce_Z058N076_pes.png` | true |
| NMAP-6 | The inspected `Z=58` observation block lists even neutron numbers around `N=75` without a `133Ce` entry. | database-coverage-boundary | direct-web-snapshot | `raw/figures/gpt/learning-daily/20261101-day29-133ce-nuclearmap-pes/nuclearmap-obs.js`, `if (Z==58)` block | true |

## Summary

NuclearMap is a useful neighboring-even-even core prior for the private
`133Ce` analysis. It does not provide a direct odd-mass `133Ce` PES in the
inspected route, so interpolation across `132Ce` and `134Ce` is a provisional
research inference rather than a site result.

## Competing Interpretations and Limitations

- The website's `β` and `γ` values are model outputs, not direct observables.
- The absence of a tested `133Ce` entry does not prove that no calculation
  exists elsewhere; it records only this route's access boundary.
- Neighboring even-even cores do not determine the odd-particle alignment,
  signature mixing, tilted-precession stability or wobbling phonon content of
  `133Ce`.
- The site framework should be used as a prior and comparison surface; it
  cannot replace an odd-mass PRM/TAC or equivalent calculation tied to the
  measured transition set.

## Extracted Pages

- `NMAP-1`–`NMAP-6`: theory framework, `132Ce`/`134Ce` fields and archived PES
  images.
- Related route: [[133ce-triaxial-core-collective-mode-route-20261101]]

## Human Review

This page records a local web snapshot and Codex self-audit. It remains
`unreviewed` and does not set `human-reviewed`.
