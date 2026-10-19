---
type: source
title: "NNDC 207Pb/207Bi参考记录：混合比、归一依赖与光子角色"
title_original: "207Pb Adopted Levels, Gammas and 207Bi EC Decay; ENSDF201102"
aliases: [NNDC Pb207 Bi207 reference records, 207Pb1064 polarization calibration]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: evaluated-selected-data-records
reading_depth: read
authors: [F. G. Kondev, S. Lalkovski]
year: 2011
journal: Nuclear Data Sheets
volume: 112
pages: "707-853"
doi: "10.1016/j.nds.2011.02.002"
data_version: "ENSDF201102; cutoff2010-08-01; EC format note2012-03-07"
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "NNDC ENSDF207082001/207082005; Kondev/Lalkovski NDS112,707-853(2011)"
source_url: "https://www.nndc.bnl.gov/ensdf/"
raw_file: "raw/data/gpt/day17-20261019/pb207-adopted-81eeda5ce504.ens"
raw_sha256: "81eeda5ce5045342b86f2f89a2612470cd50f707434d710fa670e9f5a5c850de"
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [207Pb, 207Bi]
reactions: []
experiments: [triumf-griffin-compton-source-calibration]
models: [BrIcc]
observables: [multipole-mixing-ratio, internal-conversion-coefficient, photon-emission-probability]
methods: [ENSDF-field-audit, source-reference-identity, covariance-propagation]
tags: [NNDC, source-calibration, polarization, normalization, covariance]
---

# 207Pb源参考：compiled数值与独立标定不是一件事

## Bibliographic Record

NNDC官方DatasetFetchServlet的quick207PB选择给Adopted`207082001,207PB`、`207BI EC DECAY`为`207082005,207PB`，均页面标2011-02。按页面实际form POST精确selected key取得ENSDFtext，完整wrapper/text双hash保留。初次遗漏searchType返回200home，已识别而未当核数据；旧NSRlegacyURL同样只返homepage，随后按现行公开JS找到真正KeyNumberSearchServlet，未将home/404当原paper。

Crossref核Kondev/Lalkovski、*NDS*112,707–853、2011年3月和DOI。header为201102、cutoff2010-08-01；EC另有J.Tuli2012-03-07 format note“Moved some EKC,ELC to2Grec”。2012format更改与2026获取不是新独立测量。

| 对象 | 真实缓存 | SHA-256 |
| --- | --- | --- |
| Adopted1488行 | `tmp/day17-pb207-reference/adopted.ens` | `81eeda5ce5045342b86f2f89a2612470cd50f707434d710fa670e9f5a5c850de` |
| 207Bi EC154行 | `tmp/day17-pb207-reference/bi207ec.ens` | `407ab95256d74a0db2be414f91315d13361ce80a9baef3fe36b8744436a47e4d` |

[selecteddownloads](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/pb207-selected-downloads.json)保存payload/HTTP/hash。raw归档槽未填，未修改raw/Bib。参考格式另按[[tuli-2001-ensdf-format-manual]]本session原PDF24/30视觉核N与EC栏，不能从一个float列猜单位。

## Scope and Reading Depth

完整读本selected EC对象154行；Adopted只读header/字段说明、0/569/1633及3726-keV母态和相关γ/comments，不通读其1488行全部能级，更不称通读147页A207评价。目标是[[garnsworthy-2019-griffin-facility]] GF19-8–10的207Bi源参考和[[grsisort-2026-compton-polarimetry-code]]旧模板所需的身份、MR和概率边界。

