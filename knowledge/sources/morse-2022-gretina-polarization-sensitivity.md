---
type: source
title: "Morse2022：GRETINA偏振标定、跟踪响应与GRETA外推"
aliases: [Morse 2022 GRETINA polarization sensitivity]
created: 2026-10-18
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: experimental-method-paper
reading_depth: deep-read
title_original: "The polarization sensitivity of GRETINA"
authors: [C. Morse, H. L. Crawford, A. O. Macchiavelli, A. Wiens, et al.]
journal: Nuclear Instruments and Methods in Physics Research A
year: 2022
volume: 1025
pages: 166155
doi: "10.1016/j.nima.2021.166155"
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "doi:10.1016/j.nima.2021.166155; actual read: UNC author preprint 2021-12-02"
source_url: "https://doi.org/10.17615/4vxa-4h20"
raw_file: "raw/papers/gpt/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention/morse-2022-gretina-calibration-author-preprint.pdf"
raw_sha256: "f76cf7073fb5c5240d638b332802730614f9f81d8aa2f971c6957acfddbfc241"
raw_storage_status: verified-raw-archive
raw_archive_verified_at: 2026-10-23
nuclei: [24Mg]
reactions: ["24Mg(p,p')24Mg"]
experiments: [atlas-gretina-mg24-pp-2450kev-six-quads]
models: [Geant4, UCGretina, Gaussian-position-smearing]
observables: [angular-distribution, linear-polarization, polarization-sensitivity, figure-of-merit]
methods: [gamma-tracking, Compton-polarimetry, source-normalization]
tags: [GRETINA, GRETA, response-calibration, normalization-convention, selection-identity]
---

# Morse2022：实测标定与模拟曲线分开

## Bibliographic Record

