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
- 写入前分支为 `main`，没有 staged 文件。继承的 Day 2 / Day 3 `run-01` 和 `raw/papers/gpt/day2-shell-gap-20260928/` 未跟踪内容保持未修改、未暂存；受保护 BibTeX 哈希与预检基线一致。

## Candidate pool and selection

候选池依据 [当前问题列表](../../knowledge/questions.md)、[A≈130 thesis evidence matrix](../../knowledge/projects/a130-thesis-evidence-matrix.md)、[A≈130 model-choice card](../../knowledge/projects/a130-model-choice-card.md)、[131Ce/133Ce project](../../knowledge/projects/131ce-collective-mode-discrimination.md)、9 月 27 日 Day 1 和 9 月 28 日 Day 2 记录，以及 Wiki 已有来源指纹重建。

| 槽位 | 候选问题 | 信息增益与选择 |
|---|---|---|
| 连续性 | `131Ce` 现有 crossing/alignment/signature 证据如何对应 CSM 与投影模型的能力，哪些观测才足以判别 γ-soft、wobbling 或 chirality？ | 选择。现有 project 将普通 signature/configuration coupling 排在较前，但目标带仍缺直接 `δ`/偏振、partner-resolved lifetime 与 absolute `B(E2)/B(M1)`；Day 3 要求的模型适用条件可直接约束下一步证据需求。 |
| 新颖性 | 粒子数投影对截断 PSM 的改善是否单调、能否直接消除 pairing-related spuriosity？ | 选择。用 Hara–Sun 的 `156Er` Figs.26–27 检查另一个核区/方法失效模式，与 `131Ce` 的集体模式问题不共享目标数据。 |
| 暂缓 | 重开 `130Sn/132Sn` 壳隙与数据字段谱系。 | Day 2 的高信息缺口已记录；与本日模型适用性练习不重叠，留在 Day 2 continuation 路线，避免把不同观测问题塞进本日。 |
| 续接延伸 | 现代 A≈130 TPSM 对邻近 odd–odd 核的实际可检验量是什么，能否验证历史 `N=76/78` 候选或 `131Ce`？ | 继续检索并选 Bhat et al. 2014 `124,126,130,132Cs` 作为方法迁移控制。该文确有 `130Cs` 计算，但目标为 `Z=55,N=75`，不覆盖 Hara–Sun 的相关核素，也不是 `131Ce` 数据；其信息增益在于区分绝对强度计算与既有相对比值。 |

来源 fingerprint 有意使用 Wiki 已有的 AFN90 与 HARA95 两篇理论综述，因为这是矩阵规定的 Day 3 主线；不把综述当作两条独立实验。续接的 Bhat 2014 是新检索到的理论模型/data-comparison 论文，其 arXiv v1 与期刊 DOI 分层记录；它沿用早先实验，不算新实验。Alwaleedi `131Ce` 论文仅作目标核的既有观测边界，不在本续接中重复摄入。

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

## Sources and evidence

