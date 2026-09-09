---
type: system-checklist
graph-excluded: true
updated: 2026-08-04
---

# Wiki 系统核查清单

本文件是人工可读的最高层检查入口。检查必须报告“通过 / 警告 / 失败 / 未执行”，不得把未执行写成通过。

## 自动检查入口

在仓库根目录运行：

```bash
python system/scripts/wiki_lint.py --fail-on error
```

- exit code `0`：没有达到失败阈值的问题；
- exit code `1`：存在 error，提交前必须处理；
- `--fail-on warning`：临时采用更严格阈值；
- `--format json --output outputs/lint-report.json`：生成机器可读报告；
- Gitee `chx6/silicon_graduate` 是维护远端；GitHub 仅作为镜像，不作为本仓库维护或 CI 入口。

修改 lint 脚本或配置后还要运行：

```bash
python -m unittest discover -s system/tests -p "test_*.py" -v
```

自动 lint 覆盖结构、链接、哈希、字段、A/Z/N、可解析的中子蒸发反应道、Git 边界和 claim-level 治理统计。`GOVERNANCE` 行报告页面/source unreviewed、claim 待审、缺 locator/kind、source 缺 raw_file/citation key；涉及科学解释、证据独立性和物理等价性的项目仍需人工判断。

## A. 会话记忆与治理

- [ ] 已按 `AGENTS.md` 的顺序读取固定启动文件；`README.md` 只作为稳定入口，不因其中链接自动扩展读取；`system/handoff.md` 只读 `Active handoff`，`system/log.md` 只读最近 10 条记录；仅在规定触发条件成立或用户明确要求时额外读取 `PLAN.md`。
- [ ] `PLAN.md` 保持宏观计划、个人好奇心与研究方向草稿性质，未被当作 cite-key 文献清单、执行日志或必须立即执行的任务列表。
- [ ] `PLAN.md` 未在缺少用户明确要求时被覆盖、重写、删除、重排或机械整理。
- [ ] `system/handoff.md` 顶部包含短的 `Active handoff`，包括 current active task、branch / WIP or local commit、last task status、unfinished items、P0/P1 review focus、risks、next prompt 和 recent user decisions；历史交接未堆入 active 区块。
- [ ] 启动时未默认读取完整 `system/wip-queue.md`；只有涉及 unfinished WIP、review continuation、safe suspend、non-serial work 或用户询问 pending WIP 时才读取。
- [ ] PLAN/handoff 冲突已按“方向与优先级看 PLAN、执行事实与交接细节看 handoff”分类；无法分类时已询问用户。
- [ ] `system/memory.md` 只保存稳定规则与用户确认过的偏好，不保存临时聊天摘要。
- [ ] 已判断本次是否需要更新 `USER_GUIDE.md`；需要时已经同步。
- [ ] 本次规则修改已同步到 `AGENTS.md`、`check.md` 和相应工作流。
- [ ] L0-L4 完整定义只存在于 `system/workflows/autonomous-research.md`；AGENTS/query/reflect/ingest/Skill 仅保留短路由，没有复制漂移或堆积第二套规则。
- [ ] ordinary Q&A 未误触发写入；授权 ingest/reflect/project/synthesis 默认运行 L2；高价值问题进入 L3 时有明确 scope/milestone；L4 已形成 candidate、safe suspend 并由用户确认数据后手动启动。
- [ ] 每周自测先分为 `weekly-learning`、`continuation-audit` 或 `maintenance`；只有 `weekly-learning` 计入轮次，定位符/状态/重复核验没有新的决策信息时不得冒充新知周测。
- [ ] `weekly-learning` 每次最多主动研究两个满足硬重要性门槛的问题，并在具体取证前完成 Wiki 内全局候选筛选：保留温故槽和新知槽；只要有合格候选，新知槽来自非重叠覆盖区域；无合格候选时不为填槽升级低价值问题。
- [ ] 选题从最近八次仓库内 `weekly-learning` 报告重建覆盖债务；同一核素/project 不连续占据新知槽，同一核心来源冷却两个学习周期；hard P0、新独立原始证据、实质冲突或用户明确要求的例外已记录，并只在同等级候选间使用可复现随机 tie-break。
- [ ] 每份实质周测报告有 `Selection audit`，记录运行类型、是否计入轮次、候选覆盖类别、两个槽位、核心来源指纹/重叠、冷却或 deferred 原因、新增知识和 belief revision；其它重要问题写入 `Deferred important issues`。
- [ ] 核素问题在适用时比较同位素和同中子素；L3 只使用合法、可核验的 Nature-first 获取路径和 Agent 管理的 `raw/papers/gpt/**`、`raw/zotero/gpt.bib`；关键 SI 才下载，`wiki-inbox.bib` 永不修改/暂存。
- [ ] L4 只生成 `outputs/l4/<issue>-<date>/report.md` readiness（`ready`/`partial`/`not-ready`）；`partial`/`not-ready` 不停用周测，不假定用户已有实验数据。
- [ ] pending review 只阻止重叠写入，不阻止全局只读选题或无重叠的新知任务；有实质变化的周测生成 `outputs/self-tests/` P0/P1 报告和相应 WIP/final 状态，通过 H3/发布检查后按持续授权自动 push；未完成或无实质变化时未制造空 commit。
- [ ] 检查不依赖 Docker、固定路径、`.codex/`、`.obsidian/` 或特定 AI 工具配置；这些属于本地运行环境。
- [ ] 本轮只执行与 Wiki 任务相关的命令；未依赖桌面端 GUI 或 Computer Use，浏览器下载已指定到仓库内路径。
- [ ] 递归删除、历史重写、raw 证据删除/覆盖、已发布标签改写和其它不可逆操作均有用户明确授权；普通 push 使用持续授权但仍通过 H3/发布检查，未把自主发布授权解释为 force push 或 raw 覆盖授权。
- [ ] `system/log.md` 只追加，没有重写历史记录；启动或普通恢复未用 `ReadAllText(system/log.md)` 读取完整 log。
- [ ] 若使用定时续跑，已遵循 `system/workflows/scheduled-continuation.md`，并说明本机应用、调度服务与电脑可用性前提。
- [ ] 若启用 Wiki farmer，已先运行 dry-run；监控范围仅为 Wiki 根目录内的公开 rollout JSONL，会话状态只写入 `tmp/farmer/`，没有读取 Codex SQLite、凭据或 raw。
- [ ] Hook 只通过 `system/scripts/wiki_hook.py` 显式调用；输入按数据处理，未自动修改 Codex 配置、source/eval 目标文件或执行外部安装器。
- [ ] 创建分支、提交、fetch 或 push 前运行 `python3 system/scripts/wiki_automation_preflight.py --root .`；不依赖 PowerShell、ACL、运行时 marker 或项目 sandbox profile。
- [ ] 定时任务正文未通过 shell、补丁或文件 API 读写 Codex 宿主 automation memory、global state、sandbox state 或任何 Wiki 外文件；宿主状态仅由 Codex automation 功能维护。
- [ ] 定时任务的“一次/重复”、时区和下次运行时间在界面中无歧义；一次性请求未显示为“每天”。
- [ ] 只有在存在运行回执且产物已核验时，才把定时任务报告为“已执行/已完成”；无回执明确写为“未触发/未验证”。
- [ ] 若执行余量不足、检查失败需要用户决策、长任务未完成或任务无法稳定完成，已停止扩大范围，运行三项 Git 检查并把完整 safe suspend 信息写入 handoff。
- [ ] Safe suspend 未被表述为自动睡眠/原地恢复，未自动创建 automation 或 push；大量 diff 场景已按规则判断是否创建本地 WIP checkpoint。
- [ ] Safe suspend / checkpoint 已写明未完成内容、未核查 locator / claim gaps、P0/P1 风险和 continuation prompt；未把 metadata-only 或 skimmed 伪装成 read / deep-read。


