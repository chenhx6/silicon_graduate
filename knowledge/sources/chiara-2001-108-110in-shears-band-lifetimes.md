---
type: source
title: "Chiara et al. 2001 - Spectroscopy and lifetime measurements in 108,110In"
aliases: [Chiara 2001 108In 110In shears lifetimes, Chiara Ref. 16 for Mukhopadhyay 2008]
created: 2026-10-09
updated: 2026-10-25
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

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

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

## Day19量化审计：剪刀带磁转动巨大跃迁比、AMR平坦线与靶强度溯源控制

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_chiara01_shears_amr_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/chiara01-shears-amr-result-052.json`，核准了 $^{108,110}\text{In}$ 剪刀带磁转动与反磁转动电磁跃迁率的物理判决边界：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| CHI01-D19-1 | 对 Table VI 中 $^{110}\text{In}$ 能带的跃迁率进行系统学审计：(1) 剪刀带磁转动指纹：Band 3 在 $18^+$ 与 $19^+$ 态导出极高比值 $B(M1)/B(E2) = 46.55$ 与 $49.22\text{ \mu}_N^2/(e^2\text{b}^2)$，比常规集体转子（$\sim 0.3$）高出超 150 倍，严格印证了磁偶极矩剪刀角关闭机制；(2) 反磁转动（AMR）平坦线判决：Band 5（候选 AMR）在带交叉后的三个纯态（$19^{(-)}, 21^{(-)}, 23^-$）随转动频率变化具有微弱正斜率（$+0.185\text{ e}^2\text{b}^2/\text{MeV}$，四极跃迁强度变化 $+6.0\%$），在已测频率窗口（$\hbar\omega \le 0.536\text{ MeV}$）内完全未观测到理论预测的 $B(E2)$ 塌缩；理论剪刀闭合塌缩预言在 $\hbar\omega > 0.70\text{ MeV}$，而该高频段已观测到的 $(27^-)$（1419 keV）与 $(29^-)$（1627 keV）尚未获得能级寿命测量，因此 $^{110}\text{In}$ Band 5 仍为未决 AMR 候选；(3) 靶强度溯源控制：若将带衬靶强度误代入无衬薄靶，将引入 $1.972\times$ 的表观 $B(E2)$ 虚假阶跃与 $1.404\times$ 的 $Q_t$ 畸变，确立了跨靶态光子归一谱系不可混用的数据契约。 | task-shears-and-amr-audit | derived-and-boundary | PDF pp.18-20 Tables V-VI; chiara01-shears-amr-result-052.json | true |

## Day19量化审计：磁转动B(M1)单调暴跌、反磁转动B(E2)四次方塌缩与手征转动四路全景判决

**checkpoint088：撤回旧科学认证；原标题保留为历史anchor。**

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| CHI01-D19-2 | 撤回checkpoint080的四路排他认证。手填jp/jn、B0和相位后检查自身数值只构成toy模型；不是108In或106Cd实测轨迹。MR的B(M1)可在对齐处增加；理想对称AMR横向磁矩抵消不能泛称所有奇极跃迁由宇称禁戒；chirality的强度/交错判据有模型适用域，不能由硬填180度或双比值唯一裁决106Ag。寿命还取决于能量、全部支路、ICC及混合，不能按模式标签固定窗口。 | source-and-analysis-correction | direct-where-reread-otherwise-withdrawn | checkpoint088 source scope and rejection registry | true |
## Day21周考推断阶梯审计：磁转动寿命测量与电四极深度受抑判据

依据独立审计程序 `system/scripts/day21_checkpoint008_magnetic_rotation_shears_audit.py` 与审计产物 `outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/magnetic-rotation-shears-audit-008.json`，确立本源在推断阶梯上的边界：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| CHI01-D21-1 | **superseded at checkpoint098**：旧7+→10+及1.75→.28轨迹不在TableV，旧绝对寿命/强度认证撤回；使用CHI01-D22-R098-1/2的实际态和范围。 | task-correction | rejected-and-replaced | 054314-19 TableV; checkpoint098 | true |

## Day22 checkpoint098：真实寿命窗口和对齐上扬

本次只回读054314-18–19和21–23相关正文，并视觉核p.19 TableV与Fig12；不重称全文30页新读。原source已有的完整阅读范围保持。

| ID | Statement | claim_kind | evidence_level | source_independence | locator | needs_review |
|---|---|---|---|---|---|---|
| CHI01-D22-R098-1 | TableV的108In Band2实测寿命态为14−/15−/16−，B(M1)=.911/.600/.398 μN²；Band3的16+/17+/18+/19+给2.48/2.38/1.71/5.22 μN²，18+→19+的中央商约3.05。旧CHI01-D21-1中7+→10+、1.75→.28的轨迹不在该表，不应引用。表给τ经branch/ICC后导出B，误差未含最高约20%的stopping系统量；不是裸τ直接等B。 | measured-strength-and-identity-correction | direct-original | same-DSAM-dataset | 054314-19 TableV; 054314-18 uncertainty paragraph | true |
| CHI01-D22-R098-2 | 作者明确B(M1)在各组态随spin降低、在alignment附近可升高，并以新对齐粒子形成更长剪刀后再闭合作解释；TAC在对齐后spin高估约1–2ℏ、pairing/低j混合问题保留。因此MR不要求跨组态全段单调B(M1)，比值或固定阈值不能单独认证叶片机制。 | author-interpretation-and-model-limit | direct-original | same-data-model-comparison | 054314-21–23 SecVA/Figs12–14 | true |


## Day23：不改计数的已发表组态交换与可检验连接

本次沿既有全文阅读继续核PDF18–20、23–28及TableIV p.11；视觉核p.19 TableV、p.23 alignment文字、p.11的748.4行，未新称全30页重读。原hash/flags不变；以下均needs_review:true。

| ID | 陈述 | claim_kind | evidence_level | source_independence | locator | needs_review |
|---|---|---|---|---|---|---|
| CHI01-D23-1 | 作者原方案将110In bands8/9分别联系到BEF/EFG三准中子组态；p.28明确可交换两组态，因为两带parity只tentative。交换更合observed alignments，却不能重现Fig19的Routhian相对次序或解释bands3/8 crosstalk，故作者偏好原方案。这是不改实测计数/能级、只改解释层mapping的已发表竞争方案，未获得同等可信度；本节未测这些弱带τ。 | published-configuration-alternative | direct-original | same-dataset-model-comparison | printed054314-27–28 Sec.V.C and Figs.19–20 | true |
| CHI01-D23-2 | TableIV列748.4(1)keV为8→3连接，印刷path为(18+)→(17+)，Iγ,thin=1.0(.1)、Iγ,backed=.2(.1)，Mλ标M1/E2，两个RDCO栏空白。这不是本篇对该线新增实测δ/P或独立确定parity。作为检验组态交换的候选须先确认该placement/spin及band3 parity，不能按表的假定M1/E2标签反过来认证原组态。 | transition-identity-and-unmeasured-companion | direct-original-and-boundary | same-event-samples-and-assignment | printed054314-11 TableIV, 748.4-keV row; printed054314-28 alternate-assignment paragraph | true |

Knowledge Impact and Learning Decision：supports多观测共同判断组态，limits只用alignment排序或将tentative parity当独立测量；本task提出的连接性质补测见[[signature-tip-shears-discrimination-contract]]。本文的MR/AMR实测与TAC/PAC边界也校准[[shears-mechanism]]和[[antimagnetic-rotation]]，不移植其τ/Q/机时到Pr/Au。
