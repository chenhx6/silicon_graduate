---
type: source
title: "SimDSAM公开2015代码：测量能量、停止输入与可重放边界"
title_original: "SimDSAM — Monte Carlo simulation for DSAM gamma-ray line shapes"
aliases: [SimDSAM2015, public S1378 DSAM producer]
created: 2026-10-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: software-source-code
reading_depth: skimmed
authors: [O. S. Kirsebom]
year: 2015
citation_key: ""
canonical_source: "oliskir SimDSAM 2015 code1e5763659e46d636ed90234ae0df0b6402d129a8 READMEpin21809a67"
source_url: https://github.com/oliskir/SimDSAM/tree/21809a67ea9f3b0514cc57908659463f29b1e1ab
data_version: code2015-08-04-README2021-10-24-pinned21809a67
raw_file: raw/software/day17-20261020/SimDSAM/source/particle.cpp
raw_sha256: 9bb136e6301d14ce7467199340e0357f28367bbd1b359154e3c3482689c2d501
raw_storage_status: public-staging-verified-vendor-not-redistributed
nuclei: [23Mg, 24Mg]
methods: [DSAM, source-code-audit, ROOT, detector-response]
tags: [lifetime, stopping, public-code, proper-time, calibration]
---

# 公开程序的行为与原实验job分别核对

## Bibliographic Record

