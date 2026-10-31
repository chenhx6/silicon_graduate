---
type: research-note
title: "30天后核结构论文的图表与数据合同"
aliases: [post-30-day paper figure plan, nuclear-structure manuscript data contracts]
created: 2026-10-31
updated: 2026-10-31
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [matta-2015-transverse-wobbling-135pr, lv-2022-evidence-against-wobbling-135pr, sensharma-2026-evolution-chirality-transverse-wobbling-135pr, chakraborty-2023-131xe-wobbling-origin, banik-2020-131xe-multiple-band-structures, alwaleedi-2013-band-structures-131ce, li-2004-lifetimes-131ce, ding-2021-131ba-133ce-signature-splitting, lv-2021-tilted-precession-135nd, tonev-2007-134pr-dynamic-chirality, mukhopadhyay-2007-135nd-chiral-vibration-static]
created_from: "Day31 post-Day28 paper prospectus work"
promotion_target: "post-30-day-nuclear-structure-paper-prospectus"
scope: nuclear-structure/paper-design/figure-data-contract
tags: [paper-design, figure-plan, source-lineage, l4-readiness, nuclear-structure]
---

# 30天后核结构论文的图表与数据合同

## Research Trigger

现有 prospectus 已有 P1 `135Pr`、P2 `131Xe` 和 P6 `131Ce/133Ce` 三条候选。下一步需要把“研究问题”变成可执行的 figure/data contract，使后续拿到 raw/response/Cov 后可以直接进入分析，而不是重新发明论文结构。

## Grounded Evidence

| Candidate | Primary evidence anchors | Current boundary |
|---|---|---|
| P1 `135Pr` | `M15-D22-R095-1`; `L22-D22-R095-1`; `SH26-D22-R095-1`; `CH26-B1`–`CH26-B7` | large/small `δ` branches and model-conditioned inertia are not a common response likelihood |
| P2 `131Xe` | `C23-D28-1`–`C23-D28-10`; `BNK20-D28-1`–`BNK20-D28-3`; `131xe-1601-parity-version-boundary` | 2020/2023 identity/parity versions and 882 double root lack primary AD/response/Cov |
| P6 `131Ce/133Ce` | `AW13-9`, `AW13-11`, `AW13-16`–`AW13-22`; `LI04-1`–`LI04-5`; `D21-4`–`D21-9` | current matrix is a decision boundary; target-nucleus `δ`, polarization, partner lifetime and absolute strengths are missing |
| P3 `135Nd/134Pr` | `MU07-*`, `ZH03-*`, `LV19-*`, `TO07-*`; 2025 same-lineage extension | `135Nd` state-level and line-level ledgers are not yet a common absolute-EM matrix; `134Pr` mixed `M1/E2` and feeding covariance remain incomplete |

## Provisional Reasoning

### Paper P1 — `135Pr` common-response evidence audit

| Figure/table | Claim | Required input | Stop rule |
|---|---|---|---|
| Fig.1 source-lineage graph | Matta/Sensharma share Gammasphere lineage; Lv is an independent counter chain | reaction, array, gate and response ledger | if line identity cannot be aligned, do not form a joint likelihood |
| Fig.2 branch map | large/small `δ`, `A/P/R_ac` are not interchangeable observables | angular counts, polarization counts, `a(E)`, `Q(E)`, gates and covariance | preserve non-identifiability if profiled prediction sets overlap |
| Fig.3 nuisance profile | response/feeding/acceptance can reorder branches | joint nuisance model and calibration covariance | no fixed `σ/I` χ² as a universal verdict |
| Fig.4 holdout | partner lifetime or absolute EM strength tests branch/model | independent companion observable | without holdout, paper remains readiness/method paper |

### Paper P2 — `131Xe` identity and branch-boundary paper

| Figure/table | Claim | Required input | Stop rule |
|---|---|---|---|
| Fig.1 immutable state ledger | B5, B1(a), yrast/yrare cannot be merged by band label or near energy | full level/transition/gate ledger and source lineage | retain local identity only |
| Fig.2 794-keV version map | 2020 E1/positive-parity and 2023 negative-parity labels are version-dependent | 1983/1979 primary line data, author revision or new target-line measurement | no final parity claim if primary target-line evidence absent |
| Fig.3 671/882/1055 branch profile | central small `δ` is not global uniqueness | raw angular distributions, response, polarization and joint `Σ` | report both branches/readiness if prediction sets overlap |
| Table 1 derived-strength covariance | `RE` and `RM` share `r` and `δ` | matched intensity/efficiency/energy covariance | never count two derived ratios as independent votes |

