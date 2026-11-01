---
type: system-workflow
graph-excluded: true
operation: research-archive
updated: 2026-11-01
---

# 研究材料留档

本规则适用于研究使用的论文、学位论文、外部笔记、报告、图片、网页快照、
数据、补充材料和参考代码。原始材料保存在 `raw/`，可复用的研究认识写入
`knowledge/`，过程回执放在 `outputs/`。现有用户资料使用原路径；新获取的材料
按 `system/path-contract.md` 的类型目录归档。图片及其配套网页快照使用
`raw/figures/gpt/learning-daily/<date>-<topic>/`。

每个研究单元先建立所用材料清单，实际获取的字节在本地归档。单文件来源页须填写
`raw_file`、`raw_sha256`、`archive_required: true`。多文件材料用
`manifest.json` 登记，每条包含仓库相对 `raw/` 路径、64 位 SHA-256、原始 URL
或本地来源说明；清单顶层包含带时区的实际 `retrieved_at`。有文件大小时同时登记。
来源页指向清单，并保留逐文件 locator、阅读范围和未取得全文的限制。只获得摘要、
元数据或访问失败页时，归档实际获得的内容并标明其身份，不冒充全文。
来源页同样记录清单本身的 `raw_sha256`，文件内容和清单身份分别核验。
其它 `*_file`/`*_sha256` 配套材料也验证；`library_file` 是原 Zotero 库的外部
书目指针，`actual_body_file`、`public_staging_file` 和 `staging_file` 是已有页面的
历史暂存记录，均不作为已归档凭证
或访问外部目录的授权；有效原件由 `raw_file` 校验。

新产生的分析笔记仍按路径契约写入 `knowledge/`；不把 AI 总结复制到 `raw/`
冒充原始材料。用户提供的未发表数据和个人文档保持本地，留档授权不扩大为公开
发布授权。移动 raw 需要用户对指定范围明确授权，并保留路径映射与哈希。

确定性检查：

```bash
python3 system/scripts/wiki_archive_gate.py check --root . --changed
python3 system/scripts/wiki_archive_gate.py check --root . -- knowledge/sources/example.md raw/figures/gpt/learning-daily/example/manifest.json
python3 system/scripts/wiki_archive_gate.py check --root . --full
```

`--changed` 检查所有已暂存、未暂存和未跟踪的来源页、当前清单，以及已设置
`archive_required: true` 的来源。它还复核六类 `gpt/learning-daily/` 下的归档清单，
因此被 Git 忽略的 raw 材料丢失也会失败。缺档、错哈希、空清单、外部路径或声明
路径不存在均返回非零退出码；不自动修复、覆盖、删除或下载。

归档门已接入 `wiki_automation_preflight.py`，每日 runner 与现有 Git 发布脚本会
执行它；显式 `wiki_hook.py after-edit` 和 `session-summary` 也执行检查。它不是
安装到 Codex 或 `.git/hooks/` 的全局拦截器，不能发现完全没有登记的下载。技能入口为
`.agents/skills/research-archive/SKILL.md`；`AGENTS.md` 负责在任务开始时路由到本规则。

`--full` 用于全库缺档盘点。历史缺口单列恢复队列，不自动降低检查标准、修改原件
哈希或清除 review 状态；有界检查通过不等于全库已完成归档。

旧下载器的 `results`/`sources` 回执与逐文件归档清单是不同格式。自动发现会把可识别
的旧回执列入 `legacy_receipts_not_archive_validated`，不把其视为已通过归档核验；
若来源页直接指向这些回执，仍须按归档清单要求验证。新清单登记
`archive_type: research-archive-v1`，已有的 `files` 格式清单同样接受；不修改历史原件。
