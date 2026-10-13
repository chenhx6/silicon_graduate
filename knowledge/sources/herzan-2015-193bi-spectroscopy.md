---
type: source
title: "Herzáň et al. 2015 - Detailed spectroscopy of 193Bi"
aliases: [Herzan 2015 193Bi spectroscopy]
created: 2026-09-21
updated: 2026-10-13
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Detailed spectroscopy of 193Bi"
authors: [A. Herzáň, S. Juutinen, K. Auranen, T. Grahn, P. T. Greenlees, K. Hauschild, U. Jakobsson, P. Jones, R. Julin, S. Ketelhut, M. Leino, A. Lopez-Martens, P. Nieminen, M. Nyman, P. Peura, P. Rahkila, S. Rinta-Antila, P. Ruotsalainen, M. Sandzelius, J. Sarén, C. Scholey, J. Sorri, J. Uusitalo]
journal: "Physical Review C"
year: 2015
volume: 92
pages: "044310"
doi: "10.1103/PhysRevC.92.044310"
citation_key: Herz__2015
citation_key_origin: crossref-content-negotiation
citation_key_verified: 2026-09-21
canonical_source: "https://doi.org/10.1103/PhysRevC.92.044310"
library_file: "raw/papers/gpt/high-spin-20260920/纲图/2015_Herzáň et al_Detailed spectroscopy of Bi 193.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/纲图/2015_Herzáň et al_Detailed spectroscopy of Bi 193.pdf"
raw_sha256: "f727485ad0f52269a66b27272dac75d34d9e67aaf8b073631cfeac5fe81d3aea"
nuclei: [193Bi, 192Pb, 191Bi, 193Tl]
reactions: [165Ho-32S-4n]
experiments: [JYFL, JUROGAM-II, RITU, GREAT]
models: [Nilsson, oblate-configuration-coupling, superdeformation, shears-like-interpretation]
observables: [level-scheme, RDCO, IPDCO, isomer-half-life, E2, M1, alpha-decay]
methods: [gamma-gamma-coincidence, recoil-decay-tagging, isomer-tagging, linear-polarization-asymmetry]
tags: [193Bi, high-spin, isomer, superdeformation, shape-coexistence]
---

# Detailed spectroscopy of `193Bi`

## Bibliographic Record

- A. Herzáň *et al.*, *Phys. Rev. C* **92**, 044310 (2015), DOI `10.1103/PhysRevC.92.044310`.

## Scope and Reading Depth

- The 20-page article was read end-to-end: reaction/detector setup, RDT and isomer tagging, Tables I–II, Figs.1–18, all band/group discussions, high-spin isomers, spherical/oblate interpretation, superdeformed band, systematics and conclusion.

## Experimental Evidence

`193Bi` was produced in `165Ho(32S,4n)` at 152 MeV with JUROGAM II, RITU and GREAT. Prompt γ rays were analyzed with recoil-gated matrices/cubes; delayed γ rays and conversion electrons were recorded at the focal plane (PDF pp.1–3). DCO ratios used 157.6°/75.5° matrices; IPDCO used single-crystal versus same-clover two-crystal events, with the measured clover sensitivity fitted as `Q(Eγ)=Qpoint(0.42(4)−1.9(7)×10−4 Eγ)` (pp.2, 9–10, Eq./Fig.4).

The level scheme extends Band 1 (`πi13/2`) to `45/2+`, Band 2 to `29/2−`, and identifies new Bands 3–4 and groups D/F. DCO/IPDCO and coincidence/energy-sum evidence assign M1/E2 characters where statistics permit; weak Group D/F links retain uncertain assignments (pp.9–12, Table I, Fig.2).

## Isomers and Shape Interpretation

The known `(29/2−)` isomer has `T1/2=3.02(8) μs`; a `49 keV` transition is observed in delayed γ–electron coincidence and has a conversion coefficient consistent with E2, placing the isomer at about `2405 keV` (pp.12–15, Figs.6–9). A new `29/2+` isomer at `2350 keV` has `T1/2=85(3) μs` and decays through an `84 keV` E2 transition with `B(E2)=1.6(1)×10−3 W.u.`; the authors associate it with a `π(h9/2 i13/2)`-coupled oblate configuration (pp.15–18, Figs.8, 17).

