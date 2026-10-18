---
type: source
title: "UCGretina G411：实际源能谱构建、记录兼容与源框顺序"
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
nuclei: [152Eu, 152Sm, 152Gd]
reactions: []
experiments: []
models: [Geant4, unpolarized-source-energy-response]
methods: [fixed-source-build, native-binary-ABI, same-seed-control]
observables: [gamma-ray-energy-spectrum]
tags: [software-validation, calibration-identity, geometry, response-readiness]
---

# G411源模拟：程序退出、有效记录和实验响应分别核验

## Bibliographic Record

直接对象为UCGretina公开`geant4.11`分支的[固定2024-01-21版本](https://github.com/rileyle/UCGretina/tree/02e5a9241322f661c6918f6705cab813c691cd21)。归档16,909,304bytes，SHA256如frontmatter；724个blob（含symlink本身）全部对实际Git tree核准，构建与运行后保持。第三方源码、编译目录、几何副本和MC二进制仅在本repo的`tmp/`，raw归档槽尚未填，不改原始raw/Bib。

README关联Riley2021 DOI10.1016/j.nima.2021.165305及Morse2022 DOI10.1016/j.nima.2021.166155；本页不是两篇论文全文摄入，也未认证任一实验的actual binary。前一公开七quad数据对象另见[[ucgretina-2012-eu152-public-calibration-data]]。

## Scope and Reading Depth

本批读README的版本/build/geometry/source/output主线、GNUmakefile与source宏/输入依赖，定向沿`UCGretina.cc`初始化、`PhysicsList`、`TrackingAction`、`EventInformation`、`EventAction`输出、`PrimaryGeneratorAction`源表、`Target`与messenger的源框/Construct路径追踪。没有通读724个对象、整个Geant4或偏振实现。自有headless CMake wrapper明确记录public commit；不执行原Makefile的安装/清理，不以外层Wiki HEAD冒充第三方版本。

实际SDK为11.4.2，README说11.2.0；配置的数据包均已安装，但版本不等于历史2012/2021包。构建未启用POL、SCANNING、LHTARGET或NEUTRONS，使用原默认非偏振EM。README明确“not extensively tested”“polarized electromagnetic physics does not appear to be functional”；本页只研究无偏振源能谱。

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

- 原几何/SDK警告未被“允许继续”消除。精确reviewed warning之外的新异常、容量越界、坏truth或native解析失败都会阻止扩大模型结论。
- 源框顺序对照只针对所选公开版本和SDK；不声称历史2012采集或Morse/L26实际producer采用同样错误。preinit指针/母volume尚未就所有平台作通用修复；本run明确另命名宏recipe。
- beta/boost字段仍不认证。源能谱读coreE/timestamp，不读beta；这个子空间可继续，不据source-only instrumentation推广到in-beam偏振。
- 一γ/event的主线表没有cascade、电子与真实decay/event的全部物理。它与decay模式不是两个独立实验，sourceframe修改后相同seed也不保证逐event相同物理decay抽样。
- 本页已执行1000控制与各100000history统计；后者仍不是历史2012模板。未拟历史p1、threshold或resolution，未认证真实高区source-free、整响应或Q。

## Knowledge Impact and Learning Decision

`supports`用实际可用版本建立源能谱/finite-MC分析输入；`revises`以宏含sourceFrame或程序exit0代替有效geometry/truth核验的做法；`limits`将源能谱重放提升为偏振response认证。仍是Day16下partial17知识预习，不给Day17正式学分，所有新claims保留needs_review。

## Extracted Pages

- [[gretina-eu152-source-response-replay]]：source event单位、geometry、truth、finite-MC与实验response的分层合同。
- [[compton-polarimetry]]：无偏振能谱模拟通过仍不足以恢复Q或选择δ支。
- [[ucgretina-2012-eu152-public-calibration-data]]：历史processedhist和当前新模型的版本边界。
