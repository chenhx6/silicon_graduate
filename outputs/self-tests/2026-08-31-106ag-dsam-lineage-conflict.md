---
type: output
title: "Weekly self-test: 106Ag DSAM lineage conflict"
created: 2026-08-31
updated: 2026-08-31
status: awaiting-review
review_status: unreviewed
tags: [weekly-self-test, 106ag, chirality, dsam, lifetime, evidence-independence]
---

# Weekly self-test: `106Ag` DSAM lineage conflict

## Selection audit

- Run type: `weekly-learning`; counted as a learning cycle: yes.
- Repository-local coverage history: the four earlier `weekly-learning` reports selected `131Ce`, `131Ce`, `131Ce`, and `135Pr`; the 2026-08-19 D21-8 report is a `continuation-audit` and does not count as a learning cycle.
- Continuity slot: not used. The pending `135Pr` PDF/lineage check and `131Ce` D21-8 review produced no new independent evidence in this run and remain deferred.
- Novelty slot: selected the `106Ag` original-DSAM lineage behind the chirality counterexample. It passes the hard gate because the current Wiki treats absolute strengths as configuration-discriminating counter-evidence while both original 2014 lifetime chains were absent from the source corpus.
- Candidate pool and coverage: (1) `106Ag` DSAM/configuration conflict, A≈100 nucleus + absolute `B(M1)/B(E2)` + source independence — selected; (2) `137Nd` D3/D6 partner-lifetime gap — deferred because the direct source already states the missing observable and no new dataset was found; (3) `74As` absolute E1/M1/E2 and reflection-asymmetric-model gap — deferred because the direct source already bounds the claim and no new independent measurement was identified; (4) P-ADO `sigma/I` code mapping — blocked on user-specific inputs.
- Core-source fingerprint: Lieder et al., *Phys. Rev. Lett.* **112**, 202502 (2014), DOI `10.1103/PhysRevLett.112.202502`; Rather et al., *Phys. Rev. Lett.* **112**, 202503 (2014), DOI `10.1103/PhysRevLett.112.202503`, arXiv:1310.7731v1; NNDC/ENSDF reaction-dataset records; Bark 2024 and Wang 2023 only as secondary discovery routes. There is no overlap with the recent `135Pr` or `131Ce` core-source clusters; no cooldown exception was used.
- New knowledge: the vague “contemporary alternative” in the current secondary `106Ag` record resolves into two independent, same-day PRL DSAM chains using the same reaction at different energies and different detector/analysis lineages. Both reject a simple chiral-partner assignment for the two crossing low bands, but they do not provide independent replication of one detailed configuration model.
- Belief revision: retain the robust counterexample “near degeneracy/crossing plus branching fingerprints are insufficient.” Downgrade the stronger synthesis “absolute strengths uniquely establish Lieder's two- versus four-quasiparticle partition” to a source-specific interpretation until both local PDFs, band crosswalks, lifetime fits, and model assumptions are compared claim by claim.

## Scope

This run rebuilt the recent weekly-learning coverage history, screened the Wiki globally, and then inspected CrossRef/arXiv metadata, the arXiv full text of Rather 2014, externally visible Lieder 2014 text, and NNDC/ENSDF reaction records. It compared one Ag isotope and one N=59 isotone. It did not create a source, band, experiment, nucleus, project or L4 page; did not write BibTeX; did not promote a PDF; and did not touch the protected Zotero BibTeX.

## P0

- Scientific P0: none identified. The current Wiki already avoids a final chirality verdict for `106Ag`.
- Git/raw P0: none identified. Controlled downloads produced failure manifests only; no candidate PDF or BibTeX record was promoted.

## P1