### 启动与工具开销控制

- [ ] 未读取 handoff archive，除非用户明确要求审计历史。
- [ ] 未对全仓库运行无过滤 `Get-ChildItem -Recurse`、`tree`、`ls -R` 或 `rg "关键词" .`。
- [ ] 搜索已限定到 `knowledge/`、`system/`、`AGENTS.md`、`check.md`、`USER_GUIDE_DETAIL.md` 或明确目标文件；未无目的扫描 `.git/`、`.qmd/`、`.obsidian/`、`tmp/`、`raw/`、`outputs/`、`share_message/`、`__pycache__/`、`.pytest_cache/`。
## B. 原始证据完整性

- [ ] `raw/` 只有本轮明确授权的 Agent 管理入口发生变化；`raw/zotero/wiki-inbox.bib` 与其他未授权 raw 文件未被修改、移动、重命名或删除。
- [ ] 每个已摄入来源均记录 `raw_file` 与 `raw_sha256`。
- [ ] 哈希变化被标记为 `source-modified`，并进入重新摄入流程。
- [ ] DOI、期刊、卷页、年份、实验或理论类型等元数据尽可能完整。
- [ ] 关键结论包含页码、图号、表号、能级或其他精确定位信息。

## C. 科学表述与证据

- [ ] 已查看 lint 的 `GOVERNANCE` 统计，页面级 review 状态与 claim-level `needs_review` 没有混为一谈。
- [ ] `CLAIM_NEEDS_REVIEW` info 已列入人工审阅队列，未因页面为 `human-reviewed` 而自动清除。
- [ ] `claim_missing_locator` 与 `claim_missing_kind` 均为 0，或已按 error 处理。
- [ ] `source_missing_raw_file` 与 `source_missing_citation_key` 均为 0，或已解释并处理。
- [ ] 实验事实、作者解释、模型结果和个人推断已明确区分。
- [ ] 置信度没有仅凭引用数量自动提高。
- [ ] `high` 置信度均有用户确认记录。
- [ ] 多来源结论已判断证据是否真正独立。
- [ ] 竞争解释、反证与限制没有被静默覆盖。
- [ ] “候选”“支持”“强证据”“确定”用词与证据强度匹配。
- [ ] 单篇来源或二手综述没有被写成领域共识。

