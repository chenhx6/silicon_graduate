---
type: source
title: "Bringel et al. 2005 - Evidence for wobbling excitation in 161Lu"
aliases: [Bringel 2005 161Lu wobbling]
created: 2026-07-16
updated: 2026-07-25
status: active
review_status: human-reviewed
source_type: journal-article
reading_depth: deep-read
title_original: "Evidence for wobbling excitation in 161Lu"
authors: [P. Bringel, G. B. Hagemann, H. Hübel, A. Al-khatib, P. Bednarczyk, A. Bürger, D. Curien, G. Gangopadhyay, B. Herskind, D. R. Jensen, D. T. Joss, Th. Kröll, G. Lo Bianco, S. Lunardi, W. C. Ma, N. Nenoff, A. Neußer-Neffgen, C. M. Petrache, G. Schönwasser, J. Simpson, A. K. Singh, N. Singh, G. Sletten]
journal: European Physical Journal A
year: 2005
volume: 24
pages: 167-172
doi: 10.1140/epja/i2005-10005-7
canonical_source: https://doi.org/10.1140/epja/i2005-10005-7
citation_key: bringel_2005_Evidencewobbling
raw_file: "raw/papers/2005_Bringel et al_Evidence for wobbling excitation in 161Lu.pdf"
raw_sha256: 048AAD3F155D237B3C86C88D160474E925E55D6E3622BFFA82D57B32B099FF59
nuclei: [161lu]
reactions: ["139La(28Si,6n)161Lu"]
experiments: []
models: [cranked-nilsson-strutinsky-model]
observables: [moments-of-inertia, wobbling-energy]
methods: [gamma-gamma-coincidence]
tags: [experiment-ingest, wobbling, suggested, triaxial-superdeformation]
---

# Evidence for wobbling excitation in `161Lu`

## Bibliographic Record

EPJ A 24, 167-172 (2005), DOI `10.1140/epja/i2005-10005-7`; PDF/BibTeX identity checked.

## Scope and Reading Depth

- Completed reading_depth: `deep-read`
- Covered scope: full article, setup, TSD1 extension, TSD2 discovery, rotational systematics and limitations.
- Not covered: unpublished/forthcoming detailed level data and independent model calculations.
- Coverage caveats: electromagnetic properties of TSD2→TSD1 links were not determined; energies/spins are tentative.

## Paper Question and Scientific Motivation

- Author-explicit motivation: extend Lu-isotope wobbling systematics to lighter `161Lu` and test whether a newly found TSD2 sequence behaves like the n_w=1 partners in heavier Lu isotopes (PDF pp.167-168).

## Method and Design Logic

- Build and extend the TSD level scheme from high-fold EUROBALL coincidences, compare excitation, alignment and moments of inertia with `163,165,167Lu`, and state explicitly which electromagnetic measurements remain unavailable (PDF pp.168-172, Figs.1-8).

## Key Evidence and Reasoning Chain

- TSD2 decay links and similar rotational systematics → candidate common TSD family; lack of δ/polarization/lifetimes → no direct E2-strength test; isotope analogy → authors say “strongly suggest,” not confirm, wobbling (PDF pp.170-172).

## Summary

This is a deliberately weaker case: the authors say Lu-isotope systematics “strongly suggest” `n_w=0,1`, while explicitly acknowledging that the final electromagnetic proof is missing.

## Experimental or Theoretical Setup

`139La(28Si,6n)161Lu` at 175 MeV, Vivitron/IReS Strasbourg, EUROBALL; `2.8×10^9` presorted events in cubes/hypercube.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BR05-1 | TSD1 was extended by six transitions and a weaker TSD2 sequence decaying to TSD1 was discovered. | experimental-fact | direct | PDF pp.168-170, Figs.1-3 | true |
| BR05-2 | TSD1/TSD2 populations are about `1.4%/0.6%` of the `161Lu` channel. | experimental-fact | direct | PDF p.170 | true |
| BR05-3 | TSD bands show rotational/alignment systematics similar to heavier odd-A Lu isotopes; TSD2 lies about 650 keV above TSD1 in the tentative scheme. | experimental-fact | direct | PDF pp.170-171, Figs.5-8 | true |
| BR05-4 | Absolute excitation energies and spins are not firmly established. | experimental-fact | direct | PDF p.171 | true |
| BR05-5 | Electromagnetic properties of the `ΔI=1` links could not be determined and are explicitly identified as the missing final proof. | experimental-fact | direct | PDF p.171 | true |
| BR05-6 | Authors conclude that systematics strongly suggest TSD1/TSD2 as `n_w=0/1` wobbling excitations. | author-interpretation | contextual | PDF pp.171-172, Summary | true |

## Nuclear Structure Information

TSD1 is extended and a weak TSD2 sequence is connected to it; absolute excitation energies/spins remain tentative and TSD2 lies roughly 650 keV above TSD1 in the proposed scheme.

