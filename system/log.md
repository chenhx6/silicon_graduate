---
type: system-log
graph-excluded: true
created: 2026-07-01
updated: 2026-07-15
---

# 操作日志

本文件仅追加。格式：

`## [YYYY-MM-DD HH:MM] operation | description`

## [2026-07-01] initialize | 建立低能核结构研究 Wiki 的治理层与第一版结构

## [2026-07-01] audit | 完成初始化结构核查；0 个结构性失败，qmd 未安装，端到端摄入待验证

## [2026-07-01] restructure | 将编译知识层重命名为 knowledge；模板、日志和输出分别归入 system 与 outputs

## [2026-07-01] git | 建立本地 Git 基线提交 9264fdb；PDF 和大型原始资料未跟踪

## [2026-07-01] ingest | Zamfir & Casten 1991：γ-soft/γ-rigid 的 γ-band staggering 判据

## [2026-07-01] ingest | Frauendorf & Meng 1997：aplanar TAC 与核转动手征性

## [2026-07-01] ingest | Chakraborty et al. 2023：131Xe wobbling/signature partner 判别

## [2026-07-01] ingest | Frauendorf 2024：wobbling 模型、证据与争议综述

## [2026-07-01] synthesize | 建立 γ-soft/rigid、chiral TAC、wobbling/signature 三个证据矩阵

## [2026-07-01] audit | 第一版核查：45 个 knowledge Markdown、181 个 Wikilink、0 断链、4/4 来源哈希匹配

## [2026-07-01] configure | 用户完成 Obsidian vault、Dataview、私有 GitHub 仓库与 Zotero Wiki Inbox 自动导出

## [2026-07-01] review | 用户轻度校准 131Xe 两个待审能带页和 wobbling/signature 综合页，整体评价良好

## [2026-07-01] ingest | Ayangeakaa et al. 2016：133Ce 中高自旋谱学、CNS 与 TAC-CDFT

## [2026-07-01] ingest | Petrache et al. 2020：137Nd 两对候选手征双重带

## [2026-07-01] ingest | Ding et al. 2021：131Ba/133Ce g7/2 强耦合带与 signature splitting 多机制

## [2026-07-01] synthesize | 建立 signature splitting 的非轴性、低-j mixing 与 Coriolis 耦合证据矩阵

## [2026-07-01] audit | 第二轮核查：64 个 knowledge Markdown、372 个 Wikilink、0 断链、7/7 来源哈希匹配

## [2026-07-02] git | 用户提交并推送 Obsidian/Zotero 桥接配置；main 已跟踪 origin/main

## [2026-07-02] review | 用户审阅 137Nd D2-D3、D5-D6 与 signature-splitting 机制综合，未发现大的问题

## [2026-07-02] automate | 实现标准库 Wiki lint、声明式配置、6 项测试和 GitHub Actions

## [2026-07-02] audit | 自动 lint 本地通过：61 个正式页、372 个 Wikilink、7/7 source hash、0 error、0 warning

## [2026-07-02] automation | 03:35 一次性 heartbeat 未触发且无运行记录；11:15 删除后由当前会话继续收尾

## [2026-07-02] git | 自动 lint 提交 d807369 已推送 origin/main；私有仓库 Actions 状态因当前环境未登录而暂未核验

## [2026-07-02] postmortem | 03:35 heartbeat 到期时本地调度进程不活跃；建立回执门、长等待禁用 heartbeat 和一次性界面无歧义规则

## [2026-07-02] correction | 用户确认故障时应用持续开启、电脑持续接电且禁用休眠；根因收敛为 Codex 后台调度链路未消费 heartbeat

## [2026-07-02] workflow | 用户建立 README/PLAN 类根目录笔记，用于阶段记录、使用备忘和下一步计划；Agent 保持只读

## [2026-07-02] structure | 将 RAEDME + PLAN.md 拆分为可迁移的 README.md 与用户拥有的 PLAN.md，并规范 Agent 启动顺序

## [2026-07-02] governance | PLAN 改为条件读取并与 handoff 按方向/执行事实分工；新增 safe suspend、Git 检查与人工唤醒恢复规则

## [2026-07-02] skill | 新建 instruction-only wiki-evidence-query，用于默认只读、可追溯且区分证据类型的核结构知识问答

## [2026-07-02] governance | 建立论文级证据门、页面/claim 双层人工审阅规则与日常摄入闭环；9 PDF/9 BibTeX 已核对，7 个 source citation key 精确同步

## [2026-07-02] lint | claim-level 审阅与字段缺失统计接入 Wiki lint、overview 和 check；待审 claim 以非阻断 info 暴露

## [2026-07-02] documentation | wiki-evidence-query 以独立 commit 提交；新增详细用户说明书，简洁指南与 README 只同步入口

## [2026-07-02] ingest-project | 以 review/background 摄入 De Voigt 1983 高自旋综述，建立高自旋基础页面与 A≈130 证据地图 project seed；保留 3 条新增 claim 待人工复核

## [2026-07-02] governance | 写入 bounded initiative 与 Windows PowerShell Git PATH fallback；允许必要最小同步，禁止非必要顺手优化

## [2026-07-02] review | 用户审阅 De Voigt 1983 source；确认经典高自旋术语、γ 探测基础与机制框架仍可作为有效背景，页面升级为 human-reviewed，3 条二手转述 claim 保持待审

## [2026-07-02] claim-review | 用户逐条对照 De Voigt 1983 原文确认 8 条 Key Results；DV83-2、DV83-7、DV83-8 的 needs_review 改为 false

## [2026-07-03] workflow | 固化九类 ingest strategy、Global ingest rules、短提示词接口与 vocabulary 最小同步边界

## [2026-07-03] ingest-project | 深读摄入 Domscheit 1999 `163Lu` 三轴超形变实验与 UC/PES 比较；建立 13 条待审 claims、核素/SD1/SD2/实验/超形变/四极矩页面，并仅以非 A≈130 比较背景接入 A≈130 project

## [2026-07-03] claim-review | 用户确认 Domscheit 1999 citation key、科学表述及 5n/4n 反应道；DO99-1 至 DO99-13 完成复核，并补充 SD-ND two-band mixing 等中英术语消歧

## [2026-07-03] ingest-project | 深读摄入 Matta 2015 `135Pr` transverse-wobbling 支持方实验；建立 15 条 claims、核素/四带/两实验页和争议 project，保留 14 条待审且不 commit/push

## [2026-07-03] claim-review | 用户审核 Matta 2015 source 与全部 Key Results；M15-1 至 M15-15 完成复核，派生页与争议 project 保持 unreviewed

## [2026-07-03] claim-review | 用户完成 A16-2、C23-2/C23-5、F24-2/F24-4/F24-7、FM97-6、P20-2、ZC91-5 复核；当前结构化 claim-level 待审队列清零

## [2026-07-03] terminology | 建立双语术语归一化 seed registry；query 与 wiki-evidence-query 支持中文、英文、缩写和实验口语扩展并保留歧义边界

## [2026-07-03] ingest-project | 深读摄入 Sensharma 2019 `135Pr` two-phonon wobbling 支持方实验；建立 13 条分层 claims、TW2 候选带和独立 DGS 数据集页，并将其作为依赖 Matta 2015 assignment 的支持链接入争议 project；保留 12 条待审且不 commit/push

## [2026-07-03] claim-review | 用户审核 Sensharma 2019 source 与全部 Key Results；S19-1 至 S19-13 完成原文核对，source 升级为 human-reviewed，派生页与争议 project 保持 unreviewed

## [2026-07-03] correction | 按用户校正将 Sensharma 2019 的强非谐性表述改为 successive wobbling-phonon spacing 关系，避免把第二声子增量误写成 TW2/TW1 带能量的简单倍数关系

## [2026-07-03] safe-suspend | Lv 2022 counter-source 已完成 PDF/BibTeX 预检、深读、13 条 claims 与 JUROGAM II experiment 页；因执行余量不足暂停跨页/project 同步，等待“继续摄入文献lv_2022_Evidencewobbling”

## [2026-07-03] ingest-project | 续跑完成 Lv 2022 `135Pr` counter-source：将联合 polarization/angular-correlation、mixing-ratio 双解、M1-dominated links、能级重组与 QTR realignment 接入争议 project；保留 12 条待审且不 commit/push

## [2026-07-03] correction | 按用户复核校正 Lv 2022 L22-13 的模型证据边界：区分 Fig.3(d) 机制示意、p.5 realignment 正文陈述与 Fig.4(c) 的近恒定 j_parallel，避免把后者误作主轴分量图证

## [2026-07-03] claim-review | 用户审核 Lv 2022 source 与全部 Key Results；L22-1 至 L22-13 完成核对，source 升级为 human-reviewed，派生页与争议 project 保持 unreviewed

## [2026-07-03] synthesize-project | 基于 Matta 2015、Sensharma 2019 与 Lv 2022 重构 `135Pr` wobbling controversy evidence matrix；分层记录观测、判据、解释、模型、反证、证据门和 follow-up，并在 PLAN 中追加 TiP 理论/实验知识建设方向

## [2026-07-03] ingest-project | 深读摄入 Sensharma 2020 `187Au` longitudinal-wobbling 支持方实验；建立 15 条 claims、核素/yrast/LW/SP/实验页和独立争议 project，并以判据层链接 `135Pr` 争议；保留 14 条待审且不 commit/push

## [2026-07-04] review | 用户审核 `135Pr` evidence matrix 全页与 Sensharma 2020 source/AU20-1 至 AU20-15，未发现问题；两页升级为 human-reviewed，派生页与 `187Au` project 保持 unreviewed

## [2026-07-04 03:40] ingest-project | 深读摄入 Guo 2022 `187Au` low-spin wobbling counter-source；建立 17 条分层 claims 与 HIRFL `R_ac-P` experiment，更新三条 band、核素、判据/模型页及 two-sided controversy project；全部 claims 待审，未建 umbrella project，未 commit/push

## [2026-07-04 05:14] claim-review | 用户确认 Guo 2022 G22-3、G22-4、G22-15；补充粉色 `α=-1/2` unfavored-signature sequence 身份、Rupnik β 衰变至 `I=19/2` 的覆盖，以及 `J=j+R` 中低自旋 `R≈1ħ` 的 wobbling-approximation 限制；其余 14 条 claims 待审

## [2026-07-04 05:23] git | Guo 2022 `187Au` counter-source 与本轮 claim-review 以 commit `e7b08a2` 提交并推送至 `origin/main`；用户 `.obsidian/graph.json` 与 `raw/zotero/wiki-inbox.bib` 修改未纳入

## [2026-07-04 14:42] claim-review | 用户确认 Guo 2022 source 与其余 14 条 claims；source 升级为 human-reviewed，G22-1 至 G22-17 全部改为 `needs_review: false`，结构化 claim 待审队列再次清零

## [2026-07-04 14:58] git | Guo 2022 source 全量审核状态以 commit `20656c9` 提交并推送至 `origin/main`；用户 `.obsidian/graph.json` 与 `raw/zotero/wiki-inbox.bib` 修改未纳入

## [2026-07-04 15:15] automation-audit | 未找到清晨 `187Au` project-level synthesis 的自动化配置、运行线程、运行回执或匹配产物；按回执门判定未触发/未执行，由当前会话直接运行

## [2026-07-04 15:15] synthesize-project | 基于已人工复核的 Sensharma 2020 与 Guo 2022 重构 `187Au` controversy locator-level evidence matrix；新增 AU-SYN-1 至 AU-SYN-10 待审综合 claims、paper evidence gate、unresolved issues 与 follow-up sources，不裁决争议，不 commit/push

## [2026-07-04] review-supplement | 用户审核 `187Au` project 的 AU-SYN-1 至 AU-SYN-10；project 升级为 human-reviewed。Guo/Lv 2022 supplementary material 作为各自主文附属证据层挂接，不新建 DOI/Bib/source；新增 G22-18 至 G22-20、L22-14 至 L22-15 与 AU-SYN-11 至 AU-SYN-12 待审，并在 PLAN 记录 TiP 摄入后启动 low-spin wobbling umbrella project

## [2026-07-04] git | `187Au` controversy synthesis、supplementary evidence 挂接与 umbrella PLAN 以 commit `41bcc6d` 提交并推送至 `origin/main`；用户 `.obsidian`、raw PDF 与 `wiki-inbox.bib` 修改未纳入

## [2026-07-04] claim-review | 用户确认 Guo/Lv supplementary material 新增的 G22-18 至 G22-20、L22-14 至 L22-15 与 project synthesis AU-SYN-11 至 AU-SYN-12；144 条结构化 source claims 待审队列清零

## [2026-07-04] workflow | 文献摄入默认本地 WIP、不 push；审核后 amend 为 final commit，safe suspend 大量 diff 时优先本地 WIP checkpoint，避免临时提交累积与持续高 CPU

## [2026-07-04] synthesize-project | 新建 low-spin wobbling controversies umbrella project，将已审核的 `135Pr/187Au` 案例接入共享 identification framework；新增 7 条待审跨案例 synthesis claims、TiP future extension、data-analysis bridge 与 innovation candidates，不裁决争议

## [2026-07-04] git | umbrella project 草案创建本地 WIP commit，未 push；用户 `.obsidian` 与 raw/BibTeX 修改未纳入

## [2026-07-04] review | 用户审核 low-spin wobbling umbrella project 与 LSW-SYN-1 至 LSW-SYN-7；校准大 `abs(δ)`/predominant-E2 为必要但非充分判据，并区分增强 E2 的其他机制与 γ-softness 形变动力学

## [2026-07-04] git | umbrella project WIP amend 为 `Build low-spin wobbling controversies evidence map` 并推送至 `origin/main`；用户 `.obsidian` 与 raw/BibTeX 修改未纳入

## [2026-07-04] ingest-project | 深读摄入 Lawrie 2020 TiP 理论基础；建立 15 条待审 theory claims 与 tilted-precession concept，并将 3D QTR、wobbling approximation、coupling geometry 和 phonon quantization 边界接入 low-spin wobbling umbrella

## [2026-07-04] git | Lawrie 2020 theory-ingest 创建本地 WIP commit，未 push；用户 `.obsidian` 与 raw/BibTeX/PDF 未纳入

## [2026-07-04] claim-review | 用户审核 Lawrie 2020 source 与 LAW20-1 至 LAW20-15；校准 Fig.4 中 `f(n,I)` 自旋趋势的参数/耦合适用范围，并明确 Eq.34 的 1 轴为最大-MoI intermediate axis

## [2026-07-04] git | Lawrie 2020 theory-ingest WIP amend 为 `Ingest Lawrie 2020 TiP and wobbling framework` 并推送至 `origin/main`；用户 `.obsidian` 与 raw/BibTeX 改动未纳入

## [2026-07-04] ingest-project | 深读摄入 Lv 2021 `135Nd` experimental TiP case；建立 LV21-1 至 LV21-18、D1/TiP1/TiP2、JUROGAM II experiment，并将 M1-dominated links、QTR energies/wave functions/transition ratios 与 TiP-vs-wobbling 边界接入 low-spin umbrella

## [2026-07-04] git | Lv 2021 `135Nd` 摄入创建本地 WIP commit，未 push；用户 `.obsidian` 与 raw/BibTeX/PDF 未纳入

## [2026-07-04] claim-review | 用户审核 Lv 2021 source 与 LV21-1 至 LV21-18；以 Table II 和 E2-fraction consistency 校准 618.3/566.8 keV mixing ratios，补齐 75.5°/104.5° clover geometry 与 LV21-13 的 TiP model-consistency 语义

