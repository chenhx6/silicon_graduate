---
type: project
title: "A≈130 high-spin model-choice card"
aliases: [A130 model choice card, A≈130 模型选择卡]
created: 2026-09-26
updated: 2026-09-27
status: active
review_status: unreviewed
project_stage: seed
confidentiality: private
nuclei: [131ba, 133ce, 131ce]
tags: [a130, model-choice, mean-field, cranked-shell-model, hfb, angular-momentum-projection]
---

# A≈130 high-spin model-choice card

本页把 Day 3 的模型选择练习固化为可复用决策卡。它用于把实验问题映射到最小理论路线，不把计算的 `β₂/γ`、能级或组态标签写成实验事实。

## Research Question

面对 `131Ba/133Ce` 的 signature splitting、alignment、band crossing 或 `131Ce` 的竞争集体模式，应该选择哪一种最小模型路线？每条路线能回答什么、不能回答什么，哪些实验 companion observables 才能检验模型？

## Current Hypotheses

- static mean-field/HFB 适合给出自洽 intrinsic density、pairing 和候选形状；它不能单独给 laboratory `J`-resolved bands。
- cranked mean-field/CSM 适合 high-spin rotating-frame routhians、alignment、crossing 和 signature；它对 deformation、pairing、reference 和 configuration truncation 敏感。
- angular-momentum projection/PSM/TPSM 把 intrinsic states 恢复为良好 `I` 并混合配置，适合比较 band energies、signature、`B(E2)/B(M1)` 和 g-factors；投影空间与 effective operators 仍是模型输入。
- γ-soft、shape coexistence 或 wobbling 的判断需要超越单个 intrinsic minimum 的 fluctuation/mixing 处理，并由 lifetime、polarization、mixing ratio、absolute strengths 和 linking data 约束。

## Evidence Available

### Model-choice matrix

| 实验问题 | 最小模型路线 | 可以回答 | 不能单独回答 | 必要 companion observable |
|---|---|---|---|---|
| 低自旋 equilibrium shape / pairing | constrained HF/HFB 或 mean-field | intrinsic density、pairing、候选 `β₂,γ,β₃` minima | unique laboratory band identity、绝对 `J`-resolved spectrum | masses/separation energies、`E(2+)`、lifetime/`Q_t`、transfer |
| high-spin alignment/crossing/signature | cranked mean field/CSM，必要时 QTR/TRS | routhians、`i_x`、`J^(2)`、crossing 和 `S(I)` 的机制敏感性 | 把拟合 `γ` 当直接形变；唯一 configuration 或 wobbling/chirality | DCO/ADO、mixing ratio/偏振、lifetimes、absolute `B(E2)/B(M1)`、linking |
| band energies 与 transition strengths 的 laboratory 比较 | PSM/TPSM 或 projected configuration mixing | good-`I` bands、configuration weights、signature、`B(E2)/B(M1)`、g-factors | 对任意模型输入给出唯一实验解释；截断/有效荷/配对误差不会自动消失 | absolute strengths、δ/polarization、band identity、common-data comparison |
| γ-soft vs γ-rigid / coexistence | projected or beyond-mean-field fluctuation/mixing | competing minima、collective wave functions、shape mixing trends | single calculated minimum as proof of rigid shape/coexistence | partner-resolved `Q_t`, E0/E2 links, lifetimes, invariants, transfer or Coulomb excitation |

### A≈130 case mapping

- For Ding 2021 `131Ba/133Ce`, start with CSM/QTR because the direct handles are level energies, `R_ac`, alignment, `J^(2)` and `S(I)`. The source itself says low-`j` `s1/2` Coriolis mixing and non-axiality compete (D21-4–D21-6).
- Use projected configuration mixing only after the target transitions and band identities are fixed; it can compare laboratory transition strengths but does not turn `γ=10°/15°` into a measurement.
- For `131Ce` Bands 1–7, no model route closes the missing δ/polarization/lifetime/absolute-strength chain. The current project ranking therefore remains an evidence question, not a model-selection result.

