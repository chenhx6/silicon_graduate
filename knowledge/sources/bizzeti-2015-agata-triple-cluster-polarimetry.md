---
type: source
title: "AGATA triple-cluster校准：角/符号合同、有限几何退化与Cs参考边界"
aliases: [Bizzeti2015 AGATA analyzing power, Pd Coulomb excitation polarization calibration]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: detector-method-experiment-article
reading_depth: deep-read
title_original: "Analyzing power of AGATA triple clusters for gamma-ray linear polarization"
authors: [P. G. Bizzeti, P. Sona, C. Michelagnoli, B. Melon, D. Bazzacco, E. Farnea, A. M. Bizzeti-Sona, G. de Angelis, A. Gadea, A. Gottardo, S. Lunardi, R. Menegazzo, D. Mengoni, A. Nannini, D. R. Napoli, A. Perego, F. Recchia, E. Sahin, J. J. Valiente-Dobon, C. A. Ur]
journal: European Physical Journal A
year: 2015
volume: 51
pages: "49"
doi: "10.1140/epja/i2015-15049-4"
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "publisherPDF DOI10.1140/epja/i2015-15049-4, published28-Apr-2015"
source_url: "https://link.springer.com/content/pdf/10.1140/epja/i2015-15049-4.pdf"
raw_file: "raw/papers/gpt/day16-20261018/bizzeti2015-agata-polarimetry-46a0bc767d94.pdf"
raw_sha256: "46a0bc767d944c16cc728411ebbb819705fed8393a7e172e30bffe828efec53c"
raw_storage_status: verified-raw-archive
raw_archive_verified_at: 2026-10-23
nuclei: [104Pd, 108Pd, 137Cs]
reactions: ["104Pd(12C,12C')104Pd", "108Pd(12C,12C')108Pd"]
experiments: [LNL-AGATA-two-triple-clusters]
models: [GOSIA, Geant4, segment-packing, position-smearing]
observables: [azimuthal-asymmetry, analyzing-power, calculated-reference-polarization, hit-position, Compton-angle]
methods: [Coulomb-excitation, response-normalization, gamma-tracking, source-convention-audit]
tags: [finite-geometry, calibration, shared-reference, covariance, literal-formula-boundary]
---

# 先核同一角度零点和参考权重，再比较分析能力

## Bibliographic Record