## [2026-07-04] git | Lv 2021 `135Nd` experimental TiP WIP amend 为 `Ingest Lv 2021 experimental TiP bands in 135Nd` 并推送至 `origin/main`；用户 `.obsidian` 与 raw/BibTeX/PDF 改动未纳入

## [2026-07-05] synthesize-project | 基于已审核 Lawrie 2020/Lv 2021 source claims 将 TiP 作为 low-spin wobbling alternative framework 接入 umbrella；新增 LSW-TIP-SYN-1 至 LSW-TIP-SYN-8、近似条件/耦合/判据矩阵与 `135Pr/187Au` cross-case boundaries，19 条 project-level synthesis notes 待审，不 commit/push

## [2026-07-05] review | 用户审核 TiP / low-spin wobbling umbrella synthesis；LSW-SYN-5、LSW-THEORY-1 至 LSW-THEORY-5、LSW-TIP-1 至 LSW-TIP-5、LSW-TIP-SYN-1 至 LSW-TIP-SYN-8 共 19 条 notes 改为 `needs_review: false`；LSW-THEORY-1 校准为 Bohr–Mottelson Vol. II 提出 principal-axis rotation + harmonic-phonon wobbling approximation，Lawrie 2020 负责与完整 TiP/3D rotation 对照并检验适用条件，原书留作 future primary-source ingestion

## [2026-07-05] git | TiP / low-spin wobbling project synthesis 以 `Integrate reviewed TiP synthesis into low-spin wobbling project` 提交并推送至 `origin/main`；用户 `.obsidian/graph.json` 与 `raw/zotero/wiki-inbox.bib` 改动未纳入

## [2026-07-05] governance | 将 bounded initiative 第四条改为以可验证验收标准收敛任务的 Agent 行为契约
## [2026-07-05] daily-ingest-project | 按 Nomura 2017 → Nomura 2021 → Babra 2019 顺序完成 γ-soft deformation 三文献批次摄入

- Nomura 2017 采用 `theory-ingest + project-ingest`，建立 NOM17-1 至 NOM17-10。
- Nomura 2021 采用 `theory-ingest + project-ingest`，建立 NOM21-1 至 NOM21-9。
- Babra 2019 采用 `experiment-ingest + project-ingest`，建立 B19-1 至 B19-12；实验寿命/`Q_t`、模型结果与作者形变解释分层记录。
- 更新 A≈130 evidence-map project 的来源角色、证据缺口与 data-analysis bridge；不创建 synthesis，不修改 raw。
- 三篇 source 与 31 条 claims 均待用户审核；自动 lint 为 0 error、10 warning、31 info。

## [2026-07-05] git | γ-soft 三文献批次创建单一本地 WIP ingest checkpoint

- message：`WIP ingest: gamma-soft three-paper batch for user review`。
- 仅纳入本批 13 个知识库文件；用户 `.obsidian/graph.json`、`raw/zotero/wiki-inbox.bib` 与 raw PDF 未纳入。
- 未 push；等待用户审核 NOM17-1 至 NOM17-10、NOM21-1 至 NOM21-9、B19-1 至 B19-12 后 amend/finalize。

## [2026-07-05] claim-review | 用户审核 γ-soft 三文献 source notes 与 31 条 claims

- NOM17-7 限定为偶偶核 `0+_1` 的 Fig.13 结果；NOM17-8 补齐 Figs.14-15 中奇 A 各低能态的态依赖变化。
- NOM21-7 补齐 D-F 与 W-J/O(6) 极限定义、四个参考值、Fig.3 计算点位置及对 `131Ce/133Ce` 的奇 A 外推边界。
- B19-4 将 `stopping power` 绑定中文释义“阻停能力”。
- 三篇 source 升级为 `human-reviewed`，NOM17-1 至 NOM17-10、NOM21-1 至 NOM21-9、B19-1 至 B19-12 全部改为 `needs_review: false`。

## [2026-07-05] synthesize-project | 建立 gamma-soft deformation evidence map 并扩写阶段性 synthesis

- 新建 gamma-soft project，按 theory/experiment、模型、观测量、证据缺口、low-spin relation 与未来 `131Ce/133Ce` 数据入口组织。
- 扩写既有 `gamma-soft-vs-gamma-rigid-diagnostics`，没有创建重复 synthesis。
- 基于 Zamfir–Casten 1991、Nomura 2017/2021、Babra 2019 和 low-spin review/background 完成反向检验；不把模型解释写成实验事实，不把 γ-soft 自动绑定 wobbling。
- 新增 GSD-PROJ-1 至 GSD-PROJ-6 与 GSD-SYN-1 至 GSD-SYN-8，共 14 条跨来源 statements 待用户审核。
- 自动 lint 为 0 error、10 warning、0 info；未修改 raw、PDF、数据、图片、PLAN 或治理规则。

## [2026-07-05] git | gamma-soft project + synthesis 创建本地 WIP checkpoint

- message：`WIP synthesis: gamma-soft deformation evidence map for user review`。
- 仅纳入本轮 9 个 project/synthesis/必要同步文件；用户 `.obsidian/graph.json` 与 `raw/zotero/wiki-inbox.bib` 未纳入。
- 未 push；等待用户审核 GSD-PROJ-1 至 GSD-PROJ-6 与 GSD-SYN-1 至 GSD-SYN-8。

## [2026-07-05] review-synthesis | 用户审核 gamma-soft project 与 synthesis 的 14 条跨来源 statements

- GSD-PROJ-4 重写为三层证据链：实验寿命/`Q_t` 与带交叉约束集体性变化，TRS/TPSM 给出模型形变结果，作者据此提出 γ-soft→rigid/stable-triaxial transition；不把模型形状写成直接实验事实。
- 手征双重带与 wobbling bands 记录为稳定三轴性研究的重要候选集体指纹，但模式指认不能单独证明 γ-rigid 形变。
- 重点扩展 GSD-SYN-5 与 soft-to-rigid transition 专节，并按用户授权在 `PLAN.md` 写入 A≈130、特别是 `131Ce/133Ce` 的未来证据摄入计划。
- GSD-PROJ-1 至 GSD-PROJ-6、GSD-SYN-1 至 GSD-SYN-8 全部改为 `needs_review: false`；project 与 synthesis 页面升级为 `human-reviewed`。

## [2026-07-05] theory-ingest-project | Nomura 2022：γ-soft odd-mass low-spin bands 的 IBFM alternative

- 全文精读并视觉核对 Figs.1-13、Tables I-II；新建 source 与 IBFM model，建立 NOM22-1 至 NOM22-15 待审 claims。
- 分层记录 EDF→IBM-2/IBFM assumptions、四核谱与 E2/M1 model results、既有实验值 comparison、作者对 earlier wobbling assignments 的 challenge，以及 `127Xe` 异常大计算 `abs(δ)` 对结论普遍化的限制。
- Umbrella project 新增 LSW-IBFM-1 至 LSW-IBFM-4，gamma-soft project 新增 GSD-PROJ-7；IBFM alternative 与 TiP/QTR 分开，不把理论结果写成实验事实或最终裁决。

## [2026-07-05] claim-review | 用户审核 Nomura 2022 source 并完成 source 级收尾

- NOM22-10 明确补入 `105Pd` 原 wobbling paper 中 band B/C 与本文 B1/B2 的对应关系，避免跨文献带标号混淆。
- NOM22-11 改写为分别陈述 `B(E2)out/B(E2)in` 与 `B(M1)out/B(E2)in`；对 `133La` 明确前者 agreement 较好、后者仍偏大，并同步修正 NOM22-8 的相同表述风险。
- [[nomura-2022-questioning-wobbling-ibfm]] 升级为 `human-reviewed`；NOM22-1 至 NOM22-15 全部改为 `needs_review: false`。
- [[low-spin-wobbling-controversies]] 与 [[gamma-soft-deformation-evidence-map]] 同步为“Nomura 2022 source 已审、LSW-IBFM-1 至 4 与 GSD-PROJ-7 仍待审”。
- 复核后 lint 为 114 pages、1124 Wikilinks、20/20 source hash、0 error、10 warning、0 info；source claim 待审队列清零，剩余 5 条 project-level notes 待审。

## [2026-07-05] claim-review | 用户确认 Nomura 2022 project notes 已审核通过

- LSW-IBFM-1 至 LSW-IBFM-4 与 GSD-PROJ-7 全部由 `needs_review: true` 改为 `needs_review: false`。
- `low-spin-wobbling-controversies` 与 `gamma-soft-deformation-evidence-map` 中关于 Nomura 2022 的 project-level 待审提示改为已审收口。
- `knowledge/overview.md` 中 project-level synthesis 待审计数同步清零。
- `135Pr` 只加理论 cross-reference；`133La/127Xe/105Pd` 不建空壳 nucleus/project；`187Au` 只记录本文模型空间困难。未新增 synthesis，未修改 raw。

## [2026-07-05] governance | 建立 Human review triage protocol

- 为 ingest、project/synthesis、data-analysis-bridge 和 claim-review-update 定义 P0/P1/P2/P3 审核优先级与统一复盘格式。
- P0 全部列出，P1 限前 10，P2/P3 按文件聚合，并要求给出精力有限时优先审核的 3–5 个位置。
- Paper evidence gate 候选默认进入 P0/P1；P0 未审核前不建议 final amend 或 push。

## [2026-07-06] synthesize-project | 建立 low-spin wobbling、γ-soft deformation 与 TiP/IBFM alternatives 跨主题研究地图

- 新建 cross-project synthesis，按 conceptual layers、共享实验判据、case map、model landscape、observed/model/interpretation 分层、evidence gaps 与未来 `19F+116Sn` 数据入口组织。
- 更新 low-spin umbrella 的 γ-soft context、`136Sm` 背景参照、TiP/IBFM 区分、E2/M1 ratio 记录边界和 gamma-soft-aware model stress-test 候选。
- 新增 LSW-XPROJ-1 至 LSW-XPROJ-5 与 LSW-GSAI-SYN-1 至 LSW-GSAI-SYN-10，全部为 `needs_review: true`；不改变既有已审核 source/project claims。
- 最小同步 gamma-soft project、index、overview、handoff；不扩写 concept/model/observable，不修改 PLAN、raw、PDF、数据、图片或治理规则。
- 自动 lint：115 pages、1172 Wikilinks、20/20 source hashes、0 error、10 warning、1 info；未 push。

## [2026-07-06] claim-review | 用户确认跨主题综合审核通过

- `[[low-spin-wobbling-controversies]]` 中 LSW-XPROJ-1 至 LSW-XPROJ-5 全部改为 `needs_review: false`，页面恢复为 `human-reviewed`。
- `[[low-spin-wobbling-gamma-soft-deformation-and-alternative-interpretations]]` 中 LSW-GSAI-SYN-1 至 LSW-GSAI-SYN-10 全部改为 `needs_review: false`，页面升级为 `human-reviewed`。
- `knowledge/overview.md`、`system/handoff.md` 与 `system/log.md` 同步清除本轮 cross-project 待审提示；不修改 raw、PDF、数据、图片、PLAN 或治理规则。

## [2026-07-06] governance | 明确 human-review WIP 的 amend 收口优先级

- 文献摄入等待审核统一使用 `WIP ingest:`；project、synthesis 与跨来源综合等待审核统一使用 `WIP review:`。
- 用户审核完成并要求 final commit/push 后，必须 amend 对应 WIP，不保留独立 WIP 后再新增 final commit；该仓库内授权优先于通用“不主动 amend”约束。
- Final commit message 由用户指定时原样使用；未指定时由 Codex 推荐直接相关的 message 并在最终报告中说明。

## [2026-07-06] tooling | 启用 QMD project-local 本地检索层

- 安装状态确认为 QMD `2.5.3`；初始化被 Git 忽略的 `.qmd/`，`nuclear-knowledge` 只索引 `knowledge/**/*.md`。
- 建立 118 个文档、348 个向量 chunk，并下载 embedding、generation、reranking 本地模型。
- BM25、语义与完整 hybrid 检索均通过；按实测性能建立 direct read → BM25 → semantic → full hybrid 的分层路由。
- 明确 `qmd pull` 只管理模型，禁止 `qmd update --pull` 接管 Git；搜索结果必须回读完整页面和 source/raw。
- 同步 AGENTS、check、query/lint workflow、USER_GUIDE、详细指南、PLAN、memory 与 handoff；未修改科学知识页或 raw。

## [2026-07-07] framework | Optimized ingest startup and recap budget: Active handoff replaces full startup handoff, log tail-only rule clarified, ingest strategies split into runtime short rules plus detail tutorial, ordinary ingest QMD embed/overview updates made deferrable, no-unfiltered-scan rule added, active summary/staged PDF reading/compact recap rules synchronized; no science pages or raw files modified.

## [2026-07-07] framework | Active handoff refreshed and wording clarified after framework optimization commit 769b9ab; clarified README startup, workflow detail vs PDF reading depth, ordinary single-paper ingest, sequential multi-paper ingest, reading-depth expectations, automatic handoff/log closeout, and safe suspend/checkpoint expectations.

## [2026-07-08] framework | Review-finalization trigger was confirmed/supplemented and Pending WIP queue workflow was added; active sigma-over-I WIP ingest `7b1e52a` was preserved separately and not pushed.

## [2026-07-08] claim-review | 用户完成 sigma-over-I alignment sources 审核并请求 finalization

- Draper 1970 补充 DR70-3 mixed final population `\bar{P}(M)`、DR70-6 Fig.3 `bdry` mixture boundary 解释、DR70-7 stretched E2 定义。
- Zobel 1980 补充 Z80-3 三未知量歧义的 a/b/c 出路、Z80-10 Gaussian/ALY 条件性重点、Fig.5 lifetime-to-`αK` 位移记录，并同步 project 写作支撑。
- Zobel 1983 source 按用户审核意见完成收口；三篇 source 与 sigma-over-I project 均升级为 `human-reviewed`，相关 `needs_review` 清零。
- `knowledge/overview.md`、`system/handoff.md` 与 `system/wip-queue.md` 已同步；QMD update/embed/status 成功；lint 为 0 error、10 warning、0 info。
- 本地 final commit 已创建；push 到 `origin/main` 连续两次因 GitHub `443` 连接超时失败，随后按用户建议使用 `http://127.0.0.1:7890` proxy 仍因本地代理端口不可达失败，当前为 not pushed。

## [2026-07-09] checkpoint | article4-6 sigma-over-I deorientation ingest：Cejnar 1996 completed

- Completed source: [[cejnar-1996-spin-deorientation-alpha-2n-gamma]] with C96-1 to C96-11.
- Current source in progress: none; next source is Radeck 2012.
- Unfinished items: Radeck 2012 and Lauritsen 2025 source ingests; final checks/report/WIP commit.
- Locator gaps: none identified for Cejnar key claims; figures not digitized.
- P0/P1 risks: C96-4/C96-5/C96-10 and project SIO-PROJ-7/SIO-PROJ-8 require user review.
- Continuation prompt: Continue article4-6 ingest from Radeck 2012 PDF and update checkpoint after that source.

## [2026-07-09] checkpoint | article4-6 sigma-over-I deorientation ingest：Radeck 2012 completed

- Completed source: [[radeck-2012-deorientation-lifetime-98ru-rdds]] with R12-1 to R12-12.
- Current source in progress: none; next source is Lauritsen 2025.
- Unfinished items: Lauritsen 2025 source ingest; final checks/report/WIP commit.
- Locator gaps: none identified for Radeck key claims; figure curves not digitized.
- P0/P1 risks: R12-3 boundary, R12-7/R12-8/R12-10 formula-chain claims, and project SIO-PROJ-9/SIO-PROJ-10 require user review.
- Continuation prompt: Continue article4-6 ingest from Lauritsen 2025 PDF and update checkpoint after that source.

