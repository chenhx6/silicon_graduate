# 一个月核结构研究生式训练：Docker 内 Codex CLI 操作计划

**目标:** 在 30 次成功的实质每日学习运行中，让硅基研究生形成可检查的核结构研究闭环：理论理解、实验谱学判读、证据审计、反证搜索、可复现小练习和独立研究问题设计。2026-09-22 的 Day 1/Day 2 运行只作 Docker/runner 实例验收，不计入这 30 天；正式周期从新的 `day_index: 1` 开始。

**运行环境:** Docker 容器内 `/workspace/wiki`；Codex CLI `0.155.1`；Docker daemon 模型优先级 `gpt-6-luna/max → gpt-6-sol/high → gpt-6-astra/medium`；GPT-5.6 已废弃；Codex 状态目录 `/root/.codex`；时区 `Asia/Shanghai`；当前仓库分支 `main`。

**规格来源:** `system/workflows/continuous-learning.md`、`system/workflows/autonomous-research.md`、`system/workflows/scheduled-continuation.md`、`PLAN.md` 和用户已确认的一个月训练设计。每日 runner 每次创建新的 Codex session；对应 `run.json` 保存 `session_id`、`session_mode` 和 `resume_command`。

博士论文导向的扩展规格见 [`2026-09-22-a130-triaxial-thesis-pipeline.md`](2026-09-22-a130-triaxial-thesis-pipeline.md)。每日训练同时承担课程能力和 A≈130 证据资产积累。

**全局约束:**

- 每日运行可按证据和信息增益自主推进 L1/L2/L3/L4；用户已授权 Docker 内 full-access、联网和可访问的真实/公开/模拟数据分析。
- L4 仍须具备输入、单位、不确定度、响应、协方差、代码和失败检查；缺失时写 readiness boundary，不生成代理结果。
- `raw/`、`PLAN.md`、`raw/zotero/wiki-inbox.bib`、用户临时文件和凭据不修改、不自动暂存。
- 不把模型结果写成实验事实，不把 Codex self-audit 写成 `human-reviewed`。
- 不用固定论文数量代表学习完成；每日以信息增益和能力产物验收。
- 外部检索允许联网使用 arXiv、NNDC/ENSDF、Google Scholar、Crossref、出版商和机构页面；记录 URL/DOI 与 locator，不把搜索摘要当作全文证据。

## 1. Docker 内的实际运行模式

### 1.1 单次交互式启动

用于首次建立训练会话、人工观察一轮或需要长篇讨论时：

```bash
cd /workspace/wiki
codex \
  -C /workspace/wiki \
  -m gpt-6-luna \
  -c model_reasoning_effort=max \
  -s danger-full-access \
  -a never \
  --search \
  --no-alt-screen
```

这里显式使用 Docker 容器内的 `danger-full-access`，避免嵌套 `workspace-write` 在当前内核中再次启动 bubblewrap；这是用户为本计划明确授权的运行方式。研究 prompt、`-C /workspace/wiki` 和 Gitee 恢复链路负责记录边界。不使用 `--dangerously-bypass-approvals-and-sandbox`。

中断后优先把 run receipt 中记录的 UUID 放入 shell 变量 `SESSION_UUID`，再续跑：

```bash
SESSION_UUID="$(jq -r '.session_id' outputs/learning-daily/$(TZ=Asia/Shanghai date +%F)/run.json)"
codex resume "$SESSION_UUID" -C /workspace/wiki -s danger-full-access -a never
```

只有确认最近一个 session 就是本训练任务时才使用：

```bash
codex resume --last -C /workspace/wiki -s danger-full-access -a never
```

### 1.2 无人值守单次运行

每日 daemon 在容器内调用 `codex exec`，每次调用创建新的 session，而不是复用一个永不退出的交互终端。`/root/.codex` 必须作为 Docker 的持久卷保留；禁止使用 `--ephemeral`，否则 session、失败恢复和 run receipt 不能跨容器重启保留。每个回执提供 `codex resume <session_id> ...`，用户可回到对应日期讨论。

标准命令形态：

```bash
RUN_DATE="$(TZ=Asia/Shanghai date +%F)"
mkdir -p "/workspace/wiki/outputs/learning-daily/$RUN_DATE"
codex \
  -C /workspace/wiki \
  -m gpt-6-luna \
  -c model_reasoning_effort=max \
  -s danger-full-access \
  -a never \
  --search \
  exec \
  --json \
  -o "/workspace/wiki/outputs/learning-daily/$RUN_DATE/last-message.md" \
  - < /workspace/wiki/system/prompts/daily-learning.md \
  > "/workspace/wiki/outputs/learning-daily/$RUN_DATE/events.jsonl" \
  2> "/workspace/wiki/outputs/learning-daily/$RUN_DATE/stderr.log"
```

