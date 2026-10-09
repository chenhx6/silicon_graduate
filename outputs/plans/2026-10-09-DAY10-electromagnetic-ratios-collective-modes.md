---
type: task-plan
graph-excluded: true
created: 2026-10-09
updated: 2026-10-09
---

# 正式 DAY10 学习计划｜电磁比值与集体模式判别

## 运行安排

Day9 normal-runner finalizer 已验证只完成卡 9，并将课程推进到 `next_day_index=10 / completed_day_count=9`。Day10 正式任务应由下一次 schedule 在 **2026-10-09 16:00 Asia/Shanghai** 使用新 session 启动；硬研究截止为 **2026-10-10 15:00**，之后仅收束。此计划只定义待执行卡片，不启动 session，也不把 Day9 中的 Day10 预习计为 Day10 正式回忆或课程学分。

- 正式提示词：[DAY10 prompt](../learning-daily/prompts/20261009-DAY10-electromagnetic-ratios-collective-modes.md)
- 上一日正式日报：[DAY9 report](../learning-daily/20261008-DAY9-be2-bm1-reduced-matrix-elements-strengths.md)
- DAY9 receipt：[DAY9 run receipt](../learning-daily/20261008-DAY9-be2-bm1-reduced-matrix-elements-strengths-run-01/run.json)
- 对照卡片：[daily task matrix, Day 10](2026-09-22-one-month-daily-task-matrix.md)

Day9 preview 已读 MU07、Zhu、LV19、LKH82 和若干竞争解释；DAY10 开始时先列独立召回，再以这些已有笔记校准，并标为 `primed recall`。不得称 blind recall，也不得把预习代替 Day10 的逐卡 audit。

## 卡片交付

| 动作 | 正式交付 | 证据/边界 |
|---|---|---|
| 回忆 | 解释有量纲的 `B(M1)/B(E2)` 强度商、同一跃迁 `δ²`、同自旋 out/in 强度商及 `Qt` 的不同输入；召回后校准并标 primed。 | LKH82-1；MU07-11；Day9 recall-record 仅作预习校准，不作为正式回忆记录。 |
| 主线 | 对照 `135Nd` Band A/B 的五个 Table-I 同自旋强度商和四个图估 out/in 点；将测得/拟合强度、跨线身份、模型解释分层。 | MU07-5/7/8/11；printed 172501-2 Table I、printed 172501-3 Figs.2–3。 |
| 定量练习 | 建立两条候选带随自旋的 `B(M1)`、`B(E2)` 和比值表；只对线身份和母态预算假设写条件计算，逐项写单位/共同输入/误差覆盖边界。 | MU07-9/10/13/16；ZH03-3；LV19-9；LKH82-1。Day9 中的 photon-budget 不相容只排除所列的附加联合解释，不认定作者错误、不推定唯一真实线身份。 |
| 模式反证 | 用至少两个可产生相似比值指纹的替代机制或不同模式例，检验只凭比值趋势无法唯一判别的边界。 | TI07-11/13/14/15（组态混合）；SU08-6/7/8/13（E2 分母）；PE06-1/2（crossing/alignment/模型依赖形状）；C23-2/3/7 或 LV21-9/10/11/17（不同核或不同带的混合比控制）。不同数据集不可并成一份独立测量。 |
| `Qt` 和证据单位审查 | 在缺少逐线 `(Eγ, Ji→Jf, K)` 或适用转子矩阵元时写出不报唯一 `Qt` 的理由；绝对 B、RME、reverse-B、同母态商与 Qt 的共用输入不重复计证据。 | MU07-11；SI16-17；ZH03-3；`knowledge/questions.md` 中的 135Nd transition-identity question。 |
| durable knowledge + audit | 将至少一条新的可复用差异/误差/判别边界写入 canonical `knowledge/`，或对具体候选矩阵作 grounded verified-no-op；日报有唯一 writeback、十个标准标题及不少于四行 Day10 completion audit。 | 只引用 `knowledge/sources/` 里逐字存在的单一 atomic locator；所有 review flags 保持。 |

## 分析边界与结束条件

1. MU07 Figs.2–3 不按跃迁列出 out-point 线身份；ZH03 与 LV19 仅限制候选，不把之后的谱线归属冒充为 2007 B 值的实测绑定。
2. MU07-16 是同一强度/寿命链的条件母态预算一致性检查，不是另一项实验；未测分支、IC、feeding、stopping、图点覆盖及联合协方差仍须明示。
3. `B(M1)/B(E2)` 的量纲商不等同同跃迁 `δ²`。缺失候选跃迁能、终态和 `K` 时不反解或编造 mixing ratio/Qt。
4. 对每条机制结论列一个可区分的伴随观测量；模型计算不得当作实验事实。没有原始事件/响应/协方差/可执行拟合包时，不自称已完成 L4。
5. 所有并行比值、ratio-of-ratios、RME/reverse-B 及同母态变换先写依赖图，避免同一源强度与寿命被重复加权。
6. 保持 `day_index=10`。只在所有 Day10 矩阵交付通过后记 `[10]`；若不完整，只记为 partial。是否预习下一卡只由 Day10 当次 Runtime snapshot 决定。

## 出版与保护

先检查 Git 入场状态和路径边界；保护 `raw/`、`PLAN.md`、Zotero BibTeX、继承脏文件及 review 状态。最终只显式暂存本 run 自有 manifest，执行 `git diff --check`、Wiki lint、fresh-fetch / ancestry / `HEAD:main` dry-run / 同 refspec 非 force push 和 post-commit reconciliation。
