---
type: source
title: "Schmid et al. 1998 - Gamma-ray polarization sensitivity of the Gammasphere segmented germanium detectors"
aliases: [Schmid 1998 Gammasphere polarization]
created: 2026-09-20
updated: 2026-10-18
status: ai-draft
review_status: unreviewed
source_type: method-paper-and-application
reading_depth: deep-read
title_original: "Gamma-ray polarization sensitivity of the Gammasphere segmented germanium detectors"
authors: [G. J. Schmid, A. O. Macchiavelli, S. J. Asztalos, R. M. Clark, M. A. Deleplanque, R. M. Diamond, P. Fallon, R. Kruecken, I. Y. Lee, R. W. MacLeod, F. S. Stephens, K. Vetter]
journal: "Nuclear Instruments and Methods in Physics Research A"
year: 1998
volume: 417
pages: "95-110"
pii: "S0168-9002(98)00624-X"
doi: "10.1016/S0168-9002(98)00624-X"
canonical_source: "Schmid et al., NIM A 417, 95-110 (1998)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1998_Schmid et al_Gamma-ray polarization sensitivity of the Gammasphere segmented germanium.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1998_Schmid et al_Gamma-ray polarization sensitivity of the Gammasphere segmented germanium.pdf"
raw_sha256: "66502edb2f0ff2d09321d3b388767ea98736b83865b90f128fdd1e46921b2a2c"
alternate_versions: ["raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1998_Schmid et al_Gamma-ray polarization sensitivity of the Gammasphere segmented germanium2.pdf"]
alternate_sha256: "bdb397650e5b8cc92f358e386f52703604dd0962184364004eb8985f76998558"
nuclei: [56Fe, 24Mg, 109Ag, 197Pb, 176Yb]
reactions: [24Mg(p,pγ), 56Fe(p,pγ), 109Ag(p,pγ), 176Yb(26Mg,5n)197Pb]
experiments: [gammasphere-polarimetry]
models: [Klein-Nishina-response, shears-mechanism]
observables: [polarization-sensitivity, Compton-asymmetry, parity, Q(E), figure-of-merit]
methods: [compton-polarimetry, Monte-Carlo-detector-response]
tags: [Gammasphere, segmented-Ge, polarization, detector-response, 197Pb]
---

# Gamma-ray polarization sensitivity of Gammasphere segmented Ge detectors

## Bibliographic Record

