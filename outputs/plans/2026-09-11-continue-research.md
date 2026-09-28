# 学位论文批次持续研究、温故知新与发布计划

## 总目标

以 现有任务书 (outputs/plans/2026-09-10-degree-dissertation-corpus-ingest.md) 作为长期执行入口，继续开展原文检索、跨来源 L3、具备条件的公开数据 L4，以及已有知识复核。研究由 Codex 自行完成 self-audit，不以用户
提前审核作为前置条件；研究结束后完成交接、final commit 和 push。

科学冲突、暂定能带指认、缺寿命、缺绝对强度和模型竞争解释可以保留为有边界的 partially-researched 或 stopped。来源身份、哈希、raw、权限、凭据、危险重叠和 Git 安全问题才属于阻塞性 hard P0。

## 持久化规则

更新当前任务书，并同步修改：

- AGENTS.md
- system/workflows/ingest.md
- system/workflows/reflect.md
- system/workflows/autonomous-research.md
- system/paper-evidence-gate.md
- check.md
- USER_GUIDE.md
- system/memory.md

统一写入以下规则：

- 研究摄入、L3/L4、跨来源综合和批次收尾由 Codex self-audit 完成。
- Codex 不主动要求用户审核 source、P0/P1 或研究报告。
- review_status、needs_review 保留为证据成熟度记录，但不阻止普通研究继续、批次收尾、final commit 或 routine push。
- human-reviewed 只表示真实用户审核；Codex self-audit 不伪装成用户审核。
- 用户审核只在后续问答需要裁决具体说法，或论文写作需要使用具体 claim 时触发。
- 研究结果即使包含 partial/stopped 项，只要技术安全和证据边界完整，也可以 final 并发布。
- 根目录 PLAN.md 保持用户宏观计划性质，不纳入本任务修改。

任务书增加“持续执行协议”，记录长期目标、研究顺序、软时间预算、温故知新入口、L3/L4 条件、停止规则、self-audit 和发布步骤。system/handoff.md 记录当前执行位置，system/wip-queue.md 只保留短恢复索引。

## 研究主路线

### 1. 135Nd D3/D4 原文 crosswalk

检索并获取最初论文、博士论文引用 [128]、后续重新分析、修订能级图、作者版本和勘误。

逐篇比较：

- D3/D4 带头和逐线跃迁；
- parity、自旋、R_DCO、R_ac 和连接关系；
- 后发论文如何解释前文的错误或序列调整；
- 哪一版本目前证据最强；
- 哪些内容仍无法裁决。

允许结论为“后续论文修正了早期指认”，也允许结论为“源内冲突已定位但外部证据不足”。不强行选择最终 parity。

### 2. 100Sn、131Ba 和 87Zr

建立定量和谱系交叉表：

- Hinke/Lubos 的 half-life、endpoint/Q、B(GT)、branching、response correction 和 model-space；
- Qiang 的 87Zr τ=1017(16) ps、B(E2)、B(M1)、混合比和内转换输入；
- Qiang、Guo、Ding 的 131Ba shared-GALILEO lineage；
- 130Ba 9.4/9.5 ms 差异及 g-factor/B(E2) 派生误差。

### 3. 135Pr/187Au

继续检索支持方、反方和后续解释来源，复核：

- mixing-ratio 分支；
- polarization 和 R_ac；
- weak links、band identity 和 coincidence closure；
- lifetime、absolute B(E2)/B(M1)；
- Sensharma、Lv、Guo 的实验和理论依赖。

输出每个争议的支持证据、反证、替代解释、缺失伴随观测和 belief-revision 条件。

### 4. 公开数据 L4

优先检查：

1. 16C 75/240/400 MeV/u 的公开截面和 R_s；
2. 135Nd/136Nd 已发表的逐线跃迁和 transition-strength 数据；
3. 32S reorientation 的公开 yield、GOSIA 输入或可靠数字化结果；
4. CSR Gamma Ball 后续工程论文、几何、效率曲线或 GEANT4 输入。

