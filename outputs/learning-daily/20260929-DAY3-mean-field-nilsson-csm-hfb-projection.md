---
type: learning-daily
graph-excluded: true
run_id: prompt-2026-09-29-day-03
runner_run_id: 2026-09-29-day-03-03
parent_run_id: 2026-09-29-day-03-01
run_date: 2026-09-29
timezone: Asia/Shanghai
day_index: 3
phase: nuclear-structure-framework
cycle: 2026-09-30-day-substantive
schedule_id: wiki-daily-learning
schedule_name: Wiki 30-day substantive daily learning
run_kind: substantive
acceptance_only: false
review_status: ai-draft
session_id: 01a0eb92-e525-7863-a0c9-af73a53d832b
session_mode: resumed-existing-session
---

# 2026-09-29 Day 3：平均场、Nilsson/CSM、HFB 与投影模型

## Run state

- 本报告收口正式 30 天学习周期的 Day 3，run ID `2026-09-29-day-03-03`，主题“平均场、Nilsson/CSM、HFB 与投影模型”。研究窗口于 `2026-09-30 15:00 Asia/Shanghai` 关闭；此后仅完成日报、知识写回、回执、next-day prompt 和发布门，不再开新科学路线。
- 本次由原入口 session 恢复，session ID `01a0eb92-e525-7863-a0c9-af73a53d832b`；恢复命令：`codex resume 01a0eb92-e525-7863-a0c9-af73a53d832b -C /workspace/wiki -s danger-full-access -a never`。原 run-01 因服务高负载 exit `1` 的事件保留，当前 session 沿用同一 session，不伪装为新的 schedule session。
- 入口回执/续接记录位于 [`run-03/run.json`](20260929-DAY3-mean-field-nilsson-csm-hfb-projection-run-03/run.json) 和 [`continuation-prompt.md`](20260929-DAY3-mean-field-nilsson-csm-hfb-projection-run-03/continuation-prompt.md)；正式 Day 4 prompt 生成于 [`20260930-DAY4-pairing-quasiparticle-configuration.md`](prompts/20260930-DAY4-pairing-quasiparticle-configuration.md)。
- 继承的 Day 2、Day 3 run-01 输出与原始材料保持未修改；本日 Banik 2020 和 Jehangir 2022 PDF、访问 manifest 与渲染图/文本只保存在 Wiki 内 `raw/` / `tmp/`，不进入 Git。`PLAN.md`、受保护 `raw/zotero/wiki-inbox.bib` 和已 human-reviewed 的 `131Xe` 页面未修改。
- 报告、48 项 writeback、lint、boundary、preflight、diff 与 next-day prompt 检查通过后，run receipt 标记 `completed / counted_in_substantive_test: true`；[30 天状态](../learning-milestones/2026-09-one-month-state.json) 已推进至 `next_day_index: 4`。Git H3 发布结果在 scheduler event 和最终回顾记录。

## Candidate pool and selection

### Current continuation selection (2026-09-30)


基于当前模型卡和 Hara Table 5 余下候选，选择 136Pr 为本续接主问题：是否已有同核现代三轴 mean-field 计算，且它是否属于角动量投影。它与已完成的 131Ce 测量设计不共享目标核或跃迁，作为非重叠新颖性路线；136Pr 同时是 Hara N=77 候选。预期高信息增益在于判断新 TAC-CDFT 解究竟支持哪类模型结论，以及哪些残差/缺项仍挡住唯一指认。检索池包括 134La、135Ce、136Pr、137Pr 的 exact-nuclide projection/TPSM 查询，137Nd 的同核异模型案例，以及现有 131Ce transition-design 延续项。arXiv、Crossref、OpenAlex、Semantic Scholar、INSPIRE 和已存 Wiki 来源的覆盖边界均记入；Google Scholar HTML 请求无响应，不将其计作负结果。按可读全文与决策信息增益排序，选择 136Pr 2025 TAC-CDFT 论文完整复核，并保留 134La/135Ce/137Pr 为后续有限路线。候选池依据 [当前问题列表](../../knowledge/questions.md)、[A≈130 thesis evidence matrix](../../knowledge/projects/a130-thesis-evidence-matrix.md)、[A≈130 model-choice card](../../knowledge/projects/a130-model-choice-card.md)、[131Ce/133Ce project](../../knowledge/projects/131ce-collective-mode-discrimination.md)、9 月 27 日 Day 1 和 9 月 28 日 Day 2 记录，以及 Wiki 已有来源指纹重建。

| 槽位 | 候选问题 | 信息增益与选择 |
|---|---|---|
| 连续性 | `131Ce` 现有 crossing/alignment/signature 证据如何对应 CSM 与投影模型的能力，哪些观测才足以判别 γ-soft、wobbling 或 chirality？ | 选择。现有 project 将普通 signature/configuration coupling 排在较前，但目标带仍缺直接 `δ`/偏振、partner-resolved lifetime 与 absolute `B(E2)/B(M1)`；Day 3 要求的模型适用条件可直接约束下一步证据需求。 |
| 新颖性 | 粒子数投影对截断 PSM 的改善是否单调、能否直接消除 pairing-related spuriosity？ | 选择。用 Hara–Sun 的 `156Er` Figs.26–27 检查另一个核区/方法失效模式，与 `131Ce` 的集体模式问题不共享目标数据。 |
| 暂缓 | 重开 `130Sn/132Sn` 壳隙与数据字段谱系。 | Day 2 的高信息缺口已记录；与本日模型适用性练习不重叠，留在 Day 2 continuation 路线，避免把不同观测问题塞进本日。 |
| 续接延伸 | 现代 A≈130 TPSM 对邻近 odd–odd 核的实际可检验量是什么，能否验证历史 `N=76–78` 候选或 `131Ce`？ | 先用 Bhat et al. 2014 `124,126,130,132Cs` 作为方法迁移控制；该文的 Cs 核不覆盖 Hara 候选。随后逐表映射 Hara Table 5，并检索现代三轴投影计算。 |
| 本续接非重叠新颖性槽 | `137Nd (Z=60,N=77)` 后续三轴计算是否对 Hara Table 5 形成同核直接复核？ | 选择。Wiki 已有 Petrache 2020 `137Nd` 实验/模型来源；同核但转向 CDFT/PRM 与 D2/D3、D5/D6，和 `131Ce` 611.1-keV 测量设计不共享目标数据。需要核查其是否是 PSM 复算还是另一组带的三轴模型应用。 |

来源 fingerprint 有意使用 Wiki 已有的 AFN90 与 HARA95 两篇理论综述，因为这是矩阵规定的 Day 3 主线；不把综述当作两条独立实验。续接的 Bhat 2014 与 Sheikh et al. 2024 都是理论模型/数据比较，不是新实验；后者沿用 Biswas 2019、Matta 2015 等已有数据。Alwaleedi `131Ce` 论文仅作目标核的既有观测边界，不在本续接中重复摄入。

### Active recall（开原文前）


- 我先前的工作记忆：静态 mean field 给 intrinsic density 与形状；cranking 以旋转参考系追踪 alignment 和 crossing，但不直接给良好角动量的本征谱；HFB 将配对纳入自洽准粒子态；angular-momentum projection 对旋转取向作群积分，再在投影态空间求能谱。
- 当时不确定：多组态投影是否只是单态能量比值的重复；轴对称计算无法拟合是否足以推出三轴；粒子数投影是否总能减轻配对近似误差。
- 原文复核后的修正：多投影态需要同时保留 Hamiltonian 与 norm kernel 的广义本征问题；轴对称模型失配只形成三轴候选；particle-number projection 在截断空间也可能让受污染的 pair state 更靠近 yrast。

### Continuation active recall（开 Bhat TPSM 原文前）


- 我先前对 TPSM 的预期：三轴 Nilsson+BCS/HFB intrinsic states 经三维角动量投影后做多准粒子组态混合；结果能比较良好 `I` 的谱与 transition matrix elements，但参数化、基底和 effective operators 仍是模型条件。
- 我预期 `130Cs` 案例能比较的至少有能级、带内/带间 `B(E2),B(M1)`；不确定哪些是实验直接量、哪些由 branching/模型派生，也不确定同源 `γ` 参数如何定义。
- 原文复核后：`130Cs` 的绝对跃迁强度是 TPSM 计算，图上叠加的实验是既有 `B(M1)/B(E2)` ratios；论文将绝对 lifetime data 留作后续检验。Table 1 输入按 Eq. (3) 复算出的 `130,132Cs` γ 值还与 p.6 约 30° 的文字不一致。

### Continuation active recall（开 Simons primary 原文前）


- 我预期 Bhat Ref. [32] 是一项原始 `130Cs` γ 谱学实验：应能核实 reaction、band identity/links、multipolarity 判据、Bhat 图中比值的来源和是否有 absolute strengths。
- 口试式不确定点：相近能量只表示 partner 候选；若没有寿命，`B(M1)/B(E2)` 是否只能从相对强度/分支导出？polarization 和 DCO 能闭合自旋宇称/电磁性质到什么程度？是否出现一个需要把 chiral interpretation 限定到自旋区间的反证？- 原文核对后：Euroball 反应与 Tables 1–2 给出直接谱学和四条带间 link 的 DCO/偏振；文章认为 A/B 同宇称/组态，并报告 `S(I)` 与 ratio fingerprints。Band B 的 `B(M1)/B(E2)` 未出现预期 staggering，absolute lifetimes 缺失，高自旋 crossing 使作者将 chiral 解释限在 `I\lesssim16`。

### Continuation active recall（检索 Hara Table 5 后续计算前，2026-09-29）


- 当前问题池包括：① 是否有现代三轴投影计算直接覆盖 Hara–Sun Table 5 的星号核素；② `131Ce` 目标跃迁的 mixing ratio/偏振、伙伴带寿命和绝对强度如何组成可判别设计；③ Bhat v1 的 `γ` 参数表述能否由最终版核对。选择①作为当前延续问题：它检验历史模型候选是否有后续计算，但可避免把 `130Cs` TPSM 或 `131Ce N=73` 证据迁移到不同核素。
- 不看新文献的回忆：Hara–Sun 的 triaxial 标记源自轴对称 PSM 对实验描述不足，是作者提出的模型候选；它不是直接形状测量。现代直接检验需要先逐个锁定 Table 5 的核素，再核对新计算是否使用三轴 intrinsic basis/角动量投影、实际报告了哪些同核能级或电磁量、以及参数与组态空间是否足以和旧候选比较。只看到“TPSM”或邻近核素名称并不能满足直接覆盖。
- 复看原文 Table 5 (PDF p.712) 后确定，星号覆盖 `N=76–78` 的七个单元格：`133La`、`134La`、`135Ce`、`135Pr`、`136Pr`、`137Pr`、`137Nd`；p.713 将 N=76 与 78 描述为形状转变端点，并要求三轴投影代码核对中间核素。
- 检索后发现 2024 arXiv/book chapter `2405.08368v1` 对 `133La`、`135Pr` 做 TPSM 计算；它覆盖原表七个候选中的 2 个。另发现 2026 IJMPE DOI `10.1142/S0218301326500448`，但当前只核实书目信息和访问状态，没有把摘要当作科学证据。下一步若缺少可得全文，转入 `131Ce` 最小观测设计，并保留各核素证据边界。

### Continuation active recall（131Ce 观测设计复核前，2026-09-29）


- 当前候选：连续性问题是 `131Ce` Bands 1–7 哪一组新增观测最能区分 signature/configuration coupling、γ-soft core response、wobbling 与 chirality；非重叠候选是 Hara Table 5 余下五个星号核素的后续投影计算。先做前者，因为它直接关联 thesis 主问题和下一次实验可决策观测；若公开数据检索能为余下五核提供原文，再并列推进。
- 不看 source page 的回忆：`131Ce` 已有能级、signature/crossing、alignment 与至少部分目标带寿命/`Q_t` 信息，但我不能确定现有寿命覆盖了哪些 partner transitions；Alwaleedi 的 `B(M1)/B(E2)` 假设 `δ=0`，不能替代逐跃迁 multipolarity/偏振。Wobbling 至少需要确定的 `n_ω=0/1` band identity、随自旋的 `E_wob`，以及连接跃迁以 E2 为主的证据；相似能量/能带近简并不足以区分 wobbling 和 chiral/signature partner。
- 我初步认为高价值观测是：①逐条 ΔI=1 links 的 branch/sign-resolved `δ` 加 polarization/DCO；② yrast 与 partner 两带同自旋区的 lifetime，使 `B(E2)_out/B(E2)_in` 和 `B(M1)_out/B(E2)_in` 能以绝对强度重建；③保留 crossing/alignment 作为 configuration 对照。独立形状量（quadrupole invariants/Coulomb excitation 或可靠 `Q_t`）只帮助分 γ-soft/rigid，不能单独建立 wobbling。
- 仍待核实：现有 2013/2004/2016 `131Ce` 数据究竟已有多少绝对强度点和哪些跃迁身份；最小设计要避开把同一 dataset 的不同论文重复计权，并覆盖弱 link、feeding、response 和 `δ` 双解。这些问题先以 source locator 核对，再确定最小测量次数，不凭记忆填数值。

### Continuation active recall（核对 `137Nd` 后续模型案例前，2026-09-29）


- 连续性路线（`131Ce` 611.1-keV link 的测量顺序）已完成当前设计；新颖性候选是 Hara Table 5 剩余候选中的 `137Nd (N=77)`。Wiki 已有 Petrache 2020 `137Nd` 多重手征 source/nucleus 页面，但“同核出现了现代三轴理论”不等于“对 Hara 轴对称 PSM 失配做了直接投影重算”。
- 先前的工作记忆是该 `137Nd` 案例涉及 D2/D3、D5/D6 的近简并带及 CDFT/PRM 解释；我不能确定它的形变参数来自自洽解还是拟合，也不确定计算与 Hara 表中的低能谱是否同一组态/同一可观测量。
- 本次核对要找 method/model input、被比较的 `137Nd` bands、直接实验数据 lineage 和定位图表；只有覆盖同一核素还不够，必须说明对 Hara 的直接程度。若仅是另一组带的 chirality 计算，则归为相关的三轴模型案例，不计入“后续验证 Hara 预测”的份额。

### Continuation active recall（复查 Hara Table 5 余下五核之前，2026-09-29）


- 非重叠候选为 Hara Table 5 剩余的 `134La (Z=57,N=77)`、`135Ce (58,77)`、`136Pr (59,77)`、`137Pr (59,78)`、`137Nd (60,77)`；目标是查是否有直接三轴投影计算，不把邻核或同质量区的 TPSM 方法论文当成覆盖。
- 先前 Wiki 指纹里 `137Nd` 有 chirality/集体模式来源，`135Pr` 有独立 wobbling/TiP 争议；但我没有把它们记成 Hara 原表核素的直接 TPSM 计算。此前 arXiv/Crossref 精确检索对若干核素没有命中，这只能降低先验，不等于完整检索结束。
- 新发现的 NPA DOI `10.1016/j.nuclphysa.2026.123419` 标题覆盖 `128–134La`，可能触及 `134La (N=77)`；Crossref 没有摘要，OpenAlex 标成 closed/no-repository。我的预期是这可能是一条 odd–odd La TPSM/chirality 模型路线，但没有主文就不能判断是否逐核计算 `134La` 或是否比较 Hara 的原始候选；不会把标题范围当结果。
- 当前续接选择该五核检索为 novelty slot，与刚完成的 `131Ce` 611.1-keV 实验设计不共享目标跃迁或数据。下一步先检查 Wiki 已有来源，再用不同书目索引查 exact nuclide/model terms；只有拿到全文后才评估其 `ε/ε′/γ` 输入、模型输出和原始数据依赖。

