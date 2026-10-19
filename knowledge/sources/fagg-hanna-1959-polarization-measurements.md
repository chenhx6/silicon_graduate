---
type: source
title: "Fagg and Hanna 1959 - Polarization measurements on nuclear gamma rays"
aliases: [Fagg Hanna 1959 polarization]
created: 2026-09-21
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: review
reading_depth: deep-read
title_original: "Polarization Measurements on Nuclear Gamma Rays"
authors: [Lawrence W. Fagg, Stanley S. Hanna]
journal: "Reviews of Modern Physics"
year: 1959
citation_key: fagg_1959_Polarization
volume: 31
pages: "711-758"
doi: "10.1103/RevModPhys.31.711"
canonical_source: "Fagg & Hanna, Rev. Mod. Phys. 31, 711-758 (1959)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1959_Fagg_Hanna_Polarization Measurements on Nuclear Gamma Rays.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1959_Fagg_Hanna_Polarization Measurements on Nuclear Gamma Rays.pdf"
raw_sha256: "bb3571150d4c552dc5acdbd148546acc7eea4f07dce907eaf0d82377191cb2ee"
nuclei: [generic]
reactions: [radioactive-source, nuclear-reaction, Coulomb-excitation]
experiments: [Compton-polarimetry, photodisintegration, photoelectric-polarimetry]
models: [angular-correlation, polarization-distribution]
observables: [linear-polarization, circular-polarization, parity, multipolarity]
methods: [Compton-effect, photoelectric-effect, deuteron-photodisintegration]
tags: [polarization, Compton, angular-correlation, review, parity]
---

# Polarization measurements on nuclear γ rays

## Bibliographic Record

