---
type: source
title: "Hübel 2005 - Magnetic rotation in nuclei"
aliases: [Hübel 2005 magnetic rotation review]
created: 2026-09-20
updated: 2026-11-27
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
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/review/2005_Hübel_Magnetic rotation in nuclei.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/review/2005_Hübel_Magnetic rotation in nuclei.pdf"
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
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/review/2005_Hübel_Magnetic rotation in nuclei.pdf`。

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

## 2026-11-27 — 馆藏原件与覆盖核对

- {"from": 1, "to": 12, "sections": "刊头、摘要、目录、§§1–2 引言与高自旋谱学、§3 开头"}
- {"from": 13, "to": 24, "sections": "§3.1–3.2 Pb 与轻质量区谱学、§4 DSAM 与 RDM 方法"}
- {"from": 25, "to": 32, "sections": "§4.1–4.2 Pb 与轻质量区寿命结果、§5 开头"}
- {"from": 33, "to": 43, "sections": "§§5.1–5.2 磁偶极矩与电四极矩、§6.1 剪刀耦合主体"}
- {"from": 44, "to": 57, "sections": "§6.1 结尾、§§6.2–6.4 TAC、Pb 组态比较与带终止、反磁转动、§7.1 开头"}
- {"from": 58, "to": 65, "sections": "§§7.1–7.3 半经验剪刀几何、有效相互作用及核芯竞争、§8 开头"}
- {"from": 66, "to": 69, "sections": "§8 总结余文、致谢、参考文献[1]–[106]"}
- 本次获取的具体覆盖：逐页核读所供物理第1–69页文本，包括各节正文、图1–53的图注、表1的提取文本、编号公式、致谢和文献[1]–[106]。所供文本中各图图注齐备，图内点位、误差棒和标记未作视觉核验。建议接受既有记录的同版全文文本覆盖，科学主张按本回执勘误，关键图证待管理者复核。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A21-1 | 综述所列 Pb 磁转动带的强 ΔI=1 M1 级联伴有很弱或未检出的 E2 跨越跃迁。所选 Pb 带由 DSAM 或 RDM 寿命结合分支比导出的 B(M1) 较大，沿带随跃迁能量或自旋升高而下降。⁸⁴Rb 的带头附近也报告较大 B(M1)，并有小 B(E2)。 | 综述转述的谱学观测与寿命推导 | source-reported | 物理第4–5页图2及正文，第18–20页图15–17与多极性、宇称判定，第25–27页图22–24，第28–29页图25–26及正文。 | true |
| A21-2 | ¹⁹³Pb 带1的 2584 keV、29/2− 带头由 TDPAD 得到 g=0.68(3)，另一项 TDPAD 四极相互作用分析得到 &#124;Qₛ&#124;=2.84(26) b。四极拟合只利用调制比振幅的首次下降，所报误差未包含可能的系统不确定度。 | 综述转述的静态矩测量 | source-reported | 物理第33–35页 §5.1、图31–32，第36–38页 §5.2.1、图34（第37页）。 | true |
| A21-3 | 综述报告 ¹⁰⁶Cd 最低正宇称带观察到 ΔI=2 E2 级联，由 DSAM 线形拟合寿命导出的小 B(E2) 随自旋下降。第57页称 J⁽²⁾ 近似恒定，因此 J⁽²⁾/B(E2) 在此例很大且随自旋上升。逐点数值、误差棒和高自旋端的覆盖须看第32页图30。 | 综述转述的寿命推导与个案趋势 | source-reported | 物理第29–32页 §4.2、图30（第32页），第56–57页 §6.4，文献[33]。 | true |
| A21-4 | 磁转动模型以高 j 粒子和空穴逐步对齐解释自旋增长及横向磁矩减小，弱变形核芯仍可贡献角动量。TAC 用倾斜轴解比较 Pb 的能量、对齐和带交叉。半经验模型用两片近似定长的剪刀及正 V₂ 的 P₂ 型粒子–空穴相互作用拟合带内能量，¹⁹⁷Pb 带2的例子给出 V₂=1.35 MeV。 | 模型解释与半经验拟合 | source-reported | 物理第42–43页图38及正文，第44–46页式(1)–(16)，第47–55页图40–48、表1，第57–62页式(17)–(23)、图49、51–52。 | true |

综述中的数值沿用所引实验或拟合。[50]–[55]支撑 Pb 寿命，[32]支撑 ⁸⁴Rb，[33]支撑 ¹⁰⁶Cd 寿命，图30另引私人通信[42]。[65]给出 ¹⁹³Pb 带头 g 因子，综述第35页的 g_calc=0.71(4) 来自候选组态的磁矩可加性估算。[66]给出该带头的 |Qₛ|，其负号及弱扁形解释来自 TAC 比较。¹⁹⁶Pb 组态表依据[36]，半经验相互作用分析主要沿用[37]及[97]–[99]。

- 替换 HU05-D19-1 和 HU05-D21-1 的双剪刀表述。物理第55–56页 §6.4 描述两个 g₉/₂ 质子空穴分别参与两套剪刀耦合。理想几何下横向磁矩近乎相消，模型具有绕总角动量轴旋转 180° 的对称性。¹⁰⁶Cd 个案的实验表述为未观察到 M1 跃迁。两条旧记录中的严格零值应撤回。
- 撤回向综述归属的两套剪刀角、0.407→0.0198 e²b²、20.5 倍降幅、54.1→约1110 的比值、24⁺ 严格归零和发散定理。物理第56页叙述叶片从 I=16 向 I≈26 闭合，TAC 给出形变趋近零，并将约 I=26 表述为可能的带终止。第57页的“大于100”是此例描述。第32页图30的惯量插图给出 J⁽²⁾ 对转动频率关系，逐点强度及其来源待查。同版文本支持寿命导出的 B(E2) 下降及反磁解释，综述明确指出当时该机制的实验基础较少。
- 将角度与公式分开著录。物理第46页式(16)采用 TAC 倾角 ϑ，其四次正弦因子与内禀四极矩同在一式。第57页式(18)和第58页图49采用单剪刀半经验模型的质子角 θπ，θ 表示两叶片夹角。两式均不支持旧记录将 ¹⁰⁶Cd 寿命结果写成已验证的 sin⁴θ 定律。第56页具体中子组态的上下标和括号提取错位，精确转录待核该页。
- 将跃迁强度综述句限定到相应核素与观测量。物理第27页图23–24为 Pb 的 B(M1)，第28页图25–26为 ⁸⁴Rb 的 B(M1) 和 B(E2)，第31页图28为 ¹¹⁰Cd 的自旋及 B(M1)，第32页图29为 ¹⁴²Gd 的 B(M1)。¹⁰⁶Cd 另见第32页图30。¹⁹³Pb 的四极测量著录为 |Qₛ|，扁形归入模型解释。图31–34实际分布在物理第34–37页，图36–37位于第40页。
- 将约2.3 MeV著录为物理第62–63页所述有效相互作用能标，约400–600 keV为按质子–中子对数折算的量。式(23)的归一化比值无量纲。第58页正文称图50为 ¹⁹⁸,¹⁹⁹Pb，第59页图注写 ¹⁹⁷,¹⁹⁸Pb，引用具体核素前核第59页图内标记。
- 精确转录前核查排版和内部歧异。物理第44页式(1)–(2)的撇号及期望值记号有乱码，第45页式(8)后有关 ΔI=1 的 ϑ=90° 字样疑失不等号，第49页明确叙述所讨论剪刀带的倾角远离 90°。具体组态以物理第48页图42图注的 ABC 和第55页表1所列带1的 ABCE11 为对照，保留第48页正文的 ABCD 与第53页终止段 ABE11 的异文待核。第68页文献[55]的提取文章号 0664314 也待核原页。