## D. 低能核结构领域专项检查

- [ ] 核素的 `A/Z/N` 自洽，元素符号与质量数正确。
- [ ] 自旋宇称、能级、跃迁能量和带标签保留原文单位及不确定度。
- [ ] 组态指认与实验观测分开记录。
- [ ] DCO、角分布、线偏振、寿命、分支比等证据类型没有互相替代。
- [ ] 对转动带、振动、wobbling、chiral doublet 的判据写明适用条件。
- [ ] γ-soft、γ-rigid、triaxial deformation 没有因词面相近被自动合并。
- [ ] 不同模型参数、约定、坐标系和符号定义已注明来源。
- [ ] 熔合蒸发反应道、束流、靶核、蒸发粒子道与余核对应关系自洽。

## E. 结构与链接

- [ ] 所有知识页都有合法 YAML frontmatter 和允许的 `type`。
- [ ] Wikilink 目标存在，或明确标记为待建页面。
- [ ] 没有 slug/aliases 重复造成的概念分裂。
- [ ] `knowledge/index.md` 覆盖全部正式知识页。
- [ ] 系统页均设置 `graph-excluded: true`。
- [ ] 没有把临时输出误写进长期概念页。

## F. 摄入、查询与综合

- [ ] 用户未指定摄入模式时采用标准深入阅读模式；Agent 只建议切换，没有自行升级或降低。
- [ ] 三种用户模式与 `reading_depth` 四值保持分离；source 的 `reading_depth`、Covered scope 和 Not covered 反映实际完成范围，未从局部深查推断全文 `deep-read`。
- [ ] 标准深入阅读逐项评估论文问题、动机、设计逻辑、证据链、假设/限制、比较、迁移边界、竞争解释、反向检验、研究问题和认识修正，但没有机械制造固定产量。
- [ ] 标准深入阅读已记录简短 Knowledge Impact and Learning Decision；`no material change` / `source-only` 被视为合法结果，没有机械创建 project、synthesis、research-note 或 overview。
- [ ] 重要 Related Knowledge / Project Relation 使用受控 relation type 并附具体说明；普通链接未被强制类型化，`retrospective-connection` 与 `not-direct-evidence` 的边界未被误用。
- [ ] 多篇摄入任务达到触发条件时，已在自然主题阶段执行 thematic batch REFLECT；单篇重要来源只执行 Knowledge Impact，没有单独触发 batch REFLECT；核心论文阶段没有因后续宽泛综述而被推迟，且无持久化时记录了具体 no-persistence decision。
- [ ] 作者明示内容与 `Analytical reconstruction` 分开；分析性重建列出 evidence、locator、推断步骤和不确定性，未冒充 source-grounded fact。
- [ ] Ordinary Q&A 没有默认启动完整学习闭环或持久化 provisional reasoning；研究型任务按 query routing 进入 ingest/reflect。
- [ ] Ordinary Q&A 保持 read-only，没有因读取旧页面而静默写回；发现迁移需求时只报告并路由到授权 workflow。
- [ ] on-touch migration 只处理当前授权 ingest/reflect/project/synthesis/claim-review-update/研究写作任务实际使用的旧页面，没有批量升级未触及历史页。
- [ ] 没有批量补历史 ingest mode、research-note、Personal Notes 或统一 frontmatter；科学 claim、interpretation、review/reasoning state 或知识关系变化已进入 Human review triage。
- [ ] Research note 只在授权研究任务且满足持久化门时创建；没有成为每篇文献的默认产物。
- [ ] L2 只记录高价值、可检验的未决问题；L3 包含背景/已有工作、候选课题、假设、反证、信息增益与 milestone；L4 记录数据身份、运行复现、失败和 belief revision，没有用文献综合、作图或写作冒充数据研究。
- [ ] Codex 自审核未伪装成 Human review，未自行清除 `needs_review`、设置 `confidence: high` 或晋升正式 synthesis。
- [ ] Research note 使用 `review_status: unreviewed` 与 `reasoning_status: provisional` 起步；`reasoning_status` 未重复 `unreviewed/reviewed`，`revised` 只作为 history event。
- [ ] `Grounded Evidence` 与 `Provisional Reasoning` 明确分开；note 不替代 source evidence。
- [ ] `promoted` note 有正式 promotion target、Human review 和 grounded-source 回链；rejected/superseded/withdrawn 保留处置依据。
- [ ] Ordinary Q&A 已排除 `knowledge/research-notes/` / `type: research-note`；研究型任务使用 note 时显示 provisional 状态并回读 grounded sources。
- [ ] Lint 只验证 research-note 的结构、枚举、grounded-source 非空和 promotion/review 一致性；没有把 lint 通过解释为推理科学正确。

