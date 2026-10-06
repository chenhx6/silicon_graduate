# 2026-10-05 Day 6 — 转动、振动、alignment 与 signature

## Run state

- 计划：Day 6，nuclear-structure-framework；运行标识 2026-10-05-day-06-01；study window 截止 2026-10-06 15:00（Asia/Shanghai）。
- 恢复：原 session 01a10816-f550-7003-bb53-8dfafc2c18a2 在用户要求停止后留下 interrupted 回执；本轮按用户指令恢复该 session。恢复命令：codex resume 01a10816-f550-7003-bb53-8dfafc2c18a2 -C /workspace/wiki -s danger-full-access -a never。
- run-01 事件日志显示停止前已读计划和近期记录、完成主动回忆、核读 Liu 1996 全文并检查 Fig. 15；没有日报或知识写回。该中断不计作 Day 6 完成。
- completed_day_indices: [6]
- partial_day_indices: [7]
- Day 6 card audit: complete
- Day7 preview 未计入本次完成卡；user decision: closed DAY6 at 2026-10-06 12:55 Asia/Shanghai and retained Day7 as the next official card. Day8 is outside this run's scope.
- **收束状态修订：** run-06 把两槽局部证据饱和当成全日停止条件，这是过早的时间判断。随后按新时间门检查后，DAY6 续接继续到 Day7 preview。用户约于 `2026-10-06T12:55+08:00` 明确要求现在完成 Day6 收束、Day7 留作下一张正式日卡；本次收束记录时间为 `2026-10-06T13:23:13+08:00`，距原定硬截止 `2026-10-06T15:00:00+08:00` 尚有 97 分钟。下方 Day7 回忆、能带判读和自评分只保留为不计学分的准备材料；本次按用户指示停止学习，不推进或开展 Day8。DAY6 的报告、AW13/LU96 知识写回、必需检查、Day7 提示和 run-06 Gitee 发布门已通过；最终课程状态收在 `next_day_index=7`。

### Day 6 card completion audit

| 日卡交付项 | 可复核证据或产物 | 状态 |
|---|---|---|
| 回忆 rotational/vibrational band、alignment 与 signature | 本报告“来源前主动回忆”及 Day7 预览回忆 | complete |
| 主线来源与关键图表/公式 | [Stephens 1975](../../knowledge/sources/stephens-1975-coriolis-rotation-alignment.md) ST75-1–3；[Liu 1996](../../knowledge/sources/liu-1996-signature-inversion-a130.md) LU96-1–5；[Alwaleedi 2013](../../knowledge/sources/alwaleedi-2013-band-structures-131ce.md) AW13-1–19 | complete |
| 自旋—频率与 alignment 定量练习 | AW13-18 Eq. (2.25)/Table 4.1；MA90-5 Eq. (2) Harris 参考转子复算 | complete |
| signature inversion 与 crossing 的反证/替代解释 | LU96-4/5；ST75-2/3；AW13-11；保留自旋锚点、组态混合和 `δ=0` 边界 | complete |
| alignment/signature 判读卡与带结构图 | 本报告两张重建表及 [A≈130 thesis evidence matrix](../../knowledge/projects/a130-thesis-evidence-matrix.md) crosswalk | complete |

## Candidate pool and selection

| 候选 | 近期香港覆盖与预期信息增益 | 选择 |
|---|---|---|
| 连续性：131Ce Bands 1–7 的 signature/configuration coupling 能否与振动或其它集体模式区分？ | 当前开放问题要求 mixing ratio、偏振、寿命和伙伴带绝对强度；Day 3 已整理 mean-field 与模型适用边界，Day 4 已覆盖 pairing/crossing，Day 5 已覆盖形状观测量。Day 6 的转频重建可把能级证据接到可测的模式判据。 | 选。沿用现有 131Ce 项目与原始 thesis 数据，不新建重复项目。 |
| 新颖性：A≈130 奇奇 h11/2 带的 signature inversion 对 bandhead spin crosswalk 有多敏感？ | Liu 1996 汇集 La/Pr/Pm/Eu/Cs 多核素，展示奇数 ΔI 重标可改变 signature 顺序；Cs 的相互冲突参考为独立于 131Ce 的系统学边界。 | 选。只研究自旋锚点和系统学，不把不同核素拼成 131Ce 的直接证据。 |
| Band termination 判据 | Afanasjev 1999 提供固定组态、有限最大自旋和 collectivity 衰减的综述判据。所选 131Ce 带没有本轮可核的 termination 端点。 | 作为练习的边界参照，不另开第三个案例。 |
| Day 7 准备预览：[集体运动口试](../plans/2026-09-22-one-month-daily-task-matrix.md) | 在较长 DAY6 窗口中预演 Day1–6 回忆与 131Ce 证据链；用户随后明确保留 Day7 作为下一张正式日卡。 | 仅预览；`partial_day_indices=[7]`，不计课程学分。 |

