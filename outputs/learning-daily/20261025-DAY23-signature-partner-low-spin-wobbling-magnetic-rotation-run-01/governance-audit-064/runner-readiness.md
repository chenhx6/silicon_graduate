# Day23同session收束readiness：用户延长至17:00后的实际缺口

只读代码与现有回执检查，观测时刻2026-10-26约05:37–05:50UTC。**本任务没有queue、finalize、start/run/tick、准备提示词、runner/state/handoff修改或daemon启动。** 本文为执行前建议，不是已执行回执。

## 当前结论

当前代码不能在保留原15:00历史字段的同时，直接以用户新授权的17:00研究截止通过标准finalizer。`--until 17:00`不是当前活动receipt的可用延期命令：它对新run/prepare分支生效，但resume/finalize分支仍锁定`run_date+1 15:00`，且缺少显式override证据解析。还存在两个独立缺口：Day23缺`baseline.json`，以及无clock-state时Day22 one-shot模板会在`farmer_control()`缺键失败。

因此，不能在原15:00提前queue closeout，也不能等到17:00后临时改`overnight_until`或伪造queued来绕过门。最小可审计路径是：在真实收束前完成窄范围override resolver与新建one-shot状态支持，记录真实用户授权/时间/原始身份，修复或审计迁移baseline，再在**实际17:00–18:00+08（09:00–10:00UTC）**完成真实同线程queue与收束门。用户授权的17:00在此按父代理确认的effective研究截止处理；原始15:00保持历史事实。

## 只读实测身份与文件

| 项目 | 实测 |
|---|---|
| run目录 | `outputs/learning-daily/20261025-DAY23-signature-partner-low-spin-wobbling-magnetic-rotation-run-01/` |
| run_id/date/day | `2026-10-25-day-23-01` / `2026-10-25` / 23 |
| session | `01a172fd-cbfb-7a13-b715-cfa0c479e08e` |
| 当前进程`CODEX_SESSION_ID` | 与上述session完全相同；没有改环境变量来制造匹配 |
| events首条 | `thread.started`，thread_id与上述session相同 |
| run状态 | `running`；closeout_turn、finished_at未有；session_mode=`new-session-per-run` |
| 原始开始 | `2026-10-25T20:16:26.996821+08:00` |
| 原始截止/收束终点 | overnight_until=`2026-10-26T15:00:00+08:00`；closeout_window_ends_at=`2026-10-26T16:00:00+08:00` |
| 新用户指令 | 父代理于本任务转达：必要时今天约17:00开始收束；父代理已决定effective研究截止17:00。不是原receipt自带字段 |
| baseline.json | **缺失** |
| baseline-001.json | 存在；observed_at=`2026-10-25T12:18:53.915992+00:00`，head=`ee0163b4dc9eb882874df0d70cd33bd388d8fba7`，717个knowledge_sha256；无run_id/day_index/session_id/report_existed_before字段 |
| clock-state / attestation | `clock-state.json`、`interactive-closeout-attestation.json`、`closeout-one-shot-queue.json`均缺失 |
| 课程状态实际路径 | `outputs/learning-milestones/2026-09-one-month-state.json`，不是daily根下state.json；next_day_index=23、last_run_id为Day22、status=active |
| 相关常驻进程 | 05:50UTC按/proc的实际script argv token只读检查，未发现run_daily_learning.py、run_daily_learning_daemon.py或run_learning_session_clock.py；这是该时刻观察，不保证未来16:00无人触发 |

baseline-001比原started_at晚约147秒。其status_porcelain未出现Day23日报名，但**这不是report_existed_before=false的完整证明**：还需核ignore/tracked状态及该时刻之前是否已写日报/知识。不得给它添加伪造的entry时间或假称runner原始baseline。

## 当前代码路径与副作用

