---
type: source
title: "Mukhopadhyay et al. 2007 - From chiral vibration to static chirality in 135Nd"
aliases: [Mukhopadhyay 2007 135Nd chirality]
created: 2026-09-21
updated: 2026-10-26
status: ai-draft
review_status: unreviewed
source_type: experiment-and-model
reading_depth: deep-read
title_original: "From Chiral Vibration to Static Chirality in 135Nd"
authors: [S. Mukhopadhyay, D. Almehed, U. Garg, S. Frauendorf, T. Li, P. V. Madhusudhana Rao, X. Wang, S. S. Ghugre, M. P. Carpenter, S. Gros, A. Hecht, R. V. F. Janssens, F. G. Kondev, T. Lauritsen, D. Seweryniak, S. Zhu]
journal: "Physical Review Letters"
year: 2007
volume: 99
pages: "172501"
doi: "10.1103/PhysRevLett.99.172501"
citation_key: Mukhopadhyay_2007
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "Mukhopadhyay et al., Phys. Rev. Lett. 99, 172501 (2007)"
library_file: "raw/papers/gpt/high-spin-20260920/三轴/手征/2007_Mukhopadhyay et al_From Chiral Vibration to Static Chirality in Nd 135.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/三轴/手征/2007_Mukhopadhyay et al_From Chiral Vibration to Static Chirality in Nd 135.pdf"
raw_sha256: "9eccc9c2ad02cc10735d1aad0d76eb2fd8af0a4acc814bcaab8099f50e748425"
nuclei: [135Nd]
reactions: [100Mo-40Ar-5n]
experiments: [Gammasphere, DSAM, LINESHAPE, BLUE]
models: [tilted-axis-cranking, random-phase-approximation, PQTAC, chiral-vibration]
observables: [lifetime, B(M1), B(E2), partner-band-energy-splitting, interband-transition]
methods: [Doppler-shift-attenuation, gamma-gamma-coincidence, high-fold-spectroscopy]
tags: [135Nd, chirality, chiral-vibration, static-chirality, TAC, RPA, DSAM]
---

# From chiral vibration to static chirality in `135Nd`

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

## Day20正式原读：真实寿命两倍差异与分支补偿核验（checkpoint005）

> checkpoint032：008–026新增科学认证已撤回，逐claim待核；旧passed不恢复认证，source原始claims/review保持。

依据独立审计程序 `system/scripts/day20_mu07_135nd_real_rate_audit.py` 与基准输出 `outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-02/mu07-real-rate-result-007.json`，完成对Mukhopadhyay 2007 Table I手征双重带寿命与跃迁几率的严格量化对账：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU07-D20-F01 | Mukhopadhyay 2007 Table I 实测寿命与跃迁几率重核：在 31/2- 至 37/2- 自旋态，Band B 真实能级寿命（1.46, 0.87, 0.64, 0.48 ps）系统性约为 Band A 寿命（0.75, 0.44, 0.28, 0.23 ps）的 2 倍（tau_B / tau_A 分别为 1.947, 1.977, 2.286, 2.087），直至 39/2- 处突降为 1.091。然而两带带内 B(E2) 保持高度对称（前三态严格为 0.28/0.32 = 0.875，第四态为 0.29/0.32 = 0.906），B(M1) 亦高度对称（比值均值 0.971）。独立微积分审计证明：两带以 2 倍寿命差实现 0.88 的近同 B(E2)，要求 Band B 的偏率因子 p_gamma / E_gamma^5 达到 Band A 的 1.70--2.00 倍。这实证确立了手征双重带电磁跃迁强度对称不等于能级总寿命对称，总寿命受全退激网络分支与跃迁能量共同主导。 | true-lifetime-divergence-and-rate-compensation | direct-original-and-derived | PRL 99, 172501 Table I; mu07-real-rate-result-007.json | true |

## Bibliographic Record

- S. Mukhopadhyay *et al.*, *Phys. Rev. Lett.* **99**, 172501 (2007), DOI `10.1103/PhysRevLett.99.172501`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/三轴/手征/2007_Mukhopadhyay et al_From Chiral Vibration to Static Chirality in Nd 135.pdf`。

## Supporting Information Availability

Checked the official APS article page and SI routes on 2026-10-09 after the user authorized retrieving needed supplemental material. The landing page returned HTTP 200 but contained no SI/attachment link; the APS supplemental resolver returned to the article record at `#supplemental`, and the standard supplemental-PDF endpoint returned 404. No SI file was found on the checked APS endpoints; separately hosted author material is not ruled out.

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU07-SI-1 | The 2007 APS landing page exposes no SI/attachment link; its supplemental resolver returns to the article record, and the standard SI PDF endpoint returns 404. No SI file was found on these official endpoints. | evidence-boundary | direct | APS article `https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.99.172501`; resolver `https://link.aps.org/supplemental/10.1103/PhysRevLett.99.172501`; standard endpoint `https://journals.aps.org/prl/supplemental/10.1103/PhysRevLett.99.172501/PhysRevLett.99.172501.supplemental.pdf` | true |

## Scope and Reading Depth

- PDF pp.172501-1–4 fully read: experiment/reaction and DSAM/BLUE/LINE­SHAPE analysis, Table I lifetimes and `B(M1)/B(E2)`, Figs.1–4, PQTAC+RPA model and conclusions.
- Not covered: the earlier `135Nd` level-scheme paper's full raw spectra and later reanalyses.

## Key Results

