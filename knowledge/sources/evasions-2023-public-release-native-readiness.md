---
type: source
title: "EVASIONS2023公开release：真实衍生事件与原版native边界"
title_original: "CFougeres/EVASIONScode v1.0.0, Zenodo8044973"
aliases: [EVASIONS2023 release readiness, EV23 native contract]
created: 2026-10-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: public-software-and-data-release
reading_depth: read
authors: [Chloé Fougères]
year: 2023
citation_key: ""
doi: 10.5281/zenodo.8044973
canonical_source: "EVASIONSv1.0.0 c6a4ff3756724d6becd17414851bc8140d00a311 Zenodo8044973"
source_url: https://doi.org/10.5281/zenodo.8044973
raw_file: raw/code/day17-20261020/EVASIONScode-v1.0.0.zip
raw_sha256: 4aae83027ed68704088d9c5b90f6dff88e06ce061943ad3aae8dcaa3f1dd8503
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [23Mg, 24Mg, 22Na]
methods: [public-data-query, Monte-Carlo-response, software-contract, lifetime]
tags: [DSAM, EVASIONS, reproducibility, covariance, readiness]
---

# 公开事件已取得，原版发布程序尚不能代替论文fit

## Bibliographic Record

[[fougeres-2023-mg23-velocity-difference-lifetime]]直接引用[Zenodo8044973](https://doi.org/10.5281/zenodo.8044973)的EVASIONS v1.0.0。实际zip15494623bytes/MD5`ee3579b86bcdf8b7d6e16d598f6b4485`，34文件CRC/sha与[Git commit c6a4ff3](https://github.com/CFougeres/EVASIONScode/tree/c6a4ff3756724d6becd17414851bc8140d00a311)逐blob匹配。当前main为`04e8fec...`，不拿它覆盖论文release。[冻结清单](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/fougeres2023-producer-source-manifest.json)。

原snapshot在`tmp/day17-fougeres2023/producer-source/`，34文件未改；native构建与客户端在另copy，原release的数据ROOT/原脚本/inputs不进Git索引。该release附GPLv3文本，所有诊断明确为本run客户端，没有把原作者源码修成我们的实验结果。

## Scope and Reading Depth

先声明已读main/CodeA/MC_sim等priming，再冻结剩余producer/native回忆；实际读README/inputs/Makefile、全部主要C++/headers、Backup提取例、单页MCalgo图、五activeSRIM header/代表行。未独立审核每一SRIM数值或原DAQ/calibration史。[actualscope](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/evasions2023-producer-reading-scope.json)。

实际查409303-entry TreeMaster全部标量范围/multiplicity和部分筛选descriptor；没有由此提取新实验寿命、branch或置信区间。原版make首次失败、补输出目录后成功；只运行无CodeA/B路径及原函数的有界组件，没有运行带未初始化长度的完整MC。

## Summary

作者公开了可读的实验标记衍生事件，readiness已有实质进展。可同时确认：公开release本身有输出按值传递、表加载/输入格式和未完成fit分支等可复现边界。它们阻止把这个发布包称为论文完整复现，却不证明论文实际生产程序/实验结果有相同错误。没有改原源码或通过补丁重造论文τ/BR。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| EV23-1 | Zenodo v1.0.0/34files完整对应Git c6a4ff3 blob，原snapshot与nativecopy原34hash均保。当前main/derivedclient不混作原paperjob。 | actual-release-identity | direct-archive-and-Git | producer-source-manifest；exercise original34/copy34 | true |
| EV23-2 | 作者README标为experimentaldata的data.root确有409303-entry TreeMaster、12branches；公开Snapshot不等全DAQ/全部PID/calibration历史，三个tree_results预置对象皆0entry/无branches。 | actual-public-data | direct-ROOT-schema | public-root-schema；README saveddata | true |
| EV23-3 | 实际nbTrack0–7，0/1/2…7分别58621/284091/55409/9481/1463/216/20/2；所查Brho/Theta/Phi/ThetaLdeg/Si字段无nonfinite。最大7低于release trackarrays31的长度，只对这份文件/当前调用读法成立。 | actual-input-range-check | direct-public-data-query | public-event-initial-ranges | true |
| EV23-4 | Si_dE>0实际7933条且均Si_theta>0，角范围约11.673–21.525°；这是衍生event选择descriptor，不是BRp分母、绝对eff或与论文全部event数闭合。 | actual-bounded-observable-query | direct-public-data-query | public-particle-selection-descriptors | true |
| EV23-5 | 原make因缺lib输出目录exit2；隔离copy只补该目录后原make exit0。编译保sizeof-array/缺return等warnings；无CodeA/B的原CLI读409303entries并“finished”后按源return1，非崩溃或完整fit成功。 | native-build-and-return-contract | direct-native | native-original-build001/002；native-noanalysis-run | true |
| EV23-6 | 原LoadSRIMFile以值传N_energy，caller sentinel−123保持；原逗号小数table在当前C locale输入后返回status1但firstEnergy999/Se0。此为原函数原输入的native事实，不是有效停止表已加载/全MC可用。 | native-original-input-failure | direct-native | Extraction_SRIM_stopping_powers.C L31–94；exercise loader_native | true |
| EV23-7 | loader声明fileSPrecoil却在slot1加载particle_in_matter，另recoil_in_matter实际header为Mg/Si而非Gold；5张表均逗号小数/keV per micron合同。正确paper阻止输入未由这些literal路径认证，不自动替表修源码。 | actual-stopping-route-boundary | direct-code-and-input | Extraction_SRIM_stopping_powers.C L13–28；SP_SRIM headers | true |
| EV23-8 | VAMOS_kinematics的betaRecoil按值传；原nativecaller .123456789保持而角数组回写。CodeA/CodeB期待caller beta更新，原路径的输出合同未闭；这不等论文实际β反演错误。 | native-output-parameter-contract | direct-native-and-code | kinematics.C L16–44；CodeA/CodeB callsites；exercise kinematics_native | true |
| EV23-9 | MCsim_kinematics也以值传BrhoMeas/Eloss，后续拟合arrays期待回传；dbeam在Nbeam外初始化且用targetµm×1000与后续Å×.0001不一致，loss_E调用把nuclear表传两次。均literal source边界，未据此重跑论文MC/估τ偏差。 | source-only-MC-contract | direct-code | MC_sim.C L11–80/L117–141/L238–268 | true |
| EV23-10 | main extraction_inputs的theta_VAMOS_max按值传，main再由SPIDER23/119.8几何改成约10.8678°；inputs gap19000µm不同于正文back-to-backfoil。默认inputs为τ5fs等，不冒原最佳拟合或paperexactsetup。 | actual-default-parameter-boundary | direct-code-and-input | inputs.dat L4/L30/L38–41；main.cpp extraction_inputs | true |
| EV23-11 | CodeB使用Si_theta却未SetBranchAddress；Si_Ep_to_Ep中薄靶分支为comparison而非assignment、角式含π/190、部分index无边界默认。只读源发现，未运行其未初始化路径或把修改后的数据当实测BR。 | source-only-particle-response-boundary | direct-code | CodeB_particle.C L42–69；kinematics.C L100–143 | true |
| EV23-12 | Tools对arrayparameter使用sizeof，当前64bit推size1，random-angle函数另缺return；原编译warnings确认。TH1 weighted/data fit helper/LL注释与论文Pearson须匹配实际job，不能从一段comment重建论文χ²。 | source-and-compiler-counter-evidence | direct-code-and-build | Tools.C L85–120；native-original-build002 | true |
| EV23-13 | release extract_width分支空/“to be added”，旧CodeA fit段在blockcomment；因此公开release不含可直接调用的完整原τ/Eχ²grid与BR量化工作流。不能codeavailable就认原grid/Cov复现，也不据缺代码认论文实验错。 | inference-producer-readiness | direct-code | main.cpp extract_width；CodeA_gamma.C/CodeB_particle.C | true |
| EV23-14 | 新脚本在fresh隔离copy复现missinglib→build成功、原noanalysisreturn1、loader/VAMOSsentinel及真实409303/7/7933query，全部hash保留；没有全MC/原fit或修公开源。 | reproducible-actual-audit | direct-native-and-public-data | exercise result/commands | true |
| EV23-15 | 后续原读作者2022thesisChapter4，明确target/catcher实测19(1)mm支持public19000µm；EV23-10与Naturebacktoback字面对照不应升级成geometry错误。原loader/scalar/native阻点仍独立保持，未因此认证exactjob/修source或重报CI。 | new-primary-revision | direct-thesis-companion | F22-2/15 | true |
| EV23-16 | 后续新ROOT固定双版本源码/native确认Chi2Test不消费LL；CodeA L42–141的LL/manual调用全在blockcomment，保EV23-13原结论，不能推paper实际调用；Tools.C原log_likelihood的o0/s0及FindBin端点边界已另组件核。 | actual-API-companion-and-boundary | direct-code-and-native | RCT26-2/8/9/11 | true |
| EV23-17 | 后续原Chapter3 Eq3.6与publicTools.C Brho_Ekin_conv原body/native同见momentum/β合同：.95Tm/M3728/A4/Z2给43.93835vs同r physicalmomentum42.92645MeV，inverse回.95仍不认证物理。paper原cal/job未知，未改release或新报能量/τ/CI。 | new-primary-and-native-physics-boundary | direct-thesis-code-native | F22-58/59/73；Tools.C L176–181 | true |
| EV23-18 | 新actualpreflight确认trackZ1范围−323.578至−108.341mm，publicinputs AGATA_shift_z=−17且main明确relative nominal shift；不把thesis绝对阵列位置−252.3再次加到已存坐标。原34source/datahash保持。 | actual-frame-contract | direct-code-and-public-data | inputs.dat parameter32；main.cpp L248–250；conditional-event-preflight | true |
| EV23-19 | 本次条件query初冻结曾把绝对位置与相对shift混同，实际selection前由preflight纠正为−17并另冻，原记录不改；这次纠正不等扫描offset强配结果，也不认证原calibration版本。 | task-failure-and-prequery-revision | execution-audit-not-physical-evidence | conditional-event-frame-revision-freeze | true |
| EV23-20 | 预定engineeringquery(Bρ>0,0≤ThetaLdeg<12°,labγ120–176°,meanβ.077/beamaxisDC)在409303条中base363176、angulartracks382017；A.2三窗L/S/U18/20/13，51不同events、无窗内多track。只为该approxquerydescriptor，不叫原keyyield。 | actual-bounded-public-data-query | direct-derived-data-query | conditional-event-result selected_records | true |
| EV23-21 | 同固定query的D=S−(L+U)/2=4.5，eventcluster二阶矩与独立trackdiag均27.75，因为51条各只一个windowtrack；fixedN中心化为27.749944。未提供实际fullCov/CI，不能由此宣称任何gate多track都无Cov或实验τ误差通过。 | actual-moments-and-statistical-boundary | data-query-and-conditional-algebra | conditional-event-result sum_event_outer_products | true |
| EV23-22 | 同queryS集合/同37.5–39.5MeV门，两Bρ表达式各3events但entry集合不同：共同132983/205708，literal独11896、momentum独124638(0-basedentry)。同计数不保证同sample；未裁哪条是物理key或改源事件。 | actual-membership-counterexample | direct-data-and-declared-kinematics | conditional-event-result same_count_gate_membership_comparison | true |
| EV23-23 | 原recoilθDS/PID/targetid/contaminationmask未match，meanβ/beamaxisquery不能当原论文selection/BR分母；51entryledger及34hash给可复现边界，未重fitτ/新实验yield/CI。 | original-selection-readiness | synthesis-with-data-contract | conditional-event-contract；F22-20/24/25/71 | true |
| EV23-24 | 新actualdata指纹：Si_dE>0的7933条Si_theta仅16值，全部match预定atan((24+.75+1.5i)/119.8),i0..15，最大残差8.47e−7deg。旧7933/范围不作新独立data，新增的是逐角occupancy与generatorrecipe相容性。 | actual-producer-fingerprint | direct-public-data-and-code | recipe-fingerprint-result actual_angle_rows；Backup/extractionData.C | true |
| EV23-25 | 反算Z集中119.8的浮点量级只反映storedrecipe，不能报独立几何survey精度/trueθresolution，也不能据此补DCT/targetshift或认证paperproducer。 | precision-and-source-dependence-boundary | inference-with-actual-fingerprint | recipe-fingerprint-result；F22-68/72 | true |
| EV23-26 | Si_theta可恢复recipeindex但不能恢复Q1–Q4/rawamplitude/完整calCov；同index四象限collapsed，不能用它补TableB.2 missingQ1strip14或唯一选gain。 | information-loss-and-calibration-readiness | direct-schema-and-recipe | Backup/extractionData.C outputbranches/Si_theta；F22-81/84 | true |
| EV23-27 | Backup源链target1–5、activeGATCONF1和Brho>0；QPL/time额外门只comment。abs(trackE−6875)>8循环只有selfassignment，不删track/改nbTrack，不能当实际γveto或原2Dcontaminationmask。该body在旧scope已读，本轮是新primary下定向复核非新来源。 | actual-archived-extraction-contract | direct-code | Backup/extractionData.C L8–15/L66–109；producer-reading-scope | true |
| EV23-28 | 原data.root实际rawtrackE在[6867,6883]keV inclusive内有26tracks/26events；仅观察能窗占用，不把它们全归28Si或从此一刀切原photopeak。原raw/code34hash不改、fullPID/θDS/mask/CI仍缺。 | actual-counter-evidence-and-boundary | direct-derived-data-query | recipe-fingerprint-result raw_track_energy_6867_to_6883_keV_inclusive | true |

## Analytical Reconstruction and Self-Audit

[执行前合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/evasions2023-before-producer.md)、[最小组件前冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/evasions2023-native-component-before.md)、[客户端](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/evasions2023-native-component.cc)、[hash/预期合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/evasions2023-exercise-contract.json)、[复算脚本](../../system/scripts/day17_evasions_release_native_contract.py)、[真实结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/evasions2023-exercise-result.json)。原source/inputs/data均不改；publicdata聚合查询与native局部调用是本任务L4边界核，不是新实验拟合。

当前系统Python没有uproot，初import失败已留档，后直接用既有PyROOT6.40.04；没有为获取data访问改变权限或凭据，也没有联系作者。readonly原输入检查和有界组件比未初始化fullMC更能定位readiness阻点，后续不靠加history填空。

## Competing Interpretations and Limitations

论文实际工作流可能用另一生产版本/配置或私有analysis；本release不能闭合该桥。需要原fit脚本/配置、参数传递正确的匹配producer或作者thesis的具体response/门定义，才可继续拟合。科学partial/readiness状态并不等实验被否定，也不阻止保留/发布可复核输入。

L4当前可做真实publicderivedevent查询、独立物理变量/响应合同审核；完整τ/BR/联合CI仍not-ready。任何修正实现应另名并声明模型变化，不能改原release后把结果称为原paperreplay。新branch独立companionFriedman2020值得原读，不能由F23引用自动补其完整response/独立性。

## Knowledge Impact and Learning Decision

`supports`公开原衍生event已取得且可读；`revises`把publicrelease当成完整可运行论文fit；`limits`literal代码故障对实际实验结论的外推。所有新claim needs_review，没有human-reviewed或新实验τ/Bp/自旋/CI。继续限于Day17原窗口的Day18知识preview。

## Extracted Pages

[[fougeres-2023-mg23-velocity-difference-lifetime]]、[[lifetime-strength-audit-165tm-136nd]]、[[doppler-shift-attenuation-method]]、[[polarimetry-shared-calibration-count-design]]。

## 作者thesis反证：19mm不是已证几何故障

[[fougeres-2022-thesis-evasions-response-contract]] F22-2/15原Chapter4明确实测19(1)mmgap，和public19000µm一致。因此EV23-10仍保“Natureback-to-back与input描述不同”的历史比较，但不能把它归为已证错误或与loader/scalar问题混加。新primary纠正了这一风险；不改原rows/review/source，也不因此认为完整paperjob已认证。

## 统计API与inactive示例的边界

[[root-2026-chi2test-option-contract]] RCT26-1–13固定6.24.06/6.40.04、原表达式native与原code34hash。LL本身静默忽略，自动UU/UW/WW依Sumw2状态；手写函数跳过o0/s0而且高端bin排除。整段示例inactive，原paperROOT/job未知，不能由当前组件推实验τ偏差或声称已经运行示例fit。

## 真实事件的条件选择与track分母

[初冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/evasions2023-conditional-event-before.md)、[原坐标预检](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/evasions2023-conditional-event-preflight.json)、[计数前frame修订](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/evasions2023-conditional-event-frame-revision-before.md)、[实际query合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/evasions2023-conditional-event-contract.json)、[membership前冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/evasions2023-conditional-event-membership-before.md)、[程序](../../system/scripts/day17_evasions_conditional_events.py)、[真实结果/51entryledger](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/evasions2023-conditional-event-result.json)。

程序先核34原文件hash，再只读Tree，array上限/GetEntry/binding与finite控制实际通过，未运行原未初始化fullMC。window采用半开[lo,hi)，原paperbin边界未知；实际datafield所代表的target/run/PID/history不从12branch补造。初绝对/相对shift误认在selection前已修并保留，不算科学观测，也不能把后来固定工程选择的20个S当paperphotoline实际计数。

此query支持计数、samplemembership与响应合同分开保存：不同表达式可给同3但换一entry，有限实际样本中cluster/track二阶矩恰同并非通用独立性定理。signed4.5只是操作结果，不附实验显著性/置信区间或跨版本keyyield裁决。

## 存储角度的生成规则指纹

[新问题前冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/evasions2023-recipe-fingerprint-before.md)、[预定recipe/float容差](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/evasions2023-recipe-fingerprint-contract.json)、[程序](../../system/scripts/day17_evasions_recipe_fingerprint.py)、[实际结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/evasions2023-recipe-fingerprint-result.json)。旧scope已读Backup，本轮只在Ch3/B新输入下对actualdata作新问题查询。初RVecOps Abs名称JIT失败exit1已留档，改用逐track std::abs，固定source/selection不变后实际exit0；无外部/Volumes路径或RECREATE执行。

不能把计算公式写回tree的离散性当独立几何精度：119.8与float一致只支持生成recipe，不能用它消除物理位置/对准/响应的不确定性。所有角度对应多个象限，缺rawcalibration仍缺；原gamma循环无veto的静态发现与26窗口占用也不替原energy-anglemask。

| recipe index | stored Si_theta deg | positive Si_dE records |
| --- | --- | --- |
| 0 | 11.672762871 | 541 |
| 1 | 12.359054565 | 625 |
| 2 | 13.041762352 | 494 |
| 3 | 13.720722198 | 602 |
| 4 | 14.395776749 | 560 |
| 5 | 15.066773415 | 548 |
| 6 | 15.733565331 | 373 |
| 7 | 16.396013260 | 564 |
| 8 | 17.053985596 | 508 |
| 9 | 17.707353592 | 519 |
| 10 | 18.355998993 | 533 |
| 11 | 18.999809265 | 494 |
| 12 | 19.638673782 | 385 |
| 13 | 20.272495270 | 564 |
| 14 | 20.901180267 | 301 |
| 15 | 21.524641037 | 322 |
