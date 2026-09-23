---
type: system-workflow
graph-excluded: true
operation: autonomous-research
updated: 2026-08-06
---

# Autonomous Research：L0-L4 科研自治

本文件是 Wiki 科研自治等级、升级条件、问题状态、每周自测和用户数据关口的唯一 canonical owner。其它治理文件只做路由。Docker 的运行权限不表示科学自治等级；L0–L4 仍按本文件和用户授权推进。

## 能力等级

| 等级 | 定位 | 默认产物 |
|---|---|---|
| L0 | 精读指定来源，核验元数据、locator 与原始证据，准确摄入 | source 与必要基础页 |
| L1 | 建立证据关联、适用边界和初步竞争解释 | 反链、关系与轻量知识固化 |
| L2 | 在授权摄入/综合中自动运行 L1，质疑、低成本验证并记录高价值问题 | 知识页与 `knowledge/questions.md` |
| L3 | 调查研究领域，梳理已有工作，发现不足，提出并检验课题或假设 | project、evidence map、research prospectus |
| L4 | 使用真实、公开或可靠模拟数据开展可复现研究，形成并验证新认识 | manifest、analysis run、failure、decision、provisional finding |

普通问答仍只读。用户要求摄入、固化、reflect、project 或 synthesis，即授权与任务直接相关的 L0-L2 写入；不得因 ordinary Q&A 静默写回。

所有 L0–L4 研究单元遵守 [`system/path-contract.md`](../path-contract.md)：source、project、evidence map、research prospectus、问题修订和可复用研究结论写入 `knowledge/`；`outputs/` 只保存研究报告、审计、readiness、run receipt、调度状态和 `outputs/plans/` 计划书。报告里的 durable knowledge delta 必须能回链到 canonical `knowledge/` 页面；报告不能成为唯一知识副本。

## Codex self-audit 与后续用户裁决

Codex 默认自主完成普通摄入、locator 复核、低风险纠错、关联固化、L3/L4 研究和候选问题记录。Codex self-audit 必须检查直接来源、locator、claim kind、证据层级、竞争解释、source lineage、适用条件和失败条件，并把判断写入对应报告或 source/project 页面。

- 用户审核只在后续问答需要裁决具体说法，或论文写作需要将具体 claim 纳入 paper evidence gate 时发生；
- `human-reviewed` 只记录真实用户审核事件，Codex self-audit 不伪装成该事件；
- 权限、ACL、项目配置、用户 raw、不可逆操作和外部状态变化仍按各自安全边界处理。

Codex self-audit 可以依据直接证据更新 `needs_review` 和 confidence 的技术记录，但必须保留证据边界，不能设置 `human-reviewed`。论文写作或后续问答中的最终措辞仍按 paper evidence gate 需要用户确认。

## L2 默认研究学习闭环

摄入任务完成精确 source 后，默认执行：

1. 判断新证据对既有认识是 supports、limits、revises、conflicts 还是 no material change；
2. 固化可复用事实、方法和适用边界；
3. 检查反例、替代解释、证据独立性和迁移条件；
4. 回查影响主要结论的 locator、数值、公式或外部元数据；
5. 将高价值且尚不能解决的问题去重写入 `knowledge/questions.md`；
6. 输出摄入、自校验、知识变化和遗留问题摘要。

### L2 bounded verification

L2 内可以围绕一个直接相邻问题继续求证，不新增 L2.5：

- 若直接来源或小计算可能解决重要冲突，Codex 自主验证；
- 若需要系统背景调查、多个竞争解释或可能形成研究课题，自然升级为 L3；
- 不按固定文献数量或检索次数决定深度，而按重要性、信息增益、证据充分度、资源成本和权限边界决定；
- 当继续搜索不能改变主要判断、开始重复证据或成本明显高于收益时停止并记录理由。

## 问题严重度与状态

P0/P1 表示重要程度，不自动等于等待用户逐项处理。每个重要问题记录受影响 claim、状态、验证依据、隔离措施和下一步。

允许状态：

- `self-checking`
- `resolved`
- `downgraded`
- `remains-open`
- `active-L3`
- `candidate-L4`
- `blocked-needs-source`
- `blocked-needs-user-data`
- `safe-suspended`
- `formal-review-required`

来源身份/哈希无法确认、关键数值或 locator 无法追溯、数据安全/权限/Git/raw 异常、用户数据可能被破坏属于技术 hard P0，必须阻止 finalization/push。科学措辞越级、争议、partial/stopped 研究状态和未触发的用户审核由 Codex self-audit 降级、隔离并记录，不单独阻止发布。

