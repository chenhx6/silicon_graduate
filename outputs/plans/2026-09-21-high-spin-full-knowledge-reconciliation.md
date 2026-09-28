# 高自旋文献全库综合、一致性审计与问题驱动补证计划

**目标:** 在已完成高自旋文献集合阅读的基础上，把来源事实、方法边界、竞争解释、研究问题和外部补充文献整合进 Wiki 的全库知识网络，并完成可追溯的一致性审计。

**当前基线:** 原始清单 127 条；用户确认污染排除 9 条；有效条目 118 条；唯一 SHA-256 110 个；精确重复副本 8 条；当前台账包含 102 个 `read-and-source-created`、8 个 `reused-and-audited-existing-source`、7 个 `audited-reused-duplicate` 和 1 个 `attached-material-read-and-audited`。这些数字分别表示台账行状态，不能直接当作独立论文数或独立实验数。

**范围:** 以当前 118 个有效高自旋来源为固定初始语料；在具体研究问题暴露证据缺口时，允许主动检索和纳入新的外部来源。外部来源必须单独编号、记录来源增量和依赖关系，不改变原 127 条清单的分母。

**不在本计划中的事项:** 不恢复用户删除的 9 个污染 PDF；不移动、覆盖或重命名 raw 原件；不把综述、预印本、学位论文和同一实验的多个版本计为独立实验；不把模型结果写成实验事实；不把 Codex self-audit 改写成 `human-reviewed`。

**计划状态:** 待用户审阅。用户明确开始后，按本文件顺序执行；本文件审阅阶段只写计划，不修改科学页面。

## 一、全库更新的判定方式

这里的“全库更新”定义为：所有受到本批证据影响的知识节点都能从来源页回溯到原文 locator，并且在跨来源综合、研究问题、索引和状态统计中保持一致。它不意味着重写每一个与高自旋无关的页面。

需要纳入影响面审计的层级如下：

| 层级 | 必查对象 | 更新条件 |
| --- | --- | --- |
| 来源层 | `knowledge/sources/`、`outputs/high-spin-learning-20260920/ledger.json` | 身份、版本、raw 哈希、覆盖范围、claim 表、自审状态或 source slug 不一致 |
| 方法层 | `knowledge/methods/` | 新来源改变公式、标定、效率、对齐、符号约定或适用条件 |
| 概念层 | `knowledge/concepts/` | 新来源改变定义、必要观测量、竞争解释或证据等级 |
| 模型层 | `knowledge/models/` | 新来源改变模型参数、近似、适用区间或失败条件 |
| 观测量层 | `knowledge/observables/` | 新来源增加数值解释、误差传播或 convention 边界 |
| 核素/能带/实验层 | `knowledge/nuclei/`、`bands/`、`experiments/` | 来源提供可复用的结构身份、能级、实验或反应信息 |
| 项目与综合层 | `knowledge/projects/`、`knowledge/synthesis/` | 至少两类来源存在支持、反证、时间演化或竞争解释 |
| 全局入口层 | `knowledge/index.md`、`knowledge/overview.md`、`knowledge/questions.md` | 新实体、新问题、规模统计或开放缺口发生变化 |
| 研究状态层 | `outputs/`、`system/handoff.md`、`system/log.md` | 每阶段需要跨会话恢复或审计回执 |

## 二、执行原则

1. **先建立影响图，再编辑共享页面。** 先从 ledger、source frontmatter、wikilink 和 claim 表生成影响清单；共享页面写入前检查同一文件是否已被其他 WIP 修改。
2. **证据层分离。** 每个主张分别记录实验直接报告、作者解释、模型结果、Agent 推导和跨来源综合；不因多个来源重复引用而提高独立证据等级。
3. **先修身份和 locator，再做综合。** source slug、raw 哈希、版本关系、页码和图表定位未修好时，不把该主张提升到项目结论。
4. **冲突保留。** 对数值、符号、反应、带号、模型参数和结论冲突建立冲突表，保留双方原文和适用条件；不静默取平均或用最新文献覆盖旧文献。
5. **研究问题驱动外部补证。** 不为增加文献数量而搜索；只有现有 corpus 无法回答一个具体问题、无法区分竞争假设或存在关键历史断点时才检索。
6. **外部全文可追溯。** 检索优先使用 DOI/Crossref、OpenAlex、INSPIRE、arXiv、出版社开放版本、机构仓储、作者仓储、补充材料和合法机构访问。自动化下载遵守站点条款、robots、速率限制和缓存哈希；不自动绕过访问控制或批量抓取未经授权的受版权保护副本。用户若另行提供可合法使用的 PDF，按同一身份、哈希、locator 和自审流程处理。
7. **L3 与 L4 分开。** 文献比较、反证和可区分预测可以完成 L3；只有输入、代码、单位、不确定度、响应处理、负例和复现路径齐全时才建立 L4 run。
8. **结论必须能停止。** 每个综合主题和 L3 单元都写出完成条件、证据不足条件、停止原因和后续路线，避免无限检索。

