---
type: project
title: "A≈130 high-spin model-choice card"
aliases: [A130 model choice card, A≈130 模型选择卡]
created: 2026-09-26
updated: 2026-09-30
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
- Day 3 后续还核读 Jehangir et al. 2022 odd-neutron TPSM：`131Xe` 展示从 1ν/1ν+2π 到 3ν/3ν+2π 投影基底的扩展，但只是 N=77 同中子素方法控制，不是 Hara 表三核或 `131Ce` 的直接计算。

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
| Frequency-dependent Woods–Saxon TRS shape surface | [[banik-2020-131xe-multiple-band-structures]] BNK20-6, BNK20-7 | β₂, γ minima versus rotational frequency for fixed quasiparticle configurations; compare with S(I)/alignment trends | minima are model outputs dependent on potential, configuration, frequency and Lund convention; broad γ-soft surfaces do not establish a rigid shape or coexistence | partner-resolved lifetimes and absolute B(E2)/B(M1), Q_t, and an independent shape-sensitive observable; do not average with fixed TPSM/TPRM γ inputs |
| PSM/TPSM or projected configuration mixing | [[hara-sun-1995-projected-shell-model-high-spin]] HS10-1, HS10-3, HS10-4, HS10-5 | projected good-`I` energies, configuration weights, `B(E2)/B(M1)`, g-factors and crossing trends | axial-code mismatch is not direct triaxial evidence; basis truncation, particle-number projection and effective operators must be sensitivity-tested |
| A≈130 odd–odd TPSM transfer control | [[bhat-2014-tpsm-cs-doublet-bands]] BHA14-1, BHA14-3, BHA14-4, BHA14-5 | `124,126,130,132Cs` projected bands and energy comparison; for `130Cs`, TPSM absolute `B(E2)`, `B(M1)` predictions plus previously published intensity-derived ratios | `130Cs` is `N=75`, not `131Ce N=73` or the historical `N=76–78` candidates; absolute `130Cs` strengths are not measured here, and the Table 1/Eq.3 gamma mapping needs version/parameter clarification |
| `130Cs` primary experiment behind the TPSM ratios | [[simons-2005-130cs-chiral-structures]] SIM05-1, SIM05-3–SIM05-7; [[bhat-2014-tpsm-cs-doublet-bands]] BHA14-4 | observed band/link scheme, DCO/polarization, smooth `S(I)` and intensity-derived ratio patterns; Bhat Fig.8 reuses the Simons Euroball data | band B lacks `B(M1)/B(E2)` staggering, mid-spin splitting is finite and the high-spin crossing changes structure; no `130Cs` lifetimes/absolute strengths | partner-resolved lifetimes and absolute strengths; do not double-count the theory comparison or transfer to `131Ce` |
| Odd-neutron TPSM basis-extension control | [[jehangir-2022-odd-neutron-tpsm-extension]] JN22-1, JN22-2, JN22-4, JN22-6, JN22-8, JN22-11, JN22-13, JN22-14 | 117–131Xe projected bands; `131Xe` demonstrates the 3ν/3ν+2π extension, yrast comparison and predicted crossing/signature behavior; HFB consistency relates QQ strength `χ` to input `ε`; approximate `ε′/ε` mapping agrees with Table I to rounding | `131Xe` is not a Hara Table 5 nucleus; `γ=29°` is an inherited input, its yrare band is unobserved, and nonorthogonal amplitudes are not probabilities; the HFB relation does not make inherited deformation a new shape determination | band-resolved experimental levels/links, measured electromagnetic strengths and g-factors; do not count as independent data or transfer from N=77 Xe to N=73 `131Ce` |
| `131Xe` primary dataset and later reanalysis | [[banik-2020-131xe-multiple-band-structures]] BNK20-1, BNK20-2, BNK20-5, BNK20-6; [[jehangir-2022-odd-neutron-tpsm-extension]] JN22-12; [[chakraborty-2023-131xe-wobbling-origin]] C23-2, C23-3, C23-7 | 38-MeV `130Te(α,3n)` INGA level scheme, 72 added links, relative intensities, DCO/polarization; 2022 TPSM Fig.7 uses earlier levels; 2023 analysis reuses the same acquisition | a single experiment supports three publications, not three independent data sets; no lifetime or absolute `B(E2)/B(M1)`; TRS shapes are model outputs and B1(b) γ-band assignment remains open | partner-resolved lifetimes and absolute strengths; branch-complete inter/intraband transitions; do not transfer N=77 `131Xe` evidence to N=73 `131Ce` |

