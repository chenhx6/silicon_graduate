---
type: source
title: "Schönwaßer et al. 2003 - One- and two-phonon wobbling excitations in triaxial 165Lu"
aliases: [Schonwasser 2003 165Lu wobbling]
created: 2026-07-16
updated: 2026-07-25
status: active
review_status: human-reviewed
source_type: journal-article
reading_depth: deep-read
title_original: "One- and two-phonon wobbling excitations in triaxial 165Lu"
authors: [G. Schönwaßer, H. Hübel, G. B. Hagemann, P. Bednarczyk, G. Benzoni, A. Bracco, P. Bringel, R. Chapman, D. Curien, J. Domscheit, B. Herskind, D. R. Jensen, S. Leoni, G. Lo Bianco, W. C. Ma, A. Maj, A. Neußer, S. W. Ødegård, C. M. Petrache, D. Roßbach, H. Ryde, K. H. Spohr, A. K. Singh]
journal: Physics Letters B
year: 2003
volume: 552
pages: 9-16
doi: 10.1016/S0370-2693(02)03095-2
canonical_source: https://doi.org/10.1016/S0370-2693(02)03095-2
citation_key: schonwasser_2003_Onetwophonon
raw_file: "raw/papers/2003_Schönwaßer et al_One- and two-phonon wobbling excitations in triaxial 165Lu.pdf"
raw_sha256: F7DF3707DD9C5C5AAD439F22205840F1CC85D36C43428F60AC95F1343A048AC3
nuclei: [165lu]
reactions: ["139La(30Si,4n)165Lu"]
experiments: []
models: [particle-rotor-model, cranked-nilsson-strutinsky-model]
observables: [interband-e2-strengths, moments-of-inertia]
methods: [gamma-gamma-coincidence, dco-ratio]
tags: [experiment-ingest, wobbling, multiphonon, triaxial-superdeformation]
---

# One- and two-phonon wobbling excitations in triaxial `165Lu`

## Bibliographic Record

Physics Letters B 552, 9-16 (2003), DOI `10.1016/S0370-2693(02)03095-2`; PDF/BibTeX identity checked before ingest.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: full article, reaction/setup, three TSD bands, DCO constraints, branching ratios, relative E2 strengths, UC/particle-rotor comparison and conclusion.
- Not covered: independent recalculation of the model or all transition intensities.
- Coverage caveats: TSD3 links lack sufficient DCO statistics; two-phonon identification is more systematics/model dependent than TSD2.

## Paper Question and Scientific Motivation

Test whether two newly observed TSD bands in `165Lu` form the `n_w=1,2` members of a wobbling family analogous to `163Lu` (PDF pp.10-11).

## Method and Design Logic

The experiment establishes TSD2/TSD3 decay patterns and rotational similarity, measures DCO for the strongest TSD2→TSD1 links, derives relative `B(E2)_out/B(E2)_in`, and compares them with particle-rotor calculations and Lu-isotope systematics.

## Key Evidence and Reasoning Chain

- Six TSD2→TSD1 links and mixed-multipole DCO results → an electromagnetically connected one-phonon candidate; adopted large-E2 branches and relative strengths → agreement with the particle-rotor n_w=1 calculation; TSD3 similarity and decay systematics → a weaker, homology-based n_w=2 assignment (PDF pp.11-16, Table 1, Figs.4-6).

## Summary

The source reports comparatively strong evidence for one-phonon wobbling in TSD2 and a more indirect/systematics-based two-phonon assignment for TSD3. Its regional statement “firmly establish” remains author wording.

## Experimental or Theoretical Setup

`139La(30Si,4n)165Lu` at 152 MeV, Vivitron/IReS Strasbourg, EUROBALL with large-volume Ge, Clover/composite detectors, BGO suppression and a 210-element BGO multiplicity filter (PDF p.11).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SW03-1 | Known TSD1 was extended and connected to ND states; two new TSD bands with populations about `0.4%` and `0.1%` of the 4n channel were identified. | experimental-fact | direct | PDF pp.11-12, Figs.2-3 | true |
| SW03-2 | Six TSD2→TSD1 transitions were observed; DCO values for 667.9 and 682.5 keV links support mixed dipole/quadrupole character. | experimental-criterion | direct | PDF p.11 | true |
| SW03-3 | The adopted large-E2 solution yields about `92.3%` E2 for the measured links and relative `B(E2)_out/B(E2)_in` values around `0.16-0.17`. | experimental-fact | direct | PDF pp.11-12, Table 1 | true |
| SW03-4 | TSD1-3 have similar moments of inertia and alignments outside interaction regions. | experimental-fact | direct | PDF pp.12-14, Figs.4-5 | true |
| SW03-5 | The particle-rotor calculation reproduces the TSD2→TSD1 relative E2 strengths for `n_w=1→0`. | model-result | direct | PDF pp.14-15, Fig.6 | true |
| SW03-6 | TSD3 is assigned `n_w=2` mainly from isospectrality/decay systematics with `163Lu`; its weak links do not provide the same direct electromagnetic test. | author-interpretation | indirect | PDF pp.11-16 | true |
| SW03-7 | Authors conclude `n_w=0,1,2` wobbling and stable triaxiality in the A=165 region. | author-interpretation | indirect | PDF p.16 | true |

## Nuclear Structure Information

TSD1, TSD2 and TSD3 form the proposed n_w=0/1/2 family. TSD2 has six observed links to TSD1 and measured relative strengths for the strongest branches; TSD3 has weaker links and substantially less complete multipolarity information.

## Authors' Interpretation