NSR1976Av01实际单record及Crossref核primary题名/作者/DOI，尚未取得其原正文；APS landing403与官方harvest401已记录，未重试权限终态/改凭据。原source评论中的数据可作为评价信息，不能冒充本session直接读primary。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| N207-1 | 当前选定对象为201102评价，cutoff2010-08-01；EC2012更改为字段搬移。Adopted/EC共享评价与旧实验，不是两次独立reference测量。 | evaluated-object-and-version | direct-evaluation | Adopted L2–5；EC L2–5 | true |
| N207-2 | Adopted E1633.356(4),13/2+与E569.6982(20),5/2−；EC为1633.358(4)/569.6988(20)，γ1063.656(3)/569.698(2)，终态1/2−。level least-square差/光子recoil/舍入不要求与Eg逐位同值，需保持母态/终态身份。 | transition-identity | direct-evaluation | Adopted L78/L92/L155/L168；EC L23–24/L34/L79/L84 | true |
| N207-3 | 1063.656γ为M4+E5、MR显式+.02、DMR1，即+.02±.01；570γ为E2但MR栏空，不等于独立测得δ严格0。codecomment+.03不是官方central/误差，也不构成显著冲突；native/first-last/operator相位仍需另核。 | mixing-input-and-phase-boundary | direct-evaluation-and-format | Adopted L92/L168/L179；EC L34/L84/L100–102；TU01-1/2 | true |
| N207-4 | EC把MR追到1976Av01的γγ角关联合并已有数据；1977Ku09另报A2=.259(.016)、A4未报并推δ+.12(+.08−.06)。它是评价保留的不同primary输入，不由当前字段或source标签自动消除。 | measurement-lineage-and-counter-input | direct-evaluation | EC L100–102；Adopted L179 | true |
| N207-5 | EC的Nrecord NR=BR=NB=1，RI570=97.75(.03)、RI1064=74.5(.3)按该branch为每100母体光子；570总CC=.0217(.0003)、1064=.128(.004)来自实验汇总。Adopted总CC由BrIcc给.0216/.1257，来源/误差层不同，不能裸合并。 | probability-normalization-and-ICC-provenance | direct-evaluation-and-format | EC L6/L17/L34–36/L84–86；Adopted L5/L92/L168 | true |
| N207-6 | RI570 comment写(100−.131)/(1+α570)，.131是另一旁路1442γ的RI；故RI570与α570是派生依赖。当前任务声明独立bypass/αprimitive时，total RI(1+α)的α项取消；这不是恢复原jointΣ。 | derived-normalization-covariance | direct-comment-and-task-derivation | EC L38/L121–127；pb207-reference-audit-result normalization | true |
| N207-7 | selected cascade中1064先发后，570光子概率名义1/(1+.0217)=.9787609；每207Bi母体的双光子发射概率条件值约.7291769，非两条marginal singles乘积.7282375，更非探测符合效率。原Q/门/角权重/背景Σ未得。 | cascade-photon-vs-detection-boundary | direct-input-and-conditional-calculation | EC L34/L84/L121；pb207-reference-audit-result photon pair | true |
| N207-8 | Adopted还有1063.71γ、[M1]、来自3726.094-keV母态，尾标?；不能能量近便绑定reference1063.656。母体207Bi QEC2397.5(21)不能直接populate该高母态；这只约束纯207Bi decay，不排其它污染/背景。 | near-energy-identity-and-source-selection | direct-evaluation-and-energy-boundary | Adopted L611–623；EC L8 | true |
| N207-9 | EC在569.6988 level记录IB=.0380(.0022)%、IE=8.9(.5)%；Nrecord定义其单位。GF19 PDF26的“noβparticles”不能当数学上绝对零β+的输入约束，实际background/selection影响并未由这个小branch计算。 | beta-plus-companion-and-scope | direct-evaluation-and-format | EC L24–33；TU01-6；GF19 PDF26 | true |
| N207-10 | MR+.02的E5份额δ²/(1+δ²)≈.00039984，但双线性系数2δ/(1+δ²)≈.039984；强度near-pure不保证P的同等小误差。这只是振幅系数，不是实际P改变量或实验CI。 | interference-versus-intensity-boundary | task-derivation-from-evaluated-input | EC L84；pb207-reference-audit-result mixing boundary | true |
| N207-11 | NSR真record1976AV01为Avignone/Girard、PRC13,2067–2070(1976)、DOI10.1103/PhysRevC.13.2067；bibliography verified但APS primarybody未得。未从NSR的measuredγγ字段补写原fit/phase/Σ。 | primary-identity-and-readiness | direct-NSR-and-metadata | NSR KeyNumberSearchServlet1976Av01；Crossref exactDOI；avignone1976-body-boundary | true |
| N207-12 | Adoptedheader虽201102，所取Qrecord引用2012WA38且comment另列evaluation用2003Au03旧Q；currentselected object不是2011出版物字节不变的保证。本文reference的QP/Eg/MR保持各自字段来源，不用fetch日期或一项mass更新抹成全dataset新测量。 | record-level-version-boundary | direct-evaluation | Adopted L2–8；EC L3–8 | true |
| N207-13 | 用EC Precord QEC2397.5keV和standard2m_ec²≈1021.998keV，β+到1633.358 level的名义预算约−257.856keV、到569.6988 level约805.803keV；上支β+直接馈入在该source条件下不开放。因此全source少量β+不等于1064/570选中cascade本身有β+，实际随机/污染背景仍需events。 | energy-accessibility-companion-boundary | direct-input-and-kinematic-inference | EC L8/L24/L79/L81；TU01-7 | true |