### Hara Table 5: later TPSM coverage check (2026-09-29)

Hara–Sun Table 5 的星号位置经原表视觉复核为：`133La (Z=57,N=76)`、`134La (57,77)`、`135Ce (58,77)`、`135Pr (59,76)`、`136Pr (59,77)`、`137Pr (59,78)` 和 `137Nd (60,77)`（[[hara-sun-1995-projected-shell-model-high-spin]] HS10-4）。Sheikh et al. 2024 [[sheikh-jehangir-bhat-2024-tpsm-wobbling]] 对其中 `133La` 与 `135Pr` 做了三轴投影计算：Table 1 给定的 `γ` 分别为 `36°`、`32°`，Figs. 11–14 比较谱能、摇摆频率、对齐和跃迁比。此处 `γ` 是输入，不是测量；图中实验曲线重用此前论文。该篇文章明确覆盖 2/7 个 Table 5 星号案例的 TPSM 计算，但不构成独立形状确认。

另一个相关但不同模型路线是 [[petrache-2020-137nd-multiple-chiral-bands]]：它研究 Hara 表内 `137Nd (N=77)` 的 D2/D3、D5/D6，并用 constrained CDFT 与 PRM 得到约 `β=0.20–0.21, γ=28.9°–29.5°` 的模型解；PRM 使用约 `γ=20.9°/23.5°`。这是同核后续三轴模型应用，但对象是较晚识别的候选手征带，不是对 Hara 轴对称 PSM 计算或其旧能级序列的逐项投影重算，因此不能计作 Hara 结论的直接复核。新 D3/D6 仍缺实验 `B(M1)/B(E2)`（P20-4/P20-5），几何与手征解释仍为模型/作者解释。

[[budaca-budaca-2025-harmonic-chiral-vibration]] 对同一 `137Nd` D5/D6 `πh11/2²⊗νh11/2⁻¹` energy-splitting 数据使用 harmonic chiral-vibration approximation，输入 `j=11/2,j′=10`，Fig.4f 拟合 paper-sector `γ=97.5°`；按 `120°−γ` 对称映射，常用 sector 为 `22.5°`。按该文 Eqs. (2),(7) 复算，`I_c≈17.804ℏ`：Fig.4f 纳入的 `I=16.5ℏ`、`17.5ℏ` 点低于该模型阈值，`I=18.5ℏ` open point 高于阈值且未纳入；论文未声明这就是排除原因。P20 D5/D6 PRM input `γ=23.5°` 与 P25 的 `22.5°` 约差 `1°`，但 P25 重用 P20 Ref. [30] 同一实验数据、只有很少的拟合点且未给 `137Nd` transition-ratio test；数值接近是模型内部一致性线索，不是独立 shape measurement、统计误差区间或 Hara axial-PSM 重算。

当前 full-text 确认的 Hara 候选模型路线为：`133La`、`135Pr` 的 2024 TPSM 应用，以及 `137Nd` 的 2020 CDFT/PRM 与 2025 harmonic-PRM-type model。`134La`、`135Ce`、`136Pr`、`137Pr` 的具体可复核投影覆盖仍需查证。

For `131Ce`, this crosswalk makes the experiment-design order explicit: first secure band identity and measured connecting-transition `δ`/polarization; then obtain partner-resolved lifetimes and absolute `B(E2)/B(M1)` or `Q_t`; only afterward rank CSM/QTR, projected mixing and γ-soft alternatives on a common observable set. A calculated `γ`, configuration weight or projected band energy without that last comparison remains a model result.

### 2026-09-30 extension: 136Pr TAC-CDFT is not projection coverage

