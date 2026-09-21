---
type: source
title: "Reed et al. 2016 - Impact of triaxiality on the rotational structure of neutron-rich rhenium isotopes"
aliases: [Reed 2016 neutron-rich Re triaxiality]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Impact of triaxiality on the rotational structure of neutron-rich rhenium isotopes"
authors: [M. W. Reed, G. J. Lane, G. D. Dracoulis, F. G. Kondev, M. P. Carpenter, P. Chowdhury, et al.]
journal: "Physics Letters B"
year: 2016
volume: 752
pages: "311-316"
doi: "10.1016/j.physletb.2015.11.056"
citation_key: Reed_2016
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "https://doi.org/10.1016/j.physletb.2015.11.056"
library_file: "raw/papers/gpt/high-spin-20260920/旋称/2016_Reed et al_Impact of triaxiality on the rotational structure of neutron-rich rhenium.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/旋称/2016_Reed et al_Impact of triaxiality on the rotational structure of neutron-rich rhenium.pdf"
raw_sha256: "5689134f0960028580c4341bc26ae12d78c633cb1f0ee9ba98cc9be28721ea11"
nuclei: [187Re, 189Re, 191Re]
reactions: [deep-inelastic-136Xe-plus-192Os, deep-inelastic-136Xe-plus-187Re, deep-inelastic-136Xe-plus-186W]
experiments: [atlas-gammasphere-rhenium]
models: [triaxial-particle-rotor-model, configuration-constrained-PES, total-routhian-surface]
observables: [signature-splitting, M1-E2-mixing-ratio, gamma-vibrational-band-energy, isomer-lifetime, angular-correlation]
methods: [gamma-gamma-coincidence, angular-correlation, conversion-coefficient]
tags: [rhenium, triaxiality, gamma-softness, signature-splitting, high-spin]
---

# Impact of triaxiality on the rotational structure of neutron-rich rhenium isotopes

## Bibliographic Record

- M. W. Reed *et al.*, *Physics Letters B* **752**, 311–316 (2016), DOI `10.1016/j.physletb.2015.11.056`。
- 规范文件：`raw/papers/gpt/high-spin-20260920/旋称/2016_Reed et al_Impact of triaxiality on the rotational structure of neutron-rich rhenium.pdf`。
- 6-page open-access experiment/model paper; figures, level schemes, angular correlations and model parameters checked.

## Scope and Reading Depth

- PDF pp.311–316 fully read: `187,189,191Re` isomer decay spectroscopy, lifetimes/conversion coefficients, γγ angular correlations, Figs.1–6, particle-triaxial-rotor model, configuration-constrained PES/TRS, conclusions.
- Not covered: raw Gammasphere cubes, full model code and the promised complete level-scheme paper.

## Key Evidence and Reasoning Chain

- Deep-inelastic `136Xe` measurements populate Re isotopes; isomer decays reveal the `9/2−[514]` rotational band, associated γ-vibrational bands and high-K states.
- Three signatures increase with neutron number: `9/2−[514]` signature splitting, decreasing `9/2−[514]⊗2+γ` bandhead energy (586→545→476 keV), and M1/E2 mixing ratios departing from axial-rotor predictions.
- Angular correlations determine M1/E2 mixing (e.g. `δ=0.28^{+0.14}_{−0.12}` for the 140-keV `191Re` transition); lifetimes/isomer assignments and conversion coefficients constrain level spins/parities.
- Particle-rotor calculations reproduce splitting, moments of inertia and mixing with γ≈5°, 18°, 25° for `187,189,191Re`, while configuration-constrained PES/TRS indicate γ softness/rotation-stabilized triaxiality and failure of a purely rigid-triaxial picture.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| RE16-1 | Signature splitting, γ-bandhead energies and M1/E2 mixing ratios jointly increase the inferred triaxiality from `187Re` to `191Re`. | experimental-synthesis | mixed | PDF pp.311–316, Figs.1,5,6 | true |
| RE16-2 | Particle-triaxial-rotor fits use γ≈5°,18°,25° for `187,189,191Re` and reproduce several rotational observables. | model-result | direct | PDF p.315, Fig.6 | true |
| RE16-3 | PES/TRS calculations suggest γ softness and rotational stabilization; a rigid-triaxial interpretation is too simple. | model-result/author-interpretation | mixed | PDF pp.315–316 | true |
| RE16-4 | The `9/2−[514]⊗2+γ` bandhead falls 586→545→476 keV with neutron number. | experimental-result | direct | PDF p.315, discussion | false |

## Summary

Reed *et al.* provide a compact cross-isotope evidence chain for developing triaxiality/γ softness in neutron-rich Re. The strongest lesson is that signature splitting alone is insufficient; γ-vibrational energies and M1/E2 mixing must be combined, and model results retain softness/rotation boundaries.

## Competing Interpretations and Limitations

Configuration mixing, γ softness, rotation-dependent shape and particle polarization can mimic or alter the signature-splitting trend. The particle-rotor model fails for some excited γ-band members; conversion/lifetime and raw-level data are not fully reproducible from the paper alone.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| RE16-AR-1 | Evidence chain | Level schemes/isomers → angular correlations/mixing → signature/γ-band systematics → PTR/PES/TRS comparison. | PDF pp.311–316 | self-checking |
| RE16-AR-2 | Transfer condition | γ values are best-fit PTR inputs, not direct deformation measurements; compare with matching observable set. | PDF p.315 | provisional |
| RE16-AR-3 | Failure condition | Rigid triaxial and γ-soft alternatives, model failure for excited bands and rotation-stabilization ambiguity remain. | PDF pp.315–316 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[signature-partner-bands]], [[triaxial-deformation]] and γ-softness diagnostics; it cautions against a one-observable γ inference.
- Persistence: link to Ding 2021 `131Ba/133Ce` signature map as a cross-mass comparison.
- Review state: Codex self-audited; not `human-reviewed`.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[signature-partner-bands]] | Signature splitting mechanism with low-j mixing and triaxiality. |
| supports | [[triaxial-deformation]] | Combined splitting, γ-vibration and M1/E2 diagnostics. |
| methodological-bridge | [[angular-correlation]] | Mixing-ratio extraction in odd-A rotational bands. |

## Human Review Triage

### P0

- `RE16-P0-1`: inferred γ values are model outputs; signature splitting does not uniquely measure triaxiality.

### P1

- `RE16-P1-1`: γ-soft/PES/TRS alternatives and model failure for excited bands require source-level follow-up before quantitative transfer.

## Extracted Pages

- Nuclei: `187Re`, `189Re`, `191Re` (source-level).
- Concepts: [[signature-partner-bands]], [[triaxial-deformation]]。
- Methods: [[angular-correlation]]。
