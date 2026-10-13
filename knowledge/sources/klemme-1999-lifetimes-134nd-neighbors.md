---
type: source
title: "Lifetimes measurements for 134Nd and neighboring nuclei with the coincidence-plunger technique"
aliases: [Klemme 1999 coincidence-plunger lifetimes, Klemme 1999 134Nd]
created: 2026-08-11
updated: 2026-10-13
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Lifetimes measurements for 134Nd and neighboring nuclei with the coincidence-plunger technique"
authors: [T. Klemme, A. Fitzler, A. Dewald, S. Schell, S. Kasemann, R. Kühn, O. Stuch, H. Tiesler, K. O. Zell, P. von Brentano, D. Bazzacco, F. Brandolini, S. Lunardi, C. M. Petrache, C. Rossi Alvarez, G. De Angelis, P. Petkov, R. Wyss]
journal: Physical Review C
year: 1999
volume: 60
pages: 034301
doi: 10.1103/PhysRevC.60.034301
language: en
canonical_source: doi:10.1103/PhysRevC.60.034301
citation_key: klemme_1999_Lifetimesmeasurements
raw_file: "raw/papers/1999_Klemme et al_Lifetimes measurements for 134 Nd and neighboring nuclei with the.pdf"
raw_sha256: 2A6DFCDAC12DE9DBF61B2A63C274AED8E286249A3DD28D1A2C6C5A46F1C00604
nuclei: [130ce, 131ce, 132ce, 133pr, 134pr, 134nd, 135nd]
reactions: [110Pd(28Si,4n)134Nd, 110Pd(28Si,alpha4n)130Ce, 110Pd(28Si,alpha3n)131Ce, 110Pd(28Si,alpha2n)132Ce, 110Pd(28Si,p4n)133Pr, 110Pd(28Si,p3n)134Pr, 110Pd(28Si,3n)135Nd]
models: [interacting-boson-model, triaxial-rotor-model, total-routhian-surface, triaxial-particle-rotor-model]
observables: [transition-quadrupole-moment]
methods: [recoil-distance-doppler-shift]
tags: [experiment-ingest, method-ingest, project-ingest, a130, lifetime, rdds, ddcm, gamma-softness, triaxiality]
---

# Klemme 等（1999）：`134Nd` 与邻核 coincidence-plunger 寿命

## Bibliographic Record

T. Klemme 等，*Physical Review C* **60**, 034301 (1999)，DOI `10.1103/PhysRevC.60.034301`；citation key `klemme_1999_Lifetimesmeasurements`。

## Scope and Reading Depth

- Reading mode: standard deep reading；10 个 PDF pages 全文逐页阅读并视觉复核。
- Covered: GASP-II coincidence plunger、22 distances、DDCM equations/diagnostics、finite-stopping correction、`134Nd` Tables I-II/Figs. 1-7、六个 neighboring channels 的 Table III、`135Nd` ASYR comparison、`130,132Ce` deformation systematics 与结论。
- Not covered: 早期 level-scheme/configuration references 的独立复核；未给出的原始 distance spectra/matrices；后来的 chiral reinterpretations。
- Strategy: `experiment-ingest + method-ingest + project-ingest`。所有 KL99 与 analytical-reconstruction claims 保持 `needs_review: true`。

## Paper Question and Scientific Motivation

论文以高精度 absolute `B(E2)`/`Q_t` 检验 A≈130 γ-soft/triaxial collective models，并解决早期 `134Nd` ground-band lifetimes 之间的显著冲突。它同时利用六个竞争 reaction channels 给出 `130-132Ce`、`133,134Pr` 和 `135Nd` 低位 yrast lifetimes（PDF pp. 1, 4-5 / journal pp. 034301-1, 4-5）。

## Method and Design Logic

- 125 MeV `110Pd(28Si,xny p)`；1.02 mg/cm² self-supporting enriched `110Pd` target、11.5 mg/cm² Au stopper、Cologne plunger；GASP configuration II 移除 inner BGO ball，把 Ge detectors 靠近靶以提高 photopeak efficiency（PDF p. 1）。
- `1.47×10^9` fold≥3 events，22 个 target-stopper distances (`5-2003 μm`)；前后四个 detector rings 提供足够 Doppler separation（PDF pp. 1-2）。
- DDCM 以 feeding transition shifted component 作 gate，从 shifted/unshifted decay curves 的 intensity/derivative ratio逐 distance 得到 `τ(x)`；理想 `τ` curve 应为常数，distance dependence 是系统误差诊断（PDF p. 2; Eqs. 1-3; Fig. 2）。
- 对 `<2 ps` states，Au stopper 内约 `1.1 ps` slowing time 不能忽略；作者用 DSAM-like finite-stopping correction，并把 stopping-power不确定度写入 asymmetric adopted errors（PDF p. 3）。

