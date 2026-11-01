---
type: prompt
graph-excluded: true
created: 2026-10-31
updated: 2026-10-31
---

# Day30：证据门收束与研究 prospectus

Day29 已完成 `131Xe` 794-keV 宇称与 882-keV 双根的研究设计答辩。Day30 的任务是把
开放路线压缩成可执行的 post-30-day 研究 prospectus，并完成一次 source lineage、claim
language 和 L3/L4 readiness 的定向复核。不得把同一 INGA acquisition 的 2020/2023/2022
材料计为独立实验，不得制造 event-level counts、response、covariance 或 holdout。

优先顺序：

1. 完成 `131Xe` source lineage 字段的定向审计：`lineage_id`、`lineage_role`、
   `dependent-reanalysis`、journal/arXiv version relation、raw hash 与 review scope。
2. 将 `135Pr`、`135Nd/134Pr`、八极 source-page 和全库 claim calibration 组织为候选
   prospectus；每项写清最小新增输入、falsifier、停止条件和不独立证据。
3. 复核 `outputs/`、`raw/`、`knowledge/` 路径契约和 source→raw reconciliation；只做
   可逆、逐文件、证据闭合的修改。若用户在运行中明确授权整理指定 raw 子树，
   可按用户给定语义逐文件移动或清理，但必须先生成哈希/目的地清单、保留回滚
   记录并通过 `wiki_archive_gate.py`；不得扩大到其它 raw 子树。
4. 产出 Day30 报告、知识写回、课程审计和下一阶段恢复命令；若关键输入仍缺失，保留
   `partial`/`readiness boundary`，不以论文数量代替信息增益。

正式回读：

- `knowledge/research-notes/131xe-day29-research-design-defense.md`
- `knowledge/projects/post-30-day-nuclear-structure-paper-prospectus.md`
- `knowledge/research-notes/full-library-claim-calibration-audit-20261031.md`
- `outputs/learning-daily/20261031-DAY29-research-design-defense.md`
- `system/path-contract.md`

Day30 的课程 credit 只有在 prospectus、lineage audit、知识写回、报告和发布门全部完成后
推进；局部预览不得推进 next_day_index。

## User-authorized archive amendment (2026-11-01)

用户要求所有论文、学位论文、笔记、网页快照、图片、私有数据和其它
source-dependent 材料在 `raw/` 内留档。使用：

- `.agents/skills/research-archive/SKILL.md`
- `system/scripts/wiki_archive_gate.py`
- `python3 system/scripts/wiki_hook.py after-edit --root .`

`133Ce` 研究可在完成留档后继续作为有界自主路线：以
`knowledge/research-notes/133ce-triaxial-core-collective-mode-route-20261101.md`
为入口，使用已归档的 NuclearMap `132Ce/134Ce` PES 邻核先验和
`raw/data/SouthAfrica/` 私有数据；不得把 `133Ce` 直接 PES、事件级响应或
完整 L4 结果从缺失输入中推造出来。

<!-- DAILY_LEARNING_CURRICULUM_COVERAGE_V1 -->
## Curriculum card completion record
In the report's Run state include exactly these two machine-readable list lines:
- completed_day_indices: [N, ...]
- partial_day_indices: [N, ...]
Count a card only after every deliverable on that Day card is complete. For every completed day, add `- Day N card audit: complete` under Run state and a `### Day N card completion audit` table with at least four Day-matrix deliverables, each linked to an evidence locator/artifact and marked complete. Partial previews go only in partial_day_indices. List cards contiguously from the requested day; at most one next-day card may be advanced in one run.
For a completed Day 7 card also include these exact audit lines:
- Day 7 scorecard: complete
- Day 7 weekly REFLECT: complete

<!-- DAILY_LEARNING_TIME_GATE_V1 -->
## 时间判断与学习收束
候选问题或来源达到局部证据饱和时，先读取最新 Runtime schedule snapshot；手动恢复且没有新快照时，调用当前时间工具，并按 Asia/Shanghai 与回执中的 overnight_until 比较。
距离硬截止至少 120 分钟：继续当前高信息问题；若当前选定问题已饱和，检查下一张未完成日卡，只有其全部交付项能在剩余时段完成时才整卡前移。
距离硬截止 90–119 分钟：继续当前问题或做有边界的预览，不给下一日卡完整学分。少于 90 分钟：不打开新来源或新卡，只完成当前分析。硬截止后停止研究，在回执的有效截止后一小时内收束；默认15:00–16:00，显式用户延期按已校验的effective窗口执行。
不能仅因两个候选槽位饱和而提前结束；须重建候选池、检查下一张可行日卡，并记录时间快照和决定。用户明确停止、硬证据/数据/权限阻塞或运行故障可提前结束，但必须保留未完成状态和续接命令。
每次调用生成的新 Runtime snapshot 优先于本文件中的旧快照。课程学分只沿连续完整日卡推进；部分预览不得推进 next_day_index。
