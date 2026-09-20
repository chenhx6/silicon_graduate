---
type: source
title: "Klein & Nishina 1929 - Compton scattering from free electrons in Dirac theory"
aliases: [Klein Nishina 1929 Compton formula]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: historical-theory-paper
reading_depth: deep-read
title_original: "Über die Streuung von Strahlung durch freie Elektronen nach der neuen relativistischen Quantendynamik von Dirac"
authors: [O. Klein, Y. Nishina]
journal: "Zeitschrift für Physik"
year: 1929
volume: 52
pages: "853-868"
canonical_source: "Klein & Nishina, Z. Phys. 52, 853 (1929)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1929_Über die Streuung von Strahlung durch freie Elektronen nach der neuen relativistischen Quantendynami.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1929_Über die Streuung von Strahlung durch freie Elektronen nach der neuen relativistischen Quantendynami.pdf"
raw_sha256: "5020b8c9480606b29a96496412219cb3f985ba3f522223d5bf016c407565a40d"
nuclei: []
reactions: []
experiments: []
models: [Dirac-electron, relativistic-Compton-scattering]
observables: [Compton-cross-section, photon-energy-shift, scattering-angle]
methods: [Compton-polarimetry, Klein-Nishina-response]
tags: [Compton, Klein-Nishina, Dirac, historical-theory, detector-response]
---

# Compton scattering from free electrons in Dirac theory

## Bibliographic Record

- O. Klein and Y. Nishina, *Zeitschrift für Physik* **52**, 853–868 (1929).
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1929_Über die Streuung von Strahlung durch freie Elektronen nach der neuen relativistischen Quantendynami.pdf`。
- 16-page German historical theory PDF; OCR was visually spot-checked for equations and section flow. The paper calculates intensity, not the later polarization treatment promised in its conclusion.

## Scope and Reading Depth

- Full paper read: introduction, Dirac Hamiltonian/eigenfunctions, plane-wave perturbation, scattering amplitude, energy-angle dependence, negative-energy/spin terms and comparison with older Dirac–Gordon formulas.
- Not covered: Nishina's subsequent polarization paper and modern detector-response simulations.

## Key Results and Method Boundary

- Dirac relativistic electron dynamics predicts the Compton scattering intensity with corrections of order `hν/(mc²)` relative to older formulas; the result becomes important for hard γ rays.
- The calculation tracks free-electron initial/final spin states and energy/momentum conservation, yielding the angular/energy response later known as the Klein–Nishina cross section.
- The paper explicitly restricts itself to scattering intensity; polarization is deferred to a subsequent work. Modern polarimeter formulas must therefore pair this source with Fagg/Hanna and detector-specific response papers.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KN29-1 | Dirac relativistic quantum dynamics changes the Compton intensity/energy-angle response relative to older Dirac–Gordon formulas. | formalism | direct | PDF pp.853–868, introduction and derivation | true |
| KN29-2 | The source derives a free-electron scattering response used as the theoretical basis for later Klein–Nishina polarimeter calculations. | formalism | direct | PDF pp.853–868 | true |
| KN29-3 | Polarization is not calculated in this paper; it is explicitly deferred to subsequent work. | limitation | direct | PDF p.853 | false |

## Summary

Klein–Nishina 1929 is the relativistic scattering foundation underlying Compton polarimetry. It is a historical response theory source, not a nuclear-structure or polarization-calibration experiment.

## Competing Interpretations and Limitations

The paper's OCR/notation and historical units require care; polarization, finite detector geometry, multiple scattering and background are outside its scope. Do not quote its free-electron response as a complete modern detector sensitivity.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| KN29-AR-1 | Theory chain | Dirac equation → spin-resolved scattering amplitude → relativistic Compton intensity. | PDF pp.854–868 | self-checking |
| KN29-AR-2 | Transfer condition | Use only as free-electron cross-section layer; detector `Q/R`, geometry and polarization require later sources. | Scope/limitation | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[compton-polarimetry]] and the historical response lineage.
- Persistence: link to Simpson, Bass and Garcia-Raffi detector pages; preserve polarization-not-in-this-paper boundary.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `KN29-P0-1`: do not conflate the free-electron intensity formula with detector-specific polarization sensitivity.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]]。
