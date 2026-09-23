---
type: system-workflow
graph-excluded: true
operation: continuous-learning
updated: 2026-09-05
---

# Continuous learning：90 天核结构专家型“硅基研究生”

## 适用范围与目标

本工作流是每日独立学习任务的操作契约，不替代
[`autonomous-research`](autonomous-research.md) 中的 L0–L4、P0/P1 和人工关口，
也不替代 [`ingest`](ingest.md)、[`reflect`](reflect.md) 或
[`scheduled-continuation`](scheduled-continuation.md) 的专门规则。

- 第一周期为 90 天：2026-09-05 至 2026-12-03；约 80% 用于核结构，约 20% 用于相邻核科学。
- A≈130 是研究锚点而非收录边界；选择来源时同时看质量区、机制、方法和证据价值。
- Wiki 保存可追溯的本体、实验判据、竞争解释、研究问题和失败经验；通用模型的背景知识不因本任务重复搬运而取代来源证据。
- 当前入口 corpus 是 15 篇学位论文（丁兵已有、Alwaleedi 复读、13 篇新增）及附加的 `103Pd` 实验报告；批次状态见 [`degree-dissertation-ingest-20260905`](../../outputs/degree-dissertation-ingest-20260905.md) 和 [`learning queue`](../learning-queue.md)。
- `PLAN.md` 仍由用户维护；每日任务不得改写、重排或机械扩展它。

## 来源阅读闭环

每篇实际使用的来源都完成“全文主线 + 关键证据深读”：问题/动机、方法、结果、讨论、结论，以及影响判断的图、表、公式、能级纲图、跃迁、模型参数、误差和限制。默认不逐篇通读全部参考文献；只有关键 claim、冲突或谱系判断需要时才回查。

source 页及其必要关联页至少记录：

1. `citation_key`、`raw_file`、哈希和阅读覆盖；
2. 可复核的 claim、locator、`claim_kind`、`evidence_level` 与 `source_independence`；
3. 支持证据、反证、竞争解释、适用条件、失败条件和缺失的必要伴随观测；
4. 一段 **Knowledge Impact and Learning Decision**，说明 supports、limits、revises、conflicts 或 no material change；
5. 在有依据时建立 source→核素/能带、source→实验/方法/模型、source→相关 source/project，以及目标页→source 的反向入口。

模型计算、作者解释、实验直接报告和本任务推断必须分层。原文歧义、图表不可读、元数据或 locator 不足时保留 `needs-human-review`，不补写确定性结论。

## 四阶段路线

| 阶段 | 周次 | 主要坐标 | 优先来源与里程碑 |
| --- | --- | --- | --- |
| 1. 专家框架 | 1–4 | 单粒子/壳结构/配对/平均场/形变；转动、振动、alignment、backbending、signature、K-isomer、shape coexistence、wobbling、chirality、γ-soft/γ-rigid、magnetic/antimagnetic rotation；A≈80/100/130/160/190、超形变和裂变同核异能态 | 丁兵、Alwaleedi、强赟华、车兴来、Smith、Sensharma；里程碑是跨质量区共同比较坐标和首轮 graph closure |
| 2. 实验谱学 | 5–8 | 熔合蒸发/裂变/碎片化/衰变布居；γ 符合、门条件、Doppler correction、DCO/ADO、角分布、线偏振、内转换、mixing ratio、RDDS/DSAM/fast timing/MSCD、寿命、`B(E2)`、`B(M1)`、`Q_t`、背景和 negative evidence | Régis、Dietrich、王华磊、Wang Enhong、Hinke、Lubos 及必要方法论文；里程碑是“观测量→证据→结构结论”判据矩阵 |
| 3. 广义核科学 | 9–11 | 核反应/衰变/质量/Q-value、β/GT/Fermi、质子滴线/rp-process、裂变/超形变/高-K/K-mixing；壳模型、CSM、TRS、TAC、PRM/QTR/TPSM、IBM/IBFM、CDFT、RPA、R-matrix、NEEC；探测器、电子学、数据分析和可复现计算 | Morgan、Hayes、Pálffy、陈思泽、Wang Enhong，并按覆盖缺口主动发现来源；里程碑是相邻领域桥接而不稀释核结构主线 |
| 4. 综合与研究判断 | 12–13 | 完成可读 corpus；至少三个主题 REFLECT；支持/限制/冲突/替代解释/独立性矩阵；跨质量区地图、实验判据矩阵、竞争解释矩阵 | 形成 2–4 个可检验研究问题或实验分析方向、90 天 research prospectus 和下一阶段候选池；L3 milestone 或 L4 candidate 遵守人工关口 |

阶段表是覆盖方向，不是每天的固定清单。阶段切换以里程碑和信息增益为准，不以论文数或主题数硬切换。

## 每日独立运行

### 调度与启动

每日 22:00（`Asia/Shanghai`）由 Docker 内的
`system/scripts/run_daily_learning_daemon.py` 触发。它只在 `/workspace/wiki`
内调用每日 runner，不使用宿主机任务计划、Docker socket、PowerShell 或外部
project cron。任务开始先读取：`README.md`、涉及选题时的 `PLAN.md`、
`system/handoff.md` 的 Active handoff、`profile.md`、`system/memory.md`、
`knowledge/index.md`、`system/log.md` 最近 10 条、[`learning queue`](../learning-queue.md)、
相关 workflow 和最近学习报告。不得读写 Codex 宿主 automation memory、global state、sandbox state 或 Wiki 外文件。

容器内启动与检查：

```bash
python3 system/scripts/run_daily_learning_daemon.py --root /workspace/wiki --dry-run
python3 system/scripts/run_daily_learning_daemon.py --root /workspace/wiki
```

