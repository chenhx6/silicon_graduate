---
type: system-workflow
graph-excluded: true
operation: ingest-strategies-detail
updated: 2026-07-07
---

# INGEST STRATEGIES DETAIL：详细教程与扩展示例

本文件为 `system/workflows/ingest.md` 提供详细策略背景。策略是读取与写回范围的约束，不是必须填满的抽取清单；只记录文中实际存在且能够定位的信息。
本文件保留拆分前的详细说明、长解释和示例。普通单篇摄入默认读取短规则 [ingest-strategies.md](ingest-strategies.md)，只有用户要求解释策略、修改 workflow、复杂多篇摄入、短规则不足以判断、要求 detailed recap / detailed strategy audit，或明确要求查阅详细教程时才读取本文件。

## Global ingest rules

所有策略共同遵守：

1. 只记录文中实际存在的信息，不为填满清单而编造或推断未报告的数据。
2. 每条 claim 尽量给出精确 locator，例如 page、section、figure、table、level scheme、spectrum、equation 或具体段落。
3. 需要人工核对的 claim 保留 `needs_review: true`。
4. 页面级 `human-reviewed` 与 claim-level `needs_review` 独立。
5. 不把作者解释写成观测事实，不把模型结果写成实验事实。
6. 不把综述转述写成原始证据。
7. 不把非目标质量区文献写成目标质量区的直接证据。
8. 不修改 raw PDF、论文、数据或图片。
9. 不修改 `raw/zotero/wiki-inbox.bib`，除非用户明确要求。
10. 不新增 Skill、automation、脚本或调度器。
11. 普通摄入不修改 lint 脚本、lint 配置或测试；若认为必须修改，停止并询问用户。
12. 普通文献摄入在长任务、未完成、等待审核或存在 hard P0 时创建本地 WIP ingest commit并暂不 push；完成发布门后按持续授权自动 push，完整规则见下节。
13. 摄入后列出新增 claims、`needs_review` claims、证据缺口和建议人工审阅的文件。
14. 按 `AGENTS.md` 的 bounded initiative 只做直接相关的最小同步；有帮助但非必要的修改只列为建议。
15. 单篇文献的新术语或别名优先写入页面 `aliases`。只有需要跨库统一、存在歧义或重复 slug/aliases 风险，或用户明确要求时，才修改 `system/vocabulary.md`；不确定时先询问或只列建议。
16. 文献摄入、project、synthesis、data-analysis-bridge 和 claim-review-update 完成后，按下述 Human review triage 对审核点排序；不得把所有 `needs_review` 等权重铺开。

## Human review triage protocol

本节提供分类示例和详细说明；P0/P1/P2/P3 的运行时输出与批次规则以 [ingest-strategies.md](ingest-strategies.md) 为 canonical owner。若本节示例与短规则冲突，以短规则为准。

审核优先级描述“用户应先审哪里”，与页面级 `review_status` 和 claim-level `needs_review` 分别维护。`needs_review: true` 不自动等于 P0；优先级应由该项对科学结论、证据链、project/synthesis 主线和论文级使用的影响决定。

### P0：必须审核

P0 未审核前，不建议把对应 WIP amend 为 final commit 或 push。P0 包括：

- 影响科学结论、project/synthesis 主线或 paper evidence gate 的核心 claim 或段落；
- high-risk observed fact、experimental criterion、model result 或 author interpretation；
- wobbling、TiP、chiral doublet、signature partner、gamma-soft deformation、triaxiality 等核心解释判断；
- transition、band、spin/parity、multipolarity、mixing ratio 指认；
- DCO/ADO、angular distribution/correlation、linear polarization、lifetime、`B(E2)`、`B(M1)`、跨带/带内强度比、wobbling energy、quadrupole moment 或 moment of inertia 等关键判据和数值；
- 公式、图表、数值或 locator 不确定但支撑核心结论的位置；
- observed fact、model result、author interpretation 与 Wiki synthesis 可能混写的位置；
- 用户数据被写成 possible interpretation、competing interpretation、innovation candidate 或 paper-level candidate 的位置；
- 与已有 source/project 冲突、反驳或重解释的位置；
- synthesis 中可能被误读为最终裁决的段落。

每个 P0 必须给出：文件、section/位置、claim ID（如有）、source locator、为什么是 P0、用户具体要检查什么，以及不审核的风险。

