---
type: source
title: "Bhat et al. 2014 - Investigation of doublet bands in 124,126,130,132Cs with TPSM"
aliases: [Bhat 2014 Cs TPSM, A≈130 Cs triaxial projected shell model]
created: 2026-09-29
updated: 2026-09-29
status: ai-draft
review_status: unreviewed
source_type: theory
reading_depth: deep-read
title_original: "Investigation of doublet-bands in 124,126,130,132Cs odd-odd nuclei using triaxial projected shell model approach"
authors: ["G. H. Bhat", "R. N. Ali", "J. A. Sheikh", "R. Palit"]
journal: "Nuclear Physics A"
year: 2014
volume: 922
pages: "150-162"
doi: "10.1016/j.nuclphysa.2013.12.006"
arxiv: "1312.6963v1"
language: en
canonical_source: "G. H. Bhat et al., Nucl. Phys. A 922 (2014) 150-162, doi:10.1016/j.nuclphysa.2013.12.006; arXiv:1312.6963v1."
citation_key:
library_file: "raw/papers/gpt/day3-mean-field-20260929/bhat-2014-tpsm-124-132cs.pdf"
raw_file: "raw/papers/gpt/day3-mean-field-20260929/bhat-2014-tpsm-124-132cs.pdf"
raw_sha256: "3d1e411d0dfad9d565aa5134d9ad75710a2cbb31607286f0bbc9c8b0537a9757"
nuclei: [124cs, 126cs, 130cs, 132cs]
models: ["triaxial-projected-shell-model", "triaxial-Nilsson-model", "BCS-pairing"]
observables: ["band-energies", "B(E2)", "B(M1)", "B(M1)/B(E2)", "signature-staggering"]
methods: ["angular-momentum-projection", "configuration-mixing", "Hill-Wheeler-diagonalization"]
tags: [a130, chiral-candidate, odd-odd, TPSM, triaxiality, configuration-mixing]
---

# Investigation of doublet-bands in 124,126,130,132Cs using TPSM

## Bibliographic Record