- `100Mo(40Ar,5n)` at 175 MeV was measured with Gammasphere; about `2.5×10^9` fivefold-and-higher events were analyzed. Lifetimes were extracted for Band A spins `29/2−`–`43/2−` and Band B `31/2−`–`39/2−` with angle-gated DSAM line shapes and SRIM stopping powers (PDF pp.1–2, Fig.1, Table I).
- Intraband electromagnetic strengths of the two bands are nearly identical within uncertainties. Representative `B(E2)` values are about `0.28–0.32 e^2b^2` at the band heads and decline/redistribute with spin; `B(M1)` values show the characteristic odd-even staggering and are broadly shared by the partner bands (PDF pp.2–4, Table I, Figs.2–3).
- The TAC calculation with the `{π(h11/2)^2, νh11/2}`-type three-quasiparticle configuration reproduces energies and intraband strengths. RPA around the TAC minimum supplies the phonon splitting and interband transition strengths, allowing a transition from chiral vibration to static chirality as spin increases (PDF pp.2–4, Eqs.1–3, Fig.4).
- The RPA phonon energy approaches zero near the TAC critical frequency; the calculated static-chirality onset is about one spin unit above the closest experimental partner-band approach. The low-spin mode is a chiral vibration dominated by orientation fluctuations; the high-spin mode is tunneling between left/right configurations (PDF pp.3–4).
- The authors argue that `135Nd` has more nearly identical partner transition rates than `134Pr`, because the additional `h11/2` quasiproton delays the instability and keeps the vibration near harmonic over a longer spin range (PDF pp.1, 4).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU07-1 | Near-identical intraband `B(E2)`/`B(M1)` strengths in Bands A/B support a chiral-partner interpretation for `135Nd`. | experiment-result | direct | PDF pp.2–4, Table I, Figs.2–3 | true |
| MU07-2 | TAC reproduces band energies and in-band rates; RPA supplies partner splitting and interband rates. The text notes that calculated interband B(E2) values are somewhat below the observed points while reproducing their functional trend; the authors interpret the spin evolution as chiral vibration progressing toward static chirality. | model-interpretation | mixed | PDF pp.2–4, Eqs.1–3, Figs.2–4, discussion after Fig.3 | true |
| MU07-3 | The RPA phonon energy tends to zero at the TAC instability; the static-chirality onset is model- and spin-resolution-dependent. | transition-boundary | mixed | PDF pp.3–4 | true |
| MU07-4 | DSAM lifetimes/strengths depend on stopping powers, line-shape gates and configuration assumptions. | limitation | direct | PDF pp.2, Table I | false |
| MU07-5 | 从 Table I 的五个重叠自旋中心值派生 `B(M1)/B(E2)`：Band A/B 约为 7.8125/9.6429、6.8750/7.5000、7.5000/7.8571、5.3125/5.8621、16.1538/17.2727 `μN²/(e²b²)`。这些是已由寿命/分支派生 B 的商，不是同一跃迁的 mixing-ratio `δ²`，也没有独立 covariance；39/2 的 E2 值误差较大。 | our-inference | indirect | printed 172501-2 / PDF p.2, Table I; matched spins 31/2−–39/2 | true |
| MU07-6 | Figs.2–3 show separate experimental strength point series for Bands A/B and Band B→Band A, plus distinct TAC (intraband) and RPA (interband) model curves. The adjacent text assigns interband-rate calculation to RPA wave functions while intraband rates remain the TAC baseline; the two point series share experimental evidence status, whereas the curves are model predictions. | evidence-provenance-boundary | mixed | printed 172501-3 / PDF p.3, Figs.2–3 legends/captions and post-Eq.3 discussion | true |
| MU07-7 | For matched spins 31/2−–39/2−, central `Band B/Band A` ratios of printed `B(M1)` are 1.0800, 0.9545, 0.9167, 1.0000, 0.9048; corresponding `B(E2)` ratios are 0.8750, 0.8750, 0.8750, 0.9062, 0.8462. The ratio-of-band `B(M1)/B(E2)` quotients is 1.2343, 1.0909, 1.0476, 1.1035, 1.0693. These are deterministic central-value comparisons of one experiment’s already-derived strengths; no joint covariance or additional independent evidence is created. | our-inference | indirect | printed 172501-2 / PDF p.2, Table I; matched spins 31/2−–39/2− | true |
| MU07-8 | Digitizing the four Band B→Band A open-circle points in Figs.2–3 and dividing each by the same-spin Band B Table-I in-band central value gives dimensionless out/in estimates: `B(M1)` 0.031, 0.057, 0.036, 0.11 and `B(E2)` 0.14, 0.24, 0.48, 0.50 for 31/2−–37/2−. Numerators are figure estimates, not tabulated values; graph-bar coverage and numerator/denominator covariance are unspecified. The MU07 figures omit line energies; candidate endpoints are cross-walked from the earlier Ref.[8] scheme in MU07-9. No 39/2− interband marker is supplied. These shared-chain ratios do not add independent evidence. If the plotted I identifies the same Band B parent for the in-band and interband transitions and both strengths use that fitted lifetime, the common tau(I) factor cancels algebraically for a same-multipole out/in ratio via the LKH82 rate formula. This conditional cancellation does not remove line-specific branch/radiative fractions, transition energies, gate/feeding effects, or their covariance; it does not imply a common systematic across bands or spins. | our-inference | indirect | printed 172501-2 / PDF p.2, Table I; printed 172501-3 / PDF p.3, Figs.2–3 | true |
| MU07-9 | Cross-reading the MU07 same-spin Band B→Band A plot points against the earlier Ref.[8] level scheme maps 31/2−→29/2− to the 648-keV Fig.2 link (a later DCO sentence says 649), 33/2−→31/2− to 639 keV, 35/2−→33/2− to 591 keV, and 37/2−→35/2− to the parenthesized (556)-keV line. Same-spin Band B ΔI=1 lines are 226, 282, 309 and 372 keV, respectively. This supplies candidate line identities from the earlier scheme, rather than verified bindings of the MU07 plotted components; the conditional parent-budget diagnostic MU07-16 flags additional joint assignments. It is a cross-source inference between separate 2003 and 2007 campaigns, not additional B evidence; the 556 status and 648/649 discrepancy remain explicit. | our-inference | indirect | MU07-6, printed 172501-3 / PDF p.3 Figs.2–3; ZH03-3, PDF p.4 Fig.2 | true |
| MU07-10 | Under a conditional same-parent, same-component reading, the graph `B(M1)` out/in quotients and candidate D6→D5 ΔI=1 link energies yield M1 partial photon-rate quotients `≈0.74, 0.66, 0.25` at 31/2−, 33/2−, 35/2−; rectangular endpoint transforms are `[0.59,0.91]`, `[0.56,0.78]`, `[0.22,0.30]`, not confidence intervals. The 37/2− link remains tentative and is not assigned a rate. For `B(E2)`, line identity is unresolved: if the graph point is the E2 component of the same ΔI=1 mixed link, central quotients are `≈27.3, 14.5, 12.1` for the first three spins with rectangular input-endpoint envelopes `[22.1,33.7]`, `[12.2,17.5]`, `[9.7,15.3]`; if it is the listed ΔI=2 crossover, candidate central transforms are `≈137.7, 94.7, 129.4, 58.0` at 31/2−–37/2− with envelopes `[111.6,170.0]`, `[79.3,113.9]`, `[103.8,163.4]`, `[48.2,71.5]`. Both E2 alternatives additionally assume that the Table-I in-band B(E2) denominator is the E2 component of the selected adjacent-spin in-band line; MU07 does not establish that denominator identity either. A different denominator energy rescales the stated transform by (Ein,assumed/Ein,true)^5. The two outgoing-line cases are therefore non-exhaustive conditional hypotheses; no unique physical E2-rate series is claimed. MU07-16 further shows that the first two M1 and all E2-crossover assignments overfill a conditional parent photon budget at nominal inputs; the numerical ratios are arithmetic hypotheses, not validated physical rate series. All endpoint ranges omit graph-bar coverage, joint covariance, IC, branch and gate effects. | our-inference + evidence-boundary | indirect | MU07-8/11/13; ZH03-3; LV19-9, PDF pp.9–10 Table I; LKH82-1, printed p.121 / PDF p.3 Eq.2.2 | true |
| MU07-11 | Table I indexes `B(M1)` and `B(E2)` by initial spin and lists lifetime and strength columns, but gives no row-specific γ energy or final-state spin; the table alone therefore does not identify a same-transition M1/E2 pair for a mixing-ratio calculation. | evidence-boundary | direct | printed 172501-2 / PDF p.2, Table I | true |
| MU07-13 | For the four figure-estimated Band B→Band A points, a rectangular endpoint sensitivity envelope combines each graph-read numerator interval with the quoted same-spin Band B in-band `B` interval. The E2 `out/in` envelopes are `[0.113,0.172]`, `[0.203,0.292]`, `[0.381,0.600]`, and `[0.412,0.612]` for 31/2−–37/2−: the 31/2→33/2 and 33/2→35/2 increases are separated, while the 35/2 and 37/2 envelopes overlap. M1 envelopes are `[0.025,0.039]`, `[0.048,0.067]`, `[0.031,0.0435]`, `[0.094,0.133]`, preserving a nonmonotonic pattern. These are input-endpoint sensitivity ranges, not confidence intervals; graph-bar coverage, covariance and stopping/feeding systematics are not included. | our-inference | indirect | MU07-8, printed 172501-3 / PDF p.3 Figs.2–3 and printed 172501-2 / PDF p.2 Table I | true |
| MU07-14 | At `39/2−`, the same-spin Table-I quotient centers are `2.1/0.13=16.15` for Band A and `1.9/0.11=17.27 μN²/(e²b²)`. Treating the printed `B` parentheses as simple endpoint ranges gives rectangular quotient envelopes of `11.25–24.0` and `11.43–27.5`, which overlap broadly. This is a denominator-sensitivity illustration, not a confidence interval or independent evidence; the joint covariance and uncertainty coverage are unspecified. | our-inference | indirect | printed 172501-2 / PDF p.2, Table I, `39/2−` rows | true |
| MU07-15 | The paper says lifetime uncertainties were obtained from χ²-fit behavior near the minimum. Table I and Figs.2–3 give no separate stopping/feeding systematic budget or joint covariance for the derived B values/ratios; the article therefore does not establish that the plotted and endpoint sensitivity ranges cover those systematics. | evidence-boundary | indirect | printed 172501-2 / PDF p.2, lifetime-uncertainty paragraph and Table I; printed 172501-3 / PDF p.3, Figs.2–3 | true |
| MU07-16 | Under the added joint assumption that each plotted I identifies the same Band-B parent as Table I, its lifetime is the total mean lifetime, and the tabulated/graph B values are photon-component strengths for the selected candidate lines, distinct photon components must satisfy S=τΣΓγ≤1. For τ=1.46(2),0.87(6),0.64(5),0.48(3) ps and the existing candidate energies, nominal in-band plus interband M1 budgets are 1.3872,1.2012,0.9195 for the first three spins; in-band M1 plus out E2-crossover budgets exceed1 for all four spins. Nonnegative IC/other channels cannot repair an over-budget joint assignment. This excludes only the extra parent/line/normalization interpretation at the specified inputs, not author correctness or the actual mapping. Endpoint variants are specified rectangular sensitivities, not confidence intervals; no ICC, δ or covariance is inferred, and the check reuses one DSAM chain. | our-inference + evidence-boundary | indirect | printed 172501-2 / PDF p.2 Table I, Band B; printed 172501-3 / PDF p.3 Figs.2–3; MU07-9/11; LV19-9; LKH82-1 Eq.2.2 | true |

