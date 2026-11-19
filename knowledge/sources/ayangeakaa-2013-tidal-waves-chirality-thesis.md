---
type: source
title: "Ayangeakaa 2013 - Nuclear tidal waves and chirality"
aliases: ["Ayangeakaa doctoral thesis 2013", "Exotic modes of collective excitations"]
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: doctoral-thesis-experiment
reading_depth: read
title_original: "Exotic Modes of Collective Excitations: Nuclear Tidal Waves and Chirality"
authors: ["Akaa D. Ayangeakaa"]
year: 2013
institution: "University of Notre Dame"
doi: "10.7274/w9504x5422x"
url: "https://doi.org/10.7274/w9504x5422x"
canonical_source: "Notre Dame doctoral thesis, title page July 2013, CurateND Version 1"
raw_file: "raw/theses/gpt/query/20261119-international-nuclear-structure/AyangeakaaAD072013D.pdf"
raw_sha256: "d9f0edcf30c82d4f4fb6b4e3e5f46f88f67340daec76ce98e5095835cd24d1a6"
raw_storage_status: archived-local
archive_required: true
nuclei: ["102Pd", "133Ce"]
tags: ["DSAM", "tidal-waves", "chirality", "angular-distribution", "thesis"]
---

# Ayangeakaa 2013：102Pd潮汐波与133Ce多重手征候选

## Bibliographic Record

作者Akaa D. Ayangeakaa（仓储全名Akaa Daniel Ayangeakaa），导师Umesh Garg，
Notre Dame物理学博士论文。题名页July2013；仓储自身登记2013-07-18与上述DOI。
不把题名年月或仓储发布日期写成已核实的答辩/授予日期（PDF1-2）。

## Scope and Reading Depth

- Covered scope：186个PDF页由九个主读单元实际供给Gemini并返回；正文PDF20为印刷1，
  以后printed=PDF-19。章节入口PDF20/65/101/131/173/177经实际标题守卫核对。
- 主读中AY-FOUND-1因任务止于PDF42而partial，非未读输入页；管理层定向核PDF44-46，
  并与后续寿命/强度章节闭环。原worker状态不改写为complete。
- 管理层核关键原式、表、实验条件和解释边界；两次订正/草稿请求均ReadTimeout且无响应。
  本来源笔记由Codex从已返回主读缓存与定向原页证据整理，不冒称Gemini已交付草稿或八项订正。
- Not covered：未运行作者DSAM、RMF、PRM、GCM或PDM程序，未重分析事件、数字化全部曲线、
  逐篇核读外部引文。仅做明确列出的强度/角动量代数检查；记为read，不作全公式/代码认证。

## Summary

102Pd实验用DSAM寿命约束高自旋带内B(E2)的增长，作者将近恒定B(E2)/J与七个
自旋对齐d玻色子的潮汐波图像联系。133Ce实验建立两组同宇称候选伙伴带，结合
组态约束RMF和PRM作多重手征解释。两类工作均须分清实测量、推导量、模型结果与作者解释；
近线性趋势、近简并或模型符合都不单独提供排他机制证明。

## Key Results

| ID | claim_kind | evidence_level | locator | statement / boundary |
| --- | --- | --- | --- | --- |
| AY13-T1 | experiment / analysis | direct-original-pages | PDF113-121, Table3.2 | 102Pd的6+至14+寿命用于求向下B(E2)；16+寿命不能与侧馈分离，原文只作下限。 |
| AY13-T2 | author-interpretation | direct-original-pages | PDF123,129,174 | 七玻色子解释到I=14，n=I/2=7；16+可能是八玻色子延伸，不是“16+七声子”。 |
| AY13-T3 | uncertainty | direct-original-pages | PDF118,120-121 | MINOS统计区间与可达约20%的停止本领系统误差分开，后者未包含于给出的寿命误差。 |
| AY13-T4 | model-comparison | direct-original-pages | PDF126-129 | WS-SCTAC未对这组实验调参；几何GCM拟合低能谱且调整强度尺度，本文不能同时很好描述能量和B(E2)。不是所有同名模型永久失效的证明。 |
| AY13-C1 | experiment / analysis | direct-original-pages | PDF139-143, Eq4.1 | 实际低统计判据是any-gated后角/近90度强度比Rang，而非仅凭章节称DCO就套角度交换定义。 |
| AY13-C2 | model-input | direct-original-pages | PDF154, Table4.7 | RMF给态a的(beta,gamma)=(0.22,17.5度)，态b=(0.23,15.2度)，作为PRM输入；不是直接测得两种内禀形状。 |
| AY13-C3 | model-comparison | direct-original-pages | PDF155-165 | 负宇称带5-6与正宇称带2-3的比较支持作者的手征解释；正宇称例引入Coriolis衰减xi=0.7，不能称全模型无唯象输入。 |
| AY13-C4 | evidence-boundary | direct-original-pages | PDF158-159,169 | 绝对B(M1)、B(E2)为PRM计算；带x可呈约20keV近简并但连接未定，说明更近简并不自动意味着更可靠的模式指认。 |