**来源前主动回忆：** 转动带是同一内禀结构上随角动量增加的能级序列，低自旋时常以 I(I+1) 作为理想参照；振动带对应形变自由度的量子振荡；alignment 是准粒子角动量沿转轴的投影，数值依赖转频和参考转子；signature 是转 π 的离散对称标签，signature inversion 表示两支能量偏好随自旋反转。我记得 131Ce Band 1 的两支 crossing 约为 0.329 和 0.367 MeV/ℏ，但不确定 Table 5.1 的误差，也不确定能否从现有来源得到逐点 i_x(ω) 或 termination 证据。后续核到的表值、定位和误差见下节。

## Sources and evidence

| Wiki 来源与原文 locator | 证据层 | 本轮核实及边界 |
|---|---|---|
| [Davidson 1965](../../knowledge/sources/davidson-1965-rotations-vibrations-deformed-nuclei.md)：DV65-1，printed pp.105–146；DV65-2，printed pp.129–146。DOI [10.1103/RevModPhys.37.105](https://doi.org/10.1103/RevModPhys.37.105)。 | 集体模型综述 | 形变表面坐标量子化为振动 phonon，稳定形变产生转动带；odd-particle、Coriolis 和 decoupling 改变能带系统学。它是理论背景，不是 131Ce 的观测证据。 |
| [Stephens 1975](../../knowledge/sources/stephens-1975-coriolis-rotation-alignment.md)：ST75-1，PDF pp.43–44 Eq. (1)；ST75-2，Secs. II–III；ST75-3，Sec. IV。DOI [10.1103/RevModPhys.47.43](https://doi.org/10.1103/RevModPhys.47.43)。 | Coriolis 与 alignment 综述 | Coriolis coupling 可混合邻近 K 带并改变 alignment、signature 和 backbending；blocking、配对和形变共同影响 crossing。它没有唯一指定某个 crossing 的组态。 |
| [Alwaleedi 2013, 131Ce](../../knowledge/sources/alwaleedi-2013-band-structures-131ce.md)：AW13-14/16/19/20/21，Table 4.1/4.2/4.4；Figure 4.1/4.5；§4.3.1、§5.2.1；AW13-5、AW13-4、AW13-9、AW13-11、AW13-18。DOI 10.17638/00015073；PDF SHA-256 B50C22877418DE560F06002588BB46D34F5BA670C6880E30A89D1509C79AD8C1。 | 直接能级/连接、派生 crossing、作者组态解释 | 同一 Gammasphere acquisition 的六条带间支路是：Band1→4 的 504.9-keV M1/E2（25/2−→23/2−）和 871.2-keV E2；Band4→1 的 538.3-keV M1/E2（15/2−→13/2−）和 611.1-keV M1/E2；Band4→yrast 的 994.3/1108-keV E2。505-keV Figure 4.5 峰对应 Table 4.2 的 504.9-keV 行。表中 R 不是 δ；没有逐线 measured δ/偏振、lifetime 或绝对强度。 |
| [Liu et al. 1996](../../knowledge/sources/liu-1996-signature-inversion-a130.md)：LU96-1，Tables I–II；LU96-2，Fig. 15；LU96-3，PDF pp.729–730；LU96-4，Table II；本轮新增 LU96-5，PDF p.729 Sec. VI.C。DOI [10.1103/PhysRevC.54.719](https://doi.org/10.1103/PhysRevC.54.719)；本地原文 SHA-256 为 ca3e1c1bc834158112dee525fa4c42c3d44596975a506f3a2a1da023580a346f。 | 已发表能级的系统学重标；独立模型计算 | Table I 中 13 个已有 bandhead spin 指认有 11 个被修改，且这 11 个改变量都是奇数；Fig. 15 在作者新指认下显示讨论核素的低自旋 signature inversion。Table II 对 Cs 保留不相容方案。Liu 汇编旧实验而非新 acquisition；Tajima 的模型参数拟合过 124Cs、I0=7 的同一参考，不能当作该自旋锚点的独立验证。 |
| [Ma et al. 1990, 131Ba](../../knowledge/sources/ma-1990-131ba-competing-alignments.md)：MA90-2，PDF pp.725–728 Figs. 5–7/Table II；MA90-5，PDF p.725 Eq. (2)/Fig. 5。DOI [10.1103/PhysRevC.41.717](https://doi.org/10.1103/PhysRevC.41.717)；原文 SHA-256 为 a0dbdd4957d1d11af570b5daffc9c44609d9ef5ed570dc3ad32a67388dad90de。 | 不同核素的直接谱学与派生 alignment | 131Ba 的 crossing 与 Harris alignment 作方法对照。其 119Sn(12C,4n) 实验与 131Ce Gammasphere 谱不同，不能当成 131Ce 的独立验证。 |
| [Afanasjev et al. 1999](../../knowledge/sources/afanasjev-1999-termination-rotational-bands.md)：AF99-1，PDF pp.4–7、33–39；AF99-2，PDF pp.33–40、43–95。PII S0370-1573(99)00035-6。 | 终止转动综述 | termination 指固定组态的集体转动连续走向该组态有限的最大 aligned spin；须联合能量、alignment、转动惯量和 Q_t/B(E2) 变化，排除 crossing、混合及统计不足。未在本轮 131Ce 序列上判定 termination。 |

**网络与原文核验：** Crossref 返回 Liu 的作者、题名、期刊、卷期页码和 DOI，与本地 PDF 一致；出版商 APS abstract URL 返回 HTTP 403。Google Scholar 检索请求失败，未把检索结果用于证据。论文主文 PDF 在仓库内可读，Liu 页 719–730 已沿摘要、spin-systematics 方法、La/Pr/Pm/Eu 与 Cs 赋值、Tables I–II、Figs. 1–15、模型比较和结论通读；Fig. 15 图像已渲染目视核查。原文特别说明 124Cs 的 I0=7 与 130Cs 的 I0=9 不能同时成立，并给出 130Cs I0=11 的另一方案。

## Theory/analysis exercise

**概念判读。** 转动序列通常依赖共同的形变内禀结构，能量可近似随 I(I+1) 增长；振动序列来自 β/γ 等形变自由度的量子激发，需用多声子能量和跃迁强度模式检验。仅有规则能级、近简并或高自旋 crossing 都不足以把带命名为振动、wobbling 或 chirality。alignment 描述准粒子对总角动量的贡献；signature splitting/inversion 描述按 signature 分支整理后的相对能量变化，不是唯一机制的标签。

**从 131Ce Table 4.1 重建自旋—转频点。** 原文 Eq. (2.25) 对 ΔI=2 转移定义 ℏω=Eγ/2，频率位置取跃迁自旋中点。将 Table 4.1 的 Eγ 从 keV 换成 MeV，得到一支 Band 1 序列：

| 跃迁 | 中点自旋 | Eγ | ℏω=Eγ/2 |
|---|---:|---:|---:|
| 15/2→11/2 | 13/2 | 507.9 keV | 0.25395 MeV |
| 19/2→15/2 | 17/2 | 641.2 keV | 0.32060 MeV |
| 23/2→19/2 | 21/2 | 749.3 keV | 0.37465 MeV |
| 27/2→23/2 | 25/2 | 825.4 keV | 0.41270 MeV |
| 31/2→27/2 | 29/2 | 780.6 keV | 0.39030 MeV |
| 35/2→31/2 | 33/2 | 691.4 keV | 0.34570 MeV |

频率随跃迁中点自旋上升至 25/2 后下降；Table 4.1 未给这些 γ 能量的不确定度，故只报中心值。该走势提示能带偏离简单刚性转子系统学，但单个转移序列不定位 crossing 来源。Table 5.1 另从实验 Routhian 提取 Band 1 两个 signature 的 crossing：0.329±0.002 和 0.367±0.002 MeV/ℏ。它们不是由单个 Eγ/2 点直接算出；表中未给两 crossing 的协方差，故不计算差值误差。Table 5.1 的 Band 2 两 signature 都列 0.316±0.002 MeV/ℏ，但其负宇称标签与 Figure 4.1、Tables 4.5–4.6、§5.2.2 冲突，本轮隔离该 parity 单元，不据此得出结论。

**alignment 参考项复算。** Ma 1990 Eq. (2) 的参考转子为 I_ref=J0ω+J1ω³，J0=11.90 ℏ² MeV⁻¹，J1=21.1 ℏ⁴ MeV⁻³；用 x=ℏω（MeV）后，I_ref/ℏ 的数值表达式为 11.90x+21.1x³。将作者报告的 131Ba 两 signature crossing 代入，得：

| ℏω | I_ref/ℏ | 仅传播报告的 crossing-frequency 误差 |
|---:|---:|---:|
| 0.415±0.003 MeV | 6.447 ℏ | ±0.068 ℏ |
| 0.445±0.003 MeV | 7.155 ℏ | ±0.073 ℏ |

微分使用 d(I_ref/ℏ)/dx = 11.90+3×21.1x²；J0/J1 拟合协方差未在 source page 给出，表中误差只来自 crossing-frequency 项。I_ref 是参考转子角动量，不是总自旋，也不是独立测量的 alignment gain；完整 i_x 还需同一频率下的带自旋和一致的参考。

**band termination 判据。** 需要固定组态下可追踪的有限最大 aligned spin，并同时看到转动/能级斜率、alignment、moment of inertia 与 Q_t 或 B(E2) 的相容演化；低强度末端跃迁、能带突然中止或单个 backbend 都不能单独证明 termination。AF99 的例子属于综述系统学和模型解释，不将其外推为 131Ce 的已观测终止带。

**Day 7 口试：前六日主动回忆（先于本轮来源回看）。**

1. Day 1：claim 要有原文 locator；实验事实、作者解释、模型结果和本任务推断分开，重复论文/学位论文不自动成为独立证据。
2. Day 2：壳隙与单粒子轨道随核素和形变背景而变；转移强度/角分布是轨道占据与结构的观测约束，不能把模型轨道图当作直接观测。
3. Day 3：Nilsson 描述形变平均场单粒子结构，CSM 加入转动框架与 alignment，HFB 处理平均场配对；投影恢复被近似破坏的对称性。模型谱与实验能带要分层对照。
4. Day 4：配对、blocking 与准粒子破对会改变 crossing 和 alignment；能谱 backbend 是现象，不唯一指定哪一种准粒子组态。
5. Day 5：β、γ 和八极自由度须由各自合适的电磁/形变观测量约束；同核存在不同形变带不等于已证明这些带互为 shape-coexisting partners。
6. Day 6：signature 是离散转动对称标签，signature inversion 是两支能量顺序改变；alignment 依赖频率和参考带，crossing/近简并本身不能证明振动、wobbling 或 chirality。

回看 [Day 1](../20260927-DAY1-baseline-research-contract.md)、[Day 2](../20260928-DAY2-shell-gap-single-particle.md)、[Day 3](../20260929-DAY3-mean-field-nilsson-csm-hfb-projection.md)、[Day 4](../20260930-DAY4-pairing-quasiparticle-configuration.md) 和 [Day 5](../20261003-DAY5-beta-gamma-octupole-shape-coexistence.md) 日报后，未发现足以推翻上述定义的错误；Day 4/5 的实际反例进一步加强了“带标签不能替代伴随观测”和“同一数据集转载不算独立证据”两项检查。

**131Ce 已读案例的完整证据链口述。**

- **壳结构/形变层：** Alwaleedi 2013 用 Woods–Saxon/TRS 与 CSM 讨论粒子组态和形变背景；作者采用的 `β2=0.218, β4=−0.023, γ=0°` 是模型输入/极小值，不是实验直接测形变（AW13-6）。Band 1/4 的负宇称 `νh11/2` 类轨道指认仍属组态解释（AW13-8）。
- **直接谱学层：** 100Mo(36S,5nγ)、165 MeV、Gammasphere 建立/扩展 Bands 1–7。AW13-14 的 Band1 507.9-keV E2 行为 15/2−→11/2−。完整六链接网络见上表：505-keV 是 Table 4.2 的 504.9-keV Band1→Band4 M1/E2 行（25/2−→23/2−）；Table 4.4/Figure 4.1 还显示 538.3-keV Band4→Band1（15/2−→13/2−），而 611.1-keV 也是 Band4→Band1。243.7-keV 才是同为 17/2−→15/2− 的 Band4 intraband transition。
- **alignment/signature 层：** 对 ΔI=2 行按 AW13-18 的 `ℏω=Eγ/2` 放在跃迁中点，Band 1 的频率先升后降；Table 5.1 的两个 signature crossing 为 `0.329` 与 `0.367 MeV/ℏ`（AW13-5）。跨带比较还依赖 band identity、spin assignment 和参考带，不能把派生量改称独立 alignment 测量。
- **作者解释/模型层：** CSM/TRS 讨论准粒子 crossing、spin-dependent core polarization 和可能的非轴响应；Band 4 被作者标为 γ-vibration-coupled `e/f` 序列（AW13-4/7）。这些是作者/模型解释，不等于已测得振动声子或 γ-soft 势面。
- **替代解释与裁决边界：** Coriolis mixing、signature partner、准粒子 alignment、配对/形变演化均可造成 crossing 或相似能谱（ST75-2/3）。论文没有 `δ`、线偏振、寿命、绝对 `B(E2)/B(M1)` 或 partner-resolved 强度闭合链（AW13-9/11）；因此现有最简解释仍是 signature/configuration coupling 主导，振动/摆动/手征不能升级为实验事实。

**未知短能带 20 分钟判读练习（以下描述完全为合成题，不对应核素/实验）：** 两条同宇称短序列各有若干 ΔI=2 γ 线；其中一条的 `Eγ/2` 随中点自旋先升后降，出现一个作者称为“交叉”的斜率变化；只报告一条两带间 ΔI=1 γ 线，multipolarity 未定；没有寿命、直接 `δ`、偏振或绝对强度。可以说：存在两条被指认为同宇称的序列、该条线的能量给出随自旋变化的运动学趋势、并有一个待核的带间连接。不能说：crossing 已由唯一组态解释、短带已终止、第二带必是 γ 振动伙伴，或这两带属于 wobbling/chirality。替代解释至少有 signature partner/准粒子 crossing、Coriolis mixing、配对/形变响应及未知门条件/feeding。停止条件是先核定自旋/宇称/带身份和 crossing reference；若无法取得 direct `δ`/偏振与匹配寿命/绝对强度，就保持 provisional，不对模式命名。

**最可能改变当前排序的证据：** 一套 branch-complete、partner-resolved transition matrix：对 504.9、538.3、611.1-keV M1/E2 links 测得有约定的 δ 和偏振，并与匹配自旋的 Band1/Band4 寿命组合得到绝对 B(E2)_out/B(E2)_in 及 B(M1)/B(E2)。若相邻自旋区间出现灵敏度已量化、可重复的 E2-rich interband strength pattern，collective-coupling 排序上升；若 M1 主导且 out-of-band E2 在校准灵敏度下受限，普通组态连接排序上升。单个 505-keV 几何连线不再是待确认的端点问题，R 也不代替 δ。

## Counter-evidence and missing companion observables

- Liu 1996 的结论随 bandhead spin crosswalk 变化：多数有旧自旋指认的 La/Pr/Pm/Eu 带中，11/13 个 I0 被改动且全是奇 ΔI；odd ΔI 会交换偶/奇自旋对应的 signature 标记。作者采用平滑同位素系统学支持改标，但平滑趋势本身是 systematics prior，不是新的直接自旋测量。
- Cs 仍无唯一锚点：文中称 124Cs I0=7 与 130Cs I0=9 无法同时满足平滑曲线，并列出 130Cs I0=11 的另一重建。Tajima 对 124Cs 的计算吻合不能解决此问题，因为模型参数拟合于同一 I0=7 数据。
- 131Ce 的 crossing/alignment 约束作者的准粒子组态解释，却不能单独区分 Coriolis mixing、配对/形变演化与振动响应。Band4 的 γ-vibrational 标签仍是作者解释；本论文已映射六条 Band1/Band4/yrast links，但没有逐跃迁 measured δ、线偏振、匹配 partner lifetime 或绝对 B(E2)/B(M1)。其他 131Ce lifetime sources 不提供 Band4 partner matrix，所以现有 gap 是电磁强度和 response/covariance，而非 505/611 link 的端点身份。
- 必要伴随量：可靠自旋/宇称与带身份、完整带间 links、混合比两个分支和偏振、匹配自旋区间的寿命与绝对 B(E2)/B(M1)，以及能支持形状判断的 quadrupole observable。测量后须用同一 transition matrix 区分 signature/configuration coupling 与集体振动；若讨论 wobbling/chirality，还需相应 out-of-band E2、伙伴身份和随自旋模式能量。
- 源独立性：Alwaleedi 是一套 100Mo(36S,5nγ) Gammasphere acquisition；Liu 是多篇旧谱学的汇编；Tajima 是独立模型路线但模型参数依赖 124Cs 的同一自旋假设；Ma 是 131Ba 的不同反应/实验，仅作 alignment 方法参照。
- Day 7 口试重复使用 AW13 不是第二份 `131Ce` acquisition；LU96 是既有 A≈130 多核素数据汇编，Tajima 与 `124Cs I0=7` 共用拟合锚点。当天 REFLECT 只改变学习者的证据分层检查，不新增独立实验权重。

## Knowledge Impact and Learning Decision

**DAY6 decision: revises。** 对 A≈130 signature-inversion crosswalk 的知识边界作了窄幅修订：除 `I0` 重标和 Cs 参考未决外，加入“模型与其拟合锚点共享 `124Cs I0=7`，因此不能独立验证该锚点”的来源定位。对 `131Ce` 的排序维持：已有能级、crossing 和作者组态解释支持普通 signature/configuration coupling 为可行基线；尚无寿命/偏振/partner-resolved 绝对强度，不能把带标签升级为振动、wobbling 或 chirality 的实验结论。

**DAY7 preview reflection: provisional no material change。** 这次预演没有发现与已有 source/project 知识冲突的新直接证据；这些反思只作准备材料，不替代正式 Day7 口试、评分和 weekly REFLECT。

## Durable knowledge delta

- [Liu 1996 source page](../../knowledge/sources/liu-1996-signature-inversion-a130.md)：新增 LU96-5，记录 Tajima 的 Cs 参数拟合依赖和非独立 spin-anchor 边界。
- [Alwaleedi 2013 source page](../../knowledge/sources/alwaleedi-2013-band-structures-131ce.md)：新增 AW13-18，保存原文 Eγ/2 转频定义和 Table 4.1 的跃迁中点自旋—转频复算。
- [A≈130 thesis evidence matrix](../../knowledge/projects/a130-thesis-evidence-matrix.md)：修订 signature-inversion crosswalk 行，把同一 124Cs spin assignment 的拟合依赖纳入 evidence boundary。
- 复算表、来源依赖关系和停止条件同时写在本日报；可复用的转频复算与模型独立性边界已分别落入上述 source 和 project knowledge 页。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/sources/liu-1996-signature-inversion-a130.md",
      "summary": "Added the source-grounded caveat that Tajima's Cs inversion-spin agreement is calibrated on the same 124Cs I0=7 anchor and therefore is not an independent validation of that assignment.",
      "anchor": "LU96-5",
      "sources": [
        {
          "path": "knowledge/sources/liu-1996-signature-inversion-a130.md",
          "locator": "PDF p.729"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
      "summary": "Persisted the thesis rotational-frequency convention and the Band 1 transition-midpoint frequency reconstruction with the missing gamma-energy uncertainty boundary.",
      "anchor": "AW13-18",
      "sources": [
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "Eq. (2.25)"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "Table 4.1"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-thesis-evidence-matrix.md",
      "summary": "Revised the A≈130 signature-inversion crosswalk row with the model-to-spin-anchor dependence boundary.",
      "anchor": "A≈130 πh11/2⊗νh11/2 signature-inversion crosswalk",
      "sources": [
        {
          "path": "knowledge/sources/liu-1996-signature-inversion-a130.md",
          "locator": "LU96-5"
        }
      ]
    }
  ]
}
```

## Open questions and belief revision

1. 131Ce Band 1 的 0.329/0.367 MeV/ℏ crossing 在统一带身份、reference 和偏振/mixing 约定下是否仍保留？若测得的 interband links 具有稳定且增强的 E2 强度，并由寿命给出匹配的绝对 B(E2)，可提高集体振动/摆动解释；若 links 以 M1 为主并随 crossing/组态演化，则普通 signature/configuration 解释更合适。
2. 哪一项独立自旋/宇称测量能排除 Cs 中不相容的 124Cs/130Cs 参考？若独立测得的 I0 改变偶奇自旋交错，将重排 Liu 图 15 的 favored/unfavored 标记，signature-inversion 结论及其 γ 解释须重新计算。
3. 是否存在具备固定组态、可达最大自旋和连续 Q_t/B(E2) 数据的 A≈130 候选 termination 带？在这些观测闭合前，本轮只采用 AF99 判据，不作目标核判定。

4. 正式 Day7 开始时，能否在不看资料的条件下重新完成 Day1–6 定义回忆，并用 source locators 独立复述 `131Ce` 证据链？本次预览不预支该卡学分。

### Day 7 preview inventory — not credited

| 正式周考交付项的准备情况 | 可复核预览材料 | 本轮状态 |
|---|---|---|
| Day 1–6 定义回忆 | 本报告已写一次回忆草稿；正式 Day7 仍须重新闭卷回答 | preview only |
| `131Ce` 壳结构至竞争解释链 | 本报告 `AW13-1/4/5/6/8/11/14/16/18`、`ST75-2/3` 草稿 | preview only |
| 合成未知能带判读 | 本报告合成题；正式 Day7 应独立重做并复核停止条件 | preview only |
| 可能改变排序的证据 | AW13-16 direct `δ`/polarization→寿命和 absolute-strength 路线草稿 | preview only |
| 周考六项评分与 weekly REFLECT | 下方分数与反思为草稿，不作为正式评分或周考完成证明 | not credited |

### Day 7 preview self-score — not official

| 维度 | 分数（0–4） | 自评依据 |
|---|---:|---|
| 理论 | 3 | 能区分转动、准粒子 crossing 与振动解释；非轴集体模还需几何和跃迁强度闭合。 |
| 判图 | 3 | 能把 `Eγ/2` 放在跃迁中点并区分 band link 和同带线；本轮合成题无真实 level scheme。 |
| 误差 | 3 | 保留 AW13 Table 4.1 未报误差、crossing 参数协方差缺失及 Harris 参数协方差边界。 |
| 证据分层 | 4 | 实验 line/link、派生频率、作者的 γ-vibrational 指认和模型形变输入分开。 |
| 反证 | 3 | 列出 Coriolis、signature/configuration、pairing/shape alternatives；需 direct 电磁测量决胜。 |
| 可证伪问题 | 3 | 预览草稿把 611.1-keV 作为 Band4→Band1 link；原文支持这个方向。DAY7 第一版 erratum 错误地把它降为带内线，后续 raw-source audit 已纠正并补出 538.3-keV 第二条 Band4→Band1 dipole link。Day6 preview 不计 Day7 学分。 |

### Day 7 preview reflection — not official

- 本周核心进步不是多给模式贴标签，而是把“观测量→赋值→机制”拆成可检查层，并把来源共享实验、模型拟合锚点和统计不确定度一起写进证据权重。
- 常见错因：把 crossing 当作唯一组态证明；把 `R` 与 `δ` 混为一谈；把 TRS 的 `γ` 当成测得形状；把同一数据的学位论文/期刊重述当独立复核；把近简并或 signature inversion 当作 collective-mode 充分条件。
- belief revision：Liu 的 `I0` crosswalk 的来源依赖边界变清楚，`131Ce` signature/configuration baseline 更可复核；但没有新独立 `131Ce` electromagnetic observable，故不改变 `wobbling/chirality` 排名，也不提高 γ-vibration 的实验证据等级。
- 预览阶段的 overlap check 没有发现增量，但正式 DAY7 原文审计随后纠正了 AW13-16 的跨带身份；见下方 erratum。该预览错误不计入 Day7 完成结论。
- 下一张正式日卡保持 Day 7。以上口试草稿只作准备材料，Day7 运行应按提示词重新完成卡片并单独验收。

### Formal DAY7 erratum to this preview — 2026-10-06

A later Day7 erratum incorrectly demoted 611.1 keV, and this Day6 report repeated that mistaken classification. The complete raw-source audit now supersedes it: 611.1 keV is the Table 4.4/§4.3.1 Band4→Band1 M1/E2 link (17/2−→15/2−), while the separate 243.7-keV line with the same spin change is intraband; Figure 4.1/Table 4.4 additionally map 538.3 keV (15/2−→13/2−) as Band4→Band1. Figure 4.5's 505-keV peak corresponds to Table 4.2's 504.9-keV Band1→Band4 M1/E2 row (25/2−→23/2−), with endpoint assignment in the table. The complete network also includes 871.2-keV Band1→Band4 and 994.3/1108-keV Band4→yrast E2 branches. None supplies direct δ/polarization, lifetime or absolute strength. Day6 remains complete; its Day7 preview remains uncredited.

## L0–L4 state

- L0：写前 Wiki boundary check exit 0；保留原始 Liu/Ma/Alwaleedi PDF，不覆盖 raw。
- L1：本地全文、source page locators、Crossref 元数据和 publisher URL 状态已核对；Google Scholar/APS 的访问失败作为路由记录，未以摘要片段补结论。
- L2：完成 131Ce ΔI=2 跃迁中点的 Eγ/2 转频重建和 131Ba Harris reference 数值复算；能量行未报不确定度，Harris 拟合参数 covariance 缺失，按边界保留。
- L3：继续使用既有 131Ce collective-mode project 和 A≈130 thesis matrix；本轮没有新建研究问题或声称完成新 L3 milestone。
- L4：未进入。没有 event-level counts、共同 response/covariance package 和分析代码，不能做代理拟合或把派生曲线升格为原始实验事实。

## Verification and continuation

- 边界检查：写前运行 python3 system/scripts/wiki_boundary_check.py --root .，exit 0，errors=0、warnings=0。
- farmer：`wiki_farmer.py status` 显示原 session 有活动记录；`once --dry-run` exit 0，actions=[]。本次按用户明确指示收束现有 run，不启动重叠的 DAY6 runner。
- Wiki lint：python3 system/scripts/wiki_lint.py --fail-on error，exit 0，errors=0、warnings=91、info=1309。
- runner 语法检查：`python3 -m py_compile system/scripts/run_daily_learning.py system/tests/test_daily_learning_runner.py`，exit 0；`python3 -m unittest system.tests.test_daily_learning_runner -v`，exit 0，35 tests passed。
- 日报/课程解析：必需标题均存在；最终课程解析通过，`completed_day_indices=[6]`、`partial_day_indices=[7]`、下一个正式日卡为 7；状态文件保持 `next_day_index=7`。
- `git diff --check` exit 0；继承的 run-01 事件/回执、旧 DAY6 prompt 与 raw/tmp 材料均未暂存。
- 标题、单一 knowledge-writeback 块、3 个 anchor、4 个原子 locator、DAY7 prompt 和 Day6 逐卡审计已核验；本次用户指定收束回执见 [run-08 receipt](20261005-DAY6-rotation-vibration-alignment-signature-run-08/run.json)。原 run-01/run-07 事件与回执保留。
- primary 发布门已通过：Gitee origin 的 fetch exit 0、origin/main ancestor 检查 exit 0、push dry-run exit 0、实际 HEAD:main push exit 0；branch main，commit subject 为 Complete DAY6 rotation-alignment-signature evidence study。
- 本轮通用时间门更新也已通过 Gitee 发布门：branch `main`，commit subject `Apply time-aware daily-learning closeout gate`，fetch/ancestry/dry-run/push 均 exit 0，refspec `HEAD:main`。
- DAY6 用户指定收束文件已发布至 Gitee `main`：commit subject `Finalize DAY6 closeout and prepare DAY7`，fetch/ancestry/dry-run/push 均 exit 0，refspec `HEAD:main`；run-08 最终回执记为 completed/countable，Day7 preview 保持 partial。
- run-06 的原始 receipt 记有报告、知识写回、lint/diff 和 Gitee 发布通过，但也记有两槽局部饱和后提前停止。按用户 2026-10-06 明确指示，本次在原截止前提前收束 DAY6；完成 `[6]`，将 `[7]` 留作下一张正式日卡。状态保持 `next_day_index=7`，Day8 不在本次范围内。
- DAY7 正式学习提示已就绪：[2026-10-06 Day7 prompt](prompts/20261006-DAY7-collective-motion-oral-exam.md)。本次没有启动 Day7 学习；由后续 `wiki-daily-learning` 触发创建新 session。
