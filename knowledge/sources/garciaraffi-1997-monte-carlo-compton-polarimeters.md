---
type: source
title: "Garcia-Raffi et al. 1997 - Monte Carlo simulation of Compton polarimeters"
aliases: [Garcia-Raffi 1997 GEANT3 polarimeter simulation]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: method-paper
reading_depth: deep-read
title_original: "Monte Carlo simulation of Compton polarimeters"
authors: [L. M. Garcia-Raffi, J. L. Tain, J. Bea, A. Gadea, J. Rico, B. Rubio]
journal: "Nuclear Instruments and Methods in Physics Research A"
year: 1997
volume: 391
pages: "461-467"
pii: "S0168-9002(97)00389-6"
canonical_source: "https://doi.org/10.1016/S0168-9002(97)00389-6"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1997_García-Raffi et al_Monte Carlo simulation of Compton polarimeters.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1997_García-Raffi et al_Monte Carlo simulation of Compton polarimeters.pdf"
raw_sha256: "2b860327fa3d8e0aeeab31e89b8e337ff8278b24f452b4fb456b6bbda4871e31"
nuclei: []
reactions: []
experiments: [compton-polarimeter-calibration]
models: [geant3-monte-carlo, klein-nishina-scattering]
observables: [polarization-sensitivity, detector-efficiency, figure-of-merit, compton-asymmetry]
methods: [compton-polarimetry, monte-carlo-detector-simulation]
tags: [polarimetry, Compton, GEANT3, detector-response, method]
---

# Monte Carlo simulation of Compton polarimeters

## Bibliographic Record

