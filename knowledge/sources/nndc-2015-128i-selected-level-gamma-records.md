---
type: source
title: "NNDC 2015 128I选定记录：低位锚点、102-keV位置与来源边界"
aliases: [NNDC 128I 2015 selected ENSDF, Elekes Timar A128 lowlevel records]
created: 2026-10-16
updated: 2026-10-16
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data-tables
reading_depth: read
title_original: "128I ADOPTED LEVELS, GAMMAS / 124SN(7LI,3NG) / 127I(N,G) E=THERMAL:SECONDARY"
authors: [Zoltan Elekes, Janos Timar]
journal: Nuclear Data Sheets
year: 2015
volume: 129
pages: "191-436"
doi: 10.1016/j.nds.2015.09.002
canonical_source: "NNDC-ENSDF:128I:201510:128053001,128053024,128053003"
citation_key: ""
raw_file: "raw/papers/gpt/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam/nndc-128i-adopted-2015.ens"
raw_sha256: "27afae52bb7be1c4aa50e332e60abfe30a3d615d7e1586cd1b8b98bc65e5527e"
raw_storage_status: reserved-unpopulated-public-objects-verified-in-wiki-tmp
data_version: "201510; CUT28-Feb-2015; objects128053001/128053024/128053003; retrieved2026-10-16"
nuclei: [128I]
reactions: ["124Sn(7Li,3n)128I", "127I(n,gamma)128I"]
methods: [level-scheme-reconstruction, internal-conversion-analysis, evaluated-data-crosswalk]
observables: [level-energy, gamma-energy, spin-parity, half-life, relative-intensity, conversion-coefficient]
tags: [ensdf, source-version, transition-identity, iodine, data-lineage]
---

# 128I选定评价对象与primary的拓扑边界

## Bibliographic Record

