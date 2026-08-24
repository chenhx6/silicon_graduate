---
type: output
title: "Weekly self-test: 135Pr mixing-ratio branch reassessment"
created: 2026-08-24
updated: 2026-08-24
status: awaiting-review
review_status: unreviewed
tags: [weekly-self-test, 135pr, wobbling, mixing-ratio, polarization, evidence-independence]
---

# Weekly self-test: `135Pr` mixing-ratio branch reassessment

## Selection audit

- Run type: `weekly-learning`; counted as a learning cycle: yes.
- Repository-local coverage history: the available three earlier `weekly-learning` reports all selected `131Ce`; the 2026-08-19 D21-8 report is a `continuation-audit` and does not count as a learning cycle.
- Continuity slot: not used. The pending `131Ce` D21-8 review has no new independent evidence or decision-changing conflict in this run, so it remains deferred and does not consume the learning cycle.
- Novelty slot: selected the `135Pr` 747/813/450-keV mixing-ratio branch conflict. It passes the hard gate because the conflicting branch choice reverses the E2/M1 character of the necessary companion observable for the wobbling interpretation.
- Candidate pool and coverage: (1) `135Pr` wobbling versus signature/TiP, angular distribution plus polarization, direct experimental conflict — selected; (2) `106Ag` chirality configuration counterexample, secondary-to-primary lineage gap — deferred; (3) `137Nd` chiral-candidate lifetime/absolute-strength gap — deferred; (4) `74As` E1/octupole-correlation versus stable-deformation boundary — deferred; (5) P-ADO `sigma/I` code mapping — blocked on user-specific inputs.
- Core-source fingerprint: Matta 2015, Sensharma 2019, Lv 2022 main plus supplement, Matta 2021 erratum, Sensharma 2021 corrigendum, Guo 2020 comments, and Sensharma et al. 2026 / arXiv:2403.10749v2. There is no overlap with the recent `131Ce`/Ding/`127Xe`/`129Ba` weekly source cluster; no cooldown exception was used.
- New knowledge: a 2026 peer-reviewed `135Pr` paper adds a new Gammasphere run, combines it with the Sensharma 2019 DGS data, and reports large-`|δ|` solutions for the 746/812/754-keV links together with full `χ²(δ)` comparisons. This is new decision-relevant evidence, but it is only partially independent and supplies no new polarization measurement.
- Belief revision: replace “the branch has not been re-evaluated in a sufficiently explicit analysis” with “two explicit experimental analysis chains now disagree.” The 2026 result strengthens the large-`|δ|` side, while Lv 2022 retains an independent combined `P-R_ac` small-`|δ|` result. The current Wiki cannot adjudicate the wobbling assignment without a common-response analysis or independent absolute electromagnetic strengths.

## Scope

This run audited the existing `135Pr` controversy, rendered the relevant pages of Matta 2015, Sensharma 2019, Lv 2022 and the Lv supplement, and performed a finite CrossRef/arXiv search followed by a Google Scholar domain check for the exact correction/comment lineage and newer direct evidence. The Scholar query returned no results in this runtime, so arXiv, APS/CrossRef, PubMed and NNDC/NSR were used as the verification routes. It did not modify a source, project, nucleus or band page; it did not change review states, download SI, start L4, or touch the protected Zotero BibTeX.

## P0

- Scientific P0: none identified. The existing project already preserves both interpretations and does not state a final wobbling verdict.
- Git/raw P0: none identified. No PDF entered the verified `raw/papers/gpt/` corpus and no BibTeX entry was written.

## P1

1. **New direct evidence is absent from the Wiki corpus.** Sensharma et al., *Phys. Rev. C* **113**, 024313 (2026), DOI `10.1103/3g4p-ncjn`, arXiv:2403.10749v2, directly addresses Lv 2022. The arXiv HTML was read, but the controlled downloader could not save the PDF in this runtime, so no source page or formal project row was created.
2. **The 2026 evidence is partially, not fully, independent.** A new 63-detector Gammasphere run was combined with the Sensharma 2019 DGS run to give `2.5×10^10` fold≥3 events. The event sample therefore contains new data but reuses a core supporting dataset and substantially overlaps the author/analysis lineage.
3. **The conflict is now analysis-chain versus analysis-chain.** The 2026 combined angular-distribution analysis reports `δ=-1.40(+0.14/-0.12)`, `-1.63(+0.02/-0.03)` and `-2.16(+0.06/-0.05)` for 746/812/754 keV, with Fig. 12 favoring the large branch at fixed `σ/I=0.2`. Lv 2022 instead reports `δ=-0.47(+0.09/-0.22)`, `-0.37(+0.10/-0.14)` and `-0.31(+0.10/-0.13)` for 747/813/450 keV from an independent `P-R_ac` dataset. Neither result may be erased by the other without common detector response, alignment and likelihood treatment.
4. **Polarization remains the unresolved companion.** The 2026 paper adds no new polarization for the wobbling links; it treats Matta's positive asymmetries as confirmation of angular-distribution branch selection. Lv's measured polarization central values are near zero and are combined with `R_ac`. Thus the new paper strengthens the large-branch angular evidence but does not independently reproduce the disputed polarization observable.
5. **Corrections do not resolve the physical conflict.** Matta 2021 corrects two Fig. 2 drafting/plotting details and keeps the fits/Table I unchanged. Sensharma 2021 corrects a 770.3-keV label and the Fig. 4 alignment-caption expression and states that conclusions are unchanged. Guo's two arXiv comments challenge branch/polarization handling but are arguments, not new `135Pr` experimental datasets.

