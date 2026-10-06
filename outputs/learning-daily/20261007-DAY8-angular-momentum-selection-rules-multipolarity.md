---
type: learning-daily
graph-excluded: true
created: 2026-10-07
updated: 2026-10-07
---

# 2026-10-07 DAY8 — 角动量耦合、选择定则与多极性

## Run state

- run_id: `prompt-2026-10-07-day-08`
- run_date: `2026-10-07`; timezone: `Asia/Shanghai`; day_index: `8`; phase: `nuclear-structure-framework`
- schedule_id: `wiki-daily-learning`; run type: `substantive daily-learning`
- session_id: `01a111fb-370d-7ed1-afe9-881ccc47caf4`
- resume_command: `codex resume 01a111fb-370d-7ed1-afe9-881ccc47caf4 -C /workspace/wiki -s danger-full-access -a never`
- session mode: 本日新建会话；起始工具调用被用户中断后在同一本日会话继续，未复用 Day7 会话。
- status: `running / Day8 card content complete / study-window open`。本文是持续更新的实质日报，不是提前结束本日的回执；课程 state 仍为 `next_day_index=8 / completed_day_count=7`，收束时经正常 runner 验收与发布门后才保存学分。
- completed_day_indices: [8]
- partial_day_indices: []
- Day 8 card audit: complete
- hard research deadline: `2026-10-08T15:00:00+08:00`；15:00–16:00 用于收束、DAY9 计划/prompt 和发布。
- 原定启动：`2026-10-07T16:00:00+08:00`；本次由用户提前手动启动。提前启动不把截止改成 10 月 7 日 15:00。
- 当前正式回执：[multipolarity-run-01/run.json](20261007-DAY8-angular-momentum-selection-rules-multipolarity-run-01/run.json)。继承的 `multipoles-run-01/02` 不含可核验的完成结果，保留原件，不据其计卡。
- [运行前基线](20261007-DAY8-angular-momentum-selection-rules-multipolarity-run-01/baseline.json) 保存 562 个 knowledge Markdown 哈希、Git dirty baseline、PLAN、课程 state 与既有 dirty daemon 哈希。raw、PLAN、已有 daemon 修改和全部 review 标记保留。
- 实时钟基线：`2026-10-07T00:22:25+08:00`，距硬截止 2317 分钟；后续原生时钟核验为 `2026-10-07T01:29:38+08:00`。每轮继续前重新读当前时间，不沿用旧快照。
- 容器内同 session 计时监督在 `2026-10-07T01:50:21+08:00` 启动。双锁阻止今日 16:00 重复启动，检查点以正式 run 的 started_at 为锚，每两小时一次；15:00/15:45/16:00 分别是收束、条件提醒和逾时记录。`clock-state.json` 的心跳只证明计时进程在线，不冒充持续研究或提示已执行。
- Farmer 已 dry-run 并确认 watcher 在线（PID 87927）；只恢复允许的暂态错误，成功 turn 不由 farmer 自动续学。

### Day 8 card completion audit

| Day-matrix deliverable | Locator / artifact | Status |
|---|---|---|
| 查来源正文前回忆 E1/M1/E2、triangle/parity 和 forbidden/hindered，再记录差异 | [来源前原答与核对表](20261007-DAY8-angular-momentum-selection-rules-multipolarity-run-01/recall-record.md)；RB67 printed p.320 / PDF p.15；LKH82 pp.120–123 / PDF pp.2–5 | complete |
| 正式核对两篇主来源的 δ、符号、相位、初末态和发射吸收条件 | 下文 convention 表；[LKH82](../../knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md) LKH82-1/4/5；[RB67](../../knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md) RB67-1/4/6/8 | complete |
| 三条合成跃迁重新推导全部 gamma 候选，说明高阶截断与互补测量 | [独立枚举与负例](20261007-DAY8-angular-momentum-selection-rules-multipolarity-run-01/synthetic-multipoles.json)；下文三例表；RB67-5/7，LKH82-5 | complete |
| 分开 spin/parity/multipolarity 的观测和依赖，检查是否循环使用一个拟合 | 下文依赖审计；[spin-parity 方法页](../../knowledge/methods/spin-parity-assignment.md) 的 Assignment Evidence Dependencies | complete |
| 交付可回链的选择定则、多解/测量表、全部 convention locators，并保存 durable knowledge | [多极混合比知识页](../../knowledge/observables/multipole-mixing-ratio.md)；本日报唯一 writeback block；[来源身份哈希核对](20261007-DAY8-angular-momentum-selection-rules-multipolarity-run-01/source-identity.json) | complete |

