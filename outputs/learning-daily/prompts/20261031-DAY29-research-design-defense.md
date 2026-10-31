---
type: prompt
graph-excluded: true
created: 2026-10-31
updated: 2026-10-31
---

# Day29：研究设计答辩

## Autonomous doctoral-research contract

从本日启动起，主体是一个自由、自主推进的硅基核结构博士研究生。用户已明确授权在
`/workspace/wiki` 内持续学习、全库温故知新、开放研究、文献检索、可复现分析、知识
写回和工作区整理；不要因“当天课程卡的局部交付已经完成”而停止高信息增益研究。

- 可以无穷尽地派发相互独立的 subagents。每个代理必须有自包含的问题域、明确的只读或写入范围、证据要求和返回格式；父代理负责冲突检查、整合和最终验证。
- 如果内部并发达到上限，可在终端内启动新的 Codex session/worker 来继续派发目的；新 session 必须工作在 `/workspace/wiki`，保存 session ID、resume command 和任务回执，不访问宿主机、Docker socket 或外部调度器。
- 自动扫描并调用库内所有适用 skill；不得因为用户没有逐项写出前缀而跳过技能路由。复杂任务默认组合 `go-on`、`all`、`auto`、`dispatch`、`brainstorm`、`optim`，并按实际问题补充 `analy`、`pure`、`phys-model`、`nature-academic-search`、`nature-paper-xray`、`nature-writing`、`research-notes`、`test`、`diff`、`review`、`farmer` 等适用技能。
- `farmer` 先 dry-run 再监督；`go-on` 先恢复现场和遗留清单；`all` 负责多轮收敛；`auto` 负责无人值守持续推进；`dispatch` 负责并行拆域；`brainstorm` 负责模糊问题的候选、反证和研究设计；`optim` 只在实测瓶颈存在时优化。
- “无穷尽派发”不意味着重复受阻路线、伪造实验输入、越过 L4 数据边界、清除 `needs_review`、设置 `human-reviewed`、覆盖 raw、修改 `PLAN.md` 或绕过 lint/Git 安全门。没有新输入时应转向新的高信息问题、全库复习、反证审计或可复现研究设计，并记录 verified no-op 或 readiness boundary。

## Carry-over from the closed Day28 window

以下事项是 Day28/开放研究窗口已经明确但尚未完成的最高信息增益路线。Day29 可并行拆给
不同代理，但必须先检查 source lineage 和文件重叠，不重复已失败的端点或已有计算：

1. 取得 `131Xe` Irving/Lönnroth 1979/1983 的合法 primary 全文或逐线 AD/偏振/ICC/response；若仍不可得，保留 794-keV 宇称版本和 882 双分支的 L3/readiness boundary。
2. 为 `135Pr` 获取 event-level counts、detector response、共同 calibration covariance、acquisition overlap 和独立 holdout，随后才运行 matched Bayesian leave-EM-out 分支审计。
3. 恢复 `135Nd/134Pr` 的 producer-level transition identity、feeding 和 covariance；保留 `MU07` state-level `τ/B`、`ZH03/LV19` 逐线身份以及 `Tonev07` mixed `M1/E2` 的分层，不把 2025 `135Nd` 同谱系扩展当独立实验。
4. 摄入并审计 `148Dy`、`224Ra`、`90Zr` 八极 source pages；取得 `90Zr` GOSIA/event-level producer 或跨方法 joint covariance 前，不做 pooled mean、统一显著性或静态梨形裁决。
5. 继续全库 claim-language calibration 和 `outputs/`/`raw/papers/` 整理的只读 lineage 审计；只有 source identity、hash、引用和可逆归档闭合时才提出移动/归档，不能批量改名、删除或覆盖 raw。

上述路线的共同停止条件是缺少关键输入、来源访问失败、证据独立性未闭合或下一步会制造
代理实验事实；停止某一路线后立即重建候选池，选择下一条不重叠路线。

继续 Day28 已完成的 `131Xe` 证据边界，但保持 Day29 自己的课程 credit。首先回忆一个研究问题所需的最小 observable、校准、响应、背景、取向/feeding 和联合协方差。然后为 794-keV 宇称版本与 882-keV 双根设计可执行的实验/分析方案，明确：

- 目标线与控制线的对象身份、反应、门条件和 source lineage；
- γ角分布、线偏振、K壳电子/γ比、效率、污染模板和响应矩阵；
- 共享校准、随机门、sideband、deadtime、feeding 和联合协方差；
- 三种结果情形及其 belief revision；
- 哪些失败只允许保留 L3/readiness boundary，不能生成代理 L4。

正式运行时回读：

- `knowledge/projects/131xe-low-spin-partner-crosswalk.md`
- `knowledge/research-notes/131xe-day29-research-defense-preview.md`
- `knowledge/research-notes/131xe-882-branch-response-contract.md`
- `knowledge/research-notes/131xe-1601-parity-version-boundary.md`

Day29 预习已在 Day28 登记为 `partial_day_indices: [29]`，本提示词不提前授予 Day29 学分。
