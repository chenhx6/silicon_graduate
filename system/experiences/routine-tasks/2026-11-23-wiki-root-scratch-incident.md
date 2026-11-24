---
type: system-incident-postmortem
title: "Wiki 根目录临时产物误落与跨平台路径问题"
created: 2026-11-23
updated: 2026-11-23
graph-excluded: true
tags: [incident, routine-task, scratch, workspace-boundary]
---

# Wiki 根目录临时产物误落与跨平台路径问题

2026-11-21 至 22 日，馆藏核读的 PDF 截图和文本提取使用了相对输出名，产物随当前工作目录落到 Wiki 根目录。两次任务还在 Linux 上直接使用 Windows 工作路径，生成了以 `C:\Users\...` 为字面名称的目录。五张图随后又被复制到根目录。Bash 收到 Windows 的 `taskkill` 与 `nul` 重定向写法，命令失败并留下 `nul` 文件。

核查确认 121 个未跟踪的临时文件，约 28.3 MiB，包含早期遗留的两个 `.degree-read-*` 目录。它们已完整移入 `tmp/20261123-wiki-root-scratch/`，同目录的 `original-paths.json` 记录移动前后的名字。旧路径检查会检查 canonical 目录及 `outputs/` 分类，根目录临时文件在其检查范围之外。另有一批馆藏改动已经提交在学习分支，工作文件仍在 `main` 的检出中，Git 状态需要按两条分支分别检查。

## 下次如何执行

1. 启动 PDF 渲染、OCR 或阅读 worker 前，在本机 Wiki 的 `tmp/<task>/` 下分配绝对输出目录。把该目录指定为输出路径或进程工作目录。向 worker 提供原件的绝对只读路径，避免切换工作目录后读取错误原件。
2. 按执行端解析路径与命令。Linux 不接收 Windows 盘符路径作为输出目录。Python 调用外部命令时可用 `subprocess.DEVNULL` 做跨平台静默重定向。
3. 任务收尾执行 `python3 system/scripts/wiki_boundary_check.py --root .`。遇到 `ROOT_SCRATCH_ARTIFACT`，按列出的路径核对归属，将确认的临时产物完整移到 `tmp/`。使用明确的文件清单暂存提交。并行长任务在各自的工作树中修改文件，避免独立索引提交后留下共享工作树差异。

相关规则见 [路径契约](../../path-contract.md) 和 [检查手册](../../../check.md)。
