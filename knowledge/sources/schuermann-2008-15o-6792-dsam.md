---
type: source
title: "Schürmann2008：15O6792的DSAM有限寿命反证与几何校准"
aliases: [Schuermann 2008 O15 DSAM, Schürmann 2008 lifetime6792]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: experiment
reading_depth: deep-read
title_original: "Lifetime measurement of the 6792 keV state in 15O, important for the astrophysical S factor extrapolation in 14N(p,γ)15O"
authors: [D. Schürmann, R. Kunz, I. Lingner, C. Rolfs, F. Schümann, F. Strieder, H.-P. Trautvetter]
year: 2008
journal: Physical Review C
volume: 77
pages: 055803
doi: 10.1103/PhysRevC.77.055803
citation_key: ""
canonical_source: https://doi.org/10.1103/PhysRevC.77.055803
raw_file: raw/papers/2008_Schuermann_et_al_15O6792_Doppler_attenuation.pdf
raw_sha256: e052b2ab382b9982522d009612cb1362f4ecb981a8724ad7b3829ff492671f61
raw_storage_status: verified-raw-archive
raw_archive_verified_at: 2026-10-23
nuclei: [15O, 14N]
reactions: [14N(p,gamma)15O, 19F(p,alpha-gamma)16O]
methods: [doppler-shift-attenuation-method, centroid-shift, geometry-calibration]
tags: [DSAM, lifetime, upper-limit, calibration, stopping, counter-evidence]
---

# 15O6792：数据点相容不等于寿命提取结论相同

## Bibliographic Record

