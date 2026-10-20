---
type: source
title: "Amro et al. 2003 - The wobbling mode in 167Lu"
aliases: [Amro 2003 167Lu wobbling]
created: 2026-07-16
updated: 2026-07-25
status: active
review_status: human-reviewed
source_type: journal-article
reading_depth: deep-read
title_original: "The wobbling mode in 167Lu"
authors: [H. Amro, W. C. Ma, G. B. Hagemann, R. M. Diamond, J. Domscheit, P. Fallon, A. Görgen, B. Herskind, H. Hübel, D. R. Jensen, Y. Li, A. O. Macchiavelli, D. Roux, G. Sletten, J. Thompson, D. Ward, I. Wiedenhöver, J. N. Wilson, J. A. Winger]
journal: Physics Letters B
year: 2003
volume: 553
pages: 197-203
doi: 10.1016/S0370-2693(02)03199-4
canonical_source: https://doi.org/10.1016/S0370-2693(02)03199-4
citation_key: h.amro_2003_wobblingmode
raw_file: "raw/papers/2003_The wobbling mode in 167Lu.pdf"
raw_sha256: 2C28C101A58D920C9CADE83A2B166D9FE5D3F80D59EFF8D6E1C7C9571B89EC88
nuclei: [167lu]
reactions: ["123Sb(48Ca,4n)167Lu"]
experiments: []
models: [particle-rotor-model, cranked-nilsson-strutinsky-model]
observables: [multipole-mixing-ratio, interband-e2-strengths, moments-of-inertia]
methods: [gamma-gamma-coincidence, dco-ratio, angular-distribution]
tags: [experiment-ingest, wobbling, triaxial-superdeformation]
---

# The wobbling mode in `167Lu`

## Bibliographic Record

Physics Letters B 553, 197-203 (2003), DOI `10.1016/S0370-2693(02)03199-4`; PDF/BibTeX identity checked.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: experiment, TSD1/TSD2 links, SpeeDCO/angular-distribution mixing ratios, relative strengths, alternatives and PRM comparison.
- Not covered: forthcoming ND-structure analysis and independent UC/PRM reproduction.
- Coverage caveats: no usable polarization for the links; large-`abs(δ)` branch is selected by analogy/model consistency.

## Paper Question and Scientific Motivation

- Author-explicit motivation: test whether the newly connected TSD2 band in `167Lu` is the wobbling excitation of TSD1 and whether the Lu-isotope interpretation survives a different experiment and nucleus (PDF pp.197-199).

## Method and Design Logic

- Establish TSD1/TSD2 links and rotational similarity; use SpeeDCO/angular distributions to obtain δ branches; convert the adopted branch and branching ratios to relative E2/M1 strengths; compare signature and three-quasiparticle alternatives with UC/PRM expectations (PDF pp.199-203, Table 1, Fig.6).

## Key Evidence and Reasoning Chain

- Connected ΔI=1 links → common decay topology; mixed-multipole fits → two δ branches; analogy with electric `163Lu` links selects the large branch → 92-98% E2; relative strengths and band systematics → author wobbling assignment (PDF pp.199-203).

## Summary

The paper gives evidence for TSD2 as one-phonon wobbling in `167Lu`, based on large inferred E2 components and relative strengths. Unlike `163Lu`, polarization did not independently select the branch.

## Experimental or Theoretical Setup

`123Sb(48Ca,4n)167Lu` at 203 MeV with the LBNL 88-Inch Cyclotron and 100-detector Gammasphere; TSD1/TSD2 populations about 8%/2% of yrast.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AM03-1 | TSD1 and TSD2 were firmly assigned to `167Lu` and connected by several `ΔI=1` transitions. | experimental-fact | direct | PDF pp.199-202, Figs.2 and 5 | true |
| AM03-2 | SpeeDCO/angular-distribution analysis gives small and large negative `δ` solutions; polarization was unavailable. | experimental-criterion | direct | PDF pp.200-201 | true |
| AM03-3 | Authors reject the small branches by analogy with electric links in `163Lu`; adopted links contain about `92-98%` E2. | author-interpretation | indirect | PDF p.201, Table 1 | true |
| AM03-4 | Derived `B(E2)_out/B(E2)_in` values are much larger than cranking-like expectations and agree with PRM wobbling estimates. | model-result | direct | PDF pp.201-202, Fig.6 | true |
| AM03-5 | Signature-partner and three-quasiparticle alternatives are rejected using excitation energy, alignment and predicted weak links. | author-interpretation | indirect | PDF p.202 | true |
| AM03-6 | Authors assign TSD2 as one-phonon wobbling built on TSD1. | author-interpretation | indirect | PDF pp.202-203 | true |

## Nuclear Structure Information

- TSD1 and TSD2 are assigned to the same `167Lu` TSD family, with populations near 8% and 2% of yrast and several interband ΔI=1 links. The assignment-critical information is the branch-dependent E2 content rather than a complete duplicated level scheme.

## Authors' Interpretation

