---
type: source
title: "245Cm/249Cf偏振参考：当前评价、历史MR与异常转换系数"
title_original: "245Cm Adopted Levels, Gammas and 249Cf Alpha Decay; ENSDF202305"
aliases: [NNDC Cm245 Cf249 polarization reference, SeGA333388 reference]
created: 2026-10-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: evaluated-selected-data-records
reading_depth: read
authors: [C. D. Nesaraja]
year: 2023
journal: Nuclear Data Sheets
volume: 189
pages: "1"
data_version: "ENSDF202305; cutoff14-Feb-2023"
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "NNDC245096001/245096004; Nesaraja NDS189,1(2023)"
source_url: "https://www.nndc.bnl.gov/ensdf/"
raw_file: "raw/data/gpt/day17-20261019/cm245-adopted-c7f95f70b908.ens"
raw_sha256: "c7f95f70b9089969c23212c06c51c9e1b85f2713a749bf92e92c12914904d0da"
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [245Cm, 249Cf]
reactions: []
experiments: [SeGA-alpha-gamma-calibration]
models: [BrIcc]
observables: [gamma-energy, relative-photon-intensity, internal-conversion-coefficient, multipole-mixing-ratio]
methods: [ENSDF-fixed-column, reference-identity, calibration-readiness]
tags: [polarimetry, calibration-reference, actinide, anomalous-conversion, source-independence]
---

# SeGA333/388参考的评价证据与实际校准边界

## Bibliographic Record

当前官方DatasetFetchServlet对245CM的实际列表返回五对象，页面均标2023-05；按实际form取Adopted `245096001,245CM`和`249CF A DECAY` `245096004,245CM`。两者header为C.D.Nesaraja、NDS189,1(2023)、CUT14-Feb-2023。此处页1仅引用header起页，不补未核完整页范围/DOI。

| 对象 | actualtext缓存与范围 | SHA256 |
|---|---|---|
| Adopted | `tmp/day17-cm245-reference/adopted.ens`，372行全文 | `c7f95f70b9089969c23212c06c51c9e1b85f2713a749bf92e92c12914904d0da` |
| Cf249alpha | `tmp/day17-cm245-reference/cf249alpha.ens`，425行全文 | `85d9aa9b4f4dcc112b5ed268d0749952431b3f8679f373506a1b6908402faa4f` |

原始HTTP wrapper/hash、精确payload和selectedkeys在本run `cm245-official-discovery.json` / `cm245-selected-downloads.json`。没有把HTTP200首页当ENSDF；identityline/固定栏/文本hash均核。raw归档槽未填，原raw/Bib不改；官方body目前在Wiki内暂存，canonical本页保存可复用原子证据和locator。

官方NSR `KeyNumberSearchServlet`新取两个完整书目record：2015AH03 Ahmad/Greene/Kondev/Zhu，PRC91,044310，DOI10.1103/PhysRevC.91.044310；1977BA67 Baranov/Shestopalova/Uchevatkin/Shatinskii，Izv.Akad.NaukSSSR41,1258及英文Bull.Acad.Sci.USSR41,No6,130，无DOI。它们是书目/实验关键词，未当本session已读primary正文。2015publisherPDF候选前缀验证不确定，下载工具拒绝Wiki路径，随后有界官方HTTPS GET403非PDF；OpenAlex无OA URL，OSTI DOI检索200却非JSON、未取得记录，SemanticScholar无OA URL，publisherMarkdown provider不可用。没有绕过访问控制或将正文摘要冒全文。

## Scope and Reading Depth

在cm245-reference-before和exercise冻结、声明MI07旧/新priming后，完整读这两个selectedENSDF对象的797行、源/字段说明/levelγ/ICC/旧MR评论；不称通读全部A245评价、其它Am/Bk/transfer对象或2015/1977primarybody。目标是[[miller-2007-sega-polarization]]的α–γ两reference，不重建完整245Cm结构。