上述 complete 表示本次独立完成卡的内容交付；尚未发生本日 15:00 收束、课程状态推进或 final publication。DAY9 若后续预习，只添加到 partial 列表，保持今日 day_index=8，不计 DAY9，不打开 Day10。

## Candidate pool and selection

本日问题是“选律允许什么，以及测量究竟能排除什么”。优先使用用户指定的两篇已摄入来源；与 Day7 预习 source fingerprint 重叠是正式课程要求，不能据此继承预习学分。没有为合成题搜索新文献批次，也没有转入新的核素案例。

| Candidate / coverage | 选择与信息增益 | 状态 |
|---|---|---|
| 一般角动量/宇称与 E1/M1/E2 口诀的边界 | 完整 triangle 避免漏掉 `Ji+Jf`；检查高 L 是否被误删 | 本轮已完成 |
| KS/RB/BR 的 δ 相位、归一化和级联顺序 | 裸 RME 简写、positive-root 和第一/第二 γ 的符号会影响结果比较 | 本轮已完成；继续保留跨 convention 的应用条件 |
| angular rank K 与 photon rank L；polarization/alignment 条件 | 原知识页把 polarized 初态误作 odd K 的充分条件，原文可直接纠正 | 本轮已完成，产生实质知识修订 |
| E0、K-shell ICC 和未观测寿命分支 | `2+→2+` 可有无 gamma 的转换通道；普通两成分 ICC 式需要条件 | 本轮已完成，下一轮复述检查 |
| 三题的观测可识别性和循环赋值 | 每题列出允许高阶、测量需求与共享假设，不造实验结果 | 本轮已完成；后续检查点继续用负例检验 |
| 已有争议核素、独立实验或 event-level L4 | 可改变具体机制判断，但本题没有事件、response/covariance 数据，且无需扩展批次 | deferred；不作为本日模拟结果 |
| 下一未完成卡 Day9：B(E2)/B(M1)、寿命/分支输入链 | 与本日 rate/phase 区分直接相连；允许恰好一张不计学分的预习 | 课程卡已检查，知识预习尚未开始 |

下一阶段先检查本日多成分可识别性、截断敏感性和级联相位是否仍有信息增益；局部饱和后按实时钟进入有边界的 Day9 预习。Day8 内容交付完成没有结束学习窗口。

## Sources and evidence

两份 raw PDF 的 SHA-256 已分别重新计算，与 source 页一致；结果在 source-identity.json。原 PDF 只读，所有渲染留在 `tmp/day8-20261007/`。主代理独立查看 LKH82 printed pp.121/122/169 与 RB67 pp.318/319/320 原图，交叉核对代理的公式、符号及条件。

| Source | 身份、主线与本次实际阅读 | Evidence boundary |
|---|---|---|
| Lange, Kumar & Hamilton 1982，DOI `10.1103/RevModPhys.54.119` | 76 页综述/汇编，实际印刷页为 **119–194**，已修正旧的 119–185。目录主线：定义/符号 → 模型 → 数据处理 → 实验与模型比较。本次读摘要、目录、相关引言，图核 pp.121–123 / PDF pp.3–5 和 p.169 / PDF p.51，核验首页/末页 | 本轮没有重读全部历史数据表；原有 deep-read 是历史摄入状态，本次局部核对不重新认证它。理论定义与被综述的实验分别记录 |
| Rose & Brink 1967，DOI `10.1103/RevModPhys.39.306` | 42 页 theory-method paper；本次代理图读 pp.306–326、335–336，之后追加 pp.339/340/347 的 R_K/ρ_K 附表及表注，共 26/42 页。主线：微扰论、emission/absorption、time reversal → 多极算符 → 角分布/宽度/δ → 布居/级联 → 核矩阵元与 convention。III.B–III.E 是 pp.314–321，III.F 是 pp.321–326 | 本轮未重读全部 appendix 或所有后续单粒子矩阵元。PDF 页 = printed−305；例如 p.320 是 PDF p.15。旧 source 的 `PDF pp.306…` 数字原指印刷页，已加明确 crosswalk |

