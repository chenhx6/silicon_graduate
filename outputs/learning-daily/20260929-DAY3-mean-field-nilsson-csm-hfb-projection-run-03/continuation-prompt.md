# Day 3 最终续接提示：平均场、Nilsson/CSM、HFB 与投影模型

本日学习窗口已于 2026-09-30 15:00 Asia/Shanghai 关闭；继续讨论可恢复同一 Codex session，但 Day 3 不再开启新的科学路线。

- run id：`2026-09-29-day-03-03`
- session：`01a0eb92-e525-7863-a0c9-af73a53d832b`
- 恢复命令：`codex resume 01a0eb92-e525-7863-a0c9-af73a53d832b -C /workspace/wiki -s danger-full-access -a never`
- 日报：`outputs/learning-daily/20260929-DAY3-mean-field-nilsson-csm-hfb-projection.md`
- receipt：`outputs/learning-daily/20260929-DAY3-mean-field-nilsson-csm-hfb-projection-run-03/run.json`
- 下一日任务：`outputs/learning-daily/prompts/20260930-DAY4-pairing-quasiparticle-configuration.md`

## 本日可恢复状态

- Hara–Sun Table 5 direct TPSM 覆盖仍是 `2/7`（`133La`、`135Pr`）。余下 `134La`、`135Ce`、`136Pr`、`137Pr`、`137Nd` 本轮未核实到直接 PSM/TPSM；后三核有 CDFT/PRM/HA 或 TAC 路线，但不算角动量投影。
- `131Xe` odd-neutron TPSM 显示 `1ν/1ν+2π` 到 `3ν/3ν+2π` 基底扩展；`γ=29°` 是沿用输入，yrare 带未观测，非正交投影振幅不是概率。
- Banik 2020 的 APS publisher-direct PDF 已完整阅读，SHA-256：`21e7e1eed7a93ffc3c38f4580fcf93863d02c56e40ffc900b1634df14c7f34e6`；Nature Downloader OA-only route 返回 `oa_not_found`，公开 publisher URL 直接给 PDF；未取 SI。该 38-MeV INGA acquisition 被 2022 TPSM 能谱比较与 2023 重分析复用，不能重复计为三次独立实验。
- 仍有 band-label 交叉问题：Banik 2020 称高自旋 B1(a) 为 signature partner；C23 对同一数据重分析后偏向低自旋 yrare `13/2−` 序列，并说 yrast `13/2−` 起源未决。不要在没有逐跃迁 crosswalk 时合并 B1(a)、B5 和 C23 标签。
- Banik TRS 的 `γ≈−26°` 是特定转频能面输出，TPSM `29°` 是固定输入，TPRM `33°` 是模型再现参数；pairwise 差为 `3°/4°/7°`，不求平均、不称独立形状测量。
- 131Ce 当前完整 crosswalk 包含六条带间支路：Band 1→Band 4 的 504.9-keV M1/E2（25/2−→23/2−）和 871.2-keV E2；Band 4→Band 1 的 538.3-keV M1/E2（15/2−→13/2−）和 611.1-keV M1/E2；Band 4→yrast 的 994.3-和 1108-keV E2。Table 4.2/4.4、Figure 4.1/4.5 与 §4.3.1/§5.2.1 共同给出身份和方向。504.9 行端点已知；611.1 是带间线，243.7 才是同自旋变化的 Band 4 带内线。仍缺 branch-resolved measured δ/偏振、伙伴寿命/绝对强度、response/covariance；没有打开新来源批次。

## canonical 知识入口

- `knowledge/sources/banik-2020-131xe-multiple-band-structures.md`
- `knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md`
- `knowledge/models/triaxial-projected-shell-model.md`
- `knowledge/models/cranked-shell-model.md`
- `knowledge/projects/a130-model-choice-card.md`
- `knowledge/questions.md`

保持全部新 claims 的 `needs_review: true` 和相关页面原 review 状态；不要修改 `knowledge/nuclei/131xe.md`。