1. **Two independent experimental chains, not one experiment plus commentary.** Lieder uses `96Zr(14N,4n)` at `71 MeV` with AFRODITE and reports three negative-parity bands; Rather uses the same reaction at `68 MeV` with 20-clover INGA and independently measures the two crossing bands. Their event samples and author groups are distinct, so the lifetime evidence is experimentally independent even though the physics question and reaction channel overlap.
2. **Agreement at the falsification level.** Both papers reject the earlier simple identification of the two lowest crossing bands as one chiral pair. This is the durable counterexample that can be reused across nuclei.
3. **Disagreement at the detailed interpretation level.** Lieder finds alignments near `6ℏ` for Band 1 and `10ℏ` for Bands 2/3, assigning Band 1 as two-quasiparticle and Bands 2/3 as four-quasiparticle structures. Rather finds approximately equal `B(E2)` values in the two crossing bands, different `B(M1)` behavior, and a TPSM description with one-proton–one-neutron states from the same mean-field triaxial deformation but different projected configurations. These are not identical configuration claims and should not be collapsed into a single independently replicated assignment.
4. **Lifetime-systematics remain analysis dependent.** Rather's arXiv text exposes the global line-shape procedure, side-feeding construction, a `Ge(n,n'γ)` contamination avoidance for the partner `12−` lifetime, and Table I uncertainties. Lieder's visible text records ≈20% average lifetime uncertainty, ≈10% stopping-power contribution, cascade/side-feeding terms, small fitted `δ`, and one example `τ(16−, Band 2)=0.40(4) ps`. A common reanalysis has not been performed.
5. **Local evidence gate remains closed.** Rather's arXiv PDF was read through a direct external viewer, but the controlled local fetch failed; Lieder's candidate institutional URL resolved to a publication list rather than the article. Without local file signatures, hashes, and stable PDF locators, neither paper was ingested and no precise project row was added.

## Required weekly checks

- Necessary companion: partner-resolved absolute `B(M1)` and `B(E2)` exist in both original chains, but a stable band/transition crosswalk plus alignment and model-input comparison is required before claiming one detailed configuration solution is independently confirmed.
- Background/resolution/gate: Rather explicitly treats side feeding, two detector angles, stopping powers and one contamination; Lieder reports cascade/side-feeding and stopping-power contributions. The remaining discrepancy is therefore not reducible to one obvious mislabeled PDF point, but exact fit covariance and band mapping remain unverified locally.
- Source independence: Lieder/AFRODITE at 71 MeV and Rather/INGA at 68 MeV are independent experiments. Bark 2024 and Wang 2023 repeat the Lieder programme lineage and are not additional experiments. The later 2019 3DTAC-CDFT work is a theoretical follow-up, not experimental replication.
- Belief-revision trigger: strengthen one detailed configuration partition only after both original PDFs are locally verified and a transition-by-transition comparison reconciles band identity, lifetimes, branching/mixing inputs, alignments, side feeding and model spaces. Failure of that reconciliation leaves only the falsification-level conclusion robust.
- Isotope boundary: `104Ag` A/B has similar candidate fingerprints but no lifetimes, polarization or dedicated chiral calculation, so it cannot validate either `106Ag` DSAM partition.
- Isotone boundary: odd-odd `104Rh` (`N=59`) has lifetimes for only one partner sequence; it demonstrates why one-sided absolute strengths are insufficient and cannot select between the two `106Ag` chains. Odd-A `105Pd` has different coupling physics and is not used as a direct chiral calibration.

## L3/L4 status

- L3 milestone: completed-provisional. The evidence architecture changed from one secondary counterexample to two independent but interpretation-divergent original experimental chains.
- L4: not started. A common-response lifetime/transition reconstruction would require locally verified spectra, branching/mixing inputs, stopping/feeding assumptions and fit surfaces; those inputs are not established as a reproducible public dataset in this run.

## Deferred important issues

1. **Local dual-source ingest.** Obtain and verify Lieder 2014 and Rather 2014 PDFs, then ingest both in one bounded lineage review so the band crosswalk and incompatible model spaces remain explicit.
2. **2019 3DTAC-CDFT follow-up.** Zhao, Wang and Chen 2019 (DOI `10.1103/PhysRevC.99.054319`, arXiv:1905.10544) supports a two-/four-quasiparticle split and proposes Band 2/3 chiral vibration; ingest only after the two experimental baselines are fixed, because it is theory rather than an independent lifetime dataset.
3. **`137Nd` D3/D6 absolute strengths.** Still important and non-overlapping, but no new dataset was identified in this run.
4. **`74As` absolute cross-parity strengths.** Still needed to separate correlations from stable octupole deformation beyond branching-derived ratios.
5. **Pending weekly reviews.** The `135Pr` partial-independence/branch conflict and `131Ce` D21-8 lineage remain awaiting focused review; neither was silently resolved here.

## Human review focus

- P0: none identified.
- P1: confirm that Lieder and Rather are counted as independent experimental chains, that their common rejection of the simple chiral-pair reading is separated from their nonidentical configuration interpretations, and that the current Wiki's stronger two-/four-quasiparticle wording remains secondary until dual-source ingest.
- Do not use this report as paper admission for a detailed `106Ag` configuration claim until both local PDFs and exact source locators are verified.

## Files, Git, and checks

- Branch: `main`; no task branch was created, and this report is part of the finalized weekly-self-test batch.
- Commit: current main HEAD `Finalize weekly self-tests through 2026-08-31`.
- Publication: final-not-pushed. Fresh fetch and ancestry passed, but both system and Codex bundled Git failed the exact-refspec dry-run because the protected repo-local AskPass executable could not be spawned (`Permission denied`); no real push was attempted.
- Acquisition: controlled Node fetches failed for both candidates; the supposed Peking University PDF was externally identified as a publication list, while Rather's genuine arXiv PDF was readable only through the external viewer. No file was promoted and no BibTeX was written.
- Knowledge pages: unchanged because the dual-source local evidence gate was not met.
- Overview/index/QMD: unchanged/deferred because no knowledge page or local source was added.