The authors interpret TSD2 as one-phonon wobbling and reject signature-partner/three-quasiparticle alternatives. The E2 dominance is inferred through an adopted branch, not directly fixed by polarization.

## Model Results

UC calculations constrain alternative configurations; PRM calculations reproduce the adopted relative-strength pattern. Both comparisons depend on selected deformation/moments of inertia and on the large-|δ| solution.

## Competing Interpretations and Limitations

The decisive E2 dominance is not directly fixed by polarization. Relative strengths depend on adopted branch; UC/PRM exclusions are model-conditioned.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AM03-AR-1 | Core reconstruction | The evidence is stronger than systematics alone but weaker than `163Lu` because the decisive large-E2 branch is selected without polarization. | Key Results and Competing Interpretations above | unreviewed |
| AM03-AR-2 | Assumptions and dependencies | The adopted band identities, mixing-ratio branches, configuration assignments, and model inputs are valid within the stated measured range. | Method/results/model sections cited above | unreviewed |
| AM03-AR-3 | Transfer conditions | Transfer only the measured observables and their explicit conditions; do not transfer the author interpretation without equivalent link and configuration evidence. | Source scope and claim locators above | unreviewed |
| AM03-AR-4 | Failure conditions | Alternative branch, band identity, configuration, or model dependence can weaken the structural label even when the measured transitions remain valid. | Competing Interpretations and Limitations above | unreviewed |
| AM03-AR-5 | Reverse/falsification test | Obtain independent lifetimes/multipolarities or common-input competing-model tests targeted to the stated evidence gap. | Follow-up observables identified by the source/Agent | unreviewed |
| AM03-AR-6 | Research-question decision | Retain the source in the project/synthesis evidence map with the source-local review boundary explicit. | Whole-source assessment | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: The Wiki already contained the broader wobbling topic and related candidate map, but not this source in a complete source-local evidence and review structure.
- Effect of this source: supports
- Reason: The evidence is stronger than systematics alone but weaker than `163Lu` because the decisive large-E2 branch is selected without polarization.
- Persistence decision: project update / synthesis update
- Review state: page-level `human-reviewed`; Key Results claims remain `needs_review: true` for future claim-specific paper use.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[wobbling-motion]] | Lu-isotope high-spin candidate with relative strength evidence. |
| limits | [[multipole-mixing-ratio]] | Shows inference risk when polarization cannot select the solution. |

## Human Review Triage

Review disposition: the user completed a rough page-level review on 2026-07-25 and accepted the current evidence-calibrated wording without correction. The P0/P1 items below are retained as future strict paper-use verification prompts, not unresolved ingest blockers.

### P0

- `AM03-2`/`AM03-3`, Table 1 — Evidence: no usable polarization; large negative δ branches are chosen by analogy with `163Lu`, producing 92-98% E2. Agent inference: branch selection and PRM agreement are not independent. User check: both δ solutions, adopted branch, and recalculated strengths. Risk: a small branch removes the electromagnetic basis of the assignment.

### P1

- `AM03-4`/`AM03-5` — Review how strongly UC/PRM exclusions depend on selected deformation, configuration and branch assumptions.

### P2/P3

- P2: BibTeX author-field mismatch is metadata-only. P3: navigation.

## Human Review Record

- 2026-07-25: the user completed a rough review of this source page and accepted its current claims, attribution boundaries, locators and stated limitations without requesting corrections.

## Review Status

Page-level review is complete for this ingest round. Claim-level `needs_review` and Analytical Reconstruction review markers remain unchanged because this was a rough review rather than exhaustive claim-by-claim paper certification.

## Extracted Pages

- Nuclei: [[167lu]]
- Bands: retained in nucleus/source page.
- Concepts: [[wobbling-motion]]
- Methods: [[dco-ratio]], [[angular-distribution]]

## Non-source Notes and Follow-up

The BibTeX author field contains only H. Amro, but title/year/DOI uniquely identify the paper; raw BibTeX remains read-only.


## Day18定量审计：混合比双解对相对B(E2)提取的决定性影响

在Day18正式学习中重新核验本文Table 1数值。原AM03-1–6各claim及`human-reviewed`状态完全保留；新AM03-D18-1待审。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AM03-D18-1 | 本文Table 1中带间相对强度比 $B(E2)_	ext{out}/B(E2)_	ext{in}$ 完全由分支比 $\lambda$ 与混合比 $\delta$ 提取；由于采用大解（$\delta \sim -3.1$ 至 $-5.1$），得到比值 $0.23	ext{--}0.27$。若采用未被测量的另一小解（$\delta \sim -0.07$ 至 $-0.35$），该比值将被压低 8.6 至 197.5 倍，导致强度比跌至 0.001–0.031。这证明相对强度提取同样面临混合比双根的极端敏感性。 | task-sensitivity-audit | derived-and-boundary | PDF p.201 Table 1；新amro03-167lu-result-014 | true |

新[分析合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/amro03-167lu-contract-014.json)及[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/amro03-167lu-result-014.json)4项检查全过，定量揭示了线偏振缺失对相对强度判据的潜在系统影响。