## [2026-07-09] checkpoint | article4-6 sigma-over-I deorientation ingest: Lauritsen 2025 completed

- Completed source: [[lauritsen-2025-gamma-angular-formalism-tracking-arrays]] with L25-1 to L25-15.
- Completed article4-6 three-source source-note/project-map ingest and updated project evidence rows SIO-PROJ-11/SIO-PROJ-12.
- Added or updated method/concept anchors: [[tracking-array]], [[angular-correlation]], [[deorientation]], [[angular-distribution]], [[linear-polarization-asymmetry]], [[attenuation-coefficient]], [[sigma-over-i]].
- Lint passed with 0 errors / 10 warnings / 38 info; Cejnar/Radeck/Lauritsen new claims remain human-review pending.
- Next action: finish QMD refresh, final report, WIP queue, and local WIP ingest commit without push.

## [2026-07-09] finalization | article4-6 sigma-over-I source review

- Applied user review edits to C96-4, R12-7 and L25-14; marked Cejnar 1996, Radeck 2012, Lauritsen 2025 and SIO-PROJ-7--SIO-PROJ-12 reviewed.
- Added [[152dy]] and [[atlas-gretina-152dy-ca48-191mev]] for Lauritsen 2025 `152Dy` experimental information.
- Lint passed with 0 errors / 10 warnings / 0 info; lint unittest passed; QMD update/embed/status succeeded.
- Final commit created and article4-6 WIP queue entry moved to completed; final commit pushed to `origin/main`.

## [2026-07-09] checkpoint | article7-9 sigma-over-I practice ingest: Chiara 2012 completed

- Completed source: [[chiara-2012-cu65-cu67-core-coupled-protons]] with CH12-1 to CH12-8.
- Current source in progress: `2013_Summary of Bases for Spin and Parity Assignments.pdf`.
- Unfinished items: Summary 2013 source note; Gray 2020 source note; project update; minimal method/concept updates; checks/report/local WIP ingest commit.
- Locator gaps: none identified for Chiara targeted `sigma/I` claims; Summary 2013 and Gray 2020 not yet checked.
- P0/P1 risks: Chiara `sigma/I=0.5` AD assumption and `1115 keV` `delta` sensitivity remain human-review pending.
- Continuation prompt: Continue article7-9 from Summary 2013 high-spin angular-distribution / DCO sections and checkpoint before starting Gray 2020.

## [2026-07-09] checkpoint | article7-9 sigma-over-I practice ingest: Summary 2013 completed

- Completed source: [[summary-2013-bases-spin-parity-assignments]] with SB13-1 to SB13-7.
- Current source in progress: Gray 2020 hyperfine-field / `g`-factor paper.
- Unfinished items: Gray 2020 source note; project update; minimal method/concept updates; checks/report/local WIP ingest commit.
- Locator gaps: none identified for Summary 2013 targeted high-spin assignment rules; Gray 2020 not yet checked.
- P0/P1 risks: keep Summary 2013 at guide-level `σ/I = 0.3` practice background; do not promote it into a universal prior.
- Continuation prompt: Continue article7-9 from Gray 2020 TDPAD `R(t)` amplitudes and empirical alignment-expectation sections.

## [2026-07-09] checkpoint | article7-9 sigma-over-I practice ingest: Gray 2020 completed

- Completed source: [[gray-2020-hyperfine-fields-g-factor-measurements]] with G20-1 to G20-9.
- Current source in progress: none; source-note ingest for the three requested papers is complete.
- Unfinished items: project update; minimal method-page additions; checks/report/local WIP ingest commit.
- Locator gaps: none identified for Gray 2020 targeted alignment-amplitude claims.
- P0/P1 risks: keep Gray 2020 in a TDPAD / host-specific boundary role; do not generalize its `sigma/I` discussion to ordinary P-ADO fitting.
- Continuation prompt: Continue article7-9 from project update and minimal method pages before final checks.

## [2026-07-09] wip | article7-9 sigma-over-I practice ingest packaged for review

- Completed: project/method/index/overview updates for article7-9, plus QMD refresh.
- Checks: `wiki_lint` passed with 0 errors; QMD update/embed/status succeeded after sandbox escalation.
- Pending: wait for user review of CH12-*, SB13-*, G20-* and SIO-PROJ-13/14/15. External report written to `E:\imp\prompt\wiki\article7-9_reports.md`. Local `HEAD` is now the article7-9 `WIP ingest:` commit and was not pushed.

## [2026-07-09] review-finalized | article7-9 sigma-over-I practice sources

- User review finalized CH12-*, SB13-*, G20-* and SIO-PROJ-13/14/15; corresponding source/project pages were moved to `human-reviewed` / `needs_review: false`.
- Applied review corrections: CH12-5 softened to adopted/literature-`δ` range wording; Summary 2013 corrected to `σ/I = 0.3`; Gray 2020 now records extra source-backed factors affecting inferred `σ` scale.
- Checks: `wiki_lint` passed with 0 errors / 10 warnings / 0 info; QMD update/embed/status succeeded after sandbox escalation.

## [2026-07-09] checkpoint | article10-11 supplemental core ingest: Ekstrom 1979 completed

- Completed source: [[ekstrom-1979-spin-alignment-attenuation-a61-a67]] with EK79-1 to EK79-9.
- Current source in progress: Ionescu 1981 improved angular-distribution analysis.
- Unfinished items: Ionescu source note; project and knowledge-page updates; checks; report; local `WIP ingest:` commit.
- Locator gaps: none identified for the Ekstrom 1979 claims already entered.
- P0/P1 risks: keep MANDY/CNR alignment estimates separate from user-code `sigma/I`, and keep the Gaussian-limitation claim at the "too restrictive" level rather than a universal invalidation.
- Continuation prompt: Continue article10-11 from Ionescu 1981 source note, then integrate both papers into the `sigma-over-i` project before final checks.

## [2026-07-09] recovery | article10-11 supplemental core ingest repaired after interruption

- Recovery audit confirmed that the Ekstrom 1979 source note needed repair, while the Ionescu 1981 source note was largely complete and only needed minimal metadata / extracted-page cleanup.
- Repaired or confirmed: [[ekstrom-1979-spin-alignment-attenuation-a61-a67]], [[ionescu-1981-improved-angular-distribution-analysis-particle-xn]], [[direct-feeding]], [[compound-nucleus-reaction-model]], [[spin-alignment-attenuation-factor]], and the `sigma-over-i` project evidence rows for EK79 / IO81.
- Remaining before closeout: final Git/lint checks, external report write, and the local not-pushed article10-11 commit.

## [2026-07-09] local-commit | article10-11 supplemental core ingest sanity-checked

- Scope of sanity review is limited to `git diff --check`, `wiki_lint`, and staged-file hygiene; no new long-form scientific review was performed in this turn.
- Prepared local not-pushed commit scope: [[ekstrom-1979-spin-alignment-attenuation-a61-a67]], [[ionescu-1981-improved-angular-distribution-analysis-particle-xn]], [[direct-feeding]], [[compound-nucleus-reaction-model]], [[spin-alignment-attenuation-factor]], [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]], [[knowledge/index]], plus handoff/log/queue updates.

## [2026-07-09] follow-up | ionescu branching-ratio delta note added

- After user review corrections on Ekstrom/Ionescu, added a new follow-up task in `PLAN.md` and a new source-level note `IO81-10` about model-dependent `delta` values inferred from branching ratios in Ionescu 1981.
- Follow-up status: `git diff --check` and `wiki_lint` pass; only `IO81-10` remains claim-level pending review, so push was deferred.

## [2026-07-09] review-finalized | article10-11 iionescu follow-up approved

- User approved `IO81-10`, keeping the core wording that branching-ratio-derived `delta` values are model dependent and belong to an intraband rotational-band context.
- Article10-11 now has no remaining source/project claim-level review items; next step is QMD refresh, amend local commit `6609bc3`, and push.

## [2026-07-09] push-blocked | article10-11 final commit ready but GitHub unreachable

- Article10-11 review-finalized content is now in local final commit `4fb459c` on `main`; `wiki_lint`, `git diff --check`, and QMD refresh all succeeded.
- `git push origin HEAD:main` failed because `github.com:443` was unreachable at the time of the attempt, so only a push retry remains.

## [2026-07-09] pushed | article10-11 supplemental ingest finalized to origin/main

- After syncing `system/handoff.md`, `system/log.md`, and `system/wip-queue.md`, the final article10-11 commit was amended to `f4934e7` and pushed to `origin/main`.
- Scope remains the reviewed Ekstrom 1979 / Ionescu 1981 supplemental ingest plus the user-requested `PLAN.md` note; `.obsidian/` and `raw/zotero/wiki-inbox.bib` stayed outside the commit.

## [2026-07-10] framework | clarify experimental nuclear-structure scope beyond A130

- Clarified that the current main mass region is a research anchor rather than a Wiki collection boundary.
- Ingest scope and lightweight page decisions must follow source-supported experimental nuclear-structure value, evidence density, reuse value, comparative value, and explicit user-declared priority instead of mass region alone.
- Long-term framework text stays abstract and must not infer user participation history or store personal-title / reaction-specific background.

## [2026-07-10] synthesis-planning | sigma-over-I writing-support synthesis created locally

- Completed a readiness audit across the sigma-over-I project, 11 source notes, and related concept/method pages; no current source-note metadata/locator/kind blocker was found.
- Added `knowledge/synthesis/sigma-over-i-assumptions-and-mixing-ratio-extraction.md` and updated the sigma-over-I project page plus `knowledge/index.md`.
- This is a local WIP review state only: overview/QMD refresh is deferred, push is intentionally not done, and human review is still required for terminology mapping and paper-evidence-gate boundaries.

## [2026-07-10] review-follow-up | repaired index display and tightened sigma-over-I wording

- Restored `knowledge/index.md` from a clean base after user-reported display corruption, repaired the handoff title line, and kept the new sigma-over-I synthesis entry in the index.
- Updated the sigma-over-I project/synthesis/concept chain to reflect the user's review: split the Ekstrom Gaussian-limitation and threshold/feeding conclusions, preserved the reaction-threshold wording boundary, and added a bounded low-spin caution plus an explicit user-analysis normalization note that is not source-backed evidence.
- State remains local review only: no push, overview/QMD still deferred, and the current WIP review commit should be amended rather than duplicated.

## [2026-07-10] review-finalized | sigma-over-I synthesis planning approved for finalization

- User accepted the bounded conclusion that the present 11-paper package does not yet supply direct low-spin-specific `sigma/I` sensitivity evidence strong enough for a stronger universal claim.
- Promoted the reviewed sigma-over-I project/synthesis/terminology pages to `review_status: human-reviewed`, refreshed `knowledge/overview.md`, and completed `qmd.cmd update`, `qmd.cmd embed -c nuclear-knowledge`, and `qmd.cmd status`.
- The prior local `WIP review:` commit was converted into the final `Create sigma-over-I writing-support synthesis` commit; only the push remained at this checkpoint.

## [2026-07-10] framework | review-history workflow added

- Added `system/review-history.md` as the forward-looking index for completed review/finalization tasks; no old completed reviews were backfilled.
- Synchronized Pending WIP queue, review-finalization, user-guide, and checklist rules so future finalized reviews move from pending queue into review history without extra queue-only status commits unless a sync step was truly missed.

## [2026-07-10] framework | review-history semantics and evidence guidance refined

- Refined human-review history, review-commit traceability, and evidence-calibrated citation guidance.

## [2026-07-10] framework | optimized wiki-informed evidence query skill

- Reframed `.agents/skills/wiki-evidence-query/SKILL.md` around Wiki-as-personalization-layer open-world ordinary Q&A, with conditional governance reads, Fast/Standard/Deep routing, external-verification triggers, answer scaling, stop conditions, and read-only state-file boundaries.
- Minimally synchronized `system/workflows/query.md` so ordinary mode may use stable general background without pretending it is Wiki evidence, and corrected `system/evidence-policy.md` heading from four to six statement classes.

## [2026-07-10] framework | surfaced useful knowledge and corrected review semantics

- Compressed `wiki-evidence-query` while making review status a disclosure and verification-priority signal rather than a visibility, value, or manuscript-eligibility filter.
- Added active surfacing of high-information unreviewed material, claim-specific verification on unreviewed pages, and rechecking/deeper extraction of previously reviewed material; synchronized query workflow and evidence policy without changing Review history.

## [2026-07-10] framework | aligned paper gate with claim-specific verification

- Replaced page-status-based paper admission with candidate discovery, focused claim/source verification, and explicit user-confirmed admission for the proposed manuscript wording.
- Clarified claim-scoped P0/P1 review and future writing-skill candidate handling; minimally synchronized the evidence-query description, user guides, and checklist without changing science pages or Review history.

## [2026-07-10] framework | aligned review, output, and Wiki growth rules

- Updated long-term memory and user guidance for the public GitHub remote and exclusion of unpublished, collaboration, peer-review, personal, and sensitive raw material.
- Aligned high-value candidate surfacing, reviewed-knowledge rechecking/growth, claim-specific paper admission, Review history boundaries, and complete strict-mode triggers across current governance files.

## [2026-07-10] maintenance | added public repository metadata package

- Added public licensing, citation metadata, bilingual disclaimer, contribution files, and the current bibliography snapshot.

## [2026-07-10] framework | improved clickable Wiki evidence navigation

- Standardized ordinary evidence entries as page name, one-sentence support note, and a verified absolute `file.md:line` content link.
- Recorded that Codex opens these links in the live rendered editable view, with file-plus-section fallback when direct line navigation is unavailable; no science or review-history content was changed.

## [2026-07-10] framework | closed failed read-only evidence route

- Confirmed that neither ordinary Markdown line links nor inline code-comment references can reliably force unchanged Wiki files into a read-only review surface.
- Retained verified exact-line evidence navigation with file-plus-section fallback and prohibited evidence-page edits, fake diffs, or temporary commits as UI workarounds.

## [2026-07-10] governance | added editable-evidence line-ending safeguards

- Added repository LF rules for Markdown and common text formats, with binary handling for PDF/image/archive/ROOT files; no repository-wide renormalization was performed.
- Recorded the ignore-EOL verification and restore procedure for evidence pages opened in the editable Codex view, while keeping local `.obsidian/` state outside commits.

## [2026-07-11] governance | added knowledge dirty-state Git preflight

- Added a mandatory documented preflight before every stage, commit, and push: classify modified knowledge pages, verify unrelated evidence-view noise with file-specific ignore-EOL diffs, and block Git writes when substantive differences remain.
- Kept the workflow documentation-only: no scripts, hooks, repository-wide renormalization, or knowledge/source content changes were added.

## [2026-07-11] governance | added write-entry preflight and EOL cleanup

- Added a tracked-knowledge EOL-only cleanup script and moved dirty-state classification to the first repository write while retaining commit and pre-push checks.
- Added dirty baselines, dynamic file-entry scope, staged-file isolation, pending-WIP overlap/dependency rules, and a serial-review recommendation with safe parallel WIP support.
- Kept scientific work on review WIPs while allowing fully specified governance tasks to final directly; no knowledge content was modified.

## [2026-07-11] governance | restricted cleanup to LF/CRLF changes

- Changed cleanup comparison from `--ignore-space-at-eol` to `--ignore-cr-at-eol`, preserving trailing spaces, Markdown double-space line breaks, and Tabs as substantive changes.
- Added post-restore status verification, DryRun candidate counting, and expanded temporary-repository safety coverage including Chinese paths; no knowledge content was modified.

## [2026-07-12] governance | completed inline evidence-link governance

