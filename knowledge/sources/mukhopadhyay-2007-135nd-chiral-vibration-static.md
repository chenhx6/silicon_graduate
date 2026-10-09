---
type: source
title: "Mukhopadhyay et al. 2007 - From chiral vibration to static chirality in 135Nd"
aliases: [Mukhopadhyay 2007 135Nd chirality]
created: 2026-09-21
updated: 2026-10-09
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