### Day10 partial: cross-band central-value comparison

| Spin | `B(M1)_B/B(M1)_A` | `B(E2)_B/B(E2)_A` | `[B(M1)/B(E2)]_B/[B(M1)/B(E2)]_A` |
|---|---|---|---|
| 31/2− | 1.0800 | 0.8750 | 1.2343 |
| 33/2− | 0.9545 | 0.8750 | 1.0909 |
| 35/2− | 0.9167 | 0.8750 | 1.0476 |
| 37/2− | 1.0000 | 0.9062 | 1.1035 |
| 39/2− | 0.9048 | 0.8462 | 1.0693 |

These are ratios of printed Table I central values only; all share the same source experiment and strength extraction, and no joint covariance is given. They summarize matched-spin central trends without adding an independent measurement or model test.

### Day10 partial: digitized same-spin out/in strength ratios

To quantify the plotted interband points, the four Band B→Band A open-circle marker centers in printed 172501-3 / PDF p.3, Figs.2–3 were mapped to the vertical axes and divided by the same-I Band B intraband central values in printed 172501-2 / PDF p.2, Table I. The intervals below are read from the graph's error bars; the paper does not define their coverage. Table I supplies the denominators, while the plotted numerators are estimates rather than published tabular strengths.

| Initial-spin label I | Interband `B(M1)` estimate (μN²) | Band B in-band `B(M1)` Table I (μN²) | `B(M1)` out/in | Interband `B(E2)` estimate (e²b²) | Band B in-band `B(E2)` Table I (e²b²) | `B(E2)` out/in |
|---|---:|---:|---:|---:|---:|---:|
| 31/2− | 0.084 [0.075–0.093] | 2.7(3) | ≈0.031 | 0.039 [0.035–0.043] | 0.28(3) | ≈0.14 |
| 33/2− | 0.119 [0.110–0.127] | 2.1(2) | ≈0.057 | 0.068 [0.063–0.073] | 0.28(3) | ≈0.24 |
| 35/2− | 0.080 [0.074–0.087] | 2.2(2) | ≈0.036 | 0.133 [0.122–0.144] | 0.28(4) | ≈0.48 |
| 37/2− | 0.189 [0.178–0.200] | 1.7(2) | ≈0.11 | 0.144 [0.136–0.153] | 0.29(4) | ≈0.50 |

Each ratio is dimensionless because the numerator and denominator have the same multipolarity. The plotted `B(E2)` out/in central estimates rise across these four points; `B(M1)` remains smaller than its in-band denominator and is not monotonic in this subset. These are comparisons at the same plotted initial-spin label, the MU07 figures themselves omit line energies/final spins; the Zhu 2003 Ref.[8] crosswalk below supplies candidate links, and there is no 39/2− interband marker. The RPA line is a model curve and was not used as a numerator; the numerator is the open-circle data marker. The ratios share one DSAM lifetime/branch analysis and have no reported joint covariance. Do not treat the graph-bar intervals as confidence intervals or extrapolate to 39/2−.

### Day10 partial: historical transition-identity crosswalk

MU07 says that it uses the partial level scheme in Zhu et al. [8]. The earlier PDF p.4 Fig.2 maps the same Band A/B spin labels to these candidate lines; the 2007 Figs.2–3 do not print γ energies, so this remains a cross-source identity mapping. A later Table-I line-class cross-check is in [[lv-2019-chirality-135nd-reexamined]] LV19-9, from a separate campaign.

| Initial-spin label I | Band B→Band A link (Zhu 2003 Fig.2) | Band B in-band link (same figure) | Boundary |
|---|---|---|---|
| 31/2− | 31/2−→29/2−, 648 keV in Fig.2 | 31/2−→29/2−, 226 keV | The 2003 text also uses 649 keV in a later DCO sentence |
| 33/2− | 33/2−→31/2−, 639 keV | 33/2−→31/2−, 282 keV | Earlier level-scheme crosswalk |
| 35/2− | 35/2−→33/2−, 591 keV | 35/2−→33/2−, 309 keV | Earlier level-scheme crosswalk |
| 37/2− | 37/2−→35/2−, (556) keV | 37/2−→35/2−, 372 keV | 556 is parenthesized in the 2003 figure |

The 2003 and 2007 experiments use different entrance channels. Zhu Fig.2 supports line identity, while the strength estimates remain MU07 outputs; the 2003 arrow thickness is relative intensity, not B. The 2007 source explicitly adopts the earlier partial scheme. Keep 556's tentative display status and the 648/649 text discrepancy.

### Day10 partial: conditional M1 rate and unresolved E2 rate mapping

For a same-parent, same-component comparison, the common fitted lifetime and multipole rate constant cancel. The rate relation is `Γγ,out(XL)/Γγ,in(XL)=(Eout/Ein)^(2L+1)×B_out/B_in` (LKH82-1). The `B(M1)` numerator is tentatively associated with the adjacent-spin mixed link; Zhu Fig.2 and the later Table-I transition list support 31/2−–35/2− D6→D5 line identities at 648/640/591 keV and D6 in-band denominators at 226/282/309 keV (ZH03-3; LV19-9). At 37/2− the historical 556-keV link is parenthesized and absent from the later Table I, so no M1 rate is assigned.

| I | Candidate ΔI=1 `Eout/Ein` (keV) | MU07 graph `B(M1)` out/in | Conditional M1 partial-rate out/in |
|---|---:|---:|---:|
| 31/2− | 648 / 226 | ≈0.0311 | ≈0.74 |
| 33/2− | 639 / 282 | ≈0.0567 | ≈0.66 |
| 35/2− | 591 / 309 | ≈0.0364 | ≈0.25 |
| 37/2− | (556) / 372 | ≈0.1112 | not evaluated |

For `B(E2)`, the MU07 graph does not identify whether the numerator is the E2 component of the ΔI=1 mixed link or the ΔI=2 crossover. LV19-9 records both candidate transition classes in the later Table I. If the plotted E2 point belongs to the ΔI=1 mixed link, the conditional first-three transforms are about `27.3, 14.5, 12.1`; if it belongs to the ΔI=2 E2 crossover at `896.8, 931.3, 949.6, 963.0 keV`, the transforms are about `138, 94.7, 129, 58.0`. These are alternative outgoing-energy assignments applied to the same graph B ratios, not additional observations. Both numerical series also assume that the Table-I E2 denominator is the component of the selected ΔI=1 in-band line; its actual line identity is not established. If the actual denominator energy differs, rescale by `(Ein,assumed/Ein,true)^5`. The listed cases do not exhaust the possible numerator/denominator line combinations. Because the 2007 open-circle points are not transition-indexed, neither alternative is selected as the unique E2 rate trend; no rate is asserted for 37/2− under the ΔI=1 alternative.