### Continuation active recall（打开 arXiv:2508.00373 前）


- INSPIRE discovery 命中一篇 2025 年理论论文 “Harmonic chiral vibration in triaxial nuclei” (`10.1016/j.physletb.2025.139794`, arXiv `2508.00373`)，但标题不能确认它是否覆盖 `137Nd` 或 Hara Table 5 的其它核素。
- 先前工作记忆：谐振手征振动是三轴核中左右手征构型附近的量子振动解释，可与准粒子—转子 / triaxial models 联系；具体模型类型、核素、参数和哪些 electromagnetic observables 是输入/输出我不能靠记忆确定。若涉及 `137Nd`，还需看它是否复用 P20 的同一 D2/D3、D5/D6 数据与缺失强度边界。
- 本轮核对目标：读摘要确认核素范围，若对 Hara 候选有直接相关性则通过合法 arXiv 全文核对模型主线、表图及限制；将模型结果与 `137Nd` 的测量分开，判断它是方法学替代解释、同核模型补充还是不覆盖候选。
- 核对结果：[[petrache-2020-137nd-multiple-chiral-bands]] 的 `P20-1/P20-2` 给同核 D3/D6 实验带，`P20-4` 给 CDFT/PRM 三轴参数，`P20-5` 指出新带缺实验 `B(M1)/B(E2)`。因此 Hara N=77 的 `137Nd` 有较新的同核三轴模型应用，但不是 PSM/TPSM 投影复算，也未逐项回代 Hara 的旧能级/形状判断；手征解释仍为实验带结构加模型，不是直接形状测量。
- 2026 NPA `10.1016/j.nuclphysa.2026.123419` 标题范围可能含 Hara 的 `134La`，但 Crossref 无摘要、OpenAlex/OpenAIRE 均无可用仓储全文，arXiv 和 OA downloader 无全文结果。它当前只作为 metadata lead，未计入已验证模型覆盖数。
- source-page review result: Petrache 2020 确实给 `137Nd` 同核 triaxial model case，但使用 constrained CDFT/PRM，分析 D2/D3、D5/D6；这不是 PSM/TPSM，也不是对 Hara 原来低能谱的逐项重算。Table 2 形变是模型结果，D3/D6 缺测 `B(M1)/B(E2)`，故只作为“同核后续三轴模型应用”记账，不计为直接投影重算或独立形状测量。
- arXiv 全文核对结果：Budaca & Budaca 2025 用 semiclassical harmonic approximation 解释低自旋 chiral-partner `ΔE(I)`；对 `137Nd` D5/D6 取 `πh11/2²⊗νh11/2⁻¹`, `j=11/2,j′=10`, 报 `γ=97.5°`（常用 sector `22.5°`）。Fig.4 复用 P20 Ref. [30] 能量数据；`137Nd` 只有两个拟合点和一个被排除的 open point，拟合值未显示统计误差。它补充同核 model route，但没有 PSM/TPSM wave-function projection，也没有 `137Nd` transition-ratio validation。

### Continuation active recall（打开 136Pr 2025 PRC 正文前，2026-09-30）


- 先前记忆：136Pr 是 Z=59、N=77 奇奇核，Hara–Sun Table 5 将其列为 presumptive-triaxial 候选，但仍是轴对称 PSM 失配后的模型标签。我预期后续三轴计算可能走 TAC-CDFT 或 TPSM；只有 TPSM/其他角动量投影路线才计为直接投影覆盖。
- 仍不确定：新文是新实验还是旧数据复用；是否做了总角动量投影；D1/D2/D4/D6/Q1 的实验约束能否闭合到唯一组态、宇称或形状；D4/D6 的 prolate/oblate 说法是否来自不同自洽支。
- 原文核对后：2025 文报告新 JUROGAM II 数据并称统计约为此前该核实验的 240 倍；方法为 PC-PK1 TAC-CDFT 与 SN100PN 壳模型，不含角动量投影。Q1 宇称仍缺偏振测量，D1/D2 强度比与计算拟合方向不同，D5 无 TAC-CDFT 匹配组态；D4/D6 形状共存只是作者保留的竞争方案。

### Continuation selection: 137Pr (2026-09-30)


Current continuity question: Hara Table 5 N=78 137Pr has no verified direct projection source yet; can a post-table high-spin paper clarify the measured band, competing mechanism and any mean-field route? This is the same coverage problem as the prior 136Pr work but uses a distinct nucleus and dataset. I selected the 2007 PRC source discovered through the 2025 136Pr paper's magnetic-rotation references; no separate novelty slot was added.

### Active recall before opening Agarwal et al. 2007


- Before the APS PDF, I expected a 137Pr odd-A high-spin case where magnetic rotation would require M1-dominated ΔI=1 links, weak crossover E2 and a spin-dependent B(M1)/B(E2) trend; band crossing could also change those trends.
- I did not know whether the 2007 paper newly measured the sequence or reused older data, whether polarization/DCO fixed the negative-parity band identity, how absolute the strength data were, or whether TAC reproduced the crossing.
- The full text shows a new INGA measurement, DCO/IPDCO M1 assignments and first reported weak crossover E2; B(M1)/B(E2) is derived from relative intensities assuming δ² negligible. Hybrid TAC proposes 3qp→5qp crossing, but the high-spin solution remains shifted by roughly 2ℏ and 2.2 MeV.

### 本续接新颖性槽：odd-neutron TPSM 方法控制（2026-09-30）

- 候选池：重试已封闭的 `134La/135Ce` direct-projection 获取路线；检查 `131Xe` 的 TPSM odd-neutron 基底扩展；或回到 `131Ce` 的寿命/偏振设计。前两条分别受全文不可得与可获得主文约束；选择 `131Xe` 主文作为方法控制，因为它直接展示投影组态空间扩展，但可和 Hara N=77 核素逐一隔离。
- 开原文前的回忆：预期 TPSM 从三轴 Nilsson+配对准粒子态作角动量投影，3ν/5qp 扩展或能影响第二次 crossing；我不确定 Xe 同位素范围、131Xe 的实验覆盖、模型形变来源和 yrare 是否已观测。
- 核对后：全文范围是 `117–131Xe`，Eq. (1) 含 `1ν`、`1ν+2π`、`3ν`、`3ν+2π`；`131Xe` yrast 带与已发表能级比较，但 Table I 形变沿用前文，yrare 带没有实验观测。Figs. 8–10 的投影振幅不能作通常概率解释。
- 本槽不把同中子数当同核覆盖；重点核对 N=77 映射和与 `131Xe` 已有人审的低 E2/signature-partner 解释是否同一实验谱系。

### 方法段主动回忆：TPSM 中 HFB 条件的角色

- 回看 Eq. (4) 前的预期：TPSM 的投影态以三轴 Nilsson+配对准粒子态为基础；我不确定论文是否每个核都重新求 HFB 形变极小值，还是只用 HFB 自洽条件固定 quadrupole–quadrupole 相互作用强度。
- 原文 Eq. (4) 说明 `χ` 与 `ε` 依 self-consistent HFB condition 相联系；Table I 的各核形变参数则来自先前工作。故“用到 HFB 自洽关系”不等于本文独立测量形状，也不等于所列 `γ` 是本论文从实验反演出的量。

### Hara N=77 direct-projection 文献补查：主动回忆与停止边界

- 查索引前的回忆：目前 `134La` 只有 2026 NPA 标题覆盖范围的闭源元数据线索；`135Ce` 已知一条 AIP conference 条目，但我不知道是否存在可合法获取的 TPSM 主文或作者仓储版。不能用标题、引文或同中子素结果补成 direct-coverage claim。
- 新路由结果：Crossref 检索只返回已登记的 2026 `128–134La` 论文及无关 TPSM 方法条目；INSPIRE 对 `134La` 没有命中、对 `135Ce` 的查询返回 `131Xe` false positive；OpenAlex/Semantic Scholar 有 429 或无新精确命中，Bing 页面结果不相关，DuckDuckGo 请求超时。没有找到新全文，也没有从 snippets 导入科学主张。
- 停止条件：相同 OA/仓储端点与精确标题查询已在前续接检查；除非出现新 repository URL、author manuscript 或公开会议录，不重试已失败 publisher URL。direct TPSM 覆盖暂维持 `2/7` 的 bounded-search 结论。

### 连续性来源选择：追到 `131Xe` 的 Banik 2020 原始实验

- 候选池：继续等待 Hara N=77 闭源投影文章；或沿 Jehangir Fig. 7 / Chakraborty 2023 的明确引用回到 Banik et al. 2020 primary `131Xe` experiment。选择后者，因为它能确认两篇后续工作的具体共用数据范围，并核对 `131Xe` 有没有寿命、绝对强度或只有限的能级/分支资料。
- 开原文前主动回忆：Crossref 题名是 “Revealing multiple band structures in `131Xe` from α-induced reactions”，2023 文称重分析 Banik 数据；我预期主实验是 `130Te(α,3n)` 布居，但不知道其线表、探测阵列、带间多极性、寿命/绝对强度，以及哪些 2023 新建跃迁不在 2020 数据中。下面核对主文，不以标题或 2023 摘要补细节。

### 复核跨模型 γ 参数前的主动回忆

- 我记得 2020 TRS 的 `131Xe` B1 中频极小约在 `γ=−26°`、2022 TPSM 表列 `29°`、2023 TPRM 取 `33°`；不确定这三者是否分别是计算输出、继承输入和拟合参数，也不确定它们是否约束同一组实验跃迁。
- 回查来源后确认：TRS 值随 `ℏω` 变化，TPSM 形变由既有文献固定，TPRM 参数用于再现 signature partners；2022 和 2023 均引用/重分析 Banik 数据，所以三数不可平均成实验形状值。

### 连续性比较选择：`131Xe` 上 TRS、TPSM 与 TPRM 的 γ 角色

- 候选池：用 2020 直接实验源确认完整数据层；比较同核 2020 TRS、2022 TPSM 和 2023 TPRM 对 γ 形变的不同使用方式；或再次检索 Hara N=77 闭源论文。选择跨模型 γ 比较，因为能检验“数值接近是否等于独立形状验证”，并且三篇论文共享/依赖同一 `131Xe` 谱学数据。
- 对照前主动回忆：我记得 Banik TRS 在中频输出约 `γ=−26°`，Jehangir Table I 把 `γ=29°` 作为 Xe 输入，Chakraborty TPRM 使用 `γ=33°`；但尚未核对三个数分别是频率依赖极小、沿用输入还是为能谱拟合的参数，也未核对 γ sector/convention 是否可直接互换。

### 复核 BNK20 的 B1(a)/B5 与 C23 序列前的主动回忆

- 先前记忆：Banik 2020 把一组高自旋平行带记为 B1(a)，另把 13/2− 起始的序列记为 B5；Chakraborty 2023 说 unfavored signature partner 过去未观测，并重分析出 9/2−、13/2−、17/2−、21/2− 序列。我怀疑 C23 的新标记主要对应低自旋 B5，而非高自旋 B1(a)，但尚未核对它们是否共享哪些能级、跃迁和标签。
- 复核目标：对照两篇 Fig. 3/ Fig. 1 与 Table I/主文，区分“相同原始事件”“相同已置跃迁”“相同能带指认”，不把数据复用说成结果完全相同，也不把新 placement 误写成新实验。

## Sources and evidence


