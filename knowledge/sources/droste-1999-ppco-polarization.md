---
type: source
title: "Droste et al. 1999 - PPCO polarization-polarization correlation from oriented nuclei"
aliases: [Droste 1999 PPCO]
created: 2026-09-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: method-paper
reading_depth: deep-read
title_original: "PPCO: polarization-polarization correlation from oriented nuclei"
authors: [Ch. Droste, K. Starosta, A. Wierzchucka, T. Morek, S. G. Rohozinski, J. Srebrny, M. Bergström, B. Herskind, E. Wesolowski]
journal: "Nuclear Instruments and Methods in Physics Research A"
year: 1999
citation_key: droste_1999_PPCO
volume: 430
pages: "260-270"
pii: "S0168-9002(99)00224-7"
canonical_source: "Droste et al., NIM A 430, 260-270 (1999)"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/mixing ratio/1999_Droste et al_PPCO polarization–polarization correlation from oriented nuclei.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/mixing ratio/1999_Droste et al_PPCO polarization–polarization correlation from oriented nuclei.pdf"
raw_sha256: "7d2a0ecf0805c1ea8d845c3d0f1e36fb873b0ae87e16d5be20152ba8b97773ee"
nuclei: [164Yb, 114Cd, 118Sn, 126Ba]
reactions: [138Ba(30Si,4n)164Yb, 114Cd(16O,4n)126Ba, 114Cd-Coulomb-excitation, 118Sn-Coulomb-excitation]
experiments: [eurogammII-clover-polarimetry]
models: [PPCO, PDCO, oriented-state-angular-correlation]
observables: [PPCO, polarization-polarization-correlation, DCO, spin-parity, multipole-mixing]
methods: [Compton-polarimetry, PPCO, DCO-ratio]
tags: [PPCO, polarization, CLOVER, DCO, mixing-ratio, high-spin]
---

# PPCO polarization–polarization correlation from oriented nuclei

## Bibliographic Record

