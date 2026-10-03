---
type: learning-daily
graph-excluded: true
run_id: 2026-10-03-day-05-01
run_date: 2026-10-03
timezone: Asia/Shanghai
day_index: 5
phase: nuclear-structure-framework
schedule_id: wiki-daily-learning
run_kind: substantive
acceptance_only: false
review_status: ai-draft
session_id: 01a0ffe6-1332-7ed2-87f0-6a0722bc4a06
session_mode: new-session-per-run
recovery_run_id: 2026-10-03-day-05-02
manual_finalization: true
---

# 2026-10-03 Day 5：β–γ–八极自由度与形状共存

## Run state

- 正式 30 天计划 Day 5。原定 2026-10-01 的触发漏过后于 2026-10-03 补跑；日序仍是 Day 5。按两个选定槽位完成有限候选复排后记录 evidence saturation，未开启第三个问题。
- Codex session：`01a0ffe6-1332-7ed2-87f0-6a0722bc4a06`；恢复命令：`codex resume 01a0ffe6-1332-7ed2-87f0-6a0722bc4a06 -C /workspace/wiki -s danger-full-access -a never`。初始回执 [run-01](20261003-DAY5-beta-gamma-octupole-shape-coexistence-run-01/run.json) 保留原运行；手动终态回执 [run-02](20261003-DAY5-beta-gamma-octupole-shape-coexistence-run-02/run.json) 记录同一 session 的收尾。
- 启动时 tracked 工作树干净；继承的 Day 2/3/4 raw 文件和 run 目录保持识别。本轮未覆盖继承 raw、PLAN.md、Zotero inbox 或用户原件；仅在新建的 raw/papers/gpt/day5-20261003/ 保存两份公开 ENSDF 评估 PDF 和一份 arXiv 理论 PDF，均核对来源身份与 SHA-256，保持未暂存。
- 前台 runner 在 continuation 1 的 Codex turn 已完成后消失，未写 `runner-finished` scheduler 事件；run-01 保留为 `recovered-continuation`，run-02 记录同一 session 的手动终态 reconciliation。Farmer 确认 session `complete`，Codex events 以 `turn.completed` 结束、stderr 为空；父 runner 退出码未捕获，明确保留为 null。

## Candidate pool and selection

候选池从[开放问题](../../knowledge/questions.md)、[131Ce 集体模式判别项目](../../knowledge/projects/131ce-collective-mode-discrimination.md)、[A≈130 thesis evidence matrix](../../knowledge/projects/a130-thesis-evidence-matrix.md)、γ-soft 综合页及 Day 2–4 学习记录重建。

| 槽位 | 候选 | 选择理由 |
|---|---|---|
| 连续性 | 131Ce 的 γ-soft 背景、静态矩、高度形变带与 shape-coexistence 关系 | 开放问题要求区别 signature/configuration coupling、γ-softness、chirality 和 shape coexistence。已有 TDPAD 与 DSAM anchors，却缺跨带 identity。Day 2–4 已覆盖壳层、平均场与配对，本轮聚焦观测量对形状命题的支撑范围。 |
| 新颖性 | 直接 E3/E1 证据如何区分八极集体性与静态反射不对称 | 选 144Ba 直接 Coulomb excitation，以独立的 220Rn/224Ra 检验动静解释，并以 78Br 和 131Ba E1-link 网络作间接证据对照；这些目标核不可互相迁移。 |
| 暂缓 | 62Cr、Pb 区等其它形状共存系统学 | 已选问题覆盖四极形状和八极形状；暂不展开第三个独立问题。 |

**开源前主动回忆：** β₂ 是四极形状幅度，γ 是四极张量的三轴坐标，β₃ 是奇宇称八极坐标。γ-soft 表示沿 γ 的势能较平、波函数分布较宽；γ-rigid 意味着局域在非零 γ 邻域，是更强的动力学命题。形状共存需同一核素内不同低能结构的证据；单带、拟合 γ 或模型极小值都不充分。开源前我不确定单一 staggering、B(E2)、静态矩或带间连线各能支持多强的命题，本轮逐项补齐边界。

## Sources and evidence