Z. Elekes、J. Timar，*Nuclear Data Sheets* **129**,191–436(2015)，DOI[10.1016/j.nds.2015.09.002](https://doi.org/10.1016/j.nds.2015.09.002)。Crossref核题名/作者/年/卷页；本页读的是NNDC选定128I数据对象，**没有读整篇质量链评价论文**。没有唯一Bib匹配，citationkey留空。

## Scope and Reading Depth

- 下载并核3个201510对象：adopted2327行、7Li reaction230行、thermal-secondary1265行。
- 实际读：三个header/来源约定；reaction230行完整主线；adopted/capture的137/167/183/226/270/285及必要1562邻域。reaction独立生成PDF共6页，本轮读页1–3表和脚注、视觉核页2，不声称重审所有levelscheme图或全部2327/1265行。
- 未读：2009Zh51正文、2012Di14正文、capture原论文；无原events、响应/完整Cov或代码，不以编译对象代替primary。
- `raw_file`为未填保留槽，原raw未改。实际对象在Wiki内tmp，以下URL/表单/哈希和atomicclaim定位为持久证据；不公开PDF/raw对象到Git。

## Public Query and Provenance

POST [DatasetFetchServlet](https://www.nndc.bnl.gov/ensdf/DatasetFetchServlet)，`nuc=128I,nsrch=Search,searchType=quick,datasource=ensdf`；GET曾返回“Not a valid input method”，未当数据。再POST [EnsdfDispatcherServlet](https://www.nndc.bnl.gov/ensdf/EnsdfDispatcherServlet)，`dbclass=ensdf,page-source=singular,chooseit=ENSDF text format`，`datasetcheck`逐个为`128053001,128I`、`128053024,128I`、`128053003,128I`。取HTML pre文本，保留原列/空行，未更改物理字段。

| 对象 | text SHA256 | HTML response SHA256 |
| --- | --- | --- |
| adopted128053001 | 27afae52bb7be1c4aa50e332e60abfe30a3d615d7e1586cd1b8b98bc65e5527e | c36cc45daecc7b34c0866ac90d488ea1640753a713eca5c0d11c798c7f22b8a9 |
| reaction128053024 | 126efa18a375524a26f26d62a32be280c663b3db3f470a9b9e5db94690b28114 | 2fc295d1340b476c102d28cbe0b58aab33d1fefc1348bad3ce607a9a7e6a80d4 |
| capture128053003 | 5a5315c8888c159014784c0beb9e7af8ac2b20c117a388c8b2ddd48c0d8a5239 | 36893377d450e055d49da45f2913ff8b92cbef7e000ac45c825c6cb7111e1a93 |

同reaction表单选`PDF Version`得到72441bytes/6页，SHA256`3d38146944df96e0762fe0e85ba9e4c1bb1511396a35e7be41cc564990bf6370`。PDF页2明确列Ei/Ef，复核fixed-column parent绑定；text/PDF是同数据的两种表示，不是独立实验。

## Summary

评价保留低位spin候选与精确capture锚点，且给出与thesis/CPL不同的102/15.6位置和字段绑定。它能够暴露来源/拓扑问题，不能因“adopted”或版本较新就裁决哪一图物理正确。逐对象的normalization、CC/ECC/EKC及评价者加的误差必须随数值保留。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| N128-1 | 三对象header为201510、cut28-Feb-2015、Elekes/Timar NDS129191；本页仅选定对象，不是整质量链全文或新实验。 | object-identity-and-scope | direct | objects128053001/128053024/128053003 H records | true |
| N128-2 | Reaction说明除注明外data来自2010Wa27/2012Di14，2012Di14为Tsukuba同作者、几乎相同结果。2009Zh51在评价summary中另列CIAE14Ge/25,28,32MeV/preliminary；这只是一项编译来源，不等本任务已读旧paper或验证独立rawrun。 | compiled-lineage-and-primary-boundary | direct-and-derived | reaction128053024 header comments2010Wa27/2009Zh51/2012Di14 | true |
| N128-3 | adopted低位为167.368(4)(6)−、175(15)ns；183.0(8)(7−)；226.102(5)及269.712(7)均(5,6,7)−；285.24(18)(8−)。不把thesis建议6/7静默升级为evaluation唯一标签。 | evaluated-level-and-assignment-crosswalk | direct | adopted L167.368/L183.0/L226.102/L269.712/L285.24 | true |
| N128-4 | reaction把G102.2放L269.57下、RI≤632、ECC=.60(7)，而L285.19下列15.6与117.8；PDF页2直接列285.19→269.57的15.6和269.57→167.367的102.2。Adopted相应L285.24也有15.6而没有该parent的102。与Ding/CPL强102为285→183不同，不能按sameenergy复制ICC或认作rounding；原因待primary核验。 | literal-topology-and-field-binding-conflict | direct-and-derived | reaction L269.57/G102.2 and L285.19/G15.6; reaction PDF2 gamma table; adopted L285.24 | true |
| N128-5 | ReactionE/RI来自2010作者2010-08-24邮件给的总体range；evaluator按Iγ>50、20–50、<20分别赋.1keV/5%、.3keV/15%、.5keV/30%误差。它不是原逐linefitCov的恢复，不能倒填thesis所有σ。 | evaluator-error-provenance | direct-and-derived | reaction header cG E,RI comments; reaction PDF3 footnote dagger | true |
| N128-6 | adopted101.3的RI100与reaction146、capture以I(133.61)=46.9/N=1.06(13)归一的RI尺度不同。reaction102.2是≤632而Ding有563和≥79两行，不能相加/改limit方向或据此计算无条件fraction/branch。 | intensity-normalization-and-limit-contract | direct-and-derived | adopted L1562.27/G101.3; reaction L1562.21/G101.3 and L269.57/G102.2; capture RI comment and N record | true |
| N128-7 | Reaction102的CC.703为理论totalICC，XG ECC=.60(7)为实验total估计；capture102.344在L269.711下，CC.700为理论total而EKC=.55(11)是实验K-shell。两个实验alpha对象不同，不能混同K/total或将相同ECC跨primaryparent自动迁移。 | conversion-field-identity | direct-and-derived | reaction L269.57/G102.2 XG/S G; capture L269.711/G102.344 XG; reaction PDF3 double-dagger | true |
| N128-8 | adopted167.368的175(15)ns与29.512(5)(E2)支属于该parent；其CC175.0在理论字段。下方137.851(3)4−的T1/2=.845(20)μs是另一parent。不得借这些寿命给225/285/1562算B；本轮不重算absoluteB。 | timing-parent-and-ICC-boundary | direct-and-derived | adopted L137.851 and L167.368/G29.512; capture corresponding lowlevelblocks | true |
| N128-9 | getrefs将2012Di14识别为PRC86,034302 DOI10.1103/PhysRevC.86.034302；header“几乎同2012Wa27”中的该key在refs实际是Uoctupole论文，保留不静默改。2009header32MeV与reference-summary42MeV也并列，不借二级metadata裁决旧原件。 | reference-key-and-metadata-boundary | direct-and-derived | reaction header adoption comment; getrefs recid128053024 entries2012DI14/2012WA27/2009ZH51 | true |
| N128-10 | 2012Di14的exactDOI/title/authors/PRC86(3),034302和2012-09-04身份已核；本轮API401、publisherPDF403、OpenAlex/S2无可用副本、选定arXiv0/Scholar失败，body未取得。310本地PDF的metadata检查未匹配该fullDOI，PRC105.034302误候选按卷/DOI排除；不建未读source、不以metadata裁决N128-4。 | exact-primary-access-and-fingerprint-boundary | direct-and-derived | getrefs2012DI14; exactCrossref10.1103/PhysRevC.86.034302; boundedaccess audit2026-10-16 | true |
| N128-11 | 在本任务声明的selectedgraphs、忽略15.6观察且将两个近能102投影为同group时，756.5/764.7/117.8三门的101/102支持集在两拓扑都为{102}/{101,102}/{101}。这只限制coarse support的区分力，不证明actualcounts/angular/timinglikelihood相同，也不证明原detector看不见15.6。 | our-source-conditioned-observability-design | derived | N128-4 records; CPL printed082701-3 Fig4; DingPDF82 Fig6.5 | true |
| N128-12 | 用printed节点差15.6keV作为nominal独立state-tag间隔，在另声明knowncenters/commonGaussianwidth/midpoint/balancedprior设计下，每类wrongtag≤5%要求σ≤4.74206keV、FWHM≤11.16671keV。非现有γ探测器或Ex-tag性能/实验CI；实际tag、tails/calbias/响应/Cov缺失。 | our-conditional-measurement-specification | derived | N128-4 lowlevelrecords; DingPDF78 endpoints; boundeddesigninput2026-10-16 | true |
| N128-13 | ReactionADO注释与CPL原文都明确R>1还可对应ΔI0D或某些mixedΔI1，CPL以764.7举例；这是generalambiguity，不表明58.5/255.6实际有该混合或J7被数据支持。Capture226.101→167的58.74列M1，M列来自relativeIγ/Ice，允许set需带同线identity/anchor条件；MR空白不等测得δ=0。 | source-hypothesis-scope-and-role | direct-and-derived | reaction cG RADO comments; capture cG M header and L226.101/G58.74; CPL printed082701-2 | true |
| N128-14 | 本任务fixedupper7/anchor6时，旧restrictedH0/H2+两L1+reactiontrend得{6}；改用M1component-present family，两L1与nondecreasingtrend只给{6,7}。再独立给255stretchedΔI1才回{6}；selectionrule集合不是actualRADOlikelihood或新spinassignment，也非穷尽所有multipole/lineidentity。 | our-hypothesis-domain-audit | derived | N128-13 sourcewarning; DingPDF78–79 localthreeedges | true |
| N128-15 | 若同线匹配/anchor6成立，M1→6的exacttriangle给{5,6,7}，与历史allowedset同形；同一证据所导的set再相交不算新增独立测量。Reactionspintrend是额外布居prior，parentEx-tag只识别状态位置不自动测spin，需独立spin/含实际响应的sequence检验。 | our-evidence-role-and-identifiability-boundary | derived | capture L226.101/G58.74; adopted L167.368; DingPDF79 | true |
| N128-16 | 本任务声明pureL1、同parentJ7 density、matchedselection/fADO1、point37/90后，从CG振幅权重和transversephoton角函数导出a2(7→7)=−13/8 a2(7→6)，逐Mi精确成立；Jx6时两branch相同。它是radiation系数关系，不是把未观测U代入gate或源实测δ0。 | our-common-parent-radiation-baseline | derived | DingPDF78 local255/314 rows and PDF57 geometry; YA67 angular definitions | true |
| N128-17 | 该baseline下H_Jx7要求(R314−1)(R255−1)≤0，源打印中心.91/.92不满足；H_Jx6还要求两R相等而中心差.01。Chosenpositiveparent=.1m0+.9uniform给R314=.971008/R255_H7=1.049063（H6两者.971008），都在各quoted半宽内；box无jointcoverage，也非full58/feedingfit，不给实际排除。 | our-central-control-and-marginal-box-boundary | derived | DingPDF78 RADO.91(15)/.92(20); commonparentanalysisinput2026-10-16 | true |
| N128-18 | 换成两个不同的显式正postselecteddensity，可在samelevel/H_Jx7下让两R−1同号，说明parentlevel相同不等commonconditionalpopulation。此为chosen失效控制，非实际gate效应；finitegeometry/fADO、E2混合/干涉和原Cov未给时不升级为实际spin判据。 | our-selection-response-failure-control | derived | reaction RADO gatedspectrum header; DingPDF54–55 ADO definition; declaredcommonparentinput | true |

## Theory/Analysis Exercise

[[level-scheme-reconstruction]]“128I评价对象：102-keV位置与字段不能随能量迁移”保存28-check固定列审计、primary/evaluation端点与误差/归一/ICC分层。其能量和比较只是说明102.2与15.6的交换不能由总和117.8识别中间节点；primary中的183→167差额不被补成已测15.6跃迁。

## Competing Interpretations and Limitations

已读[[wang-2010-128i-new-high-spin-level-scheme]] Fig3/4与DingFig6.2把强102.2放285→183，评价text/PDF则如N128-4。两者共享Tsukuba来源，不是独立复测。2012Di14正文、官方erratum/更新说明、原门谱/转换分析与正确component binding仍是最高信息companion；当前不认定数据库错、source图正确或相反，不给新spin/δ/模式。

## Knowledge Impact and Learning Decision

Decision: **revises** “评价已adopted就能替代逐row identity”的读法；**supports** 按object/source/parent/limit/field provenance保存；**limits** 从perlineerror恢复Cov、用更精确能量或更新版本独自裁决topology。全部claims true、review unreviewed，source自审不等人审。

## Agent self-audit triage

P0：对象身份/哈希/原列与独立PDF表示已核；N128-4/9冲突在source明确隔离，不用于推广实验事实。P1：primary2012Di14、2009Zh51及数据/版本差异原因未解，保持needs_review；不能把同一评价的text/PDF或adopted/reaction计为独立数据。P2：进一步核其normalization/branch与daughter mapping，需原scope清单。P3：raw保留槽未填、citationkey未配，不修改用户raw/Bib。

## Extracted Pages

- [[level-scheme-reconstruction]]、[[a130-thesis-evidence-matrix]]：低位/transitionidentity冲突与输入合同。
- [[ding-2012-phd-thesis-127-128i-high-spin]]、[[wang-2010-128i-new-high-spin-level-scheme]]：primary对照。
- [[tsukuba-127-128i-li7-28-32mev]]、[[128i]]：谱系与核素入口，未因database对象新造独立实验。

## 2012原文未得后的最小判别设计

本轮exactCrossref核2012Di14的题名/作者/PRC86/034302/2012-09-04；公开来源路线未取得body。不能把“曾尝试读取”写成全文已读。本地初次rg默认被Gitignore过滤，已用no-ignore重新枚举，再读310PDF文档metadata；丁兵另名PDF与thesis同hash/100页，PRC105.034302只是相同article-number的不同paper，未读其科学body。没有对原目录作“全球/本地全文不存在”断言，也不改raw/配置或绕验证。

[[level-scheme-reconstruction]]“128I未定位置：三张门谱的区分力与最小独立tag”将不能获取primary之后的工作限定为设计，不编正文或数据。14项check只证明在明确粗化/selectedpath条件下三门support可相同，并计算一个自选Gaussianstate-tag要求；不把它升为fullresponse同值、现有detector性能或对任何图的裁决。G15.6只有record/未给RI也不自动意味着本任务已验证其observed状态；primary183下方未列的decay保持未知，不补成已测线。

Decision: **limits** 用相同峰出现模式/混峰ICC单独定位parent；**supports** 将下一观测对准独立母态/末态或可解析的时间顺序。新10–12 true，旧1–9/review保持。原文与actualresponse/数据边界仍在，formal14/partial15不变。

## 58.5-keV的假设集范围与证据角色

本轮回核已读reactionADOcomments、capture58.74/M1与CPLgeneralwarning，不开新source或回填未读2012正文。[[level-scheme-reconstruction]]“128I自旋候选：假设集合、stretched条件与证据角色”保存13项条件集合审计。旧039限定H0/H2的结果在其原条件下仍成立；允许M1(+E2)的ΔI1族后，genericL1与非下降reactiontrend不单独唯一。没有由该必要规则反例提出J7的新实验指认。

Capture M1与历史allowedspinset若使用同一底层Ice/Iγ及anchor，后者不能再算第二份独立数据；reactiontrend则属于不同的物理prior。MR空白、同能量与表上label仍不恢复δ/response/Σ。新N128-13–15 true，旧1–12/review保持；sourceJ6建议/原data/raw和formal分数不改。

## 两个commonparentbranch的条件角约束

043只核necessaryspinsets，没有丢弃源RADO。当前23项CG/transversephoton核验在严格列明条件下对actual两个ratio建立更强baseline；[[level-scheme-reconstruction]]“128I共有母态：必要角关系、打印中心与选择响应”保存精确−13/8关系、中心控制、正populationboxwitness和不同postselection失效例。没有由kinematicJ7候选说它已拟合，也没有由conditionalcenter不满足说它被实验排除。

δ0/pureL1、point角组、相同parentdensity与fADO1均为chosenmodel；原每线gate/finiteacceptance、sharedCov和E2混合未得。58的另一parent没有放入两branchfit，sourceJ6/原数据/正式成绩保持，新16–18true，旧1–15/review不改。Decision: **supports** 使用共有parent的联合信息；**limits** 忽略真实角数据或拿特殊baseline直接裁决spin。
