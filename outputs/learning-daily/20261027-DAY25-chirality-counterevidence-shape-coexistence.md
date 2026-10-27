---
type: daily-learning
graph-excluded: true
created: 2026-10-27
updated: 2026-10-27
---

# Day25：手征反例、形状竞争与133Ce实际分析蓝本

## Run state

- run_id: 2026-10-27-day-25-01
- session_id: 01a17cdd-58b4-7a53-b782-5248260f526a
- day_index: 25
- schedule_id: wiki-daily-learning
- status: running
- completed_day_indices: []
- partial_day_indices: [25, 26]
- curriculum_cards_completed: 0
- next_day_index: 25
- hard_deadline: 2026-10-28T15:00:00+08:00
- closeout_window: 2026-10-28 15:00–16:00 Asia/Shanghai

本报告为持续研究checkpoint005，不授分、不提前收束。原run.json仍status:running、counted:false，其此前写入的completed[25]与本报告旧“已授分”不构成正式信用；课程state实际累计24/next25，Day25尚无card-credit/final-session回执。保留原runner字段，不擅改历史身份/截止；正式信用待截止后原runner门。

Day24本次直接核run.json、card-credit-24.json、final-session-receipt-24.json与task-publication-receipt-24.json：completed、formal[24]、preview[25]；发布回执为published。未新增Day24信用，Day21/22/23既有人审/撤回不改。

### Day 25 card readiness audit

|课程matrix交付|当前可审查证据|状态|
|---|---|---|
|近简并非充分、共存与手征区分|[[chirality-shape-coexistence-companion-matrix]] 理论判据；PE06 printed112502-1–4；[[triaxial-shape-coexistence]] Day25段|ready-for-final-audit|
|三源主线阅读|PE06原四页回读/TableI视觉；LV19既有主线ledger+本次PDF2/5定向核；HW11原读ledger及概念校准|ready-for-final-audit|
|134Pr/135Nd/136Nd三行对照|竞争矩阵Evidence Available，实验/作者/替代分列且保family|ready-for-final-audit|
|companion最小组合与缺一项降级|竞争矩阵“最小companion组合是问题设计，不是普适终判”|ready-for-final-audit|
|持久化竞争解释矩阵|knowledge/projects/chirality-shape-coexistence-companion-matrix.md及本报告唯一写回块|ready-for-final-audit|

## Candidate pool and selection

回忆在读源前提出：能谱相近不足以测几何；同一个B比可以隐藏绝对尺度；自由非对角元与数据相容不等于证明手征。读源后的修正是：近简并也不是动态手征的普遍必要条件，未见线必须有实际灵敏度才构成反证。

|候选|信息增益/实际输入|选择|
|---|---|---|
|134Pr off-diagonal E2与TableI身份|四页原件及真实实验/计算两列齐备，可反向核验旧扫描|连续主问题|
|133Ce程序/双分母实际合同|已有原表、1997原方法与错误倒算的直接反例|不重叠附属问题|
|GAMPN实际job重放|版本/header/BCS/blocking/signed核缺失|记录缺口，不反复撞端点|
|Day26既有八极/MR preview|仅复核已存在稿中的普适硬门/归因，未增加课程范围|partial[26]、无学分|

用户另要求巡查五个子会话，作为本run执行可靠性的有界支持任务处理；未替代核结构主线。

## Sources and evidence

