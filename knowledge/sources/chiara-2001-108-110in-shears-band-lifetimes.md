---
type: source
title: "Chiara et al. 2001 - Spectroscopy and lifetime measurements in 108,110In"
aliases: [Chiara 2001 108In 110In shears lifetimes, Chiara Ref. 16 for Mukhopadhyay 2008]
created: 2026-10-09
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: experiment-and-method
reading_depth: deep-read
title_original: "Spectroscopy in the Z=49 108,110In isotopes: Lifetime measurements in shears bands"
authors: [C. J. Chiara, D. B. Fossan, V. P. Janzen, T. Koike, D. R. LaFosse, G. J. Lane, S. M. Mullins, E. S. Paul, D. C. Radford, H. Schnare, J. M. Sears, J. F. Smith, K. Starosta, P. Vaska, R. Wadsworth, D. Ward, S. Frauendorf]
journal: Physical Review C
year: 2001
volume: 64
pages: "054314"
doi: "10.1103/PhysRevC.64.054314"
canonical_source: "https://doi.org/10.1103/PhysRevC.64.054314"
publisher: American Physical Society
language: en
citation_key: ""
raw_file: "raw/papers/gpt/high-spin-20261009/2001_Chiara et al_Spectroscopy in 108,110In isotopes_Lifetime measurements in shears bands.pdf"
raw_sha256: "5672ffce1e4049245b3107e6132af0ff7501d14182a03d803cd66828e6660a4e"
nuclei: [108in, 110in]
experiments: [Stony-Brook-six-Ge-array, 8pi, DSAM-backed-target]
observables: [lifetime, branching-intensity, B(M1), B(E2), transition-multipolarity]
methods: [Doppler-shift-attenuation, LINESHAPE, gamma-gamma-coincidence]
tags: [108in, 110in, lifetime, branching, shears-band, internal-conversion]
---

# Chiara et al. (2001): `108In/110In` lifetimes and branching-to-strength method

## Bibliographic Record

- C. J. Chiara *et al.*, *Phys. Rev. C* **64**, 054314 (2001), DOI `10.1103/PhysRevC.64.054314`.

### Access and local original

下列网络访问记录属于2026-10-09原摄入；本次Day17只重核本地同hash原件并扩展实际阅读范围，不新称OA许可或网络body取得。

- Crossref metadata resolves the author order, title, journal, volume and DOI. The official APS abstract page exposes the standard `citation_pdf_url`; the HTTPS publisher PDF endpoint returned HTTP 200 with `application/pdf` and a valid `%PDF-1.3` body in this run.
- Unpaywall reports `is_oa=false`, `has_repository_copy=false`, and no OA locations; the exact arXiv DOI query returned zero records. The file was obtained from the directly accessible official APS publisher endpoint, not an OA repository. No institutional login or challenge was used. The APS article page had no supplement link; no SI file was found there.
- Raw PDF: `raw/papers/gpt/high-spin-20261009/2001_Chiara et al_Spectroscopy in 108,110In isotopes_Lifetime measurements in shears bands.pdf`; 440,801 bytes; SHA-256 `5672ffce1e4049245b3107e6132af0ff7501d14182a03d803cd66828e6660a4e`.

## Scope and Reading Depth

- 原2026-10-09 targeted reading for MU08 Ref. [16]: PDF p.1 abstract; p.7 Table III intensity-normalization caption; pp.18–19 Sec. IV.C DSAM analysis, Eqs. (2)–(3), and Table V; p.29 conclusions.
- The article covers separate `108In` and `110In` level schemes, DSAM lifetimes, reduced strengths and TAC comparisons. This source note captures the cited lifetime/branch/ICC procedure and its limits, not every band assignment or model comparison in the full article.
- 原目标阅读当时未覆盖完整level-scheme/TAC主线；本次新增范围见下。原raw spectra、历史LINESHAPE producer/inputs与fullfitΣ仍未取得。