## Authors' Interpretation

The authors interpret the pair as n_w=0/1 primarily from Lu-isotope systematics and explicitly identify electromagnetic characterization as the missing final proof.

## Model Results

No independent transition-strength PRM test is presented for the assignment. Cranked-systematics discussion concerns shapes, alignments and crossings rather than a direct wobbling observable.

## Competing Interpretations and Limitations

Shape differences and neutron crossings are discussed; no measured mixing ratio, polarization or relative E2 strength closes the assignment.

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| BR05-AR-1 | Core reconstruction | This source establishes a linked systematic candidate, not an electromagnetic wobbling identification. | Key Results and Competing Interpretations above | unreviewed |
| BR05-AR-2 | Assumptions and dependencies | The adopted band identities, mixing-ratio branches, configuration assignments, and model inputs are valid within the stated measured range. | Method/results/model sections cited above | unreviewed |
| BR05-AR-3 | Transfer conditions | Transfer only the measured observables and their explicit conditions; do not transfer the author interpretation without equivalent link and configuration evidence. | Source scope and claim locators above | unreviewed |
| BR05-AR-4 | Failure conditions | Alternative branch, band identity, configuration, or model dependence can weaken the structural label even when the measured transitions remain valid. | Competing Interpretations and Limitations above | unreviewed |
| BR05-AR-5 | Reverse/falsification test | Obtain independent lifetimes/multipolarities or common-input competing-model tests targeted to the stated evidence gap. | Follow-up observables identified by the source/Agent | unreviewed |
| BR05-AR-6 | Research-question decision | Retain the source in the project/synthesis evidence map with the source-local review boundary explicit. | Whole-source assessment | unreviewed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: The Wiki already contained the broader wobbling topic and related candidate map, but not this source in a complete source-local evidence and review structure.
- Effect of this source: supports
- Reason: This source establishes a linked systematic candidate, not an electromagnetic wobbling identification.
- Persistence decision: project update / synthesis update
- Review state: page-level `human-reviewed`; Key Results claims remain `needs_review: true` for future claim-specific paper use.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| limits | [[wobbling-motion]] | Explicit example where systematic similarity is evidence but not final proof. |

## Human Review Triage

Review disposition: the user completed a rough page-level review on 2026-07-25 and accepted the current evidence-calibrated wording without correction. The P0/P1 items below are retained as future strict paper-use verification prompts, not unresolved ingest blockers.

### P0

- `BR05-4`/`BR05-5`/`BR05-6`, PDF pp.170-172 — Evidence: spins/energies are tentative and no mixing ratio, polarization, lifetime or relative E2 strength is measured. Agent inference: this is a systematics-only candidate. User check: whether any cited external measurement closes the gap. Risk: presenting it as observed/confirmed would convert analogy into direct evidence.

### P1

- P1: check the Lu-isotope alignment/MoI homology and neutron-crossing caveats in Figs.5-8.

### P2/P3

- P2: population and tentative-energy transcription. P3: navigation.

## Human Review Record

- 2026-07-25: the user completed a rough review of this source page and accepted its current claims, attribution boundaries, locators and stated limitations without requesting corrections.

## Review Status

Page-level review is complete for this ingest round. Claim-level `needs_review` and Analytical Reconstruction review markers remain unchanged because this was a rough review rather than exhaustive claim-by-claim paper certification.

## Extracted Pages

- Nuclei: [[161lu]]
- Concepts: [[wobbling-motion]]
- Methods: [[gamma-gamma-coincidence]]

## Non-source Notes and Follow-up

Keep wording at “evidence/strongly suggests,” never “observed/confirmed.”

## Day18 checkpoint054修订：转动性质类比与电磁观测量未测状态

原BR05-claims保持；旧BR05-D18-1降格为superseded。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BR05-D18-1 | **superseded**：旧关于“不具备哪怕单一项证据”的断言降格，由BR05-D18-2/3分层记录作者发现的TSD带结构与明确指出的测量局限。 | task-correction | superseded-interpretation | 本段D18-2/3；旧lu-ta-wobbling-lineage-result-027 | true |
| BR05-D18-2 | 本文发现161Lu中TSD1和微弱TSD2能级序列，其动态转动惯量J^(2)和排列角动量ix展现出与重奇A镥同位素（163,165Lu）高度相似的转动系统学特征。 | source-result-and-method | direct | PDF pp.168-171 Figs. 1-8；Sec. 3 | true |
| BR05-D18-3 | 作者明确指出由于统计限制，连接线Delta I = 1的电磁多极性（DCO/偏振）与能级寿命无法测定，自旋与绝对激发能量仍具暂定性（tentative）；作者据此将TSD1/TSD2作为wobbling候选带提出，并强调电磁跃迁测定是最终确证的必要条件。 | author-interpretation-boundary | direct-and-boundary | PDF p.171 Summary；Sec. 4 | true |