- L. M. Garcia-Raffi *et al.*, *NIM A* **391**, 461–467 (1997), PII `S0168-9002(97)00389-6`; DOI route recorded above.
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1997_García-Raffi et al_Monte Carlo simulation of Compton polarimeters.pdf`。
- 7-page selectable-text PDF; title-page journal/author/PII identity agrees. The 1997 simulation paper is distinct from the 1995 non-orthogonal polarimeter design paper and is a method-lineage source, not a nuclear-structure experiment.

## Scope and Reading Depth

- PDF pp.461–467 fully read, including introduction, GEANT3 modifications, three configuration comparisons, Figs.1–3, Table I, conclusion and Stokes-parameter Appendix Eqs.(8–16).
- Figure/table audit: five-coaxial, four-coaxial and EUROGAM CLOVER sensitivity curves; detector-size/distance tests; and Table I sensitivity/merit values were checked against the text.
- Not covered: GEANT3 source code, detector-response files, raw calibration spectra and the upstream papers' full data.

## Paper Question and Method Logic

The paper asks whether a polarization-aware Monte Carlo can predict the linear-polarization sensitivity `Q` and statistical merit of realistic Ge/Ge(Li) Compton polarimeters, including multiple Compton scatterings and detector geometry, well enough to supplement sparse online calibration points.

1. Modify GEANT3's `GCOMP` into `GCOMPOL` so the Klein–Nishina angular distribution and outgoing polarization are sampled for each Compton interaction; retain the polarization vector between successive scatterings using a `POLAR` variable and a general rotation routine `GDROT3` (PDF pp.462–463).
2. Treat primary photons as polarized and secondary bremsstrahlung/annihilation photons as unpolarized; compare calculated `Q(E)` with published measurements for a five-coaxial, four-coaxial and CLOVER geometry (PDF pp.463–466).
3. Use the background-free symmetric-polarimeter merit `M=εQ²` to compare sensitivity–efficiency trade-offs at a common 25-cm source distance and 50-keV threshold (PDF p.465, Eq.7/Table I).

## Key Evidence and Reasoning Chain

- The five-coaxial case (threshold 60 keV, scattering-angle window 70°–110°) is reproduced within the experimental uncertainty; the largest deviation is about 12% at the lowest energy, while calculated statistical uncertainty with `10⁶` events is 0.8–4% (PDF pp.463–464, Fig.1).
- For the compact four-crystal configuration, geometry changes of 5 mm alter `Q` by only a few percent, but ignoring polarization after the first Compton scatter underestimates `Q` by about 40% (PDF p.464, Fig.2). This is the key detector-response warning: multiple scattering must carry polarization information.
- The CLOVER comparison also agrees within quoted uncertainties (Fig.3); its sensitivity is lower than the five-crystal limit but its coincidence efficiency is much higher. Table I gives example `Q` values at 0.5/1.5/4.0 MeV and `M=εQ²`, with the compact configurations having larger merit despite lower `Q`.
- The authors conclude that, when geometry, thresholds and response parameters are known, the simulation reaches roughly 10% accuracy and can guide polarimeter design where calibration lines are sparse (PDF p.466).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GR97-1 | A polarization-aware GEANT3 modification reproduces the measured sensitivity of three Compton-polarimeter geometries to about 10% or better. | method-validation | direct | PDF pp.462–466, Figs.1–3 | true |
| GR97-2 | Propagating polarization through multiple Compton scatterings is essential; first-scatter-only treatment underestimates `Q` by about 40% in the four-crystal test. | method-result | direct | PDF p.464, Fig.2 | false |
| GR97-3 | Compact four-crystal/CLOVER geometries trade lower `Q` for higher coincidence efficiency and larger `M=εQ²` than the five-coaxial geometry. | detector-tradeoff | direct | PDF pp.464–466, Table I | true |
| GR97-4 | Geometry, energy threshold, scattering-angle window and source distance are required inputs; the quoted accuracy is not universal. | limitation | direct | PDF pp.463–466 | false |

## Summary

The modified GEANT3/Stokes treatment reproduces the tested five-coaxial, four-coaxial and CLOVER polarization sensitivities and shows that multiple-scatter polarization transport is essential. The result is a response-simulation validation, not a universal detector calibration.

## Competing Interpretations and Limitations

The reported agreement is conditional on known detector geometry, thresholds, source distance, scatter-angle windows and background-free counting. Missing response files and raw calibration spectra prevent an independent rerun; `Q` and `M=εQ²` must not be transferred between arrays without a new response audit.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| GR97-AR-1 | Equation chain | Klein–Nishina/Compton sampling → Stokes-vector propagation → detector coincidence/asymmetry → `Q(E)` and `M=εQ²`. | PDF pp.462–466, Appendix | self-checking |
| GR97-AR-2 | Transfer condition | `Q`/merit values can transfer only after reproducing detector geometry, thresholds, distance and analysis windows; no universal detector constant is implied. | PDF p.465, Table I | self-checking |
| GR97-AR-3 | Failure condition | Missing detector dimensions, multiple-scatter handling, background or calibration line definitions can invalidate a quoted sensitivity. | PDF pp.462–466 | active-L3 |
| GR97-AR-4 | Independence | This method validates response simulation, not an independent nuclear-structure measurement; upstream five-/four-crystal/CLOVER data are cited, not remeasured. | PDF pp.463–466 | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` and `revises` the Compton-polarimetry method map. The 1995 non-orthogonal response functions need a simulation layer; `Q`, efficiency and merit cannot be compared across arrays without geometry and multiple-scatter treatment.
- Persistence: link this source to [[compton-polarimetry]], [[linear-polarization-asymmetry]] and the detector-method project; preserve the 10%-order validation as source-specific, not a universal error bar.
- Review state: Codex self-audited; not `human-reviewed`.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[compton-polarimetry]] | GEANT3/Stokes implementation links detector geometry to `Q` and merit. |
| limits | [[garciaraffi-1995-nonorthogonal-compton-polarimeter]] | Non-orthogonal `Q1/Q2/Q3` response also needs geometry-specific simulation; the 1995 design does not supply a universal shortcut. |
| supports | [[linear-polarization-asymmetry]] | Detector-level asymmetry/polarization conversion requires calibrated, response-aware `Q`. |

## Human Review Triage

### P0

