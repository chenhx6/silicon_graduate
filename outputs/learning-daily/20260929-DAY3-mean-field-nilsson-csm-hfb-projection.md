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

- 当前是 **Day 3 continuation checkpoint**，不是学习日最终结算；运行仍待后续续接，`counted_in_substantive_test: false`。原窗口截止时间为 `2026-09-30 15:00 Asia/Shanghai`，本检查点不推进 `next_day_index`。
- 本轮 prompt 标识为 `prompt-2026-09-29-day-03`。入口运行器回执 `2026-09-29-day-03-01` 因服务高负载在 `2026-09-29 13:41 Asia/Shanghai` 以 exit `1` 结束；同一 Codex session 随后恢复。Farmer 状态将该 session 识别为 `running`，`once --dry-run` 没有待恢复动作。当前 session ID 为 `01a0eb92-e525-7863-a0c9-af73a53d832b`，可复制续接命令：`codex resume 01a0eb92-e525-7863-a0c9-af73a53d832b -C /workspace/wiki -s danger-full-access -a never`。
- 注入 prompt 给出的 `output_dir` 是 `...-run-03`，入口 runner 的失败回执和执行事件位于继承的 `...-run-01`。本检查点遵循注入路径，新建 `...-run-03/run.json` 与 `continuation-prompt.md`；`run-01` 失败回执、事件日志、Day 2 原始材料目录均保留原样。
- 本续接开始时分支为 `main`、没有 staged 文件。继承的 Day 2 / Day 3 `run-01` 和 `raw/papers/gpt/day2-shell-gap-20260928/` 未跟踪内容保持未修改；本续接新取得的 Sheikh et al. PDF 位于 `raw/papers/gpt/day3-mean-field-20260929/2405-08368-wobbling-133La-135Pr/`，只作为原始证据留在本地，不纳入 Git 暂存。受保护 BibTeX 未修改。

## Candidate pool and selection

候选池依据 [当前问题列表](../../knowledge/questions.md)、[A≈130 thesis evidence matrix](../../knowledge/projects/a130-thesis-evidence-matrix.md)、[A≈130 model-choice card](../../knowledge/projects/a130-model-choice-card.md)、[131Ce/133Ce project](../../knowledge/projects/131ce-collective-mode-discrimination.md)、9 月 27 日 Day 1 和 9 月 28 日 Day 2 记录，以及 Wiki 已有来源指纹重建。

| 槽位 | 候选问题 | 信息增益与选择 |
|---|---|---|
| 连续性 | `131Ce` 现有 crossing/alignment/signature 证据如何对应 CSM 与投影模型的能力，哪些观测才足以判别 γ-soft、wobbling 或 chirality？ | 选择。现有 project 将普通 signature/configuration coupling 排在较前，但目标带仍缺直接 `δ`/偏振、partner-resolved lifetime 与 absolute `B(E2)/B(M1)`；Day 3 要求的模型适用条件可直接约束下一步证据需求。 |
| 新颖性 | 粒子数投影对截断 PSM 的改善是否单调、能否直接消除 pairing-related spuriosity？ | 选择。用 Hara–Sun 的 `156Er` Figs.26–27 检查另一个核区/方法失效模式，与 `131Ce` 的集体模式问题不共享目标数据。 |
| 暂缓 | 重开 `130Sn/132Sn` 壳隙与数据字段谱系。 | Day 2 的高信息缺口已记录；与本日模型适用性练习不重叠，留在 Day 2 continuation 路线，避免把不同观测问题塞进本日。 |
| 续接延伸 | 现代 A≈130 TPSM 对邻近 odd–odd 核的实际可检验量是什么，能否验证历史 `N=76–78` 候选或 `131Ce`？ | 先用 Bhat et al. 2014 `124,126,130,132Cs` 作为方法迁移控制；该文的 Cs 核不覆盖 Hara 候选。随后逐表映射 Hara Table 5，并检索现代三轴投影计算。 |

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
- 口试式不确定点：相近能量只表示 partner 候选；若没有寿命，`B(M1)/B(E2)` 是否只能从相对强度/分支导出？polarization 和 DCO 能闭合自旋宇称/电磁性质到什么程度？是否出现一个需要把 chiral interpretation 限定到自旋区间的反证？
- 原文核对后：Euroball 反应与 Tables 1–2 给出直接谱学和四条带间 link 的 DCO/偏振；文章认为 A/B 同宇称/组态，并报告 `S(I)` 与 ratio fingerprints。Band B 的 `B(M1)/B(E2)` 未出现预期 staggering，absolute lifetimes 缺失，高自旋 crossing 使作者将 chiral 解释限在 `I\lesssim16`。

### Continuation active recall（检索 Hara Table 5 后续计算前，2026-09-29）