- L. W. Fagg & S. S. Hanna, *Rev. Mod. Phys.* **31**, 711–758 (1959), DOI `10.1103/RevModPhys.31.711`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1959_Fagg_Hanna_Polarization Measurements on Nuclear Gamma Rays.pdf`。

## Scope and Reading Depth

- PDF pp.711–758 (48 pages) fully read: linear/circular polarization theory, alignment versus polarization, Compton/photoelectric/deuteron processes, experimental detector methods, direction–polarization/circular correlations and tabulated historical experiments.
- Not covered: primary data behind every historical entry and later segmented-detector developments.

## Key Results

- The review separates nuclear alignment (`w(m)=w(−m)`) from polarization (`w(m)≠w(−m)`), explaining which direction/polarization/circular correlations each preparation can support (PDF pp.711–718, Table I).
- Linear polarization distributions are written as angular-correlation expansions with Legendre/associated Legendre functions; mixed multipoles enter through amplitude ratios and orientation coefficients. Polarization can resolve electric/magnetic parity ambiguity left by direction-only measurements (PDF pp.712–718, Eqs.I-1–I-14).
- Compton scattering is the primary plane-polarization analyzer; photoelectric effect, deuteron photodisintegration, pair production and nuclear photoeffect are reviewed as complementary analyzers (PDF pp.719–726).
- The experimental survey covers annihilation radiation, direction–polarization correlations, radioactive sources, nuclear reactions/Coulomb excitation, aligned nuclei, circular polarization and tabulated parity/multipolarity results (PDF pp.726–756).
- For a simple mixed transition, polarization can determine the sign of the angular-correlation term and often constrain the mixing branch, but pure dipole/pure quadrupole special cases require additional information (PDF pp.713–718, Eqs.I-8–I-11).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| FH59-1 | Alignment supports linear but not circular polarization; polarization requires a directed substate population. | formalism-result | review | PDF pp.711–718, Table I | false |
| FH59-2 | Compton/photoelectric and related processes provide parity-sensitive polarization analyzers complementary to angular distributions. | method-synthesis | review | PDF pp.719–756 | true |
| FH59-3 | Polarization can resolve multipole/parity or mixing ambiguities only with orientation, convention and detector response controlled. | limitation | review | PDF pp.712–718, 726–756 | false |

## Summary

Fagg and Hanna's review is the historical bridge between nuclear orientation theory and modern Compton polarimetry. It clarifies the alignment/polarization distinction and records the detector and correlation logic underlying later CLOVER, SeGA and PDCO measurements.

## Competing Interpretations and Limitations

- Historical polarization signs depend on scattering-plane definitions, detector corrections and phase conventions; tabulated experiments are not automatically interchangeable.
- Direction–polarization correlations require known or modeled alignment and multipolarity; polarization alone does not identify a unique state sequence.
- The review's detector technology and numerical sensitivities are historical baselines, not current array calibrations.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| FH59-AR-1 | Orientation chain | Population mechanism → alignment/polarization tensor → angular distribution/correlation → linear/circular polarization. | PDF Table I, Eqs.I-1–I-14 | self-checking |
| FH59-AR-2 | Detector chain | Compton/photoelectric/deuteron analyzer → asymmetry/polarization sign → parity/multipolarity constraint. | PDF Secs.II–III | self-checking |
| FH59-AR-3 | Transfer condition | Map historical plane/sign conventions and detector response before comparing with modern `P/A/Q` values. | PDF pp.726–756 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[compton-polarimetry]], [[linear-polarization-asymmetry]], [[angular-correlation]], [[angular-distribution]] and polarization history.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `FH59-P0-1`: Preserve historical convention and detector-response boundaries; do not import tabulated polarization signs without source-level mapping.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]], [[angular-correlation]]。


### 原件再核：ratio 字典、同跃迁布居边界与表值版本

2026-10-19 本session完整重读48页 Sections I–III、Table XIII/Addenda、致谢及全部参考文献；对本文判断相关的 Eq.I-4–I-9、I-15–I-17、II-1/2、III-1/3与Fig.1/2/16–23/26/37、Tables II–VI/XII及XIII选定行视觉回查。未逐个重读全部转引实验的primary或恢复其event/producer。本页旧claim的false/true标记保留，新增claim均true。

旧Wiki末页756少了两页；实际原件printed711–758与Crossref卷31(3)/DOI一致，757/758为本篇bibliography继续，不是邻文。已修本页卷页和阅读范围；原PDF/Bib不改。另纠正本run开读前回忆的来源归属：SU59 Ref6是Fagg–Hanna1953 PhysRev92,372（Fa53），B15 Ref23才是本1959综述。相同作者不能合并为同一source；冻结before保留，纠正另存。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| FH59-4 | 原件是48页printed711–758，末两页为同篇bibliography；Crossref亦给711–758，修旧711–756 metadata，不改原件。 | bibliographic-correction | original-and-Crossref | pp757–758 bibliography headers | true |
| FH59-5 | Eq.I-4/5的electric angle γ从reaction plane量起，P1=(J0−J90)/(J0+J90)是plane-axis；与SU59 normal-axis P相反。p714脚注明确sign依γ零点及I-7的符号，不靠electric/magnetic字母同名互换。 | original-axis-and-phase-contract | direct-review-formalism | p713 Eq.I-4/5；p714 footnote | true |
| FH59-6 | I-2给δn²为两辐射intensity ratio、实δn及initial/final outer-state角色；但F表和相位依据转引Bi53/Fe55。本run未得这两份original，不能仅从本综述给SUx或FHδ到KS/RB的完整operator/RME桥。 | historical-amplitude-readiness | direct-and-limited-inference | pp712–713 Eq.I-1/2说明 | true |
| FH59-7 | I-7带显式leading minus。按原CG式精确重算Table II(b)18个列出项全部相同；首脚本抄漏负号导致首项+1/2而非−1/2，已留失败snapshot并按原图修，未调输入。 | exact-table-replay-and-failure | actual-symbolic-computation | p713 Eq.I-7/TableII(b) | true |
| FH59-8 | 原p=J0/J90是光子偏振强度比，R是有限几何response ratio；III-1给r=N0/N90=(p+R)/(pR+1)。同plane零点定义P=(p−1)/(p+1)、Q=(R−1)/(R+1)，则(N90−N0)/(sum)=PQ。该p不是SU59的Compton analyzing power。 | observable-dictionary-and-algebra | direct-and-exact-derivation | pp728–729 Eq.III-1 | true |
| FH59-9 | 同篇III-3的circular R另定义为2(N+−N−)/(N++N−)，和linear response R是不同对象。复制asymmetry时必须保留2及磁化角色，不能按同字母消因子。 | normalization-role-boundary | direct | p738 Eq.III-3/5/7 | true |
| FH59-10 | printedE3/m1多项式W=1+111t−305t²+225t³、G=−1+131t−355t²+225t³，t=cos²θ；(W+G)/2=t(15t−11)²、(W−G)/2=(5t−1)²保证physicality，无需clip。独立electric-vector spherical-harmonic导数给同两强度形状。 | source-polynomial-and-physicality | exact-algebra-and-independent-classical-check | p715 Eq.I-15/17；p716 TableVI(b) | true |
| FH59-11 | 原literalpoly在cos²θ=1/5给Pplus=+1（63.435/116.565°），cos²θ=0、11/15给−1；原文写约62/118°并在118°给近完整P。直接代118°为.998406，保留approx与精确式的差，不重标实验角或认证finite acceptance。 | literal-angle-and-pure-limit | actual-printed-equation-calculation | p715 Eq.I-17后段；p733 FrenchNewtonparagraph | true |
| FH59-12 | 综述转述French–Newton在Ep≈.33MeV、α–γ118°研究O16的6.13MeV线并判E3；又转述Fa53在Ep=.874MeV/beam90°下6.13MeV线近无偏振。同transition/EM不等同一population/reference-gate；不能把前者P直接给后者。 | same-transition-preparation-counterexample | review-report-not-new-primary | p733 SecIII-A(e)；pp736–737 Fa53 | true |
| FH59-13 | 4(2)2(2)0例由1/8+1/24得plane-axisP90=1/6及p=7/5。它对这里pureE2的first/last交换相同；unresolved mixed EM/能量分支需按各自效率混合，不推广任意cascade。 | source-limit-and-role-boundary | direct-and-central-arithmetic | p730 4–2–0example | true |
| FH59-14 | Me50的Rh106例direction-coefficients为预期一半、Cs134有其它coincidentγ，本文保留tentative/不能unique的判断；FH59表和Me50图复述同采集，不计新实验。 | counter-evidence-and-independence | direct-review | p730 Rh/Csparagraphs；TableXIII Pd106/Ba134 | true |
| FH59-15 | TableXIII说明逗号及(u)为未分辨多线、分号为已作能量区分、“or”为可区分但未指定哪条进入polarimeter；multipolarity还可来自外部证据。这些标记不可抹去后当每条线独立P。 | table-object-and-companion-contract | direct-review | pp744–745 TableXIII说明 | true |
| FH59-16 | p743正文给Ap58 Co60 A=−.340(.035)、Na22 +.295(.054)；TableXIII p746 Ne22行写−.340而p751 Ni60行写+.295，数对相对正文交换。原Ap58未读，本页隔离literal版本，不从表任选值作calibration或自动更正原作者数据。 | isolated-text-table-identity-conflict | direct-visual | p743 Ap58paragraph；p746/p751 TableXIII Ap58rows | true |
| FH59-17 | p729转述Me50用已知KN偏振的scatteredCoγ校response/有效角宽；p719脚注又指出Fig2和Me50高能θmax曲线差异原因未知。原detectorgeometry/能量平均/producer未得，不能由理想KN重建原response曲线。 | calibration-and-model-boundary | direct-review | p729 calibrationparagraph；p719 footnote to Fig2 | true |
| FH59-18 | 本页旧“alignment不支持circular”在该文parity-conserving取向/EM框架下使用；本文另述对初态unpolarized核反应的circular-null搜索，以检验parity conservation。旧摘要不能代替这些对称性假设或将有限精度null宣称exactzero。 | scope-qualification | direct-review-and-explicit-conditions | pp740–741 Wilkinsonparagraph | true |

在同一reaction-plane参照下，FH59的P与现代plane-axis Stokes兼容，而SU59需一次反号。还要分开electric-vector角、Compton scattering-plane角与count ratio的分子：对FH59 `r=(1−QP)/(1+QP)`；用反比计数就必须相应改asymmetry号。极限p=1或R=1给r=1；p→∞给r→1/R，不将强度比p当作有界的polarization degree。circular III-3的2是定义的一部分，未借此重定义其它来源Q。

E3原式的两非负平方和没有共同零点，故该literal模型处处有非零W且|P|≤1。它也直接显示同一electricmultipole的P可随角跨零/换号；本例Pplus在90°为−1而118°约+.9984。因此“electric一定positive”的口诀不能代替spin/population/axis判断。118°与约62°是源文近似角，未替真实response补出精确P。

p733转述experiment的namedratio1.14(.06)与M3/E3预测.84/1.19，若固定预测只作central diagnostic，残差分别5与−.833σ；原计数、namedratio的完整角零点/接受度未在本run恢复，不把这个review比值硬映成现代N0/N90或当作新拟合。它与Fa53的近无偏振结果是不同Ep/选择对象，既不是重复验证同一P也不是相互冲突的E3赋值。

本轮`supports`完整count-role/P轴合同与sourcepurelimits；`limits`“同E/同EM即可迁移校准”、review表作primary和无operator定义的历史δ转换；`revises`旧末页及本run误记SU→FH59的引用关系。旧claims/review保持，新项needs_review；科学可复核脚本不增加独立实验或课程信用。

复算：[FH59原式程序](../../system/scripts/day16_fagghanna1959_convention_audit.py)，[冻结输入/结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/fagghanna1959-convention-audit-result.json)。全原件与选定渲染只读/保存在tmp；BR1953、Fe55、Me50、Ap58原件及完整rawresponse/Cov仍有缺口。

相关：[[suffert-1959-proton-capture-polarization]]、[[bizzeti-2015-agata-triple-cluster-polarimetry]]、[[modulation-curve]]、[[compton-polarimetry]]、[[high-spin-angular-polarization-mixing-ratio]]。
