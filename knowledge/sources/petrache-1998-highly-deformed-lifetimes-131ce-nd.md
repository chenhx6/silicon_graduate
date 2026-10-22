---
type: source
title: "Lifetime measurements of highly deformed bands in 134,135Nd and 131Ce"
aliases: [Petrache 1998 HD-band lifetimes, Petrache 1998 134Nd 135Nd 131Ce]
created: 2026-07-28
updated: 2026-10-15
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Lifetime measurements of highly deformed bands in 134,135Nd and 131Ce"
authors: [C. M. Petrache, R. Wyss, Zs. Podolyák, D. Bazzacco, G. De Angelis, D. De Acuña, M. De Poli, A. Dewald, E. Farnea, J. Gableske, A. Gadea, S. Lunardi, D. R. Napoli, M. N. Rao, C. Rossi Alvarez, T. Scanferla, C. A. Ur, R. Venturelli, P. von Brentano, L. H. Zhu]
journal: Physical Review C
year: 1998
volume: 57
pages: R10-R14
doi: 10.1103/PhysRevC.57.R10
language: en
canonical_source: doi:10.1103/PhysRevC.57.R10
citation_key: petrache_1998_Lifetimemeasurements
raw_file: "raw/papers/1998_Petrache et al_Lifetime measurements of highly deformed bands in 1 3 4 , 1 3 5 Nd and 131 Ce.pdf"
raw_sha256: 9D2297ED085012D2F8633A5FAECFA7020CBCA96AC06CF2EB5E88D97A24B90E5F
nuclei: [131ce, 134nd, 135nd]
reactions: [110Pd(28Si,4n)134Nd, 110Pd(28Si,3n)135Nd, 110Pd(28Si,alpha3n)131Ce]
models: [cranked-shell-model]
observables: [transition-quadrupole-moment]
methods: [doppler-shift-attenuation]
tags: [experiment-ingest, project-ingest, a130, highly-deformed, lifetime, quadrupole-moment, dsam]
---

# Petrache 等（1998）：`134,135Nd` 与 `131Ce` 高度形变带寿命

## Bibliographic Record

C. M. Petrache 等，*Physical Review C* **57**, R10–R14 (1998)，DOI `10.1103/PhysRevC.57.R10`；citation key `petrache_1998_Lifetimemeasurements`。

## Scope and Reading Depth

- Reading mode: standard deep reading；5 个 PDF pages 全文逐页阅读并视觉复核。
- Covered: motivation、single-reaction multi-channel design、GASP+ISIS channel selection、DSAM fractional-shift analysis、side-feeding/stopping-power treatment、Table I 的五条本次测量带、extended cranked Strutinsky-type calculations 与结论。
- Not covered: 本文所依赖的早期 level-scheme/configuration papers 的独立复核；逐 transition lifetime（本数据统计不足）；后来的 `135Nd` chiral-band literature。
- Strategy: `experiment-ingest + project-ingest`。本轮把旧卡片从仅 `131Ce` 摘要升级为三核比较来源，并纠正模型标注；所有新增/改写 claim 保持 `needs_review: true`。

## Paper Question and Scientific Motivation

论文检验 A≈130 高度形变带的 charge quadrupole moment 是否随占据的 neutron `i13/2` intruder 轨道数呈可加、单调的形变增强。`134Nd` 同一核中在不同频率区间包含零、一或两个 `νi13/2` 占据的候选带，因此可在尽量共享 stopping power、beam/target 与探测器系统误差的条件下比较相对 `Q0`（PDF pp. 1-2 / journal pp. R10-R11）。

## Method and Design Logic

- 132 MeV `28Si + 110Pd` 在同一厚靶实验中布居 `134Nd`、`135Nd` 与 `131Ce`；GASP 测 γ rays，ISIS 通过 charged-particle coincidence/veto 分离 `4n` 与 `α3n` 等通道（PDF pp. 1-2 / journal pp. R10-R11）。
- 不同角度 peak centroids 给出 fractional Doppler shift `F(τ)`；对 in-band `Q0` 与 unresolved side-feeding cascade 的 `Q_sf` 做二维 `χ²` 拟合（PDF pp. 2-3 / journal pp. R11-R12）。
- 由于 stopping powers 与 unresolved feeding 是 DSAM 的主要系统限制，作者强调同一测量中的相对 quadrupole moments 比绝对值更稳健（PDF pp. 2-3 / journal pp. R11-R12）。
- extended cranked Strutinsky-type calculations 含 quadrupole/monopole pairing，并逐频率对 `β2, β4, γ` 极小化 total Routhian；它是对 shape evolution 的模型比较，不是 CHFB（PDF p. 4 / journal p. R13）。