两个来源都是理论/方法或汇编，不是本次新的独立实验。LKH82 对 RB67/KS 等 formalism 的重述不增加实验独立性。此题没有具体核素，故 isotope/isotone 对比不适用；没有因此建立核素页。

### Convention 和公式定位

| 项目 | 原文约定或本次等价重写 | 精确 locator / 适用条件 |
|---|---|---|
| 单光子选律 | `L∈整数且L≥1`；`\|Ji−Jf\|≤L≤Ji+Jf`；E：`πiπf=(−1)^L`，M：`πiπf=(−1)^(L+1)` | RB67 printed p.320 / PDF p.15, Eqs.3.40–3.41 后说明。宇称式是其 E/M 列表的等价重写；需确定的初末态宇称 |
| KS 的 rate 定义 | `δ²=Tγ(E2)/Tγ(M1)`；不是包含内转换的总率比 | LKH82 printed p.121 / PDF p.3, Eq.2.1；E2/M1 均允许 |
| KS 有符号定义 | `δKS=(√3/10)qγ ⟨Jf\|\|M(E2)\|\|Ji⟩/⟨Jf\|\|M(M1)\|\|Ji⟩`，`qγ=Eγ/(ℏc)`；BM 算符、final bra/initial ket，无额外 CoulEx `i^λ` | LKH82 printed p.121 / PDF p.3, Eq.2.5 与后文；常用单位 Eq.2.6 是 `0.835 Eγ(MeV) × RME(E2)[eb]/RME(M1)[μN]`；positive-root 系数不把 δ 强制为正 |
| RB 有符号定义 | `a_Lπ=⟨Ji\|\|T_L^π\|\|Jf⟩/√(2L+1)`；`δ_Lπ=a_Lπ/a_lowest`，最低阶的 δ=1；此处 initial bra | RB67 printed p.319 / PDF p.14, Eq.3.39。T 自身含能量/相位；和 KS 核算符之比不能只换名称 |
| RB 算符/实数条件 | T 直接定义于 Eq.3.20；相位沿 Eqs.3.16–3.23；TR 在 Eq.3.23、核态相位 Eq.2.23，实 RME 条件 Eq.3.32 note(v)，ratio 的 Lloyd 条件 footnote17 | RB67 pp.314–316 / PDF pp.9–11；p.310 / PDF p.5；pp.318–319 / PDF pp.13–14。Eq.3.24 是发射振幅展开；LKH82 Sec.II 本身没有给 TR 的证明 |
| 发射/吸收与状态顺序 | RB 发射用 initial-left 的 Ha；改用 initial-right 要连同 He=Ha†；离散态与 continuum 边界不能混用 | RB67 pp.308–312 / PDF pp.3–7, Eqs.2.12–2.16′、2.26。LKH82 p.122 / PDF p.4, Eq.2.10b 的电算符发射+、吸收−；磁算符 2.10c 没有此± |
| 发射级联 KS↔BR↔RB | γ1：`δKS=−δBR=−δRB`；γ2：`δKS=+δBR=−δRB`。KS 第一/第二 γ 的交叉项分别 −2δF / +2δF | LKH82 p.122 / PDF p.4, Eqs.2.8–2.11 和页末关系。仅用于该发射级联；不无条件推广其它 multipole pairs、吸收或所有叫 Biedenharn 的约定 |
| RB 的级联相位 | 第一 γ cross term 另有 `(−1)^(Lbar1−L1)`，第二 γ 没有此因子；source-case population 对应 intermediate J2 | RB67 p.326 / PDF p.21, Eqs.3.71–3.73。Eq.3.73 原图未显式印 ΣK；若恢复完整 W 的 K 求和，要说明来自上下文 |
| 线偏振和未测偏振 | linear amplitudes 是两种 helicity 的 coherent superposition；Eq.3.25 仍保持 q，不是 helicity 求和；未测偏振才非相干相加 | RB67 p.316 / PDF p.11, Eq.3.24 后及 Eq.3.25；p.319 / PDF p.14, Eq.3.35 前。此处没有任意现代 polarimeter 通用的 P 数值公式 |
| even K 与 rank 上限 | 确定宇称+未测偏振 ⇒ even K，即使初态 polarized；独立地 `w(−M)=w(M)` ⇒ odd B_K=0。`K≤2Ji`，`\|L−L′\|≤K≤L+L′` | RB67 p.320 / PDF p.15, Eqs.3.40–3.41；p.317 / PDF p.12, Eq.3.28；p.319 / PDF p.14, Eq.3.36；p.318 Eq.3.32 note(iii) |
| 宽度与 sign | 固定 `Ji→Jf` 和 k：`τγ,f^−1=(4k_f/ℏ)Σ_(Lπ)\|a_Lπ,f\|²`；本跃迁各多极的部分 γ 宽度比 = `\|δ\|²`。固定实 δ 条件下写 δ²，无相对符号 | RB67 p.318 / PDF p.13, Eq.3.29；pp.318–319 对 normalized RME 的说明。求多个末态总率时逐个用 k_f 相加，实验总寿命还需非 γ 通道 |
| E0/ICC | `qK²=T_K(E0)/[αK(E2)Tγ(E2)]`；`αK,obs=[αK(M1,λpen)+δ²(1+qK²)αK(E2)]/(1+δ²)` | LKH82 p.123 / PDF p.5, Eq.2.12；p.169 / PDF p.51, Eq.4.1。K 壳、M1/E2 gamma 截断；qK 不是 photon qγ，λpen 不是 rank。忽略 E0/penetration 才得到普通两成分 ICC 式 |

