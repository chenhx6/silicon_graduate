---
type: source
title: "A generalized figure of merit for gamma-ray polarimeters"
aliases: ["Logan 1974 polarimeter merit", "Generalized Compton polarimeter figure of merit"]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: method
reading_depth: deep-read
title_original: "A GENERALIZED FIGURE OF MERIT FOR GAMMA-RAY POLARIMETERS"
authors: ["B. A. Logan", "R. T. Jones", "A. Ljubičić"]
journal: "Nuclear Instruments and Methods"
year: 1974
volume: 117
pages: "273-275"
doi: "10.1016/0029-554X(74)90409-1"
language: en
canonical_source: "Logan, B. A., Jones, R. T. & Ljubičić, A. A generalized figure of merit for gamma-ray polarimeters. Nucl. Instrum. Methods 117, 273-275 (1974)."
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1974_Logan et al_A generalized figure of merit for gamma-ray polarimeters.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1974_Logan et al_A generalized figure of merit for gamma-ray polarimeters.pdf"
raw_sha256: "1b3e1ad53b79b5128dee32cf63224b7b6f5f6a3d6bc50408814aec681421f364"
nuclei: []
models: []
observables: ["polarimeter-sensitivity", "coincidence-efficiency", "peak-to-background", "figure-of-merit", "linear-polarization"]
methods: ["compton-polarimetry", "linear-polarization-asymmetry", "detector-response-simulation"]
tags: [figure-of-merit, Compton-polarimeter, background, efficiency, detector-comparison]
---

# A generalized figure of merit for gamma-ray polarimeters

## Bibliographic Record