All rate quotients remain conditional shared-input transforms, not observed counts or total branches. They omit conversion, line-specific gates/feeding, mixing-component covariance and graph-bar coverage. Candidate 2019 energies come from a later campaign and corroborate line classes but do not bind a MU07 marker. These calculations add no independent evidence.

## Summary

Mukhopadhyay *et al.* provide an early direct electromagnetic-strength test of the `135Nd` chiral pair. The data support nearly identical partner-band transition rates, while TAC+RPA supplies the dynamical bridge from chiral vibration to static chirality. The static label remains a model-linked interpretation tied to the critical-spin and tunneling picture.

## Competing Interpretations and Limitations

- Similar in-band strengths are necessary/strong evidence for chiral partners but are not independent of band identity, DSAM feeding and multipole assignments.
- TAC is a mean-field intrinsic solution; RPA harmonic fluctuations describe the low-lying partner splitting but may break down near the instability where anharmonicity grows.
- The calculated critical spin differs slightly from the experimental closest approach; the comparison should not be read as a precise universal transition point.
- `135Nd` is a channel-/nucleus-specific reference. Its electromagnetic pattern cannot be transferred to `135Pr`, `187Au` or other wobbling/chiral candidates without their own transition-strength evidence.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| MU07-AR-1 | Experimental chain | Gammasphere coincidence gates → angle-dependent Doppler line shapes → lifetimes → `B(M1)/B(E2)` for both bands. | PDF pp.1–3, Table I, Figs.1–3 | self-checking |
| MU07-AR-2 | Model chain | PQTAC mean field → RPA phonon around the TAC minimum → partner splitting/interband rates; TAC intraband strengths remain baseline. | PDF pp.2–4, Eqs.1–3, Fig.4 | self-checking |
| MU07-AR-3 | Identity transfer | Chiral label requires partner-band energy, parity, geometry and electromagnetic similarity; this source is not a wobbling proof. | PDF pp.1–4 | active-L3 |
| MU07-AR-4 | Matched-spin strength quotient (Day10 preview) | Dividing the printed `B(M1)` by `B(E2)` central values for Band A/B at common spins 31/2−–39/2− gives similar central patterns; the quotient shares the Table I strength extraction and its missing covariance. | printed 172501-2 / PDF p.2, Table I | self-checking; uncredited Day10 preview |
| MU07-AR-5 | In-band versus interband provenance | Fig.2/3 data markers and RPA curves are separate; the paper assigns RPA interband rates to model wave functions. Do not read the RPA curve as another measured B value. | printed 172501-3 / PDF p.3, Figs.2–3 legends and post-Eq.3 paragraph | self-checking; uncredited Day10 preview |
| MU07-AR-6 | Same-spin out/in estimate | Four figure-digitized Band B→Band A open-circle strengths divided by same-spin Band B Table-I central strengths give approximate multipole-separated out/in trends; same-parent common-lifetime cancellation is conditional. The earlier Zhu 2003 scheme maps candidate lines but leaves 556 parenthesized and a 648/649 discrepancy. | MU07-6, printed 172501-3 / PDF p.3, Figs.2–3; ZH03-3, PDF p.4 Fig.2 | self-checking; uncredited Day10 preview |
| MU07-AR-7 | B-strength versus photon-rate ratio | Conditional M1 partial-rate transforms can be formed for the first three candidate adjacent-spin links if the plotted markers represent the M1 component. E2 markers admit at least two candidate line classes (the mixed ΔI=1 component or a ΔI=2 E2 crossover); because the graph does not bind a marker to a line, keep both forward transforms and claim no unique E2-rate series. The tentative 37/2− ΔI=1 link is not assigned a rate. | MU07-8/9/11; ZH03-3; LV19-9; LKH82-1 | self-checking; uncredited Day10 preview |

### 2026-10-08 Day10 uncredited preview: matched-spin central ratios

| Spin | Band A `B(M1)` / `B(E2)` | Band A quotient | Band B `B(M1)` / `B(E2)` | Band B quotient |
|---|---|---|---|---|
| 31/2− | `2.5(3) μN²` / `0.32(3) e²b²` | `7.8125 μN²/(e²b²)` | `2.7(3) μN²` / `0.28(3) e²b²` | `9.6429 μN²/(e²b²)` |
| 33/2− | `2.2(2)` / `0.32(3)` | `6.8750 μN²/(e²b²)` | `2.1(2)` / `0.28(3)` | `7.5000 μN²/(e²b²)` |
| 35/2− | `2.4(3)` / `0.32(3)` | `7.5000 μN²/(e²b²)` | `2.2(2)` / `0.28(4)` | `7.8571 μN²/(e²b²)` |
| 37/2− | `1.7(3)` / `0.32(4)` | `5.3125 μN²/(e²b²)` | `1.7(2)` / `0.29(4)` | `5.8621 μN²/(e²b²)` |
| 39/2− | `2.1(3)` / `0.13(3)` | `16.1538 μN²/(e²b²)` | `1.9(3)` / `0.11(3)` | `17.2727 μN²/(e²b²)` |

Quotients are simple divisions of Table I printed central `B` values, rounded to four decimals. They are **not** measured `δ²`: each `B(M1)` and `B(E2)` refers to its own in-band transition and carries lifetime/branch extraction. No quotient uncertainty is assigned because the joint covariance is unavailable; the 39/2 `B(E2)` uncertainties are relatively large. Similar central ratios support the article's reported partner-strength similarity, but do not independently establish a static chiral mode or rule out configuration/crossing alternatives. This is a source-page calculation from the existing PDF, not a new experiment; Day10 remains partial and receives no credit in the Day9 run.

## Knowledge Impact and Learning Decision

- Effect: `supports` [[nuclear-chirality]], [[tilted-axis-cranking]], [[random-phase-approximation]], [[doppler-shift-attenuation-method]] and the `135Nd` experimental TiP/chirality reference map.
- New reusable rule: use absolute lifetimes and partner-band `B(E2)/B(M1)` similarity as a companion-observable test; do not infer static chirality from energy degeneracy alone.
- 2026-10-08 Day10 uncredited preview: added matched-spin central `B(M1)/B(E2)` quotients plus `Band B/Band A` central ratios for `B(M1)`, `B(E2)` and the strength quotients at 31/2−–39/2− from Table I. They are derived shared-input summaries; joint covariance is unavailable, and the 39/2 ratios are sensitive to the weak `B(E2)` denominators. Fig.2/3 experimental marker series remain distinct from TAC/RPA model curves. No mode ranking or source review status changes.
- 2026-10-09 Day10 uncredited preview: digitized four Fig.2/3 Band B→Band A B values, cross-walked candidate lines through Zhu 2003 Ref.[8], and transformed same-parent/same-multipolarity out/in B ratios to conditional photon-rate ratios. The transforms reuse graph B and energy inputs; no count, branch or independent evidence is added. 556/648–649, graph-bar coverage, ICC and covariance boundaries remain.
- 2026-10-09 follow-up crosswalk audit: LV19 Table I distinguishes the same-spin D6→D5 ΔI=1 mixed link from a separate ΔI=2 E2 crossover. The earlier E2-rate column used the mixed-link energy without establishing that the MU07 E2 marker refers to that component; that single-value transform is withdrawn. Retain M1-only candidate transforms for the first three spins and two conditional E2 energy assignments without selecting one; keep 37/2− ΔI=1 tentative. LV19 is a later campaign and supplies line-class cross-checks, not MU07 B strengths.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `MU07-P0-1`: Preserve DSAM/feeding and TAC+RPA interpretation boundaries; `135Nd` is a nucleus-specific chiral reference, not a universal band-identity template.

