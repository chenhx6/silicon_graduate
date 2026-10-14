---
type: source
title: "Ciemała 2021：耗散反应的初速度展开与寿命线形方法"
aliases: [TKEL recursive unfolding lifetime, Ciemała EPJA 57 156]
created: 2026-10-14
updated: 2026-10-14
status: ai-draft
review_status: unreviewed
source_type: experimental-method-paper
reading_depth: deep-read
title_original: "Accessing tens-to-hundreds femtoseconds nuclear state lifetimes with low-energy binary heavy-ion reactions"
authors: [M. Ciemała, S. Ziliani, F. C. L. Crespi, S. Leoni, B. Fornal, A. Maj]
author_list_scope: first-six-of-public-copy
journal: The European Physical Journal A
year: 2021
volume: 57
pages: 156
doi: 10.1140/epja/s10050-021-00451-6
data_version: public-preprint-v1-and-published-final-both-seventeen-pages
canonical_source: "https://doi.org/10.1140/epja/s10050-021-00451-6"
citation_key:
raw_file: "raw/papers/gpt/day13/ciemala-2021-deep-inelastic-lifetime-method.pdf"
raw_sha256: "b6b3e032000e50f7332bb05393b2b7b8759bf41eb31a43932857f96b212c3bd3"
raw_storage_status: reserved-unpopulated-public-preprint-only
external_pdf_url: "https://arxiv.org/pdf/2012.05180v1"
nuclei: [13c, 17o, 18o, 19o, 20o]
methods: [doppler-correction, dsam, monte-carlo-transport, velocity-unfolding]
tags: [agata, vamos, paris, tkel, sensitivity-limit, formula-convention, shared-data]
---

# 末速度约束怎样进入发射历史

## Bibliographic Record

M. Ciemała等，European Physical Journal A **57**, article156(2021)，DOI如上；Crossref题名/作者/卷/article/发表月核验。读取arXiv2012.05180v1（2020-12-09，17页）与publisherfinal（17页、发表2021-05-03）。v1封面未插入journal页码；下列原claims明确标preprintPDF，新增claims标publisherPDF，不混用figure编号。

`raw_file`未填充；publiccopy实际`tmp/day13/reopened/ciemala-2021-deep-inelastic-lifetime-method.pdf`，SHA如上。Publisherfinal公开副本为`tmp/day13/reopened/ciemala-2021-method-publisher.pdf`，URL`https://link.springer.com/content/pdf/10.1140/epja/s10050-021-00451-6.pdf`，SHA`06255eba585919d4fd25ce987e224eead1185787f7041d9ab63cd47c8db25e87`；p.16明确CC-BY4.0。当前无版本号arXivURL仍返回v1相同hash。

与[[ciemala-2020-c16-o20-lifetimes]]及2019CO19/ZL19同18O126MeV+Ta6.64mg/cm²实验谱系，17O/19O controls与详细方法不是另一次独立测量。

## Scope and Reading Depth

- Covered scope：preprint17页和publisher17页主线、Sec.3数据准备、Sec.4 TKEL生成/transport/拟合/极限、Figs.11/15/18/20–26；preprintp.7与publisherp.6 Eq.(1)、publisherp.13 confidence/feeding和Fig.18/19已视觉核验。
- Not covered：生产事件、TKEL残差/正规化代码、实际二维χ²grid/完整统计定义、feedingentrytemplate、协方差与参考文献全文。已读方法仍不等源码可复现。

## Paper Question and Scientific Motivation

对初速度不唯一、direct/dissipative混合的低能binaryreaction，怎样用state-conditioned末速度、精细γ方向与transport重建可辨识的寿命，并界定短/长τ的sensitivitylimits。

## Method and Design Logic

数据准备→stateγ门下末速度→按TKEL递归重建direct/dissipative混合→eventgenerator抽靶depth/角/TKEL和衰变时间→AGATAGeant/OFT/response→以三角区线形共同拟合τ/Eγ。不同阶段的实验输入、输运内量、analysisreference与sharedcalibration应分别保存。

## Key Evidence and Reasoning Chain

