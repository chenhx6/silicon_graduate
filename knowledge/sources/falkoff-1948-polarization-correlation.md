---
type: source
title: "Falkoff 1948 - Polarization Correlation of Successive Gamma-Ray Quanta"
aliases: [Falkoff 1948 polarization correlation]
created: 2026-09-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: theory-letter
reading_depth: deep-read
title_original: "Polarization Correlation of Successive Gamma-Ray Quanta"
authors: [David L. Falkoff]
journal: "Physical Review"
year: 1948
volume: 73
pages: "518"
canonical_source: "Falkoff, Phys. Rev. 73, 518 (1948)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1948_Falkoff_Polarization Correlation of Successive Gamma-Ray Quanta.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1948_Falkoff_Polarization Correlation of Successive Gamma-Ray Quanta.pdf"
raw_sha256: "47cf0977334fc9dc8fc27b3d25b46a2eac4272c611df4c10ce69ccdb07d2b589"
nuclei: [60Co, 46Sc]
reactions: []
experiments: []
models: [angular-correlation-formalism]
observables: [polarization-correlation, multipole-character, angular-correlation]
methods: [polarization-correlation, Compton-analyzer]
tags: [polarization, angular-correlation, historical-formalism, multipole]
---

# Polarization Correlation of Successive Gamma-Ray Quanta

## Bibliographic Record

- David L. Falkoff, *Physical Review* **73**, 518 (1948).
- The supplied one-page scan contains the Falkoff letter on the right/lower portion plus unrelated preceding material; only the titled Falkoff article is used here. Hash and filename are preserved.

## Scope and Reading Depth

- Falkoff letter read end-to-end: Eq.(1) printed `W(φ)=1+A cos2φ`, interpreted as `cos(2φ)` with the source ratio and independent CG audit (FA48-D17-1/2); old cos² transcription is withdrawn, Eqs.(2–3) coefficient/sign, dipole/dipole Table I, `60Co/46Sc` quadrupole example and comparison with angular correlations.
- Not covered: original analyzer response, raw experiments and the separate preceding article on the scan page.

## Paper Question and Method Logic

The letter derives polarization correlations for two successive γ rays and argues that the sign of the correlation distinguishes electric/magnetic character and nuclear parity information beyond ordinary directional correlations.

- The coefficient `A=2N/D` is built from angular-momentum matrix elements summed over the intermediate state's magnetic substates; its sign depends on multipole orders, parities and whether both transitions are electric/magnetic.
- For `60Co/46Sc` quadrupole–quadrupole cascades, the predicted positive/negative sign distinguishes parallel versus perpendicular polarization, with `|A|=2/7` and a maximum/minimum ratio about 1.8.
- Dipole–dipole values are tabulated for `ΔJ=0,1`; polarization correlation is roughly twice as sensitive as corresponding angular-correlation parameters but is intended as a supplement, not a replacement.

## Key Results

**历史行处置：FA48-1旧cos²转录不再作为现行公式；原行与false标记仅保留历史，现行字典见FA48-D17-1/2。这不是human审核或sourceerratum。**

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| FA48-1 | Successive-γ polarization follows `W(φ)=1+A cos²φ`; the coefficient sign encodes electric/magnetic character and parity information. | formalism | direct | PDF p.518, Eqs.1–3 | false |
| FA48-2 | For quadrupole–quadrupole cascades in `60Co/46Sc`, `|A|=2/7` and the sign predicts parallel/perpendicular maxima. | model-result | direct | PDF p.518, example paragraph | true |
| FA48-3 | Polarization correlations complement directional correlations because their form is common across multipoles but sensitivity is larger. | method-result | direct | PDF p.518, Table I and final paragraphs | true |


