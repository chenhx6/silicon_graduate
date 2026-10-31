---
type: research-note
title: "全库主张校准审计：实验事实、模型结果与作者解释的语言边界"
aliases: [full-library claim calibration audit, expert cognition correction ledger]
created: 2026-10-31
updated: 2026-10-31
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [hendrie-1968-hexadecapole-deformation, rohozinski-1988-triaxial-scissors-mode, zagrebaev-2001-superheavy-synthesis-survival, piekarewicz-2004-soft-monopole-mode, karmakar-2025-doublet-wobbling-105pd, matta-2015-transverse-wobbling-135pr, chakraborty-2023-131xe-wobbling-origin, mukhopadhyay-2007-135nd-chiral-vibration-static, bucher-2016-144ba-direct-octupole, alwaleedi-2013-band-structures-131ce]
created_from: "2026-10-31 full-library review and claim-language scan"
scope: knowledge-governance/evidence-calibration/nuclear-structure
tags: [claim-calibration, evidence-level, source-audit, full-library-review]
---

# 全库主张校准审计：实验事实、模型结果与作者解释的语言边界

## Research Trigger

近期 source 页出现 claim table 与正文动词不一致：条目标为 `model-result` 或
`author-interpretation`，正文却使用 proof-like 语言。

## Grounded Evidence

代表性锚点包括 `HEN68-1`–`HEN68-4`、`ROH88-1`–`ROH88-4`、`ZAG01-1`–`ZAG01-4`、
`PIE04-1`–`PIE04-4`、`KAR25-1`–`KAR25-5`，以及 `M15-*`、`C23-*`、`MU07-*`、
`BU16-*` 和 `AW13-*`。

## Audit Trigger

全库复习发现，部分近期 source 页的表格已经把条目标为 `model-result` 或
`author-interpretation`，但正文仍使用“证明、确立、完全排除、彻底失效”等语言。
这会让后续问答或论文草稿把模型计算、作者解释和实验直接报告混成同一层。
本页是自审账本，不修改原 source 的数值、locator 或 review 状态，也不把自审写成
`human-reviewed`。

## Highest-Priority Corrections

| Source page | Existing atomic claims | Safe reading | Language to use after calibration |
|---|---|---|---|
| [[hendrie-1968-hexadecapole-deformation]] | `HEN68-1`–`HEN68-3` are experimental-result; `HEN68-4` is a Nilsson model result | The scattering analysis reports extracted shape parameters; the microscopic mechanism is a model interpretation | “Hendrie et al. report the fitted `β2/β4` systematics; their Nilsson discussion interprets the sign change.” Do not call the single-particle mechanism directly measured |
| [[rohozinski-1988-triaxial-scissors-mode]] | `ROH88-1`–`ROH88-4` are formalism/model results | The degeneracy breaking, splitting formula and strength partition hold inside the stated triaxial two-rotor framework | “The model predicts…” or “within the formalism…” Do not use the paper alone as a measured `γ` or a demonstrated double peak |
| [[zagrebaev-2001-superheavy-synthesis-survival]] | `ZAG01-1`–`ZAG01-4` are model results | Barrier, width ratio and survival probability are calculated outputs conditional on the reaction and statistical/Langevin inputs | “The calculation gives…” and preserve parameter/model dependence; do not present `W_surv` or `Γf/Γn` as direct experimental observables |
| [[piekarewicz-2004-soft-monopole-mode]] | `PIE04-1`–`PIE04-3` are model results; `PIE04-4` is author interpretation | The RRPA predicts a soft response and an inferred sensitivity of `Kτ`; these are not a direct neutron-skin measurement or a universal equation-of-state fact | “The RRPA calculation predicts…” and “the authors argue…”; retain the functional, model-space and sum-rule dependence |
| [[karmakar-2025-doublet-wobbling-105pd]] | `KAR25-1`–`KAR25-3` are experimental-result; `KAR25-4` is model-result; `KAR25-5` is author-interpretation | The paper reports bands and transition observables, then assigns a doublet-wobbling interpretation using TPSM and discusses alternatives | “The experiment reports…” followed by “the authors assign/argue…”; do not convert the TPSM assignment into an independently confirmed mode or claim that all alternatives are excluded |