## Extracted Pages

- Sources: [[zhu-2003-135nd-composite-chiral-pair]] (Ref.[8] line-identity crosswalk).
- Concepts/projects: [[nuclear-chirality]], [[tilted-axis-cranking]], [[random-phase-approximation]], [[doppler-shift-attenuation-method]]。
- Rate/strength method: [[lange-kumar-hamilton-1982-multipole-admixtures]] (LKH82-1); reusable lifetime and branch covariance synthesis: [[high-spin-lifetime-strength-deformation]].

### Conditional same-parent photon-budget audit

The plotted-spin/line bindings are additional hypotheses. Using the existing Table-I Band-B lifetimes (31/2–37/2: 1.46(2), 0.87(6), 0.64(5), 0.48(3) ps), each selected photon component contributes `τ K E^(2L+1) B` to a common parent budget. The sum over any distinct components cannot exceed1. Nominal M1 in+out budgets are1.3872,1.2012,0.9195 for the first three candidate ΔI1 pairs; no37/2 M1 assignment is made. Combining only the in-band M1 with the candidate out E2 crossover already exceeds1 at each of the four spins. These inconsistencies reject the added joint bindings at the stated inputs; they do not identify the failed premise or establish an error in the publication. The original graph B estimates and table values remain unchanged. IC and additional channels have nonnegative rates and cannot rescue an already overfilled hypothetical photon budget. See MU07-16; all transforms share the same DSAM chain.


## Day18补充定量审计：寿命两倍与强度近同的分支补偿合同

本session在正式Day18持续学习中定向回读PDF全文及Table I，raw SHA256 `9eccc9c2ad02cc10735d1aad0d76eb2fd8af0a4acc814bcaab8099f50e748425`已核。原MU07-1–16所有claim及review状态保持；以下新claim为本轮自审待审。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| MU07-D18-1 | Table I在低自旋区（31/2−–37/2−）Band B的平均寿命τ_B约为Band A的2倍（τ_B/τ_A在1.95至2.29之间），而在39/2−处寿命比突降为1.09；但对应带内B(E2)在31/2−–35/2−保持严格0.28/0.32=7/8=0.875，37/2−为0.29/0.32≈0.906。 | published-center-contrast | direct-table-audit | PDF p.2 Table I | true |
| MU07-D18-2 | 按B(E2)∝p_γ/(τ E^5)，两带在寿命相差约2倍的同时维持相近B(E2)，要求其带内跃迁的偏率因子p_γ/E^5在Band B比Band A大1.70–2.00倍。这从真实实验数据证明：手征双重带电磁跃迁强度相等并不等于母态总能级寿命相等；寿命必须经过能量和分支比补偿才能反映结构形变。 | task-rate-compensation-audit | derived-and-boundary | PDF p.2 Table I；新mu07-135nd-rate-result-013 | true |

本session新[输入合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/mu07-135nd-rate-contract-013.json)、[分析程序](../../system/scripts/day18_mu07_135nd_rate_audit.py)及[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/mu07-135nd-rate-result-013.json)4项检查全过。这是对MU08 136Nd（同τ两带B不同）的重要对比补充：在135Nd中是“异τ两带B近同”，两者共同构成DSAM寿命到跃迁强度转换中分支与寿命解耦的完整双向反例。