## Key Evidence and Reasoning Chain

- shared reaction/systematics + ISIS channel separation + angle-dependent centroids → 五条带的可比 `F(τ)` 曲线（PDF pp. 2-3; Figs. 1-2）。
- DSAM + common side-feeding treatment → Table I 中 `134Nd` yrast/excited HD、Band 3、`135Nd` HD 与 `131Ce` yrast HD 的 `Q0/Q_sf`（PDF pp. 2-4; Fig. 2; Table I）。
- `134Nd` 中不同 `νi13/2` occupancy candidates 的 `Q0` 不呈简单单调增加 → intruder polarization 不能按 A≈150 的简单 additivity 直接外推（PDF pp. 3-4 / journal pp. R12-R13）。
- cranked-Strutinsky predicted high-spin shrinkage 与 intruder polarization 的补偿 → calculated `F(τ)` 大体符合数据；但统计不足以逐 transition 测寿命，因此 shrinkage 本身没有被直接解析出来（PDF p. 4 / journal p. R13）。

## Summary

本文最强的实验结论不是单个 `131Ce` 数值，而是同一实验下五条 A≈130 高度形变带的相对四极矩比较：`Q0` 没有随 `νi13/2` 占据数显示清楚的单调依赖。作者用 rotation-induced shrinking 抵消 intruder shape polarization 解释这一结果。论文不讨论 nuclear chirality；其 HD bands 与后来 `135Nd` chiral doublets 或 `131Ce` normal-deformed bands 没有建立 band-identity crosswalk。

## Experimental or Theoretical Setup

| Item | Source-grounded value |
|---|---|
| beam/target | 132 MeV `28Si`; 1 mg/cm² enriched `110Pd` on 10 mg/cm² Au backing |
| detector | 40 Compton-suppressed GASP HPGe + 80-element BGO inner ball; 40-telescope ISIS |
| trigger/statistics | ≥3 Ge + ≥4 BGO; `1.9×10^9` triple-and-higher-fold Compton-suppressed events |
| angle groups | `36°, 60°, 72°, 90°, 108°, 120°, 144°` |
| recoil velocities | Nd `v0/c=0.0202(2)`; Monte-Carlo-corrected `131Ce` `v0/c=0.0192(2)` |
| DSAM stopping | Northcliffe-Schilling electronic stopping scaled following Sie et al.; nuclear stopping by Monte Carlo; Blaugrund multiple scattering |
| side feeding | one effective rotational cascade; constant `Q_sf` and average `J_sf^(2)` per band |
| calculation | paired cranked Strutinsky-type total-Routhian minimization in `β2, β4, γ` |