## 三、文件结构与产物

执行期间新增或修改的主要文件如下：

- 新建计划：`outputs/plans/2026-09-21-high-spin-full-knowledge-reconciliation.md`。
- 既有逐条状态：`outputs/high-spin-learning-20260920/ledger.json`。
- 追加事件：`outputs/high-spin-learning-20260920/ledger-events.jsonl`。
- 阅读交接：`outputs/high-spin-learning-20260920/checkpoint.md`、`system/handoff.md`。
- 批次报告：`outputs/high-spin-learning-20260920/report.md`。
- 全库影响审计：`outputs/high-spin-reconciliation-20260921/impact-map.md`、`outputs/high-spin-reconciliation-20260921/claim-conflicts.md`、`outputs/high-spin-reconciliation-20260921/knowledge-update-ledger.json`。
- 主题综合：`knowledge/synthesis/` 下按主题建立或更新页面；每页必须链接来源页和原文 locator。
- 外部补证：`outputs/high-spin-reconciliation-20260921/external-research/EXT-*.json` 与对应的 `knowledge/sources/` 页面。
- L3/L4 状态：`outputs/high-spin-reconciliation-20260921/research-units/`，L4 成果仅在输入满足条件时写入 `outputs/l4/`。

`knowledge/overview.md` 和 `knowledge/questions.md` 只在影响图完成后更新，避免在未对账时生成过时统计或问题清单。

## 四、执行任务分解

### Task 1：冻结语料与建立影响图

**文件:**

- 读取：`outputs/high-spin-learning-20260920/ledger.json`、`ledger-events.jsonl`、`checkpoint.md`、`report.md`、`knowledge/index.md`。
- 新建：`outputs/high-spin-reconciliation-20260921/impact-map.md`、`knowledge-update-ledger.json`。
- 修改：无共享知识页修改。

**Consumes:** 当前 127 行 ledger、source frontmatter、wikilink、项目页和已提交版本 `8b94431`。

**Produces:** 每个有效条目的 source slug、关联节点、依赖来源、拟更新页面、是否存在冲突、是否需要外部补证和优先级。

**步骤与验证:**

1. 读取每个有效条目的 `source_slug`、`knowledge_links`、`issue_ids`、`l3_l4_units`、`self_audit_status`。
2. 从 source 页 frontmatter 和正文提取所有 wikilink，并按 `source → method/concept/model/observable → project/synthesis` 建立边。
3. 将边分为 `supports`、`limits`、`revises`、`conflicts`、`methodological-bridge`、`same-source-dependency`。
4. 运行唯一性检查：每个 valid ledger row 有 source 映射或明确的复用/附件路线；每个 duplicate row 有逐条自审；每个 source slug 指向实际文件。
5. 运行：`python3 system/scripts/wiki_lint.py --fail-on error`。预期：`errors=0`；warnings/info 逐项记录，不把既有 `needs_review` 当成错误。

### Task 2：修正身份、版本和来源页一致性

**文件:**

- 修改：`outputs/high-spin-learning-20260920/ledger.json`、`ledger-events.jsonl`、对应 `knowledge/sources/*.md`。
- 重点检查：HS-012、HS-017、HS-029、HS-053、HS-070/071、HS-085/086、HS-094、HS-105–108、HS-116、HS-126，以及所有 source slug 与文件名的映射。

