---
type: source
title: "Craig Mehl 2015 MSc thesis: Developing a sorting code for Coulomb excitation data analysis"
title_original: "Developing a sorting code for Coulomb excitation data analysis"
aliases: [Mehl iThemba S3 sorting thesis, AFRODITE S3 Doppler correction thesis]
created: 2026-10-13
updated: 2026-10-13
status: ai-draft
review_status: unreviewed
source_type: thesis-method
reading_depth: skimmed
authors: [Craig Mehl]
advisor: [J. N. Orce, P. M. Jones, S. Triambak]
journal: "University of the Western Cape MSc thesis"
year: 2015
pages: 145
doi:
arxiv:
language: en
canonical_source: "Craig Mehl, Developing a sorting code for Coulomb excitation data analysis, University of the Western Cape MSc thesis, 2015."
zotero_item_key:
citation_key:
zotero_uri:
library_file:
raw_file: "raw/papers/gpt/day11-reaction-doppler-20261013/mehl-2015-coulomb-sorting-thesis.pdf"
raw_sha256: "1fc595022c6f1e912b8e2378ccdb092f014babc2434ba901d020e942e09c3d5e"
nuclei: [20ne, 194pt]
reactions: ["194Pt(20Ne,20Ne*)194Pt*"]
experiments: [ithembalabs-coulomb-excitation]
models: [gosia, geant4, semiclassical-coulomb-excitation]
observables: [gamma-ray-energy, particle-energy, doppler-shifted-spectrum]
methods: [s3-ring-angle-calibration, particle-gamma-coincidence, doppler-correction, energy-loss-simulation]
tags: [thesis, ithemba-labs, afrodite, s3-detector, coulomb-excitation, doppler-correction, sorting-code]
---

# Mehl 2015：Coulomb-excitation sorting code 与 S3 Doppler correction

## Bibliographic Record