## Theory/analysis exercise

### 来源前 recall 与正式核对

原答在 `2026-10-06T16:15:17Z`（北京时间 10 月 7 日 00:15:17）先保存在工具上下文，写前门通过后原样存入 recall-record.md。此前已读用户 prompt 和 index/handoff 的概览，未读 Day7 日报正文或 Day8 两篇来源正文，故标为 **prompt-primed recall**，不称 blind recall。之后读取 Day7，仍重新推导本日题目。

初答正确给出 photon rank、triangle/parity、E1/M1/E2 和三题候选，明确寿命不给 sign。来源后新增/修正包括：δ 的能量和 `√(2L+1)` 归一化；KS/RB 的不同 RME 顺序；两条 γ 的 convention 映射；`2+→2+` 的 E0；angular K 与 photon L 的不同上限；even K 的精确条件。

Forbidden/hindered 的教学区别保留为一般背景：前者是在明确守恒/选律假设下某一指定振幅为零，后者是允许跃迁相对明确强度参照受抑。LKH82 p.120 的 leading collective M1 ∝总 J 而禁止非对角跃迁，是特定最简模型规则；它不等同于普遍 triangle/parity 禁止。题目没有率或参照尺度，因此不能给任何候选贴上 measured hindrance。

### 独立重推三条合成跃迁

从 Wigner–Eckart 所需 triangle 出发，逐个整数 L 枚举 E/M 的宇称因子；代码用 Fraction 保留半整数自旋。本题所有数值是题设，**不对应实验、核素或新结果**。

| Case | `\|Ji−Jf\|` / `Ji+Jf` / parity | 全部单 γ 候选 | 常用截断及其它通道 | 单 γ 最大可能 even K |
|---|---|---|---|---|
| A：`3/2+→1/2−` | 1 / 2 / 改变 | E1、M2 | E1-only 忽略 M2；E1/M2 的 mixing ratio 不用 E2/M1 的 0.835 公式；指定跃迁无 E0 | 2 |
| B：`2+→2+` | 0 / 4 / 保持；photon 要 L≥1 | M1、E2、M3、E4 | M1/E2 忽略 M3/E4；另允许非 γ 的 E0 conversion，不能藏入普通 γ δ | 4 |
| C：`3+→1+` | 2 / 4 / 保持 | E2、M3、E4 | M1 被 triangle 排除；E2/M3 忽略 E4；纯 E2 又忽略 M3；指定跃迁无 E0 | 6 |