### P1：优先审核

P1 有时间应优先审核，但不必阻塞所有后续工作。P1 包括：

- source 页关键 claims、project evidence matrix、supporting/counter/alternative evidence notes；
- model assumptions、experimental criteria 和 synthesis 的跨来源总结；
- 新建 concept/model/observable 页的定义、边界与 aliases；
- 与现有 project 新建立的 source 关系；
- 会影响后续 query 的术语归一化或 aliases；
- 轻量 project seed 的 research question、scope 与 evidence gaps；
- 指向 `135Pr`、`187Au`、TiP、gamma-soft 或 low-spin wobbling 等核心 project 的交叉关系。

每个 P1 必须给出：文件、section/段落、claim ID（如有）、source locator（如有）、为什么是 P1，以及用户需要检查什么。

### P2：可抽查

P2 建议按文件聚合抽查，包括背景 claims、source summary、章节/主题地图、follow-up sources、evidence gaps、next actions、非核心 concept/model/observable 小补充、project planning notes、synthesis 非核心背景、seed source 列表和低风险 relation/future extension。应说明抽查重点，不逐条铺开。

### P3：快速扫过

P3 通常只需快速扫过，包括 index、overview、handoff、log、普通反链、普通 aliases 小补、格式、非科学导航以及 lint/check 结果记录。

若 aliases、术语或导航涉及高歧义边界，例如 shell model/CSM/PSM/TPSM、angular distribution/angular correlation、gate/开门/拉门/开窗、wobbling/TiP/precession 或 gamma-soft/gamma-rigid/triaxiality，应提升为 P1，不按普通 P3 处理。

### 最终复盘格式

相关任务的最终复盘必须包含：

```text
Human review triage

P0 必须审核：
1. 文件：
   - 位置：
   - claim ID / section：
   - source locator：
   - 为什么是 P0：
   - 用户需要检查：
   - 如果不审核的风险：

P1 优先审核：
1. 文件：
   - 位置：
   - claim ID / section：
   - source locator（如有）：
   - 为什么是 P1：
   - 用户需要检查：

P2 可抽查：
- 文件：
  - 位置或内容类型：
  - 抽查重点：

P3 快速扫过：
- 文件：
  - 内容类型：

精力有限时建议先看：
1. 第一优先审核位置；
2. 第二优先审核位置；
3. 第三优先审核位置；
4. 必要时第四优先审核位置；
5. 必要时第五优先审核位置。
```

输出约束：

1. P0 无总量硬上限并全部逐项可审核；可分批但不得聚合隐藏、降级或遗漏。没有 P0 时明确写 `P0: none identified`。
2. P1 可按认知负担分组；每个重要判断仍须呈现 evidence、Agent inference 和审核目的，不得只给文件名。
3. P2/P3 只聚合，不逐条列 claim。
4. 始终给出精力有限时最值得先看的 3–5 个位置；不足 3 个时列出全部实际审核点，不虚构。
5. 不把低风险 index/overview/handoff/log 与科学 claim 混为同一优先级。
6. 多篇摄入按每篇文献分别列 P0/P1，再统一聚合 P2/P3。

### 不同任务的 triage 重点

- 文献摄入：分别评估 source-level、claim-level、locator-sensitive、project/synthesis-related 审核点和低风险导航修改；优先列核心 scientific claims、关键图表/公式/transition/observable、模型与实验比较、作者解释、争议重解释和 paper evidence gate 候选。
- Project/synthesis：优先列主结论、evidence matrix、cross-source interpretation、需回 source/locator 核对、可能过度裁决、可能把模型写成事实或把 synthesis 写成论文结论的位置。
- Data-analysis-bridge：分别列 direct data facts、analysis outputs、possible/competing interpretations、innovation/paper-level candidates 和 planning notes。用户数据一旦进入物理解释、创新点或论文候选，至少列为 P0 或 P1。
- Claim-review-update：列明哪些 `needs_review` 改为 `false`、哪些保留 `true`、哪些影响 paper evidence gate、哪些仍需 P0/P1 复核，并确认只处理用户审核报告明确提到的内容。

### 格式示例（非真实 claim）

