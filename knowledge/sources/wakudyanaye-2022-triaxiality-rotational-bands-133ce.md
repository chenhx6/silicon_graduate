---
type: source
title: "Wakudyanaye 2022：133Ce三轴性与转动带硕士论文"
title_original: "Triaxiality and Rotational Bands in 133Ce"
aliases: [Wakudyanaye 2022 133Ce thesis, 133Ce硕士论文]
created: 2026-10-26
updated: 2026-10-26
status: ai-draft
review_status: unreviewed
source_type: masters-thesis
reading_depth: deep-read
authors: [Ignasio Wakudyanaye]
year: 2022
institution: University of the Western Cape
degree: Magister Scientiae
citation_key: ""
canonical_source: "raw/papers/degree dissertation/Triaxiality and Rotational bands in 133Ce.pdf"
raw_file: "raw/papers/degree dissertation/Triaxiality and Rotational bands in 133Ce.pdf"
raw_sha256: "48556dbfe5284efebdb901cd949f534ac5552c6504e2c744603afca386660080"
nuclei: [133ce, 131ba]
models: [QTR, Nilsson, BCS, frozen-alignment]
methods: [gamma-coincidence, angular-distribution, signature-splitting]
tags: [133ce, thesis, signature, tilted-precession, wobbling, analysis-blueprint]
---

# 133Ce原件：从符合纲图到QTR逐量检验

## Bibliographic Record

Ignasio Wakudyanaye，*Triaxiality and Rotational Bands in 133Ce*，University of the Western Cape，March 2022，Magister Scientiae。封面PDF1；全文130页，正文印刷1–107对应PDF12–118，正文页码+11=PDF页码。来源为用户指定原件，不改原文件名/内容；未唯一匹配本地Bib故citation_key留空。

## Scope and Reading Depth

主代理完成正文Ch1–7及参考文献的主线文本阅读，Ch3和Ch6关键形式/比较回读；不把3806个native block的提取当阅读。视觉实际核PDF77/82/111/112/114整页，PDF65纲图旋转大图，PDF48/67/68/69/70/80/81/85/86/89/90/94/95/101/103/105/109/113的contact sheet；子代理独立核关键表图。小字/曲线只作所述范围核验，未逐一数字化所有图。

Covered：两实验来源/实际装置、Band1–4符合逻辑、AD与DCO/RAD区别、g7/2 signature/Coriolis主线、h11/2 TiP/FA主线、QTR basis/程序分工、逐线δ/两类相对B分母、图表内部差异与实际输入缺口。Not covered：引用74篇原件的独立全文、作者GAMPN/ASYMO/PROBMO版本与输入卡/输出、原event/效率/AD/P/协方差、目录/参考逐条中文翻译、用户独立数据重分析。

`deep-read`表示本source主线和关键证据达到相应阅读深度；不表示用户要求的长期深入学习已完成。后续分析蓝本、推导、核对、反证及可复现练习在[[133ce-thesis-analysis-blueprint]]持续推进。

## Summary