- Ch. Droste *et al.*, *NIM A* **430**, 260–270 (1999), PII `S0168-9002(99)00224-7`.
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/mixing ratio/1999_Droste et al_PPCO polarization–polarization correlation from oriented nuclei.pdf`.

## Scope and Reading Depth

- PDF pp.260–270 fully read: polarization definitions, single/two-polarimeter quantities, PPCO equations, Gaussian alignment, PP1/PP2/AA1/AA2 observables, DCO combination contours, EUROGAM-II/CLOVER test and conclusions.
- Not covered: full FORTRAN code and raw matrices.

## Key Results

- PPCO correlates polarizations of two successive γ rays from an oriented state; four coincidence counts (`N⊥⊥`, etc.) are modeled using polarimeter sensitivities `Q1/Q2`, alignment width and multipolarity sequences.
- New observables PP1/PP2 and AA1/AA2 compress the four-count relation; combining PPCO with DCO reduces spin/parity/multipolarity ambiguities relative to DCO alone.
- The method is intended for segmented CLOVER/EUROGAM arrays and high-spin reactions, but relies on alignment/population and detector-specific `Q` calibration.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DR99-1 | PPCO measures polarization–polarization correlations of two cascade γ rays from an oriented nucleus and can constrain spin/parity/multipole sequences. | method-result | direct | PDF pp.260–264, Eqs.1–15 | true |
| DR99-2 | Combined PPCO+DCO contours reduce solution multiplicity compared with DCO alone. | method-result | direct | PDF pp.263–270, Fig.3 onward | true |
| DR99-3 | Alignment distribution and detector sensitivity `Q` are explicit model/calibration inputs. | limitation | direct | PDF pp.261–264 | false |


### Day17原件新增自审

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DR99-D17-1 | 本篇实验是138Ba(30Si,4n)164Yb；旧Wiki176Yb/152Cd/152Sn及197Pb metadata并非本篇对象，已按原件纠正。114Cd/118Sn/126Ba是所引Ref5标定层，非另三项本篇独立测量。 | source-identity-correction | direct-and-self-audit | printed262 Sec2; printed265 Sec3 | true |
| DR99-D17-2 | EUROGAM-II有24Clover在75.5/104.5度两环，选18个similar efficiency；pairgroupφ近0/30/60/90，各fourN矩阵；不是所有arraymember可无条件平均。 | experimental-fact | direct-and-self-audit | printed265 Sec3 Fig4–6 | true |
| DR99-D17-3 | 明确假定a=1、18Clover identical及Q由Ref5单NORDBALL曲线近似EUROGAM，和ST99共享主采集/标定假设而非独立确认。 | calibration-and-independence-boundary | direct-and-self-audit | printed266 assumptions1–3 | true |
| DR99-D17-4 | Eq8在两局部正交分析器σ响应factorize，作用于四jointW；源W不预设等两个singles乘积，未知alignment用Eq7 Gaussian模型。 | formalism-boundary | direct-and-self-audit | printed262 Eq7; printed263 Eq8 | true |
| DR99-D17-5 | PP1是jointfield parity差和，AA1=Q1Q2 PP1。Footnote3说明它是两个singleP之外的一个additional ratio自由度；四normalizedN只三shape自由度。 | formalism-and-information | direct-and-self-audit | printed263 Eq11–13 footnote3 | true |
| DR99-D17-6 | PP2=(W∥∥−W⊥⊥)/(W∥∥+W⊥⊥)，AA2=(N⊥⊥−N∥∥)/(N⊥⊥+N∥∥)；有限Q下Eq14/15混入crossW、两个R，不普遍AA2=Q1Q2 PP2。 | observable-boundary | direct-and-self-audit | printed263 Eq14; printed264 Eq15 | true |
| DR99-D17-7 | 569–577 pureE2 cascade的AA2=.235±.027给14+ sigma/I=.22(+.06/−.11)，不同于490–569的AA2=.229±.038；不是独立无误差alignmentprior。 | experimental-fit-and-input | direct-and-self-audit | printed266 Sec3.1 Fig6 | true |
| DR99-D17-8 | Table1在RDCO≈1列八positive-parity候选；AA2/4N排2/3/6/7却留1/4/5/8，非唯一16+。改sigma/I .2→.25不改作者结论；Table脚注.3的pureE2 AA2=.200仍近实测。 | author-interpretation-and-counterevidence | direct-and-self-audit | printed266 Table1; printed267 Sec3.2 | true |
| DR99-D17-9 | 490/569原R1=1.62、R2=1.57，AA1=.038±.028；原作者说AA1内所有候选在2sigma均接受。按固定Q转换PP1约.724±.533仅AA1误差，非fullCI。 | reported-result-and-task-calculation | direct-and-self-audit | printed267 Sec3.2 | true |
| DR99-D17-10 | Eq9 fourN fit只浮K，Fig8与Fig9对照hypotheses1/2；未给actual peakcounts、Sigma/nu/producer。不能凭chi2/nu还原pvalue或独立重复统计检验。 | fit-readiness-boundary | direct-and-self-audit | printed263 Eq9; printed267 Fig8; printed268 Fig9 | true |
| DR99-D17-11 | 647原强度约262的15%，求和φ与530/463/375 gates，R1=1.53/R2=1.65；sigma/I .2时E1/M1候选chi2/nu .6/6，.25结论同。它是同dataset conditional discrimination，不给通用15%检出限。 | experimental-analysis-and-boundary | direct-and-self-audit | printed268 Sec3.3 | true |
| DR99-D17-12 | 几何对称pair或stretchedgate可求和以改善计数；实际gate重叠、Q(E)/权重/背景须传递，原理论相等不证明重复event独立。 | method-and-statistical-boundary | direct-and-self-audit | printed264 Fig3 discussion; printed265 Fig4; printed268 Summary | true |
| DR99-D17-13 | Summary明确某些4N仍不唯一、lifetime可作companion；1MeV未来segmented Q≈.3来自simulation/Ref19private+21，clover≈.15，不是本文新阵列实测。 | counterevidence-and-model-boundary | direct-and-self-audit | printed267 Sec3.2; printed269 Summary | true |
| DR99-D17-14 | 本任务归一Eq8推AA2=(Q1P1+Q2P2)/(1+Q1Q2 PP1)，同singles不定PP1；exclusive fixedN multinomial局部Cov(AA1,AA2)=0只是声明countmodel控制，非实验峰面积Σ。 | task-calculation | direct-and-self-audit | printed263 Eq8–14; printed264 Eq15 | true |

## Summary

Droste *et al.* extend PDCO/DCO into a two-polarimeter PPCO method, providing a formal multi-observable route to spin, parity and mixing-ratio assignment in high-spin arrays.

## Competing Interpretations and Limitations

PPCO is sensitive to alignment width, polarimeter geometry/sensitivity, cascade ordering and multipolarity hypotheses; it does not create a universal threshold. Finite statistics and correlations between four counts must be retained.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| DR99-AR-1 | Formula chain | `P`/Compton asymmetry → four polarization counts → PPCO observables → combined DCO fit. | PDF Eqs.1–15 | self-checking |
| DR99-AR-2 | Transfer condition | Requires matched CLOVER geometry, Q calibration, alignment and cascade gate. | PDF Secs.2–4 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[linear-polarization-asymmetry]], [[compton-polarimetry]], [[angular-correlation]] and DCO/PPCO method map.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `DR99-P0-1`: PPCO observables are response/alignment-specific; do not transfer contours without the full geometry/calibration mapping.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]], [[angular-correlation]]。

## Day17原件复核：同源164Yb的fourN而非独立新实验

本session先冻droste1999-before/exercise并声明旧摘要priming后，完整text与visual读原11页260–270；Eq1–15、Fig1–9、Table1八行、21refs均核，raw277602bytes/hash `7d2a0ecf0805c1ea8d845c3d0f1e36fb873b0ae87e16d5be20152ba8b97773ee`保持。旧DR99-1–3/flags与review不改，14新claim待审；原脚注FORTRAN availablefromauthors不等本次取得producer。

本篇复用[[starosta-1999-pdco-experimental-test]] Ref5的164Yb EUROGAM-II主采集与NORDBALL Q迁移假设。旧Wiki nuclei/reactionmetadata误配已改，不能继续沿197Pb/152Cd作证据。Eq8 twoanalyzerσfactorization不要求源jointWfactorization；推导/矩阵/信息及countmodel反证见[[ppco-joint-response-and-information]]。4N改进相对一个AA2的信息，但不是四个独立ratio，也不保证唯一spin/parity；Table1及原negative-parity讨论/lifetimecompanion保留。

决定`revises`旧摘要过强的“组合便赋值”印象，`supports`joint响应合同与额外observable的信息；未增加独立实验数、重新拟合164Yb δ/Jπ或认证Q迁移。实际四谱净面积/背景、逐门事件唯一性与jointΣ/完整producer缺时保持readiness；不从图读出pseudo精确counts。