- `GR97-P0-1`: never reuse the quoted `Q` or `M` values for a different detector without a geometry/threshold/angle-window simulation or calibration.

### P1

- `GR97-P1-1`: the paper's approximate 10% agreement is against selected historical datasets and does not provide a complete uncertainty budget for every detector response.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]]。
- Source lineage: [[simpson-1983-sectored-geli-compton-polarimeter]], [[garciaraffi-1995-nonorthogonal-compton-polarimeter]], [[logan-1974-generalized-polarimeter-merit]]。

## L3/L4 Follow-up

- L3 question: can a common response-simulation protocol reconcile `Q`, efficiency and merit rankings across historical Ge(Li), CLUSTER and CLOVER designs using identical thresholds and angular windows? Required counter-checks are multiple-scatter propagation, background and geometry sensitivity.
- No L4 run is started: the PDF contains no code or machine-readable raw spectra; it is a method-validation source only.


## 2026-10-19 Day17无学分预习：原件与响应合同续核

本session重读原7页461–467、Eq1–16、3图/TableI/29refs，Crossref核题名/六作者/391/461–467/1997。旧source完整前缀及GR97-2/4的needs_review=false保留；本节是新self-audit，新增claims均true，未发生本日人审。[[gr97-stokes-response-and-merit]]给完整数据/条件/计算。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| GR97-5 | TableI九项Q/M是source计算，统一距源25cm、每晶体50keV、对称ε=εparallel+εperp；不是九次新实验。M/Q²推回ε仍是同一计算的派生量。 | simulation-and-normalization | direct-table-and-arithmetic | p465 TableI/Eq7 | true |
| GR97-6 | 验证五coax用60keV与70°–110°角窗，四coax150keV、CLOVER60keV；TableI改50keV且未重申同角窗。不同样本的Q/efficiency不能裸合并。 | response-object-boundary | direct-original | pp463–465 validation/TableI | true |
| GR97-7 | 原Eq3/11/13均为(Eprime/E)²前因子；Eq11乘Eq12与Eq13分量、Eq14/15相合。本run先漏读Eq13撇号的假设已由高分辨原图否决，不当source勘误；P00-10的反向字面属于另一paper。 | equation-and-reinspection | direct-plus-algebra | pp462/466 Eqs3/11–15 | true |
| GR97-8 | 原GCOMPOL/POLAR/GDROT3跟踪primary Compton链的偏振；brems/annihilation secondary photons被假定unpolarized并调用原GCOMP。此近似不等于所有光子通道完整偏振输运。 | transport-model-domain | direct-original | p463 firstcolumn/codeparagraphs | true |
| GR97-9 | 几何敏感性并非永远几percent：五coax scatterer长度+5mm给Q降7%，四coax长度+5mm降9%；其它±5mm/±3mm测试有其局部样本条件。 | geometry-counter-control | direct-original | p464 firstcolumn | true |
| GR97-10 | 本run以原TableI推ε和未知Cov(M,Q)局部误差范围；absoluteε比不能与正文active-solid-angle归一的50%/4倍比较，M也不是独立于Q的校准。 | derived-statistics-and-object-boundary | printed-input-calculation | TableI；p464 active-solid-angleparagraph | true |
| GR97-11 | 按印刷中央数/理想独立count/no背景/已知Q条件，M比与有限P时间修正仍偏好紧凑配置；不把此条件设计移作新阵列推荐、实际曝光或误差预算。 | conditional-count-design | Codex-analysis | Eq7/TableI；gr97-stokes-response-and-merit | true |
| GR97-12 | Fig1/2/3图注给Refs24/25/27，而相应正文给22/23/25；保留两者，不静默改号。正文对应von_der_Werth/Bass/Jones的历史数据，本文不增三套独立核结构测量。 | citation-lineage-boundary | direct-original | pp463–465 Figs1–3；pp466–467 refs | true |
| GR97-13 | 五coax Eq6拟合在.3–1.8MeV给a=.79(.17)、b=.0780(.0011)MeV^-1，Cov未给；不同于TableI50keV样本，4MeV也非该fit域。不能调Cov或外推强闭合TableQ。 | calibration-domain | direct-plus-arithmetic | p463 Eq6；p465 TableI | true |
| GR97-14 | Eq9是非负偏振度，线性Stokes分量与参考轴仍带方向/符号；P=A/Q的核实验signedP不能裸换为sqrt(P1²+P2²)/P0。T的正性、2φ旋转与条件出射态混合由本run核验，未重放全GEANT3/原40%MC差。 | magnitude-versus-signed-polarization | original-and-Codex-control | pp465–466 Eqs8–15；p464 Fig2 | true |

