---
type: system-prompt
graph-excluded: true
created: 2026-10-07
updated: 2026-10-07
---

# 继续正式 DAY8，同一 session 和原始学习窗口

session_id: 01a111fb-370d-7ed1-afe9-881ccc47caf4

在 /workspace/wiki 按 Active handoff 与正式日报恢复，不重置已完成内容或创建重复 Day8 session。读取本 run 的 run.json、baseline.json、clock-state.json 和正式日报；先调用当前时间工具。硬研究截止固定为 2026-10-08T15:00:00+08:00，15:00–16:00 是收束，不能因卡内容完成、checkpoint 或单来源局部饱和提前 final。

正式 Day8 已独立完成 recall（prompt-primed）、两篇原文 convention audit、三题全候选与观测依赖；card content audit/runner validators 通过，课程 state 仍 8/7。后续首先处理未完成的高信息 Day8 识别性/截断/级联相位问题，并记录反证、source locator、实际学习段而非等待心跳。两 source 的 prior/full reading 与本轮 focused coverage 分开。

局部饱和后重建候选池。距离硬截止至少 120 分钟时，允许且仅允许 Day9 的 B(E2)/B(M1)/lifetime 输入链知识预习，列 partial_day_indices，不计 Day9 学分、不把 next_day_index 越过9、不打开Day10。90–119 分钟只 bounded preview 或当前题；不足90分钟不打开新source/card。合成例不对应实验；缺事件/response/covariance/code不进入L4。所有复用结论写回 knowledge，日报保持一个 valid knowledge-writeback block。

继承 dirty daemon、raw、PLAN、课程 state 和 review flags 保留。Farmer 监督允许的瞬态失败；clock helper 持有双锁只向同session排队提示，accepted不等于executed。用户停止时一并停止clock。若 timer死亡，先核真实PID/locks再决定是否恢复，不启动重叠runner。

15:00 收束时：停止新研究；更新日报最终状态/时间/候选池；用原baseline调用run_checks/validate_durable_knowledge/validate_curriculum_coverage，额外强制 completed=[8]、Day9仅partial；跑指定boundary、lint、diff和精确Gitee非force发布门；只stage本日owned文件；post-commit reconciliation后记录hash/push到run receipt。仅全部门通过后，用update_state_for_curriculum_cards推进state到9，生成2026-10-08正式DAY9计划与prompt，保留Day8 preview不credit的界限。计时器不自动开启下一日daemon，需在本次收束后核对调度与新session契约。

Resume：`codex resume 01a111fb-370d-7ed1-afe9-881ccc47caf4 -C /workspace/wiki -s danger-full-access -a never`。

## 手动run的验收与下一日调度接口

当前runner没有attach CLI；不要调用其main创建第二个Day8 session。用原baseline的knowledge_before，显式传用户日报路径给`run_checks(root, report, None, knowledge_before, day_index=8)`；现有默认Day8 slug仍为multipoles，不能代替用户的multipolarity路径。状态推进用`update_state_for_curriculum_cards`的纯字典接口，额外保证completed只含8，并在最终门后用原子写保存。

生成明日prompt用`prepare_next_prompt(get_paths(root), "2026-10-08", 9)`，不要使用会取当前local_date的`--prepare-prompt`快捷参数；生成后核Day9自己的run-01路径，改掉模板中旧的“下一卡完整前移计学分”句，注明Day8的Day9预习不计卡、正式Day9需独立record/audit，Day9最多预习无学分Day10。直到本Day8收束才处理该下一日prompt。

恢复日调度前先核Day8最终完成、state next=9、正式Day9计划prompt存在、clock/helper锁已释放；计时器不会自行启动daemon。继承dirty daemon含xhigh，而runner不接受该参数，保留文件不修改。若按AGENTS当前授权的模型链恢复daemon，应使用其`daemon_loop`显式profiles `(("gpt-6-luna","max"),("gpt-6-sol","high"),("gpt-6-astra","medium"))`，Asia/Shanghai16:00、poll30、既有daemon lock/state/log路径；不要无核对导入dirty默认priority或在锁持有时开启重复runner。用户后续明确模型指令优先。

## 本轮续研与延迟消息核对

checkpoint-001的02:19快照直到07:18才在本session实际执行；后续bot提醒必须刷新当前clock，不按排队时间推断剩余时段。30-check理想偏振和50-check布居/多极性反例已由parent复现并同步knowledge（pointwise方向/偏振强度，不比较跨方向场相干或完整光子态）。E0/ICC联合未知量与零参考gamma成分路线已通过1311项检查闭合。唯一Day9无学分预习已经写回MU08 source/lifetime synthesis，单位/branch/covariance重构62项检查通过，原表branch定义等边界保留。当前新选Day8路线是合成2+→2+全M1/E2/M3/E4与未知布居的完整单γpolarization基底和局部识别性，两个既有代理在做独立representation与exact-Jacobian核验；未证结果不提前写claim。