- 作者：B. A. Logan, R. T. Jones, A. Ljubičić。
- 期刊：*Nuclear Instruments and Methods* 117, 273-275 (1974)。DOI：`10.1016/0029-554X(74)90409-1`。
- 原始文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1974_Logan et al_A generalized figure of merit for gamma-ray polarimeters.pdf`；SHA-256：`1b3e1ad53b79b5128dee32cf63224b7b6f5f6a3d6bc50408814aec681421f364`。

## Scope and Reading Depth

- Completed reading_depth: `deep-read`。
- Covered scope: PDF pp.273-275 全文；background-inclusive counting statistics、generalized merit Eq.(3)、conventional/planar polarimeter comparison、Table 1/2、Figs.1-2 和结论已阅读。
- Not covered: 原始 detector data、引用 polarimeter calibration papers and later response simulations。
- Coverage caveats: merit depends on photon polarization `P`, sensitivity `Q`, efficiency and two orientation-specific signal/background ratios; it is not a single universal detector number.

## Paper Question and Scientific Motivation

- 论文把“达到给定 asymmetry statistical accuracy 所需时间”转成可比较的 polarimeter figure of merit，并把 full-energy peak background 纳入公式（摘要；PDF pp.273-274）。
- 目标是比较 conventional multi-crystal Compton polarimeter 与 planar Ge(Li) polarimeter，避免只用 Q 或效率单独评价。

## Method and Design Logic

- Asymmetry `A=QP` is measured from two orientations; signal counts include background `B1/B2`, with signal-to-background ratios `S1/S2` and efficiency `ε`。
- Generalized merit `M` depends on `Q`, `P`, `ε`, asymmetry correction and `S1/S2`; in the high-background-free limit it reduces to the familiar efficiency-times-sensitivity squared form, while finite backgrounds strongly penalize low-S systems (PDF pp.273-274，Eq.(3))。
- Table 1 uses 977-keV `56Co` examples: conventional Q≈0.40, ε≈16, S1/S2≈13; planar Q≈0.08, ε≈10, S1/S2≈0.2. Table 2 shows the merit changes with photon P and normalizes conventional full-polarization merit to 1.

## Key Evidence and Reasoning Chain

1. Statistical accuracy depends on both asymmetry magnitude and count/background variance; increasing M decreases required measurement time for the same accuracy (PDF p.273，Eq.(2)-(3)).
2. Background-free comparisons can hide the severe penalty of planar polarimeters with low peak-to-background; the 977-keV example gives planar merit only about `0.0048-0.0049` relative to conventional across P=0.1-1 (PDF p.274，Table 2).
3. The conventional polarimeter remains superior in the analyzed energy range; larger planar detectors can improve merit but are still expected below conventional multi-crystal systems (PDF pp.274-275，Figs.1-2).

## Summary

Logan et al. provide a background-inclusive figure of merit for gamma polarimeters. The method separates sensitivity Q, efficiency ε, photon polarization P and orientation-dependent signal/background. It explains why a detector with acceptable efficiency but poor Q or peak-to-background can be statistically inefficient, and why polarimeter comparisons must state the source spectrum and background conditions.

## Experimental or Theoretical Setup

- Comparison: conventional two/three-Ge(Li) Compton polarimeter versus planar Ge(Li) system。
- Reference: 977-keV `56Co` photons; Table 1 uses measured Q, efficiency and S values from earlier detector comparisons。
- Statistics: two orientations, asymmetry variance and confidence factor `x`.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| L74-1 | Generalized merit includes Q, ε, P and orientation-specific signal/background ratios; it reduces required measurement time when increased. | method-definition | direct | PDF pp.273-274，Eq.(2)-(3) | false |
| L74-2 | At 977 keV, conventional Q≈0.40 and planar Q≈0.08; planar merit is only about 0.0048-0.0049 of the conventional reference in Table 2. | detector-comparison | direct | PDF p.274，Tables 1-2 | false |
| L74-3 | Polarimeter merit depends on photon polarization and background, so no single detector ranking is universal without source conditions. | method-limitation | direct | PDF pp.273-275 | false |

## Nuclear Structure Information

- 不适用；来源是 detector-statistics method paper。

## Authors' Interpretation

- Optimizing Q alone is insufficient; peak-to-background and efficiency determine practical time-to-precision。

## Model Results

- 不适用；statistical counting model only。

## Competing Interpretations and Limitations

- Table 1 values are from a specific 977-keV source/detector comparison; they cannot be transferred to modern clover/tracking/CdTe arrays。
- The merit formula assumes the specified asymmetry/counting arrangement; event-selection correlations and detector-response details must be included in a later analysis。

## Analytical Reconstruction

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| AR-L74-1 | Core reconstruction | This source formalizes a decision metric for rare polarization measurements, not a universal detector score. | PDF pp.273-275 | self-checking |
| AR-L74-2 | Assumptions and dependencies | Depends on P, Q, ε, background, confidence target and two-orientation count rates. | PDF pp.273-274 | self-checking |
| AR-L74-3 | Transfer conditions | Formula transfers; numerical Q/ε/S values do not. | PDF Tables 1-2 | provisional |
| AR-L74-4 | Failure conditions | Ignoring peak-to-background or using the wrong P branch can reverse detector ranking. | PDF pp.273-275 | active-L3 |
| AR-L74-5 | Reverse/falsification test | Recompute M for the actual array, source P, event cuts and backgrounds; compare with a matched reference configuration. | PDF Eq.(3) | candidate-L3 |
| AR-L74-6 | Research-question decision | Add as P/A/Q/efficiency project method bridge; no L4. | PDF pp.273-275 | completed |

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: Wiki tracks P/A/Q/efficiency separately but had not yet formalized background-inclusive merit as a detector-comparison condition.
- Effect of this source: `supports` and `methodological-bridge`。
- Reason: It supplies a statistical reason to keep Q, ε and peak-to-background separate when planning a rare polarization measurement.
- Persistence decision: update [[compton-polarimetry]] and [[gamma-ray-linear-polarization-in-nuclear-spectroscopy]] source set。
- Review state: `unreviewed`; method claims self-audited by Codex, not human-reviewed。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[compton-polarimetry]] | Background-inclusive merit and detector comparison。 |
| supports | [[gamma-ray-linear-polarization-in-nuclear-spectroscopy]] | Connects Q/P/A to efficiency and peak-to-background trade-offs。 |

## Human Review Triage

### P0

- L74-P0-1：M is condition-dependent; Table 1/2 detector ranking cannot be transferred to another array or source without recalculation。

### P1

- L74-P1-1：For a future user dataset, include P, Q, ε, background and confidence target in the manifest rather than optimizing Q alone。

### P2/P3

- DOI, volume and pages are aligned from the PDF PII; no nucleus page created。

## Extracted Pages

- Nuclei: none。
- Bands: none。
- Concepts: detector merit, background, sensitivity/efficiency trade-off。
- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]]。

## Non-source Notes and Follow-up

- Next: compare L74 merit with Simpson S83 and Garcia-Raffi GR95 response curves; continue HS-014.