### Paper P6 — `131Ce/133Ce` mode identifiability

| Figure/table | Claim | Required input | Stop rule |
|---|---|---|---|
| Fig.1 transition identity ledger | exact endpoints and direction matter more than band labels | AW13 Table 4.1–4.4 rows, gates, state assignments | unresolved endpoint remains provisional |
| Fig.2 observable bundle matrix | signature/configuration, γ-soft, wobbling, chirality and coexistence make different predictions | measured `δ`, polarization, lifetimes, absolute `B(E2)/B(M1)`, `Q_t` | compatibility matrix only if companion observables missing |
| Fig.3 model sensitivity | `S(I)`/PES/γ can be degenerate with Coriolis attenuation | common CSM/QTR parameterization and sensitivity scan | no fitted γ is called a measurement |
| Fig.4 independent holdout | g factor, invariant or HD–ND linking can reorder explanations | one unused structural observable | without holdout, no mode-discovery claim |

### Paper P3 — `135Nd/134Pr` partner-resolved absolute-EM benchmark

| Figure/table | Claim | Required input | Stop rule |
|---|---|---|---|
| Fig.1 identity/lineage ledger | MU07 state-level `τ/B`, ZH03 topology and LV19 D5/D6 lines must remain separate | producer-level parent/final state, `Eγ`, multipolarity, branch and campaign ledger | do not bind MU07 plotted `B` points to `648/896` or any nearby line without producer evidence |
| Fig.2 partner EM matrix | Tonev07 `134Pr` lines can support a line-level control; `135Nd` remains partly state-level | matched lifetime, feeding, `B(E2)/B(M1)`, mixed-transition `δ` and shared covariance | keep `134Pr` and `135Nd` source families separate; no cross-nucleus pooled fit if mappings differ |
| Fig.3 same-lineage extension | Lv 2025 `17/2−_3`, band T and `B(E2,752)/B(E2,908)=2.0(5)` extend the TiP transition ledger | full producer response, event-overlap relation to 2021, absolute lifetime and matrix elements | treat as same-lineage extension, not independent confirmation |
| Fig.4 holdout/falsifier | partner-resolved absolute EM can distinguish static chirality, dynamic mixing and crossing | one unused lifetime/absolute-strength or configuration-sensitive holdout | without producer mapping, covariance and holdout, paper remains an identity/readiness audit |

## Assumptions

Each candidate uses source-lineage first, then observable identity, then response/covariance, then model comparison. Existing published values remain source-attributed; proposed figures do not imply that raw inputs exist or that an analysis has been performed.

## Competing Explanations

The same energy spacing, `B(M1)/B(E2)` trend or model γ can arise from multiple mechanisms. A paper that lacks a preselected falsifier or an independent holdout should be framed as an evidence/readiness audit.

## Transfer Conditions

The figure contracts can transfer to other A≈130 cases only after re-freezing state identity, detector response, feeding, branch convention and source independence. Numerical thresholds, posterior widths and model parameters cannot be copied between nuclei.

## Failure Conditions

If response, covariance, event counts, line identity or a required companion observable is unavailable, do not fill the gap with synthetic data or model output. Keep the paper at L3 and label the missing input explicitly.

## Falsification or Reverse Tests

Before drafting a conclusion, predefine a result state: `supports`, `limits`, `reorders`, `non-identifiable` or `input-blocked`. A candidate model is only excluded when its profiled prediction set is disjoint from the controlled data domain and the comparison includes the relevant nuisance covariance.

## Open Questions

- Which candidate can acquire real raw/response/Cov first?
- Which figure can be generated from already public event-level data rather than requiring a new experiment?
- Does the external literature already contain an equivalent common-response or partial-identification analysis?
- Which journal level matches an evidence-boundary paper without overstating novelty?

## Human Review

This is a Codex self-audit and manuscript-design asset, `review_status: unreviewed` and `reasoning_status: provisional`. It is not a draft submission and does not claim a new experimental result.

## Knowledge Impact and Learning Decision

`supports`: turns the prospectus into executable paper work packages with explicit figure claims and data contracts.

`limits`: all three candidates remain conditional; missing response, covariance and holdout inputs prevent immediate full manuscripts.

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-10-31 | post-Day28 paper-design review | none | provisional | three candidates have source/lineage anchors but distinct missing-input contracts | [[post-30-day-nuclear-structure-paper-prospectus]] |
