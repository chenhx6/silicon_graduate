---
type: research-note
title: "Starosta 1999：PDCO校准、五点表值与候选边界"
aliases: [ST99 PDCO calibration table replay]
created: 2026-10-17
updated: 2026-10-17
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [starosta-1999-pdco-experimental-test, droste-1996-pdco-formalism, nndc-2018-164yb-pdco-reference-records]
created_from: Day15 daily-learning uncredited Day16 preview
promotion_target: dco-pdco-ambiguity-worksheet
tags: [pdco, calibration, covariance, table-replay, mixing-ratio, provisional]
---

# Starosta 1999：校准与五点重放的证据边界

## Research Trigger

理论PDCO模式可区分某些同DCO候选，但实际实验还须证明Q、a、geometry、alignment和观测协方差属于相同数据身份。本页核[[starosta-1999-pdco-experimental-test]]的实际164Yb实验，不再把D96的5→4→2作者模型当实验点。

## Grounded Evidence

- ST99-5/6：原始164Yb主采集、126Ba/114Cd/118Sn标定；Eq5的10^-5指数纠正旧Wiki转录。
- ST99-7/9/13：单CLOVER标定移用、四组polarimeter–detector、式7的五点/NDF和事件/校准依赖。
- ST99-8及[[droste-1996-pdco-formalism]] DR96-8：D96 Eq4已发表勘误，非实现坐标映射。
- ST99-10/11/12：表格重放缺口、647类别与自旋候选、独立转换观测和寿命推断边界。

## Assumptions

本页按原表的P/R与NDF计算，不回拟原实验；十进制舍入box和四P等相关Sigma均为明确选择的诊断模型。未取得unrounded producer output、实际joint response或totalCov，也不假定原P误差完全不含校准项。

## Provisional Reasoning

### 校准链与几何身份

原文定义为

$$P=\frac{W_\parallel-W_\perp}{W_\parallel+W_\perp},\quad
A=\frac{aN_\perp-N_\parallel}{aN_\perp+N_\parallel}=QP,\quad
a=\frac{N_\parallel(\mathrm{unpolarized})}{N_\perp(\mathrm{unpolarized})}.$$

W的parallel指电场，N的parallel指Compton散射；不是同一种标签。几何a与Eq6原文能量变量alpha也不同。所有P/A/Q/a/R都是无量纲。

EUROGAM-II有30coaxial与24CLOVER；本分析实际选18polarimeters，个体a在.95–1.05、合并在.99–1.01内，采用a=1。Q则另由NORDBALL79°的一台CLOVER测得，再近似移用。不同threshold/collimator/geometry可使Q不同；single-gamma Q不确定full joint gate response。

PDCO A/B组是CLOVER polarimeter与其它CLOVER standard segments的相对phi约0/180°及90/270°；C/D分别与coaxial22.4/157.6°及46.4/133.6°rings配对。integrated模式合并更大接受，其缺失立体角/效率未经修正时，作者只作定性比较。不能把integrated P再添为五点拟合的第六个独立datum。

Eq5/6的正确印式为

$$Q(E)=\frac{1+x}{1+x+x^2}\left[.31+7\times10^{-5}E_{\rm keV}\right],
\qquad x=E_{\rm keV}/511.$$

Table1的A/P中央值核算与表列Q在印刷精度相容；P来自已有角分布/GOSIA，不是独立无误差标准。490keV作者近似Q=.24时，.120(12)/.24=.50(.05)，这里误差仅随A传播。印刷central curve给Q=.23431434、P=.51213254、仅A的sigma=.05121325。两者输入精度不同，不能强求精确相同。旧10^-4若照用，会给Q=.444401、P=.270026；这是错误转录的负控制，不是另一条可用标定。

原文给拟合参数边际误差.31(2)、7(2)×10^-5，未给二者Cov及误差预算。本页不从这两个括号独立拼出Q置信带，也不将Q方差叠加在预算未知的printed P误差上。

### 五点式7与NDF

按`y=(P_A,P_B,P_C,P_D,R_DCO)`，原式是

$$\chi^2_\nu=\frac{1}{\nu}\sum_{i=1}^5
\left(\frac{y_i-y_i^{\rm th}}{s_i}\right)^2.$$

490观测为(.71,.33,.50,.54,.96)，误差(.08,.13,.08,.08,.02)；647为(.31,.29,.37,.34,.51)，误差(.15,.15,.12,.07,.03)。固定sigma/I=.26时Table2 pureE2的nu=5、mixed的nu=4；浮动sigma/I时Table3 pure4/mixed3，Table4全为3。这些是原文NDF；本页既不重新拟合delta/sigma，也不从同一表估计新NDF。