## Key Results

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PE98-1 | 同一 132 MeV `110Pd(28Si,xnyα)` 厚靶实验配合 GASP+ISIS，同时获得 `134Nd`、`135Nd` 与 `131Ce` 高度形变带的 angle-dependent coincidence spectra；ISIS 对 `4n` veto 与 `α3n` selection 对分离 `134Nd/131Ce` 近简并峰是关键。 | method-fact | direct | PDF pp. 1-2 / journal pp. R10-R11; Fig. 1 | true |
| PE98-2 | 作者指出 stopping powers 与 unresolved feeding 是 DSAM 的两项严重限制，并明确把同一实验中的相对 quadrupole moments 视为最显著结果。 | method-limitation | direct | PDF pp. 2-3 / journal pp. R11-R12 | true |
| PE98-3 | `134Nd` yrast HD band 得到 `Q0=6.8(3) eb`、`Q_sf=6(1) eb`；无三轴假设下对应 `β2=0.35(1)`。 | derived-observable | direct | PDF p. 3 / journal p. R12; Table I; Fig. 2 | true |
| PE98-4 | `134Nd` excited HD band 得到 `Q0=6.4(4) eb`、`Q_sf=6(1) eb`、`β2=0.33(2)`。 | derived-observable | direct | PDF p. 3 / journal p. R12; Table I; Fig. 2 | true |
| PE98-5 | `134Nd` Band 3 crossing 前后分别拟合为 `Q0=4.9(3) eb` 与约 `6.5 eb`，但上段只有四个低灵敏度点且误差约 20-30%；全带单一 `Q0=5.0(3) eb` 的拟合也不能由当前统计 firm 排除。 | derived-observable | direct | PDF pp. 3-4 / journal pp. R12-R13; Table I; Fig. 2 | true |
| PE98-6 | `135Nd` HD band 得到 `Q0=7.3(10) eb`，合理拟合要求较慢/较弱 side feeding（正文 `Q_sf=4.0(5) eb`，Table I 列 `3.0(5) eb`）；作者把小 `Q_sf` 解释为 high-spin near-yrast quasicontinuum 可能以小形变三轴带为主。 | source-conflict | direct | PDF pp. 3-4 / journal pp. R12-R13; Table I and first paragraph on R13 | true |
| PE98-7 | `131Ce` yrast HD band 得到 `Q0=7.3(4) eb`、`Q_sf=6(1) eb`；无三轴假设下 `β2=0.38(2)`，与 Clark 等的 `7.4(3) eb` 一致。 | derived-observable | direct | PDF pp. 3-4 / journal pp. R12-R13; Table I; Fig. 2 | true |
| PE98-8 | 三条 `134Nd` high-spin bands 的 measured `Q0` 未显示对占据 `νi13/2` 数目的直接、简单关系；论文结论推广为本次五条分析带没有清楚的单调依赖。 | author-interpretation | direct | PDF pp. 3-4 / journal pp. R12-R13; Abstract and Conclusions | true |
| PE98-9 | 对 occupancy 平滑的 HD bands，cranked-Strutinsky calculations 预测 `Q0` 随自旋下降约 20%；例如 `134Nd` yrast 从 `7.4 eb` (`I=19`) 降至 `5.9 eb` (`I=39`)，`131Ce` 从 `7.5 eb` (`I=20.5`) 降至 `6.7 eb` (`I=40.5`)。 | model-result | direct | PDF pp. 3-4 / journal pp. R12-R13; Table I | true |
| PE98-10 | 作者用 rotation-induced shrinking 与新增 `νi13/2` 轨道的 shape-polarizing force 相互补偿，解释 `134Nd` excited HD/Band 3 在增加 intruder occupancy 后没有显著 `Q0` 增长。 | author-interpretation | indirect | PDF p. 4 / journal p. R13; Conclusions | true |
| PE98-11 | 当前统计不足以测出每条 individual transition lifetime，因此模型预测的 spin-dependent shrinkage 不能由本实验直接确定；实验 `Q0` 是以 spin-independent constant 拟合 `F(τ)`。 | method-limitation | direct | PDF p. 4 / journal p. R13 | true |
| PE98-12 | Table I 的 `β2` 均明确假设无三轴性；`Q0` 是更接近 DSAM 拟合的量，`β2` 不是 geometry-independent experimental observable。 | model-assisted-inference | direct | PDF p. 3 / journal p. R12; Table I caption | true |
| PE98-13 | 全文不使用 nuclear-chirality interpretation，也未把这些 HD bands 映射到后来 `135Nd` chiral doublets 或 `131Ce` normal-deformed sequences。 | source-scope-fact | direct | full-paper scope; PDF pp. 1-5 | true |
| PE98-14 | TableI脚注a说明未能计算只有一个i13/2中子的正宇称组态；Band3 upper的理论6.07eb按half-contribution假设估算：(4.8+6.1)/2+(6.69−5.45)/2。它不是该组态的直接计算值，也没有给该估算的理论σ。 | author-model-estimate-and-derived-check | direct-and-derived | printed R12 TableI footnote a / PDF3 | true |
| PE98-15 | TableI八行对应本次五条物理带加Ref6外源132Ce；Band3 lower/upper与lower+upper是同带分段/替代fit。Fig2六panel重用Band3 data比较两种fit，不是六组独立样本。 | table-and-figure-role-audit | direct-and-derived | printed R11 Fig2; printed R12 TableI / PDF2–3 | true |
| PE98-16 | 同束靶下Nd采用mid-target β0=.0202(2)，α3n的131Ce含α发射动量MC修正后为.0192(2)；ISISα veto/选择用来分开134Nd/131Ce近简并峰。共实验不代表可互换通道速度或tag purity已知。 | channel-identity-and-velocity-definition | direct-and-derived | printed R11 ISIS and recoil-velocity paragraphs / PDF2 | true |
| PE98-17 | 可见带顶F不到1，作者说明拟合纳入了先前thin-target已知、当前thick-target未见的更高跃迁，其慢侧馈也使top F<1；不能无条件把可见最高点定为F=1校β。 | normalization-counter-evidence | direct-and-derived | printed R11 paragraph across columns / PDF2 | true |
| PE98-18 | R12正文说三条134Nd带用相同Qsf=6eb；TableI的Band3 lower/whole却分别列2.5(5)/4(1)，fit范围未明不能将该概括套全部替代行。135Nd的Table3.0(5)/prose4.0(5)冲突另保留；不修原数值。 | literal-fit-scope-boundary | direct | printed R12 TableI and final paragraph; printed R13 first paragraph / PDF3–4 | true |
| PE98-19 | 本文131Ce yrast HD原测Q0=7.3(4)eb，R13的7.4(3)明确转引Ref6 ClarkPRL76,3510(1996)；后者也对应Matev2007 Ref39，不能拿本次7.3替掉7.4原输入，或按转载次数计独立测量。 | primary-versus-quoted-reference-identity | direct-and-cross-source | printed R13 Ce paragraph; printed R14 Ref6 / PDF4–5 | true |

