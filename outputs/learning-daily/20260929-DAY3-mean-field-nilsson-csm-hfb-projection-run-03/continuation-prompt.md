# Day 3 continuation checkpoint

继续 `prompt-2026-09-29-day-03`，不要将当前 checkpoint 当作学习日结算。窗口截止时间保持 `2026-09-30T15:00:00+08:00`；session 为 `01a0eb92-e525-7863-a0c9-af73a53d832b`，可复制恢复命令：

```bash
codex resume 01a0eb92-e525-7863-a0c9-af73a53d832b -C /workspace/wiki -s danger-full-access -a never
```

## 已完成并可复用

- 核对 Åberg–Flocard–Nazarewicz 1990 与 Hara–Sun 1995 原文身份、哈希和关键 locator；出版商网页返回 403，使用仓库内原 PDF。
- 阅读/视觉核对 Hara–Sun Eqs. (2.7), (2.19)–(2.20), (2.40), `156Er` Figs.26–27、A≈130 Table 5，以及 ABFN Fig.12；区分模型输出与实验报告。
- 更新 `knowledge/projects/a130-model-choice-card.md`，补入投影核广义本征问题、particle-number projection 截断风险，并注明 Hara Table 5 的 N=76/78 triaxial 候选不可转移到 `131Ce` N=73。
- 日报已建立：`outputs/learning-daily/20260929-DAY3-mean-field-nilsson-csm-hfb-projection.md`；当前仍是 checkpoint，`counted_in_substantive_test=false`。

## 后续最高信息增益路线

1. 检索并核验一篇现代 A≈130 三轴投影/配置混合来源，确认它实际计算的核素、形变自由度、组态空间和实验比较量；优先判断历史 N=76/78 候选是否有三轴代码直接检验。文献身份和 locator 回到原文，不凭摘要或 Wiki 搜索片段写结论。
2. 如果没有可访问的直接来源，转到 `131Ce` 目标跃迁缺口设计：将 measured `δ`/偏振、伙伴带寿命、absolute `B(E2)/B(M1)`/`Q_t` 映射到 CSM/QTR 与投影模型的可区分预测；保留 ordinary signature/configuration coupling 作为竞争解释。
3. 每条续接都要先重建候选池并主动回忆，检查反证、必要 companion observable、来源独立性，并做一项可复算或最小设计练习。不要重复读取已核对的 AFN90/HARA95 全文，除非新来源产生具体冲突。

## 收尾边界

- 15:00 Asia/Shanghai 起停止新增来源路线；留出一小时完成最终报告、knowledge writeback 校验、lint、`git diff --check`、回执、state-file 推进和次日提示。
- 未到正式 closeout 前保留 `next_day_index=3` 与 continuation 状态，不把模型结果升格为实验事实，不改 review status。
- 继承目录 `20260929-DAY3-mean-field-nilsson-csm-hfb-projection-run-01/` 和 Day 2 的 untracked raw bundle 保持原样；只显式暂存本日授权文件。
