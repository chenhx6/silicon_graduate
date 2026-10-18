---
type: source
title: "UCGretina G411：源能谱、角关联与记录/几何合同"
aliases: [UCGretina G411 source replay, Eu152 Geant4 11 compatibility]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: software-code
reading_depth: read
title_original: "UCGretina — geant4.11 branch"
authors: [L. A. Riley, UCGretina contributors]
year: 2024
data_version: "public02e5a9241322f661c6918f6705cab813c691cd21; installedGeant4 11.4.2; source-only recording overlays explicitly separate"
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "fixed public G411 code, official Geant4 headers, and declared source-history controls"
source_url: "https://github.com/rileyle/UCGretina/tree/02e5a9241322f661c6918f6705cab813c691cd21"
raw_file: "raw/data/gpt/day16-20261018/ucgretina-g411-02e5a924.tar.gz"
raw_sha256: "0a8b686fd54aab33542b76f2b599696a40e6e2b9301dde2053472bd7e7dc5024"
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [152Eu, 152Sm, 152Gd, 60Co, 60Ni]
reactions: []
experiments: []
models: [Geant4, unpolarized-source-energy-response, gamma-gamma-angular-correlation]
methods: [fixed-source-build, native-binary-ABI, same-seed-control]
observables: [gamma-ray-energy-spectrum, gamma-gamma-angular-correlation]
tags: [software-validation, calibration-identity, geometry, response-readiness]
---

# G411源模拟：程序退出、有效记录和实验响应分别核验

## Bibliographic Record

