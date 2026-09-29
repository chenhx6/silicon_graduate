---
type: project
title: "A≈130 high-spin model-choice card"
aliases: [A130 model choice card, A≈130 模型选择卡]
created: 2026-09-26
updated: 2026-09-29
status: active
review_status: unreviewed
project_stage: seed
confidentiality: private
nuclei: [131ba, 133ce, 131ce]
tags: [a130, model-choice, mean-field, cranked-shell-model, hfb, angular-momentum-projection]
---

# A≈130 high-spin model-choice card

本页把 Day 3 的模型选择练习固化为可复用决策卡。它用于把实验问题映射到最小理论路线，不把计算的 `β₂/γ`、能级或组态标签写成实验事实。

## Agent active summary

- Day 3 已把 Hara–Sun 的投影核与轴对称迁移边界写入本卡；续接补入 Bhat 2014 `130Cs` 比较，并发现 Sheikh et al. 2024 对 Hara Table 5 的 `133La`、`135Pr` 两个 `N=76` 星号核素做了 TPSM 计算。后者的固定 `γ` 是模型输入，数据复用既有实验；不改变 `131Ce` project 的模式排序，也不确认其 `N=73` 形状。

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
| A≈130 odd–odd TPSM transfer control | [[bhat-2014-tpsm-cs-doublet-bands]] BHA14-1, BHA14-3, BHA14-4, BHA14-5 | `124,126,130,132Cs` projected bands and energy comparison; for `130Cs`, TPSM absolute `B(E2)`, `B(M1)` predictions plus previously published intensity-derived ratios | `130Cs` is `N=75`, not `131Ce N=73` or the historical `N=76–78` candidates; absolute `130Cs` strengths are not measured here, and the Table 1/Eq.3 gamma mapping needs version/parameter clarification |
| `130Cs` primary experiment behind the TPSM ratios | [[simons-2005-130cs-chiral-structures]] SIM05-1, SIM05-3–SIM05-7; [[bhat-2014-tpsm-cs-doublet-bands]] BHA14-4 | observed band/link scheme, DCO/polarization, smooth `S(I)` and intensity-derived ratio patterns; Bhat Fig.8 reuses the Simons Euroball data | band B lacks `B(M1)/B(E2)` staggering, mid-spin splitting is finite and the high-spin crossing changes structure; no `130Cs` lifetimes/absolute strengths | partner-resolved lifetimes and absolute strengths; do not double-count the theory comparison or transfer to `131Ce` |

### Hara Table 5: later TPSM coverage check (2026-09-29)

Hara–Sun Table 5 的星号位置经原表视觉复核为：`133La (Z=57,N=76)`、`134La (57,77)`、`135Ce (58,77)`、`135Pr (59,76)`、`136Pr (59,77)`、`137Pr (59,78)` 和 `137Nd (60,77)`（[[hara-sun-1995-projected-shell-model-high-spin]] HS10-4）。Sheikh et al. 2024 [[sheikh-jehangir-bhat-2024-tpsm-wobbling]] 对其中 `133La` 与 `135Pr` 做了三轴投影计算：Table 1 给定的 `γ` 分别为 `36°`、`32°`，Figs. 11–14 比较谱能、摇摆频率、对齐和跃迁比。此处 `γ` 是输入，不是测量；图中实验曲线重用此前论文。这个证据把“后续 TPSM 是否覆盖 Hara 核素”从未知改为已确认 2/7，但不构成形状的独立确认。其余五个星号核素仍待逐核查。

For `131Ce`, this crosswalk makes the experiment-design order explicit: first secure band identity and measured connecting-transition `δ`/polarization; then obtain partner-resolved lifetimes and absolute `B(E2)/B(M1)` or `Q_t`; only afterward rank CSM/QTR, projected mixing and γ-soft alternatives on a common observable set. A calculated `γ`, configuration weight or projected band energy without that last comparison remains a model result.

## Theory/analysis exercise

### Day 3 kernel reconstruction and applicability check (2026-09-29)

