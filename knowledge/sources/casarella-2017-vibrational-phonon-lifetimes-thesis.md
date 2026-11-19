---
type: source
title: "Casarella 2017 - Vibrational phonon candidates and rare-earth lifetimes"
aliases: ["Casarella doctoral thesis 2017", "160Gd 162Dy vibrational lifetimes thesis"]
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: doctoral-thesis-experiment
reading_depth: read
title_original: "Lifetime Measurements and the Feasibility of Vibrational Phonon Configurations in Deformed Rare-Earth Nuclei"
authors: ["Clark R. Casarella"]
year: 2017
institution: "University of Notre Dame"
doi: "10.7274/mg74qj7554s"
url: "https://doi.org/10.7274/mg74qj7554s"
canonical_source: "Notre Dame PhD thesis, title April 2017, CurateND Version 1"
raw_file: "raw/theses/gpt/query/20261119-international-nuclear-structure/CasarellaCR042017D.pdf"
raw_sha256: "dd4188d06f45f1d48f6c53c8900f06ccfe8cae9e081f76b7fa95466382a3aba4"
raw_storage_status: archived-local
archive_required: true
nuclei: ["160Gd", "162Dy"]
tags: ["DSAM-INS", "GRID", "lifetimes", "gamma-vibration", "multiphonon", "thesis"]
---

# Casarella 2017：变形稀土核振动声子候选与寿命约束

## Bibliographic Record

Clark R. Casarella，导师Ani Aprahamian，Notre Dame物理学博士论文。
题名页April2017；CurateND自身登记2017-04-13与上述DOI，不据此推断具体答辩/授予日期（PDF1-2）。

## Scope and Reading Depth

- Covered scope：Gemini十五主单元实际覆盖PDF1-333；PDF21为printed1，其后PDF-20。
  十二处章节/附录实际标题已核。35页frame单元先返回并缓存，主运行复用，不重复计入。
- 三个定向任务返回七项实质答复及可复用短段，管理层核关键原页并选择性编辑集成。
  CC-GDDISC的receipt等义对象仅作缓存格式规范化，原响应保留、无新API调用。
- 定向METHOD返回对PDF118同时列covered/unread，且声称读取未在该请求供给的92-93；
  不冒称该请求完整覆盖。管理层另核原件91-92、112、114-116、118；主读333页覆盖不受此问题改写。
  各worker自报verified/SUCCESS不是科学验收，也不等于另一份独立证据。
- Not covered：未运行v1pgm、CINDY、GRID/GRIDDLE或作者其它程序，未重新拟合事件/谱；
  未逐篇核读所有外部引文或确认2017年稿件后来的接受版。仅做注明输入的单位/分支/混合代数；无PDM。

## Summary

摘要称新增160Gd的29项及162Dy的47项寿命，借助UKAL的DSAM-INS约束低激发
四极/八极及多声子候选。作者尤其讨论162Dy的K=0与K=4双gamma候选，
但重要跃迁涉及寿命下限、文献分支、M1/E2混合、污染与未观测线。
强度增强/能量非简谐可以支持集体解释，不自动测出纯声子波函数。
附录另含ILL的GRID实验；技术独立与重复刊载须分别处理。

## Key Results

| ID | claim_kind | evidence_level | locator | statement / boundary |
| --- | --- | --- | --- | --- |
| CC17-1 | experiment / analysis | direct-original-pages | PDF77-80,112-118 | DSAM-INS由质心位移求F再反解tau；停止误差传播、分支筛选与近阈布居均影响寿命。 |
| CC17-2 | analysis / source-version | direct-original-pages | PDF125,190,251,263 | 1379keV态>1350fs与1558keV态>590fs；1599keV成员从发表版下限到后稿有限值的变化来自同谱系重估。 |
| CC17-3 | author-interpretation | direct-original-pages | PDF192-193,263 | 1599keV向gamma带的41(+16/-37)Wu支持作者的双gamma候选，误差和版本依赖不去掉。 |
| CC17-4 | analysis / interpretation | direct-original-pages | PDF146-148,212-213 | 1535keV的向gamma带强E2与2181keV混合/文献分支不同，不将后者完全排除混入或确证纯态。 |
| CC17-5 | source-consistency / calculation | original-plus-declared-algebra | PDF146-147 | 1Wu脚注与标准162E2换算相差约1e4；中心值核算与表强度相容，不认证作者代码或静默修原件。 |
| CC17-6 | methodology / lineage | direct-original-pages | PDF317-319 | GRID极端feeding范围及0.6tau_max经验值不是常规统计CI/最优中心，不与DSAM点估计直接平均。 |
| CC17-7 | author-interpretation / alternative | direct-original-pages | PDF222,240 | 向gamma带的较强E1也可来自K选择性，不能据此冒认E3实测或唯一八极-四极耦合。 |

## Experiment and Method

### DSAM-INS、误差与混合比

