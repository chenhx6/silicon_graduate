---
type: learning-report
graph-excluded: true
created: 2026-10-14
updated: 2026-10-15
---

# DAY14 第二次周考：从谱到能级纲图

## Run state

- run_id: `2026-10-14-day-14-02`
- run_date: `2026-10-14`；timezone: `Asia/Shanghai`
- day_index: 14；phase: `gamma-spectroscopy-and-level-schemes`
- schedule_id: `wiki-daily-learning`；run_kind: `substantive / weekly-learning`
- session_id: `01a13a0e-e8bd-7251-b970-f6975679e281`
- resume_command: `codex resume 01a13a0e-e8bd-7251-b970-f6975679e281 -C /workspace/wiki -s danger-full-access -a never`
- overnight_until: `2026-10-16T16:00:00+08:00`；用户因断网明确延长至次日16:00最终交付；预留15:00–16:00收束，不延到17:00。原截止`2026-10-15T15:00:00+08:00`保留为历史。
- planned_research_cutoff_at: `2026-10-16T15:00:00+08:00`；15:00–16:00仅closeout。
- research_status: active-user-extended；15:37曾按原截止转closeout，15:45用户明确加时并恢复，当前截止2026-10-16 16:00上海。中间未观察时段不补造研究。
- completed_day_indices: [14]
- partial_day_indices: [15]
- Day 14 card audit: complete
- Day 14 scorecard: complete
- Day 14 weekly REFLECT: complete
- course_credit: 尚未推进；需report/writeback/checks/continuation/publication通过后才计Day14，持续研究不重复计卡。

本次session身份由run-02 `events.jsonl` 的thread.started与原生goal threadId交叉确认；补记receipt和scheduler事件。run-01是此前已取消的另一session，不接管、不自动重启。恢复任务使用用户已给出的持续学习、写入与Gitee授权，Farmer只监督allowlisted瞬时错误，没有Git角色。已有Day6–9/Day13回执、旧log与daemon修改保留。

### Day 14 card completion audit

| 课程交付 | 本次artifact与精确evidence locator | 状态 |
| --- | --- | --- |
| 来源前画三层级联、门条件与DCO/偏振/寿命位置 | [冻结回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/active-recall-before-sources.md)，三层图和六条原答；保存后才打开source/raw，明确primed | complete |
| 沿全文主线核验一图一表 | [[herzan-2015-193bi-spectroscopy]] HE15-4/8，PDF p.3与p.7 Table I / p.8 Figure2；本文pp.1–20主线回读，关键图表视觉核验 | complete |
| 重建子纲图并逐线分级 | [[level-scheme-reconstruction]] “Day14 五能级七跃迁逐边审计”，七条E/C/M/J证据；HE15-4、HE15-8 | complete |
| 理论/定量练习 | [fixture](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/level-scheme-fixture.json)与[analysis](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/level-scheme-analysis.json)，35项检查；HE15-4/8/9/10/12 | complete |
| 可能重排纲图的反证与必要伴随观测 | HE15-9，PDF p.7 Table I footnote f；HE15-5 p.10 Fig.5；方法页“标定、寿命与伴随观测的逐项契约” | complete |
| 实验判据矩阵、六维评分和weekly REFLECT | 本文对应三节；[周度回执](../learning-weekly/20261014-week-two-spectrum-to-level-scheme-reflect.md)；canonical方法页“第二周证据链的可复用认识修正” | complete |

## Candidate pool and selection

连续性问题是“能量闭合和共同门能否唯一指定跃迁身份、顺序与Jπ”。Day14课程明确指定Herzáň或Ding；选择Herzáň193Bi既便于正式复核昨日预习，又与近期A≈130/C/O Doppler工作的核素及采集不同。正式卡要求覆盖同一source，所以这是记录在案的cooldown exception，不能继承Day13预习19/24或其学分。

| 候选 / coverage | 信息增益与选择 | 当前边界 |
| --- | --- | --- |
| 193Bi一图一表、Band1五level七边 | continuity selected；将单三层closure扩为相关cycle审计，查到319.8-keV表尾行 | 没有逐对事件/Σ，不重新评价实验能级精度 |
| 393.4/394.0双线顺序与shared R/A | 同一continuity问题的直接反证；能量和和允许ΔI均不解除未定顺序 | 需要独立endpoint、branch、time或tag |
| a(E)/Q(E)、isomer assignment与parent lifetime | 同一证据链必要companion；明确source实际DCO定义及条件性spin | 无原counts，反事实不重估作者误差或δ |
| SD floating X、1836-keV tentative link与46/87-keV非观测 | 检查原论文结论边界；保留model/作者解释 | 无confirmed link/absolute strengths，不能确定X或形变 |
| Ding127/128I再做同类闭合 | deferred；近期已作反应/谱系，当前未定双线更能检验方法 | 不是用重复来源充填novelty |
| Day15 ADO知识预习 | 当前shared-POL必要域已固化，转向相邻卡的geometry/gate修正与误差可识别性 | partial15；不计卡，实际matched-gate/response/covariance仍缺 |

最近学习覆盖：Day8选律/δ约定，Day9寿命/branch→strength，Day10双带电磁指纹与谱系，Day11–12反应布居/符合背景，Day13 Doppler/速度/停止/统计，均以既有日报与canonical知识页定位。当前不把这些日报用作新的实验来源，也不从数量推学习饱和。另一个非重叠novelty问题未强行选择。

### 延期候选池：从模型转回实际寿命提取

Matev2007局部算符/表检验完成后，选择Riley2001公开作者实验报告补actual extraction，而非继续变换同一toy。它回答恒定Qt、gate/侧馈、systematics与数据谱系，预期增益高于重复J^(2)或同一overlap计算。Laird2002最终全文、Ce/Sm外源原实验仍缺；已失败获取路线不原样重试。193Bi当前static/time/recoil问题局部饱和，实际events/τ/response/Σ未得；Day15的下一卡只作已记录的无学分预习，不开Day16。

### Active recall 与 priming

来源前答案完整保存在[冻结回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/active-recall-before-sources.md)。已读运行prompt/handoff中的昨日预习摘要，所以明确为primed recall；未凭记忆填Herzáň具体能量、R/A或误差。原答正确指出共同门、相对能量自由度、阵列特定DCO、P/A/Q分离和parent lifetime，但尚未写出三个cycle的相关性或本文未定双线表注，这些由正式读图/表后补足。

## Sources and evidence