[[tuli-2001-ensdf-format-manual]] TU01-1/2/5的固定栏语义用于MR/RI/CC解读，空MR与无显式号历史comment不能自行补有符号δ。header版本、fetch日期与不同primary采集时间分开。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| N245-1 | 两对象同Nesaraja202305/14Feb2023cut；Adopted E/RI引Cf249alpha，alpha的J/T引Adopted，不能把二者计独立reference测量。 | version-and-dependence | direct-evaluation | Adopted L1–13; Alpha L1–2/L129–130 | true |
| N245-2 | reference同parent388.170(.012)keV、9/2−，T1/2=.450(.020)ns；333.37(.02)到54.784(.012)9/2+、388.15(.02)到ground7/2+。MI07旧388.3是原版本示意，不能据位数变化判其实验错。 | transition-identity | direct-evaluation | Adopted L56/L120/L132/L136; Alpha L177/L252/L270/L281 | true |
| N245-3 | 当前两个reference均标(E1)，MR/DMR栏空；不是测得δ严格0或独立认证MI07纯dipole假设。另266.63同parent支明确E1+M2/MR.076(+.007/−.008)，不能迁给333/388。 | mixing-input-boundary | direct-evaluation | Adopted L127–139; Alpha L262–291 | true |
| N245-4 | Alpha评论保1977Ba67的333 E1+M2幅度.084(+.014/−.018)、388 .13(+.01/−.02)，未给显式sign/primaryphase；当前fields不采用它们为MRcentral，不当signednative输入。 | historical-counter-input | direct-evaluation-comment | Alpha L274/L285 | true |
| N245-5 | 2015Ah03的L3 ICC接近pureE1理论，K/L1+L2/M/N等约两倍，被评价解释为anomalousE1conversion；不能仅由转换系数异常判γ含指定M2或从BrIcc反造δ。 | interpretation-and-alternative | direct-evaluation | Alpha L122–128/L271/L275–291 | true |
| N245-6 | reference的CC .0348(.0005)/.0254(.0004)及Srecord分壳由BrIccv2.3e FrozenOrbitals给，另2G experimentalICC来自2015；modelCC和实测分壳不是独立的同量实验重复。 | conversion-provenance | direct-evaluation | Alpha L135/L270/L275–291; Adopted L31/L132–139 | true |
| N245-7 | Alpha Nrecord NR=BR=1，RI33314.8(.4)/38866.0(2.0)为该alpha分支absolutephoton；Adopted22.4(.6)/100(3)是同parentrelative。其比.224242/.224末位相容，不是两次独立branch测量或P值。 | probability-normalization | direct-evaluation-and-arithmetic | Alpha L142–144/L270/L281; Adopted L132/L136 | true |
| N245-8 | 333与388从同388.170母态是替代支，单次该母态退激不会连发两者；333后还可54.77低支但该支大ICC。不能把两个边际RI乘成其photonpair或当P权重。 | cascade-role-boundary | direct-level-map | Alpha L177–187/L252–291 | true |
| N245-9 | 54.77低支为54.784→0、MR1.3(+.4/−.2)/CC219(33)；另一54.77为442.892→388.170、MR.63(.04)/CC121(8)，不同parent/selection，不能按Eγ同名合并。 | near-energy-reference-identity | direct-evaluation | Alpha L177–187/L298–314 | true |
| N245-10 | .450ns为half-life，mean约.649213ns；不是MI07同源Q/P的独立误差输入。下游低支采用CC219时photon概率名义1/220=.00454545，不能由此否定仅α–333而不观测下游的完整trace。 | arithmetic-and-conditioning | direct-input-and-task | Alpha L177/L179/L252 | true |
| N245-11 | directalpha到388母态Iα82.4(.3)%、442.892为4.68(.07)%且能馈入，58xxα门/Si接受可改变有效布居；当前评价未提供SeGAactualα能门/响应/联合Σ，不把evaluationbranch当测得取向。 | feeding-and-gate-readiness | direct-evaluation-and-scope | Alpha L253/L298–305; MI07-D17-2/3 | true |
| N245-12 | 历史MR幅度只作代数，M2份额约.0070066/.0166191而最大双线性系数.166823/.255679；不是实际P偏移或实验CI。小强度不能单凭自身保证matchingP误差同阶小。 | interference-versus-intensity | task-calculation | Alpha L274/L285 | true |
| N245-13 | reportedexperimental分壳central之和333=.06474、388=.05566，约为modeltotalCC的1.8603/2.1913；它们是部分shellsum/未知Cov的诊断，不是新totalICC测量或转换anomaly到M2唯一反演。 | partial-ICC-arithmetic | task-calculation | Alpha L275–291 | true |
| N245-14 | 2015AH03书目四作者/PRC91,044310/DOI已由官方NSR核；1977BA67四作者/双语刊页核。NSR pdfAvailablefalse不说明所有仓储无全文，当前publisherGET403不重试权限终态，primarybody仍未读。 | primary-identity-and-access-boundary | official-NSR-and-retrieval | NSR2015AH03; NSR1977BA67 | true |
| N245-15 | 当前评价保anomalousconversion与旧混合评论，限制直接跨年把pureE1当无误差P参考；不因此否定MI07实验，actualγP还需α–γAD/相位/finiteacceptance和matchingQ/a/Σ。 | knowledge-impact-and-readiness | source-synthesis | N245-3; N245-4; N245-5; MI07-D17-6/7 | true |
| N245-16 | 对已核Ji9/2→Jf9/2与7/2，若两pureE1且sharedconditionalrho/已unfold同接受，rank2系数R333=−4√330/165、R388=√330/60，故a333/a388=−16/11，不需Gaussianalignment。它是必要条件，不自动认证actualsource共同响应。 | task-common-parent-necessary-relation | exact-CG-and-Racah | Adopted L120/L132/L136; MI07-D17-6 | true |
| N245-17 | 用原MI07 a333−.29(.02)/a388.17(.01)，条件residual−.0427273；独立误差额外假设下sigma.0247299/比1.72775，未知corr的localσ范围.0054545–.0345455。一倍marginalboxes不交/两倍交，并非jointCI、实验reject或Q重标。 | task-summary-uncertainty-boundary | derived-conditional | MI07 printed716 Fig5/Sec4.1; N245-16 | true |