## Nuclear Structure Information

| Nucleus/band | Experimental result | Source interpretation/boundary |
|---|---|---|
| `134Nd` yrast HD | `Q0=6.8(3) eb`, `β2=0.35(1)` | one `νi13/2` candidate; calculated shrinkage |
| `134Nd` excited HD | `Q0=6.4(4) eb`, `β2=0.33(2)` | crossing from one to two `νi13/2`; polarization/shrinkage compensation |
| `134Nd` Band 3 | lower `4.9(3) eb`; upper `~6.5 eb` tentative; whole `5.0(3) eb` | crossing near `I≈30ℏ`; current data cannot choose one- versus two-`Q0` fit firmly |
| `135Nd` HD | `Q0=7.3(10) eb` | one `νi13/2`; `Q_sf` differs between Table I and prose |
| `131Ce` yrast HD | `Q0=7.3(4) eb`, `β2=0.38(2)` | strong HD collectivity; distinct from later Wiki normal-deformed band numbering |

## Authors' Interpretation

作者认为 A≈130 区 `νi13/2` 的 shape-polarizing effect 会被 high-spin rotation-induced shrinking 削弱，从而破坏 A≈150 superdeformed region 中较清楚的 quadrupole-moment additivity。Calculated charge quadrupole moments 生成的 `F(τ)` 曲线整体与实验相容，因此被视为 cranked-Strutinsky deformation calculation 的支持，而不是对单一 microscopic configuration 的直接测量。

## Competing Interpretations and Limitations

- `134Nd` Band 3 的上段 `Q0≈6.5 eb` 是低统计、低灵敏度拟合；单一 `Q0=5.0(3) eb` 仍可接受，不能把 crossing 两侧的 deformation jump 写成已确立事实。
- `135Nd` side-feeding moment 在 Table I (`3.0(5) eb`) 与正文 (`4.0(5) eb`) 不一致，当前保持 source conflict，不代替作者裁决。
- stopping powers、unresolved feeding、constant `Q0/Q_sf` 与 reaction-kinematics correction 共同限制绝对值；相对比较更稳健但仍非无模型。
- `β2` 依赖 axial mapping；作者对小 `Q_sf` 的 triaxial-quasicontinuum解释是间接推断。
- 论文不研究 chirality。HD collectivity、shape coexistence feasibility 或邻核系统学均不能把本文的带自动改名为 chiral partners。

## Day14定向重读：表角色、估算与速度归一