## Core Prior-Run Corrections

The following five older conclusions have the largest downstream effect on the research
queue. They are not new experimental findings; they are the safe re-read of existing
source pages.

| Topic | Canonical anchors | Safe statement |
|---|---|---|
| `135Pr` wobbling | `M15-3/M15-4/M15-8/M15-10`, `L22-3/L22-4/L22-11`, `SH26-8/SH26-13/SH26-15`; [[135pr-mixing-branch-input-contract]] | Matta's large-`|δ|` chain and Lv's independent small-`|δ|` `P–R_ac` chain remain in conflict; Sensharma's fixed-`σ/I` result is conditional. Public inputs do not uniquely rank wobbling, tilted precession, signature partner or configuration mixing |
| `131Xe` low-spin identity | `BNK20-D28-1/2/3`, `C23-2/3/6/7`; [[131xe-low-spin-partner-crosswalk]] | The 2020/2023 work shares acquisition lineage; the candidate unfavoured signature-partner reading is local to the mapped sequence. The 1600.9-keV version, 794.8-keV electromagnetic character and 881.8-keV branch remain open |
| `135Nd/134Pr` chirality | `MU07-1/2/3/8/10/11`, `TO06-D24-003/005/006`, `TO07-D24-002/003/005/006/007`, `PE06-1/2`; [[partner-em-interval-loso-audit]] | `135Nd` is compatible with an author model of chiral evolution, while `134Pr` is a counterexample to ideal static chirality; neither result alone identifies the geometry or excludes dynamic/configuration-mixing alternatives |
| `144,146Ba` octupole | `BU16-1/2`, `EXT146-1/2/3`, `BE16-D26-004/005/007/008`; [[octupole-and-rare-electromagnetic-decay]] | Direct strong `E3` is a high-value observable, but SCCM occupation and dipole-cancellation decompositions remain model outputs; they do not by themselves establish a rigid static pear shape |
| `131Ce/133Ce` collective modes | `AW13-9/16/19/20/21/22`, `LI04-1`–`LI04-5`, `D21-4`–`D21-7`; [[131ce-133ce-mode-identifiability-boundary]] | Band-specific lifetimes and conditional `δ=0` strength arithmetic constrain the system, while TRS/TPSM `γ` values remain model inputs/results. Current data do not uniquely identify wobbling, chirality, γ-rigidity or shape coexistence |

These corrections should be applied before using historical run summaries in a paper
outline. A numerical result may remain reproducible and still be unsuitable as an
independent evidence vote.

## Applied Calibration in This Run

The proof-like wording was minimally softened in five representative source pages:

- [[hendrie-1968-hexadecapole-deformation]] now calls the Nilsson mechanism a model
  interpretation and the `β4` transfer claim a model sensitivity.
- [[rohozinski-1988-triaxial-scissors-mode]] now labels the double-peak and `γ`
  sensitivity as formalism predictions and experiment-design candidates.
- [[zagrebaev-2001-superheavy-synthesis-survival]] now keeps survival and
  cross-section consequences conditional on the statistical/Langevin inputs.
- [[piekarewicz-2004-soft-monopole-mode]] now distinguishes RRPA predictions from
  universal incompressibility claims.
- [[karmakar-2025-doublet-wobbling-105pd]] now separates measured bands and ratios
  from TPSM/author assignment and retains competing TiP/IBFM explanations.

No numerical claim, source locator, review flag or raw file was changed by this
calibration pass.

## General Rule

The verb in a reusable summary must be determined by the claim layer:

1. `experimental-result`: “measured”, “reported”, “the table gives”, with the exact
   detector/method and locator.