完整13行的原表score、逐字面重算和保守舍入包络如下。包络假设每个两位小数的观测均值、理论值及sigma均可独立在末位±.005内变化；score印值按±.05。它是一个条件rowwise十进制box，不是实际confidence interval，不断言各行包络端点可由同一组输入同时实现。

| 原表/路径 | nu | 原表score | 字面重算 | 舍入包络 | 与原表印刷区间相交 |
| --- | ---: | ---: | ---: | --- | --- |
| Table2 16+→14+ | 5 | 1.4 | 1.535558 | .841633–3.208676 | 是 |
| Table2 15+→14+ | 4 | 79.5 | 108.911451 | 92.243024–132.757156 | 否 |
| Table2 14+→14+ | 4 | .7 | .786636 | .588235–1.175289 | 是 |
| Table2 13+→14+ | 4 | 116.8 | 125.160988 | 106.149857–152.404267 | 是 |
| Table2 12+→14+ | 5 | 3.1 | 3.345137 | 2.633874–4.489387 | 是 |
| Table3 16+→14+ | 4 | 1.4 | 1.406481 | .611100–3.408889 | 是 |
| Table3 14+→14+ | 3 | .7 | .786767 | .523958–1.303704 | 是 |
| Table3 12+→14+ | 4 | 1.1 | 1.229960 | .767028–2.322489 | 是 |
| Table4 11−→10+ | 3 | .6 | .583932 | .444473–.824878 | 是 |
| Table4 9−→10+ | 3 | 1.2 | 1.172396 | .912402–1.633167 | 是 |
| Table4 11+→10+ | 3 | 4.8 | 4.917356 | 3.915518–6.355913 | 是 |
| Table4 10+→10+ | 3 | 7.7 | 7.830478 | 5.740165–11.195591 | 是 |
| Table4 9+→10+ | 3 | 9.2 | 9.016788 | 7.425846–11.168126 | 是 |

若d_i=|y_i−t_i|、h=.005，则本模型的每行包络由

$$q_{\min}=\frac1\nu\sum_i\frac{[\max(d_i-2h,0)]^2}{(s_i+h)^2},\qquad
q_{\max}=\frac1\nu\sum_i\frac{(d_i+2h)^2}{(s_i-h)^2}$$

给出。Table2 15+行在此相当宽的印刷末位模型内仍不闭合。**保留原79.5**；未知unrounded minimum/理论输出/误差处理/producer代码使原因不可归定，不能静默把它改成108.9、放松容差或判作者错误。其它12行区间相交也只表示这个舍入模型未排除，不等于已重放原程序。

### 共享校准的chosenCov敏感性

四个P使用同一线Q/a及重叠gate/events，DCO也可能复用事件。原式的对角近似不能证明实际五维Sigma对角。为检查结论对未知相关性的依赖，本页只选

$$\Sigma=D\,\operatorname{diag}(C_4(\rho),1)D,\quad
C_4=(1-\rho)I_4+\rho\mathbf1\mathbf1^T,$$

D为印刷边际sigma，rho取−.2,0,.2,.5,.8，均正定（−1/3<rho<1）。它保持边际误差，不在其上再加一份Q方差，也不被称为实际Cov。共享common模式和三个contrast模式的惩罚随rho不同；数值矩阵逆解与解析分解核验一致。

| Table3候选 | rho=0 | rho=.5 | rho=.8 |
| --- | ---: | ---: | ---: |
| 16+→14+ | 1.406481 | 1.803495 | 3.004560 |
| 14+→14+ | .786767 | 1.569083 | 3.920744 |

在这组**自选**Sigma中两候选score排序可改变，证明仅有printed marginal errors不足以认证actual joint排序。这里没有p值、posterior probability、新delta置信域或新最优alignment。零相关只恢复字面式7，不替代共享事件/背景/校准的实际估计。

### 能分解候选的必要观测

490keV在原文保留16+→14+ E2与14+→14+ M1/E2、atan(delta)≈−21°。正P与R≈1没有唯一性；继续测同数据的ratio改写不提供独立识别。原结论建议转换观测，两假设预测为印刷`alpha_κ=.012/.033`。本页保留该下标，原文在此未另定义壳层，不将其补成total ICC或未经核定的指定壳层，也不将预测写作已测。