|来源|本checkpoint实际读区与证据角色|限制|
|---|---|---|
|[[petrache-2006-near-degenerate-chiral-misinterpretation]]|父代理回读四页主线，PDF3 fresh视觉TableI/Eqs3–5；独立代理交叉核|非新实验；Ref11/Ref9不同不证明统计独立|
|[[lv-2019-chirality-135nd-reexamined]]|复用既有全文ledger；本次独立代理定向PDF2/5、VoR024314-8/Figs5–6|正pair本篇未给成对absoluteEM，不作全领域无寿命断言|
|[[petrache-2018-chiral-bands-even-even-136nd]]|独立代理定向Fig3/TableI/Fig6及MU08 TableII谱系|D5比值与D3模型几何不拼成同pair完整实测|
|[[heyde-wood-2011-shape-coexistence-review]]|复用既有原读HW11-D25P-001/002/006，核本轮概念量词|E0不唯一测形状/混合，不强制所有核有E0+Coulex|
|[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]]|父代理PDF67/78文字视觉、112文字；独立代理49/50/54/59/61/69/71/77/98/99|关键页再核，不新称130页全文重读|
|[[emediato-1997-133ce-rdds-lifetimes]]|父代理PDF2/2106 fresh视觉参数；独立代理方法/表II–III|负λ50.6为旧job直接反例，不恢复WK22 actual输入|
|AW13、Li04、Singh16、Joss98|独立代理按节点与时钟迁移定向回原件|不同clock/组态/spin/实验不能直接合并|
|BU16/BU17、Garg15|只核已存在Day26 preview所用原段|来源/模型层分开，不给Day26信用|

实际文件签名、页数、SHA及本次覆盖记录在本run source-fingerprint-005.json；缺文件会明确记录，不用搜索摘要补正文。公开来源入口/DOI沿各source。Paul1991本次另定向核PDF2/3/4/6及公式/引用，纠正元数据、branching字典和分母；不重新声称14页通读。

Tonev2006/2007复用同实验，实测E2不对称、TQPTR/IBFFM结果和作者动态解释分层；模型失败不等于所有静态手征或刚性共存已被无模型排除。新claims均needs_review:true，不增加human-reviewed。

## Theory/analysis exercise

### 134Pr：先区分实验与计算，再做前向核

PE06 TableI的17ny/17y/18ny实验为.3(1)/.6(1)/.22(9)，18y为<.08；.33/.70/.17/.062属于Q比2的计算列。旧χ²/95%表因目标列错误且无likelihood/producer而撤回，不能用Δχ²=4直接比较总χ²。

固定原α、正b、共同实对称forward核Q/q1的两行分别为(1,x)与(x,y)；M=Rf Q Riᵀ。17→15跨连续带身份交换，Table out/in须取raw跨/内比倒数；18→16不倒。

|x|y|R17ny|R17y|R18ny|R18y|
|---|---|---|---|---|---|
|0|.50|.333870|.703522|.170382|.062384|
|.04|.73|.315145|.647261|.187283|.067046|
|.08|1|.303851|.600031|.201070|.073618|

这证明条件前向敏感性；没有八行联合fit、Cov、上限likelihood或新CI。α复用原提取，q12对称为额外ansatz；q1=q2不等于完整形状相同或chiral波函数。UC为ultimate cranking约1.25，TRS另约1.7。

### 133Ce：双分母、协方差与能量原点

一致光子yield、同母、非零分子时，out/out与out/in相除可消去混合线、δ与τ，得到(Yin/Yout)(Eout/Ein)^5。能量相关效率/gate接受度不自动消去。

465的原表中心给10.62663，Table6.11打印商11.77778/11.78723；仅ρ=0时一阶σ=1.37205，ρ=−1/+1时为1.93848/.08564。实际Cov未得，不报真实CI，不由重叠证明底层计数同源。

582假设817.7分母的反演.882/1.157/1.192均只是summary条件目标。Table5.2弱线不构成该局部门谱upper limit，分母仍未闭合，禁止逆造线。

Table6.2中|18–20〉实值5.8046/5.8239/5.8985；6.423是50.6−5.5ħω倒算，不能证明原点。Emediato负νh11/2实际用λ50.6、Δ.92、ħω8.41及N4/5空间，直接反驳旧跨壳禁令；不能转填WK22。标准BCS共同移位ε/λ不改u/v，须核actual单位与header。

四点S的条件协方差另补第三邻ρ=−.05，仅lag≥4为零；实际Cov(E)不由独立等方差控制恢复。