Lv et al. 2025 add a high-statistics JUROGAM II 136Pr dataset and compare it with PC-PK1 tilted-axis-cranking CDFT; SN100PN shell-model calculations address D5 and related low-energy states. This is a direct modern calculation for an exact Hara Table 5 nucleus, but it does not perform angular-momentum projection and does not increase the confirmed TPSM count beyond two of seven candidates. Its Table II deformations and configurations are model outputs. The calculation describes D1 energies better than its B(M1)/B(E2) values, underestimates the D2 ratios, and finds no TAC-CDFT configuration for D5. Q1 parity remains unresolved by the reported polarization attempt. The authors leave magnetic rotation and prolate–oblate triaxial shape coexistence as alternatives for D4/D6; this does not establish either shape experimentally ([[lv-2025-136pr-tac-covariant-density-functional]] LV25-3–LV25-10).

The current bounded full-text map is: 133La and 135Pr have direct TPSM calculations; 136Pr and 137Pr have exact-nucleus TAC-family applications; 137Nd has CDFT/PRM plus a harmonic chiral-vibration fit that reuses the P20 data. These routes are not interchangeable. The other five Hara Table 5 nuclei (`134La`, `135Ce`, `136Pr`, `137Pr`, `137Nd`) have no verified direct PSM/TPSM projection source in this run: `136Pr/137Pr/137Nd` have accessible full text only for nonprojected routes, while `134La/135Ce` remain metadata/access-blocked. This bounded-search statement is not proof that no projection paper exists.

### 2026-09-30 extension: 137Pr TAC magnetic-rotation case

Agarwal et al. 2007 establish a negative-parity ΔI=1 M1 band in 137Pr through 47/2− with DCO and linear-polarization support and newly observed weak crossover E2 transitions. Relative-intensity B(M1)/B(E2), calculated with δ² assumed negligible, rises through about 37/2− and then decreases. Their hybrid TAC compares a low-spin 3qp configuration with a high-spin 5qp configuration to explain the back-bend. The 5qp calculation is shifted by about 2.2 MeV and two spin units, so the crossing is a model-supported interpretation with visible normalization limits. This adds an exact-nucleus TAC route for Hara N=78 137Pr, but not angular-momentum projection or direct shape confirmation ([[agarwal-2007-137pr-magnetic-rotation-bandcrossing]] AG07-2–AG07-9).

The confirmed direct TPSM projection coverage remains 2/7. `136Pr` and `137Pr` have later TAC-family model applications, and `137Nd` has CDFT/PRM and a harmonic-approximation analysis; none performs PSM/TPSM projection. Their model parameters do not replace a shape-sensitive measurement. For `134La/135Ce`, current leads remain metadata-only/closed; no scientific claim is imported from those titles.

### 2026-09-30 continuation: `131Xe` primary experiment and shared data lineage

Banik et al. 2020 [[banik-2020-131xe-multiple-band-structures]] are the primary INGA `130Te(α,3n)` experiment: the authors report 72 added transitions and table relative intensities with `R_DCO`/`Δ_PDCO`, not partner-resolved lifetimes or absolute strengths. Their B1(a) signature-partner interpretation is supported by the measured links; B1(b) remains a possible γ side band without enough intra-band links to close the case. Figs. 17–20 are Woods–Saxon Strutinsky TRS calculations, not measured shapes. Jehangir TPSM 2022 compares to Banik's data; Chakraborty 2023 explicitly reanalyzes the same data to test a wobbling interpretation. These papers form one acquisition lineage, not three independent experiments. The band-label crosswalk is open: C23 states the unfavored partner was not established in earlier 131Xe work and favors a low-spin yrare-13/2 interpretation, while the 2020 article labels B1(a) a signature partner; do not equate B1(a), B5 and the C23 sequence without transition-level reconciliation (BNK20-10; C23-6). The 2023 low-E2/M1-dominated result strengthens the signature-partner reading, while absolute transition strengths and lifetimes remain missing ([[chakraborty-2023-131xe-wobbling-origin]] C23-2, C23-3, C23-7).

### 2026-09-30 continuation: odd-neutron TPSM method control

Jehangir et al. 2022 [[jehangir-2022-odd-neutron-tpsm-extension]] extends the odd-neutron projected basis to `3ν` and `3ν+2π` configurations and compares the `117–131Xe` chain with previously published levels. For `131Xe`, Table I gives `ε=0.160`, `ε′=0.090`, `γ=29°`; these are inherited model inputs. The yrast comparison is available, but the `131Xe` yrare band is unobserved and its signature behavior is predicted. Figure 7 uses earlier experimental references; the paper adds no experiment. Its warning that projected amplitudes from a nonorthogonal basis are not probabilities also limits configuration claims (JN22-1–JN22-11).

