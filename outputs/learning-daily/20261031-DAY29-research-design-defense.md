---
type: output
graph-excluded: true
created: 2026-10-31
updated: 2026-10-31
---

# Day29：131Xe 研究设计答辩

## Run state

- run_id: `2026-10-31-day-29-01`
- prompt_run_id: `prompt-2026-10-31-day-29`
- day_index: 29
- session_id: `01a191e7-29f8-79f2-8276-9a88282a4ed5`
- resume_command: `codex resume 01a191e7-29f8-79f2-8276-9a88282a4ed5 -C /workspace/wiki -s danger-full-access -a never`
- timezone: Asia/Shanghai
- overnight_until: `2026-11-01T15:00:00+08:00`
- closeout_window_ends_at: `2026-11-01T16:00:00+08:00`
- runtime_snapshot_at_start: `2026-10-31T20:19:43.035873+08:00`
- completed_day_indices: [29]
- partial_day_indices: []
- next_day_index: 30
- research_status: completed
- Day 29 card audit: complete
- scientific_state: provisional-l3-readiness
- human_review: none; Codex self-audit only
- audit_integration_status: complete
- day29_credit_status: complete
- credit_transition_applied: true

Day29 课程要求的研究设计已完成。`131Xe` 的 2020 与 2023 论文被确认属于同一 INGA 原始采集谱系；因此本日没有把版本差异计为独立实验。研究结论停在可执行的 L3/readiness 合同，未生成事件级 L4、代理计数、显著性或人工审核状态。

### Day 29 card completion audit

| Day29 deliverable | Status | Evidence artifact | Evidence locator |
|---|---|---|---|
| 最小 observable、对象身份与 source lineage | complete | `knowledge/research-notes/131xe-day29-research-design-defense.md` | `## Source lineage and object identity`; `## Minimal observable contract` |
| 794-keV 宇称版本实验/分析方案 | complete | Day29 research note | `### A. 794-keV宇称块`; `794-keV` target/control rows |
| 882-keV 双根的角分布、DCO、偏振与污染响应 | complete | Day29 research note；既有 response contract | `### B. 882-keV双根块`; `knowledge/research-notes/131xe-882-branch-response-contract.md` |
| 共享校准、deadtime、feeding、sideband、random 与联合协方差 | complete | Day29 research note | `### C. Shared calibration and joint covariance`; `## Analysis sequence` |
| 三种结果情形、belief revision 与 L3/L4 停止边界 | complete | Day29 research note | `## Three outcome scenarios and belief revision`; `## L3/readiness boundary` |

## Candidate pool and selection

| Route | Decision | Reason |
|---|---|---|
| `131Xe` 794-keV宇称版本 | active and completed as design | 直接承接 Day28 的版本冲突，新增观测可明确写成 ICC/电子响应合同 |
| `131Xe` 882-keV双根 | active and completed as design | 已有 `R_DCO=0.64(11)` 与双解边界，最小新增输入是逐门峰形、真实角对和偏振响应 |
| Irving/Lönnroth 1979/1983 primary recovery | stopped at current boundary | 已核对 NNDC 书目与实验覆盖；IOP PDF 端点落到 Radware CAPTCHA，CORE/OA-only 未取得全文，不能把失败端点当成物理不可得，保留 readiness boundary |
| `135Pr` event-level response/Cov | deferred | 缺 event-level counts、response 和 overlap；与本日 131Xe 设计不重叠，但不能凭公开图表运行 L4 |
| `135Nd/134Pr` producer ledger | deferred | 需要 producer-level transition identity、feeding 和 covariance；保留同源性分层 |
| 八极 source-page audit | deferred | `90Zr` joint covariance/producer 输入仍缺；不做 pooled mean 或静态梨形裁决 |
| 全库 claim/path audit | performed as read-only guard | 只检查重复证据与写回位置，没有移动、删除或覆盖 raw |

## Evidence synthesis

### Primary recovery and locator audit

`Irving 1979` 已核对为 A. D. Irving et al., *J. Phys. G* 5, 1595, DOI `10.1088/0305-4616/5/11/015`；`Lönnroth 1983` 已核对为 T. Lönnroth et al., *Phys. Scr.* 27, 228–240, DOI `10.1088/0031-8949/27/4/002`。NNDC 引用页确认两项历史来源分别覆盖能级、角分布、偏振或内转换等实验字段，但本轮 IOP PDF 请求落到 Radware bot-manager CAPTCHA，CORE 与 OA-only 检索没有返回可核原文。因此不能把 1979/1983 的目标线逐行 AD、ICC 或偏振数值写成已复核 primary。

