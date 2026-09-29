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
- 对 Bhat Ref. [18] `126Cs` primary lifetime article（DOI `10.1016/j.physletb.2011.07.062`）做了 OA 路由检查：ScienceDirect PDF 与 OpenAIRE resolver 均 HTTP 403，arXiv exact-title 搜索为 0；没有读取或导入该文。
- 视觉核对 Hara Table 5 (PDF p.712) 与 p.713 说明：七个星号核素为 `133La` (N=76)、`134La` (N=77)、`135Ce` (N=77)、`135Pr` (N=76)、`136Pr` (N=77)、`137Pr` (N=78)、`137Nd` (N=77)。p.713 把 N=76/78 说成形状转变端点，并要求三轴投影代码确认中间核素。
- 通过合法 arXiv OA 获取 Sheikh, Jehangir & Bhat 2024（arXiv `2405.08368v1`；书章 DOI `10.1201/9781032691633-12`），SHA-256 `a7fa3cc75113a1ff2881cbc7edd9d3285a228b429c34b6f0b9b22da4c2b90d22`。全文及 Table 1、Figs. 11–14 核对显示该 TPSM 计算覆盖 `133La`、`135Pr` 两例；固定输入 `γ=36°/32°`，实验曲线沿用旧实验，不能作独立形状测量。新建 source page 并更新 Hara source、TPSM model/card、`131Ce` project 和 index。
- 发现 2026 IJMPE DOI `10.1142/S0218301326500448`；Crossref/OpenAlex/Semantic Scholar 元数据一致，但 OpenAlex 标记 closed/no repository full text，World Scientific 返回 403，arXiv 精确题名无命中，OA downloader 返回 `oa_not_found`。只记身份与访问状态，不用摘要作科学证据，不重试相同端点。
- 日报已建立：`outputs/learning-daily/20260929-DAY3-mean-field-nilsson-csm-hfb-projection.md`；当前仍是 checkpoint，`counted_in_substantive_test=false`。

## 后续最高信息增益路线

1. 为 `131Ce` 设计最小可判别观测包：固定目标带与连接跃迁清单，排序 mixing-ratio/偏振、伙伴带 lifetime、absolute `B(E2)/B(M1)`/`Q_t` 的测量顺序，并说明各自如何区分配置耦合、γ-soft、wobbling 与 chirality。
2. 如有新信息增益，再查 Hara Table 5 其余五个星号核素 `134La`、`135Ce`、`136Pr`、`137Pr`、`137Nd` 的直接三轴投影计算；不要复用已失败的 2026 DOI/arXiv/出版社端点，不把邻核输出迁移到 `131Ce`。
3. Bhat arXiv v1 Table 1/Eq. (3) 与 p.6 约 `γ=30°` 文字冲突仍开放；只有在发现新的合法最终版/勘误路径时才查，保持 `needs_review`。
4. 每条续接都先重建候选池并主动回忆，检查反证、必要 companion observable、来源独立性，并做一项定量或最小设计练习。用户已说明常规全文/SI 获取不必逐次询问；仍只用合法公开或已配置授权路径。

## 收尾边界

- 15:00 Asia/Shanghai 起停止新增来源路线；留出一小时完成最终报告、knowledge writeback 校验、lint、`git diff --check`、回执、state-file 推进和次日提示。
- 未到正式 closeout 前保留 `next_day_index=3` 与 continuation 状态，不把模型结果升格为实验事实，不改 review status。
- Farmer 守护进程正常；本轮 dry-run 无 pending recovery。继承目录 `20260929-DAY3-mean-field-nilsson-csm-hfb-projection-run-01/` 与 Day 2 raw bundle 保持原样；Day 3 新 PDF 仅留本地 raw，不暂存。
- 当前提交目标为 `Record 2024 TPSM coverage of Hara Table 5 nuclei`；需重跑 writeback validator、boundary、lint、`git diff --check`，仅显式暂存本轮知识页、日报、续接/回执、handoff 和 log，然后按 Gitee H3 发布。最终检查与 push 结果尚待写回。