- 当前问题池包括：① 是否有现代三轴投影计算直接覆盖 Hara–Sun Table 5 的星号核素；② `131Ce` 目标跃迁的 mixing ratio/偏振、伙伴带寿命和绝对强度如何组成可判别设计；③ Bhat v1 的 `γ` 参数表述能否由最终版核对。选择①作为当前延续问题：它检验历史模型候选是否有后续计算，但可避免把 `130Cs` TPSM 或 `131Ce N=73` 证据迁移到不同核素。
- 不看新文献的回忆：Hara–Sun 的 triaxial 标记源自轴对称 PSM 对实验描述不足，是作者提出的模型候选；它不是直接形状测量。现代直接检验需要先逐个锁定 Table 5 的核素，再核对新计算是否使用三轴 intrinsic basis/角动量投影、实际报告了哪些同核能级或电磁量、以及参数与组态空间是否足以和旧候选比较。只看到“TPSM”或邻近核素名称并不能满足直接覆盖。
- 复看原文 Table 5 (PDF p.712) 后确定，星号覆盖 `N=76–78` 的七个单元格：`133La`、`134La`、`135Ce`、`135Pr`、`136Pr`、`137Pr`、`137Nd`；p.713 将 N=76 与 78 描述为形状转变端点，并要求三轴投影代码核对中间核素。
- 检索后发现 2024 arXiv/book chapter `2405.08368v1` 对 `133La`、`135Pr` 做 TPSM 计算；它覆盖原表七个候选中的 2 个。另发现 2026 IJMPE DOI `10.1142/S0218301326500448`，但当前只核实书目信息和访问状态，没有把摘要当作科学证据。下一步若缺少可得全文，转入 `131Ce` 最小观测设计，并保留各核素证据边界。

## Sources and evidence