P.G. Bizzeti等，*European Physical Journal A* **51**,49(2015)，DOI[10.1140/epja/i2015-15049-4](https://doi.org/10.1140/epja/i2015-15049-4)。Crossref核题名/作者/article49；[出版商实际PDF](https://link.springer.com/content/pdf/10.1140/epja/i2015-15049-4.pdf)HTTP200取得，11页，SHA256见frontmatter。当前文件`tmp/day16-bizzeti2015/publisher.pdf`，未改raw/Bib，raw槽未归档。

这是[[morse-2022-gretina-polarization-sensitivity]]的Ref15、[[go-2024-demonstration-nuclear-gamma-ray-polarimetry-cdte]] Ref28。它测Pd Coulomb-excitationγ而非60Co，不能把前一候选source的未知source/gate记成本文实验。

## Scope and Reading Depth

本session完整读11页Sections1–7、AppendicesA–D和References，视觉核10图、5表、正文及appendix关键公式。以下分开原装置/实验As、GOSIA计算P、MC响应、本文literal公式审计与Codex条件推断。所见符号/单位/平均误差非闭合不等于已证明作者实际producer错误，未改原文或原实验结论。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| B15-1 | LNL以32MeV12C、约17pnA激发104Pd555.8/108Pd433.9keV的首2+→0+；2mg/cm²靶、富集91%/98%、靶面相对beam45°。独立Cs661.6作response reference，两triple共6晶体距靶约25cm。 | acquisition-and-reference-identity | direct | pp1–2Sec2/Table1/Fig1–2 | true |
| B15-2 | Table2中心P和Tables3/4按event平均的P是GOSIA/target-energy计算；原As是CE/Cs比值的φ调制。calculatedP与measuredAs/PderivedA不是三次独立P观测，中心P不能直接替eventweightedP。 | observable-layer-and-weighting | direct | Tables2–4；Sec3/5；AppendixA | true |
| B15-3 | GOSIA用50个θ点×10个beamenergy做积分，非500次独立实验；靶中能损约5.4MeV，referenceP对reorientation改变约8%、higher2+耦合约2%。这是模型敏感度而非给定σP，完整五ME/producer/Cov未提供。 | reference-model-readiness | direct-author-model | AppendixA EqA1/MEparagraph | true |
| B15-4 | 最终要求同cluster、fullenergy窗约10keV、两种cosθ均在±.35、两者差<.1、r12>15mm；PSA坐标另加±1mm均匀voxel抖动。约18% accepted跨同cluster不同晶体，2–3%是相对impinginggamma的acceptedfraction。 | response-selection-identity | direct | Sec4.1cutsa–e/Figs3–6 | true |
| B15-5 | energyorder同时physical仅是较弱条件；两次序又满足几何需(1−cosθ1)(1−cosθ2)=1/q²、θ1+θ2=π+α，给sinθcr=1/q−sin(α/2)。555.8在α3.4°的backwardcos≈−.48268，匹配文中约−.483；433.9在所报α≤16°无该解。 | finite-geometry-degeneracy | source-and-symbolic-arithmetic | Sec4.2Eq4–6；Fig7；AppendixC | true |
| B15-6 | Sec4.2在α0举例时将104/108Pd与555.8/433.9的标签配对写反；正确实验身份由Sec2/Fig3/Tables2–4一致给104555.8/108433.9。只隔离该段label问题，不换数据。 | isolated-energy-label-boundary | direct-visual-crosswalk | PDF5Eq5后paragraph；Sec2/Fig3/Tables3–4 | true |
| B15-7 | 同一φ零点下Eq9 N=a0+a2cos2φ与Eq10(N90−N0)/(N90+N0)严格给−a2/a0，而正文/表以+a2/a0操作。Sec3的P1方向与Eq7一句normal方向亦不同；不能直接互换namedAs、fitcoefficient、E-fieldφ与beamplaneφ。 | literal-sign-contract-boundary | exact-algebra-and-source-visual | Sec3Eq1–2；Sec4.3Eq7–10/后文；AppendixB | true |
| B15-8 | 条件probe取pure2→0/m0、a2=5/7/a4=−12/7时，literalEq1/2的cos2ψ项给P=−1，Jones/独立helicity与classical meridional electricquadrupole给+1（非零强度处）。ψ旋转π/2可精确映射两式；未取得原axis/producer桥前不能据此修改PdP或认定整篇实验错误。 | conditional-pure-limit-and-axis-audit | symbolic-and-two-independent-physics-controls | 本页pureprobe公式；B15Eq1–2；J02Eq9 | true |
| B15-9 | AppendixB同时给cosφ=n1·n12及sinφ=绝对值[(n1×n12)·r12]/r12；literal后式在一般几何多出cosθ，不能与前式构成sin²+cos²=1。用cosφ算cos2仍可能不受该印刷式影响；实际代码未得，不重写其φ数据。 | literal-geometry-failure-control | symbolic-orthogonal-vector-control | AppendixB末两式 | true |
| B15-10 | Fig5图轴/每长度label写µm，但同段recipe明确r12>15mm、PSAvoxel2mm，二者不能同时当同单位。smearingb=7.35√keV·mm是用δcos分布tuning的模型值，不能认证实测PSA分辨率或无单位迁移。 | units-and-model-boundary | direct-visual | Fig5/Seccut e；Sec4.5FWHMparagraph | true |
| B15-11 | Cs与CE能量不同，AppendixD用Compton角截面与secondaryγ衰减长度加权Cs；作者仍估残余As不确定约.013。整counter比值不等于更细regionwise加权；φ→φ+π对称化消oddharmonics而不能一般消cos2系统项。 | reference-energy-and-spatial-boundary | direct-and-Fourier-algebra | Sec4.3/5/7；AppendixD | true |
| B15-12 | 用Tables3/4的quotedA/σ作独立加权，mean/χ²df5重放.484054/1.445及.451122/.959；104σ=.023895闭合报.024，108σ=.030957未闭合报.034。未给完整Cov/权重/模型P误差，保留科学非闭合，不改源值。 | conditional-table-replay-and-nonclosure | actual-printed-input-calculation | Tables3–4；本页加权公式 | true |
| B15-13 | .013为作者由四个δcos子区spread后验估计、称fixedstatisticalcomponent并与Poisson项quadrature合成；相同数值不自动给跨counter Cov。不能以mean/χ²重现证明全误差预算重放。 | reported-error-procedure-boundary | direct | Sec5Tables3–4前后 | true |
| B15-14 | Table5是同MC的segmentcenter/no-tracking处理，6行3decimalbins的unweightedcos2fit重放相应A≈.09–.125；averagebins得.100712而表报.102，原fitweights/Cov未给。36°grouping sinc=.935489已在作者定义中计入，不作无说明的二次修正。 | same-model-processing-and-binning | source-and-conditional-bin-replay | Sec6/Table5；本页sinc公式 | true |
| B15-15 | 本文F=A²ε中的ε为accepted/impinginggamma，脚注明确常见定义另乘ω=Ω/4π；与Go绝对ε/F不能裸比。Table5与tracking的A比.102/.484≈.211只对这些处理对象成立，不是独立实验或等efficiency的信息比。 | FOM-denominator-and-independence | direct-and-central-arithmetic | PDF8Sec5footnote3；Sec6/Table5 | true |
| B15-16 | 追加核Ref16的Suffert原件：其electric angle从beam–γ plane normal量起，而本文Sec3文字从plane量起；同物理辐射P_SU=−P_plane。该原件桥可解释literalEq1/2与normal轴相容，不能认证本文actualproducer或将operational表符号静默改成另一合同。 | upstream-axis-crosswalk | two-original-sources-and-algebra | B15Sec3Eq1–2；SEH59-4/5 | true |

## Reference与response分层

GOSIA生成ρ20/ρ00、ρ40/ρ00，沿靶厚/beamenergy和unobservedprojectileθ积分，再对每个gamma hit的θ1计算P；Tables3/4列的P是event平均，Table2是countercenter值。作者估计recoil出靶小于2%、deorientation因子> .99后近似beam轴对称；该估计依模型/几何，不是已测全ρ。

实际As来自`R(φ)=NCE(φ)/NCs(φ)`。Cs是另一采集、能量661.6与两CEγ不同，因此共享energyreweight/geometry并不等于同对象unpolarizedresponse。AppendixD权重为secondaryγ的`μ exp(−μr12)`比乘Compton截面比；首hit深度的能量变化被作者估为对φ较小。当前没有rawhit/weights/完整ME/原Geant4与tracking版本，未重放这些response。

作者指出更严谨的处理需将counter分region分别比值，再按CE事件份额加权。全counter比值、简单φ对称化和T21的空间ν方案各有合同；cos2残差不会仅因消掉first harmonic就获独立认证。

## Literal符号、坐标与pure-limit审计

原Eq9给`N(0)=a0+a2`、`N(π/2)=a0−a2`。若Eq10的perp/parallel就是同一φ的90/0，endpoint asymmetry为`−a2/a0`。原操作和table把`As=a2/a0`；这两个named量必须分开。若把As与P同时反号，`A=As/P`保持原正比值，不能只翻其中一个就搬用表值。

对另声明的pureE2/m0 probe，令x=cosθ1、`I=15x²(1−x²)/2`。将同一a2/a4放入B15 literalEq1/2得cos2ψ系数`−I`，而[[jones-2002-calibration-compton-polarimeters]] Eq9/本run helicity kernel及classical m0 electricquadrupole给`+I`。独立classical计算用tracelessQ和`Etrans=Qn−n(n·Qn)`，场在meridionalplane，I∝sin²θcos²θ；节点仍标undefined。

代数上`W_B(ψ)=W_J(ψ+π/2)`，同时转换Stokes轴/分析角才可保持observable。这里不是复现实际Pd的ρ、不是新测P，也没有替作者认定哪一段axis命名/代码是正确版本。Eq7的ϕ按E-field plane定义，而排序中的ϕ按beam–γ plane定义；Sec3/4方向字词还需真正producer桥。这个literal边界足以阻止不经转换地复制式子。

AppendixB的sine问题也只隔离到字面公式。两plane normals均垂直incomingr1，故其叉积沿r1；向outgoingr12投影产生`sinφ cosθ`。配合原cos式，单位圆缺陷为`−sin²φ sin²θ`。若代码直接用`cos2φ=2(n1·n12)²−1`，此项并不必影响cos2；未得producer时不推断真实φ分布被破坏。

## 排序退化的条件与有限接受角

[[tsuzuki-2021-sicdte-template-polarimetry]]的能量规则先问两个排序是否各有physicalcos；B15进一步要求相同两hit与source方向满足完整几何：

`[1−cosθ1][1−cosθ2]=1/q²`，`θ1+θ2=π+α`。

写`θ1=θcr+α/2`、`θ2=π−θcr+α/2`可得`sinθcr=1/q−sin(α/2)`。在555.8/α3.4°，两临界角约64.539/118.861°、后者cos−.482683；α0下cos±.393334，Cs661.6则±.635173。433.9对所报α≤16°无该几何解，即使较弱的energyorder条件在某些角成立。

原选择`|cosθG|,|cosθE|<.35`、差<.1与r12>15mm有针对性，仍须response和hitresolution决定actual错误率。本文MC的packing与positiontuning是同一实验的校验处理，不额外计实验。

## 原表算术与未闭合部分

固定quotedA_i/σ_i且假设rows独立，`w_i=σ_i^-2`、`Abar=Σw_i A_i/Σw_i`、`σbar=1/sqrtΣw_i`。结果：

| 对象 | 简单加权mean | σbar独立假设 | reducedχ²/df5 | 作者mean/σ |
| --- | --- | --- | --- | --- |
| 104Pd555.8 | .484054 | .023895 | 1.44503 | .484(.024) |
| 108Pd433.9 | .451122 | .030957 | .95853 | .451(.034) |

最初代码将两组σ都应在.001内闭合当作guard，108Pd触发exit1；已留初源码/失败回执。随后只把这项无根据closure要求改为显式nonclosure输出，原numbers、Cov缺口与physics/hash guards不变。实际最终程序exit0不代表原误差预算全复现。

按printedAs/printed event-P重新相除会有最后几位差，不能用中心P替代。原Pmodel/共同Cs/reference/四cutspread的Cov未恢复；.013也不能仅因名字statistical就被当成六个完全独立或完全共享项。

Table5每counter的五个rounded MC bin给unweightedA与表值3dp相容；averagebinrow在该同一无权设计得.100712，对比原.102，原权重/未舍入数据未知。`sinc(π/5)=.935489`是36°cos2bin平均衰减；需先定义比较的是bin-integrated还是unbinned振幅，不能再无说明乘/除一次。它与trackingA约.484使用不同处理/选择，未提供共同efficiency下的信息比。

## 单位、F与数据边界

Fig5标r12单位µm，同正文15mm cut/2mm voxel不同；不要从图轴刻度回填hitgeometry。literal`FWHM=b/√E`配印刷`b=7.35√keV·mm`在E=100keV给.735mm（σ≈.312mm）；这是单位代入和模型tuning的有条件值，未认证actualproducer单位或真实PSAresolution，不用它自由调参追别的paperQ。

本source的ε相对impinginggamma，F不含source到counter的ω。只有相同P/response、简单isotropicflux时，转换到每emittedgamma的absolute形式才另乘ω；真实角分布还要接受角积分。它不能和Go的absolute ε或Morse另归一的Q/F裸比数值排名。

## Summary

原件提供真实Pd/Cs校准、GOSIA reference与trackingresponse链，并揭示复制formula时必须保存的sign、frame、单位与统计对象。报告A的幅度支持detector能力；本run保留literal/误差非闭合，不新增实验P/δ或producer认证。

## Competing Interpretations and Limitations

- 原paper中P是model、As是experiment、A是两者比值；同MC多处理、GOSIA500grid和多个figure不增加独立数据。
- literalEq9/10、Eq1/2 probe、AppendixB sine与Fig5单位问题只对应已读版本。未得exactproducer/authorclarification，不由此否定整篇采集或替换calibration数值。
- 原GOSIA五ME、beam-energy/stopping选择、Cs eventweights、未舍入bin counts与联合Cov未完整给出。当前只原表/解析控制，experimentalL4fit仍notready。
- 前候选Alikhani2012原件未取得；这里只引用B15所述比较，不把机构摘要/二手Q当已读其primaryformula。

## Knowledge Impact and Learning Decision

`supports`真实reference/finitegeometry与tracking校验；`limits`formula符号互换、Pcenter/Peffective替代、错误率/误差预算和F裸比较；`revises`本run“所有reportedmeanerrors都能由独立权重回放”的先验。所有新claims needs_review，不作human-reviewed或课程credit扩张。

## Extracted Pages

- [[compton-polarimetry]]、[[modulation-curve]]：reference/angle/normalization/统计对象。
- [[linear-polarization-asymmetry]]：endpoint sign与fitcoefficient须分开。
- [[tsuzuki-2021-sicdte-template-polarimetry]]：energy-only规则与fullgeometry/response的续接。
- [[jones-2002-calibration-compton-polarimeters]]：purelimit/axis的条件crosswalk。

## Reproducibility

[source原表/符号/有限几何脚本](../../system/scripts/day16_bizzeti2015_reference_audit.py)最终实际exit0；[结果](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/bizzeti2015-reference-audit-result.json)、初exit1源码/失败与冻结contract均保留。只使用实际printedinputs及明确pure/axis probes，无fakeeventhist、未重跑实际GOSIA/实验拟合。PDF/原render与第三方软件只tmp不stage。


### 上游原件补核：Suffert的normal轴

[[suffert-1959-proton-capture-polarization]] SEH59-4–12重新原读，明确其Eq2的electric-anglezero在beam–γ plane的normal，Eq3的P为normal减plane；这与本source文字Stokesaxis相差π/2。同一scatter-plane零点，SU59给N∝1+pP_SUcos2χ，plane-axis则N∝1−pP_planecos2χ，P_SU=−P_plane使observable一致。B15Eq1的pureprobe可与normal-axis合同相容；本追加缩小符号歧义，仍未找到actualproducer或解释所有literal差异，原表/As/P不改。
