---
type: learning-daily
graph-excluded: true
created: 2026-10-16
updated: 2026-10-16
---

# Day15：ADO、角分布系数与几何修正

## Run state

- run_id: 2026-10-16-day-15-01
- run_date: 2026-10-16
- day_index: 15
- phase: angular-correlation-polarization-and-mixing-ratio
- schedule_id: wiki-daily-learning
- timezone: Asia/Shanghai
- session_id: 01a14510-aec7-7e00-aa23-f7c77a5124bc
- resume_command: `codex resume 01a14510-aec7-7e00-aa23-f7c77a5124bc -C /workspace/wiki -s danger-full-access -a never`
- hard_deadline: 2026-10-17T15:00:00+08:00
- status: in-progress
- completed_day_indices: []
- partial_day_indices: [15]
- Day 15 card audit: in-progress

本次是独立session；课程基线next15/count14未推进。本页是持续学习检查点，不表示整个时段完成。15:00前仍有高价值当前问题时继续；最多预习恰好Day16并只记partial16，不开Day17。receipt见[run.json](20261016-DAY15-ado-angular-distribution-geometry-run-01/run.json)。

### 本session主动回忆

[冻结原答](20261016-DAY15-ado-angular-distribution-geometry-run-01/active-recall-frozen.md)于2026-10-16T22:17:56.981021+08:00、打开科学source/raw和Day14详细报告前保存。已暴露本prompt预习摘要、index和active handoff，明确为primed recall。SHA-256 `91eee8abb4bce71d0447617b1d5cb0d64240259115b9522a012963872cb25c67`；文件不回写。

原答正确指出A2/A4、核alpha、reference及几何不同层，且仅两角计数不足识别f；但对f的乘除方向不确定。来源后纠正为Zheng Eq3的`R=r f`，从符合比恢复本征r要除f。原件还明确组效率和self-exclusion所用的台数，不能以单台效率再除一次。没有把Day14的19/24、21/24或旧28-check当本日成绩。

## Candidate pool and selection

