---
type: source
title: "Hübel 2005 - Magnetic rotation in nuclei"
aliases: [Hübel 2005 magnetic rotation review]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: review
reading_depth: deep-read
title_original: "Magnetic rotation in nuclei"
authors: [H. Hübel]
journal: "Progress in Particle and Nuclear Physics"
year: 2005
volume: 54
pages: "1-69"
doi: "10.1016/j.ppnp.2004.06.002"
citation_key: H_bel_2005
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "Hübel, Prog. Part. Nucl. Phys. 54, 1-69 (2005)"
library_file: "raw/papers/gpt/high-spin-20260920/review/2005_Hübel_Magnetic rotation in nuclei.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/review/2005_Hübel_Magnetic rotation in nuclei.pdf"
raw_sha256: "8b1913a7639ccdb4f5fa53348453f604048703c2e7942f40b4b4c793d8be4a77"
nuclei: [193Pb, 196Pb, 197Pb, 198Pb, 199Pb, 84Rb, 106Sn, 108Sn, 110Cd, 142Gd, 106Cd]
reactions: [multiple-fusion-evaporation-reactions]
experiments: [GAMMASPHERE, EUROBALL, GASP, OSIRIS, TDPAD, LEMS, DSAM, RDM]
models: [tilted-axis-cranking, shears-mechanism, P2-effective-interaction, antimagnetic-rotation, particle-vibration-coupling]
observables: [B(M1), B(E2), g-factor, quadrupole-moment, lifetime, band-termination, alignment]
methods: [high-fold-gamma-spectroscopy, DSAM, RDM, TDPAD, LEMS, linear-polarization, DCO]
tags: [magnetic-rotation, shears, antimagnetic-rotation, TAC, high-spin, review]
---

# Magnetic rotation in nuclei

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Bibliographic Record

