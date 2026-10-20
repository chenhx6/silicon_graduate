---
type: source
title: "Wadsworth et al. 1977 - Gamma ray spectroscopy in 61Ni: levels below 2.2 MeV"
aliases: [Wadsworth 1977 61Ni spectroscopy, 61Ni levels below 2.2 MeV]
created: 2026-09-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Gamma ray spectroscopy in 61Ni-levels below 2.2 MeV in excitation"
authors: [R. Wadsworth, A. Kogan, P. R. G. Lornie, M. R. Nixon, H. G. Price, P. J. Twin]
journal: "Journal of Physics G: Nuclear Physics"
year: 1977
citation_key: wadsworth_1977_Gamma
volume: 3
pages: "35-53"
canonical_source: "Wadsworth et al., J. Phys. G 3, 35-53 (1977)"
library_file: "raw/papers/gpt/high-spin-20260920/纲图/1977_Wadsworth et al_Gamma ray spectroscopy insup61-sup Ni-levels below 2.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/纲图/1977_Wadsworth et al_Gamma ray spectroscopy insup61-sup Ni-levels below 2.pdf"
raw_sha256: "47533c460e7af3bdb01b6864790dc1f14aea69f4a1316ea4faf42eb28aec279a"
nuclei: [61Ni, 58Fe, 61Cu]
reactions: [58Fe(alpha,nγ)61Ni, 61Ni(p,n)61Cu]
experiments: [liverpool-geLi-compton-dsam]
models: [compound-nuclear-statistical-model, shell-model]
observables: [level-scheme, gamma-branching, angular-distribution, linear-polarization, mixing-ratio, DSAM-lifetime]
methods: [gamma-gamma-coincidence, angular-distribution, compton-polarimetry, doppler-shift-attenuation]
tags: [61Ni, level-scheme, DSAM, polarization, mixing-ratio, spectroscopy]
---

# Gamma ray spectroscopy in 61Ni: levels below 2.2 MeV

## Bibliographic Record

- R. Wadsworth *et al.*, *J. Phys. G* **3**, 35–53 (1977).
- 规范文件：`raw/papers/gpt/high-spin-20260920/纲图/1977_Wadsworth et al_Gamma ray spectroscopy insup61-sup Ni-levels below 2.pdf`。
- 19-page experiment; title/reaction/figures/tables and historical provenance checked.

## Scope and Reading Depth

- PDF pp.35–53 fully read: `58Fe(α,nγ)61Ni` coincidence experiment at 8.0/8.5/12 MeV, angular distributions/polarization at 7.8/11/13 MeV, `61Cu` β+ reference, Rose–Brink convention, Tables 1–4, level scheme, nine spin/parity assignments, mixing ratios and DSAM centroid shifts/lifetimes.
- Figure/table audit: spectra and decay scheme, all branching/mixing/lifetime tables and representative χ²/polarization plots.
- Not covered: raw spectra, full MANDY/DSAM codes, modern shell-model calculations and later reevaluations.

## Paper Question and Experimental Logic

The paper determines the low-lying `61Ni` level scheme below 2.2 MeV, spin/parity and γ multipole mixing using γγ coincidences, angular distributions, linear polarization and Doppler-shift attenuation, then compares with shell-model calculations.

1. Populate `61Ni` with `58Fe(α,nγ)` and use two Ge(Li) detectors for γγ coincidences; excitation functions and a `61Cu` β-decay source constrain branches.
2. Fit angular distributions with compound-nuclear alignment/population parameters and Rose–Brink phase convention; use a three-GeLi Compton polarimeter for linear polarization.
3. Extract centroid shifts versus `cosθ`, attenuation factors and mean lifetimes using Blaugrund/Lindhard stopping treatment.

## Key Evidence and Reasoning Chain