## Key Evidence and Reasoning Chain

- high-statistics multi-distance coincidence gates → suppress unknown feeding/deorientation and produce independent ring/gate lifetime estimates（PDF pp. 1-5; Figs. 1-4）。
- DDCM constant-`τ` diagnostics + contaminant/systematic error budget → 12 `134Nd` lifetimes，多数精度优于 5%（Tables I-II）。
- lifetimes + branching intensities → `B(E2)` and `Q_t` across g.s.b., γ, S1/S2 and negative-parity sequences → strong band-dependent deformation changes（Table II; Figs. 5-7）。
- IBM O(6)/U(5), axial/triaxial rotor and TRS comparisons → γ-softness is supported but no single simple collective model reproduces energies and transition strengths globally（PDF pp. 6-8）。
- neighboring-channel lifetimes + ASYR for `135Nd` `[514]9/2` band → triaxial particle-rotor description of one reference band, not a chiral-pair test（Tables III-IV; Fig. 8）。

## Summary

本文的主要贡献是高精度 coincidence-RDDS/DDCM 数据链。`134Nd` low-spin g.s.b. 的平均 `Q0=4.37(4) eb`、`β2=0.246(2)`；crossing 后 S1 reaches `Q_t=5.5(+0.3/-0.2) eb`，S2 则明显较小，提示强 deformation/band-mixing change，但 S1/S2 microscopic configurations 仍未裁决。`135Nd` 三个低位负宇称寿命与现有 D1 levels 对应，并由 ASYR (`ε2=0.18, ε4=0.01, γ=23°`) 较好描述。全文不讨论 nuclear chirality；`134Pr 9+` 的单点寿命和 `135Nd` 单带 ASYR 不能充当 chiral-doublet electromagnetic evidence。

## Experimental or Theoretical Setup

| Item | Source-grounded value |
|---|---|
| beam/target | 125 MeV `28Si`; 1.02 mg/cm² enriched self-supporting `110Pd` |
| stopper/plunger | 11.5 mg/cm² Au; Cologne plunger; distance regulation accuracy `<0.1 μm` to 20 μm and `<1 μm` to 2000 μm |
| array | GASP configuration II, inner BGO removed; Compton-shielded Ge closer to target |
| statistics/distances | `1.47×10^9` fold≥3 events; 22 distances, `5-2003 μm` |
| recoil speed | mean `v/c=1.6%` |
| DDCM angles | rings near `31.7-36°, 58.3-60°, 72°, 90°, 108°, 120-121.7°, 144-148.3°`; quantitative analysis uses four farthest from 90° |
| models | IBM O(6)/U(5), axial and rigid-triaxial rotor, TRS; `135Nd` ASYR particle-plus-triaxial-rotor |

