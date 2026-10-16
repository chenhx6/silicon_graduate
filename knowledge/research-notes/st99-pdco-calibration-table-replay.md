---
type: research-note
title: "Starosta 1999：PDCO校准、五点表值与候选边界"
aliases: [ST99 PDCO calibration table replay]
created: 2026-10-17
updated: 2026-10-17
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [starosta-1999-pdco-experimental-test, droste-1996-pdco-formalism]
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
- [[dco-pdco-ambiguity-worksheet]]：本实验与独立point-response练习对照。

## Human Review

未获human review；本session完成source/claim self-audit，新增推断仍provisional，原source旧flags保留。本页定义缺口为研究边界，不自动转为用户待办。

## Promotion or Rejection History

- 2026-10-17：在Day15正式卡完成后的恰好Day16无学分预习中建立；source身份/Q修正与D96勘误可进入方法使用注记，表值replay/实际Cov原因仍open。无新Jpi、delta或集体模式赋值。