下一项有区分力的实验须报告同一490keV branch的电子/γ净计数、转换壳层、效率和背景、竞争分支/E0允许性、原子修正和joint errors；先确认预测与观测是同一个alpha量。亦可用独立spin/level证据，但需逐实验标数据依赖。

647keV的Table4中11−与9−初态都给较低score，共同为|ΔI|=1 E1类别；它不是PDCO唯一选择11−的证明。.26(5)又是以同647 DCO及先验已知11−→10+ E1求得，不能当独立alignment prior再循环强化该指认。

E1/M2 alternative的≥4ns来自Weisskopf和推荐强度上限；无预期约.9keV Doppler偏移/展宽与约400ps飞行作反证。速度.0163/.0183等属于作者setup计算。这里既有transition-strength假设又有响应检测前提，不是直接寿命测量或无需效率的普适上限。

## NNDC实际参考记录：有寿命不等于已测490转换

[[nndc-2018-164yb-pdco-reference-records]]保存本session新取得的三份官方对象、原始text hash和sourcekeys；不是第二个164Yb实验。三者header201712、评价2018/cutoff2017-11-30，2026只是retrieval date。ADOPTED高spin E/RI主要采用1995NO04，AD/ce主要追1986JO02；BrIcc理论字段与实测字段分层。

| 同一目标 | ADOPTED | 152Sm16O对象 | 124Sn44Ca合并对象 |
| --- | --- | --- | --- |
| 490 parent/γ→ground14+ | 3388.98(13), J=(16+)；489.8(1)→2899.20(13) | 3389.26(18), J=16+；489.8(1)→2899.48 | 3390.0,16+；489.9→2900.1 |
| 647 parent/γ→ground10+ | 2400.80(12), J=(11)-；647.4(1)→1753.35(11) | 2401.09(17),11-；647.4(1)→1753.63 | 2401.2,11-；647.3→1753.9 |

三种level-energy基准不应当独立加权平均；source都做LS fit且采用的low-spin anchors不同。selectedground references的ADOPTED减152Sm差为−.28/−.26/−.34/−.28/−.28/−.29/−.28keV，未给jointlevel/γcalibrationCov。字面target490/647在ADOPTED的energy residual为−.02/+.05keV，只做identity sanity，不是χ²或placement的唯一证据。附近492.6/491.8/650.4/645.7等属于不同parents，不能只靠最近energy取记录，也未据此宣称ST99实测峰被污染。

### 647的实验EKC与490的理论KC不能互换

152Sm对象G647.4明确写`EKC LT 0.0042`，缺省来源为1986JO02，未给CL；同时的CC=.00351(.00010)、KC=.00298(.00009)是BrIcc Frozen Orbitals。其MR=+.016(.026)对应**M2/E1**，不是别的M1/E2 δ。ST99本已用该647已知性质校准sigma/I，数据库再引用它不能变成新的独立确认。

G489.8在所查块没有EKC；CC=.0188、KC=.01475(.00021)均为理论字段，来自采用E2而非测量证明E2。ST99原alpha_κ预测的历史shell notation边界仍保留，不用这些theory数值倒推一份不存在的490实测ICC。现在的高信息下一输入仍是matched shell/electron–γ measurement或其它独立spin约束。

### 母态时间与derived strength的使用门

ADOPTED母态与124Sn对象均列T1/2=1.75(.35)ps；换成mean tau为2.524716(.504943)ps，lambda为3.960841e11s^-1（局部sigma=.792168e11）。这是同一时间的定义换算，非两次测量。Ca对象以1996XI01为main reference，但它混收RDDS、DSAM及quasicontinuum工作，g.s. global规则不能替sideband行自动确认primary fit定义；原文/feeding/response未得。

ADOPTED的BE2W=210(50)沿采用E2与branch/time模型导出，不能反过来作δ选解的独立证据。302.3的CC/M空白保留unknown；同parent RI比，ADOPTED2.9/100=.029，reaction.8/27.2=.029412，主要是同primary强度的rescaling，未给Cov。原ST99 alternative atanδ=−21°只给radiative component fractions M1=.871572、E2=.128428；它不是整个state的decay分支。若改变候选，必须同时改变其ICC/γbranch/strength model，不能沿用pureE2 CC或直接把210乘.128当新B(E2)。

### 隔离的reaction metadata冲突

