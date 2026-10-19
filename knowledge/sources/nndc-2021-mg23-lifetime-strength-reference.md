---
type: source
title: "23Mg官方记录：近能母态、自旋候选与寿命—强度输入"
title_original: "23Mg Adopted Levels, Gammas and selected reaction datasets, ENSDF 202101"
aliases: [NNDC2021 Mg23 reference, Mg23 lifetime strength lineage]
created: 2026-10-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data
reading_depth: skimmed
authors: [M. Shamsuzzoha Basunia, Anagha Chakraborty]
year: 2021
journal: Nuclear Data Sheets
volume: 171
pages: 1-252
doi: 10.1016/j.nds.2020.12.001
citation_key: ""
canonical_source: "NNDC ENSDF202101 Mg23 selected objects, NDS1711, cutoff1Jun2020"
source_url: https://www.nndc.bnl.gov/ensdf/
raw_file: raw/nuclear-data/day17-20261020/23Mg-Adopted-202101.ens
raw_sha256: 422cbdddc20eb594d6f02697e61ff8ff8095d1514f01364a7925177a7cdd96cc
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [23Mg, 22Na, 23Na]
reactions: [12C(12C,n-gamma)23Mg, 24Mg(3He,alpha-gamma)23Mg, 22Na(p,gamma)23Mg]
methods: [ENSDF-fixed-fields, DSAM, gamma-spectroscopy, resonance-strength]
tags: [lifetime, branching, spin, covariance, reference-lineage]
---

# 自旋和分支是寿命换强度的实际输入

## Bibliographic Record