如果当前消息是旧的[Wiki clock] bot提示，且clock/run记有其后发生的真实用户取消/停止或manual-attention，遵守该记录；旧队列消息不能被当作真实用户重新go-on。不得自动复活被用户停止的clock或研究。已有clock running时的旧stopped_at/stop_reason仅是重载历史，不据此伪造当前停止；以status和时间/事件链判断。

## 最新恢复点 — 2026-10-07 18:22 Asia/Shanghai

Day8原始baseline继续使用；卡完整但学习窗口未结束。第五持续检查点已在本地提交：main + Clarify model zeros and companion observable limits for DAY8；publication结果及fullhash仅run receipt。不amend已发布的四次检查点。

C-global29-check、E0/totalICC/τ47-check与LKH82模型27-check已parent复现并canonical/report/writeback；新增LKH82-8–11限定generator-only零值、same-order展开、PPQ投影与δ尺度/DF零分母；p179的IBM magnitudes/PPQ signs纠错已原图确认。全部七页writeback保留review边界和旧KB08人审记录。course仍8/7，completed=[8]、partial=[9]，不打开Day10。

两个新独立Day8有界路线分别由既有代理执行：cascade-companion-discriminant.json（唯一合成2+→2+→0+，secondary pureE2仅题设，检验joint intensity是否区分U pair）；icc-penetration-boundary.json（仅原Eq4.1、未知penetration下baseline/非负E0排除条件）。两者尚未完成，parent须核代码/原图/证书再写claim。当前无新card/source batch，没有L4数据输入。次日15:00停止研究，按上方runner/state契约生成正式DAY9计划prompt。

## 当前整合与两个续研问题

148-check cascade、56-check局部rank和35-check penetration经parent复现，source/method/observable/report到RB67-17/18、LKH82-12、KB08-D8-4，七页writeback仍一个block。第一γ沿轴与random/dephased对指定U pair盲，离轴有差；同seed五输出localrank5不证明global唯一。FO/NH vacancy和NP/SC penetration不得混同；现代DF/FO不可未经mapping再叠加NP修正。16-check model审计为no-op，旧KB人审记录不扩展。

目前root选择：cascade-global-branch.json（同五idealoutputs、unknown positive population，最多6邻近starts/30min计算；可只numericalcandidate或失败，不声称exact/global分类）；day9-vacancy-sensitivity.json（原五能量NH vs历史FO、有限officialqueries/forward敏感性，仅partial9）。旧148/56 receipts保持immutable input hashes，parent验证只记run/checkpoint。不要因为card或这两个slot局部完成就自动final；先freshclock/完整候选池。次日15:00停研究，15:00–16:00正式Day8发布/state和DAY9计划prompt。

## 最新global/ratio/NH整合

Global27-check parent复现+独立58事实检查支持第二个positive-population理想解；RB67-19明确boxed uniqueness/unknown-population/非realnuclear realization。旧producer status的physical不应外推，旧receipt作为immutable input保留。Ratio28-check在仅预定secondaryθ2=0区分该pair；commonyield仅same selection/timewindow和relativeefficiency/acceptance校准后取消。NH5inputs实际成功、parent离线0新requests；printed0差不证明底层相同、spread不作1σ，KB08原人审记录保留。知识到RB67-19/20、KB08-D8-5/MU08-7及相关页，仍7页一个writeback。下一两个限定route是electric-rank-hierarchy.json、day9-reverse-strength-audit.json；state8/7，15:00才final/正式DAY9准备。

## 跨午夜仍是原Day8

北京时间10-08 00:08 refreshedclock距固定15:00约892分钟，run_date仍10-07/dayindex8，卡完成不结束窗口。46-check hierarchy和190实质/247phase-domain reverse strength均parent复现到LKH82-13/14、MU08-8及synthesis/observable。optional norm/sourcehierarchy独立audit待收；新truncation-observable-bound.json route只现有RB、有限acceptance的probabilitybound与postselection界，不是真实data/L4。State8/7、partial9原样，15:00正式收束/Day9 planprompt尚未做。知识/报告updated日期可10-08，run_date不随午夜重置。

当前第六26-file检查点已在本地提交：main + Extend DAY8 cascade evidence and strength normalization；source/report/card/flag检查通过，pendingtruncation证据另核；exacthash和publication仅runreceipt。