ENSDF152Sm对象的secondary comment写150Sm(16O,4n)，质量平衡只到162；NSR1986JO02及Lund作者机构abstract均写150Sm(18O,4n)，可到164。raw如实保留16O的原行；本任务不把它定义为另一个164采集，不从这处comment推广错nuclide。primary全文尚未取得，机构abstract属于外部核验的摘要/metadata层。可靠主152Sm(16O,4n)与三对象header身份不受该隔离冲突影响。

[冻结crosswalk input](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-n164-record-crosswalk-input.json) hash `d412f15d95efeb69ba48a18d95f2ef790eb5561cc6e4de1afbb8ddb90bd6138c`，[脚本](../../system/scripts/day16_n164_record_crosswalk.py)与[结果](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-n164-record-crosswalk.json)核三raw、fixedcolumns、unknown和unique selectors；首轮col77 comment flag的off-by-one在无numeric output时失败并修正，原selectors/raw不变。actualevent/response/Σ/302ICC及两primary body仍缺，实际L4未开始。

## Competing Explanations

表值重放差异可能涉及未公开的unrounded producer output、表列值与minimum的对应、误差预算或原出版转录；现有输入无法选择其一。未知Cov不是事后强行使79.5成立的拟合旋钮。物理候选歧义、相位约定错误和印刷表重放缺口分别保留。

## Transfer Conditions

迁移Q或PDCO必须重核能量单位、a/Q、threshold、collimator、ring/pair/gate、初始alignment及误差谱系。Eq7本身可复用为诊断，但source的对角/五点/NDF不自动适用另一实验。

## Failure Conditions

输入v1未报告的647 A、旧错误Q指数、把integrated P另算一份独立datum、把同647DCO校准当外部prior，都会破坏此推断合同。只给print marginals或single-gamma Q不能声称actual joint fit已重放。

## Falsification or Reverse Tests

取得unrounded theory/minima与实际recipe后，应直接重算式7，并以同一输入核对published79.5；若可闭合，则修订本页ST99-10的replay boundary及其原因。取得event/背景/calibration的真实Sigma后，替换chosen模型检验候选排序；与同量alpha_κ的独立转换观测匹配后再判断两分支。

## Open Questions

1. 原程序的unrounded minima、Table2每行预测及实际误差预算是否可获得？这直接决定ST99-10缺口能否闭合。
2. Q/a/ring效率、pair selection、背景与共享事件的完整Sigma如何构造？NORDBALL单台曲线不足以回答。
3. 原结论alpha_κ的明确壳层定义、对应原子系数来源及匹配独立490keV转换数据是什么？未核同量前不设计虚假的精度要求。

## Reproducibility

- 正式使用[冻结输入v2](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-st99-calibration-table-input-v2.json)，SHA-256 `651c05306a16d12d6121d4e7d097e6906d8d541d2f26d1232eb3aba9b1f4fe6a`。首版agent误填未报告的647 integrated A，已在任何数值脚本前移除；[纠正记录](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-st99-input-correction.json)保留其身份，首版不得作来源输入。
- [复算脚本](../../system/scripts/day16_st99_table_replay.py)与[完整结果](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-st99-calibration-table-replay.json)记录script/input/raw hashes，核原PDF SHA-256 `883fdd7b08831efefe25f5df610e84b95bb1acbcd7b8e7f684b1a1b31bf8030b`。primed回忆/coverage另留本run，不冒称盲复现。
- 这是公开印刷表的L2校验和L3观测设计；无events/producer/actualCov，实际L4重分析未开始。新推断保留provisional/needs_review，不继承旧ST99-4或旧人审范围。

## Sources

- [[starosta-1999-pdco-experimental-test]] ST99-5–13；原子入口分别见上文，不把组合ID充作单一locator。
- [[droste-1996-pdco-formalism]] DR96-8：已发表Eq4勘误；理论与实验复用边界。
- [[nndc-2018-164yb-pdco-reference-records]] N164-1–13：三个官方selectedobjects、EKC/理论CC、time/RI/strength依赖与隔离的secondaryreaction冲突。
- [[dco-pdco-ambiguity-worksheet]]：本实验与独立point-response练习对照。

## Human Review

未获human review；本session完成source/claim self-audit，新增推断仍provisional，原source旧flags保留。本页定义缺口为研究边界，不自动转为用户待办。

## Promotion or Rejection History

- 2026-10-17：在Day15正式卡完成后的恰好Day16无学分预习中建立；source身份/Q修正与D96勘误可进入方法使用注记，表值replay/实际Cov原因仍open。无新Jpi、delta或集体模式赋值。