本session新冻结强priming回忆后，完整读30页/printed054314-1–30、Figs1–21、TablesI–VII与Eqs1–3及末页references，文本/视觉全部主线检查。旧freeze预期29页保原，实际metadata/最后参考文献页显示30；没有声称全部levelgraph/每一intensity独立重建或raw谱重拟。[完整scope](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/chiara2001-full-reading-scope.json)。

TableI直接表明StonyBrook六Ge与8π两阵列；本次据原件纠正旧frontmatter的Gammasphere误标，review状态与旧CHI01-1–6全保持。

## Lifetime-to-Strength Procedure Relevant to Ref. [16]

For the backed-target analyses, angle-dependent coincidence spectra were fitted with LINESHAPE. The `108In` transition intensities used in that fit came from efficiency-corrected broadened-peak counts normalized to a stopped transition lower in the cascade; the authors note that the thin- and backed-target `108In` datasets used different reactions and could populate high-spin states differently (PDF p.18, Sec. IV.C).

The paper converts fitted level lifetimes to partial transition lifetimes using the observed branching ratios, then calculates `B(M1)` or `B(E2)` with the transition energy and partial lifetime. Internal-conversion effects are included and described as small. `ΔI=1` dipole lines are treated as predominantly pure M1 with minimal E2 admixture (`δ≈0`); where an E2 crossover is not observed within experimental sensitivity, its crossover intensity is assumed to be zero (PDF p.19, Eqs. (2)–(3) and text following the equations; Table V caption).

Table III reports efficiency-corrected `108In` intensities normalized to 100 for the 213-keV reference transition (PDF p.7, Table III caption). Table V then tabulates the fitted level lifetime, M1 and E2 transition energies/intensities where observed, and derived strengths; its caption states that lifetimes are adjusted for branching ratios and internal conversion. Those relative-intensity and observed-branch procedures do not, by themselves, demonstrate a complete absolute photon-per-parent ledger for every level.

The fit errors include covariance between in-band and side-feeding lifetimes, but quoted errors omit stopping-power-model systematics that may reach ±20% (PDF p.18, Sec. IV.C; PDF p.19, Table V caption). The original analyses use data and bands specific to `108In/110In`; they are a methodological precedent, not independent evidence for a `136Nd` branching denominator.

## Key Results