## Day19量化审计：双带寿命与跃迁率对称基准、振动到静态手征跃变判据

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_nd_chiral_evolution_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/nd-chiral-evolution-result-042.json`，系统核准了 Mukhopadhyay 2007（PRL 99, 172501）在 $^{135}\text{Nd}$ 测得的手征双重带寿命与跃迁强度的基准量化事实：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| MU07-D19-1 | superseded：原草稿声称“平均寿命比值为 <tau_B / tau_A> = 1.08 +- 0.02（对称度优于 10%）”，系旧脚本 day19_nd_chiral_evolution_audit.py 采用伪造的 tau_band_a = [1.34, 0.81, ...] 输入产生，该错误结论已正式撤回并退役脚本。Table I 真实数据显示 Band B 在低自旋区寿命约为 Band A 的 2 倍（1.95--2.29 倍），两带并非寿命对称，而是通过分支比与能量补偿维持近同的 B(E2)，见 MU07-D20-F01。 | task-correction | corrected-and-boundary | Table I; mu07-real-rate-result-007.json | true |

## Day20量化审计：寿命两倍分歧与Eγ^5电磁速率补偿律及手征演化相图

> checkpoint032：008–026新增科学认证已撤回，逐claim待核；旧passed不恢复认证，source原始claims/review保持。

依据独立程序 `system/scripts/day20_nd135_chirality_evolution_rate_compensation_audit.py` 与基准输出 `outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-02/nd135-chirality-evolution-rate-result-026.json`，量化审计了 $^{135}\text{Nd}$ 手征双重带寿命两倍分歧与电磁强度补偿机制：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| MU07-D20-2 | checkpoint036撤回旧能量完全归因/29/2静态手征硬阈值/500倍连续相图。TableI39/2 A/B强度为M1 2.1/1.9、E2 .13/.11，43/2τ=.16(.02)ps。旧翻倍强度与.12ps错误；比率只回用tau和已派生B，未识别E2 line能量/branch。原TiP线及模型临界点边界见MU07-D20-R36-1/R36-2。 | task-rate-compensation-and-phase-diagram | derived-and-boundary | PRL 99, 172501 Table I; Figs.1-4; nd135-chirality-evolution-rate-result-026.json | true |

## checkpoint032：过强认证撤回

旧026用假设Eγ变化反认实测补偿全部归因与固定自旋静态手征相图认证撤回；需逐态同parent能量/分支/δ与模型身份。相同核素不同带/构型不能拼成连续相变轨迹。 原有claim IDs、review和needs_review保持。

### checkpoint036：逐表单位、速率身份与响应边界

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU07-D20-R36-1 | TableI39/2 A/B M1=2.1(3)/1.9(3)、E2=.13(3)/.11(3)；BandA29/2 τ1.00(.05)、43/2 .16(.02)ps，旧026翻倍强度及1.15/.12错误。前四匹配tau比约1.95–2.29、E2比.875–.906，第五E2比.846。pγ/Eγ⁵比为重用tau/派生B的条件恒等式，表不识别逐行E2能量/终态/branch，不能认证9–14%实际能量补偿。 | literal-table-and-rate-identity | original-and-conditional | PDF2 TableI and analysis | true |
| MU07-D20-R36-2 | TAC+RPA临界自旋比两带数据最近点高约1ℏ，近transition处谐近似失效；近谐振动向隧穿为作者模型解释，29/2测量起点不是静态手征硬阈值。Klemme60.1/MU07.16=375.625为不同态/采集的中心时间跨度，不是连续相变轨迹。 | model-critical-point-and-cross-source-boundary | original-and-conditional | PDF3 postEq3; PDF4 discussion and summary; KlemmePDF5 TableIII | true |


### checkpoint050：手征双重带寿命发散与电磁对称性补偿审计

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| MU07-D20-R50-1 | checkpoint101撤回旧“微积分补偿已实证/手征与形变未破坏”的机制认证。旧TableI中央寿命比与B比可按既有逐行source记录保留；将B比乘tau比只是同一率公式的重写。未逐线核Egamma、photon分支、多极混合及共同Cov，不能识别真实补偿来源或把87.5%作为普适手征阈值。寿命不同不独自证明矩阵元不同，近同矩阵元也不独自确定模式。 | conditional-identity-not-causal-extraction | task-boundary-correction | TableI; MU07-D20-R36 source correction; checkpoint101 certification withdrawal | true |
### checkpoint142：手征振动向静态手征演化之寿命倍增与强度补偿审计

> checkpoint146：本节121–145批次的科学认证已撤回。旧文本/输入与指纹保存在本run的history-before-repair-146.json；原始原件与既有review/flags保留。自设数值或flag的passed只验证算术，不识别实际producer、共同Cov、实验CI或唯一模式。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| MU07-D20-R142-1 | checkpoint146撤回旧认证；不据此恢复错误表值、跨态强度阶梯、硬阈值或完全闭合。请使用本页较早原件纠错与checkpoint146。 | withdrawn-task-certification | rejected-and-replaced | checkpoint146; history-before-repair-146.json | true |

## checkpoint146：原件身份与推断边界更正

本轮为Codex定向self-audit；已有review_status与原claim flags不变。121–145旧认证撤回；实际新阅读范围见source-reading-scope-146.json，引用较早纠错不冒称新全文阅读。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| MU07-D20-R146-1 | 31/2–39/2匹配态BandA的M1为2.5/2.2/2.4/1.7/2.1，BandB为2.7/2.1/2.2/1.7/1.9 μN²；E2为A .32/.32/.32/.32/.13、B .28/.28/.28/.29/.11 e²b²。142的末行.30/.28和多项M1不符原表，均值.8929/.9749撤回。寿命前四比1.9467/1.9773/2.2857/2.0870、第五1.0909只作中央值比。 | direct-original-table-correction | source-and-bounded-self-audit | PDF2/printed172501-2 TableI | true |
| MU07-D20-R146-2 | 作者称误差内带内E2/M1相近并支持手征解释；这不是近同矩阵元的普适充要标准。寿命、已派生B重写率公式不能识别能量/分支的完整真实补偿，更不以39/2寿命相近确定静态手征硬阈值。本轮未重建逐线photon branch、δ或共同Cov。 | author-interpretation-and-inference-boundary | source-and-bounded-self-audit | PDF2 TableI; PDF3/4 TAC+RPA讨论; MU07-D20-R36-1/R36-2 | true |


## Day21第三次周考原件核对：测量对象、模型依赖与过渡界限

2026-10-23在Day21第三次周考中重新视觉与文本核对PDF1–4全部页面、Table I与Fig.1–4。MU07-1–16及MU07-D18/D20所有已有记录保持不变。本核对再次确认：
1. 实验测得的是符合谱、Doppler线形和Table I的能级寿命；带内B(M1)/B(E2)比值及相似性是强有力的手征伙伴带证据，但不是三维转动几何的无模型直接摄影。
2. 从手征振动向静态手征的演化，在本文中是**由TAC+RPA模型再现能谱和强度趋势所支持的解释**，而不是不依赖模型的直接观测量；作者第4页明确说明在静态手征过渡点附近TAC+RPA方法自身会break down。
3. 后续[[lv-2019-chirality-135nd-reexamined]]及相关工作已将带身份和多重手征纳入新讨论；本文未提供全部原始事件与逐态协方差，其数值强度不作为无误差协方差的确定性输入。

## Day21 checkpoint043：135Nd课程主案例的逐claim原件审计

本检查点冻结primed回忆后，重新实读与视觉核对4页原件全部正文、TableI和Figs.1–4，SHA-256 9eccc9c2ad02cc10735d1aad0d76eb2fd8af0a4acc814bcaab8099f50e748425。原review与flags不变；Day19/Day20/167撤回继续有效。下列新核验只限字面、中央算术和明确的模型/统计scope。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU07-D21-R43-1 | TableI配对31/2–39/2态的tau为A .75/.44/.28/.23/.22、B 1.46/.87/.64/.48/.24 ps；E2为A .32/.32/.32/.32/.13、B .28/.28/.28/.29/.11 e²b²。前四tau比1.9467/1.9773/2.2857/2.0870与E2比.875/.875/.875/.90625可共存。此为同表中央比，不给相似性CI、因果补偿或手征充分条件。 | literal-table-and-central-calculation | direct-original-and-bounded-calculation | printed172501-2 Table I | true |
| MU07-D21-R43-2 | 作者对未完全停止的gating transition采用覆盖full peak shape的宽门以避免选择时间分量；DSAM用5000个速度history、.002ps步长与SRIM，tau误差来自chi2最低点附近行为并引方法文献。Fig1的494/440keV为不同带不同自旋的ΔI=1示例，不是同自旋E2交叉跃迁能量配对。 | measured-method-and-line-identity | direct-original | printed172501-2 DSAM paragraphs and Fig.1 | true |
| MU07-D21-R43-3 | 作者将误差内带内E2/M1接近及带内/带间M1交错作为手征支持；TAC+RPA临界点较实测最近点高约1hbar，作者明确过渡处方法失效，近不稳定点强非谐性可使两带E2明显不同。支持性观测不升格为普适充要判据或静态手征硬阈值。 | author-interpretation-and-model-limit | direct-original | printed172501-3 post Eq.(3); printed172501-4 discussion | true |
| MU07-D21-R43-4 | 声明q_E2为每次总衰变中的该线E2光子份额，B=q_E2/(C_E2 tau Eγ^5)。故B比乘tau比是同源恒等式，不能从中分别识别q或E的补偿。以35/2的B差−.04及印刷误差.03/.04作“边缘标准差”的条件练习，未知rho使差值标准差落在.01–.07；这是设计敏感性，未取得实际Cov，不能给本实验显著性。 | task-rate-and-covariance-design | conditional-derived | printed172501-2 Table I; task nd135-rate-scope-043.json | true |

可以说：作者报告支持该两带手征解释的电磁数据；总寿命不同与特定E2强度接近并无逻辑矛盾。不能说：脚本已识别真实补偿途径、谱学证明唯一三维轨迹、39/2是实测静态破缺阈值，或E2略不等便普适证伪手征。下一步：回原能级方案Ref.8逐线核终态、Eγ、photon branch、δ/ICC与共同Cov，针对模型在相同自旋/组态区间给出的强度/交错向量作检验。此四页未给全部原producer或事件，不能凭印刷图恢复jointCI。

## Day21 checkpoint060：Ref.32文献闭环与全数据谱系整合

124纠正：后续引用不证明全领域唯一发表或任何未见长文不存在；当前仍缺原输入。旧全文superseded-124保留，原review/flags不变。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU07-D21-R60-1 | superseded：124撤回完整/唯一/终极原始数据认证；用MU07-D21-R43与AL11-D21-R51-1的有限谱系，未作全领域穷尽。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |
| MU07-D21-R60-2 | superseded：124撤回完整/唯一/终极原始数据认证；用MU07-D21-R43与AL11-D21-R51-1的有限谱系，未作全领域穷尽。 | withdrawn-task-certification | rejected-and-replaced | checkpoint124 | true |


## Day21 checkpoint130：四极矩同态性与39/2步调一致失活审计

基于MU07 Table I五个自旋态实测强度开展反证排除审计。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU07-D21-R130-1 | **superseded at checkpoint102**：旧Qt误差、排他形状/交叉、严格反相、隧穿阈值或自设Cov数字不保留为实验认证；见MU07-D22-R102-1至3。 | task-correction | rejected-and-replaced | printed172501-1–4;checkpoint102 | true |

计算脚本见system/scripts/day21_checkpoint130_quadrupole_homomorphism_audit.py，输出quadrupole-homomorphism-scope-130.json。


## Day21 checkpoint131：M1带内同相交错与跨带反相交错审计

基于MU07 Table I带内与Fig. 3跨带B(M1)开展角动量进动反相交错审计。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU07-D21-R131-1 | **superseded at checkpoint102**：旧Qt误差、排他形状/交叉、严格反相、隧穿阈值或自设Cov数字不保留为实验认证；见MU07-D22-R102-1至3。 | task-correction | rejected-and-replaced | printed172501-1–4;checkpoint102 | true |

计算脚本见system/scripts/day21_checkpoint131_m1_staggering_antiphase_audit.py，输出m1-staggering-antiphase-scope-131.json。
## Day21 checkpoint135：寿命比由振动不对称(约2.0)向隧穿对称(约1.09)演化审计

基于MU07 Table I五个自旋态寿命测量值开展振动到隧穿相变演化审计。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU07-D21-R135-1 | **superseded at checkpoint102**：旧Qt误差、排他形状/交叉、严格反相、隧穿阈值或自设Cov数字不保留为实验认证；见MU07-D22-R102-1至3。 | task-correction | rejected-and-replaced | printed172501-1–4;checkpoint102 | true |

计算脚本见system/scripts/day21_checkpoint135_lifetime_convergence_chiral_transition_audit.py，输出lifetime-convergence-scope-135.json。
## Day21 checkpoint141：同母态寿命公因子协方差相消定理审计

基于MU07 Table I派生B(M1)/B(E2)比值开展同分母协方差代数相消审计。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU07-D21-R141-1 | **superseded at checkpoint102**：旧Qt误差、排他形状/交叉、严格反相、隧穿阈值或自设Cov数字不保留为实验认证；见MU07-D22-R102-1至3。 | task-correction | rejected-and-replaced | printed172501-1–4;checkpoint102 | true |

计算脚本见system/scripts/day21_checkpoint141_shared_denominator_covariance_audit.py，输出shared-denominator-covariance-scope-141.json。

## Day22 checkpoint102：继承数字、手征与TiP对象边界

本轮四页正文与TableI/Figs2–4实际回读，视觉核p3三图；原source及Day21课程学分/评分不因此改动，新增仅Codex self-audit。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU07-D22-R102-1 | TableI五配对spin的sqrt[B(E2)B/B(E2)A]均值.935616、跨spin总体标准差.010156，解释了旧.9356±.0102的数值来源；后者不是由各点误差/Cov传播的Qt置信区间。sqrt比只有共同E2几何下才作Qt代理，不能独立限内禀形变差到1%。37/2→39/2的E2中央降幅A .32/.13=2.46154、B .29/.11=2.63636，商1.07102，不是旧2.57/1.043。作者称误差内强度相近支持手征，而非排他排除一切形状共存/带交叉。 | literal-table-and-statistic-identity | direct-original-and-task-arithmetic | 172501-2TableI;172501-4tilt/anharmonicitydiscussion | true |
| MU07-D22-R102-2 | M1在Fig2，E2在Fig3，不能互错。作者报告带内与带间M1交错反相；有限图点的差分符号/相关r不是原文新报的全spin反相检验或机制唯一性。本文第1页明确核chirality由time reversal互换左右手、space inversion不变；两带同宇称，不是宇称双重态。RPA临界spin比实测最近点高约1ℏ且过渡处方法失效，寿命比趋近1不能单独标定静态手征硬阈值。 | observable-phase-and-symmetry-boundary | direct-original | 172501-1chiralitydefinition;172501-2strengthparagraph;172501-3Figs2/3;172501-4criticaldiscussion | true |
| MU07-D22-R102-3 | 同一母态派生B若有共同1/τ因子，其比值代数可消τ；但原文不给完整branch/energy/δ/Cov，不能据此指定ρ=.856或统一5.87%比值误差。该实验175MeV thick-targetGammasphere测的是三准粒子chiralpair；Lv2021的152MeV thin-targetJUROGAM研究低spinD1/TiP1/TiP2单νh11/2家族，是不同带/组态和采集，不能用同核名称互为模式否证。 | covariance-and-band-family-identity | direct-original-and-cross-source-boundary | 172501-1setup/configuration;172501-2TableI;LV21printed044308-4setup/044308-11Summary | true |

## Day23内的Day24无学分预习：135Nd导出端点与clock合同

本节是外部IAEA export的field/身份核验，**不是MU07的新测量或原producer复现**。本次定向回核本原件PDF1 setup、PDF2 TableI/方法和PDF3图/角色，fresh视觉PDF2/3，raw SHA9eccc9c2ad02cc10735d1aad0d76eb2fd8af0a4acc814bcaab8099f50e748425相符；[[zhu-2003-135nd-composite-chiral-pair]]的原Fig2亦fresh视觉。旧flags/撤回范围保持，不新称重读全部4页。

官方请求为`https://www-nds.iaea.org/relnsd/v0/data?fields=gammas&nuclides=135nd`和`fields=levels`，本次均HTTP200；CSV分别168条非空γ/94条非空level，各有1条全空终止record。Extraction_date2026-10-25，ENSDF_publication_cut-off22-Jan-2008，评价作者为B.Singh/A.A.Rodionov/Y.L.Khazov；当前可访问不等当前实验/新评价。完整CSV仅tmp staging，正式raw归档deferred，sha分别153f5735282b2ce8cc7932f38d0a9aa14d604704fa82177123922c25c4af65b4与accf66c5f5fb5d5d6dbdaeaf57336b9f2141b57de819cc07d836050ca70aca93。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU07-D24P-001 | 本snapshot的γ三元ID(59,52,2)为648keV、31/2−→29/2−，(60,52,1)为649.2keV、33/2−→29/2−；(66,60,1)为590keV、35/2−→33/2−，(66,59,2)为591keV、35/2−→31/2−。近能量而端点/ΔI不同，不能按Eγ单键合并或把后者591的E2 crossover当interband ΔI1；它不自动认证旧Fig2/3 plotted components的实际line binding。 | external-snapshot-line-identity | actual-official-export-not-new-experiment | IAEA gammas135nd snapshot, IDs(59,52,2)/(60,52,1)/(66,60,1)/(66,59,2); levels135nd matching idx | true |
| MU07-D24P-002 | 导出level半衰期与本TableI mean lifetime需分开：例如B31/2 idx59为T1/2=1.012ps，除ln2得约1.4600ps；A31/2 idx55为.52ps，得到约.7502ps。十个声明同I/family配对的转换中心与MU07表中心最大差约.0044ps，只有算术/舍入相容，不构成独立复测或误差/CI验证。idx/归属仍绑定本snapshot和历史family，不能用排序或近能量代替。 | external-clock-identity-and-bounded-comparison | official-fields-plus-centre-arithmetic | IAEA levels135nd idx55/59 and declared pairedidx60/61/63/66/68/69/72/73; MU07 PDF2 TableI | true |
| MU07-D24P-003 | 官方guide把γ的RTPW定义为Weisskopf Units；b_e2/b_m1导出字符串不能直接与本表e²b²/μN²数值相比。226条目(59,56,0)的mixing_ratio为正字符串.14、unc_mr空且缺原adopted notes/phase，这里不认证其为实测signed δ。relative_intensity100只为该parent的相对归一；现代字段不能恢复225.8keV偏振正号/16.3h排他方案、原branch完整性或实验jointCov。 | external-unit-and-missing-note-boundary | actual-guide-and-export-with-limits | IAEA official APIguide gammas/RTPW paragraph; gammas135nd ID(59,56,0) | true |

