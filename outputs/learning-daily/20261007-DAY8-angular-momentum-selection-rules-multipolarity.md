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
- partial_day_indices: [9]
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
| Day8 模型零值、同阶展开与自由反例的迁移 | 27项检查已闭合generator-only零值与通用rank1的区别；原图纠正历史比较 | 有界L2完成，新的条件已写回 |
| Day8 单γ多解的cascade companion | 指定一个合成2+→2+→0+、末支pureE2，检验未追踪的final-state信息是否可辨 | selected；结论待验证 |
| Day8 penetration/ICC baseline | 重读Eq4.1检验固定κ下的E0排除如何随未知penetration变化 | selected；不补原文未给的数值界 |
| 下一未完成卡 Day9：B(E2)/B(M1)、寿命/分支输入链 | 已产生MU08转录纠正和有条件B/RME重算，62-check单位核验通过 | 无学分预习已写回；branch/IC/covariance边界保留 |
| Day8 B：四gamma成分与未知布居的完整单γ偏振识别性 | 43-check实际rank4、fraction-changing tangent与IFT给出连续联合解；独立表示论及calibration通过 | 有界路线完成；等待下轮候选池/clock重建 |

下一阶段先检查本日多成分可识别性、截断敏感性和级联相位是否仍有信息增益；局部饱和后按实时钟进入有边界的 Day9 预习。Day8 内容交付完成没有结束学习窗口。

## Sources and evidence

两份 raw PDF 的 SHA-256 已分别重新计算，与 source 页一致；结果在 source-identity.json。原 PDF 只读，所有渲染留在 `tmp/day8-20261007/`。主代理独立查看 LKH82 printed pp.121/122/169 与 RB67 pp.318/319/320 原图，交叉核对代理的公式、符号及条件。

| Source | 身份、主线与本次实际阅读 | Evidence boundary |
|---|---|---|
| Lange, Kumar & Hamilton 1982，DOI `10.1103/RevModPhys.54.119` | 76 页综述/汇编，实际印刷页为 **119–194**，已修正旧的 119–185。目录主线：定义/符号 → 模型 → 数据处理 → 实验与模型比较。本次读摘要、目录、相关引言，图核 pp.121–123 / PDF pp.3–5 和 p.169 / PDF p.51，核验首页/末页；续读Sec.III pp.123–133、Sec.V pp.174–184与Sec.IV.A.2 pp.167–169主线，原图重点复核模型/比较，实际没有独立Summary节 | 本轮没有重读全部历史数据表；原有 deep-read 是历史摄入状态，本次局部核对不重新认证它。理论定义与被综述的实验分别记录 |
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

### 检查点续研：条件明确的偏振排解与布居反例

[30-check polarization artifact](20261007-DAY8-angular-momentum-selection-rules-multipolarity-run-01/polarization-branches.json) 已由主代理复现；保留 RB Eq.3.24 的 magnetic q^π、p.316 的 WE ordering 和 p.312 footnote7 的 `d=exp(−iθJy/ℏ)`。分析轴取 `x′=(cosθ,0,−sinθ)`、`y′=(0,1,0)`，归一强度满足 Ix′+Iy′=W，定义 Q_s=(Ix′−Iy′)/W。

| 指定 w(±3/2)=1/2 时的 RB δ | Ix′ | Iy′ | Q_s(90°) |
|---|---|---|---|
| 0 | `3cos²θ/4` | `3/4` | −1 |
| √3 | `3/4` | `3cos²θ/4` | +1 |

两根的full W相同但这个理想轴下的线偏振不同。Σhelicity的W、其角平均、d的生成元与orthogonality先通过，再做coherent polarization；只复现W不能认证P代码，因为遗漏magnetic q^π可以保留W却改变线偏振。这里没有detector Q(E)、接受角积分或实测asymmetry。pure M2/high-M的90° Q_s=3/5；等权Mi给Ix′=Iy′=1/2；δ=−√3的forward/backward zero intensity点不定义Stokes比。原始公式与轴定义已写回RB67-11/12及observable。

[50-check population artifact](20261007-DAY8-angular-momentum-selection-rules-multipolarity-run-01/population-multipolarity-degeneracy.json) 再放松独立布居约束：pure E1、w(±3/2)=1/2给B2=+1；pure M2、w(±1/2)=1/2给B2=−1。第二组直接用(aE1,aM2)=(0,1)，没有把无穷δ当有限值。两组从振幅独立计算都得：

`W=3(1+cos²θ)/4`，`Ix′=3cos²θ/4`，`Iy′=3/4`。

每个固定方向的(−,+) helicity强度矩阵同为`(3/8) matrix((1+x²,1−x²);(1−x²,1+x²))`（x=cosθ），trace=W；相同的是pointwise方向/偏振强度，未比较不同方向的场相干、γγ correlations、核末态或完整光子量子态。共同k和辐射振幅单位下目标γ宽度相同，total τ仍需ICC及其它通道。

信息变化：固定布居时偏振能区分本对角分布解；布居作为共享未知输入时，两种measurement channel仍可保留联合多极解。独立B2校准须来自同初态、已建立multipole且R2≠0的另一个branch，并匹配gate/feeding/response；ICC需Z/E/壳层和有分辨力的预测/实测区间。原文支持见p.324 / PDF19右栏末段、p.347 / PDF42 ρ2表、p.316的振幅式；矩阵等式是本轮L2重构，不是作者新实验结论。