实际producer：本run forward-checks-005.py/json；独立矩阵乘法复核最大差1.11×10⁻¹⁶。代码只是条件算术，不调用114隔离producer。

### Paul1991：分母与单位复核

原Eq6是.697 E2^5/(E1^3 λpure)，λpure为纯M1分量branching比。用整条混合光子线Λ时需(1+δ²)；旧source漏E1²及E2份额已纠正。原Fig2低spin约1/高spin约5倍是ΔI1 E2分母，不能转作Fig3 ΔI2分母。Table1反应元数据与N.Xu作者亦按原页修正，具体PA91-D25-A005-01–04。

## Counter-evidence and missing companion observables

|核/family|直接观测|作者/模型解释|替代与缺口|
|---|---|---|---|
|134Pr旧Band1/2|谱/对齐/E2分支、Tonev绝对E2不同|PE06简化解混合；Tonev涨落/动态手征|配置交叉/混合、offdiag E2须检；不证形状唯一|
|135Nd正D3/D4、负D5/D6|正pair一个D3比值；负pair双方τ和绝对B(E2)、B(M1)|CDFT/PRM、TAC/RPA各有限域|正pair不借负pair强支持；本篇缺匹配absoluteEM|
|136Nd五pair|D5双方relative比；旧MU08的D4/D3主带EM|D3显式3DTAC；不同配置交叉/混合|弱C伙伴缺自己的比；旧主带互比不替新伙伴，也不否定正D5|

最小组合按具体问题选取：身份/响应→匹配absoluteEM尺度→固定空间/参数的可失败预报→有分离预报的独立结构holdout。缺身份则暂缓对应matched比较；缺clock且无其它绝对约束则只得relativeEM；缺BR/ICC/response则复算仍条件化；缺独立holdout则保留等效解释。g/Qs只是可选互补量，完整组合也不保证唯一模式。

## Knowledge Impact and Learning Decision

- supports：134Pr对近简并充分性的原反例；135Nd负pair绝对EM强支持；136Nd D5有限relative支持。
- revises：旧Table计算列当实验、无依据CI、壳offset恢复、假检出限、3qp相对Ex下限与Au相位错误归因。
- limits：PES/RMS几何、相同B比或弱线缺失的解释范围；动态/共存/配置解释均须具体预报。
- Day26 preview只纠正既有MR普适下降/AMR严格禁戒、SCCM宏微观归因；没有新卡信用。

## Durable knowledge delta

