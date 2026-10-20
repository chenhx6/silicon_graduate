---
type: source
title: "58Fe官方参考谱系：同一Coulomb B、半衰期与静态Q"
title_original: "58Fe Adopted Levels, Gammas; Coulomb Excitation; 55Mn(alpha,p-gamma), ENSDF201004"
aliases: [NNDC 2010 Fe58 reference, Fe58 811 reference lineage]
created: 2026-10-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data
reading_depth: read
authors: [Caroline D. Nesaraja, Scott D. Geraedts, Balraj Singh]
year: 2010
journal: Nuclear Data Sheets
volume: 111
pages: 897
citation_key: ""
canonical_source: "NNDC ENSDF201004 Fe58 exact datasets58026001/58026019/58026007"
source_url: https://www.nndc.bnl.gov/ensdf/
data_version: ENSDF201004-cut12Jan2010-Adopted-JPIerrata12Nov2013
raw_file: raw/nuclear-data/day18-20261020/58Fe-Adopted-201004.ens
raw_sha256: c322943905a154f113f18a5b1929e2345274298052590512e9e72ad3fde77a5f
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [58Fe, 56Fe]
reactions: [Coulomb-excitation, 55Mn(alpha,p-gamma)58Fe]
methods: [ENSDF-fixed-fields, source-lineage, mean-half-life-conversion]
tags: [58Fe, Coulomb-excitation, DSAM, reference, covariance]
---

# 811参考态：两种写法可以是同一个实验输入

## Bibliographic Record

NNDC官方exact对象`58026001,58FE` Adopted、`58026019,58FE` Coulomb Excitation、`58026007,58FE`55Mn(α,pγ)。header为ENSDF201004、Nesaraja/Geraedts/Singh *NDS*111897(2010)，cut12Jan2010；Adopted另有12Nov2013“Corrected some JPI”记录。2026下载日不代表已含2026新实验或本年重新评价。

