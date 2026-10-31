---
type: source
title: GRIFFIN角关联分析：事件混合与有限几何响应
aliases: [Smith 2019 GRIFFIN angular correlations, Smith 2018 arXiv 1807.07570, GRIFFIN event mixing]
created: 2026-10-16
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
source_type: experiment-and-method
reading_depth: deep-read
title_original: "Gamma–gamma angular correlation analysis techniques with the GRIFFIN spectrometer"
authors: ["J. K. Smith", "A. D. MacLean", "W. Ashfield", "A. Chester", "A. B. Garnsworthy", "C. E. Svensson"]
journal: Nuclear Instruments and Methods in Physics Research Section A
year: 2019
volume: "922"
pages: "47-63"
doi: "10.1016/j.nima.2018.10.097"
arxiv: "1807.07570v1"
language: en
canonical_source: "Smith et al., NIM A 922,47–63(2019), DOI10.1016/j.nima.2018.10.097; 本页实际读arXiv1807.07570v1(2018),28页。"
raw_file: "raw/papers/gpt/learning-daily/20261016-DAY15-ado-angular-distribution-geometry/smith-2018-griffin-angular-correlation-arxiv1807.07570v1.pdf"
raw_sha256: "0390bdbb6b78f035d1d49abd4ecf863a684f3a8eb3ba6c537cfbd8fb6e352f33"
nuclei: [60Ni, 152Gd, 66Zn]
observables: [gamma-gamma-angular-correlation, angular-distribution-coefficient, multipole-mixing-ratio]
methods: [event-mixing, gamma-gamma-coincidence, GEANT4, finite-geometry-correction]
tags: [griffin, angular-correlation, event-mixing, response, covariance, version-boundary]
---

# GRIFFIN角关联分析：事件混合与有限几何响应

## Bibliographic Record