[NNDC ENSDF](https://www.nndc.bnl.gov/ensdf/)当前返回202101版、cutoff 1-Jun-2020的23Mg记录。对应Basunia和Chakraborty，*Nuclear Data Sheets*171，1–252(2021)，[DOI10.1016/j.nds.2020.12.001](https://doi.org/10.1016/j.nds.2020.12.001)。2026下载日不是2026新评价或实验。

实际通过DatasetFetchServlet的POST quick query发现对象，再按精确datasetcheck从EnsdfDispatcherServlet取得ENSDF text；保留响应与提取文本的不同hash。首次缺少searchType的GET返回首页、完整GET返回“Not a valid input method”，均保留为失败，不把HTTP200当取得数据。

| 对象 | datasetcheck | 实际行数 | 缓存 |
| --- | --- | --- | --- |
| Adopted | 23012001,23MG | 630 | tmp/day17-mg23-reference/adopted.ens |
| 12C(12C,nγ) | 23012029,23MG | 286 | tmp/day17-mg23-reference/c12ng.ens |
| 24Mg(3He,αγ) | 23012034,23MG | 160 | tmp/day17-mg23-reference/he3ag.ens |
| 22Na(p,γ) | 23012005,23MG | 71 | tmp/day17-mg23-reference/pg.ens |
| 1H(22Na,p):res | 23012027,23MG | 40 | tmp/day17-mg23-reference/p-res.ens |

[四对象下载/hash](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/mg23-selected-downloads.json)、[散射对象下载/hash](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/mg23-p-res-selected-download.json)。raw槽未归档，原始保护文件不改。以下行号包括实际首空行。

## Scope and Reading Depth

先冻结本session回忆并声明J04/K16 priming，后读四reaction对象全557行；Adopted定向L1–48、L330–465，未读全部630行或252页评价正文。字段解释循[[tuli-2001-ensdf-format-manual]]。2013Jenkins详细原件、2011Sallaska原件及旧transfer/角关联原件尚未由此取得；编译者转述须按评价证据层使用。

## Summary

同一近能态在fusion reaction中为7785.2、7/2(+)，Adopted为7784.7、3/2+,5/2+并明确保留旧7/2(+)意见。它仍采用J04的half-life6.9(2.1)fs并列K16的<8.3fs；没有由新上限自动判掉旧mean10(3)fs。另一个capture对象报告第二γ支路和更新的共振强度，直接限制把J04单支/旧adopted强度当完整输入的做法。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| M23-1 | 五个精确对象均为ENSDF202101、NDS1711、cutoff1Jun2020；下载日不增加实验或评价版本。四reaction共557行全文、Adopted仅定向范围实际读。 | identity-version-and-scope | direct-evaluation | all datasets L2–4；reading-scope | true |
| M23-2 | c12ng把2013Je04/2004Je02合列于ATLAS16/22MeV、Gammasphere fractional-Doppler链，并称2005/2006为同组会议报告；具体采集是否完全共用尚未原详细文核。编译靶160µg/cm²与J04原40µg/cm²不同，不静默统一或单凭此认新独立实验。 | shared-lineage-and-unresolved-setup | direct-evaluation-and-primary-comparison | c12ng L5–13；J04-2 | true |
| M23-3 | 编译DCO参照为stretched D .9(.1)、stretched Q1.8(.1)，EM字符另借寿命/RUL；J04原1.7(.2)仍保留。ratio顺序/实际门/布居/Σ没有由编译补齐，不能迁作通用P/A/Q或δ判据。 | angular-and-character-contract | direct-evaluation | c12ng L24–42 | true |
| M23-4 | reaction7785.2(1.3)为7/2(+)、half-life6.9(2.1)fs，注释明确来自J04 mean10(3)fs；Adopted7784.7(.8)为3/2+,5/2+，Jcomment保留fusion7/2(+)与不同transfer L。评价不是消除实验候选差异的独立测量。 | matched-parent-and-competing-spin | direct-evaluation | c12ng L223–226；Adopted L394–398 | true |
| M23-5 | K16对应reaction7787.1(2.0)的half-life<8.3fs，gamma7335(2)；九upper和两个未平均finite都与原mean×ln2在.05fs打印范围内。原K16上限95%标签来自primary，编译LT自身不重构coverage或提供新CI。 | half-mean-and-limit-bridge | direct-fields-and-arithmetic | he3ag L89–158；exercise limit_half_mean_bridge | true |
| M23-6 | he3ag2052.3的half65(12)fs为55(14)与72(12)平均；2769.9的75(10)fs为107(21)与68(10)平均。后两个K16输入72/68是104/98乘ln2，不是原mean被改成72/68；合并评价值也不是K16重测。 | averaged-input-role | direct-evaluation-and-primary | he3ag L38–39/L82–84；K16 TableII | true |
| M23-7 | fusion7769.4支2316.9/5054.8的RI .8/1.1，Adopted7770.4为73/100；所列光子归一约.421/.579，吻合J04的42/58打印尺度，但归一/不同表不是新branch实验或totaldecay inventory。 | photon-normalization-and-dependence | direct-fields-and-arithmetic | c12ng L213–216；Adopted L380–385 | true |
| M23-8 | capture7784.7的5732/7332.7支为11(5)/89(5)，Adopted5732/7333.2为16(4)/100(6)，前者低支RI又被与23AlEC作unweighted average。不同归一/数据源不能用作两项独立确认；J04只见7333.7不能保证物理单支。 | missing-companion-and-shared-evaluation | direct-evaluation | pg L36–40；Adopted L399–402 | true |
| M23-9 | pg注释给2011Sa12的omega_gamma5.7(+1.6,-.9)meV，与J04adopted1.8(.7)不同。本文仅读编译，未核2011原yield/normalization/系统误差或做联合新率拟合，不能据两个表中心宣称显著冲突。 | newer-strength-input-and-readiness | direct-evaluation | pg L6–23/L36–40 | true |
| M23-10 | c12ng7852.3及5138.1支保留评价注释：J04报告、2013fullversion缺失，2019沟通称可能有误但未确认。此为编译者记录的未决身份边界，不改写为作者正式勘误或删除原J04观测。 | identity-counter-evidence | direct-evaluation-comment | c12ng L227–236 | true |
| M23-11 | Adopted能量经测得γ的least-squares fit，派生γ在fit后由gap作recoil subtraction；各reaction另有具体注释。它不解决J04原recoil声明与K16二级评论的定义差异，不把gap和photon机械相加裁决。 | energy-definition-and-provenance | direct-evaluation | Adopted L13–21；he3ag L17–19；pg L19–30 | true |
| M23-12 | 选定的2013Ji13散射对象只有8611/8793/8916三态；elastic-only R-matrix假设明确。它未给7785的Γp，不能仅同核素/近反应补本问题缺少的particle branch。 | necessary-companion-unavailable | direct-evaluation | p-res L8–38 | true |
| M23-13 | 声明两通道/mean10fs/omega5.7meV及22Na spin3、p spin1/2，J3/2中心组合无实Bp根；J5/2两根.2811/.7189，J7/2两根.1862/.8138。只是固定输入约束，既非spin排除也非branch测量或jointCI。 | conditional-strength-exercise | task-model | exercise conditional_rate_constraints | true |
| M23-14 | 同条件omega固定，tau上界g hbar/(4omega)对J3/2、5/2、7/2为8.248/12.372/16.497fs。τ误差、新upper、omega误差/共享源及通道假设未组成joint likelihood，不能把中心不可行称实验矛盾。 | conditional-constraint-and-boundary | task-derivation | exercise conditional_rate_constraints | true |
| M23-15 | 所列两γ的归一Jacobian各列和零，故p1+p2=1的Cov必有约束；Adopted16/100归一为.13793/.86207不同于capture.11/.89，未得原Σ不强行平均/独立误差叠加或制造CL。 | normalization-covariance-contract | task-derivation | exercise listed_gamma_normalization | true |

## Theory/analysis exercise

[回忆冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/mg23-reference-before-freeze.json)、[算前合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/mg23-reference-exercise-before.md)、[hash输入](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/mg23-reference-exercise-contract.json)、[程序](../../system/scripts/day17_mg23_reference_contract.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/mg23-reference-exercise-result.json)。旧parser只读/hash锁定，没有改Pb207/S31或K16原打印数据。

声明窄共振仅p/γ两通道：

\[
\Gamma=\hbar/\tau,\quad g=\frac{2J+1}{(2J_t+1)(2J_p+1)},\quad
\omega\gamma=g\Gamma B_p(1-B_p)\leq\frac{g\hbar}{4\tau}.
\]

从中心点得到的无根只说明这些固定量不能共同满足这个条件模型；需要匹配自旋、particle branch、原实验误差和共同输入后才能比较。原K16<12fs也不提供固定τ=12fs或正下界，不能拿上限端点代替寿命测量。

## Competing Interpretations and Limitations

原始计数/停止与feeding配置/fitΣ仍缺。2013详细文的公众入口实际未得body：UNC TLS EOF、APS abstract403/harvest401、Birmingham只有record、OSTI DOI XML空、arXiv exactDOI0、HAL DOI/title0、York403；这些是当前路线失败，不是全网穷尽或科学否定。[readiness回执](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/jenkins2013-primary-readiness-boundary.json)。不绕权限，不联系作者，不把摘要/元数据冒作body。

## Knowledge Impact and Learning Decision

`revises`把旧fusion J7/2当所有后续反应唯一自旋、把原单支/旧adopted强度视完整输入；`supports`按mother/branch/source匹配和half/mean桥；`limits`评价转载、中心代数、裸DCO对新实验结论的保证。所有新claim保持needs_review；没有新实验τ、Jπ、Γp、ωγ、δ或置信区间。当前只是Day17窗口内恰好Day18无学分预习。

## Extracted Pages

[[jenkins-2004-23mg-fractional-doppler-rate]]、[[kirsebom-2016-23mg-dsam-lifetimes]]、[[lifetime-strength-audit-165tm-136nd]]、[[doppler-shift-attenuation-method]]、[[linear-polarization-asymmetry]]。
