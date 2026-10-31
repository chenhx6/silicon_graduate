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
   可逆、逐文件、证据闭合的修改，不移动或覆盖 raw。
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