- Consolidated Wiki evidence presentation around inline informative page/source plus line links, removed the default duplicate end-of-answer evidence section, and documented the detailed user-facing behavior.
- Kept generic anchors as prohibited examples only; synchronized query workflow and checklist without modifying knowledge content.

## [2026-07-12] governance | closed Wiki-miss open-knowledge ambiguity

- Replaced the over-absolute user-guide wording with a single rule: report Wiki evidence boundaries, add stable general background in ordinary Q&A when useful, and keep its provenance distinct from Wiki-grounded or externally verified evidence.
- Added checklist coverage for non-refusal on Wiki misses and prevention of model-memory source fabrication; no knowledge content was modified.

## [2026-07-12] ingest | added four gamma-spectroscopy method sources

- Ingested Rezynkina 2017, Kramer-Flecken 1989, Kibedi 2008, and Rusev 2009; added internal-conversion method/observable anchors; updated DCO, angular-correlation, polarization, mixing-ratio, and sigma-over-I project pages.
- Left `knowledge/overview.md` and QMD refresh deferred for post-review finalization; kept `raw/zotero/wiki-inbox.bib` untouched as a protected user change.

## [2026-07-12] review | finalized gamma-spectroscopy method source review

- Applied user review to the four-source method bundle and the related sigma-over-I project notes.
- Corrected the KF89 `sigma/I` low-spin `I < 6` wording, added the experimental `R_DCO` intensity-ratio formula, and tightened `RU09-6` into an author-judgment branch-selection note. QMD refresh and wiki lint succeeded.

## [2026-07-13] ingest-checkpoint | Meng 2010 nuclear chirality review

- Deep-read Meng 2010 and added a source note, core chirality/MχD concepts, TAC/PRM boundary updates, and the initial nuclear-chirality/MχD evidence-map project.
- Safe-suspended before Ayangeakaa 2013 and Liu 2016 because repeated multi-file patch stalls made further expansion unreliable; next run must recover and amend the same local WIP.

## [2026-07-13] ingest-checkpoint | Ayangeakaa 2013 133Ce MChD

- Deep-read the `133Ce` PRL and added the source, two source-specific MChD pair pages, DCO/angular-distribution assignments, `S(I)`, RMF+TPRM model roles, lifetime gap, and triaxial-shape-coexistence boundary.
- All `A13-1..12` remain pending joint human review; Liu 2016 is the next and final source in this WIP.

## [2026-07-13] ingest-checkpoint | Liu 2016 78Br MChD and octupole correlations

- Deep-read Liu 2016 and added `78Br` structure, ADO/polarization, two MChD pair pages, eight-E1-link evidence, octupole observables/terminology, and MDC-CDFT/TPRM boundaries.
- The three-source project matrix and overview are complete locally; all 38 source claims await one joint user review, with QMD deferred to review finalization.

## [2026-07-13] review | finalized nuclear-chirality/MχD source review

- Applied the joint review to Meng 2010, Ayangeakaa 2013, and Liu 2016; all 39 source claims are now reviewed.
- Clarified semiclassical TAC tunneling, `133Ce` bandheads and bounded `135Nd` systematics, `78Br` quartet future-observation wording, and the cross-source role of `S(I)`.

## [2026-07-13] ingest-checkpoint | Jones 2002 Compton polarimeter calibration

- Deep-read Jones 2002 and added the source note with P/A/Q definitions, Klein-Nishina sensitivity, a2/a4 and Rose-Brink formalism, calibration examples, and low-energy detector boundaries.
- Go 2024 and Longfellow 2026 remain to be ingested; detailed Jones sign-sensitive and numerical claims are pending human review.

## [2026-07-13] ingest-checkpoint | Go 2024 CdTe Compton-camera demonstration

- Deep-read Go 2024 and added the source note covering the 20-layer CdTe camera, `56Fe(p,p'gamma)` 847-keV calibration, two-hit event selection, Geant4/ComptonSoft response, likelihood inference, modulation factor and sensitivity-efficiency trade-off.
- Longfellow 2026 remains to be ingested; Go numerical detector claims and response-inference locators are pending human review.

## [2026-07-13] ingest-checkpoint | Longfellow 2026 GRETINA in-beam polarimetry

- Deep-read Longfellow 2026 and added the source note covering energy ordering, Gaussian alignment, P/A0/Q, mixed-transition ambiguity, laboratory-frame Lorentz aberration/Jacobian and separate Doppler-energy correction.
- All three source notes are complete; project/method-page updates and final checks remain. Formula-level and numerical claims await user review.

## [2026-07-13] ingest-checkpoint | gamma-ray linear-polarization evidence map

- Added the project `gamma-ray-linear-polarization-in-nuclear-spectroscopy` and minimal P/A/Q, Compton, modulation, efficiency, Lorentz and Doppler knowledge anchors; updated the index and overview.
- Wiki lint passes with 0 errors; QMD and final Git checks remain before a local WIP commit. No push is authorized in this task.

## [2026-07-13] ingest-checkpoint | gamma-ray linear-polarization QMD refresh

- `qmd update`, `qmd embed -c nuclear-knowledge` and `qmd status` completed; the collection has 190 indexed Markdown files and 999 embedded vectors with no pending count shown.
- Final Git checks and the local WIP checkpoint commit remain; no push is authorized.

## [2026-07-13] ingest | gamma-ray linear-polarization WIP checkpoint

- Created local `WIP ingest: gamma-ray linear polarization sources for user review` on `main` after explicit staging, lint/tests, QMD refresh and staged diff checks.
- Post-commit cleanup/status show only the protected `raw/zotero/wiki-inbox.bib` change; no push was performed.

## [2026-07-13] review | gamma-ray linear-polarization source bundle

- User review completed for Jones 2002, Go 2024, Longfellow 2026 and the evidence map. Corrected the J02-13 table pipe escape and restored the Go Eq.3 `nu_j` division index; source/project claim review markers are cleared.
- Existing `raw/zotero/wiki-inbox.bib` is explicitly authorized for the final amend/push; final lint, QMD refresh and Git checks remain.

## [2026-07-13] ingest-checkpoint | Diamond 1966 nuclear alignment

- Deep-read and added `knowledge/sources/diamond-1966-nuclear-alignment-heavy-ion-reactions.md` with claims D66-1..11 covering heavy-ion entrance alignment, Gaussian m-substate approximation, A2/A4 angular distributions, spin-sequence constraints, alignment-dependent mixing-ratio inference, and extranuclear deorientation limits.
- Frauendorf 2001 remains in staged deep reading. The protected `raw/zotero/wiki-inbox.bib` change is still unstaged; no commit or push has been performed for this task.

## [2026-07-13] ingest-checkpoint | nuclear alignment and rotating-symmetry sources

- Completed deep-read source notes for Diamond 1966 (D66-1..11) and Frauendorf 2001 (F01-1..15), with source-level review markers retained.
- Added rotating-mean-field, spontaneous-symmetry-breaking, magnetic/antimagnetic rotation, shears, band-termination, reflection-asymmetry and Routhian anchors; updated chirality, TAC, rotational-band, alignment, angular-distribution, mixing-ratio and sigma-over-I links.
- Wiki lint passes with 0 errors, 12 existing warnings and 26 expected needs-review infos. Final explicit staging and local WIP commit remain; no push is authorized. The existing `raw/zotero/wiki-inbox.bib` change remains unstaged.

## [2026-07-13] ingest | nuclear alignment and rotating-symmetry WIP checkpoint

- Created local WIP commit (`Ingest nuclear alignment and rotating-symmetry sources`) on `main` after amending checkpoint metadata; current `HEAD` is the recovery pointer and no push was performed.
- Only the protected pre-existing `raw/zotero/wiki-inbox.bib` remains unstaged. Human review is pending for D66-1..11, F01-1..15 and the new rotating-nuclei theory pages.

## [2026-07-13] review-finalization | nuclear alignment and rotating-symmetry sources

- User accepted D66-1..11 and F01-1..15; source review markers were cleared and the overview/project status was synchronized.
- Final lint, QMD refresh, explicit staging and WIP amend completed; the final review commit was pushed to `origin/main`. The user explicitly authorized staging the existing `raw/zotero/wiki-inbox.bib`.

## [2026-07-14] setup | full Nature Skills global install

- Cloned `Yuan1z0825/nature-skills` to `C:\Users\22721\ai-skills\nature-skills` and installed all `_shared` / `nature-*` skill directories into `C:\Users\22721\.codex\skills`.
- Upstream `scripts/update-codex-skills.sh --check` reports all installed directories match the clone. Optional per-skill Python/MCP/API dependencies were not installed.

## [2026-07-15] architecture | continuous research-learning upgrade Phase 0

- Recorded the user-approved Phase 0 decisions and clean `main@803a19d` baseline on `codex/continuous-research-learning-upgrade` in a planned architecture update.
- Created the single local Phase 0 checkpoint commit with only the architecture update, Active handoff and this short log; no active rule, science page, research-note infrastructure, QMD configuration, pilot, or push was performed. Phase 1 requires explicit user approval.

## [2026-07-15] architecture | continuous research-learning upgrade Phase 1

- Separated user ingest modes from completed `reading_depth`, added the standard research-learning loop and analytical-reconstruction boundary, clarified provisional promotion and ordinary/research routing, and removed the P0 hard-cap behavior.
- No science page, research-note instance, QMD configuration or push was included; Phase 1 validation and local checkpoint commit follow.

## [2026-07-15] architecture | continuous research-learning upgrade Phase 2

- Added the controlled `research-note` type, five-state maturity model, template, persistence/promotion lifecycle, ordinary-query exclusion, structural lint/test coverage, and thin Skill/Guide routing.
- No real research-note instance, science page, QMD collection change or push was included; Phase 2 validation and local checkpoint commit follow.

## [2026-07-15] pilot | continuous research-learning upgrade Phase 3

- Supplemented Kibédi 2008 BrIcc and Nomura 2022 IBFM with auditable question, design, evidence-chain, transfer/failure and persistence assessments.
- No science P0, research note, project/synthesis/overview update or push was produced; two scoped analytical sections remain P1 for user review.

## [2026-07-15] validation | continuous research-learning upgrade Phase 4

- Tightened research-note evidence/promotion consistency checks and validated ordinary-query exclusion in workflow/Skill contracts; nine tests and Wiki lint pass.
- Retained the single QMD collection; no real note, QMD refresh, science-page change or push was introduced in Phase 4.

## [2026-07-15] architecture | continuous research-learning upgrade Phase 5

- Closed the validated architecture release locally at `ready-for-push`, refreshed the unchanged single QMD collection after the pilot, and recorded remaining P1/deferred operational checks.
- No research note, project/synthesis/overview rewrite, merge or push was produced.

## [2026-07-15] review | continuous research-learning pilot sources

- User accepted both pilot Analytical Reconstruction sections; restored their source pages to `human-reviewed` and converted the reviewed reasoning to compact evidence-separated tables.
- Removed duplicated Personal Notes reasoning and clarified that review finalization may create local commits but push always requires explicit authorization; lint/tests and incremental QMD refresh pass, with no merge or push.

## [2026-07-15] release-cleanup | Continuous Research-Learning v1 Gate 2A

- Gate 1 identified push-authorization, overview-trigger, and on-touch migration blockers; Gate 2A applies the minimal framework cleanup, current-system wording, release index, and workflow contract tests.
- The planned local `Prepare Continuous Research-Learning v1 release` commit stays on the implementation branch; no merge, tag, or push is performed.

## [2026-07-15] release | Continuous Research-Learning v1 Gate 2B

- External final review passed with no science/framework P0; fast-forward merge, annotated tag, and push were explicitly authorized.
- Actual publication result will be recorded by Git and the final report; no post-push status-only commit will be created.

## [2026-07-15] checkpoint | triaxial wobbling source batch

- Completed first ten main sources in order: Hamamoto 2002/2003, Frauendorf-Dönau 2014, Streck 2018, Chen 2019, Chen-Frauendorf 2022 plus associated publisher erratum, Jia 2022, Petrache 2016, Chakraborty 2023 canonical-key metadata update, and Mullins 1993.
- Current step: batch-level wobbling REFLECT before Ye 2024, Kumar 2025 and Clark 2000.
- New claims remain `needs_review: true`; no raw PDF, `.bib` or unrelated framework file was staged or modified. `git diff --check` is clean.
- Next continuation: add minimum theory-lineage/transfer-boundary reflection to existing wobbling project/synthesis, then continue Ye 2024.
## [2026-07-15] checkpoint | triaxial wobbling source batch (final three reviews)
- Completed Ye 2024, Kumar 2025 and Clark 2000 review/background source notes after the first-ten-paper wobbling REFLECT; no separate source page was created for the Chen publisher erratum.
- Updated index, overview, minimal MR/AMR/shears/band-termination/TAC source links, and Active handoff. New claims remain pending human review.
- Checks so far: `git diff --check` clean; wiki lint 0 errors / 24 warnings / 129 info. QMD refresh and WIP commit remain.

## [2026-07-15] checkpoint | triaxial wobbling source batch WIP
- Created local WIP with message `WIP ingest: triaxial wobbling source batch for user review`; no push.
- Post-commit protected-path check is clean; only user `raw/zotero/wiki-inbox.bib` remains uncommitted. Review queue remains open for new source claims and wobbling REFLECT notes.

## [2026-07-16] checkpoint | Chakraborty 2023 source-framework migration

- Added current-framework `Analytical Reconstruction`, `Project Relation`, historical review record, Human Review Triage and `Review Status` sections to the already reviewed C23 source.
- Preserved `C23-1..C23-7` and `needs_review: false`; this is an on-touch format migration, not a new scientific review round. Protected user BibTeX remains unstaged.

## [2026-07-16] review finalization | triaxial wobbling source batch

- User reviewed Petrache 2016, Chakraborty 2023 and Mullins 1993; corrected PE16 two-run target assemblies and MU93 DOI/pagination, then cleared only the reviewed experimental claims.
- Operationally closed the batch. Ten theory/review sources and WOB-REFL/WOB-PROJ-REF claims remain unreviewed with `review deferred until use`; final amend/push was explicitly authorized, with Git as the publication record.

## [2026-07-16] framework | Continuous Research-Learning v1 refinement

- Added compact Knowledge Impact decisions, typed major knowledge relations and natural-theme-stage batch REFLECT rules without changing science content or review/evidence boundaries.

## [2026-07-16] framework | source learning wording polish

- Removed duplicate persistence wording, made typed-relation examples single-choice, and limited thematic batch REFLECT to multi-source ingest tasks.

## [2026-07-16] checkpoint | experimental wobbling evidence batch

- Duplicate/PDF-title/DOI/BibTeX precheck passed for 15 ordered sources; all were ingested with calibrated claim strength and locator-level experimental criteria.
- Added 15 source notes, 13 nucleus pages, `163Lu` TSD3, and a cross-mass evidence-strength synthesis; updated wobbling/chirality projects and overview.
- All new claims remain `needs_review: true`; Guo 2024 Supplemental Material is missing, no raw/BibTeX file was modified, and no push is authorized.

## [2026-07-16] checkpoint | experimental wobbling source-template alignment

- Realigned all 15 WIP source pages to the current deep-reading template and persisted source-local P0/P1 triage without changing existing Key Results or review state.
- Added the six-part Analytical Reconstruction and event-driven Human Review Notes/Record rules; the current WIP remains unpushed for user review.

## [2026-07-25] review | experimental wobbling evidence sources

- User completed a rough page-level review of all 15 sources and accepted the current calibrated wording and explicit limitations without correction.
- Marked the source pages `human-reviewed` while retaining claim-level and Analytical Reconstruction review markers for future strict paper use; authorized final amend/push.