Craig Mehl, *Developing a sorting code for Coulomb excitation data analysis*, University of the Western Cape MSc thesis, 2015, 145 PDF pages. The official repository item is [handle 10566/16610](https://hdl.handle.net/10566/16610), UUID `ca0d0003-0eb8-4797-8a3e-c77dd824f744`. Its ORIGINAL bitstream is `Mehl_c_msc_ns_2015.pdf` (13,330,552 bytes); the locally stored copy at the raw path above has SHA-256 `1fc595022c6f1e912b8e2378ccdb092f014babc2434ba901d020e942e09c3d5e`. The UWC DSpace item also exposes generated extracted text, a license file and a thumbnail, but no separate event data or executable sorting-code package.

## Scope and Reading Depth

- Completed `reading_depth: skimmed`; the reading was targeted to the S3 geometry, the `20Ne+194Pt` setup and the Doppler implementation, not a full audit of the entire thesis.
- Visually checked the S3 schematic (printed p.27, Fig.3.1), the 15-mm placement and Coulomb-excitation angle plots (p.35, Fig.3.8), the `20Ne+194Pt` setup and angle coverage (p.37, Fig.3.11), the Doppler coordinate system and Eqs.(4.9)–(4.13) (pp.54–56, Figs.4.12–4.13), and the ring-radius table (Appendix C, p.128, Table C.1).
- Not covered: full GOSIA parameter review, executable/source repository, event-level spectra, response covariance, all `208Pb+40Ar` results or a full independent reanalysis.

## Summary

Mehl's 2015 thesis develops an iThemba LABS particle–γ sorting code for Coulomb-excitation data. It documents the S3 ring/sector geometry, an experiment-specific 15-mm target placement, ring-angle reconstruction and a GEANT4 elastic-peak route to β. Its 20Ne+194Pt run is a separate acquisition from Mavela's 2019 32S experiment; the shared apparatus makes it a method comparator, not a transfer source for Mavela's velocity or data.

## Paper Question and Scientific Motivation

The thesis develops a particle–γ sorting code for iThemba LABS Coulomb-excitation measurements using the AFRODITE HPGe clover array and an S3 double-sided silicon detector. Its relevant contribution here is a source-specific account of S3 geometry, ring-angle mapping, elastic-peak GEANT4 velocity estimates and Doppler correction.

## Key Evidence and Reasoning Chain

| issue_id | priority | source_and_locator | core_claim | claim_kind | evidence_level | locator | conflict_or_gap | competing_explanations | l3_l4_route | research_status | stage_conclusion | knowledge_increment | remaining_uncertainty | next_autonomous_route | needs_review |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ME15-1 | P1 | Printed pp.37–38, Sec.3.8, Fig.3.11 | Mehl reports separate 2013 `20Ne+194Pt` Coulomb-excitation runs at 73 MeV (backward) and 96 MeV (forward); the 73-MeV run used a 1.2 mg/cm² target, AFRODITE with nine clovers (six at 90°, three at 135°) and an S3 detector in the target chamber. Reported backward coverage is 113.4°–141.5°; the 96-MeV forward run reports 38.5°–66.5°. | experimental-fact | direct | Printed pp.37–38, Secs.3.8.1–3.8.2, Fig.3.11 | These are Mehl's 2013 `20Ne` runs, not Mavela's 2019 `32S` dataset. | The same target, AFRODITE and S3 family make the setup methodologically comparable; acquisition identity is not implied. | Use only as an apparatus/method comparator; do not transfer its β or event data to Mavela. | completed | A separate acquisition documents a comparable iThemba S3/AFRODITE geometry. | apparatus-method cross-check | The exact Mavela installation and data-processing provenance must come from Mavela's own code/setup. | Compare only explicit geometry and correction conventions, retaining isotope/run boundaries. | true |
| ME15-2 | P1 | Printed p.27, Fig.3.1; Appendix C, p.128, Table C.1 | The S3 detector has 24 rings and 32 sectors, active diameters 22 and 70 mm, ring width 0.886 mm and sector width 11.25°; Table C.1 lists each ring's inner and outer radii, from ring 1 (11.48–12.366 mm) to ring 24 (34.158–35.044 mm). | experimental-method | direct | Printed p.27, Fig.3.1; printed p.128, Table C.1 | The dimensions do not alone determine scattering angles; target distance and detector orientation are also needed. | Ring/sector segmentation supplies position bins; finite widths imply angular intervals rather than exact rays. | Use the published ring radii with the actual installation distance and alignment to reconstruct angles. | completed | S3 geometry is explicit and independently agrees with the detector dimensions in Mavela 2019. | method parameter | The angular response and ring-centroid convention are setup-specific. | Preserve distance, ring boundaries and alignment in a reusable geometry record. | true |
| ME15-3 | P1 | Printed p.35, Fig.3.8; printed pp.37–38, Fig.3.11 | The S3 plane is reported 15 mm from the target for forward and backward operation; the 73-MeV backward `20Ne+194Pt` setup reports angles 113.4°–141.5°. | experimental-method | direct | Printed p.35, Fig.3.8; printed pp.37–38, Fig.3.11 | This distance is specific to the Mehl measurement; do not substitute it for Mavela's separately listed `d_target2s3`. | The target chamber can support multiple S3 placements; Mehl reports its own chosen geometry. | Compare with Mavela's Appendix C code and retain the two distances as separate run metadata. | completed | Demonstrates a 15-mm S3 placement in the same facility; Mavela later lists −1.30 in its code, likely −13 mm under its cm convention. | independent method comparator | Whether the chamber/adapter geometry is identical between runs is not established. | Use each thesis's own position and ring mapping. | true |
| ME15-4 | P1 | Printed pp.54–56, Eq.(4.9), Eqs.(4.10)–(4.13), Figs.4.12–4.13 | Mehl uses the relativistic Doppler transform `Eγ,k=Eγ(1−β cosθp−γ)/sqrt(1−β²)` with `β≈0.08c` for the `20Ne` measurement; the text says β was obtained from GEANT4 simulations of elastic peaks. Clover directions use measured detector geometry and 196-mm target-to-clover distance; S3 ring θ values are built from target distance and the ring's inner/outer radii, then Doppler correction is applied after particle–γ/ring-sector gates. | experimental-method | direct | Printed pp.54–56, Eq.(4.9), Eqs.(4.10)–(4.13), Figs.4.12–4.13 | The stated β is for Mehl's `20Ne` runs and no event-level β covariance or centroid residual table is reported in these passages. | GEANT4 elastic-peak simulation is an analysis-derived velocity estimate, not an independent measurement of Mavela's scattered `32S` velocity. | Use as a method comparator; do not transfer the scalar `0.08c` to a different beam/angle setup. | completed | Confirms the ring-geometry correction chain and a GEANT4-based β route in a separate run. | method cross-check | Input uncertainties, stopping and event-by-event response are not available here. | Seek actual per-run sorter/calibration files before quantitative transfer. | true |
| ME15-5 | P1 | Appendix C, printed p.128, Table C.1; printed pp.54–56, Eqs.(4.11)–(4.13) | Applying the thesis's face-on nominal geometry with its reported 15-mm distance to the published radii gives backward edge angles `180°−atan(35.044/15)=113.2°` and `180°−atan(11.48/15)=142.6°`, close to the reported 113.4°–141.5° acceptance. This is a task-derived geometry cross-check, not a transfer to Mavela. | our-inference | indirect | Task calculation from Table C.1 and Eqs.(4.11)–(4.13); compared with Sec.3.8.1 angle coverage | The 0.2°/1.1° edge differences may reflect ring-center/ring-edge convention, alignment or rounded coverage. | A face-on centered geometry is a check assumption; detailed alignment can shift boundaries. | Use exact per-ring table and surveyed setup in any reanalysis. | completed | The simple geometric conversion is consistent with the reported range to about a degree. | method consistency check | Alignment, finite solid angle and angular response remain unmodeled. | Do not infer exact angle efficiency from active radii alone. | true |

## Key Results

- **ME15-1 / ME15-3:** The thesis reports 20Ne+194Pt Coulomb-excitation runs at 73 MeV backward and 96 MeV forward; for the 73-MeV setup the S3 detector was 15 mm from the target and the reported backward angle span was 113.4°–141.5° (printed pp.35, 37–38; Figs.3.8, 3.11).
- **ME15-2 / ME15-5:** S3 has 24 rings/32 sectors, active diameters 22/70 mm, 886-μm rings, 11.25° sectors, and a ring-radius table in Appendix C (printed p.27, Fig.3.1; p.128, Table C.1).
- **ME15-4:** The Doppler equation is printed as Eq.(4.9); the thesis states projectile β≈0.08c from GEANT4 elastic-peak simulations and calculates S3 ring θ from the target distance and ring inner/outer radii (printed pp.54–56, Eqs.(4.9)–(4.13), Figs.4.12–4.13).

## Source Independence and Limitations

Mehl's source is a distinct `20Ne+194Pt` acquisition from Mavela's 2019 `32S+194Pt` study. It uses the same iThemba LABS, AFRODITE array, target isotope and S3 detector family, so it is a useful apparatus/method comparator but not independent evidence for Mavela's beam velocity, yields or quadrupole moment. The 15-mm distance and `β≈0.08c` belong only to the Mehl run.

## Competing Interpretations and Limitations

- The reported 15-mm distance, angle coverage and β≈0.08c apply to Mehl's own 20Ne+194Pt runs. They do not establish the distance or velocity for Mavela's 2019 32S+194Pt acquisition, even though the facility and detector family are shared.
- GEANT4 elastic-peak simulations provide an analysis-derived velocity input; these passages do not report event-level β covariance, centroid residuals or a raw event package.
- The thesis explains the ring-angle geometry, but exact angular acceptance still depends on the surveyed plane position/alignment and ring boundaries. Its UWC item exposes the thesis PDF and derivatives, not a separate executable or event dataset.
- The source page remains `unreviewed`; all claims retain `needs_review: true`.

## Knowledge Impact and Learning Decision

- This source **extends** the S3/Doppler method boundary with a separate iThemba example: β was obtained from GEANT4 elastic peaks, and S3 ring angles were calculated from actual target distance and ring radii.
- Persistence is method-page/source-page only; it does not add a `32S` level, `Q_S` value or Mavela event-level observable.
- Page review remains `unreviewed`; all claims retain `needs_review: true`.

## Related Knowledge

- [[doppler-correction]] — ring-specific direction reconstruction and event correction.
- [[mavela-2019-32s-quadrupole-moment-doppler-correction-thesis]] — a separate `32S+194Pt` experiment using the same facility/detector family but its own 1.30-cm code input and ring β array.

## Extracted Pages

- Printed pp.26–27: S3 detector segmentation and geometry.
- Printed p.35 and pp.37–38: S3 distance and `20Ne+194Pt` forward/backward coverage.
- Printed pp.54–56: Doppler equation, coordinate definition and ring/sector angles.
- Appendix C, printed p.128: S3 ring radii.

## Human Review Triage

- P1: confirm no geometry or velocity value is transferred from the `20Ne` run to Mavela's `32S` run; all source comparisons remain method-only.