D. Schürmann等，PRC77,055803(2008)，DOI[10.1103/PhysRevC.77.055803](https://doi.org/10.1103/PhysRevC.77.055803)。Crossref题名/七作者/卷/文章号/2008-05-13出版日期已核。实际原读[arxiv0804.1934v1](https://arxiv.org/abs/0804.1934v1)七页，页边11Apr2008而正文dated11Nov2018。官方src含`\date{\today}`，只说明日期为编译时变量，不能将它当2018新测量或官方科学更正；所用PDF/hash完整保留。未取得/比较期刊VoR body。

Actualcache `tmp/day17-schuermann2008/PDFs/Schuermann_2008_Lifetime_measurement_6792_keV_15O.pdf`，SHA256`e052b2ab382b9982522d009612cb1362f4ecb981a8724ad7b3829ff492671f61`；officialsrc包hash`8fe6218d63ce3a340e1dc237fca327c161d8fe78786cea2ae07e4770219a28d1`。raw保留槽未填，protectedBib未改。

## Scope and Reading Depth

本session来源前承认metadata/abstract与其它DSAM priming后冻结回忆，再原读七页全部主线/参考、Figs1–9、TablesI–II、Eqs1–2；PDF1–6所有主要图表/式视觉核。未读Ref12 Bertone2001或Ref18 Bister1977 primary，未取得原centroids/jointΣ、sixth-orderstoppingpolynomialcoefficients或SRIM collisionhistory；不给原谱重拟合信用。

## Summary

本文用同一HPGe的密角扫描、时间增益监控和五线共享geometryfit，将6792/6172的F提取推到与fullDopplershift相容，只报告寿命上限。原作者保留“旧数据与新数据不矛盾”同时反对旧有限寿命结论；它是测量/校准/提取合同的重要反例，不能用论文票数决定真值。

## Experimental or Theoretical Setup

Bochum500kV加速器、100–150µA protonbeam，实际Ep318keV在N-implantedTa的厚靶yieldplateau上经过Ec.m.259keV窄共振；不能把318/259当同一beamenergy。单108%HPGe位于转台，frontface13.1cm，约−40°至116°，多次反向/左右对称及两targetholderpositions核几何/吸收。CaF靶6129-keV线在相同束流focus/energy下反复监控增益；这条line有angle-dependenttail，不是无条件纯stoppedreference。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| SCH08-1 | metadata2008与actualarxivv1标签/dated2018字面分开；官方tex date today，不用编译日期造新实验/改raw。七页/九图/两表/两式本session实际完整原读。 | identity-version-and-reading | direct-original-and-metadata | PDF1；source-version receipt | true |
| SCH08-2 | 实际beamEp318keV、N-implantedTa厚靶yieldplateau选择Ec.m.259keV resonance；targetprofile/饱和stoichiometry假设进入slowing，不是Sun128MeVtransfer/Au的同response。 | experimental-kinematics-and-stopping-input | direct | PDF2–3 SecII；Fig4 | true |
| SCH08-3 | 同一Ge在转台扫描，左右/不同holder/重复角可检geometry/beamalignment；初geometry不确定约3mm，combinedfit给a−2.6mm、b.4mm。不能把单独转台nominalangle当已知无误差。 | geometry-calibration | direct | PDF2–5；Figs3/7/8 | true |
| SCH08-4 | CaF6129reference的0/90°tail形状不同，background处理可令centroid差至1keV；作者采用0°errorfunction/90°linear后约.15keV相合。gainoffset约±.08keV、slope relative5×10⁻5与时间趋势修正，皆同calibration链。 | reference-background-and-gain-boundary | direct | PDF3–4；Fig5 | true |
| SCH08-5 | Eq1 Eθ=E0[1+β0 P F cosθ]，P=.987为GEANT4有限Ge尺寸Doppler修正，非线偏振P、polarimeterQ或angularQk。F=Delta/(Deltafull P)保留分母。 | formula-and-symbol-contract | direct | PDF4 Eq1；PDF5首段 | true |
| SCH08-6 | 五条line combinedfit共同a/b，primaryF仅允许在1±.01，secondaryF独立；primarylines用于约束geometry，不能把所有五F当五个无约束独立参考。正文2385与TableI/Fig8的2375字面差保留。 | shared-fit-and-input-boundary | direct | PDF4–6；TableI；Fig8 | true |
| SCH08-7 | 本次secondary5181 F.78(.02)、τ8.4(1.0)fs；6172与6792均F.99(.01)、τ<.77fs。TableI较旧BertoneF.68/.91/.93与τ9.67/2.1/1.6来自其转引，不算本任务已读旧primary。 | reported-fit-and-limit | direct-current-and-cited-old | PDF6 TableI；PDF5 SecIII | true |
| SCH08-8 | 原文称旧F.93被本密角数据排除>5σ，同时称旧data点与当前不矛盾。该显著性是作者的具体拟合比较，不能把两个reported中心差/合并误差自动读成同一test。 | author-comparison-and-statistical-object | direct-and-boundary | PDF5左栏；PDF6 SecIV；Fig7 | true |
| SCH08-9 | Eq2的F由衰变权重平均recoilprojectedvelocity，SRIMcollisiondetails再拟sixth-orderpoly；implantN interstitial/Tadensity假设影响curve。作者称N:Ta1:1替代令1σupperlimit仅+2%、5181约9fs；未给完整Σ/curvecoefficients，不能复现originalτfit或改称90%limit。 | stopping-model-and-upper-limit-semantics | direct-and-boundary | PDF5 Eq2/SecIII；Fig9 | true |
| SCH08-10 | 5181finiteτ与旧评价8.2(1.0)fs相合是methodcontrol，但共享本次calibration/slowing；TableII对14N两态再用Bister1977的旧experimentalF重算8.1(.4)fs和14(8)fs，不是另测两态。原primary未得，所谓independentcheck须保留此依赖。 | companion-observable-and-source-dependence | direct-and-boundary | PDF5–6；TableII；Ref17/18 | true |
| SCH08-11 | 本任务按Eq1中心值，P.987×F.99给Delta/Deltafull=.97713；若错误省P，apparentF下降.01287。仅条件normalization敏感性，不是原作者错误/实际τbias；P误差与Cov未得。 | conditional-design-exercise | derived-from-source | Eq1；schuermann2008-attenuation-result geometry_mapping | true |
| SCH08-12 | 将两个reportedF误差额外当独立SD，6792中心差contrast约1.897，而固定旧central/仅用新scale约6；5181F差约2.774且τ差仅约.774。这些不是原作者>5σ重现或新CI，显示F→τ模型和test对象不能混。 | conditional-summary-statistics-boundary | derived | TableI；schuermann2008-attenuation-result contrasts | true |
| SCH08-13 | τ<.77fs给ℏ/τ>.85482eV，与作者Γγ>.85eV中心换算相合；数学上首先是totalwidth，radiative/branch条件需另保留。本文lowerlimit/1σ措辞不能无输入升级成90%bound或完整capture反应率。 | conditional-width-and-inventory-boundary | direct-and-derived | PDF6 SecIV；schuermann2008-attenuation-result width_conversion | true |

## Nuclear Structure Information

15O6792亚阈3/2+态关系到14N(p,γ)15O的groundstate S因子外推，但这里的DSAM观测首先约束F/τ。R-matrix的γ宽度和不同数据取舍属于另外的分析层，不由本τ上限唯一固定S(0)或核结构模式。

## Authors' Interpretation

作者认为新数据不能提取6792/6172的finiteτ，并对该快态能否用DSAM测finitevalue表示怀疑；其叙述不是普遍禁止所有装置改进后的fs寿命测量。本文没有改变R-matrix外推的全部结论，也要求更多直接数据/详细分析。

## Model Results

GEANT4P、SRIM减速与sixth-orderpolynomial、interstitialN/Ta密度是模型输入；所列误差/替代stoichiometry不能自动视为完整Bayesianprior或actualjointΣ。全stoppingkernel未得，不由一个Fτpair反解并制造authorcurve。

## Competing Interpretations and Limitations

- 更好的geometry/energycalibration可将apparentattenuation改为fullshift-compatible，不能把finiteτ的消失全归于统计增加。
- 相同sourceF列对应不同slowingmodel时，F差异与τ差异不能用一个commoninversecurve解释；表里的参数不是实验独立性证据。
- primaryF被限制到1±.01有其物理假设和共同geometry作用；需原input/Σ才可问对此先验/限制的敏感性。
- 原v1保留2385/2375与6791/6792等标签字面；不修改原件，不凭小转录差否定实验。

## Analytical Reconstruction and Self-Audit

[冻结合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/schuermann2008-attenuation-contract.json)、[程序](../../system/scripts/day17_schuermann2008_attenuation_audit.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/schuermann2008-attenuation-result.json)保存真实TableI五行/TableII两行与限定算术。所有Σ/概率假设另列；F/P缺Cov不填零，不把独立SDcontrast拿去否定作者profile结论。原ξ/Compton定义不迁到本P，DSAM有限尺寸P也不迁回polarization。

## Knowledge Impact and Learning Decision

`revises`把finiteτ/upperlimit当只由σ大小决定的习惯；`supports`共同几何/能标/companion控制的必要性；`limits`原表旧新比较和“independentcheck”的独立性。原实验、作者解释、SRIM/GEANT模型和任务推导分层；新claims全needs_review，不设human-reviewed。

## Human Review Triage

P1：若用于正式寿命/核反应率结论，先核原VoR、Bertone/Bisterprimary与actualcentroid/MC/Σ。当前不把这些缺口自动派给用户，也不假称已获得原数据。

## Extracted Pages

[[doppler-shift-attenuation-method]]、[[lifetime-strength-audit-165tm-136nd]]；与[[sun-2023-bayesian-dsam-31s]]按不同实验/观测对象比较，不迁参数数值或当同data重复验证。