## [2026-07-26] setup | Nature Skills full update

- Fast-forwarded the external Nature Skills clone from `b98b53e` to `8d674eb` and synchronized all 19 top-level skills into the global Codex skills directory.
- Added `nature-paper-card` and `nature-shared`, pruned obsolete `_shared`, and verified every installed file against the clone by SHA-256. Optional dependencies and integrations were not installed.

## [2026-07-26] setup | Nature Skills non-API runtime

- Installed and verified the downloader, patent-document and Playwright dependencies; pinned a compatible `pdfplumber 0.11.4` / `Pillow 10.4.0` pair and installed Playwright Chromium.
- Registered the global `academic-search` MCP through `uv`, verified no-key PubMed/CrossRef access, and stored the contact and institutional settings only in local user configuration. API-key providers remain deliberately unconfigured.

## [2026-07-26] setup | Wiki-only L3 boundary staged

- Wrote the system-enforced `wiki_l3` permission profile and migrated the user configuration away from legacy `sandbox_mode`; all runtime/cache paths now target Wiki-local `tmp/` locations. The settings require a complete Codex restart and runtime acceptance tests before L3 is considered active.
- Added the Nature-first acquisition route, Agent-managed `raw/papers/gpt/` and `raw/zotero/gpt.bib` entry points, sanitized acquisition-manifest contract, and explicit protection for `raw/zotero/wiki-inbox.bib`. No scientific knowledge page or QMD index was changed.

## [2026-07-26] correction | L3 boundary changed from machine-wide to Wiki-scoped

- Removed the Windows system `requirements.toml` so other Codex projects are no longer forced read-only; restored user defaults to `:workspace + on-request` and removed global Wiki TEMP/cache redirects.
- Added a trusted project-level `wiki_l3 + never` configuration for `E:\imp\wiki`, including Wiki-local runtime paths, public/local network access and self-protection for project config. Wiki tasks prohibit Computer Use and external state changes; restart acceptance remains pending.

## [2026-07-26] correction | Wiki escalation reserved for explicit user approval

- Replaced Wiki `approval_policy = never` with `on-request` and fixed `approvals_reviewer = user`, so external writes remain denied by default but a specifically described operation may proceed after explicit user approval; Codex and automatic reviewers cannot self-approve.

## [2026-07-26] correction | Wiki escalation requires a three-step handshake

- Tightened temporary external writes to user-initiated requests only: Codex must restate the exact path, action and impact, then receive a subsequent explicit user approval before issuing the system permission request. Initial instructions, Codex initiative and automatic review are insufficient.

## [2026-07-26] acceptance | Wiki-scoped L3 first restart blocked

- The repaired project config loads and Wiki CRUD, root `.codex` protection, Wiki-local runtime paths, external program execution and public command-line network access pass.
- L3 remains closed because nested `.codex` is writable, `.git` staging is denied, the effective reviewer is still `auto_review`, and Academic Search MCP tools are not exposed. Downloader and escalation tests were not run; protected user BibTeX remained unchanged.

## [2026-07-26] correction | strict nested-config and Git profile applied

- With explicit user approval, added exact Wiki `.git` write access and deny-only arbitrary nested `.codex` rules while retaining root `.codex` read access. The user accepted that nested `.codex` becomes unreadable as well as unwritable and reported disabling Auto-review.
- Codex 0.143 strict configuration parsing passed. Runtime, reviewer and MCP validation require a fresh task; no download, escalation, commit or push was performed.

## [2026-07-26] acceptance | Wiki-scoped L3 third round blocked

- Academic Search MCP, Wiki-local runtime/cache paths, user-level fallback policy and protected-BibTeX invariance passed, but the current task still reports `auto_review`, default shell setup refresh fails, and root/nested `.codex` patch writes unexpectedly succeed.
- Removed all three Wiki-local probe files, stopped before `.git`, downloader or external-write tests, and kept L3 closed pending a full runtime restart/reload.

## [2026-07-26] acceptance | Wiki-scoped L3 fourth round blocked

- Default Windows PowerShell startup recovered and root `.codex` patch writes are denied, but root `.codex` is hidden from Git and arbitrary nested `.codex` remains patch-writable.
- A no-side-effect escalation auto-executed without user review and an exact Wiki `.git` file write was denied. Removed the nested probe file, ran no later acceptance rows, and kept L3 closed.

## [2026-07-26] acceptance | Wiki-scoped L3 phase-one runtime limits

- After the user manually applied the first-phase profile and restarted into a fresh task, root `.codex` remained hidden, dynamically created nested `.codex` remained writable, exact `.git` writes remained denied, and a no-side-effect escalation was still auto-reviewed.
- Official Codex 0.143 behavior shows the original project-only hard-boundary combination is not currently enforceable as specified; all probes were removed, later acceptance rows stayed closed, and the task now awaits a user decision on a practical revised boundary.

## [2026-07-26] safeguard | Wiki file-edit guard prepared

- Added a tested, hash-pinned project-hook guard for supported writes to any `.codex` path and the user-owned Zotero Inbox, with ordinary Wiki edits and protected-path reads left available.
- L3 positioning is deferred. The guard remains inactive until the user manually installs and trusts `.codex/hooks.json` in a fresh task; no protected file was modified or staged. The current runtime denied `.git/index.lock` even after escalation, so the existing WIP could not be amended.

## [2026-07-27] correction | Wiki no-escalation boundary and orphan ACL recovery

- Replaced the conflicting project hook design with `wiki_l3 + approval_policy=never`; removed the hook/guard artifacts and synchronized governance so Wiki tools can write inside the repository while external writes cannot request escalation.
- The user safely removed six orphaned DENY ACEs from `.codex`; restart verification passed there. Acceptance then found six stale capability-SID DENY ACEs on each of `.agents` and `.git`; `.agents` write failed, later probes stopped, and no commit or push was performed.

## [2026-07-27] acceptance | Wiki internal boundary and new external writes pass

- After the user removed orphan DENY ACEs from `.agents` and `.git`, all three special paths passed restart ACL checks, Wiki CRUD, Node writes and Git index write/unstage; all file probes were removed.
- PowerShell and Node external-file creation were directly denied, state JSON and new sandbox logs were clean, and Wiki lint passed with 0 errors. Existing-file external mutation and an ordinary-project runtime control remain before final amend; no push was performed.

## [2026-07-27] acceptance | Wiki external existing-file mutation denied

- The user-created external probe retained SHA-256 `7FAF13C2EA0CE01C529BB934595B5D8C14955FD43326D32B5B3D703ACC3FDD56`; overwrite and rename were denied, delete was rejected before command launch, and no alternate target appeared.
- The first ordinary-project control was invalid because it still ran at `E:\imp\wiki` with `wiki_l3`. A genuinely independent non-Wiki task remains before final amend; no push was performed.

## [2026-07-27] acceptance | Ordinary-project isolation control completed

- A fresh task rooted at `C:\Users\22721\AppData\Local\Temp\codex-wiki-profile-control` had no Wiki hook or `wiki_l3` environment value and completed local create/read/delete without touching the Wiki, confirming project-profile isolation.
- The host reported reviewer state `auto_review` despite the user config selecting `approvals_reviewer=user`; this remains a recorded P1 unrelated to Wiki profile leakage. Exact temporary-artifact cleanup and final amend remain; no push was performed.

## [2026-07-27] finalization | Wiki-scoped L3 filesystem boundary accepted

- Removed all disposable probes and ACL backups after Wiki-internal CRUD/Git, external mutation denial, sandbox state/log and independent ordinary-project controls passed; the project hook design remains removed and `approval_policy=never` is canonical for Wiki sessions.
- Finalized the existing WIP as `Finalize Wiki-scoped L3 boundary and literature ingress`; the protected user BibTeX remains unstaged, L3 scientific autonomy remains deferred, and no push was authorized.

## [2026-07-27] architecture | autonomous L2, L3 and manual-L4 governance

- Consolidated L0-L4, P0/P1 state, dynamic L3 escalation, the manual L4 data gate and weekly self-test lifecycle into one canonical workflow; AGENTS, query, ingest, reflect, Skill, guide and checklist retain only short routing.
- Reverted the stopped draft's unauthorized PLAN addition, duplicate memory text and unproven global template expansion. Governance lint passes; the user-managed Zotero Inbox remains protected and unstaged.

## [2026-07-27] ingest | Alwaleedi 2013 `131Ce` thesis

- Deep-read the 97-page thesis in structure-grounded fallback mode, created source/nucleus/experiment pages and a 16-section Paper Card, and committed the ingest as `19a3495`; the Paper Card auditor passed with one expected no-bundle warning.
- Preserved the Table 5.1 Band 2 parity inconsistency and `δ=0` ratio assumption as review boundaries; the user-managed Zotero Inbox was not staged.

## [2026-07-27] L3 milestone | `131Ce/133Ce` collective-mode discrimination

- Completed an evidence/anti-evidence matrix and provisional research prospectus: configuration/signature coupling plus a γ-soft or spin-evolving non-axial core is preferred for `131Ce`; wobbling is unsupported by current interband E2 evidence, while `133Ce` chirality/shape coexistence remain model-assisted candidates.
- Built local evidence branch `codex/131ce-l3-evidence-pilot@4f1e9fb`; fetch/push failed because GitHub network/credentials were unavailable. L4 is a candidate only and is safe-suspended pending explicit user data confirmation and manual start.

## [2026-07-27] L4 milestone | `131Ce` thesis-only quantitative baseline

- Built a seven-band crosswalk and recomputed 35 table-intensity proxy ratios across `δ=0, ±0.1, ..., ±0.5`; three formula tests pass. Ten proxies cannot be reconciled with Figure 5.5 because its gated branching inputs are not tabulated, so ratio-based configuration support is downgraded in independent weight.
- Verified the 2016 lifetime DOI and metadata, but lawful full text remains blocked by closed OA and Springer identity access. Science-only branch `09c12ac` is locally ready; fresh fetch and direct main push failed with `SEC_E_NO_CREDENTIALS`. No global credential, permission or raw user-data change was made.

## [2026-07-28] L4 milestone | `131Ce` lifetime-informed update and v2 audit

- Deep-read and visually verified Singh 2016, Li 2004 and Petrache 1998; created source pages, audited Paper Cards and a reproducible lifetime package with six passing tests. Independent lineages are preserved, the HD band stays separate, and Li's reused rows are not double-counted.
- Singh finite points give `Q_t=2.579±0.099 eb` and slope `−0.030±0.047 eb/ℏ`, so the apparent decrease is not significant in this subset. γ-soft/core response gains bounded support; shape coexistence becomes a nuclear-level candidate, while chirality/wobbling do not upgrade.
- Compressed duplicate v2 guidance and recorded four weekly-self-test dry runs. Science-only direct-main push remains authentication-blocked after a successful fetch; no global credential, permission, raw PDF or user BibTeX mutation occurred.

## [2026-07-28] review | Li 2004 lifetime P0 accepted and v2 finalization authorized

- The user accepted the visual transcription for LI04-1–4 while keeping LI04-5 and the source page unreviewed; Li 2004 and Singh 2016 current results remain independent experiments, but Singh's copied Li rows are dependency-only and are not counted again.
- Continuous Research-Learning v2 local finalization is authorized. Science-only direct-main push still exits at authentication after a successful fetch, so remote main/tag publication remains blocked without changing credentials or force pushing.

## [2026-07-28] release-candidate | 硅基研究生 V2 local topology rebuilt

- Rebuilt `codex/continuous-research-learning-v2-release` from the audited science-only lineage, then replayed the permission boundary, canonical autonomy governance and finalized lifetime-informed L4 changes without duplicating thesis/L3 science commits.
- README, PLAN, guides, memory, architecture index, overview and CI paths were aligned to v2. The branch remains a local candidate because direct-main authentication failed; no remote main update or tag is claimed.
- Canonical QMD update/embed/status completed with 249 documents and 1872 vectors; the collection is bound to the primary worktree, so the release-only overview revision is indexed after main alignment rather than through the isolated worktree.
- Codex bundled Git 2.53 was retried with command-scoped `GIT_EXEC_PATH` pointed to its actual `mingw64\bin` helpers. Public remote reads succeeded, but non-force push dry-run exited 128 without a usable authentication diagnostic; `origin/main` remained `3d7c22a`, and no tag was created.

## [2026-07-28] release | 硅基研究生 V2 main publication and push repair

- Diagnosed the remaining push failure as a nested Git-to-PowerShell credential-helper hang after GitHub's Basic challenge. A repo-local DPAPI wrapper now supplies the existing fine-grained PAT only as an exact-URL, process-scoped Authorization header to Codex bundled Git 2.53; no plaintext credential, global Git setting, system Git 2.55 or force push was used.
- Non-force fast-forward publication moved `origin/main` from `3d7c22a` to `e3aeebd`; GitHub Wiki lint run `30373076310` completed successfully. The protected Zotero Inbox and raw PDFs remained unstaged and unmodified.

## [2026-07-28] maintenance | Wiki-local authenticated push generalized

- Replaced the release-only PowerShell wrapper path with a repository-local native AskPass backed by the existing DPAPI-protected credential; ordinary Git now performs authentication without printing or embedding the token.
- Codex bundled Git 2.53 and system Git 2.55 both passed exact-refspec branch dry-runs and no-op `main` pushes. Git version is no longer treated as a permission boundary; repository scope, preflight, non-force semantics and explicit push authorization remain mandatory.
- No global/system Git setting or other project was changed. Failed and legacy helper prototypes were moved to ignored `tmp/git-diagnostic/`; no remote probe ref was created.

## [2026-07-29] publication | Wiki-local authenticated push generalization

- After fresh fetch, repository-scope, secret/raw, ancestry, lint and system-test checks, system Git 2.55 published `dee0b36` to `origin/main` by exact-refspec non-force fast-forward.
- Local HEAD, the tracking ref and remote `main` agreed after the push. The protected Zotero Inbox remained unstaged; no global/system credential, SSL, PATH, permission or other-project setting changed.

## [2026-08-04] maintenance | Wiki automation protected-path permission matrix

- Upgraded the Wiki-local automation preflight to schema 2: root and `.git` use real write probes, while `.codex/config.toml` and the repository Skill are read-only sentinels; protected-directory DENY remains diagnostic.
- A real protected-DENY run exited `0`, 15 system tests passed, Wiki lint had 0 errors, and probe cleanup succeeded. The host rejected the project-config patch, so automation and `131Ce` remain paused pending a Desktop-exited Wiki-local config edit and cold-start validation; no ACL, raw, global setting or remote was changed.

## [2026-08-04] acceptance | Wiki automation permission matrix cold start

- After the `unelevated` project override was made inactive, two consecutive schema-2 preflights passed without ACL cleanup: root and `.git` were writable, both protected sentinels were readable, and no probe remained.
- The user retained `.codex`/`.agents` as `write` in `wiki_l3`; automation alone is forbidden to exercise that grant. Tests, lint and diff checks passed, while automation, `131Ce`, raw staging and push remained paused.

## [2026-08-04] correction | Scheduled profile marker false negative

- A controlled `Run now` safe-stopped because the scheduled runner omitted the diagnostic `CODEX_PERMISSION_PROFILE` marker; startup, Git, raw and science work did not run, and the same automation was paused.
- Schema 2 now attests the project config and actual capabilities, treats a missing marker as a warning, and still blocks a non-empty mismatch. A real missing-marker simulation passed without ACL, global, raw or remote changes.
- The same `ID=wiki` prompt was updated through the automation function with the corrected semantics and kept `PAUSED`; no duplicate or controlled run was created.

