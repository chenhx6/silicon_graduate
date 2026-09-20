---
type: source
title: "Hamilton 1948 - Polarization and direction of propagation of successive quanta"
aliases: [Hamilton 1948 direction-polarization correlation]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: theory-method
reading_depth: deep-read
title_original: "Polarization and Direction of Propagation of Successive Quanta"
authors: [Donald R. Hamilton]
journal: "Physical Review"
year: 1948
volume: 74
pages: "782-787"
canonical_source: "Hamilton, Phys. Rev. 74, 782 (1948)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1948_Hamilton_Polarization and Direction of Propagation of Successive Quanta.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1948_Hamilton_Polarization and Direction of Propagation of Successive Quanta.pdf"
raw_sha256: "f569db64c7e402558fd574839ba5c3da56bc8ecf1b37dab330be706118dc0879"
nuclei: [generic]
reactions: [successive-gamma-cascade, resonance-radiation]
experiments: [polarization-correlation-formalism]
models: [direction-polarization-correlation, statistical-substate-population]
observables: [linear-polarization, angular-correlation, relative-parity, multipole-order]
methods: [polarization-correlation, angular-correlation]
tags: [polarization, angular-correlation, historical-formalism, parity]
---

# Polarization and direction of propagation of successive quanta

## Bibliographic Record

- D. R. Hamilton, *Phys. Rev.* **74**, 782–787 (1948).

## Scope and Reading Depth

- The in-scope six-page article was read end-to-end, including Eqs.(1–15), the 16 dipole/quadrupole combinations, efficiency discussion, parity-group summary and magnetic-field boundary. The following scan page (pp.788 onward) is an unrelated H. C. Corben article and was excluded from this source.

## Formalism

With the first γ defining the quantization axis, Hamilton writes the second-γ polarization intensities along the local `eθ/eφ` axes in terms of `f_|Δm|` (dipole) and `g_|Δm|` (quadrupole) functions (PDF pp.783–784, Eq.1). Electric/magnetic radiation of a fixed multipole order has the same angular distribution but orthogonal polarization. The directional-correlation function is `W(θ)=1+a2 cos²θ+a4 cos⁴θ` (p.784, Eq.6).

For the case in which one detector is polarization insensitive, Eqs.(8a–b) give polarization intensities for each first/second multipole combination. Hamilton then generalizes to finite relative efficiencies `αAB` and `αBC` when either photon may enter either detector (pp.784–786, Eqs.9–15). The sum of the two polarization intensities recovers `W(θ)` independently of detector efficiency, while their ratio carries the parity/multipole information.

## What the Observable Can and Cannot Do

The sixteen dipole/quadrupole sequences collapse into identifiable groups. For same-order electric/magnetic combinations, the polarization-direction correlation can distinguish relative parity groups even when it cannot uniquely identify the multipole order. Mixed dipole–quadrupole cases are efficiency independent only in the electric–magnetic group; same-electric or same-magnetic cases retain efficiency factors (pp.786–787). With partial discrimination of which photon reaches the polarization-sensitive detector, the relative parities of the three levels can be uniquely assigned, but the paper explicitly says that multipole-order information is no better than a directional-correlation experiment alone (p.787).

Magnetic fields preserve the correlation only when parallel to the propagation direction of the unpolarized quantum; transverse fields can wash it out (p.788's final paragraph belongs to the same Hamilton article before the unrelated Corben page marker).

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HAM48-1 | Direction–polarization correlations extend directional-correlation formalism to 16 dipole/quadrupole combinations. | method-result | direct | PDF pp.783–787, Eqs.1–15 | true |
| HAM48-2 | Relative parity can be grouped or uniquely assigned with partial first/second-photon discrimination. | parity-assignment-method | direct | PDF pp.786–787 | true |
| HAM48-3 | Detector efficiencies cancel only for specified mixed-multipole groups. | method-boundary | direct | PDF pp.785–787, Eqs.13–15 | true |

## Summary

Hamilton supplies the formal direction–polarization bridge that later Compton/PDCO experiments implement with detector-specific response functions.

## Competing Interpretations and Limitations

- Multipole order can remain grouped even when relative parity is determined.
- The formal results assume the stated substate/phasing conditions and do not substitute for modern calibration or finite-geometry simulation.

## Analytical Reconstruction and Self-Audit

| ID | Audit item | Agent judgment | Locator | Status |
|---|---|---|---|---|
| HAM48-AR-1 | Correlation chain | Direction of first quantum → statistical substates → `W(θ)` plus orthogonal polarization components; the sum remains the directional correlation. | PDF pp.783–787, Eqs.1–15 | self-checking |
| HAM48-AR-2 | Efficiency boundary | Some mixed-multipole groups cancel detector efficiencies, while same-electric/magnetic groups do not; calibration cannot be omitted generically. | PDF pp.785–787, Eqs.13–15 | self-checking |
| HAM48-AR-3 | Assignment scope | Relative parity is more robust than unique multipole order; the result is a formal method, not a modern detector calibration. | PDF p.787 | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[angular-correlation]], [[linear-polarization-asymmetry]] and the historical direction–polarization lineage behind HS-041, HS-072 and HS-092.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `HAM48-P0-1`: Keep the in-scope page boundary explicit; do not ingest the adjacent Corben article as part of Hamilton's nuclear-polarization source.

## Extracted Pages

- Methods: [[angular-correlation]], [[linear-polarization-asymmetry]]。