容器启动入口会在后台拉起同一 daemon；`/tmp/wiki-one-month-daily-learning-daemon.lock`
防止重复实例，调度状态和简要事件写入 `outputs/learning-milestones/`。

### 动态学习循环

一次运行可以继续一个问题、切换问题或交替处理多个来源；不限制主题数量、不要求完成一个主题、不要求每天完成固定篇数。按以下循环推进：

1. 在打开大量证据页、下载或写入前，重建候选池：质量区/核素、机制或竞争解释、实验 observable、证据类型、独立性和 human-review 风险。
2. 选择一个或多个能改变当前判断的高价值问题；连续三篇直接相关来源，或新证据改变解释排序时，执行 thematic REFLECT。
3. 读取来源主线和关键证据，抽取 claim/locator/证据层级/不确定性，做必要的同位素与同中子素比较；物理上不适用或没有可靠证据时明确说明。
4. 建立 source-to-source 与 source-to-knowledge 双向链接，检查门条件、背景、分辨率、feeding、效率、响应和必要伴随观测。
5. 写回 source、关联页、问题页、当日记录和可恢复状态；必要时把开放问题去重后写入 `knowledge/questions.md`。

约 2 小时和 3 小时只做 checkpoint：记录已完成内容、剩余证据、当前信息增益、资源/验证余量，然后决定继续、切换或收敛。2–3 小时不是硬性停止时间；若仍有高信息增益且资源允许可继续，若边际收益下降可提前收敛。平台运行上限只允许用 handoff/continuation 分段，不能截断论文主线或把未读内容标成完成。

真正的停止条件是：达到当前主题里程碑；继续阅读的信息增益明显下降；关键来源、数据或 locator 缺失；权限、配额、资源或执行稳定性不足；或下一步需要用户科学判断/真实数据授权。停止时必须留下剩余 gap、依据、下一步和 continuation prompt。

## 选文献、独立性与互链

来源按可复用结构信息、关键实验判据、竞争解释/反证、新质量区或模型、对既有 project 判断的影响、独立实验价值和预期信息增益排序，而不是按数量排序。

- 同一实验的学位论文与期刊论文必须互链，但标记为 `multiple-dependent`，不得重复计数；重复引用不等于独立证据。
- 高相关 source 至少连接一个核素/能带、一个实验/方法/模型、一个相关 source 或 project，并提供反向入口；低相关来源可以 source-only，但要说明原因并连接适用背景/方法。
- 发现新来源后先核验题名、作者、年份、全文、哈希、重复关系和实验谱系；用户 PDF 只读。外部候选按 Nature-first 受控路径进入隔离区，禁止修改 `raw/zotero/wiki-inbox.bib`。
- 若主题的证据独立性、必要伴随观测或竞争解释仍不足，保持 provisional/`needs-human-review`，不把相似现象写成证明。

## 持久化产物

每日记录写入 [`outputs/learning-daily/`](../../outputs/learning-daily/)；实质记录至少包含：运行日期/时区、主题与候选池、每个问题的选择理由、来源指纹与重叠、checkpoint、关键 claim/locator/证据层、支持与反证、链接增量、Knowledge Impact and Learning Decision、开放问题、停止/续跑原因、L0–L4 状态和 Git/权限结果。可复用的知识增量必须写入 `knowledge/` 的 source、project、synthesis、question 或 research-note 页面；outputs 只保存日报、周报、审计、回执和运行状态。无实质新知时写短的 verified no-op receipt，不制造空提交。

每周写入 [`outputs/learning-weekly/`](../../outputs/learning-weekly/)：覆盖范围、互链缺口、反证、独立性、下一批候选和 belief revision；不以固定论文数达标。阶段报告、调度状态和运行回执写入 `outputs/learning-milestones/`；论文证据矩阵、研究地图和其它可复用知识写入 `knowledge/`。QMD 只在多篇完成、跨来源综合或明确需要时批量刷新；单篇完成可记录 deferred。

## Git–学习双轨与发布门

每次独立运行可先调用 `python3 system/scripts/wiki_automation_preflight.py --root .`，记录受保护 BibTeX 基线和工作树状态。这是终端 full-access 环境下的轻量诊断，不是额外的权限系统。

1. **本地检查通过**：按 `check.md` 建立 dirty baseline，显式暂存本轮允许文件，运行 lint/检查，必要时创建或 amend 唯一 rolling WIP。
2. **发布失败但内容安全**：继续 Wiki 内容和学习记录写回，状态记为 `content-complete / final-not-pushed`；不重复无变化的网络或认证诊断。
3. **内容安全失败**：停止新增科学 claim，按 safe-suspend 写回可恢复状态并等待用户判断。
4. 发布到 Gitee 前检查 remote ancestry，先 dry-run 再用同一精确 refspec 非 force push；不修改全局凭据、SSL 或其它项目。

允许写入的文件必须逐个列明；严禁 `git add .`，严禁把 PDF、raw、`raw/zotero/wiki-inbox.bib`、`.codex`、`PLAN.md` 或无关用户修改带入 stage。每日任务的本地 Git 发布仍受 `check.md` 完整清单和仓库现有 WIP/amend 规则约束。

## L0–L4 与人工关口

每日学习默认运行 L0–L2；当多个竞争解释、证据缺口或可检验课题满足条件时，可在报告中形成 `active-L3`、milestone、candidate 和 research prospectus。任何涉及真实用户数据、正式论文结论、`confidence: high` 或 L4 的动作都必须按 `autonomous-research` safe-suspend 并等待用户明确启动；自动任务不得越过数据授权关口，也不把自审写成人工审核。