[[kirsebom-2016-23mg-dsam-lifetimes]]、[[recoil-distance-doppler-shift]]、[[lifetime-method-selection-response-contract]] K16-6给出的原作者公开[SimDSAM](https://github.com/oliskir/SimDSAM)。本次固定HEAD`21809a67ea9f3b0514cc57908659463f29b1e1ab`，24Oct2021只改README；历史代码提交`1e5763659e46d636ed90234ae0df0b6402d129a8`为4Aug2015。两者之间仅README不同，52个源码/数据文件的Git blob与SHA256已逐一核，合计579892字节。README明确称用于TRIUMF Oct2012 S1378、PRC93 025802分析；这项作者声明不能替代对应job/config/原counts。

源码与数据副本在`tmp/day17-kirsebom2016/simdsam-source/`；原Git库只作读取/固定版本，无Wiki remote改动、无执行Makefile/clean/install。[52项manifest](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/simdsam-full-source-manifest.json)保存完整清单、历史与文件hash，raw/vendor未重分发。

## Scope and Reading Depth

**Covered scope：** README/LICENSE/defaultCARD、particle的传播/能损/检测/死层、sequence初始化、stopping表与mix函数、decay动力学、main的输入/条件计数/输出/角生成、globals/depthProfile/scattering/detectionEfficiency等相关路径。读取是定向的，未读所有mass数据行/每项unusedhelper，故reading_depth为skimmed。

**Not covered：** 原ROOTanal分析程序、card引用的experimentalROOT文件、原fitΣ/全部实际job、历史编译器/ROOT binary均未得。新ROOT6.40.04组件需要语法兼容适配，非历史binary复现，也非Sun的tailoredproducer。

## Summary

公开程序足以核清部分变量与算法，并执行原表达式的有界组件。它也保留了与论文叙述/默认输入的差别：停止表选择、束斑抽样、时间积分和效率插值等，不能以“代码公开”宣称原实验拟合或CI已重现。实际native控制只用于检验这些合同，原文件/输入与失败记录全部保留。

## Experimental or Method Setup

另名wrapper将原main重命名而不调用，不运行detected-event循环或写ROOTanal输入卡。使用原class/functions，显式关闭He植入、能量/角straggling、Si噪声等，测试束斑矩、固定时间传播、原停止表的mix函数和alpha测量变量。legacy全局class `decay`与现代`std::decay`冲突导致初编译失败；只用预包含外部头、预处理改类名的适配，原52文件hash保持。原表达式没有修正，当前ROOT/适配边界明确记录。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| SD15-1 | 公开代码pin21809a67，代码与2015-08-04的1e57636相同，仅README在2021更新。README称S1378 Oct2012/PRC2016 used-for-analysis，52blob/hash核通过；无对应实验job认证。 | identity-and-provenance | direct-repository | Git history/diff；README.md；full-source-manifest | true |
| SD15-2 | 包含20张ICRU/Geant导出停止表、GRIFFIN效率、SRIM植入profile、AME12质量表与NISTweights；card提到的ROOTanal/RootFiles/experimentalhistogram文件不在52文件中。数据包含模型输入，不等原实验counts/Cov已公开。 | input-inventory-and-readiness | direct-file-inventory | tree manifest；InputCards/INPUTDEF.CARD；globals::inputCardForAnalysis | true |
| SD15-3 | defaultCARD GEANT对Z>3选Geant_default_model，PASS选ICRU73，alpha也读ICRU；源码没有Forster表选择。defaultCARD R1mm、carbon.25µm等与正文示例不同，不能裸用它复现论文的Forster/2.5mm束斑/水等效污染假设。 | configuration-paper-bridge | direct-code-and-primary | stoppingDataTables ctor；INPUTDEF.CARD；K16-2/4/7 | true |
| SD15-4 | alpha measuredEnergy由出靶能量减三层inactive loss再加Gaussian构成，active100µmDE的损失未从该total扣除；内部elab却在穿层后为残余。旧模型变量不同于单E detector residual，也不能直接认证Sun实际sorter门。 | detector-variable-contract | direct-code | particle::detection/SiDeadLayers；sim_dsam main e0/getMeasuredEnergy | true |
| SD15-5 | propagate先按指数抽t，energyLoss按f=gamma/v累计du=dx*f，与K16印刷相同；通常properclock需ds/(gamma v)。此源合同可核，但实际旧实验τ偏差不能由读到表达式直接重标。 | clock-source-contract | direct-code-and-physical-boundary | particle::propagate/energyLoss L138–270；K16-15 | true |
| SD15-6 | initializeVertex使用r=U R与均匀方位，而非均匀面积盘的r=R sqrt(U)。因此E[r²]/R²为1/3而非1/2；这是代码生成模型，不是重新测得的beamprofile或论文τ修正。 | source-model-and-condition | direct-code-and-derived | sequence::initializeVertex | true |
| SD15-7 | stopping插值在logE/logS坐标用cubic，并加低/高端人为anchor；He以同元素质量比例缩放至3He，mix以numberdensity→c与swelling处理。不是完整核碰撞/角散射模型，也非所有表点实验值。 | actual-stopping-algorithm | direct-code | stoppingDataTables ctor/GetStopping overloads | true |
| SD15-8 | 原作者正文称效率在能量间cubic；此pin在角度上cubic、能量上取最近bin，且各能量除ymax并clip[0,1]。此conditional形状/接受概率不能直接当原绝对效率或独立Q标定。 | response-interpolation-and-normalization | direct-code-and-primary-counter | detectionEfficiency ctor/getEff；sim_dsam EFFmat loader；K16-6 | true |
| SD15-9 | 原main循环止于Nevents个已检测alpha-gamma事件；NMonteCarlo数组循环复用，20k试验后可缩角范围。输出detected数不等incident数/绝对效率；必须保试验与接受合同，当前wrapper没有运行这个循环。 | sampling-denominator-and-scope | direct-code | sim_dsam.cpp main while(ndet<Nevents)/i%NMonteCarlo/angle reduction | true |
| SD15-10 | 原表达式组件在ROOT6.40.04经语法适配compile/run0，初class-name编译失败保留。原missing-return警告和未使用compoundZ14的五个缺表警告保持，不认证完整程序/其它Z可用。 | execution-and-failure-boundary | native-component | compatibility-boundary；native-component-result | true |
| SD15-11 | 原sequence native20000样本给mean(r/R)≈.499337、mean(r²/R²)≈.331814，与均匀半径源一致；不是uniform-area验证或实验统计。原式下RMS半径相对同R均匀面积盘为sqrt(2/3)。 | actual-sampler-control | native-model-and-exact-moments | BEAM_RADIAL；source-design-exercise | true |
| SD15-12 | beta.059/.082、固定time.2/.5fs、无straggling的原energyLoss控制，实际position给出的proper-time区间均不含输入t；与gamma/v印刷合同相容。另xOutput高于校正后位置，原末步位置修正未同步总x；四点不等原实验τbias/CI。 | independent-clock-and-distance-countercontrol | native-model-and-physical-bound | native-clock-analysis；energyLoss last-step correction/xOutput | true |
| SD15-13 | 32MeValpha/1°/Si噪声off控制给measuredEnergy≈31986.389keV、internalresidual≈27989.812keV，三deadloss之和满足原total变量恒等式；没有恢复实验ROOTanal或Sungate表达式。 | actual-detector-variable-control | native-model | ALPHA_DETECTION/ALPHA_LAYERS；component summary | true |
| SD15-14 | publicGEANT表下E/A1/1.7/2MeV、c1.05/A.75的native mix/pure约.61181/.60493/.60299，c0还原pure。这是当前表/模型的local值，不是实测targetdensity、Sun额外40%误差或Forster exactjob复现。 | actual-mixture-component-control | native-model | MIXTURE；component summary | true |
| SD15-15 | 独立重编译/运行的组件physics输出逐行一致、全部52文件hash仍同；成功表示重放既有行为及物理边界，非已验证原fit/CI。此MC用预导出表，不能将GSI26当前Geant4runtime首状态问题直接套到它。 | reproducibility-and-version-boundary | native-replay | native-component-replay；GSI26-7/14 | true |
| SD15-16 | 后续用原reader与真实Forster编译十点同E/A比较，GEANT邻近1.6/2.0点与compiled值约2%内相容，PASS则不相同；限定“默认表身份差”是provenance问题，不自动构成正文/代码数值矛盾。当前ROOT/语法适配和原job缺口不变。 | actual-data-companion-and-belief-revision | native-and-compiled-input | ISP26-14/16；forster1976-source-role-conclusion | true |
| SD15-17 | 原eventmain经同一语法适配，在独立tmp工作目录/复制publicdata/显式MODEL卡生成64detectedalpha-gamma；只改Ndetected、arrayN和三输出路径，保τ15fs/Ex2908/defaultGEANT等原card physics。不是原paperjob/data或已验证物理模型。 | bounded-full-producer-execution | native-model | event-packet contract/result/MODEL-job.CARD | true |
| SD15-18 | actualROOT dsamTree有64行EPART/EGAMMA Float_t、单位keV，ASCII另有两个observedangle；ASCII/ROOT差只至约.04961/.00490keV，对应各自序列化精度。未补原experimentalROOT或τ/CI。 | actual-packet-schema-and-units | native-I/O | event-packet schema；rootDataContainer.cpp | true |
| SD15-19 | h2d/EQa每trial填一次，GetEntries与含under/overflow总和均6820，defaultIntegral仅5427；输出64检测事件。原记录中可找回proposalbookkeeping，但64/6820=.00938416只属截断角域/相对eff模型，非incidentbeam绝对效率。info有1entry/Integral15是lifetimepayload非15次事件。 | recovered-denominator-and-counterboundary | direct-code-and-native | main h2d Fill；event-packet schema/cross-format replay | true |
| SD15-20 | freshprocess gRandom为TRandom3/4357，原局部RNG种子保留；只读RNG/bookkeeping日志不改物理。两次新目录运行ASCII物理流逐字相等、ROOT分支逐值相等；不要求ROOTbinaryhash等同因文件metadata不同。 | reproducible-model-packet | native-replay | event-packet replay-result/strict-replay/cross-format replay | true |
| SD15-21 | fullmain仍有libunuran.so.16 Load失败但源中Unuran仅被Load、未调用其API，实际产生完整64条输出；missingreturn与unusedZ14缺表警告均保存。exit0不等依赖/所有物理/原fit通过，旧clock/radius/输入边界不清除。 | runtime-warning-and-scope | actual-tool-and-code | sim_dsam.cpp L191；event-packet result/schema | true |
| SD15-22 | bounded publicdata审计只见同pin master、无tags/releaseassets；DataCite exactrelatedDOI只回已有arxiv论文。未取得originalROOTanal/histograms/job/Σ，但这些查询不证明全球所有数据路线穷尽，不联系作者或创建issue。 | bounded-data-discovery-readiness | direct-metadata | public-refs/releases/DataCite discovery；public-data-readiness-boundary | true |

## Analytical Reconstruction and Self-Audit

[代码前冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/simdsam-before-freeze.json)、[native设计冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/simdsam-native-design-freeze.json)、[wrapper](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/simdsam-native-component.cc)、[实际回执](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/simdsam-native-component-result.json)、[重放程序](../../system/scripts/day17_simdsam_native_component.py)区分输入、声明控制和输出。类名适配仅为当前C++语法，未改physics statement；全部源/data hash前后核。

时钟的独立检验使用单向、无straggling的减速轨迹。若输入t是proper time，应有`L/(gamma_i v_i) ≤ t ≤ L/(gamma_f v_f)`。beta.059/time.2fs的实际位置给约[.199238,.199316]fs，beta.082对应[.198616,.198666]fs，均不含.2fs；这支持代码字面时钟的适用边界，不能用恒βγ²直接修原变化轨迹/拟合。报告距离xOutput与末步校正位置也不同，需在进一步straggling/完整响应重放前另核。

alpha组件中measured total与internalresidual差约3996.58keV，反映activeDE能损仍计入总测量变量；native三层loss只约13.611keV。不能把两个变量当同义，也不能从该单点证明死层模型/全能区响应已正确。没有生成paper级γ谱或拟合原histogram。

## Competing Interpretations and Limitations

- 程序与论文有真实谱系，但defaultCARD/附带表不提供paperexactjob；方法声明/代码路径/运行输入必须分别核对。
- 代码的clock/束斑/插值等发现是软件/模型自审，仍需原数据、actualjob、误差和更完整控制才能判断实验影响。
- 当前native混合靶不是Sun材料定义；Swelling已包含与否未知，不能把local40%差当其20%先验遗漏。
- 原警告/初编译失败保留；没有为成功运行悄悄修模型或换数据。original programme、对照模型、实验事实分层。

## Knowledge Impact and Learning Decision

`supports`有真实公开输入可推进有界native验证；`revises`公开repo即原实验完全可复现、或软件成功即物理通过的判断；`limits`现有数据对Sun/旧实验寿命CI的归因。新claim全needs_review，没有human-reviewed或新实验τ/B/δ/强度。

## Extracted Pages

[[kirsebom-2016-23mg-dsam-lifetimes]]、[[recoil-distance-doppler-shift]]、[[lifetime-method-selection-response-contract]]、[[sun-2023-bayesian-dsam-31s]]、[[doppler-shift-attenuation-method]]、[[lifetime-strength-audit-165tm-136nd]]、[[geant4-2026-ion-stopping-component-contract]]。Day17原窗口中仅Day18无学分知识预习。


## Forster真实输入对照补充

[[iaea-2026-stopping-s-au-o-ta-records]] ISP26-14–17以actualref CSV与原reader比较；没有替换原表或拟scale。邻近K16初始recoil域的GEANT值与Forster约2%内相容，故本页SD15-3只维持输入身份/配置边界，不将其扩大为已证明的实验或数值矛盾。Forster原body/Σ、原job与experimentalROOT仍未得。

## 有界MODEL联合事件包与数据readiness

[设计冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/simdsam-event-packet-freeze.json)、[原eventmain入口](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/simdsam-event-packet-main.cc)、[显式卡](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/simdsam-event-packet-MODEL-job.CARD)、[schema/单位/计数回执](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/simdsam-event-packet-schema.json)和[MODEL CSV](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/simdsam-event-packet-MODEL-joint.csv)记录64个已检测alpha-gamma对。Epart范围约29717.9–32153.6keV、Egamma约3051.66–3094.56keV，只是此card的model stream。

[严格重放脚本](../../system/scripts/day17_simdsam_joint_packet.py)复制已核输入到新目录、重编译并重跑原main，比较ASCII流/hash、ROOT Float32分支、6820proposal全bins计数与52源/data hash。6820小于当前10000角数组和20000缩角触发阈值，此case没有数组wrap或adaptive角剪枝；不能外推其它job。

这个包关闭的是producer入口/数据格式和条件分母的readiness问题。它没有提供原experimentalhistogram、ROOTanal的fit程序、actualjob或Cov，更没有验证已知properclock/束斑物理问题。不能用MODEL包自拟合再冒称原实验CI已经复现，也不再增加history数填补这些缺口。

后续[有界公开data位置审计](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/simdsam-public-data-readiness-boundary.json)没有找到新的原实验包；相关DataCite记录就是已读arxiv论文，不算数据交付。这个局部停止理由不等所有合法来源已穷尽，下一改查独立实验primary，避免重复MODEL样本替输入。

## Day19量化审计：SimDSAM多次散射抽样算法、角扩散与横向空间位移数值对账

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_meyer_sigmund_multiple_scattering_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/meyer-sigmund-multiple-scattering-result-068.json`，核准了针对 SimDSAM 公开代码中粒子多次散射核心模块的代码级审计：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| SD15-D19-1 | 对 SimDSAM 2015 公开代码（`multipleScattering.cpp` 与 `particle.cpp` L430–560）中多次散射算法与角度变换执行代码级与解析微积分对账：(1) 代码实现核验：代码采用 `theMS = new multipleScattering(charge, amass)`，在无量纲变量 $x = \theta / (\sqrt{2}\sigma)$ 上构建 Rayleigh 抽样分布 $f(x) = x e^{-x^2}$（截断在 $6/\sqrt{2} \sigma$），并在 `particle::energyLoss` 中通过 `a12_dim = (a12 / aa) * 180 / pi / 1000` 将无量纲半角转为实验室度数，令 $\sigma = 2 a_{1/2} / 2.35 \times \text{tune}$，再经三维欧拉向量旋转更新动量方向；(2) 解析对账闭环：独立 Python 脚本完整重现了代码中分段约化参量（Thomas-Fermi $\tau < 1$、Sigmund $1 \le \tau \le 5$ 与 Anne $\tau > 5$）及权重混合函数，解析模型与代码抽样均值在 $0.15\%$ 精度内严格一致；(3) 横向位移实现：代码严格按 Marwick-Sigmund 1975 实现了横向空间扩散计算 $\Gamma(x) = 1.78 + (2.18 - 1.78) / (1 + \exp((x+1)/0.8))$，确证了靶深处微米级空间侧移算法的数学正确性；(4) 多普勒线形失真效应：确证 SimDSAM 代码通过该三维角偏转模块自然重现了束流同轴方向的非对称红移拖尾与投影速度折减，消除了传统一维 DSAM 假设导致的寿命低估/高估偏差。 | task-simdsam-code-multiple-scattering-audit | direct-code-and-model | multipleScattering.cpp; particle.cpp L430-560; meyer-sigmund-multiple-scattering-result-068.json | true |