高阶占优与否需要长波参数、矩阵元及测量条件。RB67 pp.313–314 / PDF pp.8–9 的 `kr≪1`、Eq.3.12 的 spherical-Bessel 展开以及 p.318 Eq.3.30 的 `k^(2L+1)` 解释低阶近似的来源；它们不把允许高阶振幅变成零。本题没有 Eγ、核尺度或 response，不能给定量抑制。

负例实际运行通过：`0+→0+` 没有单 γ；`1/2+→1/2+` 和 `0+→1+` 只容许 M1；将 A 末态宇称反转则变成 M1/E2。它们检验了 L≥1、Ji+Jf 和宇称过滤，避免只用 ΔJ 口诀。

### 各观测可以排除什么解

题设未提供观测，所以现在只能排除选律禁止项，不能声称某个允许候选已被实测排除。固定两个成分、实 δ 与 setup 时，响应系数有 `C_K=[C_ll+2δC_lh+δ²C_hh]/(1+δ²)` 的形式（RB67 p.321 / PDF p.16, Eq.3.47；LKH82 p.122, Eqs.2.8–2.9）；是否唯一解取决于测量、误差和剩余参数。

| 观测 | A：E1/M2 | B：M1/E2/M3/E4，另可能 E0 | C：E2/M3/E4 | 每列共同条件 |
|---|---|---|---|---|
| 单 γ angular distribution | A2 可以约束 E1/M2 振幅组合；不存在 A4 可用 | A2/A4 同时比较完整候选；只拟合 M1/E2 就已截断 | 适用布居下 A2/A4/A6 可比较候选，系数不保证非零 | 独立 alignment、效率/立体角、feeding 和协方差；同 L 的 pure E/M 在未测偏振分布中不可独立区分 |
| γγ correlation / DCO | 已知级联/gate 可限制 dipole/quadrupole 组合 | 比较多个候选，不把一个 DCO 阈值当通用证据 | 同样保留 E2/M3/E4 与 gate 的 δ | cascade spins、gating multipolarity、geometry/response；source case 的 K 上限由 intermediate spin 决定 |
| linear polarization | 在指定轴与标定下用完整幅度/误差比较 E1/M2 | 约束 electric/magnetic fractions 与干涉解，不只看符号 | 比较 E2/M3/E4 的 predicted polarization | 操作轴、Q/response、有限角度与背景；先验 parity/δ 不能再作为独立输入重复计数 |
| 内转换 | Z、Eγ 和壳层已知后比较 pure/mixed ICC | 需把 E0_K 与 M1 penetration 作为可能贡献；若 δ 未知，E0 不唯一 | 比较候选 ICC，保留 higher multipoles | 普通积分 ICC 给权重/δ²，不给相对 sign；本题缺 Z/Eγ，没有数字判别 |
| lifetime + branching | 给 total/partial rates，在已知多极和其它约束下求 strength | 额外 E0 可能漏出 gamma-only 归一化 | partial rate 本身不能在 E2/M3/E4 中唯一选 L | 完整末态分支、内转换、E0、feeding；不同允许 L 的未知矩阵元可匹配同一率；不给 δ sign |

`2+→2+` 的 K≤4 与 M3/E4 同时允许是关键负例：未观测 K6/8 没有排除力。若完整候选有 N 个非零实振幅，除整体归一化后有 N−1 个相对幅度；B 的四 gamma 成分已有三个比值，而单 gamma 分布最多两个非平凡偶 K。仅这两个系数、即使 alignment 已知，也不能保证一般四成分解唯一；未知布居只增加依赖。此为维数分析和识别性边界，不是合成实验拟合。

### 继续窗口内的精确 E1/M2 双解负例

使用 A 的 `Ji=3/2→Jf=1/2`，以 **RB** 定义 `δ=a_M2/a_E1`，另指定理想布居 `w(±3/2)=1/2`。这没有假定真实实验已经测出该布居。原 p.339 / PDF p.34 附表 K=2 行为 `0.5000 / 0.8660 / −0.5000`；p.347 / PDF p.42 的 folded ρ2 行为 `−2.0000 / +2.0000`。主代理再次图核两页，并独立用精确 Clebsch–Gordan/Racah 计算得到：

