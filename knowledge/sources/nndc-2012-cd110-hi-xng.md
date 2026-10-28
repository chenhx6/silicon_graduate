---
type: source
title: "NNDC 110Cd (HI,XNG)：高自旋能级、分支与寿命字段"
aliases: [NNDC110Cd HI XNG, 110048022 high-spin Cd]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data
reading_depth: deep-read
title_original: "110CD (HI,XNG)"
authors: [G. Gürdal, F. G. Kondev]
journal: "Nuclear Data Sheets"
year: 2012
volume: 113
pages: "1315"
citation_key: NNDC110CdHIXNG2012
canonical_source: "https://www.nndc.bnl.gov/ensdf/EnsdfDispatcherServlet?datasetcheck=110048022,110CD"
data_version: "110048022, cutoff 1-Aug-2011"
raw_file: "raw/papers/gpt/_incoming/day26-20261028-002/nndc/110cd-hi-xng.ensdf"
raw_sha256: "cd14b1104805f54023a420e6021b74fddaa149a7f7f5cd404be23a9c696b47d1"
nuclei: [110Cd]
reactions: ["96Zr(18O,4nγ)"]
experiments: [Nordball]
observables: [level-energy, gamma-branch-intensity, half-life, DCO, B(M1)/B(E2)]
methods: [gamma-gamma-coincidence, directional-correlation, ENSDF-evaluation]
tags: [110Cd, antimagnetic-rotation, evaluated-data, branch-identity, feeding]
---

# `110Cd` (HI,XNG) 评价对象

## Bibliographic Record

NNDC ENSDF dataset `110048022`, `110CD (HI,XNG)`, evaluated by Gürdal and Kondev, cutoff 2011-08-01. The archived fixed-column file is the official response with the SHA-256 above.

## Scope and Reading Depth

The complete 47,300-byte fixed-column object was read for its header, experiment comments, high-spin levels, branches, half-lives and source annotations. It is an evaluated object in the same source lineage as Roy 2011, not an independent repetition.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| NC110-HI-1 | The object identifies `96Zr(18O,4nγ)` at 65/73 MeV with Nordball, and lists measured Eγ, γγ, γ(θ), DCO and deduced half-lives and B(M1)/B(E2). | evaluated-method-and-lineage | direct | header comments | true |
| NC110-HI-2 | The evaluated fields list 18+ T1/2=0.159(21) ps with 1224.5-keV E2, 20+ T1/2=0.118(21) ps with 1323.0-keV E2, 22+ T1/2=0.15(5) ps with 1314.1-keV E2, and 24+ T1/2=0.19(5) ps with 1358.0-keV E2. | evaluated-level-data | direct | L7325.4, L8648.3, L9962.4, L11320.4 | true |
| NC110-HI-3 | The 22+ object retains a 1100-keV branch with RI=1.0(3) alongside 1314.1 keV RI=2.7(1), while its source note records that Roy 2011 did not confirm the 1100-keV line in coincidence gates. | evaluated-branch-boundary | direct | L9962.4 and G rows; cL T note | true |
| NC110-HI-4 | The fields provide branch and half-life inputs, but not Roy's line-shape templates, side-feeding covariance or stopping-power systematic treatment. | readiness-boundary | direct | header/source comments; 2011Ro01 reference | true |

## Summary

The HI,XNG evaluation closes the identity and branch part of the 110Cd input contract. It confirms the half-life/branch lineage and preserves the 22+ 1100-keV dispute, but it cannot reconstruct the original DSAM normalization or absolute B(E2) covariance.

## Competing Interpretations and Limitations

The dataset supports level and branch identity used in AMR discussions. It does not independently establish AMR, core rotation, or a universal `J^(2)/B(E2)` threshold. Evaluated fields sharing 2011Ro01 are dependent evidence.

## Model Dependence

Band labels, multipolarities and source assignments are evaluation fields based on cited experiments and level systematics; no new particle-plus-rotor calculation is performed here.

## Knowledge Impact and Learning Decision

`supports` the 110Cd branch/half-life evidence contract; `limits` any attempt to infer Roy's missing feeding covariance or silently include the 1100-keV branch in his Table 1. It sharpens the normalization gap rather than filling it with a toy correction.

## Extracted Pages

- Full fixed-column object, focused on header comments and L/G blocks around 18+–24+.

## Sources

- [[roy-2011-cd110-systematics-antimagnetic]]
- [[nndc-2012-cd110-adopted-lifetimes-branches]]

## Review Status

Codex source self-audit; not `human-reviewed`.