Band 3 resembles a low-energy M1 sequence but receives E2 links and is extended to `(37/2−)`; the authors do not promote it to a universal shears assignment. A superdeformed band based on the favored `1/2[651]` proton orbital is nearly identical in transition energies to the SD band in `191Bi` and `193Tl`, but absolute transition probabilities are still needed to confirm SD character (pp.11, 18–19, Fig.18).

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HE15-1 | The `193Bi` level scheme is extended with new bands and DCO/IPDCO-supported multipolarities. | experiment-result | direct | PDF pp.2–3, 9–12, Table I | true |
| HE15-2 | `29/2−` and `29/2+` isomer energies/half-lives and E2 decays are established by delayed γ/e− tagging. | isomer-result | direct | PDF pp.12–18, Figs.6–9 | true |
| HE15-3 | The `1/2[651]` SD band is a candidate until absolute transition probabilities are measured. | shape-boundary | mixed | PDF pp.18–19, Fig.18 | true |
| HE15-4 | Band1 Table I reports 299.2(1),323.4(1),622.4(1) keV connecting the rounded 1228 (17/2+),929 (15/2+),605 (13/2+) levels in Fig.2. Their Rexp values are 0.68(2),0.74(4),1.30(16); ΔIPDCO values −0.032(1),−0.012(1),+0.086(10); authors list M1,M1,E2. Rexp uses efficiency-corrected intensities at157.6°/75.5° with the same gate on all-angles projections. Table I also asks for about0.3-keV statistical error in addition to listed fitting errors. | experimental-fact | direct | PDF p.3, Table I; PDF p.8, Fig.2; PDF p.2 ratio definition | true |
| HE15-5 | Fig.5(a), gated on the154-keV transition, describes the peak labeled323 keV as a quadruplet of315,320,323,327-keV transitions. Fig.5(b) is gated on323.4 keV and shows feeding into Band1. Table I also places299.8(1) keV higher in Band1 (41/2+→39/2+), distinct from299.2(1) (17/2+→15/2+). | experimental-fact | direct | PDF p.10, Fig.5 caption; PDF p.3, Table I | true |
| HE15-6 | The SD Table II retains an unknown bandhead energy X and parenthesized spin/parity assignments. A weak1836(5)-keV candidate is seen in coincidence with168.3 and331.7 keV; authors require more statistics to confirm it as a link to Band6. It cannot fix X as a confirmed absolute level in the present evidence. | experimental-fact | direct | PDF p.15, Table II; Fig.13; Sec.III.B | true |
| HE15-7 | The authors do not observe the expected low-energy SD transitions near87 and46 keV. They discuss overlap with the87.4-keV Bi x ray and large E2 conversion coefficients as reasons the γ rays could be very difficult to observe; the assumed intensity flow through these lines remains an interpretation. | author-interpretation | direct | PDF p.19, Sec.IV.D | true |

## Summary

Herzáň *et al.* provide a dense high-spin/isomer spectroscopy reference in the transitional Bi region, with a clear separation between level facts, multipolarity assignments and shape/configuration interpretations.

## Competing Interpretations and Limitations

- Weak groups have incomplete DCO/IPDCO coverage and retain uncertain assignments.
- SD transition-energy similarity is not a direct deformation measurement without absolute strengths.

## Analytical Reconstruction and Self-Audit

| ID | Audit item | Agent judgment | Locator | Status |
|---|---|---|---|---|
| HE15-AR-1 | Assignment chain | Coincidences + RDCO + IPDCO + isomer tagging support the principal band multipolarities; weak groups retain explicit uncertainty. | PDF pp.2–3, 9–12, Table I | self-checking |
| HE15-AR-2 | Isomer identity | Half-lives, delayed γ/e− coincidence and E2 conversion provide a stronger identity chain than systematics alone; configuration remains an interpretation. | PDF pp.12–18, Figs.6–9, 17 | self-checking |
| HE15-AR-3 | SD boundary | Energy-pattern similarity is a candidate SD signature; without absolute transition probabilities it is not direct deformation proof. | PDF pp.18–19, Fig.18 | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` high-spin isomer/shape-coexistence evidence and [[linear-polarization-asymmetry]], [[signature-partner-bands]] and [[band-termination]] method comparisons; it broadens the A≈190 control region beyond the A≈130 focus.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `HE15-P0-1`: Preserve the setup-specific IPDCO calibration and the distinction between confirmed level/isomer evidence and configuration/SD interpretations.

## Extracted Pages

- Nucleus/methods: `193Bi`, [[linear-polarization-asymmetry]], [[gamma-gamma-coincidence]]。

## Selected transition and gate self-audit

原始PDF哈希复核一致；重点原图核验Table I(p.3)、Figure2(p.8)和Figure5(p.10)，并回读reaction/tagging(p.1–2)、Band1和isomer/SD主线(p.10–15)、configuration/SD解释与结论(p.16–20)的对应段落。本次预习不替代正式周考，也不改变原阅读/审核状态。[[level-scheme-reconstruction]] 固化三层子图、energy closure/covariance练习与复合峰/互斥branch控制；[[doppler-correction]] 使用HE15-5作独立的多线峰反例。

299.2+323.4−622.4=0.2keV是本任务算术，不是作者单独报告的closure test。TableI/Fig.2/Fig.5共享同次实验；relative intensities、DCO/IPDCO与coincidences不能重复计成独立实验。HE15-4/5/6保持needs_review=true。