2. `derived`: “inferred from”, “calculated from the reported…”, with the conversion
   convention, inputs and shared uncertainty stated.
3. `model-result`: “the model predicts”, “the calculation yields”, with the model,
   parameters, truncation and comparison data named.
4. `author-interpretation`: “the authors interpret/assign/argue”, followed by at
   least one competing explanation or missing companion observable.
5. `our-inference`: “this review infers”, with the inference chain and failure
   condition explicit.

Words such as “proof”, “unique”, “first confirmed”, “completely excludes” and
“universal” require an additional independent evidence gate. A formal derivation can
prove a statement inside a model without proving that a nucleus realizes the model.
Likewise, a successful fit or an apparently precise posterior does not establish model
identity when the response, state assignment or holdout is unresolved.

## Reusable Stop Conditions

Do not promote a claim above L3 when any of the following is missing:

- the observable is not separated from its inferred structural label;
- the source is a model paper but the proposed sentence is written as an experiment;
- a transition strength is derived from branching, lifetime or normalization without
  the full input and covariance contract;
- an alternative model can reproduce the same energy or strength pattern;
- the source lineage, response, feeding, background or independent holdout is absent.

Under these conditions, keep the source page active if its locator is useful, but phrase
the knowledge page as a conditional evidence boundary. A toy calculation may be kept as
an analysis exercise or falsifier design; it cannot be used as an experimental fact.

## Why This Changes the Research Queue

This audit raises the value of evidence-boundary papers relative to further unanchored
parameter scans. The next paper candidates should first freeze claim kind, source
lineage, state identity, response and a falsifier. For the current queue, this rule
directly supports the `135Pr` common-response audit, the `131Xe` identity/branch paper,
the `135Nd/134Pr` absolute-EM ledger and the cross-mass octupole data map.

## Knowledge Impact and Learning Decision

`revises`: the current full-library map remains useful as a navigation layer, but several
recent source summaries require calibrated wording before they can be reused in a paper.

`limits`: this page does not silently rewrite the five source pages, change their review
flags, or decide whether any author interpretation is physically wrong. It records the
language and evidence-layer boundary that a future source-by-source correction must obey.

`supports`: the existing source claim tables, paper prospectus and figure/data contracts
already contain enough schema to apply this audit without inventing new evidence.

## Open Questions

- Which of the five source pages has a version-specific locator or author correction that
  changes the claim classification?
- Can each model-result statement be linked to an independent observable or holdout
  without reusing the same data in both fit and validation?
- Which older source pages contain the same language mismatch and should enter the next
  bounded audit batch?

## Provisional Reasoning

语言强度应由 claim kind 和 evidence level 决定。模型内部的形式推导不能自动
证明核素实现该模型；成功拟合也不能自动建立模式身份。

## Assumptions

本页只做 self-audit 和复习排序，不重写 source 数值、不清除 review flag、不把
历史运行总结当作新的独立证据。

## Competing Explanations

同一能级、强度或模型趋势可能由多个机制产生；竞争解释必须保留到 companion
observable、response/Cov 和 holdout 闭合。

## Transfer Conditions

语言校准规则可迁移到其它 source/project，但每个 claim 仍必须回到自己的原文
locator、source lineage 和 evidence level。

## Failure Conditions

若 source locator、claim kind 或数据谱系缺失，不升级动词；若存在多个版本而未
闭合，保留版本冲突和 `needs_review`。

## Falsification or Reverse Tests

当一个强表述声称“唯一、证明或完全排除”时，要求独立观测、竞争模型和预先冻结
falsifier；若任一缺失，反向校准为 conditional/provisional wording。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-10-31 | full-library claim-language scan | none | provisional audit ledger | proof-like wording was found in representative model-heavy source pages; no source facts were rewritten | [[wiki-full-library-map-20261030]] |

## Human Review

This is a Codex self-audit. `review_status: unreviewed`; no claim is promoted to
`human-reviewed`, and no source-page review flag is cleared.