**Consumes:** Task 1 影响图、原始 PDF 哈希、现有 source frontmatter。

**Produces:** 无孤立 source、无错误父子关系、无误计独立实验、无缺失附属材料说明的来源层。

**步骤与验证:**

1. 对每个版本或附属材料比较标题页、作者、DOI、页数、图表和关键结论。
2. 修复 source slug 与 ledger 的双向映射；任何修复都追加 ledger event，不重写历史事件。
3. 对复用来源写明“已复核内容”和“未重新阅读内容”；对附件写明父 source、覆盖范围和不计独立实验原因。
4. 对每个 raw 文件运行 SHA-256 对账；对污染文件只保留用户排除记录。
5. 运行定向脚本，预期 `missing_source=0`、`hash_mismatch=0`、`unreviewed_duplicate=0`。

### Task 3：统一 claim、locator 和自审格式

**文件:**

- 修改：受影响的 `knowledge/sources/*.md`、方法页和概念页。
- 保持：`review_status` 的真实状态；不得自动写成 `human-reviewed`。

**Consumes:** Task 2 的 source identity 结果、原文页码/图表/公式定位。

**Produces:** 统一的 `Key Results` claim table、`Analytical Reconstruction and Self-Audit`、`Competing Interpretations and Limitations` 和 `Human Review Triage`。

**步骤与验证:**

1. 每个重要 claim 至少包含 `claim_kind`、`evidence_level`、`locator`、`needs_review`。
2. locator 使用 PDF 页码、章节、公式、图、表、能级或明确扫描页位置；不可读处写边界，不补猜数值。
3. 把实验结果、作者解释、模型结果和 Agent 推断拆成不同 claim。
4. 对综述、评论和同实验版本建立来源谱系，禁止把引用数量当作独立实验数。
5. 运行 lint，预期 `claim_missing_locator=0`、`claim_missing_kind=0`、`errors=0`。

### Task 4：主题一——角分布、角关联、偏振和混合比

**文件:**

- 修改：`knowledge/methods/angular-distribution.md`、`angular-correlation.md`、`compton-polarimetry.md`、`linear-polarization-asymmetry.md`、`knowledge/observables/multipole-mixing-ratio.md`。
- 新建或更新：`knowledge/synthesis/high-spin-angular-polarization-mixing-ratio.md`。

**Consumes:** Yamazaki、Rose–Brink、Taras、Hamilton、Suffert、Lange、DCO/PDCO/PPCO、CLOVER/GeLi/SeGA/AFRODITE 来源及其 locator。

**Produces:** 一张方法证据表，明确 `δ` sign convention、alignment/`σ/J`、detector `Q`、efficiency、finite-angle、cascade order、DCO/ADO/PDCO/PPCO 的可迁移边界。

**必须回答的问题:**

- 哪些观测只约束 multipole combination，哪些能区分 electric/magnetic character？
- `δ` 的符号如何在 angular distribution、γγ correlation 和 polarization 之间转换？
- 哪些参考线和 `R_DCO/R_ADO/Q(E)` 只能在阵列内使用？
- alignment、side feeding 和 detector response 的协方差是否使某些来源的 δ 不可识别？

**停止条件:** 若某个方法的通用化需要原始响应矩阵或未公开代码，保留方法边界和 L3 问题，不继续外推。

### Task 5：主题二——寿命、跃迁强度、形变和高自旋机制

**文件:**

- 修改：`knowledge/methods/doppler-shift-attenuation-method.md`、`knowledge/concepts/angular-momentum-alignment.md`、`band-termination.md`、`rotating-mean-field.md`、相关 `models/`。
- 新建或更新：`knowledge/synthesis/high-spin-lifetime-strength-deformation.md`。

**Consumes:** Jensen、Mukhopadhyay 2007/2008、Petrache、Herzáň、Afanasjev、Nolan、Walker 等来源。

**Produces:** DSAM/RDDS/RDM 证据链、`τ → B(E2)/B(M1) → Qt` 的假设清单，以及 configuration crossing、band termination、magnetic rotation、collectivity 的竞争解释矩阵。

**必须回答的问题:**