## [2026-08-04] weekly self-test | `131Ce` lifetime and γ-soft boundary

- Schema-2 permission preflight passed with the expected missing-marker warning; protected BibTeX, root/`.git` probes and protected reads remained safe.
- Corrected the `131Ce` evidence chain so lifetime/`Q_t` directly constrains E2 collectivity/core response, while γ-softness remains TRS/model-assisted; the author's `3→2.5 eb` visual summary is separated from the Wiki's `0.64σ` null trend.
- Added a reviewable P0/P1 report and new pending GSD-PROJ-8/GSD-SYN-9 without overwriting prior human-review history. Tests and lint passed; no push occurred.

## [2026-08-04] review | `131Ce` lifetime and γ-soft boundary accepted

- The user completed the targeted P1 review without corrections and authorized push.
- GSD-PROJ-8/GSD-SYN-9 are accepted; the Singh source's unrelated claim-level review states remain unchanged.
- Finalization will amend the existing scientific WIP, replay the dependent governance final and use exact-refspec non-force push after H3.

## [2026-08-04] governance | WIP post-commit reconciliation

- Corrected the weekly WIP's stale pre-commit wording and amended the same scientific WIP from `6beee7d` to `4dcb9b1` without changing science.
- Added a mandatory no-push-inclusive H3 reconciliation: repository state uses branch + subject, self-hashes are forbidden, and any status correction amends the same commit rather than creating a second WIP/status commit.
- The governance work remained on a dependent local branch until the reviewed scientific lineage was finalized; protected raw, automation, ACLs and remote state were not changed.

## [2026-08-04] integration | reviewed weekly lineage assembled

- Integrated the accepted `131Ce` scientific final with the dependent WIP-reconciliation governance final; no additional scientific claim state changed.
- Used an ignored Wiki-internal temporary worktree so the protected user BibTeX remained untouched and unstaged in the primary worktree.
- The integrated tests passed; final primary-worktree lint, H3 and the user-authorized exact-refspec push remain the publication gate.

## [2026-08-04] safe suspend | reviewed weekly lineage push

- Local H3, fresh fetch and remote ancestry passed for the integrated reviewed lineage.
- System and bundled Git both failed the exact-refspec dry-run because the protected repo-local AskPass could not be spawned in the current runtime; no push occurred.
- Preserved the integrated local final and protected BibTeX; resume in a fresh Wiki runtime without changing ACLs or credentials.

## [2026-08-05] safe suspend | reviewed weekly lineage fetch gate

- Current H3 stopped at fresh fetch because `.git/FETCH_HEAD` was denied after the guardian restored the known explicit DENY rules; no status transaction, dry-run, or push was performed.
- Preserved the integrated local final and protected BibTeX; resolve the Desktop `.git` write lifecycle outside Codex before retrying.

## [2026-08-05] publication | reviewed weekly lineage

- After the user precisely removed the known guardian DENY rules outside Codex, schema-2 root/`.git` probes, fresh fetch, ancestry, tests, lint and the complete H3 passed in the Wiki runtime.
- Published the reviewed `131Ce` scientific final and dependent WIP-reconciliation governance final to `origin/main` by exact-refspec non-force fast-forward; protected BibTeX remained unstaged and hash-matched.

## [2026-08-07] safe suspend | counter-evidence workflow push

- Created local final `Strengthen counter-evidence research workflows` for the 116Cs-derived method/governance reinforcement; Wiki lint passed with 0 errors.
- Two fresh-fetch attempts failed because TCP connectivity to `github.com:443` was unavailable, so exact-refspec dry-run and push were not attempted; protected `.gitignore` and `raw/zotero/wiki-inbox.bib` remained unstaged.

## [2026-08-10] weekly self-test | `131Ce` Band 5 configuration continuity

- Direct page rendering confirmed that Alwaleedi Table 5.3 prints `f⊗AE → e⊗AEFG`; this is not OCR noise.
- Table 5.2 signature labels and the Band 5 `eAE/fAE + FG crossing` discussion support `f⊗AEFG` only as a probable-typo working reconstruction pending user review and independent confirmation; no push occurred.

## [2026-08-11] review | `131Ce` Band 5 Table 5.3 mapping

- The user retained the literal `e⊗AE → e⊗AEFG` and `f⊗AE → e⊗AEFG` mappings and rejected the Agent's `f⊗AEFG` reconstruction.
- AW13-12/AW13-13 and directly propagated nucleus/project/report wording are the only scientific review scope; unrelated claims remain unchanged.
- The weekly WIP was amended to local final `Finalize weekly self-test 2026-08-10: 131Ce Band 5 configuration continuity` as commit 1 of the two-commit plan. Guo 2024's current local PDF identity was reverified and its source hash metadata synchronized without modifying raw evidence or scientific claims.
- Publication remains deferred. Corpus write-entry is safe-suspended until the user-managed Zotero export removes the two duplicate alias keys.

## [2026-08-11] ingest | Petrache 1996 `134Pr` rotational bands

- The user re-exported the protected BibTeX; both deprecated duplicate keys disappeared while the canonical Guo/Frauendorf keys remained unique.
- Deep-read and visually checked the 21-page Petrache 1996 paper; created the `134Pr` source/nucleus and two experiment entries, and added a bounded historical-precursor relation to the nuclear-chirality project.
- Preserved the paper's explicit unresolved Band 1/Band 2 alternatives and did not back-project nuclear chirality into the 1996 author interpretation. The corpus remains one rolling local WIP and is not pushed.

## [2026-08-11] ingest | Petrache 1998 `134,135Nd/131Ce` HD-band lifetimes

- Re-read and visually checked all five pages; expanded the old `131Ce`-only card into the full shared-systematics DSAM comparison of five bands in three nuclei.
- Added `134Nd` and the common GASP+ISIS experiment entry, updated `135Nd/131Ce`, and corrected the old CHFB label to the source's paired cranked-Strutinsky calculation.
- Preserved the `134Nd` Band 3 fit ambiguity, the `135Nd Q_sf` Table/prose conflict and the absence of any band crosswalk to later chiral partners. The paper is deformation control context, not direct chirality evidence.

## [2026-08-11] ingest | Klemme 1999 `134Nd` and neighbor lifetimes

- Deep-read and visually checked all ten pages; captured 12 `134Nd` and 12 neighboring-state coincidence-RDDS lifetimes, the DDCM diagnostic/error chain and the g.s.b./γ/S1/S2 strength comparison.
- Created the GASP-II plunger experiment and reusable RDDS/DDCM method pages; crosswalked the `135Nd [514]9/2` low-spin sequence to later D1 as high-confidence provisional.
- Kept `134Pr 9+` level-only and separated measured lifetimes/`Q_t` from O(6), TRS, rigid-triaxial and ASYR interpretations. No direct chirality evidence was assigned.

## [2026-08-11] ingest | Hecht 2001 `136Pm/138Eu` chiral-twin candidates

- Deep-read and visually checked all four pages, including both partial level schemes, the `138Eu` spectrum, `136Pm` polarization asymmetry, experimental ratios and 3D TAC table.
- Created two nucleus, two experiment and two stable candidate-pair entries; connected the direct candidate evidence to the nuclear-chirality project without promoting it to model-independent proof.
- Preserved the stronger-title versus “good candidates” conclusion, systematics-dependent bandhead spins/common-configuration inference, and the boundary that 3D TAC cannot calculate the observed quantum doublet mixing. The user authorized continuation through all 23 corpus targets; no remote action occurred.

## [2026-08-11] ingest | Starosta 2001 N=75 chiral vibrations

- Deep-read and visually checked all four pages; added `130Cs/132La` experiments, nuclei and candidate pairs, plus a retrospective `134Pr` Bands 1/2 crosswalk without rewriting Petrache 1996.
- Preserved the charge-inconsistent printed `116Sn(24Mg,4n)136Pm` channel, the detector-description conflict and the non-independent Starosta/Hecht evidence lineage instead of silently normalizing metadata or double-counting support.
- Completed a project-level 1996-2001 N=75 thematic REFLECT: linked bands plus electromagnetic assignments and aplanar TAC are the reusable advance, while “chiral vibration” remains an uncalculated dynamical interpretation of band displacement. No remote action occurred.

## [2026-08-11] ingest | Hecht 2003 `140Eu` chirality/shape coexistence

- Deep-read and visually checked all 14 pages; created the `140Eu` source/nucleus/YRAST experiment and stable Bands 1/2 and Bands 3/4 candidate-pair pages.
- Preserved the title question mark and the source's unresolved chirality-versus-`γ≈±25°` shape-coexistence alternatives; common configurations, missing signature partners and the Band-5 20.5-keV link remain explicitly indirect/unobserved.
- Recorded the Compton-asymmetry convention opposite to Hecht 2001 and the lifetime/absolute-strength discriminator. Wiki lint passed with zero errors; no remote action occurred.

## [2026-08-11] ingest | Li 2004 `131Ce` lifetimes

- Re-read and visually checked all three pages; expanded the existing source while retaining the user's accepted LI04-1–4 Table-1 transcriptions and their claim-level review state.
- Added the CIAE HI-13 experiment and separate negative-/positive-parity lifetime reference pages; preserved finite lifetimes, `19/2−` lower limit and feeding-uncorrected `31/2−/25/2+` effective upper limits.
- Classified the source as normal-deformed collectivity/shape-driving control rather than a same-parity partner or chirality measurement. Wiki lint passed with zero errors; no remote action occurred.

## [2026-08-11] ingest | Timár 2007 `105Ag` chiral search

- Deep-read and visually checked all 11 pages; created the `105Ag` source/nucleus/Stony-Brook experiment, corrected Band-E reference and D/G candidate-pair pages.
- Separated the intended Band-E partner null at ≈0.1 population sensitivity from the distinct natural-parity D/G candidate with ≈70-keV separation, smooth `S(I)` and similar staggered branching ratios.
- Preserved corrected `+2ℏ` Band-E spins, absent dedicated D/G TAC/PRM, tentative high-spin assignments, configuration-mixing alternative and assumed-`Q0` octupole exclusion. Wiki lint passed with zero errors; no remote action occurred.

## [2026-08-11] ingest | Suzuki 2008 `103,104Rh` lifetimes

- Deep-read and visually checked all five pages; created the `103,104Rh` source/nuclei, inverse-kinematics Gammasphere-plunger experiment and two stable candidate-pair pages, and extended the RDDS method.
- Captured the one-member lifetimes/absolute strengths and the result that weak ratio staggering is driven by `B(E2)` while `B(M1)` decreases with spin.
- Preserved the missing partner-band lifetimes, pure-M1/prior-branching dependencies, recoupling-versus-shape ambiguity and the paper's explicit future decision rule. Wiki lint passed with zero errors; no remote action occurred.

## [2026-08-11] ingest | Luo 2009 even-even Ru chirality evolution

- Deep-read and visually checked all six pages; created the `108,110,112Ru` source/nuclei, `252Cf` Gammasphere experiment and three stable composite-structure pages, and extended the chiral-vibration concept/project.
- Kept `108Ru` as an unresolved γ-soft control and `110,112Ru` as soft zero-/one-phonon candidates with similar `S(I)` and branching-derived ratios.
- Preserved pure-M1 assumptions, planar `φ=0°` TAC/no static chirality, the unobserved calculated shape change and the `112Ru` RPA-breakdown/large-amplitude requirement. Wiki lint passed with zero errors; no remote action occurred.

## [2026-08-11] ingest | Wang 2013 `104Ag` high-spin structure

- Deep-read and visually checked all nine pages; created the `104Ag` source/nucleus/CIAE experiment and separate A/B candidate, D/E electric-rotation and F magnetic-rotation pages.
- Preserved the revised A-F scheme, A/B fingerprint chain and coexistence of single-particle, electric-quadrupole and magnetic rotation.
- Kept the local “true partners” phrase subordinate to the candidate conclusion, and recorded missing lifetime/polarization/dedicated model, provisional `N=57` border and systematics-dependent configurations. Wiki lint passed with zero errors; no remote action occurred.

## [2026-08-11] ingest | Kuti 2014 same-configuration MχD in `103Rh`

- Deep-read and visually checked all five pages; created the source/LBNL experiment and two negative-parity pair pages, and updated `103Rh`, its positive-pair page, the MχD concept and chirality project.
- Reserved the same-configuration MχD claim for negative Bands 3/4 and 6/5; kept Suzuki's positive-pair lifetime member separate because the band-number crosswalk is not explicit.
- Preserved the parity assumption, nonabsolute-ratio boundary, deferred TAC detail, ≈200-keV PRM energy excess and missed Bands 5/6 alignment jump. Wiki lint passed with zero errors; no remote action occurred.

## [2026-08-11] ingest | Singh 2016 `131Ce/133Pr` lifetime control

- Re-read and visually checked all eleven pages; preserved the prior reviewed `131Ce` claims and completed the omitted `133Pr` half with a nucleus/band, two IUAC experiment pages and a DSAM method page.
- Retained the independent Li/Singh lineage and `131Ce` 0.64σ null trend; persisted exact `133Pr` lifetimes/limits and the positive-parity feeding constraint.
- Classified the high-Ω neutron versus low-Ω proton comparison as TRS-assisted shape polarization, not direct chirality; kept singles-only statistics, roughly 1-ns side feeding and pre-crossing validity explicit. Wiki lint passed with zero errors; no remote action occurred.

## [2026-08-11] ingest | Petrache 2018 even-even chirality in `136Nd`

- Deep-read and visually checked the repository cover plus all six journal pages; created the source/JUROGAM-II experiment and five stable pair identities, and updated `136Nd`, MχD and the chirality project.
- Separated the D5/D5-chiral partner-ratio evidence from four weak candidates without partner ratios; retained D3 as the only explicit 3D planar-to-aplanar TAC example.
- Preserved deferred angular-correlation details, unobserved weak dipoles, model-space configuration inference, backbend/ratio failures and undocumented MQ-PRM summary wording. Wiki lint passed with zero errors; no remote action occurred.

## [2026-08-11] ingest | Xiong-Wang 2019 chiral-doublet data tables

- Deep-read and visually checked all 33 pages, including the full 47-nucleus level/ratio table and the smaller absolute-`B(M1)`/`B(E2)` table; created a census source and updated MχD/project/index boundaries.
- Retained 59 reported doublets, 47 nuclei and eight reported/suggested MχD nuclei as a historical literature census rather than confirmations, and persisted the table-label/precision conventions.
- Preserved heterogeneous ratio provenance, sparse lifetime-based strengths, named crossings/backbends and other fingerprint exceptions; no nucleus/band/experiment pages were mechanically created from the secondary compilation. Wiki lint passed with zero errors; no remote action occurred.

## [2026-08-11] ingest | Guo 2020 pseudospin-chiral quartet in `131Ba`

- Deep-read and visually checked all six pages; created the source, a pseudospin-chiral concept, the D3-D6 positive four-band page and D7/D8 negative-pair page, and updated `131Ba`, GALILEO, concepts, project and index.
- Preserved D3-D6 as one stable experimental manifold because energies/links do not uniquely select two pairs; separated the RAT-PRM pseudospin/chiral decomposition from direct observables.
- Recorded direct E1 octupole-correlation evidence without stable-deformation promotion, plus assumed weak-line δ, no lifetimes, tentative β3, D5 feeding mismatch and deferred angular-momentum geometry. Wiki lint passed with zero errors after schema/index repair; no remote action occurred.

## [2026-08-11] ingest | Wang 2020 review of multiple chiral doublets

