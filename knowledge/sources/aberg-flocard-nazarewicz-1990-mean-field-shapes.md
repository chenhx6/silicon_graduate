---
type: source
title: "Åberg, Flocard and Nazarewicz 1990 - Nuclear shapes in mean field theory"
aliases: [Aberg Flocard Nazarewicz 1990 mean-field shapes]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: review
reading_depth: deep-read
title_original: "Nuclear Shapes in Mean Field Theory"
authors: [S. Åberg, H. Flocard, W. Nazarewicz]
journal: "Annual Review of Nuclear and Particle Science"
year: 1990
volume: 40
pages: "439-528"
canonical_source: "Åberg, Flocard & Nazarewicz, Annu. Rev. Nucl. Part. Sci. 40, 439-528 (1990)"
library_file: "raw/papers/gpt/high-spin-20260920/形变/1990_Aberg et al_Nuclear Shapes in Mean Field Theory.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/形变/1990_Aberg et al_Nuclear Shapes in Mean Field Theory.pdf"
raw_sha256: "90e3d1324dbf591cc042a3ad3b777a75e00af1463869d9ad557af433469562e6"
nuclei: [generic, 152Dy, 192Hg, 147Gd, 212Rn, 186Pb]
reactions: [generic-high-spin-mean-field]
experiments: [high-spin-spectroscopy, electromagnetic-moments]
models: [Hartree-Fock, Hartree-Fock-Bogoliubov, Nilsson-Strutinsky, cranked-mean-field, relativistic-mean-field]
observables: [shape, beta2, gamma, beta3, quadrupole-moment, band-termination, superdeformation, shape-coexistence]
methods: [mean-field, constrained-HF, HFB, Strutinsky, rotating-frame]
tags: [mean-field, nuclear-shapes, triaxiality, high-spin, octupole, shape-coexistence, superdeformation]
---

# Nuclear shapes in mean-field theory

## Bibliographic Record

- S. Åberg, H. Flocard & W. Nazarewicz, *Annu. Rev. Nucl. Part. Sci.* **40**, 439–528 (1990).
- 规范文件：`raw/papers/gpt/high-spin-20260920/形变/1990_Aberg et al_Nuclear Shapes in Mean Field Theory.pdf`。

## Scope and Reading Depth

- PDF pp.439–528 (89 pages) fully read by section: effective interactions and constrained HF/HFB, symmetries and Nilsson–Strutinsky, shape parametrization/consistency, axial/triaxial quadrupole shapes, high-spin stretching/polarization/intruder bands/termination/noncollective rotation/superdeformation, reflection-asymmetric/octupole shapes, shape coexistence, neutron–proton and higher-deformation interactions, relativistic/configuration developments and beyond-mean-field limits.
- Not covered: cited primary data and post-1990 computational developments.

## Key Results