一个宽末速度分布不能用平均β代表。TKELbasis可由已知运动学+材料/TOFresponse生成，再匹配逐态分布；该展开受生成器与响应限制。窄/长线、短态和极短态分别检验calibration、内部line-shape和sensitivityboundary，不能统称“controls全部通过”而丢失各自条件。

## Summary

本文提供100层靶、2MeVTKEL步进、TOFσ1ns与direct19O stoppingcontrol等具体细节，缩小了2019/2020的方法缺口。版本对照消除了对正式公式的疑点：v1文字标签与式冲突，publisherp.6明确Eγ为测量、Eγ0为校正并乘D；靶后reference/材料项也更具体。正式版本还新增80%总误差区域和cumulative/feeding说明，不能继续用v1“1σ”替代。90°“unaffected”仍须限制为低速一阶；这些文档/适用条件不证明生产代码错误或据此重判150fs。

## Experimental or Theoretical Setup

同18O126MeV+Ta6.64mg/cm²、31AGATA/PARIS/VAMOS实验。新细节包括入口driftchambers改善φ、PARIS/RF drift修正、有限beamspot与sourceenergyreplay。相同装置名称不能补成与VD16heavy-ionMWPC的同一运行/config。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CM21-1 | 同18O+Ta测量；入口driftchambers给方向，20O1.6–1.9MeVγ FWHM改善约1.4；TOF用102ns RF、v=D/T。 | experimental-fact | direct | preprintPDF pp.3–4, Fig.3 and Sec.3.1 | true |
| CM21-2 | PARIS–RF drift修正改善massFWHM约1.2；beamspotσx=.5/σy=.4mm，保留距中心4mm内trajectory。 | experimental-criterion | direct | preprintPDF pp.4–5, Figs.6–7 | true |
| CM21-3 | Trace/OFT重放含crosstalk/neutrondamage、timing、core/segment恢复；静止energyanchors多数detector residual<.2keV、4detectors约.5keV，Mg2754lineFWHM改善1.4。 | experimental-criterion | direct | preprintPDF pp.6–7, Figs.8–10, Sec.3.2 | true |
| CM21-4 | p.7 Eq.(1)印Eγ=Eγ0/[γ(1−βcosθ)]，紧接说Eγ0为measuredlabenergy、θ为反冲/γ夹角；与以这些输入还原restenergy的标准乘法inverse不同。 | synthesis | direct | preprintPDF p.7, Sec.3.2.1 Eq.(1)/following definitions; visually verified | true |
| CM21-5 | 校正β包含入口DC能损（先LISE oxygenlaw），再用long>1ps19O1375.80和13C3853.170keV线fine-tune；velocitychanges .4%/.7%，不报告为分辨率。 | experimental-criterion | direct | preprintPDF p.7, Fig.11/text | true |
| CM21-6 | TKEL从逐态末速度递归展开；靶100层、随机reactiondepth，每层beam能损约.1MeV；按实测角度抽样、TOFσ1ns，ΔE*=2MeV、nmax10，归一化后递归相减。 | experimental-criterion | direct | preprintPDF pp.8–10, Sec.4.1, Figs.14–15 | true |
| CM21-7 | 19O1471直接布居/已知运动学下，改变Ziegler stopping最多20%，末velocityfit作者1σ约束variation<5%；ATIMA能损差约2–3%，作者认为后续影响可忽略。 | author-interpretation | direct | preprintPDF pp.9–12, Fig.18/text | true |
| CM21-8 | 主MC典型4×10⁶events，TKEL/depth/角与τ生成γ，经真实31crystalgeometry、AGATAsimulation与同OFT/response分析；Fig.19 firstpointdistribution比较。 | experimental-criterion | direct | preprintPDF pp.10–12, Sec.4.2, Fig.19 | true |
| CM21-9 | Fig.20明确长τ校正使用ionfinalvelocity(aftertarget)，寿命长于crossingtime时角区有对称同centroid；Tcross约130fs，展示20/100/2000fs。 | experimental-criterion | direct | preprintPDF pp.12–13, Fig.20/text | true |
| CM21-10 | 17O2184line联合拟合τ159(+40/−30)fs/E2184.3(+.3/−.2)keV；19O2779line复用140(+50/−40)fs/E2779.0(+1/−.8)。 | experimental-fact | direct | preprintPDF pp.13–14, Figs.21–22 | true |
| CM21-11 | simulation给sensitivity约.2Tcross–4Tcross；long19O2371给τ>400fsvalley，ultrashort17O3842给0–70fsvalley；引用E3842.3(.4)才给20(+20/−20)fs。 | experimental-criterion | direct | preprintPDF pp.13–15, Sec.4.4, Figs.23–24 | true |
| CM21-12 | 作者称90°detectors不受Dopplershift，有助精确E；该说法在精确Lorentz/finiteangularcoverage下需适用条件。 | author-interpretation | direct | preprintPDF pp.12/15, Fig.20/short-limit discussion | true |
| CM21-13 | 17O2184的frontsegment处理相对fulltracking：1σ区域E约5倍、τ约2.3倍，χ²minimum约2.5倍；同数据重处理不能重复计独立experiment。 | experimental-fact | direct | preprintPDF pp.15–16, Sec.4.5, Figs.25–26 | true |

