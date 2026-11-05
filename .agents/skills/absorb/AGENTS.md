# AGENTS.md — Wiki absorb 技能目录

本目录实现 `absorb`：自动盘点 Git 库中新加入的外来内容，固定来源与许可，隔离分析缺陷和价值，
通过吸收矩阵选择 `keep/adapt/reference-only/reject`，再以最小改动、测试、审查和实测优化完成闭环。
`SKILL.md` 是流程权威；`scripts/absorb_inventory.py` 生成覆盖清单与风险信号，
`scripts/test_absorb_inventory.py` 覆盖提交/暂存/工作树分版本、gitlink、类型变化、符号链接、
ignored 开关、许可证、秘密和截断扫描边界。

运行清单放在 `tmp/runs/absorb/`，不执行外来代码、安装器、hook、Makefile 或二进制；
不修改 `raw/`、`PLAN.md`、凭据、全局配置或无关工作树。来源、许可和适配记录见
`PROVENANCE.md` 与 `references/sources.md`。