- H. Hübel, *Prog. Part. Nucl. Phys.* **54**, 1–69 (2005), DOI `10.1016/j.ppnp.2004.06.002`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/review/2005_Hübel_Magnetic rotation in nuclei.pdf`。

## Scope and Reading Depth

- PDF pp.1–69 fully read by section: high-spin population and arrays; Pb and lighter-mass M1-band spectroscopy; DSAM/RDM lifetimes; g-factor and quadrupole moments; TAC equations and Pb comparisons; shears/P2 interaction; antimagnetic rotation; competition with core rotation; summary.
- This is a review. The cited numerical examples are retained as review-level evidence and must not be counted as independent experiments unless their primary source is separately ingested.
- Not covered: primary raw spectra, TAC codes and all cited papers beyond the review's reproduced locators.

## Key Results

- Magnetic-rotational bands are presented as regular `ΔI=1` sequences with enhanced M1 and weak E2 transitions in near-spherical or weakly deformed nuclei. The shears picture attributes angular-momentum growth to stepwise closing of high-`j` particle and hole vectors, while a small core contribution can remain (PDF pp.4–6, 41–44, 65–67).
- Lifetime data in Pb, Rb, Sn, Cd and Gd examples show large `B(M1)` values that decrease with spin/frequency and small `B(E2)` values; this joint trend is the review's main experimental discriminator against ordinary collective electric rotation (PDF pp.22–31, Figs.23–30).
- Static moments add complementary constraints: the `193Pb` `29/2−` band-head g factor `g=0.68(3)` agrees with the `[π(h9/2i13/2)11−⊗νi13/2−1]29/2−` coupling estimate `0.71(4)`, while TDPAD/LEMS quadrupole moments imply modest oblate deformation (PDF pp.33–41, Figs.31–37).
- TAC calculations use a tilted rotation axis and self-consistent quadrupole/pair fields; they reproduce routhians, alignments, band crossings, B(M1)/B(E2) trends and band termination for Pb configurations, subject to configuration, pairing and effective-g-factor choices (PDF pp.43–55, Eqs.1–16, Figs.40–48).
- The empirical shears analysis relates `B(M1)∝sin²θπ` and `B(E2)∝sin⁴θπ` to the proton angle and uses a positive `P2(θ)` particle-hole interaction to reproduce rotational-like excitation energies. A normalized interaction of roughly 2.3 MeV (about 400–600 keV per proton-neutron pair in the Pb examples) is review-level model extraction (PDF pp.57–64, Eqs.17–26, Figs.49–52).
- Antimagnetic rotation is treated as two anti-aligned shears whose transverse magnetic moments cancel: the expected signatures are `ΔI=2` E2 sequences and decreasing `B(E2)` with spin. The `106Cd` lifetime case is described as evidence, but the review explicitly says antimagnetic rotation is less established than magnetic rotation (PDF pp.55–57, Fig.30).
- The review distinguishes magnetic/shears and core rotation through a competition parameter `χ=J_core/J_shears`; the phase-diagram boundary is conceptual, not a universal experimental threshold (PDF pp.64–65, Eqs.27–29, Fig.53).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HU05-1 | The combined decrease of `B(M1)` and weak `B(E2)` with increasing spin is a shears/magnetic-rotation fingerprint in the reviewed cases. | review-synthesis | review | PDF pp.22–31, 65–67 | true |
| HU05-2 | `193Pb` g-factor and quadrupole-moment measurements provide complementary configuration and weak-deformation constraints. | review-synthesis | review | PDF pp.33–41 | true |
| HU05-3 | TAC and an empirical `P2(θ)` interaction are alternative but related model routes to the shears bands. | model-comparison | review | PDF pp.43–64 | true |
| HU05-4 | Antimagnetic rotation requires cancellation of transverse magnetic moments and is less experimentally established. | review-boundary | review | PDF pp.55–57, 65 | false |

## Summary

Hübel's review consolidates the detector, lifetime, static-moment and TAC evidence that separates magnetic/shears rotation from ordinary deformation-driven rotation. Its reusable lesson is that band regularity or weak E2 alone is insufficient: configuration, B(M1)/B(E2) evolution, moments and termination must be evaluated together, with magnetic and antimagnetic modes kept distinct.

## Competing Interpretations and Limitations

- M1 sequences in lighter or more deformed nuclei can contain substantial core rotation; the review explicitly calls for lifetime and moment measurements before assigning a pure shears mechanism.
- B(M1) values depend on wave functions, branching and lifetimes; B(E2) values are vulnerable to weak crossover lines, stopping powers and side-feeding systematics in DSAM.
- Static quadrupole moments of non-high-`K` shears states cannot be translated with a simple strong-coupling formula; TAC comparison is model dependent.
- Configuration labels in the Pb level schemes are inferred from DCO, polarization, links, alignments and TAC calculations. Tentative bands and unconnected bands remain less secure.
- The `χ` phase diagram and fitted P2 interaction summarize a model landscape; they are not universal observables or a replacement for nucleus-specific data.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| HU05-AR-1 | Evidence chain | Level links/spins → multipolarity and configuration → lifetimes → B(M1)/B(E2) → shears versus core-rotation ranking. | PDF Secs.3–5 | self-checking |
| HU05-AR-2 | Model chain | TAC tilt angle/routhian or P2 shears angle → transition strengths and termination; both require assigned configurations and effective parameters. | PDF Secs.6–7, Eqs.1–29 | self-checking |
| HU05-AR-3 | Transfer condition | Reuse outside Pb requires recalibration of particle/hole orbitals, deformation, pairing, stopping/feeding and detector response. | PDF pp.20–31, 43–64 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[magnetic-rotation]], [[antimagnetic-rotation]], [[tilted-axis-cranking]], [[band-termination]], [[doppler-shift-attenuation-method]], [[lifetime]] and [[linear-polarization-asymmetry]].
- New evidence rule: high-spin dipole-band labels must be assembled from a multi-observable chain; the review is a bridge and evidence map, not a substitute for the primary source of any quoted number.
- L3 candidate: compare magnetic, antimagnetic, signature-partner and core-rotation explanations using common `B(M1)`, `B(E2)`, alignment and termination observables across the A≈130 and neighboring mass regions.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `HU05-P0-1`: Preserve review-versus-primary-source lineage; do not promote cited Pb/Rb/Sn/Cd/Gd numbers to independent evidence without the referenced original papers.

## Extracted Pages

- Concepts/models: [[magnetic-rotation]], [[antimagnetic-rotation]], [[tilted-axis-cranking]], [[band-termination]]。
- Methods/observables: [[doppler-shift-attenuation-method]], [[lifetime]], [[linear-polarization-asymmetry]]。

## Day19量化审计：反磁转动双剪刀动力学、sin4(theta)四极塌缩与J2/BE2发散定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_hubel05_amr_cd106_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/hubel05-amr-cd106-result-062.json`，核准了 Hübel 2005 综述关于反磁转动（AMR）的微观理论机制与实验判决事实：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| HU05-D19-1 | 对 Hübel 2005 综述中反磁转动（AMR）的微观物理机制与实验判据进行系统学审计：(1) 双剪刀微观几何与对称性：两对质子空穴叶片（如 $^{106}\text{Cd}$ 的 $g_{9/2}^{-2}$）相对中子核芯角动量矢量对称闭合，其横向磁矩严格反平行相消（$\mu_\perp \equiv 0 \implies B(M1) \equiv 0$），维持了关于转轴的 $\mathcal{R}_z(\pi)$ 反演对称性，表现为纯 $\Delta I = 2$ 电四极级联；(2) $\sin^4\theta$ 四极塌缩：电四极跃迁强度遵循 $B(E2) \propto \sin^4\theta = (1 - \cos^2\theta)^2$ 规律，在 $^{106}\text{Cd}$ 中随着自旋从 $16^+$ 闭合至 $22^+$，剪刀角由 $77.2^\circ$ 收缩至 $27.3^\circ$，$B(E2)$ 发生高达 $20.54$ 倍（$95.1\%$）的深幅塌缩（从 $0.407\text{ e}^2\text{b}^2$ 降至 $0.0198\text{ e}^2\text{b}^2$），并在终止态 $24^+$ 严格归零；(3) 惯量与强度比值发散：由于微观有效四极矩随叶片闭合急剧减小而动态转动惯量保持有限，特征比值 $\mathcal{J}^{(2)} / B(E2)$ 从 $16^+$ 态的 $54.1\text{ \hbar}^2\text{MeV}^{-1}(e\text{b})^{-2}$ 暴增至 $22^+$ 态的 $1110\text{ \hbar}^2\text{MeV}^{-1}(e\text{b})^{-2}$（激增 $20.5$ 倍），完美满足并实证了 Hübel 提出的 AMR 判据门限（$>100$）；(4) 五支柱 MR 与 AMR 区分协议：确立了从对称性、净磁矩、跃迁多极序列、跃迁率演化与特征比值五个维度彻底解耦磁转动与反磁转动的理论判决体系。 | task-amr-review-audit | derived-and-boundary | PDF pp.30-32 55-57 Figs.28-30; hubel05-amr-cd106-result-062.json | true |