本地两份核心原件仍可直接回链：Banik 2020 `10.1103/PhysRevC.101.044306` 的 Table I/ Fig.4/ footnote k 给出 794.8-keV E1 版本及 880.9/881.2 近邻；Chakraborty 2023 `10.1103/PhysRevC.107.064318`（arXiv `2311.09713`）的 Sec. III、Fig.2 和 Table I 区分 880.1/881.8 双峰，并给出 881.8 的 `R_DCO=0.64(11)`。2023 明确是 2020 INGA 数据的重分析，同一采集不能重复计权。ENSDF A=131 adopted PDF 和 BrIcc 只提供评价/理论响应，不是新的实验来源。

### 794-keV宇称版本

将 2020 版本写为 `1600.9(2) keV, 17/2+ → 15/2−`、794.8-keV E1，并将 2023 版本写为同一节点的 `17/2−` 标签，作为两个待检假设。目标测量是同一对象和门条件下的 K 壳电子与 γ 联合计数：

\[
r_K^{\rm obs}=N_{K,e}^{\rm net}/N_{\gamma}^{\rm net}=\kappa_K\alpha_K.
\]

`κ_K` 必须包含电子/γ效率、几何接受、门条件、deadtime/livetime 和背景模型。E1 的纯 ICC 与 M1/E2 混合 ICC 只能作为前向理论响应，统一 `Z=54`、能量、壳层、FO/NH 和 BrIcc 版本，并把理论共同误差放进 profile。历史 `EKC=0.0017(7)` 仍没有原始电子计数、归一和误差语义闭合，不能单独裁决宇称。

### 882-keV双根

把 `881.8-keV` 目标线作为 `1046.0-keV, 13/2− → 11/2−` 的 M1/E2 候选，把 `880.1-keV` 近邻作为显式污染列。逐门保留峰形、sideband、random、峰位漂移、实际晶体/角对和级联顺序；对同一 `1046-keV` 母态保留取向、feeding 和退取向 nuisance。DCO/角分布与 Compton 平行/垂直或完整方位角 scatter-bin 联合拟合，不能从一个总不对称量或名义探测角直接选根。

线性 M1/E2 响应可写成：

\[
q_i(\delta,\eta)=\frac{a_i(\eta)+2b_i(\eta)\delta+c_i(\eta)\delta^2}{1+\delta^2},
\qquad
\mu_i=Y_gq_i+B_i+\lambda_gT_{880,i}.
\]

系数必须由真实有限几何、取向/feeding、效率、相位约定和 detector response 积分得到。若输入是压缩的 `R_DCO`、偏振不对称或 `EKC`，必须提供它们与共享校准的联合 `Σ`；原始计数和派生比值不能重复进入似然。

### 控制线和共享 nuisance

- `642-keV` 已知 E2：检查角度接受与取向传播。
- 2020 反复用作 E1 参照的约 795-keV线：检查电子/γ归一；不能替代 794 目标的宇称测量。
- `704.6-keV` 同母态竞争退激：约束 1046-keV 条件取向；不能强制作为 882 互符合门。
- `816/930-keV` 上游门、663-keV控制门、能量 sideband 和 prompt/random：检查级联身份、背景和偶然符合。
- 无偏振源和空门：检查 Compton 轴符号、串扰、阈值和背景。

共享校准参数包括能量/分辨、全能峰效率、K 电子传输、有限几何、Compton `Q_eff` 或 Stokes 响应、deadtime/livetime、run overlap、feeding/alignment、sideband/random 缩放和 BrIcc 理论误差。共享事件、共享校准线和同一 INGA acquisition 的协方差必须保留。

## Three result scenarios

| 结果 | belief revision | 允许表述 |
|---|---|---|
| 794 电子/γ比与 E1 预测分离，且 882 两分支在共同 profile 与留出门中稳定分离 | 下调另一宇称版本或双根简并，提升指定分支支持 | 只能说在声明的响应/理论合同内排除候选 |
| 794 与 M1/E2 ICC 凸包重叠，或 882 两分支 profile 仍交叠 | 宇称与 δ 双根保持未决 | 数据对当前设计不足以裁决 |
| 880 污染、alignment/feeding、轴符号、deadtime 或共同校准吸收差异 | 先修订对象/门/响应身份，再讨论结构机制 | 不把响应失败写成 wobbling 或 signature-partner 新证据 |

## Hard boundary

