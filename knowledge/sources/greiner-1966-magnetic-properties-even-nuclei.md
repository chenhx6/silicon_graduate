---
type: source
title: "Greiner 1966 - Magnetic Properties of Even Nuclei"
aliases: [Greiner 1966 magnetic properties, proton-neutron deformation g tensor]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: theory-paper
reading_depth: deep-read
title_original: "Magnetic Properties of Even Nuclei"
authors: [Walter Greiner]
journal: "Nuclear Physics"
year: 1966
volume: 80
pages: "417-433"
pii: "0029-5582(66)90100-3"
canonical_source: "Greiner, Nuclear Physics 80, 417-433 (1966)"
library_file: "raw/papers/gpt/high-spin-20260920/振动/1966_Greiner_Magnetic properties of even nuclei.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/振动/1966_Greiner_Magnetic properties of even nuclei.pdf"
raw_sha256: "3e7aecb21de5329e02419861eed21d3526bc8efbc51c3c9cc432e974d0cdf83f"
nuclei: [even-nuclei, rare-earth-nuclei]
reactions: []
experiments: []
models: [rotation-vibration-model, pairing, collective-model]
observables: [rotational-g-factor, magnetic-dipole-transition, M1-E2-mixing-ratio]
methods: [rotation-vibration-model, collective-magnetic-moment]
tags: [magnetic-properties, g-factor, M1, E2, pairing, even-nuclei, historical-theory]
---

# Magnetic Properties of Even Nuclei

## Bibliographic Record

- Walter Greiner, *Nuclear Physics* **80**, 417–433 (1966), PII `0029-5582(66)90100-3`。
- 规范文件：`raw/papers/gpt/high-spin-20260920/振动/1966_Greiner_Magnetic properties of even nuclei.pdf`。
- 17-page selectable/OCR-assisted historical theory paper; section headings, equations, Figs.1–6 and Table 1 checked.

## Scope and Reading Depth

- PDF pp.417–433 fully read: proton/neutron deformation model, tensorial magnetic moment Eqs.(1–17), rotation-vibration states and M1/E2 mixing Eqs.(18–35), rotational-band gR factors Eqs.(36–39), vibrational nuclei Eqs.(40–51), comparison with experimental gR/mixing data Figs.2–6 and Table 1, discussion and limitations.
- Not covered: the private/older experimental datasets cited in Figs.2–6 and modern microscopic pairing calculations.

## Paper Question and Model Logic

The paper asks why rotational `gR` factors in even nuclei are often below `Z/A`, and whether the same proton–neutron pairing/deformation difference can generate magnetic dipole transitions and M1–E2 mixing between collective β/γ and ground bands.

1. Assume proton pairing is stronger than neutron pairing (`Gp>Gn`), giving an average proton deformation smaller than the mass/neutron deformation.
2. Express the magnetic moment as a tensor coupled to angular momentum and quadrupole collective variables, rather than a scalar `gR`; derive the tensor coefficients from the difference parameter `f` (Eqs.9–17).
3. Insert the tensor operator into the rotation-vibration basis and derive g factors, M1 probabilities and M1/E2 mixing ratios for deformed and vibrational nuclei (Eqs.18–51).
4. Compare with historical gR and mixing-ratio data; assess qualitative/semi-quantitative agreement and the failure near magic nuclei or where data are uncertain.

## Key Evidence and Reasoning Chain