The mass-number check `131−Z(Xe=54)=N=77` puts `131Xe` in the same isotone chain as Hara's `134La`, `135Ce`, and `136Pr`, but the paper covers zero of those three exact candidate nuclei. This changes the method-control inventory, not the confirmed Hara direct TPSM coverage count (still `2/7`). For `131Ce`, neither its `N=73` structure nor the missing target-band transition strengths can be inferred from this neighboring isotone. A useful next discriminator for the model's predicted odd-neutron structure is the author-proposed g-factor measurement; measured lifetimes and absolute transition strengths would also test the predicted electromagnetic response. The 2022 TPSM Figure 7 and Chakraborty et al. 2023 share the Banik 2020 `131Xe` experimental-data lineage (JN22-12); count the latter as a new analysis/interpretation of that dataset, not an independent experiment. Its low-E2/M1-dominated signature-partner interpretation is counter-evidence to treating triaxial input or energy agreement alone as wobbling evidence ([[chakraborty-2023-131xe-wobbling-origin]] C23-2, C23-3, C23-7).

As an input consistency check, Bhat et al. 2014 Eq. (3) gives the approximate mapping `γ=arctan(ε′/ε)`. For the Jehangir `131Xe` Table I values, `arctan(0.090/0.160)=29.36°`, consistent with its integer `29°` entry (JN22-14; BHA14-6). This verifies only that the listed model parameters are mutually consistent under that convention; it does not infer shape from data and does not resolve the separate Bhat `130,132Cs` prose/table mismatch.

#### Nonorthogonal projected-amplitude check (illustrative)

For two normalized projected basis states with overlap `s` and equal coefficients `c`, norm normalization gives `1=2|c|²(1+s)`. If an illustrative overlap is `s=0.5`, then `|c|²=1/3` for each state while the sum of squared coefficients is only `2/3`; the remaining `1/3` is the cross term from nonorthogonality. This is a toy algebra check, not a TPSM fit or a value taken from Jehangir et al. It explains why JN22 Fig. 8–10 projected amplitudes cannot be read as conventional configuration probabilities ([[jehangir-2022-odd-neutron-tpsm-extension]] JN22-2, JN22-8).

#### 131Xe cross-model γ parameter role check (2026-09-30)

| Source/method | `131Xe` γ entry | What the number means | Data/interpretation boundary |
|---|---:|---|---|
| Banik 2020 TRS | `γ≈−26°` at `ℏω=0.21–0.26 MeV`; low-frequency surface is γ-soft and high-frequency minima split | A frequency-dependent Woods–Saxon Strutinsky TRS minimum for the 1-qp `B1` configuration; Lund convention is explicitly stated | A model output from the same INGA band data, not a static shape measurement (BNK20-6) |
| Jehangir 2022 TPSM | `γ=29°`, with `ε=0.160`, `ε′=0.090` | An adopted Table I deformation input for the odd-neutron TPSM chain, including `131Xe`; approximate `arctan(ε′/ε)=29.36°` check is parameter arithmetic | It is not fitted/observed in the 2022 calculation; Fig. 7 reuses earlier levels (JN22-4, JN22-12, JN22-14) |
| Chakraborty 2023 TPRM | `γ=33°`, `ε₂=0.13`, `ξ=1` | A TPRM parameter set selected to reproduce the observed favored/unfavored signature partners | It analyzes the Banik acquisition; it is not an independent shape-sensitive experiment (C23-4, C23-7) |

Using absolute values only as a descriptive arithmetic screen gives pairwise differences `|29−26|=3°`, `|33−29|=4°`, and `|33−26|=7°`. This is not an uncertainty-weighted model average: one value is an `ℏω`-dependent TRS output, one is an inherited TPSM input, and one is a rotor-model parameter set; their conventions/configuration spaces differ and no common covariance is reported. Their numerical proximity can motivate a common-observable comparison but cannot count as independent confirmation of `131Xe` shape or wobbling. Partner-resolved lifetime/absolute-strength and g-factor data remain the higher-information tests.

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