| ID | Statement | claim_kind | evidence_level | source_independence | locator | needs_review |
|---|---|---|---|---|---|---|
| CHI01-1 | The paper reports DSAM lifetimes for four `ΔI=1` and one `ΔI=2` bands in `108In/110In`, together with reduced transition strengths for the dipole bands. | experimental-fact | direct | single | PDF p.1, abstract | true |
| CHI01-2 | The authors derive partial `τ(Mλ)` from fitted level lifetimes and observed branching ratios, include internal-conversion corrections in `B(M1)/B(E2)`, and give the rate formulas in Eqs. (2)–(3). | experimental-method | direct | single | PDF p.19, Eqs. (2)–(3) and paragraph below | true |
| CHI01-3 | The dipole transitions are treated as nearly pure M1 (`δ≈0`); if an E2 crossover is not observed within experimental sensitivity, its crossover intensity is assumed to be zero. | analysis-assumption | direct | single | PDF p.19, paragraph below Eqs. (2)–(3) | true |
| CHI01-4 | Table III intensities are corrected for detector efficiency and normalized to 100 for the 213-keV reference line; Table V uses branch/IC-adjusted partial lifetimes and propagates lifetime-fit errors to the strengths. | evidence-boundary | direct | single | PDF p.7, Table III caption; PDF p.19, Table V caption | true |
| CHI01-5 | In-band/side-feeding lifetime covariance is included in the fit-derived uncertainty, while stopping-power systematic errors are excluded and may reach ±20%. | method-limitation | direct | single | PDF p.18, Sec. IV.C, uncertainty paragraph | true |
| CHI01-6 | For the `108In` Band 2 `15−` Table V row, the two listed observed gamma intensities are `31.6` for the 527.8-keV M1 line and `2.0` for the 864.2-keV E2 crossover. Dividing only these two entries by their sum gives relative shares `0.9405` and `0.0595`; these are shares of the two listed observed photon intensities, not absolute per-parent photon probabilities or a complete all-channel branch ledger. | our-inference | indirect | single | PDF p.19, Table V, `I=15−` row | true |
| CHI01-7 | 本session完整原读实际30页/21图7表3式和references；旧Day9仅targeted。TableI将旧metadata Gammasphere误标纠正为SB六Ge/8π，rawhash不改，仍unreviewed而非humanreview。 | identity-scope-and-metadata-revision | direct-paper-and-hash | same-original-not-new-measurement | PDF1–30；TableI | true |
| CHI01-8 | 四campaign分别108In thin76Ge(37Cl,5n)138MeV/8π、backed94Mo(18O,p3n)85MeV/SB，110In thin96Zr(19F,5n)85与backed88MeV。thin µg/cm²与backed mg/cm²不可读同单位，只有两backed数据做本次DSAM。 | actual-experiment-identity | direct | separate-campaigns-shared-method | PDF2–3 TableI | true |
| CHI01-9 | 108In因thin/backed反应不同，line-shape用backed broadened峰全积分/eff校正及低线归一估energies/intensities；110In用同反应thin数据的energy/intensity。表V/VI输入列不能跨thin/backed裸替，组合levelscheme不等共用feeding。 | actual-input-provenance | direct | dataset-roles-explicit | PDF18 SecIV.C | true |
| CHI01-10 | R_DCO=Iγ(F/B,90)/Iγ(90,F/B)为SB特定角矩阵；TableII用σI/I=.3 Gaussianalignment作模型预测，pureD/Q门不同，ΔI0/1/mixed有重叠。由known邻核transitions核预测，不是可迁任意array的常数或唯一δ。 | actual-angular-contract | direct | instrument-specific | PDF3 Eq1；PDF4 TableII | true |
| CHI01-11 | 108In band3 link DCO不能区分E1与near-pureM1，作者采用Ref24偏振赋positiveparity；110In band3采用Ref25旧pol/E1。是本文对旧P证据的采用，本次未新读这些prior bodies或重验其P/A/Q校准，不计新偏振实验。 | necessary-polarization-companion | direct-author-adoption | shared-prior-data-boundary | PDF6 SecIV.A3；PDF15 SecIV.B2 | true |
| CHI01-12 | LINESHAPE用5000 velocityhistories/2fs、shell-corrected NorthcliffeSchillingstop至初能.1%、逐level再globalfit。5步SF先effectiveQ后换独立τ，108band2还纳入已测band3feed；quotedfit含inband/SFCov，但stop系统最高±20%未含。 | actual-fit-and-uncertainty-contract | direct | same-fit-derived-strengths | PDF18 SecIV.C；TablesV/VI | true |
| CHI01-13 | 108band3 I16+除357.3M1外有1220.5E1(3→2) depop。backed I16.8/2.5与τ.432的visibleγ-only/α0/δ0 control给pM1.870466、partialτ.496286ps、BM1 2.51351；只rate表一列会2.88755。原reported2.48保持，不将控制称完整branch或独立重测。 | actual-parent-inventory-control | derived-and-boundary | shared-tau-intensities | Fig2；TableIII1220.5；TableV16+；branch-result | true |
| CHI01-14 | 110band3(18+)要计366.9link(.8)与565.6M1(13)/1052.3E2(1.5)同parent。γ-only control BM1 1.36326/BE2.0316327，原1.35/.029分列，E2中心约9%未闭合保留；不反解α/δ或调整branch/ρ来强配，原IC/fullledger/Cov未得。 | actual-linked-parent-and-nonclosure | derived-and-boundary | shared-parent-chain | Fig3；TablesIV/VI(18+)；branch-result | true |
| CHI01-15 | 110band3(19+)作者thin6.2/.9给γ-only BM1 2.51663/BE2.0514789；故意替backed2.1/.7会2.16146/.101528。条件BE2比1.97222、同G Qt比1.40436，仅示输入误换可制造形变差，不是作者实际Qt或实验更正。 | provenance-countercontrol | derived-and-boundary | same-source-not-independent | TableIV572.9/1138.6；TableVI(19+)；branch-result | true |
| CHI01-16 | MR bands的B(M1)在alignment前下降、附近可上升；作者解释新对齐粒子形成更长blades再关闭。fixedK估计与TAC比较亦受g7/2/d5/2 admixture(可约35%)与g_s attenuation .6影响，不能要求全I域单调或按幅度单独定组态。 | structure-interpretation-and-model-boundary | direct-author-interpretation-and-model | model-versus-derived-data | PDF21–23 Figs12–14 | true |
| CHI01-17 | 作者把large J2/BE2明确视为necessary-not-sufficient，weakpairing/smalldeformation也可能大。110band5已测BE2在postalignment约.265–.281而非确认下降；17点在crossing受mixing，AMR解释仍需下降/companion检验。 | counter-evidence-to-mode-sufficiency | direct-author-limitation | same-data-derived-ratio | PDF2；PDF25–26 Fig17 | true |
| CHI01-18 | TableVI四个110band5寿命点ωmax=.536MeV/hbar，作者预测B(E2)明显下降在>.70；TableIV的(27-)/(29-)1419.1/1626.8分别对应.70955/.8134但无该文τ/B。是新测高频率lifetime/feeding的具体companion，不能把已见line当已测strength。 | actual-coverage-and-design | direct-plus-arithmetic | energy-data-not-new-lifetime | TablesIV/VI；PDF25；branch-result | true |
| CHI01-19 | 未shift的108band5/110band4 roughτ>1.2/1.1ps与BE2<.09/.10依equalinbandQ和SF约20%faster等条件。作者明确slowSF可能解释与modelBE2≈.23差，当前不能检验；缺shift不独立测小shape，不能把roughbounds升级统一CL。 | feeding-alternative-and-limit | direct-author-model-and-boundary | conditional-limit-not-new-fit | PDF26 SecVB | true |
| CHI01-20 | TAC/PAC的ε2/γ来自energyminimization网格.01/5°，protonpairing0、neutronΔ.85/.91MeV固定、staticj忽略quantumfluctuation。smallj/高频spin1–4hbar残差与pairing/config问题保留，TableVII形状是模型不等Qt/β实验测量。 | model-assumptions-and-failures | direct-model | not-independent-shape-observable | PDF19–25 TableVII/Figs11/14/16 | true |
| CHI01-21 | 110bands8/9 parities/configs有tentative与可交换alternative：交换更合alignments但不合Routhianordering/crosstalk，作者偏好原assignment；未有这些bands的lifetime。不能用theory-assigned parity再当独立验证该theory。 | competing-configuration-boundary | direct-author-comparison | interpretation-not-direct-spin-fact | PDF27–28 Figs19/20 | true |
| CHI01-22 | 全文只给B(M1)/B(E2) partial-rate Eq2/3，没有bandQt直接换算/轴公式；SFQ先作effectiveτ参数后替换，不是静态Qs/Qt。methodRef16因此仍不能指定MU08 actualQtgeometry/historicalproducer。 | verified-geometry-source-boundary | full-paper-negative-check | method-not-data-transfer | PDF18–20 Eqs2/3；fullreading-scope | true |
| CHI01-23 | 新fullread与三个parent forwardcontrol没有原rawspectra/stopinput/code或actualΣ，原IC已含但数值未取；所有derivedB/Qt对照只conditional，不给新τ/B/shape/CI或独立显著性。方法相似与同array名不能合并多核素误差预算。 | readiness-and-reproducibility | synthesis-with-primary | shared-inputs-explicit | branch-contract/result；CHI01-9/12 | true |
| CHI01-24 | 新判断supports τ/branch数据来源与MR多观测链，revises旧array误标与两列即fullbranch习惯，limits大J2/BE2/无shift/模型ε2对AMR与形变的保证。原CHI01-1–6/review状态保持，新claims全needs_review，仅Day18无学分preview。 | knowledge-impact-and-scope | synthesis | no-new-experiment-or-course-credit | CHI01-7/13/17/19/22 | true |