`system/scripts/day24_preview_nd135_export_identity.py`对真实CSV做strict-width/核素/duplicate-unc_hl列位置/uniqueID/全部端点energy与Jπ join/clock单位和near-line identity共14检查通过。level的两个unc_hl按column12/15保留，不用DictReader覆盖；没有将全部过关扩为原实验或原level scheme认证。半衰期/评价B字段与原DSAM/强度链可能共源，原adopted notes及2007图marker的组件/branch对应仍缺，不给新δ、τ CI、Q/g、机时或最终手征静态阈值。

## Day23内的Day24无学分预习：作者矢量图可读性与未给的逐线ledger

NuDat3 `getdataset.jsp?nucleus=135ND&unc=nds`本次HTTP429，未自动循环重试。OpenAlex DOI99.172501实际返回arXiv0708.1493；官方abs显示v1为2007-08-10、v2为2007-09-14。`https://arxiv.org/src/0708.1493`实际HTTP200/application-gzip/21003 bytes，SHA24bbe35114c39469835515e88113b9fc69f3cbfeffe655a11bd333620cf0a692。六个regular文件（fig1–4.ps、ndchiralrev4.tex/.bbl）先检查无absolute/../symlink/hardlink、累计111234 bytes后只解到tmp；**没有执行TeX、PostScript或其中脚本**。不是原实验producer/events，正式raw归档仍deferred。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU07-D24P-004 | 作者source TeX TableI的13行meanτ/B(M1)/B(E2)字面值与已存期刊表相同；源表仍没有逐行Eγ/Jf。fig2.ps和fig3.ps各有4个data EARC加1个legend EARC，实际axes/tick/colour/marker命令可作为绘图坐标读取，不能当原未舍入data table或第二次采集。 | external-author-representation-and-table-version | official-author-source-read-as-data | arXiv0708.1493v2 source ndchiralrev4.tex TableI; fig2.ps/fig3.ps EARCs and axes/legends | true |
| MU07-D24P-005 | 按声明linear axes从四位小数矢量坐标重建，图I=15.5/16.5/17.5/18.5的interband drawn B(M1)中心约.08364/.11858/.08047/.18899 μN²，drawn B(E2)约.03903/.06803/.13301/.14427 e²b²。只在I确属同TableI BandB parent及组件相同的附加条件下，out/in中心为M1 .03098/.05647/.03658/.11117，E2 .13939/.24295/.47503/.49749。原source未补组件/γ身份，所以该比仍conditional；绘图误差棒端点及所设±.00005坐标rounding包络均非实验CI或jointCov。 | rounded-vector-coordinate-and-conditional-ratio | author-drawing-data-plus-bounded-arithmetic | arXiv0708.1493v2 fig2.ps lines931–934; fig3.ps lines931–934; TeX TableI | true |