```text
Human review triage

P0 必须审核：
1. 文件：knowledge/sources/example-paper.md
   - 位置：Key claims / transition mixing
   - claim ID：EX24-3
   - source locator：Fig. 7 and Sec. III.B
   - 为什么是 P0：该数值直接支撑核心结构解释。
   - 用户需要检查：图、正文与所录数值及 claim kind 是否一致。
   - 如果不审核的风险：可能把模型解释写成实验裁决。

P1 优先审核：
1. 文件：knowledge/projects/example-project.md
   - 位置：Evidence matrix / EX24-3 row
   - claim ID / section：Evidence matrix
   - source locator：Fig. 7 and Sec. III.B
   - 为什么是 P1：该行决定 source 在支持与反证中的归类。
   - 用户需要检查：归类是否保留限制与竞争解释。

P2 可抽查：
- 文件：knowledge/sources/example-paper.md
  - 位置或内容类型：Summary and follow-up sources
  - 抽查重点：是否忠实概括且未夸大覆盖范围。

P3 快速扫过：
- 文件：knowledge/index.md
  - 内容类型：导航入口。

精力有限时建议先看：
1. EX24-3 与 Fig. 7；
2. project evidence matrix 的 EX24-3 行；
3. source summary。
```

## Default commit policy and WIP lifecycle

普通文献摄入完成且 Git 检查与 Wiki lint 通过后，如果尚未完成证据链、等待审核或存在 hard P0，创建本地 WIP ingest commit；若已完成发布门且没有本轮覆盖指令，默认完成 final commit 并自动 push：

```text
WIP ingest: <paper short name> for user review
```

WIP commit 只是等待审核或恢复的临时检查点，用于保存当前结果、减少未提交 diff 和文件监听负担；不表示页面或 claims 已完成人工复核，因此保持本地，不自动 push。

只有用户明确写出“禁止任何本地 commit”“不要创建 WIP commit”或“不要本地临时 commit”时，才不得创建 WIP。旧式“不 commit/push，等待审核”在文献摄入场景中解释为：

- 不创建 final commit；
- 不 push；
- 允许创建本地 WIP ingest commit。

以下任一情况存在时不得创建 WIP ingest commit：

- 检查失败；
- 存在无法解释的文件；
- 存在 raw、PDF、论文、数据或图片 diff；
- 无法安全、显式地暂存本轮文件。

WIP ingest commit 只允许包含本轮文献摄入相关文件。不得包含：

- `.obsidian/graph.json`；
- `raw/zotero/wiki-inbox.bib`；
- raw PDF、论文、数据或图片；
- 未经用户明确要求的 `PLAN.md`；
- 无关 framework/governance 文件；
- 无法解释的文件。

同一分支最多允许一个 active WIP ingest commit。若 HEAD 已以 `WIP ingest:` 开头，不得开始下一篇摄入；必须等待用户审核后 finalize/amend，或由用户明确要求另开分支、放弃 WIP。审核完成后按 `system/workflows/ingest.md` 使用 amend 把 WIP 转换为 final commit，避免临时 commit 累积。

## 1. review-ingest

**适用**：大型综述、review article、RMP、Physics Reports、Annual Review，以及长篇历史、理论或实验综述。

**默认抽取重点**：

- scope、chapter/topic map、terminology、historical framework；
- major concepts、phenomena classification；
- 综述汇总的 experimental criteria 与 model families；
- review-level author synthesis；
- follow-up original sources 与 evidence gaps。

**默认更新页面**：

- source、concept、observable、method、model；
- synthesis，仅当内容长期可复用；
- project，仅当与当前 project 明确相关。

**禁止事项**：

- 不逐页机械抽取全文，不创建大量空壳页面；
- 不把综述转述的具体核素结果写成原始实验事实；
- 不让综述替代原始实验论文；
- 不把 review/background 写成 observed fact。

**最终复盘**：

- 章节/主题地图；
- 新增 review/background claims；
- 需要回看原始来源的 claims；
- follow-up sources 与 evidence gaps。

## 2. experiment-ingest

**适用**：原始实验论文，以及具体核素、能级、能带、γ 线、谱学判据、in-beam γ spectroscopy、DCO/ADO、polarization、lifetime 等实验结果。

**默认检查项（仅在文中报告时抽取）**：

