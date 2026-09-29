# Day 3 continuation checkpoint

继续 `prompt-2026-09-29-day-03`，不要将当前 checkpoint 当作学习日结算。窗口截止时间保持 `2026-09-30T15:00:00+08:00`；session 为 `01a0eb92-e525-7863-a0c9-af73a53d832b`，可复制恢复命令：

```bash
codex resume 01a0eb92-e525-7863-a0c9-af73a53d832b -C /workspace/wiki -s danger-full-access -a never
```

## 已完成并可复用

- 核对 Åberg–Flocard–Nazarewicz 1990 与 Hara–Sun 1995 原文身份、哈希和关键 locator；出版商网页返回 403，使用仓库内原 PDF。
- 阅读/视觉核对 Hara–Sun Eqs. (2.7), (2.19)–(2.20), (2.40), `156Er` Figs.26–27、A≈130 Table 5，以及 ABFN Fig.12；区分模型输出与实验报告。
- 更新 `knowledge/projects/a130-model-choice-card.md`，补入投影核广义本征问题、particle-number projection 截断风险，并注明 Hara Table 5 的 N=76/78 triaxial 候选不可转移到 `131Ce` N=73。
- 取得 arXiv OA 版本 Bhat et al. 2014 (`1312.6963v1`, DOI `10.1016/j.nuclphysa.2013.12.006`)，核对 `130Cs` TPSM/Fig.8 与 absolute-strength 数据缺口；新建 source page 和 TPSM/model-choice/index 关系。Table 1/Eq. (3) 的 `γ` 复算与约 `30°` 文字不一致，保留 `needs_review`。
- 从 Bhat Ref. [32] 回溯并核验 Simons et al. 2005 `130Cs` primary Euroball source（DOI `10.1088/0954-3899/31/7/001`），读取 Tables 1–2、Fig.1、Figs.5–7 和 conclusion；确认 Bhat 使用同一 experiment 的 ratios，不是另一条独立数据线。
- 日报已建立：`outputs/learning-daily/20260929-DAY3-mean-field-nilsson-csm-hfb-projection.md`；当前仍是 checkpoint，`counted_in_substantive_test=false`。

## 后续最高信息增益路线

1. 对 Bhat arXiv v1 Table 1/Eq. (3) 与 PDF p.6 的约 `γ=30°` 文字冲突，查 DOI 期刊版/勘误；若不可取得，保留版本/参数边界。
2. 核验 Bhat Ref. [18] `126Cs` lifetime data 与 SIM05/BHA14 之间的独立性；不要把 theory comparison 另计为实验。
3. 若时间允许，查直接覆盖 Hara Table 5 `N=76/78` 核素的现代三轴投影计算；若没有，转到 `131Ce` measured `δ`/偏振、partner lifetimes 和 absolute strengths 的最小设计。
4. 每条续接都要先重建候选池并主动回忆，检查反证、必要 companion observable、来源独立性，并做一项可复算或最小设计练习。不要将 `130Cs` 或 `131Ce` 的模型结果跨核迁移。

## 收尾边界

- 15:00 Asia/Shanghai 起停止新增来源路线；留出一小时完成最终报告、knowledge writeback 校验、lint、`git diff --check`、回执、state-file 推进和次日提示。
- 未到正式 closeout 前保留 `next_day_index=3` 与 continuation 状态，不把模型结果升格为实验事实，不改 review status。
- 继承目录 `20260929-DAY3-mean-field-nilsson-csm-hfb-projection-run-01/` 和 Day 2 的 untracked raw bundle 保持原样；只显式暂存本日授权文件。
