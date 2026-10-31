---
type: source
title: "Ewan et al. 1969 - Gamma-ray polarization with a single Ge(Li) detector"
aliases: [Ewan 1969 single GeLi polarimeter]
created: 2026-09-21
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: method-and-application
reading_depth: deep-read
title_original: "Gamma-ray polarization measurements with a single Ge(Li) detector"
authors: [G. T. Ewan, G. I. Andersson, G. A. Bartholomew, A. E. Litherland]
journal: "Physics Letters B"
year: 1969
volume: 29B
pages: "352-354"
pii: "0370-2693(69)90382-7"
canonical_source: "Ewan et al., Phys. Lett. B 29B, 352-354 (1969)"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1969_Ewan et al_Gamma-ray polarization measurements with a single Ge(Li) detector.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1969_Ewan et al_Gamma-ray polarization measurements with a single Ge(Li) detector.pdf"
raw_sha256: "ded2493ef0e816b3ed74bc5921f61324ec71b1ae34de8be96c988c71fa3e7be5"
nuclei: [102Ru, 100Mo, 56Fe, 24Mg, 28Si, 12C]
reactions: [100Mo-alpha-2n, 56Fe-p-p-gamma, 24Mg-p-p-gamma, 28Si-p-p-gamma, 12C-p-p-gamma]
experiments: [single-planar-GeLi-Compton-polarimeter]
models: [Klein-Nishina-response, angular-distribution]
observables: [polarization-asymmetry, Q, E2-M1-mixing, parity]
methods: [Compton-polarimetry, angular-distribution]
tags: [GeLi, polarization, Compton-polarimeter, 102Ru]
---

# Polarization with a single planar Ge(Li) detector

## Bibliographic Record