- G. H. Bhat, R. N. Ali, J. A. Sheikh & R. Palit, *Nuclear Physics A* **922**, 150–162 (2014), DOI [`10.1016/j.nuclphysa.2013.12.006`](https://doi.org/10.1016/j.nuclphysa.2013.12.006).
- Lawful open version: [arXiv:1312.6963v1](https://arxiv.org/abs/1312.6963), submitted 2013-12-25. Crossref verified the published title, authors, year, volume and pages; the locally preserved evidence is the arXiv v1, not an independently inspected publisher proof.
- Local PDF: `raw/papers/gpt/day3-mean-field-20260929/bhat-2014-tpsm-124-132cs.pdf`; 247,430 bytes; SHA-256 `3d1e411d0dfad9d565aa5134d9ad75710a2cbb31607286f0bbc9c8b0537a9757`.
- Local BibTeX search found no unique citation-key entry; no key was inferred or added to the protected `.bib`.

## Scope and Reading Depth

- Completed `deep-read` of the 14-page arXiv v1 main paper: abstract/introduction, TPSM construction, deformation input Table 1, band diagrams Figs.1–2, energy comparison Fig.3, configuration decomposition Fig.5, transition-probability comparisons Figs.6–9 and conclusion. The deformation table, `130Cs` model-vs-data energy plot and transition-strength figures were visually checked.
- Not covered: the cited `126Cs` primary experiment in Ref. [18] was not independently re-read; the publisher's final typeset version was not acquired; model code and parameter covariance are unavailable. Ref. [32] for `130Cs` was subsequently identified as Simons et al. 2005 and cross-checked against its primary source page.
- Coverage caveat: arXiv v1 is the verified full text. Numerical and wording inconsistencies that may depend on a later journal correction/version remain `needs_review`.

## Paper Question and Scientific Motivation

The paper asks whether observed near-degenerate yrast/partner bands in odd–odd `124,126,130,132Cs` show transition-probability patterns expected for chiral symmetry breaking, and whether multi-quasiparticle TPSM can describe those patterns (Abstract; PDF pp.1–2).

## Method and Design Logic

- The odd–odd basis contains one-neutron plus one-proton quasiparticle configurations, formed from a triaxial Nilsson basis with BCS pairing (Eq. (1), PDF p.3).
- Three-dimensional angular-momentum projection restores good `I`; the projected configurations are mixed by diagonalizing the shell-model Hamiltonian. The interaction contains quadrupole–quadrupole, monopole-pairing and quadrupole-pairing terms (Eqs. (2)–(3), PDF pp.3–4).
- Table 1 gives the axial/triaxial Nilsson inputs `ε, ε′`; Figs.1–2 show projected configurations and Fig.3 compares mixed TPSM energies with previously reported levels. Electromagnetic matrix elements are calculated with effective charges and gyromagnetic factors (PDF pp.4–6, 10–13).

## Key Evidence and Reasoning Chain

1. The model generates projected `K`-configuration bands from the triaxial one-neutron/one-proton basis and mixes them at fixed spin (Eqs. (1)–(3); Figs.1–2, PDF pp.3–5).
2. Fig.3 compares the mixed TPSM yrast/side-band energies with known `124,126,130,132Cs` levels; the plotted experimental points are taken from earlier references, not measured by this theory paper (Fig.3 caption, PDF p.6).
3. For `126Cs`, Fig.6 compares calculated absolute `B(E2)`, `B(M1)` and selected interband strengths with a previously published lifetime/transition-probability data set from Ref. [18] (PDF p.9). This is a theoretical comparison to an external experiment, not a new measurement; Ref. [18] was not re-read here.
4. For `130Cs`, Fig.8 shows calculated absolute transition strengths and compares the measured `B(M1)/B(E2)` ratios in Simons et al. 2005 Ref. [32] (PDF p.11). The primary experiment reports ratios from its transition data, not absolute `130Cs` strengths or lifetimes; Bhat's absolute curves remain model outputs.
5. The authors find the `126Cs` energy/strength comparison consistent with a chiral interpretation, while the `124,130,132Cs` transition patterns are predictions or limited ratio comparisons; they call for lifetime measurements before confirming those interpretations (Conclusion, PDF p.13).

## Summary

This paper demonstrates an A≈130 odd–odd application of triaxial projected configuration mixing, including a `130Cs` case. It is useful evidence that TPSM can calculate projected bands and electromagnetic strengths in nearby nuclei. It does not test `131Ce` and does not validate Hara–Sun's separate `N=76/78` historical candidates. For `130Cs`, agreement is with energies and intensity-derived `B(M1)/B(E2)` ratios; the plotted absolute `B(E2)` and `B(M1)` are calculations, and the authors still request lifetimes. The paper therefore supports the model route while limiting what can be inferred from near-degeneracy or ratio agreement alone.

## Experimental or Theoretical Setup

- Framework: triaxial Nilsson + BCS intrinsic basis; angular-momentum projection; projected multi-configuration mixing with quadrupole–quadrupole and pairing interactions.
- Inputs in Table 1 (PDF p.4): `ε/ε′ = 0.256/0.170` (`124Cs`), `0.260/0.150` (`126Cs`), `0.160/0.145` (`130Cs`), and `0.170/0.150` (`132Cs`). These are model inputs, not measured deformations.
- Compared experimental material is inherited from cited sources: energies for the four isotopes; absolute lifetime-derived strengths for `126Cs` (Ref. [18]); `B(M1)/B(E2)` ratios for `130Cs` and `132Cs` (Refs. [32] and [27]). Ref. [32] is Simons et al. 2005, the same `130Cs` Euroball data set, not an independent experiment. Ref. [18] and Ref. [27] were not re-read here.

## Key Results

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BHA14-1 | TPSM uses one-neutron/one-proton quasiparticle states, three-dimensional angular-momentum projection and projected configuration mixing with Q·Q and pairing interactions. | model-definition | direct | Eqs. (1)–(3), PDF pp.3–4 | false |
| BHA14-2 | Table 1 uses `ε=0.160, ε′=0.145` for `130Cs`; Eq. (3) relates the parameters approximately by `γ=tan⁻¹(ε′/ε)`. | model-input | direct | Eq. (3), Table 1, PDF p.4 | false |
| BHA14-3 | TPSM mixed energies are compared with previously published yrast/side-band energies for all four Cs isotopes. | model-result / data comparison | direct | Fig.3, PDF p.6 | false |
| BHA14-4 | For `130Cs`, absolute `B(E2)` and `B(M1)` curves in Fig.8 are calculations; the overlaid `B(M1)/B(E2)` points are described as measured ratios from Ref. [32]. | model-result / secondary comparison | direct | Fig.8 and caption, PDF p.11 | true |
| BHA14-5 | The authors say detailed absolute transition-probability data exist for `126Cs`; for `124,130,132Cs` they provide predictions/limited ratio comparisons and request lifetime measurements before confirming chirality. | author-interpretation / limitation | direct | Abstract, Fig.6 caption, Conclusion, PDF pp.1, 9, 13 | true |
| BHA14-6 | Applying the paper's Eq. (3) to its Table 1 gives `γ≈42.2°` for `130Cs` and `≈41.4°` for `132Cs`, while the prose says the chosen non-axial deformation approximately corresponds to `γ≈30°`. This is an internal parameter/wording mismatch in arXiv v1, not a corrected deformation measurement. | source-consistency audit | Codex calculation | Eq. (3), Table 1, PDF pp.4–6 | true |

## Nuclear Structure Information

- The calculations cover odd–odd `124,126,130,132Cs`. The `130Cs` model case is `Z=55,N=75`; it is not the `131Ce` (`Z=58,N=73`) target and is not a computation of Hara–Sun's `N=76/78` entries.
- No new experimental level scheme or lifetime is established by this theory paper. Band energies and reported intensity ratios are comparisons to previously published data; calculated transition strengths remain model results.

## Authors' Interpretation

- For `126Cs`, the authors interpret the energy and measured transition-probability agreement as consistent with chiral symmetry breaking.
- The `130Cs` calculation shows `B(M1)` patterns the authors describe as characteristic of chiral bands, and the calculated ratios reproduce cited measured ratios. The paper nevertheless does not claim a new direct measurement of absolute strengths for `130Cs`; its conclusion requests lifetimes for the remaining isotopes.

## Model Results

- Fig.3 reproduces the broad spin-dependent energy trends of previously reported bands; Fig.8 predicts `130Cs` absolute `B(E2)`, `B(M1)` and interband strengths and compares selected ratios to data.
- Model deformation inputs, effective charges, pairing and configuration space are assumptions. The apparent ratio agreement does not independently determine `ε, ε′`, prove a stable triaxial minimum or establish a chiral geometry.

## Competing Interpretations and Limitations

- The paper itself notes that near-degenerate bands do not necessarily arise from chiral symmetry breaking; electromagnetic selection patterns are needed (Introduction and Conclusion, PDF pp.2, 13).
- For `130Cs`, the absolute transition strengths used in the TPSM chiral pattern are not measured in this paper; only earlier intensity-derived ratios are compared. No lifetime means the absolute-strength test remains open.
- For `132Cs`, the partner band is only known to about `I=14`, and the authors attribute near-degeneracy to a crossing of bands from different quasiparticle configurations (PDF pp.9–10), an alternative to a fixed two-band interpretation.
- The Table 1/Eq. (3) gamma parameter audit does not resolve whether the discrepancy is a convention/approximation issue or a version difference. Keep `BHA14-6` at `needs_review: true` and check the published version before quoting a derived `γ`.
- `Ref. [32]` is verified as Simons et al. 2005 and is the same `130Cs` Euroball data set; do not count Bhat's theory comparison as an independent experiment. The `126Cs` Ref. [18] data remain unaudited here.

## Analytical Reconstruction

| ID | Audit item | Agent assessment | Evidence / locator | Status |
|---|---|---|---|---|
| AR-BHA14-1 | Core reconstruction | The contribution is a model/data-comparison route: triaxial intrinsic basis → good-`I` projection → configuration mixing → energy and transition-strength comparison. | Eqs. (1)–(3), Figs.3, 6, 8, PDF pp.3–6, 9, 11 | self-checking |
| AR-BHA14-2 | Assumptions and dependencies | Predictions depend on `ε, ε′`, pairing, effective charges, gyromagnetic factors, projected configuration truncation and the identity of the reused experimental bands. | Table 1; Figs.3, 6, 8; PDF pp.4–11 | self-checking |
| AR-BHA14-3 | Transfer conditions | The `130Cs` case establishes that TPSM is a usable neighboring-nucleus model route, but its N=75 data/inputs do not transfer to `131Ce` or the historical N=76/78 cases. | Table 1; Figs.3, 8, PDF pp.4, 6, 11 | provisional |
| AR-BHA14-4 | Failure condition | If the measured mixing ratios, lifetimes or absolute strengths do not follow the predicted pattern, the chiral interpretation must be reduced; energy agreement alone is insufficient. | Fig.8; Conclusion, PDF pp.11, 13 | active-L3 |
| AR-BHA14-5 | Reverse test | Compare the same transition matrix with measured `δ`/polarization, lifetime and absolute `B(E2)/B(M1)`; independently verify Table 1 parameters and cited Ref. [32]. | Fig.8, Table 1, PDF pp.4, 11 | candidate-L3 |
| AR-BHA14-6 | Research-question decision | Add as a method-transfer control to the TPSM model card, not as target-nucleus evidence or an independent experiment. | BHA14-1–6 | completed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: the A≈130 model-choice card already separated static mean field, CSM and projected models, and the Hara–Sun historical axial calculation.
- Effect: `supports` TPSM as a calculational route and `limits` its transfer from neighboring Cs nuclei to `131Ce` or Hara–Sun's N=76/78 candidates.
- Reason: the paper compares TPSM predictions with previous Cs data, but for `130Cs` it overlays intensity-derived ratios rather than absolute measured transition strengths; its own conclusion requests lifetimes. The Table 1/Eq.3 gamma consistency check also remains unresolved.
- Persistence: add one TPSM source, one model-page relation and one model-choice crosswalk row; do not change the `131Ce` hypothesis ranking or create Cs band pages.
- Review state: source/model claims remain `unreviewed`; Codex self-audit does not count as human review.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| foundational-background | [[triaxial-projected-shell-model]] | A≈130 odd–odd Cs implementation, including projected bands and electromagnetic observables. |
| methodological-bridge | [[a130-model-choice-card]] | Shows how TPSM energy and ratio comparisons differ from lifetime/absolute-strength validation; `130Cs` is a neighboring model case only. |
| methodological-bridge | [[simons-2005-130cs-chiral-structures]] | The `130Cs` ratios compared in Fig.8, Ref. [32], are this same Euroball data set; the TPSM theory paper is dependent on it. |
| not-direct-evidence | [[131ce-collective-mode-discrimination]] | Does not calculate `131Ce` and cannot supply its missing transition-level observables or mode evidence. |

## Human Review Triage

### P0

- None identified for this bounded theory-source read.

### P1

- `BHA14-6`: Eq. (3), Table 1 and the `γ≈30°` prose are internally inconsistent for the printed `130Cs/132Cs` parameters in arXiv v1. If a paper cites the deformation, verify the published version and retain the ambiguity until resolved.
- `BHA14-4`: Ref. [32] is now cross-checked against Simons 2005, confirming that the overlay is an intensity-derived ratio from the same Euroball data set. The source still does not provide absolute `130Cs` strengths/lifetimes; keep that evidence boundary and do not count Bhat as a second experiment.

### P2/P3

- Citation key is absent from the protected local Zotero export; source is stably identified by DOI and arXiv ID. Add a key only if a unique Zotero entry is later provided.

## Extracted Pages

- Nuclei: existing `124Cs`, `126Cs`, `130Cs`, `132Cs` records are not asserted or created by this model-only source.
- Bands: no standalone band pages created; source retains its isotope-specific yrast/partner labels.
- Models: [[triaxial-projected-shell-model]]; [[a130-model-choice-card]].

## Non-source Notes and Follow-up

- Verify the final journal version and the primary data in Refs. [18] and [32] before using `130Cs` numerical transition properties as direct experimental support.
- Do not transfer the `130Cs` triaxial parameters or chiral label to `131Ce`.
