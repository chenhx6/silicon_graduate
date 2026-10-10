---
type: learning-run-checkpoint
graph-excluded: true
created: 2026-10-10
run_id: 2026-10-09-day-10-01
checkpoint_id: checkpoint-005
---

# DAY10 checkpoint-005 — 可恢复状态

## 运行状态

- run.json 首读仍为 running；day_index=10；session_id=01a11ffc-03bc-77e2-98ee-a227ea51f371。resume：codex resume 01a11ffc-03bc-77e2-98ee-a227ea51f371 -C /workspace/wiki -s danger-full-access -a never
- 当前实际时间：2026-10-10 06:54:38 Asia/Shanghai；hard deadline：15:00；约余 485 分钟。Decision=continue-current-or-partial。
- checkpoint-003 已在 run.json.observed_clock_executions 登记；未重复添加。没有新建 Codex session，也没有重启 daemon。
- 课程状态 next_day_index=10 / completed_day_count=9；日报仍是 completed_day_indices:[10]、partial_day_indices:[11]。Day11 仅 uncredited preview；Day12 未打开。

## 本轮来源与模型结果

- Hamamoto 2011 已有 source page；另核读 Koike, Starosta & Hamamoto 2004 PRL 93, 172502。Crossref 与 Tohoku record 5332 元数据一致，DOI 10.1103/PhysRevLett.93.172502；四页全文、Eqs.(1)–(10)、Figures 1–3 已读/查看，SHA-256 f39816a5d2f3f3ec45098fc636371ee3e8e4dc721b0ced33e7c87b453b7f155e。
- 两文采用同一 gamma=90°、同单-j 质子粒子/中子空穴与 A 对称的特殊粒子-转子模型。Koike 2004 明言规则对其 Hamiltonian 的本征态成立，不要求实际形成手征几何（KOIKE04-3/4/5）；故规则相容不能独立证明几何，2004/2011 不是两项独立实验/模型验证。
- 128Cs 的五条 side→yrast ΔI=1 links 已有 Koike 2003 Table VII 的线能、自旋、gate、DCO；Grodner 2006 Fig.4 只有 I=12/14/16 对 L532/L571/L639 的候选匹配，I=13 因 Y622/L622 重叠不唯一，I=15 为上限，I=11 无强度点。新 synthesis matrix 明确指出这还不是 A-rule 的逐线测试：无 A 本征态标签，且这些 interband links 没有完整 line-resolved absolute B 值/branch covariance。
- 134Pr 方向：现有 Petrache 2006 source 的 PE06-2 给 measured in/out E2 branches 派生的 Q0,1/Q0,2=2.0(4)，可定位到不等四极性质，但不复核 M1 selection-rule 违例。Tonev 2007 DOI 10.1103/PhysRevC.76.044313 的 Crossref 元数据核验；arXiv 查询无结果。Scholar 指向 University of Zagreb PDF，但机构 landing 与下载均返回 HTTP 418；HAL API 只有记录/摘要字段。未下载全文，也未把摘要当证据。
- 所有新增 source claims 仍 needs_review:true；source pages 保持 review_status:unreviewed。

## 刷新候选池与信息增益

| 槽位 | 当前定位与状态 | 剩余缺口 | 预期信息增益 |
|---|---|---|---|
| 135Nd continuity | MU07 与 ZH03/LV19 公开 scheme crosswalk 已饱和；MU07-5/6/8/10/11/13/15/16、ZH03-3/4、LV19-9。 | event/gate/branch ledger、response 和 joint covariance 不公开，不能唯一绑定 Fig.2–3 markers。 | 只有原始门控/支路/响应输入能改变归属。 |
| 128Cs novelty | Koike 2003、Grodner 2006、Chen 2017、Grodner 2018、Grodner 2011、Koike 2004、Hamamoto 2011 已分层。理论规则同源；五条 links 与部分 B marker 做了 crosswalk。 | A 不是观测标签；部分 B marker 无逐线绝对强度，DCO/混合类型不够检验模型不等式。 | 可继续核验可用公开表/figure，但不能用图像数值化补成 B 表。 |
| Counter-evidence | SU08 E2-denominator、MU08 crossing 与 PE06-2 branch-derived 134Pr Q0 ratio；Hamamoto 对 134Pr M1 违例仍是作者概述。 | Tonev 2007 全文路由 418；Koike 2004 是理论，不是 M1 新测量。 | 保留 access/line-level 边界；若有可访问原始 134Pr M1 source 再核对，否则不把二手概述升级。 |
| Day11 preview | HE15-1 等一个有界反应入口→prompt gamma 预习。 | 本次仅 partial/uncredited。 | 不扩为 Day11 全卡，不打开 Day12。 |

当前可继续的 Day10 高值问题：在不赋予实验态未经测量的 A 标签的前提下，哪些已发表 line-resolved B/δ 数据足以对 selection-rule consistency 作有限检验？下一步优先检查 Koike 2003 interband links 的混合/强度表边界与 2006 marker mapping；若仍无绝对逐线数据，记录 verified limit 后转到当前问题池的其它既有开放项。

## 新增 canonical 写回

- knowledge/sources/koike-2004-chiral-bands-selection-rules.md：A 对称规则、模型参数、规则不依赖实际手征几何的边界、参考数据谱系。
- knowledge/sources/hamamoto-2011-selection-rule-chiral-geometry.md：2011 重述与 128Cs/134Pr 作者比较。
- knowledge/synthesis/chirality-wobbling-competition-evidence.md：规则的理论非唯一性、134Pr PE06-2 来源边界和五条 128Cs link 的 A-rule 可检验性矩阵。
- knowledge/questions.md：模型规则离开 gamma=90°/同单-j 极限后的识别问题；已加入 Koike04/Petrache来源定位。
- knowledge/index.md：新增 Koike 2004 与 Hamamoto 2011 source entries。
- 报告仍只有一个 knowledge-writeback block；需要在 closeout 验证 anchors 与 atomic locators。

## 待收尾

- 研究硬截止 15:00；前置 boundary checks exit 0。最终还需跑 boundary、wiki_lint、git diff --check 并记录 exit codes/warnings。
- 之后精确计算 run-owned path list、检查 baseline overlap、cached diff、fetch origin/main、ancestor、dry-run/non-force push 和 post-commit reconciliation。不要 stage Day6–Day9 inherited files、daemon 改动、tmp PDF 或 PLAN.md。