直接对象为UCGretina公开`geant4.11`分支的[固定2024-01-21版本](https://github.com/rileyle/UCGretina/tree/02e5a9241322f661c6918f6705cab813c691cd21)。归档16,909,304bytes，SHA256如frontmatter；724个blob（含symlink本身）全部对实际Git tree核准，构建与运行后保持。第三方源码、编译目录、几何副本和MC二进制仅在本repo的`tmp/`，raw归档槽尚未填，不改原始raw/Bib。

README关联Riley2021 DOI10.1016/j.nima.2021.165305及Morse2022 DOI10.1016/j.nima.2021.166155；本页不是两篇论文全文摄入，也未认证任一实验的actual binary。前一公开七quad数据对象另见[[ucgretina-2012-eu152-public-calibration-data]]；Riley2021原件已随后另读于[[riley-2021-ucgretina-energy-response]]，该文十二quad/有效层验证不直接认证本页SDK/七quad模型。

## Scope and Reading Depth

本批读README的版本/build/geometry/source/output主线、GNUmakefile与source宏/输入依赖，定向沿`UCGretina.cc`初始化、`PhysicsList`、`TrackingAction`、`EventInformation`、`EventAction`输出、`PrimaryGeneratorAction`源表、`Target`与messenger的源框/Construct路径追踪。没有通读724个对象、整个Geant4或偏振实现。自有headless CMake wrapper明确记录public commit；不执行原Makefile的安装/清理，不以外层Wiki HEAD冒充第三方版本。

实际SDK为11.4.2，README说11.2.0；配置的数据包均已安装，但版本不等于历史2012/2021包。构建未启用POL、SCANNING、LHTARGET或NEUTRONS，使用原默认非偏振EM。README明确“not extensively tested”“polarized electromagnetic physics does not appear to be functional”；本页研究关闭polarized EM的源能谱与native核γγ角关联，不认证Compton Q。

两个官方[11.4.2头文件](https://github.com/Geant4/geant4/tree/v11.4.2/source/processes/hadronic/models/radioactive_decay/include)已HTTP200取得，与安装副本逐字节相同：`G4Radioactivation.hh` SHA256=`1c164b2b68cb557975964e3c3b8076844de0c944c685e9f515f2c3409454c718`，`G4RadioactiveDecay.hh` SHA256=`7ffc97f3141a64deac3de6194a454c2b76edcee4bf203c18a07feceac090765a`。安装metadata不是核结构实验事实，实际接口正文才支撑以下兼容判断。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| UG24-1 | 固定G411分支README称未广泛测试、POL/偏振EM不可用；本run用11.4.2成功构建无POL源程序，不据编译成功认证偏振响应。 | version-and-scope | direct-code-and-build | README Compile and install lines5–9；固定build contract | true |
| UG24-2 | 原γ宏每event一条primary photon，Eu152表最大1408.022keV；decay宏以静止152Eu为primary、停用Reaction并由RadioactiveDecay处理。两个event分母不能互换。 | simulation-source-identity | direct-source-code | PrimaryGeneratorAction.cc SetSourceEu152 lines334–395；eu152.mac source/Reaction commands | true |
| UG24-3 | 原TrackingAction只接收名为Radioactivation的decay creator；实际11.4.2的G4Radioactivation是G4RadioactiveDecay别名，后者默认名RadioactiveDecay。原1000衰变运行程序exit0、349条CRYS，但1000条G4SIM的num全0，不能按程序exit0认可truth。 | runtime-interface-failure | direct-code-header-and-execution | TrackingAction.cc40；G4Radioactivation.hh31；G4RadioactiveDecay.hh74；原decay audit | true |
| UG24-4 | 仅兼容两个process名后，原AddEmittedGamma仍按匹配核态beta索引i写photon槽并递增光子数；实际1000event出现26个零能truth槽。这个索引对象不同于连续photon index，原失败留存。 | distinct-index-failure | direct-code-and-execution | EventInformation.cc AddEmittedGamma lines23–39；name-only v3 decay audit | true |
| UG24-5 | 另名source-only副本按实际合格callback连续追加E/位置/方向，并对40槽容量设Fatal guard；没有补造缺失光子，未修改原724blob。它没有通用修复每光子的beta/boost，禁止当in-beam或Q patch。 | limited-instrumentation | declared-code-overlay | source-truth-append patches；TrackingAction与EventInformation两个overlay | true |
| UG24-6 | 本机编译实际GEB.hh得到header16、CRYS464、IP24/offset80；原G4SIM292，HIGHMULT40时1132，EG28/offset12。只解码有效prefix，忽略trig_time、unused IP tail、padding及未认证beta。 | binary-format-contract | native-compiler-and-decoder | GEB.hh CRYS_IPS/G4SIM_EGS；EventAction.cc638–661/811–840 | true |
| UG24-7 | 1000event/seeds20261019,152001的γ原宏得到183条晶体记录/160个探测history；seeds20261019,152002的decay原宏得349/270。source-append副本的truth能量均正且有限、无容量/IP能量求和异常，实际decoder均exit0。 | conditional-simulation-result | executed-source-model | v4 gamma/decay GEB audits | true |
| UG24-8 | 原程序与source-append在上述两组相同种子下，全部183/349条已初始化CRYS字段逐位相同。只证明所选history的能量/有效点记录未变；未将未初始化字节、beta或其它种子纳入不变结论。 | same-seed-counter-control | executed-binary-field-comparison | source-append gamma/decay CRYS invariance；EventAction writeDecomp | true |
| UG24-9 | 原γ宏在runinitialize之后设置sourceFrame，原decay宏在之前。Target::setSourceFrame立即delete旧Target_phys并向expHall_log放frame/tape，而expHall_log在Target::Construct才赋值；不能把命令接受等同源框已进入当前world。 | geometry-order-contract | direct-code | eu152_gammas.mac/ eu152.mac sourceFrame placement；Target.cc26–28/132–155 | true |
| UG24-10 | 同种子单event tracking实测：原decay顺序primary Eu152初始volume为Target、无有效POLYETHYLENE；只将源框移到initialize后，初始volume变euTape且材料列为used。两个trace均程序/包装器exit0；证明本版本环境存在实际几何差别，不等于几何全部验证。 | geometry-navigation-counterexample | actual-track-and-material-log | sourceframe trace pre/post primary initStep；registered couples POLYETHYLENE | true |
| UG24-11 | 新命名postinitialize-frame recipe的1000衰变history产生367条CRYS/287个探测history，decoder通过；与原349/270不再要求逐条不变，因为几何改变，后续随机数消耗亦改变。不是独立效率测量或paired显著性检验。 | controlled-model-recipe | actual-source-simulation | sourceframe-smoke-006 GEB audit | true |
| UG24-12 | 六个GeomMgt1001警告来自CConvexPolyhedron缺BoundingLimits；自有CalculateExtent有finite vertex/voxel路径，但尚未证明全几何无bias。decay的PART102/He1发生于停用的默认reaction kinematics，最终primary明确Eu152；警告逐块保留，仅放行精确reviewed模式。 | residual-failure-boundary | direct-code-and-run-log | CConvexPolyhedron CalculateExtent；smoke exception blocks；Outgoing_Beam default/update | true |
| UG24-13 | 两组1000history模型的120–128/1404–1412keV singles依次为27/5与38/14；跨区H12为0/3，固定N总数crossCov为−.135135/+2.470470counts²。相同推导在一γ与完整decay下可有不同符号，不是实验Cov或两个独立Q校准。 | finite-MC-covariance | actual-history-calculation | source-cov-1k gamma/decay region_H_sum_ccT/region_cov_total_fixedN | true |
| UG24-14 | 两组1000history在1540–1800及1800–3000都无hit；零观测只给该模型history-hit概率的单侧95%上限1−.05^(1/1000)=.00299125，不能作实测source-free证明或直接当mean-count上限。 | finite-sample-boundary | declared-binomial-model | source-cov-1k zero-hit probability bound | true |
| UG24-15 | 新种子各100000history实际run/native/history检查均exit0；γ/decay有20431/32976条CRYS、17576/26257个探测history，低区singles为2364/555与3611/850，H12=0/38、fixedN总数Cov12=−13.120331/+7.306573counts²。 | finite-MC-source-result | actual-model-histories | source-cov-100k gamma/decay regional statistics | true |
| UG24-16 | 100k模型γ的1540–1800/1800–3000计数0/0，decay为3/0；后一高区零观测给history-hit概率单侧95%上限2.9956874×10^-5，仅限该模型。它没有证明真实数据高区无source或恢复旧alpha/fitCov。 | source-window-counterexample | actual-model-counts-and-binomial-bound | source-cov-100k regional highcounts/zero-hit bound | true |
| UG24-17 | 三个decay高区history为52586/60023/81372，coreE1647.3406/1643.4116/1608.4141keV；中间history的两记录γ1299.1331+344.2786与core在3.06×10^-5keV内闭合，core大于任一单γ。支持保留sum-in竞争解释，未以能量相符替代逐track归属。 | identified-history-energy-closure | direct-valid-binary-fields | highregion-history-audit history60023；GEB timestamp600230000 | true |
| UG24-18 | 当前两shape的asolid行按holeL/thickB/thickC/capS/capT/thickO解析，得到coax1.5/back2.5/outer.9mm，usePassive默认true；与Riley2021 Table2 II数值相同。仅这个tuple相同不能认证十二quad原实验/材料/producer，100k输入未被改写。 | actual-geometry-input-crosswalk | fixed-file-parser-and-source-table | G120C4solid.list9/21；geometry_description34–37；Gretina_Array.cc359–365 | true |
| UG24-19 | co60/iso宏使用native AngularCorrelations true/false，同时SetGammaPolarization false且binary无POL；实际co60几何symlink是NSCLstd12quads/48crystals，与Eu例七quad分开。源无sourceFrame，不能直接充R21/LaBr或L25实际reference。 | source-control-identity | direct-macro-code-input | co60/co60.mac/iso.mac；aeuler12行；PhysicsList.cc439–445 | true |
| UG24-20 | 固定Ni60level文件给2505.753(4)→1332.514(2)的1173.239keV、MP407/δ−.0025，按实际G4编码为E2/M3；1332.514(2)→0是MP4/pureE2。这是本模型输入，不是新测的实验δ。 | multipole-order-and-input | direct-level-file-and-SDK | z28.a60.lvldata level4→1与level1→0；G4GammaTransition SampleDirection | true |
| UG24-21 | 原sorting未在填emitted_delta前确认两目标γ都存在，缺失时−1占位仍进入dot/len²/len²；合法unit方向时该式才退化为cos。实际1k corr/iso各1/6history缺完整pair，本分析显式排除并保存literal无效值，不把非平坦占位谱当物理角关联。 | selection-precondition-and-control | literal-code-and-actual-histories | MakeHistos60CoSim.cxx truth-loop；smoke pair analysis missing-pair rows | true |
| UG24-22 | native crmat.LINUX与固定GRUT crmat.dat对12quad的48矩阵，索引转换及cm→mm后R最大差2.96×10^-8、translation差1.22×10^-5mm；native最高deposit点往返误差约.0012mm。只核静态文件/数值，不认证实际GRUTSYS/binary或PSA分辨率。 | coordinate-and-unit-crosscheck | fixed-public-matrix-and-native-fields | EventAction.cc450–487；TGretina CrystalToGlobal/SetCRMAT；crmat-crosscheck | true |
| UG24-23 | 两组1000Co60history实际程序/native检查0，CRYS773/712、探测history518/481，全部48crystal出现；truth有效前缀正finite、无容量/能量求和异常。原六GeomMgt1001保留，完整几何/Q未认证。 | source-model-bookkeeping | actual-simulation | co60-smoke-run/native corr/iso results | true |
| UG24-24 | 1k完整unique emitted pairs999/994；声明无smearing/rawcore双门detector pairs仅7/4，10bins中7个iso denominator为0。源moment a2为.13998±.07327/.09773±.07094；这些误差不支持精确detector W、a4或Q，ratio一阶Cov不是exact CI。 | finite-MC-statistical-boundary | actual-history-analysis | co60-gate-smoke-analysis-result emitted_moments/coarse bins | true |
| UG24-25 | 声明unpolarized4→2→0 joint-amplitude模型及nativeδ−.0025给a2=.1005293099、a4=.00940581308；RBδ+.0025配套operator phase后同observable。pureE2给5/49、4/441；与实际G4 F/F3公式收缩差≤1.48×10^-15，不从此拟实验δ或认证完整MC。 | phase-and-conditional-theory | independent-amplitude-and-source-algebra | 本页joint-cascade模型；G4PolarizationTransition F/F3/daughter update；theory/F3 results | true |
| UG24-26 | 原生GammaTransition仅在gamma/discrete、核correlation flag及spin限制满足时用核ρ采样方向；PhotonEvaporation从CorrelatedGamma设这个flag并在RDM中保存/移除核tensor。这个核状态传播与polarized EM消费光子Stokes分开；本Co60无POL控制不给Compton Q。 | state-and-observable-contract | official11.4.2-code | G4GammaTransition SampleTransition/SampleDirection；G4PhotonEvaporation Initialise/EmittedFragment | true |
| UG24-27 | 原Co60 sorting的max_layer在晶体循环外初始化并累计；对实际1k rawbank顺序，corr/iso的per-crystal back记录为103/78、prefix为123/89、whole-event类为166/126，reverse顺序改变48/35个history的标签。只是已定义输入上的选择对象反证，不是原R21实验back fraction或normalGRUT顺序偏差认证。 | selection-object-and-order-boundary | actual-history-literal-predicate | MakeHistos60CoSim max_layer/energy_involves_phi；backflag-result actualhistory witnesses | true |
| UG24-28 | 新seed各100000Co60history run/native/angle分析均0：完整truth pairs99840/99845，a2=.105902±.007183/.006829±.007092、a4=.007674±.009631/.008455±.009514。前者与预定mixed point、后者与0的条件2D moment比较均相容；支持局部source开关控制，不据此唯一分辨tinyM3/相位或认证全producer。 | source-model-control-and-uncertainty | actual-MC-moments | co60-100k gate-analysis emitted_moments；moment-comparison | true |
| UG24-29 | 相同100k数据的rawcore detector pairs507/549；10个iso bins均非零、最小39，比值SE约.135–.245。矩阵/Cov/求和/hash/无IP截断检查通过，但不是原README10^7精度、实验W或Q标定；source图与detector图保留不同population/分母。 | response-statistical-readiness | actual-named-detector-recipe | co60-100k-gate-analysis detector counts/ratioCov；control figure source CSV | true |
| UG24-30 | 声明unpolarized4→2→0、point gate不分析reference helicity的完整joint-photon模型，pureE2 first/last的P_parallel相同（全13角最大差2.09×10^-16），90°均1/6。角色不同本身不保证这个理想极限的physical P不同，仍不许可跨实际能量/响应迁Q。 | conditional-joint-cascade-design | declared-amplitude-calculation | 本页point-gate joint density；conditional-stokes-v2 pureE2 rows | true |
| UG24-31 | 实际level配置MP407/nativeδ−.0025的同point模型在90°给P_first=.1652824009、P_last=.1643540933，scalarW两角色差≤4.45×10^-16；native→RB连同算符转换后IQUV0差。它是固定输入forward量，不是MC photon Stokes、实测P或δ重拟合。 | conditional-mixing-and-role | declared-physical-model | conditional-stokes-v2 actualmixed rows/control_residuals | true |
| UG24-32 | 同pureP=1/6、自由静止电子/Comptonψ90°、nominal1173.239/1332.514keV的point contrast为.0641180/.0577730；小M3配置为.0635855/.0569714。不同E即使同P也有不同KN分析能力；这些数不叫array Q或L25标定复现。 | conditional-analyser-design | stated-Klein-Nishina-model | conditional-stokes contract KNconditionaldesign；90° rows | true |
| UG24-33 | pureE2模型对x=cosθγγ给W=5(24+3x²+x⁴)/126、P_parallel=(1−x²)(4−x²)/(24+3x²+x⁴)，与joint两角色/13角到3.34×10^-16相符。若直接平均局部W P得19/189，正确在共同目标轴积分全部reference方向却给Stokes≈0；不能用局部偏振幅度均值代全局observable。 | closed-form-and-axis-average-control | analytic-and-joint-density-calculation | 本页pure闭式；closedform-script-result；ungated controls | true |
| UG24-34 | 130个完整joint-density配置显式Hermitian/PSD/trace检查通过；native/RB、pureM3全局号、Rz、独立intermediate-density路线残差≤8.89×10^-16。固定target轴时参考面旋转使Q_J+iU_J按e^(2iφ)变换，12控制残差≤9.74×10^-17；Q_J是Stokes分量，不是polarimeterQ。 | mathematical-failure-controls | explicit-density-and-symmetry-validation | conditional-stokes-v2 jointPSD/spin2/control_residuals | true |

## Summary

真实源码、SDK和二进制已把“不能运行”推进为一个有明确版本、原失败和几何对照的源能谱模型。它也暴露了程序exit0会掩盖的记录/几何问题。这个结果没有恢复历史MC模板、原拟合Cov、Compton Q或实验δ。

## 可复现入口与数值对照

冻结合同和结果位于`outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/`，主要为`ucgretina-g411-source-tree-verification.json`、`source-truth-append-build-contract/result`、`GEB-decode-contract-v4-*`、`v4-*-GEB-audit`、`sourceframe-trace-contract/result/audit`、`sourceframe-GEB-audit`（文件均有前缀`ucgretina-g411-`）。精确overlay差异持久化于`ucgretina-g411-source-truth-append-patches.json`；第三方原文件不覆盖。

| 运行对象 | history数 | CRYS数 | 探测history | truth状态 |
| --- | --- | --- | --- | --- |
| 原γ宏＋source-append | 1000 | 183 | 160 | 一条γ/event；检查通过 |
| 原decay宏、原binary | 1000 | 349 | 270 | 所有num0；失败保留 |
| 原decay宏、仅process名兼容 | 1000 | 349 | 270 | 26个zero-E槽；失败保留 |
| 原decay宏＋source-append | 1000 | 349 | 270 | 有效能量/方向检查通过 |
| postinitialize源框＋source-append | 1000 | 367 | 287 | 检查通过；另名几何recipe |

γ/decay原宏的有效IP和core求和最大差分别约9.92×10^-5/1.48×10^-4keV；均远小于事前门`.05keV+10^-5 E`。这些是浮点bookkeeping检查，不是实测能量分辨率。单光子history检查deposit不超过emitted E；decay含电子/核反冲，不将仅γ真值和当总初始能量守恒测试。

代码入口：[构建](../../system/scripts/day16_ucgretina_g411_build.py)、[宏执行](../../system/scripts/day16_ucgretina_g411_smoke.py)、[native解码](../../system/scripts/day16_ucgretina_geb_decode.py)、[有效CRYS比较](../../system/scripts/day16_ucgretina_core_invariance.py)。同种子比较排除的字节由原writeDecomp初始化语句核定，不能直接比较整个文件SHA来证明物理输出相同。

[history统计脚本](../../system/scripts/day16_ucgretina_source_spectrum_cov.py)在相同四个事前能区实际执行，8000个1keV bins与完整history向量的计数逐项闭合，fixedN矩阵PSD。moment公式与NumPy样本协方差乘N最大差分别约7.11×10^-15/2.13×10^-14counts²；原二进制读后hash不变。decay有一个bin在同history含多次singles，Hdiag比裸counts多2，不能只从hist entries断言所有统计量是独立Poisson。

### 100000history：高区与有限MC检查

两组新seed分别为`20261019 152101/152102`，macro/输入/四区/无能量smearing或fit均事前冻结；run约319.48/380.66s。二进制分别124,606,880/130,628,480bytes，SHA256=`1e88a205b634b38d6d559c0c4f5673781cc8c115950107957963323cd8f942c8`与`0b1a691814bf986860b4d68aa6e315316e1ea66239197ffc21038e138a48eb40`。原source724blob再次核无mismatch。

| 模型（各N100000） | 120–128 | 1404–1412 | 1540–1800 | 1800–3000 |
| --- | --- | --- | --- | --- |
| 单primaryγ | 2364 | 555 | 0 | 0 |
| 完整decay＋postinit frame | 3611 | 850 | 3 | 0 |

各区均为keV半开区间、原始core singles，非净Gaussian峰面积。fixedN矩阵PSD，moment与NumPy Cov路线残差分别约1.82×10^-12/1.41×10^-11counts²；under/overflow0，未探测history82424/73743包含在N内。两个低区H12为0/38，因此Cov12在fixedN下为−13.120331/+7.306573，在Poisson化history数下为0/38；不能混用两种条件化后比较误差大小。

decay高区三条记录的actual emitted energies和timestamp已保存，单γlist没有这些弱高能/级联路径；其中一个history与两γ之和闭合。此例只是当前源模型的source-window反证，不估真实实验污染比例，不从3个counts作精确rate fit。1800–3000的零插件方差也不等于真实源率已知为0。

## Competing Interpretations and Limitations

### 60Co控制例的实际读取范围

另沿固定Co60例完整读README、co60/iso宏、angCorr.C、两Makefile和source.set；source.res/threshold各108记录以值集合核，Ni60level文件只读与source可达级联有关的前50行（全文件hash固定），未声称精读373个高激发level。MakeHistos60CoSim完整约490行已读；README提及的co60_gammas.mac在此版本未提供。未运行带rm规则的Makefile、GRUT/GrROOT；source.set九detector映射也不代实际十二quad输入。

官方11.4.2的GammaTransition/PolarizationTransition主线和PhotonEvaporation的correlation/transition路径定向核准，三文件实际HTTP200/hash另存`co60-sdk-transition-source-discovery.json`。GRUT第五份matrix文件已对Git tree blob核准，原四代码文件不改。

source真值只在唯一1171–1175与1331–1334keV光子均存在时入角谱；detector另名recipe使用未smear core能量的1168–1178/1328–1337双门，最高deposit IP经producer自己的crmat转回公共坐标。原例另外的1327.5–1337.5 raw gate、反复Gaussian measuredE和runtime矩阵/threshold没有被此recipe重放。角γγ的cosθ不是Compton ξ。

### 级联相位与pure控制

模型取第一光子方向为z并对未观测helicity求和，从unpolarized Ji4得到intermediate J2的PSD布居，再计算第二E2光子。native amplitudes含`(−1)^L A_L h_EM(λ)`；RB基去掉该L相位并对相邻E2/M3使用`δ_RB=−δ_native`，两套表达连同算符一起转换。实际输入给中间m=−2…2布居约(.159318,.221987,.237390,.221987,.159318)。

pureE2极限a2=5/49、a4=4/441；actual mixed给.1005293099/.00940581308。若只抄同符号δ到RB而不换operator，会得到.1035476991/.00873505993；这是一项错误约定控制，不是另一个物理解。忽略核反冲、point/source/rest-frame及未包含detector response的假设均明示。

将官方F/F3源码在初态P00=1、第一光子沿z收缩，得到`a_k=(−1)^k F_second(k) F3_first(k,k,0)/F3_first(0,0,0)`。独立CG/helicity trace与有理数/Wigner9j源码表达式闭合到1.48×10^-15；不是把同一程序两次运行计为独立实验。代码：[cascade theory](../../system/scripts/day16_co60_cascade_theory.py)、[F3 crosscheck](../../system/scripts/day16_co60_g4f3_crosscheck.py)、[native gate audit](../../system/scripts/day16_co60_gate_audit.py)。

各100000history的corr/iso run/新seed/门与moment-Cov设计事前冻结，现已实际完成。run约549.21/646.01s，76667/76330条CRYS、50920/50888个探测history，无IP截断/坏truth/新异常；原六geometry警告保留。完整truth pairs99840/99845，余160/155history按冻结能窗规则排除；不是把每个event的num2当成目标pair。

corr的source a2/a4为.105902±.007183/.007674±.009631，iso为.006829±.007092/.008455±.009514。同history moment Cov进入预定2D Gaussian比较，对mixed理论/iso0的D²约.6023/1.7086（χ²df2 tail近似.740/.426）。这些是条件MC近似相容性，不是实验CI；a4与微小M3/错误相位曲线的差未被该N唯一分辨。

source-level效应与detector角响应分开：[实际控制图](../../outputs/learning-daily/20261018-DAY16-dco-rdco-mixing-ratio-convention-run-01/co60-control-figure/co60-control.svg)及CSV/PDF/PNG保留全部冻结bins/不确定度。source归一用完整pair N，detector ratio用所有generated N，后者507/549pairs、10bins的iso最小39，SE约.135–.245。图为当前无polarized EM/未smear rawcore模型；没有将零/小误差强补、拟Q或重放原GRUT。README所称约10^7events的detector W精度未被本诊断宣称复现。

back-slice选择另有实际控制：[backflag脚本](../../system/scripts/day16_co60_backflag_audit.py)仅重放原max_layer的布尔predicate，segment0–35和无IP截断先核；没有smear或选择FEP。nativebank每晶体的`b_j`、prefix `B_j=OR_(k≤j)b_k`和whole-event `OR_all b`给不同数目，原代码在循环中使用prefix。倒序同一history保留了全部能量/IP却改变一部分prefix标签，证明这三种观察对象不能互换。尚未核原论文actual sorting/denominator及runtime晶体顺序，不以这个控制解释R21图5/10的量级或重算效率。

- 原几何/SDK警告未被“允许继续”消除。精确reviewed warning之外的新异常、容量越界、坏truth或native解析失败都会阻止扩大模型结论。
- 源框顺序对照只针对所选公开版本和SDK；不声称历史2012采集或Morse/L26实际producer采用同样错误。preinit指针/母volume尚未就所有平台作通用修复；本run明确另命名宏recipe。
- beta/boost字段仍不认证。源能谱读coreE/timestamp，不读beta；这个子空间可继续，不据source-only instrumentation推广到in-beam偏振。
- 一γ/event的主线表没有cascade、电子与真实decay/event的全部物理。它与decay模式不是两个独立实验，sourceframe修改后相同seed也不保证逐event相同物理decay抽样。
- 本页已执行1000控制与各100000history统计；后者仍不是历史2012模板。未拟历史p1、threshold或resolution，未认证真实高区source-free、整响应或Q。

## Knowledge Impact and Learning Decision

### Point gate的first/last偏振：存在相同极限，不能替实际response

本批把两光子振幅写成`A_(λ1λ2,Mi)=Σ_m H2_(λ2,0m) H1_(λ1,mMi)`，对unpolarized Mi平均成4×4联合光子密度矩阵，再对reference helicity作partial trace。两target角色只改变哪个方向固定为reference z，级联顺序始终4→2→0；不是把first transition的spin/order反过来。reference partial trace假设偏振等效率的identity tag；真实tagger不主动分析偏振也未必具有这个response。Jones轴与Q_J/U_J/V_J定义见冻结合同，不以同字母δ或Q猜转换。

pureE2在这组明确假设下对first/last确有相同P；actual小M3给轻微差别。pureM3上极限控制则在90°给first P≈+.303030、last≈−.333333，整体振幅号±不改observable；这是另一个理论limit而非对Co60的物理赋值。source态、multipole/phase、门角色、reference选择和能量响应都须保存，不能概括成“角色互换总相同”或“总不同”。

纯模型的解析式令`x=cos θγγ`、`Q_J=I_parallel−I_perp`：

`W(x)=5(24+3x²+x⁴)/126`，`Q_J(x)=5(1−x²)(4−x²)/126`，`P_parallel=Q_J/W`。

由此P90=1/6、P60=45/397，积分W dx=2。将每个不同reference面的正局部P直接以W平均会得19/189≈.1005291；真正无gate的reference全立体角平均必须先把密度矩阵转到共同目标轴，得I=1、Q_J/U_J/V_J≤1.75×10^-16。固定target z时，reference方位φ旋转给`Q_J+iU_J=e^(2iφ)(Q_J+iU_J)_0`，这正是标量平均漏掉的信息。

自由电子KN point例使用`Σ_KN=sin²ψ/(r+1/r−sin²ψ)`、`r=1/[1+E(1−cosψ)/(m_ec²)]`及`A_point=Σ_KN P_parallel`。只比较单个散射点的理想分析能力，不提供detector Q、finite gate、photopeak切选或其它论文幅度归一。collinear γγ时reference plane标undefined，不报告相对该plane的harmonic。

脚本：[joint Stokes](../../system/scripts/day16_co60_conditional_stokes.py)、[纯闭式](../../system/scripts/day16_co60_closedform.py)。v1/v2结果与v1源码snapshot保留；v2增加显式完整joint PSD及reference面spin2检查，没有更改level输入。此前100k MC关闭polarized EM，未参与生成这些photon Stokes值。

`supports`用实际可用版本建立源能谱/finite-MC分析输入；`revises`以宏含sourceFrame或程序exit0代替有效geometry/truth核验的做法；`limits`将源能谱重放提升为偏振response认证。仍是Day16下partial17知识预习，不给Day17正式学分，所有新claims保留needs_review。

## Extracted Pages

- [[co60-gate-role-response-benchmark]]：实际target/gate、δ多极子顺序、角关联/偏振响应及有限MC比较对象。
- [[gretina-eu152-source-response-replay]]：source event单位、geometry、truth、finite-MC与实验response的分层合同。
- [[compton-polarimetry]]：无偏振能谱模拟通过仍不足以恢复Q或选择δ支。
- [[ucgretina-2012-eu152-public-calibration-data]]：历史processedhist和当前新模型的版本边界。