论文有两条分别定标的研究线。正宇称g7/2带展示γ与Coriolis/邻轨道混合共同影响signature splitting；负宇称h11/2的Band1/4把九轨道QTR与单轨道FA逐量比较。完整空间能量/S和rE2较好、FA连接δ更近、Fig6.16/正文给两者rM1 spin趋势均不佳（表6.9趋势有内部冲突），故学习价值在于从实验定义到模型失效的完整过程，不能只取摘要的总体判断。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WK22-01 | 133Ce实验由125Te(12C,4n)在57MeV进行，靶2mg/cm² Te、8mg/cm² Au背衬；论文§5.2.1报告13clovers为45°1、90°8、135°4，与Ch4一般介绍及Ding2021两版本所写8clovers的实际run对应尚待ledger核查。 | experimental-method | direct-original-or-explicit-task-derivation | PDF61, §5.2.1 | true |
| WK22-02 | 论文报告2.8×10^10双符合和5.4×10^9三重及以上事件；校准和sorting由合作方，作者做γγ符合/纲图分析及QTR解释，不能把总events当某弱线有效计数。 | experimental-report-and-provenance | direct-original-or-explicit-task-derivation | PDF61, §5.2.1; PDF54 §4.6 | true |
| WK22-03 | Band4从832.0keV、13/2−延伸到3616.2keV、27/2−；Table5.2列13条带内及15条带间跃迁，正文“six”mixed后实际列七条。 | experimental-level-scheme | direct-original-or-explicit-task-derivation | PDF67, Table5.2; PDF62 | true |
| WK22-04 | 608.3keV Band4内19/2−→15/2−与608.7keV Band4→Band1的15/2−→13/2−构成重叠gate；209/399在608门出现不能直接判与608.3共路径。 | experimental-analysis-example | direct-original-or-explicit-task-derivation | PDF62–63, §5.2.2.1; PDF68 Fig5.2 | true |
| WK22-05 | 871与936门对490/380的出现/缺失关系用于把490/380置于871的平行支路；不由单一缺峰推出严格零强度。 | experimental-analysis-and-boundary | direct-original-or-explicit-task-derivation | PDF62, §5.2.2.1; PDF68 Fig5.2 | true |
| WK22-06 | Band2正宇称g7/2线与Band1/4负宇称h11/2线是两条研究主线；Band2的signature分支不能同Band4集体候选合并。 | source-scope | direct-original-or-explicit-task-derivation | PDF75, §6.1; PDF76 §6.2; PDF98 §6.3 | true |
| WK22-07 | Table5.3保留2733.4和2739.5keV两条19/2+能级；881.2/886.8不能因spin相同自动合并。 | experimental-identity | direct-original-or-explicit-task-derivation | PDF69, Table5.3; PDF65 Fig5.1 | true |
| WK22-08 | 本文S(I)由四个相邻能量的线性组合定义，不是Eγ/(2I)，亦不是独立新增实验。 | observable-definition | direct-original-or-explicit-task-derivation | PDF35, Eq2.37 | true |
| WK22-09 | QTR轴1/2/3依次intermediate/short/long，Jk=(4/3)J0 sin²(γ−2πk/3)为模型假设；不能把形状γ与实测刚性等同。 | model-assumption | direct-original-or-explicit-task-derivation | PDF37, Eq3.2 | true |
| WK22-10 | 强耦合D2对称basis含K−Ω偶整数，BCS u²+v²=1，最终态为不同K/ν振幅的相干展开；只给最大的三个分量不足以恢复全部EM矩阵元。 | model-formalism | direct-original-or-explicit-task-derivation | PDF47, Eqs3.17–3.20 | true |
| WK22-11 | GAMPN→ASYMO→PROBMO依次单粒子态/矩阵元、粒子芯耦合本征态、电磁矩阵元/δ/矩；没有真实版本、输入卡和中间文件，不能称复现作者计算。 | model-producer-contract | direct-original-or-explicit-task-derivation | PDF49–50, §3.4 | true |
| WK22-12 | 正宇称10轨道，Harris J0=10.4、J1=35.7分别以ħ²MeV−1/ħ⁴MeV−3计；先按γ0能量定标，再扫描γ、Coriolis χ。 | model-input-and-calibration | direct-original-or-explicit-task-derivation | PDF77–79, §6.2.1 | true |
| WK22-13 | Ce在χ1时γ0–15仍有可比能谱/S描述；χ.7时需较大γ约20才恢复显著S。作者以邻s1/2、d3/2的K1/2混合作解释，不把S唯一反演为γ。 | model-result-and-interpretation | direct-original-or-explicit-task-derivation | PDF79, PDF84; Figs6.1–6.5 | true |
| WK22-14 | 正宇称Table6.1列ε4=.1，紧接正文ε4=.01；两处视觉确认，原input缺失，不挑一值当实际作者输入。 | source-internal-conflict | direct-original-or-explicit-task-derivation | PDF77, Table6.1 and following paragraph | true |
| WK22-15 | Table6.3 9/2+主分量振幅.982/−.202/.185平方和1.039353；按caption贡献=振幅平方、正交归一basis解释不闭合，不能以遗漏小分量修复或静默重归一。 | task-derived-source-audit | direct-original-or-explicit-task-derivation | PDF82, Table6.3 | true |
| WK22-16 | 负宇称9轨道，ε2=.183/γ21°/ε4=.015；Harris J0=10/J1=25，gs=.6gfree、gR=Z/A≈.44，是模型输入，非本研究测得g。 | model-input | direct-original-or-explicit-task-derivation | PDF77 Table6.1; PDF98–99 §6.3.2 | true |
| WK22-17 | Band1/4主要轨道18≈νh11/2[514]9/2−，Band4低spin主(Kl,Ωl)≈(13/2,9/2)、Rl≈2ħ；高spin其它成分增长，不能将一个主峰标签当各态精确转轴或完整波函数。 | model-result-and-validity | direct-original-or-explicit-task-derivation | PDF99–106, Tables6.6–6.8; Figs6.12–6.13 | true |
| WK22-18 | 作者的FA把空间限制到轨道18，同惯量下能量偏高且S很小；这是特定单轨道计算比较，不等于所有wobbling模型/HFA的普适否定。 | model-comparison-and-boundary | direct-original-or-explicit-task-derivation | PDF107–109, §6.3.3; Fig6.14 | true |
| WK22-19 | Table6.11报告625/582/465标签线δ分别−1.5(+.97/−5.7)、−.55(+.12/−.25)、−.17(+.09/−.2)；准确母末态用Table5.2绑定624.6/582.7/464.4。 | source-reported-mixing-ratios | direct-original-or-explicit-task-derivation | PDF112, Table6.11; PDF67 Table5.2 | true |
| WK22-20 | Table6.11同时给out/out和out/in两类分母；582的out/out ΔI2分母在Table5.2未直接确认，保持missing，不能捏造817.7keV线/强度。 | observable-identity-gap | direct-original-or-explicit-task-derivation | PDF112, Table6.11; PDF67 Table5.2 | true |
| WK22-21 | 跨Band4→1 δ在FA下比九轨道QTR更接近实验；Fig6.16及作者正文称两模型rM1随spin下降而实验上升（Table6.9打印值另有冲突，见WK22-22）；九轨道rE2较好。各项须分别保留。 | author-model-comparison | direct-original-or-explicit-task-derivation | PDF113–115, Figs6.15–6.16; §6.3.5 | true |
| WK22-22 | Table6.9 rM1首点.01 vs Fig6.16a约.10；Table6.10 rE2 .44/.11 vs Fig6.16b约.044/.011；caption b的in/out与轴/正文相反；精确producer缺失，图读数仅量级。 | source-internal-conflict | direct-original-or-explicit-task-derivation | PDF111, Tables6.9–6.10; PDF114 Fig6.16 | true |
| WK22-23 | 按Eq3.24，Eγ用MeV、B(E2)用e²b²、B(M1)用μN²，严格同母态同reference下δ²≈.7Eγ²rE2/rM1；两种B比与δ同源，不能在无Cov下当三份独立观测。只用实验Eγ诊断实验summary，不能替作者模型Eγ。 | task-derived-dependency | direct-original-or-explicit-task-derivation | PDF48, Eq3.24; PDF112 Table6.11 | true |
| WK22-24 | 582 δ中央−.55给E2光子份额23.2%，正文约30%不是另一独立测量；625误差很大而无成分占优的确定判断。 | task-derived-central-values | direct-original-or-explicit-task-derivation | PDF111, first paragraph; PDF112 Table6.11 | true |
| WK22-25 | 图6.15a的Band1 intrabandδ来自Ref56 Paul1991；Band4连接线数据为本实验。正宇称成果进入Ref22 Ding2021，学位论文与该文不重复计实验票。 | source-lineage | direct-original-or-explicit-task-derivation | PDF113, Fig6.15 caption; PDF117 Ch7 | true |
| WK22-26 | 作者以abs(δ)>1必要条件拒绝Band4 wobbling；本库保留其原解释但不恢复跨核硬门：130Ba两准粒子M1占优仍有真实支持链；HFA有效域、完整非谐拓扑、电磁量须分检。 | author-interpretation-and-calibration-boundary | direct-original-or-explicit-task-derivation | PDF110–111, §6.3.4 | true |
| WK22-27 | AD/DCO/RAD定义及典型参考值属于该阵列/门/取向条件，实际133Ce用all-detector gate RAD；论文未交付联合AD/P原计数、response和逐线δ likelihood，不能据该文本重拟CI。 | experimental-method-and-input-boundary | direct-original-or-explicit-task-derivation | PDF58–59, Eqs4.3–4.6 | true |
| WK22-28 | Table5.2打印Iγ与Table6.11中央δ条件重组的比值不全等于6.11；只说明summary/处理谱系未闭合，原gate/效率/双峰/Cov缺失，未做显著性或实验错误判决。 | task-derived-summary-audit | direct-original-or-explicit-task-derivation | PDF67 Table5.2; PDF112 Table6.11 | true |
| WK22-29 | 由Eq3.14所含j²提出selected lab单j11/2、P=span(m±9/2)控制：PjxP=PjyP=0而Pjx²P=Pjy²P=31/4；这是任务定义的算符投影练习，非真实轨道18/作者FA复现或实验值，不能把top3归一冒实际态。 | task-derived-projection-control | conditional-mathematics-not-nuclear-fit | PDF45 Eq3.14; PDF99 Table6.6; PDF107 §6.3.3 | true |
| WK22-30 | Tables6.2/6.4 ε列标MeV且约5.45–6.51，正文正宇称Ce λF50.6MeV/Ba λF51.0MeV；本轮未找到这些具体量共同零点/转换说明。不能据背景ħω自动改表单位，负宇称λ更不能继承正宇称值；需实际GAMPN/ASYMO接口header与λ/Δ合同。 | source-literal-and-input-unit-gap | direct-original-and-readiness-boundary | PDF78 Table6.2 and preceding paragraph; PDF87–88 Table6.4; PDF47 Eq3.20 | true |
| WK22-31 | 同源Ding2021稿本/正式版均写8clovers两环，thesis具体段13三环；同事件计数等字段只给强同源线索，actual geometry/run ledger缺，不能据13或8任一描述直接认证δ响应。 | cross-source-apparatus-and-dependency | direct-original-and-readiness | PDF61 §5.2.1; DingmanuscriptPDF2 §II.A; Dingpublished064304-2 §II.A | true |
| WK22-32 | 固定H/态/E2/能量，仅整个M1算符乘共同正η时δ除η、rM1乘η²、rE2不变；打印表中央值所需逐线η不同只作条件诊断，不是g拟合/CI/原模型排除。模型mixed光子yield会变，实验counts不变；单改gs也不等同整体η。 | task-derived-operator-scale-control | conditional-mathematics-not-model-replay | PDF48 Eq3.22–3.25; PDF111 Tables6.9–6.10; PDF112 Table6.11 | true |
| WK22-33 | Band4的#17/#16轨道激发替代须在同H/算符/空间下找到能量和全连接匹配的本征序列；两轨道已在原九轨道混合内，仅换标签无新预测。3qp另增空间/blocking/残余力，低832keV可行性未知，不与TiP自动等可信；真实gK、signedδ预测当前缺输入，保持unknown。 | task-configuration-design | source-grounded-candidate-not-fitted-model | PDF99 Table6.6; PDF104 Table6.8; PDF107 §6.3.3 | true |
| WK22-34 | 与AW13对照时Band3不可按同号合并：本论文Band3为1/2+ground，Band2的13/2+1459.9与Band3同spin1445.8相差14.1keV，412.4/767.7跨带links可定位；不等于已测ωc/混合矩阵元。 | source-identity-and-analysis-boundary | direct-original-and-explicit-central-difference | PDF69 Table5.3; PDF71 Table5.4; AW13 printed82 §5.2.2 Band3 (PDF86) | true |
| WK22-35 | Eq4.6把135°/90°目标线都用all-detectors门，正文说R_AD不依赖gate multipolarity并给约1.3/0.8；它是本文方法/经验校准表述，不单由“all”一词推出任意有限acceptance的精确4π消去。在声明equalweight point-ring条件下，13布局的rank2/4 gate acceptance moments为−11/52、31/416；Ding8布局为−1/8、−1/64，均非零。此数学练习不认定actual geometry、不预测真实R_AD或重拟δ。 | literal-method-and-task-acceptance-boundary | direct-original-plus-declared-mathematical-exercise | PDF59 Eq4.6 andfollowingparagraph; PDF61 §5.2.1; DingmanuscriptPDF2 §II.A | true |