- HF/HFB and Nilsson–Strutinsky are complementary mean-field routes: self-consistent effective interactions treat the full density, whereas the shell-correction approach separates liquid-drop and shell energies and uses a variational potential deformation. Shape inconsistency in the latter is usually a few percent but can matter when converting mass to charge moments (PDF pp.442–454, Eqs.8–14).
- The quadrupole surface uses `β2,γ`; prolate and oblate limits are `γ=0°` and `60°`, with triaxial sectors and rotation-axis conventions explicitly defined. Higher multipoles are required for realistic large-deformation surfaces (PDF pp.452–456).
- Rotation changes shape through centrifugal stretching, decoupled-particle polarization, intruder configurations, band termination, noncollective rotation and superdeformation. Alignment and shape evolution must be solved self-consistently in the rotating frame (PDF pp.457–488, Sec.5).
- Reflection-asymmetric shapes are treated with octupole degrees of freedom. Octupole correlations, parity doublets, E1/E3 moments and exotic higher-order shapes are related, but a static octupole minimum is not implied by a single parity splitting or relative transition strength (PDF pp.488–502, Sec.6).
- Shape coexistence is reviewed for prolate/oblate competition, spherical–deformed isomers and pairing isomers; mean-field minima require beyond-mean-field mixing/projection to connect intrinsic configurations to laboratory spectra (PDF pp.502–511, Sec.7).
- Neutron–proton interactions, higher multipole deformations, approximate configuration labels and early relativistic mean-field work are identified as important extensions, while the final section lists symmetry restoration, collective fluctuations and configuration mixing as missing beyond-mean-field ingredients (PDF pp.511–527, Secs.8–10).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AFN90-1 | Mean-field potential minima are intrinsic model outputs; laboratory shape claims require consistency, observables and (when needed) symmetry restoration/mixing. | model-boundary | review | PDF pp.442–454, 518–527 | true |
| AFN90-2 | Rotation can drive stretching, triaxiality, noncollective alignment, band termination and superdeformation. | review-synthesis | review | PDF pp.457–488 | true |
| AFN90-3 | Octupole and shape-coexistence minima have distinct companion observables and competing dynamic interpretations. | interpretation-boundary | review | PDF pp.488–511 | true |
| AFN90-4 | `β2/γ` parametrization and rotation-axis sector are convention-dependent; higher multipoles and self-consistency matter for large deformations. | formalism-boundary | direct | PDF pp.452–456 | false |

## Summary

Åberg, Flocard and Nazarewicz provide a foundational map from effective interactions to rotating nuclear shapes. The durable Wiki lesson is to keep intrinsic mean-field minima, laboratory spectra, symmetry restoration and collective fluctuations as separate evidence layers; high-spin alignment, octupole, superdeformation and coexistence labels cannot be read directly from a single calculated `β,γ` point.

## Competing Interpretations and Limitations

- Nilsson–Strutinsky, HF/HFB and early relativistic mean-field results can agree qualitatively while differing in parameterization, pairing, self-consistency and zero-point corrections.
- High-spin shape changes may arise from centrifugal stretching, quasiparticle polarization, band crossing, termination or shape coexistence; alignment alone does not uniquely identify a triaxial or superdeformed minimum.
- Octupole observables can reflect static deformation, soft vibrations or reflection-asymmetric correlations. E1/E3 and parity-doublet information must be combined with lifetimes and model sensitivity.
- Mean-field minima break rotational/parity symmetries; projection and configuration mixing are required before assigning a unique laboratory band identity.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AFN90-AR-1 | Shape chain | Effective interaction → constrained HF/HFB or shell-correction energy surface → intrinsic `β,γ,β3` minimum → rotating-frame observables. | PDF Secs.2–5 | self-checking |
| AFN90-AR-2 | High-spin chain | Cranking/rotation → quasiparticle alignment and shape polarization → band crossing/termination/superdeformation; configuration and pairing are explicit inputs. | PDF Sec.5 | self-checking |
| AFN90-AR-3 | Laboratory transfer | Intrinsic octupole/coexistence minimum → projected/mixed states and transition moments; without restoration, retain model-only status. | PDF Secs.6–10 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[rotating-mean-field]], [[triaxial-deformation]], [[octupole-deformation]], [[octupole-softness]], [[triaxial-shape-coexistence]], [[band-termination]] and [[superdeformation]].
- New reusable rule: annotate every shape claim as intrinsic/model, direct observable, or projected/laboratory inference; preserve rotation-axis and parametrization conventions.
- This source is a review and adds no independent experiment; it is a theory backbone for cross-source self-audit and L3 shape questions.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `AFN90-P0-1`: Do not promote mean-field minima or early model examples into direct triaxial/octupole/shape-coexistence evidence without observable and beyond-mean-field boundaries.

## Extracted Pages

- Concepts/models: [[rotating-mean-field]], [[triaxial-deformation]], [[octupole-deformation]], [[octupole-softness]], [[triaxial-shape-coexistence]], [[band-termination]], [[superdeformation]]。
