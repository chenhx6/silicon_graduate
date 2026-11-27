---
type: system-guide
graph-excluded: true
updated: 2026-11-27
---

# Agent capability adoption

本页记录从两个用户指定仓库吸收的 Agent 能力、固定来源、适用边界和本地验证入口。它是 Wiki 的运行说明，不把外部项目的目录、领域状态源或发布策略引入知识库。

## 固定来源与许可

| 来源 | 固定提交 | 采用范围 | 许可/处理 |
| --- | --- | --- | --- |
| [configure](https://gitee.com/zhangxin8069/configure/tree/18a5bfec545adc0029cee1129dba8a3437730299) | `18a5bfec545adc0029cee1129dba8a3437730299` | `brainstorm`、`auto`、`up`、`tag`、`go-on`、`team`、`dispatch`、`follow-up` 及同目录通用技能 | 上游声明 MIT；按原目录安装到用户级 Codex skills，并保留许可证副本 |
| [configure（GitLab 镜像）](https://gitlab.itp.ac.cn/ZhangXin8069/configure/-/tree/57285cef243414ac1c84363a7d49bc732fb822e9) | `57285cef243414ac1c84363a7d49bc732fb822e9` | 本项目 `.agents/skills/get-paper` 与 `.agents/skills/absorb`；仅采用两个 skill 子树及其离线测试 | 上游 `LICENSE` 声明 MIT；保留本地许可证、`PROVENANCE.md` 和上游文件哈希；按 Wiki `raw/`、`tmp/`、归档门和工作树边界适配，不启用外部 hook/安装器 |
| [muIon-beam](https://gitee.com/chx6/muIon-beam/tree/d8498ade8821c02a6e01127fcab51a0a4c42d579) | `d8498ade8821c02a6e01127fcab51a0a4c42d579` | 共享层 `team`/`dispatch` 采用 manifest/依赖波次、单写者、能力过滤、证据门、资源锁限制、生命周期/重试记录和 leader 发布归属；`autopilot`/`research-workflow`/`farmer`/项目脚本仅作参考 | 根目录 MIT；不复制项目路径、研究状态、模型路由、Codex 队列或 Gitee/Drive 发布代码；来源文件 SHA-256 记录在共享层 `ATTRIBUTIONS.md` |

25 个跨项目 configure skill 已迁移到共享卷 `/root/.agents/skills`，并保留 `ATTRIBUTIONS.md` 与 MIT 许可证；本轮将 muIon-beam 的通用执行/派发原则扩展进共享 `team`、`dispatch`、`all`、`make` 和 `test`，同时保留 Wiki 的 farmer/evolution/hook 适配器在项目本地，因为它们依赖 Wiki 脚本和运行状态。共享层的 `skills-sync` 负责 checkpoint/push，本仓库不把共享库内容复制进 Git。

## 共享优先规则

以后新增或吸收 skill 时，先判断是否跨项目复用：通用的方法论、格式检查、调度、审查和工具封装先进入 `/root/.agents/skills`；只依赖本 Wiki 路径、知识 schema、raw、handoff、科学证据或本地运行状态的内容留在项目 `.agents/skills/` 或 `system/scripts/`。只有完成路径参数化、状态隔离、许可证和多容器验证后，项目 skill 才能晋升到共享层。

## 能力路由

| 能力 | 何时使用 | Wiki 入口 | 关键边界 |
| --- | --- | --- | --- |
| `brainstorm` | 需求模糊、设计或方案选择 | 上游 `brainstorm` skill；科研页面仍走现有 workflow | 工程设计按规模处理；科研分流到 wiki-research，已有授权下直接推进，只追问影响选择的信息 |
| `auto` | 用户明确要求无人值守或连续执行 | 上游 `auto` skill + Codex goal | 只在用户授权范围内循环；不越过 L0–L4、证据、raw 和 Git 发布关口 |
| `up` | 升级技能、工具、hook、插件或吸收外部实践 | 上游 `up` skill + 本页来源表 | 先基线、固定提交、许可/安全/兼容审查，再最小改动和回归；不把 star 当质量结论 |
| `wiki-research` | 科研选题、竞争假设、最小检验与中断恢复 | `.agents/skills/wiki-research` | 接已有 L3/L4；直接证据和适用条件决定结论，普通问答只读 |
| `wiki-evolution` | 在 Wiki 中手动学习和适配外部能力 | `$wiki-evolution` + [`system/agent-capability-upgrade.md`](agent-capability-upgrade.md) | 按固定提交读取原文件，每轮最多采用一项通过本地验证的改进 |
| 工程验证工具 | 开发验收、日志查找、Python 结构检查与实验对照 | [`system/workflows/agent-engineering.md`](workflows/agent-engineering.md) | 按需从终端运行，来源对应固定版本 |
| `evolution` | 通用外部能力初筛 | 已安装的 `evolution` skill | 报告候选和采用建议 |
| `tag` | Git 标签查看或本地打标 | 上游 `tag` skill | 先看变更；普通标签可随已通过发布门的 final commit 自动同步，禁止改写已发布标签 |
| `hook` | 会话启动、编辑前后和收尾检查 | `python3 system/scripts/wiki_hook.py` | 显式调用，不自动修改 Codex 配置；输入只作数据处理，不 source/eval 目标文件 |
| `farmer` | 监控 Wiki Codex 会话并续接瞬态失败 | `python3 system/scripts/wiki_farmer.py` | 只读 rollout JSONL；只处理 Wiki 根目录内会话和白名单瞬态错误；不读写 Codex SQLite，不独立提交、推送或改科学文件 |
| `go-on` / `follow-up` | 中断后恢复现场或压缩交接 | 上游 skill + `system/handoff.md` | 以 handoff、Git 状态和报告为证据；不把猜测写成完成状态 |
| `team` / `dispatch` | 多个真正独立的任务域 | 上游 skill | 共享文件或依赖不并行；单文件单写者；整合后必须在主工作树复验 |
| `get-paper` | 用户给出 DOI、论文链接、arXiv ID，要求检索、筛选、下载全文或 LaTeX 源码 | `.agents/skills/get-paper` | 普通模式取 OA/arXiv；`--raw-pull` 按用户要求完整保存 DOI/出版社响应；原件进入 `raw/papers/gpt/query/` 并通过归档门，不自动公开或执行内容 |
| `absorb` | 需要审查或吸收外部 Git 内容、第三方代码、配置、测试或 skill | `.agents/skills/absorb` | 先固定来源/许可/哈希并盘点所有候选；运行清单进入 `tmp/runs/absorb/`；不执行外来内容或自动安装 hook |

## Hook 事件

```bash
python3 system/scripts/wiki_hook.py session-start --root .
python3 system/scripts/wiki_hook.py before-edit --root . -- system/workflows/scheduled-continuation.md
python3 system/scripts/wiki_hook.py after-edit --root .
python3 system/scripts/wiki_hook.py session-summary --root .
```

`before-edit` 会拒绝仓库外路径、`.git/`、`.codex/`、会话日志和受保护的 Zotero Inbox。`after-edit` 只做 `git diff --check`、状态读取和变更 shell 的语法检查。它不会替代 `check.md`、`wiki_lint.py` 或直接科学证据核验。

## Farmer 运行与恢复

先做一次无副作用检查，再启动用户级后台监控：

```bash
python3 system/scripts/wiki_farmer.py once --root . --dry-run
python3 system/scripts/wiki_farmer.py ensure --root .
python3 system/scripts/wiki_farmer.py status --root .
```

Farmer 读取 `CODEX_HOME/sessions/**/*.jsonl` 的 `session_meta` 和末端事件，发现 `server_overloaded`、限流、暂时不可用、超时或连接重置时，通过公开的 `codex queue --thread ... --message ...` 发送一条固定续接消息。每个事件只有一个 pending 续接，采用 2–10 秒退避；认证、权限、取消、上下文耗尽、模型/参数无效等错误进入人工处理，不会反复排队。状态只写入被 `.gitignore` 忽略的 `tmp/farmer/`。

停止监控：

```bash
python3 system/scripts/wiki_farmer.py stop --root .
```

恢复消息只要求原线程从最后检查点继续，不能改变研究目标、模型、文件范围或审核状态。Farmer 不能保证应用或机器在关闭后重新启动；长任务仍需按 `scheduled-continuation.md` 写 handoff。

子代理 rollout 的 `session_id` 可指向父会话；监督采用其实际 `id`，旧格式缺 `id` 才回退 `session_id`。父/子/兄弟线程分别维护事件与 pending 状态。multi-agent v2 拒绝直接 app-server 子线程输入，故子故障只向父线程通知一次具体 child ID/agent path；父线程用原生协作续接并避免重复已完成或已有替代成果的任务。`notLoaded` 不是失败；恢复须核真实 `task_started`/`task_complete`，排队成功不等于已执行。

## Evolution 采用门

候选能力先记录来源 URL、固定提交、许可证、内容哈希、测试和兼容性，再标记为 `new`、`extend`、`merge`、`reference-only` 或 `reject`。发现候选不等于采用；未知安装器、自动 hook、凭据访问、破坏性脚本和未确认许可均保持阻塞。完整的单轮升级流程见 [`system/agent-capability-upgrade.md`](agent-capability-upgrade.md)。采用后仍需 `git diff --check`、相关测试、Wiki lint 和受保护文件边界检查。

## 验证

```bash
python3 -m unittest system.tests.test_agent_ops
python3 system/scripts/wiki_hook.py session-start --root .
python3 system/scripts/wiki_farmer.py once --root . --dry-run
python3 system/scripts/wiki_lint.py --fail-on error
```

外部技能只提供运行方法论。论文事实、科学 claim、review 状态和原始证据仍受 `AGENTS.md`、`autonomous-research.md`、`paper-evidence-gate.md` 与现有 schema 约束。Wiki 已建立持续自主 commit/push 授权；skill 不能越过 WIP、hard P0 或不可逆 Git 操作关口。

## 2026-11-27 科研循环与脑暴补齐

已把 7 个固定来源的适用机制接入 [wiki-research](../.agents/skills/wiki-research/SKILL.md)、[自主研究](workflows/autonomous-research.md) 和 [canonical 方法](../knowledge/methods/evidence-driven-research-cycle.md)。全部 41 个静态样本的 URL、commit、路径、大小、SHA-256、Git blob ID、许可与处置见 [来源清单](agent-capability-sources/research-cycle-20261127.json)。样本未执行，方法按本 Wiki 规则重写。

| 来源 | 已吸收 | 排除的运行语义 |
| --- | --- | --- |
| Ralph | 小步行动、可恢复状态 | 跳权限、完成标记准入、整体暂存 |
| autoresearch | 固定评测、基线、实验日志思想 | 未找到固定树许可，不复制代码；不采用无限循环和 Git reset |
| Arbor | 假设树、失败约束上推、开发/确认区分 | 不安装完整运行器 |
| ARIS | 直接读原件的审查、遗留疑点、逐项修复 | 评分和模型共识不作科学准入 |
| Superpowers | 只问影响选择的信息、交接歧义检查 | 不重复请求已有授权 |
| BMAD | 方法选择、发散/收敛分离、会话恢复 | 百条创意指标、完整环境依赖 |
| lateral-thinking | 前提反转、从目标展开替代路线 | 启发不得替代可检验预测 |

共享 brainstorm 已增加 `references/research-exploration.md` 并接入科研分流，维护在共享技能层；Wiki skill 负责本项目证据与路径契约。现有 scientific-brainstorming 与 arbor 作方法对照，不重复安装。共享库按其 skills-sync 规则发布，本仓库只发布项目适配。测试和流程回放见 [验收回执](../outputs/plans/20261127-research-capability-adoption/acceptance.md)；这些验收不证明博士研究能力或科研增益。