## Experimental or Theoretical Setup

论文具体段报告的13-clover133Ce与Ding8-clover描述仍待actual ledger；133Ce与GALILEO的131Ba是不同目标核采集。论文Ch4对阵列历史/一般结构的描述不能替代Ch5具体run配置。相对Iγ按170.2keV归一；同归一的误差相关性应恢复。原能级、光子强度、多极/δ提取、PES和QTR输出分别建账。

QTR合同：H=Hint+Σ(Ik−jk)²/(2Jk)，D2 strong basis和BCS；正宇称10轨道、负宇称9轨道、FA1轨道互不混用。三程序接口只是程序角色描述，尚不具有可复跑完整输入。gs与gR是算符选项而非额外磁测量。

## Competing Interpretations and Limitations

作者在Lawrie/TiP解释框架下讨论HFA和小δ；本库继承Day23校准：几何、harmonic phonon近似、完整非谐拓扑和实测EM量分开；F14冻结内禀j仍可有M1；M1占优不能唯一指定TiP/SP/MR，δ和W.u.不设普适硬门。[[frauendorf-2014-transverse-wobbling]]与[[chen-2019-transverse-wobbling-even-even]]保留支持方，[[lv-2022-evidence-against-wobbling-135pr]]与[[guo-2022-low-spin-wobbling-187au]]保逐线反证。

