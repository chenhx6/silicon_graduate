# 低能核结构研究 Wiki

本 Wiki 是面向个人科研工作的可追溯知识库，用于积累文献事实、竞争性物理解读、研究决策和失败经验，并支持 Obsidian 浏览、AI 辅助整理与科研写作。

Wiki 可在不同操作系统和 AI 工具环境中使用。Docker、Obsidian、QMD 和其它工具配置属于使用者本地环境；科学证据、原始资料和不可逆 Git 操作仍按本仓库工作约定处理。

## 当前定位

当前系统是 **Continuous Research-Learning v2（硅基研究生 V2）**：面向低能核结构研究的 Human-in-the-loop research Wiki。它支持 traceable evidence、摄入默认 L2、课题调查型 L3、手动启动且可复现的数据研究型 L4，以及以 P0/P1 为中心的集中审核；ordinary Q&A 保持轻量，正式知识晋升仍由 Human review 控制。

A≈130 是当前研究锚点，不是 Wiki 的收录边界。v2 的设计决策与 `131Ce` pilot 见 [Continuous Research-Learning v2 architecture record](system/architecture-updates/2026-07-l3-autonomy-l4-foundation.md)；完整 L0–L4 状态机只在 [autonomous-research workflow](system/workflows/autonomous-research.md) 维护。Wiki 仍不是最终权威，也不保证文献完整覆盖；论文级结论必须回到 `knowledge/sources/`、`raw/` 原文、精确 locator 和人工复核，并遵循 [system/paper-evidence-gate.md](system/paper-evidence-gate.md)。

## 研究范围

- 基于熔合蒸发反应的低能原子核结构研究；
- A≈130 质量区原子核；
- 原子核转动与振动；
- wobbling motion；
- chiral doublet bands；
- γ 形变、γ-soft deformation 和 γ-rigid deformation；
- 相关实验判据、理论模型及竞争解释。

## 推荐阅读入口

| 需要了解的内容 | 入口 |
| --- | --- |
| Wiki、Obsidian 和日常使用方法 | [USER_GUIDE.md](USER_GUIDE.md) |
| 详细使用说明、术语和示例提示词 | [USER_GUIDE_DETAIL.md](USER_GUIDE_DETAIL.md) |
| 已有核素、能带和主题 | [knowledge/index.md](knowledge/index.md) |
| 知识库规模和健康状态 | [knowledge/overview.md](knowledge/overview.md) |
| 尚未解决的科研问题 | [knowledge/questions.md](knowledge/questions.md) |
| 当前阶段计划和用户备忘 | [PLAN.md](PLAN.md) |
| 90 天持续学习工作流与队列 | [system/workflows/continuous-learning.md](system/workflows/continuous-learning.md) · [system/learning-queue.md](system/learning-queue.md) |
| 最近一次 Agent 执行交接 | [system/handoff.md](system/handoff.md) |
| 摄入论文 | [system/workflows/ingest.md](system/workflows/ingest.md) |
| 查询知识库 | [system/workflows/query.md](system/workflows/query.md) |
| 跨来源综合与反向检验 | [system/workflows/reflect.md](system/workflows/reflect.md) |
| L0–L4 科研自治、每周自测与人工关口 | [system/workflows/autonomous-research.md](system/workflows/autonomous-research.md) |
| Agent 能力采用、hook 与 farmer 恢复 | [system/agent-capability-adoption.md](system/agent-capability-adoption.md) |
| Agent 能力升级与自我进化流程 | [system/agent-capability-upgrade.md](system/agent-capability-upgrade.md) |
| 自动检查 | [system/workflows/lint.md](system/workflows/lint.md) |
| 字段、页面类型和命名规则 | [system/schema.md](system/schema.md) |
| 术语和禁止混并的概念 | [system/vocabulary.md](system/vocabulary.md) |
| Zotero 连接方式 | [system/zotero-integration.md](system/zotero-integration.md) |
| 论文级证据门 | [system/paper-evidence-gate.md](system/paper-evidence-gate.md) |
| 完整人工检查 | [check.md](check.md) |

日常主要浏览 `knowledge/`。`raw/` 保存原始证据，`system/` 保存规则与执行交接，`outputs/` 保存审计和写作产物。

推荐流程：

```text
Zotero Wiki Inbox
→ PDF 放入 raw/papers
→ Agent 摄入
→ 用户在 Obsidian 审阅
→ synthesis 跨来源综合
→ outputs 形成文章、报告或汇报
→ lint
→ Git commit/push
```

自动检查命令：

```bash
python system/scripts/wiki_lint.py --fail-on error
```

会话 hook 与 farmer 的显式检查命令见
[`system/scripts/README.md`](system/scripts/README.md)。

## Repository information

文献摄入推荐按“一篇摄入 → 本地 WIP → 用户审核 → amend 为 final → 再摄入下一篇”串行推进，以减少共享知识页重叠。确需并行时可保留多个 pending WIP，但写入前必须检查文件 overlap，并选择合并、依赖或暂缓共享文件。

- Canonical repository: [Gitee `chx6/silicon_graduate`](https://gitee.com/chx6/silicon_graduate)
- GitHub 若存在仅作为 Gitee 镜像，不承担本库维护或 CI。
- Citation: [`CITATION.cff`](CITATION.cff)
- License: [`LICENSE`](LICENSE)
- Disclaimer: [`DISCLAIMER.md`](DISCLAIMER.md)
- Contributions: [`CONTRIBUTING.md`](CONTRIBUTING.md)

## README、PLAN 与 handoff

- `README.md` 是稳定、简洁的 Wiki 入口，不保存大量阶段性待办。
- `PLAN.md` 是用户拥有和维护的宏观阶段计划、个人好奇心备忘和研究方向草稿，不是执行日志或 cite-key 文献清单。
- `system/handoff.md` 是 Agent 的执行交接，记录最近完成事项、具体状态、文件修改、未解决问题和下一步。

Agent 只在任务涉及阶段计划、研究优先级、文献选择方向、项目建立、长期探索或多步骤知识库建设等场景时读取 `PLAN.md`；普通小任务以 handoff 恢复执行状态。`PLAN.md` 管方向和好奇心，`system/handoff.md` 管状态和交接细节。

若三者存在冲突，当前用户明确指令永远最高；方向与优先级以 `PLAN.md` 为准，最近执行事实与交接细节以 `system/handoff.md` 为准。无法分类时，Agent 应停止并询问用户。

## Agent 使用规则

Agent 必须遵循 [AGENTS.md](AGENTS.md)，按规定读取启动文件，保护用户已有修改和 `raw/` 原始证据，不得以猜测补写事实或擅自覆盖 `PLAN.md`。
