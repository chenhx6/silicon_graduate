---
type: source
title: "Hartley et al. 2009 - Wobbling mode in 167Ta"
aliases: [Hartley 2009 167Ta wobbling]
created: 2026-07-16
updated: 2026-07-25
status: active
review_status: human-reviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Wobbling mode in 167Ta"
authors: [D. J. Hartley, R. V. F. Janssens, L. L. Riedinger, M. A. Riley, A. Aguilar, M. P. Carpenter, C. J. Chiara, P. Chowdhury, I. G. Darby, U. Garg, Q. A. Ijaz, F. G. Kondev, S. Lakshmi, T. Lauritsen, A. Ludington, W. C. Ma, E. A. McCutchan, S. Mukhopadhyay, R. Pifer, E. P. Seyfried, I. Stefanescu, S. K. Tandel, U. Tandel, J. R. Vanhoy, X. Wang, S. Zhu, I. Hamamoto, S. Frauendorf]
journal: Physical Review C
year: 2009
volume: 80
pages: 041304(R)
doi: 10.1103/PhysRevC.80.041304
canonical_source: https://doi.org/10.1103/PhysRevC.80.041304
citation_key: hartley_2009_Wobblingmode
raw_file: "raw/papers/2009_Hartley et al_Wobbling mode in Ta 167.pdf"
raw_sha256: 4667DA2A7D58D75EE751B85D8B7489437A2DC9ECC4BA8F22FD533D36782D1525
nuclei: [167ta]
reactions: ["120Sn(51V,4n)167Ta"]
experiments: []
models: [particle-rotor-model, cranked-nilsson-strutinsky-model]
observables: [moments-of-inertia, interband-e2-strengths]
methods: [gamma-gamma-coincidence, angular-correlation]
tags: [experiment-ingest, wobbling, suggested, triaxial-superdeformation, tantalum]
---

# Wobbling mode in `167Ta`

## Bibliographic Record

PRC 80, 041304(R) (2009), DOI `10.1103/PhysRevC.80.041304`; PDF title `167 Ta` corresponds uniquely to filename/BibTeX `Ta 167`.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: full rapid communication, level scheme, angular-correlation ratios, rotational comparison, assumed E2 fraction and limitations.
- Not covered: lifetime follow-up or independent recalculation.
- Coverage caveats: polarization was not measured; `90%` E2 was imported from `163Lu`, not determined in `167Ta`.

## Paper Question and Scientific Motivation

- Author-explicit motivation: test whether wobbling-like TSD band structures occur outside lutetium by identifying a linked TSD pair in `167Ta` (PDF pp.1-2).

## Method and Design Logic

- Establish TSD1/TSD2 topology and angular-correlation ΔI=1 character, compare alignments/moments of inertia and alternatives, then estimate relative E2 strengths only after importing a 90% E2 fraction from `163Lu` (PDF pp.2-5).

## Key Evidence and Reasoning Chain

- Linked similar TSD bands → candidate shared structure; angular correlations → ΔI=1 but not E2 fraction; assumed Lu-like 90% E2 → quoted strength ratios; combined systematics → authors “suggest” wobbling outside Lu (PDF pp.3-5).

## Summary

The source suggests the first wobbling mode outside Lu. It does not experimentally determine E2 dominance, so the derived relative strengths are assumption-dependent.

## Experimental or Theoretical Setup

`120Sn(51V,4n)167Ta` at 235 MeV using ATLAS and 101-detector Gammasphere; approximately `2×10^9` fourfold-or-greater events.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HA09-1 | A `πi13/2` TSD1 band and a similar TSD2 band feeding it by `ΔI=1` links were identified. | experimental-fact | direct | PDF pp.2-3, Figs.1-2 | true |
| HA09-2 | Angular-correlation ratios for selected links support `ΔI=1`, but do not determine E2/M1 mixing. | experimental-criterion | direct | PDF p.3 | true |
| HA09-3 | TSD1/TSD2 alignments and moments of inertia become similar above `ħω≈0.4 MeV`; signature-partner interpretation is argued against. | experimental-fact | direct | PDF pp.3-4, Figs.3-4 | true |
| HA09-4 | Polarization was unavailable; the paper assumes links are `90%` E2 by analogy with `163Lu`. | author-interpretation | contextual | PDF p.5 | true |
| HA09-5 | Under that assumption, `B(E2)_out/B(E2)_in=0.37(4),0.32(4),0.36(4)` for three states. | model-result | indirect | PDF p.5 | true |
| HA09-6 | Authors use “suggest” for the first wobbling observation outside Lu. | author-interpretation | indirect | PDF p.5, Summary | true |
| HA09-7 | A possible SD-to-TSD interaction near `I=51/2` is proposed and requires lifetime validation. | author-interpretation | indirect | PDF pp.4-5 | true |

## Nuclear Structure Information

A πi13/2 TSD1 band and a linked TSD2 band are compared above ħω≈0.4 MeV; a possible SD-TSD interaction is discussed near I=51/2.

## Authors' Interpretation