- Deep-read and visually checked all nine pages; created the review source and updated the MχD, chirality-parity-quartet, pseudospin-chiral-quartet, project and index pages.
- Preserved the observed-candidate census and predicted-minimum map as secondary review products, and recorded the printed `136Nd` `(5n)` reaction as inconsistent with mass balance and the original `(4n)` experiment.
- Kept ideal `gamma=90°` PRM fingerprints, the approximate two-band interaction estimate and proposed chiral-wobbler/quartet extensions model-conditional or prospective. Wiki lint passed with zero errors; no remote action occurred.

## [2026-08-11] ingest | Musangu 2021 `104,106Mo` soft chiral-vibration candidates

- Deep-read and visually checked all sixteen PDF pages; created the source, two nuclei, two stable Bands-4/5 candidate pages and a Mo-specific shared-lineage Gammasphere analysis page.
- Separated observed close bands/angular correlations from extended-TPSM configuration, predicted connecting E2 strengths and `104Mo` component geometry; retained the nonabsolute-ratio/lifetime gaps.
- Preserved unobserved connecting links, `106Mo` upper-limit tension, fixed-deformation discrepancies, unpublished generalized-TPSM detail and the `gamma=100°` axis-order workaround. Wiki lint passed with zero errors; no remote action occurred.

## [2026-08-11] ingest | Peng-Chen 2022 `102-107Rh` chiral-rotation evolution

- Deep-read and visually checked all eight pages; created the theory source and lightweight `102/105/106/107Rh` pages, and updated `103/104Rh`, TAC/CDFT, static/chiral-vibration, moments, project and index.
- Preserved finite `103-107Rh` mean-field critical frequencies separately from the unconverged planar `102Rh >0.75-MeV` suggestion and recorded the `(gd)`-neutron component mechanism.
- Kept imported experimental data secondary, exposed no-pairing `102/104Rh` discrepancies, and retained the inability of mean-field TAC to calculate partner bands, tunnelling or splitting. Wiki lint passed with zero errors; no remote action occurred.

## [2026-08-11] ingest | Guo 2022 `192-200Tl` chiral/MχD screening

- Deep-read and visually checked all ten PDF pages; created the theory source and lightweight `192-200Tl` pages, and updated MχD, triaxial shape coexistence, CDFT, project and index.
- Preserved the `192-198Tl` favorable-minimum map and `199,200Tl` null controls as constrained-RMF results, not rotational doublets or handed geometries.
- Kept Fig.4 evidence secondary, `(fp)` unresolved, pairing omitted and `195Tl` five-quasiparticle states outside the model space. Wiki lint passed with zero errors; no remote action occurred.

## [2026-08-11] ingest | Xiao 2022 `74As` chirality and octupole correlations

- Deep-read and visually checked all nine PDF pages; created the source, `74As`, two band pages and the iThemba-AFRODITE experiment, and updated chirality/octupole/TPRM concepts, project and index.
- Preserved Bands 1/2 as a five-link, `≈400-keV`, fitted-TPRM candidate with total-I aplanarity but neutron three-axis mixing; no lifetimes or absolute strengths were measured.
- Separated the three Band-3→1 E1 links from the additional low-lying E1 and retained the `1ℏ` spin revision, `≈11.8-keV` gap, tentative Band-3 orbit and correlation-versus-stable-deformation boundary. Wiki lint passed with zero errors; no remote action occurred.

## [2026-08-11] ingest | Wang 2023 experimental nuclear-chirality studies in China

- Deep-read and visually checked all 17 PDF pages; created a topical-review source and updated DSAM, nuclear chirality, octupole correlation, the corpus project and index.
- Kept the 23-nucleus/three-region census as a secondary original-source router and preserved the `106Ag` absolute-strength counterexample, sparse partner-lifetime coverage and correlated-DSAM-uncertainty warning.
- Quarantined the charge-inconsistent `82Ge` targets printed/extracted for the `82Br/81Kr` rows and retained the Br octupole/chirality trend as a reflection-symmetric-model, cross-source hypothesis rather than causal fact. Wiki lint passed with zero errors; no remote action occurred.

## [2026-08-11] ingest | Bark 2024 iThemba LABS nuclear-chirality review and corpus closure

- Deep-read and visually checked all 32 PDF pages; created the review source and lightweight secondary `106Ag` page, and updated `193,194,198Tl`, chirality/MχD/TPRM/DSAM/polarization pages, project, index and overview.
- Persisted the restricted-versus-realistic QTR fingerprint boundary, `106Ag` two-/four-quasiparticle counterexample and `193,194Tl` three-observed/four-calculated pairing ambiguity; repeated `74As/78Br` evidence was not counted independently.
- Reconciled Wang 2023's charge-inconsistent `82Ge` rows to Bark's `82Se` at the related-review level, quarantined Bark Eq.(5)'s algebraic error, and completed a six-claim final thematic REFLECT. QMD refreshed to 357 documents/2390 vectors; lint passed with zero errors. All 23 target papers are ingested; no remote action occurred.

## [2026-08-11] governance-finalization | ordinary ingest self-review and publication boundary clarified

- User clarified that ordinary literature ingest is completed like a graduate student's own reading: the Agent performs full-text/locator/evidence-layer/P0-P1 self-audit and publishes without waiting for per-paper human review. Agent self-audit does not create Human Review history, promote `review_status`, or clear `needs_review`; claim/evidence statements are reviewed later when used in Q&A or research.
- The completed 23-paper nuclear-chirality rolling WIP has no unresolved hard P0 and was amended to current branch HEAD final `Ingest 23-paper nuclear chirality corpus`, preserving the Band-5 final as commit 1 and corpus final as commit 2 before exact-refspec publication preflight.

## [2026-08-11] governance | schema-2 push DENY hardening

- Added runtime token user/group SID reporting and SID-normalized token-matching versus nonmatching explicit DENY diagnostics; real root/`.git` probes and protected reads remain the only capability gate.
- Confirmed the current `.git` stale DENY entries are nonmatching and do not block schema-2 exit `0`; added a temporary ACL regression test and synchronized push/network/authentication failure routing without changing ACLs, project config, Skills, credentials or protected BibTeX.
- Governance final commit and non-force publication remain pending H2/H3 reconciliation.

## [2026-08-11] governance | schema-3 weekly automation state-drift repair

- Replaced the persistent `wiki-inbox.bib` hash gate with a per-run schema-3 baseline and same-run stability checks; independent Zotero updates now establish a fresh baseline. The two stale `.git` guardian DENY ACEs were removed by the user outside Codex and are being rechecked as diagnostics only.
- Bounded weekly self-test scope to at most two important active problems, with no fixed literature count, finite relevant batches, isotope/isotone comparison, deferred-issue recording and nonblocking L4 readiness reports. Governance finalization and non-force publication remain pending H2/H3.

## [2026-08-11] governance-finalization | automation replacement published

- Published the schema-3/run-local-baseline governance repair by exact-refspec non-force fast-forward; the main checkout retained only the protected user BibTeX modification, and the two known `.git` guardian DENY SIDs remained absent after H3.
- Rebuilt the Wiki Monday 19:20 Asia/Shanghai local cron as `wiki-replacement`, enabled it with the bounded two-problem/no-fixed-literature-count/L3-L4 readiness contract, and removed the stale `wiki` automation ID. No scientific content or raw evidence was changed.

## [2026-08-13] tooling | Nature Skills PowerShell update completed

- The WSL `bash scripts/update-codex-skills.sh` route failed before synchronization because the Windows checkout was CRLF and WSL parsed `set -o pipefail` incorrectly; no Wiki file was affected.
- The user then ran the PowerShell-compatible update: `C:\Users\22721\ai-skills\nature-skills` fast-forwarded from `8d674eb` to `d1fb103c635e63288c0f2174460276b1ab7582d8`, and `C:\Users\22721\.codex\skills` was synchronized with all 19 Nature directories.
- The install manifest records `d1fb103`; source/target content hashes match. The strict Robocopy check only reported target-side `__pycache__` directories under `nature-academic-search` and `nature-downloader`, which are runtime caches excluded from skill content. The user restarted Codex; API keys remain intentionally unconfigured, and Nature Skills remain subordinate to Wiki evidence rules.

## [2026-08-13] tooling | double-click Nature Skills updater implemented

- Added `system/scripts/update_nature_skills.cmd`, `system/scripts/update_nature_skills.ps1` and `system/scripts/README.md`; the CMD entry is the recommended user-facing update path.
- The PowerShell engine keeps the fixed upstream and existing install paths, performs fast-forward-only Git checks, discovers all top-level `SKILL.md` directories, blocks removals/reparse points/submodules/dangerous binaries and oversized files, stages and hashes before activation, preserves a previous backup, supports `-CheckOnly`/`-Rollback`/`-NoPull`, and leaves unrelated Codex skills untouched.
- Fixture tests passed for first install, read-only check, update, backup, rollback, skill-removal blocking, dangerous-file blocking and preservation of a non-Nature directory. The current environment's Defender command returned `0x80004005`; the updater reports this as a warning and continues structural/hash validation, while threat-like output remains a hard stop.

## [2026-08-14] tooling | Nature Skills updater Huorong safety gate

- Replaced the updater's Microsoft Defender scan/fallback with fixed-path Huorong `HipsMain.exe -s "<absolute staging path>"`, a 12-hour process wait, nonzero/launch/timeout fail-closed handling and explicit `Y/y` confirmation of the Huorong GUI's completed/zero-risk result. The terminal confirmation prompt itself waits for user input without a 12-hour countdown.
- Added post-confirmation whole-staging and per-skill SHA-256 checks before the existing `Move-Item` activation; rollback, cleanup and final verification remain unchanged. Updated `system/scripts/README.md`; no real update, Huorong scan, commit or push was performed.

## [2026-08-17] weekly-self-test | `131Ce` N=73 isotone discrimination

- Recovered Ding 2021's under-extracted N=73 `129Ba/131Ce/133Nd` `[404]7/2+` systematics and bounded it as contextual reuse of prior experiments rather than a new independent `131Ce` dataset.
- Compared the configuration-distinct `127Xe/129Ba` `h11/2` wobbling candidates, including delta/polarization coverage, contamination and legacy-data dependence; they establish mechanism feasibility but do not supply target-nucleus evidence.
- The `131Ce` hypothesis ranking is unchanged; the new source/project claims await focused human review, and no L4 research was started.

## [2026-08-18] tooling | Nature Skills update verified

- User completed the double-click Nature Skills update after closing the process that held `nature-academic-search\mcp-server`.
- Source and global Codex installation now match commit `44defbcce0b8534f9a0a4734f56c40e4f703bbf4`; the manifest records 20 skills, and read-only `-CheckOnly` returned `MATCH` for all 20.
- No Wiki scientific content or protected `raw/zotero/wiki-inbox.bib` was modified by the update; no commit or push was performed in this sync.

## [2026-08-19] tooling | Nature Skills updater maintenance

- Fixed Windows PowerShell 5.1 handling of normal Git fetch stderr, removed the `Get-FileHash` module auto-loading dependency by using .NET SHA-256, and added a fail-closed diagnostic for locked Nature Skills directories.
- The maintenance is limited to the updater and its usage records; no Nature Skills content, scientific Wiki content or protected BibTeX was changed.

## [2026-08-19] workflow | weekly self-test WIP published to main

- Preserved the original `955ddc9094ada187aa183b0c19427d3128cbbfac` WIP commit and connected it to `main` for traceability; the scientific review remains pending.
- The merge touched only the weekly self-test knowledge/output/queue records and system handoff/log updates; protected `raw/zotero/wiki-inbox.bib` remained untouched and unstaged.

## [2026-08-19] weekly-self-test | `131Ce` D21-8 locator and lineage audit

- Rechecked Ding 2021, `127Xe` 2020 and `129Ba` 2024 by direct PDF render; no scientific P0 or ranking change was found.
- Expanded D21-8 to Figs.4-6 and made the `129Ba/131Ce/133Nd` refs.46/47/48 experimental lineages explicit while retaining the original-full-text and evidence-independence limits.
- Reconciled the active queue/report with the already-published `main` history; focused scientific review and QMD refresh remain pending.

## [2026-08-20] governance | global weekly-learning scheduler repair

- Separated `weekly-learning`, `continuation-audit` and `maintenance`; added a global candidate pool, continuity/novelty slots, repository-local eight-cycle coverage history, two-cycle source cooldown and ISO-week tie-break rules.
- Reclassified the 2026-08-19 D21-8 run as continuation-only and added Selection audits to the four historical self-test reports; the next novelty slot must leave the current `131Ce`/Ding/`127Xe`/`129Ba` cluster unless a hard exception is recorded.

## [2026-08-24] weekly-self-test | `135Pr` mixing-ratio branch reassessment

- Selected a non-overlapping novelty slot and found Sensharma et al. 2026, which adds a new Gammasphere run plus a combined-data large-`|δ|` analysis for the disputed wobbling links.
- Reclassified the evidence state as two explicit, conflicting experimental analysis chains: the partially dependent 2026 angular-distribution result versus Lv 2022's independent small-branch `P-R_ac` result; no final wobbling verdict or L4 run was made.
- Controlled PDF downloads failed without producing a candidate PDF; acquisition status was recorded, no source/project page was changed, and the protected Zotero BibTeX remained outside task scope. The local WIP was not pushed because fresh fetch and its bounded network diagnostics could not reach `github.com:443`.

## [2026-08-31] weekly-self-test | `106Ag` dual-DSAM lineage conflict

- Selected a non-overlapping A≈100 novelty slot and identified Lieder 2014 and Rather 2014 as independent AFRODITE/INGA DSAM experiments rather than one experiment plus a vague alternative.
- Both chains reject the simple crossing-band chiral-pair reading, but their two-/four-quasiparticle versus same-deformation projected-configuration interpretations are not identical; only the falsification boundary is currently robust.
- Controlled local PDF fetches failed, so no source/project/nucleus page or BibTeX was changed; acquisition and review state were recorded for later dual-source ingest.

## [2026-09-01] publication | weekly self-tests finalized, AskPass blocked

- Amended the rolling weekly WIP to final `Finalize weekly self-tests through 2026-08-31` without recording a Human Review or changing scientific review state.
- After the user removed the stale `.git` DENY, schema-3, fresh fetch and ancestry passed; system and bundled Git both failed exact-refspec dry-run because the protected repo-local AskPass executable could not be spawned.
- No real push, credential change, schema-4 implementation or automation Run now was performed; protected `raw/zotero/wiki-inbox.bib` remained unstaged.

## [2026-09-02] ingest | 丁兵 2012 博士论文：127,128I 高自旋能级结构研究

- Deep-read and extracted all 7 chapters (100 pages) of Ding Bing's 2012 PhD thesis on `127,128I` in-beam gamma spectroscopy with CIAE HI-13 tandem ($^7\text{Li} + {}^{124}\text{Sn}$).
- Created source note `ding-2012-phd-thesis-127-128i-high-spin`, experiment page `ciae-hi13-127-128i-li7-28-32mev`, nuclei `127i` and `128i`, and 5 band pages (`127i-pi-h11-2-decoupled-band`, `127i-pi-g7-2-rotational-band`, `127i-pi-d5-2-band`, `128i-pi-g7-2-nu-h11-2-structure`, `128i-pi-h11-2-nu-h11-2-structure`).
- Recorded 11 structured claims covering $\pi h_{11/2}$ decoupled band extension to stable $^{127}\text{I}$, $\pi g_{7/2}/\pi d_{5/2}$ high-K oblate rotational reinterpretation via newly observed interband transitions, $15/2^+, 23/2^+$ 3qp single-particle/collective coexistence in a $\gamma$-soft/$\beta$-soft PES, and $^{128}\text{I}$ 2qp multiplets supported by NPA and empirical shell model. Synchronized `knowledge/index.md`.