| 函数/位置 | 实际行为 | 当前限制 |
|---|---|---|
| `run_daily_learning.parse_deadline`，约366–383行 | 解析HH:MM，以调用时本地日期构造；若时间已过，滚到次日 | 活动run延期应绑定run_date+1的**绝对时间**，不能17:00之后重跑该解析而误变10月27日 |
| `main`约1609–1629行 | 先算args.until；新run/prepare使用该值；finalize调用只传paths/receipt，resume虽收args但其主体不读取until | 当前`--finalize-receipt ... --until17:00`会被解析但不应用；不能误称已延期 |
| `resume_running_receipt`约1124–1136行 | 从receipt.overnight_until读取，要求等于planned默认15:00；读baseline.json | 改overnight字段为17会被拒；会尝试同session writer attach，不适合仅登记延期 |
| `finalize_interactive_closeout`约1425–1476行 | 要求默认15:00及其1小时内；同环境session、baseline、attestation、report hash、clock queued身份全部过门 | 17:00执行当前实现必失败；仅补queued也不够 |
| `clock.load_spec`约112–158行 | 检查receipt路径/UUID/session/root/day/start；overnight必须默认次日15:00，closeout_end须+1h | 它也必须使用同一个effective resolver，不能只修runner |
| `Supervisor.__init__`约325–352行 | 若无state，只建identity/events/pending，尚不写first_supervisor_started_at | 不能直接把Day22模板用于新state |
| `Supervisor.start`约366–383行 | 才写first_supervisor_started_at、pid/running、clock-started/resumed日志并保存 | 不能为绕缺键而调用start并假装已有历史daemon |
| `farmer_control`约385行 | 直接读取state[first_supervisor_started_at] | 无state直接attempt会先KeyError；Farmer取消/恢复必须在真实queue边界核 |
| `pending_checkpoints`约424–442行 | 只根据真实observed_clock_executions标delivery_observed，但**会save state** | 本次没调用；不是只读probe |
| `attempt`约444–492行 | 终态去重、Farmer控制、重读spec身份、真实codex queue；先in-flight/save/log，exit0才queued/save/log/heartbeat | attempt自身不检查now是否到event.at；调用者须真时钟guard。timeout=unknown，不可盲重发 |
| `acquire_locks`约231行 | 同时非阻塞获取daemon和runner锁；打开锁文件也有写副作用 | 本次未获取；未来LockBusy应停，不抢锁/删锁/重启daemon |

`queue exit0`只表示broker接受排队，`delivery_observed=false`；不证明提醒已被该线程读到或完成收束。不能将这两个事实混写。closeout attestation只能在真实同session收束完成后生成。

## 最小窄修建议（本任务未实施）

### 1. 一个共用、只读的effective截止解析器

由runner/clock共用一处纯函数，避免两个脚本出现不同截止。可放在小型共享模块，或在runner中定义后由clock导入无副作用函数；不要因此调用main。建议返回`original_deadline,effective_deadline,effective_closeout_end,override_identity/hash`。

无override时保持当前默认及拒绝naive/wrong-date行为；有override时必须验证同run/session/day、用户授权来源、绝对时区时间、原始截止与历史receipt的对应及sidecar哈希。不能只读一个无身份的`effective_deadline`字符串就放行。

建议新增真实`user-deadline-override.json`侧回执，至少包含：

- schema_version、run_id、run_date、day_index、session_id、原run.json路径；
- `authorization_source=current user instruction in this existing session`及可追溯的原指令引用/文字；引用ID未知就明示未知，不编ID；
- `recorded_at`为真正登记时刻，不能写成用户发话时间，除非平台已提供准确时间；
- 原始`overnight_until`、原始`closeout_window_ends_at`及原receipt SHA；
- effective research deadline=`2026-10-26T17:00:00+08:00`、effective closeout end=`2026-10-26T18:00:00+08:00`；
- reason、writer/operation身份、无新session/daemon、历史字段未覆盖声明。

run.json可以**新增**`effective_overnight_until`、`effective_closeout_window_ends_at`和侧回执路径/哈希作为current effective索引，原`overnight_until`/`closeout_window_ends_at`保持原值。或者只用固定sidecar并在真实最终receipt追加相同索引；关键是所有消费者验证同一来源而非各自guess。

需要改到的调用点：resume的schedule_deadline、finalize的deadline比较/attestation/clock匹配、clock.load_spec/identity/plan_events，以及生成reminder文案与runtime snapshot。`closeout_window_end(deadline)`和`should_run_closeout_turn(now,deadline)`本身是泛化+1小时逻辑，不必把默认15改成全局17。

`clock.message_for`当前写死“15:00–16:00/15:45/before16:00”；应按spec.deadline/end动态格式化，保留原deadline为历史字段。共享prompt时间门也不应在effective17时继续输出矛盾的硬编码15–16指令。`planned_closeout_for_run_date`默认仍15；**只对本次显式override**生效。

当前CLI没有只登记活动receipt延期的受支持分支。最小新增方式是窄scope的“登记当前run override”入口（需显式receipt、--until或绝对时间、用户授权证据），只追加sidecar/current-effective索引；它不得顺便resume/create-session。也可由授权的当前writer显式生成侧回执后交给上述纯resolver验证；不要谎称旧CLI已经实现。

### 2. 真实one-shot初始化，避免无state缺键

