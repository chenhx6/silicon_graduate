---
type: system-workflow
graph-excluded: true
updated: 2026-09-10
---

# Agent capability upgrade：up 与 evolution

本流程把 `configure` 的 `up` 和 `muIon-beam` 的 `evolution` 适配到 Wiki。它适合更新 Agent skill、hook、工具和运行方法，不负责科学 claim 摄入，也不把外部仓库当作自动安装源。

## 任务定义

开始前写清四项：升级对象、期望行为、允许修改的路径和验证标准。默认范围是本 Wiki 的 `system/workflows/`、`system/scripts/`、`system/tests/`、README 入口和用户级 `/root/.codex/skills/`；`raw/`、`PLAN.md`、`raw/zotero/wiki-inbox.bib`、`.codex` 和凭据永远排除。

## 基线与候选

1. 读取 `git status --short --branch`，保留已有 dirty baseline。
2. 盘点本地入口、脚本、测试和文档，确认是否已有同一能力；缺失目录是事实，不是新建理由。
3. 对外部候选固定 URL 和 commit/tag，核对许可证、安装钩子、脚本副作用、测试和运行器兼容性。
4. 把候选标为 `new`、`extend`、`merge`、`reference-only` 或 `reject`，写出增量价值和拒绝理由。

`star` 和热榜只能用于发现候选，不能替代许可、安全、兼容性和回归证据。无法获取结构化结果时保留“未核实”，不补写排名。

## 单轮自我升级

一轮只落地一个有边界的候选：

```text
基线 → 候选证据 → 最小改动 → 结构/行为/安全验证 → 记录采用或拒绝
```

升级 `up` 或 `evolution` 自身时，还要重新检查触发描述、调用链、保护路径、用户审核门和本地测试；禁止递归触发、无限自改或在同一轮顺手重写其它 skill。验证失败则停止该候选，保留失败原因，回到下一候选或 handoff。

## Wiki 专用验证

```bash
python3 -m unittest system.tests.test_agent_ops
python3 system/scripts/wiki_hook.py session-start --root .
python3 system/scripts/wiki_farmer.py once --root . --dry-run
python3 system/scripts/wiki_lint.py --fail-on error
git diff --check -- system/agent-capability-adoption.md system/agent-capability-upgrade.md system/scripts system/tests
```

Farmer 的运行状态只存在 `tmp/farmer/`；hook 不自动启用；外部 skill 安装到用户目录后，下一次 Codex 会话才重新发现。Wiki 已授予持续自主 commit/push；因此通过 preflight、lint、H3、remote ancestry 和精确 refspec 门后可自动发布。当前指令的“不要 push”“只 commit”“只修改”、未完成 WIP、hard P0 和不可逆 Git 操作仍可阻止发布。

## 停止条件

达到验证标准、连续两轮没有实质增量、候选不可复现/许可不明，或遇到需要用户科学判断的边界时停止。停止时把已采用、未采用、证据缺口、验证命令和下一步写入 `system/handoff.md`；不要把“候选已发现”写成“升级已完成”。