UKAL的DSAM-INS由多角度质心移动求F(tau)，再用Winterbon/v1pgm的慢化曲线反解寿命。作者说明停止本领使F约有10%的不确定度，并将其传播到寿命误差；非线性反解不意味着所有寿命都恰有10%误差（PDF77-80、112）。F与零相容或负值的分支不进入该文寿命平均（PDF112、114）；约10-600fs是理想灵敏区，不是硬性截断，原表仍报告部分大误差的ps级有限值或下限。160Gd的角分布入射能为1.5、2.0、2.8MeV，162Dy为1.6、2.2、3.1MeV（PDF92-94）；靠近布居阈值旨在减少而非无条件消除级联feeding（PDF118）。

角分布与多极混合比分析采用CINDY Hauser-Feshbach统计模型程序，通过拟合实验$a_2, a_4$系数完成$\chi^2$极小化（PDF 115-116）。实验装置为单探测器系统，不存在线偏振$P$测量；角分布幅度$A_0$仅代表经校正的光子产额，不可脱离寿命与分支比视作绝对跃迁几率（PDF 116）。非弹性散射对本实验高自旋（$J>5$）布居较弱的选择性源于中子动量与轨道角动量转移受限，非自旋单粒子本征截断（PDF 81, 110）。负宇称态退激中观测到的较强$E1$跃迁不能直接证明八极声子-四极声子耦合，存在$K$选择定则与两准粒子混杂的并列解释（PDF 222, 240）。

此处没有P参与的delta联合提取；不能把CINDY布居/光学模型条件概括成
“固定sigma/I”，也不能把未报告一个Gaussian宽度当成布居独立的实验结果。
从寿命求B仍依赖辐射分支、ICC与混合成分。F的逆方差平均不等于
对非线性tau简单平均；未观测/负F分支不应被任意赋零并作为普通数据点。

### 稿本与实验谱系

经原页核查，Casarella博士论文附录A与E分别对应已发表的PRC 91, 054317 (2015)（PDF 250）与PRC 95, 024329 (2017)（PDF 317）；附录B（2016-11-29稿，PDF 257）、附录C与D（2017-03-31稿，PDF 272, 297）均为论文所附的预印/近终稿，不可视作后续年份的最终刊出版本。附录E的ILL反应堆GRID多普勒展宽实验与正文中UKAL加速器的DSAM-INS测量属于不同技术路径与独立数据采集，重印附录不增加独立观测数，且共用文献衰变分支可能引入推导跃迁几率的协方差。附录B中的GCM明确为生成坐标法（Generator Coordinate Method，PDF 261）。

GCM缩写须按局部定义读取：此附录B的Gogny-D1S生成坐标计算，不是
[[ayangeakaa-2013-tidal-waves-chirality-thesis]]里的几何集体模型。
“附在2017论文中”不证明B/C/D已是后来最终刊出版本。

在162Dy寿命评估中，附录E的GRID测量因未观测级联馈入采用了极端假设以界定tau_min至tau_max范围，其给出的tau=0.6*tau_max仅为参考已知能级馈入比例的经验约定值，并非高斯统计拟合置信区间（PDF 319表I）。鉴于GRID与DSAM-INS存在截然不同的慢化机制与级联馈入滞后效应，对1535 keV与1728 keV能级不可进行无物理校正的直接平均。此外，原文PDF 244指出160Gd无法在ICEBALL进行(alpha,2n)测量系由于反应所需的158Sm靶不稳定，并非160Gd缺乏稳定靶材（其实验采用29.4564 g富集160Gd2O3，PDF 91；162Dy则用24 g，PDF 92）。

例如1535keV GRID范围0.15-5.2ps、表列讨论值3.1ps；1728keV范围0.25-1.0ps、
讨论值0.6ps（PDF319）。这些范围来源于未定feeding的极端设定，不冒称68%/95%置信区间。
与DSAM数据比较须保留各自的停止/feeding及共同文献分支，不从方法名推断零协方差。

## Vibrational Evidence and Boundaries

### 160Gd：0+带与重估数据

依据论文PDF 125表4.1、PDF 190及附录A（PRC 2015，PDF 251表I）与附录B（手稿，PDF 260、263表I），160Gd中1379 keV态τ>1350 fs（B(E2)<3.10 W.u.），正文>320 fs仅为该带成员寿命下限的统括下限；1558 keV态τ>590 fs。1599 keV态由2015年发表的τ>300 fs在后续手稿中重估为800(+730/-300) fs，致使541.53 keV至3+γ跃迁由<174 W.u.修正为41(+16/-37) W.u.，作者据此提出γγ候选；该值误差大且依赖寿命与混合比重估。能级编号在正文（0+3）与手稿表I（0+2）存在不一致，建议以激发能认同各态并保留原编号，避免混淆。

这里的>320fs是全带成员的宽泛下限叙述，不能覆盖掉各能级自己的原报限值。
转动成员向gamma带的强E2与带头向基态的弱E2是不同约束；不能仅凭较弱的
基态支路就否定所有集体混合，也不能把一种增强支路变成唯一微观机制。

### 162Dy：强度依赖与两声子候选