- G. J. Schmid *et al.*, *NIM A* **417**, 95–110 (1998), PII `S0168-9002(98)00624-X`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/polarizaiton/1998_Schmid et al_Gamma-ray polarization sensitivity of the Gammasphere segmented germanium.pdf`。

## Scope and Reading Depth

- PDF pp.95–110 fully read: segmented detector design/Doppler correction, Klein–Nishina polarization formalism, conventional and two-fold definitions, calibration reactions, Monte Carlo, Tables/Figs.1–10 and `197Pb` shears-band application.
- Not covered: raw Gammasphere matrices and full Monte Carlo source.
- Alternate-version audit: the 44-page LBNL-41340 preprint/eScholarship copy was reread by section (Secs.1–7, calibration, Monte Carlo and `197Pb` application). It is an earlier/alternate presentation of the same NIM A source, not an independent experiment; no material claim change was found.

## Key Results

- Gammasphere segmented Ge detectors used as two-fold Compton polarimeters yield `Q(E)` from about 5% at 415 keV to 4% at 1368 keV; Monte Carlo agrees within ~20% over measured energies.
- Segmentation improves Doppler resolution and permits confined/shared event asymmetry, but cannot measure a true up/down versus left/right asymmetry without detector rotation; new definitions are required.
- High-background `176Yb(26Mg,5n)197Pb` data demonstrate the sign of linear polarization and support negative parity for Shears Band 1, despite relatively poor sensitivity.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SG98-1 | Segmented Gammasphere Ge detectors provide a low-sensitivity but practical two-fold Compton polarimeter for high-spin arrays. | method-result | direct | PDF pp.95–100 | true |
| SG98-2 | Experimental `Q(E)` and Monte Carlo response agree within about 20% from 415–1368 keV. | method-validation | direct | PDF pp.95–110, Fig.10 | true |
| SG98-3 | A high-background `197Pb` application uses polarization sign to support negative parity of Shears Band 1. | application-result | mixed | PDF pp.95–110, application section | true |
| SG98-4 | 双分段不能直接测四方向的vertical/horizontal散射比；作者定义eta=Su/Cu，A=(etaC−S)/(sqrt(eta)(C+S))，并在总photopeak yield与偏振方向无关等Eq13条件下得A=QP。普通(C−S)/(C+S)或balanced-denominator式不是同一个A。 | detector-specific-observable-definition | direct | printed100–101 Eqs12–16 | true |
| SG98-5 | C必须合计sidepeak附近2FWHM的“本侧全吸收”与ADCzerochannel的“另一侧全吸收”；S介于两者。zerochannel不是无photopeak事件，而是fullsignal过threshold、side signal未过threshold，不能丢弃后沿用原eta/Q。 | event-classification-and-threshold | direct | printed96 threshold说明；printed103 Sec4.3/Fig8 | true |
| SG98-6 | Table1三条pureE2参考的P由实测a2/a4和Eq6算，再用A/P校Q；Q与该A不是独立测量。Table3的peakerror不自动涵盖eta/Q calibration及其共同Cov。 | calibration-dependency-and-error-boundary | direct-and-self-audit | printed101–103 Sec4/Table1；printed107 Sec6.3；printed108 Table3 | true |
| SG98-7 | Eq17在knowneta/Q、C/S独立Poisson层给误差；nearA0的Eq18才近似1/(Nincident epsilon Q²)。双分段epsilon在这里是photopeak efficiency，传统四分段用coincidence efficiency；同名字F不保证高背景下可比较。 | variance-and-efficiency-definition | direct | printed100–101 Eq10/11/17/18；printed104 Table2/讨论 | true |
| SG98-8 | Fig9的eta示例threshold130keV，Fig10的Q为60keV；Pb应用取80–100度12台gainmatchedsegmentedGe、side threshold60keV。不同threshold或detectorselection的eta/Q不能只按同energy互借。MC与实验约20%差异的全局scale校正依赖作者的geometry不确定性解释，不是已证明的唯一原因或actualcode重放。 | response-transfer-boundary | direct-and-self-audit | printed105 Figs9/10；printed106 Fig11/Sec6.1 | true |
| SG98-9 | 197Pb在beam135MeV的176Yb(26Mg,5n)中测，Table3的432线C30934(402)/S4449(125)、eta.163(.003)、A.041(.011)、P.75(.20)；作者用相对inband符号支持E1/负宇称，但同时认为过大的幅值和带内散布受高背景拟峰系统误差限制。 | actual-measurement-and-interpretation-boundary | direct | printed107–109 Sec6.3/Figs13–15/Table3 | true |
| SG98-10 | 本任务按Eq15重算Table3七行，六行与所列A按最后位舍入盒相容；294行得到−.048106而表为−.045，当前尾位盒不闭合。原图eta.061/C16622/S1226已核，未调eta或修改表，unrounded producer/cuts/aggregation原因未决。 | bounded-printed-table-replay | task-calculation | printed101 Eq15；printed108 Table3；day16_sg98_polarimetry_preview.py | true |
| SG98-11 | 432行按quotedC/S fiterrors独立传播的A尺度约.00980、eta误差敏感性.00611，sqrt(area)Poisson诊断仅.00508；都是指定Cov假设下诊断，非恢复原fullΣ/新P误差或显著性。完整传播须保留C/S/eta/Q与A-Q共享校准Cov。 | uncertainty-layer-audit | task-calculation | printed101 Eq17；printed107 error来源说明；printed108 Table3 | true |
| SG98-12 | 作者的约36%是其purehighspin-dipole/maximumalignment比较条件，不是任意conditionalgamma的通用physicalP上限；通用|P|≤1和具体spin/mixing/selection界分开。Table3中央值越过36%不能自行夹值或改误差，也不能无条件据符号给唯一Jpi。 | physics-versus-analysis-boundary | direct-and-self-audit | printed106 Sec6.2；printed108 Fig14与正文；printed109讨论 | true |

## Summary

### 2026-10-18 Day16内恰好Day17知识预习：实际覆盖

先冻结带Day15/ST99与本run priming说明的P/A/Q回忆，再核raw hash，完整读published16页（printed95–110）的正文主线、Figs1–15/Table1–3；原图重点核Eq12–18、eventzero/threshold、三calibration与七个actualPb peak rows、background反证。Crossref重新核12作者、DOI/1998/NIMA417/95–110。新SG98-4–12为Codex self-audit，原SG98-1–3的flags/page review保持；这是Day16下的无学分Day17 preview，不给正式17学分。

新代码[day16_sg98_polarimetry_preview.py](../../system/scripts/day16_sg98_polarimetry_preview.py)在Table3 input冻结后重算，不以sqrt(area)替代quotedfiterrors，也不从A/P除法反造独立Q。294印刷closure失败显式保存：要给表中A中央值需eta≈.06175054，但这是由target反推的条件值，**不是新calibration或被允许替换的输入**。其余六行的tail-digitbox相容不等于已重放rawfit/实际uncertainty。 所需eta仍在quoted .061±.001范围内，A的.0031中央差远小于其quoted .019，不能把printingclosure失败称为实验矛盾。

对44页alternatepreprint（hash bdb397…）本次仅做targeted text/图像定位，未找到可独立核294counttable的内容，不声称重新完整读44页或用它修复published行。它和期刊版是同一研究的版本，不增加实验独立性；原scope中的旧alternate审核历史保留。

[[compton-polarimetry]]的“Gammasphere双分段的P/A/Q与actual峰面积”保存本任务导数、actual432/294实例、Cov/efficiency定义；[[linear-polarization-asymmetry]]保留不能把它当genericcloverA的使用门。决定limits高背景下从小A恢复精确P或用裸F比较仪器，supports先核eventdefinition/threshold/calibration及matchedgate；不改原197Pb赋值或给新δ/Jpi。

Schmid *et al.* establish the Gammasphere segmented-Ge response layer, its new confined/shared asymmetry definition and its limitations in high-background high-spin spectroscopy.

## Competing Interpretations and Limitations

Detector segmentation, energy thresholds, geometry, response Monte Carlo and background determine `Q`; polarization sign alone is not a complete parity proof without multipolarity/configuration context. The `197Pb` parity application remains source-specific.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| SG98-AR-1 | Response chain | Segmented charge signals → confined/shared counts → calibrated asymmetry → `Q(E)` → `P`. | PDF Secs.2–3 | self-checking |
| SG98-AR-2 | Transfer condition | `Q` and 20% simulation agreement are geometry/energy/background-specific. | PDF Tables/Figs. | self-checking |
| SG98-AR-3 | Failure condition | No detector rotation, crosstalk/background and weak statistics limit asymmetry/parity inference. | PDF Sec.3/application | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[compton-polarimetry]] and high-spin parity/multipolarity evidence map.
- Persistence: link to Simpson/Garcia-Raffi/Bass/von der Werth detector lineage.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `SG98-P0-1`: Gammasphere `Q(E)` and parity inference are array/background specific; preserve detector-response calibration.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]]。