`events.jsonl` 是 CLI 运行证据，`last-message.md` 是模型最终交接，`stderr.log` 只记录运行错误；三者不能替代当天的学习报告。没有 `run.json`、退出码和目标报告时，状态只能写成 `not-triggered` 或 `triggered-unverified`。

### 1.3 Docker 内调度、会话队列与 Farmer 的边界

- `system/scripts/run_daily_learning_daemon.py` 是 Docker 内每日时钟；它等待 `Asia/Shanghai` 22:00，调用同一容器内的 runner，并把调度状态写入 Wiki。
- `codex queue --thread "$SESSION_UUID" --message "$MESSAGE"` 只用于向一个仍存活的 CLI session 投递后续消息，不承担每日调度；`MESSAGE` 必须由调用脚本显式定义。
- `wiki_farmer.py` 只监视 rollout JSONL 并恢复允许的瞬时失败，不承担每日时钟；daemon 与 farmer 是两个独立的容器内进程。
- 当前容器启动脚本会在 `sleep infinity` 前后台拉起 daemon，因此不需要宿主机 cron、Task Scheduler、Docker socket 或外部 project automation。

## 2. 每日运行状态机

每次正式运行使用连续成功计数，而不是日历日期推进：`day_index` 只有在报告、检查和 checkpoint 全部成功后才加一。运行失败或被中断时，下次重复同一个 `day_index`，不跳过学习日。2026-09-22 的验收回执保留在历史目录并标记 `acceptance-only`，不参与正式计数。

### 启动阶段

1. 读取 `README.md`、`knowledge/index.md`、`profile.md`、`system/handoff.md` Active handoff、`PLAN.md`、最近 10 条 `system/log.md`、`system/learning-queue.md`、本计划和最近学习报告。
2. 运行 `git status --short --branch`、`python3 system/scripts/wiki_automation_preflight.py --root .` 和只读 QMD 状态检查。
3. 建立 dirty baseline；把用户已有的 `raw/`、临时 OCR/图片和其它未跟踪文件列为继承内容，禁止纳入本轮 stage。
4. 从 `knowledge/questions.md`、已有 project、最近八次 daily/weekly 报告和当前阶段覆盖债务构建候选池。

### 选择阶段

每轮最多两个槽位：

| 槽位 | 选择条件 | 本月优先例子 |
|---|---|---|
| Continuity | hard P0/P1、实质冲突或可能改变既有判断 | `131Ce` 集体模式、`135Pr/187Au` wobbling、`A2/A4–δ–Q(E)` 可识别性 |
| Novelty | 与近期 source fingerprint 不重叠的质量区、机制或方法 | `100Sn` 衰变、`61Ni` 方法谱系、`144/146Ba` 八极、A≈190 MR/shape coexistence |

候选按科学影响、可证伪性、独立证据、必要伴随 observable、数据可得性和预计信息增益排序。相同核素/project 不连续占用 novelty 槽；没有合格候选时记录 verified no-op，不凑论文。

### 学习阶段

每轮必须完成下列六项中的全部核心项：

1. **回忆:** 不看资料写出前一日的关键定义或公式。
2. **理论:** 推导一个最小关系，或解释公式中每个物理量的实验含义。
3. **主来源:** 完成一篇主文献的全文主线和关键图/表/公式/能级/误差阅读。
4. **反证:** 找到至少一个竞争解释、负例、null result 或必要伴随观测缺口。
5. **练习:** 完成一次表格重算、误差传播、能级纲图判读、公开数据查询、短代码/伪代码或实验设计检查。
6. **复述:** 用研究生口试式问答回答“作者声称什么、直接测了什么、还缺什么、什么结果会推翻它”。

### 收尾阶段

当天写入 `outputs/learning-daily/YYYY-MM-DD.md`，至少包含：

- `run_id`、时区、`day_index`、阶段和运行类型；
- 候选池、选择理由、来源指纹和重复/依赖关系；
- claim、locator、claim kind、evidence level、source independence；
- 支持、反证、替代解释、必要伴随 observable 和失败条件；
- 理论推导/练习结果；
- `Knowledge Impact and Learning Decision`；
- 新增或修订的问题、L0–L4 状态和停止原因；
- CLI session、退出码、lint、Git 和 QMD 状态；
- 下一轮 continuation prompt。