Hara–Sun define the angular-momentum projector as

`P̂^I_MK = (2I+1)/(8π²) ∫ dΩ D^{I*}_MK(Ω) R̂(Ω)` (Eq. 2.7, PDF p.642).

For one intrinsic state, the projected Hamiltonian and norm kernels are

`H^I_KK′ = ⟨Φ| Ĥ P̂^I_KK′ |Φ⟩`,  `N^I_KK′ = ⟨Φ| P̂^I_KK′ |Φ⟩`,

and configuration amplitudes solve the non-orthogonal generalized eigenproblem

`Σ_K′ (H^I_KK′ − E_I N^I_KK′) F^I_K′ = 0`,  `Σ_KK′ F^{I*}_K N^I_KK′ F^I_K′ = 1`

(Eqs. 2.19–2.20, PDF p.644). The familiar ratio `⟨Φ|ĤP̂^I|Φ⟩/⟨Φ|P̂^I|Φ⟩` is the one-configuration limit; it should not replace the kernel diagonalization when several projected configurations mix. A triaxial intrinsic state can contribute multiple `K` components to the same `I`, while the axial single-`K` case reduces to the simpler expression (Eq. 2.21).

This derivation separates a cranked mean-field/CSM calculation, which tracks rotating-frame alignments and crossings, from projection, which restores good angular momentum within the chosen intrinsic basis. In the PSM that basis is built from Nilsson+BCS quasiparticles and selected multi-quasiparticle configurations; the Hamiltonian includes quadrupole–quadrupole and pairing terms (Eq. 2.40, PDF p.651). Both the intrinsic deformation and the projected-space truncation remain model inputs.

For the `131Ce` application, the minimum defensible chain is:

`level energies + R_ac + alignment → CSM/QTR sensitivity map → projected/mixed transition prediction → δ/polarization/lifetime/absolute-strength test`.

Alwaleedi's `B(M1)/B(E2)` comparison assumes `δ=0`, and the dataset lacks lifetimes, absolute `B(E2)`, linear polarization and direct shape measurement. Removing the final experimental test therefore leaves a model comparison, not a unique shape or collective-mode assignment.

## Counter-evidence and missing companion observables

- AFN90-1/AFN90-4: intrinsic minima and `β₂/γ` conventions are model outputs; rotation-axis and higher-multipole conventions can change the interpretation.
- AFN90-2: alignment, stretching, band termination, intruder polarization and shape coexistence can produce similar high-spin changes.
- HS10-4: Hara–Sun §5.1, Table 5 (PDF pp.712–713) labels N=76–78 candidates “presumably triaxial” after axial PSM failed to reproduce data; p.713 states that their code assumed axial symmetry and calls for a triaxial projection calculation. This is a model-based inference, not a direct shape measurement, and it does not transfer to `131Ce` (Z=58, N=73), which Table 5 places in the prolate `+0.22` column.
- HS10-5: in `156Er`, particle-number projection changes the backbending and brings the lowest quasiparticle-pair state closer to yrast (Figs.26–27, PDF pp.700–701). The authors warn that truncation can leave spurious pair-state admixtures, so adding number projection is not automatically a safer result.
- BHA14-4/BHA14-5: `130Cs` TPSM matches published energies and intensity-derived ratios, but the absolute transition-strength curves are predictions; the paper explicitly calls for lifetime measurements. This supports using TPSM to design a comparison, not using neighboring-Cs agreement as `131Ce` evidence.
- SIM05-3/SIM05-5/SIM05-7: the primary `130Cs` experiment establishes linking-transition multipolarity/polarization and derives ratio trends, but band B lacks `B(M1)/B(E2)` staggering and the paper requests lifetimes. Bhat Ref. [32] reuses this dataset, so the theory/experiment pair is one experimental lineage.
- BHA14-6: the printed `ε,ε′` and Eq. (3) imply `γ≈42°` for `130,132Cs`, unlike the nearby prose's approximate `30°`; keep the parameter/wording mismatch localized to the arXiv v1 until the journal version and convention are checked.
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
