---
type: source
title: "GRSISort固定Compton偏振代码：事件混合、归一与输入消费边界"
title_original: "GRSISort ComptonPolarimetryHelper and Compton analysis utilities"
aliases: [GRSISort Compton polarimetry, GRIFFIN Compton helper]
created: 2026-10-19
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: software-code
reading_depth: read
authors: [GRIFFIN Collaboration contributors]
year: 2026
data_version: "GRSISort6bd3c617cf212158da80918594ba9623fb4137c2; GRSIData54dfb1d244593a48820142ee20232a12cc959d50"
citation_key: ""
citation_key_status: no-unique-local-BibTeX-entry
canonical_source: "GRIFFINCollaboration/GRSISort selected pinned files and targeted GRSIData API"
source_url: "https://github.com/GRIFFINCollaboration/GRSISort/tree/6bd3c617cf212158da80918594ba9623fb4137c2"
raw_file: "raw/software-reference/day17-20261019/GRSISort-ComptonPolarimetryHelper-72015fa7.cxx"
raw_sha256: "feeabebf67987b60ca3a8b169feea976870a7ba2d9ec1e482999056a792301be"
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: []
reactions: []
experiments: []
models: [Compton-polarimetry, event-mixing]
observables: [gamma-ray-linear-polarization, asymmetry, polarization-sensitivity]
methods: [fixed-code-component-execution, response-readiness]
tags: [GRIFFIN, software-validation, polarimetry, covariance]
---

# GRSISort：公开偏振producer的实际选择与消费端合同

## Bibliographic Record

