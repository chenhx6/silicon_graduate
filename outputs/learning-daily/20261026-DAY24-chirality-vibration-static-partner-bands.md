---
type: daily-learning
graph-excluded: true
created: 2026-10-26
updated: 2026-10-26
---

# Day24：手征伙伴带与133Ce附属分析（进行中）

## Run state

- run_id: 2026-10-26-day-24-01
- run_date: 2026-10-26
- day_index: 24
- session_id: 01a177ac-521f-7212-9312-ba967400db98
- resume_command: `codex resume 01a177ac-521f-7212-9312-ba967400db98 -C /workspace/wiki -s danger-full-access -a never`
- completed_day_indices: []
- partial_day_indices: [24]
- status: research-continues / checkpoint001
- hard_deadline: 2026-10-27T15:00:00+08:00
- checkpoint_at: 2026-10-26T18:23:56.106936+08:00
- minutes_to_deadline: 1236.1
- next_day_index: 24（不变），累计formal completed=23。

本run身份/截止来自实际`20261026-DAY24-chirality-vibration-static-partner-bands-run-01/run.json`，不是准备prompt的run-24。原receipt尚未写入session字段时，本checkpoint以当前执行环境session ID记录，不代改runner receipt；runner随后自行对账。未创建新session/run/deadline，不修改课程状态。

先核Day23的四份实际receipt：`run.json` completed [23]/partial[24]；`card-credit-23.json` formal[23]、累计23/next24且no-double-credit；`final-session-receipt-23.json` completed；`task-publication-receipt-23.json` published、postcommit reconciliation passed。其SHA/路径列在本run 本地忽略的`session-receipt-001.json`，未根据准备文猜测。原15:00字段保留，显式override的effective deadline17:00只属于Day23；Day21/22信用、人审及撤回不动。

### Day 24 card checkpoint audit

|课程交付|本checkpoint实际覆盖|仍需继续/信用|
|---|---|---|
|三根角动量、左右手、振动/静态区别|`recall-001.md`（Wiki primed、非盲测）；FM97全部主线和关键visual|继续原模型有效域，不先授分|
|三条指定阅读入口|nuclear-chirality及FM97期刊17页/MU07四页本轮回读|主线已读，图未全数字化，非producer复现|
|energy、B(M1)/B(E2)、geometry、g逐伙伴图|[[135nd-chiral-partner-resolved-evidence-map]]，原τ/B按partner分列，g unknown|branch/normalizer/共同Cov仍缺，不能补数|
|crossing/configuration/γ-softness/mixing反证|map四路线及所需holdout；FM97负证据边界|未拟合替代模型，不裁胜负|
|实验/TAC-RPA/推断分层交付|同map完整矩阵＋harmonic近似阶次练习|这是checkpoint而非card-credit receipt|

## Candidate pool and selection

|候选|输入/信息增益|本轮决定|
|---|---|---|
|主槽：135Nd原件与谐振/临界模型合同|FM97/MU07原件可读；已有预习缺一张清晰的正式owner map|优先完成；从预习实际缺口接续，不机械重做库存脚本|
|重要附属：133Ce共同采集/角响应|两论文描述可核，actual mask未交付；可解析finitegate条件|主卡高价值工作后执行一项有边界推导|
|133Ce582 out/out分母|现有ledger不能确认，817.7仅能差|deferred；不逆造线、不反复计算同一缺口|
|GAMPN/ASYMO/PROBMO实际输入|版本/header/λ零点/signedEM仍缺|deferred；不运行114隔离producer，不凭ħω重造input|
|Day25下一卡|当前问题仍有高价值原模型路线|本checkpoint未打开；足时只准恰好Day25无学分预习，不开Day26|

## Sources and evidence