`system/scripts/day24_preview_mu07_vector_plot.py`纯读文本命令，19项frame/tick/halfspin/data-vs-legend/bar/envelope/TableI控制通过；初次literal-frame检查因`.1500`与source的`0.1500`字符串不同失败，改为原literal写法后重跑，未调整任何科学点。Source图面四位小数本身限制精度，不能把输出浮点位数当更多实验有效数字；±.00005仅声明nearest-rounding模型，不自动涵盖truncation/其它图变换。MU07-8/13的旧手工读图可由此减少表示误差，MU07-9/10/16的parent/component/branch假设却**没有因此认证**，更不据旧条件budget判作者错误。

关键残余缺口是：图例只给BandB→BandA，没有逐点γ能量、finalI、多极component及原branch/IC/响应ledger。归档有drawings/TeX/bibliography，未提供raw spectra、data/AGR输入或分析producer。新可读表示支持更可复核的图点转录，不增加独立物理证据票，不恢复Qt代理CI、225.8P正号/机时排他认证。新needs_review:true。

## Day23内的Day24无学分预习：检验绝对宽度与selected-outlet归一假说

本节是**compound hypothesis诊断，不是论文错误判定或新实测分支**。使用实际source TeX/roundedPS与135Nd API候选端点，率定义来自[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-D24P-001。[[almehed-2011-chiral-vibrations-a135]] AL11-D24P-001/002表明不同m/归一不能自动互换，未提供本核missing line ledger。

声明H_abs同时假定：(i)图I为TableI BandB同一initial parent；(ii)图中的M1_out/E2_out为绝对physical component B；(iii)M1_out走648/639/590/556keV的ΔI1候选，E2_out走896/930/949/963keV的ΔI2候选；(iv)表内M1_in/E2_in分别走226/282.1/309/371.2与399/508/591/682keV；(v)TableI的τ是这个parent的total mean lifetime。所有这些binding未由作者source逐点ledger共同认证。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU07-D24P-006 | 在H_abs四个I=31/2…37/2中心输入中，qγ=τΣλγ的in-only为.85076/.82217/.88874/.98551，out-pair-only为.98743/.97775/.98876/.97684，合计1.83820/1.79993/1.87750/1.96235。它们与同一parent的photon库存≤1不相容；非负IC/漏枝不能减少该photon总和。只否定该compound中央绑定，不否定原实验、作者B定义或手征解释，也未用未知Cov报告显著性。 | compound-binding-centre-diagnostic | declared-hypothesis-and-source-data-arithmetic | MU07 TableI; arxiv0708.1493v2 fig2.ps/fig3.ps EARCs; API135Nd IDs asinput-contract020; LKH82-D24P-001 | true |
| MU07-D24P-007 | 该候选out-pair中，从drawnB派生的M1 photon份额为.59170/.48408/.18809/.28066，API这两条totalγ relativeI的份额为.60000/.47712/.18584/.28571；out-only q接近1与该shape近似构成一个值得查ledger的selected-outlet归一候选。它不证明作者作了条件归一；648为mixed line，totalI不等其M1component，不据差值反演δ。不同parent/line/component或其它normalizer仍是竞争假说，未给各自可信度/fit胜负。 | alternative-normalization-readiness-hypothesis | bounded-diagnostic-not-author-attribution | MU07-D24P-006 inputs; officialAPI relativeI rows648/896,639/930,590/949,556/963 | true |

`system/scripts/day24_preview_mu07_inventory_hypothesis.py`实际读取author TeX/PS与CSV，不用历史outputs认证为事实源；22项单位/能量幂/源端点spin/非负/homogeneity检查通过。这里的derivedλ是**条件核光子部分宽度**，不是设施探测率/新机时。代码没有用IC补齐库存、没有给normalizer实测值，也没有修改任何published B/τ。

若选H_cond为解释，需要原normalizer和absolute radiative branching说明，才能把selected-outlet quantities与真正的同parent绝对B/width对应；数学上给某个未知scale留可行域不代表这个解释与原模型同等可信。若选H_other，必须明确到底改变哪个parent/Jf/component/plot-I含义。最高信息输入是作者原branch/normalization ledger，而不是增加小数位或从数据域内任意缩放。本节不能恢复旧MU07父预算“paper-error”式强结论、Qt代理CI或225.8偏振/机时排他认证；新needs_review:true。

## Day23内的Day24无学分预习：完整同自旋EM块尚缺哪一格

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MU07-D24P-008 | 依018的candidate A/B family与M1 Ii→Ii−1构块，还需A31/2idx55→B29/2idx56、A33/2idx60→B31/2idx59、A35/2idx63→B33/2idx61、A37/2idx68→B35/2idx66这四个outlets。API中央ΔE分别−130.7/+1.4/+125.6/+254.0keV，当前snapshot均无forward或inverseγ行；缺行不等实测absence/upperlimit/zeroB。第一条为上跃而reverseRME仍可存在，逆向B29/2 parentτ空且MU07 TableB从31/2开始；+1.4中心还缺完整energyCov/IC/可测性输入，不能据中央正号认证开放退激。 | actual-export-missing-cell-and-readiness-boundary | snapshot-query-and-declared-family-inference | IAEA135Nd levelsidx55/56,60/59,63/61,68/66 andgammas forward/inverse search; MU07 TableI | true |

[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-D24P-004/005需要完整同Ii/If的相干RME块，不是只给两band in-strengths和一个方向的跨带图点就能算不变量。原graph/normalizer/component账未闭合，反向matrix element不能填0、带外未观测也不能证明projector封闭。必要伴随输入为这些特定outlet的可追溯强度或有效界、正确spin简并反向关系、各τ/branch/IC/response和可获得的relativephase约束；当前不拟新δ、g/Q、寿命CI或机时。新needs_review:true，仅Day24无学分preview。