### 检查点续研：E0/ICC的联合解和参考率零点

[ICC/E0 identifiability artifact](20261007-DAY8-angular-momentum-selection-rules-multipolarity-run-01/icc-e0-identifiability.json) 已由主代理复现。代码使用Fraction精确检查125组纯代数(a,r,t)网格和端点/负例，共1311项断言通过；这些检查验证分类公式，没有提供atomic ICC、测量值或新的L4数据。

合成B的完整gamma候选是M1/E2/M3/E4；下面额外只留M1/E2、忽略penetration、只看K壳并要求αK(E2)>0。定义t=δ²、z=qK²、a=αK(M1)/αK(E2)>0、r=αK,obs/αK(E2)>0。有限t>0时：

`r=[a+t(1+z)]/(1+t)` ⇒ `z=(r−a)/t+r−1`。

非负E0要求 `(r−1)t≥a−r`。r>1且a>r时需t≥(a−r)/(r−1)，a≤r时任意t>0；r=1需a≤1；0<r<1需a<r且0<t≤(r−a)/(1−r)。a=r=1时z=0但任意t均给同一ICC。一个r通常留下连续(t,z)解；例a=4,r=2既容许(2,0)又容许(4,1/2)，只是合成代数，不能当真实原子系数。

关键零点：t=0时z的E2-rate分母为零，不能据δ=0删除E0。用 `y=tz=T_K(E0)/[αK(E2)Tγ(M1)]` 得 `r=(a+t+y)/(1+t)`，于是t=0仍可r=a+y、y≥0。固定有限z的t→0与固定y的t→0是不同路径；后者z可发散。pure E2则改用E2参照r=1+z，t/y未定义。K参考系数为零或两保留γ率都为零时，只说明该归一化失效；不能默许允许的其它gamma/非gamma通道消失。

普通z=0 ICC是两纯系数的convex combination，所以r在min(a,1)与max(a,1)之间。高侧越界可与E0相容，但还要查M1 penetration、允许高阶、响应/背景或assignment；低侧越界连非负E0也解释不了这个假设包。这个判据检验模型条件，不独证E0，更不提供δ sign。前提见LKH82 printed p123/PDF5 Eq.2.12与p169/PDF51 Eq.4.1；所有不等式和端点属于本轮解析重构，已到source LKH82-6和observable的ICC边界。

### 四γ成分的完整偏振矩阵与局部连续联合解

在合成B `2+→2+` 中保留全部M1/E2/M3/E4；设RB实辐射振幅 `a=(1,u,v,z)`、aligned diagonal布居 `w0=p0,w±1=p1/2,w±2=(1−p0−p1)/2`、已知对称轴、Mf未观测。不是已测population或高阶fraction。

[独立表示审核](20261007-DAY8-angular-momentum-selection-rules-multipolarity-run-01/four-multipole-representation-audit.json) 与 [43-check完整振幅/Jacobian回执](20261007-DAY8-angular-momentum-selection-rules-multipolarity-run-01/four-multipole-observable-rank.json) 分别用factorial-d/CG-Racah与完整振幅求和交叉核验。主代理另复现后者43項（exit0、约6.96s计算主体）。所有高阶同时保留后，归一方向与线偏振差为

`W=1+A2P2+A4P4`，`Δ=Ix′−Iy′=C2P2^(m=2)+C4P4^(m=2)`，`H=matrix((W,−Δ);(−Δ,W))/2`。

`P_K^(m=2)`是关联Legendre，不是P_K平方。初态J2、axisymmetry和aligned布居只留K0/2/4，所以M3/E4不产生K6/8。在meridian轴U=V=0；已知轴旋转混Q/U而不增独立transition/population系数。因scalar角函数跨通道可有重叠，正确计数使用matrix-valued基底；normalized W固定constant项，剩四个形状系数，Q=Δ/W一般为有理函数。所有等式只关逐方向强度，不比较跨方向field coherence、γγ correlation或完整光子态。

| Actual bounded check | Result | 判断及边界 |
|---|---|---|
| seed `(u,v,z,p0,p1)=(1/2,1/3,1/4,1/4,1/4)` | w0=w±2=1/4、w±1=1/8；fractions=(144,36,16,9)/205 | 严格内域、四成分非零；没有用isotropic或zero-amplitude端点造generic结论 |
| 五输入→四shape coefficients | exact Jacobian rank4，非零4×4minor | 不只是参数计数；exact代数判零与核检验已保存 |
| kernel的radiative-fraction tangent | 约(−0.30699,−1.11783,+0.63941,+0.78541) | 非零；IFT给一维精确fixed-observable level set，附近fractions不同 |
| 同一kernel的有限直线步 | 只保证一阶不变 | 没有把它冒充精确第二解；精确曲线存在来自IFT |
| independently fixed p0/p1 | 同点4×3 amplitude-only rank3 | 仅局部逆解/识别性改善；不宣称global唯一 |
| isotropic p0=1/5,p1=2/5 | 任意mixing W1、Δ0 | 直接反证“校准布居就必然所有点唯一” |
| 新增合成same-parent2+→0+ E2参考设计 | R2c=−√70/14、R4c=−2√14/7，均非零 | 可同时校准B2/B4；该branch不是题设或实测，须independent Jπ与gate/feeding/axis/response匹配 |

