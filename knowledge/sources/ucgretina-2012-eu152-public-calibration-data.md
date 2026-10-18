---
type: source
title: "UCGretina公开Eu152校准：实际能谱、背景归一与sorting选择"
aliases: [UCGretina Eu152 source data, NSCL 2012 seven quad calibration]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: public-data-and-software-objects
reading_depth: skimmed
title_original: "UCGretina"
authors: [L. A. Riley, UCGretina contributors]
author_role: repository-software-attribution-not-certified-data-acquisition-authorship
year: 2012
year_scope: acquisition-period-from-example-README-not-repository-publication
data_version: "UCGretina1271388e03ec9b3f8e055a988aeb4c2e4d2efedf; GRUTinizerf648d7cb4fc0609f13aaad7148977f87641ecac9"
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "pinnedUCGretina Eu152 run007/run020 ROOT, README/Fit and sorting objects; pinnedGRUT point decoder"
source_url: "https://github.com/rileyle/UCGretina/tree/1271388e03ec9b3f8e055a988aeb4c2e4d2efedf/examples/sources/eu152"
raw_file: "raw/data/gpt/day16-20261018/ucgretina-eu152-run020-58bc3420b3a2.root"
raw_sha256: "58bc3420b3a2af9892bf722411679eefdfb56ddbd554cc8aec59391465504379"
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [152Eu]
reactions: []
experiments: [NSCL-GRETINA-2012-seven-quads-source-calibration]
models: [Poisson-counting, background-template, Geant4]
methods: [source-normalization, ROOT-histogram-audit, covariance-propagation, code-contract]
observables: [gamma-energy-spectrum, source-background-normalization, detector-angle-histogram]
tags: [public-data, calibration-identity, sorting, response-readiness, not-polarization-calibration]
---

# Eu152公开能谱：实际数据能支持哪一层校准

## Bibliographic Record

