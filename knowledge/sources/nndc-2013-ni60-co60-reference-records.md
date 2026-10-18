---
type: source
title: "60Ni/60Co参考输入：评价混合比、归一与源模型边界"
aliases: [NNDC Ni60 Co60 reference records, ENSDF6002800160028002]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data-object
reading_depth: skimmed
authors: [E. Browne, J. K. Tuli]
title_original: "Nuclear Data Sheets for A = 60"
journal: Nuclear Data Sheets
year: 2013
volume: 114
pages: 1849--2022
doi: "10.1016/j.nds.2013.11.002"
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "NNDC60028001 ADOPTED; 60028002 CO60 B-1925.28D; 201312"
source_url: "https://www.nndc.bnl.gov/ensdf/"
data_version: "201312/fullcut31-Dec-2012; Adopted updatecut1-Dec-2013; retrieved19-Oct-2026"
raw_file: "raw/data/gpt/day16-20261018/ni60-adopted-1acde766a8ee.ens"
raw_sha256: "1acde766a8eec3f2ca12927a39b4f1e13319e9bd5a740eb8366cf0f4ce459c58"
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [60Ni, 60Co]
reactions: []
observables: [gamma-energy, relative-photon-intensity, multipole-mixing-ratio, conversion-coefficient]
methods: [ENSDF-fixed-column, source-lineage, conditional-error-propagation]
tags: [reference-transition, calibration, phase-convention, shared-input, source-model]
---

# 60Co校准中的评价输入与实际观测要分开

## Bibliographic Record