- reaction、beam、target、detector；
- level scheme、gamma rays、transition energies、relative intensities、branching ratios；
- coincidence relationships、gating conditions、linking transitions；
- spin/parity assignments、band structure、multipolarity；
- DCO/ADO、angular distribution、linear polarization；
- lifetime、B(M1)/B(E2)、quadrupole moment；
- dynamic/kinematic moment of inertia、signature splitting、wobbling energy；
- configuration assignment、experimental criteria；
- author interpretation、model comparison、limitations 与 unresolved assignments。

文中未报告的项目保持缺失，不编造、不硬补。

**默认更新页面**：

- source、nucleus、band、experiment、observable、method、concept；
- synthesis，仅当涉及多来源综合；
- project，仅当用户指定或现有 project 明确相关。

**禁止事项**：

- 不把作者解释或模型比较写成实验事实；
- 不把暂定 spin/parity 写成确定值；
- 不把非目标质量区文献写成目标质量区直接证据；
- 关键 claim 不得缺 locator。

**最终复盘**：

- observed facts、experimental criteria；
- author interpretations、model comparisons；
- unresolved assignments 与 `needs_review` claims；
- 是否更新 project，以及该文献是核心证据还是比较背景。

## 3. theory-ingest

**适用**：理论或模型论文，包括 PRM、TAC、CDFT、MχD、TPSM、CSM、CNS、shell model、cranking 等。

**默认抽取重点**：

- model name、model assumptions；
- 核心 Hamiltonian/equations、parameters、deformation inputs；
- configuration assumptions、calculated nuclei/bands；
- calculated observables、energy spectra、B(M1)/B(E2)；
- wobbling energy、signature splitting、chirality indicators；
- angular momentum geometry、potential energy surface；
- triaxiality/gamma deformation；
- comparison with experiment 与 model limitations。

**默认更新页面**：

- source、model、concept、observable、synthesis、project；
- nucleus/band，仅当计算明确对应具体核素或能带。

**禁止事项**：

- 不把模型结果写成实验事实；
- 不把模型预测写成已经观测；
- 不忽略参数依赖和模型假设；
- 不替用户决定最终物理解释。

**最终复盘**：

- model assumptions、model results；
- comparison with experiment、model limitations；
- competing interpretations 与 `needs_review` claims。

## 4. method-ingest

**适用**：方法或技术论文，包括 DCO、ADO、polarization、angular distribution、lifetime、DSAM、RDDS、γγ coincidence、detector array 和 analysis method。

**默认抽取重点**：

- method definition、measured quantity；
- required detector geometry；
- formula/ratio/calibration；
- gating requirement、normalization；
- uncertainty sources、applicability、limitations；
- diagnostic criteria 与 example usage。

**默认更新页面**：

- source、method、observable、experiment、concept；
- project，仅当与数据处理或判据使用直接相关。

**禁止事项**：

- 不把示例核素结果自动写成具体核素事实；
- 不省略适用条件；
- 不把理想公式写成无条件适用；
- 不让方法判据替代物理解释。

**最终复盘**：

- 方法定义与适用条件；
- 限制和误差来源；
- 可服务的 project 或数据分析任务；
- `needs_review` claims。

## 5. targeted-ingest

**适用**：长文献中只关心局部问题；只查某个判据、图、表、公式或定义；或 token/额度有限。

**默认抽取重点**：

- user-specified question；
- relevant sections/figures/tables；
- directly relevant claims；
- 明确标记未读、未覆盖章节；
- 是否需要后续 full ingest。

**默认更新页面**：

- source；
- 与目标问题直接相关的 concept、observable、method 或 project；
- 不做大范围扩展。

**禁止事项**：

- 不伪装成全文摄入；
- 不更新大量无关页面；
- 不创建大量新概念页；
- 不把未读章节写成已覆盖。

**最终复盘**：

- 本轮定向问题；
- 实际阅读的章节、图和表；
- 未覆盖范围与新增 claims；
- 是否建议未来 full ingest。

## 6. project-ingest

**适用**：为特定 project、研究问题、数据处理结果或创新点候选摄入文献。

**默认抽取重点**：

- project research question 与 source contribution；
- observed facts、experimental criteria、model results；
- author interpretation、competing interpretations；
- evidence gaps、follow-up sources；
- data-analysis bridge 与 innovation candidate notes。

**默认更新页面**：

- source、project；
- 相关 nucleus、band、concept、observable、model、method；
- synthesis，仅当需要跨来源综合。