核查162Dy之Table 4.8（PDF 146-147）与正文（PDF 148）：注脚标注之1 W.u.=5.25E-7 e2b2与A=162标准单粒子值（0.005246 e2b2）相差约10^4倍，但中心值代数核算（0.64761 MeV、1.2 ps、分支0.497得56.6 W.u.）与表中57 W.u.一致，与所核表中中心值相容，不认证作者实现或其它表格。1535 keV（4+1）能级寿命仅依赖572 keV单一跃迁测定（475 keV受本底污染，647 keV呈负F(τ)排除）；表中所列括号值明确为代入文献强度的推导结果（B(E2)为23、98、120 W.u.），复用时须注明各跃迁测量受限与强度来源依赖。

162Dy中2181 keV（4+2）态的1217 keV跃迁以M1为主（δ=0.24(+0.07/-0.06)，tau=240(+190/-80)fs），经文献相对强度归一后B(E2)=0.7 W.u.（假定单分支约为1.3 W.u.，PDF 146、213）；退激至2+γ带头的1292 keV跃迁本实验未测得，文献分支导出8.3~8.5 W.u.，表4.8终态列3+γ而与能差及正文不一致（与888 keV能差不符）。该态具有文献依赖性与多极混合，弱E2分支不能排除γγ成分亦不能确证纯态。同理，1400 keV（0+2）态多项跃迁依凭文献分支或上限（如512 keV退激<16 W.u.），物理结论应表述为带不确定性的γγ两声子候选。

本实验较强的1535keV退激与高能2181keV的小分量/文献分支并存，
应区分“主要强度集中于某态”“碎裂/混入成分”和“纯振动态”三个命题。
1400keV候选的512keV支路受湮灭峰限制；不能把未直接测到的分支当作确定的本实验数值。

## Competing Interpretations and Limitations

- 较强E1不等于已测B(E3)；K选择性、双准粒子及声子耦合须并列（PDF222、228-240）。
  其它E2增强也可能含带混合，不能只按一个Wu门槛给所有态分配声子数。
- 原表/稿本按激发能认同：1558keV编号、1292keV终态标签、正文与表中分支归一，
  都应保存差异，不在全库静默统一编号或取平均。
- 表4.8的1Wu=5.25e-7 e2b2脚注不直接复用。采用R=1.2A^(1/3)fm时，
  B_W(E2)=(3/5)^2*R^4/(4*pi)，A162约0.005246 e2b2；
  用0.64761MeV、tau1.2ps、光子分支0.497作中心值核算得约56.6Wu，原报57Wu。
  核算采用所列分支并忽略可能的小ICC修正，未重分析谱、未估计完整相关误差；不由相容性反推作者实现必定采用某一常数。
- 2181keV的delta0.24给E2份额约0.05446。文献强度1.13:1归一后，1217支约0.70Wu；
  单分支假设约1.32Wu；1292支用文献分支给约8.4Wu，与原表8.3/正文8.5的量级相容。
  1292的能差2180.69-1292.51=888.18keV对应2+gamma，但表延续页写3+gamma；保留冲突。
- GRID经验比例的讨论值不自动成为概率分布中心；不能按普通正态误差与DSAM合并。
  文献尺度差异需先核同态、单位、方法及feeding，不凭新旧年份裁决。

## Extracted Pages

- PDF1-2：自身题名、博士年月与仓储DOI；PDF21起实际正文页映射。
- PDF91-94：两核靶与入射能/角度条件；不将Dy的24g误套成Gd的29.4564g。
- PDF112-118：Winterbon、F误差传播、分支平均、CINDY/角分布与feeding边界。
- PDF125、146-148、190-193、210-219：低0+、双gamma数据、限值、混合和文献强度。
- PDF249-263、271-272、296-297：附录刊本/稿本身份、1599keV重估及编号差异。
- PDF317-319：GRID出版底本、实验路径、未知feeding极端范围与经验0.6比例。

## Open Questions and Transfer

- 本任务的拟议检验：在有原始谱和协方差时，比较保留带符号质心位移的完整似然与仅选正F分支的流程，
  检验寿命限值/覆盖率是否敏感；本轮没有证明作者流程产生何种偏差，也未运行该检验。
- 模式区分仍需互补证据：向gamma带的E2与带混合、E0/转移反应选择性、负宇称带的E3等，
  各约束不同自由度；不将每一种探针强制变成所有候选必须齐全的资格门槛。

## Knowledge Impact

- [[dsam-doppler-shift-attenuation-and-picosecond-lifetime-inversion]]：订正通用固定时间窗、
  “精确反演/对称误差/唯一模式检验”的过强说法；区分INS与重离子DSAM的输入和误差。
- 与[[ayangeakaa-2013-tidal-waves-chirality-thesis]]比较：该102Pd分析未含约20%停止系统误差，
  本文说明F的约10%不确定传播到tau；不是所有DSAM数据都能同样加/不加一个固定百分比。
- 稿件/实验谱系、方法和单位优先于标签；本轮不运行PDM，不将本文无P数据伪装成P-delta测量。