来自[DatasetFetchServlet](https://www.nndc.bnl.gov/ensdf/DatasetFetchServlet)实际发现27datasets后，用[EnsdfDispatcherServlet](https://www.nndc.bnl.gov/ensdf/EnsdfDispatcherServlet)逐个exactdatasetcheck请求ENSDFtext。原响应/参数和text hash保存于[两个对象回执](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/fe58-official-downloads-004.json)、[reaction回执](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/fe58-official-reaction-download-004.json)。不是NuDat摘要或搜索snippet。

缓存`tmp/day18-20261020/fe58-official/`中Adopted1139行、Coulomb34行、reaction140行；首空行保持。Coulomb SHA256`712fbff829d1023d8a5f2bbc0d574d2e06c4ccf909f64e4c762c70080a108acf`，reaction SHA256`99a244e02eee5bcc21a3f275aec91c35a8417e2adb4894c04d0976ac0ea8167f`。raw归档槽未写，protectedBib不改。

## Scope and Reading Depth

本Day18在WO26原文/reference priming后冻结新问题。Adopted只读header/provenance1–65及67–133的选定低态/γ/来源评论，**未读全部1139行**；Coulomb全部34行，reaction全部140行。反应对象是为区分原papermean与官方half-life而作必要同核扩展，不是新卡或masswide扫描。

原1981Le02、1978Bo35正文未读；NSR两exactkey查询均因SSL验证失败未得body，不降TLS或改凭据。当前原paperbibliography来自已读[[woodside-2026-fe58-collectivity-coulex-dsam]] Ref29/16；官方记录的来源标识独立保留，不假称NSR检索已成功。

## Summary

官方811态的6.54(.19)ps是half-life，且评论明确**由1981Le02的B(E2)=.1234(.0036)推得**。平均寿命9.435ps、对应RME约.351eb与WO26采用的referenceτ/RME相对应，单位换算并非新增寿命测量。静态Q也回指同1981Coulomb研究；实际B/Q联合Σ未给，不能按同源就猜其相关系数，更不能直接裁定Gosia发生何种计权。

## Experimental or Method Setup

官方Coulomb对象区分1981Le02的12C/52Cr激发、2009Ea02的高速58Fe g-factor实验及其它旧结果。g-factor、MOME2和BE2是不同观测；同data对象名或同near-energy不能合成一项新标定。reaction对象则逐项标1978Bo35 DSAM/pγ和1977Ca28不同束能/γ谱，非本任务原读两篇旧实验。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| F58-1 | 三exact对象为ENSDF201004/cut12Jan2010；Adopted2013errata仅说明correctedJPI，不代表全部新测量已更新。对象/原响应/首空行/texthash均核，2026获取不当新评价或实验。 | identity-version-and-scope | direct-evaluation | Adopted L2–5；Coulomb L2–4；alpha-pg L2–4 | true |
| F58-2 | Adopted810.7662(20)2+的T字段6.54PS/DT19，评论“from B(E2)=0.1234 {I36} (1981Le02, Coul. ex.)”；Coulomb811也列同T及“deduced from B(E2)”。该T与B是同源派生，不是独立lifetimecompanion。 | direct-reference-lineage | direct-evaluation | Adopted L82/L99–105；Coulomb L14/L27–32 | true |
| F58-3 | Adopted静态MOME2=−.27(.05)，comment为1981Le02 reorientation及2005St24compilation；CoulombliteralMOME2=−27.3(5.0)亦1981Le02。保不同打印/单位字段，不与Q_t/sidefeedingQ_s混用；B/Q来自同primary不能凭此给实际Cov数值。 | static-moment-lineage-and-boundary | direct-evaluation | Adopted L85/L96–97；Coulomb L16/L25–27 | true |
| F58-4 | 按half→mean换算，6.54(.19)ps给9.43523(.27411)ps，与WO26采用9.4(.3)相近。Coulomb励起Bup=.1234e²b²的声明E2chart给RME sqrt(Bup)=.351283eb、Bdown=.02468e²b²；固定printedCC=.000332及γ.8107593MeV的现代率换算得τ9.43732ps。都是条件算术，不新实验或原程序认证。 | task-unit-and-rate-chart | derived-and-boundary | F58-2；Adopted L103–105；WO26 PDF5Eq1/reference段；新fe58-official-input-result-004 | true |
| F58-5 | alpha-pg的T默认来自1978Bo35、C标1977Ca28；810.77T2.4ps、1674.75T1.6ps、2076.70T.37ps均是half-life，后者另comment.24(.07)1977Ca28。除ln2得mean约3.462/2.308/.5338，对WO26旧3.4/2.30/.54只作打印/角色桥，不重拟或更正原寿命。 | direct-old-data-lineage-and-unit-bridge | direct-and-derived | alpha-pg L5/L26–40 | true |
| F58-6 | Adopted2076.52、4+的T.28(.04)ps来自.24(.04)与.24(.07)/.37(+.06−.05)half-life加权，γ1265.74给BE2W47(7)；此旧评价平均与2026updatedτ不是两份新独立测量。 | evaluated-average-and-age-boundary | direct-evaluation | Adopted L117–124 | true |
| F58-7 | Adopted1674.731、2+T1.6(.4)来自αpγ，863.951γ为M1+E2/MR−.69(.05)、1674.725γRI76.4(1.5)。这些是WO26旧branch/δ/原τ的谱系入口，不把RI76.4当absolutephotonfraction或把旧T替2026重分析meanτ。 | exact-parent-branch-and-mixing-input | direct-evaluation | Adopted L106–116 | true |
| F58-8 | 以x=lnBup为唯一随机primitive且E/branch/ICC固定，lnM=x/2、lnτ=c−x；联合logCov必为Var(x)C，其中C的两行为(1/4,−1/2)与(−1/2,1)、rank1/corr−1。数值把printedrelativeB scale代Var(x)只为局部设计，非实际GosiaΣ或重复计权已发生的证明；真实能标/ICC/Q可增加自由度。 | task-conditional-dependency-and-covariance | derived-and-boundary | F58-2/4；WO26-4/5；新13checks结果 | true |

## Analytical Reconstruction and Self-Audit

新[对象合同](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/fe58-official-input-contract-004.json)、[程序](../../system/scripts/day18_fe58_reference_lineage_audit.py)/[13项结果](../../outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01/fe58-official-input-result-004.json)先核三hash和literal来源，再作half/mean、referenceRME/单支E2率与声明rank1chart。RawBup误差给RME局部尺度约.005124eb，WO26原.351(.006)保持；本文不从差值反解其采用的舍入/协方差，亦不改paper输入。

“同源”只回答哪些约束不是独立新测量。WO26 actualGosia是否将它们同时赋独立权重、是否有专门normalization处理或何种τ约束权重，仍须job/目标函数才能判断。官方评论本身不提供这份执行证据；不做circular-invalid或误差缩小多少的结论。

## Competing Interpretations and Limitations

官方评价的sourcekey、值、时间字段和comments不是对旧实验系统误差的重新测量；2010的adoptedB47不能覆盖2026的新采集。MOME2与g-factor标不同roles，compiledB/T可确定派生依赖但不能补actualB/Q covariance。旧αpγ的branch/δ引用还混合不同papers，需逐branch来源而非整dataset独立。

## Knowledge Impact and Learning Decision

`supports`[[woodside-2026-fe58-collectivity-coulex-dsam]] WO26-5的actualinput优先级；`revises`把adopted9.4ps与reference.351eb自动当两个独立观测的输入图。关系写回[[lifetime-strength-audit-165tm-136nd]]与[[doppler-shift-attenuation-method]]，只做输入依赖审计，未裁决该paper原fit或结构结论。

## Extracted Pages

来源对照：[[woodside-2026-fe58-collectivity-coulex-dsam]]；方法：[[doppler-shift-attenuation-method]]；研究审计：[[lifetime-strength-audit-165tm-136nd]]。不新建重复的58Fe核素页，不修改原评价/用户raw/Bib或其它项目。

## Human Review Triage

P0自审：F58-2来源T/B依赖、F58-8条件Cov域与actualGosia区分；P1：旧paperbody/NSR TLS、2013限定更新、半衰期/mean/RI/δ角色。所有claims needs_review、sourceunreviewed，非human-reviewed。

## Reproducibility and Evidence Gaps

ENSDFtext与响应/payload/hash/行号在本Day18 run及缓存；raw归档deferred。当前未得original1981Coulomb/实际B-QΣ、Gosia版本/约束权重/逐探测器计数及去目标τprofile。下一有价值输入是这些匹配原件或执行合同，不重复13项算术来代替。