Crossref exact DOI记录核到作者、2019年、NIM A922和47–63；arXiv官方history仅列2018-07-19的v1，并回链该期刊DOI。本页的全部正文locator均指[arXiv1807.07570v1](https://arxiv.org/abs/1807.07570v1)的PDF页码，**不把预印本当作已经逐字核对的2019 VoR**。公开PDF经nature-downloader取得，%PDF、题名、28页、1920698bytes及raw hash逐项核验；[采集manifest](../../outputs/literature-acquisition/20261016-day15-smith-griffin.json)记录版本和新raw逐文件gate。没有改写已有raw或Bib。

Crossref-deposited官方Elsevier XML入口一次ConnectionError，未取得VoR正文，不重复相同访问，也不把下述v1内部问题归为已确认的期刊版错误。未取得原始GRIFFIN事件、各拟合的完整Cov/χ²网格或当年生产sorter；参考文献中的软件DOI只作为后续可验证入口，不等于本session已build或重放。

## Scope and Reading Depth

本session在打开全文前先冻结已暴露abstract的primed回忆。随后读完PDF1–17主文与表1–9/A.10、18–27的全部附录图注/level-scheme说明及28参考文献；核对Eq1–29的主线。视觉重点核PDF6 Fig2、7 Fig3、10 Table4/5、11 Eq27/Table6、14 Table7/8、17 TableA.10；Fig1/6/8/9及附录A.10–A.19作整页/联系表图像核查。没有从联系表估精确数据点或重建未公开的图中Cov；Fig7曲面没有独立数值重拟合。

## Paper Question and Scientific Motivation

大型clover阵列的晶体组合数、energy/time效率和finite detector response怎样影响gamma-gamma角关联系数，以及如何用实验与模拟把它们分开处理？作者在随机取向beta衰变source、短中间态寿命及本研究Jx=2的条件下工作；其`W=A00(1+a2P2+a4P4)`截断在这些cascade上精确，不能自动推广到in-beam alignment或更高rank。

## Method and Design Logic

### 事件混合只先消去匹配的效率权重

Eq6–10把观测写成对ordered crystal pairs的和：

\[
w_i=\sum_{jk}A_{jk}\int N_{jk,i}(\theta)W(\theta)d\theta,\qquad
y_i=\sum_{jk}A_{jk}\int N_{jk,i}(\theta)Y(\theta)d\theta,
\quad A_{jk}=\int\epsilon_j(E_a,t)\epsilon_k(E_b,t)dt.
\]

同opening-angle bin内N_jk可视为相同、两hist的能量/效率时间权重匹配、Y=1时，Eq13给`w_i/y_i=int Ni W / int Ni`。还需W在接受区近常数，或N对称且W近线性，才能到Eq14的`W(theta_i)`。因此效率归一后的比仍是角响应卷积；single-γ isotropy不意味着joint gamma-gamma response已消失。Eq11印刷式未显式保留Eq7的time integral，使用时以Eq6/7的A_jk定义保存这项依赖。

不同核的同一nuclide衰变用2–200μs的间隔混合，prompt要求小于300ns。原文另要求mixing间隔远长于中间态寿命、短于效率变化尺度。固定短/长时间窗并不代替实际trigger、rate、time-dependent efficiency与同cuts核验。作者认为增加每次interaction的mixed partners可减小分母误差；原文没有提供用于本Wiki实际数据的完整event-reuse Cov，不能把pair entries自动当独立物理事件。

### 完整模板、基函数与代数近似

Method1对不同spin/δ直接生成GEANT4模板；Method2只需同两能量/同setup的三个正输入分布`Z0=1、Z2=1+P2、Z4=1+P4`，再用Eq19线性合成`A00[(1−a2−a4)Z0+a2Z2+a4Z4]`。线性组合系数可以为负，不能将它们当成三种随机事件的混合概率；源文的0→2→0例给`x=−500,y=357,z=1143`。

Method3用`L0=alpha、L2=alpha(1+beta P2)、L4=alpha(1+gamma P4)`近似完整Z模板，忽略部分bin级几何细节。Eq25/26得到`c2=beta a2、c4=gamma a4`，其中beta/gamma是detector几何响应近似，不是核alignment alpha、偏振Q(E)或ADO的f。Eq27传播c2/c4的Cov及beta/gamma的边际误差；将它用于共享模拟/校准时，额外beta-gamma及data-calibration Cov是否为零仍需验证，这是本Wiki使用边界。

Method4再以两能量函数积`f(E1,E2)=g(E1)g(E2)`近似beta/gamma，Eq29的参数和能量依赖在本setup标定；lambda量纲与E的单位须匹配。本文给24行TableA.10模拟输出，未给本Wiki可直接取用的完整fit parameter Cov。高rank、trigger、初始alignment、addback、折叠/分组或setup改变需要重验响应，不能移植表中标量因子。

## Key Evidence and Reasoning Chain

1. PDF3说明16个clover、64独立晶体、11cm配置，4032个energy-labelled ordered crystal pairs和51个unique opening angles；同一晶体的sum peaks另有64项。本文未用addback；极角相近不保证pair几何等价。
2. 同一60Ni cascade的Fig2给7.96→2.34→1.02的reduced chi-square改善，分别对应pair数归一、再加single-crystal efficiency、event mixing；三个处理不是三次独立采集。
3. Fig3的66Zn0→2→0纯E2、无δ歧义校验表明，event-mixed实验分布仍不同于未卷积的物理曲线；full detector GEANT4模板与实验的χ²/NDF=1.01。支持进一步校正finite geometry，不能由此保证任意新阵列模拟正确。
4. Tables4/6/7还给60Ni的Ji=2/4、152Gd的3/4、66Zn(1+)例的1/3/4等angular-only候选；充分的角覆盖仍可能多解。不同Ji路径使用的多极子对和δ语义也不同，不能只比一个符号数。
5. Table8的四种方法重用同一批实验数据和共同模拟/效率处理；literature a2/a4部分由已有δ推得。Method1的a2/a4明确由本次δ再传播，不是另外测了两个独立observable。

## Summary

这篇独立装置方法来源提供了“匹配event-mixed效率归一→保留finite-response卷积→用同setup已知cascade验证模拟→提取物理系数”的直接实验路线。其随机初态、Jx=2、no-addback及time-window条件清楚，适合约束ADO校准可迁移性的论证。原始events/完整Cov未取得，v1若干表格与正文存在局部不一致，故本页保留版本及输入边界。

## Experimental or Theoretical Setup

- 60Co/152Eu商业source与ISAC产生的66Ga source，测女核60Ni、152Gd和66Zn的五条cascade；不是Zheng2002的145Tb采集。
- 两种阵列距离在装置介绍中分别为11cm和14.5cm，本文数据用11cm、16clovers；不能把装置可配置范围误写成本文混合使用两套response。
- Table2中Ni1173.2/1332.5、Gd778.9/344.3、Zn2751.8/1039.2、1333.1/1039.2、833.5/1039.2keV逐cascade绑定；所有第二条为pureE2。
- full GEANT4模拟含detector、材料/Compton等影响；本session未运行该模拟，不替作者认证新版本。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| SG19-1 | 实际读取2018arXiv v1、28页；2019NIM A922,47–63及DOI只核metadata，VoR全文未取得，不能把v1内部问题归为期刊版错误。 | source-version-boundary | direct-and-self-audit | arXiv官方submission history；PDF p.1 | true |
| SG19-2 | 本文数据用11cm、16clover/64crystal，4032个ordered pairs、51个unique opening angles，无addback；同晶体sum peaks另计64项。 | experimental-setup | direct | PDF p.3，Sec2与Table1；PDF p.4首段 | true |
| SG19-3 | 匹配两能量和time-dependent效率、同opening-angle组内匹配pair kernel且Y=1时，event-mixed比为响应加权W平均；只有额外constant/linear近似才是中心角W。 | method-definition | direct | PDF pp.4–5，Eq6–14 | true |
| SG19-4 | 本文mixing窗2–200μs，prompt<300ns；还要求寿命≪mixing间隔≪效率变化尺度。未提供本Wiki可直接用的完整event-reuse Cov。 | method-and-boundary | direct-and-self-audit | PDF pp.6–7，Sec3.2 | true |
| SG19-5 | 同一60Ni分布按pair数、single-crystal效率和event mixing处理，与模拟比较的χ²/NDF为7.96、2.34、1.02。 | experimental-method-validation | direct | PDF p.6，Fig2及正文 | true |
| SG19-6 | 66Zn0→2→0的event-mixed分布仍受finite detector response影响；full模拟对实验χ²/NDF=1.01，不能直接拟合未卷积的物理曲线。 | experimental-and-model-validation | direct | PDF p.7，Fig3 | true |
| SG19-7 | Method2以Z0=1、Z2=1+P2、Z4=1+P4的模拟线性合成任意保留k≤4的物理分布；权重不必为非负概率。 | method-definition | direct-and-inference | PDF pp.8–9，Eq15–19及负x例 | true |
| SG19-8 | Method3近似c2=beta a2、c4=gamma a4；Eq27保留c2/c4 fit Cov及beta/gamma边际误差，未列一般共享校准的全部cross项。 | method-and-boundary | direct-and-self-audit | PDF p.11，Eq25–27 | true |
| SG19-9 | 部分cascade在angular-only扫描中保留多个Ji/δ候选；不能从方法校验直接推出唯一spin。 | identifiability-boundary | direct | PDF p.10，Table4 | true |
| SG19-10 | Methods1–4重用实验数据；Method1的a2/a4由本次测得δ派生而非独立测量。 | source-independence | direct | PDF p.14，Table8及脚注 | true |
| SG19-11 | Method4以g(E1)g(E2)拟合固定setup的beta/gamma；24行TableA.10是模拟输出，完整surface参数Cov未给，不能据边际表值重造原置信面。 | model-and-boundary | direct-and-self-audit | PDF pp.12–13，Eq28/29；PDF p.17，TableA.10 | true |
| SG19-12 | 作者要求新trigger/initial alignment应用先确认功能；addback、折叠/分组等应匹配修改后的模拟。 | transfer-boundary | direct | PDF p.17，Summary | true |
| SG19-13 | v1 Table5把Zn0+的beta印为.955706(27)，相邻正文为.9557(27)；按括号误差的末位语义差两个小数位，不能静默选定其一。 | source-consistency-boundary | direct-and-self-audit | PDF p.10，Table5与左栏末段 | true |
| SG19-14 | v1 Gd Method2 a4在Table4为−.002(3)，Table8为+.002(3)；Appendix A.16(c)图注Ji=1与Table4的3/4候选不一致。保留对象/表版本边界，未裁决VoR。 | source-consistency-boundary | direct-and-self-audit | PDF p.10，Table4；PDF p.14，Table8；PDF p.24，FigA.16(c)图注 | true |
| SG19-15 | v1正文给简化几何Q22=.923–.941、Q44=.761–.814，却称Table5的约.95/.84值在范围内；字面范围不覆盖，不能当独立定量一致性证明。 | source-consistency-boundary | direct-and-self-audit | PDF p.11，Eq25/26后简化几何段落 | true |
| SG19-16 | 本session取得Ref21/22所指2017固定公开软件归档：angular extension v1.0、detectorSimulations v1.0.0；Zenodo byte/MD5及本地SHA核过，非当前版本或成功执行证明。 | software-object-identity | direct | Zenodo records1120421/1123461的version/files；本页软件对象表 | true |
| SG19-17 | 固定detectorSimulations v1.0.0 README明确NDA/第三方IP源码被省略并需另取，要求旧Geant4/ROOT；公开源文件还说明constructor/geometry在local NDA文件。当前只做有限静态核查，未build或重放论文full response。 | software-readiness-boundary | direct-and-self-audit | archive v1.0.0 README.md L4/L10/L18/L34；src/DetectionSystemGriffin.cc L40–44 | true |
| SG19-18 | Day17只定向重核原v1 PDF3/Table1/caption/Sec2与PDF4实际data/kernel合同；Table1含与装置论文Table8同样的113.4/152.3/160.2及近86/94四小数脚注，不增独立实证。两文与当前native/Table2的有界不闭合须保留，不能据表重复认证historicalproducer或真实角response。 | targeted-cross-source-table-boundary | direct-targeted-source-and-comparison | PDF3 Table1/Sec2；PDF4 Table2/Eq6–12；GF19-15/16/18 | true |

### Day17定向角表与response合同复核

本session仅针对[[garnsworthy-2019-griffin-facility]] GF19-15/16/18的角表问题重核本篇原hash/PDF3–4及两页图像；旧SG19-1–17逐字/flags保持，不重记28页全文credit。Table1与装置Table8的相同三行和caption属于共享几何谱系，不能作独立验证；[[triumf-griffin-compton-source-calibration]]记录当前paper/code与actualevent/Σ缺口。当前native位置/打印方向相合和Table8的partial边界不认证本篇实际geometry producer，也不修改原表或既有实验coef/δ。

## Nuclear Structure Information

女核cascade是方法校准对象；不因五条cascade额外建立新能带或模式页。已知spin的校验与从angular-only扫描容许多个spin是不同命题。需要裁决E/M或初态spin时，应使用同一跃迁的独立偏振、ICC、选择定则或其它level信息，并核其可测性。

## Authors' Interpretation

作者将四种方法描述为降低后续模拟成本的连续近似层级；同setup的energy-parameterized方案只需首次校准。Method3的低阶多项式丢失部分bin细节，作者用拟合误差膨胀处理残差，并报告精度下降。此为其校准策略，不是任意不良χ²都可只放大误差的通则。

## Model Results

Method1–4的仪器响应模拟与实验fit必须分开。TableA.10给response模拟参数；Fig3的蓝线是输入物理correlation、magenta是full response模拟、黑点是实验。对三个图层交换身份会误判“各向同性初态意味着无关联”或“efficiency校准已经校正有限角”。

## Competing Interpretations and Limitations

- 一般alignment/feeding与条件门的分布可能改变，不应把随机source的event-mixed reference直接迁移到in-beam ADO。
- 同opening angle的不同pair geometry与time weights需要匹配；scalar效率只有零阶信息。Full response的角矩、pair losses和shared-event Cov尚需本实验输入。
- 预印本表/文字差别保留SG19-13/14/15。完整Cov缺失、图中ellipse未定义统一覆盖约定时，不据视觉重造显著性；本文的“1sigma ellipse”未在本session转换成68.3%二维联合置信区。
- 四种方法和文献引用不是独立实验倍增。数据由三类parent source产生，同一66Ga的三条66Zn cascade也共享采集/仪器处理。

## Analytical Reconstruction

可迁移的是“同能量/时间/选择下验证pair响应”的工作流，不能迁移GRIFFIN11cm的beta/gamma、mixing窗或calibration精度。[[ado-covariance-calibration]]已给另一套明确自设输入的背景/效率Cov；它与本source实验数值不同，没有补出GRIFFIN实际Σ。下一项有信息的推导是mixed-partner复用对分母/比值Cov的影响，及原文正Z基函数在完整响应下的线性/归一合同；未得事件和production配置前保持条件分析。

## Knowledge Impact and Learning Decision

`supports`效率归一与finite geometry分步验证；`limits`single-γ标定和event mixing到full-response的自动等同；`revises`将geometry模型误差、版本内部歧义和多spin候选纳入输入合同。没有新增真实Jpi/δ或集体模式结论。

## Related Knowledge and Project Relations

- [[angular-correlation]]：补充独立装置的event-mixing/finite-response实证及共同数据边界。
- [[angular-distribution]]与[[ado-covariance-calibration]]：限定ADO门/几何校准迁移，不把c=beta a或gamma因子当Zheng的f。
- [[angular-distribution-coefficient]]：a=Aii/A00、raw c、instrument beta/gamma与核alpha需逐文约定。
- [[zheng-2002-ado-coincidence-angular-anisotropy]]：两文不同装置/采集；比值定义和响应对象也不同，不能合并参考阈值。
- [[rose-brink-1967-phase-defined-angular-distributions]]：本文Ref3的理论入口；理论引用不构成额外独立实验。

## Human Review Triage

本节为Codex source self-audit，不是用户待办或人审记录。P0科学使用边界为v1≠VoR、event mixing≠完整几何去卷积、未得实际Σ；未发现未隔离technical hard P0。P1为SG19-13/14/15和scalar/full response迁移、δ/spin多解及Cov假设。全部新claims保留`needs_review: true`；若后续正式写作需要某个v1有歧义的数值，再对具体claim查VoR或作者数据。

## Non-source Notes and Follow-up

本文Ref21指向angular-correlation模拟修改的固定软件DOI `10.5281/zenodo.1120421`，Ref22指向GRIFFIN模拟`10.5281/zenodo.1123461`。初次主文核读时只核到paper引用；本run随后已取得公开归档并做下述有限静态检查，仍没有build或重放full response。未取得的private inputs不以默认几何或新版本软件补造。

## Day15固定软件对象：公开归档与完整重放的边界

以下是独立于论文正文的公开代码原件补核；paper的deep-read不扩张成整个代码包已精审。Zenodo两记录均HTTP200，原文件byte数与MD5匹配，再核SHA-256；只在Wiki新增raw归档，未覆盖旧raw或将zip纳Git。[软件manifest](../../outputs/literature-acquisition/20261016-day15-griffin-software.json)保留固定版本、文件身份和检查范围。metadata license字段均为`other-open`，本次未把包集成到tools或重新许可。

| 原对象 | 版本/日期 | raw归档/SHA-256 |
| --- | --- | --- |
| [Zenodo1120421](https://doi.org/10.5281/zenodo.1120421)，paper Ref21 | v1.0，2017-12-20 | `raw/papers/gpt/learning-daily/20261016-DAY15-ado-angular-distribution-geometry/zenodo-1120421-v1.0.zip`；`62c8c36d216fd6b3b1d3c8b8e300ef5606d473592ce18b5f92eca8e7afd28664` |
| [Zenodo1123461](https://doi.org/10.5281/zenodo.1123461)，paper Ref22 | v1.0.0，2017-12-21 | `raw/papers/gpt/learning-daily/20261016-DAY15-ado-angular-distribution-geometry/zenodo-1123461-v1.0.0.zip`；`09acdabb08f58724574ce16490b0c41c3c713ae03767744ec5dd193ac7a7834e` |

angular包根目录`README.md`共4行，L4说明扩展旧Geant4.10.01的radioactive-decay module；没有据此认证现版接口。detector包`README.md`的setup区L1–42已核，L4/L18/L34明确第三方IP/NDA源码省略、需要额外文件且公开/保留部分都需要；L10列Geant4.10.01、ROOT6.04.00，L39还提示usage可能过时。`CMakeLists.txt`111行读完，实际依赖Geant4；`src/DetectionSystemGriffin.cc`只核header/dependency和L40–44的constructor/local-NDA说明，未将3049行全文件称为已读。

这是**当前公开输入不足以重放full response**的readiness boundary，不是已经观测到build失败或判作者没有这些材料。没有执行README的外部安装/private-access脚本，没有读凭据、访问private collaboration仓库或改变本机软件配置。没有补production宏、原事件、拟合Cov或源文χ²；继续可做明确条件的统计推导或公开接口核查，而不假造原阵列响应。

SG19-4的partner复用问题现由[[event-mixing-statistics]]保存精确U统计量矩、finite-K噪声、ratio cross Cov及一阶投影退化控制；所有概率和MC为本任务自设，不改本文实验error bars。SG19-2的48-pair/64-crystal表值只给该方法中uniform-tag条件界的离散输入，不是测得efficiency/Σ。

## Extracted Pages

- 更新[[angular-correlation]]的event-mixing/finite-response方法边界，并接回[[angular-distribution]]与[[ado-covariance-calibration]]。
- 保留source中的三女核/五cascade作为明确校准样本，不建立无额外结构问题的nucleus/band页。
- 新增source入口及反向索引；正式写作所需的VoR/具体歧义数值核验留在claim边界，不冒称human-reviewed。