借鉴Day22的**单次attempt**思想，新增一个明确的`initialize_for_one_shot(now)`或等价窄入口，而非调用start/run/tick。它只在state不存在时，用真实当前时刻写one-shot初始化来源、first-start时间及identity/event计划，日志明确`one-shot-initialized`；不冒充daemon历史开始、session执行或旧提醒已送达。

注意Farmer边界：现实现用first_supervisor_started_at筛旧事件。若首次one-shot刚写now，就可能把now之前几秒的鲜活cancel/recovery误忽略。应在初始化与queue实际边界用本run study_started_at或明确的recovery reference核**鲜活同thread**Farmer状态，或增加one-shot专用Farmer检查；不能因缺state绕过Farmer。

将真实queue保留在现有attempt逻辑内，保留in-flight/attempt_history/unknown/queued及sent_event_ids一致性；`now`由真实本地时钟取得，要求effective_deadline≤now<effective_closeout_end，且仅选择event_id=closeout。其余历史checkpoint只是planned/pending，不能补写已执行。

### 3. baseline缺口必须独立审计

当前main在约1765行调用`snapshot_knowledge(root)`，但本文件中找不到把该原始快照落为baseline.json的写入；resume/finalize却强制读取它。这是窄的持久化/兼容缺口，不是允许closeout时重拍快照的理由。

新run修复：在首次session运行前，原子保存run_id/day/session绑定（session可在thread.started后补索引）、report_existed_before及knowledge_sha256_before，保存真实observed_at和原始report状态。

本Day23迁移：baseline-001已记录真实717页快照，字段是knowledge_sha256；可作为**候选entry witness**，先以first-run工具日志/首次写入时间、已记录head和文件状态核它在知识写入前，以及日报当时确实不存在。通过后，用显式`baseline-migration-attestation`指向原文件SHA/观测时刻和验证证据，再由窄兼容resolver映射字段；不得把它静默重命名成“runner原始baseline”或填一个未经证明的false。

若原始报告absence/快照前写入边界无法证明，保持缺口，不能为了学分绕过durable-knowledge门。可以如实保留partial/未正式授卡和当前内容发布状态，不伪造formal completed。当前readiness只确认候选文件存在，未完成这项溯源。

## 真实收束时必须通过的字段与顺序

1. **实际时间及授权**：重读用户override侧回执和current-effective索引，核原15:00仍在；确认此时真实≥17:00且<18:00+08。此前不queue/finalize。
2. **身份**：run/session/env/events thread一致；day23仍等于课程next_day_index；不通过改环境变量制造同session。
3. **技术准备**：baseline审计有效；当前无危险writer重叠；两学习锁可取得；鲜活Farmer没有取消、人工介入或恢复占用。
4. **真实queue**：窄one-shot初始化及Supervisor.attempt一次closeout；exit0留下queued、queued_at、attempt_history、sent_event_ids，且clock ledger绑定effective17/18与overridehash。timeout/unknown不盲重发，失败如实保留。
5. **同session真正收束**：完成日报、canonical知识写回、逐卡交付审核、科学边界、续接提示及发布必要工作。只有实际处理完才写attestation；卡24仅预习不授分。
6. **attestation**：status=`closeout-turn-completed`、run_id、session_id、closeout_event_id=`closeout`、hard_deadline=effective17的ISO、closeout_at实际处于有效1小时内、report_sha256与最终报告相符、window_missed=false、time_snapshot；另外保留original_deadline与overridehash。
7. **报告**：包含精确`closeout_event_id: \`closeout\``以及同session ID；所有required headings/Knowledge writeback/卡审计真实有效。attestation之后改报告必须重核hash并如实重做attestation。
8. **标准finalizer**：使用修复后的resolver和现有门，不跳过preflight/lint/diff/report/knowledge/card校验；成功时一次推进Day23，next24；若只partial不冒充授卡。检查返回receipt，不凭命令启动即宣称完成。
9. **最终对账**：state、run、next prompt、发布回执、实际hash/H3各自核对，避免第二次加学分；已completed的幂等返回不代替人工确认本次实际成果。

## prepare_next_prompt的具体副作用

`run_daily_learning.prepare_next_prompt`约912–940行**不是只读预览**：

