---
type: source
title: "Afanasjev et al. 1999 - Termination of rotational bands"
aliases: [Afanasjev 1999 band termination review]
created: 2026-09-21
updated: 2026-09-21
status: ai-draft
review_status: unreviewed
source_type: review
reading_depth: deep-read
title_original: "Termination of rotational bands: disappearance of quantum many-body collectivity"
authors: [A. V. Afanasjev, D. B. Fossan, G. J. Lane, I. Ragnarsson]
journal: "Physics Reports"
year: 1999
volume: 322
pages: "1-124"
pii: "S0370-1573(99)00035-6"
canonical_source: "Afanasjev et al., Phys. Rep. 322, 1-124 (1999)"
library_file: "raw/papers/gpt/high-spin-20260920/review/1999_Afanasjev et al_Termination of rotational bands.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/review/1999_Afanasjev et al_Termination of rotational bands.pdf"
raw_sha256: "dff5cc076849dbdcc503bd0a9921efb12059f76ccba3fec643c84473f7e02009"
nuclei: [20Ne, 48Cr, 80Zr, 102Pd, 109Sb, 158Er]
reactions: [generic-high-spin-spectroscopy]
experiments: [gamma-ray-arrays, high-spin-bands]
models: [cranked-nilsson-strutinsky, rotating-liquid-drop, cranked-HF, shell-model]
observables: [band-termination, alignment, Q_t, B(E2), transition-energy, configuration]
methods: [rotating-frame, configuration-dependent-CNS]
tags: [band-termination, high-spin, CNS, alignment, collectivity]
---

# Termination of rotational bands

## Bibliographic Record

- A. V. Afanasjev *et al.*, *Phys. Rep.* **322**, 1–124 (1999), PII `S0370-1573(99)00035-6`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/review/1999_Afanasjev et al_Termination of rotational bands.pdf`。

## Scope and Reading Depth

- PDF pp.1–124 fully read by sections: cranking/macroscopic–microscopic theory, CNS configurations, observables and termination types, detailed A≈110 smooth termination, other mass regions, alternative methods and summary.
- Not covered: all cited raw data and later post-1999 calculations.

## Key Results

- Band termination is the continuous loss of collective rotation as a fixed configuration reaches its maximum aligned spin; deformation evolves toward an oblate/noncollective aligned state (PDF pp.4–7, Secs.1–2).
- Configuration-dependent cranked Nilsson–Strutinsky (CNS) calculations track routhians, alignments, shape changes and transition quadrupole moments without relying on pairing at high spin. Macroscopic–microscopic, rotating-liquid-drop and shell corrections are kept separate (PDF pp.7–32).
- Experimental termination observables include transition-energy slopes, dynamic/kinematic moments, alignment, decreasing `Q_t/B(E2)`, weak crossover transitions and finite-spin configuration limits; smooth bands around A≈110 (`109Sb` and neighbors) are the principal benchmark (PDF pp.33–95).
- Termination systematics also occur in p/sd shells, A≈45–50, A≈60, A≈80, A≈100 and A≈155–160; alternative shell-model, projected-HFB and mean-field methods are reviewed (PDF pp.95–111).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| AF99-1 | A terminating band is a configuration-specific collective-to-aligned evolution, not simply a band ending because of missing statistics. | concept-result | review | PDF pp.4–7, 33–39 | true |
| AF99-2 | `Q_t/B(E2)`, alignment and transition-energy behavior jointly diagnose smooth termination. | observable-synthesis | review | PDF pp.33–40, 43–95 | true |
| AF99-3 | CNS configuration labels and shape evolution are model-dependent but can be compared systematically with high-spin data. | model-boundary | review | PDF pp.18–32, 54–95 | false |

## Summary

Afanasjev *et al.* establish the theory and experimental evidence map for rotational-band termination. The key distinction is between direct finite-spin/configuration observables and the CNS interpretation of deformation/alignment; a single abrupt energy change or weak E2 line is not sufficient without a fixed-configuration crosswalk.

## Competing Interpretations and Limitations

- Band crossings, configuration mixing, pairing collapse, shape changes and fission can mimic or interrupt termination; a band must be followed over enough spin with a stable configuration assignment.
- CNS neglects pairing at high spin and uses macroscopic–microscopic potentials; other methods may shift energies, alignments and `Q_t`.
- `Q_t/B(E2)` and lifetime-derived strengths depend on feeding, stopping powers and transition placement; direct and model layers remain separate.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AF99-AR-1 | Termination chain | Fixed configuration → cranking/alignment → shape evolution → finite max spin → noncollective endpoint. | PDF Secs.1–4 | self-checking |
| AF99-AR-2 | Evidence chain | Energies/alignment/`Q_t`/B(E2)/crossovers → termination ranking; retain feeding/configuration alternatives. | PDF Secs.4–7 | self-checking |
| AF99-AR-3 | Transfer condition | A≈110 benchmark cannot be copied to A≈130 without CNS configuration and transition-strength mapping. | PDF Secs.5–7 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[band-termination]], [[rotating-mean-field]], [[cranked-shell-model]], [[doppler-shift-attenuation-method]], [[magnetic-rotation]].
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `AF99-P0-1`: Preserve fixed-configuration, observable and CNS-model boundaries before labeling a high-spin sequence terminated.

## Extracted Pages

- Concepts/models: [[band-termination]], [[rotating-mean-field]], [[cranked-shell-model]]。