- [[frauendorf-meng-1997-tilted-rotation-chirality]]：期刊17页全文文本主线；fresh visual PDF2/3/5–10/12–16，覆盖Figs1–9及主要公式。raw SHA `9dc81b3147a786189dd0c2f31d79a56e9bb5d83e16fd0c8137bccaf2a43d81e2`。新增FM97-D24-001/002。原human-reviewed claims保持，本轮新增仍needs_review:true。
- [[mukhopadhyay-2007-135nd-chiral-vibration-static]]：原四页全文，fresh visual PDF2/3/4的TableI/Figs1–4/Eqs1–3与非谐讨论。SHA `9eccc9c2ad02cc10735d1aad0d76eb2fd8af0a4acc814bcaab8099f50e748425`。MU07-D24-001/002分开实验相近与谐振共同TAC曲线。
- Crossref两个DOI端点均HTTP200，题名/期刊/年份身份核到，记录在`external-metadata-001.json`。它们是元数据交叉核验，不是新实验或全文独立票。
- [[wakudyanaye-2022-triaxiality-rotational-bands-133ce]] PDF54–61方法连续段及PDF59/61fresh visual；[[ding-2021-131ba-133ce-signature-splitting]]稿本PDF2定向回读、两raw哈希核到。WK22-35为finitegate数学边界；Ding既有正式版对照本轮不冒称重读全文。
- MU07同一实验的TableI/图/作者TeX和IAEA adopted不重复计票。2003纲图与2007DSAM有各自采集贡献，但共享assignment/branch的具体ledger仍缺。

## Theory/analysis exercise

主卡：map写出F(q)=a+bq+cq²、v=ℏ/(2𝓜Ω)的谐振本征期望：F00=a+cv，F11=a+3cv，F10=b√v。线性截断给共同对角基线，二阶曲率可破等；Ω→0须检查小振幅失效。它说明近似阶次，未把内禀对角量当跨spin实验B或给actual135Nd临界参数。

附属：[[133ce-thesis-analysis-blueprint]]“有限all-detector门的接受度练习”推导真实联合响应积分与方位平均条件核。equalweight point-ring的G2/G4：8布局−1/8、−1/64；13布局−11/52、31/416，均非4π消去。`system/scripts/day24_finite_gate_acceptance.py`两路线/极限等32控制通过，输出`finite-gate-acceptance-001.json`。chosen positive kernel两ratio仅是synthetic示例，不是AD/DCO/Rac实测或原producer预测。

## Counter-evidence and missing companion observables

FM97 Fig7抑制属于本模型；其134Pr高spin未见links同时有弱布居限制。MU07认可135Nd实验正支持，也承认带间E2低估、M1趋势差异、近transition TAC+RPA breakdown与非谐B差异；RPA含shape自由度不等实核γ刚性认证。

Map逐项给crossing、configuration change、γ-softness和bandmixing需哪些额外预报/holdout。尚缺两partner g、完整signed EM与projector、逐线parent/Jf/component/normalizer/Cov。133Ce尚缺actual run/mask/45°event/sorting/同门参考counts，Eq4.6“all”不能自动代替完整响应积分。不能把这些科学partial当用户待办或技术hard P0。

## Knowledge Impact and Learning Decision

`supports`135Nd已有实验手征支持，`limits`共同理论曲线和临界点的过强解释；`limits`finiteallgate的普适精确独立性外推。没有撤销其它核的真实支持链。Pr747 P+.04/δ−.47、813 P−.03/δ−.37、SH26 fixedσ/I=.2条件支持、Au band2原wobbling/band3原SP，以及Li2004/Singh2016等寿命边界沿用Day23校准，未作新数据认证。

## Durable knowledge delta