`R2(11)=1/2, R2(12)=√3/2, R2(22)=−1/2, B2=1`。

由 Eq.3.47，`a2(δ)=[1+2√3δ−δ²]/[2(1+δ²)]`，`W=1+a2P2`。解 `a2=a2(0)=1/2` 得到 `δ=0` 和 `δ=√3`；后者 M2 γ 份额 `3/4`。两根在全部角度有相同 normalized W。这比“可能多解”的口述提供了具体、可复现的数学反例，仍没有 measured δ、count、response 或 covariance。

选归一振幅 `(1,0)` 与 `(1/2,√3/2)` 后，两者 Σa²=1；固定相同末态和 k，Eq.3.29 的 γ 宽度也相同。本 γ channel 的率不能区分这两根；若 ICC/其它分支不同，不据此宣称实验 total lifetime 也相同。缺独立 strength、ICC 与完整分支输入时，τ 本身不提供唯一 δ。所有解析推论已同步到 multipole-mixing-ratio 的“合成 E1/M2 的精确角分布双解”，source coefficients 到 RB67-10。复现 artifact 为本 run 的 angular-degeneracy.json；代码/依赖只在 tmp，源原文与 canonical 公式保留于 knowledge。

## Counter-evidence and missing companion observables

| 待定标签/判断 | 当前支持是什么 | 反证或循环依赖检查 | 需要的 companion |
|---|---|---|---|
| 三例 Ji/Jf | 题设输入 | 不是从观测拟合所得；不能回头称为 measured spin | 独立 spin anchor、可靠级联及完整候选比较 |
| 三例 parity | 题设输入，过滤 E/M 候选 | 若 parity 先固定 E/M，再用所选 E/M 证明 parity，即循环；electric 本身不区分 E1/E2 的宇称变化 | 已约束 photon rank L、已知末态宇称与 convention/setup 明确的互补 E/M 约束 |
| “只有 M1/E2”或“只有 E2/M3” | 低阶模型 | 高阶由 triangle/parity 允许；未见高 K 不等价于不存在高 L | 有灵敏度的高阶上限、完整响应模型或明确可验证的截断条件 |
| δ sign 已确定 | 干涉敏感数据在明示 convention 下可约束 | τ、rate ratio、普通 ICC 都只有 δ²；phase map 改变可能只是标签变化 | operator/RME/axis/gate convention、拟合全分支与协方差 |
| parity、spin、multipolarity 被三次独立确认 | 一个含假设的拟合可能输出三标签 | 相同 angular counts、同一 gate/alignment 与已固定 Jπ 是共享来源，不能重复计数 | 观测通道互补、统计相关和实验谱系分别列明 |
| 大 δ 即强集体 E2 | 相对 gamma fraction 较大 | M1 分母很小也可产生大 δ；没有 τ/branch 不能给 absolute B(E2) | 绝对强度输入链与相应物理模型的 companion observables |

原始 counts、detector response、背景/gate/feeding、能量、branching/covariance 和寿命均缺失。本题没有真实缺失信号的灵敏度，不能把“没有数据”写为 null result。对实际 odd K 异常，先检查轴对称、helicity/宇称假设、响应与背景；仅凭 odd K 标签不能直接宣布新 parity mixing。

## Knowledge Impact and Learning Decision

本轮 `revises` 三处已有记录：LKH82 页范围纠正为 119–194；δ 必须包含能量/幅度归一化而保留 sign；RB67 的 definite-parity、未测偏振 even-K 结果适用于 polarized 初态。它们均由 raw 原图和精确 locator 支持。

本轮 `limits` 两种过强推断：低阶截断不能作为选律禁止，角分布高 K 的缺失不能普遍排除高 L；γ-only 分支归一化不能默许没有 E0。自旋、宇称、多极和绝对强度的观测依赖已逐项写回。

没有新增实验事实，没有将三个合成例赋给核素，没有改变 wobbling/chirality 等机制排序。L0 来源复核与 L2 解析练习完成；当前继续用本日识别性问题和允许的一张 Day9 预习获得信息增益，不把卡内容完成当作学习时段完成。

## Durable knowledge delta

