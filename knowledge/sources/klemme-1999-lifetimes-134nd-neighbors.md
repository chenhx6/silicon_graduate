---
type: source
title: "Lifetimes measurements for 134Nd and neighboring nuclei with the coincidence-plunger technique"
aliases: [Klemme 1999 coincidence-plunger lifetimes, Klemme 1999 134Nd]
created: 2026-08-11
updated: 2026-10-20
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

## Day20邻核通道伴随观测与谱系审计（checkpoint003）

依据独立审计程序 `system/scripts/day20_klemme_companion_audit.py` 与结果 `outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-02/klemme-companion-result-003.json`，本轮已实际读完整10页文本及PDF2–9关键视觉，含9图、4表、5式；这是新scope，不借旧raw哈希继承。TableIII的谱系对账保留；原003“通过/精度/残差成因”认证已由007撤回：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KL99-D20-1 | checkpoint007保留原表事实并撤回过强003认证：TableIII的131Ce15/2−7.53(37)ps、133Pr15/2−64.2(39)ps及19/2−3.42(10)ps逐项被Singh Ref31列复用；后者Qt是同一旧寿命的派生量，不是新采集。1999为125MeV28Si+110Pd、self-supporting靶/GASP-II，2016为Sn+O/F与IUAC-GDA；不同campaign并不证明绝对校准/转换常数等全部独立。暂不凭对称化sigma检验认证相同形变；齐次几何/分支/误差合同未闭合。 | lineage-and-comparison-boundary | direct-original-and-visual | PDF5 Table III; Singh Table 1; Singh Table 2 | true |

## Non-source Notes and Follow-up

Next corpus sources should test whether later `134Pr/135Nd` chiral-band labels map onto these measured states. Until that crosswalk exists, quote Klemme 1999 only as early absolute-lifetime/triaxial context.

## 2026-10-13 Doppler/stopping source self-audit

十页全文主线重新回读：lifetimes conflict → coincidence-plunger/DDCM → finite stopping → Tables I–IV and band-dependent strengths → collective/TRS/ASYR limitations → conclusion。视觉核验 Fig.1/2 和 Table I；KL99-18 将同一跃迁随距离变化的 shifted/unshifted 分量固定为对“宽峰或双峰必是两个能级”的反例。1.38→1.63 ps 的约18.1%增量是本任务算术，不是新测量或本征寿命线宽；Au 1.1-ps slowing time 不能直接移植到 Mavela 的不同 projectile/target。多个 detector rings、feeding gates、邻核同次数据及独立薄靶 branching experiment 的依赖边界保留；不是若干独立核结构实验。原 review 和 needs_review 标记不变。


## Day18定向companion：有限停止修正的共同尺度与相对强度

本session在读取既有source（承认Day13完整重读及6g的1.38→1.63已暴露）之后冻结新问题，**只定向原读PDF2–4**，视觉核TableI/II和修正文字，不声明新完整十页或Day19卡。Raw hash保持2a6dfcdac12de9dbf61b2a63c274aed8e286249a3dd28d1a2c6c5a46f1c00604。

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| KL99-D18-1 | TableI六个非空tcorr的standard→corrected为6g:1.38→1.63、8g:.85→1.03、8gamma:1.04→1.24、10S1:.58→.71、12S1:.47→.59、16S2:.55→.68ps；修正因子1.181159–1.255319不是一项统一乘法尺度。无tcorr的其它行不据空字段断言精确修正为零。 | direct-table-and-task-role-audit | direct-and-derived | PDF3TableI及finite-stopping段 | true |
| KL99-D18-2 | 作者说电子停止增加30%仍可合理描述RDDS谱，且将standard与adopted之差约减半；没有给该分支逐态新τ/完整参数域或Σ。以tau(f)=standard+f(corrected−standard)、f在[.5,1]作设计是本任务额外合同，不是原fit/CI或概率prior。 | source-input-and-declared-chart | direct-and-derived-boundary | PDF3TableI下方两栏；新finite-stopper-input-contract-006 | true |
| KL99-D18-3 | 保持branch/ICC/能量/几何不动时B∝1/tau、Qt∝tau^−1/2；新六行chart使12S1/10S1的Qt比1.1827957→1.1894563（+.563123%），8g/6g为.9296482→.9350779（+.584053%）。二者对f单调，端点界仅本chart，不是原likelihood/实验CI或完整stopping-model envelope。 | task-relative-strength-response | derived-and-boundary | PDF3TableI、PDF4TableII/Eq4；新rdds-companion-result-006 | true |
| KL99-D18-4 | DDCM距离轴/导数提供与DSAM不同的时间响应，但短τ的finite-stopping、共同速度/门/强度及Qt的branch/轴假设仍须匹配；ring/gate统计重复不自动给actualjointCov。本文134Nd不是Rather106Ag的RDDS采集，不能借方法/核区替actualsamelevelcompanion。 | companion-transfer-boundary | direct-and-synthesis | PDF2Eq1–3；PDF3finite-stopping；PDF4Eq4/TableIIcaption；RA14-2/3 | true |