本页对象是公开软件，不是新增论文或实验。GRSISort固定commit为[6bd3c617cf212158da80918594ba9623fb4137c2](https://github.com/GRIFFINCollaboration/GRSISort/tree/6bd3c617cf212158da80918594ba9623fb4137c2)，公开LICENSE为MIT（Copyright2024 GRIFFIN）。公开metadata/commit/tree和各blob均实际HTTP200，Git blob SHA-1与SHA-256双核；本次查询tree未截断。GRSIData另固定[54dfb1d244593a48820142ee20232a12cc959d50](https://github.com/GRIFFINCollaboration/GRSIData/tree/54dfb1d244593a48820142ee20232a12cc959d50)，它是所查依赖API的版本，不是已构建两repo完整组合的认证。

原件缓存位于repo内`tmp/day17-grsisort/`，raw归档槽尚未填；本任务不修改raw。source原始URL/pin/hash已核，不以缺归档槽冒称缺失来源身份。精确获取清单见[download manifest](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/grsisort-pinned-download.json)与[GRSIData manifest](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/grsidata-pinned-download.json)。本repo固定tree没有`.root`文件，不能据此声称全世界无公开数据；本轮未取得配套真实event/matrix/calibration/Σ。

## Scope and Reading Depth

完整读所选`examples/ComptonPolarimetryHelper.cxx`199行、`.hh`114行、`util/AnalyzeComptonMatrices.cxx`343行、`LeanAnalyzeComptonMatrices.cxx`575行、`Compton_Scale_Plot.cxx`90行及README35行/LICENSE21行。定向读CMakeLists的utility target与GRSIData FetchContent，TDetector.h/cxx的AddHit/GetHit/Copy，GRSIData TGriffin的GetGriffinHit/AddFragment/FixCrossTalk与TGriffinHit.h的ArrayNumber。未通读两个repo，未做全量build、真实data重放或历史2016/2017 calibration认证。

[组件程序](../../system/scripts/day17_grsisort_component_audit.py)抽取原样Exec body、time/energy predicates、Polarization/KCoeff函数与误差表达式，保留源文件哈希；仅在外层提供声明的hit/settings/histogram sink，链接实际ROOT6.40.04/MathMore/TVector3/TH1D/TGraphErrors。编译和执行均actualexit0，原selected expressions未patch。它不等于完整helper constructor/RDF、真实detectorgeometry、analysis TTree、deadtime或experimental response。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| GRS26-1 | 固定helper以same-clover不同晶体双hit的energy sum匹配一门，再要求另一clover的第三hit匹配另一门；默认1170–1176/1329–1335keV均严格开区间。pair要求E1≥E2并检查g1-g2与g1-g3 prompt；不是clover裸N⊥/N∥。 | code-selection-contract | direct-code | Helper.cxx99–156；Helper.hh14–25/46–66 | true |
| GRS26-2 | ξ由n1=v3×v1、n2=v1×v2两法向夹角构造，θ为γγ方向角；保存crystal/detector两种θ矩阵及逐crystal诊断。BGO参数虽传入，所读Exec没有使用它做suppression；字段/参数存在不证明已进入选择。 | code-observable-and-input-consumption | direct-code | Helper.cxx99–162；Helper.hh101–107 | true |
| GRS26-3 | 每slot以10个empty event初始化，混合使用当前双hit与历史event第三hit；历史循环仍比较g1/g2与历史g3的list index。原样Exec组件在同一历史hit multiset仅改变有效hit的index0/1/2时mixed entries为0/0/1，prompt均1；这是局部index依赖，非原数据偏差估计。 | mixed-reference-contract | actual-component-and-code | Helper.cxx5–9/165–198；grsisort-component-result MIX | true |
| GRS26-4 | targeted API中TDetector::AddHit为push_back，TGriffin::GetGriffinHit返回Hits().at(i)并先做cross-talk，FixCrossTalk改energy未排序；这些路径未提供跨event共享hit身份。ArrayNumber明定1–64，而geometry枚举one为0–63，相关exclusion输入需核其basis。未认证完整DAQ/event-order分布。 | hit-identity-and-index-boundary | direct-code | TDetector.h60–63；TGriffin.cxx241–259/295–328/441–461；TGriffinHit.h63–64；Helper.cxx66–78/103–110 | true |
| GRS26-5 | 新Analyze消费端读取F.Jf.Jx但b与a′仍使用F.Ji.Jx；原函数组件中仅把second table换零，输出仍.04439854。明确pureE2 point oracle用同source comment Co60两表得.16662554；这是函数依赖/输入合同控制，不是新Co60偏振测量。 | coefficient-consumption-control | actual-component-and-code | AnalyzeComptonMatrices.cxx304–332；LeanAnalyzeComptonMatrices.cxx406–409/517–521；grsisort-component-result POL | true |
| GRS26-6 | 必要反证：所查CMake UTIL_NAMES包含LeanAnalyzeComptonMatrices而不含AnalyzeComptonMatrices；Lean的B/a′确实使用F_JfJx。因此GRS26-5不能扩成“默认GRSISort或历史所有实验都用了错误P”；还需真实producer/执行命令/版本。 | build-version-and-counter-evidence | direct-code | CMakeLists.txt341–345；LeanAnalyzeComptonMatrices.cxx513–521 | true |
| GRS26-7 | Analyze以A=1−(n/N)/(m/M)作归一ratio，却将point error乘A而非ratio；null设计n=m100/N=M1000时实际ROOT组件保存σ=0，而独立Poisson-bin并含自身total的局部σ=.134164。真实mixed-reuse/fitΣ仍未知，不能沿用此设计误差替实验。 | normalized-count-error-boundary | actual-component-and-derivation | AnalyzeComptonMatrices.cxx190–206/220–249；grsisort-component-result ERROR | true |
| GRS26-8 | Analyze grouped积分使用两端FindBin且ROOT Integral包含两端；真实ROOT180-bin/0–180.000001°控制使相邻[0,2]/[2,3]均计2个单位bin，重复边界bin2；ungrouped循环bin<nbins省最后bin。当前grouped点不自动互斥/独立，实际hist/fit影响未重放。 | bin-selection-and-covariance-contract | actual-ROOT-and-code | AnalyzeComptonMatrices.cxx194/210–249；grsisort-component-result BINS | true |
| GRS26-9 | 预测曲线采用.5 Q P cos2ξ。新Analyze中measured/used Q energy被读取/校验但该body未将它们代入缩放；旧Lean另有ScaleQ均匀θ平均的KN sensitivity ratio及硬编码Q备注。备注数值不代独立校准，半因子/能量权重须随具体observable。 | response-normalization-and-version-boundary | direct-code | AnalyzeComptonMatrices.cxx24–28/91–143/260–275；LeanAnalyzeComptonMatrices.cxx72–80/111/550–575；Compton_Scale_Plot.cxx43–90 | true |
| GRS26-10 | 本轮固定tree无ROOT数据；获得的是选定代码和组件运行，没有实际TTree/矩阵、逐台calibration/gate/response或Σ，也未编译完整GRSISort/GRSIData。它不能恢复ST99/SG98、A≈130或其它论文的actualproducer。 | data-readiness-and-source-independence | direct-discovery-and-audit | pinned repository tree；download manifests；本页Scope；component scope | true |
| GRS26-11 | 原样完整Compton_Scale_Plot编译/运行0，固定Q=.2509/energyUsed1332时打印100keV .111820、3000keV .445044；函数角色适配器确认循环调用ScaleQ(E,1332)是ScaleQ(1332,E)的倒数。按同函数的calibration→target角色后者应给.562967/.141449；旧Lean使用正向角色。仅核参数/版本合同，不修实际实验Q(E)。 | full-program-energy-role-control | actual-unmodified-program | Compton_Scale_Plot.cxx43–59/71–90；LeanAnalyzeComptonMatrices.cxx74–77/101；grsisort-q-energy-result | true |
| GRS26-12 | ScaleQ平均的是单次KN sensitivity的均匀θ积分，而非KN截面×dΩ事件权重或真实阵列response。本任务另积分核E→0时三者point90=1、uniformθ=√2−1、KN×dΩ=1/2；是归一/权重反例，不将任何一个当实测clover Q或随意删除.5因子。 | response-weighting-and-limit-boundary | source-code-and-task-derivation | Compton_Scale_Plot.cxx71–90；本页能量角色与平均核；grsisort-q-energy-result analytic limits | true |
| GRS26-13 | 新helper的xiThetaDet/Cry/Mixed/Count keys与默认Lean读取的六个XiHist2D_* legacy keys不同。完整Lean源在仅追加batch entry的原样body执行中，设计new-key fixture实际exit139且无四目标graphs；同内容legacy-key正控制exit0并输出graphs。匹配schema是运行/统计合同，不可仅同repo便串联两版本。 | full-consumer-schema-failure-control | actual-original-body-and-ROOT-fixture | Helper.cxx11–28；LeanAnalyzeComptonMatrices.cxx141–184；grsisort-lean-schema-result | true |

## Summary

公开producer确实补上了“Compton双hit–第三γ–ξ/θ–event mixing–归一ratio–cos2 fit”的实际代码入口。它同时说明：有几何表、BGO对象、参考F向量或Q能量参数，不代表这些输入已被消费到目标观测。必须区分新的helper/Analyze路径、CMake默认Lean目标与历史采集。

这与[[starosta-1999-pdco-experimental-test]]和[[schmid-1998-gammasphere-polarization]]的实际计数合同不同；不能将其Q、A和half-factor裸换。[[polarimetry-shared-calibration-count-design]]承接matching weight/Σ与本页公开producer的缺口，[[compton-polarimetry]]/[[linear-polarization-asymmetry]]保存使用门。

## 条件组件的实际数值与反证

输入[component-input](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/grsisort-component-input.json)在执行前保存。两Co60 coefficient vectors取旧Lean comment，mixing1/2均声明为0、L2=2、θ=90°；原新Analyze函数P=.04439854156，改变F.Jf.Jx为全零仍相同。独立pureE2点核为

\[
P_{90}=\frac{\frac32 F_{1,2}F_{2,2}+\frac58F_{1,4}F_{2,4}}
{1-\frac12F_{1,2}F_{2,2}+\frac38F_{1,4}F_{2,4}}
=.16662553865.
\]

数值与精确1/6的末位差源于chosen印刷coefficient小数，未用于新拟合MR。旧Lean B/a′使用second table，是必须同记的版本反证；其active默认模板与comment也不能自动视为用户真实cascade输入。这里没有修补第三方代码或宣称另一通用版本已经认证。

归一ratio令R=(n/N)/(m/M)、A=1−R。在**两组独立Poisson bins、每个total包含本bin**的声明极限，

\[
\operatorname{Var}(A)\simeq R^2\left(\frac1n-\frac1N+\frac1m-\frac1M\right).
\]

它在A=0时一般仍正。源表达式的A乘数使本设计σ=0，真实ROOT TGraphErrors GetErrorY也为0；不能由此直接断言真实fit偏了多少。共有norm、mixed partner复用、边界bin重叠和共同events会产生更完整Σ；独立bin式也不是通用替代品。

Exec组件用declared hits、固定单元几何与histogram counters，历史valid1332-keV hit依次置于同一history multiset的index0/1/2，mixed entries=0/0/1，prompt=1/1/1。只是对跨event的list-index veto作不变量控制；targeted API没有能量排序这一自动消除机制，但真实输入的event packing、fragment时间序、slot分配、spectra和偏差仍未恢复。不可把它写成真实experiment failed。

## Competing Interpretations and Limitations

### 能量角色与平均核

未改动的完整`Compton_Scale_Plot.cxx`/原Globals.h以实际ROOT编译执行，而非只重写Python输出。原main打印(.111820,.151032,.445044)对应E=(100,500,3000)keV，默认常量Q=.2509、energyUsed=1332。原ScaleQ函数comment与实际返回值定义为calibration E1→target E2的平均sensitivity之比；main循环却传(E,1332)。保持函数不变的include适配器在(1332,E)给scale(2.2437904,1.6612401,.5637648)，因此正向角色缩放应为(.5629670,.4168051,.1414486)。1332→1332两者都为1，单能量自校验不能发现角色反转。

这是相对于函数自身角色字典和固定1332参考的程序行为，**不是**实测clover Q(E)被更正。旧Lean main在line101传(energyMeasured,energyUsed)，保留与独立plot调用的版本/用途区别。原program、include-adapter、binary/hash、输出与独立积分见[完整结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/grsisort-q-energy-result.json)和[可复算脚本](../../system/scripts/day17_grsisort_q_energy_audit.py)。

定义r=E′/E=[1+(E/m_ec²)(1−cosθ)]⁻¹、B=r+1/r−sin²θ，原sensitivity为Σ=sin²θ/B。源码用1000等θ点平均Σ。独立Simpson积分核同一uniformθ结果相合；另一个**明确声明的自由电子单次散射/全接受模型**则按r²Bsinθ加权，得到〈Σ〉_KN=∫r²sin³θdθ/∫r²Bsinθdθ。1332keV的两个平均分别.17917330/.21199965；从1332到100keV的比为2.2437904/2.2636514，不能因数值接近就认成真实相同response。

E→0时r=1，uniformθ为π⁻¹∫sin²θ/(1+cos²θ)dθ=√2−1，KN×dΩ平均为(∫sin³θdθ)/(∫(1+cos²θ)sinθdθ)=1/2，而point90=1。独立积分已核这两个解析极限；没有向原ScaleQ传E=0或把0/0当物理输出。三数不同来自接受/事件权重合同，与消费端经验Q及.5QPcos2ξ定义不是可任意互换的half-factor。

这些平均都缺真实geometry、threshold、多次散射、sorting/partial charge、背景和校准Cov，不是任何实际detector的替代Q。再增加同kernel积分点只提高数值精度，不提供独立response证据。

- 不同代码path/版本、手动更正的本地producer、历史宏或选择条件可能使论文实际分析未经过这些表达式；默认CMake为Lean是直接反证，必须保留。
- 两repo当前公开版本独立固定；CMake FetchContent写GRSIData main，不是锁定的历史依赖。本文未证明原实验的binary和当前组合相同。
- zero-error、bin重叠或mixed-index依赖是组件层的已观察行为；没有实际counts、作者执行命令、Q/门ledger与Σ，不能报新的P/Q/δ、排除概率或实验误差修正。
- helper保留逐crystal诊断，但输出2D矩阵本身不含完整可恢复eventID/所有sharing关系。字段存在不等于能从hist恢复完整统计结构。
- 本轮没有联系作者、上报issue或改外部repo；GitHub只作为外部公开科学代码来源，不是本Wiki维护入口。

## Analytical Reconstruction and Self-Audit

### 默认Lean完整消费端的ROOT schema控制

[执行前合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/lean-schema-before.md)、[程序](../../system/scripts/day17_grsisort_lean_schema_audit.py)、[actual result](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/grsisort-lean-schema-result.json)保存完整原Lean source/hash、batch入口与原MathMore路径。只将main改名供wrapper调用并设置gROOT batch以避免GUI；原选择、积分、fit和预测body未修改。

两个设计ROOT fixture都为六个180×180 TH2D、角范围0–180.000001°，prompt均值1000(1−.2cos2ξ)、mixed1000、geometry1；只更换newhelper/legacy两套key。它们不是Poisson抽样、真实events或原实验histogram。new-helper-schema输入触发原consumer缺key后的Segmentation violation、actualexit139，生成文件存在却四目标graphs均缺失；不能因有output.root或检查程序exit0就声称消费成功。legacy输入actualexit0，给raw171点、binned19点、folded10点与theory101点。binned/folded原fit amplitude分别.1995232/.1996137，quoted程序fiterrors只记录其行为，不是实验CI/coverage或P/Q认证。

这缩窄了“代码已公开即可串联”的预期：输入对象、版本和schema必须与执行路径匹配，缺key需要独立失败记录。没有以重命名实际作者data、patch程序、改template或抹去exit139来强求通过。真正的originalproducer/actualmatrix、校准/response/Σ仍未取得，不能把fixture正控制称真实GRIFFIN分析复现。

| 项目 | 证据与实际结果 | 边界 |
| --- | --- | --- |
| provenance | Git commit/blob与SHA-256、MIT、完整selected source read | 非整repo审核或exactpaperproducer |
| native component | g++编译0/run0；ROOT6.40.04/MathMore；原函数body hash | 明确hit/settings/sink shims，不认证RDF/DAQ |
| 反证 | Lean的second F消费和CMake默认目标 | 禁止跨版本泛化新Analyze的局部结果 |
| next input | actualmatrix/TTree、settings、逐台selection、calibration/Σ | experimentalL4 not-ready；不再用同toy补缺口 |

## Knowledge Impact and Learning Decision

`supports`以真实code path核验计数与Q/geometry输入；`revises`只要公开helper/参数存在就已有matching response的预期；`limits`从选定组件问题裁决整个软件或原实验。来源为同一public软件链，多个函数/版本对照不是独立实验；新claims全needs_review，不设human-reviewed。

## Human Review Triage

P1：未来用于实验分析前，必须核原作者/用户实际执行的helper/analyzer/版本、完整input/response/Σ。当前为Codex self-audit，无默认用户待审任务；涉及正式论文claim时再定向核验。

## Extracted Pages

- [[compton-polarimetry]]、[[linear-polarization-asymmetry]]、[[polarimetry-shared-calibration-count-design]]；event-mixing统计与原shape/δ实验结论不由本software page替代。