## Key Results

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KL99-1 | 125 MeV `110Pd+28Si` GASP-II plunger experiment collected `1.47×10^9` fold≥3 events at 22 distances and identified six competing channels feeding `130-132Ce`, `133,134Pr`, `134Nd` and `135Nd`. | method-fact | direct | PDF pp. 1-2 / journal pp. 034301-1-2 | true |
| KL99-2 | DDCM extracts `τ(x)` from coincidence-gated shifted/unshifted intensities and the derivative of the shifted decay curve; a nonconstant `τ(x)` is an explicit systematic-error signal. | method-result | direct | PDF p. 2; Eqs. 1-3; Fig. 2 | true |
| KL99-3 | 12 `134Nd` states and 12 neighboring-nucleus states were measured; most `134Nd` lifetimes have accuracy better than 5%, with statistical, contaminant and 2% small-correction terms separated. | experimental-fact | direct | PDF pp. 3-5; Tables I-III; Conclusions | true |
| KL99-4 | For lifetimes below about `2 ps`, finite Au-stopper slowing (`~1.1 ps`) changes the result; a plausible 30% electronic-stopping increase could fit the spectra, so adopted lifetimes use asymmetric errors spanning about half the correction difference. | method-limitation | direct | PDF p. 3 / journal p. 034301-3 | true |
| KL99-5 | `134Nd` g.s.b. `Q_t` values are `4.32(7), 4.40(5), 3.98(+0.16/-0.08), 3.70(19) eb` for `2+,4+,6+,8+`; the first two give average `Q0=4.37(4) eb` and `β2=0.246(2)`. | derived-observable | direct | PDF pp. 4, 6; Table II; Fig. 5 | true |
| KL99-6 | `134Nd` S1 increases from `Q_t=4.65(+0.21/-0.14) eb` at `10+` to `5.5(3) eb` at `12+`, while S2 has `2.16(12), 3.76(13), 3.8(+0.4/-0.3) eb` at `10+,12+,16+`; authors infer strong band-dependent deformation change. | derived-observable | direct | PDF pp. 4, 6-7; Table II; Figs. 5-7 | true |
| KL99-7 | IBM O(6), U(5) and rigid-triaxial rotor models do not reproduce the full `134Nd` energy/transition data within experimental precision; O(6) is closest and supports γ-soft character, but `4+g→2+g` and γ-band strengths remain problematic. | author-interpretation | direct | PDF pp. 6-8; Figs. 5-7 | true |
| KL99-8 | TRS predicts a new `β≥0.3` high-frequency minimum possibly connected to neutron `[541]1/2` occupation and the strongly collective S1 band, but the detailed S1/S2 particle configurations require more theory/data. | model-result | indirect | PDF pp. 6-7; Fig. 7 | true |
| KL99-9 | S2 configuration remains unresolved: earlier neutron `(h11/2)^2` and later proton `(h11/2)^2` proposals yield deformation differences too small for the measured transition probabilities to distinguish. | competing-interpretation | direct | PDF p. 7 / journal p. 034301-7 | true |
| KL99-10 | The measured `B(E2;8γ+→6γ+)=0.77(+0.34/-0.20) e²b²` exceeds O(6) prediction and is reproduced by a triaxial rotor, but that rigid rotor fails γ-band staggering and g.s.b. strengths; no simple model explains all data. | derived-observable | direct | PDF pp. 7-8 / journal pp. 034301-7-8 | true |
| KL99-11 | Table III gives `τ=173(12), 7.53(37) ps` for `131Ce 11/2-,15/2-`; `64.2(39),3.42(10) ps` for `133Pr 15/2-,19/2-`; `4.96(11) ps` for `134Pr 9+`; and `60.1(67),7.76(63),4.61(25) ps` for `135Nd 11/2-,13/2-,15/2-`. | experimental-fact | direct | PDF p. 5; Table III | true |
| KL99-12 | `130Ce 2+g,4+g` lifetimes are `181.3(70),7.65(31) ps`; `132Ce` are `70.1(32),3.9(10) ps`; derived `Q_t` pairs give `β2=0.259(4)` and `0.237(3)`, respectively. | derived-observable | direct | PDF pp. 5, 8-9; Table III; Fig. 9 | true |
| KL99-13 | `135Nd` low negative-parity sequence is assigned `h11/2:[514]9/2`; ASYR with `ε2=0.18, ε4=0.01, γ=23°` (`β≈0.19`) rather well reproduces energies and relative/absolute transitions. | model-result | direct | PDF p. 8; Table IV; Fig. 8 | true |
| KL99-14 | The `135Nd 11/2-,13/2-,15/2-` levels/energies and `[514]9/2` assignment match the later Wiki D1 reference-band identity; this is a cross-source reconstruction, not a Klemme-era D1 label. | cross-source-identification | indirect | KL99-11/13 plus [[135nd-d1-band]] level energies/configuration | true |
| KL99-15 | Gates above the level of interest exclude unobserved feeding and deorientation effects in the reported low-spin lifetimes; the authors warn that deorientation can severely affect states up to `4ℏ`. | method-limitation | direct | PDF p. 5 / journal p. 034301-5 | true |
| KL99-16 | The paper does not invoke chirality or establish a partner-band geometry; its `135Nd` ASYR test concerns one band, and its single `134Pr 9+` lifetime has no explicit crosswalk to the 1996 Band 1/Band 2 pair. | source-scope-fact | direct | full-paper scope; PDF pp. 1-10 | true |
| KL99-17 | The fusion-evaporation recoils had a reported mean `v/c=1.6%`; GASP rings covered 31.7–148.3°, and the four rings farthest from 90° were selected because their Doppler shifts were large enough for quantitative lifetime analysis. | experimental-fact | direct | PDF pp. 1-2; detector-ring geometry; Fig. 1 | true |
| KL99-18 | Fig.1 follows the same 134Nd 2g+→0g+, 4g+→2g+ and 6g+→4g+ lines at 24, 103 and 1203 μm, under a gate on the shifted feeding component. Their shifted/unshifted fractions change with distance. Table I gives the 6g+ average lifetime 1.38(4) ps before finite-stopping correction and 1.63(6) ps in its corrected column; Table II adopts asymmetric 1.63(+0.06/−0.12) ps after stopping-power uncertainty. | experimental-fact | direct | PDF p.2, Fig.1; PDF p.3, Table I; PDF p.4, Table II | true |