### Model-to-observable locator crosswalk

| Model layer | Source-grounded locator | Observable handle | What would falsify or downgrade the route |
|---|---|---|---|
| Static mean-field/HFB or Nilsson–Strutinsky | [[aberg-flocard-nazarewicz-1990-mean-field-shapes]] AFN90-1, AFN90-4 | intrinsic `β₂/γ/β₃`, pairing and rotating-frame minima; conventions must be fixed | a laboratory claim based only on one minimum, or a change under self-consistency/rotation-axis convention, leaves the result model-only |
| CSM/QTR sensitivity map | [[ding-2021-131ba-133ce-signature-splitting]] D21-1, D21-4, D21-5, D21-6 | level energies, `R_ac`, alignment, `J^(2)`, `S(I)` and sensitivity to `γ` versus low-`j` Coriolis mixing | the same `S(I)` reproduced by competing attenuation/mixing choices without transition-level `δ`, polarization or strength constraints cannot identify `γ` uniquely |
| PSM/TPSM or projected configuration mixing | [[hara-sun-1995-projected-shell-model-high-spin]] HS10-1, HS10-3, HS10-4, HS10-5 | projected good-`I` energies, configuration weights, `B(E2)/B(M1)`, g-factors and crossing trends | axial-code mismatch is not direct triaxial evidence; basis truncation, particle-number projection and effective operators must be sensitivity-tested |

For `131Ce`, this crosswalk makes the experiment-design order explicit: first secure band identity and measured connecting-transition `δ`/polarization; then obtain partner-resolved lifetimes and absolute `B(E2)/B(M1)` or `Q_t`; only afterward rank CSM/QTR, projected mixing and γ-soft alternatives on a common observable set. A calculated `γ`, configuration weight or projected band energy without that last comparison remains a model result.

## Theory/analysis exercise

For a projected intrinsic state `|Φ_K⟩`, the schematic laboratory energy is

`E_I ≈ ⟨Φ| H P^I |Φ⟩ / ⟨Φ| P^I |Φ⟩`,

followed by a generalized eigenvalue problem when several projected configurations are mixed. The exercise establishes why a calculated projected band has good `I`, while the intrinsic `β,γ` and configuration weights remain model inputs. For the `131Ba/133Ce` case, the minimum defensible chain is:

`level energies + R_ac + alignment → CSM/QTR sensitivity map → projected/mixed transition prediction → δ/polarization/lifetime/absolute-strength test`.

Removing the final experimental test leaves a model comparison, not a unique shape or collective-mode assignment.

## Counter-evidence and missing companion observables

- AFN90-1/AFN90-4: intrinsic minima and `β₂/γ` conventions are model outputs; rotation-axis and higher-multipole conventions can change the interpretation.
- AFN90-2: alignment, stretching, band termination, intruder polarization and shape coexistence can produce similar high-spin changes.
- HS10-4: an A≈130 axial PSM mismatch can motivate a triaxial candidate, but the review explicitly does not treat axial-code failure as direct proof of triaxiality.
- HS10-5: particle-number projection and truncated spaces can introduce spurious pair states or sensitivity to configuration selection.
- The required companion set for a mode claim remains transition-level δ/偏振, partner-resolved lifetimes and absolute strengths, and independent linking/identity constraints.

## Risks and Blockers

- No common A≈130 model table with parameter covariance is available in this run; no proxy fit is generated.
- `γ` values from CSM, QTR, PES, PSM or TRS use different parameterizations and cannot be averaged.
- Historical PSM examples and review conclusions are dependent theory sources, not independent experimental confirmation.
- L4 remains not-ready without event/response/covariance/code inputs.

## Next Actions

1. Apply this card to one `131Ce` question only after a band/transition manifest is available.
2. Compare axial CSM, triaxial QTR/TPSM and a γ-soft alternative on the same observable set.
3. Keep model outputs, author interpretations and measured electromagnetic properties in separate evidence rows.