## Experiment and Method

### 102Pd：寿命到电磁强度

ATLAS的76Ge(30Si,4n)反应，束能90MeV；500ug/cm2的76Ge、26mg/cm2 Au背衬，
中间11ug/cm2 Al阻挡层。实验时Gammasphere有98个HPGe探测器，收集约3.1e9个
三重及以上符合事件（PDF113-114）。这些是该实验条件，不是阵列永久规格。

BLUE角度/能量数据库、上方门与线形分析配合使用；DECHISTU模拟反冲轨迹，
停止本领取Ziegler编表并作低能修正。侧馈用五级级联描述；寿命、侧馈和谱参数先拟合，
部分本底/污染峰参数随后固定，再逐级纳入全局拟合（PDF114-120）。
原文MINOS描述包含对其它参数的重新极小化，不能仅抓住“fixing”一词称全部干扰参数始终固定。
原文未给完整协方差/逐态停止本领灵敏度，不保证系统影响只是统一尺度、不改变趋势。

Table3.2（PDF121，印刷102）的关键原始量如下；括号误差保留原报方式：

| I -> I-2 | E_gamma (MeV) | tau (ps) | B(E2) (e^2 b^2) | Qt (eb) |
| --- | --- | --- | --- | --- |
| 6 -> 4 | 0.836 | 1.15(32) | 0.174(48) | 2.36(33) |
| 8 -> 6 | 0.902 | 0.720(42) | 0.190(11) | 2.41(07) |
| 10 -> 8 | 0.980 | 0.409(28) | 0.221(15) | 2.56(09) |
| 12 -> 10 | 1.062 | 0.252(18) | 0.240(17) | 2.65(09) |
| 14 -> 12 | 1.083 | 0.201(11) | 0.272(+0.015/-0.022) | 2.80(+0.08/-0.13) |
| 16 -> 14 | 1.104 | 0.180(21), 原文寿命下限 | 0.277(+0.033/-0.042) | 2.81(+0.17/-0.21) |

14+、16+强度较大的负向误差计入XUNDL所列、但本实验未能确定的可能支路。
16+这一行不能当作与其它行同等确定的普通寿命/强度点。
Qt按所用K=0转动几何形式换算，不是独立静态四极矩测量或唯一内禀beta的直接测定。
原文Eq3.15为B(E2)=0.0816/[E_gamma^5*tau(E2)]，单位分别为MeV、ps、e^2b^2；
直接中心值核算与表相容。这不是重做DSAM；实际使用需区分总寿命与对应辐射部分寿命，
保留分支、内转换与混合成分，不能把未定支路置零。

PDF112脚注指出Ref107的6+绝对寿命约为本文两倍、相对强度比却相容；
这是作者对Kalyva等AIP831,472(2006)的比较，本轮未取得该引文的独立裁决。

### 102Pd：理论比较的输入角色

此处J_tw=2I/E_gamma，hbar=1（Eq3.17），并非与Chapter1中(2I-1)/E_gamma的
量子运动学惯量严格同式。B(E2)与J_tw近线性增长、B(E2)/J_tw在误差内近恒定，
支持作者以形变振幅增长为主的潮汐波解释，不等于微观声子数或唯一形状被直接测量。

WS-SCTAC使用通用Woods-Saxon参数；名称含TAC，但本例自洽解沿中间主轴转动。
几何集体模型GCM为Geometric Collective Model，不是Shimada的Generator Coordinate Method。
该例势参数拟合低能级比、能量按2+定标，B(E2)除以13.6作比较（PDF127）；
应记录尺度调整及剩余偏差，而非称作盲预测或断言所有四极集体模型不可能成功。
本文IBM-1例在大自旋强度下降，作者联系其五玻色子截断；结论限于所用模型空间与参数。

### 133Ce：实际角信息与模型

116Cd(22Ne,5n)、112MeV、两次Gammasphere实验（PDF137-139）。角矩阵的一个轴为all-rings、
另一轴为specific-ring；准各向同性单门提取角度谱，再作探测器数/效率归一。
统计足够处拟合A2/A0、A4/A0，Table4.2给出例如328keV的-0.812(32)、0.037(61)，
544keV的0.279(31)、0.161(30)（PDF143）。电磁性质指认仍含PDF97所述物理假设，
不能把角分布本身写成测得电/磁性质或线偏振。