以下缺失会把任务停在 L3/readiness：794 目标电子/γ原始计数与共同效率；881.8/880.1逐门峰形；真实 detector-pair/Compton response；1046-keV alignment/feeding；deadtime、random、sideband和acquisition overlap；完整联合协方差；以及目标线的 primary provenance。不得用代理计数、合成 response、出版图像的视觉交点或评估字段生成 L4 似然、Bayes factor、排除σ、全局 mixing-ratio CI 或结构认证。

## Dispatched audits

- `McClintock`：primary/source recovery；完成 Irving/Lönnroth 书目、访问失败边界、794/880/881/766/704/815/930 locator 和同源性审计。
- `Volta`：794 方案；确认 E1 与 M1/E2 两假设、K-electron/γ 最小观测与 profile 边界。
- `Kepler`：882 响应合同；确认 880.1 污染、真实角对、偏振响应、feeding/alignment 和 raw-count likelihood 要求。
- `Dirac`：全库 lineage/path audit；完成同源性、版本重复、review-scope、source→raw 缺口和账本漂移检查；本轮只修正 Day29 自身回执字段，没有批量改 canonical 页面。

## Continuation checkpoint

- 对 `135Pr` 的四个本地 primary PDF 做了只读 SHA-256 对账：Matta 2015、Sensharma 2019、Lv 2022 和 Sensharma 2026 均与对应 source 页的 `raw_sha256` 一致。
- 该新增结果只闭合 source identity；它没有闭合 event/run overlap、跨阵列 response 等价性、联合 `Σ`、独立 holdout 或原始 counts，因此 `135Pr` 仍停在 L3 public-summary/readiness boundary。
- `135Pr` source-to-raw 与 observable lineage ledger 已写入 `knowledge/research-notes/135pr-common-response-evidence-contract-20261031.md`，并同步更新 prospectus；Day29 学分保持不变，Day30 仍未计分。
- P3 `135Nd/134Pr` 只读复核未产生新写回：`MU07-11` 仍是 state-level `τ/B`，`TO07-D24-001/002/003` 仍是更完整但含未分解混合线的逐线控制，`TO07-D24-007` 保持 Tonev06/07 同谱系边界；缺 producer、feeding、response 和 joint covariance，停在 L3 identity audit。
- P4 `90Zr` 2024/2026 方法分离复核为 verified-no-op：已有 note 的 `16(3)` 与 `19.6^{+1.7}_{-1.6}` W.u. 条件差异复算为约 `1.04–1.06σ`，但缺跨方法 producer、feeding 对齐和 joint covariance，不能 pooled 或升级为静态八极结论。

## Knowledge writeback

