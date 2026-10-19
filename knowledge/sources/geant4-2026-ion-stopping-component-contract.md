---
type: source
title: "Geant4 11.4.2离子阻止：模型选择、实际组件与首次查询边界"
title_original: "Geant4 v11.4.2 ion stopping call paths and native SDK component"
aliases: [Geant4 stopping component 2026, G4 stopping contract]
created: 2026-10-19
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: software-source-code
reading_depth: skimmed
authors: [Geant4 Collaboration]
year: 2026
citation_key: ""
canonical_source: "Geant4 v11.4.2 ion stopping source and installed SDK component"
source_url: https://github.com/Geant4/geant4/tree/v11.4.2
data_version: v11.4.2-G4EMLOW8.8
raw_file: raw/software/day17-20261019/G4EmStandardPhysics_option4.cc
raw_sha256: 04337300cc119a4fd893d515059cc75cef9f042849b183848643a4c4bf104c89
raw_storage_status: public-staging-verified-vendor-not-redistributed
nuclei: [31S, 32S, 15O, 16O, 17O, 18O]
methods: [Geant4, stopping-power, native-component, source-code-audit]
tags: [DSAM-input, stopping, model-selection, reproducibility]
---

# 同一个Geant4版本也须记录实际模型与查询合同

## Bibliographic Record