- G. T. Ewan *et al.*, *Phys. Lett. B* **29B**, 352–354 (1969), PII `0370-2693(69)90382-7`.
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/polarizaiton/1969_Ewan et al_Gamma-ray polarization measurements with a single Ge(Li) detector.pdf`。

## Scope and Reading Depth

- Three-page letter fully read: planar 4×2.5×0.35 cm³ Ge(Li) geometry, 0.8–4.4 MeV calibration, `100Mo(α,2n)102Ru` application, angular-distribution correction and conclusion.
- Not covered: detailed theoretical calculation in the companion report.

## Key Results

- A single thin planar Ge(Li) detector measures polarization from Compton events in its total-absorption peak; asymmetry `Q=2(N⊥−N∥)/(N⊥+N∥)` is calibrated with polarized γ rays from `56Fe`, `24Mg`, `28Si` and `12C` (PDF pp.352–353, Table 1, Fig.1).
- 原EW69命名的correctedQ=2A/P为15.7%/10.4%/12.6%/6.4%，对应0.847/1.368/1.779/4.43MeV；若改用通常A/P定义，同计数合同下依次.0785/.0520/.0630/.0320，不能裸用原百分数作modernQ。photoelectric低能削弱响应，见EW69-D17-1–4。
- In `100Mo(α,2n)102Ru`, 475/631/766-keV transitions show positive E2 polarization, while an 833-keV line has opposite asymmetry and weak angular distribution, indicating mixed multipolarity (E1+M2 or M1+E2) (PDF pp.353–354, Table 2).
- Detector orientation/solid-angle differences are corrected below 1% for the calibration geometry, but response remains energy/geometry dependent (PDF p.353).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| EW69-1 | A single planar Ge(Li) detector can measure parity-sensitive γ polarization with sufficient sensitivity above ~0.8 MeV. | method-result | direct | PDF pp.352–354 | true |
| EW69-2 | `102Ru` calibration/application separates pure E2 and a mixed-polarity 833-keV transition. | application-result | direct | PDF pp.353–354, Table 2 | true |
| EW69-3 | Detector geometry, photoelectric contribution and incomplete-polarization correction control `Q`. | limitation | direct | PDF pp.352–353 | false |

## Summary

Ewan *et al.* demonstrate that even a single planar Ge(Li) can provide useful polarization/parity information. The source is a historical baseline for later segmented and Clover polarimeters; its `Q` values are calibration-specific.

## Competing Interpretations and Limitations

- Photoelectric absorption and finite detector geometry change `Q(E)`; the historical calibration cannot be transferred without remeasurement.
- The mixed 833-keV assignment remains a method demonstration rather than a universal parity rule.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| EW69-AR-1 | Response chain | Known polarized calibration → single-detector Compton asymmetry → corrected `Q(E)` → `102Ru` parity/mixing inference. | PDF Table 1, Fig.1 | self-checking |
| EW69-AR-2 | Transfer condition | Recalibrate orientation, solid angle, threshold and photoelectric fraction for another detector. | PDF pp.352–354 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[compton-polarimetry]], [[linear-polarization-asymmetry]], [[multipole-mixing-ratio]] and historical GeLi detector lineage.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `EW69-P0-1`: Do not transfer single-Ge(Li) `Q` values across energies/geometries without calibration.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]]。


## Day17原件自审：单晶Q的平均分母与百分数

本session先冻primed回忆，再实际新读3页/1图/2表/两个未编号定义与偏振式/10refs。hashded2493ef0e816b3ed74bc5921f61324ec71b1ae34de8be96c988c71fa3e7be5/260960bytes不变；旧EW69-1–3/true true falseflags保持，reviewunreviewed，新10条待审，不称human-reviewed。

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| EW69-D17-1 | 原Q=(Nperp−Nparallel)/[.5(Nperp+Nparallel)]=2A，计数是单planarGeLi两次转动的fullabsorptionpeak，不是两个Comptonabsorber的N；Table1right/图1再除knownP纠到100%。同合同的通常A/P灵敏度=Qcorr/2，物理P不因改名字变。 | observable and normalization dictionary | direct and algebraic | pp.352–353 Fig1/Table1 and Q definition | true |
| EW69-D17-2 | Table1 rawQ百分数8.3/9.7/10.2/6.4，correctedQ15.7/10.4/12.6/6.4；隐含P=.528662/.932692/.809524/1.000，仅同链派生不是新增P测量。通常A/P=.0785/.0520/.0630/.0320，各sourceσ同样除200，不重造Cov或CI。 | Codex actual-calibration arithmetic | derived | p.353 Table1 | true |
| EW69-D17-3 | 原planeGeLi4×2.5×.35cm³、16cm距，parallel/perp以crystalplane相对reactionplane定义；两orientation角接受不同，作者在此几何AD校正<1%inQ。不能转任意dist/array或当background/eff误差都<1%。 | geometry and count-role | direct | pp.352–353 Fig1 and orientation paragraph | true |
| EW69-D17-4 | 全能峰同时含Comptonscatter后吸收与无偏振asymmetry的photoelectric贡献，原theorycurve只前者，<约1MeV时差大；475是Coulomb已知2+→0+reference用同reactionAD/asymmetry标低能，不是独立的MC验证。photoelectricfraction/transport输入未给。 | response-dilution and reference-dependence | direct | pp.353–354 Fig1 discussion | true |
| EW69-D17-5 | 原p353印式对475给2.234742。随后EW69-D17-11精确核该式为强度比(1+p)/(1−p)，映有界p=.381713；此前把>1称超物理范围/公式failure的解释撤回。原P命名未明确，不将代数比值解释冒作已证作者意图或officialerratum。 | revised-convention interpretation | direct plus exact algebra | p.353 printed P90 formula; Table2 475 row | true |
| EW69-D17-6 | 在明确用TW70pureE2point合同的条件下，475/631/766的P90=.381713/.462110/.482389，代本sourceQraw得correctedEWQ约14.4087/15.3643/15.3403%，相应A/P约.07204/.07682/.07670；不是作者原job/新实验Q，不digitize图曲线或推σ。 | conditional cross-source exercise | derived | p.353 Table2 475/631/766 rows | true |
| EW69-D17-7 | 833的−3.4±1.3%是sourceQraw=2A，普通A=−.017±.0065而非physicalP；作者由非零偏振及weakAD提出E1+M2或M1+E2两候选。未得matchingQ833/原Cov/levelcompanion，不新定δ/Jπ或套pureE2公式。 | observable versus interpretation | direct and algebraic | pp.353–354 Table2 833 row | true |
| EW69-D17-8 | Table1校准为p,p'四条不同resonance/target：Fe3.145MeV/thick、Mg2.40/25µg/cm²、Si3.095/30µg/cm²、C5.375/200µg/cm²。与B73同γ能量不等同布居/P或实验谱系；校准ADcoeff未在Table1给，不借后文P强配。 | calibration-input identity | direct | p.353 Table1 | true |
| EW69-D17-9 | 文末新6×3.5×.65cm³detector只报告更高fullpeakeff、Qslightlyless并荐>1MeV，无实际该装置table/response；不能合并旧四点或据volume推FOM。Refs4/5/10是tobepublished，原producer/数据/Σ未取得。 | version and readiness | direct | p.354 conclusion/references | true |
| EW69-D17-10 | 本sessionfactor2/percent/三条E2source算术不增加独立实验；lettercalibration/application共detector与AD链，ChalkRiver不同于B73/TW70装置仍共已知nuclearlines/方法。newsource保需要review，无新P/Q/δ/Jπ/CI。 | independence and knowledge-impact | synthesis | pp.352–354 scope and tables | true |

[四校准/四Ru输入](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/ewan1969-calibration-contract.json)与[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/ewan1969-calibration-result.json)，script `system/scripts/day17_ewan1969_convention_audit.py`。初诊断曾给833也算pure式（toolstdout保），最终显式设为null；不用于新claims，见scope-correctionreceipt。

本次`revises`跨文Q数值比较的分母假设；后续精确代数撤回原“P>1即公式failure”解释，原式可表示强度比。`limits`未定命名便套有界范围及只由Qsign定δ；[[compton-polarimetry]]/[[linear-polarization-asymmetry]]保matchingcount/knownP/energygeometry。原Qcalc和actualpolarization不是同列，物理P与方法归一分开。


## Day17再审：撤回把强度比判为有界偏振度的failure

对照[[twin-1970-polarization-angular-correlation-40k]] TW70-D17-7的原pureE2式及[[schlitt-1994-sectored-compton-polarimeter]] Eq23/24后，本session继续作精确符号桥接，发现EW69印式并非必须违反物理。设TW70/SC94的有界pureE2偏振度为p，则

\[
p=\frac{\frac32a_2+\frac58a_4}{1-\frac12a_2+\frac38a_4},\quad
r_{EW}=\frac{1+a_2+a_4}{1-2a_2-a_4/4}
       =\frac{1+p}{1-p},\quad p=\frac{r_{EW}-1}{r_{EW}+1}.
\]

原EW式可严格解释为`Jparallel/Jperp`；例如475的r=2.234742映p=.381713，与TW70式完全一致。**撤回本session checkpoint053把>1直接叫“公式failure”的判断**，EW69-D17-5已定向修订，needs_review仍true；原历史版本/result快照保，不改raw。本文没有显式把该P定义为这一强度比，原Ref9书章body未得，所以代数自洽解释不升级作者意图已证，也不声称官方勘误。

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| EW69-D17-11 | 精确sympy桥证明印rEW=(1+p)/(1−p)，由(r−1)/(r+1)回TW70pureE2有界p；Ru475/631/766逐点相同。r>1对强度比允许，旧“>1物理failure”解释撤回，不把名义比值当实验degree。 | Codex belief revision / convention bridge | exact-derived | p.353 printed P90 formula | true |
| EW69-D17-12 | 同pureE2/point/已归一AD系数有W0/W90=1+p；它是两发射角强度比，不等rEW的两电矢量强度比。finiteacceptance需积分I/Q与同transition/门，mixed含interference不由此解δ；未实施新两角校准或给新P/Q/CI。 | observable-dictionary and transfer-boundary | derived | p.353 P2/P4-coefficient definition | true |

[修订的精确桥](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/polarization-ratio-degree-result.json)，script `system/scripts/day17_polarization_ratio_bridge.py`。旧EW69result的“formula_failure”布尔只在历史快照`ewan1969-calibration-result-before-ratio-audit.json`保，当前脚本/结果改用ratio字段与撤回标记；旧Git版本可恢复初计算，不把当时mistakeninterpretation沿用。
