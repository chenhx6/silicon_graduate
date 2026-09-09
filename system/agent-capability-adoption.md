---
type: system-guide
graph-excluded: true
updated: 2026-09-10
---

# Agent capability adoption

本页记录从两个用户指定仓库吸收的 Agent 能力、固定来源、适用边界和本地验证入口。它是 Wiki 的运行说明，不把外部项目的目录、领域状态源或发布策略引入知识库。

## 固定来源与许可

| 来源 | 固定提交 | 采用范围 | 许可/处理 |
| --- | --- | --- | --- |
| [configure](https://gitee.com/zhangxin8069/configure/tree/18a5bfec545adc0029cee1129dba8a3437730299) | `18a5bfec545adc0029cee1129dba8a3437730299` | `brainstorm`、`auto`、`up`、`tag`、`go-on`、`team`、`dispatch`、`follow-up` 及同目录通用技能 | 上游声明 MIT；按原目录安装到用户级 Codex skills，并保留许可证副本 |
| [muIon-beam](https://gitee.com/chx6/muIon-beam/tree/d8498ade8821c02a6e01127fcab51a0a4c42d579) | `d8498ade8821c02a6e01127fcab51a0a4c42d579` | 共享层 `team`/`dispatch` 采用 manifest/依赖波次、单写者、能力过滤、证据门、资源锁限制、生命周期/重试记录和 leader 发布归属；`autopilot`/`research-workflow`/`farmer`/项目脚本仅作参考 | 根目录 MIT；不复制项目路径、研究状态、模型路由、Codex 队列或 Gitee/Drive 发布代码；来源文件 SHA-256 记录在共享层 `ATTRIBUTIONS.md` |

25 个跨项目 configure skill 已迁移到共享卷 `/root/.agents/skills`，并保留 `ATTRIBUTIONS.md` 与 MIT 许可证；本轮将 muIon-beam 的通用执行/派发原则扩展进共享 `team`、`dispatch`、`all`、`make` 和 `test`，同时保留 Wiki 的 farmer/evolution/hook 适配器在项目本地，因为它们依赖 Wiki 脚本和运行状态。共享层的 `skills-sync` 负责 checkpoint/push，本仓库不把共享库内容复制进 Git。

## 共享优先规则

以后新增或吸收 skill 时，先判断是否跨项目复用：通用的方法论、格式检查、调度、审查和工具封装先进入 `/root/.agents/skills`；只依赖本 Wiki 路径、知识 schema、raw、handoff、科学证据或本地运行状态的内容留在项目 `.agents/skills/` 或 `system/scripts/`。只有完成路径参数化、状态隔离、许可证和多容器验证后，项目 skill 才能晋升到共享层。

## 能力路由

| 能力 | 何时使用 | Wiki 入口 | 关键边界 |
| --- | --- | --- | --- |
| `brainstorm` | 需求模糊、设计或方案选择 | 上游 `brainstorm` skill；科研页面仍走现有 workflow | 先分类 spike/bounded/architectural；复杂设计先批准再实现 |
| `auto` | 用户明确要求无人值守或连续执行 | 上游 `auto` skill + Codex goal | 只在用户授权范围内循环；不越过 L0–L4、人工审核、raw 和 Git 发布关口 |
| `up` | 升级技能、工具、hook、插件或吸收外部实践 | 上游 `up` skill + 本页来源表 | 先基线、固定提交、许可/安全/兼容审查，再最小改动和回归；不把 star 当质量结论 |
| `evolution` | 主动发现外部能力 | 本地 adapted skill + `system/agent-capability-upgrade.md` | 只报告候选和采用建议；候选必须可固定、可核验、无未知安装钩子 |
| `tag` | Git 标签查看或本地打标 | 上游 `tag` skill | 先看变更；普通标签可随已通过发布门的 final commit 自动同步，禁止改写已发布标签 |
| `hook` | 会话启动、编辑前后和收尾检查 | `python3 system/scripts/wiki_hook.py` | 显式调用，不自动修改 Codex 配置；输入只作数据处理，不 source/eval 目标文件 |
| `farmer` | 监控 Wiki Codex 会话并续接瞬态失败 | `python3 system/scripts/wiki_farmer.py` | 只读 rollout JSONL；只处理 Wiki 根目录内会话和白名单瞬态错误；不读写 Codex SQLite，不独立提交、推送或改科学文件 |
| `go-on` / `follow-up` | 中断后恢复现场或压缩交接 | 上游 skill + `system/handoff.md` | 以 handoff、Git 状态和报告为证据；不把猜测写成完成状态 |
| `team` / `dispatch` | 多个真正独立的任务域 | 上游 skill | 共享文件或依赖不并行；单文件单写者；整合后必须在主工作树复验 |

## Hook 事件

```bash
python3 system/scripts/wiki_hook.py session-start --root .
python3 system/scripts/wiki_hook.py before-edit --root . -- system/workflows/scheduled-continuation.md
python3 system/scripts/wiki_hook.py after-edit --root .
python3 system/scripts/wiki_hook.py session-summary --root .
```

`before-edit` 会拒绝仓库外路径、`.git/`、`.codex/`、会话日志和受保护的 Zotero Inbox。`after-edit` 只做 `git diff --check`、状态读取和变更 shell 的语法检查。它不会替代 `check.md`、`wiki_lint.py` 或人工科学审核。

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

## Evolution 采用门

候选能力先记录来源 URL、固定提交、许可证、内容哈希、测试和兼容性，再标记为 `new`、`extend`、`merge`、`reference-only` 或 `reject`。发现候选不等于采用；未知安装器、自动 hook、凭据访问、破坏性脚本和未确认许可均保持阻塞。完整的单轮升级流程见 [`system/agent-capability-upgrade.md`](agent-capability-upgrade.md)。采用后仍需 `git diff --check`、相关测试、Wiki lint 和受保护文件边界检查。

## 验证

```bash
python3 -m unittest system.tests.test_agent_ops
python3 system/scripts/wiki_hook.py session-start --root .
python3 system/scripts/wiki_farmer.py once --root . --dry-run
python3 system/scripts/wiki_lint.py --fail-on error
```

外部技能只提供运行方法论。论文事实、科学 claim、review 状态和原始证据仍受 `AGENTS.md`、`autonomous-research.md`、`paper-evidence-gate.md` 与现有 schema 约束。Wiki 已建立持续自主 commit/push 授权；skill 不能越过 WIP、hard P0、人工审核或不可逆 Git 操作关口。