## `134Nd` Lifetime and Strength Matrix

| Structure/state | adopted `τ` (ps) | `Q_t` (eb) | Boundary |
|---|---:|---:|---|
| g.s.b. `2+` | `94.4(30)` | `4.32(7)` | low-spin collective baseline |
| g.s.b. `4+` | `4.94(10)` | `4.40(5)` | old singles values differ strongly |
| g.s.b. `6+` | `1.63(+0.06/-0.12)` | `3.98(+0.16/-0.08)` | finite-stopping corrected |
| g.s.b. `8+` | `1.03(10)` | `3.70(19)` | possible early S1 mixing or γ softness |
| S1 `10+,12+` | `0.71(6),0.59(6)` | `4.65(+0.21/-0.14),5.5(3)` | strong rise, model/configuration assisted |
| S2 `10+,12+,16+` | `4.89(23),10.8(3),0.68(13)` | `2.16(12),3.76(13),3.8(+0.4/-0.3)` | weaker than S1; configuration unresolved |
| γ `8+` | `1.24(30)` | `4.8(+1.0/-0.7)` | large uncertainty; model tension |
| negative `8-,10-` | `24.9(18),6.79(20)` | not assigned | `B(E2)` listed without rotor `Q_t` |

## Competing Interpretations and Limitations

- Low-spin constant `Q_t` is consistent with an axial rotor average, while energy ratios/staggering and O(6)/TRS favor γ softness. The same data do not uniquely select rigid triaxiality versus γ-softness.
- `8+g` reduced `Q_t` may mark S1 mixing already at `6+/8+`, or reflect γ softness; the source explicitly leaves this conditional.
- S1 high collectivity aligns with a TRS second minimum, but its `[541]1/2` configuration is model-assisted and systematics raise unresolved questions.
- S2 neutron/proton `(h11/2)^2` alternatives are not separated by measured strengths; γ/S-band interaction mechanism remains unclear.
- Short-lifetime finite-stopping and stopping powers impose asymmetric uncertainties; DDCM precision does not remove all model dependence in `B(E2)→Q_t` conversion.
- `134Pr`/`135Nd` chiral relevance is retrospective only. No partner-band lifetimes, interband matrix elements or chiral geometry are established.

## Analytical Reconstruction

| ID | Reconstruction role | Wiki synthesis | Source basis | status |
|---|---|---|---|---|
| AR-1 | Core reconstruction | Precision coincidence-plunger data turn apparent model agreement into a discriminator: no single collective limit explains all `134Nd` strengths. | KL99-2 to KL99-10 | unreviewed |
| AR-2 | Method chain | above-feeding gate → distance-resolved shifted/unshifted curves → DDCM constant-`τ` test → finite-stopping correction → lifetime/branching → `B(E2),Q_t`. | KL99-1 to KL99-5, KL99-15 | unreviewed |
| AR-3 | Cross-source identity | Klemme's `135Nd [514]9/2` levels are the low-spin portion later called D1; this adds absolute lifetime constraints to the reference band only. | KL99-11, KL99-13/14 | unreviewed |
| AR-4 | Failure condition | Neither one `134Pr 9+` lifetime nor one `135Nd` band plus ASYR supplies the paired electromagnetic evidence required for chirality. | KL99-16 | unreviewed |
| AR-5 | Research decision | Persist RDDS/DDCM as a reusable method page and use later chiral papers to establish band crosswalks before importing these lifetimes into chiral claims. | full evidence chain | unreviewed |

### Companion Evidence Audit

- `134Nd` Tables I-II: current experiment, direct lifetime/derived-strength chain.
- Neighbor lifetimes in Table III: current by-products with above-feeding coincidence gates; direct but sparse.
- Branching intensities in Table II: imported from a separate thin-target GASP coincidence experiment; dependent companion evidence.
- Earlier lifetime comparisons and `134Nd/135Nd` configurations: literature-dependent, not new independent assignments.
- TRS/IBM/rotor/ASYR shapes and configurations: model evidence, not direct geometry measurements.