公开[Geant4 v11.4.2](https://github.com/Geant4/geant4/tree/v11.4.2)，`git ls-remote`解析tag object为`1a99784d3bf92d3e0c86437f3609daa4d6d60059`、peeled commit为`8cc04f65977807f1848da7b958c421cd5e162f26`。源码经实际raw URL取得并逐文件SHA256记录；初错误standard模块路径404、tree API403都保留，没有凭据修改或原样重试。安装SDK实际`geant4-config --version`为11.4.2、运行banner为12Jun2026；它不是Sun论文私有构建的身份认证，也没有从tag/hash证明安装二进制完全同源。

[来源下载清单](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/geant4-stopping-source-downloads.json)及002–005后续清单保存真实路径/hash，`G4IonParametrisedLossModel`在lowenergy，`G4IonStoppingData`在materials，`G4IonICRU73Data`在standard模块。原下载错误文件保持404内容，成功路径另名缓存，没有覆盖失败记录。

## Scope and Reading Depth

**Covered scope：** 来源前冻结已知Sun/IAEA/Bethge和Day16SDK priming；定向读physics constructor的generic-ion选择、ionisation初始化、ICRU数据装载/能量与单位、Lindhard/ParamICRU73局部损失和step修正、calculator查模/电子量、run初始化调用链。实际执行新native组件与只插诊断语句的单独源副本；两张G4EMLOW8.8表各53行核。详[actual scope](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/geant4-stopping-code-scope.json)。

**Not covered：** 没有读完整Geant4源码/物理手册，若干Bragg文件仅取得未全读，故reading_depth保留skimmed。无Sun实际physics list/version/config、事件或后验；无SchürmannSRIM2006原producer；没有做电子/核完整transport、速度投影或实验寿命拟合。

## Experimental or Method Setup

新fixture只建Au/Ta及vacuum world，已有SDK/数据只读调用；所有build、temporary和输出在Wiki内，无系统安装。三种独立进程配置为`standard`、`option4`、option4非空name触发的`external`。初始化必须到RunInitialization建physics tables后才可查询；没有生成事件。63条真实编译实验输入按各行同位素、`Etotal=A×(E/A)`与NIST纯材料查询，另3条声明的31S/15O诊断输入；不是原implantation/完整材料响应。

电子查询使用`G4EmCalculator::ComputeElectronicDEDX`，先DBL_MAX cut三次，再1keV cut三次；六值全部保留。输出除材料density转为MeV/(mg/cm²)，未加入核阻止。1µm production range cut与查询的delta-electron energy cut分别记录，不把它们混作相同参数。

## Summary

本次实际执行显示，版本名称不足以唯一指定离子阻止模型，查询还需给出表、能量、cut与初始化/调用合同。新的模型比较及首次range建表诊断都属于声明的组件结果，不能替代Sun实际实验producer、完整DSAM速度历史或误差模型。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| GSI26-1 | 公开v11.4.2源码/tag与实际SDK11.4.2、G4EMLOW8.8身份记录；不是Sun privateproducer，也未证明安装binary与所取源码逐位同构。 | identity-and-version-boundary | direct-code-and-runtime | tag identity；SDK component commands/version | true |
| GSI26-2 | defaultstandard genericion用ionIonisation默认Bragg/BetheBloch；option4默认装LindhardSorensen，只有非空name令fUseExternalDEDX=true才装ParamICRU73。实际MODEL记录三者分别Bragg/LindhardSorensen/ParamICRU73。 | actual-model-selection | direct-code-and-native | G4ionIonisation::InitialiseEnergyLossProcess；option4 ctor/ConstructProcess/header | true |
| GSI26-3 | option4设置UseICRU90Data与MaxNIELEnergy1MeV，standard本次为false/0；核阻止的注册开关与电子ComputeElectronicDEDX对象不同。ICRU90特殊靶/数据选择不是所有材料无条件换表。 | process-and-data-role | direct-code-and-native | option4 ctor；G4EmStandardPhysics::ConstructProcess；G4IonICRU73Data::Initialise | true |
| GSI26-4 | 本次实际ICRU73表z16_79/z8_73各53点、原文件域.025–1000MeV；Lindhard辅助G4IonICRU73Data重采样.025–2.5、低于.025用sqrt缩放。API传入的是其定义的scaled energy，不能把总E、E/A与proton-mass-scaled energy无声等同。 | table-domain-and-unit-contract | direct-code-and-data | G4IonICRU73Data ctor/GetDEDX/ReadElementData；actual dataset identities | true |
| GSI26-5 | ComputeElectronicDEDX经ComputeDEDX，离子会调用CorrectionsAlongStep，内部长度1nm；不能直接用模型裸ComputeDEDXPerVolume代整个calculator或重复加step修正。DBL_MAX与1keV cut三次重复/单位/同位素都实际记录。 | API-and-observable-contract | direct-code-and-native | G4EmCalculator ctor/ComputeDEDX/ComputeElectronicDEDX | true |
| GSI26-6 | 三模式各66输入均完成，第二/三次稳定且稳定restricted≤total。Wr1979两点的编译值/组件比，standard约.922–.935、option4约.496–.546、external约.498–.548；只是指定组件/编译对象比较，无原独立σ/先验拟合或Sun错误认定。 | conditional-component-comparison | task-native-calculation | geant4-stopping-comparison-summary Wr1979 | true |
| GSI26-7 | external下15O/Ta声明低能点Etotal.0213543MeV首次total≈.0144161、随后≈.1501867MeV/(mg/cm²)，同输入重复定位首次query transient；standard/option4此控制稳定。初值不当物理cut依赖/实验数据。 | reproducible-component-countercontrol | direct-native-component | repeat-order probes；parsed queries row1001 | true |
| GSI26-8 | 仅加诊断输出的原源副本重现native数值：首次range构建使chargeSquareRatio从≈6.14324变64，末尾q2/chargeSquareRatio给≈.0959881抑制；缓存range后的重复不变。strict-context/hash重放一致，SDK/原文件未改。只定位本API/版本/声明输入的路径，不归因为Sun实际实验CI或transport普遍失效。 | traced-source-mechanism-and-scope | diagnostic-model-and-native | ParamICRU73::CorrectionsAlongStep/BuildRangeVector；param trace conclusion/replay | true |
| GSI26-9 | 初fixture仅Initialize后查询在FindEmModel崩溃−11，gdb与RunManagerKernel定位缺RunInitialization的BuildPhysicsTables；补client生命周期后原三配置回归0。另trace重放初缺patch工具，改严格Python上下文应用，不安装系统包；失败记录保留。 | failure-control-and-reproducibility | actual-tool-evidence | initial-segv/gdb/root-cause；param-replay-initial-failure | true |
| GSI26-10 | 原63编译行、当前模型/源码、条件组件和诊断插桩四层分开；actualSunmodel/材料/事件/Σ仍缺，不能由成功组件或数据/模型比值建立新的spGaussianprior、F(τ)、τ/B/CI。 | readiness-and-independence | evidence-boundary | SUN23-6；ISP26-5/9；component contract | true |
| GSI26-11 | 后续原读nativeAlongStep路径：PostStepGPIL按track更新material/model/q²，DoIt显式SetCurrentCouple、用真实step与productioncut再调用CorrectionsAlongStep，随后fluctuation/energybalance；故API1nm观测必须另核native，不能直接泛化。 | native-callpath-and-counter-boundary | direct-code | G4VEnergyLossProcess::PostStepGetPhysicalInteractionLength/AlongStepDoIt；G4VEmModel::ChargeSquareRatio | true |
| GSI26-12 | 新native控制为纯Ta内15O初21.354261keV、seed13579，external/option4各.1/1nm步长，lossfluctuations/nuclearoff，2events各记录前2steps再人为kill。四次运行exit0，step确由StepLimiter定且逐步pre−post−deposit残差<10⁻¹⁶MeV；不是完整track/实际实验。 | actual-controlled-transport-model | native-model | geant4-alongstep-native-result/summary | true |
| GSI26-13 | external两步长均首event首stepdeposit/次event同起点首step≈.09598809169；option4两者均1。原native与仅插诊断的副本NATIVE_STEP逐值相同，证实此声明控制中的first-state差异，不认普遍实验bias或统计置信度。 | native-first-state-countercontrol | native-and-diagnostic-model | geant4-alongstep-native-summary；trace/qtrace | true |
| GSI26-14 | .1nm未触发range积分，native first UpdateDEDXCache却在15000MeV过渡计算调用GetChargeSquareRatio，把先前local6.14324改64，末尾q2/denominator抑制能损；1nm另含range路径。此前API的range归因仍有效，但不能当全部首次状态问题的唯一原因。 | expanded-source-mechanism-and-revision | traced-code-and-model | UpdateDEDXCache；CorrectionsAlongStep；geant4-alongstep-qtrace | true |
| GSI26-15 | strict-context/hash脚本重建native与两诊断副本、完整步骤及trace一致；未patch安装SDK/原publicfile。rawpre/postcharge字段保留，不把它直接平方当model有效q²。缺真实Sun配置、target/track/Σ，所以仍不计算原τ/CI偏差。 | reproducibility-and-inference-boundary | native-replay-and-readiness | geant4-alongstep-replay；reading-scope/inference-boundary | true |

## Analytical Reconstruction and Self-Audit

[组件程序](../../system/scripts/day17_geant4_stopping_component.py)、[C++ fixture](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/geant4-stopping-fixture.cc)、[合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/geant4-stopping-component-contract.json)、[完整命令/输出](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/geant4-stopping-component-result.json)与[parsed queries](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/geant4-stopping-parsed-queries.json)保留原63行及新增声明控制。不同模式对完整能区有不同表/过渡/修正，不能按两个低点的比值设constant scale。

软件初假设也要反证：calculator确实调用step correction，故已否决“漏掉修正”的直觉。低能异常经同输入重复、不同配置控制与diagnostics-only源副本定位，未给SDK打补丁；[trace脚本](../../system/scripts/day17_geant4_stopping_trace.py)严格匹配原hash和diff上下文、实际编译运行/数值trace一致。仅instrumentation的ELF符号替代不是独立实现或实验。初次查询的范围建表会改变模型内部状态，不能静默warmup后把失败抹去。

## Competing Interpretations and Limitations

- 组件值取决于physics constructor、表版本、能量映射、query cut和局部step语义。当前比较没有提供实验误差的联合概率模型或新独立标定。
- IAEA/SRIM/ICRU表可能共享历史测量；未核训练谱系，不称这些模型为独立数据。
- 纯Au/Ta、无碰撞事件的查询不处理implant profile、nuclear angular straggling、feeding或实际geometry，无法给DSAM投影历史/新寿命。
- low-energy firstquery问题属于已声明API/路径，actualtransport调用顺序、Sun所用版本/模型和数据未知，不从此推实验偏差。

## Knowledge Impact and Learning Decision

`supports`把“Geant4 stopping”展开为可核的模型/表/API合同；`revises`把版本名当唯一曲线、把首次返回值当稳定物理量；`limits`无actualproducer时模型比值对实验先验/CI的作用。所有新claim保持needs_review，未设human-reviewed，Day18仍无学分。

## Extracted Pages

[[iaea-2026-stopping-s-au-o-ta-records]]、[[bethge-1966-heavy-ion-stopping-charge-states]]、[[sun-2023-bayesian-dsam-31s]]、[[doppler-shift-attenuation-method]]、[[lifetime-strength-audit-165tm-136nd]]。

## 从API观测到native AlongStep的定向核验

后续[来源前冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/geant4-alongstep-before-freeze.json)、[设计冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/geant4-alongstep-design-freeze.json)明确不能预填API→transport迁移。实际读native调用链后才执行[原生fixture](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/geant4-alongstep-fixture.cc)，[步骤摘要](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/geant4-alongstep-native-summary.json)保留两种模型/步长与人为终止剩余能量边界。[重放脚本](../../system/scripts/day17_geant4_alongstep_control.py)对native和两诊断副本验证原输出一致。

具体deposit：external .1nm首event首step约2.40793459×10⁻⁶MeV，次event对应2.50857637×10⁻⁵MeV；1nm分别2.40086283×10⁻⁵与2.50120904×10⁻⁴MeV。option4在对应两个事件相同。这些是声明软件模型数值，不是实测停止本领或meanlifetime。能量账本逐步闭合并不消除内部状态差异，后者由[qtrace](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/geant4-alongstep-qtrace.json)定位到首次高能过渡cache的q²覆盖；短步无需range构建便能出现，收窄此前只强调range的解释。

没有把这几个step积分成完整slowing轨迹、F(τ)或实验响应，没有替Sun选择版本/physicslist或估计其后验偏差。下一若要问影响范围，须分别改变声明模型的初能/材料/step/cut/history，并保留首次与稳定状态；那仍是模型适用域研究，不能兑换原实验数据与Σ。