- [ ] 摄入前已查重并检查 aliases。
- [ ] 摄入时区分了当前研究锚点与 Wiki 收录边界，没有把主线质量区当成知识库边界。
- [ ] 没有把质量区本身当成唯一排除标准或唯一纳入标准。
- [ ] 若主线锚点之外的来源被保留为 source-only，理由基于证据密度、复用价值或任务范围，而不是质量区本身。
- [ ] 用户明确声明某文献、核素、反应体系或方法为重点时，摄入已尊重该优先级，且没有虚构用户参与历史。
- [ ] 摄入已判断是否存在足以支持轻量 nucleus、method、concept、band 或 project 页的 source-supported 可复用信息。
- [ ] framework-level 规则没有使用未定义的 AC/AD 缩写；需要时已写成角关联、角分布或展开后的英文全称。
- [ ] 摄入前已按 `system/workflows/ingest-strategies.md` 运行时短规则选择策略；普通单篇摄入定义明确，未默认读取 `ingest-strategies-detail.md`。
- [ ] 已确认 `ingest-strategies-detail.md` 的 detail 指 workflow detail，不是 PDF reading depth；不读取 detail 不得降低文献阅读深度。
- [ ] 策略默认清单只用于检查文中是否报告相关信息，没有为填满清单编造内容。
- [ ] 摄入复盘采用 compact final recap，优先列 Result status、commit/push、关键文件、Human review triage、checks 和 next action。
- [ ] 摄入后已做必要最小同步；普通单篇摄入没有无必要重写 `knowledge/overview.md`，若 deferred 已说明原因和建议补跑时机。
- [ ] 查询答案的核心结论可追溯到来源页，而非只引用综合页。
- [ ] 高复用答案才持久化，普通聊天不机械入库。
- [ ] 综合前执行了反向检验，并记录未找到反证时的回音室风险。


### Project / synthesis active summary 与 staged reading

- [ ] 如果本轮修改了大型 project/synthesis 主体，已同步最小更新该页 `Agent active summary`；若页面缺失 active summary 且本轮实际修改该页，已创建短 summary。
- [ ] 用户明确要求补充 project/synthesis 时，没有只修改 active summary。
- [ ] Active summary 仅作为导航和 section 定位，没有替代 source locator、project/synthesis 主体或原文证据。
- [ ] PDF staged evidence reading 被作为阅读顺序优化执行，不被解释为降低用户模式要求；最终 `reading_depth` 如实反映实际完成范围。
- [ ] 如果核心 PDF 读取未完成，已 safe suspend 并列出已读范围、未读 section/figure/table/locator，而不是省略核心读取。
### QMD 本地检索

- [ ] 从仓库根目录运行 `qmd.cmd status` 时使用 project-local `.qmd/index.sqlite`，collection 名为 `nuclear-knowledge`，范围仅为 `knowledge/**/*.md`。
- [ ] `.qmd/` 作为可重建缓存已被 Git 忽略，没有把 SQLite 索引或模型提交进仓库。
- [ ] 普通单篇文献摄入未强制 `qmd.cmd embed`；若 QMD refresh deferred，已说明原因和建议补跑时机。批量摄入、多篇完成、用户明确要求或大型 project/synthesis 依赖最新检索时，已运行或明确安排 `qmd.cmd update` / `qmd.cmd embed -c nuclear-knowledge`。
- [ ] 精确查询优先 `rg`/`qmd search`，语义查询按需使用 `qmd vsearch`；完整 `qmd query` 只在收益足以覆盖数分钟冷启动时使用。
- [ ] 已对候选结果执行 `qmd get` 或直接读取完整文件，没有把搜索摘要、分数或 reranker 输出当成科学证据。
- [ ] QMD 不可用、超时或索引异常时已如实报告并降级到 `rg`、index 和直接读取。
- [ ] 没有运行 `qmd update --pull` 或让 QMD 隐式操作 Git；`qmd pull` 只在首次下载或修复模型时使用。

### Human review triage

