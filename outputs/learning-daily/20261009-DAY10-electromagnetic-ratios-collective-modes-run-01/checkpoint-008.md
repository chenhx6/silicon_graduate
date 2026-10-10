---
type: learning-run-checkpoint
graph-excluded: true
created: 2026-10-10
run_id: 2026-10-09-day-10-01
checkpoint_id: checkpoint-008
---

# DAY10 checkpoint-008 — 可恢复状态

## 运行状态

- run.json status=running；day_index=10；session_id=01a11ffc-03bc-77e2-98ee-a227ea51f371；resume 命令仍有效。
- 当前实际时间：2026-10-10 10:22:41 Asia/Shanghai；hard deadline 15:00；约余 277 分钟。Decision=continue-current-or-partial。
- checkpoint-003 已在 run.json.observed_clock_executions 登记。未新建 session、未重启 daemon。
- course state 仍 next_day_index=10 / completed_day_count=9；报告 coverage 保持 completed_day_indices:[10]、partial_day_indices:[11]。Day11 仅 uncredited preview，Day12 未打开。

## 当前证据与刷新候选池

| 槽位 | 当前证据/定位 | 仍缺什么 | 信息增益/下一步 |
|---|---|---|---|
| 135Nd continuity | MU07 与 ZH03/LV19 的公开 transition map 已查；MU07-5/6/8/10/11/13/15/16、ZH03-3/4、LV19-9。 | 事件门、branch ledger、response、joint covariance 仍不公开。 | 只有实测门控/响应输入能绑定其余图点；不再重复无新表格的公共 crosswalk。 |
| 128Cs model/experiment | Koike04/Hamamoto11 同一 A-symmetry 模型链；Koike03 Table VII 五条 line identity/DCO 与 GR06 Fig.4 部分 B marker map。 | 没有实验 A labels；I=13 Y622/L622 重叠、I=15 limit；没有完整 interband absolute B/covariance。 | 继续只做可行性/判据审计，不从比例或带标签推断 A。 |
| 126Cs 数据谱系 | Wang05 thesis 与 Wang06 PRC 共用 Komatsubara NORDBALL acquisition；Wang06 Table I 加线表/ADO与branch-derived ratios。I=14/15 table rederivation: yrast 1.41→5.08, side 2.61→3.05（KOIKE03-9；WS06-4/7/8）。Grodner11 是不同的 120Sn(10B,4n)/Warsaw OSIRIS II DSA campaign，13 lifetimes/26 absolute B；Bhat14复用Grodner11。 | Wang05 对 Koike04 的 M1 same-A/opposite-A 方向转述相反；Grodner11报告 M1 pattern/S-symmetry但不给state A labels，Fig.3 image不可得。 | 检查已存在的 Prochniak 2011 S-symmetry 理论来源是否能澄清规则层级；继续保留 source conflict。 |
| 134Pr counter | PE06-2 给 branch-derived Q0 ratio=2.0(4)；Hamamoto11 M1 violation仍是author-summary。Tonev07 repo PDF端点418。 | 无完整Tonev文本，不能核验具体M1 lines/依赖。 | 保留access boundary，不使用abstract。 |
| Day11 preview | HE15-1 与 reaction entrance/CNR范围已有一条有界preview。 | 仅partial/uncredited。 | 不做完整Day11，不开Day12。 |

## 新增知识结果

- Wang06 source page追溯到 arXiv nucl-ex/0702006v1、DOI 10.1103/PhysRevC.74.017302、PDF SHA-256 88e8cc5625493de58e5d7b2ee88318e49c44183db7e2613009e344538954f536。
- Wang06原文说明其新分析是 Komatsubara 1993 NORDBALL 数据再处理，与 Wang05 thesis 共用 acquisition，不是新的独立实验；Table I给线能/相对强度/ADO与自旋；本轮用Koike03 Eq.(7)对I=14/15同母态branch复算得比值趋势。
- 新增 Wang06 source-index entry、126Cs NORDBALL line/ratio synthesis 段、来源谱系 question 更新；所有 claim 保持 review_status:unreviewed/needs_review。
- Grodner11 DSA 是另一个绝对强度 acquisition；但它沿用 Wang06 的 multipolarity context。Bhat14的126Cs图为同一Gro dner2011数据模型比较，不能重复计数。

## 检查与待办

- 最近 wiki_boundary_check.py 在本轮知识写入前 exit 0。
- 最近 knowledge-writeback locator audit：exit 0；单一机器块、22 items、anchors与atomic locators无错误、无non-atomic locator suspect。
- 最终 boundary、wiki_lint、git diff --check、状态/dirty-baseline对照、精确path stage、Gitee H3与post-commit reconciliation仍待15:00 closeout。
- 下一条可尝试路线是查 Wiki 是否已有 Prochniak 2011 S-symmetry source card；若没有，再基于公开/可访问全文评估是否能解释“规则来自A对称还是额外S对称”这一层。DAY11仍只保留uncredited preview，Day12不打开。