| CM21-14 | Publisher Eq.(1)为Eγ0=Eγγ(1−βcosθrel)，明确Eγ measured、Eγ0 corrected，物理inverse一致；v1文字标签冲突未沿用。 | experimental-criterion | direct | publisherPDF p.6, Eq.(1)/definitions; visual | true |
| CM21-15 | Publisher明确aftertarget v=vV+ΔvV，ΔvV=T/[vV² f(θ,φ)]，T先取LISE并按Z由knownlongline fine-tune；文字称f正比DCpathlength。T非TOF的同量，未给实际数值/Σ。 | experimental-criterion | direct | publisherPDF pp.6–7, Sec.3.2.1, Fig.9 | true |
| CM21-16 | 正式版示1375.80keV19Ocontrolτ1.27ps、3853.170keV13Ccontrolτ12.4ps；Mg2754line来自PARIS NaI neutroncapture生成24Na后βdecay。 | experimental-criterion | direct | publisherPDF pp.5–7, calibrationtext/Fig.9 | true |
| CM21-17 | Publisher Sec.4.3把statistics/stopping/background/ionvelocity systematics并入totalerrors，所示区域按80%CL；preprint同controls说1σ，不能统一换标。 | experimental-criterion | direct | publisherPDF pp.12–14, Sec.4.3, Figs.18–21/captions | true |
| CM21-18 | Publisher明称获得cumulativelifetime、可能含feeding；作者以无观察到populatingγ解释所考虑cases feedingnegligible。此为有检测边界的作者解释。 | author-interpretation | direct | publisherPDF p.13, Sec.4.3 | true |
| CM21-19 | Publisher图14黄线为fulltargetsum初速度、绿线为first10layers；v1图17绿线则写midtarget。randomdepth以约60%abovebarrier/beamenergy~10%variation时crosssection近constant论证；ΔTKEL2MeV称与VAMOSenergyresolution一致。 | experimental-criterion | direct | publisherPDF pp.8–10, Sec.4.1/Fig.14; preprintPDF pp.9/11 Fig.17 | true |
| CM21-20 | Publisher数据声明noassociateddata或不deposit，说明AGATAcollaboration ownership/DataPolicy；文章CC-BY4.0不授予events可访问性。 | experimental-fact | direct | publisherPDF p.16, Data Availability/Open Access | true |

## Nuclear Structure Information

17O/19O为已知τcontrol，20O150fs引用2020结果。各control的exactτ、γ能量、target-crossing条件分开；本页不报告新的absolutestrength或结构归因。

## Authors' Interpretation

tracking精度、precisevelocity与扩大angularcoverage使该方法适用于binaryreaction，stoppingcomparison/knownstatefit支持其transport。这些证据在同experiment内互补；不能增加独立采集数量或消除全部model/prior依赖。

## Model Results

TKELbasis、MonteCarlogenerator、target-crossing/sensitivity范围均是本文source模型/方法结果；不是任务复现productiontemplates。ATIMA对照与variation<5%保留作者的state-conditioned验证范围。

## Competing Interpretations and Limitations