- 目标为`outputs/learning-daily/prompts/<date>-DAY<next>-<topic>.md`；优先canonical文件，若不存在则取同date/day的排序首个旧文件，否则新建canonical。
- 已存在文件：读取后仅在缺少两个合同marker时附加curriculum/time-gate段，再`write_text`；不是整篇重新生成，所以用户已有备注保留。
- 不存在：调用render_prompt，用该next_run_date的默认planned次日15:00，创建目录并写文件。
- 不创建session、run或课程学分，也不启动daemon；但它实际写prompt。finalizer在校验deliverables_passed后、state写入前调用它。
- 若准备失败，finalizer将deliverables/success置false，记录next_prompt_error；已发生的文件写入未必回滚。应留目标文件before/after及异常，不假称无副作用。
- 本次延长研究会越过正常16:00触发。下一提示词的run_date和实际下一次schedule触发需明确记录；不能把“prompt已生成”写成“下一run已启动”，也不能为赶下一run新建session。05:50无daemon仅是当前观察，16:00前后仍需重查实际重叠。

## 建议的限定测试（本任务未运行生产动作）

既有测试文件：`system/tests/test_daily_learning_runner.py`、`system/tests/test_learning_session_clock.py`。

可沿用的既有用例：runner的`test_final_closeout_turn_uses_only_reserved_1500_to_1600_window`（约174行）、`test_resume_exec_command_and_overnight_deadline`（386行）、next-prompt两例（314/324行）、partial primary/preview不加分例（282–306行）；clock的wrong-date/naive、UTC等价（246–272行）、真实reminder/overdue去重和过期不补送（358/371行）。

新增最小测试应使用TemporaryDirectory/FakeClock/FakeQueue，禁止真实codex queue：

- 默认无override仍15–16；授权17保持原15字段、effective17–18；16:59:59拒finalize、17:00接受、18:00拒；UTC等价可接受。
- 错session/day/run/hash、naive时间、未授权/缺侧回执、默改原15字段全部拒绝；17点后HH:MM不能滚到次日伪延长。
- resume/finalize/clock读取同一resolver；17前绝不生成closeout queued；current state次日仍按正常默认，不把本次延长设为全局。
- 无clock-state的one-shot初始化可调用fake attempt，不写daemon running/start历史；鲜活Farmer cancelled/recovery在初始化前后都阻queue。
- queue timeout→unknown且不重复；exit0→queued但delivery_observed=false；首次queued不等同实际收束完成。
- baseline.json原始路径与经验证legacy migration各自通过；缺report absence/错hash/后拍snapshot拒绝；测试main确实在session前持久化baseline。
- `prepare_next_prompt`新建/已有备注保留/错误时课程不推进；partial23与preview24不误授分。

## 本次检查对应代码指纹

截至05:50UTC读取：

- `system/scripts/run_daily_learning.py` SHA256 `6e8303f2fcd639c591c5bddc4f7e09ad6944d9d0fcce38d0fea2977a72cc173f`。
- `system/scripts/run_learning_session_clock.py` SHA256 `6d629808b574659188b31684c251c4a8c1327bbb7e1202c77c432b8c1c8d15cd`。
- `system/tests/test_daily_learning_runner.py` SHA256 `f6ec7061fa650e08f7e7ac30e5e4e73754b83a7ab792deba594c886c87a9bae6`。
- `system/tests/test_learning_session_clock.py` SHA256 `75789c1577879dbea1b14f823727e6d759ec1bd8ff4e486d8132dcbd8e3d25c9`。

后续若父代理实施窄修，应以新的代码/测试和真实回执重新验收；本文行号只对应上述读取版本，不冒称修复已经存在。

## 06:14UTC补核：baseline重构证据已显著加强

父代理已在05:56UTC真实落盘`user-deadline-override-064.json`及原run完整副本/hash；本worker未重复写授权。当前run保留原overnight15、新增effective17和effective closeout18，身份未变。未来resolver应认该**现有侧回执的实际字段**：`authorization_kind`、`user_instruction`、`original_research_deadline`、`effective_research_deadline`、`effective_closeout_window_ends_at`、`original_receipt_snapshot`及其sha256；不要硬要求本文此前建议但现有回执没有的同名字段。run_date/day_index可从已hash绑定的原receipt快照验证，而非伪补授权文件。

`baseline-readonly-evidence.json`保存以下实际Git object只读核查结果：

