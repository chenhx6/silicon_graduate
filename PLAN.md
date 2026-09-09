# Wiki 阶段计划（用户拥有）

> 本文件由用户拥有和维护。Agent 仅在用户明确要求时修改；它记录宏观方向、研究优先级和未来问题，不替代执行日志、WIP queue 或 handoff。

## 已完成里程碑

- Evidence Wiki v0 与 Continuous Research-Learning v1 已建立可追溯 source、claim、locator、review、QMD 和 Git 治理。
- 关键高自旋谱学方法、wobbling/chirality、γ-soft/γ-rigid、shape coexistence、TiP 与 `sigma/I` 证据已形成可复用知识层。
- Wiki 项目级文件边界完成验收：Wiki 内可写，Wiki 外只读且不可提权，不影响其它项目。
- Continuous Research-Learning v2（硅基研究生 V2）已完成 pilot 与发布验收：摄入默认 L2；L3 可调查课题和竞争解释；L4 由用户确认数据后手动启动并形成 manifest、代码、测试、失败检查与 belief revision。
- `131Ce` 已建立 Alwaleedi 2013 结构基线、L3 竞争解释地图，以及 Singh 2016、Li 2004、Petrache 1998 lifetime-informed L4。物理结论保持 provisional。

## 当前发布状态

- Continuous Research-Learning v2（硅基研究生 V2）已完成全仓库检查、去重、公开内容审计与非 force fast-forward 发布。
- canonical Git reference 为 annotated tag `continuous-research-learning-v2`；实际远端状态以 Git ref 和 Gitee `chx6/silicon_graduate` 为准，结构检查以本地 Wiki lint 为准。GitHub 仅作为 Gitee 镜像，不承担本库维护。

## 下一阶段：用户独立 `131Ce` 数据

用户提供 Wiki 内数据路径并手动启动 L4 后：

1. 为独立实验建立单独 manifest，记录身份、哈希、单位、不确定度、校准、角度覆盖和处理版本；
2. 完成 level/band/transition identity mapping，不预设其扩展博士论文能级纲图；
3. 与 thesis 和 lifetime 数据分层比较，不静默合并统计量或重复证据；
4. 依据数据实际包含的偏振、角关联、mixing ratio、寿命或符合关系，选择能够最大改变解释排序的分析；
5. 结果先作为 provisional finding，只有通过针对性科学审核后才能进入正式论文结论。

启动格式：

```text
开始 131Ce L4：数据=<Wiki 内路径>；问题=<可省略>
```

## 真实证据缺口

- Alwaleedi Figure 5.5 的 gated branching intensities；
- Bands 1–7 连接跃迁的 measured mixing ratio `δ`、符号与线偏振；
- 伙伴带之间可比较的 absolute `B(E2)`、`B(M1)`、`Q_t` 与带间/带内矩阵；
- normal-deformed 与 highly-deformed 序列之间的 linking/decay-out、混合或共同形变不变量；
- 能把 signature/configuration coupling、γ-soft core response、chirality、wobbling 和 shape coexistence 明确区分的最小 observable 组合。

## 动态研究节奏与每周自测

- 不采用“每天至少若干篇”或“每 5/10 篇固定综合”的机械指标；是否继续、暂停或进入 L3 取决于问题价值、信息增益、证据充分度、资源成本和权限边界。
- 每周自测用于纠正知识、发现反证和形成高价值问题；可自然进入 L3，但 L4 candidate 必须 safe suspend 并等待用户确认数据和手动启动。
- 有实质变化时建立本地 commit 与 P0/P1 报告；用户集中审核后才能 push。无实质变化时不制造空 commit。
- 自动调度尚未创建；未来由用户在 Codex 应用中启用后，Wiki 只记录并核验真实运行回执。

## QMD MCP 暂缓

当前继续使用 project-local QMD CLI 作为 `knowledge/**/*.md` 的可重建候选检索层。MCP daemon/常驻服务暂缓，直到多轮真实查询表明 CLI 成为稳定瓶颈且收益超过后台服务、路径与资源维护成本；QMD 不接管 Git，也不替代 source/raw 复核。

## 维护边界

- 用户维护本文件中的阶段目标、优先级和备忘；Agent 不把它改写为 cite-key 清单或执行流水账。
- 当前执行事实写入 `system/handoff.md`，未完成检查点写入 `system/wip-queue.md`，历史事件追加到 `system/log.md`。