长期结果已写入竞争矩阵、概念页、133Ce蓝本及三研究笔记；来源原子claim保留输入/模型/条件推导。输出脚本和巡检回执只供复现，不作为第二知识库。下列唯一块兼顾本run此前增量与当前修订；旧结论保留Git/入口快照，正文已替换为当前可支持版本。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/projects/chirality-shape-coexistence-companion-matrix.md",
      "anchor": "## 理论判据：近简并为什么不是手征充分条件及手征与形状共存的鉴别",
      "summary": "三核逐family比较；纠正普适必要/充分硬门、计算列误作实验及无依据CI。",
      "sources": [
        {
          "path": "knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md",
          "locator": "PE06-D25-A005-01"
        },
        {
          "path": "knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md",
          "locator": "PE06-D25-A005-03"
        },
        {
          "path": "knowledge/sources/lv-2019-chirality-135nd-reexamined.md",
          "locator": "LV19-D25-002"
        },
        {
          "path": "knowledge/sources/petrache-2018-chiral-bands-even-even-136nd.md",
          "locator": "PE18-D25-001"
        },
        {
          "path": "knowledge/sources/petrache-2018-chiral-bands-even-even-136nd.md",
          "locator": "PE18-D25-003"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/triaxial-shape-coexistence.md",
      "anchor": "## Day 25 正式核验：三轴形状共存与核手征性的鉴别边界",
      "summary": "区分结构/模型层次，E0和EM/holdout设计不作为所有核的强制终判。",
      "sources": [
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-D25P-001"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-D25P-002"
        },
        {
          "path": "knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md",
          "locator": "PE06-D25-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/133ce-thesis-analysis-blueprint.md",
      "anchor": "## Day 25 持续深入学习：131Ce/133Ce 拓扑节点对照、带头零点翻转与 582 keV 出带分母未闭合之严格约束",
      "summary": "逐节点/双分母/相关误差；撤回壳offset、检出限、3qp伪下限；实际输入缺口保持。",
      "sources": [
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-D25-A005-01"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-D25-A005-02"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-D25-A005-03"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-D25-A005-04"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-D25-A005-05"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-D25-A005-06"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D25-A005-01"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-thesis-evidence-matrix.md",
      "anchor": "## Evidence matrix",
      "summary": "两条Day25证据行保留观测/模型/实际输入缺口，长期蓝本未结项。",
      "sources": [
        {
          "path": "knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md",
          "locator": "PE06-D25-A005-01"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-D25-A005-03"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/134pr-two-band-mixing-offdiagonal-e2-sensitivity.md",
      "anchor": "## Research Trigger",
      "summary": "原八行TableI分列，补17→15倒数；可执行前向例替代旧统计认证。",
      "sources": [
        {
          "path": "knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md",
          "locator": "PE06-D25-A005-01"
        },
        {
          "path": "knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md",
          "locator": "PE06-D25-A005-02"
        },
        {
          "path": "knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md",
          "locator": "PE06-D25-A005-03"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/133ce-afrodite-rad-finite-geometry-and-qtr-code-contract.md",
      "anchor": "## Research Trigger",
      "summary": "程序角色与actual输入分开；BCS共同零点不变性及负宇称50.6的原文反例。",
      "sources": [
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-30"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-31"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-35"
        },
        {
          "path": "knowledge/sources/emediato-1997-133ce-rdds-lifetimes.md",
          "locator": "EM97-D25-A005-01"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/131ce-133ce-topological-nodes-configuration-substitution-contract.md",
      "anchor": "## Research Trigger",
      "summary": "节点闭合、全links替代和相位规范；不以3Δ作相对Ex下限。",
      "sources": [
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-33"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-46"
        },
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-D25-A005-04"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/paul-1991-n75-electromagnetic-properties-triaxiality.md",
      "anchor": "## Bibliographic Record",
      "summary": "补齐source结构并据原公式纠正能量幂/混合份额、分母身份、反应和作者元数据；本checkpoint为定向读区。",
      "sources": [
        {
          "path": "knowledge/sources/paul-1991-n75-electromagnetic-properties-triaxiality.md",
          "locator": "PA91-D25-A005-01"
        },
        {
          "path": "knowledge/sources/paul-1991-n75-electromagnetic-properties-triaxiality.md",
          "locator": "PA91-D25-A005-02"
        },
        {
          "path": "knowledge/sources/paul-1991-n75-electromagnetic-properties-triaxiality.md",
          "locator": "PA91-D25-A005-03"
        },
        {
          "path": "knowledge/sources/paul-1991-n75-electromagnetic-properties-triaxiality.md",
          "locator": "PA91-D25-A005-04"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/bucher-2017-146ba-direct-octupole.md",
      "anchor": "## Day25内Day26无学分preview：相消机制的实际分解",
      "summary": "纠正已存在preview中的宏微观归因，保留原SCCM中子/质子贡献边界。",
      "sources": [
        {
          "path": "knowledge/sources/bucher-2017-146ba-direct-octupole.md",
          "locator": "BU17-D25P-A005-01"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/garg-2015-135pr-magnetic-rotation.md",
      "anchor": "## Day25内Day26无学分preview：比值趋势与模型条件",
      "summary": "Garg原比值上升反例；候选MR与寿命方法不设普适硬门，原review保持。",
      "sources": [
        {
          "path": "knowledge/sources/garg-2015-135pr-magnetic-rotation.md",
          "locator": "GA15-D25P-A005-01"
        },
        {
          "path": "knowledge/sources/garg-2015-135pr-magnetic-rotation.md",
          "locator": "GA15-D25P-A005-02"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "### 133Ce深入学习与两篇学位论文补充",
      "summary": "增加本run来源/受控研究笔记的导航，不把推理页当source证据。",
      "sources": [
        {
          "path": "knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md",
          "locator": "WK22-D25-A005-01"
        }
      ]
    },
    {
      "knowledge": "knowledge/overview.md",
      "anchor": "## Current Snapshot: 2026-10-27 Day25 checkpoint005",
      "summary": "同步实际lint/目录统计；科学纠错例来自PE06，计数本身仅由lint给出。",
      "sources": [
        {
          "path": "knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md",
          "locator": "PE06-D25-A005-01"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/a130-chirality-counterexamples-and-shape-coexistence-systematics.md",
      "anchor": "## Research Trigger",
      "summary": "A≈130手征反例与三轴形状共存系统学：近简并破缺、电磁跃迁伴随量判据与四核多维比对。",
      "sources": [
        {
          "path": "knowledge/sources/petrache-2006-near-degenerate-chiral-misinterpretation.md",
          "locator": "PE06-D25-A005-01"
        },
        {
          "path": "knowledge/sources/grodner-2006-128cs-chiral-doublet-lifetimes.md",
          "locator": "GR06-D18-4"
        }
      ]
    }
  ]
}
```

## Open questions and belief revision

1. 134Pr实际联合likelihood、上限置信定义、α/V/能隙Cov与signed E2核未得；下一步不能把自由q12拟合相容当手征证成。
2. WK22 actual GAMPN/ASYMO/PROBMO header/input、ε4冲突、单位/零点/负λ、BCS/blocking、signedEM仍缺。
3. 817.7同母gate背景/效率/局部upper limit和582分母身份未闭合；不靠其它弱线填值。
4. 832keV的3qp可行性unknown；新空间须给能量/Jπ/全部links预报。两个19/2+原表行保存，.5keV闭合差不抹平。
5. 已核131/133Ce时钟不能跨态/核/组态移植，单Qt不测γ软度。

信念修订：更多术语、漂亮算式或lint通过不增加科学证据。实际原表列身份、母末态和响应合同决定可做的推断；没有输入时保持unknown，并继续有可解析输入的问题。

## L0–L4 state

L0：原件身份/页数/哈希核验；L1：节点/带/谱系分开；L2：条件前向振幅和误差传播；L3：三核竞争矩阵、可失败设计；L4：actual事件/response/Cov/producer缺失，未宣称重分析或复现。自审中的科学未决为P1/明确隔离的解释边界，不冒充技术验证失败或用户待办；人工review标志保持。

## Verification and continuation

本checkpoint正式检查结果写required-checks-005.json，未执行前不写通过。科学核验与结构检查分开；runner写回验证须用真实原baseline和当前checkpoint入口两套快照，不用未传baseline的valid冒称run-change检查。

用户所列五子会话的巡检见subagent-supervision-005.json：一个capacity失败、四个已完成；失败线程已用原生协作续接并完成有界只读核对。Farmer误把子id归到父session_id的问题已用失败回归复现并修正；v2禁止直接app-server子输入，故改为父线程接通知后原生协作恢复。父未运行时不唤醒历史子失败，dry-run零恢复动作；10项AgentOps测试通过。新监督器live PID442391，保持原root session/model，不新建daily run或改deadline。

next-continuation-005.md保留可恢复研究问题。仅本次15:00截止后启动正式收束/信用审计与Day26准备；现在继续Day25，Day26无学分，Day27不打开。Git发布只显式本run文件，raw/PLAN/Bib、旧dirty及114保持。用户回复只给必要结果，完整执行证据留回执。