- [ ] 文献摄入、project、synthesis、data-analysis-bridge 或 claim-review-update 的最终复盘包含 Human review triage。
- [ ] 每篇 source-specific triage 已写回对应 source 页面而非只存在于聊天/复盘，并直接采用现有 P0/P1/P2/P3 定义。Human Review Notes/Human Review Record 只在实际批注或审核事件发生后实例化。
- [ ] Triage 明确列出 P0/P1/P2/P3；没有 P0 时写明 `P0: none identified`。
- [ ] P0 无总量硬上限；所有 P0 逐项给出实际判断、文件、section/段落、claim ID（如有）、source locator、grounded evidence、Agent inference、审核目的和不审核风险。
- [ ] P0 可以分批但没有聚合隐藏、降级、删除或直接晋升；后续未审 P0 队列完整保留。
- [ ] 没有把所有 `needs_review` 等权重铺开；P1 可按文件分组但重要判断仍可审核，P2/P3 按文件聚合。
- [ ] 审核点较多时给出“精力有限时建议先看”的 3-5 个位置。
- [ ] 低风险 index/overview/handoff/log、格式和导航更新与科学 claim 分开。
- [ ] Paper evidence gate 候选被列为 P0/P1；未完成 P0/P1 审核时没有描述为可直接用于论文。
- [ ] 高相关未核验材料未因 `unreviewed` 或缺少 Review history entry 而被隐藏；已作为 candidate evidence 标明 review/source/locator 状态、适用条件、缺口和核查路径。
- [ ] P0/P1 聚焦当前关键 claim 或证据项；没有要求用户先全面审核整页/整篇，除非当前 claim 依赖更广上下文。
- [ ] 页面整体 `unreviewed` 未阻止具体 claim 核验；页面 `human-reviewed` 也未替代精确、高风险或论文用途 claim 的直接来源核验。
- [ ] Paper admission 由具体 claim、拟用措辞、直接来源、locator、适用条件、数据一致性和竞争解释共同决定，并经用户明确确认；局部准入未扩张为整页或其它 claims 的 review 状态更新。
- [ ] 用户数据解释、competing interpretation、innovation candidate 和 paper-level candidate 被列为 P0/P1。
- [ ] 多篇逐篇摄入没有粗略批处理；每篇文献分别列 source-level / claim-level 审核重点和 P0/P1。
- [ ] Project/synthesis 任务列出主结论段落、evidence matrix 和跨来源解释的审核优先级。
- [ ] 普通 ingest 的 P0 已由 Agent 逐项回证据处置；未隔离 hard P0 会阻止 final/push，P1 与已隔离/降级项目保留为未来问答、研究或论文证据采用时的核验优先级，不机械等待用户逐篇审核。

### 中英文术语归一化

- [ ] concept/model/observable/method 页面包含检索所需的中英文 aliases。
- [ ] 单篇来源新增术语优先写入页面 aliases；只有跨库统一、歧义、slug 风险或用户明确要求时才更新 `system/vocabulary.md`。
- [ ] Query workflow 已使用 vocabulary 与页面 aliases 扩展中文、英文、缩写、历史写法和实验口语。
- [ ] 中文和英文等价查询能够命中同一 canonical concept 及核心 source/claim。
- [ ] 泛称命中多个模型或方法时已列出候选，没有静默选定或合并。
- [ ] `angular distribution` / `angular correlation`，以及 shell model / CSM / PSM / TPSM 等易混术语保持分离。
- [ ] vocabulary 只用于查询归一化；回答中的科学主张仍引用知识页、source 和 locator。

## G. 输出要求

系统核查报告写入 `outputs/system-audit-YYYY-MM-DD.md`，至少包含：

1. 检查时间与范围；
2. 通过、警告、失败、未执行的数量；
3. 每个失败项的证据；
4. 修复优先级 P0/P1/P2；
5. 未自动修复且需要用户判断的项目。

## H. Git 与文档同步门

### WIP ingest/review 与 safe suspend checkpoint