| 证据层 | 本日核对 | 精确来源位置与状态 |
|---|---|---|
| 实验直接报告（目标核背景） | Alwaleedi 2013 建立/扩展 `131Ce` Bands 1–7，并用角强度比、crossing/alignment 与准粒子 Routhian 约束谱学。Table 5.1 报告 Band 1 两 signature 的 crossing frequency `0.329`、`0.367 MeV/ℏ`。这些是能级/跃迁分析量，不是独立测得的形状或集体模式。 | [Alwaleedi 2013 source page](../../knowledge/sources/alwaleedi-2013-band-structures-131ce.md#key-results)：`AW13-1`, `AW13-5`; 本次沿用既有 source 页的 PDF/Table locator，没有重新声称复核整篇原始 thesis。 |
| 实验派生量与缺项 | 论文的 `B(M1)/B(E2)` 由 branching 和能量推得并假设 `δ=0`；source page 记录本数据集缺寿命、absolute `B(E2)`、偏振和直接形状测量。 | 同上：`AW13-9`（Eqs. 5.6–5.7、Table 5.4），`AW13-11`（Chapters 3–5 数据/方法 inventory）。对应的现有证据排序见 [131Ce/133Ce project](../../knowledge/projects/131ce-collective-mode-discrimination.md#evidence-available)。 |
| 作者解释 / 历史模型归类 | Hara–Sun §5.1 Table 5 将七个单元格标为“presumably triaxial”：`133La (Z=57,N=76)`、`134La (57,77)`、`135Ce (58,77)`、`135Pr (59,76)`、`136Pr (59,77)`、`137Pr (59,78)`、`137Nd (60,77)`。p.713 把 N=76、78 写作转变端点，并说中间区间仍需三轴代码确认。`131Ce` 是 `Z=58,N=73`，表中归为 prolate `+0.22`；候选不能迁移到 `131Ce`。 | [Hara–Sun 1995 source page](../../knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md#key-results)：`HS10-4`; 原文 §5.1 Table 5，PDF pp.712–713。星号是作者/模型候选，不是直接形状测量。 |
| 理论模型结果 | Åberg 等 Fig.12 展示 `132Ce (π,α)=(+,0)` 在 `ℏω=0.47,0.59 MeV` 的 cranked Routhian surfaces；图注将 `β₂≈0.40` prolate 极小与两个中子占据 `i13/2` 联系，并把另一处局部极小与 `h11/2` 中子对 alignment 联系。Hara–Sun 的 `156Er` Figs.26–27 比较不做/做粒子数投影的 band diagrams；投影改变 backbending，并使最低 `qp`-pair 态更靠近 yrast。 | [Åberg–Flocard–Nazarewicz 1990 source page](../../knowledge/sources/aberg-flocard-nazarewicz-1990-mean-field-shapes.md#key-results)：`AFN90-2`，Fig.12 / PDF p.468；[Hara–Sun source page](../../knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md#key-results)：`HS10-5`，§4.3 Figs.26–27 / PDF pp.700–701。均为模型计算，不是实验观察。 |
| 续接：现代 TPSM 邻核方法控制 | Bhat et al. 2014 用三轴 Nilsson+BCS、三维角动量投影和多组态混合计算四个 odd–odd Cs；`130Cs` Fig.3 比较已有能级，Fig.8 的绝对 `B(E2)`/`B(M1)` 曲线是模型输出，实测比较主要是先前发表的 `B(M1)/B(E2)` ratios。作者要求对 `124,130,132Cs` 进行寿命测量后再确认 chiral interpretation。 | [Bhat et al. 2014 source page](../../knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md#key-results)：`BHA14-1`, `BHA14-3`–`BHA14-5`；Eqs. (1)–(3), Fig.3, Fig.8, Conclusion / arXiv PDF pp.3–6, 11, 13。它是模型比较论文，引用的实验不是本轮新增或独立重测。 |
| 续接：`130Cs` primary experiment | Simons et al. 用 Euroball IV 扩展 bands A/B；Tables 1–2 记录能级、相对强度、multipolarity、DCO 和偏振。四条 interband links 的磁偶极/偏振证据被作者用于确认同宇称/组态。 | [Simons 2005 source page](../../knowledge/sources/simons-2005-130cs-chiral-structures.md#key-results)：`SIM05-1`–`SIM05-4`；Tables 1–2, Fig.1, Eqs. (2)–(3), PDF pp.3–7。直接实验事实与“chiral”模式解释分栏。 |
| 续接：`130Cs` 派生观测与竞争解释 | `S(I)` 在 I≈12 后大致平滑；`B(M1)/B(E2)` 与 in/out 比值有部分、但非全套 chiral-like staggering；band B 缺少预期的 `B(M1)/B(E2)` staggering。能级差在中自旋约 160 keV；I≈16–17 crossing 的 h11/2 neutron-pair 归因是作者/模型解释。论文没有 `130Cs` lifetime/absolute strengths，并要求寿命测量。 | [Simons 2005 source page](../../knowledge/sources/simons-2005-130cs-chiral-structures.md#key-results)：`SIM05-5`–`SIM05-7`；Figs.4–7、Conclusion / PDF pp.9–12。Bhat 2014 Ref. [32] 就是这组 Simons 数据，属于依赖性模型复用，不是第二次实验。 |
| 续接：Hara Table 5 的后续 TPSM 覆盖 | 2024 TPSM 章节对 Hara 星号表的 `133La` 与 `135Pr` 做投影计算；Table 1 给定 `γ=36°`、`32°`，Figs.11–14 比较谱能、摇摆频率、对齐与跃迁比，作者分别归类为 longitudinal 与 transverse。固定形变为模型输入；并未覆盖其余五个表格候选或形成独立形状测量。 | [Sheikh et al. 2024 source page](../../knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md#key-results)：`SHJ24-3`–`SHJ24-8`；Table 1, Figs.11–14 / arXiv PDF pp.10,17–20。图中实验曲线沿用 Refs. [11]–[15]，不是新实验。 |
| 续接：2026 TPSM 文献访问边界 | Crossref 与 OpenAlex 核实到一篇 2026 年在线发表的 Rather–Bhat–Shah TPSM 论文；OpenAlex 标记 closed、无仓储全文。World Scientific DOI 页面返回 HTTP 403，精确题名 arXiv 搜索为 0，OA downloader 返回 `oa_not_found`。没有获取主文，未把摘要结论写成科学证据。 | DOI [`10.1142/S0218301326500448`](https://doi.org/10.1142/S0218301326500448)；[Crossref DOI work record](https://api.crossref.org/works/10.1142/S0218301326500448)；OpenAlex [`W7167921416`](https://openalex.org/W7167921416)；访问状态详见本日 [run receipt](20260929-DAY3-mean-field-nilsson-csm-hfb-projection-run-03/run.json) 的 `source_access_routes`。这些是来源身份/访问状态记录，不是全文证据。 |

**来源身份/访问：** Åberg, Flocard & Nazarewicz, *Annual Review of Nuclear and Particle Science* **40**(1), 439–528 (1990), DOI [`10.1146/annurev.ns.40.120190.002255`](https://doi.org/10.1146/annurev.ns.40.120190.002255)，本地原 PDF SHA-256 `90e3d1324dbf591cc042a3ad3b777a75e00af1463869d9ad557af433469562e6`；Hara & Sun, *International Journal of Modern Physics E* **4**(4), 637–785 (1995), DOI [`10.1142/S0218301395000250`](https://doi.org/10.1142/S0218301395000250)，citation key `HARA_1995`，本地原 PDF SHA-256 `13ca9edbd3092d2d3c4612e9d22b7cb1ff740d07f0f97c5f139ac901a7b26dac`。Crossref 分别核实题名、作者、年份、卷期与页码；两家出版商页面本轮均返回 HTTP 403。全文核对使用 Wiki 内哈希匹配的原 PDF，未用搜索摘要替代证据。

**续接来源身份/访问：** Bhat, Ali, Sheikh & Palit, *Nuclear Physics A* **922**, 150–162 (2014), DOI [`10.1016/j.nuclphysa.2013.12.006`](https://doi.org/10.1016/j.nuclphysa.2013.12.006)，arXiv [`1312.6963v1`](https://arxiv.org/abs/1312.6963)。Crossref 核对期刊元数据；OpenAlex 标记合法 green OA，Nature Downloader 以 `--no-si` 从 arXiv PDF 下载并验签。原文件保存在 `raw/papers/gpt/day3-mean-field-20260929/bhat-2014-tpsm-124-132cs.pdf`，SHA-256 `3d1e411d0dfad9d565aa5134d9ad75710a2cbb31607286f0bbc9c8b0537a9757`。本轮核对 arXiv v1，不宣称核对过出版社最终排版版。

**续接 primary experiment：** Simons et al., *Journal of Physics G* **31**(7), 541–552 (2005), DOI [`10.1088/0954-3899/31/7/001`](https://doi.org/10.1088/0954-3899/31/7/001)。OpenAlex 标记 publisher OA；IOP PDF 直接下载并以 `%PDF` 签名和 SHA-256 核验，原件位于 `raw/papers/gpt/day3-mean-field-20260929/simons-2005-130cs-chiral-structures.pdf`，SHA-256 `da71d9f1c88421bc7d4421c87c4f1eb3f15043892a1ae821c62ab48cd5a611d6`。该实验是 Bhat Ref. [32] 的同一数据集，不能双计。

## Theory/analysis exercise

**练习：** 将群投影算符与投影后本征问题连起来，据此为 `131Ce` 选择一个“最小模型 → 升级模型 → 可观测检验”路线。

Hara–Sun 的角动量投影算符为

$$
\hat P^I_{MK}=\frac{2I+1}{8\pi^2}\int d\Omega\,D^{I*}_{MK}(\Omega)\hat R(\Omega),
$$

见 Eq. (2.7), PDF p.642。对单个 intrinsic state 定义

$$
H^I_{KK'}=\langle\Phi|\hat H\hat P^I_{KK'}|\Phi\rangle,\qquad
N^I_{KK'}=\langle\Phi|\hat P^I_{KK'}|\Phi\rangle,
$$

并求解

$$
\sum_{K'}(H^I_{KK'}-E_I N^I_{KK'})F^I_{K'}=0,\qquad
\sum_{KK'}F^{I*}_{K}N^I_{KK'}F^I_{K'}=1.
$$

Hamiltonian 与 norm kernel、广义本征方程和归一化见 Eqs. (2.19)–(2.20), PDF p.644。单态比值 `⟨Φ|H P^I|Φ⟩/⟨Φ|P^I|Φ⟩` 只是单一组态极限；多组态混合时需对非正交投影基对角化。三轴 intrinsic state 可让同一 `I` 出现多个 `K` 分量，轴对称单 `K` 情形则较简单。

| 路线 | 最小输入/能回答 | 不能单独回答 | 与当前观测的连接 |
|---|---|---|---|
| 约束 HF/HFB 或 Nilsson–Strutinsky | 给出 intrinsic density、配对与候选形变能面；自洽 HF/HFB 与 shell-correction 是互补路线。 | 不直接给唯一的实验 band identity、良好 `I` 能谱或模式指认；一个 `β₂/γ` 极小不等于测得形状。 | 用质量、低自旋能级、transfer、lifetime/`Q_t` 等约束静态输入和配对。 |
| Cranked mean field / CSM | 在旋转参考系跟踪 Routhian、alignment、crossing 与随频率的极小移动。 | 只凭拟合 `γ`、crossing 或 alignment 不能唯一反演形状，也不自动恢复良好角动量。 | `131Ce` 现有能级、signature 和 crossing 可先检验配置/对齐解释；需保留参考转动惯量、配对和组态截断依赖。 |
| AMP / PSM / TPSM | 投影 intrinsic Nilsson+BCS/HFB 组态到良好 `I`，在受限基中混合并预测能谱、signature 与电磁跃迁。 | 不能自动消除基底截断、有效算符/相互作用依赖；轴对称 PSM 失配不等价于实验三轴证据。 | 只有把 `B(E2)/B(M1)`、`g` 因子或伙伴带跃迁同实验比较，并对基底/配对/参数作敏感性检查，才可能提升解释力。 |

**练习结论：** 对 `131Ce` 先用 CSM/QTR 处理 crossing/alignment/signature 作为配置假设检验；只有当实验 band identity 和跃迁矩阵清楚后，再用投影配置混合比较实验室系能谱与跃迁。现有 `δ=0` 派生比值和缺少寿命/偏振/绝对强度的状态不足以裁定 `γ` 刚/软、wobbling、chirality 或 shape coexistence。这个路线是设计结论，没有生成代理数值或新实验结论。

### 续接定量核对：TPSM 参数与可观测量分层

Bhat 等 Table 1 (PDF p.4) 给 `130Cs` `ε=0.160, ε′=0.145`；同页 Eq. (3) 近似写作 `γ=tan⁻¹(ε′/ε)`。按该式复算，`130Cs` 为 `42.18°`，`132Cs` (`0.150/0.170`) 为 `41.42°`，而 `126Cs` (`0.150/0.260`) 为 `29.98°`。正文 PDF p.6 将所选非轴形变概述为约 `30°`；这与 `130,132Cs` 的印刷参数对不上。保留为 arXiv v1 的 source-internal parameter/wording mismatch，可能涉及近似或版本/参数约定，不能替作者更正，也不能把复算角度当作实验形状。

Fig.3 (PDF p.6) 比较四个 Cs 核的 TPSM 与先前报告能级；Fig.8 (PDF p.11) 对 `130Cs` 显示 TPSM 计算的绝对 `B(E2)`、`B(M1)` 和 interband strengths，叠加的是 Ref. [32] 报告的 `B(M1)/B(E2)` ratios。结论说 `130Cs`/`132Cs` 的结果呈现 chiral-like 选择规则，但同时要求寿命测量；因此它只能支持相邻 odd–odd 核的模型可行性，不能替代 `131Ce` 的 absolute-strength 数据，也不能验证 Hara–Sun 的 `N=76–78` 案例。

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

## Counter-evidence and missing companion observables

- 对“轴对称计算失败即证明三轴”的反证是原作者自己的边界：Table 5 的七个 `N=76–78` 星号是暂定模型标签，p.713 要待三轴投影验证；该表给 `131Ce (Z=58,N=73)` 的是模型 prolate `+0.22`，不在这些星号内。未来的现代投影计算或不同配对/组态空间若拟合同一数据而不需三轴，将削弱历史解释。
- Hara–Sun p.712 说明 doubly-odd level density 约为 odd-mass 核的十倍，不同配置在低能区可有近似相等的波函数权重；shell filling 与选取组态会显著影响结果。这使“轴对称拟合差”也可能受模型空间/组态敏感性影响。
- 粒子数投影的 `156Er` 方法学反例是数量级/方向上的，而非 `131Ce` 实验证据：投影能改变 backbending，但最低受污染 `qp`-pair 态更靠近 yrast；有限空间里 spurious 态不会因增加投影而必然自动消失。
- 对 `131Ce` 集体模式必须补的伴随量仍是目标跃迁的 measured `δ` 与偏振、伙伴带分别解析的 lifetime 和 absolute `B(E2)/B(M1)`/`Q_t`、可靠 interband links 与 band identity；若使用形状解释，还需独立形变敏感 observable。邻核模型值不能代替目标核测量。
- **证据独立性：** 两篇理论综述不是两次独立实验；Hara–Sun 的 Table 5 汇总早期 A≈130 实验与模型比较，本轮未回到其 refs.70/72 的原始实验逐项审计。Alwaleedi 的 Band/crossing 与 `δ=0` 比值属于一个目标核数据集；其派生值不能按 observable 行数重复计权。
- Bhat TPSM 控制进一步显示：`130Cs` 的绝对 `B(E2)`/`B(M1)` 图是计算，已测输入主要是文献报告的能级和 intensity-derived `B(M1)/B(E2)` 比值；该论文明确要求对 `130Cs` 等核做 lifetime measurements。它不能作为绝对跃迁强度的独立实验支持，更不能跨核填补 `131Ce`。
- Simons 2005 primary experiment 确认了四条带间 link 的 DCO/偏振与 M1 character；同一数据集的 band-B ratio 没有预期 staggering，绝对 lifetime 仍缺。这既支持 same-parity band link，也限制静态 chirality 的强结论；Bhat 2014 Ref. [32] 重用该 Euroball 数据，不是第二项实验。
- Bhat arXiv v1 的 Eq. (3)+Table 1 数值复算与其 PDF p.6 “γ≈30°”概述不一致。此处保留 `needs_review`，不据此替作者指定 γ，也不把形状参数当实验测量。
- Sheikh et al. 2024 的 `133La`/`135Pr` TPSM 曲线引用或比较了更早实验，不产生新的谱学观测；其中 `135Pr` 的 wobbling 指认仍受独立实验反证：Lv et al. 2022 的 JUROGAM II 数据对关键 link 给出小 `|δ|`、以 M1 为主的解（[Lv 2022 source page](../../knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md#key-results)：`L22-4`, `L22-5`），同时提供独立的 γ-soft IBFM 解释（[Nomura 2022 source page](../../knowledge/sources/nomura-2022-questioning-wobbling-ibfm.md#key-results)：`NOM22-2`–`NOM22-12`）。
- **伴随观测边界：** 后续模型对这些核素的判别若要从能量趋势提升到结构结论，仍需逐带/跃迁身份、`δ` 与偏振、partner-resolved lifetimes 和绝对 `B(E2)/B(M1)`；只有 `E_wob` 或固定 `γ` 输入不能独立识别集体模式。对 `131Ce` 仍优先缺目标带同口径的上述测量。
- 2026 年 DOI 候选的全文未取得；此处只记录 Crossref/OpenAlex 书目与访问结果，不把数据库摘要当作反证、支持证据或计算结果。

## Knowledge Impact and Learning Decision

**决定：`revises` 后续模型覆盖图，`supports` 两个具体核素上的 TPSM 应用，`limits` 将这些计算作为 Hara 形状表独立确认或迁移到 `131Ce` 的做法。** Hara–Sun Table 5 的七个星号核素现已逐格映射；2024 章节覆盖其中 `133La`、`135Pr` 两个 `N=76` 个案，参数仍是模型输入，实验曲线来自既有来源。2026 DOI 论文目前只完成来源身份与 OA 访问检查，未导入其摘要内容。`131Ce/133Ce` project 模式排序不变：普通 signature/configuration coupling 仍是当前较节约的基线，γ-soft 是模型辅助背景，目标核 wobbling/chirality 仍缺关键电磁链。

## Durable knowledge delta

- 更新 [A≈130 high-spin model-choice card](../../knowledge/projects/a130-model-choice-card.md#theoryanalysis-exercise)：新增 Eq. (2.7)、Eqs. (2.19)–(2.20) 的投影核重构和基于原文 Figs.26–27 的有限空间反例；同时明确 Hara Table 5 的 N=76–78 triaxial candidate 不适用于 N=73 `131Ce`。这是可复用的模型输入/输出、计算式与迁移边界，review 状态仍是 `unreviewed`。
- 在 [131Ce/133Ce project](../../knowledge/projects/131ce-collective-mode-discrimination.md#related-sources-and-pages) 增加模型卡回链与 `N=76–78`→`131Ce N=73` 迁移边界；没有改变原有模式排序或 review 状态。
- 新增 [Bhat et al. 2014 TPSM source](../../knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md#key-results) 和 [TPSM model page](../../knowledge/models/triaxial-projected-shell-model.md#known-limitations) 关系；保存 `130Cs` 绝对强度是模型量、相对比值来自既有引用数据，以及 `ε/ε′→γ` arXiv-v1 参数边界。
- 将该源接入 [A≈130 model-choice card](../../knowledge/projects/a130-model-choice-card.md#model-to-observable-locator-crosswalk) 与 [`knowledge/index.md`](../../knowledge/index.md)。本次涉及的 knowledge pages 均维持 `unreviewed`，未更改 `131Ce` 模式排序。
- 更新 [Hara–Sun source page](../../knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md#key-results)：将 Table 5 七个带星号核素和 `N=76–78` 端点/中间核素说明固化在 `HS10-4`，原有 `needs_review: true` 保持不变。
- 新建 [Sheikh et al. 2024 TPSM source page](../../knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md#key-results)：记录投影方法、`133La/135Pr` Table 1 输入、Figs.11–14 比较和实验数据依赖；页面与所有新 claims 保持 `unreviewed` / `needs_review: true`。
- 更新 [TPSM model page](../../knowledge/models/triaxial-projected-shell-model.md)、[A≈130 model-choice card](../../knowledge/projects/a130-model-choice-card.md) 和 [131Ce project](../../knowledge/projects/131ce-collective-mode-discrimination.md#related-sources-and-pages)，加入两项后续模型覆盖及其非独立形状证据边界；更新 [`knowledge/index.md`](../../knowledge/index.md) 的 source 入口。没有改变 `131Ce` 排序或人工 review 状态。
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
        {"path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md", "locator": "BHA14-1"},
        {"path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md", "locator": "BHA14-2"},
        {"path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md", "locator": "BHA14-3"},
        {"path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md", "locator": "BHA14-4"},
        {"path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md", "locator": "BHA14-5"},
        {"path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md", "locator": "BHA14-6"}
      ]
    },
    {
      "knowledge": "knowledge/models/triaxial-projected-shell-model.md",
      "summary": "链接 A≈130 Cs TPSM 方法案例和 absolute-strength/neighbor-transfer 边界；保留 arXiv v1 参数映射不确定性。",
      "anchor": "Bhat et al. 2014: A≈130 odd–odd transfer boundary",
      "sources": [
        {"path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md", "locator": "BHA14-1"},
        {"path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md", "locator": "BHA14-4"},
        {"path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md", "locator": "BHA14-5"},
        {"path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md", "locator": "BHA14-6"}
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-model-choice-card.md",
      "summary": "把 130Cs TPSM 与实验数据层级作为邻核方法控制加入模型选择矩阵，不转移到 131Ce。",
      "anchor": "A≈130 odd–odd TPSM transfer control",
      "sources": [
        {"path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md", "locator": "BHA14-3"},
        {"path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md", "locator": "BHA14-4"},
        {"path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md", "locator": "BHA14-5"},
        {"path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md", "locator": "BHA14-6"}
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "索引 Bhat 2014 A≈130 Cs TPSM 模型比较来源及其未闭合的 lifetime/parameter boundary。",
      "anchor": "[[bhat-2014-tpsm-cs-doublet-bands]]",
      "sources": [
        {"path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md", "locator": "BHA14-1"}
      ]
    },
    {
      "knowledge": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md",
      "summary": "把 Bhat Ref. [32] 精确回链到 Simons 2005 primary Euroball source，标记 TPSM ratio comparison 与原实验属同一数据谱系。",
      "anchor": "[[simons-2005-130cs-chiral-structures]]",
      "sources": [
        {"path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md", "locator": "BHA14-4"},
        {"path": "knowledge/sources/simons-2005-130cs-chiral-structures.md", "locator": "SIM05-5"}
      ]
    },
    {
      "knowledge": "knowledge/sources/simons-2005-130cs-chiral-structures.md",
      "summary": "新增 130Cs Euroball primary experiment source note，记录 level/link/DCO/polarization、derived ratio and lifetime boundary。",
      "anchor": "Key Results",
      "sources": [
        {"path": "knowledge/sources/simons-2005-130cs-chiral-structures.md", "locator": "SIM05-1"},
        {"path": "knowledge/sources/simons-2005-130cs-chiral-structures.md", "locator": "SIM05-2"},
        {"path": "knowledge/sources/simons-2005-130cs-chiral-structures.md", "locator": "SIM05-3"},
        {"path": "knowledge/sources/simons-2005-130cs-chiral-structures.md", "locator": "SIM05-4"},
        {"path": "knowledge/sources/simons-2005-130cs-chiral-structures.md", "locator": "SIM05-5"},
        {"path": "knowledge/sources/simons-2005-130cs-chiral-structures.md", "locator": "SIM05-6"},
        {"path": "knowledge/sources/simons-2005-130cs-chiral-structures.md", "locator": "SIM05-7"}
      ]
    },
    {
      "knowledge": "knowledge/models/triaxial-projected-shell-model.md",
      "summary": "连接 TPSM 理论应用与 130Cs primary experimental lineage，指出 Bhat Fig.8 复用 Simons data。",
      "anchor": "[[simons-2005-130cs-chiral-structures]]",
      "sources": [
        {"path": "knowledge/sources/simons-2005-130cs-chiral-structures.md", "locator": "SIM05-3"},
        {"path": "knowledge/sources/simons-2005-130cs-chiral-structures.md", "locator": "SIM05-5"},
        {"path": "knowledge/sources/simons-2005-130cs-chiral-structures.md", "locator": "SIM05-7"},
        {"path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md", "locator": "BHA14-4"}
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-model-choice-card.md",
      "summary": "将 Simons 2005 direct observables 与 Bhat TPSM ratio comparison 分开，新增 lifetime/absolute-strength limit 与 shared-data lineage。",
      "anchor": "primary experiment behind the TPSM ratios",
      "sources": [
        {"path": "knowledge/sources/simons-2005-130cs-chiral-structures.md", "locator": "SIM05-3"},
        {"path": "knowledge/sources/simons-2005-130cs-chiral-structures.md", "locator": "SIM05-5"},
        {"path": "knowledge/sources/simons-2005-130cs-chiral-structures.md", "locator": "SIM05-7"},
        {"path": "knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md", "locator": "BHA14-4"}
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "索引 Simons 2005 `130Cs` Euroball experiment and its Bhat TPSM shared-dataset relation.",
      "anchor": "[[simons-2005-130cs-chiral-structures]]",
      "sources": [
        {"path": "knowledge/sources/simons-2005-130cs-chiral-structures.md", "locator": "SIM05-1"}
      ]
    },
    {
      "knowledge": "knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md",
      "summary": "视觉核对并明确 Table 5 七个 presumably-triaxial 星号单元格的核素映射，同时保留 N=76–78 转变端点与中间区间需三轴投影代码确认的原文边界。",
      "anchor": "Key Results",
      "sources": [
        {"path": "knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md", "locator": "HS10-4"}
      ]
    },
    {
      "knowledge": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md",
      "summary": "新建 2024 三轴投影壳模型 source page；记录方法、133La/135Pr 参数、Fig.11–14 结果、既有实验依赖及双声子跃迁测量边界。",
      "anchor": "Key Results",
      "sources": [
        {"path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md", "locator": "SHJ24-1"},
        {"path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md", "locator": "SHJ24-2"},
        {"path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md", "locator": "SHJ24-3"},
        {"path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md", "locator": "SHJ24-4"},
        {"path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md", "locator": "SHJ24-5"},
        {"path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md", "locator": "SHJ24-6"},
        {"path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md", "locator": "SHJ24-7"},
        {"path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md", "locator": "SHJ24-8"}
      ]
    },
    {
      "knowledge": "knowledge/models/triaxial-projected-shell-model.md",
      "summary": "连接 133La/135Pr 的后续 TPSM 计算与 Hara Table 5 两个 N=76 星号案例，保留固定形变输入、实验数据复用及模型解释边界。",
      "anchor": "Hara Table 5 的后续 TPSM 覆盖（2026-09-29）",
      "sources": [
        {"path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md", "locator": "SHJ24-3"},
        {"path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md", "locator": "SHJ24-4"},
        {"path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md", "locator": "SHJ24-5"},
        {"path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md", "locator": "SHJ24-6"},
        {"path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md", "locator": "SHJ24-7"}
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-model-choice-card.md",
      "summary": "列明 Hara Table 5 七个星号核素，记录 2024 TPSM 对 133La/135Pr 两例覆盖和不能作为独立形状验证的适用边界。",
      "anchor": "Hara Table 5: later TPSM coverage check (2026-09-29)",
      "sources": [
        {"path": "knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md", "locator": "HS10-4"},
        {"path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md", "locator": "SHJ24-3"},
        {"path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md", "locator": "SHJ24-4"},
        {"path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md", "locator": "SHJ24-5"},
        {"path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md", "locator": "SHJ24-6"},
        {"path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md", "locator": "SHJ24-7"}
      ]
    },
    {
      "knowledge": "knowledge/projects/131ce-collective-mode-discrimination.md",
      "summary": "更新 131Ce 模型路线链接，说明 Hara Table 5 N=76–78 星号候选及 133La/135Pr TPSM 结果均不能跨核迁移到 N=73 131Ce；模式排序不变。",
      "anchor": "Day 3 model-route link (2026-09-29)",
      "sources": [
        {"path": "knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md", "locator": "HS10-4"},
        {"path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md", "locator": "SHJ24-4"}
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "索引 Sheikh et al. 2024 TPSM `133La`/`135Pr` 计算与其 Hara Table 5 overlap boundary。",
      "anchor": "[[sheikh-jehangir-bhat-2024-tpsm-wobbling]]",
      "sources": [
        {"path": "knowledge/sources/sheikh-jehangir-bhat-2024-tpsm-wobbling.md", "locator": "SHJ24-1"}
      ]
    }
  ]
}
```

## Open questions and belief revision

- Bhat Ref. [18] `126Cs` lifetime/absolute-strength primary route remains unavailable in this container: OpenAlex lists a hybrid publisher PDF, but the downloader's direct ScienceDirect request returned HTTP 403; OpenAIRE's OA resolver URL also returned 403, and the exact-title arXiv query returned 0. No article file/claim was imported. The missing data matter for evaluating Bhat's `126Cs` model comparison, but they do not supply `131Ce` evidence. Highest-information next route is a new lawful repository or institutional-library path; none was available in this continuation.
- `130Cs` Ref. [32] is now confirmed as Simons 2005 Euroball, with ratio trends and DCO/polarization links; Bhat's use of these measurements is dependent, not an independent confirmation. Sheikh et al. 2024 directly compute two Hara Table 5 cases (`133La`, `135Pr`); five starred nuclei remain unchecked. Do not transfer Cs or N=76 results to `131Ce`.
- Bhat arXiv v1 Table 1/Eq. (3) `γ` mapping still needs comparison with the journal final version or correction; until then retain `BHA14-6` as `needs_review`.
- Hara–Sun Table 5 七个星号核素中，2024 TPSM 章节明确覆盖 `133La` 与 `135Pr`；`134La`、`135Ce`、`136Pr`、`137Pr`、`137Nd` 的直接现代三轴投影计算仍需逐核查。2026 DOI `10.1142/S0218301326500448` 可能相关，但全文闭获取；当前不得从摘要升级任何科学 claim。
- 2026 论文的最高信息路线是将来发现合法 OA/作者仓储全文或明确的机构授权路径后，核对其核素清单、Table/figures、计算参数及 transition observables。当前已试 Crossref、OpenAlex、Semantic Scholar、arXiv 精确题名、出版社页面与 OA downloader；不重复同一失败端点。
- 2024 `133La`/`135Pr` TPSM 曲线重用已有实验，且 `135Pr` 有 Lv 2022 的独立低自旋 M1-dominant 反证；下一续接转到 `131Ce` 的最小可判别观测设计，细化 link mixing-ratio/polarization、partner-resolved lifetime 与绝对强度的先后关系。
- `131Ce` 的优先缺项仍是目标跃迁的 measured `δ`/偏振与伙伴带绝对强度。获得这些后，才值得把 CSM/QTR、TPSM/投影混合与 γ-soft 模型放在共同观测集上比较。
- **belief revision：** 原先把角动量投影的单态能量比值当作普遍表达式；原文重读后确认它只是单组态极限，多组态时必须保留非正交 norm kernel。也修正了三个边界：Hara Table 5 在 `N=76–78` 区间有七个星号，包含若干 `N=77` 格而不是只有 `N=76/78` 两端；2024 TPSM 对其中 `133La` 和 `135Pr` 提供直接后续计算但不提供独立形状验证；这些 N=76 核素结果不迁移到 N=73 `131Ce`。增加粒子数投影也不保证截断空间的 spurious admixture 自动消失。

## L0–L4 state

- **L0：complete for the selected open TPSM comparison.** Crossref、arXiv、World Scientific 与 OpenAlex metadata; Hara–Sun、ABFN 原文关键公式/图表；Bhat arXiv v1、Simons 2005 primary 与 Sheikh et al. 2024 arXiv v1 `133La`/`135Pr` Table 1、Figs. 11–14、conclusion 已核。2026 DOI route 只完成 metadata/access audit，全文未取得。
- **L1：updated.** 新建 Sheikh et al. 2024 source page；精确修订 Hara Table 5 starred-nucleus mapping；更新 TPSM model page、A≈130 model-choice card、`131Ce` project 和 `knowledge/index.md`。所有相关 source/project pages 仍为 `review_status: unreviewed`；新增 claims 保留 `needs_review: true`。
- **L2：complete for selected and continuation exercises.** 完成主动回忆、投影核推导、HF/HFB—CSM—AMP/PSM route matrix、`ε′/ε→γ` 数值复算、Hara `Z+N→A` 表格映射、TPSM 输入与输出的区分、DCO/polarization 反证与最小 companion-observable 设计。
- **L3：candidate / ongoing。** 模型选择卡支持 `131Ce` 项目的后续比较，但本日没有新增目标核原始实验、没有重算竞争模式权重；继续路线见上文。
- **L4：not-ready。** 没有目标核事件级数据、完整响应/校准协方差、可运行模型代码和同一输入下的模型比较包；未生成代理拟合或模型结果。

## Verification and continuation

- 写入前、写入后 `python3 system/scripts/wiki_boundary_check.py --root .` 均 exit `0`，errors/warnings 均为 0；边界结果仍确认 QMD collection 指向 `/workspace/wiki/knowledge/**/*.md`。
- `wiki_lint.py --fail-on error` exit `0`：errors `0`、warnings `87`、info `1226`。warning 分类为 `CITATION_KEY_MISSING=83`、`REACTION_PARSE=3`、`RAW_GIT_CHANGE=1`。citation-key warning 保留，未读取/修改受保护 BibTeX；3 个 reaction-parser warning 指向既有文件；唯一 raw warning 列出继承的 Day 2 bundle 与本轮 arXiv downloader manifest，原始 PDF 与所有 raw 未暂存。
- 日报要求标题、唯一 `knowledge-writeback` block 与 `run.json` JSON parse 检查均 exit `0`。`wiki_knowledge_writeback.py` 校验 exit `0`、`valid=true`, `status=updated`；按初始 Git-clean knowledge 状态和工作树 CRLF 规范化重建 pre-write baseline 后，验证的 6 个变化页为 Hara source、Sheikh 2024 source、TPSM model、A≈130 model-choice card、`131Ce` project 与 index。首次用原始 LF blob 比较的结果将 19 个 clean CRLF 页面误报为变化；`git status`/diff 复核后以换行感知基线重验通过。
- `git diff --check` exit `0`；新 arXiv PDF 的 SHA-256 复核与 source page 相同：`a7fa3cc75113a1ff2881cbc7edd9d3285a228b429c34b6f0b9b22da4c2b90d22`。Farmer `once --dry-run` exit `0`、`actions=[]`；`ensure/status` 显示守护进程运行，当前 session 无待恢复动作。
- `qmd status` exit `0` 报 550 files、2,459 vectors、174 orphan chunks，索引约 3 小时前更新。QMD SQLite 实际位于 `/var/lib/qmd/cache/qmd/wiki.sqlite`，超出本轮 `/workspace/wiki` 写入边界；因此本续接没有运行 `qmd update`、`embed` 或 `cleanup`。最新 knowledge changes 暂未进入该 QMD index。
- 本回执与 continuation prompt 位于 `...run-03/`；学习窗口仍开放到 `2026-09-30 15:00 Asia/Shanghai`。尚未 stage/publish 当前 task-owned changes，也未推进 milestone；Git H3 结果由最终回顾记录。