## 3. 一个月课程映射

`day_index` 与训练内容固定如下，具体文献由候选池动态选择：

逐日的回忆、主线阅读、定量/设计练习、反证检查和交付物见
[`2026-09-22-one-month-daily-task-matrix.md`](2026-09-22-one-month-daily-task-matrix.md)。

| 天数 | 训练模块 | Wiki 入口与能力验收 |
|---|---|---|
| 1 | 基线考试、单位、记号、研究契约 | 解释 `Jπ`、能级纲图、claim/evidence 层级；建立个人错题表 |
| 2–3 | 壳结构、单粒子、平均场 | 比较 shell gap、Nilsson/CSM/HFB 的适用条件 |
| 4–5 | 配对、形变、集体自由度 | 解释 `β2/β3/γ`、配对与 shape coexistence 的观测边界 |
| 6–7 | 转动、振动、alignment、signature | 从能级序列和 alignment 曲线识别竞争机制；完成第一次周考 |
| 8–10 | 角动量与电磁跃迁 | 推导/解释 `B(E2)`、`B(M1)`、selection rules 和矩阵元 |
| 11–14 | γ 谱学实验链 | 从反应布居、门条件、Doppler correction 到能级纲图；完成实验判据矩阵 |
| 15–17 | ADO/DCO/偏振/`δ` | 分离 `P/A/Q`、alignment、feeding、几何和 convention；做双解练习 |
| 18–20 | DSAM/RDDS/fast timing | 追踪 `τ→B(Eλ)→Qt` 假设链和系统误差 |
| 21 | 实验综合考试 | 给定未知谱学描述，写出可接受和不可接受的结构结论 |
| 22–23 | wobbling 与 signature partner | `135Pr/187Au/131Xe` 支持与反证逐对比较 |
| 24–25 | chirality 与 shape coexistence | `134Pr/135Nd/136Nd` 的 partner-resolved evidence 和替代解释 |
| 26 | octupole、E1/E3、磁/反磁转动 | 建立直接观测—间接解释—模型结果证据梯度 |
| 27 | 跨质量区迁移 | A≈80/100/130/160/190 同位素/同中子素比较；说明不适用处 |
| 28 | 自主 L3 研究日 | 从问题池选一题，完成 evidence map、falsifier 和 prospectus |
| 29 | 研究设计答辩 | 提出最小测量、响应/背景、负例和 belief-revision 条件 |
| 30 | 综合口试与月度报告 | 理论题、谱学题、争议论文题、研究设计题各一项 |

## 4. 持久化与 Git 操作

本月使用两条轨道：

- **每日轨道:** 写 daily report、run receipt、checkpoint 到 `outputs/learning-daily/`；可复用知识写回 `knowledge/`；runner 每次创建新 session，并在回执中保存 session ID 和 resume 命令；无实质变化只写 verified no-op receipt。
- **每周轨道:** 第 7、14、21、28 天形成 weekly REFLECT、更新 milestone 和问题排序，运行完整 lint/QMD/保护路径检查，再按既有发布门提交/推送。

每日计划的主要写入路径包括：

- `outputs/learning-daily/`
- `outputs/learning-weekly/`
- `outputs/learning-milestones/`（阶段报告、调度状态和运行回执）
- `knowledge/` 下的 source、project、synthesis、research-note、questions 和必要关联知识页
- `system/handoff.md`、`system/log.md`、本月计划和明确的 L3/L4 报告

Docker full-access 允许 runner 为 L1–L4 任务读写 Wiki 内其它必要路径；新增路径必须在日报、回执和 handoff 中列出用途。Git 仍使用显式文件清单，禁止 `git add .`；凭据、宿主机状态、Docker socket 和无关项目不属于授权范围。

## 5. 中断、失败和恢复

| 情况 | 状态 | 恢复动作 |
|---|---|---|
| Docker/CLI 在来源阅读中断 | `interrupted` | 保留 `events.jsonl`、last message 和 checkpoint；把 receipt 的 `session_id` 赋给 `SESSION_UUID` 后执行 `codex exec resume "$SESSION_UUID"` |
| Codex 瞬时网络/服务错误 | `retryable-failure` | 仅对 allowlisted transient error 重试一次；由 farmer 监视，不循环重试认证/权限错误 |
| 外部全文需要登录/CAPTCHA | `blocked-needs-source` | 记录 DOI、访问路线和缺失 locator，不把 HTML 当全文，不绕过控制 |
| Git/保护路径检查失败 | `safe-suspended` | 不新增科学 claim；写 handoff，等待下一次 CLI 运行或用户处理环境 |
| L4 输入不完整 | `not-ready` / `candidate-L4` | 写 readiness audit，不启动伪分析；本计划可自主继续其它 L1–L4 路线，不等待额外启动语句 |
| 运行没有 receipt | `not-triggered` | 不把日期计入 30 次成功运行；下一轮重复同一 day_index |