Table6.1 ε4、Table6.3归一、Tables6.9–10 vs Fig6.16、582 out/out分母均保留open。它们限制直接复制输入/图点；不据此一概否定论文所有实验或模型。实际δ拟合/Cov/producer不足时只做可复核中央值代数，不报新CI、τ、Q(E)、绝对B或机时。

## Source Independence

Ref22 [[ding-2021-131ba-133ce-signature-splitting]]与本论文正宇称工作同源；Ref56 Paul1991给Band1旧δ，是另一个观测来源但本轮仅核此引用归属，未独立取得全文。Ref3为[[alwaleedi-2013-band-structures-131ce]]，说明论文自身也以131Ce学位研究为相关背景；不能把两个核的band号合并。跨论文/campaign是否共享event必须由实际ledger确认。

## Extracted Pages

[[133ce-thesis-analysis-blueprint]]为本轮新深入学习工程，连接[[131ce-collective-mode-discrimination]]、[[133ce]]、[[133ce-band-2]]、[[afrodite-133ce-c12-57mev]]和[[signature-tip-shears-discrimination-contract]]。source self-audit不新增human-reviewed，所有新claim保持needs_review:true。

## Day23原方法追溯

Ref62已取得并读[[ragnarsson-semmes-1988-particle-rotor-moments]] RS88-02–10：stretched/physical坐标、BCS/core-H因子、coreR基变换及历史参数各有合同；1988 gs=.7不能覆盖本论文负宇称.6。程序实际版本/input仍缺。

正文Ch1–7和前置实质段落的逐段reader目前齐备；目录/参考未逐条译/独立源核验。可用输出入口outputs/degree-dissertation/wakudyanaye-2022-133ce-reader/paper.md。它服务于深入学习，不是本source全部科学结论已闭合的认证。


### Day24 checkpoint001 Agent self-audit triage

P0: none identified（本次新增范围无未隔离技术hard P0）。P1：WK22-35对PDF59/61原字面回核；接受度数学的假设/actualmask缺口保存于133ce-thesis-analysis-blueprint，非实测response。后续论文/关键问答仍按具体claim回源，未触发用户人审事件。