E. Browne、J. K. Tuli，*Nuclear Data Sheets* **114**,1849–2022(2013)，DOI[10.1016/j.nds.2013.11.002](https://doi.org/10.1016/j.nds.2013.11.002)。Crossref核作者、题名、卷页；实际读取的是NNDC选定文本对象，不声称通读整条A=60评价。

官方[ENSDF入口](https://www.nndc.bnl.gov/ensdf/)先经`DatasetFetchServlet`选60NI，再POST `EnsdfDispatcherServlet`，`chooseit=ENSDF text format`及精确`datasetcheck`。对象与完整HTTP wrapper/文本hash见[下载回执](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/ni60-reference-selected-downloads.json)。原文保存于仓库tmp，raw归档槽仍缺，未修改raw/Bib。

| 对象 | 版本/范围 | 原文本位置 | SHA-256 |
| --- | --- | --- | --- |
| 60028001,60NI Adopted | 201312，2645行；fullcut31-Dec-2012，updatecut1-Dec-2013 | `tmp/day16-ni60-reference/adopted.ens` | `1acde766a8eec3f2ca12927a39b4f1e13319e9bd5a740eb8366cf0f4ce459c58` |
| 60028002,60NI Co60 β−1925.28D | 201312，140行；fullcut31-Dec-2012 | `tmp/day16-ni60-reference/co60beta.ens` | `45eac223f06bab10a1884307e886d7f5db3c5987f6240046c41a3efc56461a06` |

60028003是10.467分钟isomer，未混入本次ground-state校准源。

## Scope and Reading Depth

完整读β−140行；Adopted只读general前250行及相关low-level/γ277–351行，不声称全2645行精读。另读NSR1980KR05的正式JSON与Crossref书目，尚未取得其论文正文。新回忆明确受旧Day16模型和已读评价priming，非盲测。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| N60-1 | 两对象属Browne/Tuli2013谱系；Adopted的1-Dec-2013更新和fullcut31-Dec-2012分开，查询年份2026不等于新实验。β−对象另说明基于Helmer1998及旧评价。 | version-and-lineage | direct-object | 60028001 H lines2–6；60028002 lines2–17 | true |
| N60-2 | first1173为4+→2+、E2(+M3)，last1332为2+→0+、E2。Adopted的Ex为2505.753(4)/1332.514(4)，β−为2505.748(4)/1332.508(4)；不能静默合并成同一精度对象。 | transition-identity | direct-object | 60028001 L2505.753/G1173.228/L1332.514；60028002 L2505.748/G1173.228/L1332.508 | true |
| N60-3 | 两者first MR都为−0.0025(22)，ENSDF末位误差解码为0.0022。Adopted明确取自长寿命β−对象，后者MR注指1980Kr05；两个评价对象不计两次独立测量，文件同号亦不认证primary算符。 | evaluated-MR-and-dependence | direct-object-and-format-check | 60028001 G1173.228/MR comment339；60028002 G1173.228/DMR/comment126 | true |
| N60-4 | Adopted first/last RI为100.00(3)/100的relative值，β−为99.85(3)/99.9826(6)且N记录各归一因子1。β−RI由共同馈入/弱支/转换平衡导出，联合Cov未恢复；两个marginal photon概率相乘不是cascade pair概率。 | intensity-normalization-and-dependence | direct-object | 60028001 G1173.228/G1332.501；60028002 N63/G1332.492 RI79–83/G1173.228 RI123–125 | true |
| N60-5 | S-record first/last CC=.0001722(25)/.0001625(23)由DG声明的BrIccv2.2 FrozenOrbitals更新；旧cG另述1985HaZA实测评价与旧理论α/IPC。不能把不同层的S值与旧comment合并成独立实测ICC。 | conversion-provenance-boundary | direct-object | 60028002 DG41–42/S G121–122/cG127–132；G1332.492 S77–78/cG84–88 | true |
| N60-6 | NSR1980KR05确认为Krane/Sites/Smith/Steyert，NIM169,573–576(1980)，DOI10.1016/0029-554X(80)90959-3。β−global注明低温Co60/Fe取向γ角分布，NSR关键词为Iγ(θ,H) in Fe；这不是已取得原γγ门/phase/Cov正文。 | primary-identity-and-access-boundary | official-metadata-and-evaluation | NSR1980KR05 title/doi/keywords；60028002 global21–23 | true |
| N60-7 | 固定G411的level1/4 Ex恰匹配Adopted；first MP407/nativeδ−.0025、last MP4/δ0，文件没有δ误差。其nominal1173.239是level差，不能当评价光子E1173.228相矛盾或当primary测量。 | source-input-crosswalk | actual-file-and-object-check | G411 examples/sources/co60/z28.a60.lvldata level1/4；60028001 selected records | true |
| N60-8 | 用实际SDK11.4.2 Ni60 nuclear mass作静止两体检查，Adopted first/last Eγ为1173.2266688/1332.4980932keV，β−为1173.2276688/1332.4920933keV；反冲约.012331/.015907keV。level/γ共同Cov未知，不作独立z检验或认证lab recoil/transport。 | conditional-rest-frame-energy-check | SDK-mass-and-two-body-calculation | 本页静止两体公式；ni60-reference-audit-result rest_frame_energy_crosschecks | true |
| N60-9 | 在明确假设quotedδ映为本run native basis时，point90°/identitytag Pfirst/Plast对共同δ导数为.5527768642/.9256636491。仅δ分量的Cov为Jσδ²Jᵀ，difference σ=.0008203509；错当独立为.0023719382。此为条件模型误差分量，非实验P Cov或完整CI。 | conditional-shared-input-error | point-model-propagation | 本页共同δ误差公式；ni60-reference-audit-result pointP_shared_delta_component | true |
| N60-10 | β−评价central/当前S CC下pair概率RI1173/[100(1+CC1332)]=.9983377701；共同RI/CC误差和真实source选择未知，不能称完整实验pair CI或用两marginal乘积替代。 | conditional-evaluated-pair-probability | evaluation-central-arithmetic | 60028002 G1173.228 RI/G1332.492 S CC；本页pair公式 | true |
| N60-11 | 当前G4LevelReader先按Iγ(1+CC)抽总分支，再按1/(1+CC)抽光子。实际SDK读取同level文件的pair概率.9983894029，与corr/iso100k的99840/99845pairs条件相容；这是同模型内部核验，不计独立实验或Q验证。 | executable-source-model-check | actual-SDK-and-finite-MC | G4LevelReader-v11.4.2 lines358–362；ni60-RDM-pair-consistency-corrected-result actual_level_object | true |

## 两套评价对象与静止反冲检查

| 字段 | Adopted | 长寿命β− |
| --- | --- | --- |
| first Eγ/keV | 1173.228(3) | 1173.228(3) |
| last Eγ/keV | 1332.501(5) | 1332.492(4) |
| first RI | 100.00(3)，relative | 99.85(3)，per100decays |
| last RI | 100，relative | 99.9826(6)，per100decays |

令SDK ground nuclear mass `M=55810902.779622644keV`、`Ei/Ef`为同对象Ex，静止发射为

`Eγ=[(M+Ei)²−(M+Ef)²]/[2(M+Ei)]=(Ei−Ef)(2M+Ei+Ef)/[2(M+Ei)]`。

此处使用SDK的模型质量，不宣称新的质量测量。级联第二γ在lab还受第一步反冲/寿命/环境影响；本检查没有恢复该完整过程。两对象本身共用测量/评价输入，不能将小残差除以假定独立误差后宣称新冲突。

## 共同δ误差与实际源分支

[[co60-gate-role-response-benchmark]]的point模型只取unpolarized4→2→0、偏振等效率reference、90°、无finite geometry。条件桥`δ_native=quotedδ`不能替代尚未取得的1980算符正文；native/RB变换仍要连operator一起做。

`Covδ(Pfirst,Plast)=σδ² J Jᵀ`，其中`σδ=.0022`、`J=(.5527768642,.9256636491)`；矩阵两对角约`1.478921346e−6/4.147169445e−6`、非对角`2.476557574e−6`，rank1/PSD。central差`.0009283075`只相对于这一误差分量比较；共享误差对差值会抵消，不能概括为相关性总让误差增大。导数步长1e−5/1e−6相符，端点输入范围不叫CI。

同SDK RDMground-state输入为`.9988`馈入2505.753。设upper分支光子相对强度`Ig=(.0076,100,.000002)`、`CC=(.00557,.0001722,.0000863)`，则

`p_pair=.9988 × 100/[Σj Ig_j(1+CC_j)] × 1/(1+.0001625)`。

typed double得到`.9983894785`；实际SDK float CDF/光子概率得到`.9983894029`，差7.56×10^-8。SDK值预测每100k约99838.94pairs，实际99840/99845，fixed-input exact-binomial双侧p≈.969/.664，仅作内部一致性。最初错误地只归一Ig的表达式差4.09×10^-7，已在canonical写回前隔离，其失效试算仍保留；不能因小N下结论相同而隐去归一错误。

## Summary

本页补齐60Co参考的正式数据身份、0.0022误差尺度和同源依赖，并将评价、静止模型、已加载SDK对象与MC分开。支持当前source输入的局部一致性；不产生新δ/P/Q实验结果或phase认证。

## Competing Interpretations and Limitations

- 1980Kr05正文未取得：出版商403；公开API200但只有coredata；OpenAlex仅非OA位置、HAL0结果、ADS拒绝、Scholar超时。其它仓储路由按各回执区分失败与未查，不能写成“没有任何合法全文”。
- 同号/同数值不能认证primary reduced matrix element、发射/吸收、spin ordering、interference项。原ENSDF通用约定[[martin-1987-ensdf-mixing-ratio-phase-conventions]]与格式[[tuli-2001-ensdf-format-manual]]不是该实验producer。
- 本source未做寿命/strength分析；当前T值、旧模型寿命差及其它能级不借来补B或polarimeterresponse。
- 原输入、原publiccode和MC binary不变；phase/readiness仍needs_review，不升human-reviewed。

## Knowledge Impact and Learning Decision

`supports`明确reference identity、共同δ误差及actualSDK内部branch概率；`revises`误差末位/归一对象的潜在误读；`limits`以G4配置、两个评价转录或相容MC认证独立实验P/Q/δ。仍属Day16当前问题与partial17知识预习，不授17学分。

## Extracted Pages

- [[co60-gate-role-response-benchmark]]：target/reference角色、共同误差、实际branch权重。
- [[compton-polarimetry]]：quotedδ误差分量不能替完整reference/arrayQ校准Cov。
- [[ucgretina-2024-geant4-11-source-replay]]：同输入MC核验与独立实验的边界。

## Reproducibility

[fixed-column/误差脚本](../../system/scripts/day16_ni60_reference_audit.py)与[实际SDK分支脚本](../../system/scripts/day16_ni60_branch_replay.py)；前者使用既有`PYTHONPATH=tmp/day16-jt74/python-deps`的SymPy1.14.0，后者source parser可不加载符号依赖。SDKhelper实际编译/执行exit0，质量/level输入、源码和binaryhash均在本run的ni60相关回执。原件内容只在tmp，未stage原PDF/SDK/下载源码。精确对象marker和本页原子claim是知识依据，outputs回执仅证明执行与文件身份。