| 来源 / 身份 | 本轮实际覆盖与locator | 证据分层与独立性 |
| --- | --- | --- |
| Herzáň et al., PRC92,044310(2015), DOI[10.1103/PhysRevC.92.044310](https://doi.org/10.1103/PhysRevC.92.044310)；citation key `Herz__2015`；raw SHA256 `f727485ad0f52269a66b27272dac75d34d9e67aaf8b073631cfeac5fe81d3aea`，20页 | pp.1–2动机/setup/tagging；pp.3–7全部Table I；pp.8–9 Figure2；pp.10–15各带/isomer/SD；pp.16–20组态、systematics、结论、引用。视觉核p.3/7/8/10/15 | 一次JYFL193Bi acquisition；Table I/Figure2/Figure5是dependent图表/投影；153-ns bandhead引用Ref7，非本次七线parent的新τ |
| 外部结构化Crossref核验 | [metadata回执](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/crossref-herzan-metadata.json)，作者/题名/2015/卷92/DOI一致 | 元数据核验，不是独立实验；返回pages为空，文章号由PDF核验 |
| Canonical source与方法 | [[herzan-2015-193bi-spectroscopy]] HE15-4–14；[[level-scheme-reconstruction]]新增逐边、cycle、topology、companion sections | 实验测量、联合赋值、作者解释、模型和任务推导分开；旧needs_review全保留 |
| Zheng2002原扫描全文；DOI留空，身份由期刊页眉与rawhash核验 | [[zheng-2002-ado-coincidence-angular-anisotropy]] Z02-1/6/7/8；PDF pp.1–5，重点p.2 Eq1–5、p.3 Fig1/效率、p.4 Fig2/Ref3 | Day15无学分预习；f的计算偏离与实验标准误差分开；Ref3 DOI [10.1007/s100500170001](https://doi.org/10.1007/s100500170001)仅metadata，2002文依赖对应145Tb实验 |
| Rose–Brink1967方法依赖局部复核 | [[rose-brink-1967-phase-defined-angular-distributions]] RB67-11，printed316/PDF11 Eq3.24/25；RB67-4，printed320/PDF15 Eq3.40/41的既有直接核验；本段视觉回核printed326/PDF21 Eq3.69–3.73 | formalism，非193Bi新数据；初态polarization、photon helicity、detector sensitivity与ENSDF Q分别定义 |
| Zobel1983，DOI [10.1016/0167-5087(83)90649-X](https://doi.org/10.1016/0167-5087(83)90649-X)，citation key zobel_1983_Energyprojectile | [[zobel-1983-energy-projectile-alignment]] Z83-11/12/13/14；六页printed389–394全部视觉主线，Eq1–3、Table1、Fig1–5/refs；rawhash/metadata回执在本run | 67Ga published fit coefficients；新分析为Codex self-audit，原Jul08人审/旧flags保留；Ref4 purity/structure和Ref5方法依赖不能重复计采集 |

主要定位：HE15-8是Table I p.3/p.7及Figure2 p.8；HE15-9是p.7 footnote f；HE15-10是p.7 a定义及p.10 Figures3/4；HE15-11是p.13条件性29/2+赋值与p.14 conversion；HE15-12是p.10 Ref7寿命与p.3相对强度；HE15-13是p.19 conversion/SD解释。源页保存每条claim的locator，不用搜索片段当证据。

### 延期方法companion：109Ag可分离配对

[[wang-2017-109ag-tac-separable-pairing]] 为精确DOI10.1103/PhysRevC.96.054324、arXiv1708.06117v2，公开PDF9页SHA256 `15e901a4f5d8ad1b5cf4bffe61e050d8eb6a3c89b0f9f62dea84e5d56c335d87`。来源前回忆见[primed recall](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/tac-pairing-before-sources.md)；沿9页全部主线、Figs1–8和影响判断的理论/附录公式读并视觉回查，详见[reading audit](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/tac2017-reading-audit.json)。本次未归档raw、citation key未匹配，source明确保留槽；所读不是已核正式排版。

W17-1/3/5把RHB的U/V、轨道追踪/阻塞、未恢复粒子数与组态简称分开。其109Ag和Lv2025的136Pr是不同核素/输入；W17-13的实验点回引Datta2008，本方法并非新Pr136采集。W17-7保留回弯区不收敛；W17-9保留磁矩Dirac项处理，不能只凭拟合好转认定唯一机制。全文未给Pr136 Q1的actual blocked/spectator。

1996前作另试direct arXiv/HAL公共入口：未加引号DOI返回不匹配文章，不能计精确结果；修复为quoted DOI、title+author与HAL title后均HTTP200/0精确结果。回执`petrache96-query-repair-before-source.json`与三个repair结果保留。没有取得全文，也没有推断263/405差异原因。

### 2015上游阻塞定义的直接核验

[[zhao-2015-pairing-spin-orientation-tac]] DOI10.1103/PhysRevC.92.034319、arXiv1506.08340v2，公开PDF13页SHA256 `ce3c7672420b07e9bbe7d7a869049771c5cef9aa64f4dffce5dfd18bcb0b3c21`；Crossref完整题名/作者与PDF首页一致，arXiv API缺题名末词的元数据差异保留。来源前[primed recall](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/tac2015-blocking-before-sources.md)已先保存；全部13页主线、Figs1–5和PDF5 O1/O2字面方法核验见[reading audit](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/tac2015-reading-audit.json)。raw未归档/citation key空明确保留，未把元数据license当OA证明。

ZT15-3/4直接给出分开归一U/V、分别最大化O1/O2及继承/反转blocking；ZT15-10限定xz平面，l–i/l–s变化与上游chirality解释分层。ZT15-12的谱和强度点重用2003/2007实验，本理论不是新Pr136采集。

### 136Pr的γ/axis定向回读

[定向回读前primed recall](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/pr136-gamma-before-focused-reread.md)及[原文定位](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/pr136-gamma-focused-source-note.md)在量化前保存。[[lv-2025-136pr-tac-covariant-density-functional]] LV25-33的PDF15 TableII给D4(.17,35°)/D6(.19,39°)，Fig16仅显示0–60°扇区；PDF12的D4负γ/medium与D6正γ/short明确是alternative共存解释，并用了irrotational-flow假设。没有逐态signedγ/axis map，不能把source模型图和alternative直接合并或给D4自行改号。

### 直接γ/axis伴随源：Petrache2015

[[petrache-2015-nd-exotic-rotations-triaxiality]]，PhysScr90,114016，DOI10.1088/0031-8949/90/11/114016。公开出版商入口实际取得PDF4页（cover+正文3页），SHA256 `cc6f8b952b32ff32b462987cc86f9417a0cb8702b16bc797231356b153ca5b35`；身份、全文主线、Fig1/Table1和讨论均核验。[来源前回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/petrache2015-gamma-before-source.md)及[reading audit](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/petrache2015-reading-audit.json)保留priming。下载器把TDM链接当OA证据的标签未采纳，只称成功取得出版商PDF；raw未归档/citation key空明确保留。

PT15-5是负/正γ对应中间/短轴的模型语境，PT15-6明确要求寿命来检验其真实与否；没有Pr136实际frame。PT15-4的J2图和均值有不同选带/interaction/频率/低组图示删点规则，不能忽略这些边界把51/23分组当唯一γ测量。此为二级Nd系统学，不是新独立Pr136实验。

### 直接能级链与有限差分来源

回实际[[lv-2025-136pr-tac-covariant-density-functional]] TableI/Fig1得LV25-34/35：同3937.2-keV15+母态经207.8/265.0接不同14+；D4的16–23子链及crossover两条signature需按graph选。[[peng-chen-2022-chiral-rotation-rhodium-isotopes]] PC22-19另定向核原PDF6 Eq2/3与ω句，确为跨两条γ的source-specific式，保留其原频率标签。[source audit](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/pr136-inertia-source-audit.json)明确此轮未重做PC22全文或新实验。

### 可读的理论/实验谱系伴随源：Matev2007

[[matev-2007-a130-quadrupole-alignment-additivity]] DOI10.1103/PhysRevC.76.034304、arXiv0707.4324v1，14页PDF SHA256 `40d485c653f2016cd6dc38ef95a7694e9ced6d09458004039b5be92541d07586`。沿全文主线、Figs1–6、TablesI–III与关键公式/误差/引用链读，[reading audit](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/matev2007-reading-audit.json)记录v1/未核VOR边界。[来源前回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/nd-qt-companion-before-source.md)保留metadata前后修正；不能把此理论研究先当新τ实验。

其数据比较回指Riley2001/Laird2002，计算以131Ce HD奇A core、无配对和固定ω=.65 MeV的183/105筛选配置为范围。Qt坐标/算符、模型fit errors与上游实验分开；PT15-10另核其Ref32/46指同一Laird文献，不新增独立测量。raw未归档/citation key空明示。

### 原始作者实验报告：Riley2001

[[riley-2001-global-lifetime-a135]]：*Acta Phys.Pol.B*32 No9,2683–2695(2001)，[publisher PDF](https://www.actaphys.uj.edu.pl/fulltext?series=Reg&vol=32&page=2683)，13页416810 bytes，SHA256 `09d58089a1985ef9d3d02432921b302a77c5d51eca9846bdea03dd9330d0d036`。实际刊头No9优先于初guess URL；DOI未核，不猜填。raw未归档、citation key空保留。读前[primed recall](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/riley2001-before-body.md)及[量化前预测](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/riley2001-before-calculation.md)已冻结；13页主线、Figs1–3、TablesI–II和关键公式/误差视觉核见[reading audit](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/riley2001-reading-audit.json)。

RI01-1–5（印刷2687/2690）直接核173MeV35Cl+105Pd、97HPGe+Microball、centroid-shift DSAM/FITFTAU与恒定Qt/侧馈/门选。RI01-6–8/14的p2690 TableI按角色保存完整33行。RI01-9/15（Fig2/3 captions、Refs21/24/32）区分同global acquisition与外源Ce131/132及Sm142；相似backing/分析不证明全图同采集。本报告的Ref21是Clark1996，不是Matev2007 Ref21=Laird2002；2001 invited talk不能自动替代2002最终稿。

RI01-11（p2691 Eq3和紧接归一）回图核`Q22_code=−sqrt2 Q22_R`；文字提取漏负号。RI01-12（Fig3/TableII）7.75/7.57eb是理论core、183/105是计算配置，不是新实测Qt或band数。

### 本地原件定向补读：Petrache1998

[[petrache-1998-highly-deformed-lifetimes-131ce-nd]]，DOI[10.1103/PhysRevC.57.R10](https://doi.org/10.1103/PhysRevC.57.R10)，PRC57,R10–R14(1998)，citation key `petrache_1998_Lifetimemeasurements`。本地raw原5页SHA256 `9d2297ed085012d2f8633a5faecfa7020cbca96ac06cf2eb5e88d97a24b90e5f`与既有source一致，Crossref身份/刊头核合。沿5页全部主线与refs，视觉回核PDF2 Figs1/2、PDF3 TableI/脚注、PDF4模型/限制，见[reading audit](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/petrache1998-reading-audit.json)；[读前回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/ce131-reference-before-source.md)和[量化前预测](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/petrache1998-before-calculation.md)明确priming。这是已ingest实验的on-touch补核，未新增实验。

PE98-14核TableI脚注6.07的估算角色，PE98-15分开八表行/五当前带/一外源，PE98-16/17核channelβ与可见top归一，PE98-18保留feeding文字范围，PE98-19核本次131Ce7.3(4)与转引Clark7.4(3)。Matev Ref39实际为ClarkPRL76,3510(1996)，Petrache不是7.4的原始出处。

Clark精确metadata已核，但本地无source/raw，OA-only `nature-downloader --no-si`返回0下载/oa_not_found；工具的confirmed_oa标签与其Unpaywall false/APS default license不相容，未采纳为OA证明。Scholar工具timeout、OSTI SSL失败（未关闭验证）、OpenAlex closed/noPDF，见[取件边界](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/clark1996-access-boundary.json)。尚未读Clark原文，不用metadata/snippet生成科学claim。

## Theory/analysis exercise

七边的中心值闭合为`+0.2,+0.4,+0.3 keV`。D的rank4、三个cycle、绝对offset nullspace均由代码核验。独立0.1-keV拟合误差下条件χ²=6.666667；自设将caption约0.3 keV按quadrature加上、并令各线独立后，χ²=0.666667，dof3。后者cycle Σ为`0.1×(3,1,0; 1,3,1; 0,1,3) keV²`，不是三个可相乘的独立检验。

独立whitened least squares与cycle-space χ²相等；共享gain取消、共享加性offset保留；换row顺序结果不变；刻意错移一条crossover的失败检查能检出不相容。393/394换序演示同时保留upper=2045.5 keV，但intermediate差0.6 keV；这些不是修改后的实验能级。SD链rank13/14说明未知X仍为自由度。

依原文a(E)重算：a(323.4)=1.0955364，A=−0.012对应条件N⊥/N∥=0.8911476；错误令a=1会得−0.0575589。不是新偏振测量，未从公开表反推原始counts。三个same-parent photon-intensity ratio为2.132231、1.921569、1.157407；没有τ/ICC/δ/branch completeness，均不转换成absolute B或total branch。

执行命令：

```bash
python3 system/scripts/day14_level_scheme_audit.py --fixture outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/level-scheme-fixture.json --output outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/level-scheme-analysis.json
```

实际exit0，35/35检查通过。核心公式、数值与适用边界的canonical副本在[[level-scheme-reconstruction]]，run-dir保存输入转录、代码结果与哈希回执。

### 实验判据矩阵

| 命题层级 | 本次可用观测 | 可支持范围 | 仍需信息 / 失败条件 |
| --- | --- | --- | --- |
| emitter/line identity | reaction、RITU/GREAT tag、Figure5 matched gates | 作者归属的193Bi谱线 | random/target污染、quadruplet、299.2/299.8response必须控制 |
| placement/order | γγ/γγγ、Figure2、Table I、energy sums | source-level七边子图 | 双线order、共享祖先门与共用calibration不能只靠closure裁决 |
| multipolarity | setup-specific Rexp和校正a(E)后的A | 支持作者M1/E2赋值 | δ、高阶、alignment、gate/response；shared-doublet值不识别每一line |
| Jπ | multipolarity加可信anchor、conversion与parallel path | 有条件沿图传播 | HE15-11明确依赖Band1；不凭RDCO或偏振单独量出absolute spin |
| τ/absolute strength | 本文isomer时间与conversion；先前153-ns引用 | 对对应isomer建立更强链 | 不能把bandheadτ赋给七边parent；需各parent τ、全branches、ICC、δ |
| configuration/shape/mode | alignment/ratio/systematics、作者semi-empirical模型 | 受约束解释和candidate | SD absolute strengths与confirmed link仍缺；没有新的A≈130模式判定 |

### Continuity checkpoint：conditional gate 与复合峰

正式周考发布后继续同一问题；[计算前预测](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/gate-design-before-analysis.md)与[37-check设计结果](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/conditional-gate-design.json)保留顺序。代码 `system/scripts/day14_conditional_gate_design.py` 实际exit0、37/37；64状态枚举与5×10⁶-event独立MC的mean/second moment最大z≈2.18。b/h/效率/σ/parent数量全为自设、无IC/feeding/angular correlation的限制模型，不是193Bi数据。

已知纯A=622直接支与B=323级联门的conditional系数时，两门可解除同response两强度参数的rank1退化；A门效率→0、b→1或比例污染则失败。若只保留两张合并峰总面积且b未知，存在连续physical等价族；完整可分的joint energy spectra并不只有这两个信息。shared-event双γ在B门下产生positive covariance，固定N与Poisson parent flow的Σ不同，不能把每个line/gate都当独立Poisson。

HE15-13低能γ的设计例（N=5000、ε=.01、branch=1）给46/87-keV零计数概率0.826/0.0268；没有实际flow/efficiency/背景，这不是sourceupper limit。完整公式/数值/边界已canonical写回[[level-scheme-reconstruction]] “互斥分支门、复合峰与shared-event计数”。

### Day15 无学分ADO计算与误差图

来源前primed回忆见[预习原答](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/day15-preview-before-sources.md)。Zheng2002扫描件5页已视觉读完；Z02-6明确ε为组效率之和，1/N来自self-exclusion。仅两角计数和target效率比不能识别f，还需独立本征参考或gate response；原式方向为R_ADO=(ω1S/ω1L)f。

全部自设：5000/4800计数、效率比.80±.016、额外参考1.34±.04给R_ADO=1.302083、f=.971704、独立假设σf=.040057。改变自设efficiency/reference相关系数−.8/0/+.8，σf为.026508/.040057/.050065；不是原实验误差。均匀组内response f=.974006；保持同组总效率但使两个能量效率相关地不均匀时，explicit pair-sum f=.772081。原文5.2%/3.2%是calculated最大偏离，不是完整实验uncertainty。

脚本 `system/scripts/day15_ado_preview_worksheet.py` 实际exit0，28项检查通过。[完整计算](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/day15-ado-preview-worksheet.json)与[误差图](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/day15-ado-input-uncertainty.svg)经PNG视觉核验。等权32/58/90的P2抵消与理想31.7175/58.2825/90的P2/P4同时抵消是任务推导，未当作者的设计意图。38 hardware pairs与44 ordered energy assignments不同，不能直接推出独立统计精度。

条件接回Day14：若只靠几何乘法f恢复旧common-selection point model的shared mean，需要f≥1.488716，对应self-exclusion必要η≥.32828；145Tb均匀4台组的4/3上界不能移植到JUROGAM或作为实验排除。完整定义、推导、数值和反例已写入[[angular-distribution]]“ADO计算单：额外输入、self-exclusion与误差”；同时按RB67-4修正旧method中初态polarized必需奇K的过强表述。Day15只列partial15，不建formal audit或计学分。

### 条件γγ响应：分离式的可检验边界

[本段来源前回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/conditional-correlation-before-source-recall.md)明确priming；随后核RB rawhash并视觉读printed326/PDF21 Eq3.69–3.73和Zheng printed910/PDF2 Eq1–5。RB67-3保留random initial、definite parity与helicity-unobserved条件；Z02-9记录原Eq2乘积而不替作者声称角关联已消除。

自设0→L→0、两条pure-electric photon rank L∈{1,2}，spin-matrix/CG/helicity与独立Legendre展开给K1=1+½P2、K2=1+(5/14)P2+(8/7)P4；singleγ均isotropic，joint仍有correlation。完整均匀gate恢复I/(2L+1)，有限gate有conditional density；这不是193Bi或145Tb的新level/spin。

自设32/58/90°各4台、四方位、每组gate效率.04，explicit pair加self-exclusion：E1的R=1，E2的R=.729470，分离组式都给1。无self-exclusion的disjoint 90°ring gate也给E1/E2条件比.760271/.697063，隔离了角关联贡献。只让三极角ΣP2/P4=0仍留q=±4方位harmonic；每圈8方位才对本toy消去K2/K4。自设20°/35°finite cones把某个E2 point K=.594119变为.940478，与Qk卷积和独立quadrature一致。

代码 `system/scripts/day14_conditional_angular_response.py` 实际exit0，[35项结果](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/conditional-angular-response.json)通过；它与第一组纲图35-check是不同exercise。完整公式、density/effect、参数、数值及边界已固化到[[angular-correlation]]“条件γγ响应：各向同性marginal仍可有角关联”，接回ADO及level scheme方法。结论为limits单γfactorization的充分性、supports逐pair matched-response核验，不给shared393/394新E2/M2/Jπ结论。

### 近邻双线排序：对称性先于增加角数据

[计算前回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/order-correlation-before-calculation.md)保留了“有取向可能增加信息”的初始预期及priming。general-spin结果使预期收紧：静态random-initial intensity只依赖两方向夹角，交换不变；两个同rank/同E-M类型pure stretched downward transitions还有更强的maximal-CG对称性，中间binomial抵消，full amplitude对photon交换对称，任意同一initialρ也不能从角度/偏振数据判能量标签先后。

自设pure E2 19/2→15/2→11/2：binomial与独立total-J²/highest-state/lowering构造相同，full-amplitude swap最大差4.48×10⁻16，random/Gaussian/coherent三种initial的角强度差均在浮点误差内。非stretched控制19/2→17/2→13/2在random initial仍对称，但chosen Gaussian、chosen方位/点角下两个ordered intensities为.879316/1.297627。都不是193Bi的spin/数据预测。

脚本 `system/scripts/day14_cascade_order_identifiability.py` 实际exit0，[51-check结果](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/cascade-order-identifiability.json)通过；删除了一个无信息的response同值检查，最终数为51。exact unobserved feeding middle与每层另行设同σ/J=.3的Gaussian，L1距离为.076428/.143581，说明该重置是额外输入，不是原cascade channel自动给出的结果。

完整proof与边界在[[angular-correlation]]“双γ排序的交换对称性”，接回[[level-scheme-reconstruction]]“近邻双线排序的角关联可识别性”；source premises为RB67-3/11，HE15-9仅是实际未定order的动机。决定revises观测选择：先检验交换对称性，若在其条件内，优先middle branch/独立level/time或能证明模型条件失效的观测；不默认更精细DCO/POL能判先后。实际weak-line Q/(E2)/π、shared R/A与review flags保留，未做排序fit或significance。

### Day15无学分实测对照：67Ga条件迁移

[来源前回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/zobel83-before-source-recall.md)先于source打开；近期fingerprint仅见本run的候选提示，Ionescu1981已有Oct12使用而暂缓重复。选择非重叠novelty问题“同parent取向/参考条件迁移”，核素与data context为67Ga，与continuity的193Bi双线身份/顺序分开。主线沿Zobel全部六页、图表/公式/setup/误差/结论核完；Crossref HTTP200 exact DOI/title/207(3)/389–394/1983，rawhash匹配，未用搜索snippet当证据。

Z83-11的958.0-keV同parent Table1完整十行已upright视觉转录：[fixture](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/zobel83-958-table-fixture.json)。它们是published LS fit estimates，表误差为statistical，delta采用0；alpha9MeV该列空白未填零，其他parent的30行按matched-parent问题未选，raw40行保存。alpha22−11.3MeV的Δalpha2/4为−.299/−.588，若quotederrors按std且独立，差量误差.051624/.125176；C48−32为−.037/−.182及.049679/.144045，未报实验显著性。

作者p393明确alpha2/alpha4 statistical dependence和error ellipse（Z83-12），数值Cov未提供。源码区分GF的peak-profile Gaussian与nuclear-population Gaussian；本任务自定义s为std、half-integer complete reference |M|=1/2。Stevens/独立CG tensor一致；alpha2-only条件s/J .127046/.365043不是作者实测sigma/I或jointfit。11.3MeV residual的chosenrho −.8/0/+.8给sigma_r .197717/.148564/.071067，只是敏感性；没有原Cov/response不作Gaussian排除概率。

自设两Gaussian width .12/.38、weight .45混合给alpha=(.797082,.564819)，与同alpha2的singleGaussian alpha4差.089121，未拟合Fig3的direct fraction。另以mass-number CM64/68、扣caption4MeV阈值幅度及3.0317MeVparent重构Fig3六lower ticks，最大差.004182MeV；它是坐标cross-check，不认证作者精确mass/targetloss或反应Q符号。

脚本 `system/scripts/day14_zobel83_alignment_worksheet.py` 实际exit0，38项通过；[结果](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/zobel83-alignment-worksheet.json)、[SVG图](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/zobel83-alpha-data-model.svg)和CSV/source-data可复核。沿用Python并应用nature-figure：singlepanel alignment not applicable，glyph/collision/source audits均exit0，minfont8pt、collision0fail0warn，PNG视觉通过；源码3export/width warnings按Wiki140×110mm/vector图+400dpi预览逐项复核。详情见[图QA](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/zobel83-figure-qa.md)。

决定supports条件/feeding-aware reference transfer，limits统一sigma/I和两误差的joint检验；Z83-9的same-energy/same-target还涉及effective beam/targetloss。全数值、模型、约定、反证和边界canonical写在[[angular-distribution]]“Zobel1983：同parent反应条件与Gaussian诊断”；Z83 source新11–14为needs_review:true，旧human metadata及1–10 flags保留，未扩原Jul08审核范围。Day15仍partial、不计卡；实际数据摘要可用，原events/fitCov/完整response仍缺，L4 replay not-ready。

### Angular-fit Cov：knowngeometry与两个errors仍不唯一

[计算前回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/angular-covariance-before-calculation.md)标明priming与本source已全文读。Z83-15的C四angles同时采、alpha两组三angles加fixedmonitor是knownsetup；raw intensities/efficiencies/monitor/实际GF covariance仍未给。

本任务选三parameter beta0+beta2P2+beta4P4再归一，以sourcealpha11.3 fit point(.973,.803)、F=1为local Jacobian点（Cgeometry也固定此点以隔离geometry，不称C组actualmean）。任务pureE2 max coefficients为40/91、−216/1001；equal absolute variance下两geometry的rho为+.504879/−.631222。未知F的Jacobian、QR、直接F/alpha Fisher与profiledSchur结果一致；把F当已知会改变Cov。

同alpha六angles、same point，两个chosen positive diagonal variance examples保持marginalsigmas .037/.090，rho仍为−.963993/−.142543。两者是可行噪声示例，未认证globalbounds或恢复sourceGF。全局multiplicative mode在normalizedalpha一阶取消，但chosen2%第一run monitor-mode会改变矩阵；实际monitor error未知。

代码 `system/scripts/day14_angular_fit_covariance_design.py` 实际exit0，[26项结果](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/angular-fit-covariance-design.json)通过。完整X/J/GLS/Fisher/Schur、矩阵/variance/条件写在[[angular-distribution]]“角采样与归一化下的Cov可识别性”，Z83-15为新needs_review:true。决定limits从marginalerrors+geometry反推actualjoint判断，supports保存fitparameterization/weights/shared-normalization；没有实验significance、新sigma/I或新line assignment，Day15仍partial。

### 393/394双线的energy-time设计：标定决定可识别性

已冻结的[计算前回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/doublet-time-before-calculation.md)后完成[91-check模型](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/doublet-time-identifiability.json)。HE15-9只提供名义gap.6keV；σE=.8keV及全部r/response均chosen，不借HE15-12 bandheadτ。Known symmetric prompt下energy/time两个marginals分别相同，joint可不同；a0或r0退化。半Jeffreys小r为2r²I(a)，允许offset2r匹配前两阶矩后变为(4/3)r⁶I(a)，不是bestfit profile或实验功效。r=.1的J由.00442677变为3.18285e−7。a0的后者仍有r⁸ time-only项，保留对过度概括的反证。

Canonical [[level-scheme-reconstruction]]“近邻双线的能量—时间可识别性与响应混淆”保存全公式、表和独立积分收敛。另给非负electronics-tail反例：两种order将独立同分布核delay/仪器delay交换能量标签，可得完全相同到达时刻joint；这是未知energy-specific response的nuisance ambiguity，不是knownresponse下的no-go或真实仪器判断。局部signed核delay/offset的score共线；自设独立prompt样本补第二行信息，Schur式NI×MIcal/(NI+MIcal)量化一阶边界，而非fullshape上限。最小新增输入为独立逐能量/逐detector prompt/timewalk/tails、实际middleτ或定位branch、events/接受度/Σ。supports joint信息、limits加时间标签即定序，未赋193Bi实际order或新spin。

### A≈130实谱对照：136Pr的连接重排与模型边界

Ga67 novelty已局部饱和后，以已保存[primed来源前回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/lv25-before-source-recall.md)选择136Pr的“谱→endpoint/π→模型分组”。DOI [10.1103/PhysRevC.111.014321](https://doi.org/10.1103/PhysRevC.111.014321)由Crossref200核；实际raw是17页acceptedcopy（含cover），SHA匹配，主线、Figs1–16、TableI/II已复核。PublisherPDF403，保留本版Fig10caption/TableII的ConfigD6列示冲突，不称officialerratum。旧sourceLV25-3表行locator修至PDF8，旧12–15表中空行合回parser，原review/flags保持。

[[lv-2025-136pr-tac-covariant-density-functional]] LV25-16/17：546/876双门见661/689，使作者把Q1终点由14+改到18+并将带头spin+4ℏ至19(+)；875.6 R=.47(8)和E2-gate支持dipole，π仍模型proposal。LV25-18的5level/6edge三条并行路径由[37-check](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/pr136-scheme-crosswalk.json)核表，closure−.1/−.2keV、声明Σ下cycleCov(.54,.25;.25,.50)、conditionalχ²=.08；非实际事件拟合。320/532的R/M空栏保留。

Fig4/5真实sharedgate/跨残核污染反例、D5/D6依configuration分组和D6单侧显示均写回[[level-scheme-reconstruction]]“136Pr：双门重排、共享门峰与模型分带”、[[136pr]]与[[a130-thesis-evidence-matrix]]新row。LV25-20明示与2019/2018同acquisition，故本novelty是不同核素/拓扑问题，**不**计为与Day9的135Nd文献独立采集。Counterevidence为D1/D2强度比偏差、D6limit/配置和Q1π缺口；下一必要观测仍cleanPOL/逐parentstrength/真实gate/Σ。Supports真正定位endpoint的证据，limits模型标签和单侧点升级；不增加Day15信用或新模式裁决。

### 研究截止后的既有摘录收束：2018的136Pr对象

checkpoint008实际观察为上海15:37，立即停止新研究；最后已保存科学读取快照为11:47，中间没有可核验新研究记录，不补称持续计算。15:00后只将此前已读NNDC136的两个对象固化，新增[[nndc-2018-136pr-selected-level-gamma-records]] N136-1–8。Reaction401行全文已读、adopted770行仅global/selected，cut1-Apr2018；未读整质量链/1996primary。Metadata评价DOI10.1016/j.nds.2018.10.002已Crossref核，raw槽未填不改raw。

旧Q1 reaction3998.8 J15经876.1 D到3122.7 14+，adopted(15)/(14+)与RI重标100保持；这是旧评价记录，不是2025独立反证。旧H链3677.7→262.9→3414.8→404.9→3009.9，与LV25-26直接2025TableI的3678.4→405.1→3273.3→263.1→3010.2次序不同。原因unknown，[[level-scheme-reconstruction]]“136Pr：2018评价与2025接受稿的顺序冲突”保存crosswalk；不判哪版错误，不称已重放原数据。

1996primary只核metadata：DOI10.1016/0375-9474(96)00107-8、NPA60350–76；OA下载0、arXiv拒绝、Semantic429、Scholar失败、Padua403，终止获取。TDMlicense被工具错标confirmedOA不采信。通用136fixed-column新script/更深入量化未完成；393/394 free-recoil只冻结预测和scratch，不算验收结果，留续接。没有在截止后补做新物理或打开Day16；completed14/partial15、正式21/24不变。

### 延期继续：反冲能量—张角的独立kernel

用户延期后完成原先冻结的free-recoil预测，[66-check回执](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/doublet-recoil-energy-angle.json)全过。共同M/Mf与c0=0 anchor下，后发线shift≈−hl cosψ/M；自选A193massproxy、σE=.8keV给K≈.862eV，cosψ=±1/√2的conditional半Jeffreys约2.16245e−7nats。总能量的order差仅O(M⁻²)，能量contrast仍保留O(M⁻¹)kernel；这是条件模型，不是实际检出功效/所需counts或新order测量。

[[level-scheme-reconstruction]]“近邻双线的反冲能量—张角信息与静态排序边界”保存精确4vector、共同endpoint/zero-gap/largeM、独立两路线积分和nuisance rank控制。完全stopping去掉主要angle项但保留O(M⁻²)常数，修正早先可能全消失的预测；未知pair-response slope可与leadingorder混淆，实际τ/介质/energy-angle calibration仍缺。supports补静态angular no-go之外的条件信息，不给193Bi实际order或模式。

### 延期novelty：136Pr强度balance与hiddenbranch

[来源/计算前预测](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/pr136-flow-before-calculation.md)后，完成[44-check](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/pr136-flow-identifiability.json)。有限fixedcolumn reader核两个actualSHA/π/归一/RIerrors/首unplaced311.7/LT/空CC-MR，直接PDF核新I26318.8(.7)/I40514.9(.7)，旧RI25.7(.5)/27.6(.3)不跨采集合并。

[[level-scheme-reconstruction]]“136Pr：相对强度、缺失分支与独立母态标签”给T+F=B+L正流量连续族：zeroIC/noextraexit控制分别偏向各自reportedorder，逆序的最小loss fraction为新39/188、旧19/276；这些不是实验branch限值。更强地，两order可构造完全相同的两线检测全分布；独立495.4母态入口tag在声明已知响应下才补一行信息，并非保证全局uniqueorder。UnknownICC/δ/branchlimits、realgates/Σ仍缺，未选旧新哪方正确或重放事件。

### 延期继续：逐线candidate graph而非自动identity

[预冻结回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/pr136-identity-before-calculation.md)后，44-check从actualacceptedPDF提取TableI156行、旧reaction136G中135placed；stricttoken漏spaced1552.2(3)问题已修，不补缺欄。|ΔE|≤1.5keV下27/80/49行分别0/1/多candidate，再加自选parent≤2keV变52/104/0；窗口不是confidence，unique不等truth，unmatched不等新线。

[[level-scheme-reconstruction]]“136Pr：逐线候选图与energy-nearest的失败”固化完整候选图和反例：新D3/D5两334.4都唯一配到旧D5 334.2，611新高/低母态也共用旧能量候选；固定parent窗又会拒掉Q1已报告约1349–1351keV整体reanchor。LV25-28/N136源对象和[[a130-thesis-evidence-matrix]]保存rowcount/coverage和后续精准identity路线；不做无条件配对、不宣布新线总数或选旧新模型。

### 延期sourcecase：D3新band与旧level候选

[13项row/假设审计](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/pr136-d3-source-audit.json)核新5086.3/650.5、旧5085.7(18)/650.1与各自endpoint；不是自动认证同state，newband也不等allnewlevels。987.0 R2.07(14)d支持quadrupole，E2与positiveπ按SecII额外E2策略/已知D2锚的source-level jointassignment保留，TableI没有该线独立POL列。660.4是15+→15+、653 M/R空，不套purestretched默认。

[[level-scheme-reconstruction]]“136Pr D3：新带、旧态候选与宇称handle”、LV25-29/30、N136-10和[[136pr]]保存小图/源行/两条Fractionclosure/假设链；未作新fit或将sourceassignedπ升为裸DCO直接测量，未称作者错误。

### 延期继续：D4同parent photon比值到conditional B商

按[冻结预测](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/pr136-strength-before-calculation.md)回核LKH82 PDF3 Eqs2.1–2.6与LV25 TableI/Fig9(c)，完成[71-check](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/pr136-sameparent-strength.json)。SI κ=.696775642，sqrtκ=.834730880舍入至源.835；自选δ0/纯crossover给8个D4比值15.329、15.340、14.404、13.381、12.256、11.253、14.227、6.002，与图中16–23点在图精度下相符，非source算法/δ0证明。

[[bm1-be2-ratio]]“同母态radiative比值的抵消条件”与[[level-scheme-reconstruction]]“136Pr D4：同母态比值重算与绝对强度的区别”保存公式/数据/误差scope：同parent correctedphoton ratio取消共同τ/总rate/其它branch与ICC分母，但δ、crossoverpurity、selection/response/Σ仍必需。4个M空栏和tentativeI23不填测值；弱分母线性σ不是完整confidenceinterval，D6限值未变双侧点。相符仅同acquisition内部一致性，不重测absoluteB或判模式。

### 延期继续：valence与unpaired标签的完整性

按[预冻结问题](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/pr136-configuration-before-calculation.md)视觉回核acceptedPDF15 TableII/Figs9–10captions，完成[62-check](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/pr136-configuration-ledger.json)。十行valence都给净9p/−5n；Q1/Q1* literalunpaired listednet=(3,0)，若解释为evenreference上的完整清单，则residual=(6,−5)总差1不能仅以任何two-fermionpairs补齐。逐species规则另限like-particle pairing，pn配对只保证总fermionparity；scope补充不改源数据。

[[configuration-occupation-audit]]保存全部原列、未列项None、必要条件及均值不定sector的单species toy。没有实际blocked/ref/spectator定义，不补νsd hole、不判作者code错；valence本身正确。Spatialπ标签均+也不补Q1POL或认证输入完整性。[[a130-model-choice-card]]、[[136pr]]与[[questions]]同步此边界及旧新263/405次序开放问题，投影覆盖2/7不变，Day15仍无学分。

### 延期练习：配对、阻塞、算符与公式契约

[量化前预测](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/tac-pairing-before-calculation.md)明确正文priming；[analysis](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/tac-pairing-contract.json)由`python3 system/scripts/day14_tac_pairing_contract.py`产生，50项检查exit0。它是源参数/公式与声明Fock空间控制，不是作者RHB复跑或真实核素占据恢复。

- W17-2 Eq12的源a=.636fm给`∫P d³r=1`、`∫r²P d³r=6a²=2.426976fm²`；这是form factor形式矩，不是实测pair半径。G/P/delta与波函数积分的维度核到两体矩阵元MeV。
- Eq11的S=0 spin projector为rank1/idempotent；同类pair构造逐species固定number parity，声明pn-singlet pair构造可改变各species parity而保总parity。S=0本身不指定作者实际pn通道。全部u/v及阻塞组合为chosen。
- W17-9只缩放Dirac磁矩项。声明D=3、A=−1及源c=.58给`|cD+A|²=.5476`，而`c²|D+A|²=1.3456`，故整体B乘因子不能代替组件处理；这不是实际109Ag磁矩。
- W17-10 v2 Eq25末项缺平方的字面读法不满足同式中段的维度/缩放；W17-11 A18/A19对非零relative oscillator例子冲突；W17-12的.87/1.26直接降幅约30.95%，与打印20%不同。均保留版本/locator，不修作者代码或实验值。

### 43-check：从最大重叠到可重放输入

[量化前预测](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/tac2015-blocking-before-calculation.md)与[analysis](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/tac2015-blocking-following.json)记录声明`u²=.7,v²=.3`的实canonical双态；另用E=±1的显式BdG矩阵证明正能双态简并，避免把任意非简并混合冒充eigenstate following。`python3 system/scripts/day14_tac_blocking_following.py`最终43项检查exit0；首42项之后新增此有效性检查，源实际轨道、频率/λ和code仍未取得。

同态控制正确继承blocking；U/V交换分支反转标记后保持原blocked态的ρ/κ，说明reference改变时不能只要求裸blocked数不变。整体qp符号改变不改ρ/κ，却能使源式的signed字面控制出现tie；45°简并混合有不同旧标记的并列最大值；V=0令分开归一未定义。自设abs-score解除符号反例但不解除45°tie，first-argmax会随旧列顺序改变。全部是输入契约的条件控制，不是135Nd/Pr136计算或作者代码错误判定。

### 50-check：四极形状与相对转轴

[量化前预测](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/pr136-gamma-before-calculation.md)声明本任务normal form和irrotational law；[analysis](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/pr136-gamma-axis-audit.json)由`python3 system/scripts/day14_pr136_gamma_axis_audit.py`完成50项检查、exit0。首次import因缺SymPy exit1且尚无计算结果，改用标准库Fraction的`Q(sqrt3)`精确算术；各差式对c/s次数至多3，4×4不同有理点精确核验结合多项式唯一性，未安装全局包/未动科学输入。

在声明`Q=diag(βcos(γ+120°),βcos(γ−120°),βcosγ)`下，`TrQ²=3β²/2`、`TrQ³=3β³cos3γ/4`；±γ可由proper轴交换实现，加120°为cycle。相同unordered四极张量不证明完整密度/波函数相同，更不代表实际作者frame已核。读取TableII十行rounded模型βγ得到的是此normal form的确定性变换，不是实测E2 invariants。

声明β1/γ±20°的四极形状相同，在假设irrotational law下固定x轴惯量为.413176/.969846；转轴也同步换轴后回.413176。共同标度任意，不是Pr136 MOI或D4+35→−35重赋值。实际TAC含qp/配对贡献，不能由此以I/ω唯一反演γ。

### Table1交叉检查与下一个有序谱练习

[Table1 crosscheck](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/petrache2015-table-crosscheck.json)核四行Total=Q+D，合计73=46Q+27D；表数不是Fig1全样本或独立实验数。138Nd Table1含28Q而Fig1仅选14/15 high-spin Q，不能由census重建其平均J2；51/23只是作者选定总结，缺per-band原能量/筛选mask/Cov，未宣称复现。

PT15-9将“J2不依赖绝对spin/Ex赋值”与必须核相邻线身份、ΔI和排序分开。既有[[moments-of-inertia]]还保留Rh的source-specific centered差分；下一实际Pr136练习要先定义stencil和正确path，不能先套一个通用分母或把双signature crossover序列混作同一路。此项尚未计算，不当已完成结果。

### 71-check：实际D4曲率、位置与筛选

[量化前约定](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/pr136-j2-before-calculation.md)先冻结stencil/parentstep/图路径；`python3 system/scripts/day14_pr136_inertia_paths.py`最终71项检查exit0，[analysis](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/pr136-inertia-paths.json)保留全部输入/pairs/位置/条件协方差。首68项后补directPC22式与从level energy起点形成γ的控制，最终71全true。

本任务取`x=eγ/k`，`J2_hat/ℏ²=Δip/Δx=kΔip/Δeγ`，并单列edge-pair的spin/frequency中点；这不替代源作者坐标。绝对I/Ex起点取消不代表path/k可忽略，交错crossover连续parent的step1不可默当same-signature step2。对同一quadratic rotor，正确因子都回到声明25，错套4会给50。

实际dipole相邻7点为10.288、25.974、32.573、15.723、149.254、50.505、17.452 ħ²/MeV。149.254来自503.6/510.3差6.7keV；跨两条γ的峰75.472在另一位置，是相邻值的harmonic mean而非arithmetic mean。偶/奇crossover各3点和交错估计也有各自位置，不能当26个独立数据点。

若将quoted dE当独立σ，仅一阶条件下峰的σ≈6.301；允许未知pair相关性时为0–8.911，非实验CI。共享γ使相邻J2有相关性。声明保持本组interaction点、频率>.3后一次≥2×initialmean显示筛选会将mean43.110变25.419，完整removed point/mask保留；不是作者对Pr的筛选或Nd51/23重现/偏差显著性。4个M空、I23tentative和原closure残差不改。

### 24-check：Qt算符、系数表与逆问题

[量化前预测](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/matev2007-before-calculation.md)明确视觉读表及心算priming。`python3 system/scripts/day14_qt_operator_table_audit.py`最终24项断言通过、exit0，[analysis](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/matev2007-qt-operator-audit.json)保留34行/61组实际表值与7组None。这个“通过”指审计程序/条件控制，不代表原表全部通过一致性。

源terminal式Qt_y=Q20−Q22/sqrt3、Qt_x=Q20+Q22/sqrt3在同一物理问题换轴且Q22反号时一致，不把不同EDF预测视为相同。声明Qt=1eb可有γ−20/0/+20及Q2约.879385/1/1.347296，故单一Qt不唯一给γ。源Eq14中间轴标签原样留边界，未静默修。

若共享C/同权线性估计器，qt_eff也应满足该线性关系。按两位小数最近舍入，必要界限≈.012887eb；v1 CHF ν[402]5/2,+i和π[532]5/2,+i两条中心残差+.390829/−.918868超界，原值/条件/locator保留，59其余组只通过必要检查。理论fit σ及其舍入的Cauchy区间均有相容空间，不等于实际Σ恢复；不同权重控制证明共享估计器前提必要。没有actual C/权重/输出/VOR，未判作者code错或替换系数。

源blocks计N73/Z58/A131，是实际奇A reference例子但不是Pr实际core。声明移除ν6_1,−i增加ν6_2,+i保N/保intruder count，给δQt=.11/.04eb、δJ=−1.36/−1.44ℏ（CHF/CRMF），未实际重跑配置或赋新整数spin。源7.64/7.4(3)baseline与Eq33未用于本任务寿命提取。

### 27-check：实际Qt表角色与条件响应

[typed输入](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/riley2001-table-I-input.json)保留33原行/15核素，39个有限token逐一与原PDF表序对上，三个`<3.0`继续是无CL上限。21single、1band pair、2signature pair、5b gate pair、1c feeding pair的角色不同；42数值token不是42个独立测量。完整数值与角色的长期副本在source“Table I：保留分析角色的33行账本”。

[程序](../../system/scripts/day14_riley_global_qt_ledger.py)与[结果](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/riley2001-global-qt-audit.json)27项条件控制通过。五个b门选的名义Qt增幅分别12.069%、11.765%、8.333%、8.333%、9.091%；135Sm5.8→6.4c是另一侧馈时序假设，不能混作第六组门选。恒定Qt是拟合约束，默认Qt(sf)=Qt不等于τsf=τband。

同一已识别E2且Eγ/branch/geometry固定时，Qt×1.1给B×1.21和τ×.826446；不是原实验实测寿命变化。135Nd/133Nd的上方门Qt比=.876923、差−.8eb；若把括号误差当σ，未知相关性下ratio的一阶σ范围.003787–.057751，difference为0–.4eb。原Σ和CI没有恢复。共同scale保ratio但缩放difference，不能用这个简化例子单独证实或推翻作者差分方法精度。

名义140Eu反应预算只排除142Sm为该融合蒸发产物，不能把“守恒可行”的Ce131/132自动算作本次测到。负号归一控制说明Riley/Matev的Qt形式相容，仍不认证其实际代码版本/Pr136frame。

### 16-check：原始reference、估算与通道归一

[原表typed输入](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/petrache1998-table-I-input.json)及[程序](../../system/scripts/day14_petrache1998_reference_audit.py)/[结果](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/petrache1998-reference-audit.json)有16项源身份/角色/精确算术和定义控制，实际exit0。TableI八行中Band3 split lower/upper与whole singlefit同属一带；Fig2六panel中同data的Band3重画，不能增加独立样本量。

脚注a精确重算`(4.8+6.1)/2+(6.69−5.45)/2=6.07 eb`，是无法直接计算one-i13正宇称组态后的half-contribution估算；无该组态直接解、λ=.5置信分布或理论σ，不能据与upper~6.5相近认定唯一验证。

原文Nd β=.0202与Ce α3n校正β=.0192不可互换；若同Ce平均发射速度误借Nd β，F乘.950495，约低4.9505%。first-order、F=1条件下36°的Δβ=.001给每MeV .809017keV（144°反号/90°零），不是实测某条line偏移。可见top F<1还有原文明确的未见更高跃迁与feeding；强制top=1会使βhat/βtrue=Ftop。演示Ftop=.9、另一F=.45时归一变.5，全部chosen控制，不是拟合原数据。

## Counter-evidence and missing companion observables

HE15-9的实际未定双线是核心反例：energy sum、共享R/A和假设的ΔI=2均不足以裁决order。若一条线出现可独立定位的旁路或延迟顺序，应重审中间level；source仍保留括号Jπ与(E2)。HE15-5的quadruplet限制“一个峰是一条γ”的简化；干净622.4直接分支门与323.4级联门的299-keVcomponent差异可能迫使拆峰，但必须控制622/626门纯度、feeding、response和random。

必要companion分类：confirmed SD link与endpoint为expected-but-not-established；46/87-keV低能γ为not observed、原因仍是作者解释；缺事件/Σ的重拟合为blocked-needs-event-level data。αtot=261/12.82与87.4-keV x ray会降低γ灵敏度，不能把未见峰直接写成路径不存在。Table I/Figure2/Figure5和多角度数据共享采集，互补不等于独立复测。

### 方法companion的反证与伴随输入

W17-5/7/9是对“能谱或B(M1)接近就认证完整组态”的具体限制：数目未恢复、回弯区没有收敛解、磁矩算符选择亦改变强度。基空间在单频率的.021%/.020%检查不覆盖所有分支/电磁量。必要伴随材料仍是actual occupied/blocked/reference、轨道overlap追踪日志、模型输出和算符定义；109Ag方法与136Pr的基空间/组态不同，不能转填Q1/Q1*。

来源独立性也保持：模型比较复用上游109Ag实验，不等于136Pr独立实测；本任务的finite-Fock与公式反例均为声明数学控制。原Pr136π/POL、263/405次序原因和实际事件/响应/Σ缺口不解除。

### 上游方法的反证与必要材料

ZT15-6回弯区结果省略；ZT15-9的“无统一.3因子”是作者对选定135Nd算例的解释，Fig5仍见paired B(M1)曲线高于若干点，未给可重建联合χ²/Cov。ZT15-10只算平面旋转，不能将其当直接三维静态手征解或partner谱。[[mukhopadhyay-2007-135nd-chiral-vibration-static]] MU07-6为既有Wiki校准，实验强度/TAC/RPA层级保持；本轮没有重新摄取该实验或清其review状态。

重放仍需actual前后U/V、basis/reference、blocked/species、λ/ω路径和步长、相位/并列/zero-norm规则、overlap及收敛日志。本文方法不能补Pr136 Q1/Q1* spectator，论文数据点复用不增独立实验。

### γ/axis分析后的必要材料

几何反例限制“γ号不同就是不同形状”捷径，也不能反向宣称D4/D6完整态相同或作者模型错误。LV25-33的actual轴映射与alternative数值解仍缺；Fig11同时非零Jx/Jz提示不能用替代段principal-axis描述倒填所有TAC态。需要真实tensor/relative orientation、完整E2矩阵元链（必要相位/分支）及独立形状信息；相对Iγ、单个寿命或E2未观测都不补这些材料。原MR与coexistence仍竞争。

### Nd伴随源的限制

源文自身把寿命作为轴解释的待检验观测，且同时讨论形变/对齐占据与crossing；PT15-7不支持J2到γ的单值反演。低组删点是作者明确披露的图示选择，当前没有完整数据检验其影响，不指控作者错误或重算显著性。PT15-8不能替Pr136补lowΩ/highΩ完整输入、actual tensor/axis或原1996次序原因。

### 从曲率到结构判断的限制

同母态/同ΔI还不足以选daughter；错把265.0代替207.8配481.0，closure残差从名义−.4变−57.6keV。正确图链也有−.4…+.4的打印残差，当前没有Σ，不把这些数转为独立χ²。J2对absolute起点不敏感与对差分/校准/interaction敏感必须同时保留。原始mask、校准共同Σ和必要寿命/完整EM链缺失，不能只凭局部曲率或筛选均值为Pr定γ/轴/共存。

### 模型误差、版本与原实验缺口

模型残差被假设为零均值/同方差/不相关，并排除crossing/收敛歧义配置；其窄histogram不代表实验precision或所有A130 band均成立。alignment比Q更复杂，需宽频率检查与实际occupations。两个EDF和多个发表不等于独立实验。

v1的Eq14中项轴标、Eq31前131Cs与定义core131Ce、Fig4 caption132Sm与plot/body142Sm、Eq33 CG幂次及π404 p/h/core文字差异均作精确version boundary保留；不调用歧义去计算实验Qt/τ，不称officialerratum。原始Laird2002仍缺；新公开取得Riley2001作者报告且刊头身份已核，正文待下一步，不能先拿它的内容补数据。

共同加性项和共同乘性归一化对difference/ratio作用不同；本任务的5/7控制不判断原实验系统误差算法是否有效。要检验source作者关于差分测量/Qt的结论，仍须读实际analysis及误差结构。

### 原实验报告的限制与必要伴随输入

RI01-5正文称absolute Qt阻停加侧馈附加15–20%，TableI caption的10–15%仅阻停，relative accuracy约5–10%；来源没有formal coverage或共同Σ，不独立quadrature，也不无条件复述摘要“free”。门选敏感性、ND的配对/γ-soft解释和Fig1/TableI的quoted variants共同限制单值直推机制，但不让相对比较失去全部信息。

RI01-10：133Pr3.4(3)/3.3(3)、134Pm3.9(3)/3.9(2)、135Sm6.4(5)/6.4(4)c先保留figure/table各自值，缺完整fit/gate身份不判typo；同中心3.5的133Nd还有多表行候选。真实L4仍缺逐ring/gate谱、centroid/calibration/事件交集/Σ、β′ producer、slowing/feeding histories、transition E2/branch/geometry和FITFTAU输入；不补逐态τ、Pr136实验γ或absoluteB。

### 实测与估算仍缺的伴随输入

Petrache的二维Q0/Qsf χ² grid、原centroid/共同Σ、完整transition/geometry和slowing/feeding未得；本轮不补逐τ、Q0到triaxial Qt或新的Pr136值。Band3一值/两段作者明确不能firm区分；135Nd Qsf的3.0(5)/4.0(5)、134Nd“same6”与不同fit表行的范围均保留。132Ce外源和Clark转引须逐采集处理，不据相同数值默认独立或同data。

反证重点是作者未直接计算的组态仍有theory栏估算，以及统计不能选择的split/whole fit；必要伴随是原fit/grid、actual gating/response和原Clark几何/谱系，而不是增加转载次数。

## Knowledge Impact and Learning Decision

- **supports：** 一图一表的逐边source-level纲图和DCO/偏振/转换联合证据链。
- **limits：** 三个closure视作独立测试、shared-doublet R/A视作逐线性质、bandheadτ视作parentτ、relative intensity视作absolute strength的捷径。
- **revises：** 对下一项信息的选择从“再算能量和”转为定位未定endpoint、测试独立anchor与取得parent-resolved电磁输入。
- 193Bi与A≈130的configuration/mode排序均未改变。无新增human-review事件，source/page review状态不提升。

## Day 14 scorecard

这是本session正式任务产物的六维Codex self-assessment，受Day13预习priming影响，不能称为独立盲考能力或把19/24当基线实验。0=未做，1=复述，2=条件应用，3=有source和可复算反例，4=能沿证据链指出并测试判决边界。

| 维度 | 分数（0–4） | 本次可核验证据与短板 |
| --- | ---: | --- |
| 理论 | 3 | incidence/cycle/GLS、offset/gain区别与独立解法；未完整重推γγ角关联formalism |
| 判图 | 4 | 原图/全部续表逐边七线，查到319.8表尾行及393/394未定顺序；保留X |
| 误差 | 3 | caption额外误差、cycle相关、Σ敏感性与失败控制；真实joint response/calibration缺失 |
| 证据分层 | 4 | 直接峰量、联合placement/Jπ、作者形状解释、模型与counterfactual明确分开 |
| 反证 | 4 | 原论文doublet、quadruplet、branch互斥和弱线非观测边界均有locator |
| 可证伪问题 | 3 | 可定位branch/time/tag和parentτ设计；没有事件级数据验证实际检出功效 |

合计21/24。仍需补强的是真实gating/response功效、完整calibration covariance及角关联前向模型；不通过加分隐藏这些短板。

## Day 14 weekly REFLECT

本周从选律、B定义、双带指纹、反应与门控、Doppler和统计走到逐边纲图。最应修正的习惯是把“每一步相容”累加为“结构唯一”：HE15-9给出真实未定顺序，HE15-11显式依赖Band1，HE15-12阻止借用bandheadτ，均要求定位尚未识别的自由度。

后续判断：先验证line/parent/branch identity，再讨论δ和绝对strength；对共享数据的角度/偏振、图/表、calibration和model projection保留依赖；把最小测量对准不同候选预测会分开的observable。canonical认识修正已写入[[level-scheme-reconstruction]]，周度回执只记录学习状态。当前证据支持方法层面的修订，没有支持新的wobbling/chirality/shape裁决。

### 方法companion后的认识决定

Decision: supports 配对/阻塞是独立输入，limits 用组态简称或拟合曲线替完整输入。新增方法证据写到source、已有occupation方法、TAC模型和model-choice卡；没有新实验性质、good-I计算或PSM/TPSM覆盖。W17公式版本异常仅阻止按字面直接复现，不构成程序错误判决。当前问题下一高信息路线为Ref31的追踪/阻塞定义，或Pr136实际公开输入；不为新来源数量开卡。

### 上游阻塞定义后的决定

Decision: supports 追踪实际qp身份，revises 把“largest overlap”简称当完整可复跑算法的读法。新直接来源与43-check契约已写入canonical，不替作者补abs/phase实现；模型选择覆盖2/7和原模式排序不变。现有Pr136真实输入与历史263/405原因仍缺，当前方法表达式路线局部完成后须重建信息增益池。

### 配对方法阶段的批次REFLECT

2015→2017→2025的三来源方法阶段已比较：monopole/有限程可分离力、10/12壳、O1/O2继承、磁矩算符选择及实际136Pr输入缺口。Canonical在[[a130-model-choice-card]]“配对方法谱系的批次REFLECT”：引用谱系不认证相同代码版本/实现，更不构成三次独立实验或代码审核；模型比较改善不能唯一倒推组态。仍用现有method/project承载，不另建synthesis/note，原正式weekly REFLECT与21/24成绩不变。

### γ/axis后的认识决定

Decision: limits source模型γ、替代转轴与实验共存之间的直接等同；supports 将四极shape、relative orientation和完整模型态分开。几何必要条件已固化，但实际source frame未认证，不清原review、不给新模式或PSM/TPSM信用。当前问题的后续信息增益须来自真实输入/直接轴约定或新的伴随观测，不能继续换同一几何toy的参数。

### 伴随源后的决定

Decision: supports signedγ的相对轴语境，limits source引用/J2gap直接升级为唯一形状证据。持久化source、现有triaxial概念与LV25的Ref48核验和索引；不扩大Nd核素页/项目或改Pr136排序。下一高信息量回到当前level-chain的实际差分定义与selection敏感性，不重复同一几何toy。

### 有序能量练习后的决定

Decision: supports 先建graph再构造observable；limits 以band标签、绝对spin未知时的捷径或单一J2峰/均值认证结构。已从实际数据完成原计划下一步，保留source-specific PC22式及本任务明确stencil，不给Day15信用或改变formal21/24。下一信息增益应来自必要的实际寿命/Qt输入、原始mask或更多直接资料，不继续换同一stencil toy参数。

### Qt伴随方法后的认识决定

Decision: supports 明确charge/axis/operator/reference和数据来源，limits 单一Qt或intruder count到唯一构型/γ、将fit errors当实验σ及照搬v1表。源码/配置矩阵和原测量缺口不因23→24验证断言通过而消失。物理进展写回source/Qt observable/reference审计/model-choice，33页run-owned知识累计；原2/7投影覆盖、Pr模式排序与formal21/24不变。

### Riley实验报告后的认识决定

Decision: **supports** 共同实验条件下的相对Qt比较，**limits** 摘要无条件零systematics、把Qt表当逐transition寿命或所有双值可平均，**revises** 数据角色与外源谱系的读法。最新可复用增量同步source、Qt observable、DSAM方法、Matev上游谱系和index。Formal21/24、completed14/partial15与既有Pr解释不变，未新增独立实验计数。

### 原始reference定向回读后的决定

Decision: **revises** 将Petrache误作7.4原始出处或将八表行平铺为八带的读法，**limits** 把脚注估算当直接计算/显著形变jump，以及跨通道共用速度归一。**supports** 带身份、fit角色与响应输入一起进入证据矩阵。没有新实验计数/原始重拟合/Pr模式排序或formal成绩变化。

## Durable knowledge delta

本run累计修改的knowledge Markdown以本节唯一机器块和最新验收回执为准；超出昨日预习的增量为七边逐条证据、相关cycle/标定nullspace、未定doublet shared-quantity边界和parent-lifetime契约。canonical知识路径：

- [Herzáň source](../../knowledge/sources/herzan-2015-193bi-spectroscopy.md)：HE15-8–14及正式来源主线/triage。
- [level-scheme method](../../knowledge/methods/level-scheme-reconstruction.md)：五能级七边、GLS/反例和必要companion。
- [A≈130 thesis matrix](../../knowledge/projects/a130-thesis-evidence-matrix.md)：方法对照行，不冒充A≈130新实验。
- [NNDC193Bi evaluation](../../knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md)：公开对象的版本、RI/精度、weak-line/Q与条件CC；不是独立实验。
- [知识索引](../../knowledge/index.md)：新增评价source导航。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
      "summary": "核验七边中的表尾行、未定双线与共享角度/偏振、实际标定、条件性isomer赋值及parent寿命来源；原flags保留。；原p7/p9的352.3图表spin差异重新视觉核验。",
      "anchor": "Day14 正式逐边复核与来源边界",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-8"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-9"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-10"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-11"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-12"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-13"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-14"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "summary": "固化五level七边逐条E/C/M/J审计、三个相关cycle与带假设35-check重算；不替换作者能级。",
      "anchor": "Day14 五能级七跃迁逐边审计",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-4"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-8"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "summary": "保留actual a(E)/Q(E)、bandhead与parent寿命、conditional intensity和SD低能companion的区别；weekly认识修正同步canonical页。",
      "anchor": "标定、寿命与伴随观测的逐项契约",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-10"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-11"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-12"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-13"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-thesis-evidence-matrix.md",
      "summary": "增加spectrum-to-level correlated-closure方法对照行和active说明；193Bi不当作A≈130模式独立证据。",
      "anchor": "Day14 spectrum-to-level identity and correlated closure",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-8"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-9"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-2"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-5"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "summary": "37-check纯分支gate/unknown-branch/shared-count/low-energy nonobservation设计；全部自设条件，不作为actual193Bi counts或branch fit。",
      "anchor": "互斥分支门、复合峰与shared-event计数",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-4"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-5"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-13"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
      "summary": "新增官方选定ENSDF对象的version/hash/locators、七边精度和RI、weak-line Q/352冲突、BrIcc计算与153-ns依赖；非新独立实验。",
      "anchor": "193Bi：评价对象与原实验的分层",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-1"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-2"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-3"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-4"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-5"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-6"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-7"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-8"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-9"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "summary": "真实evaluation crosswalk与79-check；明确整数/调整精度、Q≠E2、352.3 triangle冲突、parent conditional photon/totalbranch区别。",
      "anchor": "原图、评价精度与赋值冲突的crosswalk",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-3"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-4"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-5"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-6"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-7"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-8"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "新增193Bi官方评价来源导航，注明共享2015He27与CC/model边界。",
      "anchor": "nndc-2017-193bi-level-scheme-evaluation",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/linear-polarization-asymmetry.md",
      "summary": "70-check sharedA凸组合、nearbycalibration、pureE2取向/联合R/A必要域和selection失败条件；不做line/M2/Jpi赋值。",
      "anchor": "未分峰偏振的联合命题与选择条件",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-9"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-10"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-5"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-11"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "summary": "将joint POL条件约束、orientation/geometry/selection与spin-parity边界接回level-scheme evidence chain。明确同名energy gate未必有共同target-independent effect。",
      "anchor": "Shared POL 对joint命题的条件约束",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-9"
        },
        {
          "path": "knowledge/sources/nndc-2017-193bi-level-scheme-evaluation.md",
          "locator": "N193-5"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-11"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
      "summary": "原扫描全文再核，新增组效率/self-exclusion定义、calculated偏离与数据谱系边界；不清review flags。追加Z02-9 Eq2/full-joint迁移边界；不替作者声称correlation已消除。",
      "anchor": "Day15 无学分预习：定义、归一与原始阅读",
      "sources": [
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-6"
        },
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-7"
        },
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-8"
        },
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/angular-distribution.md",
      "summary": "固化28-check ADO自设练习、f额外输入、逐台response反例、uncertainty/covariance和有条件Day14几何桥；仅partial15。接回35-check conditional γγ response。",
      "anchor": "ADO计算单：额外输入、self-exclusion与误差",
      "sources": [
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-1"
        },
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-6"
        },
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-7"
        },
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-8"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-9"
        },
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-9"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/angular-distribution.md",
      "summary": "修正polarized初态必需奇K的过强表述，保留definite-parity/helicity-summed与w(-M)=w(M)两项条件及detector/nuclear attenuation区别。",
      "anchor": "初末态宇称确定且不测 γ 偏振",
      "sources": [
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
      "summary": "局部视觉回核printed326/PDF21 Eq3.69–3.73，保留parity/helicity/random-initial条件和任务toy分层；不重复全42页阅读或清review。接入51-check最大耦合交换对称性，明确为任务推导。",
      "anchor": "Day14 条件γγ响应的局部回核",
      "sources": [
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-3"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/angular-correlation.md",
      "summary": "35-check conditional γγ toy：isotropic marginals不保证factorization，K1/K2、ρ/effect、pair/self-exclusion、azimuth cancellation与finite cones；未做真实谱重放。",
      "anchor": "条件γγ响应：各向同性marginal仍可有角关联",
      "sources": [
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-3"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-11"
        },
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-6"
        },
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/angular-correlation.md",
      "summary": "51-check general-spin、binomial/total-J²-ladder、任意initialρ的same-rank stretched full-amplitude对称性及非stretched失败控制；feeding同σ/J不是自动输出。",
      "anchor": "双γ排序的交换对称性",
      "sources": [
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-3"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-11"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "summary": "将exchange symmetry接回实际未定双线的下一观测选择；不改变weak-line赋值或宣称actual模型条件成立。",
      "anchor": "近邻双线排序的角关联可识别性",
      "sources": [
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-3"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-11"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
      "summary": "六页主线/metadata/raw核验，新增Table1 selected means、statCov边界、Ref4/5依赖与Fig3坐标核算，原Human/旧flags保留、新11–14 true。新增Z83-15实际angles/two-run normalization，原旧人审不扩。",
      "anchor": "Day14无学分预习：同parent条件迁移与统计边界",
      "sources": [
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-11"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-12"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-13"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-14"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-8"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-9"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/angular-distribution.md",
      "summary": "十个published同parent alpha pairs、38-check CG/Stevens/条件Gaussian/std/inversion/Cov sensitivity/mixture/CMticks、SVG及图QA写回；不作experimental significance或统一sigma/I。",
      "anchor": "Zobel1983：同parent反应条件与Gaussian诊断",
      "sources": [
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-11"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-12"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-13"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-14"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-8"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/angular-distribution.md",
      "summary": "26-check knowngeometry/GLS/Jacobian/Fisher/Schur/same-marginalpositivevariance/global-vs-run-mode设计，rho示例不当actualGF；完整公式/矩阵/输入边界固化。",
      "anchor": "角采样与归一化下的Cov可识别性",
      "sources": [
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-11"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-12"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/angular-distribution-coefficient.md",
      "summary": "补齐未归一β、归一Aexp、最大取向参考c与核α的变量层级；以源表作条件转换，保存Cov坐标变换/距离不变、归一cross项和语义反例。自设控制不当原文fitCov。",
      "anchor": "拟合系数、核取向与最大辐射系数的层级",
      "sources": [
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-1"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-11"
        },
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-12"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/zobel-1980-magnetic-substate-distributions.md",
      "summary": "完整9页原主线/Crossref/raw核验，保存A2/A3/A4–A6转录与代数边界、同parent一行、旧数据引用链及missing Table3/GNOMON readiness。",
      "anchor": "Day14 Ref5主线复核与公式自审",
      "sources": [
        {
          "path": "knowledge/sources/zobel-1980-magnetic-substate-distributions.md",
          "locator": "Z80-14"
        },
        {
          "path": "knowledge/sources/zobel-1980-magnetic-substate-distributions.md",
          "locator": "Z80-15"
        },
        {
          "path": "knowledge/sources/zobel-1980-magnetic-substate-distributions.md",
          "locator": "Z80-16"
        },
        {
          "path": "knowledge/sources/zobel-1980-magnetic-substate-distributions.md",
          "locator": "Z80-17"
        },
        {
          "path": "knowledge/sources/zobel-1980-magnetic-substate-distributions.md",
          "locator": "Z80-18"
        },
        {
          "path": "knowledge/sources/zobel-1980-magnetic-substate-distributions.md",
          "locator": "Z80-19"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/angular-distribution.md",
      "summary": "保存规范ratio JCovJ、source打印符号/相对误差缺项与半径约定边界；23-check chosen controls不重算原实验joint significance。",
      "anchor": "Zobel1980附录：字面公式与联合覆盖",
      "sources": [
        {
          "path": "knowledge/sources/zobel-1980-magnetic-substate-distributions.md",
          "locator": "Z80-14"
        },
        {
          "path": "knowledge/sources/zobel-1980-magnetic-substate-distributions.md",
          "locator": "Z80-15"
        },
        {
          "path": "knowledge/sources/zobel-1980-magnetic-substate-distributions.md",
          "locator": "Z80-16"
        },
        {
          "path": "knowledge/sources/zobel-1980-magnetic-substate-distributions.md",
          "locator": "Z80-17"
        },
        {
          "path": "knowledge/sources/zobel-1980-magnetic-substate-distributions.md",
          "locator": "Z80-18"
        },
        {
          "path": "knowledge/sources/zobel-1980-magnetic-substate-distributions.md",
          "locator": "Z80-19"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/angular-distribution.md",
      "anchor": "正布居矩可行域与源表中央值",
      "summary": "保存J13/2正对称布居七点凸包、rational Farkas证书、全部10+1源表行LP可行性和unknownCov的conditionalellipse相交；模型中央值不可行不升级为实验否定。",
      "sources": [
        {
          "path": "knowledge/sources/zobel-1983-energy-projectile-alignment.md",
          "locator": "Z83-11"
        },
        {
          "path": "knowledge/sources/zobel-1980-magnetic-substate-distributions.md",
          "locator": "Z80-1"
        },
        {
          "path": "knowledge/sources/zobel-1980-magnetic-substate-distributions.md",
          "locator": "Z80-17"
        },
        {
          "path": "knowledge/sources/zobel-1980-magnetic-substate-distributions.md",
          "locator": "Z80-18"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-26"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/zobel-1980-magnetic-substate-distributions.md",
      "anchor": "1979 Ref4/Ref9的输入边界",
      "summary": "精确解析共同1979参考的DOI/title/卷页与末作者拼写歧义，保存API/OA/publicPDF/Scholar访问边界；不借TDMlicense或metadata补纯度/δ/独立采集。下一公开ENSDF伴随记录路线。",
      "sources": [
        {
          "path": "knowledge/sources/zobel-1980-magnetic-substate-distributions.md",
          "locator": "Z80-20"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
      "anchor": "Selected records and source locators",
      "summary": "新增四个真实ENSDF对象的版本/selected原始L/G字段、有限MR/parent半衰期、RI/weakbranch、3层数据依赖与DCO/未分峰反证；无primary全文或重测。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-1"
        },
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-2"
        },
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-3"
        },
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-4"
        },
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-5"
        },
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-6"
        },
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-7"
        },
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "anchor": "67Ga：跨对象的parent与强度输入核验",
      "summary": "38-check回源量、half-to-mean、parent/feeder、RI/CC/库存契约及条件B=9.61853WU；同DCO不同M的actualrecord反证。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-2"
        },
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-3"
        },
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-4"
        },
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-5"
        },
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-6"
        },
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-7"
        },
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-8"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/angular-distribution.md",
      "anchor": "67Ga reference-purity与DCO的实际字段补核",
      "summary": "以δ有限quotederror补reference purity readiness，保留固定δ0物理凸包和trueCov边界；DCO/gate条件不省略。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-2"
        },
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-3"
        },
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "nndc-2005-67ga-selected-level-gamma-records",
      "summary": "新增67Ga在线objects/source-field-audit导航。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
      "anchor": "2026-10-15 Supplement — Z31实际理论输入与67Ga ledger",
      "summary": "保存4actualofficialFO inputs/Tot/K/哈希/输入失败、修正和物理/误差边界；32-check条件forward，不作实测ICC或NDS2005算法。",
      "sources": [
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D14-1"
        },
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D14-2"
        },
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D14-3"
        },
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D14-4"
        },
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D14-5"
        },
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D14-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "anchor": "67Ga：FO理论输入补全的条件强度范围",
      "summary": "源数据空白CC保持，4个theoryinputs给声明两gamma/弱M1E2/δ模型的B中心区间；源quotedCov/完整higher/extra不闭合；weakRI不等弱B反事实。",
      "sources": [
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D14-1"
        },
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D14-2"
        },
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D14-3"
        },
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D14-4"
        },
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D14-5"
        },
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D14-6"
        },
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-4"
        },
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
      "anchor": "1999 primary的数据边界与设计续路",
      "summary": "保存Danko1999 primary/OA/publicAPI/repo获取边界与missingDCOgates/geometry，不从metadata造source definition，衔接声明的L2设计。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/angular-correlation.md",
      "anchor": "67Ga真实序列的门条件设计与single-marginal盲区",
      "summary": "42-check固定actualspin/chosengeometry前向：R完整区间/失败预测、unknownscalar与pair互反、samefull-photonmarginals却不同jointR；scope严格chosen，不重放NORDBALL。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-7"
        },
        {
          "path": "knowledge/sources/nndc-2005-67ga-selected-level-gamma-records.md",
          "locator": "N67-9"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-3"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-11"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-26"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "summary": "新增双线energy-time条件模型、r²/r⁶/r⁸信息阶、独立积分及未知非负响应尾精确反例；不是actual order fit。",
      "anchor": "近邻双线的能量—时间可识别性与响应混淆",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-9"
        },
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-12"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
      "anchor": "Day14接受稿复核：连接终点、门与版本边界",
      "summary": "增加接受稿17页复核与LV25-16–25；Q1endpoint/sharedgate/分组/one-sided/同采集及配置版本边界，修旧locator和claimtable解析，旧flags保持。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-16"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-17"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-18"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-19"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-20"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-21"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-22"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-23"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-24"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-25"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "anchor": "136Pr：双门重排、共享门峰与模型分带",
      "summary": "新增实际5level6edge逐线/门/空栏/相关closure与Q1端点+4ℏ；分开model partition与event evidence。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-16"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-17"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-18"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-19"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-21"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-22"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-23"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-24"
        }
      ]
    },
    {
      "knowledge": "knowledge/nuclei/136pr.md",
      "anchor": "连接重排和数据依赖的Day14核验",
      "summary": "补Q1endpoint和π/弱线空栏，修发表年与全事件pool分母，保留D5/D6模型辅助分带。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-16"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-18"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-19"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-20"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-23"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-thesis-evidence-matrix.md",
      "anchor": "136Pr Q1 endpoint / D5-D6 partition",
      "summary": "新增A130实际谱学矩阵row及下步观测/独立性，不将模式比较写为测得形变。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-16"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-19"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-20"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-23"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-24"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
      "anchor": "136Pr 2025：同一acquisition的跨核素复用",
      "summary": "增加Ref16与136Pr共同dataset回链，旧LV19全部needs_review和page review保持。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-20"
        }
      ]
    },
    {
      "knowledge": "knowledge/experiments/jurogam2-135nd-ar40-152mev.md",
      "anchor": "同一pool的136Pr分析：channel与acquisition分开",
      "summary": "保持135Ndchannel入口，补136Pr与Ref16/31同pool、不移借calibration/τ/POL的边界。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-20"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
      "anchor": "136Pr：选定2018评价对象",
      "summary": "固化截止前已读两NNDC对象和旧endpoint/order/π/normalizer/primaryreadiness，不冒充1996全文。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-1"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-2"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-3"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-4"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-5"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-6"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-7"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "anchor": "136Pr：2018评价与2025接受稿的顺序冲突",
      "summary": "保存旧新263/405次序和Q1endpoint的versioncrosswalk；原因unknown，不新拟合。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-1"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-3"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-4"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-5"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/nuclei/136pr.md",
      "anchor": "旧评价的版本与次序边界",
      "summary": "核素入口补旧评价/接受稿冲突和更弱π，不改变模式。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-3"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-4"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-thesis-evidence-matrix.md",
      "anchor": "136Pr旧评价与新接受稿：拓扑仍须逐线验证",
      "summary": "补实际A130row的version/order风险与最小续路。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-3"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-4"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "[[nndc-2018-136pr-selected-level-gamma-records]]",
      "summary": "新增旧评价可恢复导航，来源不是新独立采集。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-1"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
      "anchor": "LV25-26",
      "summary": "将截止前已读接受稿405/263直接表行形成atomicclaim，并回链旧评价；不补差异原因。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-26"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "anchor": "近邻双线的反冲能量—张角信息与静态排序边界",
      "summary": "新增共末态精确recoil/order energy-angle kernel、未分峰信息和stopping/nuisance边界；66check为声明设计，非actual193Bi。",
      "sources": [
        {
          "path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
          "locator": "HE15-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
      "anchor": "LV25-27",
      "summary": "增加已核263/405的RI/R/parent与495.4入口候选；相对强度不认证totalflow。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-27"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
      "anchor": "N136-9",
      "summary": "增加旧reactionRI/空CC-MR与adopted每parent100边界，有限parser逐列核验。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "anchor": "136Pr：相对强度、缺失分支与独立母态标签",
      "summary": "新增44check positiveflow/完整两线投影等价与parenttag设计，hiddenfraction只为zeroIC控制，不定真实次序。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-27"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
      "anchor": "LV25-28",
      "summary": "固化actualTableI156row提取、spacedparent和identity边界，不冒充作者newgamma计数。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-28"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
      "anchor": "旧记录到新表的候选scope",
      "summary": "保留旧136G/135placed+unplaced读取范围和新旧scope差，linkedcandidategraph。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-28"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-1"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "anchor": "136Pr：逐线候选图与energy-nearest的失败",
      "summary": "新增44check逐线候选图、energy-only唯一错配与parent窗错拒Q1，不给真配对/新线数。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-28"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-1"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-4"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-16"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-thesis-evidence-matrix.md",
      "anchor": "136Pr transitionidentity：候选唯一不等物理唯一",
      "summary": "矩阵增加candidateidentity充分性与coverage契约，源定位一一回链。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-28"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-1"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
      "anchor": "D3的new-band与旧level候选分层",
      "summary": "新增D3精确分支与electricassignment假设/ΔJ0/空栏原文边界。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-29"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-30"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
      "anchor": "N136-10",
      "summary": "保存旧5085.7/650.1无band无πcandidate，非新stateidentity证明。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "anchor": "136Pr D3：新带、旧态候选与宇称handle",
      "summary": "新增D3旧态候选/新带/987πhandle分层与小图，source13checks非新fit。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-29"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-30"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/nuclei/136pr.md",
      "anchor": "D3 novelty与π的证据层",
      "summary": "核素入口同步newband/oldlevel候选与作者E2策略条件，不改labels。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-29"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-30"
        },
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
      "anchor": "同parent强度比的条件表图复核",
      "summary": "新增D4八对原表/图/空M/未给δCov的直接范围与条件重算回链。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-31"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/bm1-be2-ratio.md",
      "anchor": "同母态radiative比值的抵消条件",
      "summary": "新增同parent radiativeB商公式和τ/ICC共同分母抵消的输入契约，保留δ/purity/response。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-31"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "anchor": "136Pr D4：同母态比值重算与绝对强度的区别",
      "summary": "新增71check D4八同parent比值、单位/误差/空栏/图表一致性边界，不给absoluteB。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-31"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/nuclei/136pr.md",
      "anchor": "D4 sameparent派生比值的scope",
      "summary": "核素入口同步conditionalratio/absoluteB区分与D6限值/模式边界。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-31"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
      "anchor": "TableII列示与完整模型输入",
      "summary": "新增LV25-32 source-conditional粒子数账本边界，valence通过，不推实际程序不守恒。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-32"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/configuration-occupation-audit.md",
      "anchor": "组态列示的占据数与完整性审计",
      "summary": "新增62check general必要numberparity/active-vs-complete方法，保留未列spectator未知，不填轨道。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-32"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-model-choice-card.md",
      "anchor": "136Pr模型输入：列示轨道与完整阻塞态分开",
      "summary": "模型选择卡补actualTableII输入readiness、sourcecaption必要条件非充分和2/7覆盖不变。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-32"
        }
      ]
    },
    {
      "knowledge": "knowledge/nuclei/136pr.md",
      "anchor": "TableII输入完整性的边界",
      "summary": "核素入口同步sourceinput完整性和Π/numberparity区别，无新mode/π裁决。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-32"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "[[configuration-occupation-audit]]",
      "summary": "新增可复用组态占据方法导航。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-32"
        }
      ]
    },
    {
      "knowledge": "knowledge/questions.md",
      "anchor": "Q1/Q1* 的未列旁观者与粒子数奇偶",
      "summary": "将完整清单/active标签、实际blocking/reference必要输入变成后续问题，不自动用户待办。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-32"
        }
      ]
    },
    {
      "knowledge": "knowledge/questions.md",
      "anchor": "263/405 的旧新次序差异源于重排还是记录版本",
      "summary": "将原先已证实的旧新sourceorder差异与原文缺口写入中心问题页。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2018-136pr-selected-level-gamma-records.md",
          "locator": "N136-4"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-26"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
      "summary": "完整阅读109Ag TAC-RHB配对方法；记录blocking、未恢复粒子数、回弯失败、磁矩算符依赖与预印本公式边界。",
      "anchor": "Wang（2017）：109Ag 的 TAC-CDFT 可分离配对方法",
      "sources": [
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-1"
        },
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-3"
        },
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-5"
        },
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-7"
        },
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-9"
        },
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-10"
        },
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-11"
        },
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-12"
        },
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-13"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/configuration-occupation-audit.md",
      "summary": "固化spin与species配对条件、finite-Fock numberparity控制、formfactor维度和Dirac组件缩放，均不填Pr136真实输入。",
      "anchor": "配对方法companion不能补全实际阻塞输入",
      "sources": [
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-1"
        },
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-2"
        },
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-3"
        },
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-5"
        },
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-9"
        },
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-10"
        },
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/models/tilted-axis-cranking.md",
      "summary": "添加实际109Ag方法的半经典I、blocking、局部收敛失败与磁矩算符边界。",
      "anchor": "2017年方法校准：阻塞、收敛与磁矩算符",
      "sources": [
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-4"
        },
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-6"
        },
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-7"
        },
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-8"
        },
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-model-choice-card.md",
      "summary": "将方法companion与Pr136实际input缺口分开，保持2/7直接投影覆盖及原模式排序。",
      "anchor": "方法companion的可迁移边界",
      "sources": [
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-3"
        },
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-5"
        },
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-9"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-32"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "索引本次公开方法来源及其迁移限制。",
      "anchor": "109Ag TAC-RHB可分离配对",
      "sources": [
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
      "summary": "完整核读TAC-RHB上游阻塞定义、平面/回弯边界与模型重用实验；记录43-check实canonical/BdG条件审计。",
      "anchor": "Zhao等（2015）：配对对核自旋取向的影响",
      "sources": [
        {
          "path": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
          "locator": "ZT15-1"
        },
        {
          "path": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
          "locator": "ZT15-3"
        },
        {
          "path": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
          "locator": "ZT15-4"
        },
        {
          "path": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
          "locator": "ZT15-6"
        },
        {
          "path": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
          "locator": "ZT15-9"
        },
        {
          "path": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
          "locator": "ZT15-10"
        },
        {
          "path": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
          "locator": "ZT15-11"
        },
        {
          "path": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
          "locator": "ZT15-12"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/configuration-occupation-audit.md",
      "summary": "将O1/O2、reference变换、相位/tie/零norm与最小重放字段固化；不认证作者实现或Pr136实际输入。",
      "anchor": "O1/O2阻塞追踪的可重放契约",
      "sources": [
        {
          "path": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
          "locator": "ZT15-3"
        },
        {
          "path": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
          "locator": "ZT15-4"
        },
        {
          "path": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
          "locator": "ZT15-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/models/tilted-axis-cranking.md",
      "summary": "补入直接阻塞来源及平面方法和实验/模型层级边界。",
      "anchor": "2015年上游阻塞方法与平面限制",
      "sources": [
        {
          "path": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
          "locator": "ZT15-3"
        },
        {
          "path": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
          "locator": "ZT15-4"
        },
        {
          "path": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
          "locator": "ZT15-6"
        },
        {
          "path": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
          "locator": "ZT15-9"
        },
        {
          "path": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
          "locator": "ZT15-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-model-choice-card.md",
      "summary": "细化方法companion的重放缺口，不增Pr136实验/投影覆盖。",
      "anchor": "直接读其上游",
      "sources": [
        {
          "path": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
          "locator": "ZT15-3"
        },
        {
          "path": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
          "locator": "ZT15-4"
        },
        {
          "path": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
          "locator": "ZT15-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
      "summary": "对其Ref31加直接来源后续核验链接，不改原claims/review。",
      "anchor": "上游阻塞方法的后续核验",
      "sources": [
        {
          "path": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
          "locator": "ZT15-3"
        },
        {
          "path": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
          "locator": "ZT15-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "索引O1/O2直接方法和适用边界。",
      "anchor": "135Nd TAC-RHB配对与O1/O2准粒子阻塞定义",
      "sources": [
        {
          "path": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
          "locator": "ZT15-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-model-choice-card.md",
      "summary": "形成2015→2017→2025配对/阻塞方法谱系批次REFLECT，分开参数/算符/代码版本与独立实验计数。",
      "anchor": "配对方法谱系的批次REFLECT",
      "sources": [
        {
          "path": "knowledge/sources/zhao-2015-pairing-spin-orientation-tac.md",
          "locator": "ZT15-3"
        },
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-3"
        },
        {
          "path": "knowledge/sources/wang-2017-109ag-tac-separable-pairing.md",
          "locator": "W17-9"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-4"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-32"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
      "summary": "核TableII/Fig16与alternative signedγ/转轴的原文分层，新增LV25-33而不改原flags。",
      "anchor": "γ、模型形状与替代转轴场景的定向复核",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-33"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/triaxial-deformation.md",
      "summary": "新增声明normal form与50-check精确恒等式/转轴控制，不认证完整态或作者frame。",
      "anchor": "形状张量、轴置换与signedγ分开",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-33"
        }
      ]
    },
    {
      "knowledge": "knowledge/nuclei/136pr.md",
      "summary": "分开实际模型βγ、alternative与实验共存，保留竞争解释。",
      "anchor": "γ与相对转轴的解释边界",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-33"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-model-choice-card.md",
      "summary": "补模型input/shape/orientation界面，保持2/7投影覆盖和原排序。",
      "anchor": "136Pr的γ、形状与转轴分层",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-33"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/petrache-2015-nd-exotic-rotations-triaxiality.md",
      "anchor": "Petrache（2015）：Nd核的特殊转动与三轴性",
      "summary": "完整读三页正文/一图一表，记录γ/axis的模型语境、J2筛选/寿命验证、census算术和证据转移边界。",
      "sources": [
        {
          "path": "knowledge/sources/petrache-2015-nd-exotic-rotations-triaxiality.md",
          "locator": "PT15-2"
        },
        {
          "path": "knowledge/sources/petrache-2015-nd-exotic-rotations-triaxiality.md",
          "locator": "PT15-4"
        },
        {
          "path": "knowledge/sources/petrache-2015-nd-exotic-rotations-triaxiality.md",
          "locator": "PT15-5"
        },
        {
          "path": "knowledge/sources/petrache-2015-nd-exotic-rotations-triaxiality.md",
          "locator": "PT15-6"
        },
        {
          "path": "knowledge/sources/petrache-2015-nd-exotic-rotations-triaxiality.md",
          "locator": "PT15-8"
        },
        {
          "path": "knowledge/sources/petrache-2015-nd-exotic-rotations-triaxiality.md",
          "locator": "PT15-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/triaxial-deformation.md",
      "anchor": "Nd系统学的直接伴随源",
      "summary": "以实际Ref48校准signedγ与相对轴，保留选带/寿命和非唯一解释限制。",
      "sources": [
        {
          "path": "knowledge/sources/petrache-2015-nd-exotic-rotations-triaxiality.md",
          "locator": "PT15-4"
        },
        {
          "path": "knowledge/sources/petrache-2015-nd-exotic-rotations-triaxiality.md",
          "locator": "PT15-5"
        },
        {
          "path": "knowledge/sources/petrache-2015-nd-exotic-rotations-triaxiality.md",
          "locator": "PT15-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
      "anchor": "Ref48的实际证据层级",
      "summary": "直接核其Ref48，区分一般Nd解释与未取得的Pr136真实frame/极化输入。",
      "sources": [
        {
          "path": "knowledge/sources/petrache-2015-nd-exotic-rotations-triaxiality.md",
          "locator": "PT15-4"
        },
        {
          "path": "knowledge/sources/petrache-2015-nd-exotic-rotations-triaxiality.md",
          "locator": "PT15-5"
        },
        {
          "path": "knowledge/sources/petrache-2015-nd-exotic-rotations-triaxiality.md",
          "locator": "PT15-6"
        },
        {
          "path": "knowledge/sources/petrache-2015-nd-exotic-rotations-triaxiality.md",
          "locator": "PT15-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "Nd高自旋J^(2)系统学、signedγ/转轴解释与寿命检验边界",
      "summary": "索引本次必要companion和二级证据边界。",
      "sources": [
        {
          "path": "knowledge/sources/petrache-2015-nd-exotic-rotations-triaxiality.md",
          "locator": "PT15-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/moments-of-inertia.md",
      "anchor": "绝对标签、有限差分与有序路径",
      "summary": "新增实际D4有限response、stencil/位置/交错signature、条件协方差与声明筛选敏感性，不赋Pr形状或复现Nd均值。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-34"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-35"
        },
        {
          "path": "knowledge/sources/peng-chen-2022-chiral-rotation-rhodium-isotopes.md",
          "locator": "PC22-19"
        },
        {
          "path": "knowledge/sources/petrache-2015-nd-exotic-rotations-triaxiality.md",
          "locator": "PT15-4"
        },
        {
          "path": "knowledge/sources/petrache-2015-nd-exotic-rotations-triaxiality.md",
          "locator": "PT15-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "anchor": "136Pr：动力学惯量需要有序路径",
      "summary": "固化两个14+分支的小graph与nominalclosure，区分相同band/母态/ΔI与有序路径。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-34"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-35"
        },
        {
          "path": "knowledge/sources/petrache-2015-nd-exotic-rotations-triaxiality.md",
          "locator": "PT15-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
      "anchor": "D4有序能量练习",
      "summary": "新增graph/6.7keV差的source rows及本任务派生边界，保留原claims/review。",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-34"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-35"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/peng-chen-2022-chiral-rotation-rhodium-isotopes.md",
      "anchor": "Day14定向公式回查",
      "summary": "直接核PDF6 Eq2/3与频率句，新增locator且不替作者图坐标或扩原review。",
      "sources": [
        {
          "path": "knowledge/sources/peng-chen-2022-chiral-rotation-rhodium-isotopes.md",
          "locator": "PC22-19"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
      "anchor": "Matev等（2007）：A≈130有效四极矩与对齐的可加性",
      "summary": "完整读v1并固化34行模型矩阵、Qt定义、oddcore、模型残差/实验谱系和条件version边界，不新造测量。",
      "sources": [
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-1"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-2"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-4"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-6"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-8"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-10"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-11"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-12"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-13"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-14"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-15"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-16"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-18"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/transition-quadrupole-moment.md",
      "anchor": "从旋转系算符到Qt的输入契约",
      "summary": "固化Qt坐标/归一、反问题、共享估计器/模型fit误差与实际tableaudit；声明联量应用不作Pr结果。",
      "sources": [
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-1"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-2"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-6"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-8"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-10"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-11"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-18"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/configuration-occupation-audit.md",
      "anchor": "奇A reference的实际方法例子",
      "summary": "增加实际131Ce oddreference occupation计数与相对c定义，不替Pr确定core/blocked。",
      "sources": [
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-4"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-5"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-13"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-16"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-18"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-model-choice-card.md",
      "anchor": "Qt与相对occupation的迁移边界",
      "summary": "将unpaired HD/SD方法与ND131Ce/Pr框架和新实验分开，保持原投影覆盖/模式排序。",
      "sources": [
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-2"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-4"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-6"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-10"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-11"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-18"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/petrache-2015-nd-exotic-rotations-triaxiality.md",
      "anchor": "PT15-10",
      "summary": "核Ref32/46同文复引与Ref47模型/数据来源边界，不加独立证据。",
      "sources": [
        {
          "path": "knowledge/sources/petrache-2015-nd-exotic-rotations-triaxiality.md",
          "locator": "PT15-10"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "HD/SD无配对CHF/CRMF的Qt/有效对齐与奇A reference",
      "summary": "索引必要Qt方法source及版本/迁移限制。",
      "sources": [
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-1"
        },
        {
          "path": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
          "locator": "MT07-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/riley-2001-global-lifetime-a135.md",
      "summary": "保存13页作者报告主线、33行typed实际Qt、五门/一侧馈pair、误差范围/外源谱系与负号归一；不是逐τ重分析。",
      "anchor": "Table I：保留分析角色的33行账本",
      "sources": [
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-1"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-2"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-3"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-4"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-5"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-6"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-7"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-8"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-9"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-10"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-11"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-12"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-13"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-14"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/transition-quadrupole-moment.md",
      "summary": "分开带/signature/gate/feeding/bound；保存实际pair变化、条件Qt→B/τ、未知Σ和figure绑定与算符归一。",
      "anchor": "全局Qt表的分析选择与数据身份",
      "sources": [
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-3"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-4"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-5"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-6"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-7"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-8"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-9"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-10"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-11"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-12"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-shift-attenuation-method.md",
      "summary": "方法定义补centroid shift，保存实际门/β′定义、FITFTAU恒定Qt与systematics/L4输入边界。",
      "anchor": "质心位移与恒定Qt提取：Riley2001",
      "sources": [
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-1"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-2"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-3"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-4"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-5"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-7"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-8"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-9"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-14"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
      "summary": "追加MT07-19限定全图共采集读法；Riley/外源和reference编号分开，原18条flag/数值保留。",
      "anchor": "上游作者报告补核与数据谱系",
      "sources": [
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-1"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-5"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-9"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-11"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-12"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "新增直接实验作者报告导航；无重复实验计数。",
      "anchor": "[[riley-2001-global-lifetime-a135]]",
      "sources": [
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-1"
        },
        {
          "path": "knowledge/sources/riley-2001-global-lifetime-a135.md",
          "locator": "RI01-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
      "anchor": "Day14定向重读：表角色、估算与速度归一",
      "summary": "补全八行typed原表、半贡献6.07估算、β通道/可见top与7.3/7.4原始reference；六newclaims true，保留旧十三条与Qsf边界。",
      "sources": [
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-5"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-6"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-11"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-12"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-14"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-15"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-16"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-17"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-18"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-19"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/transition-quadrupole-moment.md",
      "anchor": "同一表中的分段fit、计算估算与原始reference",
      "summary": "分开same-band替代fit、model estimate与actualconfiguration，Q0/geometry/引用baseline仍有边界。",
      "sources": [
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-5"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-11"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-12"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-13"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-14"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-15"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-19"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/doppler-shift-attenuation-method.md",
      "anchor": "同束靶的通道速度与可见带顶归一",
      "summary": "α tag与通道β、F尺度和top未见高跃迁反证；未知grid/Σ不补τ。",
      "sources": [
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-1"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-5"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-6"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-11"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-16"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-17"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-18"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md",
      "anchor": "后续[[petrache-1998-highly-deformed-lifetimes-131ce-nd]]",
      "summary": "新增MT07-20原始reference校准，7.4来自Clark而Petrache自己7.3；原sourceflags/值不改。",
      "sources": [
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-14"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-19"
        }
      ]
    }
  ]
}
```

### Day15预习的canonical增量

- [Zheng2002 source](../../knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md)：Z02-6/7/8，原式组效率、calculated deviation和Ref3谱系。
- [角分布方法](../../knowledge/methods/angular-distribution.md)：ADO计算单与group/individual response、额外输入、covariance、条件桥，以及RB67-4的even-K条件修正。

### 条件响应的canonical增量

- [角关联方法](../../knowledge/methods/angular-correlation.md)：conditional density、K1/K2、pair/azimuth/finite-cone反例与matched-response输入。
- [RB1967 source](../../knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md)：局部原图/公式条件复核，RB67-3/11；[Zheng source](../../knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md)新增Z02-9迁移边界。

### 67Ga条件迁移的canonical增量

- [Zobel1983 source](../../knowledge/sources/zobel-1983-energy-projectile-alignment.md)：新Z83-11–14、原表/误差/依赖/mainline scope；原人审不扩展。
- [角分布方法](../../knowledge/methods/angular-distribution.md)：10行原表数据、条件Gaussian模型/标准差s约定、unknownCov、mixture与Fig3坐标核算及图。

### Ref7 原始寿命依赖的有界外部核验

本段保存了[原文前依赖回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/nieminen-before-source-recall.md)，以nature-academic-search/nature-downloader做一个DOI pack。Crossref确认Nieminen2004题名、作者、卷69/DOI；arXiv初查询400，简化query0结果；OpenAlex exact DOI closed，OA downloader exit0但下载0、oa_not_found；APS前缀502、直接HTTPS403 HTML，JYX候选API超时，Scholar工具超时。详见[access recap](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/nieminen-access-recap.json)。自动confirmed_oa标签未采信：APS default license不代表OA，且同manifest的Unpaywall为false；candidate URL不等于PDF已取。

未新增Nieminenprimary source页或猜测其寿命方法/数据谱系；153-ns仍为HE15-12的外部bandhead引用，canonical source页已固化此边界。保持研究active，转向公开193Bi evaluation做版本/locator/依赖审计，不将评估当独立复测。

### NNDC193Bi evaluation：实际数据crosswalk与weak-line反证

[评估来源前预测](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/evaluation-before-source-recall.md)先于数据打开。旧NNDC接口404、IAEA403后，解析NNDC实际form取得193083001/193083004两个官方ENSDF对象（827/819行，201709；ADOPTED有2019ERR）。SHA/version/POST参数与精确locators固化到[[nndc-2017-193bi-level-scheme-evaluation]]；raw保持不变，文本临时保存，raw槽仅reserved/unpopulated。NDS381页论文未全读，实际范围为selected data-object audit。

代码 `system/scripts/day14_ensdf_crosswalk.py` 实际exit0，79/79 identity/column/RI/weak-line/SD/条件branch检查通过。五level为605.53(18)、928.93(21)、1228.13(21)、1555.30(25)、1875.1(3)keV；原七γ中心值一致，reaction RI为原表0.1倍，selected adopted母态又重标强线100。N193-2/3明确采用2015He27并least-squares/quadrature处理；它验证评价规则，未给jointΣ，也不是独立复测。

最实质的反证：N193-5的393/394只列Q，明确shared negativePOL与placement-implied(E2)不一致，order未established；N193-6的352.3 multipolarity留空，评论原Table I(13/2−)→(11/2−)/M1与Figure2在1610的15/2−冲突。已视觉回看PDF p.9与p.7，新增primarysource HE15-15；若Figure2 ΔI=2，M1被single-photon triangle排除，但不能据此选出最终spin。原source的tentative标签与needs_review不清除。

N193-7取得的是pure-multipole BrIcc/Frozen-Orbitals CC，更新“ICC完全缺失”的边界：计算值有了，δ/branch completeness/parentτ仍未给。在两已报告channel的条件模型中，三母态的M1photon fractions为0.5142/0.5276/0.4416，含conversion的M1conditional branches为0.7543/0.7206/0.6138，不是实测totalbranch或absoluteB。N193-8把bandhead153-ns引用定位到604.7γ(t)/2004Ni06，compiler flight/intensity摘要不替代Ni04完整方法。N193-9保留14个X表达式与unplaced1836candidate。

Canonical知识已写回source、method及thesis matrix；[[level-scheme-reconstruction]]保存完整matrix、公式、normalization和赋值冲突。最高信息路线仍是解除这些具体未定约束，不以重复query或更多校准位数判结构。

### Checkpoint001送达后：shared POL 与joint hypothesis

同session实际收到clockcheckpoint001并在run.json.observed_clock_executions保存clock_event_id/same_session_id/observed_at；原queued20:56时间与实际ack22:04分开，不新建session/daemon。Run仍running、day14、原次日15:00截止；不因卡完成停止。

[计算前预测](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/shared-polarization-before-calculation.md)先于本段model。重核RB原图printed316/PDF11 Eq3.24与polarization/WE paragraph，rawhash一致；不是重读全部42页。`system/scripts/day14_shared_polarization_limits.py` 70项均通过，独立vector-gradient与Wigner/helicity kernels一致、convexcount恒等式、isotropy/normalization、LP必要域与核CG案例验证。

共享A按校正counts正权重混合，negative mean不能指定哪条line磁性，但可限制joint positivity；a(E)在.6keV的近邻差仅使floor约−1.484×10⁻5。若固定rawratio而仅重标a将mean推到0，需要增加16.45%；这不是sourcecalibration错误或新significance。

PureE2在合法取向下可negative P；在本段common selection/轴对称/point response/fixed Q_sens下，同时施加Rexp≈1.26后，pureE2 outer set的A为+.03325到+.09507，mean−.076位于外侧。2×printed-error box无解、3×有解都是sensitivity ranges，不是joint CI。分别改变有效选择能匹配两个单变量，hypothetical M2也能在松弛CG模型中匹配joint mean，但需opposite parity，未给任何line的新M2/Jπ。

[必要域图](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/shared-E2-response-region.svg)经PNG视觉检查，标签/边界可读；[完整结果](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/shared-polarization-limits.json)。Canonical落点为[[linear-polarization-asymmetry]]“未分峰偏振的联合命题与选择条件”及[[level-scheme-reconstruction]]“Shared POL 对joint命题的条件约束”。Actual beam/gate/geometry/Σ仍缺，NDS的Q及所有review flags保留。

### 系数约定练习：Day15无学分预习

本批复核Z83-1（p389 Eq1/2）、Z83-11（p392 Table1）与Z83-12（p393统计dependence），完成[17-check计算](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/angular-coefficient-conventions.json)。canonical为[角分布系数](../../knowledge/observables/angular-distribution-coefficient.md)“拟合系数、核取向与最大辐射系数的层级”。声明pureE2/point参考的c=(40/91,−216/1001)，原alpha(.973,.803)条件转为Aexp(.427692308,−.173274725)，marginalerrors(.016263736,.019420579)；不是新实测表列。

固定D的Cov变换会翻转rho符号，但同变换后的联合距离不变；chosen rho+.6与chosen比较点仅作控制。错把alpha当A仍可归一且全角为正，所以源定义不能用这些数值检查代替。β0 cross项、δ/acceptance nuisance必须保留，未知真实Cov仍未知；决定supports变量层级、limits同名量合并。原observable mixed-EOL/审核metadata已保留。此前[[attenuation-coefficient]]已有区分，本批核对后未重复改写；不计Day15、不改21/24。

### Ref5原文公式与联合覆盖：持续研究增量

[primed来源前回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/zobel80-before-source-recall.md)在打开source/raw前冻结；Crossref200/sha-verified9页、全部图/表/公式/Appendix主线核验见[mainline audit](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/zobel80-mainline-audit.json)。[[zobel-1980-magnetic-substate-distributions]] Z80-14/15/16记录p231 A2相对误差乘积缺项、A6与A4的cross-sign不一致及A3正标准差约定。A5本身须配合Q/2看，不误判独立少因子2。它们是扫描转录与Codex代数自审，未取得officialerratum；原Human/旧flags保留，新14–19 needs_review true。

[23-check计算](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/zobel80-appendix-analysis.json)给chosen positiveCb上的A2字面负variance、正确ratio covariance；joint68% fullQ=2.278868566，Q=1内容.393469340。chosen rho+.6的错cross-sign ellipse内容.520066461（512/1024积分一致）；这些不是source实验Cov或原ALY p-value。完整公式、矩阵、覆盖与反例写入[[angular-distribution]]“Zobel1980附录：字面公式与联合覆盖”。

Z80-17一行同parent数据核c/sign打印舍入，Z80-18/[[zobel-1983-energy-projectile-alignment]] Z83-13核Ref9/4同Zobel1979依赖，不能认证独立raw events。Z80-19保留scan未见Table3、GNOMON未发布的数值重放缺口；Fig4/5是原model control，companion仍需完整peak面积、fitCov、matching feeding/条件。决定revises公式的字面执行，supports保留Cov，limits把marginal误差、引用次数或ALY/Gaussian曲线当唯一布居事实。不改变21/24、不计Day15。

### 原表两矩的正布居可行域

经candidate overlap核，RB67-26已覆盖一般pureE2高阶盲区；本项使用[冻结预测](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/positive-population-before-calculation.md)，直接核真实同parent原表的运动学可行域。[40-check计算](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/positive-population-hull.json)保存J13/2正对称diagonal布居的七个exact vertices/halfspaces、Farkas certificate与全部10个Z83非空行加1个Z80行的LP状态。条件中央值(.973,.803)给−107/1000证书，fixed-reference hull要求此alpha2下alpha4≥.910；其余10个points有严格正见证。这不是实验否定、真实P重构或对作者code的归因。

在quotedmarginal errors加chosen GaussianΣ控制中，rho−.8/0/+.8/+.95给最近hull距离平方.278760/.491139/2.062470/5.154627；joint68椭圆相交的判断随ρ变化，真实Σ仍未知。Canonical[[angular-distribution]]“正布居矩可行域与源表中央值”保存全域顶点、原表、数学证书、witness/误差边界及[图](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/positive-population-hull.svg)。决定revises可行性先于Gaussian宽度反演，supports量子正性与未知response边界。无新source card信用、无实验σ/I或mode赋值。

### 必要1979 companion的获取边界

[[zobel-1980-magnetic-substate-distributions]] Z80-20固化Ref4/9的真实DOI/title/NPA316,165–188(1979)与access/readiness。nature-downloader出版商API返回credentials_missing，合法OA返回oa_not_found、publicPDF无candidate，精确Scholar检索timeout；没有primary或新raw。下载器confirmed_oa标签不能沿用：所给TDMuserlicense不是OAlicense，Unpaywall实际false。来源前回忆、各manifest/metadata保留在本run；没有修改credentials/进入宿主GUI。

停止该获取路线，仍缺primary中的δ/purity误差、采集/response细节，这些输入限制正布居检验与数据独立性。最高信息续路为NNDC 67Ga公开evaluated/reaction字段核验，source dependency与unknownCov继续保留，不能凭评价对象给实验新学分或假定独立。正文学习与正式卡均未因此重复计分，run仍active。

### 67Ga公开objects：source/τ/RI/δ/B的实量核验

[总体primed回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/nndc67-before-source-recall.md)先于NNDC查询冻结，按FLAG O/Q再[补读预测](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/nndc67-ri-source-before-recall.md)。取得4个sha-verifiedobjects：ADOPTED、Fe12C、alpha/16O、Ni58；后三者全文、adoptedglobal与selectedL/G已核，不宣称读92页masschainpaper。Canonical[[nndc-2005-67ga-selected-level-gamma-records]] N67-1–8保存versions/currentupdates、exactrecords、refs与4组hash。

N67-2/3的958为E2(+M3)、δ−0.00(1)，finite .01与alpha1978Al32依赖保留；Fe M/MR fromadopted不是另一测量。N67-5 parent4.5(4)ps为T1/2→mean6.492ps；两个feedersmean230.831/15.870ps不能借给此γ。N67-4的Fe58.2归一359+1202，与parent100(9)/weak.2(1)不同；空白M/CC不补0。

[38-check](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/nndc67-strength-crosswalk.json)按[[lange-kumar-hamilton-1982-multipole-admixtures]] LKH82-1与既有现代SIrate conversion，在zeroIC/complete2γ/δ0的declaredcontrol算B(E2)=9.61853WU，与source BE2W9.6(9)printing相容；不是新strength测量或actualevaluatorcode重放。模型/unknownCov/half-life失败控制、weakICC敏感性已写[[level-scheme-reconstruction]]“67Ga：跨对象的parent与强度输入核验”。

反证N67-7：actualNi对象给958E2与554E1同DCO1.45(7)，sameparent871E1则.77(3)，exactgates/reference/geometry缺，ratio不能单独赋E2；N67-8保持2862的未分1343/1353和π conflict的compiler可能解释。决定supports逐field来源，revises exactδ0/错误RI分母/借feederτ，limits B或DCO作mode唯一解释。L3data-object exercise完成，实验L4因原angular/events/response/GF/Cov/完整branch缺仍not-ready；正式21/24不变，Day15无学分。

### actualBrIcc理论输入与forward ledger

查询前[primed回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/bricc67-before-query-recall.md)已冻结。初4请求DE=.4/.05 decimal遭HTTP200校验页拒绝；按ENSDF末位integer4/5修正后4points有实质numericresponse，literalenergy/DE echo、失败与successhash均保留。实际backend BrIccFO/BrIccS2.3(2011)，Z31，没有本地2022/datafile/A67finite-size计算声称。

[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] KB08-D14-1–6为4个theoryinputs：168.8M1/E2 Tot .0175(3)/.0976(17)，958.01E2/M3 .000358(5)/.001513(22)。K与subshells不代Total，E168E2的energyunc>1%警告和缺radius/datafilehash保留；providererror不作独立Σ或再叠interp。原paperHuman/旧flags不扩，新D14全部true。

[32-check forward](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/bricc67-parsed-forward.json)与[32-check offline replay](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/bricc67-offline-replay.json)一致。在complete2γ/无extra、weakM1或E2、strongδ0条件下，B_E2为9.614759/9.613223WU，较zeroIC下降.0392%/.0552%；sourceCC blank不改为实测。全部δ0/.01/.02的6cases保存ledger，不是confidencebounds。若额外假设weak也E2，Bweak/Bstrong=11.776548，展示RI小不等于B小，不作weakM赋值。完整可复用结果在[[level-scheme-reconstruction]]“67Ga：FO理论输入补全的条件强度范围”。supports模型内输入补全，limits全部multipoles/extra/inventory/Cov的无条件结论，实验L4仍notready，不计Day15。

### 缺gate时的有界设计与失败预测修正

Danko99primary合法OA/publicPDF/官方API/repo均未提供正文（403HTML/401JSON边界），[[nndc-2005-67ga-selected-level-gamma-records]] N67-9固化输入缺口，没有补造NORDBALLgate/ref/angles。按[冻结预测](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/dco67-before-calculation.md)固定40°/90°与两个actualspinpath的chosen下方门，[42-check设计](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/dco67-gate-design.json)给A(E2target/E1ref) R区间[.41318,2.55158]，B(E1target/E2ref)[.81132,1.10341]。B不含1.45，首预测被revises，未调角或硬fit；不是sourceE1被排除。

在A中自选sameexactα2=α4=0的positive populations，经fractionalLP/primaldual与rationalmoments核验，jointR完整数值区间[.980174767,1.025136082]。两组完整photon1marginal都I5/5、photon2都I3/3；strictPSD的5%uniform混合仍R不同。因而singleγ校准即使精确，也不自动给出全部joint-gate响应。共同unknownscalar的交集[1.31411,1.78720]仅演示未识别calibration，不能从同targetdata反推source f。

同corrected pair cells若互换target/ref，R产品必1；literal两1.45不能按这种假设计两份独立constraints，不判原作者错误。Allscope/duals/kernels/positivewitness、首scratch单位/JSON失败及未采用边界在[[angular-correlation]]“67Ga真实序列的门条件设计与single-marginal盲区”与run文件。supports精确gate/normalization和独立kernelrow，limits裸ratio/singlemarginal替代jointresponse；无实验pvalue/真实ρ/新的card信用。

新增可复用知识见[[wang-2017-109ag-tac-separable-pairing]] W17-1/3/5/9/10，以及[[configuration-occupation-audit]]“配对方法companion不能补全实际阻塞输入”、[[tilted-axis-cranking]]“2017年方法校准：阻塞、收敛与磁矩算符”和[[a130-model-choice-card]]“方法companion的可迁移边界”。这些canonical页保存了原文方法、条件练习、版本异常和迁移边界；source实际PDF尚在tmp、raw未归档，未把outputs当唯一知识副本。

本段canonical为[[zhao-2015-pairing-spin-orientation-tac]] ZT15-3/4/11、[[configuration-occupation-audit]]“O1/O2阻塞追踪的可重放契约”、[[tilted-axis-cranking]]“2015年上游阻塞方法与平面限制”；[[wang-2017-109ag-tac-separable-pairing]]新增“上游阻塞方法的后续核验”，[[a130-model-choice-card]]细化原方法路线。可重放字段、原文规则、43-check及无实际Pr136输入的限制均在knowledge保有副本。

新增canonical为[[triaxial-deformation]]“形状张量、轴置换与signedγ分开”、[[lv-2025-136pr-tac-covariant-density-functional]] LV25-33和“γ、模型形状与替代转轴场景的定向复核”、[[136pr]]“γ与相对转轴的解释边界”、[[a130-model-choice-card]]“136Pr的γ、形状与转轴分层”。这些页保有50-check推导、实际模型值/alternative locator与未知frame边界，outputs不是唯一副本。

新增canonical为[[petrache-2015-nd-exotic-rotations-triaxiality]] PT15-1–9及Table1算术、[[triaxial-deformation]]“Nd系统学的直接伴随源”、[[lv-2025-136pr-tac-covariant-density-functional]]“Ref48的实际证据层级”。作者待检验解释、mask缺口、数据独立性和公开取得PDF/许可未核均有source locator，未把outputs当唯一知识副本。

新增canonical为[[moments-of-inertia]]“绝对标签、有限差分与有序路径”、[[level-scheme-reconstruction]]“136Pr：动力学惯量需要有序路径”、LV25-34/35和[[peng-chen-2022-chiral-rotation-rhodium-isotopes]] PC22-19。实际能量表、名义曲率、graph/位置、条件Σ与筛选边界在knowledge保有副本；outputs只作完整可重放回执。

新增canonical包括[[matev-2007-a130-quadrupole-alignment-additivity]]的18条分层claims和完整versioned TableII数值矩阵、[[transition-quadrupole-moment]]“从旋转系算符到Qt的输入契约”、[[configuration-occupation-audit]]“奇A reference的实际方法例子”、[[a130-model-choice-card]]“Qt与相对occupation的迁移边界”及PT15-10的数据/复引边界。实际表值、两条条件不相容项、geometry/fit前提与联量应用在knowledge有可复用副本，不只保存在outputs。

### Riley实验报告的canonical增量

新增[原始作者source](../../knowledge/sources/riley-2001-global-lifetime-a135.md)“Table I：保留分析角色的33行账本”，RI01-1–15给实际source locator；[Qt](../../knowledge/observables/transition-quadrupole-moment.md)“全局Qt表的分析选择与数据身份”保存条件换算和未知Σ，[DSAM](../../knowledge/methods/doppler-shift-attenuation-method.md)“质心位移与恒定Qt提取：Riley2001”保存门与输入契约，[Matev](../../knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md)“上游作者报告补核与数据谱系”校准MT07-8的使用。原始模型表的两项条件异常保持，未伪造raw归档或Laird最终重读。

### 原始reference与估算的canonical增量

[已有Petrache source](../../knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md)“Day14定向重读：表角色、估算与速度归一”存完整八行及PE98-14–19（R11–R14原位）；[Qt](../../knowledge/observables/transition-quadrupole-moment.md)“同一表中的分段fit、计算估算与原始reference”和[DSAM](../../knowledge/methods/doppler-shift-attenuation-method.md)“同束靶的通道速度与可见带顶归一”存可复用输入/判断边界；[Matev](../../knowledge/sources/matev-2007-a130-quadrupole-alignment-additivity.md)追加MT07-20明确其Ref39的真正身份。无新增raw/source档案或Clark直接结果。

## Open questions and belief revision

1. 哪个旁路、time/tag或独立spin anchor能裁决393/394的顺序？重复同一能量和不能裁决。
2. 真实response/净计数能否分别识别299.2/299.8、622/626和323 quadruplet？现有绘图不能补出逐门Σ。
3. 哪些parent τ/branch/ICC/δ输入足以把七条线的相对量接到absolute strengths？153-ns引用不能挪用。
4. 1836-keV候选link的endpoint、强度与false-link控制能否闭合X？当前保持未confirmed。
5. 哪些reference/feeding观测足以约束target conditional population？逐层重设同σ/J可能带入额外prior；需原始实测对照。
6. 对实际393/394是否存在同rank pure stretched/共同response的交换对称条件？若成立，角数据本身不提供order；若不成立，需先定位失效的具体premise。

这些是Codex后续研究路线，不自动转成用户待办。认识修订发生在方法充分性上，未改变结构模式排序。

## L0–L4 state

- L0：Herzáň20页主线/图表已正式复核，Zobel1983六页与1980九页完成；另取得67Ga四个publicENSDF对象，selectedrecords/完整三reactionobjects核验，不宣称读取wholemasschainpaper或原1978/79/99全文。
- L1/L2：source/method/matrix、原35检查与后续条件gate/POL/jointγγ/Cov/kinematic-hull均固化；正式六维21/24与weeklyREFLECT保持。
- L3：67Ga实输入/FO理论ICC与声明DCO门模型、193Bi91-check能量—时间设计、136Pr37-check新谱和旧评价crosswalk完成；实际DCO gate/geometry、原事件及1996primary仍缺，无新mode裁决。
- L4：真实event-level重分析not-ready。67Ga已有评价τ/δ，仍缺原angular/event、response、GF/jointCov、完整ICC/branch/stopping/feeding包；193Bi仍缺目标parentτ/δ/actualgates。继续最高价值可执行数据/理论路线，不把模型重算当实验。

本段为L1直接方法读取、L2边界写回与L3声明的canonical/BdG设计控制；没有actual RHB模型运行、原实验重分析或新的实验L4结果。Day14继续，Day15仅partial；source含“chiral”或模型方法不意味着打开Day16课程卡。

## Verification and continuation

首次写科学内容前boundary exit0、无error/warning；H1 preflight exit0，protected Bib基线匹配；EOL清理exit0、未触碰substantive/staged内容。raw PDF哈希与source一致，原raw/PLAN/Bib保持只读。定量脚本实际exit0，35/35。

本checkpoint实际验收：report/card/writeback均valid；wiki_lint --fail-on error exit0，0 errors/128 warnings（107既有citation key、18既有未填raw槽、3reaction parser）；git diff --check exit0；protected PLAN/Bib哈希与raw全树size/mtime均匹配基线。第一次lint exit1因inline矩阵被识别成wikilink，已改为无歧义的行列记法并回归。Gitee实际结果仅run receipt；本段内容通过验收后按显式manifest发布。恢复提示已保存[continuation-prompt](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/continuation-prompt.md)。本报告不是研究收束声明；研究截止保持原receipt，不因卡片或一个来源完成提前结束。

当前快照 2026-10-14T19:35:55.416781+08:00，距原截止1164.1分钟；下一日prompt已准备入口、未创建新session/未计Day15。QMD/overview本次deferred，未扩大维护范围。下一步：刷新clock/候选池，完成同一问题的conditional gate、composite-response与最小branch/time设计；若当前问题局部饱和，再查恰好下一张Day15作无学分预习。任何正式Day15学分留待其独立日run，Day16不打开。

### Checkpoint 002 实测与续接

2026-10-14T21:26:21.851052+08:00；距原截止1053.6分钟，research/goal仍active。35/37/79检查三段均exit0；本段lint exit0（0errors/129warnings：107citation key、19raw slot、3reaction parser），新slot为未归档的公开NNDC对象；首次新source缺Summary/Extracted Pages已补齐并回归。report/card/writeback8items/5pages与protected/rawmetadata通过；diff验收随后同batch记录。

本段知识增量是conditional gate/shared-count/低能γ功效与实际NNDCversion/assignment/ICC crosswalk，未给新spin、absoluteB或mode结论。Checkpoint001已Gitee发布，当前批次稳定subject为 `Audit DAY14 evaluated assignments and conditional branch gates`；exacthash/actualpush仅runreceipt。Clockcheckpoint001只验证queued，未冒称delivery。下一高信息currentroute：shared negativePOL能约束哪种joint(E2,E2)命题及其calibration/weight/geometry边界；之后刷新候选池，若饱和再读恰好Day15无学分预习。Day15未计卡，Day16未打开。

### Candidate-pool refresh：恰好Day15无学分预习

当前sharedPOL模型/反例已固化，仍有决定性缺口为实际matchedgate/acceptance/Σ而不是更多同公式重算。下一未完成cardDay15的ADO/角分布/几何修正是剩余高信息route，已在打开source前保存preview recall，标明priming；这里只列partial15，不计Day15、不创建formal audit、不越过Day15或打开Day16。下一核Zheng2002原定义和公开角度/效率练习，保持今天day14。


### Checkpoint003 实测与继续

2026-10-15 00:02 Asia/Shanghai快照距原截止897.4分钟，仍继续同run/session。本批次70/28项分析均通过；report/card/writeback重验valid，唯一writeback13items/8份本run修改知识页。wiki_lint --fail-on error实际exit0、0errors/129warnings（107citation key、19未归档raw槽、3reaction parser）；git diff --check实际exit0；AST、原review flags、raw/PLAN/Bib核验通过。writeback初次失败因method只写RB claim而未直接链接source；已补RB与Herzáň回链并回归。EOL exit1仅保留4项本run substantive knowledge edits，unsafe/mixed0。

本批次稳定指针 main / `Bound DAY14 shared polarization and ADO response assumptions`；精确hash与实际Gitee结果记录在runreceipt。恢复点[checkpoint003](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/checkpoint-003.md)及continuation已存在。正式21/24不变，Day15仅partial预习；下一current route为conditional γγ joint response、matched gate与finite acceptance，实际193Bi事件重拟合仍not-ready。

暂存门首次发现Matplotlib SVG尾空格，未commit；已在两份export函数去尾空格、固定SVG hash salt并去掉动态date，重执行70/28检查均exit0，数值保持。之后重新验cached diff。


### Checkpoint004 实测与继续

2026-10-15 00:35 Asia/Shanghai，距原截止865.0分钟；research仍active。conditional-response脚本35/35、exit0；report/card/writeback15items/10份本run修改知识页valid。wiki_lint --fail-on error exit0、0errors/129warnings（107citation key、19raw slots、3reaction parser）；git diff --check exit0；AST/protected/raw metadata及原review flags通过。原source仅局部回核所用公式，不重复宣称新全文阅读。

上批次已Gitee发布；本批次稳定指针 main / `Derive DAY14 conditional gamma coincidence response`，实际H3/hash仅receipt。恢复见[checkpoint004](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/checkpoint-004.md)和continuation。下一current为general-spin近邻双线排序可识别性，计算前回忆已保存；不计Day15、不停止整段时窗。


### Checkpoint005 实测与候选池重建

2026-10-15 01:09 Asia/Shanghai，距原截止830.7分钟，仍有substantive window。order脚本实际exit0、51项通过；report/card/writeback17items/10份本run修改知识页valid。wiki_lint --fail-on error exit0、0errors/129warnings（107citekey、19raw槽、3parser）；git diff --check exit0；AST/protected/raw metadata/旧review flags通过。

本批次稳定指针 main / `Test DAY14 doublet angular-order identifiability`，实际publication/hash仅runreceipt。当前模型定理局部饱和但没有结束时窗；近期fingerprint显示Ionescu1981已在10月12日Day11/12使用，暂缓重复，Zobel1983尚未见recent daily/weekly记录。下一Day15无学分知识预习候选为experimental alignment/reference transfer，仍需source-before recall、raw/metadata及主线验证。恢复见[checkpoint005](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/checkpoint-005.md)。


### Checkpoint006 实测与持续研究

2026-10-15 02:57 Asia/Shanghai，距原截止722.0分钟。38项worksheet/图throughpipeline实际exit0，report/card/writeback19items/11份本run修改知识页valid；wiki_lint --fail-on error exit0、0errors/129warnings（107citekey、19rawslots、3parser）；git diff --check exit0；AST/protected/rawmetadata/继承Review及new11–14 true通过。

Figure源/glyph/collision audits均exit0，最小8pt、collision0fail0warn，singlepanel对齐not applicable、PNG视觉通过；源3个export/width warnings已按140×110mm Wiki/vector/400dpi合同逐项核。原文Pubfit、作者解释与自设模型保持分层。原人审不扩到新增claim；正式21/24与partial15保持。

本批稳定指针 main / `Audit DAY14 empirical alignment and covariance limits`；actualH3/hash仅runreceipt。恢复点[checkpoint006](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/checkpoint-006.md)。下一bounded route是angular-fit geometry/normalization怎样影响Cov以及两个marginalerrors不能唯一指定哪些joint判断；需先冻结预测并声明chosen design，不能补出作者GF矩阵。研究未收束，不因一篇source或图完成结束时窗。


### Checkpoint007 实测与继续

2026-10-15 04:19 Asia/Shanghai，距原截止640.9分钟；researchactive。26-check covariance-design实际exit0，report/card/writeback20items/11份本run修改知识页valid；wiki_lint --fail-on error exit0、0errors/129warnings（107citekey、19rawslots、3parser）；git diff --check exit0；AST/protected/rawmetadata/继承Review及new11–15true通过。

本批稳定指针 main / `Demonstrate DAY14 angular covariance identifiability limits`，actualpublication/hash仅receipt。恢复见[checkpoint007](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/checkpoint-007.md)；下一核remaining Day15 coefficient conventions及必要统计source，先查overlap，不重复同prototype换值充填，不计Day15、不打开下一卡。


### Checkpoint008 实测与继续

17项系数约定练习全部通过，report/card/writeback valid（21items/12changedpages）；AST、保护哈希/raw metadata及原审核状态通过。wiki_lint --fail-on error exit0，0errors/129warnings（107citation-key、19raw槽、3reactionparser）；git diff --check exit0。原observable的mixed-EOL字节保持；首个validation harness因错误import exit1，改用现有函数后exit0。

恢复见[checkpoint008](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/checkpoint-008.md)及[实际clock002登记](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/clock-checkpoint-002.md)。本批稳定指针 main / `Clarify DAY14 angular coefficient conventions`，exacthash/actualpush只receipt。研究仍active，下一Ref5统计方法原主线核验已冻结primed回忆；不将方法公式补造成当前dataset的Cov，不计Day15或新开下一卡。


### Checkpoint009 实测与继续

Ref5原9页与23-check Appendix均完成；report/card/writeback valid（23items/13changedpages），AST/保护哈希/raw metadata/原review flags与diff通过。wiki_lint --fail-on error exit0，0errors/129warnings（107citation-key、19raw槽、3reactionparser）。初lint未读入空行后的六条claim，解析验收exit1；修表后freshlint解析Z80-14–19全部true，claims2471、needs_review1797，原13条false保留。

恢复见[checkpoint009](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/checkpoint-009.md)，本批稳定指针 main / `Audit DAY14 primary angular error formulas`；exacthash/actualH3只receipt。候选池核对发现RB67-26已有pureE2布居盲区证明，下一项是源表两moments的positive-population physical hull与中央值可行性，不重复已有泛化反例。Day15仍partial、正式21/24不变、研究继续。


### Checkpoint010 实测与继续

40项rational hull/LP/全source行/未知Cov控制通过；report/card/writeback valid（25items/13changedpages），AST/保护哈希/raw metadata/继承review/diff通过。wiki_lint --fail-on error exit0，0errors/129warnings（107citation-key、19raw槽、3reactionparser）；Z80-20实际parsedtrue。图source/glyph/collision全部exit0，最终0FAIL/0WARN且PNG视觉通过；四项源码WARN按Wiki尺寸、PNG预览和constantlog解释，初clip/标注碰撞修复有QA记录。

本批稳定指针 main / `Bound DAY14 positive-population moments`，exacthash/实际H3仅receipt；恢复见[checkpoint010](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/checkpoint-010.md)。1979获取分支停止、输入边界已canonical；下一公开NNDC67Ga评价/反应字段查验已冻结primed回忆，search200不代表读取objects或新独立实验。研究继续，正式21/24、Day14/partial15保持。


### Checkpoint011 实量检查与持续研究

38-check actualENSDF/source-field/unit/parent/RI/missingCC/finiteMR与DCO反例全部通过；report/card/writeback valid（29items/14changedpages），AST/保护哈希/raw metadata/原review/diff通过。首wiki_lint exit1因新source共用genericNNDCcanonicalURL及缺requiredheading；改actualobjectID/heading后exit0，0errors/130warnings（107citation-key、20rawslots、3reactionparser），8新N67claims全部parsedtrue。rawslot明示未填，未动raw/credentials。

恢复[checkpoint011](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/checkpoint-011.md)。稳定指针 main / `Audit DAY14 real ENSDF lifetime and branching inputs`；精确hash/actualH3只receipt。Currentpool仍有usefulweakICC/branch与DCOdefinition路线，researchactive；下一boundedatomicresponse或1999primary只补同一问题，不开新card、不计Day15、不改变21/24。


### Checkpoint012 theoryresponse检查与继续

4actualFO输入、32captured checks与32offline replay同值；report/card/writeback valid（31items/15changedpages），AST/保护哈希/raw metadata/原Human及旧flags/diff通过。wiki_lint --fail-on error exit0，0errors/130warnings（107citation-key/20rawslots/3parser），6新KB08-D14全部parsedtrue；未清N67sourceCC、未产生实验ICC/新B或新card credit。

恢复[checkpoint012](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/checkpoint-012.md)，稳定指针main / `Add DAY14 theoretical conversion response inputs`，exacthash/actualH3仅receipt。下一Danko1999 primaryDCOdefinition的legalretrieval已freezeprimedrecall；OA未取得/直接publisher403，继续boundedlegitimatemetadata定位，不伪造geometry/gates。原researchwindow仍active，正式21/24、Day14/partial15不变。


### Checkpoint013 门条件设计验收与pool复核

42-check chosen40/90真实spinpath前向设计、失败预测/范围、LP/duality/rationalmoments/fullsinglephotonangularmarginals与互反均通过；report/card/writeback valid（33items/15changedpages），AST/保护哈希/raw metadata/原review/diff通过。wiki_lint --fail-on error exit0，0errors/130warnings（107citation-key/20rawslots/3parser），N67-9实际parsedtrue。代码仅声明模型，无原experimentalgate/ρ/Cov/pvalue重构。

恢复[checkpoint013](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/checkpoint-013.md)，本批main / `Test DAY14 gated response beyond single-gamma calibration`，actualH3/hash只receipt。全Wikiquestions/pool/recentfingerprint/Day15精确卡已复核，Day15worksheet/convention有产物仍只partial。下一继续193Bi原order问题的jointenergy-time与独立responsecalibration设计，.6keV名义gap之外全σ/τ为chosen，不借其他parent时间、不赋新order。Research仍active，原15:00cutoff不改。


### Checkpoint014：actualclock ACK与时间模型验收

同run/session的checkpoint005在10:25实际收到并ACK（queued04:56不能当实际研究时刻）。本段91-check exit0，report/card/writeback valid（唯一34items/15changedpages），rawmetadata/protected/原source字节/AST和git diff --check通过。Freshlint实际exit0、0errors130warnings（107citekey、20rawslots、3parser）；local-score初h失败/稳定Richardson修正记录在run，未用旧74检查验收扩展。Nativeget_goal实测historicalblocked而任务有可执行工作，按用户同session续学推进research，不伪造goalactive。

当前原截止仍15:00，下一continuity已冻结free-cascade recoil的energy-opening-angle条件设计；不会将staticangular no-go推广到未建模能量响应，也不为193Bi定实际次序。Formal21/24不变，Day15仅partial无信用。第013批已Gitee发布，本批稳定subject `Bound DAY14 doublet timing with independent response calibration`；actualH3/hash只receipt。


### Checkpoint015：136Pr源表和依赖性验收

37项analysis实际exit0；report/card/writeback valid（40items/19changedpages）。旧source flags/原review、rawmetadata和PLAN/Bib保持，AST/diff通过。wiki_lint --fail-on error实际exit0、0errors130warnings（107citekeys、20rawslots、3parser）；LV25-16–25解析true，旧12–15合回同table后解析，不当新观测。前14批已发布，本批稳定main / `Audit DAY14 Pr136 links and one-sided transition evidence`；精确hash/actualH3仅runreceipt。

约11:30快照原截止仍15:00，继续1996companion检索和已freeze的193Bi free-recoil设计，不因本来源读完收束。Day14formal21/24不变，Day15仍仅partial无学分。


### 原截止观察时的收束状态（后被用户延期覆盖）

2026-10-15T15:37+08实际clock确认原15:00研究硬截止已过，之后只closeout，研究停止。最后科学读取记录11:47；该间隔不伪造运行/研究。Clock001/002/005/008已实际ACK，其它未observed不补。用户已将nativegoal恢复active，旧blocked快照保留为历史。

正式Day14逐边/判据矩阵、六维21/24自评、weeklyREFLECT和Day14cardaudit完整；Day15只有无学分预习，next_day_index只允许15。未完成136通用parser/更深量化和193Bi free-recoil exercise明确不计完成，不妨碍原正式卡验收；实际L4仍not-ready。无技术hardP0，科学未决和needs_review保留。最终可恢复提示已重写；本批稳定main / `Finalize DAY14 evidence and deadline closeout`，精确hash/actualchecks/H3仅runreceipt，课程state仅在本内容发布验收后单独对账。


### 原截止检查点的验收实测

2026-10-15T15:44:00.546184+08:00：report/card/writeback均valid；唯一block46items，覆盖20份本run修改knowledge页。原正式35、时间91、136Pr37项既有analysis的check全true；正式卡6项交付/六维21/24/weeklyREFLECT重新检查。新增评价对象hash和已读selectedline逐字一致，原LV19/LV25 claims/review、rawmetadata/PLAN/Bib与AST保持。

wiki_lint --fail-on error实际exit0，0errors/131warnings（107citationkey、21未填raw槽、3reactionparser）；git diff --check实际exit0。新N136-1–8/旧新LV25-1–26均被claimparser识别且保持true。详细机器证据见[content-final-audit](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/content-final-audit.json)。下一为显式manifest/H3发布及课程next15/count14单次对账；如发布失败保留本地commit和final-not-pushed，不改凭据。


### 用户明确延期：断网后继续同run/session

2026-10-15T15:46:53.981856+08:00用户允许加时至2026-10-16 16:00上海，原截止/15:37收束记录保留；本段新指令覆盖旧closeout-only和“未完成研究只待新任务”的限制。继续现有DAY14，不新建session、不重启daemon；formal21/24和completed14/partial15保持，officialnext14/count13等延期窗口最终对账。原第016批已显式暂存但未commit，核清29paths无其它index项后更新为延期checkpoint并发布，绝不提前计Day15。

下一继续已冻结的193Bi free-recoil energy-opening-angle设计及136Pr实际旧新263/405顺序的可识别性；固定两槽不无目的开新卡。旧metadata/provider失败和network空窗保留，不反复请求受阻入口或冒充持续计算。新截止与用户授权见[deadline-extension-001](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/deadline-extension-001.json)；当前run/day/session不变。


### Checkpoint017 延期研究验收

2026-10-15T15:59:38.789110+08:00：66项反冲设计checks全过，report/card/writeback valid（47items/20changedpages）；AST/原source字节/protected/rawmetadata/diff通过；wiki_lint --fail-on error实际exit0、0errors131warnings（107citekeys、21rawslots、3parser）。新截止余1440.4分钟，继续原两槽高信息路线。前16批已Gitee发布，本批稳定main / `Add DAY14 recoil energy-angle ordering limits`，actualH3/hash仅receipt；正式21/24与partial15无信用保持。


### Checkpoint018 延期研究验收

2026-10-15T16:13:04.021420+08:00，44项flow/parser checks全true/exit0；report/card/writeback valid（50items/20changedpages）；新LV25-27/N136-9已parse true，旧rows/review/raw/protected/AST/diff保持。wiki_lint --fail-on error实际exit0、0errors131warnings（107citekeys、21rawslots、3parser）。前17批Giteepublished，本批稳定main / `Bound DAY14 Pr136 flow and parent-tag identifiability`，actualH3/hash仅receipt。继续同136Pr实际identitycrosswalk，不以本段toy或表完成结束延期时窗。


### Checkpoint019 延期研究验收

2026-10-15T16:25:54.308021+08:00：44项candidategraphchecks全true/exit0，report/card/writeback valid（54items/20changedpages）；sourceLV25-28已parse true，旧rows/review/raw/protected/AST/diff保持。wiki_lint --fail-on error实际exit0、0errors131warnings（107citekeys、21rawslots、3parser）。前18批published，本批稳定main / `Audit DAY14 transition candidate graph identity limits`，actualH3/hash仅receipt。仍有延期窗口，下一沿newD3 oldlevel候选作逐line/π证据核验，不以算法单值或卡完成结束窗口。


### Checkpoint020 延期source验收

2026-10-15T16:37:01.209946+08:00：13项sourcechecks true/exit0，report/card/writeback valid（58items/20changedpages）；newLV25-29/30,N136-10 parsedtrue、oldrows/review/raw/protected/diff保持。wiki_lint --fail-on error实际exit0、0errors131warnings（107citekeys、21rawslots、3parser）。前19批published，本批main / `Clarify DAY14 D3 band novelty and parity evidence`，actualH3/hash仅receipt。仍继续延期窗口，下一sameparent strength/tablefigure核验已freeze，非新卡/absoluteB/L4。


### 延期窗口的最终交付边界

用户明确的明日16:00是本次运行最终交付截止；run.overnight_until保留2026-10-16T16:00+08，另以planned_research_cutoff_at=15:00预留最后一小时完成日报、检查、学分对账和发布。旧段曾计划16:00–17:00收束，已由本段和currentreceipt覆盖，不超出用户授权终点。当前研究继续，不提前credit或新session。


### Checkpoint021 延期研究验收

2026-10-15T17:10:25.297015+08:00：71项strengthcontrolchecks全true/exit0，report/card/writeback valid（62items/21changedpages）；oldrows/review/raw/protected/observableLF/AST/diff保持。初writeback因nucleus缺直接LKH链接失败已补齐回归；fresh wiki_lint --fail-on error实际exit0、0errors131warnings（107citekeys、21rawslots、3parser）。前20批published，本批main / `Recompute DAY14 Pr136 conditional strength ratios`，actualH3/hash仅receipt。继续延期窗口的TableII inputledger新问题，不新card或推进信用。


### Checkpoint022 延期研究验收

2026-10-15T17:48:24.884806+08:00：62项ledgerchecks全true/exit0，report/card/writeback valid（69items/24changedpages）；LV25-32 true、旧sourceclaims/review/raw/protected/AST/project旧bytes/questions旧行/diff保持。wiki_lint --fail-on error实际exit0、0errors131warnings（107citekeys、21rawslots、3parser）。前21批published，本批main / `Audit DAY14 configuration occupation completeness`，actualH3/hash仅receipt。继续已freeze的方法companion研究，genericmethod不补实际Pr136blockedinput。


### Checkpoint023 延期方法验收

2026-10-15T18:14:03.679377+08:00：50项源参数/Fock空间/算符/公式控制均true、exit0；report/card/writeback valid，唯一block74items/26changed knowledge页。原source未改、既有method/model/project旧行顺序和review保持，raw metadata/PLAN/Bib/AST与git diff --check exit0。初lint因新source缺固定Competing Interpretations and Limitations标题exit1，按已有内容补标题后fresh `wiki_lint --fail-on error` exit0：0errors/133warnings（108空citation key、22未填raw槽、3reaction parser）；13条新W17 claims全保留needs_review true。未宣称raw归档、官方勘误或程序错误。

前22批已Gitee发布；本批稳定指针 main / `Calibrate DAY14 TAC pairing and blocking input contract`，实际H3与精确hash只进回执。下一Ref31方法来源前回忆已保存，先核metadata/fulltext再读following/blocking定义；不借它补Pr136实际list。当前研究窗口仍active，正式21/24、Day14/partial15、official next14/count13保持。


### Checkpoint024 延期上游方法验收

2026-10-15T18:38:34.189782+08:00：最终43项canonical/BdG/overlap控制true、exit0；report/card/writeback valid，唯一block81items/27changed knowledge页，并完成2015→2017→2025方法谱系批次REFLECT。原method/model/project/W17旧行顺序与review保持，LV25及既有MU07 source字节未改，raw metadata/PLAN/Bib/AST及git diff --check exit0。初lint因矩阵双括号被解析成Wiki链接exit1，改为row记法；加入REFLECT后fresh `wiki_lint --fail-on error` exit0：0errors/135warnings（109空citation key、23未填raw槽、3reaction parser），12新ZT15 claims均parsed true。

前23批已Gitee发布；本批稳定 main / `Audit DAY14 quasiparticle following and method lineage`，实际H3/hash只回执。当前方法表达式路线局部完成，已重建池并冻结Pr136 γ/轴/替代形状场景的定向回忆，先核原文与既有知识再决定量化；不泛化重复overlap toy。研究仍active至2026-10-16 15:00、16:00交付，正式21/24、Day14/partial15和official next14/count13保持。


### Checkpoint025 延期γ/axis验收

2026-10-15T18:54:31.258823+08:00：最终50项actualTableII/精确低阶恒等式/转轴控制true、exit0；report/card/writeback valid，唯一block85items/28changed knowledge页。LV25-33 parsed true，原32条source claim及concept/nucleus/project旧行顺序和review保持，raw metadata/PLAN/Bib/AST及git diff --check exit0。首import缺SymPy exit1发生于计算前，已以标准库精确代数替代，无全局安装；fresh `wiki_lint --fail-on error` exit0，0errors/135warnings（109空citation key、23未填raw槽、3reaction parser）。

前24批Gitee已发布；本批稳定 main / `Separate DAY14 quadrupole shape from rotation-axis labels`，实际H3/hash只回执。下一回到source Ref48 Petrache2015 PhysScr90,114016的直接γ极化/轴论证，来源前回忆已保存，先核metadata/合法全文；只补当前问题，不计独立Pr136实验或新卡。当前研究仍active至2026-10-16 15:00、16:00最终交付，formal21/24、Day14/partial15和official next14/count13保持。


### Checkpoint026 延期直接伴随源验收

2026-10-15T19:11:11.983666+08:00：Petrache2015全文印刷3页、Fig1/Table1及寿命/筛选讨论核验，四行census算术一致；report/card/writeback valid，唯一block89items/29changed knowledge页。9新PT15 claims parsed true；原concept/LV25旧行和review保持，raw metadata/PLAN/Bib与git diff --check exit0。`wiki_lint --fail-on error`实际exit0，0errors/137warnings（110空citation key、24未填raw槽、3reaction parser）。下载器TDM→OA标签未采纳；本run两份方法PDF身份回执缩为已核书目信息，实际PDF/hash不改。

前25批Gitee已发布；本批稳定 main / `Trace DAY14 gamma-axis interpretation to selected Nd systematics`，实际H3/hash只回执。下一`pr136-j2-before-calculation.md`已freeze但未计算：absolute I/Ex offset与有序path/ΔI分开，明确adjacent/centered stencil和E2 interleaved signatures，不重算Nd51/23或预判Pr轴。研究仍active至2026-10-16 15:00、16:00最终交付，formal21/24、Day14/partial15及official next14/count13保持。


### Checkpoint027 延期有序能量验收

2026-10-15T19:45:04.357380+08:00：71项actual D4 path/closure/stencil/signature/offset/条件Σ/显示筛选检查全部true、exit0；report/card/writeback valid，唯一block93items/31changed knowledge页。LV25-34/35与PC22-19 parsed true，原observable/method/source旧行与review保持，raw metadata/PLAN/Bib/AST及git diff --check exit0。`wiki_lint --fail-on error`实际exit0，0errors/137warnings（110空citation key、24未填raw槽、3reaction parser）。所有stencil pair/位置、M空/I23tentative、非零closure、条件误差与删点mask均保留，没有Pr新γ/轴或Nd均值复现。

前26批Gitee已发布；本批稳定 main / `Reconstruct DAY14 inertia from ordered gamma paths`，actualH3/hash只回执。候选池转必要实际寿命/Qt来源：Matev2007 metadata核为additivity题，不能先当新实验；优先核已匹配题名的Laird2002 PRL88,152501公开fulltext，source-before recall已修正，正文尚未读。研究仍active至2026-10-16 15:00、16:00交付，formal21/24、Day14/partial15和official next14/count13不变。


### Checkpoint028 延期Qt方法与表审计验收

2026-10-15T20:51:09.850540+08:00：Matev2007 v1全文14页/Figs1–6/TablesI–III/关键公式完成，24项程序/条件控制断言通过、exit0；TableII实际2条中心值条件不相容保留，不把程序通过等同原表全有效。report/card/writeback valid，唯一block99items/33changed knowledge页，34行versioned矩阵有canonical副本。18新MT07与PT15-10 parsed true；原observable/method/project/PT旧行和review、raw metadata/PLAN/Bib/AST及git diff --check exit0。`wiki_lint --fail-on error`实际exit0，0errors/139warnings（111空citation key、25未填raw槽、3reaction parser）。无VOR/actualC/原实验重跑，原表/公式未改。

前27批Gitee已发布；本批稳定 main / `Audit DAY14 transition quadrupole operators and model tables`，actualH3/hash只回执。下一已从公开publisher取得并核刊头的Riley2001 ActaPhysPolB32 No9 p2683（13页），正文未读，source-before recall已保存；它是2001作者报告，未代2002最终稿或新增独立实验。研究仍active至2026-10-16 15:00、16:00交付，formal21/24、Day14/partial15及official next14/count13不变。

### Checkpoint029 延期原始Qt报告验收

2026-10-15T22:08:52.101495+08:00：Riley2001全文13页/3fig/2table、33行canonical typed账本和27项程序断言通过，实际exit0。report/card/writeback valid，唯一block104items/35changed knowledge页，15条RI01及MT07-19均parsed needs_review true。DSAM Purpose/type扩展和Qt旧“未核”描述更新属于明确意图，其余旧非空行与review保持；raw metadata/PLAN/Bib/AST和`git diff --check`实际exit0。初验证harness误用Page.claims报AttributeError，已改用仓库claim_rows解析器，未因此改科学内容；fresh `wiki_lint --fail-on error` exit0，0errors/141warnings（112空citation key、26未填raw槽、3reaction parser）。没有原始FITFTAU/τ/Σ重跑或Laird最终稿。

前28批已Gitee发布；本批稳定指针 main / `Audit DAY14 primary global lifetime analysis and Qt table roles`，actualH3/hash由receipt记录。下一131Ce原始实验reference的source-before recall已保存：先核已有Petrache1998对象/原件，校准矩定义、带身份和上游实验baseline；不先填7.4(3)或复算缺输入。当前研究至2026-10-16 15:00、16:00交付，formal21/24、completed14/partial15及official next14/count13不变。

### Checkpoint030 延期原始reference与通道验收

2026-10-15T22:24:20.573157+08:00：Petrache1998原5页/2fig/1table脚注与限制定向核完；16项hash/表角色/精确脚注/速度归一控制实际exit0。report/card/writeback valid，唯一block108items/36changed knowledge页。六新PE98与MT07-20 parsed true、原PE98-1–13与Matv旧claims/四页旧非空行（仅source updated日期变更）和review保持；raw metadata/原PDF哈希/PLAN/Bib/AST及`git diff --check`exit0。Fresh `wiki_lint --fail-on error`exit0，0errors/141warnings（112citekey/26raw槽/3parser）。无逐τ/Σ/χ²原始重拟合；Clark四页原全文未得，取件失败不伪造结果。

前29批Gitee已published；本批稳定 main / `Audit DAY14 original quadrupole reference and channel normalization`，actualH3/hash只receipt。实际clock再次检查距离研究cutoff仍逾16小时，重建候选池并逐字查看Day14/Day15卡（未显示Day16）：正式14全交付已具备，Day15计算单和误差/约定知识已覆盖但只partial。允许的下一有界preview是Ionescu1981原pureE2 feeding测试，source-before recall已freeze，正文/PDF未开，不重复同toy或计卡。研究2026-10-16 15:00止、16:00交付，run/goalactive、formal21/24/officialnext14/count13保持。