## L3：课题调查与假设研究

触发方式：

- `开始 L3 研究：<问题>`；
- `自动选择一个 L3 pilot`；
- 授权摄入或每周自测发现高价值问题，并满足下述升级条件。

状态为 `active-L3`、`safe-suspended`、`awaiting-milestone-review`、`completed` 或 `abandoned`。`awaiting-milestone-review` 只在后续问答/写作需要用户裁决时使用；普通研究完成 self-audit 后即可进入 `completed`。状态绑定具体研究问题，不扩散到无关任务。

### L3 升级条件

问题满足一项或多项即可进入 L3：

- 影响核心知识或重要研究判断；
- 存在多个可证伪竞争解释；
- 需要梳理领域背景和已有工作才能判断；
- 有现实可能形成研究课题、实验建议或数据分析方向；
- 下一步取证预期能改变假设排序或解决关键矛盾。

### L3 自主循环

1. 固定问题、范围、排除项、milestone 与终止条件；
2. 梳理研究背景、历史演化、已有工作及证据依赖；
3. 建立竞争解释，记录支持、反证、隐含假设和可区分预测；
4. 按信息增益选择 Wiki、Zotero、外部来源、反证搜索或小计算；
5. 更新假设排序和 belief revision，不静默删除失败路线；
6. 提出候选研究问题或可证伪假设，并按重要性、创新潜力、可检验性、数据可得性和信息增益排序；
7. 自主选择下一项文献、计算或建议测量；
8. 形成已有工作图景、证据缺口、研究 prospectus 和下一阶段文献/数据需求。

L3 不设机械检索或文献数量上限。继续条件是下一步仍可能产生实质信息增益且成本与问题价值相称。边际收益显著下降、证据开始重复、关键来源缺失、资源不足、WIP/权限冲突或下一步属于 L4 时，停止或 safe suspend。

## L4：手动发起的数据研究

L4 可使用用户真实数据、可追溯公开数值或具有代码/参数/随机种子/验证条件的可靠模拟数据。结论强度必须随数据类型校准，模拟结果不得冒充实验事实。

L4 必须同时包含：

1. 从 L3 缺口或潜在创新点提出数据可检验问题；
2. 建立数据身份、来源、版本、哈希、单位、不确定度、映射和保密边界；
3. 执行可复现分析；
4. 比较数据、预测与竞争假设；
5. 执行敏感性、负例或失败检查；
6. 根据结果改变假设排序或下一步；
7. 形成新的 provisional research insight。

重画图、机械复现、只建立 manifest、只做文献综合或只写论文不能单独算 L4。

### L4 手动启动关口与每日计划授权例外

一般任务一旦判断下一步属于 L4：

1. 完成当前 L3 milestone；
2. 建立 `candidate-L4`，写明所需数据、格式、单位、误差、分析和可能创新点；
3. 更新 handoff/WIP queue 并建立本地 checkpoint；
4. 进入 `safe-suspended`；
5. 请用户确认数据真实存在、位置和使用授权；
6. 等待用户手动发送 `开始 <项目> L4：数据=<Wiki 内路径>；问题=<可省略>`。

定时 automation 和普通摄入不得自行越过该关口。例外是用户在
2026-09-23 明确授权的 Docker 内 30 天 daily-learning 计划：该模式可自主
从 L1/L2 升级到 L3/L4，使用仓库内可访问的真实、公开或可靠模拟数据、联网
来源、代码和分析工具，不再等待单独的 `开始 … L4` 消息。它仍必须满足本节
的数据身份、可复现分析、敏感性/负例和失败检查要求；输入不全时记录
`candidate-L4`/readiness boundary，不生成代理实验结果。该例外只改变启动授权，
不改变证据分层、论文证据门或 `human-reviewed` 语义。

## 每周自主知识自测

在本 Wiki 的 Docker 运行环境中，周测由同一 Docker 内调度器在 Day 7、14、21、28
的检查点触发；不创建宿主机任务或外部 automation。实际完成必须有运行回执，
没有回执只能记为未触发。其它部署环境可以自行提供时钟，但不能把外部调度状态
写成 Wiki 已执行证据。

### 目标与动态边界

自测用于校正知识、检查跨页一致性/证据独立性、发现过强表述和遗漏反证，并主动形成研究问题。每次运行先分型：

- `weekly-learning`：真正计入周测轮次，最多主动研究两个满足硬重要性门槛的问题；
- `continuation-audit`：续跑既有 P0/P1、来源谱系或 locator 审计，只在产生新的决策相关信息时占用温故槽，不计为新知轮次；
- `maintenance`：状态对账、低风险格式或普通元数据维护，不计入周测，也不得借此升级 L3/L4。