- 本session原件纠正旧转录：1015/1454为7/2−、1609为5/2−、1807/1987为9/2−、1997为5/2−、2018为7/2−、2121为9/2+、2129为11/2−，均按原1977作者/Table3/Abstract，不作为新测或现代评价裁决。见WA77-D17-1。
- 原作者对656-keV态偏好1/2−，保3/2−备选；AD/P零单独并未排3/2，另用寿命/外部B(E2)一致性，见WA77-D17-2。
- 原1015-keV的7/2−由AD/P联合分析；948线δ=−2.46，Table3误差.15、正文/Table4误差.16分别保留。
- 寿命按原fs单位：1609为370(30)fs（旧37误抄）；908摘要1500(400)fs、正文/Table4为1600(500)fs，是约1.5–1.6ps（旧ns误写），保来源内部差异。其余1132 450(30)、1186 140(20)、1454 1200(290)、1729 99(8)、1807 1600(250)、1987 960(240)、1997 72(6)、2018 580(60)、2124 84(6)fs，均作者结果而非本次新测。见WA77-D17-3/8。
- `61Ni` low-lying positive-parity states and negative-parity particle-hole configurations are compared with shell-model predictions; older Williams et al. assignments/lifetimes are explicitly contrasted, including disagreement for the 1454-keV spin and many lifetimes.

## Key Results

历史WA77-2含旧错误转录“3−”，**不再作为现行事实使用**；保留原行和needs_review状态以追溯，原件纠正以WA77-D17-1/2为准。WA77-4的falseflag保持，新增自审均待审。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WA77-1 | γγ coincidences, angular distributions and Compton polarization establish the low-lying `61Ni` decay scheme and multiple spin/parity assignments. | experimental-result | direct | PDF pp.35–53, Tables 1–3 | true |
| WA77-2 | The 656-keV level is most likely `3/2−`, while 1015 keV is assigned `3−` with a large mixing ratio. | experimental-assignment | direct | PDF pp.37–40, Table 3 | true |
| WA77-3 | DSAM centroid shifts yield lifetimes/transition strengths for levels from 908 keV through 2.1 MeV. | experimental-result | direct | PDF pp.35–36, Table 4 | true |
| WA77-4 | Rose–Brink convention, compound-population priors and detector response are essential to δ/spin inference. | limitation | direct | PDF pp.36–37, Methods | false |

## Summary

Wadsworth *et al.* establish a detailed low-energy `61Ni` spectroscopy baseline using the same joint angular-distribution/polarization/mixing-ratio logic as the contemporary `40K` and `61Ni` studies, while adding DSAM lifetimes and explicit cross-checks against `61Cu` decay and shell-model calculations.

## Competing Interpretations and Limitations