选择Gaussian布居或M1/E2截断可以减少自由变量，但这是追加模型条件。多个measurement channels共享未知布居时，完整理想单γ方向/偏振也不保证multipole assignment唯一。完整B_K、四二次型matrix entries、非零minor、IFT证明和companion inversion已写回[[rose-brink-1967-phase-defined-angular-distributions]]的RB67-13，并到multipole-mixing-ratio和spin-parity method。原文premises：p316 Eq3.24/线偏振段，p317 Eq3.28/rotation-product identity，p319 Eq3.36，p324 folded population/同初态branch段；rank/seed/IFT属于本任务重构，不是作者直接报告的实验。没有新L4。

### 固定已知布居的全局多解：73-check U证书

[精确pair回执](20261007-DAY8-angular-momentum-selection-rules-multipolarity-run-01/four-multipole-fixed-population-pair.json) 已由主代理复现73項、exit0，计算主体约4.28s。以四成分次序(M1,E2,M3,E4)，正交U有rU=√(3/35)、sU=√(32/35)，并保留S与全部R2/T2/R4/T4二次型。取a=(1,1/2,1/3,1/4)，b=Ua约(0.38543,0.61150,0.40490,0.85859)，两向量均full-support、同S=205/144，固定p0=p1=1/4且B2/B4非零，全部W/Δ residual exact为0。两点各自local rank3，b的fractions约(0.10435,0.26266,0.11516,0.51783)，与a=(144,36,16,9)/205不同。

lifted D=aaᵀ−bbᵀ为rank2/trace0，满足五个trace条件。θ0投影links的某些sign flips对应两helicities共同的未观测final-channel unitary，在同方向photon trace中消去。详细U、向量、fraction exact expressions与short explanation已到RB67-14、mixing observable和spin-parity method。极简pureM1也映为E2/E4 coherent组合(3/35,32/35)，是补充边界例；主证书没有依靠isotropic或zero amplitude。

本例校准“已知布居+局部满秩”仍不能单独证明global唯一。其模型保留全部allowed自由振幅；微观/long-wave strength bounds、ICC、核末态、cascade、cross-direction coherence和total τ均未被证为相同，没有实际核素高阶强度判断。它是固定RB convention内不同amplitude模型的同pointwise观测，不改变operator/axis convention。

### 原合成C的局部逆解与高K零点

[41-check C回执](20261007-DAY8-angular-momentum-selection-rules-multipolarity-run-01/case-c-angular-polarization-rank.json) 经主代理复现，完整E2/M3/E4与unknown aligned population求和后W/Δ最高even K6，无K8。输入 `(u,v,p0,p1,p2)`、输出 `(A2,A4,A6,C2,C4,C6)` 在seed `(1/2,1/3,1/4,1/4,1/4)` 为exact rank5；rows(A2,A4,A6,C2,C4)的非零minor建立smooth local inverse。六forward函数、B_K与minor到RB67-15，仍无global唯一结论/实验精度估计。

pureE2在任意population下A6=C6恒0（L2+L2<6），该特殊点full-map rank4；isotropic w1/7下higher amplitudes仍非零而W1/Δ0，rank3。B6非零也可让R6干涉使A6=0；相应两real nonzero E4 roots已到source，C6不必零。正确响应下nonzero K6可排除pureE2，zero K6不能反向删掉higher candidates。这与原B的连续解是不同spin/model条件下的结果；local full rank与label independence/global选择分别审核。

### Day9 无学分预习：输入—公式—输出—误差

已读该卡的 existing lifetime synthesis 和 MU08 source 后整理本节；没有来源前 Day9 recall，也没有正式 Day9 card audit。所有知识预习仅列 partial=[9]，即使覆盖知识交付也留到 Day9 新 session 独立完成后计卡。

MU08 六页全文主线由同线程代理图读，主代理图核 PDF pp.3–5；raw SHA 与现有 source 一致。Table II 的 Band2 B(E2) 五项应对应 I=15–19，已修正旧知识页的错行/漏行。Fig.2 的464.8-keV与Table I的465.5-keV标签差异保留，不猜哪处是排版错误，不用于本次输入组。来源身份与分支边界保存在[24-check来源输入回执](20261007-DAY8-angular-momentum-selection-rules-multipolarity-run-01/day9-strength-input-packet.json)；[62-check 单位/归一化回执](20261007-DAY8-angular-momentum-selection-rules-multipolarity-run-01/day9-strength-unit-audit.json) 已由主代理复现，保存完整代码、常数和原baseline指针。

LKH82 p.121 / PDF p.3 的 Eqs.2.2–2.3a 给出 `Tγ(XL)∝Eγ^(2L+1)B(XL)` 与 `B=|RME|²/(2Ji+1)`。现代CODATA 2022下，E(MeV)、τ(ps)的系数为 C_E2=0.0816202120、C_M1=0.0568709756；这是单位重构，不能归成作者直接印出的绝对寿命常数。历史0.0816与舍入相容；0.05697不由该页直接支持。