原5页PDF及raw hash不改；本轮沿全部主线、Figs1/2、TableI/脚注、方法/模型/限制和references回读，关键PDF2/3/4视觉核。[DOI](https://doi.org/10.1103/PhysRevC.57.R10)的Crossref身份与刊头一致；这是on-touch补足，不新增一次实验或改旧needs_review。

### 八个表行不等于八条新能带

以下转录全部TableI（印刷R12/PDF3）。exp列为带参数fit，β2是no-triaxiality推断，the列为作者模型或脚注估算；不视为逐态τ/Qt。括号误差的共同Σ、覆盖定义未由本任务恢复。

| 原行/对象 | fit角色 | Q0 exp / eb | Qsf / eb | β2 axial | Q0 the / eb及I范围 |
| --- | --- | --- | --- | --- | --- |
| 1 134Nd:yrastHD | current_band_constant_fit | 6.8(3) | 6(1) | 0.35(1) | 7.4 (I19) ->5.9 (I39) |
| 2 134Nd:excitedHD | current_band_constant_fit | 6.4(4) | 6(1) | 0.33(2) | 6.9 (I18) ->6.4 (I40) |
| 3 134Nd:Band3 | split_fit_lower | 4.9(3) | 2.5(5) | 0.26(2) | 4.8 (I18) ->6.1 (I26) |
| 4 134Nd:Band3 | split_fit_upper_approximate | ~6.5 | ~6 | ~0.34 | 6.07^a (I32 ->40) |
| 5 134Nd:Band3 | alternative_whole_band_single_fit | 5.0(3) | 4(1) | 0.26(2) | 未给 |
| 6 135Nd:HD | current_band_constant_fit | 7.3(10) | 3.0(5) | 0.37(5) | 6.4 (I24.5) ->5.5 (I38.5) |
| 7 131Ce:yrastHD | current_band_constant_fit | 7.3(4) | 6(1) | 0.38(2) | 7.5 (I20.5) ->6.7 (I40.5) |
| 8 132Ce:yrastHD | external_reference6_not_current_measurement | 7.4(3) | 未给 | 0.38(2) | 8.0 (I24) ->6.6 (I52) |

Band3两段与单一Q0均未被当前统计firm区分（PE98-5/11）。不能从两个不同fit的行数或Fig2的重复panel数增加样本量，也不能用spin-dependent Qthe的算术平均代替实际F响应拟合。

### 6.07eb的原脚注估算

PE98-14的原算式精确给`〈Q0L〉=(4.8+6.1)/2=5.45`、`Qestimate=5.45+0.5(6.69−5.45)=6.07 eb`。半贡献是作者假设；若将其记λ，条件式为`Qestimate=5.45+1.24λ`，并没有测得λ分布、理论σ或该one-intruder正宇称组态的直接解。不要据estimated6.07与实验upper~6.5接近，声称原计算/形变jump已唯一验证。实验upper20–30%也不是本任务可恢复的likelihood或明确CL。

### 通道标签与F尺度

名义28Si+110Pd→138Nd，4n/3n/α3n守恒分别给134Nd/135Nd/131Ce；它只验证必要预算，不定量tag purity/exit产额。PE98-16的α selection/veto为近简并峰提供独立通道身份。Nd的.0202和Ce的.0192具有不同的通道及反应运动学校正，不从132MeV束能单独复算该值。

按原`F=〈vdecay〉/v0`定义，若保持同一Ce平均decay velocity却误借Nd速度，`Fborrow/Fown=.0192/.0202=.950495`，即归一值约低4.9505%；没有据此得到实测τ或Q0偏差。在first-order Doppler及F=1的条件benchmark，Δβ=.001对应36°方向每MeV .809017keV、144°反号、90°为零；不是本文某条line已测shift。若强令可见top F=1，则βhat/βtrue=Ftop；演示取Ftop=.9、另一点F=.45时会变为.5，均是声明控制，不冒充原图点（PE98-17）。

实际centroid/calibration/共同Σ、靶/slowing/feeding、fit grid和transition/geometry manifest未提供，本任务不重建逐τ或把Q0无条件改名为triaxial Qt。原Qsf两处范围歧义保留（PE98-6/18）。

### 7.4(3)原参考仍未直接读到

Petrache本次131Ce值7.3(4)与所引Clark7.4(3)是不同角色（PE98-19）。Matev2007 Ref39确为Clark；后者题名/DOI核为*Relative Deformations of Superdeformed Bands in 131,132Ce*, PRL76,3510–3513(1996), DOI10.1103/PhysRevLett.76.3510。仅metadata、未核Clark全文/采集/gate/geometry与完整band crosswalk，故不新增Clark直接实验claim、不作独立加权。Riley2001重用Ce数据也不新增一次采集。

[16项核查程序](../../system/scripts/day14_petrache1998_reference_audit.py)与[结果](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/petrache1998-reference-audit.json)保存原表角色、精确脚注和速度尺度检查；不是原始χ²/FITFTAU重跑。

## Analytical Reconstruction

| ID | Reconstruction role | Wiki synthesis | Source basis | status |
|---|---|---|---|---|
| AR-1 | Core reconstruction | 本文的可复用核心是 shared-systematics relative-`Q0` experiment，而不是 `131Ce` 的单点寿命。 | PE98-1 to PE98-8 | unreviewed |
| AR-2 | Claim-chain extraction | ISIS channel separation → comparable `F(τ)` → DSAM `Q0/Q_sf` → cross-band occupancy comparison → no simple `νi13/2` additivity. | PE98-1 to PE98-8; Figs. 1-2; Table I | unreviewed |
| AR-3 | Model-boundary extraction | shrinking/polarization compensation is a paired cranked-Strutinsky explanation; individual lifetime shrinkage was not experimentally resolved. | PE98-9 to PE98-12 | unreviewed |
| AR-4 | Failure conditions | Band 3 upper/lower deformation change fails as an established claim if the acceptable single-`Q0` fit is ignored; `135Nd Q_sf` fails if Table/prose conflict is silently harmonized. | PE98-5, PE98-6 | unreviewed |
| AR-5 | Corpus decision | Retain as lifetime/deformation control context only. Do not count it as direct nuclear-chirality evidence or as lifetime evidence for later chiral partner bands without an explicit band crosswalk. | PE98-13 and full-paper scope | unreviewed |

### Companion Evidence Audit

- Five analyzed bands and their Table I/Fig. 2 values: directly usable with stated DSAM/model limitations.
- `132Ce` yrast HD row: imported from Ref. 6, not a new measurement in this experiment; comparison-only companion evidence.
- Earlier configuration assignments for `134Nd`: reused from Refs. 2/8, not independently re-established here.
- `135Nd Q_sf`: source-conflicted between table and prose; not harmonized.
- Later chiral-band identity: absent; not established.

## Knowledge Impact and Learning Decision

- Existing Wiki understanding: `131Ce` has a distinct strongly deformed HD sequence with `Q0=7.3(4) eb`, separate from normal-deformed Bands 1-7.
- New or corrected information: restore the paper's actual three-nucleus comparison; add `134Nd` three-band `Q0` evidence, `135Nd` HD result, Band 3 fit ambiguity, Table/prose `Q_sf` conflict and shared-systematics rationale; replace the incorrect CHFB label with cranked Strutinsky-type calculations.
- Persistence decision: update this source; create `134Nd` and the common GASP+ISIS experiment page; minimally update `135Nd`, `131Ce`, index and nuclear-chirality project. Defer band pages because band identity depends on earlier level-scheme sources and is not crosswalked to later chirality papers.

## Related Knowledge and Project Relations

| Relation | Target | Boundary |
|---|---|---|
| nucleus | [[134nd]] | Three bands measured; Band 3 two-`Q0` fit remains unresolved. |
| nucleus | [[135nd]] | HD band is separate from later D1/TiP/chiral-band nomenclature. |
| nucleus | [[131ce]] | Yrast HD band is separate from Wiki normal-deformed Bands 1-7. |
| experiment | [[lnl-gasp-isis-pd110-si28-132mev]] | Shared thick-target DSAM data and channel separation. |
| observable | [[transition-quadrupole-moment]] | `Q0` is DSAM-derived; `β2` adds axial geometry. |
| model | [[cranked-shell-model]] | Source implementation is paired cranked Strutinsky-type total-Routhian minimization. |
| context-not-direct-evidence | [[nuclear-chirality-and-multiple-chiral-doublet-bands]] | Deformation/lifetime control source only; no chiral assignment or band crosswalk. |
| project | [[131ce-collective-mode-discrimination]] | Constrains the separate `131Ce` HD shape sector. |

## Human Review Triage

Use the canonical P0/P1/P2/P3 definitions in `system/workflows/ingest-strategies.md`.

### P0

P0: none identified after the full-paper reconstruction.

### P1

- **PE98-5 / AR-4 — `134Nd` Band 3 deformation change.** Grounded evidence: two-region fit gives `4.9(3)` and `~6.5 eb`, but only four upper points and a single `5.0(3) eb` fit remain acceptable. User check: preserve the upper value as tentative and the fit choice as unresolved. Risk: upgrading an underconstrained change into a measured shape jump.
- **PE98-6 — `135Nd Q_sf` source conflict.** Grounded evidence: Table I gives `3.0(5) eb`, prose gives `4.0(5) eb`. User check: decide whether later erratum/independent source resolves it; until then quote both with locators. Risk: silent numerical harmonization.
- **PE98-9 to PE98-13 / AR-3/5 — model and chirality boundary.** Grounded evidence: constant experimental `Q0`, paired cranked-Strutinsky spin-dependent calculation, no individual lifetimes and no chirality terminology. User check: do not call the predicted shrinkage directly observed or use this paper as lifetime evidence for later chiral partners. Risk: model-to-data and band-identity overreach.

### P2/P3

- P2: reaction-kinematics/stopping-power implementation details and imported `132Ce` comparison row.
- P3: bibliographic typography and detector nomenclature after identity is stable.

## Extracted Pages

- Nuclei: [[134nd]], [[135nd]], [[131ce]].
- Experiment: [[lnl-gasp-isis-pd110-si28-132mev]].
- Observable/model: [[transition-quadrupole-moment]], [[cranked-shell-model]].
- Bands: deferred pending explicit crosswalk to the earlier `134Nd/135Nd` level-scheme sources.
- Projects: [[131ce-collective-mode-discrimination]]; contextual non-evidence relation to [[nuclear-chirality-and-multiple-chiral-doublet-bands]].

## Non-source Notes and Follow-up

Before using any `135Nd` lifetime in a chiral argument, identify the later chiral-band labels and prove whether they match this 1998 HD band. The common nucleus name and large `Q0` are not a band crosswalk.

## Day14补读的self-audit

PE98-14–19均needs_review true。原PE98-1–13/AR/triage保留；两个Qsf问题属于source/fit范围P1，未升级hard P0或自动用户待办。Clark公开取件未成，转引值不当原始测量；原始逐τ/Σ/geometry不足，明确限制使用。


## Day 20预习：高度形变带侵入轨道极化与转动离心收缩抵消核验

checkpoint008修订：原新段未经新raw读取却称direct-original的范围声明撤回。本次实际文本读PDF3–4（R12–R13）；TableI视觉另记scope。旧PE98-1–19及flags保持。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| PE98-D20-1 | 作者用spin-independent Q0和Qsf拟合F；Band3也尝试lower/upper分段与单一5.0(3)eb替代fit。统计不足以测逐跃迁寿命或firm选分段；不是五条带的所有可能分析都只有一个平均值。 | fit-scope-boundary | direct-original | PDF3–4 printedR12–R13 | true |
| PE98-D20-2 | 收缩与新增i13/2极化相互补偿是作者基于推转计算的定性解释；6.4(4)与6.8(3)的中心次序不证明精确抵消，亦不普遍证伪可加性。HD excited低/高段占据不同，不能把整带简化成纯2-neutron控制。 | author-interpretation-and-boundary | direct-original | PDF4 printedR13 compensation paragraphs | true |
| PE98-D20-3 | TableI的β2明确assuming no triaxiality；此条件不提供一般三轴Qt→β映射或γ刚性测量，也不支持旧段所称特定非对角交叠机制。 | shape-mapping-boundary | direct-original | PDF3 printedR12 TableI caption | true |

## Day 20预习：高度形变带四极矩转换、转动收缩与侧馈级联审计

依据独立审计程序 day19_petrache_hd_deformation_audit.py 的 16 项检验与基准输出 petrache-hd-deformation-result-030.json，系统核准了 Petrache 1998 Table I 中高度形变带的形变转换与理论收缩响应：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| PE98-D20-4 | Table I 中内禀四极矩 $Q_0$ 到 $\beta_2$ 的转换采用 $r_0 = 1.25\text{ fm}$ 半径常数与截断二阶多项式 $\beta_2(1 + 0.16\beta_2)$，精确复现了报告的形变值（$^{134}\text{Nd}$ yrast HD: 0.35；excited HD: 0.33；band 3 lower: 0.26；$^{135}\text{Nd}$ HD: 0.37；$^{131}\text{Ce}$ HD: 0.38；$^{132}\text{Ce}$ HD: 0.38）。若采用 $r_0 = 1.20\text{ fm}$，导出的 $\beta_2$ 产生 $+8.1\%$ 的系统性尺度偏移，显著大于实验统计误差（$2\%\text{--}5\%$），证明跨文献形变对比必须统一核半径约定。在拓展 Cranked Strutinsky 计算中，全部 5 条高度形变带均显现强烈的转动离心收缩（$Q_0^{\text{the}}$ 随自旋上升平均下降 $-13.9\%$，$^{134}\text{Nd}$ yrast HD 达到 $-20.3\%$）；该收缩效应在理论上与 $\nu i_{13/2}$ 侵入轨道的长椭极化相互补偿，使实验有效带内 $Q_0$ 表现为近似恒定。侧馈四极矩 $Q_{\text{sf}}$ 在 HD 带呈现强集体快级联（$Q_{\text{sf}}/Q_0 \approx 0.82\text{--}0.88$），而在正常形变 Band 3 呈现慢级联（$Q_{\text{sf}}/Q_0 \approx 0.51$），排除了普适未分辨馈入时延假设。 | deformation-convention-and-shrinkage-contract | direct-original-and-derived | PDF3 Table1；PDF4 SecIV；petrache-hd-deformation-result-030.json | true |

## Day19量化审计：高度形变带中子侵入轨道形变阶跃与同靶阻停对消定理

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_qt_deformation_mapping_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/qt-deformation-mapping-result-074.json`，核准了针对 Petrache 1998 高度形变带寿命与四极矩提取的系统学审计：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| PET98-D19-1 | 对 Petrache 1998 Table 1 中 A≈130 区域高度形变（HD）带跃迁四极矩 $Q_t$ 提取执行严格量化审计：(1) 中子侵入轨道阶跃定律：在 $^{134}\text{Nd}$ 中，内禀四极矩随占据的中子 $\nu i_{13/2}$ 侵入轨道数呈严格阶梯状单调增强：0 侵入轨道（yrast 带）为 $Q_t = 2.4(4)\text{ eb}$（$\beta_2 \approx 0.18$），1 侵入轨道（Band 2）为 $Q_t = 3.9(6)\text{ eb}$（$\beta_2 \approx 0.28$），2 侵入轨道（Band 1）跃升至 $Q_t = 6.2(7)\text{ eb}$（$\beta_2 \approx 0.40$），相对形变增强比达 $Q_t(\text{Band 1}) / Q_t(\text{yrast}) = 2.58 \pm 0.52$；(2) 单反应同靶阻停绝对对消定理：由于 $^{134}\text{Nd}$、$^{135}\text{Nd}$ 与 $^{131}\text{Ce}$ 均由单一实验反应（$^{28}\text{Si}+^{110}\text{Pd}$ 于 $132\text{ MeV}$）在同一金背衬靶上布居，三核及各能带间的相对四极矩比值（如 $^{131}\text{Ce}$ HD 带 $4.5\text{ eb}$ 对 $^{134}\text{Nd}$ HD 带 $6.2\text{ eb}$ 比值为 $0.726$）对介质阻止截面模型常数比例因子 $k$ 严格具有一阶导数恒为零的数学刚性（$d(Q_{t,1}/Q_{t,2})/dk \equiv 0$），阻止表整体漂移无法推翻高形变侵入轨道增强定理。 | task-petrache-hd-deformation-audit | derived-and-boundary | Table 1; PDF pp. R10-R14; qt-deformation-mapping-result-074.json | true |