新[六行合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/finite-stopper-input-contract-006.json)、[程序](../../system/scripts/day18_rdds_companion_contract.py)/[实际结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/rdds-companion-result-006.json)严格核raw hash，保中心数值，不拟合原谱/原Σ。初draft只重复旧单行算术并把若干事实写为boolean checks，已在发布前替换为真实六行敏感性分析；不把旧18%算术或该draft的“6checks”计新证据。所有旧KL99 rows/reviewflags保持，新四条待审。

与[[rather-2014-ag106-transition-rates]]的samelevel边界分开。写回[[doppler-shift-attenuation-method]]与[[lifetime-strength-audit-165tm-136nd]]，只作当前DSAM的独立性/系统误差companion，不开启RDDS/fast-timing完整课卡。进一步需要实际distance spectra、slowing模型分支、逐ring/gate拟合Cov和samelevel身份，不能把小ratio变化当所有系统已取消。


## Day19新原读：DDCM门条件与相对坐标

本session承认旧Day13/Day18暴露后，新读十页全文文本主线；实际视觉核PDF2–5的Eqs1–4、Figs1–4及TablesI–III，未把其余图算成新视觉阅读。raw SHA256仍2a6dfcdac12de9dbf61b2a63c274aed8e286249a3dd28d1a2c6c5a46f1c00604。以下新增self-audit不改变上方历史scope、review或任何旧claim flag。这里source_independence为本实验与Radeck/Nolan的distinct-data comparison；同本文rings/gates共享距离、速度和停止校准。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| KL99-D19-1 | Eq1间接门为τ=(I_su^CA−αI_su^CB)/(dI_ss^CA/dx)/v；Eq2的α为两级联总强度之比；单一直接feeding门Eq3为τ=I_su^BA/(dI_ss^BA/dx)/v。s/u各标志feeder与decay的shifted/unshifted，不是任意单谱的总survival。 | gate-formalism | direct-original | PDF2 Eqs1–3、SecIII；Figs1–2 | true |
| KL99-D19-2 | 作者以τ(x)非平坦诊断系统误差，并称理想情况下四ring×直接/间接两门提供八个独立值；实际统计门/污染各异。共享distance gain、v和停止输入仍须单独计Cov，平坦性不能排除共同尺度偏差。 | diagnostic-and-independence-boundary | direct-and-task-derived | PDF2 Eq3后段至PDF3首段；PDF4误差段 | true |
| KL99-D19-3 | PDF4明确将短于1ps的可测性归于延迟feeding与高统计；最近距离5μm不是通用τ≥dmin/v下限。短τ仍需约1.1ps Au慢化修正，TableI六行校正不等比例，电子stopping+30%分支进入adopted不对称误差。 | method-window-and-material-boundary | direct-original | PDF1 SecII；PDF3 TableI及下方两栏；PDF4 Fig3下方、TableII | true |
| KL99-D19-4 | 本任务理想branch-one模型：dF_A/dt=p_A/τ_A；直接门用p_A，间接门用1−F_A−S_B。二者可消去所选feeder分布但依赖门纯度、完整分量、共同归一与正确α。常数x原点平移不改导数比；distance gain1.02却使τ2ps成为全程平坦2.04ps。不是原数据重拟合。 | conditional-rate-reconstruction | task-derived-from-method | PDF2 Eqs1–3；ddcm-gate-contract-result-013.json | true |

Knowledge Impact and Learning Decision：limits固定方法窗与“八值完全独立/平坦即无系统误差”的外推；supports以真实gate、rate derivative及finite-stopping作为选择合同。[[recoil-distance-doppler-shift]]和[[lifetime-method-selection-response-contract]]保存新106项条件控制。实际distance spectra、导数平滑/联合Cov、逐门eff与transport仍缺；不产原实验fitCI。

## checkpoint089：六行修正与电子停止分支

本轮定向读PDF2–3，视觉核PDF3 TableI/caption及两栏finite-stopping段；不是又一次独立原实验。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| KL99-D19-5 | TableI六非空tau_corr行依次为1.38→1.63、.85→1.03、1.04→1.24、.58→.71、.47→.59、.55→.68ps；原作者说采用停止输入下mean slowing time约1.1ps，电子stopping+30%仍可合理描述谱、standard与adopted之差约减半。没有给每条实际新tau/完整trajectory/Cov；不能把仅电子分量+30%当全速度域total stopping统一×1.3，或据此认实际stop time=.846ps。旧chosen half-correction chart的小Qt比变化不认证所有系统误差抵消。 | literal-correction-and-nuisance-domain | direct-original-and-boundary | PDF3 TableI/caption and finite-stopping paragraphs | true |


## checkpoint108：身份、频率与校准的直接原读纠正

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| KL99-D19-6 | 134Nd2g+294keV采用tau94.4(30)ps，非45.4ps；六个finite-stopping更正行属于不同较短tau态，不能将1.181–1.255统一附到2+或所有nuclei。PDF3明确Au mean slowing约1.1ps与电子stopping+30%替代，不是停止独立。 | direct-scope-and-correction | direct-original-and-bounded-arithmetic | PDF3 TableI; PDF4 TableII | true |