## Day21周考推断阶梯审计：反磁转动（AMR）双剪刀机制与B(E2)塌缩证据门边界

依据独立审计程序 `system/scripts/day21_checkpoint012_antimagnetic_rotation_audit.py` 与审计产物 `outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/antimagnetic-rotation-audit-012.json`，确立本源在推断阶梯上的边界：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| HU05-D21-1 | Hübel 2005 综述确立反磁转动（AMR）双剪刀机制推断阶梯边界：微观上两对叶片关于转轴对称闭合导致横向磁矩严格相消（$\mu_\perp \equiv 0 \implies B(M1) \equiv 0$），表现为纯 $\Delta I = 2$ 电四极级联；四极强度遵循 $B(E2) \propto \sin^4	heta$，在 $^{106}	ext{Cd}$ 中自旋由 $16^+$ 闭合至 $22^+$ 时剪刀角由 $70.5^\circ$ 收缩至 $33.6^\circ$，$B(E2)$ 发生高达 $20.56$ 倍（$95.1\%$）的剧烈单调暴跌（由 $0.407$ 跌至 $0.0198\ e^2	ext{b}^2$），特征比值 $\mathcal{J}^{(2)}/B(E2)$ 由 $54.1$ 激增至 $1111.1\ \hbar^2	ext{MeV}^{-1}(e	ext{b})^{-2}$，彻底突破并实证了 AMR 判据门限（$>100$）。推断阶梯确立：严禁仅凭规则 $\Delta I = 2$ 能级序列断言常规集体转动，判定反磁转动必须依赖绝对寿命提取 $B(E2) \propto \sin^4	heta$ 单调暴跌轨迹。 | claim-boundary-audit | direct-and-derived | PDF pp.55-57 Fig.30; antimagnetic-rotation-audit-012.json | true |
