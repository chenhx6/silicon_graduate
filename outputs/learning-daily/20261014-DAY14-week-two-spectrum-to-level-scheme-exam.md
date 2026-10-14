---
type: learning-report
graph-excluded: true
created: 2026-10-14
updated: 2026-10-14
---

# DAY14 第二次周考：从谱到能级纲图

## Run state

- run_id: `2026-10-14-day-14-02`
- run_date: `2026-10-14`；timezone: `Asia/Shanghai`
- day_index: 14；phase: `gamma-spectroscopy-and-level-schemes`
- schedule_id: `wiki-daily-learning`；run_kind: `substantive / weekly-learning`
- session_id: `01a13a0e-e8bd-7251-b970-f6975679e281`
- resume_command: `codex resume 01a13a0e-e8bd-7251-b970-f6975679e281 -C /workspace/wiki -s danger-full-access -a never`
- overnight_until: `2026-10-15T15:00:00+08:00`；15:00–16:00仅收束。
- research_status: active；本报告是内容checkpoint，不是整段时窗完成。
- completed_day_indices: [14]
- partial_day_indices: []
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
| 新颖性槽位与Day+1 | 尚未开新问题；正式周考先完成，随后刷新clock与候选池 | 最多预习下一张Day15，固定day_index14、不计其卡、不打开Day16 |

最近学习覆盖：Day8选律/δ约定，Day9寿命/branch→strength，Day10双带电磁指纹与谱系，Day11–12反应布居/符合背景，Day13 Doppler/速度/停止/统计，均以既有日报与canonical知识页定位。当前不把这些日报用作新的实验来源，也不从数量推学习饱和。另一个非重叠novelty问题未强行选择。

### Active recall 与 priming

来源前答案完整保存在[冻结回忆](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/active-recall-before-sources.md)。已读运行prompt/handoff中的昨日预习摘要，所以明确为primed recall；未凭记忆填Herzáň具体能量、R/A或误差。原答正确指出共同门、相对能量自由度、阵列特定DCO、P/A/Q分离和parent lifetime，但尚未写出三个cycle的相关性或本文未定双线表注，这些由正式读图/表后补足。

## Sources and evidence