| Wiki source and locator | 证据层 | 核验所得 |
|---|---|---|
| [Davidson 1965](../../knowledge/sources/davidson-1965-rotations-vibrations-deformed-nuclei.md)：DV65-1，printed pp.105–146；DOI [10.1103/RevModPhys.37.105](https://doi.org/10.1103/RevModPhys.37.105)，原件 SHA-256 cfaf97cac087bb39d558b654065005dc7e8177ddd5d851bf8a2f698a3abaa5b4。 | 理论综述 | 转动、振动与电磁矩/B(Eλ) 的集体模型关系是形状解释框架；形变参数仍属模型映射，不是直接形状图像。 |
| [Heyde–Wood 2011](../../knowledge/sources/heyde-wood-2011-shape-coexistence-review.md)：HW11-1 Secs. I–III、HW11-3 Sec. III.C/III、HW11-4 Sec. II.B–C；DOI [10.1103/RevModPhys.83.1467](https://doi.org/10.1103/RevModPhys.83.1467)。Crossref 与本地 55 页 PDF 均核实印刷页 1467–1521；raw SHA-256 660c376e493e638501bfc8596d4eda46f490becb811ba5f30259d6f78c652183。原 Wiki source 结束页误记 1512，本轮已校正；review_status 与 claim review 标记不变。关键视觉定位：PDF p.13（印刷 p.1479）Eq.(14)、Fig.13 为 E0 混合和 odd-Pb 例；PDF p.12 Fig.11 展示多结构能级。 | 综述/模型框架 | 共存是同核不同低能态的四极/电磁结构，而不只是单一三轴/振动带；E0、E2、半径、0+ 能级和组态谱学需组合。 |
| [γ-soft vs γ-rigid diagnostics](../../knowledge/synthesis/gamma-soft-vs-gamma-rigid-diagnostics.md)；主来源 [Zamfir–Casten 1991](../../knowledge/sources/zamfir-casten-1991-gamma-softness-triaxiality.md)：ZC91-1 Fig.1、ZC91-2 Eq.(2)、ZC91-4 Fig.2；DOI [10.1016/0370-2693(91)91610-8](https://doi.org/10.1016/0370-2693(91)91610-8)。 | 实验能级到模型判据 | γ-unstable 与固定 γ 的 Davydov 极限给出相反 staggering 相位；S(4,3,2) 理想端点为 −2 与 +1.67。只适用于相应低自旋偶偶模型对照；微弱 γ 势依赖即可显著改变 S。 |
| [Ionescu-Bujor et al. 1998](../../knowledge/sources/ionescu-bujor-1998-static-moments-129-131ce.md)：IB98-2 Table 1、IB98-3 Tables 1–2；DOI 10.1016/S0375-9474(98)00157-2。 | TDPAD 静态矩为直接测量；PTR 形状参数为模型 | 131Ce 9− isomer 的 |Q|=0.92(10) eb、g=−0.189(7) 是 state-specific 数据；ε₂、γ 来自粒子加三轴转子拟合。 |
| [Petrache et al. 1998](../../knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md)：PE98-7 Table I/Fig.2、PE98-12 Table I caption、PE98-13 full-paper scope；DOI [10.1103/PhysRevC.57.R10](https://doi.org/10.1103/PhysRevC.57.R10)。 | 寿命/DSAM 导出 Q0；形状解释为作者/模型层 | 高度形变 yrast band Q0=7.3(4) eb；β₂=0.38(2) 使用无三轴转换。原文没有与 Wiki 正常形变带编号 crosswalk。 |
| [ENSDF A=131 131Ce evaluation](../../knowledge/sources/ensdf-2006-131ce-levels.md)：ENS06-1 PDF p.1；ENS06-2/ENS06-3 PDF p.2；ENS06-4 PDF p.3/p.5；ENS06-5 normal subfile PDF p.1。DOI [10.1016/j.nds.2006.10.001](https://doi.org/10.1016/j.nds.2006.10.001)。官方 SD/normal 子文件 SHA-256 分别为 c7438a39930c111dbe6baff1f96a7fa7a3a6011001f7270d0850b8873a1d51f3 与 fc07aef609a67abc8d383d14dc96753ceb8706c977f6cb462d5d5371210a2544。 | 评价数据，非新实验 | 评估把同一 1998Pe01 HD 结果列为 Band A/SD-1；SD-2 Q0=8.5(4) 来自 1996Se03/Cl03。2005Pa30 列出 1513.9(4)、1522.6(4) keV SD2→SD1 M1+E2 transitions。normal 子文件基于 1991Pa07/1996Gi08/2004Li27，cutoff 为 2006-07-17；晚于 cutoff 的 Alwaleedi 2013 不在内。 |
| [Bucher et al. 2016 144Ba](../../knowledge/sources/bucher-2016-144ba-direct-octupole.md)：BU16-1 Table I、BU16-2 PDF p.4、BU16-3 Figs.1–2；DOI [10.1103/PhysRevLett.116.112503](https://doi.org/10.1103/PhysRevLett.116.112503)，PDF 5 页、raw SHA-256 f0da6d0a56cd10d1023633aed1a25d021f88a0ff48787c4569a26031e1b3dc4d。 | Coulomb-excitation yields/GOSIA 导出 E3/B(E3)；β₃ 是模型几何推导 | 650-MeV 144Ba + 208Pb 亚势垒激发，CHICO2/GRETINA；Table I 给 B(E3;3−→0+)=48(+25/−34) W.u.。视觉核对 p.4 的 Table I、寿命处理、Q3/β3 假设；部分 E3 links 只有上限。 |
| [Bucher et al. 2017 146Ba](../../knowledge/sources/bucher-2017-146ba-direct-octupole.md)：EXT146-1 Table I、EXT146-2 PDF pp.1/3–5、EXT146-3 Figs.3–5；DOI [10.1103/PhysRevLett.118.152504](https://doi.org/10.1103/PhysRevLett.118.152504)，raw SHA-256 c49cb44350cd24f25d172efe405cd9e78360692eb4087bb3eef1801534264beb。 | Direct Coulomb excitation for 146Ba; E1 mechanism is model interpretation | Direct B(E3;3−→0+)=48(+21/−29) W.u. has the same central value as 144Ba, while the E1 moment is reduced by over an order of magnitude. SCCM/GCM orbital-occupancy explanation remains model-dependent; distinct isotope run, shared analysis family. |
| [Nomura et al. 2018 odd-mass Ba model](../../knowledge/sources/nomura-2018-odd-mass-ba-octupole.md)：NOM18-1 PDF p.1；NOM18-2 p.5 Fig.1；NOM18-3/4 pp.6–8 Figs.3–7/Tables V–VIII；NOM18-5 p.9 Table IX；NOM18-6 p.10 Conclusions。DOI [10.1103/PhysRevC.97.024317](https://doi.org/10.1103/PhysRevC.97.024317)，arXiv [1711.09587v2](https://arxiv.org/abs/1711.09587v2)，raw SHA-256 4df5fce3696da1d019ea07111e064fe9704376f2f6c8b6bb33826cb61fa953be。 | CDFT+IBFM model result, no new experiment | Predicts beta-three-soft even Ba cores and mostly sd-space low odd-A Ba states, with selected higher 145Ba E3 configurations; boson-fermion strengths are fitted and the 147Ba ground-state spin remains mismatched. This is state-dependent model context, not an A≈130 measurement. |
| [Gaffney et al. 2013](../../knowledge/sources/gaffney-2013-pear-shaped-rn-ra.md)：GA13-1 Table 1/Methods、GA13-2 Figs.3–5/Tables 1–2、GA13-3 Fig.3、GA13-6 journal p.202 (PDF p.4)；DOI [10.1038/nature12073](https://doi.org/10.1038/nature12073)。 | 独立 radioactive-beam Coulomb-excitation | E2/E3 矩与自旋系统学对比 220Rn 较振动态运动和 224Ra 更强、更协调的静态样 collectivity；shape 标签仍含作者/模型解释。 |
| [Guo et al. 2020 131Ba](../../knowledge/sources/guo-2020-pseudospin-chiral-quartet-131ba.md)：GU20-10/11/16 PDF pp.4–5 Figs.1/5；GU20-14 PDF p.5；DOI [10.1016/j.physletb.2020.135572](https://doi.org/10.1016/j.physletb.2020.135572)，raw SHA-256 109019D2EF7338BA705462374E6CF30C0CF9D61175510DD92D63021271E8F29D。 | New 122Sn(13C,4n)131Ba GALILEO acquisition: E1 links direct, octupole meaning is author/model layer | Eight E1 links from negative-parity D7 into positive-parity D3–D6; no E3 strength/lifetimes are reported, and β3=0.05 is a tentative RAT-PRM input. D3–D6 cannot be uniquely split into two positive pairs. |
| [Liu et al. 2016 78Br](../../knowledge/sources/liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br.md)：L16-9 八条 E1 links、L16-11 的 B(E1)/B(E2) 与 delta E、L16-13 的 beta20–beta30 PES softness。 | E1 link 为直接观测；octupole-soft 是作者/模型解释 | E1、ratio 与 PES 证据层分开；它不单独建立静态八极形变，也不属于 A≈130。 |

2005Pa30 primary-source route: [NNDC NSR key record](https://www.nndc.bnl.gov/nsr/KeyNumberSearchServlet?search-type=keynumber&key=2005Pa30) and Crossref resolve E. S. Paul et al., Physical Review C 71, 054309 (2005), DOI [10.1103/PhysRevC.71.054309](https://doi.org/10.1103/PhysRevC.71.054309). The APS PDF endpoint (https://journals.aps.org/prc/pdf/10.1103/PhysRevC.71.054309) returned 403. OpenAlex metadata (https://api.openalex.org/works/https://doi.org/10.1103/physrevc.71.054309) marks it closed with no repository full text; HAL presented a bot check and Lund/Padua records exposed metadata without an accessible PDF. The ENSDF p.1/p.3 summary is the evidence actually inspected; no primary-paper claim beyond that summary is imported.

完整映射写入 [shape-observable-matrix](../../knowledge/synthesis/shape-observable-matrix.md)。原件 hash 只核对，不改写 raw。

## Theory/analysis exercise

按 Day 5 卡将 staggering、B(E2)、静态矩和跃迁连接逐项标注“可以支持 / 不能单独支持 / 最小补充”。矩阵另加入 E0/0+ 与 E3，因为它们直接决定 shape-coexistence 与 octupole 命题的边界。

| 指标 | 可以支持 | 不能单独支持 | 最小补充 |
|---|---|---|---|
| 能级 staggering | 偶偶低自旋 γ 带的序列和间距可约束 γ 势极限 | 单个 S 不给唯一刚度，也不判断共存 | 连续 spin、E2 矩阵元/集体不变量、允许 γ 涨落的模型 |
| B(E2) | 特定初末态的四极跃迁强度与集体性 | 单值不决定 β₂/γ 或两个形状并存 | lifetime、branching、多极性及相关带内/带间绝对矩阵元 |
| 静态 Qs | 某一指定态的四极响应 | 不可替代转子 Q0，也不代表其它 band | 状态身份、符号/标定与多个态的共同模型比较 |
| 跃迁连接 | 能级纲图拓扑与可能的组态沟通 | 连线或能量闭合不证明混合或共存 | Jπ、多极性、绝对强度/混合比、跨实验 band identity |

数学复核采用 ZC91-2：
S(J,J−1,J−2) = {[E(J)−E(J−1)]−[E(J−1)−E(J−2)]}/E(2₁⁺)。
γ-unstable 理想极限 S(4,3,2)=−2；γ=30° Davydov 刚性转子为 +1.67。这是模型端点复核，不是 131Ce 数据拟合；ZC91-4 显示弱 γ 势项即可移动 S，因此不把两端间的距离线性解释为软硬比例。

Bucher 的 B(E3) 保留非对称误差；β₃=0.17(+0.04/−0.06) 使用 β₂=0.18 和转子形状映射，不能称直接测量。理论预测 20–24 W.u. 没有在此处用于显著性计算。

**续读的 level-link 练习：** ENS06-4 的两条 SD2→SD1 边分别为 47/2+→45/2+ 和 43/2+→41/2+。由列出的 level values 重算 Ei−Ef−Eγ，残差为 −0.38 keV 和 +0.40 keV；按所列独立 level/gamma uncertainties 作简单平方和，合成量约 0.59 keV，残差约 0.6–0.7σ。评估的 level energies 本身来自 Eγ 最小二乘且未给协方差，所以这只是内部能量闭合核对，不能当作独立复核。2005Pa30 的 Eγ 相对早期 SD 数据系统性高约 1–8.5 keV，跨数据集 identity 不可只按能量近似匹配。

**SD band quadrupole-scale check：** ENSDF lists Q0(SD-2)=8.5(4) eb and Q0(SD-1)=7.3(4) eb, a difference of 1.2 eb. If the quoted errors were independent, σΔ=√(0.4²+0.4²)=0.57 eb, a nominal 2.1σ difference. Their covariance and common systematic treatment are not supplied, so this is a sensitivity screen, not a formal difference significance. These two values compare SD bands with each other; neither substitutes for a like-for-like normal-to-SD measurement.

**Rn/Ra 反例量级检查：** Gaffney Table 2 的 Q3 为 220Rn 2180(130) e fm³、224Ra 2520(90) e fm³；计算 Ra/Rn=1.156。若误差独立传播，σratio≈1.156×√[(90/2520)²+(130/2180)²]=0.080，即约 1.16±0.08。它显示中心矩只差约 16%，并非数量级差异；共同分析假设与未提供的跨核协方差使这不是正式显著性检验。GA13-6 还明确说明，E2/E3 矩阵元本身不能区分 parity states 来自静态 quadrupole-octupole shape projection，还是 quadrupole shape 上的 octupole vibration；静态样结论借助多跃迁系统学与形状重建。

**续读的八极强度误差传播：** 令 ΔB = B(E3;146Ba)−B(E3;144Ba)。中心差为 0 W.u.。若暂把两篇文献的不对称误差当作独立，Δ 的上误差为 √(21²+34²)=40 W.u.，下误差为 √(29²+25²)=38 W.u.，即约 0(+40/−38) W.u.。因此相同中心值与两测量相容，但这不是精密的恒定性检验：两篇共享 GOSIA/CHICO2/GRETINA 分析链，且没有跨论文响应/协方差可供传播。更直接的结论是 146Ba 的小 E1 moment 不代表 E3 octupole strength 同比例消失；具体 orbital-occupancy cancellation 来自 SCCM/GCM 模型。

**奇质量 Ba 模型敏感性核对：** NOM18 的 147Ba calculation 给出 3/2− ground state，与所引用实验的 5/2− 不同；作者检验把 1h9/2 occupation 降低 25% 可改善顺序，但明确说该调参在此框架下没有充分根据。145Ba 的低态以 sd-space 为主，而候选 octupole/f-boson 结构位于较高激发。该模型的 axial beta-two/beta-three 自由度和 fitted coupling 不能转成 131Ce 的实验结论。

## Counter-evidence and missing companion observables
- **A≈130 E1 handle:** GU20-10 reports eight observed 131Ba D7→D3–D6 E1 links; GU20-11/GU20-14/GU20-16 retain the author octupole interpretation, tentative β3=0.05 model input, and no lifetime/absolute-strength boundary. This gives the region direct parity-link evidence, but not direct E3 strength, absolute E1 probabilities, or stable deformation; it is not a 131Ce observation.


- **γ-soft/γ-rigid：** ZC91-4 的模型扫描显示弱 γ 势项可大幅改变 staggering；带混合、能级误指认也是替代解释。
- **形状共存：** Heyde–Wood 指出低能 0+、E0 或 B(E2) 变化也可能来自配对、振动、intruder 或组态混合。131Ce 的 Qs 和 Q0 虽同为 eb，但定义、状态与提取方法不同，不能以 7.3/0.92 比值推断形状差。 ENSDF crosswalk 把 PE98 高形变结果定位为 SD-1，并证实 SD1/SD2 的连接；它没有提供与 Alwaleedi normal Bands 1–7 的 transition link。
- **八极形变：** 144Ba/146Ba 的直接 B(E3) 中心值相同但 E1 moment 差异很大；E1 amplitude 与 octupole collectivity 分开。220Rn/224Ra 的 Q3 比约 1.16，GA13-6 明确指出 E2/E3 矩阵元不能单独区分静态投影与八极振动。NOM18 的模型预测奇质量 Ba 低态 octupole 含量弱、高态才出现特定 E3 结构；它受拟合和 147Ba 自旋偏差限制，不能视为新实验。78Br 的 E1 link/PES 仍是另一证据层。
- **必要观测：** gamma softness 需连续 staggering 和 E2/invariants；共存需两套 state/band identity、state-resolved E0/E2/Qs/radii 与跨带 strength；static octupole 需 E3、E1/异宇称序列和 spin dependence 联合。
- **源独立性：** Davidson、Heyde–Wood 是综述；Zamfir–Casten 是模型对比。131Ce TDPAD 与 DSAM 是不同反应但有作者重叠。Bucher 144/146Ba 是不同 isotope runs、共享 GOSIA/CHICO2/GRETINA；Nomura 2018 为同一理论作者群的 fitted model。Guo 131Ba、Liu 78Br 与 Rn/Ra 是各自独立 acquisition lineages，不能合并计数。

- **Finite candidate re-ranking:** The direct 131Ba E1 network (GU20) is the highest-information A≈130 novelty comparator found, but it lacks absolute E1/E3/lifetime closure. The 1997 even-even Ba octupole source and 1980 131Ba angular-correlation paper remain closed/metadata-only in current routes; no new lawful full text was opened. This is a bounded stop, not a claim that no such evidence exists.

## Knowledge Impact and Learning Decision

**Decision: revises.** 131Ce 的 1998 HD Q0 现可回溯映射到 ENSDF SD-1；同一评估还列出 SD-2 及 SD2→SD1 links。低态 TDPAD 与正常形变 Bands 1–7 仍是不同状态/数据谱系，normal-to-SD transition map 未闭合。A≈130 另有 131Ba 的直接 E1-link 网络，但 octupole 意义仍为作者/模型解释，没有直接 E3/绝对 E1 约束，也不能迁移到 131Ce。Ba/Rn/Ra 与 78Br 比较均分层记录 E3、E1 和形状解释；NOM18 是模型边界，不是实验新增。review 状态未改。

## Durable knowledge delta

- [shape-observable-matrix](../../knowledge/synthesis/shape-observable-matrix.md)：续读加入 131Ce ENSDF SD1/SD2 crosswalk、normal-SD gap；144Ba/146Ba、Rn/Ra 的 E3/Q3 scales 与静态/动态边界；NOM18 模型限度；以及 131Ba 八条直接 E1 links 的 A≈130 证据边界。
- [A≈130 thesis evidence matrix](../../knowledge/projects/a130-thesis-evidence-matrix.md)：更新 131Ce shape-multiplicity boundary 行，记录 IB98 静态矩、PE98 Q0、ENSDF SD-1/SD2–SD1 crosswalk 和未闭合的 normal-SD edge。
- [A≈130 高自旋集体模式图](../../knowledge/projects/a130-high-spin-collective-modes-evidence-map.md)：新增 Guo 2020 131Ba 的 direct E1-link 入口，并保留八极解释及 D3-D6 quartet grouping 的边界。
- [Heyde–Wood source page](../../knowledge/sources/heyde-wood-2011-shape-coexistence-review.md)：页码由 1467–1512 校正为 1467–1521；Crossref 和原 PDF 首尾页核实，review/claim 状态未改。
- [ENSDF 131Ce evaluation](../../knowledge/sources/ensdf-2006-131ce-levels.md)：归档官方 normal 与 SD 子文件；解决 PE98→SD-1 和 SD1↔SD2 locator，保留 normal–SD crosswalk 缺口。
- [Nomura et al. 2018 source](../../knowledge/sources/nomura-2018-odd-mass-ba-octupole.md)：收录奇质量 Ba 的 CDFT/IBFM model result 与参数拟合/基态自旋失败边界。
- [Gaffney et al. 2013 source](../../knowledge/sources/gaffney-2013-pear-shaped-rn-ra.md)：续读补入 GA13-6，定位原文对静态 quadrupole-octupole 投影与八极振动不可由现有 E2/E3 矩阵元单独区分的说明。
- [Research Questions](../../knowledge/questions.md)：保留八极证据梯度问题开放，并注明 131Ba 的直接 E1 network 与无 E3/absolute-strength 边界。
- [131Ce 核素页](../../knowledge/nuclei/131ce.md)及[131Ce 集体模式项目](../../knowledge/projects/131ce-collective-mode-discrimination.md)：记录 P98→SD-1 已闭合、normal Bands 1–7 映射仍开放。
- [131Ce 集体模式项目](../../knowledge/projects/131ce-collective-mode-discrimination.md)：记录 2005Pa30 的 DOI 与当前全文访问边界；把 ENSDF 摘要和 primary article 分层。
- [Wiki index](../../knowledge/index.md)：增加 ENSDF A=131 evaluation 与 Nomura 2018 odd-mass Ba model source 入口。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/synthesis/shape-observable-matrix.md",
      "summary": "观测量命题边界含131Ce ENSDF crosswalk、131Ba直接E1链接、Ba/Rn/Ra八极实验对照及odd-A模型限度。",
      "anchor": "## Observable-to-claim matrix",
      "sources": [
        {
          "path": "knowledge/sources/davidson-1965-rotations-vibrations-deformed-nuclei.md",
          "locator": "DV65-1"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-1"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-3"
        },
        {
          "path": "knowledge/sources/zamfir-casten-1991-gamma-softness-triaxiality.md",
          "locator": "ZC91-2"
        },
        {
          "path": "knowledge/sources/zamfir-casten-1991-gamma-softness-triaxiality.md",
          "locator": "ZC91-4"
        },
        {
          "path": "knowledge/sources/bucher-2016-144ba-direct-octupole.md",
          "locator": "BU16-1"
        },
        {
          "path": "knowledge/sources/gaffney-2013-pear-shaped-rn-ra.md",
          "locator": "GA13-2"
        },
        {
          "path": "knowledge/sources/liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br.md",
          "locator": "L16-9"
        },
        {
          "path": "knowledge/sources/ionescu-bujor-1998-static-moments-129-131ce.md",
          "locator": "IB98-2"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-7"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-13"
        },
        {
          "path": "knowledge/sources/ensdf-2006-131ce-levels.md",
          "locator": "ENS06-2"
        },
        {
          "path": "knowledge/sources/ensdf-2006-131ce-levels.md",
          "locator": "ENS06-4"
        },
        {
          "path": "knowledge/sources/ensdf-2006-131ce-levels.md",
          "locator": "ENS06-5"
        },
        {
          "path": "knowledge/sources/bucher-2017-146ba-direct-octupole.md",
          "locator": "EXT146-1"
        },
        {
          "path": "knowledge/sources/bucher-2017-146ba-direct-octupole.md",
          "locator": "EXT146-2"
        },
        {
          "path": "knowledge/sources/bucher-2017-146ba-direct-octupole.md",
          "locator": "EXT146-3"
        },
        {
          "path": "knowledge/sources/gaffney-2013-pear-shaped-rn-ra.md",
          "locator": "GA13-6"
        },
        {
          "path": "knowledge/sources/nomura-2018-odd-mass-ba-octupole.md",
          "locator": "NOM18-1"
        },
        {
          "path": "knowledge/sources/nomura-2018-odd-mass-ba-octupole.md",
          "locator": "NOM18-2"
        },
        {
          "path": "knowledge/sources/nomura-2018-odd-mass-ba-octupole.md",
          "locator": "NOM18-3"
        },
        {
          "path": "knowledge/sources/nomura-2018-odd-mass-ba-octupole.md",
          "locator": "NOM18-4"
        },
        {
          "path": "knowledge/sources/nomura-2018-odd-mass-ba-octupole.md",
          "locator": "NOM18-5"
        },
        {
          "path": "knowledge/sources/nomura-2018-odd-mass-ba-octupole.md",
          "locator": "NOM18-6"
        },
        {
          "path": "knowledge/sources/guo-2020-pseudospin-chiral-quartet-131ba.md",
          "locator": "GU20-10"
        },
        {
          "path": "knowledge/sources/guo-2020-pseudospin-chiral-quartet-131ba.md",
          "locator": "GU20-11"
        },
        {
          "path": "knowledge/sources/guo-2020-pseudospin-chiral-quartet-131ba.md",
          "locator": "GU20-14"
        },
        {
          "path": "knowledge/sources/guo-2020-pseudospin-chiral-quartet-131ba.md",
          "locator": "GU20-16"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-thesis-evidence-matrix.md",
      "summary": "新增 131Ce 静态矩与高形变 DSAM 证据桥，并保留不同 Q 定义和跨带映射缺口。 ENSDF resolves PE98→SD-1 and SD2→SD1 links; normal-SD identity remains open.",
      "anchor": "131Ce shape-multiplicity boundary",
      "sources": [
        {
          "path": "knowledge/sources/ionescu-bujor-1998-static-moments-129-131ce.md",
          "locator": "IB98-2"
        },
        {
          "path": "knowledge/sources/ionescu-bujor-1998-static-moments-129-131ce.md",
          "locator": "IB98-3"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-7"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-12"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-13"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-3"
        },
        {
          "path": "knowledge/sources/ensdf-2006-131ce-levels.md",
          "locator": "ENS06-2"
        },
        {
          "path": "knowledge/sources/ensdf-2006-131ce-levels.md",
          "locator": "ENS06-4"
        },
        {
          "path": "knowledge/sources/ensdf-2006-131ce-levels.md",
          "locator": "ENS06-5"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
      "summary": "将参考文献页码校正为 1467–1521；DOI 元数据与原 PDF 首尾页一致，review/claim 标记未动。",
      "anchor": "## Bibliographic Record",
      "sources": [
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-1"
        },
        {
          "path": "knowledge/sources/heyde-wood-2011-shape-coexistence-review.md",
          "locator": "HW11-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/131ce-collective-mode-discrimination.md",
      "summary": "Resolved PE98-to-ENSDF SD-1 identity and recorded SD2-to-SD1 links; retained the normal-SD identity gap.",
      "anchor": "### Public-source manifest seed rows (design-only)",
      "sources": [
        {
          "path": "knowledge/sources/ensdf-2006-131ce-levels.md",
          "locator": "ENS06-1"
        },
        {
          "path": "knowledge/sources/ensdf-2006-131ce-levels.md",
          "locator": "ENS06-2"
        },
        {
          "path": "knowledge/sources/ensdf-2006-131ce-levels.md",
          "locator": "ENS06-4"
        },
        {
          "path": "knowledge/sources/ensdf-2006-131ce-levels.md",
          "locator": "ENS06-5"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-7"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-1"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-16"
        }
      ]
    },
    {
      "knowledge": "knowledge/nuclei/131ce.md",
      "summary": "Added evaluated mapping of Petrache 1998 to SD-1 and the separate SD1/SD2 connection; retained the normal-SD crosswalk boundary.",
      "anchor": "## Deformation and Collective Features",
      "sources": [
        {
          "path": "knowledge/sources/ensdf-2006-131ce-levels.md",
          "locator": "ENS06-2"
        },
        {
          "path": "knowledge/sources/ensdf-2006-131ce-levels.md",
          "locator": "ENS06-4"
        },
        {
          "path": "knowledge/sources/ensdf-2006-131ce-levels.md",
          "locator": "ENS06-5"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-7"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-1"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-16"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/ensdf-2006-131ce-levels.md",
      "summary": "Added hash-verified ENSDF subfiles; identified the SD-1/SD-2 structure and source dependence without treating evaluation as independent data.",
      "anchor": "## Key Results",
      "sources": [
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-7"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-13"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-1"
        },
        {
          "path": "knowledge/sources/alwaleedi-2013-band-structures-131ce.md",
          "locator": "AW13-16"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "Added the evaluated 131Ce normal/SD level-scheme source to the Wiki index.",
      "anchor": "[[ensdf-2006-131ce-levels]]",
      "sources": [
        {
          "path": "knowledge/sources/ensdf-2006-131ce-levels.md",
          "locator": "ENS06-1"
        },
        {
          "path": "knowledge/sources/ensdf-2006-131ce-levels.md",
          "locator": "ENS06-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/131ce-collective-mode-discrimination.md",
      "summary": "Recorded the DOI-resolved 2005Pa30 route and the checked full-text access boundary; kept ENSDF evaluation results separate from unreviewed primary content.",
      "anchor": "### 2026-10-03 primary-source access boundary",
      "sources": [
        {
          "path": "knowledge/sources/ensdf-2006-131ce-levels.md",
          "locator": "ENS06-4"
        },
        {
          "path": "knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md",
          "locator": "PE98-7"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/nomura-2018-odd-mass-ba-octupole.md",
      "summary": "Added the public-text CDFT/IBFM odd-mass Ba model with fitted-parameter, state-dependence, and 147Ba spin-mismatch limits.",
      "anchor": "## Key Results",
      "sources": [
        {
          "path": "knowledge/sources/bucher-2016-144ba-direct-octupole.md",
          "locator": "BU16-1"
        },
        {
          "path": "knowledge/sources/bucher-2017-146ba-direct-octupole.md",
          "locator": "EXT146-1"
        },
        {
          "path": "knowledge/sources/nomura-2017-odd-mass-gamma-soft-shape-transitions.md",
          "locator": "NOM17-10"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "Added the 2018 odd-mass Ba octupole-model source to the Wiki index.",
      "anchor": "[[nomura-2018-odd-mass-ba-octupole]]",
      "sources": [
        {
          "path": "knowledge/sources/nomura-2018-odd-mass-ba-octupole.md",
          "locator": "NOM18-1"
        },
        {
          "path": "knowledge/sources/nomura-2018-odd-mass-ba-octupole.md",
          "locator": "NOM18-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/questions.md",
      "summary": "Kept the cross-region octupole evidence-ladder question open while annotating the direct 131Ba E1-link network and the absent target-region E3/absolute-strength evidence.",
      "anchor": "直接 E3、E1 correlation、PES",
      "sources": [
        {
          "path": "knowledge/sources/guo-2020-pseudospin-chiral-quartet-131ba.md",
          "locator": "GU20-10"
        },
        {
          "path": "knowledge/sources/guo-2020-pseudospin-chiral-quartet-131ba.md",
          "locator": "GU20-14"
        },
        {
          "path": "knowledge/sources/guo-2020-pseudospin-chiral-quartet-131ba.md",
          "locator": "GU20-16"
        },
        {
          "path": "knowledge/sources/bucher-2016-144ba-direct-octupole.md",
          "locator": "BU16-1"
        },
        {
          "path": "knowledge/sources/bucher-2017-146ba-direct-octupole.md",
          "locator": "EXT146-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/gaffney-2013-pear-shaped-rn-ra.md",
      "summary": "Added locator-level claim GA13-6 stating that E2/E3 matrix elements alone do not separate a projected static octupole shape from octupole vibration; source review state is unchanged.",
      "anchor": "## Key Results",
      "sources": [
        {
          "path": "knowledge/sources/gaffney-2013-pear-shaped-rn-ra.md",
          "locator": "GA13-1"
        },
        {
          "path": "knowledge/sources/gaffney-2013-pear-shaped-rn-ra.md",
          "locator": "GA13-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-high-spin-collective-modes-evidence-map.md",
      "summary": "Added the 131Ba D7→D3-D6 direct E1 network as an A≈130 octupole-correlation comparator; kept model beta-three and quartet-pairing limits explicit.",
      "anchor": "## Evidence Gaps",
      "sources": [
        {
          "path": "knowledge/sources/guo-2020-pseudospin-chiral-quartet-131ba.md",
          "locator": "GU20-7"
        },
        {
          "path": "knowledge/sources/guo-2020-pseudospin-chiral-quartet-131ba.md",
          "locator": "GU20-10"
        },
        {
          "path": "knowledge/sources/guo-2020-pseudospin-chiral-quartet-131ba.md",
          "locator": "GU20-11"
        },
        {
          "path": "knowledge/sources/guo-2020-pseudospin-chiral-quartet-131ba.md",
          "locator": "GU20-14"
        },
        {
          "path": "knowledge/sources/guo-2020-pseudospin-chiral-quartet-131ba.md",
          "locator": "GU20-16"
        }
      ]
    }
  ]
}
```
## Open questions and belief revision

- **修订前：** A≈130 矩阵仅写 131Ce 需新增 δ/偏振、寿命和跨带连接，未在 thesis matrix 并列形状敏感锚点。
- **修订后：** PE98 的高形变 Q0 已由 ENSDF 回溯映射到 SD-1；另有 SD-2 及 SD2→SD1 transitions。低态 TDPAD 9− 矩和 Alwaleedi normal Bands 1–7 仍是另一数据/状态链。PE98→SD1 已闭合，normal-to-SD crosswalk 仍未闭合；不比较 Qs/Q0 裸数值。
- **待解：** 131Ce 的 normal-to-SD transition map 与状态分辨 E2/E0 仍缺；131Ba 有直接 E1 links，但 GU20-14 的 β3 为 tentative model input、GU20-16 无 lifetime/absolute strength，不能代替 131Ce。144/146Ba 的 E3 强度中心值相容，E1 抑制机制仍由模型解释，跨拟合协方差缺失。
- **可证伪条件：** 若可靠状态映射显示两系列属同一组态/形变响应，应下调 shape-multiplicity 假设；若独立 E2/E0/Qs/radii 和跨带 strength 指向两种分离结构，才提升共存证据。若后续独立强度/响应分析使 144/146Ba 的 E3 差异超出共享系统误差，则需修订当前“强度相容”的判断。静态八极解释还需在不确定度下胜过动态 soft 模型并获多观测支持。

## L0–L4 state

- **L0 — complete：** 候选、来源指纹、问题和输出范围明确。
- **L1 — complete：** 更新 shape-observable synthesis、A≈130/131Ce project matrices、source pages、index、open question 与关联入口；所有既有 `review_status` 保持原样，新 claim 仍为 `needs_review: true`。
- **L2 — complete：** 主来源阅读、四类 observable 的命题矩阵、γ staggering 端点计算、B(E3) 不对称误差传播、Q3 比值敏感性检查、131Ce ENSDF level-link arithmetic 和来源独立性检查均完成。
- **L3 — bounded / evidence-saturated：** PE98→ENSDF SD-1 与 SD1↔SD2 已定位；normal Bands 1–7→SD mapping 仍开放。131Ba 有 direct E1 links，但没有 E3、absolute E1 或 lifetime closure；未升级为 A≈130 静态八极结论。
- **L4 — not-ready：** 有论文表格值，但缺 GOSIA 原始 yield、完整拟合响应/协方差和代码；不重现 144Ba E3 fit，也不做代理分析。用户实验数据不在本轮读取范围。
- 未设置 human-reviewed；未清除 needs_review。

## Verification and continuation

- `wiki_automation_preflight.py --root .` 与 `wiki_boundary_check.py --root .` 均 exit 0；受保护 Zotero inbox SHA-256 匹配。
- `clean_knowledge_eol_dirty.py`：exit 1 because it preserved 9 substantive tracked knowledge edits and classified 3 newly added task-owned knowledge pages as `REVIEW-UNSAFE`; `restored=0`, `unsafe/mixed=0`. The new ENSDF source, Nomura model source and shape synthesis were explicitly checked against the daily task scope, source identity, exact locators, backlinks and single writeback mapping; all remain authorized.
- `wiki_knowledge_writeback.py`：valid；唯一机器可读 block、13 个知识条目、所有 anchors/atomic locators 和 source backlinks 均通过；12 个 changed/new knowledge Markdown 路径全部映射。
- `wiki_lint.py --fail-on error`：最近复跑 exit 0、0 errors / 92 warnings / 1307 info；warnings 为 88 `CITATION_KEY_MISSING`、3 `REACTION_PARSE`、1 `RAW_GIT_CHANGE`。`git diff --check` exit 0。报告 10 个必需标题、唯一 writeback block、所有相对链接均通过。
- 手动 runner reconciliation：run-01 保留 `recovered-continuation`；run-02 完成相同 session 的终态 receipt。Codex continuation JSONL 末端为 `turn.completed`，Farmer session state 为 `complete`；父 runner 没有 terminal event，退出码未观测。完成此对账后，substantive state 只推进一次到 `next_day_index=6`。
- Day 6 prompt 已生成：[2026-10-04 Day 6](prompts/20261004-DAY6-rotation-vibration-alignment-signature.md)。停止原因是两条选定路线达到 evidence saturation，仍保留 normal-to-SD、原始 2005Pa30 全文和 absolute E1/E3/lifetime 等开放边界。
- Git 仅采用本轮明确列出的 tracked paths；raw PDFs、继承目录、scheduler JSONL/runtime state、凭据和 Zotero inbox 不暂存。branch + subject 是稳定提交指针，精确 commit hash 与 push outcome 写入本地 scheduler receipt。