## Knowledge Impact and Learning Decision

- New information: establishes precise normal-deformed `134Nd` strength map, explicit γ-soft/model tensions, `135Nd` D1 low-spin lifetime anchors, one `134Pr 9+` lifetime and a reusable coincidence-DDCM workflow.
- Corpus role: methodological and historical precursor/control evidence. It strengthens triaxial/γ-soft context but is not direct nuclear-chirality evidence.
- Persistence decision: create source, experiment and RDDS/DDCM method pages; update `134Nd`, `134Pr`, `135Nd`, `135Nd D1`, `131Ce` and the chirality project. Defer new `130,132Ce/133Pr` nucleus pages because their current contribution is two-state control data and their wider structure is not read here.

## Related Knowledge and Project Relations

| Relation | Target | Boundary |
|---|---|---|
| nucleus | [[134nd]] | Main 12-state lifetime/strength and band-crossing case. |
| nucleus | [[135nd]] | Three low negative-parity lifetimes plus ASYR; D1 crosswalk is Wiki reconstruction. |
| band | [[135nd-d1-band]] | Adds low-spin absolute lifetimes; no chiral-partner inference. |
| nucleus | [[134pr]] | One `9+` lifetime only; no 1996-band mapping claimed. |
| nucleus | [[131ce]] | Two low negative-parity lifetimes; no crosswalk to later Band 1 yet. |
| experiment | [[lnl-gasp-ii-plunger-pd110-si28-125mev]] | Shared coincidence-RDDS data. |
| method | [[recoil-distance-doppler-shift]] | DDCM equations, constant-`τ` diagnostic and finite-stopping boundary. |
| context-not-direct-evidence | [[nuclear-chirality-and-multiple-chiral-doublet-bands]] | Triaxial/lifetime precursor without partner-band chirality evidence. |

## Human Review Triage

### P0

P0: none identified.

### P1

- **KL99-6 to KL99-10 — `134Nd` deformation/model interpretation.** Check conditional separation among measured `Q_t`, inferred shape change, γ softness and proposed S1/S2 configurations. Risk: treating O(6)/TRS proximity as a unique experimental shape determination.
- **KL99-14/16 / AR-3/4 — D1/chirality crosswalk.** Check the `135Nd` level-by-level match to later D1 and keep `134Pr 9+` unmapped until a source establishes identity. Risk: common nucleus/energy labels silently becoming chiral-partner lifetime evidence.
- **KL99-4 / AR-2 — short-lifetime correction.** Preserve finite-stopping asymmetric errors and the dependence of `Q_t` on adopted lifetime/branching. Risk: quoting central values as analysis-independent precision.

### P2/P3

- P2: full Table III neighbor values, detector-ring notation and imported branching lineage.
- P3: bibliographic title grammar (`Lifetimes measurements`) preserved from source/BibTeX.

## Extracted Pages

- Source: this page.
- Experiment: [[lnl-gasp-ii-plunger-pd110-si28-125mev]].
- Method: [[recoil-distance-doppler-shift]].
- Nuclei/band: [[134nd]], [[134pr]], [[135nd]], [[131ce]], [[135nd-d1-band]].
- Project: [[nuclear-chirality-and-multiple-chiral-doublet-bands]].

## Non-source Notes and Follow-up

Next corpus sources should test whether later `134Pr/135Nd` chiral-band labels map onto these measured states. Until that crosswalk exists, quote Klemme 1999 only as early absolute-lifetime/triaxial context.

## 2026-10-13 Doppler/stopping source self-audit

十页全文主线重新回读：lifetimes conflict → coincidence-plunger/DDCM → finite stopping → Tables I–IV and band-dependent strengths → collective/TRS/ASYR limitations → conclusion。视觉核验 Fig.1/2 和 Table I；KL99-18 将同一跃迁随距离变化的 shifted/unshifted 分量固定为对“宽峰或双峰必是两个能级”的反例。1.38→1.63 ps 的约18.1%增量是本任务算术，不是新测量或本征寿命线宽；Au 1.1-ps slowing time 不能直接移植到 Mavela 的不同 projectile/target。多个 detector rings、feeding gates、邻核同次数据及独立薄靶 branching experiment 的依赖边界保留；不是若干独立核结构实验。原 review 和 needs_review 标记不变。