本页直接来源是[固定UCGretina example](https://github.com/rileyle/UCGretina/tree/1271388e03ec9b3f8e055a988aeb4c2e4d2efedf/examples/sources/eu152)的README、宏、拟合代码及公开ROOT对象，另读同commit的`util/GRUTinizer/MakeHistosSourcesSim.cxx`、`MakeHistosInBeam.cxx`、`MakeHistos60CoSim.cxx`。项目主体论文DOI10.1016/j.nima.2021.165305只是README给的引用关系，本run未读该论文全文，也不以它替代这些对象。

README指明2012-09 NSCL七quad GRETINA的Eu152源/room-background校准；当前数据树实际有run020源及run007背景。ROOT对象的保存时间是2013-04 metadata，既不改写README采集日期，也不是独立实验证据。此数据不同于[[morse-2022-gretina-polarization-sensitivity]]六quad反应偏振标定和L26十二quad/FMA采集。

run007文件7,123,705bytes，SHA256=`0792a20b82297f966e1e5e95ea722a129ac9a92a7d9f8bee3a83dd4348061f5e`；run020文件8,788,994bytes，SHA256见frontmatter。两者HTTP200、ROOT magic和固定tree Git blob均验证，读取后原hash保持。文件放repo tmp，raw槽尚未归档；未修改用户raw/Bib。

## Scope and Reading Depth

完整读Eu152 README/Makefile/两macro/eu152Fit.C、angdist Makefile/angDist.C/pol.C及上述三sorting文件的主线；ROOT已读全部key目录、egam数值/误差与选定角hist descriptor。没有原event/TTree或MC simulation histogram。GRUTinizer固定[2020-06-11 commit](https://github.com/pcbend/GRUTinizer/tree/f648d7cb4fc0609f13aaad7148977f87641ecac9)，四文件hash/blob核准，只定向读BuildHits→BuildFrom→SortInts、比较器/GetIP链及相关能量定义，未通读整仓库。

科学可复用数字和边界在本页；冻结输入/下载版本/原脚本实际结果见本run的`ucgretina-eu152-input-contract.json`、`ucgretina-eu152-public-data-audit.json`、`ucgretina-eu152-ROI-cov-audit.json`与`grutinizer-point-order-counterevidence.json`。ROOT读取为实际PyROOT6.40.04，不是搜索摘要或从图猜数。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| UE12-1 | README给NSCL2012-09七quad source calibration；Fit宏实际打开run020为源、run007为room background。README一处写run022，与实际文件/代码不一致；两hist不是两次独立P/Q标定。 | dataset-identity-and-lineage | direct-README-code-data | examples/sources/eu152 README Fitting；eu152Fit.C specFileName/bgFileName | true |
| UE12-2 | 实际egam均TH1F、8000bins/0–8000、按Fit宏单位1keV/bin；run007 entries/integral=1,731,654，run020=11,249,812，under/overflow均0。bins整数非负、Sumw2N0，默认error²近N，但这不认证原event独立性或完整实验Σ。 | measured-processed-histogram | direct-data-object | run007/run020 egam ROOT object | true |
| UE12-3 | 两ROOT有227/225个keys、无TTree；有egamdc_grettheta/phi与hpos_phi_theta等lab方向TH2F，但本次keys未发现Comptonξ对象。不能因phi/theta名字就把它当偏振分析角或从这些hist提Q。 | available-observable-boundary | direct-object-inventory | run007/run020 key inventory；egamdc_grettheta/phi/hpos_phi_theta descriptors | true |
| UE12-4 | Fit代码background窗口是1800–3000，README概述“above1540”；同Rebin4/闭区间bincenters下实际Y=13836、B=30293，a=Y/B=.456739181，接近印刷fixedp0=.456734；若按1540–3000则a=.492627908。未据此改窗口追拟合或称原fullfit已复现。 | actual-count-and-source-version-crosscheck | direct-code-data-calculation | eu152Fit.C bgMinE/bgMaxE；run20/run7 egam selectedbins | true |
| UE12-5 | 声明各hist independent Poisson且高区source-free时，1800–3000比例σ_a=.00468656；若将背景模板视为exact则.00388296。两个窗口的差不按独立z检验处理，source-free假设/共享系统误差与原模板算法仍未认证。 | conditional-uncertainty | actual-count-based-design | 本页alpha公式；run20/run7 egam highregion | true |
| UE12-6 | 两预选grossROI120–128/1404–1412在4keV bins取122/126及1406/1410中心，Y/B依次1299473/50784、276090/1244。共同a下条件netcounts≈1276277.957/275521.816，Cov offdiag≈1387.571counts²、相关.00225767；非Gaussian peak area或新实测Cov。 | shared-normalization-covariance | direct-counts-and-conditional-propagation | run20/run7 egam selectedROI；本页Cov公式 | true |
| UE12-7 | eu152_gammas每个模拟event是一条primaryγ，eu152 decay宏每event是一场152Eu衰变；两者均beamOn10^6但归一分母不同。README分别预计p1≈49.3与32.1；它们不能裸当两种独立效率/P/Q校准。 | simulation-event-unit | direct-source-code | README gamma/decay normalization；eu152_gammas.mac/eu152.mac | true |
| UE12-8 | Fit模型为p0 B+p1 S×[1+tanh((E−p2)/p3)]/2；先高区拟p0、后fixp0/releasep1–3、用Fit LR。README称p2/p3 fixed却列其误差，代码实际release。未取得S模板/fitCov，不能重放fullfit、替原p1误差或把printed大χ²当匹配response证明。 | fit-procedure-and-readiness | direct-code-versus-README | eu152Fit.C fitf/firstandsecondFit；README Minuit outputs | true |
| UE12-9 | 公开InBeam sorting的偏振部分逐crystal用GetDecompE选两点，门要求gretSim存在、首simulation hit IsFEP及两索引有效；没有该段target photopeak/background/Comptonψ/θ门。它是有真值条件的模拟例，不能直接当Morse/L26实际sorting复现。 | selection-object-contract | direct-code | MakeHistosInBeam.cxx296–339 Polarization | true |
| UE12-10 | 原299–315循环在无序distinct点的32排列中16个未给真实两最大值，降序distinct控制均过；进一步追到固定GRUT BuildFrom调用SortInts，比较器按decompE降序，GetIP按此vector取值。因此normal固定链满足降序前提，不能从无序反例声称原normalproducer偏差。 | counter-evidence-and-precondition | literal-code-execution-and-upstream-source | InBeam299–315；TGretinaHit.cxx BuildFrom/SortInts；TGretinaHit.h operator< /GetInteractionPoint | true |
| UE12-11 | 严格e<e1会跳过相等最大值，如降序[5,5,3]取5/3；此为声明control，不是实测tie率，原experiment binary/reader版本未认证。ξ所用y′=n×z=−eφ、x′=y′×n=−eθ同时转π，cos2/sin2不因此单独反号；不能用这一次轴命名变化解释UC21的U差。 | residual-order-and-axis-boundary | source-and-declared-control | InBeam selection/xi axes；本页point-control边界 | true |

## Summary

这份公开数据确实允许检验实际计数、背景窗口、source-event分母及共享归一Cov；它没有提供匹配Morse/L26的Compton事件/response。一个局部selector反例在查明normal decoder排序后必须收窄，这与保存代码失败控制同等重要。

## 实际背景练习与共享误差

对前置冻结的非重叠高/低区，声明独立Poisson/source-free高区时：`a=Y/B`，`Var(a)≈a²(1/Y+1/B)`。低区gross净计数`n_i=y_i−a b_i`的一阶条件矩阵为：

`Var(n_i)≈y_i+a²b_i+b_i²Var(a)`，`Cov(n_i,n_j)≈b_i b_j Var(a)`（i≠j）。

1800–3000归一给两ROI的Cov矩阵约`matrix((1366712.087,1387.571);(1387.571,276383.501))` counts²，最小特征值约276381.736为正。固定a的对角约1310067.085/276349.512；背景规模共同误差增加的不只一个单点sigma。1540–3000对照结果另存，不将两个重叠窗口当独立数据。

这些是hist层的条件传播，不是已恢复的eventCov。Sumw2N0只说明没有保留显式sum of weights squared数组，默认sqrtN误差不是独立实验误差测量；deadtime、source drift、room background变化、continuum/峰重叠、calibration与MC有限统计仍在误差预算外。ROI120–128包含gross continuum与可能的邻峰，不能当净Gaussian峰面积。

代码[实际ROOT审计](../../system/scripts/day16_ucgretina_eu152_public_data.py)只读原文件，在内存clone后rebin；读后hash仍匹配。没有运行带rm规则的provided Makefile或未经核验的macro casts。

## Sorting主线与必要反证

SourcesSim以core energy生成能谱/对称γγ矩阵、角分布与addback；InBeam先需S800Sim及dta接受、设β/offset，偏振选择再用模拟真值条件。它的r1/r2是同一crystal的两点；该段没有使用targetOffset修正polarimeter原点，也没有已认证的实际tracking/聚类/背景合同。60CoSim另有1333门、1173/1333 γγ角相关及truth方向对照；同名source的singles与γγ条件角色不能互换。

原point loop已实际抽取编译，loop SHA256=`0b9d35e7ed642148ac6c8c185c75732af4d16001fa3974f14d6a908b5894066d`。无序反例只建立代码的前置条件依赖；上游真实SortInts是必要counter-evidence。固定版本normal路径通过的事实不能扩展为原实验所有versions/ties/修改后的cluster都通过，tie率也未由这两无TTree校准hist得到。

## Competing Interpretations and Limitations

- 2012 NSCL七quad能谱与2013保存对象、2020 GRUT及2026 UCG repo版本各有角色；不认证一个合成exact producer。
- p0中央值接近支持高区算术重放，不等于复现p1、threshold、MC模板、原likelihood/Hessian或原误差。README的χ²/NDf和超小stat error还需模型/背景/fitCov，不能以漂亮p1当response认证。
- 实验raw events/point order、Compton ξ与ψ/θ选择、polarized calibration、Q(E)、背景Cov与当前target matching响应仍缺。unpolarized source能约束几何/能谱，不能独立识别polarization sensitivity。
- 同一源校准的simulated primaryγ/decay两个处理与重复拟合不新增独立实验。两个hist也不因run号不同自动有同response或统计独立；本页所有Poisson独立计算均显著声明条件。
- 没有将source activity的长期衰减归一扩展为核能级寿命/强度课程；本批仍是Day16下的partial17知识预习。

## Knowledge Impact and Learning Decision

`supports`P/A/Q前的实际source/背景/计数单位及共享误差合同；`revises`仅看无序selector就疑为normalproducer偏差的初始担忧，normal GRUT排序是反证；`limits`将另几何source histogram或truth-gated MC例替代原Compton response。新claims均needs_review，不新增正式卡或实验δ。

## Extracted Pages

- [[ucgretina-2024-geant4-11-source-replay]]：本日另名G411/11.4.2源模拟已过小规模记录/几何控制，不等于取得本2012采集的历史MC模板；两个sourceframe宏顺序不能据名称视为同几何。
- [[compton-polarimetry]]：actual calibration输入与Q/response readiness分层。
- [[event-mixing-statistics]]：共同归一带来的条件跨ROI误差，不据更多hist认证独立数据。
- [[gretina-25na1041-polarization-response-contract]]：不迁NSCL七quad校准到当前1041响应。
- [[ucgretina-2021-polarized-emission-code]]：singleemitter有限模型与sorting/source选择是不同层。