### Day17原件新增自审

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| FA48-D17-1 | 原Eq1印cos2φ，原A=2/7且max/min=1.8与cos(2φ)闭合。旧Wiki的同系数cos²φ读法撤回；不称原文officialerratum。 | Wiki-transcription-revision | direct-and-self-audit | printed518 Eq1 andCo60/Sc46 paragraph | true |
| FA48-D17-2 | 两形式可等价重参数：1+Acos(2φ)=(1−A)[1+bcos²φ]，b=2A/(1−A)。A2/7对应b4/5；只换cos²而不换coef/overallconstant会失配。 | task-calculation | direct-and-self-audit | printed518 Eq1 and2/7 ratio | true |
| FA48-D17-3 | φ是两电场polarizations的相对角，讨论限定anti-parallel photon directions/nonorientedsource；不同于DR99的两emissionplanes/探测器azimuthφ，不裸迁axis或scalarQ。 | formalism-scope | direct-and-self-audit | printed518 beforeEq1; Eq1 | true |
| FA48-D17-4 | Eq2 A=2N/D经intermediateM求和，Eq3 sign=(-1)^(l1+l2+Ji−Jf+1+s)，s同EM为1/异EM为0；不包含mixedδ相位/任意制备取向。 | formalism-scope | direct-and-self-audit | printed518 Eq2–3 | true |
| FA48-D17-5 | 原Co60/Sc46用4→2→0 purequadrupole示例，同EM正A/异EM负A；作者称stretchedquad J+2→J→J−2均abs(A)=2/7。是1948条件模型，不代现代Co60细M3/actualgate/arrayresponse。 | author-model-and-transfer-boundary | direct-and-self-audit | printed518 exampleparagraph | true |
| FA48-D17-6 | 独立本session sparseCG/Jones kernel在J2/3/4三组核Table1九dipole公式共27行，Eq3号及secondEMtoggle均过；J2–5四stretchedquad给±2/7、relativeφ多点cos(2φ)核。非原FORTRAN/实验producer。 | task-calculation | direct-and-self-audit | printed518 TableI Eq1–3 | true |
| FA48-D17-7 | 共同globalxy轴/初态unoriented/opposite方向下两marginalP=0，jointPP1=A_F可非零，AF不是单光子P或计数A。与DR99 AA1=Q1Q2PP1只在匹配轴/响应时桥接。 | cross-source-conditional-inference | direct-and-self-audit | printed518 Eq1; TableI | true |
| FA48-D17-8 | 原letter只预测相关；Madanskyapparatus在settingup，所引Brady/Deutsch为directional实验。Table1更大coef不等任意detectorQ/F更好，作者称用来补充directional数据。 | source-independence-and-boundary | direct-and-self-audit | printed518 openingandfinalparagraphs | true |

## Summary

Falkoff's short letter is an early formal justification for polarization-correlation spectroscopy as a parity/multipole discriminator. It supplies historical equations and sign logic, not a modern detector calibration.

## Competing Interpretations and Limitations

The sign and magnitude depend on phase conventions, intermediate-state alignment and analyzer response; measured polarization requires Compton/photoelectric efficiency calibration. It should not be merged with later linear-polarization asymmetry or detector `Q` conventions without mapping.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| FA48-AR-1 | Formula chain | Successive multipole matrix elements → `A` coefficient/sign → analyzer polarization correlation. | PDF Eqs.1–3 | self-checking |
| FA48-AR-2 | Convention | Electric/magnetic sign depends on phase and multipole convention; cross-source mapping required. | PDF Eq.3 | active-L3 |
| FA48-AR-3 | Scan identity | Relevant letter is only one part of the one-page scan; preceding unrelated text is excluded. | PDF p.518 | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` historical polarization-correlation and mixing-ratio method lineage.
- Persistence: link to [[linear-polarization-asymmetry]], [[angular-correlation]] and [[multipole-mixing-ratio]].
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `FA48-P0-1`: map sign/phase conventions before using `A` across later polarization analyses.

## Extracted Pages

- Methods: [[linear-polarization-asymmetry]], [[angular-correlation]]。

## Day17原件复核：cos2φ、ratio与jointP的字典

本session先冻falkoff1948-before/exercise，声明旧FA48/HAM48/DR99 priming后，完整读原一页Falkoffletter（左下起、续右栏）及Eq1–3/Table1/4refs，排除上方铜磁化率的前篇。238577bytes/hash `47cf0977334fc9dc8fc27b3d25b46a2eac4272c611df4c10ce69ccdb07d2b589`保持；原FA48-1–3/flags全保，但旧1的cos²字典明确不沿用，新8条待审。原印cos2φ与正文1.8、独立CG结果共同支持cos(2φ)解释；不替作者宣告勘误。

[[ppco-joint-response-and-information]]“Falkoff1948：相对电场角不是探测器方位角”保存exactCG/EM号、cos²重参数和PP1桥。实际新kernel不导入旧Day16tensor/原PPCOproducer；27dipole/4quad只为条件理论复算，非现代Co60或Sc46的重新实验指认，也不证明任意aligned/有限门的相同式。公开Crossref exactDOI候选查询因TLS失败，metadata未核，不以失败查询补来源body或更改citationkey。

决定`revises`Wiki符号转录，`supports`PPCO第三shape信息与原经典限。原letter无实际polarimetrycounts/Q/Σ；其coefficient大不等仪器FOM更大。人审/旧flags不晋升。