- [ ] 文献摄入长任务、中断、未隔离 hard P0 或用户明确要求先审核时，HEAD 存在且仅存在一个 active `WIP ingest:` commit；正常完成且 Agent 自审通过时已 amend/创建 final commit。
- [ ] WIP/final commit 只包含本轮摄入及直接必要同步文件；WIP message 以 `WIP ingest:` 开头，final message 与实际范围相符。
- [ ] Project、synthesis 或跨来源综合完成并等待人工审核时，HEAD 存在且仅存在一个 active `WIP review:` commit。
- [ ] WIP commit 只保存在本地，没有 push；普通 ingest final 只有在 H3、fresh fetch、ancestry 和精确 refspec dry-run 通过后才使用同一 refspec 非 force push。
- [ ] 已判断当前是否存在 pending WIP，以及本轮任务是否需要更新 `system/wip-queue.md`。
- [ ] 若存在 pending WIP、等待审核、safe-suspended task 或未 push checkpoint，`system/wip-queue.md` 已新增或更新短 entry。
- [ ] Pending WIP queue 只记录恢复索引，没有写入 raw 内容、source claim 正文或长复盘。
- [ ] Pending WIP queue 只保留继续审核所需的最新 branch / commit / next action，没有频繁追踪每个临时 commit/push 状态。
- [ ] WIP 结束时 overview/QMD deferred 状态已在 queue 和最终复盘中说明；未把 WIP push 到 `main`，且没有把 Agent 自审后的 final/push 伪装成人类审核。
- [ ] 本轮是否存在用户已经完成的实质性人工审核，以及是否可以无歧义地判断本轮审核已经结束。
- [ ] Review history 触发判断没有机械依赖固定关键词；存在歧义时未擅自创建 Review history entry。
- [ ] Review history 由审核完成语义触发，而不是由 commit、push、merge、overview 或 QMD 触发。
- [ ] Review finalization 已按用户审核意见做最小修改，并只处理用户明确确认范围内的 `review_status` / `needs_review`。
- [ ] Review history 不要求 task closed 后才能写入，并允许与 Pending WIP queue 同时存在。
- [ ] 已判断当前任务在本轮审核后是否应写入 `system/review-history.md`，以及 queue 应继续保留、更新还是清理。
- [ ] Review finalization 已按 ingest workflow 评估 `knowledge/overview.md` 触发条件；触发时最小同步，未触发时记录 deferred 理由，而不是机械更新。
- [ ] Review finalization 默认执行 QMD refresh；若用户明确不要 QMD 或 QMD 失败，最终复盘已说明。
- [ ] Review finalization 已按 WIP lifecycle amend/创建相应本地 commit；通过检查后默认自动 push，当前指令中的“不要 push”“只 commit”“只修改”可覆盖本轮发布；未完成、hard P0 或远端异常时保留本地状态并记录原因。
- [ ] Review history 条目记录了审核范围、用户判断、要求修改和遗留问题，没有伪装成 Git/push 历史。
- [ ] Review history 使用 `review commit message`，不使用 `Git reference` 或 `final commit message`，且没有记录 commit hash 或 push 状态。
- [ ] Review history 中的 `review commit message` 与实际 commit message 一致，且没有把它解释为 task closure、finalization complete 或 push complete。
- [ ] Review finalization 已刷新 Active handoff，并按规则更新 queue / review history / short log；没有把它们强制绑定为简单 queue-to-history 迁移。
- [ ] 没有在 push 后再额外创建纯 queue/status 修正 commit，除非前一次 finalization 确实遗漏了必要同步。
- [ ] 同一任务的多轮审核按 round 追加，而不是覆盖旧条目。
- [ ] 存在 unresolved P0、locator gaps、审核意见无法唯一映射或 WIP 归属不明时，未强行 finalization，已 safe suspend 或报告阻塞。
- [ ] framework setup 或普通维护没有回填旧 review history，除非用户明确要求历史审计。
- [ ] HEAD 已是 active WIP ingest/review/suspend 时，没有开始下一篇摄入、下一项综合或创建第二个 WIP。
- [ ] 普通 ingest 自审完成或用户审核完成后，均通过 `git commit --amend` 把对应 rolling WIP 转为 final commit，没有保留独立 WIP 或累积额外 review/final commits；只有真实 human-review completion event 才写 review history 或改变用户明确确认范围内的 review 状态。
- [ ] 用户指定本轮提交 message 时已原样使用；未指定时由 Codex 根据实际修改推荐直接相关的 message，并在最终报告中说明。
- [ ] 对应 active WIP + 用户审核完成时，已按持续授权 amend 为 final，并在发布门通过后自动 push；当前指令覆盖或科学发布门未通过时保留本地状态，没有错误套用通用“不主动 amend”约束。
- [ ] WIP/final commit 均未包含 `.obsidian/graph.json`、`raw/zotero/wiki-inbox.bib`、未经本轮授权的 raw PDF、论文、数据、图片、`PLAN.md` 或无关文件；获准进入 `raw/papers/gpt/**` / `raw/zotero/gpt.bib` 的文件已逐项核验并显式暂存。
- [ ] Safe suspend 遇到大量 Markdown diff 时，已优先判断并尝试本地 WIP checkpoint。
- [ ] 文献摄入、project、synthesis 或 framework 任务正常结束时，已自动刷新 Active handoff 并向 `system/log.md` 追加简短记录；用户不需要每次手动要求 handoff/log 收尾。
- [ ] Safe suspend 会暂停本轮自动 commit/push，保留可恢复 checkpoint；恢复后重新通过发布门才继续。
- [ ] Safe suspend WIP 只显式暂存本轮可分类文件；无法解释或无法安全暂存时未创建 commit。
- [ ] 旧式“不 commit/push，等待审核”已解释为“不 final commit / 不 push，但允许本地 WIP”；当前用户持续授权默认适用于已完成且通过发布门的任务，不覆盖等待审核 WIP。
- [ ] 只有用户明确禁止任何本地 commit 时，才不创建 WIP checkpoint，并已提示大 diff 的 CPU 风险。
- [ ] HEAD 已是当前任务相关 WIP 时使用 amend 更新；归属不明时已停止并询问用户。
- [ ] Ingest/review 最终复盘列出 hash、message、push 状态、关键文件、Agent self-audit/Human review 边界，以及后续需按 claim 回证据核验的 ID/段落。

## H. Git write-entry / commit / push preflight

`check.md` 本节是完整 Git preflight 的唯一权威执行清单。纯读取、搜索、普通问答和只给建议不运行清理脚本；任务一旦转入文件写入或 Git 写操作，按以下三阶段执行。

