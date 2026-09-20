---
type: source
title: "Haxel, Jensen & Suess 1949 - On the Magic Numbers in Nuclear Structure"
aliases: [Haxel Jensen Suess 1949 magic numbers]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: historical-theory-letter
reading_depth: deep-read
title_original: "On the Magic Numbers in Nuclear Structure"
authors: [Otto Haxel, J. Hans D. Jensen, Hans E. Suess]
journal: "Physical Review"
year: 1949
volume: 75
pages: "1766"
canonical_source: "Haxel, Jensen & Suess, Phys. Rev. 75, 1766 (1949)"
library_file: "raw/papers/gpt/high-spin-20260920/review/1949_Haxel et al_On the Magic Numbers in Nuclear Structure.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/review/1949_Haxel et al_On the Magic Numbers in Nuclear Structure.pdf"
raw_sha256: "55626064ffdeaf2ba8c4a836e425bffa269a2050464064015db09de73a3539a2"
nuclei: [shell-structure]
reactions: []
experiments: []
models: [anharmonic-oscillator, spin-orbit-shell-model]
observables: [magic-numbers, single-particle-levels, nuclear-spin]
methods: [historical-shell-model]
tags: [magic-numbers, shell-model, spin-orbit, historical-theory]
---

# On the Magic Numbers in Nuclear Structure

## Bibliographic Record

- O. Haxel, J. H. D. Jensen and H. E. Suess, *Physical Review* **75**, 1766 (1949).
- 规范文件：`raw/papers/gpt/high-spin-20260920/review/1949_Haxel et al_On the Magic Numbers in Nuclear Structure.pdf`。
- The one-page scan contains three neighboring letters; only the Haxel–Jensen–Suess letter is in scope. It occupies the central portion and includes Table I.

## Scope and Reading Depth

- Haxel letter read end-to-end: oscillator quantum-number grouping, anharmonic `l` splitting, strong spin-orbit `j=l±1/2` splitting, Table I and closed-shell magic-number argument.
- Not covered: unrelated neutron-reflection and atmospheric-carbon-monoxide letters on the same scan page, or the later three Naturwissenschaften communications.

## Key Results

- An isotropic/anharmonic oscillator organizes single-particle levels by `r=n1+n2+n3`; spin-orbit splitting of high-`l` terms produces shell closures.
- The letter associates magic numbers `2, 8, 20, 28, 50, 82, 126` with marked splitting of the highest-`j` term in each oscillator group and compares predicted `j` assignments with known odd-mass spins/moments.
- The authors prefer an anharmonic oscillator over a simple potential-well sequence because nuclear-force range is not much smaller than the nuclear radius.

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HJS49-1 | Strong spin-orbit splitting of high-`l` oscillator terms generates the traditional magic-number sequence `2,8,20,28,50,82,126`. | model-result | direct | PDF p.1766, Table I and letter text | true |
| HJS49-2 | Anharmonic-oscillator grouping is preferred over a simple potential well because the nuclear-force range is not negligible relative to the radius. | author-interpretation | direct | PDF p.1766 | true |

## Summary

This historical letter is an early concise statement of the spin-orbit shell model explanation of nuclear magic numbers; it is a background anchor, not a modern quantitative shell-evolution calculation.

## Competing Interpretations and Limitations

The argument is schematic and predates realistic Woods–Saxon/EDF, tensor and continuum effects; shell closures away from stability and deformation-dependent gaps require modern calculations. The scan-page identity must not include the neighboring unrelated letters.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| HJS49-AR-1 | Identity | Haxel/Jensen/Suess title and Table I are present; other scan-page letters are excluded. | PDF p.1766 | self-checking |
| HJS49-AR-2 | Model boundary | Magic-number sequence follows schematic oscillator+spin-orbit assumptions; no modern parameter-fit claim. | Table I/letter text | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` historical shell-structure background for [[covariant-density-functional-theory]] and high-spin orbital assignments.
- Persistence: source/index only; no new nucleus page.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `HJS49-P0-1`: preserve scan-page scope and historical schematic status; do not use it as modern shell-gap evidence.

## Extracted Pages

- Models: [[covariant-density-functional-theory]] (historical shell context).
