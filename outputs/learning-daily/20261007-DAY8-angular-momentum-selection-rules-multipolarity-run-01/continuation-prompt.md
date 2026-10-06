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