Docker 重启后，`/workspace/wiki` 和 `/root/.codex` 必须仍可读写；否则只能报告“容器启动但 session 未恢复”，不能声称连续学习不中断。

## 6. 首次实现文件与接口

在第一个 day 1 运行前，先建立以下三个仓库内文件；只建立运行骨架，不预写科学结论：

- `system/prompts/daily-learning.md`：每日 Codex 指令契约。它接收 runner 注入的 `RUN_DATE`、`DAY_INDEX`、`PHASE`、最近 checkpoint 和允许写入路径，要求模型完成本计划第 2 节的状态机并输出当天报告。
- `system/scripts/run_daily_learning.py`：Docker 内唯一启动器。接口为：

  ```text
  python3 system/scripts/run_daily_learning.py \
    --root /workspace/wiki \
    --day-index auto \
    --mode daily-learning
  ```

  `--dry-run` 只检查 CLI、Docker 路径、持久化 `/root/.codex`、锁、提示词和输出目录；正常运行创建 `run.json`，获取互斥锁，调用本计划 1.2 的 `codex exec` 命令，保存 `events.jsonl`、`last-message.md`、退出码和 session UUID，并且只有报告与检查成功时推进 `day_index`。
- `system/tests/test_daily_learning_runner.py`：测试日期/时区、day-index 不跳号、并发锁、用户 dirty baseline 不进入允许文件、Codex 非零退出、无 receipt 和 `--dry-run`。测试不得调用真实模型。
- `system/scripts/run_daily_learning_daemon.py`：Docker 内每日调度器；默认每日 22:00（`Asia/Shanghai`）调用 runner，提供 `--dry-run` 和 `--once`，使用单实例锁和持久化调度回执。

容器内启动命令：

```bash
python3 system/scripts/run_daily_learning_daemon.py --root /workspace/wiki --dry-run
python3 system/scripts/run_daily_learning_daemon.py --root /workspace/wiki
```

daemon 直接在容器内启动 runner；容器启动竞态、runner preflight 和科学验证失败均保留为可核验回执，不通过宿主机重试或隐式跳过。

runner 的允许写入清单、失败状态和恢复路径必须与本计划一致；它不能执行 `git add .`，不能读写凭据，不能自动修改 `raw/`、`PLAN.md` 或受保护 BibTeX。

## 7. 能力验收

第 1、7、14、21、28、30 天分别进行一次 Codex 口试。每项 0–4 分，目标不是分数总和而是没有关键短板：

1. 理论概念和公式推导；
2. 能级纲图、门条件和实验观测量判读；
3. 误差、响应、feeding、背景和协方差意识；
4. 事实/作者解释/模型/自身推断分层；
5. 竞争解释、反证和必要伴随观测；
6. 可证伪研究问题和最小实验设计。

第 30 天产出一份 research prospectus：问题、已有证据、竞争假设、最小 observable 组合、数据需求、失败检查、预期 belief revision 和下一阶段文献/实验路线。

## 8. 验收标准

计划在以下条件同时满足时结束：

- 30 次运行均有真实 receipt，失败日没有被计数；
- 4 份 weekly REFLECT 和 1 份月度 prospectus 存在且能从 source/locator 回溯；
- 至少 2 个问题完成 L3 milestone，且各自有支持、反证、停止条件和下一步；
- 至少 1 次公开数据/模拟 L4 readiness audit；若输入满足条件，才增加真实 L4 run；
- 最终口试能指出不确定性和未知，而不是只复述结论；
- lint、测试、受保护文件哈希、Git 发布门和 Docker session 回执均可核验。

## 9. 首次启动顺序

本计划写入后，首轮不直接跳入论文摄入，而按以下顺序启动：

1. `python3 system/scripts/wiki_automation_preflight.py --root .`
2. `qmd status`
3. `git status --short --branch`
4. 运行 day 1 baseline prompt；生成当天报告和 session receipt。
5. 只有 day 1 报告、检查和 checkpoint 完整后，才把 `day_index` 置为 1，并进入 day 2。