## [2026-09-02] review-correction | 丁兵 2012 博士论文摄入优化

- User confirmed the experiment was performed at the University of Tsukuba, not CIAE; corrected the experiment page slug, facility, reaction-energy mapping and detector geometry.
- Rechecked key figures/tables and corrected ADO/DCO terminology, 127I Band-A and 23/2+ energies, 128I low-lying levels/Band-B path, and NPA/PES evidence boundaries; all claim-level review flags remain unchanged.
- Wiki lint completed with zero errors; protected `raw/zotero/wiki-inbox.bib` remained untouched and unstaged. Local checkpoint was not created because schema-3 `.git` write probe returned `Access denied`; no push was attempted.

## [2026-09-05] ingest | 15 篇学位论文批次与 Git 解耦

- Completed content ingest for 15 degree dissertations (Ding existing, Alwaleedi key-evidence re-read, 13 new thesis sources) plus the 1974 `103Pd` experiment report; added source-level evidence, locators, review triage and minimal direct relations.
- Added `100Sn`/GT-strength/lifetime/signature-inversion anchors and preserved thesis/journal shared-data and independent-experiment boundaries. `178Hf` key pages were visually/OCR checked because its text layer is unreliable.
- Git failure was treated as a publication-only condition for this batch. A one-time explicit-stage publisher was added at `script/git20260905.ps1` with double-click entry `script/git20260905.cmd`; no raw PDF, protected BibTeX, ACL or credential material was changed.
- `wiki_lint.py --fail-on error` passed with zero errors; commit/push remains pending until the one-time script attempt.

## [2026-09-05] publication-attempt | degree dissertation batch

- Ran `script/git20260905.ps1` once without `-DryRun`; schema-3 stopped before staging with exit 42 because runtime marker `:workspace` did not match project profile `wiki_l3`.
- No new commit, amend, push, ACL change, credential access or raw modification occurred. Content remains complete and `final-not-pushed`; the script can be rerun by the user after repairing the Git/runtime environment.

## [2026-09-05] diagnostic | degree dissertation publisher boundary

- A child-process `-DryRun` with `CODEX_PERMISSION_PROFILE=wiki_l3` passed project-config/marker and root write checks but `.git` write probe remained `Access denied`; diagnostics showed two explicit nonmatching DENY entries and no matching current-token DENY.
- This was read-only diagnosis only; no stage/commit/push or ACL/credential change occurred. Content remains complete and the user-facing script is the sole continuation path after external repair.

## [2026-09-05] tooling | QMD refresh after degree dissertation batch

- `qmd update` indexed 27 new and 13 updated knowledge pages; `qmd embed -c nuclear-knowledge` completed with 384 files and 2615 vectors, 0 pending.
- The refresh touched only the ignored project-local `.qmd` index; no Git index, raw PDF, protected BibTeX or repository governance file was changed.

## [2026-09-05] framework | 90-day continuous nuclear-structure learning

- Implemented `system/workflows/continuous-learning.md`, `system/learning-queue.md`, and daily/weekly/milestone output indexes for the 90-day expert-learning loop (about 80% nuclear structure, 20% adjacent nuclear science).
- Documented multi-topic/multi-source learning with 2–3 hour checkpoints, milestone/information-gain stopping, graph closure, source independence, thematic REFLECT and L0–L4 boundaries; README, user guides, `check.md` and scheduled-continuation now expose the workflow.
- Created and enabled Codex project automation `wiki` for daily 22:00 Asia/Shanghai runs. The daily task has an explicit content-only path when Git/AskPass/network publication fails, while root/config/sentinel/protected-hash/raw-overlap failures still safe-suspend.
- No raw PDF, protected BibTeX, ACL, credential or `.codex` content was changed. The first daily run and post-change Wiki lint remain to be verified.

## [2026-09-06] continuous-learning | first daily run: `100Sn` B(GT) evidence map

- Selected `100Sn` GSI-vs-RIKEN B(GT) comparison as the highest-information gap after deferring overlapping `135Pr`/`187Au` review queues.
- Added a project evidence map, one deduplicated open question, reverse links, and daily record; preserved `multiple-independent`, source-level locators and all `needs_review` boundaries.
- Schema-3 root probe passed but `.git` probe remained `Access denied`; protected BibTeX hash unchanged. Content is `content-complete / final-not-pushed`; no Git publication action was attempted.

## [2026-09-07] continuous-learning | `100Sn` raw-PDF crosswalk audit

- Re-read Hinke Ch.5.1–5.4/Ch.6.2 and Lubos Ch.4.2/4.4/Ch.5.1 from the local PDFs; verified endpoint/Q corrections, branch components, response treatment, level-scheme and model-space locators.
- Updated both source pages with locator audits and expanded the `100Sn` project matrix; all claim-level review flags and independent-lineage boundaries remain unchanged.
- Preflight stopped on runtime marker mismatch `:workspace` vs `wiki_l3`; lint passed with 0 errors, and no Git publication action was attempted.

## [2026-09-10] tooling | Gitee canonical remote and GitHub maintenance retired

- Verified local `origin` fetch/push URLs as `https://gitee.com/chx6/silicon_graduate`; no GitHub remote remains. Removed only the repository-local GitHub-specific credential/SSL configuration entries.
- Retired `.github/workflows/wiki-lint.yml` and removed its `system/lint-config.json` required-path entry; updated active repository, security, contribution, check, workflow, plan and memory guidance so Gitee is the maintenance endpoint and GitHub is mirror-only.
- The explicitly scoped snapshot was committed as `Ingest dissertation corpus and migrate Wiki to Gitee` and tagged `迁移github至gitee`; concurrent capability/hook/farmer changes remained outside the commit. Gitee fetch/ancestry passed, but branch+tag dry-run failed before authentication because the stale repository `core.askpass` points to a missing Windows path; the no-askpass retry found no credentials, so no real push occurred and the state is `final-not-pushed`. No raw file, protected BibTeX or credential content was changed.

## [2026-09-10] tooling | configure/muIon-beam Agent capability adoption

- Reviewed fixed commits `18a5bfec545adc0029cee1129dba8a3437730299` (`configure`, MIT) and `a2939799aad0d7672fb3c45f612da84ad56742bf` (`muIon-beam`). Installed the 25 general configure skills plus its license copy under user-level `/root/.codex/skills`; added Wiki adapters for `evolution`, `farmer` and `hook`.
- Added `system/agent-capability-adoption.md` and `system/agent-capability-upgrade.md` with source pins, adoption/rejection gates, brainstorm/auto/up/tag routing, and the rule that external skills do not bypass L0–L4, human review, raw, credentials or Git publication controls.
- Added explicit read-only `wiki_hook.py` lifecycle checks and JSONL-only `wiki_farmer.py` supervision with one pending continuation per allowlisted transient error; no Codex SQLite, credentials, raw files, Git commit/push/tag or automatic Codex configuration was changed.
- Full system tests passed (17 tests in 65.655s), agent-ops tests passed (4 tests), and Wiki lint passed with 0 errors. Farmer dry-run observed Wiki sessions and queued no recovery message. Capability files remain uncommitted for explicit review.

## [2026-09-10] tooling | shared skill migration

- Confirmed `/root/.agents/skills` is the Docker `shared-skills` volume and the Codex-supported shared discovery path; `/root/.codex/skills` is the container-local `codex-profile` volume.
- Migrated 25 cross-project configure skills from fixed commit `18a5bfec545adc0029cee1129dba8a3437730299` into the shared repository, retaining `ATTRIBUTIONS.md` and the MIT license. Excluded system-provided `skill-creator` and Wiki-bound `evolution`/`farmer`/`hook` adapters.
- Shared `skills-sync` created checkpoint `755fc63` (`auto: update shared skills 2026-09-09T21:24:46Z`); local `main` is one commit ahead of `origin/main` and the sync marker still points to the previous pushed commit. No manual push or history rewrite was attempted.
- Added the shared-first rule to Wiki memory and capability adoption guidance. Existing Wiki raw, protected BibTeX, credentials and scientific review state were not changed.

## [2026-09-10] governance | standing autonomous commit/push authorization

- User authorized routine Wiki commit/push without per-task confirmation. Updated `AGENTS.md`, `check.md`, user guides, ingest/reflect/autonomous-research/scheduled-continuation workflows, memory and capability guidance.
- Automatic publication still requires explicit file scope, protected-path checks, preflight, lint, H3, fresh fetch, remote ancestry and exact non-force refspec dry-run. Waiting-review WIP, unresolved hard P0, safe suspend, authentication failure and remote drift remain local/`final-not-pushed`.
- “不要 push”, “只 commit” and “只修改” remain per-task overrides. Force push, history rewrite, published-tag rewrite, raw overwrite and other irreversible operations remain separately gated.
- No current Wiki commit or push was performed solely because this preference changed; existing dirty files remain preserved.

## [2026-09-10] governance | portable public repository cleanup

- Removed tracked `.codex/` and `.obsidian/` configuration, ignored future local configuration, and stopped tracking `raw/zotero/wiki-inbox.bib` while preserving local files.
- Made public AI guidance and scheduled publication wording environment-neutral; the preflight now permits public clones without a local Zotero Inbox.
- Committed as `Make Wiki repository environment portable` and pushed non-force to `origin/main`; unrelated dirty files remain uncommitted.

## [2026-09-10] governance | autonomous routine Git publication finalized

- Committed the standing commit/push policy as `Enable autonomous routine Git publication` using only the ten explicitly scoped governance/workflow files; unrelated dirty files and capability scripts remained unstaged.
- Preflight passed, full system tests passed (18 tests), Wiki lint reported 0 errors, staged diff check passed, fresh fetch/ancestry and exact non-force refspec publication passed.
- Routine final/governance/tool changes now publish automatically after the gates. Waiting-review WIP, hard P0, safe suspend, current “不要 push/只 commit/只修改” overrides, force push, history rewrite, published-tag rewrite and raw overwrite remain excluded.

## [2026-09-10] tooling | capability baseline reviewed and published

- Reviewed the dirty baseline from `git status -sb`; restored the CRLF-only `knowledge/research-notes/.gitkeep` noise and retained local `docs/` plans under `.gitignore`.
- Explicitly staged the 10 Wiki capability/governance files, including the adoption/upgrade guides, read-only hook, JSONL farmer, tests, README/lint routing and dissertation queue entry. Increased the hook's Git check timeout from 5 to 30 seconds after observing the repository's 13–14 second read-only checks.
- Preflight, 18 system tests, 4 agent-ops tests, Wiki lint (0 errors), staged diff check, exact refspec dry-run and non-force push all passed. Protected BibTeX/raw/Obsidian/local runtime content stayed outside the commit.

## [2026-09-11] continuation | degree-dissertation L3 crosswalk

- Rechecked `135Nd` D3/D4 parity from the raw thesis pages: the D4 positive/negative contradiction is present in the source text, while Table 6.1 lists D4 positive and contains a separate inconsistent D3 row. Kept `DD-20260910-136ND-03` stopped as `source-text/table conflict`; no review flag or confidence changed.
- Separated Qiang `87Zr` SHANS lifetime/derived-strength evidence from the dependent 65-MeV GALILEO `131Ba` lineage, and separated Sensharma thesis/journal support lineages from independent Lv/Guo counter data for `135Pr/187Au`. Four missing-data/provenance stops remain; L4 stays 0.
- Post-edit checks: `git diff --check` exit 0; Wiki lint exit 0 with 0 errors; raw SHA 139/139 and index links 424/424 matched. Local WIP remains unpushed because hard P0/partial issues are still present; raw/protected BibTeX/workflow paths were not modified.

## [2026-09-13] continuation | external `135Nd`/`100Sn`/`135Pr`/`187Au` evidence audit

- Added and self-audited external source pages for 2019 `135Nd` PRC reanalysis, 2024 `100Sn` In electromagnetic properties, 2021 Guo `135Pr` comment and 2026 Sensharma `135Pr` follow-up; added four credential-free acquisition manifests. Downloaded external PDFs/CSV remain ignored under `raw/papers/gpt/_incoming` and were not staged.
- `DD-20260910-136ND-03` changed from stopped to completed at the cross-source level: the 2019 PRC正文/IPDCO/E2-E1/table evidence supports D3/D4 positive parity while preserving the D3 `334.4 keV` table anomaly. `100Sn` warm-up produced no material change to the GSI/RIKEN B(GT) comparison.
- `135Pr` evidence now includes SH26 DB1/DB2 links and old-data χ² response plus GU21 double-solution/polarization counter-methodology; `SE21-1..8` remains unresolved and no new independent experiment or L4 was counted. Targeted `187Au` search found only already-ingested Guo 2022/arXiv `2011.14354v3`; `185Au` 2026 was excluded as a different nucleus.
- Farmer was started as PID 8571 and reports no transient recovery actions. Lint passed with 0 errors; current research totals are L3 `55/31/21/3` and L4 `0`. Final publication still requires explicit scope review, preflight, fetch/ancestry, dry-run and exact non-force push.

## [2026-09-13] finalize | degree-dissertation L3/L4 research package

- Completed the Codex self-audit continuation: 55 degree PDFs (54 unique hashes and one duplicate), 46 degree source mappings, 143/143 source SHA matches, index 428/428, four acquisition manifests, and protected-path checks all passed. L3 remains `55/31/21/3` and L4 remains `0`, with scientific partial/stopped boundaries preserved.
- The rolling WIP was amended to `Finalize degree dissertation corpus L3/L4 research 20260912`; the package contains the external `135Nd`, `100Sn`, `135Pr` and `187Au` crosswalk updates, governance synchronization, reports, handoff and queue reconciliation. The exact commit hash is kept in the task receipt, not in repository content.
- Final local gates passed: Wiki lint `errors=0`, 20 system tests `OK`, preflight `ok=true`, staged diff check clean, and the protected Zotero BibTeX SHA matched the baseline. Raw PDFs, OCR artifacts, local plans, temporary reading directories and protected BibTeX remained outside the commit.

## [2026-09-21] continuation | residual citation, graph and L4-input audit

- Corrected the audit boundary: the prior whole-library receipt covered structural integrity, not automatic resolution of every metadata or data-availability residual.
- Expanded the reaction parser/element map with regression tests; three genuinely underdetermined multi-channel reactions remain warnings. Restored 19 local-BibTeX citation keys and 55 Crossref-verified DOI keys without modifying protected BibTeX; 76 keys remain intentionally unmapped and are listed in the citation-key audit.
- Added the source-provenance coverage map for 59 former graph orphans, and a public-data readiness audit for the `137Ba` double-γ question. The cited Mendeley snapshot is unavailable at the checked endpoint; no L4 pseudo-result was generated.

## [2026-09-21] maintenance | QMD residual cache refresh

- Re-indexed the knowledge collection and completed CPU embedding for the post-pass tree. QMD now reports 532 Markdown documents, 2,172 current vectors, zero pending vectors and zero retained orphan chunks after compaction. This cache state does not change scientific review status.

## [2026-09-21] git | residual-resolution package committed

- Committed the explicit residual-resolution package as `Resolve high-spin audit residuals and L4 readiness` on `main`. The package contains the parser/tests, Crossref key registry, provenance hub, public-input manifests, readiness audits, reports and handoff/log reconciliation. Protected BibTeX, raw PDFs, local reading records and temporary visual/OCR artifacts remain outside the commit.

## [2026-09-21] git | residual-resolution publication verified

- Exact non-force `HEAD:main` publication succeeded on Gitee. Remote `refs/heads/main` matches the local residual-resolution commit; the protected BibTeX SHA remains unchanged and the only dirty paths are user/local raw and temporary reading inputs outside scope.