| 输入或步骤 | 公式/输出 | 误差、条件与 locator |
|---|---|---|
| Band1 parent Ex=6711.4keV, 18−；τ=0.56(8)ps | mean level lifetime，Ttot=1/τ | MU08 034311-4 / PDF4, Table II I18；stopping/feeding fit 条件 |
| 757.4keV, 18−→16−；b=0.24(2) | E=0.7574MeV，沿作者B(E2)赋值作pure-E2核验 | MU08 034311-3 / PDF3, Table I Ex6711.4三行；E误差未印出 |
| 同parent另两枝401.2:0.57(6)、389.6:0.19(2) | 三中心值和1 | 同Table I；不证明无漏枝，也未明确photon/total/IC定义 |
| gamma-only且printed b可作pγ | τγ=τ/pγ=2.3333ps；Tγ=4.28571×10¹¹s⁻¹ | 只用于条件性算术；total b须除(1+αtot)，photon β须按所有支路IC及额外非γ率归一化 |
| B(E2)=C_E2 pγ/(τ E⁵) | 0.14034e²b²；作者值0.14(2)保持原样 | 率定义LKH82 Eq.2.2；没有从作者B反推ICC |
| RME magnitude = sqrt[(2Ji+1)B] | 2.27876eb；不求signed RME或Qt | LKH82 Eq.2.3a；不能再除一遍(2Ji+1) |
| 独立quoted τ/b误差、暂略σE | σB/B=sqrt[(0.08/0.56)²+(0.02/0.24)²]，σB=0.02321e²b² | 是有条件一阶传播，不是完整confidence interval；协方差需另给 |

μN²与e²b²是不同B单位；γ宽度Γγ=ℏTγ有能量单位。假设只留M1/E2时 fM1=1/(1+t)、fE2=t/(1+t)，t=δ²；Tγ,L=pγ fL/τ，不把radiative fraction当total branching。K-shell ICC不能代替总壳层ICC。误差应传播共享τ/branch和α(E,t)，不能把同一t造成的mixing/IC变化重复当独立误差。

Counter-evidence：MU08 PDF3明确quoted errors未含可达15%的stopping-power systematic；15%不是已量化的side-feeding误差，未给其概率分布/covariance，不能自动按独立1σ求和。Pure M1是ΔI1 absolute B(M1)提取假设，未测δ。Table I、Table II、Fig.4、Qt和本轮重算来自同一输入链，中心值一致不增加实验独立性。漏枝、feeding、IC或branch definition未补全时保留条件，不把视觉峰高当B，也不对具体集体机制重新排序。

全部可复用公式、单位、输入表与误差边界已同步至[寿命强度综合](../../knowledge/synthesis/high-spin-lifetime-strength-deformation.md)；原表、错行纠正、假设和标签差异至[MU08 source](../../knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md)。没有event/line-shape、response、feeding可执行输入或covariance，不进入L4。

### Day9 无学分预习：两母态四branch负例

[22-check控制回执](20261007-DAY8-angular-momentum-selection-rules-multipolarity-run-01/day9-gamma-only-chain-controls.json) 保存完整code/hash和封存source packet引用；主代理独立复算四个中心值。Gamma-only、沿作者pure-M1/E2赋值的输出为：

| Parent | Eγ (keV), pure extraction assumption | τ (ps), printed b | Gamma-only B | Author B | Descriptive center difference |
|---|---|---|---|---|---|
| Band 1, 18− | 401.2, M1 | 0.56(8), 0.57(6) | 0.89638532 μN² | 0.9(2) μN² | -0.402% |
| Band 1, 18− | 757.4, E2 | 0.56(8), 0.24(2) | 0.14034419 e²b² | 0.14(2) e²b² | +0.246% |
| Band 2, 15− | 199.6, M1 | 1.27(6), 0.93(5) | 5.237069 μN² | 4.4(3) μN² | +19.024% |
| Band 2, 15− | 382.0, E2 | 1.27(6), 0.07(1) | 0.55306379 e²b² | 0.54(8) e²b² | +2.419% |

Band1原b0.57/0.24保留第三branch0.19，不将选中两行归一到1。19.02%仅是低能M1与作者rounded center的描述性差值，没有计算显著性或从quoted B倒解ICC、δ、ρ/branch basis。单条高能E2吻合不验证整条ledger；shared inputs、IC、未印能量误差、covariance和stopping/feeding均保留。源数据/公式见MU08-4/5/6、LKH82 p121 Eq2.2/2.3a；数值与判断已写回MU08 source及lifetime synthesis。正在核验独立理论α的可用性，结果只用于明确假设的forward比较。仍partial9，不是正式Day9卡或L4。

### Day9 无学分预习：独立FO输入与branch定义的forward敏感性

[官方查询/离线复现回执](20261007-DAY8-angular-momentum-selection-rules-multipolarity-run-01/day9-independent-icc-readiness.json) 保存五个Z60理论输入，主代理offline replay exit0、新增查询0。Actual web backend BrIccS v2.3(9-Dec-2011)/BrIccFO；unused local help v2.3d(13-Sep-2022)、缺data files、All空结果和NNDC404/IAEA403分开记录。没有向查询提交B、τ或branch，没有用输出匹配倒解输入。