- preprint Eq.(1)若照v1文字标签写lab→rest会再做一次forwardboost；publisher已把label/式匹配，消除了该正式文档疑点。生产code仍未取得，不由v1标签错误推断执行错误。
- preprintp.11/16部分stage叙述不清；publisherpp.6–7/11–12/16明确aftertargetreference与生成initial/emission链。代码字段仍需核，但已不再说source毫无stage定义。
- longγfine-tunevelocity本身使用energyreference，不能再把同线匹配计成完全独立energy/velocity校验；需hold-outangle/line和共同Σ。
- TKEL递归subtraction保留有益data约束，但basisoverlap、targetdepthprior、bin/iteration、normalization与负residualhandling需真实代码/closurepacket。实测accepted角度不能自动恢复full4π分布。
- CM21-15的公式Δv=T/(vV²f)与文字“f正比DCpath”还须生产定义核验：固定T/v时公式随f减小，而通常更长材料path应增加能损回补。这是本任务monotonicity检查，未得T/f规范化、代码或实际anglefit，不补写一个“正确f”或断言执行失败。
- 正式版cumulative/feedingnegligible解释以未观测feedingγ为依据，不能缺少efficiency、population、threshold或unseenbranches就给严格feedingupperlimit。2023发现1156feeder提供必要检查，但两个reaction的upperstatepopulation不同，不能反推它在2017sample占相同f。
- 90°在β一阶消除longitudinalshift，γfactor仍产生transverse效应；±10°角区也不是单点90°。状态/发射时β不同会留下残差。
- .2–4Tcross是该geometry/model的灵敏度区间，不是普适测量能力或仅靠τ/T判断全部identifiability；energy/response/feeding仍相关。

## Analytical Reconstruction

| ID | 审核项 | Agent判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| CM21-AR1 | 速度stage | DC-loss/fine-tuning属于analysisreference；TKEL入口与transport发射量另列，p.12finalreference是明确文字。 | CM21-5/6/8/9 | unreviewed |
| CM21-AR2 | formula/执行 | v1 label冲突/正式版一致均视觉核验；以final定义作方法入口，roundtrip不替productionaudit。 | CM21-4/14/15 | unreviewed |
| CM21-AR3 | 停止验证范围 | 1471state的fit与modelcomparison增加约束，仍与RF/calibration/kinematics同谱系；不是新independentstoppingmeasurement。 | CM21-1/5/7 | unreviewed |
| CM21-AR4 | 敏感度反证 | 两端valley、energycondition、80%totalerrors与cumulativefeeding须同时保留；frontsegment只改同data处理。 | CM21-10/11/13/17/18 | unreviewed |

## Knowledge Impact and Learning Decision

写回 [[doppler-correction]]、[[doppler-forward-inverse-convention-check]] 与 [[doppler-velocity-validation-contract]]，推进velocitystage、crossingsensitivity与sharedcalibration设计；actualL4仍not-ready。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| same-lineage | [[ciemala-2020-c16-o20-lifetimes]] | 同data详细TKEL/controls，不新增独立150fs实验。 |
| same-lineage | [[ziliani-2019-agata-calibration-controls]] | timestamp/energyreplay的后续描述。 |
| comparison | [[zanon-2023-o20-high-precision]] | 初速度/entry/feeding不同约束，原因仍未决。 |
| methodological-bridge | [[doppler-correction]] | stage/sensitivity/calibrationtransfer。 |
| methodological-bridge | [[doppler-forward-inverse-convention-check]] | Eq.(1)与productionboundary。 |
| methodological-bridge | [[doppler-velocity-validation-contract]] | data/prior/held-outclosure。 |

## Human Review Triage

P0：公版PDF与raw未归档边界隔离；v1标签边界已由正式版澄清，不外推code错误；articlelicense与dataownership分开。P1：CM21-4/5/6/7/9/11/12与实际fit/template/Σ，保持unreviewed。

## Extracted Pages

两version各1–17主线；preprintp.7 Eq.(1)/Fig.11、publisherp.6 Eq.(1)与p.13confidence/feeding视觉核验；publisher8–12TKEL/transport/stop，13–16χ²control/sensitivity/position/datapolicy。参考文献仅核相关入口，不称全部读完。