```yaml
knowledge-writeback:
  status: complete
  writeback_valid: true
  items:
    - knowledge: knowledge/research-notes/131xe-day29-research-design-defense.md
      anchor: "Minimal observable contract; Three outcome scenarios and belief revision; L3/readiness boundary"
      sources:
        - path: knowledge/sources/banik-2020-131xe-multiple-band-structures.md
          locator: "BNK20-D28-2/3; BNK20-D28-3; BNK20-D28-1"
        - path: knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md
          locator: "C23-1..C23-7; C23-D28-2; C23-D28-9"
        - path: knowledge/research-notes/131xe-882-branch-response-contract.md
          locator: "C23-D28-9; joint response equations"
        - path: knowledge/research-notes/131xe-1601-parity-version-boundary.md
          locator: "ICC/ENSDF boundary; BrIcc nominal envelope"
      changed_paths:
        - knowledge/research-notes/131xe-day29-research-design-defense.md
        - knowledge/index.md
      writeback_valid: true
    - knowledge: knowledge/projects/131xe-low-spin-partner-crosswalk.md
      anchor: "existing object crosswalk and unresolved 794/882 boundary"
      sources:
        - path: knowledge/research-notes/131xe-day29-research-design-defense.md
          locator: "Source lineage and object identity"
      changed_paths: []
      writeback_valid: true
    - knowledge: knowledge/projects/131xe-low-spin-partner-crosswalk.md
      anchor: "Day29 formal design link under Minimal Design, Falsifier and Belief Revision"
      sources:
        - path: knowledge/research-notes/131xe-day29-research-design-defense.md
          locator: "Source lineage and object identity"
      changed_paths:
        - knowledge/projects/131xe-low-spin-partner-crosswalk.md
      writeback_valid: true
    - knowledge: knowledge/sources/banik-2020-131xe-multiple-band-structures.md
      anchor: "lineage_id and primary-analysis metadata"
      sources:
        - path: knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md
          locator: "same INGA acquisition and dependent reanalysis"
      changed_paths:
        - knowledge/sources/banik-2020-131xe-multiple-band-structures.md
      writeback_valid: true
    - knowledge: knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md
      anchor: "lineage_id, dependent-reanalysis and journal/arXiv version metadata"
      sources:
        - path: knowledge/sources/banik-2020-131xe-multiple-band-structures.md
          locator: "same INGA acquisition anchor"
      changed_paths:
        - knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md
      writeback_valid: true
    - knowledge: knowledge/nuclei/131xe.md
      anchor: "Sources"
      sources:
        - path: knowledge/sources/banik-2020-131xe-multiple-band-structures.md
          locator: "same-acquisition primary analysis"
        - path: knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md
          locator: "dependent reanalysis"
      changed_paths:
        - knowledge/nuclei/131xe.md
        - knowledge/experiments/vecc-131xe-alpha-38mev.md
        - knowledge/bands/131xe-nu-h11-2-favored-sequence.md
      writeback_valid: true
    - knowledge: knowledge/research-notes/135pr-common-response-evidence-contract-20261031.md
      anchor: "Source-to-raw reconciliation and observable lineage ledger"
      sources:
        - path: knowledge/sources/matta-2015-transverse-wobbling-135pr.md
          locator: "M15-16"
        - path: knowledge/sources/sensharma-2019-two-phonon-wobbling-135pr.md
          locator: "S19-D23-1"
        - path: knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md
          locator: "L22-16"
        - path: knowledge/sources/sensharma-2026-evolution-chirality-transverse-wobbling-135pr.md
          locator: "SH26-15"
      changed_paths:
        - knowledge/research-notes/135pr-common-response-evidence-contract-20261031.md
        - outputs/learning-daily/20261031-DAY29-research-design-defense-run-01/135pr-source-raw-reconciliation.json
      writeback_valid: true
    - knowledge: knowledge/projects/post-30-day-nuclear-structure-paper-prospectus.md
      anchor: "Candidate 1: 135Pr source-to-raw reconciliation and dependent-lineage boundary"
      sources:
        - path: knowledge/research-notes/135pr-common-response-evidence-contract-20261031.md
          locator: "Source-to-raw reconciliation and observable lineage ledger"
        - path: knowledge/sources/sensharma-2019-two-phonon-wobbling-135pr.md
          locator: "S19-D23-1"
        - path: knowledge/sources/sensharma-2026-evolution-chirality-transverse-wobbling-135pr.md
          locator: "SH26-15"
      changed_paths:
        - knowledge/projects/post-30-day-nuclear-structure-paper-prospectus.md
      writeback_valid: true
  verified_no_op:
    - "No raw file, PLAN.md, 131Xe canonical page or curriculum state was modified; event-level overlap and common-response inputs remain unresolved."
    - "P3 135Nd/134Pr read-only audit added no durable fact beyond the existing identity ledger; no line-level conversion, pooled fit or mechanism ranking was performed."
    - "P4 90Zr method-separated E3 arithmetic reproduced the existing conditional 1.04–1.06 sigma comparison; no new source, pooled estimate or static-shape claim was added."
```

## Artifacts and continuation

- 正式知识写回：`knowledge/research-notes/131xe-day29-research-design-defense.md`
- `135Pr` source→raw 对账：`outputs/learning-daily/20261031-DAY29-research-design-defense-run-01/135pr-source-raw-reconciliation.json`
- `135Pr` 共同响应合同：`knowledge/research-notes/135pr-common-response-evidence-contract-20261031.md`
- 承接项目：`knowledge/projects/131xe-low-spin-partner-crosswalk.md`
- 既有设计合同：`knowledge/research-notes/131xe-882-branch-response-contract.md`
- 宇称边界：`knowledge/research-notes/131xe-1601-parity-version-boundary.md`
- 下一次恢复命令：`codex resume 01a191e7-29f8-79f2-8276-9a88282a4ed5 -C /workspace/wiki -s danger-full-access -a never`

## Self-audit

- `wiki_lint.py --fail-on error`: exit `0`, `0 errors / 437 warnings / 5224 info`.
- `wiki_boundary_check.py --root .`: exit `0`; `git diff --check`: exit `0`.
- No raw files were changed, moved, deleted or overwritten.
- No `PLAN.md` or curriculum prompt was modified.
- No synthetic counts, response matrices, holdout data or event-level L4 results were created.
- Source claims remain separated into experimental report, author interpretation, model response and current-task inference.
- Review status remains `unreviewed`; this is not human review.
