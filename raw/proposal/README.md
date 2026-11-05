# Proposal 与束流申请

本目录是束流申请等 proposal 的 canonical 保存位置，保存初稿、修订稿及必要配套材料，允许 Git 跟踪、commit/push。执行任务计划使用 `outputs/plans/`，论文手稿使用 `raw/writing/gpt/`。

当前三份材料均为早期草案，可继续修改和补充；不表示已经提交、获批，或已有实验结果。此次迁移保持原文件名、正文与状态不变。

## 当前草案

- [131Xe 宇称与混合比分支响应闭合束流申请](20261101-131xe-branch-response-beam-request.md)
- [133I γSF/LEE 束流申请](20261101-133i-gamma-strength-beam-request.md)
- [跨质量区实验与探测器方案](20261101-cross-mass-experiment-detector-beam-prospectus.md)

## 保存约定

- 单文件初稿使用 `YYYYMMDD-topic.md`；有源码、图表或附件时使用 `<topic>/` 组织申请包。
- 保留草案、修订与实际提交状态；普通修改由 Git 历史追踪，不为每次编辑制造重复副本。
- 申请书可引用知识库，但可复用的事实、方法、竞争解释及研究设计仍由 `knowledge/` 承载。目录迁移不新增科学结论。
- 本次三份草案从 `outputs/plans/` 原样迁入，逐文件 SHA-256 验证见 `outputs/self-tests/20261105-proposal-path-migration.json`。