- 哪些 `B(E2)/B(M1)` 差异足以反驳“同一理想伙伴带”？
- stopping power、feeding、side feeding 和 gate selection 如何传播到形变判断？
- `Qt`、`B(E2)`、alignment 和 band crossing 是否指向同一组态？

### Task 6：主题三——chirality、wobbling、γ-softness 与 shape coexistence

**文件:**

- 修改：`knowledge/projects/nuclear-chirality-and-multiple-chiral-doublet-bands.md`、相关 `concepts/` 和 `models/`。
- 新建或更新：`knowledge/synthesis/chirality-wobbling-competition-evidence.md`。

**Consumes:** Mukhopadhyay 2007/2008、Petrache 2006/2018、Guo 2024、Grodner、Garg、Rees、Frauendorf、Nomura、Eldridge 等来源。

**Produces:** 按核素和 pair 分开的证据矩阵，分别记录 near-degeneracy、alignment、`B(M1)/B(E2)`、interband E2、lifetime、g factor、TAC/PRM/IBFM 结果及替代解释。

**必须回答的问题:**

- 哪些 fingerprints 是必要条件，哪些只是模型内趋势？
- crossing、configuration mixing、γ vibration、shape coexistence 和 pseudospin 如何解释相同能谱现象？
- 每一对候选带最小需要哪组伴随观测才能改变结论排序？

**停止条件:** 不能把多个核素的相似 band label 合并为一个 global conclusion；缺少 partner-resolved strength 或 lifetime 时保持 candidate。

### Task 7：主题四——octupole、双光子和滴线衰变

**文件:**

- 修改：`knowledge/concepts/octupole-deformation.md`、`octupole-correlation.md`、`two-photon-nuclear-decay.md`、`drip-line-radioactivity.md`。
- 新建或更新：`knowledge/synthesis/octupole-and-rare-electromagnetic-decay.md`。

**Consumes:** Butler–Nazarewicz、Gaffney、Bucher、Li、Walz+SI、Söderström、Schirmer、Kramp、Henderson、Dey 等来源。

**Produces:** 直接 E3、E1 correlation、PES `β3`、γγ timing/energy/angle、M2E2/E3M1、2p/cluster decay 的证据层级和冲突表。

**必须回答的问题:**

- 什么是直接 E3 观测，什么只是 E1/systematics/PES 的间接解释？
- Walz 与 Söderström 的双光子多极路径冲突由哪些独立 observable 解决？
- 滴线的 2p/cluster 结论哪些受原始数据不可得限制？

### Task 8：全库入口、问题和统计更新

**文件:**

- 修改：`knowledge/overview.md`、`knowledge/questions.md`、`knowledge/index.md`、受影响的 `projects/`。
- 追加：`outputs/high-spin-reconciliation-20260921/knowledge-update-ledger.json`。

**Consumes:** Tasks 1–7 的影响图和主题综合。

**Produces:**

- 重新统计 source、nucleus、band、method、model、project 和 unresolved question 数量；
- 删除或修复孤立链接、错误 slug、重复实体和旧的“未审计/缺附件”表述；
- 把每个开放问题链接到支持、反证、所需观测量和停止条件；
- 保留未纳入本批的旧文献和其它项目，不把它们伪装成本批已重审。

**验证:** `python3 system/scripts/wiki_lint.py --fail-on error`；自定义反向链接检查；ledger 与 index 数量对账；`qmd update` 后检查 collection 文件数。

### Task 9：问题驱动的外部检索与补充来源

**文件:**

- 新建：`outputs/high-spin-reconciliation-20260921/external-research/EXT-*.json`。
- 新建或修改：对应 `knowledge/sources/*.md`、`knowledge/projects/`、`knowledge/questions.md`。

**Consumes:** Tasks 4–7 产生的具体 evidence gap；每个 gap 必须有 question ID。

**Produces:** 每个外部研究单元包含：

- question、scope、核心 claim 和竞争假设；
- 检索式、数据库、日期、时间范围、纳入/排除标准；
- DOI、作者、题名、版本、下载来源、SHA-256、是否同一实验；
- 证据 locator、增量、与现有来源的支持/冲突关系；
- 外部来源是否改变 belief ranking、是否进入 L3/L4，以及停止原因。