| Eγ/pure hypothesis | Program Tot α | αK | Coverage |
|---|---|---|---|
| 401.2 M1 | 0.0320(5) | 0.0274(4) | N6 missing warning |
| 389.6 M1 | 0.0345(5) | 0.0295(5) | no returned-table warning |
| 757.4 E2 | 0.00416(6) | 0.00351(5) | N6 missing warning |
| 199.6 M1 | 0.204(3) | 0.1739(25) | no returned-table warning |
| 382.0 E2 | 0.0251(4) | 0.0204(3) | no returned-table warning |

α无量纲，Tot不能换成K。两N6 blank未填零；KB08 p208/PDF7说明Z59–75约400keV截断及usually<10⁻⁹，未当本两点严格误差界。p206/PDF5 Table2脚注1.4%已含interp，不将约0.3%再独立加一次。default60-Nd-144（p221/PDF20 TableB.1）、actual136Nd radius/charge state、energy error、NH spread与shared covariance留边界。

在complete inventory/no extra decay假设下，相同printed numbers若作photon g，`τTγ,i=g_i/[Σg_j(1+α_j)]`；若作total β，则`τTγ,i=β_i/(1+α_i)`。Dg(B1I18)=1.0257934、Dg(B2I15)=1.191477；`(photon formula/total formula−1)`分别为401.2 +0.605%、757.4 −2.109%、389.6 +0.849%、199.6 +1.051%、382.0 −13.964%。这只是forward sensitivity，未识别Mu08实际branch/IC处理或改变mechanism ranking。

全部25项subshell/major sums、5点Tot/K、response SHA/lookup参数、原文误差/coverage locators和forward表到[KB08 dated supplement](../../knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md)的新KB08-D8-1/2/3与lifetime synthesis。该source既有page/KB08-1–8及AR人审记录原样保留，新附录明确self-audit、needs_review=true。原文Ref16仅能定位到Chiara PRC64,054314(2001)，本文未补出其full text或processing定义。仍未进入L4/正式Day9card。

### 模型零值与自由多极反例的迁移审计

[LKH82模型回执](20261007-DAY8-angular-momentum-selection-rules-multipolarity-run-01/lkh82-model-truncation-audit.json) 的27项代数检查经主代理复现exit0，39项raw/artifact/原图hash核对通过。source LKH82-8–11 保存全部可复用证明与适用条件。

| 判断 | 已核结果 | 原文/推导归属 |
|---|---|---|
| 最简collective M1零值 | 只有Eq3.9形变无关零阶piece为constant×J；[H,Jq]=0给不同能量态间零矩阵元。合法rank1 toy current仍可连接same-J/parity两multiplets | LKH82 pp.125/127/128；交换子与表示论为本任务推导，不是普遍M1禁戒 |
| perturbation阶次 | n1→n0 direct operator与wave-function mixing同阶；一阶derivative零不等于all-orders零 | pp.126–129 Eqs.3.21–3.24、3.31–3.40；152Sm例与footnote3，限source模型 |
| 大δ/DF ratio | 同δ100的任意√rate振幅可有相差10⁴的E2率；DF factor取消后A^(5/3)式不测shape，零率点只给limit | p.121 Eqs.2.1–2.6、p.125 Eqs.3.10–3.13；尺度反例与零分母审计为推导 |
| 模型比较的独立性 | IBM magnitudes/PPQ signs仍按作者8/46样本记录；TableV全部theoryδ用了experimentalEγ | pp.178–179 caption/讨论；没有新primary experiment或全表重新认证 |
| 真实核迁移 | 自由多极tuple必须落在共同states/current、long-wave/strength、absolute/nonγ与response/population条件内 | pp.119/121/124–133/169/183；不将formal存在性当成各模型同等物理可信 |

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

新增模型审计 `limits` generator-only M1零值的外推和大δ的绝对强度解读，`supports` 同阶operator/state展开；历史IBM/PPQ比较依原图纠正，review状态保留。

本轮 `limits` 两种过强推断：低阶截断不能作为选律禁止，角分布高 K 的缺失不能普遍排除高 L；γ-only 分支归一化不能默许没有 E0。自旋、宇称、多极和绝对强度的观测依赖已逐项写回。

没有新增实验事实，没有将三个合成例赋给核素，没有改变 wobbling/chirality 等机制排序。L0 来源复核与 L2 解析练习完成；当前继续用本日识别性问题和允许的一张 Day9 预习获得信息增益，不把卡内容完成当作学习时段完成。

## Durable knowledge delta

七个 canonical knowledge 页实际发生变更；运行前后的哈希由 baseline 和 writeback 验收核对。所有新 claim 保留 `needs_review: true`，原有 page/claim review 状态未升级或清除。