只有具备来源、哈希、locator、单位、不确定度、分析代码、参数和 sensitivity/negative-control 条件时才启动 L4。

## 温故知新复核槽

完成当前高优先级新证据路线后，只要仍有执行余量，就进入已有知识复核。它不是固定数量任务，也不要求为了填时间机械重读。

优先选择以下类型：

- 新学位论文可能改变的旧结论；
- 旧页面存在来源冲突、过强措辞或模型/实验混写；
- 争议主题缺少反证或替代解释；
- 同一实验的 thesis、journal、review lineage 可能重复计数；
- 已有知识与新获得的后续论文存在能带、寿命、强度或模型差异；
- 高信息增益但长期未复核的 A≈130 主题。

首轮候选优先级：

1. 131Ba MχD、pseudospin、E1 和 signature splitting；
2. 135Nd/136Nd MχD 与 TiP 竞争解释；
3. 135Pr/187Au wobbling、TiP、single-particle 和 signature-partner 解释；
4. 131Ce lifetime、γ-soft、wobbling/chirality 边界；
5. 74As/78Br chirality、pseudospin 和 octupole-correlation crosswalk；
6. 100Sn B(GT)、106Ag DSAM 和其它已有独立性争议。

每个温故知新单元至少形成以下一种实质产出：

- 旧结论得到支持；
- 旧结论被限制或降级；
- 新来源修正旧能带、跃迁、寿命或组态；
- 补齐来源依赖和独立性；
- 发现新的可检验问题；
- 确认当前没有 material change，并记录原因。

复核仍必须回到 source/raw locator，区分实验事实、作者解释、模型结果和 Codex 综合。没有新的判断变化时，只保留简短审计记录，不制造重复页面或空泛报告。

## 时间策略

12 小时是首个软检查点，不是硬截止，也不是产出配额。

- 前 12 小时优先处理仍可能改变核心判断的原始来源和 L3/L4 单元；
- 到 12 小时时完成当前正在处理的原文、表格或计算单元；
- 若仍有高信息增益来源或温故知新项目，继续执行；
- 若外部来源不可得、数据不足、证据重复或继续工作只增加背景，则停止该路线；
- 研究完成后不因为还有时间而制造低价值修改；
- 停止时记录已完成范围、未决问题、停止原因和下一路线；
- 12 小时后暂停时，仍完成报告、handoff、WIP 对账、final commit 和 push。

执行顺序采用动态排序：

135Nd 原文 → 100Sn/131Ba/87Zr → 135Pr/187Au → 可行 L4 → 温故知新 → 其它高信息增益问题 → 收尾

## 文件、数据和 Git

外部论文先进入：

raw/papers/gpt/_incoming/<run-id>/

- git fetch origin main；
- git merge-base --is-ancestor origin/main HEAD；
- git push --dry-run origin HEAD:main；
- git push origin HEAD:main。

当前 d030be4 作为 rolling WIP 延续。研究、温故知新、规则同步和 Codex self-audit 完成后，将当前 WIP amend 为：

Finalize degree dissertation corpus L3/L4 research 20260912

随后完成 post-commit reconciliation，核对提交文件、handoff、queue 和远端状态。若网络或认证失败，保留 final commit，记录 final-not-pushed，不修改凭据或 Git 全局配置。

## 默认假设

- 不主动向用户索要本批次人工审核。
- 用户后续问答或论文写作需要具体 claim 时，再进行针对性核验。
- partial/stopped 是允许的科研状态，不等于任务失败。
- 135Nd 的原文冲突可以通过后续论文解释，也可以在证据不足时作为已定位边界归档。
- 公开数值数据在具备 manifest、代码、参数和失败检查时可以进入 L4。
- 12 小时后若仍有高信息增益任务，继续研究；若信息增益下降，完成交接和发布。
- 本计划已由用户批准进入执行阶段；执行时按上述规则修改治理文件、检索原文、开展 L3/L4 和温故知新，并在 self-audit 后完成交接、commit 和 push。