## Required weekly checks

- Necessary companion: for the odd-proton one-quasiparticle wobbling claim, a coherent set of E2-dominant `ΔI=1` links remains necessary. The three decisive links still have mutually incompatible branch assignments across the two experimental chains.
- Background/resolution/gate: Lv supplementary pp.3-4 documents the 747/813/450-keV gate and contamination checks; the 2026 paper documents a combined-efficiency, ring-by-ring angular-distribution analysis. The remaining conflict is not explained by an obvious PDF extraction, mislabeled point or single stated contaminant.
- Source independence: Matta 2015 and Sensharma 2019 are supporting experiments with linked interpretation; Lv 2022 is an independent reaction/detector dataset; Sensharma 2026 adds a new run but combines it with the 2019 dataset. Correction notices and comments are not independent experiments.
- Belief-revision trigger: upgrade one branch only if a common analysis reproduces both the full angular likelihood and polarization/`R_ac` response, or if an independent experiment measures consistent polarization/`delta` across several links and preferably absolute `B(E2)_out/B(E2)_in`.
- Isotope/isotone boundary: `134Pr` is a neighboring Pr isotope dominated by odd-odd chirality/signature questions, not a one-quasiproton wobbling calibration. The N=76 isotone `136Nd` is an even-even two-quasiproton case whose clean 751-keV link is M1-dominated; it demonstrates configuration dependence and cannot transfer a branch rule to odd-A `135Pr`.

## L3/L4 status

- L3 milestone: completed-provisional. The literature state has changed materially, but the experiment-level conflict remains open.
- L4: not started. A common-response reconstruction would require ring-by-ring yields, polarization matrices, detector efficiencies/geometry and the complete likelihood/`sigma/I` treatment. These inputs were not established as a reproducible public dataset in this run.

## Deferred important issues

1. **Targeted ingest of the 2026 paper and correction lineage.** Obtain and verify the arXiv v2/published PDF, then ingest the 2026 source with a precise data-lineage statement and connect Matta/Sensharma corrections without treating them as independent evidence.
2. **Common-response branch audit.** Compare the 2026 `χ²(δ)` surface at `σ/I=0.2` with Lv's joint `P-R_ac` surface under common conventions. This should be user-started as L4 only if the necessary numerical inputs become available.
3. **`106Ag` original counterexample.** The chirality project still relies on a later review for the decisive configuration/lifetime counterexample. Pursue in a later novelty cycle if the original experiment can be obtained.
4. **`137Nd` absolute strengths.** The D3/D6 lifetime and interband/intraband strength gap remains important but had lower expected information gain in this run.

## Human review focus

- P0: none identified.
- P1: confirm the partial-independence classification of the 2026 combined dataset, the large- versus small-branch numerical comparison, and the conclusion that the evidence ranking changes from an under-specified gap to an explicit unresolved experimental conflict.
- Do not use this report as paper admission for either wobbling or anti-wobbling wording until the 2026 PDF is locally verified and the exact claim is reviewed against source locators.

## Files, Git, and checks

- Branch: `main`; no task branch was created.
- Commit: current main HEAD `Finalize weekly self-tests through 2026-08-31`.
- Publication: final-not-pushed. Fresh fetch and ancestry passed, but both system and Codex bundled Git failed the exact-refspec dry-run because the protected repo-local AskPass executable could not be spawned (`Permission denied`); no real push was attempted.
- Raw boundary: only controlled downloader manifests were created under `raw/papers/gpt/_incoming/20260824-135pr-mixing-branch/`; no PDF was downloaded, promoted or staged, and no BibTeX file was changed by this task.
- Overview/index/QMD: unchanged because no knowledge page was added and the unverified external source was not ingested. QMD refresh is deferred until targeted ingest or review finalization.