重要问题必须至少满足一个硬条件（关键事实/解释存在实质来源冲突、缺失原始证据可能改变结论或 human-review、分析不可复现且影响推断、同位素/同中子素比较可区分竞争解释，或新高质量证据可能显著限制现有结论）。措辞、格式、别名和低影响元数据不得升级为 L3/L4。

### 全局选题与双槽位

在打开具体证据页、下载文献或写入知识页之前，先做一次 Wiki 内只读的全局候选筛选。候选池至少覆盖核素/质量区、物理主题或竞争机制、实验方法/observable、证据类型和 Codex self-audit 风险；候选必须通过上述硬重要性门槛。`PLAN.md` 的 `131Ce` 数据阶段是用户方向记录，不是周测的默认选题权。

每个 `weekly-learning` 运行最多有两个槽位：

1. **温故槽**：只给 hard P0/P1、出现新独立证据或可能改变科学判断的既有问题。单纯状态修复、locator 补全或重复核验应标为 `continuation-audit`，不能独占整个周测。
2. **新知槽**：只要存在合格候选，必须从全 Wiki 的非重叠覆盖区域选择；没有合格候选时只输出核验回执，不为了填槽升级低价值问题。没有温故问题时，两个槽位可选择不同覆盖区域的新问题。

新知槽的覆盖历史从仓库内最近八次 `weekly-learning` 报告重建，不读取 Codex 宿主 memory/global/sandbox state。相同核素或 project 不得连续占据新知槽；同一核心来源集合至少冷却两个真正周测周期。hard P0、新出现的独立原始证据、实质来源冲突或用户明确指定可突破冷却，但报告必须记录例外原因。

通过重要性和冷却筛选后，按科学影响、覆盖债务、距上次检查时间、证据独立性缺口和预期信息增益排序；只在同等级候选之间使用以 ISO 周为种子的可复现随机抽选。修正规则上线后的第一轮 `weekly-learning` 新知槽不得选择 `131Ce`、Ding 2021、`127Xe` 2020 或 `129Ba` 2024，除非记录上述硬例外。

文献总量不设固定上限，但每批必须是去重、题名/DOI 明确且直接服务于两个问题之一的有限清单；在批次间按独立证据、关键 locator、竞争解释和信息增益重新评估。证据饱和、信息增益下降、验证/时间余量不足、外部来源不可得或超出两个问题时收敛或建立 WIP。未入选的重要问题写入报告 `Deferred important issues`，记录页面、证据缺口、建议路径及下次周测续研。已开始并改动文件的任务才进入 WIP。

核素问题原则上比较至少一个适用同位素和一个同中子素；物理上不适用或没有可靠资料时说明原因，不机械创建页面。L3 可按 Nature-first 路由检索、合法获取、核验 locator、摄入 `raw/papers/gpt/**` 和 `raw/zotero/gpt.bib`；关键数据/方法只在补充信息中时可获取 SI。`raw/zotero/wiki-inbox.bib` 始终只读、不得暂存。无法获得全文时记录 DOI、访问路线和下一次获取路径，不循环登录或把 HTML 当 PDF。

L4 对公开数值或可靠模拟可以在具备数据身份、参数、代码和失败检查后由 Codex 自主执行；用户提供的真实数据仍需用户手动启动。没有完整输入时先生成 readiness audit，输出来源、可复现程度、缺失 observable/locator 和 `ready`/`partial`/`not-ready` 到 `outputs/l4/<issue>-<date>/report.md`；若 readiness 产生可复用知识或研究设计，必须同步写入 `knowledge/`。`partial`/`not-ready` 只结束该问题本轮扩展，不停用周测。继续、暂停或升级仍由重要性、证据充分度、信息增益、资源、权限和实质进展决定，避免机械浅尝和无价值无限扩张。

### Git 安全门

每次运行先检查 Git/远端、dirty baseline、WIP queue、运行内 `wiki-inbox.bib` 基线和文件 overlap；独立运行之间的 Zotero 正常更新不阻断新运行。完成 H1 后先做全局只读候选筛选，再决定续跑或写入：

- active weekly/L3 WIP 只能在满足信息增益条件时占用温故槽；不能跳过新知槽筛选；
- 用户未审核的内容只阻止需要该用户裁决的最终问答/写作措辞，不阻止全局只读选题、无重叠的新知任务或 Codex self-audit 写回；
- 无法区分归属或存在 unresolved overlap 时只读检查并 safe suspend；
- 无实质发现不创建分支或 commit；
- 普通治理和周测修改继续在已核验 `main` 上小步提交；只有确有技术隔离需要时才创建分支。