C. Morse等，*NIM A*1025,166155(2022)，DOI [10.1016/j.nima.2021.166155](https://doi.org/10.1016/j.nima.2021.166155)。Crossref核题名、作者与出版年；实际全文来自[UNC机构记录](https://cdr.lib.unc.edu/concern/articles/2f75rj951)，机构DOI [10.17615/4vxa-4h20](https://doi.org/10.17615/4vxa-4h20)，公开文件[1835119.pdf](https://cdr.lib.unc.edu/downloads/9s161h65x?locale=en)。机构注明版本Preprint，PDF首页日期2021-12-02。

实际文件13页，SHA-256见frontmatter，当前存repo tmp/day16-l26-preview；raw_file是未填归档槽，未修改raw/Bib。公开publisher TDM链接只返回1893-byte core metadata，没有VoR正文；不把本次author-preprint阅读冒称VoR逐字核验。它与机构/OSTI副本和L26转述不是新独立采集。

## Scope and Reading Depth

本session全文文字主线1–13页及references已读；全部Figs.1–12、Tables1–2和Eqs.(1)–(13)相关页视觉核查。包括几何/偏振定义、6-module实验、background/source除法、AD/ξ拟合、Q/F标定、Geant4统计张量输入、位置smearing失败及GRETA能量外推。

未取得events、实际response/Cov、原未舍入fit输入与本实验producer代码。文中说从nuclear statistical tensor到photon Stokes的推导/实现留待另文；本次没有据此宣称执行了那套代码。这里是Day16下恰好Day17的无学分知识预习，不授正式17学分。

## Summary

6-quad GRETINA以24Mg(p,p′)1368-keV纯E2作偏振标定，报告Q=.196(.002)与F=2.04(.06)×10^-3。Q依赖本文的A0=Q Pbar/2、tracking/角度选择及source归一。GRETA的500–2000-keV曲线是采用同一标定/tuning的模拟结果；把它转给另一阵列配置或energy-ordering分析须核响应身份。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| M22-1 | 实际读的是UNC公开13页author preprint；1025/166155/2022为已核出版元数据，未取得VoR正文。该版本/副本不增加独立实验。 | source-identity-and-version | direct | PDF1日期/题名；UNC记录Version；Crossref DOI | true |
| M22-2 | ATLAS以2.45-MeV质子打3.3-mg/cm2天然Mg，6quads/24晶体位于一半球、约40–140°；只有24Mg的1368.7-keV 2+可达，作者据此排除更高态feeding。分析使用tracking、20°clustering，polarimetry至少两interaction points。 | acquisition-and-selection | direct | PDF4 Sec.3；Fig.3；lines157–214 | true |
| M22-3 | 用60Co1332无偏振source归一1368的角谱/ξ谱，背景取峰两侧；作者忽略1332/1368间效率差。前后角及87°偏离保留，作者讨论source/beam偏移和decomposition异常，未由本run裁决原因。 | response-normalization-and-limit | direct/author-interpretation | PDF5 Fig.5及lines217–275；PDF6 Fig.6 | true |
| M22-4 | AD fit a2=.545(.005)、a4=−.351(.005)，报告P90=1.00(.02)；Fig.6的A0=.1024(.0009)有80–100°门。另报array-weighted Pbar=.824(.008)、Q=.196(.002)。没有逐项cut/fit ledger，不将Fig.6的A0与另一个Pbar直接相除来判Q错误。 | reported-fit-and-object-identity | direct | PDF6 Figs.6–7；lines276–320 | true |
| M22-5 | 本文定义Wc(ξ)=b(1−A0 cos2ξ)、A0=Q Pbar/2和F=Q²epsilon；epsilon指可提供至少两个interaction points的Compton event效率。Table1脚注另给Litherland的Q作factor2修正；同名Q不保证同归一。 | normalization-convention | direct | PDF3 Eqs.(7)–(9)；PDF7 Table1脚注 | true |
| M22-6 | 无Ft cut报Q=.196(.002)、F=2.04(.06)×10^-3；Ft≤.6给.210(.002)/2.00(.06)×10^-3，Ft≤.1给.314(.005)/5.1(.2)×10^-4，ψ60–80°给.267(.003)/8.0(.3)×10^-4。Ft为tracking分数，与polarimeter F不同。 | reported-cut-tradeoff | direct | PDF7 Table2及lines360–385 | true |
| M22-7 | 模拟P(M=0)=.52、P(M=+1)=P(M=−1)=.24、P(±2)=0来自同一AD拟合；Eq.(11)的ρk0=Bk/sqrt(2k+1)。作者报各40×10^7 events为原模拟数量，不是本run运行量；相同derived输入回代不新增独立核布居实验。 | model-input-and-dependency | direct/model-result | PDF8 Eq.(11)、Sec.4.2、lines428–442 | true |
| M22-8 | 完美position模拟A0约.196、Q=.392(.004)；以σ100≈7mm调至Q=.207(.002)时，apparent P90却降到约.85，与实验约1不闭合。作者明确7mm不是实测分辨率，认为简单smearing可能不能近似decomposition；energy-ordering分析改变该行为。 | model-failure-and-author-limit | direct/model-result | PDF8–10 Figs.8–11；Secs.4.2–4.3 | true |
| M22-9 | P0=.131(.006)、P1=3.25(.07)×10^-4/keV的Eq.(13)曲线拟合GRETA 30-quad模拟的500/1000/1500/2000-keV四点，采用同一position tuning/布居输入；它不是四项实测GRETINA能量标定，参数Cov未给。 | model-curve-and-transfer-domain | direct/model-result | PDF10 Sec.4.4/Fig.12；PDF11 Eqs.(12)–(13) | true |
| M22-10 | 对声明的ideal-response、轴对称2→0纯E2模型，印刷a2/a4中央值反演grouped p为(.5233,.4776,−.0009)，P90=1.003776；pabs2=0时两项literal marginal error boxes仍有p0∈[.5211,.5246]。这是physical-feasibility诊断，不是负布居测量或jointCI；不夹掉源P中央值。 | Codex-physical-domain-check | conditional-calculation | PDF2 Eq.(3)；PDF6 a2/a4；本run exact photon/Racah复算 | true |
| M22-11 | 从同一Table2的中央F/Q²重算，Ft≤.1的efficiency约为baseline的.0974而F为.25；ψ60–80°约.2113/.3922。更高Q不等于本pipeline更高总信息；缺Q–F Cov不新算epsilon误差。 | Codex-cut-design-audit | conditional-calculation | PDF7 Table2 | true |

## Theory and Analysis Exercise

冻结[原数据/选择/模型输入](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/morse2022-calibration-input.json)，再用[程序](../../system/scripts/day16_gretina_convention_audit.py)/[结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/gretina-convention-audit.json)复算。输入属于13页preprint的印刷summary；没有伪造event counts、Cov或实验δ。

对2→0 pure E2，grouped populations p0、pabs1=p+1+p−1、pabs2=p+2+p−2的基底(a2,a4)为(5/7,−12/7)、(5/14,8/7)、(−5/7,−2/7)。独立Racah/tensor计算与photon trace一致。源中央fit落在物理边界外很小的距离，但physical pabs2=0与字面两marginal误差盒相容；误差盒不是联合置信集。源打印MC输入(.52,.48,0)的intrinsic moments为(.542857,−.342857)，不将它与经detector/source/fit流程得到的(.540,−.354)当完全同一对象。原代码/未舍入输入/response缺失，未归因差异。

纯m0在θ90无光子，P90应标undefined；不能因为比值0/0就填P=0或P=1。等占据density给a2=a4=P=0，作为失败控制。这里的高P校准不是所有spin/multipole/feeding条件下的通用reference。

若把Fig.6 cut A0与array Pbar错误合用，会得Q=.24854；原Q与Pbar的同对象代数关系只隐含A0≈.080752，**后者不是原文另报的测量**。未匹配选择时不据这个差异判实验错误。

Table2同一归一下的名义tradeoff：

| cut | epsilon中央值F/Q² | epsilon相对None | F相对None |
| --- | --- | --- | --- |
| None | .053103 | 1 | 1 |
| Ft≤.6 | .045351 | .85403 | .98039 |
| Ft≤.1 | .005173 | .09741 | .25 |
| ψ60–80° | .011222 | .21132 | .39216 |

这些是同pipeline的中央值代数重放，不能用两项独立误差quadrature推回原完整epsilon误差。无background/系统项且固定known response的声明统计模型下，F比例才给对应精度比例；没有给出本实验新beamtime。

## Competing Interpretations and Limitations

- σ100≈7mm是同时依赖tracking和post-processing的调参，不是测量到的detector位置误差；Fig.11的AD/P与ξ不同时闭合是必要反证。
- 一次1368点调参、同输入的simulation与GRETA能量拟合，不构成独立实验多次确认。额外quads不改变Q的推断依赖作者近似的θ独立性与同响应处理，不保证转给47-crystal energy-ordering数据。
- quoted AD与ξ/Q来自共享事件/source归一，参数及跨observable Cov未给；不作新δ、calibration显著性或jointCI。
- 本文与L26均用半因子定义Q。若在相同P/response下改写A0=Qnew P，则必须同时Qnew=Q/2；固定Q删半因子会改变observable。这个代数转换不认证Q就是原KN analyzing power的直接平均。
- source curve500–2000-keV外和不同selection的应用需要response证据；原paper和模型均保留，不由本run手调Q强配L26结果。

## Knowledge Impact and Learning Decision

`supports`真实source/Compton calibration与cut tradeoff；`limits`把调参分辨率当实测、跨mode裸迁Q、同源回代当独立验证。保持needs_review；本页没有human review或新实验credit。

## Related Knowledge

- [[ucgretina-2021-polarized-emission-code]]：另行固定的公开代码内核与pureE2反证，不认证本篇exactproducer或全阵列response。

- [[longfellow-2026-gretina-energy-ordering-polarization]]：Eq.(19)所引calibration/模拟曲线的上游来源。
- [[lauritsen-2025-gamma-angular-formalism-tracking-arrays]]：另有γγ-polarized source/reference和自己的Q定义/角门。
- [[compton-polarimetry]]、[[linear-polarization-asymmetry]]：P/A/Q、epsilon和选择身份。
- [[gretina-25na1041-polarization-response-contract]]：当前1041分支判别的匹配条件。


## Extracted Pages

- [[gretina-25na1041-polarization-response-contract]]：calibration谱系与branch/selection合同。
- [[compton-polarimetry]]、[[linear-polarization-asymmetry]]：半因子Q、physical-domain及真实cut tradeoff。
- [[dco-pdco-ambiguity-worksheet]]：matched companion reference角色，不当新R_DCO测量。