原fourcoax1.4/2.1MeV点与quotedband的例外及作者“by only30%”字面保持，不从图补完整z。约10%是作者针对所测几何的估计，非其它阵列或Table4MeV的通用σ。当前缺原修改版producer、事件histograms/材料response与fullCov，L4experimentalreplay仍not-ready；不授正式Day17学分。


前因子跨源比较另见[[palit-2000-rh99-clover-polarimetry]] P00-10；GR97已高分辨核正确，不能把本session被否决的猜测传给后续引用。


### 当前public代码基线不是历史modifiedproducer

[[geant3-vmc-2026-compton-baseline]] G3-1/2/3/5/7给标准Geant3.21+VMC固定pin的实际接口、单位/cuts和600000事件组件核验。所读callpath为G3TGAMA→G3COMP且phiuniform，POLAR字段未参与；这与本文所述改GCOMPOL/GTGAMA/POLAR的需求分层。当前代码/原modifiedproducer、核验组件/真实detectorresponse不合并，也不把文件名检索空结果说成源代码全球不存在。


## Day17本session定向复核：singlepoint分析能力与90度reference

MI07本session完整原6页是此问题anchor；本GR97只新text/visual核printed462 Eq2/3与printed466 AppendixEq11–16两页，raw701800bytes/hash `2b860327fa3d8e0aeeab31e89b8e337ff8278b24f452b4fb456b6bbda4871e31`保持。不把Day16旧7页/600000事件或旧checks换作本次新交付。旧整页前缀/claims/flags/review原字节保，新增四条待审，无新humanreview。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| GR97-D17-1 | Eq3对singleCompton、freeunpolarizedrest-electron/未分析finalpol给sin²θ的φ调制；θ是Compton角、φ是散射平面相对入射E-plane。Eq3/11/13前因子(E′/E)²保持，旧漏prime假设不复活。 | targeted-original-contract | direct-and-self-audit | printed462 Eq2–3; printed466 Eq11–13 | true |
| GR97-D17-2 | 此singlepoint模型q=sin²θ/[t+1/t−sin²θ]，t=1+α(1−cosθ)；90°才化MI07 Eq4。新导数/Descartesquartic证明α>0 globalunique最大角<90°，不是源原MC/装置Q重放。 | task-analytic-maximum | derived-from-original | printed462 Eq2–3 | true |
| GR97-D17-3 | 明示singlecollision两hit各>=T给E′与E−E′的角域；E>2T仍不充分，如E150/T60无解；E333/T150的最佳允许角104.940°/q.650232，非原实际器件效率或SeGA未给阈值。 | task-kinematic-design | derived-from-original | printed462 Eq2–3 | true |
| GR97-D17-4 | singlepoint qmax只限该散射/终态未分析模型；原多scatter偏振输运和实际阵列response不由此认证或受90°reference作统一上界，maxq角也不等maxmerit。没有改任一publishedQ/Qrel/calibrationCov。 | transfer-boundary | source-and-task-scope | printed462 Eq3; printed466 Eq11–16; GR97-2 | true |

[[compton-polarimetry]]“90度点参考不是全角最大分析能力”保存exactquartic/全局证明、energytable与cuts模型。sourcephysicalP/degree和signed实验A仍需匹配轴；本段不是general4-Stokes/全探测器MC。