Spin/parity assignments depend on compound-nuclear population estimates, Rose–Brink sign convention, polarization-efficiency calibration and stopping/feeding assumptions in DSAM. Several old/new assignments differ; weak lines and unresolved branches should not be treated as equally secure.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| WA77-AR-1 | Evidence chain | γγ level links → `a2/a4`/polarization → joint χ² δ/spin/parity → DSAM lifetime/strength. | PDF pp.36–53 | self-checking |
| WA77-AR-2 | Convention | Rose–Brink phase convention is explicit; cross-source signs require mapping. | PDF p.36 | self-checking |
| WA77-AR-3 | Transfer condition | DSAM lifetimes require matching stopping/feeding and recoil velocity; angular/polarization Q/R are detector-specific. | PDF pp.36–37, Table 4 | active-L3 |
| WA77-AR-4 | Independence | Direct `61Ni` experiment; Meyer 1978/other `61Ni` papers are related but not duplicate rows. | Scope/Introduction | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` the `61Ni` spectroscopy/level-scheme baseline and method lineage for angular distributions, polarization, mixing ratios and DSAM.
- Persistence: link to [[meyer-1978-multiparticle-configurations-61ni-67zn]], [[angular-distribution]], [[linear-polarization-asymmetry]], [[doppler-shift-attenuation-method]] and the high-spin evidence map.
- Review state: Codex self-audited; not `human-reviewed`.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| supports | [[meyer-1978-multiparticle-configurations-61ni-67zn]] | Independent/preceding `61Ni`/`67Zn` spectroscopy lineage; compare level/lifetime assignments. |
| methodological-bridge | [[doppler-shift-attenuation-method]] | DSAM centroid-shift and stopping/feeding boundaries. |
| methodological-bridge | [[linear-polarization-asymmetry]] | Early three-GeLi Compton polarization and Rose–Brink analysis. |

## Human Review Triage

### P0

- `WA77-P0-1`: preserve assignment/lifetime disagreements with prior `61Ni` studies; do not collapse historical level lineages.

### P1

- `WA77-P1-1`: historical DSAM stopping/feeding and polarimeter calibrations require source-level reanalysis for modern absolute strengths.

## Extracted Pages

- Nuclei: `61Ni` (source-level).
- Methods: [[angular-distribution]], [[linear-polarization-asymmetry]], [[doppler-shift-attenuation-method]]。
- Sources: [[meyer-1978-multiparticle-configurations-61ni-67zn]]。

## L3/L4 Follow-up

- L3 question: reconcile `61Ni` level/lifetime/mixing-ratio lineages from Williams 1975, Wadsworth 1977, Meyer 1978 and later Samanta 2019 while preserving independent datasets. No L4 run: raw spectra/codes absent.


## Day17完整原件自审：自旋转录、fs单位与互补判据

本session已primed旧页，先冻主动回忆，再新读19页/8图/4表/1个未编号布居公式及全部p53references；Table3/4另旋转视觉核，不只信OCR。rawhash47533c460e7af3bdb01b6864790dc1f14aea69f4a1316ea4faf42eb28aec279a/889555bytes保持。旧WA77-1–4行/flags与review_status=unreviewed保；更正上述错误叙述，新增全部needs_review，不称human-reviewed。

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WA77-D17-1 | 原作者1015/1454=7/2−、1609=5/2−、1807/1987=9/2−、1997=5/2−、2018=7/2−、2121=9/2+、2129=11/2−。旧Wiki整数3−与多项J错是转录问题，不是原作者或EK79彼此矛盾，原Table3/Abstract可核。 | source-transcription correction | direct | p.35 Abstract; pp.40–41 Table3 | true |
| WA77-D17-2 | 656的三支AD/P与1/2−和3/2−都相容，作者另用粗τ<30ps、外部Andreev B(E2)↑5.9(.6)WU等取1/2−优选、保3/2−备选。RDM有实验困难仅粗关系，不能把本段当新精确时间测量或新课程卡。旧Wiki3/2vs5/2错。 | author-assignment and companion-boundary | direct | pp.37/39 Sec3.2 | true |
| WA77-D17-3 | 原1609寿命370±30fs，非旧Wiki37fs；908摘要1500±400fs而正文/Table4 1600±500fs，不合并，均ps量级而非旧ns。Table4τ误差不含stop，而strength用τ±25%allowance计stop；不能把两个误差预算写成相同。 | units and uncertainty correction | direct | p.35 Abstract; p.42 Table4 and footnotes | true |
| WA77-D17-4 | AD/P在7.8/11/13MeV同时测、三GeLi polarimeter在90°；AD用其scatterersingles一γ作externalmonitor，共归一依赖。7.8靶1mg/cm²/71%/厚Au，11/13靶760µg/cm²/87%；γγ8/8.5/12用不同selfsupportingtarget，不合并成同gate响应。 | actual-geometry and shared-normalization | direct | p.36 Sec2 | true |
| WA77-D17-5 | P/A/Q校准细节委托Butler1973 NIM108497，本正文不给actualQ/a(E)/Comptoncounts/threshold合同。因此Table3“experimentalpolarization”是作者报告P，不是裸A，不能由本篇恢复Q或把1973装置名等同1977精确response。 | polarimeter-response readiness | direct and full-paper negative-check | p.36 Sec2; p.53 Butler reference | true |
| WA77-D17-6 | 原用RoseBrink约定、CNRalignment和Gaussian-type β/x联合拟AD/P/δ/取向，以.1%CL拒spin、JT74方法给δerror；本文不展示完整Cov/actualrank或完整profile。p36印布居式缺显式minus/abs，保literal边界，不拿EK79后文补成1977producer。 | inference-contract and literal-boundary | direct | p.36 Sec2 population formula | true |
| WA77-D17-7 | branching常用56Co/125Sb相对eff加AD fitteda0，但Table1/3图特别注明1729/2018取90°强度、2018弱支估自γγcounts、1186在Fig3取61Cuβ+source。不同角色/门/角响应不裸替，限值不作中心yield。 | actual-branch-input provenance | direct | pp.37–38 Table1; p.45 Fig3 caption | true |
| WA77-D17-8 | DSAM由centroidchannel对cosθ直线与fullshift F=1比较，F→τ采用Blaugrund/Lindhard。Table4多F时给寿命weightedmean而非F先平均；908/1132/1454标feedingcorrected，1997/2018多beamtime。无actualstop/β0/fitCov，不给新τ/模型差原因。 | lifetime-response and aggregation | direct | p.37 Sec2; p.42 Table4; p.46 Fig4 | true |
| WA77-D17-9 | 1609和1997的AD/P各仍允许5/2−与5/2+；作者加入τ及M2强度数百WU（1997约550±280WU）排正宇称。因此P本身/符号不独断parity，最终是强度合理性条件判据，不把作者解释标直接P观测。 | necessary-companion demonstration | direct-author inference | pp.47/49 Sec3.8/3.12; Figs5b/6 | true |
| WA77-D17-10 | 原1609四γbranch37/54/5/4%与τ.370ps、δ.33/.07在声明γ-only/α0/标准WU下给BE2 .52029/.04674WU与BM1 6.8747/12.5953mWU，近Table4 .5/.05与7/13。只是源表单位/partialrate核，未知IC/Σ不拟合；错用37fs会都放大10倍。 | Codex actual-table exercise | derived conditional | pp.38/40/42 Tables1/3/4, 1609 rows | true |
| WA77-D17-11 | 1454线在θ>45°受Dopplershifted1446重叠，仅partialAD误差大；2121受1099/1114近线无法测τ，仅>500fs。1015/2129无shift F<.02只作者τ>3ps模型界，不带统一CL。 | energy-overlap and null-limit counterevidence | direct | pp.45–46 Sec3.4/3.7; pp.50–51 Sec3.14/3.16 | true |
| WA77-D17-12 | 908/1807与Williams1975寿命不同，作者提出cosθ点数3vs8等可能原因，非已证解释；1987γγ未见旧1334强支并新置四支，Table1保不同dataset。1975body未在本session核，不沿本篇复述冒称独立审完。 | historical-disagreement and source-independence | direct-author boundary | pp.39/49 Sec3.3/3.10–3.11; Table1 | true |
| WA77-D17-13 | Fig8MSDI/ASDI为shellmodel比较，56Ni inertcore、p3/2/f5/2/p1/2价空间，参数由Ni数据拟；作者lowcollectivity为强度/模型解释，不等另一个独立测量。 | model-versus-observation | direct | pp.51–52 Fig8 and Sec4 | true |
| WA77-D17-14 | 本session完整source不提供polarimeter原counts/response/actualΣ或stopping实现；没有re-fit δ/Jπ/τ。对EK79Ref7的同lab观测建立依赖，1979predictionerror不能倒写为1977actual误差。 | readiness and knowledge-impact | cross-source synthesis | p.36 methods; p.42 Table4; p.53 references | true |

[新实际rate输入](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/wadsworth1977-rate-contract.json)与[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/wadsworth1977-rate-result.json)，script `system/scripts/day17_wadsworth1977_rate_audit.py`。声明WU定义只作为计算单位；原文没有给其完整WU公式，中央近似闭合不认证实际producer/IC/fitCov。

本次`revises`旧Wiki整数spin/37fs/ns转录；`limits`Psign独断宇称、differentgatebranch和把先前装置校准当sameactualresponse。与[[ekstrom-1979-spin-alignment-attenuation-a61-a67]]、[[butler-1973-three-geli-compton-polarimeter]]、[[lifetime-strength-audit-165tm-136nd]]、[[linear-polarization-asymmetry]]相连。Butler是下一精确response原件入口，本段未预填其校准结果。


Butler原件续查：[[butler-1973-three-geli-compton-polarimeter]] B73-D17-1–14新核Eq3/4确为a先修count、P=A/Q，旧Wiki非线性额外分母已纠。1973的a1%/Qfit/门/校准源明确，但当前仍没有本文1977实际job确认；不把此引用升级samehardware/response/Σattestation。原WA77-D17-5边界保持。