启动按顺序读README、index、profile/memory/active handoff、PLAN和三份课程/论文轨道计划；矩阵[Day15卡](../plans/2026-09-22-one-month-daily-task-matrix.md#day-15--ado角分布系数与几何修正)存在。最近学习记录和source fingerprints表明，Zheng定义、toy joint response、Gaussian/feeding与系数约定已有大量预习，需正式核原件并产生本session交付。[候选检查点](20261016-DAY15-ado-angular-distribution-geometry-run-01/research-checkpoint.json)记录选择与排除。

| 槽位/候选 | 问题与预期信息增益 | 本次处理 |
| --- | --- | --- |
| continuity | 两条独立额外输入路线如何识别f？共享背景/效率校准Cov怎样影响r误差？ | 完成新输入、解析传播、独立pair核算及MC；均为自设L2 |
| novelty | 独立GRIFFIN方法怎样验证event mixing与finite geometry，什么不能迁移到in-beam ADO？ | 已冻结primed回忆，读完28页arXiv1807.07570v1及相关图表；响应/Cov/版本边界已canonical |
| anchor内审计 | Zheng Fig1(a)与正文偶极门3.2%是否一致？ | 放大图/原文保留不一致边界；不补造精确图值 |
| 既有Zobel/Ionescu/193Bi等 | 避免重复旧练习；真实event/response/Σ缺口未补 | 必要时调取明确locator；不重算加分 |
| Day16 | 尚未开展；当前Day15路线仍有信息增益 | 不授学分，不越过下一卡 |

## Sources and evidence

### Zheng2002原件完整主线

[source页](../../knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md#day15正式复核原式方向与图文边界)保留原有review flags，新增Z02-10为`needs_review: true`。本次raw SHA-256与既有记录一致：`03044180a59fa5be55bcb6c517e9b87285c0991855afe5e1104e9dd03e9a7f23`；5页均无文本层，实际逐页视觉读完。

| 原件locator | 本次实际核读 | 证据层及限制 |
| --- | --- | --- |
| PDF1 / printed909 | 摘要、熔合蒸发取向、DCO/ADO动机及145Tb/Ref3入口 | 物理背景、作者方法动机 |
| PDF2 / printed910，Eq1–5 | 两矩阵x/y轴、target/gate、R分母效率比、R=r f、组效率与1/N | Z02-1/6直接定义；Eq2分离模型不代full joint（Z02-9） |
| PDF3 / printed911，Fig1/正文 | 12台、32/58/90°三组、Eu/Ba校准、组效率之和、energy scan及偏离定义 | 仪器事实与方法计算；缺原效率/ω2数值不能精确重放Fig1 |
| PDF4 / printed912，Fig2/总结/Refs | 已知跃迁局部约.75/1.25、作者优势解释、38/16组合数 | Fig2为局部实验验证；组合数不是独立样本或误差缩放率 |
| PDF5 / printed913 | 英文题名、作者与摘要 | 身份和主结论对照；不替代数据 |

**新边界（Z02-10）**：Fig1(a)可见点均在0和3.0刻度之间，最大仅略高于1.5；同页正文却给偶极门最大偏离约3.2%。仍按“正文报告”保存3.2%，不把它当图中可复算最大值或本计算单的误差；不由视觉读图发布替代精确数。四极门约5.2%的量级与Fig1(b)相容。这是原件内部一致性审计，不是新实验反证。

本session Crossref匹配Ref3 *In-beam study of 145Tb*, EPJ A12(3),253–255(2001)，DOI[10.1007/s100500170001](https://doi.org/10.1007/s100500170001)；只核metadata，未获其primary正文。方法文Fig2与其复用实验按依赖谱系，不计独立采集。[公开检索记录](20261016-DAY15-ado-angular-distribution-geometry-run-01/network-discovery-001.json)中的snippet只用于发现。

### 独立GRIFFIN来源与反证

[GRIFFIN source](../../knowledge/sources/smith-2019-griffin-angular-correlation-analysis.md)实际读取[arXiv1807.07570v1](https://arxiv.org/abs/1807.07570v1)的28页主文/附录/参考，关键公式与图2/3、表5/8/A.10已核，附录图/level-scheme以整页和联系表检查。原件SHA-256 `0390bdbb6b78f035d1d49abd4ecf863a684f3a8eb3ba6c537cfbd8fb6e352f33`；[采集manifest](../literature-acquisition/20261016-day15-smith-griffin.json)保存逐文件新raw gate和版本。来源前[primed回忆](20261016-DAY15-ado-angular-distribution-geometry-run-01/griffin-before-source-frozen.md)未回写。

Crossref/官方arXiv history核到2019NIM A922,47–63，DOI[10.1016/j.nima.2018.10.097](https://doi.org/10.1016/j.nima.2018.10.097)及仅v1历史；官方Elsevier全文入口一次ConnectionError，未获VoR。以下数字均限定v1，不将内部歧义归为已确认期刊错误。

| 原子入口 | 实际证据及作用 |
| --- | --- |
| SG19-3，PDF4–5 Eq6–14 | 匹配same-energy/time/pair响应的event-mixed比仍是W的角接受加权平均，不等于自动去卷积 |
| SG19-4，PDF6–7 Sec3.2 | mixed2–200μs、prompt<300ns，寿命/效率变化尺度条件及event-reuse Cov缺口 |
| SG19-5，PDF6 Fig2 | 同一60Ni数据与模拟的χ²/NDF：pair数7.96、再single效率2.34、event mixing1.02；非三次独立实验 |
| SG19-6，PDF7 Fig3 | 已知66Zn0→2→0纯E2在event mixing后仍有finite-response衰减，full模板对实验1.01 |
| SG19-7/8，PDF8–11 Eq15–27 | 正Z基函数线性组合允许负权，代数beta/gamma与核alpha/ADO f不同；Cov假设需明示 |
| SG19-9/10，PDF10 Table4、PDF14 Table8 | 部分cascade保留多Ji/δ；四种方法共享数据，Method1 a2/a4是δ派生 |
| SG19-12，PDF17 Summary | trigger/initial alignment/addback/分组改变须重验；不能把random-source校准自动移到in-beam |
| SG19-13/14/15 | v1 beta括号精度、Gd表/图及简化Q范围有局部不一致，保留版本边界，不补原Cov |

这是一项独立装置的方法反证，与Zheng/145Tb并非同采集；其四种分析不是四次独立采集。新可复用内容已写回[角关联方法](../../knowledge/methods/angular-correlation.md#事件混合效率归一之后仍有有限响应)。下一项当前问题是复用mixed partners的event-level Cov，不以增加pair条目数默认降低所有误差。

## Theory/analysis exercise

### 新ADO计算单

完整可复用输入、推导和边界在[ADO协方差方法页](../../knowledge/methods/ado-covariance-calibration.md#两路f校验与共享校准协方差)。[输入JSON](20261016-DAY15-ado-angular-distribution-geometry-run-01/ado-worksheet-input.json)身份为`DAY15-20261016-SYNTHETIC-ADO-COV-01`，SHA-256 `e8e31f0691862296b62adffb34e6e5395d22ba6cdc59f629a00c71a89eeadf04`；所有数为本run自设，未取得真实145Tb counts/逐台效率/Σ。

target x760keV、gate g420keV；32/58/90degree各4台，target组效率.044/.052/.040，gate组效率.036/.048/.032。gross峰8400/7200、共用sideband1500与固定kS=kL=.8，给净峰7200/6000；target效率比1.10。因此先由两角输入求`R=1.090909091`。

再额外给gate归一角分布`W=1+.28P2+.06P4`，在Zheng Eq4/5的分离响应内得`f_geo=.969076258`，所以`r_geo=R/f=1.125720584`。另给独立自设本征参考`r0=1.12±.024`，得`f_emp=R/r0=.974025974`。没有r0或gate响应时，等价(r,f)族说明不可识别；没有以同一R倒定义r后声称f=1。

### 误差传播和输入敏感性图

primitive P_S/P_L/B独立Poisson的chosen模型给净计数Cov `[[9360,960],[960,8160]]`。log-efficiency用共同归一、组几何和能量残差latent构造PSD Cov，并加gate A2/A4的相关及独立r0误差。所有矩阵与Jacobian保存在[完整计算结果](20261016-DAY15-ado-angular-distribution-geometry-run-01/ado-covariance-worksheet.json)。

| 输出 | chosen完整Cov sigma | 同边际误差全标量独立反事实sigma |
| --- | ---: | ---: |
| R | .025879569 | .030994534 |
| f_geo | .003211837 | .003216838 |
| r_geo | .026479979 | .032201143 |
| f_emp | .031137791 | .034662270 |

`f_emp−f_geo=.004949716±.030993214`已经包含两路f的cross covariance；自设输入内部闭合不等于真实response得到验证。共享events、背景fit、拟合k、参考/效率共用的数据在实际分析中都可能改变Σ，本例只验证一种明示模型。

![全部为自设输入的效率和Cov敏感性图](20261016-DAY15-ado-angular-distribution-geometry-run-01/ado-covariance-sensitivity.svg)

a展示效率比偏移对R与修正r中心值的影响；b展示固定各背景边际误差时，chosen背景相关改变r的传播标准不确定度，并与全标量独立反事实比较。图不包含实验点。200000次MC、seed20261016、零丢弃，标准差/线性sigma的四个比为1.000158/1.001354/1.000121/1.000279；验证chosen采样模型，未声称无偏性或实验CI。

### Convention注记

| 对象 | 本次固定的约定/边界 |
| --- | --- |
| target/gate | γ1=x为两矩阵y轴待测线；γ2=g为x轴开门线 |
| 分子/分母 | 小角S比大角L；效率比εtS/εtL在分母 |
| 修正方向 | 原Eq3为R=r f，所以r=R/f；f不是efficiency ratio本身 |
| 组/单台效率 | 输入ε是组内之和；每台为本例均匀组效率/4，不能重复归一 |
| self-exclusion | Eq2删除同一detector自符合，1/N是该分离近似的组项 |
| 共同scale | 同时乘所有效率的mode在本例严格抵消，独立化会破坏Cov中的抵消 |
| A2/A4 | 归一single-γ Legendre系数；不是核alpha或reference maximum |
| alpha/reference | [角分布系数页](../../knowledge/observables/angular-distribution-coefficient.md#拟合系数核取向与最大辐射系数的层级)保留Aexp=alpha Amax、参考spin/δ/布居及c=0限制 |
| sigma | 本计算单sigma是standard uncertainty；未拟合磁子态Gaussian宽度σ或σ/J |
| 角度/单位 | JSON用degree，数值函数转radian；比和效率无量纲，能量keV |
| 数据身份 | 全部自设；原Fig1 deviation不是计数/背景/效率/总sigma |
| joint response | single-γ校准、gate marginal与full γγ pair kernel分别保存，Z02-9限制跨cascade迁移 |

## Counter-evidence and missing companion observables

同一自设几何只把gate系数换为A2=−.30、A4=0，f从.969076变为1.016554；在相同本征r0=1.12下预计R从1.085365变为1.138540。这说明阈值需要门条件；数值不是实测换门效应。真实换门还可能改变feeding和条件density，因此要用同一target/gate身份的逐pair观测区别几何与布居效应。

20°均匀半锥只对gate single-γ角矩作平均时f=.970646822；未指定target W或joint response，不能称完整有限几何修正。[角关联方法](../../knowledge/methods/angular-correlation.md#条件γγ响应各向同性marginal仍可有角关联)已保留相同single marginals而joint不同的反例；本run不重复旧toy加检查数。

最有区分力的下一观测是同cuts的已知cascade逐detector-pair净峰/背景及换门后修正r的联合闭合，而非多测一条不明多极性的ADO。若问题是E/M性质，还需同一跃迁的线偏振或独立ICC。缺真实events、response、alignment/feeding和Σ时保持experimental L4 not-ready。

## Knowledge Impact and Learning Decision

- `supports`：原件核实R=r f及组效率/self-exclusion；两条额外输入路线可以分别检验。
- `limits`：计数比本身不识别f；独立假设、point组式和single-γ校准都不能替代真实joint输入。
- `revises`：新增Fig1(a)/正文3.2%一致性边界；百分数继续按正文引述，不能冒充精确图中重算或总误差。
- `no material change`：没有新核素Jpi、δ、B值或集体模式赋值；不改原有human-review范围。

## Durable knowledge delta

已实际新增[ADO两路校验与共享校准Cov](../../knowledge/methods/ado-covariance-calibration.md)，保存完整chosen输入、等价族、解析Jacobian、共享sideband矩阵、效率latent模型、数值、换门/finite-cone边界与复算入口；来源原子入口为Z02-6/9。Zheng source新增Z02-10并保持旧flags；[角分布方法页](../../knowledge/methods/angular-distribution.md#误差传播与可识别性)和index已给反向入口。可复用内容的唯一副本不在outputs。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/methods/ado-covariance-calibration.md",
      "summary": "新增独立本征参考/gate几何两路f、共享背景和效率latent Cov、解析传播及chosen数值和反证输入。",
      "anchor": "两路f校验与共享校准协方差",
      "sources": [
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
      "knowledge": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
      "summary": "本session逐页复核5页原件，保留原式方向/组效率，并新增Fig1(a)与正文偶极门3.2%的图文一致性边界。",
      "anchor": "Day15正式复核：原式方向与图文边界",
      "sources": [
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/angular-distribution.md",
      "summary": "新增正式Day15自设计算与相关传播的canonical入口，区分旧预习数字和本次图文边界。",
      "anchor": "Day15正式运行另建",
      "sources": [
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-6"
        },
        {
          "path": "knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md",
          "locator": "Z02-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/smith-2019-griffin-angular-correlation-analysis.md",
      "summary": "完整读2018v1主线/附录，保存独立装置效率/finite-response验证、多spin与版本/Cov边界，2019VoR未得。",
      "anchor": "事件混合只先消去匹配的效率权重",
      "sources": [
        {
          "path": "knowledge/sources/smith-2019-griffin-angular-correlation-analysis.md",
          "locator": "SG19-3"
        },
        {
          "path": "knowledge/sources/smith-2019-griffin-angular-correlation-analysis.md",
          "locator": "SG19-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/angular-correlation.md",
      "summary": "新增GRIFFIN同数据归一校验、finite-response卷积与event reuse/initial alignment迁移边界。",
      "anchor": "事件混合：效率归一之后仍有有限响应",
      "sources": [
        {
          "path": "knowledge/sources/smith-2019-griffin-angular-correlation-analysis.md",
          "locator": "SG19-3"
        },
        {
          "path": "knowledge/sources/smith-2019-griffin-angular-correlation-analysis.md",
          "locator": "SG19-5"
        },
        {
          "path": "knowledge/sources/smith-2019-griffin-angular-correlation-analysis.md",
          "locator": "SG19-12"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "为正式Day15新ADO协方差方法及独立GRIFFIN source建立可检索入口。",
      "anchor": "GRIFFIN的event-mixing/finite-response实验校验",
      "sources": [
        {
          "path": "knowledge/sources/smith-2019-griffin-angular-correlation-analysis.md",
          "locator": "SG19-5"
        }
      ]
    }
  ]
}
```

## Open questions and belief revision

1. 原Fig1(a)和正文3.2%的差异能否由作者计算表/更清楚版本解释？没有这类输入时保留Z02-10，不自行裁决。
2. 实际阵列的target/gate两能量校准是否共享同一geometry/normalization mode，sideband和参考比的cross covariance是什么？只有两角error不能恢复它们。
3. GRIFFIN提供同数据效率处理及已知pure-E2 finite-response反证（SG19-3/5/6）；复用同一interaction的多个mixed partners时，分母及prompt/mixed cross Cov怎样随partner数变化？本文未给实际event ledger/Σ，下一步做明示条件推导。

## L0–L4 state

L0完成Zheng主线；L1把source/方法/observable连通；L2完成有输入/hash/Cov/失败控制的本session计算；L3以joint-response可迁移性、GRIFFIN独立方法对照和真实companion设计继续。全部合成计算保持L2身份，未包装为新experimental L4。真实数据研究缺events、可重放sorter、逐pair响应及实际Σ，readiness为not-ready；这不阻止继续有价值的方法阅读。

## Verification and continuation

首次写入前boundary exit0、0errors/0warnings；EOL cleanup exit0且0restored；preflight exit0、protected Bib matched。[入口基线](20261016-DAY15-ado-angular-distribution-geometry-run-01/baseline-before-write.json)记录368行继承状态和607份knowledge哈希，index原为空。

计算脚本实际exit0；PSD、解析/数值梯度、独立ordered-pair、共同scale抵消、不可识别族和200000次MC均通过。图的panel alignment、glyph（minimum7pt）和collision（0fail/0warn）通过；source validator最终exit0、0fail，保留4项warning：仅交付PNG预览而非TIFF投稿栅格、300非600dpi、通用demo警告和MC/uncertainty模式误报。前两项符合本日报SVG/PDF+预览合同；后两项由显著自设标识及直接画sigma解释，不虚报实验。首次source audit的export/DPI失败及修正保留于[figure QA](20261016-DAY15-ado-angular-distribution-geometry-run-01/figure-qa.json)。

首轮仓库lint实际exit1（本次新method缺5个固定英文schema标题，且inline数组被当wikilink），已修复并重跑exit0、0error/145warning（3reaction parser、114citation key、28既有raw slots）；全局diff exit0。新增GRIFFIN source后fresh lint实际exit0、0error/146warning（3reaction parser、115citation key、28既有raw slots）；boundary/diff/preflight exit0。EOL exit1按治理规则分类为4份本次substantive知识改动、0unsafe/mixed，均保留。实际runner report/writeback/partial curriculum校验通过，[检查回执](20261016-DAY15-ado-angular-distribution-geometry-run-01/prepublication-checks-002.json)和[同session续接](20261016-DAY15-ado-angular-distribution-geometry-run-01/continuation.md)已保存。检查点稳定指针：main / `Establish DAY15 ADO covariance and independent response evidence`，H3/push结果只写run receipt。原15:00研究截止不变，继续mixed-event Cov，不在此结束或授卡。

### Day 15 card completion audit

| 本卡交付 | 本session证据与artifact | 状态 |
| --- | --- | --- |
| 主动回忆 | [冻结原答](20261016-DAY15-ado-angular-distribution-geometry-run-01/active-recall-frozen.md)与[freeze receipt](20261016-DAY15-ado-angular-distribution-geometry-run-01/active-recall-freeze-receipt.json)：本session时间/hash，primed身份 | complete |
| 主线阅读 | [Zheng source](../../knowledge/sources/zheng-2002-ado-coincidence-angular-anisotropy.md) Z02-6/9/10：PDF2 Eq1–5、PDF3 Fig1、PDF4 Fig2；5页raw hash匹配，方法/系数页已核 | complete |
| ADO计算单 | [输入/hash](20261016-DAY15-ado-angular-distribution-geometry-run-01/ado-worksheet-input.json)、[计算及完整矩阵](20261016-DAY15-ado-angular-distribution-geometry-run-01/ado-covariance-worksheet.json)，Z02-6：R/两路f及无额外输入的rank1退化 | complete |
| 不确定度与图 | [敏感性SVG](20261016-DAY15-ado-angular-distribution-geometry-run-01/ado-covariance-sensitivity.svg)、[figure QA](20261016-DAY15-ado-angular-distribution-geometry-run-01/figure-qa.json)，解析/MC与chosen Cov见计算JSON；原Fig1不作实验sigma | complete |
| convention注记 | 本日报逐项表，source Z02-6/9/10及canonical方法页 | complete |
| 反证与必要观测 | [换门/有限几何控制](../../knowledge/methods/ado-covariance-calibration.md#换门与有限几何的失败控制)；[SG19-6](../../knowledge/sources/smith-2019-griffin-angular-correlation-analysis.md#key-results) PDF7 Fig3的已知pure-E2反证及逐pair/E-M companion | complete |
| 知识/检查/续接/receipt/发布 | 六项真实knowledge-writeback已写；仓库检查与显式发布尚待本run后续 | in-progress |

只有所有行complete、要求的检查/续接/receipt/发布实际完成后才可计Day15；Day14的partial15不会自动转学分。