The paper suggests, rather than electromagnetically establishes, a wobbling mode and explicitly requests polarization/lifetime confirmation.

## Model Results

UC/PRM comparisons help reject signature and interpret band interaction, but the displayed B(E2) ratios are derived under the externally assumed E2 fraction.

## Competing Interpretations and Limitations

Unfavoured signature and band-interaction alternatives are considered. The wobbling strength result is circular if Lu-like E2 character is assumed because Lu is the comparison benchmark. Authors explicitly request polarization and lifetime measurements.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| HA09-AR-1 | Core reconstruction | Direct evidence establishes topology and rotational similarity; the wobbling-strength argument is conditional on an imported 90%-E2 assumption. | Key Results and Competing Interpretations above | unreviewed |
| HA09-AR-2 | Assumptions and dependencies | The adopted band identities, mixing-ratio branches, configuration assignments, and model inputs are valid within the stated measured range. | Method/results/model sections cited above | unreviewed |
| HA09-AR-3 | Transfer conditions | Transfer only the measured observables and their explicit conditions; do not transfer the author interpretation without equivalent link and configuration evidence. | Source scope and claim locators above | unreviewed |
| HA09-AR-4 | Failure conditions | Alternative branch, band identity, configuration, or model dependence can weaken the structural label even when the measured transitions remain valid. | Competing Interpretations and Limitations above | unreviewed |
| HA09-AR-5 | Reverse/falsification test | Obtain independent lifetimes/multipolarities or common-input competing-model tests targeted to the stated evidence gap. | Follow-up observables identified by the source/Agent | unreviewed |
| HA09-AR-6 | Research-question decision | Retain the source in the project/synthesis evidence map with the source-local review boundary explicit. | Whole-source assessment | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: The Wiki already contained the broader wobbling topic and related candidate map, but not this source in a complete source-local evidence and review structure.
- Effect of this source: supports
- Reason: Direct evidence establishes topology and rotational similarity; the wobbling-strength argument is conditional on an imported 90%-E2 assumption.
- Persistence decision: project update / synthesis update
- Review state: page-level `human-reviewed`; Key Results claims remain `needs_review: true` for future claim-specific paper use.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[wobbling-motion]] | Cross-element candidate with Lu-like topology. |
| limits | [[interband-e2-strengths]] | Relative strengths are conditional on an assumed E2 fraction. |

## Human Review Triage

Review disposition: the user completed a rough page-level review on 2026-07-25 and accepted the current evidence-calibrated wording without correction. The P0/P1 items below are retained as future strict paper-use verification prompts, not unresolved ingest blockers.

### P0

- `HA09-4`/`HA09-5`, PDF p.5 — Evidence: the paper assumes 90% E2 from `163Lu`, then derives `167Ta` B(E2) ratios used to support similarity. Agent inference: the strength argument is partly circular. User check: exact assumption, propagation into all three ratios, and whether independent evidence remains sufficient. Risk: quoting ratios without the assumption falsely presents them as measured.

### P1

- P1: possible SD-TSD interaction and signature-partner rejection, Figs.3-4.

### P2/P3

- P2: topology/spin transcription. P3: navigation.

## Human Review Record

- 2026-07-25: the user completed a rough review of this source page and accepted its current claims, attribution boundaries, locators and stated limitations without requesting corrections.

## Review Status

Page-level review is complete for this ingest round. Claim-level `needs_review` and Analytical Reconstruction review markers remain unchanged because this was a rough review rather than exhaustive claim-by-claim paper certification.

## Extracted Pages

- Nuclei: [[167ta]]
- Concepts: [[wobbling-motion]]
- Methods: [[angular-correlation]]

## Non-source Notes and Follow-up

Do not report the `B(E2)` ratios without stating the 90%-E2 assumption.

## Day18 checkpoint054修订：外来E2假定依据与推转模型对比边界

原HA09-claims保持；旧HA09-D18-1降格为superseded。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HA09-D18-1 | **superseded**：旧关于“教科书式循环论证”的过强断言降格，由HA09-D18-2/3分层记录作者的假定前提、计算结果与推转模型对比逻辑。 | task-correction | superseded-interpretation | 本段D18-2/3；旧lu-ta-wobbling-lineage-result-027 | true |
| HA09-D18-2 | 本文在无法测定线偏振的条件下，明确假定TSD2到TSD1连接线具有约90%的E2成分（该数值引自163Lu），据此提取出39/2、43/2、47/2态的B(E2_out)/B(E2_in)为0.32(4)至0.37(4)。 | source-result-and-method | direct | PDF p.5；Sec. III | true |
| HA09-D18-3 | 作者将上述提取的比值与传统推转模型（预测比值<=0.01）对比，指出二者存在显著差异，据此提出167Ta可能是Lu同位素之外首个表现出wobbling特征的核；若连接线实际为M1主导（E2份额~3%），则比值将降至~0.011，与推转模型相容，显示该结论对90% E2假定的直接依赖。 | author-interpretation-boundary | direct-and-boundary | PDF p.5；Sec. IV | true |