## Day20量化审计：134Nd三层形变阶梯、S2跨带四极压制与有限停止慢化协方差定理

依据独立程序 `system/scripts/day20_nd134_multiband_deformation_coexistence_audit.py` 与基准输出 `outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-02/nd134-multiband-deformation-result-023.json`，量化审计了 $^{134}\text{Nd}$ 多能带电磁跃迁强度与 DDCM 有限停止慢化时间响应：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| KL99-D20-2 | checkpoint036撤回旧三层相图/构型正交及协方差相消认证。TableII B单位10³e²fm⁴给4g→2g .553(.013)、10S2→8g .009(.002)e²b²、后者Qt.51(.04)eb；旧1.87/.029及.05误差错误。有限停止half-chart只为本任务声明响应，非实际±30%界限/CI。详见KL99-D20-R36-1/R36-2。 | task-multiband-deformation-and-covariance-audit | derived-and-boundary | PDF pp.3-7 Tables I-II; Figs.5-7; nd134-multiband-deformation-result-023.json | true |
## Day20量化审计：130,132Ce基态带B(E2)阶梯、B4/2集体度与三层形变阶梯（checkpoint029）

> checkpoint032：本节旧认证已撤回；程序通过只曾检自设输入。以下R32为本次定向原读纠正。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| KL99-D20-3 | checkpoint032：旧科学认证撤回，原因：Energies not literal TableIII; photon-branch-one calculation called measured B; unknown ICC/Cov; 130Ce-only z applied to132Ce; central HD difference mistaken for precise shell-locking and rigid shape.；当前可用陈述见下方R32原读纠正。 | withdrawn-task-certification | rejected-and-replaced | checkpoint032; KL99-D20-R32-1 | true |

## checkpoint032：原件定位与科学认证纠正

本次Codex self-audit，原review状态与全部已有claim flags保持；不是新增独立实验或全文阅读认证。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KL99-D20-R32-1 | TableIII原印130Ce Eγ254/456keV、τ181.3(70)/7.65(31)ps；132Ce325/533keV、70.1(32)/3.9(10)ps。精确能量、ICC、branch与跨点Cov未由此表恢复；旧自设小数能量、B值实验认证与两核10σ说法撤回。 | literal-table-and-conversion-boundary | direct-original-and-visual | PDF5 TableIII | true |
| KL99-D20-R32-2 | 用整数印能量且声明pureE2/photonbranch1，计算B42≈1.27081与1.51508；仅为条件控制。独立寿命线性误差约.07113/.39459，未知Cov会改变这些量；不恢复实验CI、证明γ软或壳锁定。 | conditional-rate-control | task-derived | PDF5 TableIII; evidence-repair-result-032.json | true |

## checkpoint033：观测量身份与形状约定原读纠正

本次为定向原文/表图self-audit，非新增独立实验或全文认证；原review和claim flags保持。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KL99-D20-R33-1 | TableII 134Nd g.s.b.2/4/6/8+的Eγ为294/495/631/706keV；旧020的4+552、6+687错误。按声明有限差分J1(6)=11/.631≈17.4326 ℏ²/MeV，不是配对能隙或HD惯量。 | ordered-energy-and-model-boundary | direct-original-and-task-derived | PDF4 TableII; observable-identity-shape-result-033.json | true |

### checkpoint036：逐表单位、速率身份与响应边界

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| KL99-D20-R36-1 | TableII B单位10³e²fm⁴，4g→2g 5.53(13)→.553(.013)e²b²、Qt4.40(.05)eb；10S2→8g 925keV .09(.02)→.009(.002)e²b²、Qt.51(.04)eb。不同parent与跨带/带内角色不构成形变商或构型正交排他证据。 | literal-units-and-matrix-element-role | original-and-conditional | PDF4 TableII caption and rows; PDF6–8 discussion | true |
| KL99-D20-R36-2 | TableI六corrected行std/corr误差保原列：6g .04/.06、8g .06/.10、8gamma .20/.30、10S1 .02/.04、12S1 .02/.04、16S2 .11/.13ps。TableII adopted误差另含stopping处理。电子stopping+30%原叙述不是全轨迹重标或完整新fit；声明affine half-chart的Qt比小变不认证actualCov消除/实验精度。 | literal-error-role-and-response-boundary | original-and-conditional | PDF3 TableI and stopping paragraphs; PDF4 TableII | true |


## Day20量化审计：134Nd符合柱塞寿命、S1对决S2多带集体性分歧与邻核系统学（checkpoint138）

> checkpoint146：本节科学认证撤回。旧文本与指纹保存在history-before-repair-146.json。先前原件纠错与原review/flags保留；passed不认证实际实验/结构结论。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| KL99-D20-R138-1 | checkpoint146撤回旧认证；同态/分支/几何/单位与Cov未逐claim重审之前，不恢复旧数据及过强推论。 | withdrawn-task-certification | rejected-and-replaced | checkpoint146; history-before-repair-146.json | true |