**检索顺序:** DOI/Crossref/OpenAlex/INSPIRE → arXiv/机构仓储/作者版本 → 出版社开放全文或合法机构访问 → 补充材料、数据仓储和代码仓储。自动检索必须遵守站点条款、robots、速率限制和缓存哈希；不自动绕过访问控制或批量抓取未经授权的受版权保护副本。用户提供可合法使用的全文后，可直接进入同一审计流程。

**停止条件:** 找不到全文时记录 metadata-only/blocker；来源只重复已知证据时记录 no-material-increment；关键数据缺失时转 L4 readiness，不用推测填补。

### Task 10：L3 研究单元与条件式 L4

**文件:**

- 新建：`outputs/high-spin-reconciliation-20260921/research-units/L3-*.md`。
- 条件满足时新建：`outputs/l4/<unit-id>/manifest.json`、`analysis/`、`decision.md`、`failure-checks.md`。

**Consumes:** Tasks 4–9 的 evidence matrices、外部来源和公开数据/代码。

**Produces:** 每个 L3 单元包含假设、必要伴随观测、判别预测、证伪路径、停止条件和认识修正条件。L4 只有在具备原始数据/公开数值、单位、不确定度、响应、代码/参数、随机种子或复现步骤、负例和失败检查时才启动。

**候选问题:**

- `137Ba` 双光子衰变的 E3M1/M2E2 path separation；
- A≈130 chiral candidate 的最小 partner-strength/lifetime evidence；
- E1 correlation 与 direct E3 之间的 octupole evidence ladder；
- alignment/δ/detector-response covariance 对跨阵列结论可迁移性的限制。

**L4 停止条件:** 真实原始数据、响应文件、代码或许可缺失时，只输出 readiness 和失败条件，不生成伪结果。

### Task 11：最终自审、报告和发布

**文件:**

- 修改：`outputs/high-spin-learning-20260920/report.md`、`checkpoint.md`、`system/handoff.md`。
- 可能修改：`knowledge/overview.md`、`knowledge/questions.md`、主题 synthesis 页。

**验证序列:**

1. `python3 system/scripts/wiki_lint.py --fail-on error`，预期 `errors=0`。
2. `git diff --check` 和 staged diff 检查。
3. raw SHA-256、127 行、118 valid、9 excluded、110 unique hash 对账。
4. protected BibTeX 基线核对：`python3 system/scripts/wiki_automation_preflight.py`。
5. `qmd update`；有条件时 `qmd embed`，记录 pending/orphan 状态。
6. 审核 source → domain → project/synthesis 反向可达性和 duplicate lineage。
7. 形成简洁文献汇报：统计、主题结论、主要冲突、L3/L4 状态、真实缺口和下一问题。
8. 用户审阅本计划并明确开始后，按现有持续发布授权执行 `git fetch origin main`、祖先检查、`git push --dry-run origin HEAD:main` 和非 force 精确 refspec；发布回执写入 handoff。

## 五、验收标准

完成本计划时，必须同时满足：

- 118 个有效条目全部有身份、阅读/复用路线、知识影响、自审和下一状态；
- 8 个重复副本逐条有映射和自审，不增加独立实验数；
- 每个新增或修正的重要 claim 有 source、locator、claim kind 和 evidence level；
- 所有受影响的概念、方法、模型、观测量、项目、问题和全局入口已对账；
- 每个主题至少保留支持、反证、竞争解释和适用条件；
- 外部补充文献单独编号并有检索、身份、哈希、增量和停止记录；
- L3 有问题定义和停止条件；L4 只有真实输入齐全时才有 run；
- lint 错误为 0，哈希和 protected BibTeX 对账通过，QMD 状态如实记录；
- 报告可以由下一次会话依据本计划、ledger、checkpoint 和 handoff 独立恢复。

## 六、用户审阅点

请重点审阅以下三点后再开始执行：

1. “全库更新”是否按受影响节点更新，而不是机械重写全部页面；
2. 外部检索是否按问题驱动、独立编号，并将新来源与原 127 条分母分开；
3. L3/L4 的停止条件是否足够严格，尤其是原始数据、响应文件和代码不可得时是否只记录 readiness。