四个 canonical knowledge 页实际发生变更；运行前后的哈希由 baseline 和 writeback 验收核对。所有新 claim 保留 `needs_review: true`，原有 page/claim review 状态未升级或清除。

- [LKH82 source](../../knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md)：完整 KS 定义、级联/吸收符号、E0/ICC 条件、页码 crosswalk 和实际本轮阅读覆盖。
- [RB67 source](../../knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md)：even-K 修正、归一幅度/初态 bra、K 上限、width/sign 与 coherent/incoherent polarization 区分。
- [multipole-mixing-ratio](../../knowledge/observables/multipole-mixing-ratio.md)：完整选择定则、三例、所有高阶候选、观测排解/截断与 E0 边界。
- [spin-parity-assignment](../../knowledge/methods/spin-parity-assignment.md)：spin/parity/multipolarity 的独立性与共享输入审计表，保留原文件 CRLF。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
      "anchor": "LKH82-5",
      "summary": "修正实际页范围、完整有符号KS辐射振幅定义、发射级联与吸收映射、K-shell E0/ICC条件和本轮定向阅读覆盖。",
      "sources": [
        {"path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md", "locator": "LKH82-1"},
        {"path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md", "locator": "LKH82-4"},
        {"path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md", "locator": "LKH82-5"}
      ]
    },
    {
      "knowledge": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
      "anchor": "Phase and Observable Audit",
      "summary": "修正polarized初态与even-K条件，明确相位定义RME/归一化、线偏振coherence、photon L与angular K、宽度与级联相位的边界。",
      "sources": [
        {"path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md", "locator": "RB67-4"},
        {"path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md", "locator": "RB67-6"},
        {"path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md", "locator": "RB67-7"},
        {"path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md", "locator": "RB67-8"},
        {"path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md", "locator": "RB67-10"}
      ]
    },
    {
      "knowledge": "knowledge/observables/multipole-mixing-ratio.md",
      "anchor": "三条合成跃迁的完整候选",
      "summary": "完整triangle/parity过滤、三例全候选与高阶截断、归一振幅/符号约定、各观测的排解条件、K上限与E0/ICC寿命分支边界。",
      "sources": [
        {"path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md", "locator": "RB67-5"},
        {"path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md", "locator": "RB67-6"},
        {"path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md", "locator": "RB67-7"},
        {"path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md", "locator": "RB67-10"},
        {"path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md", "locator": "LKH82-5"}
      ]
    },
    {
      "knowledge": "knowledge/methods/spin-parity-assignment.md",
      "anchor": "Assignment Evidence Dependencies",
      "summary": "逐项区分spin、parity、photon multipolarity、δ sign与absolute strength的观测、固定输入、共享假设和循环推断。",
      "sources": [
        {"path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md", "locator": "RB67-2"},
        {"path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md", "locator": "RB67-8"},
        {"path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md", "locator": "LKH82-4"},
        {"path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md", "locator": "LKH82-5"}
      ]
    }
  ]
}
```

## Open questions and belief revision

1. 在 B 的完整四 gamma 成分中，哪些 calibrated angular/polarization/ICC 信息能分开截断模型与更一般解？仅两个 angular coefficients 不保证三个相对幅度唯一。A 的精确 δ=0/√3 负例已闭合角分布的双解路线；下一有价值问题是相同两根的理想 helicity coherence 是否不同，仍须按原文约定重构，不先假定 polarization 必得唯一解。
2. E0_K 或 penetration 是否能模仿只按 M1/E2 解读的较大转换系数？原 Eq.4.1 允许这一歧义；没有额外 δ/电子壳层数据时保持 unknown。
3. 对两个来源中表面相反的 δ，若完整 operator/state/geometry map 后角分布不变，应判为 convention 等价；只有映射后对相同观测仍不一致，才考虑物理冲突。
4. Day9 的高信息路线是把 lifetime、所有 branching、ICC 和 radiative mixing fractions 接到 B 值及误差链；必须用 Day9 指定 source 的原始行，不把本日合成例补成真实强度结果。

Belief revision：原“polarized 初态需要 odd K”已被直接原文反证，改为分别检查 parity、helicity 和 population。原“δ 是裸 RME 比”不足，补齐运动学/归一化。原低阶表的 E2 例外不完整，恢复 Ji+Jf 边界。没有证据时不改变具体核素机制判断。

## L0–L4 state

| Level | 本日状态与证据 |
|---|---|
| L0 | 两篇已有来源的身份/哈希与关键原图定向核对完成，实际阅读覆盖明确 |
| L1 | source→observable/method 的约定、rate/phase 和证据依赖写回完成 |
| L2 | 三例全部多极、负例、截断/识别性和 companion 设计完成；均是解析学习 |
| L3 | 当前是相邻 formalism 的 bounded L2 核验；保留方法识别性问题与 Day9 接续路线，尚未形成新的系统课题调查。L3 也可研究方法问题，不限于核素 |
| L4 | 未进入。本日 prompt 的数据门未满足，缺事件数据、response/covariance 与完整分析输入链；可靠模拟虽可用于一般 L4，本轮枚举/解析没有完整数据研究、竞争假设验证和新认识链，仍为 L2 |

## Verification and continuation

写前 boundary 与 automation preflight 均 exit 0；两个 raw 哈希匹配；Fraction 枚举/负例 exit 0；计时脚本在主代理复核后 35/35 目标测试通过（含新增 Farmer 取消/人工处理/恢复暂停控制），解析双解的20项精确检查通过。两把学习锁由计时进程持有；加载取消控制后实际 PID 为110255，首次启动时间与已queued checkpoint-001/002保留，正常 daemon 尚未另行启动。继承 dirty daemon 文件不纳入本轮发布。

正式 closeout 必须再执行 `python3 system/scripts/wiki_boundary_check.py --root .`、`python3 system/scripts/wiki_lint.py --fail-on error`、`git diff --check`；使用原 baseline 调用正常 runner 的 report/writeback/card validators，强制 completed=[8]、Day9 只 partial，然后按 Gitee fetch/ancestor/dry-run/`HEAD:main` 非 force 发布门处理。未执行的 final 检查与 push 当前不写成通过。

继续顺序：本日识别性/phase 负例 → 最新时间和候选池 → 恰好一张 Day9 无学分预习 → 10 月 8 日 15:00 收束。日报到点更新最终快照、检查、receipt 与 DAY9 计划/prompt；课程仍由 card audit 及 runner/state 契约推进。本段没有提前停止或把等待心跳充当学习时长。

计时进程只调用现有 `codex queue --thread`，不创建研究 session。官方文档搜索/CLI reference/app-server 页面本轮返回 403；接口形状据本机实际 help 和 app server 的主线程可达性核验。`queued` 只表示队列接受；忙碌 turn 的处理时点尚无现场证明，后续在 clock-events 与本会话新 turn 中核对。容器或 app server 停止会阻断它，farmer 不替代日时钟。

Continuation：`codex resume 01a111fb-370d-7ed1-afe9-881ccc47caf4 -C /workspace/wiki -s danger-full-access -a never`。恢复时先读本日报、正式 run.json、clock-state、最新时间和 baseline，保留已完成内容；不得重建来源前 blind recall 或跳过已知高阶/E0/phase 边界。

### 持续学习检查点 1 — 本日学习窗口保持开放

- 最新 runner 检查点快照：2026-10-07T03:25:55+08:00，距硬截止2134分钟；本日四页 knowledge/writeback、五行 card audit、lint/diff均通过，课程 state没有推进。
- 第一条计时提示在2026-10-07T02:19:50+08:00被本机队列接受；current turn仍在执行，尚未记录该提示对应的后续turn，不能称已执行自动续学。后续queued/executed分别对账。
- 新的解析路线已经产出精确双解和20项代数校验；下一问题是同一两根的理想线偏振coherence。Day9卡已检查但其知识预习尚未开始，当前partial列表为空。剩余时段允许继续此题并随后预习恰好一张Day9，无学分。
- 本检查点已本地提交，稳定Git指针为branch `main` + subject `Checkpoint DAY8 conventions and timed learning`；本次是窗口内checkpoint，完整final/state/DAY9计划prompt在10月8日15:00–16:00处理。精确hash与push结果只进入run receipt。
