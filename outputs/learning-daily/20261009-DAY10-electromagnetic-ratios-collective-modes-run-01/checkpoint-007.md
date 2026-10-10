---
type: learning-run-checkpoint
graph-excluded: true
created: 2026-10-10
run_id: 2026-10-09-day-10-01
checkpoint_id: checkpoint-007
---

# DAY10 checkpoint-007 — 可恢复状态

## 运行状态

- run.json status=running；day_index=10；session_id=01a11ffc-03bc-77e2-98ee-a227ea51f371；resume 命令未变。
- 当前实际时间：2026-10-10 08:54:15 Asia/Shanghai；hard deadline 15:00；约余 365 分钟。Decision=continue-current-or-partial。
- checkpoint-003 已在 run.json.observed_clock_executions 登记。本轮未创建新 session、未重启 daemon。
- course state 仍 next_day_index=10 / completed_day_count=9。日报行 completed_day_indices:[10]、partial_day_indices:[11]；Day11 仍 uncredited preview，Day12 未打开。

## 候选池与证据缺口

| 槽位 | 当前证据 | 未解决边界 | 下一信息增益 |
|---|---|---|---|
| 135Nd continuity | MU07/ZH03/LV19 public scheme/transition crosswalk 已查；MU07-5/6/8/10/11/13/15/16, ZH03-3/4, LV19-9。 | 无 event/gate/branch ledger、完整响应或 joint covariance，不能绑定所有 interband B 图点。 | 只有原始实验门控和响应/协方差输入能改判。 |
| Cs selection-rule comparison | Koike 2004/Hamamoto 2011 同一 A-symmetry 模型链；Koike 2004 明言规则不要求非共面几何。128Cs 五条线的 B-marker mapping 仍部分；126Cs 新增 Grodner 2011 DSA 主实验：13 lifetimes/26 B values，Fig.3 作者报告 interband/inband M1 opposite-phase staggering。 | 126Cs Wang thesis Sec4.3 对 Koike04 M1 same-A/opposite-A 方向写反；Grodner11支持作者规则图景但无逐态 A 标签。其Fig3图像不可得，未读像素。Bhat14重用GR126，不计独立实验。 | 回查 Wang 2006 cited transition/multipolarity source，厘清 level-line provenance；保持 M1-paraphrase conflict 未解决。 |
| 126Cs independent-chain comparison | Wang 2005 NORDBALL 116Cd(14N,4n) ratios，Grodner 2011 Warsaw 120Sn(10B,4n) DSA absolute strengths，两套 acquisition 条件不同；Grodner 引 Wang06作 pure-M1/multipolarity context。 | thesis 的 selection-rule paraphrase WS05-7 与 Koike04-4 相反；两个来源的 line-level A mapping未建立。 | 核读 Wang06 Ref[12] 后确认它只是 multipolarity context还是含有新的线级结果。 |
| 134Pr counter | PE06-2 branch-derived Q0 ratio 2.0(4); Hamamoto M1 violation remains author summary. Tonev 2007 direct PDF path returned 418. | Tonev full text not accessible by checked public routes; no abstract used. | Keep the M1 claim provisional. |
| Day11 preview | HE15-1 + reaction entrance/CNR scope preview already recorded. | partial only, no course credit. | Do not expand to full card or open Day12. |

## New primary source and source conflict

- Added knowledge/sources/grodner-2011-126cs-chiral-selection-rules.md from public INSPIRE Elsevier XML, record 930155, DOI 10.1016/j.physletb.2011.07.062, CC BY 3.0, XML SHA-256 dfc649e43493debee93c4d9e76694360972f82382ce0b25a04945b7a766b728c. The paper reports a separate DSA experiment (120Sn+10B, Warsaw/OSIRIS II) with 13 lifetimes and 26 derived absolute transition probabilities.
- It reports opposite-phase inband/interband B(M1) staggering and interprets it using Koike04’s selection-rule framework plus an additional S-symmetry. It explicitly warns M1 staggering is not due to chirality alone.
- Bhat14 Ref[18] is this same measurement. Wang05’s NORDBALL experiment is a different reaction/array; Grodner11 also cites Wang06 for transition/multipolarity context.
- The Wang05 thesis’s printed p.123 / PDF p.133 paraphrase says same-A M1 is favored/opposite-A forbidden. Koike04 Eq.(6), and Hamamoto11 Eq.(7), give the reverse relative M1 strength. The mismatch is stored as WS05-7 and an open question; no label convention or typo is assumed.
- The accessible INSPIRE XML has table values/captions but not Figure3 pixels; no values were digitized. The direct publisher HTML/PDF and figure image endpoints returned 403/404; CC BY full text was read from INSPIRE.

## Checks and next action

- wiki_boundary_check.py before the latest canonical update: exit 0.
- Report knowledge-writeback validation: exactly one block; 20 items; all anchors and atomic source locators found; zero non-atomic suspects.
- Final boundary, wiki_lint, git diff --check, exact baseline/stage audit, Gitee H3 and post-commit reconciliation remain for 15:00 closeout.
- Next source route: Wang et al. 2006, PRC 74, 017302 (cited by Grodner11 as Ref[12]) through bounded public/institutional lookup. If unavailable, use the already deep-read Wang05 thesis boundary; do not claim source independence beyond the two reaction/array records.