| 证据层 | 本日核对 | 精确来源位置与状态 |
|---|---|---|
| 实验直接报告（目标核背景） | Alwaleedi 2013 建立/扩展 `131Ce` Bands 1–7，并用角强度比、crossing/alignment 与准粒子 Routhian 约束谱学。Table 5.1 报告 Band 1 两 signature 的 crossing frequency `0.329`、`0.367 MeV/ℏ`。这些是能级/跃迁分析量，不是独立测得的形状或集体模式。 | [Alwaleedi 2013 source page](../../knowledge/sources/alwaleedi-2013-band-structures-131ce.md#key-results)：`AW13-1`, `AW13-5`; 本次沿用既有 source 页的 PDF/Table locator，没有重新声称复核整篇原始 thesis。 |
| 实验派生量与缺项 | 论文的 `B(M1)/B(E2)` 由 branching 和能量推得并假设 `δ=0`；source page 记录本数据集缺寿命、absolute `B(E2)`、偏振和直接形状测量。 | 同上：`AW13-9`（Eqs. 5.6–5.7、Table 5.4），`AW13-11`（Chapters 3–5 数据/方法 inventory）。对应的现有证据排序见 [131Ce/133Ce project](../../knowledge/projects/131ce-collective-mode-discrimination.md#evidence-available)。 |
| 作者解释 / 历史模型归类 | Hara–Sun §5.1 的 Table 5 把若干 `N=76/78` 情形列为“presumably triaxial”，归因是轴对称 PSM 无法复现实验；p.713 明说当时程序采用轴对称系统，需三轴投影代码确认。表中 `131Ce` 是 `Z=58,N=73`，`N=73` 栏为 prolate `+0.22` 的模型分类；不能把 `N=76/78` 的候选标签转移给 `131Ce`。 | [Hara–Sun 1995 source page](../../knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md#key-results)：`HS10-4`; 原文 §5.1 Table 5，PDF pp.712–713。此处形状为作者/模型判断，不是直接形状测量。 |
| 理论模型结果 | Åberg 等 Fig.12 展示 `132Ce (π,α)=(+,0)` 在 `ℏω=0.47,0.59 MeV` 的 cranked Routhian surfaces；图注将 `β₂≈0.40` prolate 极小与两个中子占据 `i13/2` 联系，并把另一处局部极小与 `h11/2` 中子对 alignment 联系。Hara–Sun 的 `156Er` Figs.26–27 比较不做/做粒子数投影的 band diagrams；投影改变 backbending，并使最低 `qp`-pair 态更靠近 yrast。 | [Åberg–Flocard–Nazarewicz 1990 source page](../../knowledge/sources/aberg-flocard-nazarewicz-1990-mean-field-shapes.md#key-results)：`AFN90-2`，Fig.12 / PDF p.468；[Hara–Sun source page](../../knowledge/sources/hara-sun-1995-projected-shell-model-high-spin.md#key-results)：`HS10-5`，§4.3 Figs.26–27 / PDF pp.700–701。均为模型计算，不是实验观察。 |
| 续接：现代 TPSM 邻核方法控制 | Bhat et al. 2014 用三轴 Nilsson+BCS、三维角动量投影和多组态混合计算四个 odd–odd Cs；`130Cs` Fig.3 比较已有能级，Fig.8 的绝对 `B(E2)`/`B(M1)` 曲线是模型输出，实测比较主要是先前发表的 `B(M1)/B(E2)` ratios。作者要求对 `124,130,132Cs` 进行寿命测量后再确认 chiral interpretation。 | [Bhat et al. 2014 source page](../../knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md#key-results)：`BHA14-1`, `BHA14-3`–`BHA14-5`；Eqs. (1)–(3), Fig.3, Fig.8, Conclusion / arXiv PDF pp.3–6, 11, 13。它是模型比较论文，引用的实验不是本轮新增或独立重测。 |
| 续接：`130Cs` primary experiment | Simons et al. 用 Euroball IV 扩展 bands A/B；Tables 1–2 记录能级、相对强度、multipolarity、DCO 和偏振。四条 interband links 的磁偶极/偏振证据被作者用于确认同宇称/组态。 | [Simons 2005 source page](../../knowledge/sources/simons-2005-130cs-chiral-structures.md#key-results)：`SIM05-1`–`SIM05-4`；Tables 1–2, Fig.1, Eqs. (2)–(3), PDF pp.3–7。直接实验事实与“chiral”模式解释分栏。 |
| 续接：`130Cs` 派生观测与竞争解释 | `S(I)` 在 I≈12 后大致平滑；`B(M1)/B(E2)` 与 in/out 比值有部分、但非全套 chiral-like staggering；band B 缺少预期的 `B(M1)/B(E2)` staggering。能级差在中自旋约 160 keV；I≈16–17 crossing 的 h11/2 neutron-pair 归因是作者/模型解释。论文没有 `130Cs` lifetime/absolute strengths，并要求寿命测量。 | [Simons 2005 source page](../../knowledge/sources/simons-2005-130cs-chiral-structures.md#key-results)：`SIM05-5`–`SIM05-7`；Figs.4–7、Conclusion / PDF pp.9–12。Bhat 2014 Ref. [32] 就是这组 Simons 数据，属于依赖性模型复用，不是第二次实验。 |

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

Fig.3 (PDF p.6) 比较四个 Cs 核的 TPSM 与先前报告能级；Fig.8 (PDF p.11) 对 `130Cs` 显示 TPSM 计算的绝对 `B(E2)`、`B(M1)` 和 interband strengths，叠加的是 Ref. [32] 报告的 `B(M1)/B(E2)` ratios。结论说 `130Cs`/`132Cs` 的结果呈现 chiral-like 选择规则，但同时要求寿命测量；因此它只能支持相邻 odd–odd 核的模型可行性，不能替代 `131Ce` 的 absolute-strength 数据，也不能验证 Hara–Sun 的 `N=76/78` 案例。

## Counter-evidence and missing companion observables

- 对“轴对称计算失败即证明三轴”的反证是原作者自己的边界：Table 5 的 `N=76/78` 是暂定模型标签，p.713 要待三轴投影验证；而该表给 `131Ce (Z=58,N=73)` 的是模型 prolate `+0.22`，不是 N=76/78 标签。未来的现代投影计算或不同配对/组态空间若拟合同一数据而不需三轴，将削弱历史解释。
- Hara–Sun p.712 说明 doubly-odd level density 约为 odd-mass 核的十倍，不同配置在低能区可有近似相等的波函数权重；shell filling 与选取组态会显著影响结果。这使“轴对称拟合差”也可能受模型空间/组态敏感性影响。
- 粒子数投影的 `156Er` 方法学反例是数量级/方向上的，而非 `131Ce` 实验证据：投影能改变 backbending，但最低受污染 `qp`-pair 态更靠近 yrast；有限空间里 spurious 态不会因增加投影而必然自动消失。
- 对 `131Ce` 集体模式必须补的伴随量仍是目标跃迁的 measured `δ` 与偏振、伙伴带分别解析的 lifetime 和 absolute `B(E2)/B(M1)`/`Q_t`、可靠 interband links 与 band identity；若使用形状解释，还需独立形变敏感 observable。邻核模型值不能代替目标核测量。
- **证据独立性：** 两篇理论综述不是两次独立实验；Hara–Sun 的 Table 5 汇总早期 A≈130 实验与模型比较，本轮未回到其 refs.70/72 的原始实验逐项审计。Alwaleedi 的 Band/crossing 与 `δ=0` 比值属于一个目标核数据集；其派生值不能按 observable 行数重复计权。
- Bhat TPSM 控制进一步显示：`130Cs` 的绝对 `B(E2)`/`B(M1)` 图是计算，已测输入主要是文献报告的能级和 intensity-derived `B(M1)/B(E2)` 比值；该论文明确要求对 `130Cs` 等核做 lifetime measurements。它不能作为绝对跃迁强度的独立实验支持，更不能跨核填补 `131Ce`。
- Simons 2005 primary experiment 确认了四条带间 link 的 DCO/偏振与 M1 character；同一数据集的 band-B ratio 没有预期 staggering，绝对 lifetime 仍缺。这既支持 same-parity band link，也限制静态 chirality 的强结论；Bhat 2014 Ref. [32] 重用该 Euroball 数据，不是第二项实验。
- Bhat arXiv v1 的 Eq. (3)+Table 1 数值复算与其 PDF p.6 “γ≈30°”概述不一致。此处保留 `needs_review`，不据此替作者指定 γ，也不把形状参数当实验测量。

## Knowledge Impact and Learning Decision

**决定：`revises` 模型卡的可复核程度，并 `limits` 历史三轴解释和跨核 TPSM 推理的迁移。** 投影核方程、number-projection 反例、Bhat TPSM 与 Simons primary 共享数据 lineage、以及 `130Cs` 的 ratio-only lifetime boundary 已固化到知识页。Simons 的直接 DCO/偏振支持 `130Cs` 两带链接；mixed ratio pattern 和 lifetime 缺口仍限制模式结论。TPSM 在邻近 Cs 核有可用性，不构成对 `131Ce` 的直接观测；参数映射冲突仍保留。`131Ce/133Ce` project 模式排序不变：普通 signature/configuration coupling 仍是当前较节约的基线，γ-soft 是模型辅助背景，目标核 wobbling/chirality 仍缺关键电磁链。

## Durable knowledge delta

- 更新 [A≈130 high-spin model-choice card](../../knowledge/projects/a130-model-choice-card.md#theoryanalysis-exercise)：新增 Eq. (2.7)、Eqs. (2.19)–(2.20) 的投影核重构和基于原文 Figs.26–27 的有限空间反例；同时明确 Hara Table 5 的 N=76/78 triaxial candidate 不适用于 N=73 `131Ce`。这是可复用的模型输入/输出、计算式与迁移边界，review 状态仍是 `unreviewed`。
- 在 [131Ce/133Ce project](../../knowledge/projects/131ce-collective-mode-discrimination.md#related-sources-and-pages) 增加模型卡回链与 `N=76/78`→`131Ce N=73` 迁移边界；没有改变原有模式排序或 review 状态。
- 新增 [Bhat et al. 2014 TPSM source](../../knowledge/sources/bhat-2014-tpsm-cs-doublet-bands.md#key-results) 和 [TPSM model page](../../knowledge/models/triaxial-projected-shell-model.md#known-limitations) 关系；保存 `130Cs` 绝对强度是模型量、相对比值来自既有引用数据，以及 `ε/ε′→γ` arXiv-v1 参数边界。
- 将该源接入 [A≈130 model-choice card](../../knowledge/projects/a130-model-choice-card.md#model-to-observable-locator-crosswalk) 与 [`knowledge/index.md`](../../knowledge/index.md)。本次涉及的 knowledge pages 均维持 `unreviewed`，未更改 `131Ce` 模式排序。
- 新增 [Simons 2005 primary `130Cs` experiment](../../knowledge/sources/simons-2005-130cs-chiral-structures.md#key-results)，并回链到 Bhat Ref. [32]、TPSM model、model-choice card 和索引；核实两篇论文共享同一 Euroball experiment，不重复计权。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/projects/a130-model-choice-card.md",
      "summary": "补入 Hara–Sun 投影算符及 Hamiltonian/norm kernels 的广义本征练习；将单态能量比值限定到单组态极限；用 Fig.26–27 细化粒子数投影与截断态污染边界，并隔离 Table 5 N=76/78 标签与 N=73 131Ce。",
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
      "summary": "链接 131Ce project 到 Day 3 模型选择卡，并隔离 Hara–Sun N=76/78 历史候选与 131Ce N=73 的适用边界；不改竞争解释排序。",
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
    }
  ]
}
```

## Open questions and belief revision

- 后续最高信息增益路线：核对 Bhat arXiv v1 与期刊最终版的 Table 1/Eq. (3) 形变参数映射，并回读 Bhat Ref. [18] `126Cs` primary lifetime paper；`130Cs` Ref. [32] 已确认是 Simons 2005 Euroball experiment，仍保留 ratio derivation/absolute-strength boundary。
- Hara–Sun 的具体 N=76/78 核素是否已有后续 TPSM/其它三轴代码直接计算，仍需逐核素搜查；Bhat 2014 的 Cs 链只给方法邻核控制，不能闭合该路线。
- `131Ce` 的优先缺项仍是目标跃迁的 measured `δ`/偏振与伙伴带绝对强度。获得这些后，才值得把 CSM/QTR、TPSM/投影混合与 γ-soft 模型放在共同观测集上比较。
- **belief revision：** 原先把角动量投影的单态能量比值当作普遍表达式；原文重读后确认它只是单组态极限，多组态时必须保留非正交 norm kernel。也修正了两个迁移错误风险：N=76/78 的候选不等于 N=73 `131Ce`；增加粒子数投影不保证截断空间的 spurious admixture 自动消失。

## L0–L4 state

- **L0：complete for the bounded TPSM/130Cs lineage.** Crossref/OA metadata 与两份本地 PDF 哈希核对；Hara–Sun、ABFN 原文关键公式/图表；Bhat arXiv v1 与 Simons 2005 primary `130Cs` reaction, Tables 1–2, Figs.1,3,5–7, conclusion 已核。
- **L1：updated.** 新建 Simons source page；更新 Bhat source lineage、TPSM model page、A≈130 model-choice card 和 `knowledge/index.md`。页面保持 `review_status: unreviewed`；BHA14-6 γ parameter mismatch 与绝对 strength boundary 保留 claim-level `needs_review`。
- **L2：complete for selected and continuation exercises.** 完成主动回忆、投影核推导、HF/HFB—CSM—AMP/PSM route matrix、`ε′/ε→γ` 数值复算、DCO/polarization-to-assignment review、模型/实测 ratio/绝对强度分层、反证与 companion-observable 设计。
- **L3：candidate / ongoing。** 模型选择卡支持 `131Ce` 项目的后续比较，但本日没有新增目标核原始实验、没有重算竞争模式权重；继续路线见上文。
- **L4：not-ready。** 没有目标核事件级数据、完整响应/校准协方差、可运行模型代码和同一输入下的模型比较包；未生成代理拟合或模型结果。

## Verification and continuation

- 入口和本续接新增 raw/source 路径前 `wiki_boundary_check.py --root .` 均 exit `0`；`wiki_automation_preflight.py --root .` exit `0`，受保护 BibTeX SHA-256 匹配。首写前 EOL 清理计数均为 0。写入后 `clean_knowledge_eol_dirty.py` exit `1`：保留三页本轮 tracked knowledge substantive 修改（model-choice card、TPSM model、index），`refreshed=0, restored=0, would_restore=0, staged-not-touched=0, unsafe/mixed=0`；新增 source page 是本轮新文件，未被清理/回滚。
- 写入后 `wiki_boundary_check.py --root .` exit `0`（errors/warnings 均为0）；`wiki_lint.py --fail-on error` exit `0`，`errors=0, warnings=86, info=1218`；writeback validator exit `0`，`valid=true`, `status=updated`，changed knowledge paths 正好为 index、TPSM model、model-choice card 与 Bhat/Simons 两 source pages 五页；日报标题/机器块与 run.json JSON parse 检查 exit `0`；`git diff --check` exit `0`。
- 剩余 86 个 Wiki warnings：`CITATION_KEY_MISSING=82`、`REACTION_PARSE=3`、`RAW_GIT_CHANGE=1`。两篇新理论/实验 source 的 citation key 均未在受保护 BibTeX 找到，不推测或添加；raw warning 仍指向继承的 Day 2 `raw/papers/gpt/day2-shell-gap-20260928/` 文件包。Bhat 与 Simons OA PDFs 留在本地 raw 副本，未暂存；没有 `ORPHAN_PAGE` warning。
- 本 continuation 的原入口回执 `run-01` 保留服务高负载失败事实；当前续接回执与下一条恢复路线写在 `20260929-DAY3-mean-field-nilsson-csm-hfb-projection-run-03/`。该路径与窗口截止时间均以 prompt 注入值记录。
- 当前 Bhat/Simons cross-source continuation 的精确 staged path、`git diff --cached --check` 与新 checkpoint H3 发布仍待完成；首个 Day 3 checkpoint commit 已推送。Day 3 仍是 continuation-pending，不推进 state file。
- QMD refreshed：`qmd update` exit `0`（16 new, 11 updated, 523 unchanged, 0 removed; 清理 11 个过期 content hashes）；`qmd embed -c nuclear-knowledge --timeout 30` exit `0`（212 chunks / 27 docs，18m31s）。最终 `qmd status` 报 550 documents、2,459 vectors，并留有 174 orphaned embedding chunks（7%）；未运行 `qmd cleanup`，避免把与本知识修改无关的索引回收并入本任务。