| 证据层 | 本日核对 | 精确来源位置与状态 |
|---|---|---|
| 续接：136Pr 新实验与模型案例 | Lv et al. 2025 用 100Mo(40Ar,1p3n)、152 MeV 束流和 JUROGAM II 得到新的 136Pr 高自旋数据；作者报告 5.1×10^10 个三重及更高折符合事件，统计约为此前该核数据的 240 倍。Fig.1 建立 D1–D6、Q1–Q4 纲图；同篇再用 PC-PK1 TAC-CDFT 和 SN100PN 壳模型比较。该模型对比依赖本次同一实验数据，不是独立数据复核。 | [Lv et al. 2025 source page](../../knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md#key-results)：LV25-1、LV25-4、LV25-8、LV25-10；Fig.1、Table I–II、Figs.6–16，本地 accepted-version PDF pp.2–15。文件与 manifest 在 raw/papers/gpt/day3-mean-field-20260929/136pr-2025-tac-cdfTAC/，SHA-256 c8e14461975a7606d7e38325d6e83b500e75d232027b118743e1f1ff754537d6。 |
| 续接：137Pr 后续实验与 TAC 模型 | Agarwal et al. 2007 用 122Sn(19F,4n) INGA 新测量将负宇称 M1 带延伸到 47/2−，以 DCO/线偏振确认多极性，并首次观测弱 crossover E2。相对强度派生的 B(M1)/B(E2) 在约 37/2− 后下降；hybrid TAC 用 3qp→5qp crossing 解释 back-bending，但高自旋解偏移约 2ℏ/2.2 MeV。该路线是 exact-nucleus TAC/model comparison，不是 projected-shell-model calculation。 | [Agarwal et al. 2007 source page](../../knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md#key-results)：AG07-1–AG07-11；Fig.2、Table I、Figs.3–7，PRC PDF pp.2–7。APS 直链返回 application/pdf；Crossref 许可为 APS standard license，故在 raw manifest 中记 publisher-direct downloaded，而非开放许可。 |
| 实验直接报告（目标核背景） | Alwaleedi 2013 建立/扩展 `131Ce` Bands 1–7，并用角强度比、crossing/alignment 与准粒子 Routhian 约束谱学。Table 5.1 报告 Band 1 两 signature 的 crossing frequency `0.329`、`0.367 MeV/ℏ`。这些是能级/跃迁分析量，不是独立测得的形状或集体模式。 | [Alwaleedi 2013 source page](../../knowledge/sources/alwaleedi-2013-band-structures-131ce.md#key-results)：`AW13-1`, `AW13-5`; 本次沿用既有 source 页的 PDF/Table locator，没有重新声称复核整篇原始 thesis。 |
| 续接：可测量的 `131Ce` 互带锚点 | AW13 Table 4.4 报告 `611.1-keV 17/2−→15/2−` M1/E2 link、relative intensity `25.2±1.1` 与表内角强度比 `R=0.56±0.02`，正文识别为 Band 4→Band 1；它没有直接测得该 link 的 `δ`、偏振或绝对强度。独立 lifetime papers 测量的是 Band-1-like/宇称序列，未形成 Band 4 partner 矩阵。 | [Alwaleedi 2013](../../knowledge/sources/alwaleedi-2013-band-structures-131ce.md#key-results)：`AW13-16`, `AW13-9`, `AW13-11`；[Singh 2016](../../knowledge/sources/singh-2016-lifetime-131ce-133pr.md#key-results)：`SI16-1`；[Li 2004](../../knowledge/sources/li-2004-lifetimes-131ce.md#key-results)：`LI04-1`, `LI04-11`。这些 lifetime controls 与 thesis γ 谱不是同一实验谱系，也不是 partner-resolved interband strengths。 |
| 实验派生量与缺项 | 论文的 `B(M1)/B(E2)` 由 branching 和能量推得并假设 `δ=0`；source page 记录本数据集缺寿命、absolute `B(E2)`、偏振和直接形状测量。 | 同上：`AW13-9`（Eqs. 5.6–5.7、Table 5.4），`AW13-11`（Chapters 3–5 数据/方法 inventory）。对应的现有证据排序见 [131Ce/133Ce project](../../knowledge/projects/131ce-collective-mode-discrimination.md#evidence-available)。 |
| 作者解释 / 历史模型归类 | Hara–Sun §5.1 Table 5 将七个单元格标为“presumably triaxial”：`133La (Z=57,N=76)`、`134La (57,77)`、`135Ce (58,77)`、`135Pr (59,76)`、`136Pr (59,77)`、`137Pr (59,78)`、`137Nd (60,77)`。p.713 把 N=76、78 写作转变端点，并说中间区间仍需三轴代码确认。`131Ce` 是 `Z=58,N=73`，表中归为 prolate `+0.22`；候选不能迁移到 `131Ce`。 | [Hara–Sun 1995 source page](../../knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md#key-results)：`HS10-4`; 原文 §5.1 Table 5，PDF pp.712–713。星号是作者/模型候选，不是直接形状测量。 |
| 理论模型结果 | Åberg 等 Fig.12 展示 `132Ce (π,α)=(+,0)` 在 `ℏω=0.47,0.59 MeV` 的 cranked Routhian surfaces；图注将 `β₂≈0.40` prolate 极小与两个中子占据 `i13/2` 联系，并把另一处局部极小与 `h11/2` 中子对 alignment 联系。Hara–Sun 的 `156Er` Figs.26–27 比较不做/做粒子数投影的 band diagrams；投影改变 backbending，并使最低 `qp`-pair 态更靠近 yrast。 | [Åberg–Flocard–Nazarewicz 1990 source page](../../knowledge/sources/aberg-flocard-nazarewicz-1990-mean-field-shapes.md#key-results)：`AFN90-2`，Fig.12 / PDF p.468；[Hara–Sun source page](../../knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md#key-results)：`HS10-5`，§4.3 Figs.26–27 / PDF pp.700–701。均为模型计算，不是实验观察。 |
| 续接：现代 TPSM 邻核方法控制 | Bhat et al. 2014 用三轴 Nilsson+BCS、三维角动量投影和多组态混合计算四个 odd–odd Cs；`130Cs` Fig.3 比较已有能级，Fig.8 的绝对 `B(E2)`/`B(M1)` 曲线是模型输出，实测比较主要是先前发表的 `B(M1)/B(E2)` ratios。作者要求对 `124,130,132Cs` 进行寿命测量后再确认 chiral interpretation。 | [Bhat et al. 2014 source page](../../knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md#key-results)：`BHA14-1`, `BHA14-3`–`BHA14-5`；Eqs. (1)–(3), Fig.3, Fig.8, Conclusion / arXiv PDF pp.3–6, 11, 13。它是模型比较论文，引用的实验不是本轮新增或独立重测。 |
| 续接：`130Cs` primary experiment | Simons et al. 用 Euroball IV 扩展 bands A/B；Tables 1–2 记录能级、相对强度、multipolarity、DCO 和偏振。四条 interband links 的磁偶极/偏振证据被作者用于确认同宇称/组态。 | [Simons 2005 source page](../../knowledge/sources/simons-2005-130cs-chiral-structures.md#key-results)：`SIM05-1`–`SIM05-4`；Tables 1–2, Fig.1, Eqs. (2)–(3), PDF pp.3–7。直接实验事实与“chiral”模式解释分栏。 |
| 续接：`130Cs` 派生观测与竞争解释 | `S(I)` 在 I≈12 后大致平滑；`B(M1)/B(E2)` 与 in/out 比值有部分、但非全套 chiral-like staggering；band B 缺少预期的 `B(M1)/B(E2)` staggering。能级差在中自旋约 160 keV；I≈16–17 crossing 的 h11/2 neutron-pair 归因是作者/模型解释。论文没有 `130Cs` lifetime/absolute strengths，并要求寿命测量。 | [Simons 2005 source page](../../knowledge/sources/simons-2005-130cs-chiral-structures.md#key-results)：`SIM05-5`–`SIM05-7`；Figs.4–7、Conclusion / PDF pp.9–12。Bhat 2014 Ref. [32] 就是这组 Simons 数据，属于依赖性模型复用，不是第二次实验。 |
| 续接：`131Ce` 可测量的互带锚点 | AW13 Table 4.4 报告 `611.1-keV 17/2−→15/2−` M1/E2 link、relative intensity `25.2±1.1` 与表内角强度比 `R=0.56±0.02`，正文识别为 Band 4→Band 1；它没有直接测得该 link 的 `δ`、偏振或绝对强度。独立 lifetime papers 测量的是 Band-1-like/宇称序列，未形成 Band 4 partner 矩阵。 | [Alwaleedi 2013](../../knowledge/sources/alwaleedi-2013-band-structures-131ce.md#key-results)：`AW13-16`, `AW13-9`, `AW13-11`；[Singh 2016](../../knowledge/sources/singh-2016-lifetime-131ce-133pr.md#key-results)：`SI16-1`；[Li 2004](../../knowledge/sources/li-2004-lifetimes-131ce.md#key-results)：`LI04-1`, `LI04-11`。这些 lifetime controls 与 thesis γ 谱不是同一实验谱系，也不是 partner-resolved interband strengths。 |
| 续接：Hara Table 5 的后续 TPSM 覆盖 | 2024 TPSM 章节对 Hara 星号表的 `133La` 与 `135Pr` 做投影计算；Table 1 给定 `γ=36°`、`32°`，Figs.11–14 比较谱能、摇摆频率、对齐与跃迁比，作者分别归类为 longitudinal 与 transverse。固定形变为模型输入；并未覆盖其余五个表格候选或形成独立形状测量。 | [Sheikh et al. 2024 source page](../../knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md#key-results)：`SHJ24-3`–`SHJ24-8`；Table 1, Figs.11–14 / arXiv PDF pp.10,17–20。图中实验曲线沿用 Refs. [11]–[15]，不是新实验。 |
| 新增：奇中子 TPSM 基底扩展与 `131Xe` 对照 | Jehangir et al. 2022 将 odd-neutron 投影基底扩展至 `3ν` 和 `3ν+2π`，在 `N=3,4,5` 主壳中混合，并用能谱、signature、alignment、`J^(2)` 与 `Q_t` 比较 `117–131Xe`。`131Xe` 的 yrast 结果与旧数据比较；其 γ 参数为沿用输入，yrare 仍未观测；非正交投影振幅不是概率。Eq. (4) 将 `χ` 通过 HFB 自洽条件联系到输入 `ε`，但不把形变输入变成独立观测。 | [Jehangir et al. 2022 source page](../../knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md#key-results)：DOI [10.1103/PhysRevC.105.054310](https://doi.org/10.1103/PhysRevC.105.054310)，arXiv [2203.12851v1](https://arxiv.org/abs/2203.12851)；`JN22-1`, `JN22-2`, `JN22-3`, `JN22-4`, `JN22-5`, `JN22-6`, `JN22-8`, `JN22-10`, `JN22-11`, `JN22-13`；Eq. (1), Eqs. (2)–(8), Table I, Figs. 7–18 / PDF pp.4–15。官方 arXiv PDF SHA-256 `2c2d428aa5d82b8951d8f927bc11ccd9d30ed791fd55d488ea9cfcfb6372dea5`；主文已足以复核本节的方法、输入和限制，无需 SI。作者未报告新实验；Figure 7 数据来自 Ref. [52]–[54]。 |
| 新增原始实验：Banik et al. 2020 `131Xe` | `130Te(α,3n)` 38-MeV INGA 实验报告 72 条新放置跃迁，Table I 提供能级/相对强度/DCO/偏振和多极性；强度归一到 642.2-keV E2，不含 lifetime 或 absolute `B(E2)/B(M1)`。作者将 B1(a) 解释为 signature partner；B1(b) γ 侧带仍因内部跃迁弱而未闭合。 | [Banik et al. 2020 source page](../../knowledge/sources/banik-2020-131xe-multiple-band-structures.md#key-results)：DOI [10.1103/PhysRevC.101.044306](https://doi.org/10.1103/PhysRevC.101.044306)；`BNK20-1`–`BNK20-9`；Fig.3–4、Table I–II、Figs.14、17–20 / APS PDF pp.4–14。Publisher public URL 返回 PDF，SHA-256 `21e7e1eed7a93ffc3c38f4580fcf93863d02c56e40ffc900b1634df14c7f34e6`；OA-only 路线 `oa_not_found`，最终记录为 publisher-direct、非 OA；SI 未取。2023 Chakraborty 论文明确重分析同一数据；2022 TPSM Fig.7 也引用该数据。 |
| 跨模型 `131Xe` γ 参数角色比较 | 2020 TRS 对 B1 在中频给 `γ≈−26°` 模型极小；2022 TPSM Table I 沿用 `γ=29°` 输入；2023 TPRM 用 `γ=33°`、`ε₂=0.13` 复现 signature partners。绝对值差 3°/4°/7°，但各自是转频输出、继承输入和 rotor-fit 参数，不能平均。 | [Banik 2020](../../knowledge/sources/banik-2020-131xe-multiple-band-structures.md#key-results) `BNK20-6`；[Jehangir 2022](../../knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md#key-results) `JN22-4`,`JN22-12`；[Chakraborty 2023](../../knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md#key-results) `C23-4`,`C23-7`。三者共用/重用同一 INGA acquisition 的谱学约束；未给共同 convention/covariance，不构成独立 shape confirmation。 |
| 续接：Hara `137Nd (N=77)` 同核 triaxial model 案例 | Petrache 2020 的 JYFL `100Mo(40Ar,3n)137Nd` 数据建立 D3/D6 新带并连到 D2/D5；constrained CDFT 给 `β=0.20/0.21, γ=28.9°/29.5°`，PRM 使用 `γ=20.9°/23.5°`。这是现代同核 CDFT/PRM 应用，不是投影壳模型，也不是原 Hara 低能能级的逐项重算；D3/D6 很弱且无实验 `B(M1)/B(E2)`。 | [Petrache et al. 2020 source page](../../knowledge/sources/petrache-2020-137nd-multiple-chiral-bands.md#key-results)：`P20-1`, `P20-2`, `P20-3`, `P20-4`, `P20-5`；Fig.1, Table 1, Table 2, Fig.6 / PDF pp.2–9。它提供不同实验/模型案例；本续接未审计 Hara refs.70/72 与此 JYFL dataset 是否独立。 |
| 续接：2026 TPSM 文献访问边界 | Crossref 与 OpenAlex 核实到一篇 2026 年在线发表的 Rather–Bhat–Shah TPSM 论文；OpenAlex 标记 closed、无仓储全文。World Scientific DOI 页面返回 HTTP 403，精确题名 arXiv 搜索为 0，OA downloader 返回 `oa_not_found`。没有获取主文，未把摘要结论写成科学证据。 | DOI [`10.1142/S0218301326500448`](https://doi.org/10.1142/S0218301326500448)；[Crossref DOI work record](https://api.crossref.org/works/10.1142/S0218301326500448)；OpenAlex [`W7167921416`](https://openalex.org/W7167921416)；访问状态详见本日 [run receipt](20260929-DAY3-mean-field-nilsson-csm-hfb-projection-run-03/run.json) 的 `source_access_routes`。这些是来源身份/访问状态记录，不是全文证据。 |
| 新发现：`134La` 2026 NPA 论文访问边界 | Crossref 标题范围为 `128−134La`，可能覆盖 Hara 表中的 `134La (N=77)`；Crossref 无 abstract，OpenAlex 标 closed/no-repository，OpenAIRE 显示 CLOSED/no instance，arXiv 精确题名搜索为 0。Publisher linkinghub 返回的只是 HTML landing page；OA downloader `oa_not_found`，其 Crossref TDM license 不等于取得可读全文。题名范围仅是来源发现线索，未据此认定实际计算覆盖 `134La`。 | DOI [`10.1016/j.nuclphysa.2026.123419`](https://doi.org/10.1016/j.nuclphysa.2026.123419)；[Crossref record](https://api.crossref.org/works/10.1016/j.nuclphysa.2026.123419)；OpenAlex `W7155411427`；OpenAIRE publication record；访问 manifest `raw/papers/gpt/day3-mean-field-20260929/134la-tpsm-access/manifest.json`。只作为元数据/获取边界，不是科学内容证据。 |

**来源身份/访问：** Åberg, Flocard & Nazarewicz, *Annual Review of Nuclear and Particle Science* **40**(1), 439–528 (1990), DOI [`10.1146/annurev.ns.40.120190.002255`](https://doi.org/10.1146/annurev.ns.40.120190.002255)，本地原 PDF SHA-256 `90e3d1324dbf591cc042a3ad3b777a75e00af1463869d9ad557af433469562e6`；Hara & Sun, *International Journal of Modern Physics E* **4**(4), 637–785 (1995), DOI [`10.1142/S0218301395000250`](https://doi.org/10.1142/S0218301395000250)，citation key `HARA_1995`，本地原 PDF SHA-256 `13ca9edbd3092d2d3c4612e9d22b7cb1ff740d07f0f97c5f139ac901a7b26dac`。Crossref 分别核实题名、作者、年份、卷期与页码；两家出版商页面本轮均返回 HTTP 403。全文核对使用 Wiki 内哈希匹配的原 PDF，未用搜索摘要替代证据。

**续接来源身份/访问：** Bhat, Ali, Sheikh & Palit, *Nuclear Physics A* **922**, 150–162 (2014), DOI [`10.1016/j.nuclphysa.2013.12.006`](https://doi.org/10.1016/j.nuclphysa.2013.12.006)，arXiv [`1312.6963v1`](https://arxiv.org/abs/1312.6963)。Crossref 核对期刊元数据；OpenAlex 标记合法 green OA，Nature Downloader 以 `--no-si` 从 arXiv PDF 下载并验签。原文件保存在 `raw/papers/gpt/day3-mean-field-20260929/bhat-2014-tpsm-124-132cs.pdf`，SHA-256 `3d1e411d0dfad9d565aa5134d9ad75710a2cbb31607286f0bbc9c8b0537a9757`。本轮核对 arXiv v1，不宣称核对过出版社最终排版版。**续接 primary experiment：** Simons et al., *Journal of Physics G* **31**(7), 541–552 (2005), DOI [`10.1088/0954-3899/31/7/001`](https://doi.org/10.1088/0954-3899/31/7/001)。OpenAlex 标记 publisher OA；IOP PDF 直接下载并以 `%PDF` 签名和 SHA-256 核验，原件位于 `raw/papers/gpt/day3-mean-field-20260929/simons-2005-130cs-chiral-structures.pdf`，SHA-256 `da71d9f1c88421bc7d4421c87c4f1eb3f15043892a1ae821c62ab48cd5a611d6`。该实验是 Bhat Ref. [32] 的同一数据集，不能双计。

## Theory/analysis exercise


**练习：** 将群投影算符与投影后本征问题连起来，据此为 `131Ce` 选择一个“最小模型 → 升级模型 → 可观测检验”路线。

Hara–Sun 的角动量投影算符为

$$
\hat P^I_{MK}=\frac{2I+1}{8\pi^2}\int d\Omega\,D^{I*}_{MK}(\Omega)\hat R(\Omega),

$$
见 Eq. (2.7), PDF p.642。对单个 intrinsic state 定义

$$
H^I_{KK'}=\langle\Phi|\hat H\hat P^I_{KK'}|\Phi\rangle,\qquad N^I_{KK'}=\langle\Phi|\hat P^I_{KK'}|\Phi\rangle,

$$
并求解

$$
\sum_{K'}(H^I_{KK'}-E_I N^I_{KK'})F^I_{K'}=0,\qquad\sum_{KK'}F^{I*}_{K}N^I_{KK'}F^I_{K'}=1.

$$
Hamiltonian 与 norm kernel、广义本征方程和归一化见 Eqs. (2.19)–(2.20), PDF p.644。单态比值 `⟨Φ|H P^I|Φ⟩/⟨Φ|P^I|Φ⟩` 只是单一组态极限；多组态混合时需对非正交投影基对角化。三轴 intrinsic state 可让同一 `I` 出现多个 `K` 分量，轴对称单 `K` 情形则较简单。

| 路线 | 最小输入/能回答 | 不能单独回答 | 与当前观测的连接 |
|---|---|---|---|
| 约束 HF/HFB 或 Nilsson–Strutinsky | 给出 intrinsic density、配对与候选形变能面；自洽 HF/HFB 与 shell-correction 是互补路线。 | 不直接给唯一的实验 band identity、良好 `I` 能谱或模式指认；一个 `β₂/γ` 极小不等于测得形状。 | 用质量、低自旋能级、transfer、lifetime/`Q_t` 等约束静态输入和配对。 |
| Cranked mean field / CSM | 在旋转参考系跟踪 Routhian、alignment、crossing 与随频率的极小移动。 | 只凭拟合 `γ`、crossing 或 alignment 不能唯一反演形状，也不自动恢复良好角动量。 | `131Ce` 现有能级、signature 和 crossing 可先检验配置/对齐解释；需保留参考转动惯量、配对和组态截断依赖。 |
| AMP / PSM / TPSM | 投影 intrinsic Nilsson+BCS/HFB 组态到良好 `I`，在受限基中混合并预测能谱、signature 与电磁跃迁。 | 不能自动消除基底截断、有效算符/相互作用依赖；轴对称 PSM 失配不等价于实验三轴证据。 | 只有把 `B(E2)/B(M1)`、`g` 因子或伙伴带跃迁同实验比较，并对基底/配对/参数作敏感性检查，才可能提升解释力。 |

**练习结论：** 对 `131Ce` 先用 CSM/QTR 处理 crossing/alignment/signature 作为配置假设检验；只有当实验 band identity 和跃迁矩阵清楚后，再用投影配置混合比较实验室系能谱与跃迁。现有 `δ=0` 派生比值和缺少寿命/偏振/绝对强度的状态不足以裁定 `γ` 刚/软、wobbling、chirality 或 shape coexistence。这个路线是设计结论，没有生成代理数值或新实验结论。

### 定量映射练习：odd-neutron TPSM 的同中子素边界

用质量数关系核对 `131Xe`：`N=A−Z=131−54=77`。Hara Table 5 中同为 `N=77` 的三个 triaxial candidates 是 `134La`（57+77）、`135Ce`（58+77）和 `136Pr`（59+77）。Jehangir 2022 覆盖的 `117–131Xe` 链与这三个 Hara 核素的 exact-nucleus 交集为 `0/3`；它增加的是 odd-neutron TPSM 方法控制，不改变 direct TPSM 覆盖率 `2/7`。`131Xe` 的 `ε=0.160, ε′=0.090, γ=29°` 是 Table I 模型输入；不能由 yrast 拟合把该 γ 值升级成形状测量。Eq. (4) 用 HFB 自洽条件联系 QQ 强度 `χ` 与输入 `ε`，这并不提供新的形状测量。该文 `3ν+2π` 属五准粒子组态；它在投影非正交基中的幅度也不能当作通常概率。

用 Bhat et al. 2014 Eq. (3) 的近似转换式 `γ=arctan(ε′/ε)` 做数值一致性检查：`arctan(0.090/0.160)=29.3578°`，与 Jehangir Table I 的整数 `29°` 相符（[Jehangir source](../../knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md#key-results)：`JN22-14`；[Bhat source](../../knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md#key-results)：`BHA14-6`）。这只是形变参数之间的内部一致性，不是从能级或跃迁数据反演形状；Bhat `130,132Cs` 的表格/正文不匹配仍单独保留。

再用 Banik Table I 做相对强度的边界核算：642.2-keV `15/2−→11/2−` 线被设为 `100(6)`，177.1-keV `9/2−→11/2−` 线列为 `3.36(17)`，所以表内归一化强度商是 `3.36/100=0.0336`。两条线来自不同初始态，不能把这个值当作同一态分支比，更不能直接写成 `B(M1)/B(E2)` 或绝对强度；统计布居/feeding 和相对归一化都仍在其中（[Banik source](../../knowledge/sources/banik-2020-131xe-multiple-band-structures.md#key-results)：`BNK20-2`）。

再对非正交幅度做一个可复算的玩具范数演算。设两组归一化投影态重叠为 `s`、展开系数相同为 `c`，则 `1=⟨Ψ|Ψ⟩=2|c|²(1+s)`。取仅用于示范的 `s=0.5`，有 `|c|²=1/3`；两个系数模平方之和为 `2/3`，另 `1/3` 来自交叉项。这个数字不是 Jehangir 文中的拟合量，而是说明其 Fig. 8–10 的非正交基振幅为何不能当作独立概率（[source page](../../knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md#key-results)：`JN22-2`、`JN22-8`）。

### 131Xe 跨模型 γ 参数角色核对

| 方法/来源 | 表列/计算的 γ | 参数在模型中的角色 | 证据和依赖边界 |
|---|---:|---|---|
| 2020 Woods–Saxon Strutinsky TRS | `B1` 在 `ℏω=0.21–0.26 MeV` 时约 `−26°`；低频有 γ-soft 极小，高频出现双极小 | 频率依赖的能面极小，是模型输出；按原文 Lund convention | 使用 Banik 同一 INGA level scheme，非静态形状测量（BNK20-6） |
| 2022 odd-neutron TPSM | `29°`，输入 `ε=0.160, ε′=0.090` | 沿用文献的固定形变输入；`arctan(ε′/ε)=29.36°` 是约定下的表值一致性检查 | 不是本文拟合出来的形状；Fig. 7 比较 Banik 2020 数据（JN22-4, JN22-12, JN22-14） |
| 2023 TPRM | `33°`，`ε₂=0.13, ξ=1` | 用来再现 favor/unfavor signature partners 的转子模型参数 | C23 使用/重分析同一 Banik acquisition，不能作为独立形状测量（C23-4, C23-7） |

只看数值绝对值，差值为 `|29−26|=3°`、`|33−29|=4°`、`|33−26|=7°`。这不是可合并的三个独立形变值：一个是某转频下的 TRS 输出，一个是 TPSM 继承输入，另一个是 TPRM 选定参数；原文没有统一 convention/covariance，数据谱系也部分共享。数字接近可支持“不同表示都能描述同一谱学”这一模型一致性观察，不能当作三次独立 shape confirmation，也不增加 wobbling 证据权重。

### 续接定量核对：TPSM 参数与可观测量分层


Bhat 等 Table 1 (PDF p.4) 给 `130Cs` `ε=0.160, ε′=0.145`；同页 Eq. (3) 近似写作 `γ=tan⁻¹(ε′/ε)`。按该式复算，`130Cs` 为 `42.18°`，`132Cs` (`0.150/0.170`) 为 `41.42°`，而 `126Cs` (`0.150/0.260`) 为 `29.98°`。正文 PDF p.6 将所选非轴形变概述为约 `30°`；这与 `130,132Cs` 的印刷参数对不上。保留为 arXiv v1 的 source-internal parameter/wording mismatch，可能涉及近似或版本/参数约定，不能替作者更正，也不能把复算角度当作实验形状。Fig.3 (PDF p.6) 比较四个 Cs 核的 TPSM 与先前报告能级；Fig.8 (PDF p.11) 对 `130Cs` 显示 TPSM 计算的绝对 `B(E2)`、`B(M1)` 和 interband strengths，叠加的是 Ref. [32] 报告的 `B(M1)/B(E2)` ratios。结论说 `130Cs`/`132Cs` 的结果呈现 chiral-like 选择规则，但同时要求寿命测量；因此它只能支持相邻 odd–odd 核的模型可行性，不能替代 `131Ce` 的 absolute-strength 数据，也不能验证 Hara–Sun 的 `N=76–78` 案例。

### 续接定量映射练习：Hara Table 5 与现代 TPSM


按 Table 5 行标签的质子数 `Z` 与列标题中子数 `N` 做 `A=Z+N`，将七个星号格映射为核素：

| `Z` / 元素 | `N` | `A=Z+N` | 核素 | 2024 章节覆盖 |
|---|---:|---:|---|---|
| 57 La | 76 | 133 | `133La` | 是 |
| 57 La | 77 | 134 | `134La` | 否 |
| 58 Ce | 77 | 135 | `135Ce` | 否 |
| 59 Pr | 76 | 135 | `135Pr` | 是 |
| 59 Pr | 77 | 136 | `136Pr` | 否 |
| 59 Pr | 78 | 137 | `137Pr` | 否 |
| 60 Nd | 77 | 137 | `137Nd` | 否 |

2024 年章节明确计算其中 `2/7`（约 `28.6%`）个 Table 5 星号核素：`133La`、`135Pr`。它的 Table 1 使用 `133La: ε=0.150, ε′=0.110, γ=36°` 与 `135Pr: ε=0.160, ε′=0.100, γ=32°`。Figs. 11–14 依次比较已有 band energies / wobbling-frequency、rotational-frequency、aligned-angular-momentum 与 `B(E2)_out/B(E2)_in`、`B(M1)_out/B(E2)_in`。这个 `2/7` 仅表示该篇文章覆盖率，不表示后续文献总覆盖率；所列形变是输入，且图中实验数据由既有来源提供，因此不能当作 Hara 形状解释的独立验证。

### 续接数值核对：`137Nd` 的 HA γ 与 P20 PRM 输入

Hara Table 5 将 `137Nd` 标为 `N=77` triaxial candidate。P25 Figure 4f 对 `πh11/2²⊗νh11/2⁻¹`、`j=11/2,j′=10` 的 `137Nd` D5/D6 split 拟合为 paper-sector `γ=97.5°`；按本文 `120°−γ` 映射，常用 sector 值为 `22.5°`。P20 的 D5/D6 PRM 输入为 `23.5°`，相差 `1.0°`；P20 同页 CDFT 结果 `29.5°` 与其相差 `7.0°`。这些不是可相互平均的测量误差：P25 与 P20 使用不同模型、约定和拟合目的，而且 P25 Figure 4 Ref. [30] 重用同一 `137Nd` 能量数据。该面板有两个实心实验点和一个空心高自旋点，caption 说明空心点未参与拟合；`γ=97.5°` 未标统计 `±`。因此该拟合只能说明 HA 在所选低自旋 energy-splitting 点上给出一个三轴参数化，不说明该形状由独立 observable 测得，也不能作为 Hara 轴对称 PSM 未拟合的直接复核。P25 没有展示 `137Nd` measured `B(M1)/B(E2)` 对照。

### 定量适用性核查：`137Nd` 的 HA 临界自旋

按 P25 Eqs. (2),(7) 用 panel-f 参数 `γ=97.5°`, `j=11/2`, `j′=10` 计算。由 `J_k/J_0=sin²(γ−2πk/3)` 得 `(J_1,J_2,J_3)/J_0≈(0.14645,0.37059,0.98296)`；把 `A_k=1/(2J_k)` 代入 Eq. (7)，`J_0` 尺度约掉，得到 `I_c≈17.804ℏ`。Figure 4f 归一化参考点 `I_0=16.5ℏ`，下一个填充数据点 `I=17.5ℏ` 在此模型估值之下，空心 `I=18.5ℏ` 点在其上且未参与拟合。这个一致性提示 HA 有效域可能解释该筛点，但原作者没有把排除理由明确归因于 `I_c`，所以仅记为 Codex model-validity cross-check，不当成作者结论或测得临界自旋。

### 续接最小实验设计：从 `131Ce` 的 611.1-keV link 起步

这个设计以已发表、可定位的 Band 4→Band 1 link 为入口，不预设 Band 4 是 wobbling 或 chiral partner。详细 design row 已固化在 [131Ce/133Ce project](../../knowledge/projects/131ce-collective-mode-discrimination.md)。| 顺序 | 观测/分析包 | 判别作用 | 停止或降级条件 |
|---|---|---|---|
| 1 | 先确认 `611.1 keV, 17/2−→15/2−` 的 gate、级联两端、parity 与 Band-4→Band-1 linking；把其它候选 ΔI=1 links 同样放进 transition manifest。 | 防止把一个 feeding/link 标签直接升级成集体带身份。 | 若多级联、门控或 band identity 不闭合，记 `identity-uncertain`，不计算 wobbling label。 |
| 2 | 对已确认 interband links 联合测角分布/DCO 与线偏振，拟合 `δ` 的 branch/sign、response 和 covariance；对照 Band-1 intraband reference。 | E2-rich 互带模式保留 collective-mode 候选；稳定的 M1-dominant links 会降低 wobbling/chirality 优先级，更符合普通 signature/configuration link。 | 不把表内 `R=0.56` 当成 `δ`，也不沿用 AW13 的 `δ=0` 假设；偏振只用正负号、没有响应/幅度和 branch fit 不足以选解。 |
| 3 | 获取 Band 4 partner states 的寿命与分支，同时选取相同自旋区的 Band 1 状态，重建 absolute `B(E2)`/`B(M1)`、out/in ratios 与 `Q_t`；显式拟合 feeding/side-feeding。 | 让 `E_wob(I)` 与 E2 collectivity、M1 admixture 在相同 spin/身份下交叉检查；与已有 Singh/Li Band-1-like lifetimes 作独立 control，不按论文数合并。 | 若只有 intensity-derived ratios 或 feeding 未约束，不称 absolute-strength confirmation；limits/effective lifetimes 与 finite points 分开。 |
| 4 | 只有当前三步后 γ-soft/rigid 仍决定结论时，再加 quadrupole invariants/Coulomb excitation 或 common-input softness scan。 | 评估形状动力学，不替代 partner identity 与电磁 wobbling/chiral 判据。 | 固定 TRS/TPSM `γ` 参数不能当作测得形状。 |**数值敏感度：** AW13-9 对同分支给出 `r_B(δ)=r_B(0)/(1+δ²)`，其中 `r_B=B(M1)/B(E2)`。假设 `|δ|=0.5,1.0,1.5`，相对 δ=0 值分别为 `0.800,0.500,0.308`；这些是测量敏感度示例，不是 611.1-keV 的拟合结果。δ=1 时，采用 δ=0 会把该分支的派生比值报成正确修正值的两倍，因此把 direct δ/偏振排在伙伴寿命之前能避免错误 strength ranking。**反证/独立性：** 611.1-keV link 和 `δ=0` 派生比值都来自 Alwaleedi thesis 同一 `100Mo(36S,5n)131Ce` 谱系；Li 2004 与 Singh 2016 的 lifetime measurements 来自另两条反应谱系，但只覆盖 yrast/parity sequences，并没有 Band 4 的 partner lifetime。新测量需以共同的 detector response、feeding 和 transition matrix 重建，把这些旧数据作为带标识的控制值，而不是拼成一条伪独立证据链。

### 续接定量判据：136Pr Q1 的 875.6-keV 连线


Table I 与正文给出该 link 的 R_DCO=0.47(8)；表注说明以拉伸四极跃迁作 gate 时，偶极标定约为 0.46。暂把 0.46 当作固定中心、忽略其标定不确定度，归一化残差为 (0.47−0.46)/0.08=0.125σ，故该测量与偶极跃迁相容。这个数值只支持 multipolarity，不决定宇称。作者报告线偏振受相对强度 2.9(2) 和污染影响而无定论，因此 Q1 的正宇称仍是 TAC-CDFT 辅助的模型指派。最小设计应先降低污染并增加该连线的偏振统计，再用邻带连接闭合宇称。

### 续接定量核对：137Pr 的 B(M1)/B(E2) 派生值与带交叉


Agarwal et al. 的正文公式为 R=0.697·Iγ(M1)·Eγ(E2)^5/[Iγ(E2)·Eγ(M1)^3]，能量以 MeV 代入，并假设 δ² 可忽略。用 Table I 中 29/2− 态的 321.0(1)-keV M1，Iγ=50.9(17)，与 432.6(4)-keV E2，Iγ=1.6(3)，复算得 R≈10.16。忽略能量误差、只传播相对强度误差得约 10.16(1.93)，与表列 10.4(1.9) 相符。以表列值比较 37/2− 的 62.1(12.0) 与 41/2− 的 17.2(2.9)，比值下降约 3.61 倍；若暂把两误差视作独立，差值约 3.6σ。此重算复现的是作者的 branch-derived ratio，不构成绝对跃迁强度或独立 band-crossing 证明。

## Counter-evidence and missing companion observables


- Jehangir et al. 2022 的 Fig. 7 用已发表的 `131Xe` 数据 Ref. [52]–[54]；Ref. [53] 是 Banik et al. 2020, PRC 101, 044306。Chakraborty et al. 2023 第 II 节说明其 `131Xe` 研究重分析该 Banik 数据（2023 PDF p.2, Ref. [22]），所以存在共享实验谱系；TPSM 能谱比较不是独立实验确认。2023 分析的连接跃迁小 E2 成分及 M1 主导解释，将新序列归为 signature partner，未报告 wobbling 信号（[Chakraborty et al. 2023 source page](../../knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md#key-results)：`C23-2`、`C23-3`、`C23-7`）。
- Banik et al. 2020 的 `B1(b)` 只通过若干衰变线连到 `B1`；作者明确说因内部跃迁太弱，不能判断是否 γ band，也无法计算关键的 inter-/intraband strength ratio。B1/B4 的 γ-soft 或三轴结论由 signature/alignment 趋势和 TRS 计算共同支撑，后者是 Woods–Saxon Strutinsky 模型输出，不是独立形变测量（[Banik source page](../../knowledge/sources/banik-2020-131xe-multiple-band-structures.md#key-results)：`BNK20-4`、`BNK20-6`、`BNK20-7`、`BNK20-9`）。
- **同数据带标签边界：** Banik 2020 把高自旋 B1(a) 叫作 signature partner；Chakraborty 2023 则说旧研究尚未识别 unfavored partner，重分析后偏向低自旋 yrare `13/2−` 序列，并留下 yrast `13/2−` 起源开放（[Banik](../../knowledge/sources/banik-2020-131xe-multiple-band-structures.md#key-results) `BNK20-10`; [Chakraborty](../../knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md#key-results) `C23-6`）。两文共享一个 acquisition；B1(a)、B5 与 C23 序列的逐跃迁标签映射仍未在本轮闭合。
- 对 odd-neutron TPSM 的未观测 yrare 带，应以逐带 g-factor、partner-resolved lifetime/绝对 `B(E2)`、`B(M1)` 和可追踪的带间连接检验质子/中子组态及跃迁预测。对 `131Ce`，这些量仍需来自目标核本身；`131Xe` 同中子素类比不能补齐 N=73 的实验缺项。
- 137Pr TAC 的高自旋 5qp 曲线能重现部分趋势，却比测量偏高约 2.2 MeV、约 2ℏ，且更高自旋拟合不完整；不能用计算曲线单独确认跨带组态。
- B(M1)/B(E2) 对 δ²≈0 和弱 E2 分支强度敏感，弱跃迁还采用多门控谱平均；现有文章未给 band-resolved absolute lifetime。要区分构型交叉与 shears closing，需要同自旋区绝对寿命、feeding 控制和绝对强度。
- INGA 是本篇的新 coincidence 数据集；作者将相对强度与 Xu 1989 比较，沿用了先前低能自旋赋值。跨论文综合时需保留共享核素背景，不按文章数重复计权。
- 新的 136Pr 模型对比本身有反向约束：D1 的计算 B(M1)/B(E2) 高于实验派生值，D2 的计算值显著低于实验，D5 没有匹配 TAC-CDFT 组态；作者转用 SN100PN 解释其中部分低能态，明确显示不同方法的适用范围不相同。
- 136Pr 的 875.6-keV Q1→Q2 link 的 R_DCO=0.47(8) 与偶极标定相符，但 Q1 宇称仍未由偏振测量确定；该线相对强度 2.9(2)，且有污染。需要更高统计、可控污染的偏振/角关联约束。
- D4/D6 在 TAC-CDFT 结果与替代形状共存解释之间尚未闭合；需要逐带寿命、绝对 B(E2)/B(M1) 或 Qt 和独立形状敏感量，不能只用 Table II 的模型形变判决。
- 2025 JUROGAM II 观测是相对此前 136Pr 实验增加统计的新数据集；它改善了旧能级图，但同文 TAC-CDFT 与实验曲线来自同一新数据，不能按实验与模型重复计为两条独立观测。D4/D6 作者解释仍是竞争解释，不是独立形状证据。
- 对“轴对称计算失败即证明三轴”的反证是原作者自己的边界：Table 5 的七个 `N=76–78` 星号是暂定模型标签，p.713 要待三轴投影验证；该表给 `131Ce (Z=58,N=73)` 的是模型 prolate `+0.22`，不在这些星号内。未来的现代投影计算或不同配对/组态空间若拟合同一数据而不需三轴，将削弱历史解释。
- Hara–Sun p.712 说明 doubly-odd level density 约为 odd-mass 核的十倍，不同配置在低能区可有近似相等的波函数权重；shell filling 与选取组态会显著影响结果。这使“轴对称拟合差”也可能受模型空间/组态敏感性影响。
- 粒子数投影的 `156Er` 方法学反例是数量级/方向上的，而非 `131Ce` 实验证据：投影能改变 backbending，但最低受污染 `qp`-pair 态更靠近 yrast；有限空间里 spurious 态不会因增加投影而必然自动消失。
- 对 `131Ce` 集体模式必须补的伴随量仍是目标跃迁的 measured `δ` 与偏振、伙伴带分别解析的 lifetime 和 absolute `B(E2)/B(M1)`/`Q_t`、可靠 interband links 与 band identity；若使用形状解释，还需独立形变敏感 observable。邻核模型值不能代替目标核测量。
- **证据独立性：** 两篇理论综述不是两次独立实验；Hara–Sun 的 Table 5 汇总早期 A≈130 实验与模型比较，本轮未回到其 refs.70/72 的原始实验逐项审计。Alwaleedi 的 Band/crossing 与 `δ=0` 比值属于一个目标核数据集；其派生值不能按 observable 行数重复计权。
- Bhat TPSM 控制进一步显示：`130Cs` 的绝对 `B(E2)`/`B(M1)` 图是计算，已测输入主要是文献报告的能级和 intensity-derived `B(M1)/B(E2)` 比值；该论文明确要求对 `130Cs` 等核做 lifetime measurements。它不能作为绝对跃迁强度的独立实验支持，更不能跨核填补 `131Ce`。
- Simons 2005 primary experiment 确认了四条带间 link 的 DCO/偏振与 M1 character；同一数据集的 band-B ratio 没有预期 staggering，绝对 lifetime 仍缺。这既支持 same-parity band link，也限制静态 chirality 的强结论；Bhat 2014 Ref. [32] 重用该 Euroball 数据，不是第二项实验。
- Bhat arXiv v1 的 Eq. (3)+Table 1 数值复算与其 PDF p.6 “γ≈30°”概述不一致。此处保留 `needs_review`，不据此替作者指定 γ，也不把形状参数当实验测量。
- Budaca & Budaca 2025 对 `137Nd` 的 `γ=97.5°` fit 来自 P20 Ref. [30] 的同一 energy-splitting 数据；figure 只纳入很少的低自旋点，`γ` 未列统计误差。它与 P20 PRM `γ=23.5°` 的接近是同源理论交叉检查，不是独立 triaxial measurement；Fig. 5 未提供 `137Nd` measured `B(M1)/B(E2)` 对照。
- Budaca & Budaca 2025 的 `137Nd` γ fit 仅使用 P20 Ref. [30] 的同一 D5/D6 energy-splitting dataset；Fig.4 的 137Nd panel 只有两个实心拟合点，另有一个高自旋空心点被排除，且未显示 gamma error bar。它不能作为独立 `γ` measurement；P20 中 D5 有 ratio 数据而弱 D6 缺 `B(M1)/B(E2)`，P25 本文没有作 `137Nd` transition-ratio comparison。
- **必要伴随观测（`137Nd` 对照）：** 要检验 P25 的 chiral-vibration interpretation，需为伙伴 D5/D6 补齐绝对 lifetime/`B(E2)`、`B(M1)/B(E2)` 与 same-spin interband strengths；只拟合 `ΔE(I)` 的模型参数不闭合电磁判据。此对照仍属邻核模型问题，不能转为 `131Ce` 证据。
- Sheikh et al. 2024 的 `133La`/`135Pr` TPSM 曲线引用或比较了更早实验，不产生新的谱学观测；其中 `135Pr` 的 wobbling 指认仍受独立实验反证：Lv et al. 2022 的 JUROGAM II 数据对关键 link 给出小 `|δ|`、以 M1 为主的解（[Lv 2022 source page](../../knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md#key-results)：`L22-4`, `L22-5`），同时提供独立的 γ-soft IBFM 解释（[Nomura 2022 source page](../../knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md#key-results)：`NOM22-2`–`NOM22-12`）。
- **伴随观测边界：** 后续模型对这些核素的判别若要从能量趋势提升到结构结论，仍需逐带/跃迁身份、`δ` 与偏振、partner-resolved lifetimes 和绝对 `B(E2)/B(M1)`；只有 `E_wob` 或固定 `γ` 输入不能独立识别集体模式。对 `131Ce` 仍优先缺目标带同口径的上述测量。
- 对 `131Ce`，AW13-16 的 611.1-keV 互带 line 是可测量入口，但 `R=0.56±0.02` 是其表内 angular ratio，不是 mixing ratio `δ`；Band 1 已有的 SI16/LI04 lifetimes 也不等于 Band 4 partner lifetime。AW13-9 的 δ 修正例子显示 `δ=0` 的派生 `B(M1)/B(E2)` 可能变动很大，只有直接 branch-resolved `δ` 和 common-response strength matrix 才能闭合。
- 2026 年 DOI 候选的全文未取得；此处只记录 Crossref/OpenAlex 书目与访问结果，不把数据库摘要当作反证、支持证据或计算结果。

## Knowledge Impact and Learning Decision


新增的 137Pr full text 将 Hara N=78 候选从“模型覆盖未明”修订为“已有 2007 INGA M1-band 实验和 hybrid TAC 3qp/5qp 比较；没有直接 PSM/TPSM 投影全文”。M1/DCO/IPDCO 与 weak E2 支持作者的磁转动解释；强度比的混合比假设和高自旋 TAC 偏移限制唯一性。该论文中的 gamma≈58° 是模型解，不是对 Hara 形状标签的独立测量。本次续接将 Hara N=77 的 136Pr 从“直接模型覆盖未知”修订为“已找到同核 2025 TAC-CDFT/壳模型全文和新实验谱，但没有角动量投影”。这支持继续以投影路线检验历史候选，同时限制把自洽形变、正宇称配置或 D4/D6 形状共存当成测量结论。D1/D2 ratio 残差、pairing collapse 和 D5 TAC 失配均纳入模型选择边界。**决定：`revises` 后续模型覆盖图与实验优先级，`supports` 两个具体核素上的 TPSM 应用，并 `limits` 将同核/邻核模型输出当成 Hara 预测的独立验证或迁移到 `131Ce`。** Hara–Sun Table 5 七个星号核素已逐格映射；2024 章节在 `133La`、`135Pr` 有 TPSM 计算；Petrache 2020 给 `137Nd` CDFT/PRM 模型，Budaca 2025 再用 HA 拟合同一 P20 D5/D6 energy-splitting 数据，但不是 PSM/TPSM 重算也不是独立实验。NPA 2026 的 `134La` title-range 仍只有 closed metadata。对 `131Ce` 的设计锚定在 AW13-16 的 611.1-keV Band-4→Band-1 candidate link：先定身份和 `δ`/偏振 branch，再补同自旋伙伴寿命与 absolute strength。它不改变当前模式排序，普通 signature/configuration coupling 仍为首选，γ-soft 为模型辅助背景，目标核 wobbling/chirality 尚无闭合电磁链。

2022 odd-neutron TPSM 作为方法控制支持“增加投影多准粒子组态可检验高自旋对齐/crossing”的建模路线，但限制任何把 `131Xe` `γ=29°`、拟合能谱或非正交组态振幅直接解释为实验形状/概率的做法。`131Xe` 与 Hara N=77 候选只有同中子数，没有 exact-nucleus 重叠。数据谱系核对发现 TPSM Fig. 7 引用的 Banik 2020 `131Xe` 数据被 Chakraborty 2023 重新分析；后者的小 E2/M1 主导结果支持 signature-partner 竞争解释、限制 wobbling 指认，但不是第二套独立实验。总体学习决策：`supports` odd-neutron projected-basis 扩展作为模型工具，`limits` 把模型输入和重用谱学误作独立测量，`revises` 的是方法控制与来源依赖地图；Hara direct TPSM 覆盖仍为 `2/7`，`131Ce` 排序不变。

追到 Banik 2020 原始谱学后，实验层可具体写成：72 条新置跃迁及 Table I 的相对强度、DCO、偏振和多极性；作者将 B1(a) 作为 signature-partner、把 B1(b) 留为未定 γ-sideband。实验没有绝对寿命/强度，B1/B4 的 γ-soft/TRS 形状演化属于模型结果。它 `supports` 能带/跃迁结构与有限的 signature 解释，`limits` wobbling/γ-band/刚性三轴形状的强结论；2023 对同一 acquisition 的 reanalysis 增加判别解释，不增加独立实验权重。

跨模型参数复核将 Banik TRS 的 `γ≈−26°`（特定转频的能面输出）、Jehangir TPSM 的 `29°`（继承输入）和 Chakraborty TPRM 的 `33°`（再现 signature partner 的模型参数）分开。绝对值相差 `3°/4°/7°`，没有共同协方差或统一配置/观测条件，不能平均，也不构成三条独立形状证据；它只支持不同模型可以描述相近的三轴参数区间，且依赖同一 acquisition 的谱学资料。另保留 band-label 张力：Banik 将高自旋 B1(a) 叫作 signature partner，C23 表示早先未识别 unfavored partner、重分析后偏向低自旋 yrare `13/2−`，并称 yrast `13/2−` 起源仍开放；本轮没有把 B1(a)、B5 与 C23 序列强行视为同一带（BNK20-10; C23-6）。

这次 TRS 案例同时加深了 Day 3 的模型分层：TRS 对固定组态下的转频形变能面找极小，HFB 自洽关系约束的是 TPSM 哈密顿量的 `χ–ε` 关系，而角动量投影是在实验室系恢复良好 `I` 并混合投影态；三者输出不同，不能互相替代。

## Durable knowledge delta

- 追到 primary Banik et al. 2020 后，`131Xe` 方法比较现在有明确的“单次 INGA acquisition → 2022 TPSM energy comparison → 2023 same-data reanalysis”谱系：实验有 72 条新置线及 DCO/偏振，但无绝对寿命/强度；2023 更细的 signature-partner 解释不是另一份实验采集。这补全了伴随观测与来源独立性边界，不改变 Hara 投影计数 `2/7` 或 `131Ce` 排序。
- 新建 [Banik et al. 2020 `131Xe` source page](../../knowledge/sources/banik-2020-131xe-multiple-band-structures.md#key-results)，记录 38-MeV INGA 原始实验、72 条新置线、Table I 的相对强度/DCO/偏振、B1(a)/B1(b) 判据、缺寿命/绝对强度、`B1`/`B4` 频率依赖 TRS 模型边界，以及 B1(a)/B5 与 C23 低自旋 partner 解释的 unresolved label crosswalk；claims 均 `needs_review: true`，来源哈希和 publisher-direct 访问状态已记 manifest。
- 更新 [TPSM model page](../../knowledge/models/triaxial-projected-shell-model.md#odd-neutron-tpsm-basis-extension-and-n77-transfer-boundary-2026-09-30)、[A≈130 model-choice card](../../knowledge/projects/a130-model-choice-card.md#odd-neutron-tpsm-basis-extension-control) 和 [`knowledge/index.md`](../../knowledge/index.md)：把 Banik 原始实验、2022 TPSM 比较与 2023 重分析连为同一 INGA acquisition lineage；将 DCO/偏振、相对强度和 missing lifetime/absolute-strength 分层，未改动已有人审的 `131Xe` 核素页与 2023 source 页。
- 新建 [Jehangir et al. 2022 odd-neutron TPSM source page](../../knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md#key-results)，保存 `3ν/3ν+2π` 五准粒子基底、N=3–5 主壳、HFB 自洽条件对 QQ 强度 `χ` 的约束、`131Xe` Table I 输入、未观测 yrare 带、非正交振幅限制，以及与 Chakraborty 2023/Banik 2020 的共享实验谱系复核；source claims 保持 `needs_review: true`。
- 更新 [TPSM model page](../../knowledge/models/triaxial-projected-shell-model.md#odd-neutron-tpsm-basis-extension-and-n77-transfer-boundary-2026-09-30)、[A≈130 model-choice card](../../knowledge/projects/a130-model-choice-card.md#odd-neutron-tpsm-basis-extension-control) 和 [`knowledge/index.md`](../../knowledge/index.md)：将 `131Xe` 归为 N=77 方法控制，不计作 Hara Table 5 direct TPSM 覆盖；保存 `ε/ε′→γ` 的参数一致性核算和非正交范数玩具推导，保留 `2/7` 计数、输入形变/预测边界与数据复用关系，不修改已 human-reviewed 的 `131Xe` 页面或 `131Ce` 模式排序。
- 在 [A≈130 model-choice card](../../knowledge/projects/a130-model-choice-card.md) 的 `131Xe cross-model γ parameter role check (2026-09-30)` 保存 TRS 输出、TPSM 继承输入、TPRM 拟合参数的角色对照及 `3°/4°/7°` pairwise arithmetic；明确不同模型/转频/数据谱系不可平均，不能视作独立 shape confirmation。
- 更新 [Cranked Shell Model page](../../knowledge/models/cranked-shell-model.md#131xe-woods-saxon-trs-频率演化-2026-09-30) 与 [A≈130 model-choice card](../../knowledge/projects/a130-model-choice-card.md)：加入 Woods–Saxon/Strutinsky `131Xe` TRS 的低频 γ-soft、中频三轴、高频多极小及 `B4/B4(a)` 宽谷例子；把 TRS 能面输出从 CNS、HFB 和投影模型输入中分开。
- 修订 [knowledge/questions.md](../../knowledge/questions.md) 中既有 `131Xe` “γ-soft 还是稳定 γ 局域”开放问题：写入 TRS/TPSM/TPRM 参数角色、共享 INGA 数据谱系和 g-factor/寿命/绝对跃迁强度缺口；问题继续保持开放。
- 补充 [knowledge/questions.md](../../knowledge/questions.md) 中既有 `131Xe` yrast `13/2−` 组态问题：BNK20-11 记录 Banik 对 B5 的 decoupled-band 解释，C23-6 记录同数据重分析认为 yrast 起源仍开放、yrare `13/2−` 更适合作 unfavored partner；来源间逐跃迁标签映射仍未决。
- 同步修订 `knowledge/questions.md` 中既有 `131Xe` yrast `13/2−` 起始组态问题，记录 Banik B5 的 decoupled-band 解释与 C23 同数据重分析的 yrast/yrare 选择差异；精确序列映射和 partner-resolved strengths 仍作为开放问题。


- 新建 knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md 与 knowledge/nuclei/137pr.md；记录新 INGA 能级图、DCO/IPDCO 与 crossover E2、delta-squared≈0 ratio 假设、3qp/5qp TAC 参数、模型偏移和 Hara N=78 映射。
- 更新 knowledge/projects/a130-model-choice-card.md、knowledge/models/tilted-axis-cranking.md 与 knowledge/index.md：137Pr 有同核 TAC 模型应用，但不计为 PSM/TPSM 投影覆盖；模型 gamma 和 band-crossing 解释仍受实验强度与能量偏差边界约束。
- 新建知识源页 knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md 与核素页 knowledge/nuclei/136pr.md；将新 JUROGAM II 能级纲图、875.6-keV link 的 DCO/偏振边界、PC-PK1 TAC-CDFT 与壳模型输出、D1/D2 强度残差和 D4/D6 竞争解释写入长期知识。
- 更新 knowledge/models/tilted-axis-cranking.md、knowledge/models/covariant-density-functional-theory.md、knowledge/projects/a130-model-choice-card.md 与 knowledge/index.md：把 136Pr 记录为直接 TAC-CDFT/壳模型应用，但不计作 PSM/TPSM 角动量投影覆盖；所有页面维持 unreviewed。
- 更新 [A≈130 high-spin model-choice card](../../knowledge/projects/a130-model-choice-card.md#theoryanalysis-exercise)：新增 Eq. (2.7)、Eqs. (2.19)–(2.20) 的投影核重构和基于原文 Figs.26–27 的有限空间反例；同时明确 Hara Table 5 的 N=76–78 triaxial candidate 不适用于 N=73 `131Ce`。这是可复用的模型输入/输出、计算式与迁移边界，review 状态仍是 `unreviewed`。
- 在 [131Ce/133Ce project](../../knowledge/projects/131ce-collective-mode-discrimination.md#related-sources-and-pages) 增加模型卡回链与 `N=76–78`→`131Ce N=73` 迁移边界；没有改变原有模式排序或 review 状态。
- 新增 [Bhat et al. 2014 TPSM source](../../knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md#key-results) 和 [TPSM model page](../../knowledge/models/triaxial-projected-shell-model.md#known-limitations) 关系；保存 `130Cs` 绝对强度是模型量、相对比值来自既有引用数据，以及 `ε/ε′→γ` arXiv-v1 参数边界。
- 将该源接入 [A≈130 model-choice card](../../knowledge/projects/a130-model-choice-card.md#model-to-observable-locator-crosswalk) 与 [`knowledge/index.md`](../../knowledge/index.md)。本次涉及的 knowledge pages 均维持 `unreviewed`，未更改 `131Ce` 模式排序。
- 更新 [Hara–Sun source page](../../knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md#key-results)：将 Table 5 七个带星号核素和 `N=76–78` 端点/中间核素说明固化在 `HS10-4`，原有 `needs_review: true` 保持不变。
- 新建 [Sheikh et al. 2024 TPSM source page](../../knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md#key-results)：记录投影方法、`133La/135Pr` Table 1 输入、Figs.11–14 比较和实验数据依赖；页面与所有新 claims 保持 `unreviewed` / `needs_review: true`。
- 新建 [Budaca & Budaca 2025 source page](../../knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md#key-results)，并更新 [triaxial particle-rotor model page](../../knowledge/models/triaxial-particle-rotor-model.md)：记录 HA 的 `I_c/R_I` 适用边界、`137Nd` `γ=97.5°→22.5°` 轴 sector 换算和 P20 Ref. [30] 同数据谱系。按 Eqs. (2),(7) 得 model `I_c≈17.804ℏ`，与一个填充点/一个排除点的 Fig.4f selection 相符但不视为作者排除原因或测量。Source claims 保持 `needs_review: true`。
- 更新 [A≈130 model-choice card](../../knowledge/projects/a130-model-choice-card.md)：将 `137Nd` P20 CDFT/PRM 和 P25 harmonic-PRM-type fit 与 2024 `133La/135Pr` TPSM 作为不同模型层级，澄清它们不是 Hara axial-PSM 的直接复算或独立实验形状证据；将 Budaca 2025 source 接入 [`knowledge/index.md`](../../knowledge/index.md)。未改变 `131Ce` 假设排序或人工 review 状态。
- 更新 [TPSM model page](../../knowledge/models/triaxial-projected-shell-model.md)、[A≈130 model-choice card](../../knowledge/projects/a130-model-choice-card.md) 和 [131Ce project](../../knowledge/projects/131ce-collective-mode-discrimination.md#related-sources-and-pages)，加入两项后续模型覆盖及其非独立形状证据边界；更新 [`knowledge/index.md`](../../knowledge/index.md) 的 source 入口。没有改变 `131Ce` 排序或人工 review 状态。
- 更新 [131Ce/133Ce project](../../knowledge/projects/131ce-collective-mode-discrimination.md)：以 AW13-16 `611.1-keV Band 4→Band 1` link 具体化 δ/偏振→伙伴寿命/绝对强度的实验设计，并将 AW13-9 的 `δ=0` 比值修正量化为纯敏感度例子；不加入拟合数据或改变模式排名，page review status 保持原样。
- 更新 [A≈130 model-choice card](../../knowledge/projects/a130-model-choice-card.md)：将 [[petrache-2020-137nd-multiple-chiral-bands]] 的 `137Nd` CDFT/PRM D2/D3、D5/D6 案例单列为同核模型对照，同时标清其不同于 TPSM/Hara 旧谱重算及 D3/D6 `B(M1)/B(E2)` 缺口。
- 新增 [Simons 2005 primary `130Cs` experiment](../../knowledge/sources/simons-2005-130cs-chiral-structures.md#key-results)，并回链到 Bhat Ref. [32]、TPSM model、model-choice card 和索引；核实两篇论文共享同一 Euroball experiment，不重复计权。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/projects/a130-model-choice-card.md",
      "summary": "补入 Hara–Sun 投影算符及 Hamiltonian/norm kernels 的广义本征练习；将单态能量比值限定到单组态极限；用 Fig.26–27 细化粒子数投影与截断态污染边界，并隔离 Table 5 N=76–78 标签与 N=73 131Ce。",
      "anchor": "Day 3 kernel reconstruction and applicability check (2026-09-29)",
      "sources": [
        {
          "path": "knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md",
          "locator": "HS10-1"
        },
        {
          "path": "knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md",
          "locator": "HS10-4"
        },
        {
          "path": "knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md",
          "locator": "HS10-5"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-12"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-13"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-14"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/131ce-collective-mode-discrimination.md",
      "summary": "链接 131Ce project 到 Day 3 模型选择卡，并隔离 Hara–Sun N=76–78 历史候选与 131Ce N=73 的适用边界；不改竞争解释排序。",
      "anchor": "Day 3 model-route link (2026-09-29)",
      "sources": [
        {
          "path": "knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md",
          "locator": "HS10-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md",
      "summary": "新建 Bhat 2014 TPSM source record，分开 Cs 能级比较、130Cs 绝对跃迁强度模型量和引用的强度比值；记录 Table 1/Eq.3 参数映射不一致。",
      "anchor": "Key Results",
      "sources": [
        {
          "path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md",
          "locator": "BHA14-1"
        },
        {
          "path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md",
          "locator": "BHA14-2"
        },
        {
          "path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md",
          "locator": "BHA14-3"
        },
        {
          "path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md",
          "locator": "BHA14-4"
        },
        {
          "path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md",
          "locator": "BHA14-5"
        },
        {
          "path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md",
          "locator": "BHA14-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/models/triaxial-projected-shell-model.md",
      "summary": "链接 A≈130 Cs TPSM 方法案例和 absolute-strength/neighbor-transfer 边界；保留 arXiv v1 参数映射不确定性。",
      "anchor": "Bhat et al. 2014: A≈130 odd–odd transfer boundary",
      "sources": [
        {
          "path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md",
          "locator": "BHA14-1"
        },
        {
          "path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md",
          "locator": "BHA14-4"
        },
        {
          "path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md",
          "locator": "BHA14-5"
        },
        {
          "path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md",
          "locator": "BHA14-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-model-choice-card.md",
      "summary": "把 130Cs TPSM 与实验数据层级作为邻核方法控制加入模型选择矩阵，不转移到 131Ce。",
      "anchor": "A≈130 odd–odd TPSM transfer control",
      "sources": [
        {
          "path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md",
          "locator": "BHA14-3"
        },
        {
          "path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md",
          "locator": "BHA14-4"
        },
        {
          "path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md",
          "locator": "BHA14-5"
        },
        {
          "path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md",
          "locator": "BHA14-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "索引 Bhat 2014 A≈130 Cs TPSM 模型比较来源及其未闭合的 lifetime/parameter boundary。",
      "anchor": "[[bhat-2014-tpsm-cs-doublet-bands]]",
      "sources": [
        {
          "path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md",
          "locator": "BHA14-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md",
      "summary": "把 Bhat Ref. [32] 精确回链到 Simons 2005 primary Euroball source，标记 TPSM ratio comparison 与原实验属同一数据谱系。",
      "anchor": "[[simons-2005-130cs-chiral-structures]]",
      "sources": [
        {
          "path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md",
          "locator": "BHA14-4"
        },
        {
          "path": "knowledge/sources/simons-2005-130cs-chiral-structures.md",
          "locator": "SIM05-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/simons-2005-130cs-chiral-structures.md",
      "summary": "新增 130Cs Euroball primary experiment source note，记录 level/link/DCO/polarization、derived ratio and lifetime boundary。",
      "anchor": "Key Results",
      "sources": [
        {
          "path": "knowledge/sources/simons-2005-130cs-chiral-structures.md",
          "locator": "SIM05-1"
        },
        {
          "path": "knowledge/sources/simons-2005-130cs-chiral-structures.md",
          "locator": "SIM05-2"
        },
        {
          "path": "knowledge/sources/simons-2005-130cs-chiral-structures.md",
          "locator": "SIM05-3"
        },
        {
          "path": "knowledge/sources/simons-2005-130cs-chiral-structures.md",
          "locator": "SIM05-4"
        },
        {
          "path": "knowledge/sources/simons-2005-130cs-chiral-structures.md",
          "locator": "SIM05-5"
        },
        {
          "path": "knowledge/sources/simons-2005-130cs-chiral-structures.md",
          "locator": "SIM05-6"
        },
        {
          "path": "knowledge/sources/simons-2005-130cs-chiral-structures.md",
          "locator": "SIM05-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/models/triaxial-projected-shell-model.md",
      "summary": "连接 TPSM 理论应用与 130Cs primary experimental lineage，指出 Bhat Fig.8 复用 Simons data。",
      "anchor": "[[simons-2005-130cs-chiral-structures]]",
      "sources": [
        {
          "path": "knowledge/sources/simons-2005-130cs-chiral-structures.md",
          "locator": "SIM05-3"
        },
        {
          "path": "knowledge/sources/simons-2005-130cs-chiral-structures.md",
          "locator": "SIM05-5"
        },
        {
          "path": "knowledge/sources/simons-2005-130cs-chiral-structures.md",
          "locator": "SIM05-7"
        },
        {
          "path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md",
          "locator": "BHA14-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-model-choice-card.md",
      "summary": "将 Simons 2005 direct observables 与 Bhat TPSM ratio comparison 分开，新增 lifetime/absolute-strength limit 与 shared-data lineage。",
      "anchor": "primary experiment behind the TPSM ratios",
      "sources": [
        {
          "path": "knowledge/sources/simons-2005-130cs-chiral-structures.md",
          "locator": "SIM05-3"
        },
        {
          "path": "knowledge/sources/simons-2005-130cs-chiral-structures.md",
          "locator": "SIM05-5"
        },
        {
          "path": "knowledge/sources/simons-2005-130cs-chiral-structures.md",
          "locator": "SIM05-7"
        },
        {
          "path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md",
          "locator": "BHA14-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "索引 Simons 2005 `130Cs` Euroball experiment and its Bhat TPSM shared-dataset relation.",
      "anchor": "[[simons-2005-130cs-chiral-structures]]",
      "sources": [
        {
          "path": "knowledge/sources/simons-2005-130cs-chiral-structures.md",
          "locator": "SIM05-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md",
      "summary": "视觉核对并明确 Table 5 七个 presumably-triaxial 星号单元格的核素映射，同时保留 N=76–78 转变端点与中间区间需三轴投影代码确认的原文边界。",
      "anchor": "Key Results",
      "sources": [
        {
          "path": "knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md",
          "locator": "HS10-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
      "summary": "新建 2024 三轴投影壳模型 source page；记录方法、133La/135Pr 参数、Fig.11–14 结果、既有实验依赖及双声子跃迁测量边界。",
      "anchor": "Key Results",
      "sources": [
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-1"
        },
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-2"
        },
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-3"
        },
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-4"
        },
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-5"
        },
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-6"
        },
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-7"
        },
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/models/triaxial-projected-shell-model.md",
      "summary": "连接 133La/135Pr 的后续 TPSM 计算与 Hara Table 5 两个 N=76 星号案例，保留固定形变输入、实验数据复用及模型解释边界。",
      "anchor": "Hara Table 5 的后续 TPSM 覆盖（2026-09-29）",
      "sources": [
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-3"
        },
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-4"
        },
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-5"
        },
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-6"
        },
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-model-choice-card.md",
      "summary": "列明 Hara Table 5 七个星号核素，区分 2024 TPSM 对 133La/135Pr 与 2020 CDFT/PRM 对 137Nd 的模型覆盖层级，并保留固定参数、不同带对象及非独立形状验证边界。",
      "anchor": "Hara Table 5: later TPSM coverage check (2026-09-29)",
      "sources": [
        {
          "path": "knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md",
          "locator": "HS10-4"
        },
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-3"
        },
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-4"
        },
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-5"
        },
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-6"
        },
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-7"
        },
        {
          "path": "knowledge/sources/petrache-2020-137nd-multiple-chiral-bands.md",
          "locator": "P20-1"
        },
        {
          "path": "knowledge/sources/petrache-2020-137nd-multiple-chiral-bands.md",
          "locator": "P20-2"
        },
        {
          "path": "knowledge/sources/petrache-2020-137nd-multiple-chiral-bands.md",
          "locator": "P20-3"
        },
        {
          "path": "knowledge/sources/petrache-2020-137nd-multiple-chiral-bands.md",
          "locator": "P20-4"
        },
        {
          "path": "knowledge/sources/petrache-2020-137nd-multiple-chiral-bands.md",
          "locator": "P20-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/131ce-collective-mode-discrimination.md",
      "summary": "更新 131Ce 模型路线链接，说明 Hara Table 5 N=76–78 星号候选及 133La/135Pr TPSM 结果均不能跨核迁移到 N=73 131Ce；模式排序不变。",
      "anchor": "Day 3 model-route link (2026-09-29)",
      "sources": [
        {
          "path": "knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md",
          "locator": "HS10-4"
        },
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/131ce-collective-mode-discrimination.md",
      "summary": "把 AW13-16 的 611.1-keV Band-4→Band-1 link 转成有停止条件的 δ/偏振与 partner-lifetime 测量顺序；量化 AW13 δ=0 派生比值的敏感度，不改变模式排序。",
      "anchor": "Day 3 follow-up: test the 611.1-keV Band-4→Band-1 link (design-only)",
      "sources": [
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-16"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-9"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-11"
        },
        {
          "path": "knowledge/sources/singh-2016-lifetime-131ce-133pr.md",
          "locator": "SI16-1"
        },
        {
          "path": "knowledge/sources/li-2004-lifetimes-131ce.md",
          "locator": "LI04-1"
        },
        {
          "path": "knowledge/sources/li-2004-lifetimes-131ce.md",
          "locator": "LI04-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "索引 Sheikh et al. 2024 TPSM `133La`/`135Pr` 计算与其 Hara Table 5 overlap boundary。",
      "anchor": "[[sheikh-jehangir-bhat-2024-tpsm-wobbling]]",
      "sources": [
        {
          "path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
          "locator": "SHJ24-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
      "summary": "新建 Budaca & Budaca 2025 source page，记录 constrained particle-rotor/HA 主线、137Nd 同一 P20 数据拟合、Fig.4 点筛选、模型 Ic 复算与 transition-ratio 缺口。",
      "anchor": "Key Results",
      "sources": [
        {
          "path": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
          "locator": "BU25-1"
        },
        {
          "path": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
          "locator": "BU25-2"
        },
        {
          "path": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
          "locator": "BU25-3"
        },
        {
          "path": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
          "locator": "BU25-4"
        },
        {
          "path": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
          "locator": "BU25-5"
        },
        {
          "path": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
          "locator": "BU25-6"
        },
        {
          "path": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
          "locator": "BU25-7"
        },
        {
          "path": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
          "locator": "BU25-8"
        },
        {
          "path": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
          "locator": "BU25-AR-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/models/triaxial-particle-rotor-model.md",
      "summary": "加入 2025 harmonic chiral-vibration HA 的 PRM linkage、Ic/RI 适用边界和 137Nd gamma/energy-splitting 模型结果，注明复用 P20 数据。",
      "anchor": "[[budaca-budaca-2025-harmonic-chiral-vibration]]",
      "sources": [
        {
          "path": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
          "locator": "BU25-1"
        },
        {
          "path": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
          "locator": "BU25-3"
        },
        {
          "path": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
          "locator": "BU25-4"
        },
        {
          "path": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
          "locator": "BU25-5"
        },
        {
          "path": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
          "locator": "BU25-7"
        },
        {
          "path": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
          "locator": "BU25-8"
        },
        {
          "path": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
          "locator": "BU25-AR-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-model-choice-card.md",
      "summary": "把 `137Nd` harmonic chiral-vibration fit 纳入 Hara Table 5 同核模型地图；与 P20 CDFT/PRM 与 2024 TPSM 分开，说明 P25 重用 P20 energy data 且缺 `137Nd` transition-ratio test。",
      "anchor": "Hara Table 5: later TPSM coverage check (2026-09-29)",
      "sources": [
        {
          "path": "knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md",
          "locator": "HS10-4"
        },
        {
          "path": "knowledge/sources/petrache-2020-137nd-multiple-chiral-bands.md",
          "locator": "P20-1"
        },
        {
          "path": "knowledge/sources/petrache-2020-137nd-multiple-chiral-bands.md",
          "locator": "P20-2"
        },
        {
          "path": "knowledge/sources/petrache-2020-137nd-multiple-chiral-bands.md",
          "locator": "P20-3"
        },
        {
          "path": "knowledge/sources/petrache-2020-137nd-multiple-chiral-bands.md",
          "locator": "P20-4"
        },
        {
          "path": "knowledge/sources/petrache-2020-137nd-multiple-chiral-bands.md",
          "locator": "P20-5"
        },
        {
          "path": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
          "locator": "BU25-4"
        },
        {
          "path": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
          "locator": "BU25-5"
        },
        {
          "path": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
          "locator": "BU25-6"
        },
        {
          "path": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
          "locator": "BU25-7"
        },
        {
          "path": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
          "locator": "BU25-8"
        },
        {
          "path": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
          "locator": "BU25-AR-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "索引 Budaca & Budaca 2025 harmonic chiral-vibration model and the `137Nd` same-data boundary.",
      "anchor": "[[budaca-budaca-2025-harmonic-chiral-vibration]]",
      "sources": [
        {
          "path": "knowledge/sources/budaca-budaca-2025-harmonic-chiral-vibration.md",
          "locator": "BU25-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
      "summary": "新建 136Pr 2025 主文 source page，保存新 JUROGAM II 谱、TAC-CDFT/SN100PN 方法、模型残差、Q1 宇称限制和 D4/D6 竞争解释。",
      "anchor": "## Key Results",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-1"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-3"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-4"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-5"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-6"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-7"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-8"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-9"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-10"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-11"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-12"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-13"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-14"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-15"
        }
      ]
    },
    {
      "knowledge": "knowledge/nuclei/136pr.md",
      "summary": "新建 136Pr 核素页，连接 595-keV isomer、D1-D6/Q1-Q4 谱学、Q1 宇称边界与模型竞争解释。",
      "anchor": "## Isomer and Level Structure",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-1"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-2"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-3"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-12"
        }
      ]
    },
    {
      "knowledge": "knowledge/models/tilted-axis-cranking.md",
      "summary": "补入 136Pr PC-PK1 TAC-CDFT 例子及 pairing-collapse、projection 未实施和 D5 失配边界。",
      "anchor": "### 2026-09-30 case: 136Pr",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-4"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-6"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-8"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-13"
        }
      ]
    },
    {
      "knowledge": "knowledge/models/covariant-density-functional-theory.md",
      "summary": "连接 136Pr TAC-CDFT 全文案例，保留自洽形变为模型输出且未恢复总角动量/粒子数的边界。",
      "anchor": "## Known Limitations",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-4"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-5"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-model-choice-card.md",
      "summary": "把 136Pr 更新为直接 TAC-CDFT/壳模型应用但非角动量投影；TPSM 已核实计数仍是 2/7，并加入 D1/D2 残差、D5 失配与 Q1/D4-D6 限制。",
      "anchor": "### 2026-09-30 extension: 136Pr TAC-CDFT is not projection coverage",
      "sources": [
        {
          "path": "knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md",
          "locator": "HS10-4"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-3"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-4"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-5"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-6"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-7"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-8"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-9"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-10"
        },
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "索引 136Pr 2025 TAC-CDFT/壳模型 source page。",
      "anchor": "[[lv-2025-136pr-tac-covariant-density-functional]]",
      "sources": [
        {
          "path": "knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md",
          "locator": "LV25-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
      "summary": "新建 137Pr INGA/TAC source page，记录 M1 band、crossover E2、派生强度比的 δ² 假设和 TAC 3qp/5qp crossing 及其高自旋偏移。",
      "anchor": "## Key Results",
      "sources": [
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-1"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-2"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-3"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-4"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-5"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-6"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-7"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-8"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-9"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-10"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/nuclei/137pr.md",
      "summary": "新建 137Pr 核素页，整理 INGA 实验反应、Band 2 M1/crossover E2、3qp/5qp TAC 解释和绝对寿命缺口。",
      "anchor": "## Bands",
      "sources": [
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-2"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-3"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-4"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-7"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-8"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-9"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/models/tilted-axis-cranking.md",
      "summary": "加入 137Pr hybrid TAC 3qp/5qp band-crossing 实例并标明模型形变、配对、eta 与高自旋偏差。",
      "anchor": "### 2007 case: 137Pr magnetic-rotation band crossing",
      "sources": [
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-5"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-6"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-8"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-model-choice-card.md",
      "summary": "把 137Pr Hara N=78 exact-nucleus TAC 3qp/5qp magnetic-rotation application 与直接投影覆盖分开；保存 δ² 假设和高自旋模型偏差。",
      "anchor": "### 2026-09-30 extension: 137Pr TAC magnetic-rotation case",
      "sources": [
        {
          "path": "knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md",
          "locator": "HS10-4"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-2"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-3"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-4"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-5"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-6"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-7"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-8"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-9"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-10"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "索引 137Pr 2007 INGA/TAC magnetic-rotation band-crossing source。",
      "anchor": "[[agarwal-2007-137pr-magnetic-rotation-bandcrossing]]",
      "sources": [
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
      "summary": "新建 137Pr INGA/TAC source page，记录 M1 band、crossover E2、派生强度比的 δ² 假设和 TAC 3qp/5qp crossing 及其高自旋偏移。",
      "anchor": "## Key Results",
      "sources": [
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-1"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-2"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-3"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-4"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-5"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-6"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-7"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-8"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-9"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-10"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/nuclei/137pr.md",
      "summary": "新建 137Pr 核素页，整理 INGA 实验反应、Band 2 M1/crossover E2、3qp/5qp TAC 解释和绝对寿命缺口。",
      "anchor": "## Bands",
      "sources": [
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-2"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-3"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-4"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-7"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-8"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-9"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/models/tilted-axis-cranking.md",
      "summary": "加入 137Pr hybrid TAC 3qp/5qp band-crossing 实例并标明模型形变、配对、eta 与高自旋偏差。",
      "anchor": "### 2007 case: 137Pr magnetic-rotation band crossing",
      "sources": [
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-5"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-6"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-8"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-model-choice-card.md",
      "summary": "把 137Pr Hara N=78 exact-nucleus TAC 3qp/5qp magnetic-rotation application 与直接投影覆盖分开；保存 δ² 假设和高自旋模型偏差。",
      "anchor": "### 2026-09-30 extension: 137Pr TAC magnetic-rotation case",
      "sources": [
        {
          "path": "knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md",
          "locator": "HS10-4"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-2"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-3"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-4"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-5"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-6"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-7"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-8"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-9"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-10"
        },
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "索引 137Pr 2007 INGA/TAC magnetic-rotation band-crossing source。",
      "anchor": "[[agarwal-2007-137pr-magnetic-rotation-bandcrossing]]",
      "sources": [
        {
          "path": "knowledge/sources/agarwal-2007-137pr-magnetic-rotation-bandcrossing.md",
          "locator": "AG07-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/models/triaxial-projected-shell-model.md",
      "summary": "加入 odd-neutron 3ν/3ν+2π TPSM 基底扩展，限定 131Xe 的 inherited deformation、unobserved yrare prediction、非正交振幅和与 Hara N=77 候选的迁移边界；核对 2022 TPSM 与 2023 解释文章共享 Banik 2020 数据谱系。",
      "anchor": "Odd-neutron TPSM basis extension and N=77 transfer boundary (2026-09-30)",
      "sources": [
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-1"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-2"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-3"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-4"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-5"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-6"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-8"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-10"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-11"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-12"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-2"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-3"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-7"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-13"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-1"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-2"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-5"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-6"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-7"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-9"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-10"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-model-choice-card.md",
      "summary": "新增 odd-neutron TPSM 方法控制矩阵行：131Xe 为 N=77 同中子素示例而非 Hara Table 5 exact-nucleus 覆盖；保留谱学预测、形变输入、HFB 参数约束、共享数据与必要实验检验边界；重算 ε/ε′ 与表列 γ 的近似一致性。",
      "anchor": "Odd-neutron TPSM basis-extension control",
      "sources": [
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-1"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-2"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-4"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-6"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-8"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-10"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-11"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-12"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-2"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-3"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-7"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-13"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-14"
        },
        {
          "path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md",
          "locator": "BHA14-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "将 2022 odd-neutron TPSM 主文加入可检索 source 入口，并标明高自旋基底扩展和 131Xe 证据边界。",
      "anchor": "[[jehangir-2022-odd-neutron-tpsm-extension]]",
      "sources": [
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-1"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-4"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-6"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-8"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-model-choice-card.md",
      "summary": "把 131Xe 的 2020 主实验、2022 TPSM 能谱比较和 2023 same-data reanalysis 连接为一条 INGA acquisition lineage；保存相对强度/DCO/偏振与寿命/绝对强度缺项、B1(a)/B1(b)判据、BNK20/C23 带标签映射歧义和 TRS 模型边界。",
      "anchor": "`131Xe` primary dataset and later reanalysis",
      "sources": [
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-1"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-2"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-3"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-4"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-5"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-6"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-7"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-8"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-9"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-12"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-2"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-3"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-7"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-10"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-6"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-11"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "将 2020 `131Xe` INGA 主实验 source 接入索引，标明实验量和绝对强度边界。",
      "anchor": "[[banik-2020-131xe-multiple-band-structures]]",
      "sources": [
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-1"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-2"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-3"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-5"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-6"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-model-choice-card.md",
      "summary": "比较 Banik TRS 输出 γ≈−26°、Jehangir TPSM 继承输入 29°、Chakraborty TPRM 参数 33° 的物理角色；只做 pairwise arithmetic screen，保留频率依赖、参数继承、模型差异和共享数据边界，不平均成形状值。",
      "anchor": "131Xe cross-model γ parameter role check (2026-09-30)",
      "sources": [
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-6"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-4"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-12"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-14"
        },
        {
          "path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md",
          "locator": "BHA14-6"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-4"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/questions.md",
      "summary": "修订既有 131Xe γ-soft/稳定 γ 局域开放问题：加入 TRS 频率依赖结果、TPSM/TPRM 参数角色、共享 INGA acquisition lineage 和仍缺的伴随观测；问题状态保持 open。",
      "anchor": "`131Xe` 的三轴形变更接近 γ-soft 还是具有稳定 γ 局域？需要哪些独立观测量？",
      "sources": [
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-2"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-6"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-7"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-4"
        },
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-12"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-4"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-7"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-10"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/models/cranked-shell-model.md",
      "summary": "把 Banik 2020 `131Xe` Woods–Saxon/Strutinsky TRS 作为推转壳模型的频率依赖形变案例，标明 TRS minima 为模型输出并与 Nilsson-only CNS、HFB 和角动量投影区分。",
      "anchor": "`131Xe` Woods–Saxon TRS 频率演化（2026-09-30）",
      "sources": [
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-6"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-model-choice-card.md",
      "summary": "在模型选择 crosswalk 中加入频率依赖 Woods–Saxon TRS：记录其输入、可回答问题和 shape-sensitive falsifier/companion-observable 边界。",
      "anchor": "Frequency-dependent Woods–Saxon TRS shape surface",
      "sources": [
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-6"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/questions.md",
      "summary": "更新既有 131Xe yrast-13/2 问题：区分 Banik 2020 的 B5 decoupled-band 解释与 C23 对 yrast/yrare 13/2− 的再分析，保留同 acquisition 的 band-label crosswalk 和必要后续观测缺口。",
      "anchor": "`131Xe` yrast 13/2− 起始序列的组态与集体性质是什么？",
      "sources": [
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-11"
        },
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-10"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-6"
        }
      ]
    }
  ]
}
```

## Open questions and belief revision


- Bhat Ref. [18] `126Cs` lifetime/absolute-strength primary route remains unavailable: OpenAlex marked a hybrid publisher PDF, but the direct ScienceDirect request and OpenAIRE resolver each returned HTTP 403, while the exact-title arXiv search had 0 hits. No article or claim was imported; do not retry those endpoints without a new lawful repository path.
- `130Cs` Ref. [32] is confirmed as Simons 2005 Euroball. Bhat uses the same ratios, so the theory/experiment pair is dependent rather than an independent second experiment. Bhat arXiv v1 Table 1/Eq. (3) still gives a `γ` mismatch against the p.6 “about 30°” prose; retain `BHA14-6 needs_review` until a publisher final/correction resolves it.
- Full-text model coverage for Hara Table 5 currently consists of 2024 TPSM `133La/135Pr`, plus later `137Nd` CDFT/PRM (P20) and harmonic chiral-vibration HA (P25). P25 converts `γ=97.5°` to `22.5°` in its stated symmetry sector and gives a model `I_c≈17.804ℏ`; it reuses P20 Ref. [30] energy data, uses few fit points, and has no `137Nd` measured-ratio test. These are model comparisons, not new experiments or a direct PSM recalculation of Hara's old levels.
- 2026 NPA 134La DOI 的新 Elsevier publisher API 路由已尝试；本地 downloader 返回 credentials_missing，OA fallback 仍没有可读全文。未获取 PDF、未导入摘要或科学主张；访问回执保存在 raw/papers/gpt/_incoming/prompt-2026-09-29-day-03/134la-2026-npa-publisher-api/manifest.json。
- Two further metadata leads remain content-blocked. NPA DOI `10.1016/j.nuclphysa.2026.123419` has a title range `128–134La` and may include `134La`, but Crossref has no abstract, OpenAIRE says CLOSED/no instance, OpenAlex says closed/no repository, exact-title arXiv search returns 0 and OA downloader returns `oa_not_found`; no text/claim was imported. AIP conference DOI `10.1063/1.1905297` is “Identification of Chiral Bands in 135Ce”; Crossref/INSPIRE verify identity, OpenAlex says closed/no repository, arXiv/OA search has no full text and the DOI landing returns 403. Neither title is evidence of a calculated shape or a chiral assignment.
- Hara Table 5 的直接 TPSM 投影覆盖仍为 2/7。余下五核 `134La`、`135Ce`、`136Pr`、`137Pr`、`137Nd` 本轮均未核实到 PSM/TPSM 投影全文：136Pr/137Pr 有 exact-nucleus TAC-family 全文、137Nd 有 CDFT/PRM 与复用同一数据的 HA；这些均不是角动量投影。134La/135Ce 仅有 closed/metadata source route。此为检索边界，不是文献不存在结论。
- `131Ce`'s measurement design is now anchored to AW13-16's `611.1-keV 17/2−→15/2−` Band-4→Band-1 link. The existing table `R` is not `δ`; AW13's `δ=0` branching ratio sensitivity is large, and SI16/LI04 lifetimes do not give Band-4 partner strengths. Highest-value next route: search alternate lawful sources for the remaining direct-projection cases and keep the `131Ce` transition/lifetime package ready; mode ranking remains unchanged.
- 2022 TPSM 对 `131Xe` yrare 带的计算仍缺 g-factor、寿命和绝对跃迁强度等实验检验；已识别其 Fig. 7 与 2023 分析共享 Banik 2020 数据谱系，但尚未逐条核对该 2023 重分析与 TPSM 输入的每一条能级/跃迁。Hara N=77 的 134La/135Ce direct-projection 全文仍未取得；下一条最高信息增益路线是等待/搜索合法全文线索后核对是否提供 exact-nucleus 投影计算，不把同中子素方法文章记作覆盖。
- Banik 2020 full text 确认 `131Xe` acquisition 仅有相对强度、DCO 和偏振；B1(b) 侧带没有足够内部跃迁或 inter/intraband strength ratio，不能定为 γ band。后续高信息观测为 partner-resolved lifetime/绝对 `B(E2)/B(M1)` 与 g-factor；C23 是同一 INGA 数据的重新分析，不增加独立实验样本，也不能填补 `131Ce N=73`。
- `131Xe` yrast/yrare `13/2−` 起始序列的标签仍待逐跃迁核清：Banik 2020 把约 1046-keV 态放在 B5、称可能为 decoupled band；C23 对同一采集的重分析说 yrast `13/2−` 起源仍开，且觉得 yrare `13/2−` 更适合作 unfavored partner。此为同一数据的能带重标/解释问题，不是独立第二次实验（BNK20-10, BNK20-11; C23-6）。
- **belief revision:** The projected single-state energy ratio is only the one-configuration limit; multi-configuration mixing needs the nonorthogonal norm kernel. Hara Table 5 stars span `N=76–78` including N=77 rows. The later-model map now distinguishes (i) TPSM on two candidates, (ii) same-nucleus but different-model `137Nd` calculations reusing one dataset, and (iii) title/metadata leads that cannot be counted without text. None of the neighboring-nucleus model outputs transfers to `131Ce (N=73)`; number projection still does not remove spurious truncated-space admixtures automatically.

## L0–L4 state

- **L0：bounded source audit complete.** 已沿主文核对 Åberg–Flocard–Nazarewicz 1990、Hara–Sun 1995、Bhat 2014、Simons 2005、Sheikh et al. 2024、Budaca & Budaca 2025、Lv et al. 2025、Agarwal et al. 2007、Jehangir et al. 2022、Banik et al. 2020 和 Chakraborty et al. 2023 的关键图表、公式与限制；134La/135Ce 的闭源 metadata 仍不作为科学证据。
- **L1：updated.** 新建 2024 TPSM、2025 harmonic-vibration、2025 136Pr、2007 137Pr、2022 odd-neutron TPSM 和 2020 `131Xe` source pages，以及 136Pr/137Pr nuclei pages；更新 CSM、TPSM、TAC、CDFT、TRS 方法入口、A≈130 model-choice card、`knowledge/questions.md` 与索引。所有新 claim 保持 `needs_review: true`，页面维持原 review status；未修改已 human-reviewed 的 `131Xe` source/nucleus 页面。
- **L2：selected analyses complete.** 完成投影核与广义本征方程推导、HF/HFB—CSM—TRS—AMP/PSM 方法映射、137Pr `B(M1)/B(E2)` 表格复算、136Pr `R_DCO` 核查、Hara Table 5 `A=Z+N` 交叉映射、137Nd `γ/I_c` exercise、`131Ce` 611.1-keV link 设计、odd-neutron TPSM 非正交范数示例、`131Xe` 相对强度/同中子素核查，以及 TRS/TPSM/TPRM 参数角色比较。
- **L3：候选 / 部分收敛。** Hara Table 5 direct TPSM 投影覆盖仍为 `2/7`；余下 `134La/135Ce/136Pr/137Pr/137Nd` 本轮均无已核实的直接 PSM/TPSM 计算。136Pr/137Pr 的 TAC 与 137Nd 的 CDFT/PRM/HA 仍是不同模型路线；`131Xe` 多篇文章共享同一次 INGA acquisition。开放的来源获取、band-label crosswalk、绝对强度和目标核 `131Ce` 模式判断均保持明确边界，未改变现有 `131Ce` 排序。
- **L4：not-ready.** 没有可复现的目标核事件级数据、探测器响应与协方差、模型代码/参数包和统一 observable 对照；未生成伪造谱学值、模型拟合或 proxy 结果。
- **计数状态：** 本日仅在最终日报、canonical writeback、boundary/lint/diff、receipt 与 Day 4 prompt 检查通过后计为 Day 3，并把 `next_day_index` 推进至 4；Git H3 的实际 push 结果按发布门记录。

## Verification and continuation

- 写入前、最终 boundary check `python3 system/scripts/wiki_boundary_check.py --root .` 均 exit `0`；六类目录、outputs roots 与 QMD collection contract 无错误。
- 最终 `python3 system/scripts/wiki_lint.py --fail-on error` exit `0`：`0 errors / 92 warnings / 1281 info`。warning categories：`CITATION_KEY_MISSING=88`、`REACTION_PARSE=3`、`RAW_GIT_CHANGE=1`；缺 citation key 未从空值猜补，raw warning 对应未跟踪原始材料且不会暂存。
- Wiki automation preflight exit `0`；受保护 `raw/zotero/wiki-inbox.bib` SHA-256 与基线匹配。`git diff --check` exit `0`。
- 日报固定标题 10/10 齐全、唯一 `knowledge-writeback` block、JSON 和 run receipt parse 均通过。writeback validator 检查 48 项 anchor/backlink/atomic locator，`valid=true`, `status=updated`；按 Git 规范化差异核对 16 个知识页变更，全部在 block 映射中，`unmapped=0`。相对 HEAD 的 byte-for-byte snapshot 未单独保存，因此另记规范化路径审计，不声称本次静态 validator 执行了 snapshot 比较。
- 日报内 73 个相对链接均可解析，固定标题、run receipt、continuation prompt 与 Day 4 prompt 路径存在。`git diff --check` 当前 exit `0`。
- Banik 2020 APS PDF 与 Jehangir 2022 arXiv PDF 的本地 SHA-256 均与 manifest/frontmatter 相符；Banik 使用 publisher-direct public URL、非 OA 许可标记，OA-only route 返回 `oa_not_found`。两篇主文均无需 SI 即可复核本日报 claim。
- Farmer `once --dry-run` exit `0`, `actions=[]`；Wiki preflight 的边界探测 exit `0`。`clean_knowledge_eol_dirty.py --dry-run` exit `1`，把 9 个已核对的 substantive knowledge edits 标为 `KEEP-SUBSTANTIVE`、`unsafe/mixed=0`、`would restore=0`；没有恢复或改写这些内容。
- `qmd status` exit `0`：550 files、2459 vectors、174 orphan chunks，index reported updated 22h ago。SQLite 位于 `/var/lib/qmd/cache/qmd/wiki.sqlite`，在 `/workspace/wiki` 写入边界外，本轮没有刷新。
- Milestone 状态推进至 `next_day_index=4`；当日本地完成计数为 Day 3。Gitee H3 的 commit/push outcome 由 [scheduler event log](../learning-milestones/2026-09-one-month-scheduler.jsonl) 和最终回顾记录；未将 `raw/`、`tmp/`、Day 2/run-01 继承目录或受保护 BibTeX 暂存。