| N207-14 | 用本页真实13/2→5/2→1/2与pureM4/E2条件，双角色共享I但P90分别−24/101与183/505；directtrace/exactCG/F–F3核闭合。该P不是source测量、原phase或真实arrayQ。 | task-conditional-role-calculation | derived-model | N207-2；N207-3；pb207-stokes-result exact_formulas | true |
| N207-15 | 声明native±.02时P1064约−.250149/−.225222、P570约.374204/.350118；tinyE5强度不保证P同阶小误差。下支pure、无扰动/实际接受与primaryphase桥接是条件，未重标实验Q或造CI。 | task-interference-and-response-boundary | derived-model | pb207-stokes-result rows theta90；N207-10 | true |

## Summary

这组官方记录提供实际reference的signedMR、ICC/光子归一与旧数据谱系，收窄[[triumf-griffin-compton-source-calibration]]的输入缺口。已知reference数值不等同于已知matching gate/response/Σ；不能把同一评价的两个对象、GF19派生Q和现在代码默认值算多次独立验证。

## 原计数定义的受限练习

[冻结输入](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/pb207-reference-audit-input.json)、[程序](../../system/scripts/day17_pb207_reference_audit.py)、[actualresult](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/pb207-reference-audit-result.json)核两个原text hash、逐字段/母态身份、N倍率与MRsign；初parser诊断曾把XREF continuation当parent，正式代码用columns6/7空白区分primaryL，未沿用错误parent或修改原text。

令b=.131、a=.0217。源comment关系给R=(100−b)/(1+a)=97.7478712，与打印97.75末位相容。若**只在声明设计中**让b与a独立、σb=.002、σa=.0003，则σR≈.0287682，Cov(R,a)≈−8.61046×10⁻6。total T=R(1+a)=100−b，保留派生Cov后σT=.002；若错误将R/a独立，σT≈.0415191。这两个σ不是对原实验uncertainty重新报告，只显示derived-reference重复计误差的问题；原actualΣ未知。

光子pair名义概率按选定级联而非独立singles相乘；1064 total-transition yield74.5(1+.128)=84.036/100，与ECfeed84.0(.5)是同链相容性而非独立branch验证。ICC570/1064的experimental来源和Adopted理论列分开；没有用total vs photon混淆改GRIFFINQ。

## Competing Interpretations and Limitations

- MR评价central+.02(.01)、旧code+.03以及另primary+.12(+.08−.06)有不同来源/角色/误差预算；没有primary全文与phasebridge时不强配成同一native输入，也不选某个值重标Q。
- evaluation的空MR与采用E2标签属于不同层，不能因空栏补“测得零”；统计CI、物理模型pure限制与evaluation adopted值分开。
- 570/1064的coincidence roles、selection、finiteacceptance和nominalP必须与reference measurement匹配；source整体有少量β+不直接证明某一gatedanalysis受污染。
- N207-13给必要反证：β+到上1633level的预算为负，EC feeder与其0.806s isomer和后续130.5ps下level须分开。0.806s是相对feed之前的等待，不是已发1064与后发570之间的γγ间隔；不能仅凭这个长寿命否定prompt γγ gate，也不能把全sourceβ+率直接作为selected M4/E2背景。
- 没有取得1976primarybody、actualpolarimetryevents/峰fitcov或detectorQ/calibration联合Σ。当前仅官方记录审计/L2算术与L3 reference-readiness，不生成新P/δ或实验CI。

## Analytical Reconstruction and Self-Audit

| 项目 | 实际证据与判断 | 状态 |
| --- | --- | --- |
| source identity | 两selecteddatasets/header/fields/hash与evaluation metadata | self-audited |
| MR/ICC/normalization | 原列/continuationcomments及N/E格式视觉核 | self-audited |
| derivedCov exercise | 源公式与独立primitive假设明确，未替原Σ | conditional |
| originalphase/producer/response | NSR/DOI只identity，全文401、actualinput未得 | remains-open |

## Knowledge Impact and Learning Decision

`supports`reference母态/终态/概率字段与same-source依赖；`revises`把codecomment+.03当官方central、把RI/ICC独立或近能量join的习惯；`limits`known-P/source无β简写和near-pure强度对实际P精度的保证。source/comment/model推断分开；新增claims全needs_review，无human-review。

## Human Review Triage

P1：若以后用207Pb作为真实P/Q/δ裁决，先核原primaryphase/gates/response/Σ与reference角色，不把当前缺口自动变成用户待办。

## Extracted Pages

- [[triumf-griffin-compton-source-calibration]]、[[compton-polarimetry]]、[[linear-polarization-asymmetry]]；[[garnsworthy-2019-griffin-facility]]/[[grsisort-2026-compton-polarimetry-code]]保持跨source/版本回链。

本日新的条件参考核保存于[[pb207-gated-polarization-reference]]，实际sourcehash/母态来自N207-2/3；N207-14/15是本任务推导，不变成官方评价直接报告。