## Summary

这组新官方body确认SeGA两reference的实际parent/branches与当前版本，同时提供当前MR空字段、历史混合幅度和异常转换的不同来源层。它提高reference-readiness的具体性，却没有提供SeGA实际响应/Σ或原primaryphase；不从评价标签直接重标Q。

## Theory/analysis exercise

`system/scripts/day17_cm245_reference_audit.py`核两text hash/固定record栏、primaryL与continuation分开、两个reference和两个同能54.77parent不混、MR空/归一/ICC与历史幅度算术。冻结合同和结果为本run `cm245-reference-contract.json` / `cm245-reference-result.json`。

当前2个reference的RI ratio约.22424与原MI07“388约333四倍counts”量级相符，但不同效率、alpha selection/array/曝光不能凭此认证其精确实验countsprediction。mean寿命与half-life、photon与totalbranch、experimental2G与BrIccS/CC全部分开；缺Σ不把这些派生列当独立误差输入。

## Competing Interpretations and Limitations

- 转换异常可以保E1性质，旧E1/M2分析又有其历史数据；没有primarybody/方法/penetrationmodel/phase时不消掉任何一层或选δ号。
- 当前Adopted括号(E1)与MR空不提供严格纯度上限；旧无显式号幅度不能当native有符号δ。
- αtag实际能量/角/时间接受可改变核制备，后续门/feeding/转换亦需完整通道权重。当前不同objects/年份不是independentSeGAcalibration。
- 此selectedread没有验证MI07实际Qrel/阈值/segmentordering/peakfitΣ，也没有新测量Jπ、δ或ICC。

## Knowledge Impact and Learning Decision

`supports`两同parentreference身份及source/method依赖，`limits`空MR即pure、ICCanomaly即M2、同能γ同角色、不同评价对象即独立实验的简写。将核reference新输入接回[[miller-2007-sega-polarization]]与[[polarimetry-shared-calibration-count-design]]；[[internal-conversion-analysis]]中添加分壳异常/纯度解释入口，保needs_review。

## Related Knowledge and Project Relations

- [[miller-2007-sega-polarization]]：same249Cf/245Cm两参考的currentidentity/purity边界。
- [[compton-polarimetry]]：knownP的核制备和instrumentQ不同层。
- [[internal-conversion-analysis]]：BrIccmodel、实测分壳、penetration/anomaly与MR推断不能互换。
- [[tuli-2001-ensdf-format-manual]]：固定MR/RI/CC字段和comment的角色。

## Human Review Triage

保持所有15新claim needs_review；无human-reviewed。正式论文若依赖strictpurecalibrator，下一实际输入为2015/1977primarybody及SeGA的核P/response/Σ合同，不能从本评价正文外推其完整实验误差。

## Extracted Pages

不建立完整245Cm/249Cf能级库；本页限定source-reference identity/转换companion。可复用事实留在本knowledge页，outputs仅执行轨迹与哈希。

### 同母态pureE1的必要AD对照

N245-16/17与[[polarimetry-shared-calibration-count-design]]“Cm245同母态：先检验共同P标尺的必要关系”用actualJ/a2作本session后续bounded检查。exactratio不依赖自由取向先验，但需要实际共同ρ/门/有限接受条件；marginalsummary没有jointΣ，不从残差给新sign/混合比或推原Q失败。新script初JSON序列化sympybool失败已保、改builtinbool后才写出结果，不把无artifact时算通过。