## Summary

Chiara *et al.* provide a directly readable precedent for extracting partial M1/E2 transition lifetimes from DSAM-fitted level lifetimes, observed branching ratios and internal-conversion corrections. Their published choices include a nearly pure-M1 assumption for dipole transitions and setting an E2 crossover to zero when no crossover is seen within sensitivity. These details help interpret the procedure cited by MU08, but do not identify MU08's line-by-line branch denominator or prove that its `136Nd` ledger is complete.

## Competing Interpretations and Limitations

- The tabulated transition intensities are efficiency corrected and normalized to a reference gamma ray; this is a relative intensity scale and is not by itself an absolute photon-per-parent ledger.
- The published `108In/110In` branch and conversion choices are method examples. They should not be transferred as measurements or exact settings for MU08's distinct `136Nd` experiment.
- The line-shape lifetime fit includes in-band/side-feeding covariance, but quoted lifetime uncertainties omit stopping-power systematics that may reach ±20%.
- No raw event data, detector response, original LINESHAPE input, or complete per-parent channel inventory was available in this targeted read.

## Extracted Pages

- PDF p.1: title, abstract and experiment overview.
- PDF p.7: Table III efficiency correction and reference-line normalization caption.
- PDF pp.18–19: Sec. IV.C DSAM analysis, partial lifetime/strength Eqs. (2)–(3), Table V caption and uncertainties.
- PDF p.29: conclusions; the lifetime and strength results are interpreted as shears-band evidence for the studied indium isotopes.