The authors assign one- and two-phonon wobbling and infer stable triaxiality across neighboring Lu isotopes. This page keeps the TSD3 assignment at the weaker homology/systematics level.

## Model Results

Particle-rotor calculations reproduce the adopted TSD2 relative E2 strengths. UC calculations are used to argue against suitable low-lying alternative configurations; both comparisons depend on selected deformation, triaxiality and configuration assumptions.

## Competing Interpretations and Limitations

UC alternatives are argued to lack suitable low-lying configurations, but the regional conclusion combines dependent Lu-isotope evidence. TSD3 multipolarities are poorly constrained, and calculated ratios depend on `γ` and assumed deformation.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| SW03-AR-1 | Core reconstruction | TSD2 provides a neighboring-isotope E2-strength test, whereas TSD3 extends only the weaker homology/systematics layer. | Key Results and Competing Interpretations above | unreviewed |
| SW03-AR-2 | Assumptions and dependencies | The adopted large-E2 branch, common TSD configurations, and analogy to 163Lu are valid outside the noted interaction regions. | Method/results/model sections cited above | unreviewed |
| SW03-AR-3 | Transfer conditions | Transfer the TSD2 evidence only where link character and relative strengths are measured; treat TSD3-like homology as weaker evidence. | Source scope and claim locators above | unreviewed |
| SW03-AR-4 | Failure conditions | A different δ branch or failure of Lu-isotope homology removes the proposed phonon hierarchy, especially n_w=2. | Competing Interpretations and Limitations above | unreviewed |
| SW03-AR-5 | Reverse/falsification test | Measure polarization/lifetimes for TSD3→TSD2 and compare absolute strengths across the isotope chain. | Follow-up observables identified by the source/Agent | unreviewed |
| SW03-AR-6 | Research-question decision | Use as a split-strength case: stronger one-phonon evidence and weaker two-phonon evidence. | Whole-source assessment | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: The Wiki high-spin wobbling benchmark was centered on 163Lu, with no equally structured neighboring-isotope comparison.
- Effect of this source: supports
- Reason: TSD2 provides a neighboring-isotope E2-strength test, whereas TSD3 extends only the weaker homology/systematics layer.
- Persistence decision: synthesis update
- Review state: page-level `human-reviewed`; Key Results claims remain `needs_review: true` for future claim-specific paper use.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[wobbling-motion]] | Adds a neighbouring-isotope one-phonon strength test. |
| limits | [[interband-e2-strengths]] | TSD3 shows the weakness of assigning multiphonon character without equivalent electromagnetic coverage. |

## Human Review Triage

Review disposition: the user completed a rough page-level review on 2026-07-25 and accepted the current evidence-calibrated wording without correction. The P0/P1 items below are retained as future strict paper-use verification prompts, not unresolved ingest blockers.

### P0

- P0: none identified.

### P1

- `SW03-3`/`SW03-6`, Table 1 and Figs. 4-6 — Evidence: TSD2 has measured mixed links and relative E2 strengths; TSD3 lacks equivalent DCO coverage and relies on 163Lu homology. Agent inference: the two phonon levels do not have equal evidential status. User check: adopted δ branch and the exact basis for TSD3 homology. Risk: treating both assignments as equally established overstates the source.

### P2/P3

- P2: interaction-region exceptions and exact population values. P3: navigation.

## Human Review Record

- 2026-07-25: the user completed a rough review of this source page and accepted its current claims, attribution boundaries, locators and stated limitations without requesting corrections.

## Review Status

Page-level review is complete for this ingest round. Claim-level `needs_review` and Analytical Reconstruction review markers remain unchanged because this was a rough review rather than exhaustive claim-by-claim paper certification.

## Extracted Pages

- Nuclei: [[165lu]]
- Bands: retained within the nucleus/source pages pending user review.
- Concepts: [[wobbling-motion]]
- Methods: [[dco-ratio]]

## Non-source Notes and Follow-up

Keep TSD2 and TSD3 evidence strength separate in later synthesis.

## Day18定量审计：类比排除小解与B(E2)的33倍塌缩边界

在Day18正式学习中对本文Table 1与正文p.3中165Lu TSD2到TSD1连接线的DCO解分支与跃迁几率进行定量审计，raw SHA256 `C19D8BA76DC40FE1EBA208577543BA2F4C5FE6120D51BC034ED70119E7A310FA`已核。原SC03-1–7各claim及`human-reviewed`状态完全保留；新SC03-D18-1待审。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SC03-D18-1 | 本文Table 1报告TSD2到TSD1的三条跨带线B(E2_out)/B(E2_in)为0.16-0.22，被作为165Lu存在wobbling激发的核心证据。定量审计揭示关键类比依赖：(1) 本文未测线偏振，DCO分析产生大解（E2占92.3%）与小解（E2仅2.8%，M1占97.2%）两个分支；(2) 正文p.3明确承认‘小解是通过与163Lu的类比而排除的’；(3) 若采纳实验同样允许的DCO小解，B(E2_out)/B(E2_in)遭遇整整33.0倍断崖暴跌（暴跌至0.0049-0.0067），彻底丧失四极集体性；(4) 跨声子TSD3到TSD1连接线无一条具有足够统计量开展DCO分析。这证明165Lu的一声子与二声子wobbling证据完全受制于对163Lu同位素类比的先验假设。 | task-rate-decomposition-audit | derived-and-boundary | PDF pp.3-4 Table 1；新lu-ta-wobbling-lineage-result-027 | true |

新[分析合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/lu-ta-wobbling-lineage-contract-027.json)及[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/lu-ta-wobbling-lineage-result-027.json)4项检查全过。
