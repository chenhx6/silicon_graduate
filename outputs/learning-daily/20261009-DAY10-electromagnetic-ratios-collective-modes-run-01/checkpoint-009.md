---
type: learning-run-checkpoint
graph-excluded: true
created: 2026-10-10
run_id: 2026-10-09-day-10-01
checkpoint_id: checkpoint-009
---

# DAY10 checkpoint-009 — 可恢复状态

## 运行状态

- run.json status=running；day_index=10；session_id=01a11ffc-03bc-77e2-98ee-a227ea51f371；resume 命令不变。
- 当前实际时间：2026-10-10 11:33:56 Asia/Shanghai；hard deadline 15:00；约余 206 分钟。Decision=continue-current-or-partial。
- checkpoint-003 已在 run.json.observed_clock_executions 登记。本轮没有新建 session 或重启 daemon。
- course state next_day_index=10 / completed_day_count=9；日报 coverage completed_day_indices:[10]、partial_day_indices:[11]。Day11 仍 uncredited preview，Day12 未打开。

## 最新研究结论与证据层级

- 126Cs 三条实验/模型链已分开：Wang05 thesis 与 Wang06 PRC 共用 Komatsubara NORDBALL 数据；Wang06 提供 Table-I ADO/relative-intensity line table 和 branch-derived ratios；Grodner11 是不同 Warsaw/OSIRIS II DSA acquisition，报告 13 lifetimes/26 derived absolute B；Bhat14复用Grodner11数据。
- Wang06 I=14/15同母态 ratio 重算：yrast 1.41→5.08，side 2.61→3.05 μN²/(e²b²)，按 delta=0和独立强度误差传播；side 的 odd/even 交错较弱，与文中叙述一致。它不是绝对B、state-A或geometry测量。
- 126Cs 的 Wang05 Sec.4.3 M1 A-rule 转述与 Koike04/Hamamoto11 相反；Wang06只报告 ADO/比值交错而未分配实验 A。本轮没有理由用不同算符约定替任何来源化解文字矛盾。
- Prochniak11 的 CPHC S=PαCπν 是另一套量子数；Pα 不是空间宇称。Eq.(9)在 gR−(gπ+gν)/2=0 时抑制 same-s M1；A≈130输入给出残差−0.065，作者解释为 small but nonzero。S-symmetry可参与 M1 staggering，不能与Koike的A混为一谈。
- 134Pr PE06-2有branch-derived Q0,1/Q0,2=2.0(4)；Tonev07仍没有全文，公共机构PDF端点返回418。

## 刷新候选池与剩余信息增益

| 槽位 | 当前状态 | 剩余高价值缺口 |
|---|---|---|
| 135Nd continuity | MU07/ZH03/LV19 public scheme/transition crosswalk 已查；MU07-5/6/8/10/11/13/15/16、ZH03-3/4、LV19-9。 | 事件门、branch ledger、完整响应/协方差仍未公开。 |
| 128Cs model/experiment | Koike04/Hamamoto11 同一 A-symmetry 模型链；Koike03 Table VII 五条 line identity/DCO 与 GR06 Fig.4 部分 B marker map。 | 没有实验 A 标签；I=13 Y622/L622 重叠、I=15 limit；没有完整 interband absolute B/covariance。 |
| 126Cs selection-rule comparison | Wang05/Wang06同一NORDBALL数据；Grodner11独立DSA absolute-B；Prochniak11给出与A不同的S-symmetry；Wang06 Table-I ratios已复算。 | Wang05对Koike04的M1方向冲突未解；绝对B链没有实验A/s态标签。 |
| 134Pr counter | PE06-2给branch-derived Q0 ratio=2.0(4)；Hamamoto M1 violation仍是author-summary。Tonev07 repo PDF端点418。 | 无完整Tonev文本，不能核验具体M1 lines/依赖。 |
| Day11 preview | HE15-1与reaction entrance/CNR范围已有一条bounded preview。 | partial only，不给学分。 |

## 检查与待办

- 最近知识写入前 wiki_boundary_check.py exit 0。
- 最近 writeback locator audit：exit 0；单一机器块、26 items、anchors与atomic locators无错误、无non-atomic locator suspect。
- 最终 boundary、wiki_lint、git diff --check、dirty-baseline/stage审计、Gitee H3 与post-commit reconciliation仍待15:00 closeout。
- 下一高价值路线：核对公开Wiki中Prochniak11 S-symmetry的可用延伸/引文，避免把S和A混用；若无新增原始线级输入，继续保留现有边界。Day11仅partial/uncredited，Day12不打开。
