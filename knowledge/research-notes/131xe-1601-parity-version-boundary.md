---
type: research-note
title: "131Xe 1601-keV态的宇称版本与独立性边界"
aliases: [131Xe 794-keV parity version boundary]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [banik-2020-131xe-multiple-band-structures, chakraborty-2023-131xe-wobbling-origin]
created_from: "Day28 parity-provenance worker and parent primary-figure check"
promotion_target: "131xe-low-spin-partner-crosswalk"
tags: [131xe, parity, source-lineage, polarization, spectroscopy]
---

# 131Xe 1601-keV态的宇称版本与独立性边界

## Research Trigger

[[131xe-low-spin-partner-crosswalk]]发现1600.9-keV态在2020和2023论文中配不同宇称。需要判断该差异是否只是单行排印、是否来自新的宇称敏感观测，以及哪些历史材料能提供反证。当前只固定证据版本，不裁决该态最终宇称。

## Grounded Evidence

| Evidence | source / locator | provenance | limitation |
|---|---|---|---|
| 2020的794.8-keV行：1600.9(2)-keV 17/2+→15/2−，列E1、RDCO=0.55(1)、偏振+0.03(1) | [[banik-2020-131xe-multiple-band-structures]] BNK20-D28-2 | printed044306-6 Table I | 作者指认，不能因后文标签不同便静默更改 |
| 795-keV E1还见于Fig.4图注、Table I脚注k和B3讨论 | 同source BNK20-D28-3 | printed044306-4/-6/-8 | 多处重复不等于多个独立测量，也不保证指认正确 |
| 2023同能量/观测值行配17/2−→15/2−；Table I无单独多极性列 | [[chakraborty-2023-131xe-wobbling-origin]] C23-D28-2、C23-D28-8 | printed064318-3 Table I | 已知线的部分观测量采用2020，不能叫新的M1实测 |
| 新766.5线为quadrupole指认，偏振栏空；766门中见671、无795 | 同source C23-D28-8 | Table I、Fig.3及Sec.III | 支持级联放置；单靠quadrupole不能区分E2/M2并重新确定宇称 |

## Provisional Reasoning

### 版本差异不能简化成单行笔误

2020在图注、表注和门分析中重复使用795-keV E1，削弱“只有Table I一个正负号偶然打错”这个假设。它仍可能是共同沿用的错误指认、不同污染/双峰处理、参考标签变化或其它尚未核实的原因。没有作者修订说明或共同响应重分析前，不从重复次数选择正宇称。

2023的新符合放置与宇称敏感测量须分开。766.5-keV线的DCO可支持quadrupole；偏振栏为空，不能自行补成已测E2，再以此闭合1601-keV态宇称。794.8-keV旧观测量沿用也不构成独立复测。

### 外部核验线索与正式证据的区别

parity worker实际取得DAE2018短文、官方ENSDF档案及Kaya2018全文，已有逐URL回执、文件签名与哈希。这些材料尚在`tmp/`，没有在本轮改动受保护raw或建立缺raw的source stub。其原始数值与图表目前是待正式摄入的线索，不能凭本页晋升为已入库primary测量。

可复用的追查账本如下；来源身份、覆盖和依赖应随正式摄入保留：

| 线索 | 原件/评估locator | 本轮允许的使用层次 | 不能推出 |
|---|---|---|---|
| Banik2018两页DAE短文，Proc.DAE63,82–83，INSPIRE1732789 | printed83 Fig.2的794点及下方17/2+文字 | 2018 E1/正宇称解释的待摄入前身；具体1600.9-keV绑定仍以2020完整表为桥 | 短文未印该精确能级值；不能编造其表行 |
| 2006 A=131评估，DOI10.1016/j.nds.2006.10.001，官方2018/2020/2026档案 | 2026 `ensdf.131` L6806–6809 adopted；L7220–7223反应数据集；来源规则L7085–7091 | 负宇称/M1,E2历史评估路线及早期实验追查入口 | 新archive日期不等于新评估；dataset-global规则不等于逐行primary来源闭合 |
| Kaya2018，DOI10.1103/PhysRevC.98.014309 | printed014309-6 Table I的AGATA794/Weak行；Sec.III跨pp.5–6 | 独立采集再观测约794-keV线的待摄入证据；量子标签使用与重测分开 | 该线没有展示新的宇称敏感拟合；不能借其它级联角关联给它独立宇称权重 |