- [LKH82 source](../../knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md)：完整 KS 定义、级联/吸收符号、E0/ICC 条件、页码 crosswalk 和实际本轮阅读覆盖。
- [RB67 source](../../knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md)：even-K 修正、归一幅度/初态 bra、K 上限、width/sign 与 coherent/incoherent polarization 区分。
- [multipole-mixing-ratio](../../knowledge/observables/multipole-mixing-ratio.md)：完整选择定则、三例、所有高阶候选、观测排解/截断与 E0 边界。
- [spin-parity-assignment](../../knowledge/methods/spin-parity-assignment.md)：spin/parity/multipolarity 的独立性与共享输入审计表，保留原文件 CRLF。
- [MU08 source](../../knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md)：修正Band2原表spin/value映射，保存所选母态全部印出branches、pure-M1假设、stopping误差和未消解label差异。
- [lifetime-strength synthesis](../../knowledge/synthesis/high-spin-lifetime-strength-deformation.md)：B/RME单位、mean/partial τ、三种branch定义、mixing/ICC/共享误差与条件性MU08输入链。
- [KB08 source supplement](../../knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md)：新dated/self-audit附录保存FO lookup、1.4%含interp、N6/atomic radius/version与forward敏感性；原human-review记录不扩展到新增内容。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
      "anchor": "LKH82-5",
      "summary": "修正实际页范围、完整有符号KS辐射振幅定义、发射级联与吸收映射、K-shell E0/ICC条件和本轮定向阅读覆盖；补充K-shell ICC/E0可行解分类、零参考率重参量化和高/低侧越界的模型边界；据parent图核p179纠正IBM幅度/PPQ符号的历史8/46样本比较，未更改review状态；追加47-check fullγ+E0下total ICC/τ补全、shell contrasts与统计/函数依赖边界；写回generator-only M1零值、同阶算符/态展开、大δ绝对尺度与真实核高阶/模型迁移条件。",
      "sources": [
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-1"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-4"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-5"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-6"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-2"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-7"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-8"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-9"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-10"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
      "anchor": "Phase and Observable Audit",
      "summary": "修正polarized初态与even-K条件，明确相位定义RME/归一化、线偏振coherence、photon L与angular K、宽度与级联相位的边界；补充phase-aware helicity/coherent polarization重构，以及未知布居下pointwise方向/偏振强度联合解的边界；补充完整四γ/未知布居的pointwise方向-偏振基底、43-check局部rank/IFT多解与同初态校准的局部/全局边界；追加已知非等权布居、四成分全非零的exact U global pair，local rank3/global多解与final-channel trace解释；追加caseC完整六coefficient/five-input局部rank5、pure/isotropic rank和K6 zero/cancellation控制；追加caseC的29-check exact global reflection/两个rank5分支与B6非零的A6=C6联合抵消。",
      "sources": [
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-4"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-6"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-7"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-8"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-10"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-11"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-12"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-13"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-14"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-15"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-16"
        }
      ]
    },
    {
      "knowledge": "knowledge/observables/multipole-mixing-ratio.md",
      "anchor": "三条合成跃迁的完整候选",
      "summary": "完整triangle/parity过滤、三例全候选与高阶截断、归一振幅/符号约定、各观测的排解条件、K上限与E0/ICC寿命分支边界；补充phase-aware helicity/coherent polarization重构，以及未知布居下pointwise方向/偏振强度联合解的边界；补充K-shell ICC/E0可行解分类、零参考率重参量化和高/低侧越界的模型边界；补充完整四γ/未知布居的pointwise方向-偏振基底、43-check局部rank/IFT多解与同初态校准的局部/全局边界；追加已知非等权布居、四成分全非零的exact U global pair，local rank3/global多解与final-channel trace解释；追加caseC完整六coefficient/five-input局部rank5、pure/isotropic rank和K6 zero/cancellation控制；追加caseC的29-check exact global reflection/两个rank5分支与B6非零的A6=C6联合抵消；追加47-check fullγ+E0下total ICC/τ补全、shell contrasts与统计/函数依赖边界；写回generator-only M1零值、同阶算符/态展开、大δ绝对尺度与真实核高阶/模型迁移条件。",
      "sources": [
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-5"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-6"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-7"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-10"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-5"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-11"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-12"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-6"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-13"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-14"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-15"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-16"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-7"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-8"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-9"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-10"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/methods/spin-parity-assignment.md",
      "anchor": "Assignment Evidence Dependencies",
      "summary": "逐项区分spin、parity、photon multipolarity、δ sign与absolute strength的观测、固定输入、共享假设和循环推断；补充phase-aware helicity/coherent polarization重构，以及未知布居下pointwise方向/偏振强度联合解的边界；补充完整四γ/未知布居的pointwise方向-偏振基底、43-check局部rank/IFT多解与同初态校准的局部/全局边界；追加已知非等权布居、四成分全非零的exact U global pair，local rank3/global多解与final-channel trace解释；追加caseC完整六coefficient/five-input局部rank5、pure/isotropic rank和K6 zero/cancellation控制；追加caseC的29-check exact global reflection/两个rank5分支与B6非零的A6=C6联合抵消；写回generator-only M1零值、同阶算符/态展开、大δ绝对尺度与真实核高阶/模型迁移条件。",
      "sources": [
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-2"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-8"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-4"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-5"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-11"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-12"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-13"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-14"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-15"
        },
        {
          "path": "knowledge/sources/rose-brink-1967-phase-defined-angular-distributions.md",
          "locator": "RB67-16"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-8"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-9"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-10"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "LKH82-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
      "anchor": "Lifetime and Branching Input Audit",
      "summary": "据原图修正Band2的I15–19/B(E2)映射和遗漏值；保存I18寿命及三枝input ledger、pure-M1与quoted systematic条件、branch定义和464.8/465.5标签边界；将全部26条Table I分支与10行Table II输入/输出固化到canonical source；追加两母态四branch的gamma-only负例，保留未重归一化的0.19分支和描述性残差/共享数据边界；补入独立FO inputs/forward branch敏感性及未识别原processing的边界。",
      "sources": [
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-4"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-5"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-6"
        },
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D8-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/synthesis/high-spin-lifetime-strength-deformation.md",
      "anchor": "从寿命、分支到约化强度",
      "summary": "写回Gaussian/SI与现代E2/M1单位推导、mean/partial lifetime和total/photon branching、mixing/IC及共享误差，保留MU08的条件性B/RME重算与原作者输出；追加两母态四branch的gamma-only负例，保留未重归一化的0.19分支和描述性残差/共享数据边界；补入独立FO inputs/forward branch敏感性及未识别原processing的边界。",
      "sources": [
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "Eq.2.2"
        },
        {
          "path": "knowledge/sources/lange-kumar-hamilton-1982-multipole-admixtures.md",
          "locator": "Eq.2.3a"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-4"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-5"
        },
        {
          "path": "knowledge/sources/mukhopadhyay-2008-136nd-transition-rates.md",
          "locator": "MU08-6"
        },
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D8-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
      "anchor": "2026-10-07 Supplement",
      "summary": "新self-audit附录保存实际FO model Tot/K与全部subshell数据、response hashes、1.4%含interp、N6/radius/version可用性和两branch定义forward敏感性；原人审page/claim/AR记录保留，新claims needs_review=true。",
      "sources": [
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D8-1"
        },
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D8-2"
        },
        {
          "path": "knowledge/sources/kibedi-2008-evaluation-theoretical-conversion-coefficients-bricc.md",
          "locator": "KB08-D8-3"
        }
      ]
    }
  ]
}
```

## Open questions and belief revision

1. 在 B 的完整四 gamma 成分中，哪些 calibrated angular/polarization/ICC 信息能分开截断模型与更一般解？仅两个 angular coefficients 不保证三个相对幅度唯一。A 的精确 δ=0/√3 负例已闭合角分布的双解路线；固定布居时的理想偏振区别已闭合；改变布居后pure E1/pure M2的pointwise偏振强度等价也已闭合，说明共享布居条件必须单独取证。
2. E0_K 或 penetration 是否能模仿只按 M1/E2 解读的较大转换系数？原 Eq.4.1 允许这一歧义；没有额外 δ/电子壳层数据时保持 unknown。
3. 对两个来源中表面相反的 δ，若完整 operator/state/geometry map 后角分布不变，应判为 convention 等价；只有映射后对相同观测仍不一致，才考虑物理冲突。
4. Eq.4.1的E0/ICC联合解、参考γ成分为零的奇异边界与convex-hull反证已闭合；缺少本題Z/E，未查询数值ICC。按当前时间和完整候选池重新选择下一高信息路线。Day9 的高信息路线是把 lifetime、所有 branching、ICC 和 radiative mixing fractions 接到 B 值及误差链；必须用 Day9 指定 source 的原始行，不把本日合成例补成真实强度结果。

Belief revision：原“polarized 初态需要 odd K”已被直接原文反证，改为分别检查 parity、helicity 和 population。原“δ 是裸 RME 比”不足，补齐运动学/归一化。原低阶表的 E2 例外不完整，恢复 Ji+Jf 边界。没有证据时不改变具体核素机制判断。

## L0–L4 state

| Level | 本日状态与证据 |
|---|---|
| L0 | Day8两篇身份/哈希及关键原图定向核对完成；Day9预习追加MU08六页主线与Tables I–II核验，覆盖明确 |
| L1 | source→observable/method 的约定、rate/phase 和证据依赖写回完成 |
| L2 | 三例全部多极、负例、截断/识别性和 companion 设计完成；追加Day9无学分单位、branch/rate/RME及条件误差重构，均是解析学习 |
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
- 第一条计时提示在2026-10-07T02:19:50+08:00被队列接受，实际同session续学在2026-10-07T07:18:39+08:00留证，存在约299分钟队列处理延迟。当前fresh snapshot距截止1901分钟；该旧queued时间不冒充当前时间。后续queued/executed分别对账。
- 解析路线已产出精确双解20项、理想偏振30项、未知布居50项校验；E0/ICC的参考成分奇异边界与模型排除条件也已闭合，准备按实时钟与候选池选择唯一Day9预习。该检查点时Day9卡已检查、知识预习尚未开始；其后已启动预习，当前partial列表为[9]。剩余时段允许继续此题并随后预习恰好一张Day9，无学分。
- 本检查点已本地提交，稳定Git指针为branch `main` + subject `Checkpoint DAY8 conventions and timed learning`；本次是窗口内checkpoint，完整final/state/DAY9计划prompt在10月8日15:00–16:00处理。精确hash与push结果只进入run receipt。

### Candidate-pool rebuild — Day9无学分预习启动

D8的rank/phase、理想偏振/共享布居和E0/ICC零参考率三个有界路线均已完成。实际spin/parity赋值仍缺独立population/response和数据；本题ICC仍缺Z/E，不用新文献或虚构原子系数补它。额外cascade未给定spins/gate，先保留适用边界。最新时钟及选择记录保存于本run的progress.jsonl/run.json。

现在进入且仅进入Day9的B(E2)/B(M1)/partial-lifetime知识预习，使用该卡已有synthesis/Mukhopadhyay 2008 source；记录为partial9、不给学分、保持day_index8及course state8/7，不开Day10。本预习的完整知识即使覆盖交付，也留到正式Day9新session独立recall/evidence/card audit后才计卡。

### 可恢复检查点 — 2026-10-07 09:49 Asia/Shanghai

当前真实时钟距硬截止1750分钟，保持Day8/[8]与Day9/[9]无学分预习。rank/phase、pointwise偏振/布居联合解和E0/ICC零参照边界三个Day8有界路线已经闭合；再补真实赋值需要独立布居、响应或Z/E输入。重建候选池后继续MU08原表与rate-to-strength输入链：查Table I/II的spin/value映射、branch是否含IC、quoted统计误差与未含的stopping systematic。来源定位和下一步保存在[research-checkpoint.json](20261007-DAY8-angular-momentum-selection-rules-multipolarity-run-01/research-checkpoint.json)。正在等待同一线程已有两个代理的定向核验；没有新建主session或重启daemon。计时监督的心跳、排队与实际执行分别记录，不作为研究时长。

### 持续学习检查点 2 — 知识预习与识别性续研

当前branch `main` + subject `Extend DAY8 observable bounds and uncredited DAY9 strength inputs` 已按18-file显式manifest提交并通过Gitee fetch、ancestry、dry-run、`HEAD:main`非force push与H3文件/远端对账。精确hash只进入本run receipt。六页writeback/card validators、boundary、lint（0 errors/91 warnings）与diff通过；PLAN、dirty daemon、课程state原哈希匹配，三份raw SHA与review flags保留。课程state仍8/7，本日没有final。新增来源packet的24项检查与全Table I/II事实已经同步source，待随下一次实质增量发布。Day8四gamma/未知布居的完整单γ偏振局部识别性已由parent43-check复现并写回；Day9低能branch条件性负例保持无学分。

### 最新候选池和时间门 — 2026-10-07 12:17 Asia/Shanghai

距硬截止1602分钟。四γ/未知布居路线已43-check闭合；full global/cascade/ICC反演超出该有界证明，未强行扩展。Day9继续两个母态四branch的gamma-only负例，已显示单条E2吻合不能验证整条输入链。重建候选池后，选择existing BrICC source/local or public atomic-data input的readiness核验：若可得到独立理论all-shell ICC，才forward比较photon/total branching两种假设；不得从quoted B倒解α、ρ或δ、不得冒充MU08实际采用的处理。此项仍属唯一Day9无学分预习，未开Day10或新文献批次。当前readiness没有实际α值或新增claim；结果/失败待核验后写回。继续命令与恢复点在research-checkpoint.json，课程state仍8/7。

### 检查点续研 — C全局pair与LKH82原图纠错

C-global [29-check回执](20261007-DAY8-angular-momentum-selection-rules-multipolarity-run-01/case-c-global-polarization-pair.json) 已parent复现，两个local rank5点同六coefficients、different fractions；pureE2的三成分映像在B6非零也A6=C6均0。源/observable/method到RB67-16。LKH82 p179/PDF61 parent原图核对后，已修正LKH82-2和model段落：IBM更合δ magnitudes、PPQ更合signs；共同8例sign错误3/1，PPQ更大46例错8并有W isotope disagreement。两样本不合并统计、不作普遍model ranking。仍在重读model/truncation边界，保持本日卡与next-card无学分约束。

### 47-check companion补全 — E0、total ICC和τ

[新符号回执](20261007-DAY8-angular-momentum-selection-rules-multipolarity-run-01/gamma-icc-lifetime-e0-completion.json) 已parent复现47项。synthetic B的U pair在sameλγ与允许E0下，αobs≥maxκ可取T0,j=λγ(αobs−κj)匹配same totalα与τ^-1=λγ(1+αobs)，所有photon curves也相同；低于较大κ或λγ/τ不一致可以反证此条件包。没有实际Z/E或measurement被赋值。Shell contrast d_s=η_s(κb−κa)−(κs,b−κs,a)非零且灵敏度足够时额外shell/total可排解；全部contrast为零时仍退化。Counts共享与functional independence分别用joint Jacobian核验，不重复计算derived partial ICC证据。完整单位/零分母/Ω与covariance特例到LKH82-7及mixing observable，KB08新增附录给p204/PDF3 E0定位且保持旧人审记录。

### 恢复点与候选池 — 2026-10-07 18:22 Asia/Shanghai

最新原生时钟距硬截止1237分钟。C-global29-check、E0/ICC/τ47-check、LKH82模型27-check均已parent复现并写回七页知识中的相关页。当前选择两个独立Day8有界问题：一个明确合成2+→2+→0+的cascade是否区分已知布居U pair；Eq4.1未知penetration是否限制固定no-penetration ICC下的E0排除。两者仍在计算/来源核验，未宣称新结果。Day9仅partial9，其branch定义、atomic coverage、feeding/covariance缺口保留；没有新卡或文献批次。本日窗口保持开放，15:00才进行最终state/Day9计划prompt收束。

### 模型与companion阶段发布记录

本地检查点稳定指针：branch `main` + subject `Clarify model zeros and companion observable limits for DAY8`；17-file显式manifest只纳入已parent核验的C-global/E0/model增量、日报/恢复点和检查回执。最新检查确认七页writeback、completed8/partial9、preflight/lint/diff有效。此为持续检查点，不结束学习窗口或推进state；两个新Day8 bounded路线仍在执行。