- For equal proton/neutron deformation (`f=0`), the theory recovers `gR=Z/A`; smaller average proton deformation lowers `gR` and makes the off-diagonal tensor component nonzero, enabling collective M1 transitions.
- Ground and β-band gR factors are predicted as approximately `(Z/A)(1−2f)`; γ-band gR has a small spin dependence (Eqs.37–39). Vibrational nuclei receive a different correction and can have g factors larger than deformed nuclei (Eq.51).
- The model predicts M1/E2 mixing ratios tied to the same `f` that controls gR; Figs.3–6 show broad trends and order-of-magnitude agreement with historical data, but experimental uncertainties span factors of 2–10.
- The paper flags its core approximation: proton and mass vibrational amplitudes are taken equal, rotation-vibration mixing is perturbative, and the collective model is less reliable near magic nuclei.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GR66-1 | Proton–neutron pairing-force differences imply a smaller average proton deformation and lower rotational `gR` than `Z/A`. | model-result | direct | PDF pp.418–421, Eqs.1–17 | true |
| GR66-2 | The collective magnetic moment is a tensor; its off-diagonal component permits M1 transitions between collective bands. | model-framework | direct | PDF pp.420–423, Eqs.10–17 | false |
| GR66-3 | Ground/β/γ rotational-band gR factors and M1/E2 mixing ratios can be expressed using the same deformation-difference parameter `f`. | model-result | direct | PDF pp.422–427, Eqs.25–39 | true |
| GR66-4 | The model reproduces historical gR and mixing-ratio trends semi-quantitatively, but experimental uncertainties and magic-nucleus limits are substantial. | model-data-comparison | mixed | PDF pp.429–433, Figs.2–6, Table 1 | true |

## Summary

Greiner's historical collective model connects lowered rotational g factors and collective M1/E2 mixing to proton–neutron deformation differences induced by unequal pairing strengths. It is a useful conceptual bridge, not a modern microscopic or nucleus-specific proof of shape polarization.

## Competing Interpretations and Limitations

The proton-deformation difference is an average model assumption; single-particle orbitals can reverse it. Equal proton/mass vibrational amplitudes, perturbative band mixing, approximate pairing strengths and uncertain 1960s data limit quantitative transfer. Modern shell-model/QRPA/DFT calculations may redistribute M1 strength and cannot be replaced by the scalar `f` parameter.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| GR66-AR-1 | Equation chain | Pairing difference → proton/mass deformation difference `f` → g tensor → gR/M1/E2 mixing. | PDF pp.418–427 | self-checking |
| GR66-AR-2 | Transfer condition | Use as historical mechanism and convention bridge; fit `f` only with matched nucleus/model and modern uncertainty control. | PDF pp.429–433 | provisional |
| GR66-AR-3 | Failure condition | Magic nuclei, large band mixing, unequal vibrational amplitudes or orbital-specific proton/neutron shapes violate the simplified picture. | PDF pp.419–420, 432–433 | active-L3 |
| GR66-AR-4 | Independence | Theory source; plotted data are historical secondary comparisons, not new experiments. | Figs.2–6/Table 1 | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` and historical-bridge for [[multipole-mixing-ratio]], [[magnetic-rotation]] and g-factor interpretation; `limits` scalar `gR=Z/A` assumptions.
- Persistence: update the magnetic-transition/mixing-ratio method map and high-spin evidence map as a historical model layer.
- Review state: Codex self-audited; not `human-reviewed`.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[multipole-mixing-ratio]] | M1/E2 mixing ratios tied to a deformation-sensitive magnetic tensor. |
| methodological-bridge | [[angular-momentum-alignment]] | Collective angular momentum and proton/neutron response are separated. |
| supports | [[magnetic-rotation]] | Historical M1 mechanism context; not a magnetic-rotation experiment. |

## Human Review Triage

### P0

- `GR66-P0-1`: do not reuse the scalar `f`/gR formulas as modern universal priors; the model is historical and source-specific.

### P1

- `GR66-P1-1`: historical data in Figs.2–6 have large/uncertain errors and lack machine-readable provenance.

## Extracted Pages

- Concepts: [[angular-momentum-alignment]], [[magnetic-rotation]]。
- Observables: [[multipole-mixing-ratio]]。
- Models: rotation-vibration model (source-level; no separate page created).

## L3/L4 Follow-up

- L3 question: how much of observed A≈130 M1/E2 mixing and gR suppression is explained by proton–neutron deformation polarization versus configuration mixing and modern microscopic currents? Required comparisons are absolute M1 strengths, g factors and uncertainty-calibrated models.
- No L4 run: no modern machine-readable data/code supplied.
