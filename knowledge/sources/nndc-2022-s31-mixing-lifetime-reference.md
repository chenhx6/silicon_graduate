---
type: source
title: "31S官方记录：1248混合比双根、寿命字段与Sun模型扣除"
title_original: "31S Adopted Levels, Gammas and 32S(3He,αγ), ENSDF 202209"
aliases: [NNDC 2022 S31 reference, 31S 1248 mixing reference]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data
reading_depth: read
authors: [Jun Chen, Balraj Singh]
year: 2022
journal: Nuclear Data Sheets
volume: 184
pages: 29
citation_key: ""
canonical_source: "NNDC ENSDF202209 31S selected datasets 31016001/31016064, Chen and Singh NDS18429"
source_url: https://www.nndc.bnl.gov/ensdf/
data_version: ENSDF202209-fullcut24Jun2022-Adopted-update23Nov2022-and-XUNDL202401-2023Su03
raw_file: raw/nuclear-data/day17-20261019/31S-Adopted-202209.ens
raw_sha256: 672a9eb7db91f0cae5042e75fa08a3156d95fe70d7405ccb18ca0aafa5563c8a
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [31S, 31P]
reactions: [32S(3He,alpha-gamma)31S]
methods: [ENSDF-fixed-fields, reference-identity, mixing-ratio, lifetime]
tags: [DSAM, reference, mixing-ratio, covariance, 31S]
---

# 31S1248：官方MR输入有真实来源，也有选根条件

## Bibliographic Record

NNDC官方ENSDF selected对象：`31016001,31S` Adopted Levels/Gammas、`31016064,31S` 32S(3He,αγ)。header为NDS184,29(2022)，fullcut24Jun2022；Adopted另有23Nov2022 update，comment明确为2022(p,d)/(d,t)资料。fetch日/更新时间不等整个对象含全部后来测量，也不将其当2023Sun实验的再评价。