Eq4.1（PDF141）字面定义Rang=I(backward,gated on any)/I(near90,gated on any)：
后角组121.7、129.9、142.6、148.3、162.7度；近90度组79.2、80.7、90、99.3、100.8度。
原文称该比独立于门跃迁多极性，已知M1约0.7、E2约1.3；不能直接换成另一套几何的DCO参考值。
本章未报告该分析所用取向宽度的数值，亦无P参与的定量delta联合提取；
未报告不等于固定sigma/I，不将本论文硬塞成P-delta测量来源。

RMF的态a/b计算激发能1.71/3.78MeV，所比带头2.378/3.734MeV（PDF154），
不能笼统说两者精确相等。PRM的正宇称例xi=0.7为经验修正；负宇称不需同样衰减，
不代表其它惯量、单粒子与电磁参数不存在。绝对强度曲线是模型；实验强度比不是绝对B值。
缺少明显交错被作者在该PRM框架下解释为手征振动，不是跨所有核的充分/必要判据。

## Competing Interpretations and Limitations

1. 潮汐波图像须与非简谐性、准粒子顺排及强度碎裂竞争；16+及以上不能由表观等间距外推。
2. 133Ce双带与模型相容不排除所有竞争机制；带x连接受污染/符合关系限制，不能认作第三对已确立手征带。
3. 同初态的辐射光子强度比可直接约束辐射率之比，不因比值公式未显式含ICC便判其错误。
   从总寿命/总分支求绝对辐射强度则需相应ICC和混合修正（PDF85-86及本任务代数区分）。
4. 本原件有内部公式不一致：PDF46 Eq1.46的K=0 CG系数平方缺少同页Eq1.47所含因子2。
   标准向下系数平方为C_I^2=3I(I-1)/[2(2I-1)(2I+1)]，I=2时为1/5。
   PDF121 Eq3.16按字面给Qt约1.67-1.99eb，Table3.2为2.36-2.81eb；
   后者与标准K=0 CG反解相容。管理层用直接阶乘Wigner3j和闭式交叉核算，
   不静默改原式、不据此推断作者程序错误或宣称已找到官方勘误。
5. PDF123 Eq3.19按印刷式在I=2给B_2/B_2=2；从该文恒B/J_tw及J_tw=2I/E_gamma应得
   B_I/B_2=I*E_gamma(2)/[2*E_gamma(I)]。Eq3.20的Grodzins式为向上0+到2+，
   用作向下2+到0+还需除以5。公式核查不是新增寿命测量。
6. 本论文与[[ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce]]复用同一实验谱系，
   不作两个独立实验证据。管理层另核本地PRL出版版PDF1：其事件数4.1e9、前层50ug/cm2 Al；
   论文PDF137-138为7.8e9、前层50ug/cm2 Au，原页图像均如此。差异原因未明，
   不强行以数据筛选/笔误解释，也不静默合并；今后实验设置优先出版底本并保留该边界。

## Extracted Pages

- PDF1-2：仓储自身DOI、作者、博士题名页及年月；不推断答辩日期。
- PDF44-46、85-86：四极矩/转动强度公式和辐射强度比条件；原式冲突不当教材定理。
- PDF112-123：既有寿命差异、实验设置、侧馈、MINOS、停止系统误差与Table3.2。
- PDF126-129：WS-SCTAC实际主轴解、几何GCM调整和IBM模型空间限制。
- PDF137-143：两次133Ce实验、原始计数/靶层表述、角矩阵、Eq4.1与角分布表。
- PDF154-175：RMF/PRM输入与比较、模型绝对强度、band x连接未定、作者总结边界。
- 另核既有133Ce期刊来源的本地PRL出版版PDF1，仅针对计数/前层材料，不重复记全文阅读。

## Knowledge Impact

- [[tidal-wave]] / [[tidal-waves-in-transitional-nuclei]]：新增原始寿命、系统误差及公式适用边界，
  与[[gu-2007-tsd-tidal-waves-thesis]]的早期理论/有限电磁证据比较；不按篇数投票。
- 133Ce层面：用Rang操作定义和模型/实测分层防止错标几何、绝对强度或形变；
  不修改另一session的P/ADO/DCO合同，不运行PDM或代替用户挑复算核素。
- 本轮拒绝“16+=七声子”“严格线性即唯一证明”“全模型无自由参数”“无ICC因子必错”
  等主读越界。保留来源依赖、印刷式冲突和未测量量，不把self-audit写成人工审核。