**禁止事项**：

- 不把 project 写成论文草稿；
- 不声称文献完整覆盖；
- 不把未复核 claim 写成确定结论；
- 不替用户决定最终创新性；
- 不编造用户尚未提供的数据处理结果。

**最终复盘**：

- project 更新与 evidence matrix/notes；
- 支持或削弱哪些解释；
- evidence gaps、follow-up sources；
- data-analysis bridge 更新；
- innovation candidate notes 是否仍只是候选。

## 7. daily-ingest

**适用**：每天摄入 1–2 篇文献，或小批量多篇摄入。

**默认规则**：

- 每篇文献单独判断策略，单独建立或更新 source；
- 不为数量牺牲 locator、`claim_kind` 或 evidence gaps；
- token/额度不足时优先稳定完成第一篇，第二篇写入 handoff；
- 不仓促摄入多篇导致质量下降。

**最终复盘**：

- 每篇文献的 ingest strategy；
- 每篇新增 claims 与 `needs_review` claims；
- 每篇更新页面；
- 每篇分别列出 P0/P1 审核点，不把多篇来源混为一组；
- 是否需要分开 commit；
- 下一轮续跑建议。

## 8. claim-review-update

**适用**：用户已人工审核 source 页或 claim，需要据审核报告更新 `review_status` 或 `needs_review`。

**默认规则**：

- 只处理审核报告明确提到的 source 或 claim；
- 不自行判断其他 claim；
- 页面级 `human-reviewed` 不自动清除 claim-level `needs_review`；
- 只有用户明确确认某条 claim 或某组 claims，才把对应 `needs_review` 改为 `false`；
- 审核报告不明确时保留 `needs_review: true`。

**最终复盘**：

- 更新了哪些 source、处理了哪些 claim ID；
- 哪些 `needs_review` 改为 `false`，哪些仍为 `true`；
- 哪些修改影响 paper evidence gate，哪些仍需 P0/P1 复核；
- 是否只处理用户审核报告明确提到的内容、是否避免批量清除；
- 是否更新 overview/lint governance 统计。

## 9. data-analysis-bridge

**适用**：用户提供自己的数据处理结果，需要接入 project 或梳理创新点候选。

**默认抽取重点**：

- user-provided data facts 与 analysis outputs；
- uncertainty、limitations；
- 与现有 source/synthesis 的比较；
- possible interpretations、competing interpretations；
- missing checks、innovation candidate notes；
- follow-up measurements 或 literature。

**禁止事项**：

- 不编造用户未提供的数据；
- 不把阶段性结果写成最终结论；
- 不替用户决定最终创新性；
- 不修改 raw 数据、论文或图片；
- 不创建写作 Skill。

**最终复盘**：

- project 更新与 our analysis findings；
- possible/competing interpretations；
- direct data facts、analysis outputs、innovation candidate 与 paper-level candidate 分层；
- 用户数据进入物理解释、竞争解释或创新点候选时对应的 P0/P1 审核点；
- evidence gaps 与 literature needed；
- 哪些内容能够或尚不能进入 paper evidence gate。

## Minimal user prompt interface

以后用户只需提供：

```text
目标文献：
raw/papers/<file>.pdf

目标 BibTeX key：
<key>

摄入策略：
<review-ingest / experiment-ingest / theory-ingest / method-ingest / targeted-ingest / project-ingest>

研究主题：
<theme>

project 关系：
<不关联 / 融入已有 project / 建议是否需要新 project>

特别注意：
<非目标质量区、只读某章节、不作为核心证据等>

提交策略：
<通过发布门后自动 final commit/push / 默认本地 WIP / 禁止任何本地 commit / 审核后只 final commit>
```

用户不需要重复 Global ingest rules 或各策略默认清单。未填写提交策略时，已完成且通过发布门的任务默认自动 final commit/push；等待审核、存在 hard P0 或未完成时默认本地 WIP、不 push。旧式“不 commit/push，等待审核”也不禁止本地 WIP，只有明确写“禁止任何本地 commit”才禁止。`daily-ingest`、`claim-review-update` 和 `data-analysis-bridge` 可在“摄入策略”或任务正文中直接指定；缺少关键信息且无法从仓库唯一确定时，Codex 应先询问，不得猜测。