新增canonical owner：`knowledge/projects/135nd-chiral-partner-resolved-evidence-map.md`，保存逐伙伴原打印表、层级矩阵、近似阶次和四条反证设计，回链FM97-D24-001/002、MU07-D24-001/002。`knowledge/projects/133ce-thesis-analysis-blueprint.md`保存finitegate推导、exact moments、假设及下一输入，回链WK22-35。来源原读覆盖和概念反链也作本轮实质更新；outputs不是唯一知识副本。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/projects/135nd-chiral-partner-resolved-evidence-map.md",
      "anchor": "近似阶次练习：等强来自什么",
      "summary": "新增逐伙伴实验/模型/推断与四替代解释矩阵、harmonic阶次推导。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-meng-1997-tilted-rotation-chirality.md",
          "locator": "FM97-D24-001"
        },
        {
          "path": "knowledge/sources/frauendorf-meng-1997-tilted-rotation-chirality.md",
          "locator": "FM97-D24-002"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D24-001"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D24-002"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/frauendorf-meng-1997-tilted-rotation-chirality.md",
      "anchor": "Day24原件主线回读：模型范围与未见跃迁的条件",
      "summary": "新增原件主线/关键visual覆盖和模型迁移条件。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-meng-1997-tilted-rotation-chirality.md",
          "locator": "FM97-D24-001"
        },
        {
          "path": "knowledge/sources/frauendorf-meng-1997-tilted-rotation-chirality.md",
          "locator": "FM97-D24-002"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
      "anchor": "Day24原件主线回读：谐振等强、配对输入与临界区",
      "summary": "拆开共同TAC曲线、RPA不改期望值、配对与非谐有效域。",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D24-001"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D24-002"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/nuclear-chirality.md",
      "anchor": "Day24正式研究入口：伙伴分辨与模型有效域",
      "summary": "加入正式研究map导航和模型有效域边界。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-meng-1997-tilted-rotation-chirality.md",
          "locator": "FM97-D24-001"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D24-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/133ce-thesis-analysis-blueprint.md",
      "anchor": "有限all-detector门的接受度练习",
      "summary": "新增有限门联合响应积分与两布局接受度moments的条件推导/32控制。",
      "sources": [
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-35"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
      "anchor": "WK22-35",
      "summary": "补原Eq4.6经验校准与finiteacceptance非4π的任务边界。",
      "sources": [
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-35"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "Day24正式研究入口：135Nd逐伙伴实验",
      "summary": "增加新canonical项目的最小索引入口，模型/实验层级保持。",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2007-135nd-chiral-vibration-static.md",
          "locator": "MU07-D24-001"
        },
        {
          "path": "knowledge/sources/frauendorf-meng-1997-tilted-rotation-chirality.md",
          "locator": "FM97-D24-001"
        }
      ]
    }
  ]
}
```

## Open questions and belief revision

1. 已有Almehed2011后续方法如何定义/区分orientation与shape模、在近临界何处舍弃harmonic，能否提供本例所需的normalizer/branch ledger？下一步优先原件方法核对，不重复已饱和端点。
2. crossing/configuration等替代路线在固定算符和未定标观测下能否给不同预测？尚未拟合，不把列举等价于解释成功。
3. 133Ce actualmask/45°事件和sort输入若不可得，下一附属问题转现有原件可解析的模型输入合同或节点mapping；不继续撞缺失mask。

## L0–L4 state

L0主来源回读、L1/L2证据分层和有界推导、L3逐伙伴图/反证设计进行中。有限接受度脚本是声明条件的数学组件，不是实核L4 response重分析。无独立用户数据、无实际fit/Cov/likelihood重放；不新增human-reviewed，不清needs_review。

## Verification and continuation

入口boundary/preflight均exit0；EOL清理0且无实质tracked继承dirty，继承未跟踪Day20/22/23文件已在`entry-audit-001.json`记录、全部保护。首次lint exit1：新project缺4个schema标题及index入口（5项）；已补齐，再运行最终检查，首次失败不隐去。最终lint exit0（errors0/warnings228/info4680）、boundary exit0、git diff --check exit0；原runner report/writeback/curriculum三门均valid。接受度脚本exit0/32控制通过。precommit EOL exit1只因6个本轮实质修改保留，unsafe/mixed0。228项warnings为继承citation/review等治理欠项，未掩盖或清除；详见`required-checks-001.json`。

续接：`outputs/learning-daily/20261026-DAY24-chirality-vibration-static-partner-bands-run-01/next-continuation-001.md`。保留本session与原15:00截止；checkpoint不提前结束整段学习。当前问题仍有方法/反证高价值路线，不宣称schedule-level saturation；不授[24]、不开Day25正式卡。最终credit/final receipt/下一日准备只在对应原runner门执行。

Git稳定指针：main · Day24: map chiral partners and bound finite gate acceptance。本checkpoint采用显式manifest，实际hash/H3/远端结果只写`task-publication-receipt-001.json`；保护raw/PLAN/Bib和继承dirty。overview update deferred：这是首个增量checkpoint，最终formal closeout再按实际lint汇总；QMD刷新deferred，directread/rg可用。