| 来源 / 身份 | 本轮实际覆盖与locator | 证据分层与独立性 |
| --- | --- | --- |
| Herzáň et al., PRC92,044310(2015), DOI[10.1103/PhysRevC.92.044310](https://doi.org/10.1103/PhysRevC.92.044310)；citation key `Herz__2015`；raw SHA256 `f727485ad0f52269a66b27272dac75d34d9e67aaf8b073631cfeac5fe81d3aea`，20页 | pp.1–2动机/setup/tagging；pp.3–7全部Table I；pp.8–9 Figure2；pp.10–15各带/isomer/SD；pp.16–20组态、systematics、结论、引用。视觉核p.3/7/8/10/15 | 一次JYFL193Bi acquisition；Table I/Figure2/Figure5是dependent图表/投影；153-ns bandhead引用Ref7，非本次七线parent的新τ |
| 外部结构化Crossref核验 | [metadata回执](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/crossref-herzan-metadata.json)，作者/题名/2015/卷92/DOI一致 | 元数据核验，不是独立实验；返回pages为空，文章号由PDF核验 |
| Canonical source与方法 | [[herzan-2015-193bi-spectroscopy]] HE15-4–14；[[level-scheme-reconstruction]]新增逐边、cycle、topology、companion sections | 实验测量、联合赋值、作者解释、模型和任务推导分开；旧needs_review全保留 |

主要定位：HE15-8是Table I p.3/p.7及Figure2 p.8；HE15-9是p.7 footnote f；HE15-10是p.7 a定义及p.10 Figures3/4；HE15-11是p.13条件性29/2+赋值与p.14 conversion；HE15-12是p.10 Ref7寿命与p.3相对强度；HE15-13是p.19 conversion/SD解释。源页保存每条claim的locator，不用搜索片段当证据。

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

## Counter-evidence and missing companion observables

HE15-9的实际未定双线是核心反例：energy sum、共享R/A和假设的ΔI=2均不足以裁决order。若一条线出现可独立定位的旁路或延迟顺序，应重审中间level；source仍保留括号Jπ与(E2)。HE15-5的quadruplet限制“一个峰是一条γ”的简化；干净622.4直接分支门与323.4级联门的299-keVcomponent差异可能迫使拆峰，但必须控制622/626门纯度、feeding、response和random。

必要companion分类：confirmed SD link与endpoint为expected-but-not-established；46/87-keV低能γ为not observed、原因仍是作者解释；缺事件/Σ的重拟合为blocked-needs-event-level data。αtot=261/12.82与87.4-keV x ray会降低γ灵敏度，不能把未见峰直接写成路径不存在。Table I/Figure2/Figure5和多角度数据共享采集，互补不等于独立复测。

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

## Durable knowledge delta

本run实际修改三份knowledge Markdown，超出昨日预习的增量为七边逐条证据、相关cycle/标定nullspace、未定doublet shared-quantity边界和parent-lifetime契约。canonical知识路径：

- [Herzáň source](../../knowledge/sources/herzan-2015-193bi-spectroscopy.md)：HE15-8–14及正式来源主线/triage。
- [level-scheme method](../../knowledge/methods/level-scheme-reconstruction.md)：五能级七边、GLS/反例和必要companion。
- [A≈130 thesis matrix](../../knowledge/projects/a130-thesis-evidence-matrix.md)：方法对照行，不冒充A≈130新实验。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
      "summary": "核验七边中的表尾行、未定双线与共享角度/偏振、实际标定、条件性isomer赋值及parent寿命来源；原flags保留。",
      "anchor": "Day14 正式逐边复核与来源边界",
      "sources": [
        {"path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md", "locator": "HE15-8"},
        {"path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md", "locator": "HE15-9"},
        {"path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md", "locator": "HE15-10"},
        {"path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md", "locator": "HE15-11"},
        {"path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md", "locator": "HE15-12"},
        {"path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md", "locator": "HE15-13"},
        {"path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md", "locator": "HE15-14"}
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "summary": "固化五level七边逐条E/C/M/J审计、三个相关cycle与带假设35-check重算；不替换作者能级。",
      "anchor": "Day14 五能级七跃迁逐边审计",
      "sources": [
        {"path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md", "locator": "HE15-4"},
        {"path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md", "locator": "HE15-8"},
        {"path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md", "locator": "HE15-9"}
      ]
    },
    {
      "knowledge": "knowledge/methods/level-scheme-reconstruction.md",
      "summary": "保留actual a(E)/Q(E)、bandhead与parent寿命、conditional intensity和SD低能companion的区别；weekly认识修正同步canonical页。",
      "anchor": "标定、寿命与伴随观测的逐项契约",
      "sources": [
        {"path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md", "locator": "HE15-10"},
        {"path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md", "locator": "HE15-11"},
        {"path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md", "locator": "HE15-12"},
        {"path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md", "locator": "HE15-13"}
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-thesis-evidence-matrix.md",
      "summary": "增加spectrum-to-level correlated-closure方法对照行和active说明；193Bi不当作A≈130模式独立证据。",
      "anchor": "Day14 spectrum-to-level identity and correlated closure",
      "sources": [
        {"path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md", "locator": "HE15-8"},
        {"path": "knowledge/sources/herzan-2015-193bi-spectroscopy.md", "locator": "HE15-9"}
      ]
    }
  ]
}
```

## Open questions and belief revision

1. 哪个旁路、time/tag或独立spin anchor能裁决393/394的顺序？重复同一能量和不能裁决。
2. 真实response/净计数能否分别识别299.2/299.8、622/626和323 quadruplet？现有绘图不能补出逐门Σ。
3. 哪些parent τ/branch/ICC/δ输入足以把七条线的相对量接到absolute strengths？153-ns引用不能挪用。
4. 1836-keV候选link的endpoint、强度与false-link控制能否闭合X？当前保持未confirmed。

这些是Codex后续研究路线，不自动转成用户待办。认识修订发生在方法充分性上，未改变结构模式排序。

## L0–L4 state

- L0：anchor原文20页主线、Figure2/Table I及表注、校准与isomer/SD边界已正式复核。
- L1/L2：source/method/matrix互链、35项有条件表格/反例练习、六维周考和认识修正已固化。
- L3：line identity/ordering的有界判别问题active；当前最高信息路线是conditional gate与branch/time设计，不把counterfactual当实验。
- L4：真实event-level重分析not-ready；缺事件、response、joint covariance、执行sorter/门接受度及相关parent τ/δ。其缺失不终止其它有价值学习路线。

## Verification and continuation

首次写科学内容前boundary exit0、无error/warning；H1 preflight exit0，protected Bib基线匹配；EOL清理exit0、未触碰substantive/staged内容。raw PDF哈希与source一致，原raw/PLAN/Bib保持只读。定量脚本实际exit0，35/35。

本checkpoint实际验收：report/card/writeback均valid；wiki_lint --fail-on error exit0，0 errors/128 warnings（107既有citation key、18既有未填raw槽、3reaction parser）；git diff --check exit0；protected PLAN/Bib哈希与raw全树size/mtime均匹配基线。第一次lint exit1因inline矩阵被识别成wikilink，已改为无歧义的行列记法并回归。Gitee实际结果仅run receipt；本段内容通过验收后按显式manifest发布。恢复提示已保存[continuation-prompt](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/continuation-prompt.md)。本报告不是研究收束声明；研究截止保持原receipt，不因卡片或一个来源完成提前结束。

当前快照 2026-10-14T19:35:55.416781+08:00，距原截止1164.1分钟；下一日prompt已准备入口、未创建新session/未计Day15。QMD/overview本次deferred，未扩大维护范围。下一步：刷新clock/候选池，完成同一问题的conditional gate、composite-response与最小branch/time设计；若当前问题局部饱和，再查恰好下一张Day15作无学分预习。任何正式Day15学分留待其独立日run，Day16不打开。