### H1. Write-entry preflight

- [ ] 首个 Git 门之前已运行跨平台预检并确认 `git status -sb`、`git status --short`；配置、根目录和 `.git` 可写，受保护 BibTeX 哈希已记录。
- [ ] 第一次新增、删除、移动、重命名或修改仓库文件前，已运行 `python3 system/scripts/clean_knowledge_eol_dirty.py`，再检查 status。
- [ ] 已检查 `git diff --cached --name-only` 和 `git diff --cached --stat`，没有让任务前已 staged 的无关文件静默进入本轮 commit；未擅自 unstage 或覆盖用户内容。
- [ ] 已建立入口 dirty baseline，并将现有变化分为 initial authorized scope、authorized inherited changes、protected pre-existing changes 和 unresolved/overlapping changes。
- [ ] 清理脚本 exit code `0` 视为成功；exit code `1` 后已分类剩余 substantive/mixed/unsafe 文件，而非无条件中断；exit code `2` 已停止文件与 Git 写操作并报告错误。
- [ ] 属于本轮授权或明确承接 WIP 的 substantive 修改已保留、检查 diff 且未 restore；无关真实修改保持 protected，不修改、不 stage、不 commit。
- [ ] 来源不明、mixed/conflict、任务前已有修改且本轮需编辑同一文件，或 pending-WIP overlap 无法解决时，已在首次写入该文件前暂停。
- [ ] 新的必要关联文件在第一次写入前已通过 file-entry gate：对照 baseline、WIP queue、既有 diff、必要性和治理/科学边界后才加入动态 authorized scope。
- [ ] 任务期间只在状态意外变化、大量证据页再次打开、跨会话/safe-suspend 恢复或怀疑无关修改时额外重跑全量清理脚本。

### H2. WIP / final commit verification

- [ ] 创建或 amend WIP、或创建 final commit 前，已重新运行清理脚本、`git status -sb`、`git status --short`、`git diff --stat`，并以入口 baseline 核对本轮变化。
- [ ] staged-only knowledge 文件被脚本保留且没有被误判为清理失败；substantive、mixed 或 unsafe 状态已按授权范围和 WIP 归属处理。
- [ ] pending WIP 的预期文件已检查 overlap：无重叠可独立；同一范围继续并 amend；依赖关系写入 queue；共享文件无法隔离时先 final 上游或暂缓，没有静默创建两个独立冲突 WIP。
- [ ] 普通摄入按 rolling WIP（如需要）→ Agent 自审 → final → 通过发布门后自动 push；独立 project/synthesis、跨来源研究结论和 claim-review 在等待人工审核或存在 hard P0 时保留本地 WIP、不 push；方案已确认且检查通过的治理、框架、脚本和说明任务可直接 final commit/push。
- [ ] 没有使用 `git add .` 或其它宽泛 stage；只显式 stage 本轮实际修改且用户授权的文件。
- [ ] commit 前已运行 `git diff --cached --name-only`、`git diff --cached --stat` 和 `git diff --cached --check`，完整 index 不含无关 `knowledge/`、`.obsidian/`、未授权 `raw/` 或历史 staged 文件。
- [ ] 提交前若 handoff/queue/report 需要描述尚未发生的 commit，只使用 `commit target` / `checkpoint commit message`；没有把 `planned`、`will create` 或 `expected checkpoint` 留作最终实际状态。

### H3. Post-commit / pre-push final check

- [ ] 每个 WIP、amend 或 final commit 成功后都执行 H3；WIP 因等待审核/hard P0/安全暂停而不 push 时记录原因，不能以“未获授权”作为默认原因。
- [ ] 已用 Git 解析实际 branch、HEAD subject、最终 commit hash 和提交文件，并核对 Active handoff、WIP queue 与报告；实际状态字段不再声称该 commit 仍是 `planned`、`will create` 或 `expected checkpoint`。
- [ ] 当前 commit 包含的仓库文件没有记录该 commit 自身的精确 hash；仓库内使用 branch + subject 作为稳定指针，最终 hash 只写入任务回执。父提交、其它分支或已固定 commit 的 hash 已明确区分。
- [ ] 若 post-commit reconciliation 需要修正当前任务的 handoff/queue/report，已显式暂存这些文件并 amend 同一 commit 一次，随后从头重跑 H3；未创建第二个 WIP 或纯状态 commit。
- [ ] commit 后、push 前已重新运行清理脚本，再运行 `git status -sb`、`git status --short`、`git diff --stat`、`git diff --cached --name-only` 和 `git diff --cached --check`。
- [ ] commit 后新出现的 unrelated `knowledge/**/*.md` 已按脚本结果和 baseline 分类；无法确认无实质差异、存在 mixed/conflict 或 overlap 未解决时没有 push。
- [ ] 没有提交 LF/CRLF-only dirty state；脚本未审批科学修改，也未替代 Codex 对授权范围、baseline 和 pending WIP 归属的判断。
- [ ] 已记录实际使用的 Git executable 与 `git --version`；Git 版本号不作为许可或拒绝条件。normal/system Git 与 Codex bundled Git 均可使用，但所选运行时必须通过以下仓库级预检；若 bundled Git 需要 `GIT_EXEC_PATH`，仅对该命令使用同一发行版的路径，未修改系统 `PATH`。
- [ ] `git rev-parse --git-common-dir` 已解析到当前 Wiki 的 common Git dir；若主工作树触发 dubious-ownership，只对该条命令使用精确的 `-c safe.directory=E:/imp/wiki`，未写 global/system `safe.directory`、通配符或其它项目路径。
- [ ] H3 fresh fetch、remote ancestry、`git push --dry-run origin HEAD:main` 和同一精确 refspec 的非 force push 均已检查；远端为 `https://gitee.com/chx6/silicon_graduate`。
- [ ] 正常发布路径的最终提交不写入 `push in progress`、`publication preflight in progress` 或“no remote action”等瞬时状态；成功后的远端结果只写任务回执。只有 push 失败时才把同一 final commit 对账为 `final-not-pushed` 并 amend handoff/queue。

