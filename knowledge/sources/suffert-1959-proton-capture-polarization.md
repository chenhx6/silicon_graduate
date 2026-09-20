---
type: source
title: "Suffert, Endt & Hoogenboom 1959 - Polarization measurements of proton-capture gamma rays"
aliases: [Suffert 1959 proton capture polarization]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: experiment-and-method
reading_depth: deep-read
title_original: "Polarization Measurements of Proton Capture Gamma Rays"
authors: [M. Suffert, P. M. Endt, A. M. Hoogenboom]
journal: Physica
year: 1959
volume: 25
pages: "659-670"
canonical_source: "Suffert, Endt & Hoogenboom, Physica 25, 659 (1959)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1959_Suffert et al_Polarization measurements of proton capture gamma rays.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1959_Suffert et al_Polarization measurements of proton capture gamma rays.pdf"
raw_sha256: "ea2742bd196d30497fc919839fb249dfd7e50a88411411831d981604b2016669"
nuclei: [25Al, 31P, 33Cl]
reactions: [24Mg-p-gamma, 30Si-p-gamma, 32S-p-gamma]
experiments: [utrecht-cockcroft-walton, nai-compton-polarimeter]
models: [angular-distribution-mixing-ratio]
observables: [linear-polarization, compton-asymmetry, E2-M1-mixing-ratio, spin-parity]
methods: [compton-polarimetry, angular-distribution, proton-capture]
tags: [polarization, proton-capture, historical-method, mixing-ratio]
---

# Polarization measurements of proton-capture γ rays

## Bibliographic Record

- M. Suffert, P. M. Endt & A. M. Hoogenboom, *Physica* **25**, 659–670 (1959).

## Scope and Reading Depth

- The 12-page article was read end-to-end, including Eqs.(1–9), Figs.1–4, Table I, corrections, discussion of all eight lines and references. The scan's page order was checked; no unrelated neighboring article is included in this source page.

## Experimental Design

Eight γ rays from resonances in `24Mg(p,γ)25Al`, `30Si(p,γ)31P` and `32S(p,γ)33Cl`, with energies `0.8–8.0 MeV`, were emitted at 90° to the proton beam. A 2-inch NaI scattering crystal and two 4-inch NaI counters at interchangeable azimuths measured the Compton counter ratio (PDF pp.659–664, Figs.1–3). A ratio `R=[(NB1/NA1)/(NB2/NA2)]^{1/2}` gives `P=(1/p)(R−1)/(R+1)` after eccentricity/background and solid-angle corrections (pp.664–667, Eq.9).

The paper derives the proton-capture direction–polarization correlation for mixed M1+E2 or E1+M2 transitions, including the sign of the `cos 2φ` term (pp.660–662, Eqs.1–7). The Compton analyzing power is the Klein–Nishina ratio `p(θ)`, and the shortest statistical run time maximizes `σ_c(θ)p²(θ)` (p.662, Eq.8). Corrections include finite scattering azimuth (about 12% reduction in `p`), scattering-angle (≤3%), solid angle (≤1.5%), target eccentricity and contaminant/off-resonance background (pp.665–667).

## Results

Table I resolves ambiguities left by angular distributions. The `2.85 MeV` and `2.86 MeV` levels in `33Cl` are assigned `5/2+` and `3/2−`; the `2.69`/`2.24 MeV` lines in `25Al` and `2.85 MeV` line in `33Cl` are predominantly M1, while the `8.04 MeV` `31P` line is predominantly E2 (abstract, Table I, pp.667–669). The `33Cl` 2.86-MeV parity conclusion uses combined runs 6/7; the high-energy `31P` polarization is acknowledged as statistically limited and potentially affected by pair production/bremsstrahlung (p.669).

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SEH59-1 | Compton polarization resolves spin/parity or E2/M1 alternatives left by proton-capture angular distributions. | experiment-result | direct | PDF pp.659–669, Table I | true |
| SEH59-2 | Counter-ratio polarization requires geometry, eccentricity, background and analyzing-power corrections. | method-result | direct | PDF pp.661–667, Eqs.5–9 | true |
| SEH59-3 | The 8.04-MeV result retains a pair-production/bremsstrahlung and statistical limitation. | limitation | direct | PDF p.669 | true |

## Summary

Suffert *et al.* demonstrate how linear polarization supplies the missing observable for proton-capture spin/parity and mixing-ratio ambiguities, while preserving a detector-specific response chain.

## Competing Interpretations and Limitations

- High-energy attenuation and finite geometry can bias the polarization; the paper does not provide a modern response simulation.
- Angular-distribution alternatives depend on the external angular data and their own consistency, so polarization is not independent of those assumptions.

## Analytical Reconstruction and Self-Audit

| ID | Audit item | Agent judgment | Locator | Status |
|---|---|---|---|---|
| SEH59-AR-1 | Ambiguity resolution | Angular-distribution alternatives are separated by the sign/magnitude of Compton polarization, not by polarization alone detached from `R` and `p`. | PDF pp.660–669, Table I | self-checking |
| SEH59-AR-2 | Detector response | `p(θ)`, finite geometry, eccentricity and background corrections are setup-specific; no universal high-energy polarimeter sensitivity follows. | PDF pp.661–667, Eqs.5–9 | self-checking |
| SEH59-AR-3 | High-energy boundary | Pair production/bremsstrahlung may attenuate the 8.04-MeV result; the authors leave that discrepancy unresolved. | PDF p.669 | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[compton-polarimetry]], [[linear-polarization-asymmetry]], [[angular-distribution]] and the spin/parity evidence checklist; it supplies a proton-capture calibration lineage distinct from in-beam heavy-ion alignment.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `SEH59-P0-1`: Preserve the geometry/energy-specific Compton efficiency and the high-energy pair-production boundary before transferring the historical `P` values.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]], [[angular-distribution]]。