## Knowledge Impact and Learning Decision

- Effect: `methodological-bridge` to [[mukhopadhyay-2008-136nd-transition-rates]]; the cited article's identity, method text and access route are now directly checked.
- The branch-normalization/complete-channel gap in MU08 remains open because Chiara et al. describe their own `108In/110In` analysis, not the detailed `136Nd` line-by-line photon ledger.
- Review state remains `unreviewed`; this direct source audit is Codex self-audit, not human review.

## 本session完整主线与实际分支练习

[读取前冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/chiara2001-full-before.md)、[原件identity/hash](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/chiara2001-full-identity.json)、[30页scope](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/chiara2001-full-reading-scope.json)、[量化前冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/chiara2001-branch-exercise-before.md)、[实际输入](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/chiara2001-branch-contract.json)、[程序](../../system/scripts/day17_chiara2001_branch_provenance.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/chiara2001-branch-result.json)。

| parent | 作者采用intensity来源 | 此处可见支路(E keV;Iγ) | γ-only控制 / 原报告 |
| --- | --- | --- | --- |
| 108In B3 16+ | backed | 357.3;16.8 与1220.5 E1;2.5 | BM1 2.51351 / 2.48 |
| 110In B3 (18+) | thin | 565.6;13、1052.3;1.5、366.9 link;.8 | BM1 1.36326 / 1.35；BE2 .0316327 / .029 |
| 110In B3 (19+) | thin | 572.9;6.2、1138.6;.9 | BM1 2.51663 / 2.51；BE2 .0514789 / .051 |

γ-only controls声明α0/δ0与仅可见photon库存；原计算已含IC，数值并非本任务复原。保110(18+) E2中心差和全部Cov/漏枝边界，不反推α/ρ强配、不将共享τ/branch的两列做独立显著性。作者已按其说明选择相应来源，误替列control不是论文更正。

### 哪个观测能真正提高AMR解释的信息

110In band5已有的lifetime点ω≤.536MeV/hbar，尚未覆盖作者预测>.70的下降域；已见但未测τ的(27-)/(29-) E2候选分别在.70955/.8134。优先补这些态的lifetime及same-gatefeeding约束，比重复低频已测B或把高频J2与低频近constantB直接拼成ratio更有判别力。该design以原spin/parity候选和E2 assignment为条件，不授新实验/置信度。

此前source只作为MU08方法ancestor；完整body仍未给bandQt的直接轴公式，MU08-17的candidateG和原needs_review保持。StonyBrook/8π与MU08 Gammasphere/BLUE也不是同response，不能跨文迁stopping百分数或偏振Q。