对象来自[DatasetFetchServlet](https://www.nndc.bnl.gov/ensdf/DatasetFetchServlet)检索后，用[EnsdfDispatcherServlet](https://www.nndc.bnl.gov/ensdf/EnsdfDispatcherServlet)的exactdatasetcheck/ENSDFtext请求。实际payload、responsehash与selectedtexthash见[下载回执](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/s31-selected-downloads.json)，不是搜索snippet。

缓存`tmp/day17-s31-reference/adopted.ens`，913行，SHA256`672a9eb7db91f0cae5042e75fa08a3156d95fe70d7405ccb18ca0aafa5563c8a`；`he3ag.ens`71行，SHA256`315a14aace3b1299c7eb80a2dc7910e3567f0d6af0dd13396596434da193766c`。原响应首空行保持，locator按保留空行的实际行号。raw归档槽未填、protectedBib未改。

## Scope and Reading Depth

本session在承认Sun全文/SI与rateexercise priming后冻结回忆。实际读reaction全部71行；Adopted定向header/方法/低位1248/2234/3076、3435/4971/5156等identity/branchcontexts，未读全部913行或整份NDS评价。随后另读exactXUNDL31016069的全部45行（明确unevaluated同Sun论文编译），不当新实验或VoRbody。NSR primary key1970Mo08/1971En02的准确bibliography/DOI已核，尚未取得/阅读它们的正文/原fit/phase/Σ。

## Summary

官方1248记录提供可追溯的旧角关联MR+.35(.02)作为Sun的USDB E2扣除之外的companion输入。但同reactioncomment还保留+5.3(.4)另一根，编译中小根的偏好借助了强度上限/RUL；两个编译对象共享同源，不是两个独立MR实验。它们能收窄输入问题，不能自动替代原primaryphase/fit或产生新的Sun后验。

## Experimental or Method Setup

reactiontext描述1970Mo08的12MeV3He、CdS/Sb2S3靶、磁谱仪/Si-Au、α/γ及角关联；1971En02另为7MeV3He、ZnS、DSAM meanlives。它们是当前官方记录对旧实验的摘要，不是本任务已经读完原实验。逆运动学Sun128MeV32S/Au与此setup不同；不能按reaction互易或同发射核直接借response/A2。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| S31-1 | selectedAdopted与3Heαγ对象header/version/cutoff/texthash已核；Adopted的Novupdate限定(p,d)/(d,t)，不代表所有latermeasurement已摄入；两个对象同2022评价不计独立实验。 | identity-version-and-dependence | direct-evaluation | Adopted L2–6；reaction L2–4 | true |
| S31-2 | Adopted1248.60(.08)、3/2+母态的1248.68(.10)γ到1/2+ground，M1+E2、MR显式+.35/DMR2=±.02；RI100为相对光子强度，非单凭此就认证每次decay恰一γ/完整inventory。 | exact-transition-and-MR-input | direct-evaluation-and-format | Adopted L103/L120/L128–137；TU01-1/3 | true |
| S31-3 | reaction1249低态同MR+.35(.02)，comment还保留+5.3(.4)另一解，称其B(E2)(W.u.)62(17)偏大不太可能故prefer小值。选根包含RUL/寿命条件，不是角关联单独保证唯一δ，也不将largecomment静默删去。 | counter-root-and-selection-condition | direct-evaluation | reaction L26–32；L19–22 | true |
| S31-4 | MR/M来自1970Mo08 α–γ角关联，electric/magnetic character在有寿命时借RUL；DSAM寿命另来自1971En02。NSR准确原文为C.E.Moss NPA145423 DOI10.1016/0375-9474(70)90434-3；Engmann等NPA162295 DOI10.1016/0375-9474(71)90986-9。只bibliographyverified，body/fit/phase未读。 | original-lineage-and-readiness | direct-evaluation-and-NSR | reaction L5–22；NSR1970MO08/1971EN02 | true |
| S31-5 | 两对象levelT字段.50(.12)PS是half-life，reactioncomment明确meanτ720(180)fs。印刷half-life按ln2换为mean.72135/.17312ps尺度，与comment舍入层相近，不是第三次寿命；Sun的720(180)旧comparison正引1971En02。 | mean-half-life-and-shared-source | direct-input-and-unit-reconstruction | Adopted L120/L123–127；reaction L26–28；SUN23 PDF5 Ref11 | true |
| S31-6 | Adopted3076.54(.14)与5156.2(.3)均1/2+且给transferL0证据；reaction低精度3079栏只(1/2)。compiledidentity支持问题前提，但不恢复SunactualA2frame/私有模型；不能把旧不同精度能量认新态。 | level-identity-and-A2-scope | direct-evaluation | Adopted L156–164；L371–375；reaction L40–43 | true |
| S31-7 | Adopted4970.8附近comment明确可能有两个不同level，分别βdecay/4970γ与(α,nγ)/3722γ；Sun用4970line的母态选择不能仅按近能名join，更不能从其它channel的spin/branch填其actualresponse。 | near-energy-counter-identity | direct-evaluation | Adopted L343–355 | true |
| S31-8 | selected小根的theorycontinuation CC3.58E−5、K/L/M与IPC1.280E−5同列；K+L+M+IPC≈3.57951E−5只printingclosure，非独立实测ICC、完整Cov或可无对象迁到+5.3/modelδ的响应。 | conversion-and-pair-input-boundary | direct-evaluation-and-arithmetic | Adopted L134–136；s31-mixing-result CC_arithmetic | true |
| S31-9 | 本任务固定Sun总meanτ1.12ps、γ-onlyM1/E2条件，旧smallMR给E2fraction.109131、τM1=1.2572ps/τE2≈10.26286ps/BM1≈.0232725；USDBτE2=6.9给fraction.162319、rate-equivalent absδ≈.440195/τM1≈1.33702/BM1≈.021883。两条是不同条件输入，非新δ测量/CI或modelσ已知的显著性检验。 | conditional-companion-rate-comparison | task-derivation | S31-2/3；SUN23-12/13；s31-mixing-result | true |
| S31-10 | 同条件下largealternate+5.3给E2fraction.965624，τM1≈32.5808ps、BM1≈.000898；这里只保存原候选的幅度后果，没有用newτ/RUL或adopted标签重新选根。原primary/operator/fitΣ未得，不把evaluation正号映成Sun nativephase。 | alternative-input-and-phase-boundary | task-derivation-and-readiness | reaction L31–32；s31-mixing-result alternatives | true |

| S31-11 | Adopted对2010Do03另列RISING cluster/Miniball两组half-life统计/系统误差。中心.8/2.2ps换mean约1.154/3.174ps；额外用stat/systquadrature得到约+1.485−1.127/±7.047ps，与Sun转引1.2+1.5−1.1及3.2±7.0的打印相近。是同paper/detector分析与单位/误差组合，不是新独立lifetime或actualCov复原。 | source-unit-and-error-budget-bridge | direct-input-and-conditional-calculation | Adopted L124–127；SUN23 PDF5；s31-mixing-result2010summaries | true |

| S31-12 | exactXUNDL31016069,31S为202401、27Dec2023compiled的unevaluated2023Su03/PLB839137801。同目录另有XUNDL-11，不能靠suffix当唯一ID；新对象45行全文核，非2022Adopted已包含Sun或新实验。 | new-compiled-object-and-version-dependence | direct-XUNDL | XUNDL L2–13 | true |
| S31-13 | XUNDL把Sun两finiteτ和四upperlimit转写levelT字段：.78PS/172FS、7.6/11/4.8/10FS LT，comments另给原mean1120/250及11/16/7/15fs上限。6390T字段空，仅4156/5141γ，未提供第五个lifetimebound；编译不独立认证原posteriorcoverage。 | actual-compiled-half-life-and-limit-fields | direct-XUNDL | XUNDL L15–43 | true |
| S31-14 | 按源meancentral×ln2，2234为173.2868fs而compiled172，4971upper7fs对应4.8520而compiled4.8；保留名义residual，不补originalunroundedquantile/roundingrule或判实验错。其它row与原comments也分别保存，不能拿compiler最后位改写Sun结果。 | nominal-conversion-and-printing-boundary | derived-and-boundary | XUNDL L19–38；s31-mixing-result compiled_lifetime_rows | true |
| S31-15 | XUNDL3435两γ为2186/62(12)、3435/38(11)，matchingSun测得branchsummary而非oldAdoptedrelative83/100；两者来源/归一不同。quotederror保持，不强推严格normalizedjointΣ；levelT/branch/comments仍同paper，不造新data。 | branching-object-and-covariance-boundary | direct-XUNDL-and-primary | XUNDL L27–31；SUN23 PDF3 | true |

## Competing Interpretations and Limitations

- MR+.35/.02有真实编译来源，但preferredsmallroot另含RUL层；其quotederror不是覆盖两个根的全物理CI。
- Sun的modelE2输入与oldMRcentral不同，差值不能除以oldMRσ就称模型被排除：modeluncertainty、newτ/branch/ICC输入和primaryfit对象尚不齐。
- RI100/同一printedbranch不认证无遗漏γ/非γ；totalCC的理论列不等measurement，不能拿K列替total或对所有δ复用。
- 两ENSDF对象与NSR都回同1970/1971对象；同实验的evaluation转载、不同单位τ值与本次算术不增加独立证据。

## Analytical Reconstruction and Self-Audit

[新合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/s31-mixing-contract.json)、[程序](../../system/scripts/day17_s31_mixing_reference_contract.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/s31-mixing-result.json)核两officialtexthash、fixedfield/parentidentity、MR/.02与half-life解析。复用的parser先hash锁定，不因本问题改动旧Pb207对象或检查数。

条件ΓM/ΓE从t=δ²给fM=1/(1+t)、fE=t/(1+t)，τM=τ(1+t)、τE=τ(1+t)/t。整个表固定同1.12ps/rounded1.248MeV和现代单位系数，只比较输入合同；不是新posterior重算。|δ|=.35时E2fraction局部只含MR误差的尺度≈.011111，未将它独立叠进同时由MR派生的CC误差。正号不进入rate，故不据此声称primary/nativephasebridge完成。

## Knowledge Impact and Learning Decision

`supports`为model扣除寻找有源MRcompanion；`revises`把preferredadopted值看成无条件唯一根、或把half-life/meanτ算两次测量；`limits`官方field对实际A2/response与新置信区间的保证。新增claims全needs_review，不设human-reviewed，不将model或本条件练习升为实验事实。

## Human Review Triage

P1：若替换实际Sun的modelE2或用其作偏振参考，先取得Moss原件/phase/fit和matchingbranch/response/Σ，再做同一forwardmodel的定向比较；当前缺口由Codex追踪，不自动转用户待办。

## Extracted Pages

[[sun-2023-bayesian-dsam-31s]]、[[lifetime-strength-audit-165tm-136nd]]、[[spinhalf-angular-nuisance-response-contract]]、[[doppler-shift-attenuation-method]]。当前Day17内恰好Day18无学分方法preview，不授18、不重复17、不打开19。

字段解释另循[[tuli-2001-ensdf-format-manual]] TU01-1/3；率与现代单位常数循[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-1的既有重构，不能将BM1W(W.u.)栏直接与Sun的µN²数值比较。

## 新XUNDL补充：同文编译不是最终稿正文或新实验

[exactdownload](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/s31-xundl-selected-download.json)、[来源前冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/s31-xundl-before-body-freeze.json)、[45行actualscope](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/s31-xundl-reading-scope.json)保存新版本/fields。cache`tmp/day17-s31-reference/sun2023-xundl.ens` SHA256`56ad828fdacf39ebf44ad8a2a2bc6226a05f46ed084fbcc07550bf07c11d1ab7`。它更新当前输入账本，不改两旧ENSDF对象或宣称2023VoRbody已读。