周测 automation 只产生经过 Codex self-audit 的结果；通过 H3 和仓库发布检查后，按持续授权进行正常非 force push；存在技术 hard P0、检查失败或远端异常时保留本地 WIP。科学 partial/stopped 和未触发的用户审核不单独阻止发布。无实质变化时只输出可核验回执，不制造空提交。

### 审核报告与 checkpoint

每次完成都在任务中形成报告；有实质修改时同时创建 `outputs/self-tests/YYYY-MM-DD-<topic>.md`，依次包含 `Selection audit`、范围、P0、P1、低风险摘要/链接、验证与研究摘要、L3/L4 状态、文件/Git/检查状态。`Selection audit` 必须记录运行类型及是否计入周测、候选覆盖类别、两个槽位的选择结果、核心来源指纹及近期重叠、冷却例外/deferred 原因、本轮新增知识和 belief-revision 结果。

报告、计划和回执属于交代层；新增 source/project/synthesis/evidence-map/question 或其它长期资产必须在同一任务中落到 `knowledge/`，并在报告中列出 canonical 路径。没有新增知识时明确写 `verified no-op`，不以长报告文字替代知识增量。

用户默认可只阅读 P0、P1 和升级状态；Codex 不主动索要审核。低风险内容只提供摘要与可追溯链接；后续问答或论文写作需要用户裁决具体 claim 时，再触发定向审核。

有实质变化时完成 Git 检查、Wiki lint、显式 stage；Codex self-audit 完成且无技术 hard P0 时，使用当前 rolling WIP amend 为 final 并按发布门 push。未完成 L3、L4 输入不足、技术 hard P0 或安全暂停时使用 `WIP suspend: weekly L3 YYYY-MM-DD <topic>`，不 push。同一分支继续时 amend，不创建第二个 active WIP。无实质变化不制造空 commit。

WIP 创建或 amend 成功后，即使不准备 push，也必须按 `check.md` H3 完成 post-commit reconciliation：用实际 branch + subject（subject 取自 HEAD）核对报告、Active handoff 和 WIP queue，把提交前的 `planned` / `expected checkpoint` 未来时态改为实际本地 WIP 状态；需要修正时 amend 同一个 WIP 一次并重跑 H3。WIP 自身不得在其包含的文件中记录自己的精确 hash；最终 hash 只在任务回执中报告。

若后续发生用户审核，按用户意见进行定向 review-finalization；普通 Codex self-audit 完成后即可将 WIP amend 为 `Finalize weekly self-test YYYY-MM-DD: <topic>`，并在远端无漂移且 H3/发布检查通过时自动 fast-forward main 并 push。未完成技术 hard P0 时保留本地；科学 partial/stopped 不影响已校准结果发布。论文级最终措辞仍须通过 paper evidence gate。

## 共同停止条件

- 达到 milestone 或当前证据足以支持边界清晰的结论；
- 下一步信息增益不足；
- 来源/数据/外部验证缺失；
- 权限、raw、Git、外部写入或不可逆操作边界将被触及；
- 上下文、执行时间或资源不足以可靠完成。

停止不是丢弃：记录状态、依据、剩余 gap、下一步和 continuation prompt。论文主张、正式写作措辞、用户 raw 修改、权限变化和科学发布门仍遵守相应边界；普通 Git commit/push 已获持续授权，科学 partial/stopped 不单独阻止发布，但技术 hard P0 不能越过。

## Counter-evidence requirements (all levels)

For each high-risk claim, the next L3 milestone must record the core claim, necessary companion observable, support, counter-evidence, alternative explanation, sensitivity of any missing signal to statistics/efficiency/gate/resolution/binning, discriminating prediction, falsifier, belief-revision trigger, and stop condition. If the judgment rests only on visual impression, coarse binning, or a single feeding line, retain `active-L3` or `blocked-needs-source`.

Before entering `candidate-L4`, the data manifest and analysis plan must list expected-but-absent observables, detector-response/background templates, gate/threshold/binning sensitivity, negative or random-window controls, and how a missing companion signal changes model ranking. A suspicious counter-signal never starts L4 automatically.

Each weekly self-test of a high-risk claim must include one necessary-companion check, one background/resolution/gate check, one source-independence check, and one explicit belief-revision condition. Reports record missing necessary evidence alongside newly discovered facts.
