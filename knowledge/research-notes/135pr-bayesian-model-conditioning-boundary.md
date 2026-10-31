---
type: research-note
title: "`135Pr` Bayesian inertia模型与共同响应证据的条件边界"
aliases: [135Pr Bayesian model conditioning boundary, 135Pr model-conditioned wobbling inference]
created: 2026-10-31
updated: 2026-10-31
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [chen-2026-bayesian-inertia-wobbling-135pr, matta-2015-transverse-wobbling-135pr, lv-2022-evidence-against-wobbling-135pr, sensharma-2026-evolution-chirality-transverse-wobbling-135pr]
created_from: "Day31 post-Day28 prospectus and full-library review"
promotion_target: "post-30-day-nuclear-structure-paper-prospectus"
scope: 135pr/wobbling/bayesian-inference/model-conditioning
nuclei: [135pr]
observables: [wobbling-energy, mixing-ratio, polarization, b-e2, b-m1, moments-of-inertia]
tags: [135pr, bayesian, model-conditioning, response-boundary, paper-prospectus]
---

# `135Pr` Bayesian inertia模型与共同响应证据的条件边界

## Research Trigger

`135Pr` 现有争议同时包含实验 response/branch 冲突和新近的 Bayesian inertia 模型。若不把两层分开，容易把 within-model posterior stability 写成实验机制裁决。本页定义一个论文安全边界：Bayesian 模型可以约束什么，不能替代 Matta–Lv–Sensharma 的共同 response、协方差和 holdout。

## Grounded Evidence

| Evidence | locator | What it supports | What remains missing |
|---|---|---|---|
| Chen 2026 accepted record names CQPC and Metropolis–Hastings MCMC | [[chen-2026-bayesian-inertia-wobbling-135pr]] `CH26-B1` | model-conditioned Bayesian inertia inference | full manuscript likelihood, priors, sampler diagnostics and posterior samples |
| Chen abstract states energy-only constraints and fixed EM inputs | same source `CH26-B2`, `CH26-B4` | energies can condition inertia posterior and propagate conditional EM predictions | fixed-input values/provenance, their uncertainty and independent holdout |
| Chen reports `J_m > J_s > J_l` and transition stability over energy-compatible region | same source `CH26-B3`, `CH26-B7` | within-model robustness claim | model comparison, alternative mechanism evidence and raw experimental response |
| Matta reports large-`|δ|`/E2-rich branch | [[matta-2015-transverse-wobbling-135pr]] `M15-D22-R095-1` | support-chain branch input | detector response/Q/raw/Cov compatibility with other campaigns |
| Lv reports independent small-`|δ|` `P-R_ac` branch | [[lv-2022-evidence-against-wobbling-135pr]] `L22-D22-R095-1` | counter-chain branch input | joint likelihood across response, gates, polarization and covariance |
| Sensharma gives fixed-condition χ² preference | [[sensharma-2026-evolution-chirality-transverse-wobbling-135pr]] `SH26-D22-R095-1` | conditional reanalysis result | complete event/run ledger, nuisance profile and code |

## Provisional Reasoning

The Bayesian posterior has the conditional form

$$
p(\theta\mid D_E,M,A,F),
$$

where `D_E` are selected energies, `M` the model, `A` state assignments and `F` fixed EM/structural inputs. A narrow posterior or stable prediction inside this conditioning does not establish:

- that the chosen band/state assignments are unique;
- that Matta and Lv use the same detector response or feeding model;
- that fixed EM inputs are independent of the data used to choose the model;
- that a competing signature-partner, TiP or configuration-mixing model has lower evidence;
- that the experiment's large/small `δ` branch has been resolved.

The safe integration is therefore a two-layer analysis:

1. **Experimental layer:** freeze transition identity, response, gates, polarization/ADO conventions, background and joint covariance; profile the branch ambiguity.
2. **Model layer:** condition the Bayesian inertia model on an explicitly declared energy data vector and fixed-input provenance; propagate only conditional EM predictions.

The model layer becomes a useful holdout only when its prediction is tested against an observable not used to select `M`, `A` or `F`.

## Assumptions

The accepted record is metadata/abstract-level evidence only; no manuscript equation, numerical table, SI, code or posterior sample is treated as read. Model parameters, fitted inertias and predicted EM bands remain model outputs. Experimental branches from Matta, Lv and Sensharma are not pooled without a common response contract.

## Competing Explanations

Energy-compatible inertia regions can support wobbling-like predictions while the same spectra may be described by tilted precession, signature-partner or configuration-mixing models. A fixed EM input can make a prediction appear stable because its uncertainty is conditioned away. Conversely, a branch conflict may arise from response/gate differences rather than new nuclear structure.

## Transfer Conditions

This boundary transfers to other Bayesian nuclear-structure analyses only when the fitted data vector, model assignments, fixed inputs, priors, nuisance parameters and holdout observable are explicitly declared. It does not transfer numerical inertia orderings or posterior widths across nuclei.

## Failure Conditions

Stop the model comparison if the manuscript likelihood/priors are unavailable, the state assignment is unresolved, the fixed EM inputs were selected from the same observable used as a holdout, or the competing model has no matched data contract. Under these conditions report a conditional model-readiness boundary, not a Bayesian mechanism ranking.

## Falsification or Reverse Tests

A useful future test is a matched-input leave-EM-out prediction: fit each declared model to the same public energy vector, then predict one preselected interband E2 fraction or absolute-strength observable with common nuisance treatment. If the profiled prediction sets remain overlapping, the model cannot resolve the branch. If they are disjoint under a documented response/covariance contract, the result can rank model-conditioned explanations while still remaining conditional on the chosen state identity.

## Open Questions

- What exact energy likelihood, priors, fixed EM inputs and sampler diagnostics does Chen 2026 use?
- Are the predicted EM observables held out from model/parameter selection?
- Can Matta/Lv/Sensharma public inputs be harmonized into a common response and covariance contract?
- Which partner-resolved lifetime or absolute `B(E2)/B(M1)` observable is the least model-dependent holdout?

## Human Review

This is a Codex self-audit, `review_status: unreviewed` and `reasoning_status: provisional`. The note does not reproduce Chen's posterior or claim an experimental wobbling verdict.

## Knowledge Impact and Learning Decision

`supports`: the 2026 Bayesian source is useful as a model-conditioned layer in the `135Pr` paper queue.

`limits`: it cannot replace the missing common response, covariance, branch profile or independent holdout; current P1 remains a prospectus/evidence-contract candidate rather than a completed common reanalysis.

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-10-31 | post-Day28 Bayesian model-conditioning review | none | provisional | accepted abstract confirms conditional CQPC/MCMC layer; full inference contract and experimental holdout remain unavailable | [[post-30-day-nuclear-structure-paper-prospectus]] |
