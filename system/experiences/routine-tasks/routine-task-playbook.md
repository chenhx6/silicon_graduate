---
type: system-playbook
title: "常规工程任务执行军规与最佳实践"
created: 2026-10-30
updated: 2026-10-30
graph-excluded: true
---

# 常规工程任务执行军规与最佳实践

## 1. 显式版本控制原则

1. **绝对禁止盲目 `git add .`**：
   - 任何提交必须显式列出具体文件路径，严格防止将未授权的 raw PDF、BibTeX 本地缓存、临时测试目录或继承的无关脏文件带入暂存区。
2. **提交前双重自检**：
   - 运行 `git diff --check`（工作树无未解冲突和空白残余）；
   - 运行 `git diff --cached --check`（暂存区格式无错误）。
3. **远端非 Force 严格推送**：
   - 永远遵循标准流水线：
     ```bash
     git fetch origin main
     git merge-base --is-ancestor origin/main HEAD
     git push --dry-run origin HEAD:main
     git push origin HEAD:main
     ```
   - 严禁使用 `--force`，严禁改写已发布分支历史。

## 2. 状态机与工作树一致性

1. **状态文件原子化落盘**：
   - 任务在状态迁移时（如 `in_progress` -> `completed`），必须确保内存状态、JSON 状态文件与 Git 提交三者严格原子化对齐。
2. **守护进程与锁管理**：
   - 检查并维护 `wiki_farmer.py` 存活，绝不无故终止或重复拉起守护进程；
   - 严格尊重 `/tmp/*.lock` 锁机制，退出时安全释放或移交。

## 3. 防幻觉与执行回验

1. **工具调用真实性第一**：
   - 决不在回复中“列举已执行步骤”而省略实际工具调用；说到的步骤必须在终端有实际返回值；
2. **调用结项命令的唯一充要条件**：
   - 必须通过 `git status` 确认所有成果已成功提交，远端已确认推送成功，才允许调用 `update_goal(complete)`。