- [ ] Git 工作树状态已检查；用户已有修改未被覆盖。
- [ ] `.gitignore` 没有把应持久化的 Markdown 知识页排除。
- [ ] `raw/` 中的大型 PDF、数据与个人材料未进入普通 Git 跟踪。
- [ ] 最终 diff 中不存在意外的 raw 修改。
- [ ] `USER_GUIDE.md` 与当前目录、命令和 Obsidian 工作流一致。
- [ ] 自动 lint 已运行且 error 为 0；warning/info 已解释。
- [ ] `knowledge/overview.md` 的页面级与 claim-level 统计在阶段性更新触发时已与最新 lint `GOVERNANCE` 输出同步；普通单篇摄入 deferred 时已说明。
- [ ] 可追溯性被用于区分证据层级和校准措辞，而不是禁止合理推断。
- [ ] 回答明确区分直接事实、作者解释、模型结果、跨来源综合和暂时推断。
- [ ] 证据不完整时已降低表述强度并说明限制，而不是无必要地拒绝回答。
- [ ] 普通问答、研究讨论、综合分析或早期草稿没有误用投稿级 paper evidence gate。
- [ ] Wiki miss 被表述为个人化上下文或已整理证据缺口，而不是自动拒答；普通问题在适当时仍补充稳定的一般专业背景。
- [ ] 一般专业背景与 Wiki-grounded、human-reviewed、externally verified evidence 分开标明，没有被冒充为 Wiki 证据；没有用模型记忆虚构论文、数据、locator 或作者结论。
- [ ] Wiki 直接支持的关键判断使用就地 informative line link；anchor text 让用户看出页面/文献名称和 `line N`，没有默认重复生成末尾证据区。
- [ ] 没有使用 `[内容页]`、`[打开证据位置]`、`[证据页]` 或其它无信息 anchor；没有只给裸页面名、slug、反引号包裹的 `[[wikilink]]` 或裸 `[[wikilink]]`；名称或 alias 有多个候选时列出已解析路径，没有猜测。
- [ ] 行号是在回答时读取目标文件后确定，落在直接承载判断的 claim、段落、表格行或小节内容，没有猜测行号或在可精确定位时只链接文件开头。
- [ ] 综合/推断使用校准措辞并并列最直接的 1-3 个链接；重要但 Wiki 缺直接证据的判断已在原处说明缺口和 provenance；一般背景没有被机械要求附链接。
- [ ] 已如实说明行号链接打开实际 Wiki 文件的实时渲染可编辑视图；若客户端不支持 `文件.md:行号`，已使用带页面名称和已核实小节/claim 定位的可点击 fallback，并说明未实现直接行号跳转。
- [ ] ordinary mode 没有默认显示 citation key、raw PDF、review 状态、完整 locator 或长 evidence card；原文核实、论文级审查或 strict paper mode 按需补充 citation key、raw PDF、review 状态、locator 和 claim-to-source 表，且未要求批量改写 Wiki 正文中的 Wikilink。
- [ ] 没有为了改变证据入口的打开界面而修改 source/project/synthesis、制造 fake/空白 diff、使用 `code-comment` 冒充只读入口或创建临时 commit。
- [ ] 综合或推断已标明其性质和主要支撑来源，没有伪装成来源直接结论。
- [ ] 没有把间接讨论误写成对强结论的直接支持。
- [ ] 没有虚构 citation、DOI、页码、图表编号、locator、原文或数据。
- [ ] 论文或投稿核查、正式引用、直接来源或原文引文、精确 locator、关键科学 claim 确认时已进入 strict mode，并回到直接来源、locator 和适用条件；普通争议讨论未被自动升级。
- [ ] 修改 lint 实现时，单元与仓库集成测试已通过。