- baseline-001原文件SHA256为`3f51de609f9b91619a44a3d35b43f8194ceb095778076aa6a9447acd2748b74b`，原observed_at与原head均未改。
- head `ee0163b4dc9eb882874df0d70cd33bd388d8fba7`中恰有717个knowledge Markdown blob；baseline中也恰为717项，路径集合对应。
- 706项byte hash直接与head blob相同。其余11项中，10项完全由LF→CRLF转换解释；`angular-distribution-coefficient.md`为混合行尾，但该文件当前bytes仍等于baseline hash，规范CRLF为LF后与head blob完全相同。**717项没有发现相对于head的实质知识内容差异。** 这支持其为首次本任务科学写入前的快照；不能重拍当前知识来替换它。
- head tree中没有Day23日报。captured status_porcelain也无日报路径，且不存在`?? outputs/`或`?? outputs/learning-daily/`这类可折叠隐藏该日报的未跟踪祖目录条目；193条未跟踪行说明该状态确有记录untracked。
- 该head跟踪的.gitignore SHA为`5a7581c3f5dc3b4f8526a6a22a0b877b034476ab27a7a44876fe85122cac6bc3`，不忽略daily根下日报。当前`git check-ignore --no-index <report>`退出1，core.excludesfile未配置，`.git/info/exclude`仅默认注释。

因此可以提出一种**显式reconstructed-entry-witness** baseline来源方案：新`baseline-reconstruction-<id>.json`只包含原baseline SHA、head/object证明、captured status证明、真实重构时刻、原observed_at、run/session绑定、717页原hash字段映射，以及`report_absence_evidence_kind=head-tree+captured-untracked-status+tracked-ignore-policy`。runner窄resolver接受此kind，而不要求把它假装成原`baseline.json`或声称由runner在20:16原点写成。

边界要保留：当前global/info excludes不能绝对证明历史上未临时改变外部exclude；原baseline晚于session启动约147秒，原runner events文件没有保存baseline创建命令。可将report absence写作由当时head/status和追踪ignore政策推得，而不冒充直接stat。这里证据已足以支持**可审计重构种类的工程决策**，但是否将该限定证明纳入标准finalizer，应由显式窄代码合同和测试处理，不能静默造原始false字段。必要时增加baseline before/after保护与knowledge lineage边界，不影响科学needs_review。

## 06:14UTC补核：16:00触发与同run冲突

`scheduler-readonly-evidence.json`保存该时刻实际状态：

- `/proc`实际script token未见daily runner/daemon/clock/manual-waiter进程；仅见当前running receipt为原Day23，未见2026-10-26新run。
- 两个锁文件虽存在，但`/proc/locks`对应device/inode没有持有记录。**空锁文件不是占锁**；当前interactive session不会自动替runner持有flock。
- scheduler state仍是`last_scheduled_date=2026-10-25`、`last_status=failed`、exit130、updated_at2026-10-25 20:17:11+08。日志最后事件显示手动waiter启动Day23后被中断；没有今天的真实16:00执行回执。
- daemon的`next_due()`在今天16:00到达且last_date不是今天时会判due；若有人/容器entrypoint在16:00前后启动它，当前代码并不检查“旧run有效窗口仍active”再跳过新session。
- runner只在分配新run目录/写run.json之后获取学习锁；此时当前锁也未被interactive writer持有。因此，**不能承诺16:00天然安全**，尽管眼下并无daemon进程。

最窄防重复建议：给新run入口加入一个只读的**active-receipt guard**，位置在分配run_id/run_dir和写run.json之前、且在唯一执行锁保护的重新核查下。扫描限定root/schedule的运行回执：若另一未completed run的原身份有效、同课程next_day_index匹配、有效research/closeout窗口尚未结束（本run至18:00）、尤其已存在用户延长回执，则返回显式`deferred-existing-run`，列原run/session、effective截止和resume命令，**不创建新目录、不调用codex exec、不改course state**。

若guard由daemon接收到，应将其识别为“本次trigger因原run活动而延后/跳过duplicate”的正常有证据结果，而不是模型失败，不进入fallback重试。状态/事件应诚实标`deferred-existing-run`及原因；不可伪记Day24完成。是否在收束后另安排实际下一触发，由原schedule/用户授权的安排决定；本次不自动补起Day24、不重启daemon、不修改外部scheduler。

这条guard比临时杀/重启daemon或手改scheduler last_date更窄，也可以覆盖将来活动interactive session失去runner锁的相同情形。仅持有锁的临时后台阻塞器会变成新监督进程、还可能阻挡17点真实one-shot，不建议用它掩盖缺失active-run检查。

## 是否需要治理窄修

**需要。** 若目标是今天在同run/session、有效17–18窗口内走可验证标准收束，至少应修共享effective-deadline resolver、显式baseline-reconstruction resolver、fresh one-shot初始化/Farmer边界；在16:00前加入active-receipt guard可避免意外新session。既有runner原生--until不能解决这四点。所有修改应为功能性窄修配限定fixture测试，不放宽科学/课程门，也不构造假的queued/原baseline。本文仍仅为方案；未改这些治理文件。