Kaya的Fig.2不含1600-keV节点/794支路，应以Table I该行定位。其Ref31的Kerek1971只是候选上游；未取得该原件，也没有逐行引用，暂不能说794行的17/2−最初确定来自该文。ENSDF历史转换系数和角分布数值必须保留“评估转录、原件未核”身份；本页不以其数值裁决E1或M1/E2。

### 官方NNDC adopted PDF的评估支持

NNDC公开的`131Xe Adopted Levels, Gammas` PDF（官方评估副本，July 2006）在printed p.3列出`1600.6 17/2−`和`794.6 2 100 805.93 15/2− M1,E2`；同页注释说明`#`类Jπ来自`γ(θ)`、`α(K)exp`和衰变模式，另说明总转换系数由BrIcc Frozen-Orbitals按能量、多极性和混合比计算。这个来源加强“负宇称/M1,E2已经进入评估谱系”的事实层，但仍是评估文件，不能替代1979/1983原始实验表，也不能消除2020期刊版本的正宇称/E1冲突。官方PDF定位：[NNDC adopted PDF](https://www.nndc.bnl.gov/ensnds/131/Xe/adopted.pdf)，printed p.3及p.4注释。

NNDC官方selected-dataset reference page确认`1979IR01`为Irving、Forsyth、Hall和Martin，J. Phys. G 5, 1595 (1979)，DOI `10.1088/0305-4616/5/11/015`；来源描述包含`126,128Te(α,nγ)`、16 MeV、γ能量/强度、γ(θ)、线偏振，并称对`129,131Xe`给出levels、J、π、δ、B(E2)、B(M1)和branching ratios。该页面闭合了来源身份和实验覆盖层，但没有提供794.6-keV逐行原始表，不能把reference metadata当primary数值。定位：[NNDC reference page](https://www.nndc.bnl.gov/ensdf/getrefs.jsp?dsid=126TE%28A%2CNG%29&recid=129054022)，`1979IR01`段落。

### ENSDF转换记录的语义边界

parity-conversion worker对官方归档副本的逐行检查显示，`794.6(2)`行被记录为`M1,E2`，并带有`A2=-0.71(2)`、`A4=-0.09(4)`和`EKC=0.0017(7)`。[[tuli-2001-ensdf-format-manual]]原件printed36（PDF42）把`EKC`定义为实测K壳转换系数，`KC`才是理论系数；但当前Xe记录只有`tmp/day28-workers/parity/`归档副本，没有正式`raw/`原件和原始实验表。因此这里只保存“评估文件中的实验量记录”及其来源链，不把它写成本任务亲验的早期primary测量。

该数据集的全局说明把E、RI、M、Jπ和转换/角分布判据分配到1983Lo08、1979Ir01、1971Ke13等来源链；没有行级脚注，不能把同一`EKC`拆成多篇独立证据。`M1,E2`为非唯一候选标签，MR/DMR为空，不能从它生成已测δ。原先缺少的理论系数边界已由官方BrIcc查询补齐，但能量误差和实验—理论协方差仍未闭合。[[kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc]] KB08-2给出混合式α=(α1+δ²α2)/(1+δ²)，KB08-3/5规定误差与原子空位处理；缺这些输入时不能用历史EKC挑选一个方便的δ、再排除整族候选。完整字段和行号回执见[转换语义审计](../../outputs/learning-daily/20261030-DAY28-independent-l3-research-week-four-exam-run-01/workers/parity-conversion/findings.zh.md)；本页保持needs_review。

### 官方BrIcc名义系数与ICC边界

2026-10-30通过官方ANU BrIcc接口取得`Z=54,Eγ=794.6 keV`的`BrIccS v2.3 (9-Dec-2011)`名义值。FO/NH在本能量打印精度内相同：

| 模型 | 多极性 | αK | αTot |
|---|---|---:|---:|
| FO | E1 | 0.000932(13) | 0.001074(15) |
| FO | M1 | 0.00316(5) | 0.00365(6) |
| FO | E2 | 0.00234(4) | 0.00273(4) |
| FO | M2 | 0.00835(12) | 0.00973(14) |
| NH | E1 | 0.000935(13) | 0.001077(15) |
| NH | M1 | 0.00316(5) | 0.00365(6) |
| NH | E2 | 0.00234(4) | 0.00273(4) |
| NH | M2 | 0.00833(12) | 0.00972(14) |

固定能量、纯M1/E2混合时，名义αK凸包为`[0.00234,0.00316]`。ENSDF的`EKC=0.0017(7)`与该凸包不能直接转成统计排除：原始实验误差口径、电子/γ归一、能量误差传播和理论共同协方差均未闭合；官方表单也拒绝了`eerror=0.2`的数值误差输入。因此这些数值是理论候选集合，不是本任务的宇称裁决。可复核清单见[BrIcc研究札记](../../outputs/learning-daily/20261030-DAY28-independent-l3-research-week-four-exam-run-01/workers/bricc795/findings.zh.md)和[机器结果](../../outputs/learning-daily/20261030-DAY28-independent-l3-research-week-four-exam-run-01/workers/bricc795/bricc795-derived.json)。

### 区间几何练习：不是统计检验

仅为显示输入几何，暂把打印的`0.0017(7)`当作闭区间`[0.0010,0.0024]`，并把BrIcc打印括号只作为端点标签。则纯M1/E2名义凸包`[0.00234,0.00316]`与该实验带的交集只有`[0.00234,0.00240]`；纯E1打印区间约`[0.000919,0.000945]`，与该假定实验带不相交；M2也明显高于该带。这个结果只说明“在一种临时区间解释下，M1/E2候选集合的可见重叠很窄，E1/M2与其不重叠”，不提供置信度或排除σ。`EKC`的原始实验误差含义、能量误差、电子/γ效率、FO/NH共同理论误差和行级primary归一均未闭合，所以本练习不能裁决宇称，也不能把M1/E2标签升级为已测混合。

## Assumptions

用能量、端点、观测量和来源版本共同匹配节点；不以近能量单独认证身份。DCO多极阶数与electric/magnetic性质分开。不同论文、档案快照、同采集再分析只按实际独立观测的量去重。

## Competing Explanations

待检验项包括共同沿用的量子标签、未说明的修订、同能区污染/双线及响应差异。本页没有原始计数、峰形或作者更正，故不在这些解释间给概率排序。

## Transfer Conditions

对其它核素版本冲突同样应区分：独立观测到一条γ线、独立测得该线多极性、独立重定母态宇称。三者不能用论文或实验名称互相替代。

## Failure Conditions

把全局ENSDF来源规则套到每一行、把旧评估当新实验、把参考级联的测量能力移作目标线的结果、或把无偏振的quadrupole直接叫实测E2，都会越过证据边界。未正式摄入的暂存原件也不能成为永久事实唯一落点。

## Falsification or Reverse Tests

限定命题“正宇称仅出现在2020表格一行”已由BNK20-D28-3反驳。进一步物理判别需目标794.8线本身的独立电/磁性信息、共同门与双峰控制；或者对834.6-keV节点及766.5线建立可靠宇称/多极链。尚无输入支持新的似然、排除率或beamtime。

## Open Questions

为何同一观测值配不同宇称？是否有明确erratum或重指认说明？历史794.6-keV转换记录的逐行实验出处、壳层定义与误差如何闭合？1983原件仍未取得；2018同题/相邻实验不能补成该目标AD的已核原件。

## 2026-10-31 Source-Recovery Recheck

Using the configured CORE API, exact DOI search for `10.1088/0305-4616/5/11/015`
and title/author queries for the 1979 `131Xe` work returned no matching repository
full text or source record. The returned near matches were unrelated papers. This is a
repository no-op, not evidence that the primary article is unavailable through
institutional subscription or interlibrary loan; the 794-keV AD/ICC boundary remains
unchanged.

## Human Review

- Review scope: Codex对worker证据账本整合及2020 Fig.4原图抽查。
- Decision: provisional；未发生human review。
- Complete unresolved P0/P1 inventory: 科学P1为原始宇称敏感测量、外部原件正式来源身份与2023修订说明；没有将其转为用户必须立即处理的待办。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-10-30 | 固化版本与独立性边界 | worker output | provisional research-note | 两入库原件支持版本冲突与多处E1标签；外部资料保留待摄入层 | [[131xe-low-spin-partner-crosswalk]] |

获取与核验回执：[parity findings](../../outputs/learning-daily/20261030-DAY28-independent-l3-research-week-four-exam-run-01/workers/parity/findings.zh.md)、[source manifest](../../outputs/learning-daily/20261030-DAY28-independent-l3-research-week-four-exam-run-01/workers/parity/source-manifest.json)、[1983获取边界](../../outputs/learning-daily/20261030-DAY28-independent-l3-research-week-four-exam-run-01/workers/1983-ad/result.json)。科学版本边界的长期副本在本页；临时下载不当作永久原件归档。
