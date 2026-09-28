---
type: learning-daily
graph-excluded: true
run_id: 2026-09-28-day-02-02
prompt_run_id: prompt-2026-09-28-day-02
parent_run_id: 2026-09-28-day-02-01
run_date: 2026-09-28
timezone: Asia/Shanghai
day_index: 2
phase: nuclear-structure-framework
cycle: 2026-09-30-day-substantive
schedule_id: wiki-daily-learning
schedule_name: Wiki 30-day substantive daily learning
run_kind: substantive
acceptance_only: false
review_status: ai-draft
session_id: 01a0e767-5b2c-7792-9707-9fd1d49f2eb0
session_mode: resumed-existing-session
---

# 2026-09-28 Day 2：壳层、magic gap 与单粒子轨道

## Run state
- 本续接补入 133Sn 粒子转移 SI、131Sn 空穴侧评估边界及 AME 单中子差分；run-02 保持 in-progress，Day 2 尚未计数，state_file 的 next_day_index 仍为 2。

- 本报告记录正式 30 天实质周期的 Day 2。前一轮 `2026-09-28-day-02-01` 于 18:13 因 usage limit 以 exit `1` 结束，调度日志保留原失败事件；21:14 在同一 Codex session 恢复后，本次 recovery segment `2026-09-28-day-02-02` 继续 Day 2。恢复不是新的 schedule session。
- 当前 session：`01a0e767-5b2c-7792-9707-9fd1d49f2eb0`。可复制续接命令：`codex resume 01a0e767-5b2c-7792-9707-9fd1d49f2eb0 -C /workspace/wiki -s danger-full-access -a never`。上一轮 `run-01` 目录保留为原始失败回执，没有覆盖或暂存。
- 报告、知识页和 `run-02` 回执写在仓库内。入口时的 tracked 工作树干净；继承的 `outputs/learning-daily/20260928-DAY2-shell-gap-single-particle-run-01/` 保持不变。
- 11 个公开质量表、评估页面与 PDF 在哈希/格式/目标 locator 核验后归档到 `raw/papers/gpt/day2-shell-gap-20260928/`；没有覆盖既有 raw，整包保持未暂存。来源 URL、DOI、SI 状态、SHA-256 和 locator 见 [run-02 source manifest](20260928-DAY2-shell-gap-single-particle-run-02/source-manifest.tsv)。
- 经 hash、PDF 签名和目标行检查的 11 个公开源快照由 `_incoming/20260928-day-02-02/` 晋升至 [run-scoped raw source bundle](../../raw/papers/gpt/day2-shell-gap-20260928/)；文件只用于本地来源回链，不暂存/发布。URL、DOI、SI 状态、哈希和 locator 汇总在 [source manifest](20260928-DAY2-shell-gap-single-particle-run-02/source-manifest.tsv)。
- 写入前运行 `python3 system/scripts/wiki_boundary_check.py --root .`，exit `0`；`python3 system/scripts/clean_knowledge_eol_dirty.py` 和 `python3 system/scripts/wiki_automation_preflight.py --root .` 分别 exit `0`。受保护 `raw/zotero/wiki-inbox.bib` 哈希与基线一致。
- 原 schedule 窗口为 Asia/Shanghai 2026-09-28 16:00 至 2026-09-29 10:00。本 continuation 延续同一 Day 2 学习窗口；报告是 checkpoint，下一条高信息任务见 `run-02/continuation-prompt.md`。

## Candidate pool and selection

候选池由 [当前研究问题](../../knowledge/questions.md)、[A≈130 thesis evidence matrix](../../knowledge/projects/a130-thesis-evidence-matrix.md)、[Day 1 shell-gap bridge](../../knowledge/projects/a130-shell-gap-orbital-observable.md)、9 月 27 日学习记录和已有来源指纹重建。

- **连续性槽位：`131Ce` 单粒子轨道、寿命与集体响应的关系。** 当前问题是 `131Ce` Bands 1–7 的组态/集体模式如何由跃迁性质和寿命区分。既有资料指出 `νh11/2`、`νg7/2` 的作者形状驱动解释，但 `Q_t` 由寿命和转子角动量因子换算；本次用原始表格核对一项数值并追踪 Singh 的重新换算。
- **新颖性槽位：`N=82` 球形闭合的质量与电磁指标。** Day 1 集中在 A≈130 高自旋 signature splitting 和模式判别；`130,132,134Sn` 的 AME2020 质量二阶差分、首个 `2+` 能级和 Coulomb-excitation `B(E2)` 是不重叠的低自旋/质量系统学。为满足核结构对照要求，另比 `132Sn/134Te` 同中子数链。
- **来源冷却说明：** Li 2004、Singh 2016、Ding 2021 在最近记录中已出现；仅因当前 Day 2 任务要求轨道—观测量桥接而复用。回到原始表后发现 Li 的 `27/2−` `Q_t` 末位误录，并发现 Singh 按另一转子/Clebsch–Gordan 约定重算同一寿命；这是新的直接来源校正与机制澄清。新颖性槽位以 AME2020、Varner 2005 和 ENSDF/LiveChart 的闭壳层证据为主。
- **本轮范围保持两个问题：** `131Ce` 轨道—`Q_t` 转换；`N=82` shell-closure 证据。`131Ba/133Ce` 仅作 `N=75` 竞争解释，不另开第三个课题。

**打开原始来源前的主动回忆：** 球形壳层闭合是近球形平均场中费米面附近的轨道间隔/简并度变化，magicity 需质量曲率、低能集体性和单粒子证据共同约束；形变壳隙随 `β₂/γ`、配对、转动频率和势参数变化，常由 Nilsson/CSM 等模型给出；`nℓj` 或 Nilsson orbital 是占据/组态标签，不能单独等同于壳隙数值、形状测量或集体模式。最少观测组合应含质量/分离能、`E(2+)` 与 `B(E2)`，以及配置敏感的 transfer/decay 或高自旋 crossing/alignment。

**本次续接的候选池更新：** N=82 两中子曲率、133Sn 的 N=83 粒子转移、131Sn 的 N=81 空穴谱、N=74 形变高自旋轨道解释，以及 Orlandi 2018 的 N=81 空穴转移和自旋轨道证据是当前候选。选择 N=81/N=83 两侧的 shell-gap 连续性问题；本续接不另开非重叠新颖性问题，以免把同一壳闭合问题拆成第三个课题。主动回忆已在本日报前文记录；续接先核验 NuDat 与 DOAJ 摘要，随后通过 OpenAIRE 找到 Surrey 直接 delivery 并通读论文六页。

**本轮 N=82 候选更新：** 先前列为 missing 的 130Sn B(E2) 已通过 Radford 2005 原文转为 direct-preliminary evidence；新增高价值冲突是 132Sn 的 Varner 0.11(3) e²b² 与 NuDat gamma-table 5.5(15) W.u. 字段不一致。Gray thesis 的 5.9(1.3) W.u. 是 Radford 同一数据的再表述，不计独立实验。

## Sources and evidence

| 来源与精确定位 | 证据层 | 本轮用途与边界 |
|---|---|---|
| [AME2020 Sn mass records](../../knowledge/sources/ame2020-sn132-mass-curvature.md)：`AME20-130SN-1`、`AME20-132SN-1`、`AME20-134SN-1`；`AME20-RCT1-132SN-1`、`AME20-RCT1-134SN-1`。官方 IAEA `mass_1.mas20.txt` SHA-256 `e8599c6d7f724fac91934e59f1b9de8fb8f63e820f4b39456b790665ed2a3307`；`rct1.mas20.txt` SHA-256 `e6ba1d2256f90053464c48e24d44691828dc49820ce64054aa418d834cc18e90`。 | 质量评估值 | AME2020 文件头明确 `#` 为估算质量标记；三条质量超额行没有该标记。两张表来自同一次 AME2020 评估，不算独立复测；协方差未随检索文件提供。 |
| [IAEA LiveChart / ENSDF Sn–Te levels](../../knowledge/sources/iaea-livechart-132sn-134te-levels.md)：`LC130SN-1`、`LC132SN-1`、`LC134SN-1`、`LC134TE-1`、`NUDAT132SN-2/3/4`、`NUDAT134TE-1/2`。 | 评估能级/跃迁记录 | `130Sn` 的 `(2+)` 仍带 tentative parentheses；NuDat 和 LiveChart 是同一 ENSDF 评估的不同界面，不能当作独立实验。`132Sn`/`134Te` adopted `B(E2)` 中心值相近，但 `134Te` 原文尚未取得。 |
| [Varner et al. 2005](../../knowledge/sources/varner-2005-coulomb-excitation-132-134sn.md)：`VAR05-1/2/4/6`，PDF pp.391–394，尤其 p.392 Sec.2、p.394 Sec.3/Fig.5。原始 PDF SHA-256 `bf34234243d3a237554fd5be730ff14292b68cf6eb3d5956d847cfc5b854a5f8`。 | 直接 Coulomb-excitation yields 导出的 `B(E2)`；作者解释与响应边界 | `132Sn:0.11±0.03 e²b²`、`134Sn:0.029(5) e²b²`。作者称二者为 preliminary；`132Sn` 的 BaF₂ photon-efficiency calibration 未完成，响应由 simulation 处理；`134Sn` 束流有多种 A=134 污染组分。 |
| [ENSDF `132Sn` Coulomb-excitation subfile](../../knowledge/sources/ensdf-132sn-coulomb-excitation.md)：`ENSDF132C-1/2/3`，PDF p.1。 | 评估来源谱系 | 同表列出 `2005Va31` 的 `48Ti` 靶和 `2005Ra09` 的 C 靶实验；二者同属 HRIBF-ORNL、不同靶反应和会议论文记录。`2005Va31` 已由 Varner 原文核验；`2005Ra09` 的 DOI 为 `10.1016/j.nuclphysa.2005.02.040`（PII `S0375947405001776`），但 publisher 403 且 OpenAlex 无 repository full text。 |
| [ENSDF `134Te` Coulomb-excitation subfile](../../knowledge/sources/ensdf-134te-coulomb-excitation.md)：`ENSDF134TE-1/2/3`，PDF p.1。 | 评估 `B(E2)` 记录 | 给出 `134Te(12C,12C′)`、350 MeV、`B(E2)↑=0.13 4`；Crossref/NSR 身份指向 Barton et al. 2003, DOI `10.1016/S0370-2693(02)03066-6`。ScienceDirect 端点返回 403，故该条仍是评估层证据。 |
| [Li et al. 2004](../../knowledge/sources/li-2004-lifetimes-131ce.md)：`LI04-1/2/4/5/10`，原文 PDF p.3 Table 1、Fig.3；全三页逐页核对，SHA-256 `100a06fc1bb6d7061a153552529c9245f123248f213a93f022b202af97dcdcc5`。 | DSAM 寿命、派生 `B(E2)/Q_t`、作者轨道解释 | 原始表 `27/2−` 行为 `B(E2)=1723(322) e²fm⁴`、`Q_t=2.72(25) eb`。此前 Wiki 误记 `(26)`，已逐字更正。`[514]9/2−/h11/2` 与 `[404]7/2+/g7/2` 的形状驱动方向为作者解释。 |
| [Singh et al. 2016](../../knowledge/sources/singh-2016-lifetime-131ce-133pr.md)：`SI16-2/4/16`，PDF p.5 Table 1、Eqs. (1)–(3)，p.11 refs. [31–32]；原始 PDF SHA-256 `95e0831b9864a58fd1a896a1b20e227d88d9b7aa5de56c738c3792441caa1a30`。 | 独立 plunger/DSAM 实验与旧值重新换算 | 当前实验 `27/2− Q_t=2.26^{+0.37}_{-0.23} eb`；Ref. [32] 同一 Li `τ=1.23(23) ps` 被重新换算为 `2.28(21) eb`，不是额外实验。 |
| [Ding et al. 2021](../../knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md)：`D21-1/4/5/6/9`，原文 pp.10–13 Figs.7–9/Table III；PDF SHA-256 `752d3c5da690c20ec7e188dcc043f9da2a7f062deefc371dd8a497a190b66c37`。 | N=75 实验谱学 + CSM/QTR/PES 模型 | `N=74` `νg7/2`–`νh11/2` gap 是 Nilsson 模型解释；signature splitting 同时依赖 `γ` 和近邻 `νs1/2` Coriolis 混合，不能被当作直接 gap/形状测量。 |
| [AME2020 official table and DOI](../../knowledge/sources/ame2020-sn132-mass-curvature.md)；[Ragnarsson et al. review](../../knowledge/sources/ragnarsson-nilsson-sheline-1978-shell-structure.md) `RS78-1/3`；[Haxel et al. 1949](../../knowledge/sources/haxel-jensen-suess-1949-magic-numbers.md) `HJS49-1`。 | 质量评估 / review synthesis / 历史模型 | HJS 只用于自旋—轨道壳层背景；RNS 用于壳隙依赖形状和观测边界，二者都不是现代 A≈130 单粒子间隔的实验数据。 |

外部文件逐项身份/哈希/定位表见 [run-02 source manifest](20260928-DAY2-shell-gap-single-particle-run-02/source-manifest.tsv)；本批未下载 SI，因为正文图表已经包含本任务所需的观测量和方法。

| [Jones et al. 2010, 132Sn(d,p)133Sn](../../knowledge/sources/jones-2010-133sn-single-particle-transfer.md)：JON10-1、JON10-3/4/5/6；DOI 10.1038/nature09048；SI pp.1–5、Tables 2–4、Fig.4。SI SHA-256 1854f8e4225ca93038e170845b8a6d45e53ccba2a1e62eca50e54aa46bda5d3d。 | 实验截面与角分布；DWBA 提取因子 | SI 可核到差分/角积分截面和 local/global spectroscopic factors；Fig.3 预览展示替代 l 拟合。主文 PDF 端点返回 HTML，不能把该端点称为全文。 |
| [ENSDF 133Sn transfer levels](../../knowledge/sources/ensdf-133sn-transfer-levels.md)：ENSDF133SN-1/3/4/5/6；NuDat adopted-level rows、XREF 与 2010Jo03。 | 评估能级、transfer l 与可能组态 | ENSDF 与 Jones 2010 指向同一实验谱系，不是第二个独立转移实验；1560.9-keV h9/2 候选没有 132Sn(d,p) XREF。 |
| [ENSDF 131Sn hole-side levels](../../knowledge/sources/ensdf-131sn-neutron-hole-levels.md)：ENSDF131SN-1/2/3/4/5；NuDat 3 adopted-level rows。 | 评估能级与空穴侧背景 | 2006 cutoff 早于 Orlandi；后续独立 132Sn(d,t) 全文由 Surrey 仓储取得，评估页仍不代替直接反应数据。 |

| [Orlandi et al. 2018 neutron-hole transfer](../../knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md)：ORL18-1–18；DOI 10.1016/j.physletb.2018.08.005；Surrey delivery PDF SHA-256 0d743eefaa6f6d62d60aa1b7a5ac4d9e87b3327ababd45a3fc04b3232cd3f684。 | 逆运动学 (d,t) 实验截面、DWBA 派生强度、Woods–Saxon 模型与作者解释 | 通读 journal pp.615–620，检查 Figs.1–5 与 Eqs.(1)–(3)；0–65-keV doublet 未分辨、其他势改变 S 约10–20%、作者给 spin-orbit 约±150-keV 系统界。正文没有数据表，核心 S 值列在 Fig.3 讨论中。 |

| [Radford et al. 2005, 126/128/130Sn Coulomb excitation](../../knowledge/sources/radford-2005-130sn-coulomb-excitation-126-130sn.md)：RAD05-1–9；DOI 10.1140/epjad/i2005-06-205-y；PDF SHA-256 9d3325519c41ddf1440b76f2b45dbac0788617ee0c2a872435c6e82b15b123ed。 | 直接 Coulomb-excitation 观测与派生 B(E2) | Table 1 给 130Sn 0.023(5) e²b²，明确标为 preliminary；Fig.1 标出 E(2+)=1221 keV。正文没有原始 yields 表或详细协方差。 |
| [Gray 2021 ANU thesis cross-check](../../knowledge/sources/gray-2021-thesis-electromagnetic-moments-z50.md)：GRAY21-1/2；DOI 10.25911/yd6j-qk37；Chapter 3 Table 3.13 p.75、Ref.[28] p.81；PDF SHA-256 3ff5dc98a995e43133b23889900a3b579e57413a4a836e7264b9c870389fe152。 | 依赖性二次摘录 | thesis 将 130Sn core 强度转列为5.9(1.3) W.u.并引用 Radford 2005；用于检查单位换算，不算第二次实验。 |


## Theory/analysis exercise

**N=82 质量二阶差分。** 定义 `δ₂n(N=82,Z=50)=S₂n(132Sn)-S₂n(134Sn)=ME(130Sn)-2ME(132Sn)+ME(134Sn)`。AME2020 `mass_1` 给出质量超额 `−80132.217±1.873`、`−76546.554±1.976`、`−66433.759±3.167 keV`，得到 `δ₂n=6527.132 keV = 6.527132 MeV`。`rct1` 直接列出 `S₂n(132Sn)=12.5569730±0.0027224 MeV` 和 `S₂n(134Sn)=6.0298413±0.0037328 MeV`，中心值吻合。按三项质量误差对角传播，`σ(δ₂n)=sqrt(1.873²+4×1.976²+3.167²)=5.400 keV`；同一 `132Sn` 质量在二阶差分中系数为 `−2`，不能把两条 `S₂n` 当作互相独立。AME 文件未提供质量/分离能协方差矩阵；此处 5.4 keV 是透明的对角近似。

**N=82 单中子分离能差。** AME2020 的 131Sn、132Sn、133Sn 质量超额分别为 −77264.579±3.621、−76546.554±1.976、−70873.890±1.904 keV，中子质量超额为 8071.31806±0.00044 keV。由质量差得到 Sn(132Sn)=7353.293 keV、Sn(133Sn)=2398.654 keV，故 Δn(82)=Sn(132Sn)−Sn(133Sn)=ME(131Sn)−2ME(132Sn)+ME(133Sn)=4954.639 keV。按三条 Sn 质量误差互相独立传播，σ=5.688 keV；中子质量在差值中相消，且输入文件不含 fitted-mass covariance。NuDat 133Sn header 的 adopted Sn=2402(4) keV 与质量表导出的 2398.654 keV 在合并误差内一致。该数是包含奇偶配对和质量面贡献的经验壳闭合指标，不能直接读成某个单粒子轨道间隔。

**Isotope/isotone 能级和集体强度对照。** `130Sn (N=80)` 的 `(2+)` 候选在 `1221.26(5) keV`，`132Sn (N=82)` 的 `2+` 在 `4041.2(15) keV`，`134Sn (N=84)` 的 `2+` 在 `725.6 keV`；能级峰值落在 N=82。`132Sn/134Te` 同为 N=82，`E(2+)` 从 `4.0412` 降到 `1.27911 MeV`，而 NuDat adopted `B(E2)` 在其显示不确定度内相近（`5.5 15` 与 `6.3 20 W.u.`）。两个观测量相互补充但不是同一物理量；数据库评估与 Varner 的 `B(E2)` 均不能直接给出单粒子轨道间隔。`134Te` 的 `2003Ba01` 全文仍未取得。

**寿命到 `Q_t` 的角动量转换。** 对 `131Ce` `27/2−→23/2−`，原表 `B(E2)=1723(322)e²fm⁴ =0.1723(322)e²b²`。纯 `K=11/2` 转子因子 `C²=|⟨IK20|I−2,K⟩|²=0.233846` 给 `Q_t=sqrt(16πB(E2)/(5C²))=2.7216±0.2543 eb`，重现 Li 原表 `2.72(25)`。用 Singh Eq. (2)–(3) 的 rotation-aligned `j=11/2` 混合，`a_K²=2^{-11} binom(11,11/2+K)`，得到 `C_eff=Σ_K a_K²⟨IK20|I−2,K⟩=0.580021`，同一强度换算为 `Q_t=2.269±0.212 eb`，与其 Ref. [32] 对 Li 同一 `1.23(23) ps` 重新换算的 `2.28(21) eb` 相合。表面上的 `0.44 eb` 差值由角动量转换约定解释；两行共享同一原始寿命，不可算作独立 `Q_t` 测量。

**130Sn direct B(E2) 与单位交叉核验。** Radford Table 1 给 B(E2;0+→2+)=0.023(5) e²b²。用标准 Weisskopf E2 表达式 B_W(E2,A)=1/(4π)(3/5)²(1.2A^(1/3))⁴e²，A=130 时 1 W.u.=0.003912 e²b²，因此该值为 5.88(1.28) W.u.；Gray 2021 Table 3.13 的5.9(1.3) W.u.是同一 Radford 数据的再表述。Varner 132Sn 的0.11(3) e²b²与 Radford 130Sn 的中心值之比为4.78±1.67（仅按两项引述误差独立传播）。NuDat gamma row 的132Sn 5.5(15) W.u.换算为约0.0220(60) e²b²，与130Sn强度相近；但NuDat adopted-level row另列0.11(3)且不打印单位，正好对应Varner数值。Varner效率校准未完成；不同实验和字段不作平均。

## Counter-evidence and missing companion observables

- Radford Table 1 已给出 130Sn B(E2)=0.023(5) e²b²，但明确为 preliminary；束流含11% 7− isomer，短文未列事件 yields/完整系统误差。它填补数据库字段空白，但不是最终精度值。
- Varner 的 `132Sn` 和 `134Sn` Coulomb-excitation strengths 均标为 preliminary；`132Sn` BaF₂ photon-efficiency 的实验校准尚未完成，`134Sn` 束流 Sn 仅占 `25.6(2)%`。作者用 response simulation、Bragg composition monitor 和 control spectra 处理，但当前记录没有完整事件级 response/covariance。
- `134Te` 的 adopted B(E2) 源 `2003Ba01`（DOI `10.1016/S0370-2693(02)03066-6`）是另一 Coulomb-excitation 反应，但 ScienceDirect 返回 403；它只能作为 ENSDF/NuDat 评估结果，不能写成 Codex 直接核过的原文事实。`130Sn` B(E2) 的 Raman et al. 2001 compilation DOI `10.1006/adnd.2001.0858` 被 OpenAlex 标记为 closed、无 repository full text。
- `131Ce` 模式问题还缺 transition-level `δ`、偏振、同一 band 的寿命/absolute `B(E2)/B(M1)`；现有 Li/Singh lifetime controls 不是 thesis Bands 1–7 的 partner-resolved matrix。
- **Source independence:** AME mass files are one evaluation; LiveChart/NuDat expose shared ENSDF evaluations. Li/Singh are separate 131Ce lifetime experiments but Singh re-tabulates Li’s same lifetime; Ding 2021 contains distinct 131Ba/133Ce reactions. Jones 133Sn (d,p), Orlandi 131Sn (d,t), and Radford 130Sn CoulEx are separate data sets, though Radford/Varner share the HRIBF program; Gray’s 5.9-W.u. table repeats Radford rather than adding an experiment.

- 133Sn transfer 因子依赖 DWBA 和 local/global optical potential，Fig.3 还展示不同 l 的替代拟合；需要独立 transfer observable、强度分布和模型敏感性才能约束组态纯度。
- 131Sn 当前引用的是 2006 ENSDF 评估；空穴侧低能赋值含 systematics/moment 依据，且 11/2− isomer 的绝对激发能标为 0+X。Orlandi 的全文显示 0–65-keV doublet 的纯 d3/2 拟合 S=5.0(5) 超出 2j+1=4；只有假定 h11/2 强度为12时，S(d3/2)=4.3(5)。其他光学势改变 S 约10–20%，d5/2 强度 6.4(1.8)，7/2+ 候选未观测；这些边界不支持把低态强度写成无模型依赖的占据数。
- AME 单中子差和二中子曲率都含 pairing/smooth-mass terms；无质量协方差，二者也不能由代数关系消去这些物理项。

- NuDat 3 对 132Sn 同一 2+→0+跃迁分别显示 gamma-table B(E2)=5.5(15) W.u. 和 adopted-level B(E2)=0.11(3)（后一字段未打印单位）；按标准 W.u. 换算前者约0.0220(60)e²b²，后者数值又与Varner直接preliminary值相同。需要追踪不同字段的原始输入和效率处理，不能将其当作同一条测量。
- Radford结论称130Sn强度约1.4 single-particle units，但Table 1数值按标准Weisskopf公式为5.88(1.28) W.u.；Gray依赖性重表列5.9(1.3) W.u.，须澄清原文SP-unit术语，保留原文和换算两者。

- NuDat 3 对 132Sn 同一2+→0+跃迁分别显示 gamma-table B(E2)=5.5(15) W.u. 和 adopted-level B(E2)=0.11(3)（后一字段未打印单位）；按标准W.u.换算前者约0.0220(60)e²b²，后一数值又与Varner直接preliminary值相同。需要追踪两字段各自的原始输入和效率处理，不能将其当作同一条测量。

- NuDat 2+ lifetime 2.4 fs 的 level comment 明确标注为 from B(E2) value；它与 gamma-table 5.5(15) W.u. 不是两个独立的观测。Adopted-level 0.11(3) 无单位但带 Coulomb-excitation XREF，与 Varner 直接数值相同；5.5-W.u. 字段的底层输入仍待查。

## Knowledge Impact and Learning Decision

**Decision: revises（修正证据地图）。** 130Sn B(E2)不再是数据库缺项：Radford et al. 2005公开原文直接给出0.023(5)e²b²，并标为preliminary；标准Weisskopf换算为5.88(1.28)W.u.，Gray 2021 Table 3.13以同一来源重列5.9(1.3)W.u.。这与NuDat 132Sn gamma-table 5.5(15)W.u.相近。

NuDat 的 2+ T1/2=2.4 fs 行明确注明该值由 B(E2) 推得，因此它不是 gamma-table B(E2) 的独立确认。gamma-table 的 5.5(15) W.u. 与 adopted-level 的 0.11(3)（无单位、有 Coulomb-excitation XREF）是不同字段；后者数值与 Varner 直接的 preliminary 0.11(3) e²b² 一致。Varner photon-efficiency calibration 尚未完成，5.5-W.u. 字段的原始输入也未追清，故暂不调和或平均。

N=82 的高 E(2+)、AME 质量指标、130Sn direct-preliminary B(E2)、Varner 132Sn 强度和 transfer 两侧现在构成更完整的证据链；配对/协方差、校准和数据库输入谱系仍限制壳隙定量分解。Radford 文中“1.4 single-particle units”与标准换算5.9 W.u.的表述差异保留为单位边界。Orlandi 的131Sn空穴证据与Jones的133Sn粒子证据仍不等于直接测出唯一单粒子gap。

## Durable knowledge delta

- [A≈130 shell-gap/orbital/observable bridge](../../knowledge/projects/a130-shell-gap-orbital-observable.md)：加入 `130Sn/132Sn/134Sn` mass/level/`B(E2)` 表、`132Sn/134Te` isotone 对照、AME2020 二阶差分和 `131Ce` `Q_t` 转换复算。
- [AME2020 mass source](../../knowledge/sources/ame2020-sn132-mass-curvature.md)：保存 `mass_1/rct1` 行、SHA-256、精确质量/S₂n locator 与协方差边界。
- [IAEA/ENSDF levels source](../../knowledge/sources/iaea-livechart-132sn-134te-levels.md)、[Varner 2005 primary source](../../knowledge/sources/varner-2005-coulomb-excitation-132-134sn.md)、[ENSDF Sn CoulEx sheet](../../knowledge/sources/ensdf-132sn-coulomb-excitation.md)、[ENSDF Te CoulEx sheet](../../knowledge/sources/ensdf-134te-coulomb-excitation.md)：分别保存 adopted level rows、初步直接 `B(E2)` 数值和 evaluation/shared-target lineage。
- [Li 2004 source](../../knowledge/sources/li-2004-lifetimes-131ce.md) 的 `LI04-2` 由原始 Table 1 末位 `2.72(25)` 更正；[Singh 2016](../../knowledge/sources/singh-2016-lifetime-131ce-133pr.md) 增 `SI16-16` 重算行；[Ding 2021](../../knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md) 增 `D21-9` model-only `N=74` gap claim。既有页面级 review 状态均保留，新 claim 维持 `needs_review: true`。
- [A≈130 thesis matrix](../../knowledge/projects/a130-thesis-evidence-matrix.md) 的下一步改为指向本 bridge，避免重复复制壳隙数据表；[Research Questions](../../knowledge/questions.md) 新增 `N=82 shell-gap decomposition` 问题。

- [ENSDF 131Sn hole-side levels](../../knowledge/sources/ensdf-131sn-neutron-hole-levels.md)：新增 131Sn adopted rows、S(n)、XREF 和 2006 cutoff 边界；[A≈130 shell-gap bridge](../../knowledge/projects/a130-shell-gap-orbital-observable.md) 加入 131Sn/133Sn 两侧证据、AME 单中子差分和可复用误差传播。

- [Orlandi et al. 2018 full-text source](../../knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md)：以 Surrey PDF SHA-256 固定 (d,t) 反应、逐态 DWBA 强度、doublet/光学势误差、3p/2d spin-orbit 分裂和 Eqs.(1)–(3) 的径向机制解释。DOAJ 与 OpenAIRE 元数据快照保留在 raw source bundle。

- [Radford 2005 130Sn primary Coulomb-excitation source](../../knowledge/sources/radford-2005-130sn-coulomb-excitation-126-130sn.md)：固定Table 1的preliminary B(E2)=0.023(5)e²b²、Fig.1能级与HRIBF束流/效率边界。
- [Gray 2021 dependent thesis cross-check](../../knowledge/sources/gray-2021-thesis-electromagnetic-moments-z50.md)：Table 3.13的5.9(1.3) W.u.回链到Radford 2005，记录为同数据重述。

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/sources/ame2020-sn132-mass-curvature.md",
      "summary": "Persisted the three AME2020 Sn mass excesses, two direct rct1 S2n rows, file URLs and payload hashes for the N=82 second-difference exercise.",
      "anchor": "AME2020 shell-gap mass-curvature records",
      "sources": [
        {
          "path": "knowledge/sources/ame2020-sn132-mass-curvature.md",
          "locator": "AME20-130SN-1"
        },
        {
          "path": "knowledge/sources/ame2020-sn132-mass-curvature.md",
          "locator": "AME20-132SN-1"
        },
        {
          "path": "knowledge/sources/ame2020-sn132-mass-curvature.md",
          "locator": "AME20-134SN-1"
        },
        {
          "path": "knowledge/sources/ame2020-sn132-mass-curvature.md",
          "locator": "AME20-RCT1-132SN-1"
        },
        {
          "path": "knowledge/sources/ame2020-sn132-mass-curvature.md",
          "locator": "AME20-RCT1-134SN-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
      "summary": "Persisted adopted level records for the Sn isotope and N=82 Sn/Te isotone comparisons, including NuDat transition-strength displays and the 130Sn B(E2) coverage boundary.",
      "anchor": "Adopted low-lying level records",
      "sources": [
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "LC130SN-1"
        },
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "LC132SN-1"
        },
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "LC134SN-1"
        },
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "LC134TE-1"
        },
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "NUDAT132SN-2"
        },
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "NUDAT132SN-3"
        },
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "NUDAT134TE-1"
        },
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "NUDAT134TE-2"
        },
        {
          "path": "knowledge/sources/radford-2005-130sn-coulomb-excitation-126-130sn.md",
          "locator": "RAD05-2"
        },
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "NUDAT132SN-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/varner-2005-coulomb-excitation-132-134sn.md",
      "summary": "Added source-grounded preliminary B(E2) values for 132Sn and 134Sn with efficiency, response and mixed-beam limits.",
      "anchor": "Key Results",
      "sources": [
        {
          "path": "knowledge/sources/varner-2005-coulomb-excitation-132-134sn.md",
          "locator": "VAR05-1"
        },
        {
          "path": "knowledge/sources/varner-2005-coulomb-excitation-132-134sn.md",
          "locator": "VAR05-2"
        },
        {
          "path": "knowledge/sources/varner-2005-coulomb-excitation-132-134sn.md",
          "locator": "VAR05-4"
        },
        {
          "path": "knowledge/sources/varner-2005-coulomb-excitation-132-134sn.md",
          "locator": "VAR05-6"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/ensdf-132sn-coulomb-excitation.md",
      "summary": "Persisted the ENSDF 132Sn Coulomb-excitation value and its same-HRIBF, different-target reference lineage.",
      "anchor": "Key Results",
      "sources": [
        {
          "path": "knowledge/sources/ensdf-132sn-coulomb-excitation.md",
          "locator": "ENSDF132C-1"
        },
        {
          "path": "knowledge/sources/ensdf-132sn-coulomb-excitation.md",
          "locator": "ENSDF132C-2"
        },
        {
          "path": "knowledge/sources/ensdf-132sn-coulomb-excitation.md",
          "locator": "ENSDF132C-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/ensdf-134te-coulomb-excitation.md",
      "summary": "Persisted the adopted 134Te Coulomb-excitation B(E2), reaction and blocked-primary-text boundary.",
      "anchor": "Key Results",
      "sources": [
        {
          "path": "knowledge/sources/ensdf-134te-coulomb-excitation.md",
          "locator": "ENSDF134TE-1"
        },
        {
          "path": "knowledge/sources/ensdf-134te-coulomb-excitation.md",
          "locator": "ENSDF134TE-2"
        },
        {
          "path": "knowledge/sources/ensdf-134te-coulomb-excitation.md",
          "locator": "ENSDF134TE-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/li-2004-lifetimes-131ce.md",
      "summary": "Corrected LI04-2 to the directly inspected 2.72(25) eb Table 1 value and documented the self-audit.",
      "anchor": "Source table transcription audit (2026-09-28)",
      "sources": [
        {
          "path": "knowledge/sources/li-2004-lifetimes-131ce.md",
          "locator": "LI04-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/singh-2016-lifetime-131ce-133pr.md",
      "summary": "Added the dependent Ref. [32] re-calculation of Li 2004 27/2− Qt to preserve source lineage.",
      "anchor": "SI16-16",
      "sources": [
        {
          "path": "knowledge/sources/singh-2016-lifetime-131ce-133pr.md",
          "locator": "SI16-16"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md",
      "summary": "Added the source-located N=74 Nilsson gap statement as a model result with needs_review retained.",
      "anchor": "D21-9",
      "sources": [
        {
          "path": "knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md",
          "locator": "D21-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-shell-gap-orbital-observable.md",
      "summary": "Expanded the canonical bridge with Sn isotope and Sn/Te isotone indicators, AME2020 delta_2n, direct preliminary B(E2), N=74 model evidence and a reproducible 131Ce Qt conversion check.",
      "anchor": "A≈130 shell-gap/orbital case study (Day 2; 2026-09-28)",
      "sources": [
        {
          "path": "knowledge/sources/ame2020-sn132-mass-curvature.md",
          "locator": "AME20-130SN-1"
        },
        {
          "path": "knowledge/sources/ame2020-sn132-mass-curvature.md",
          "locator": "AME20-132SN-1"
        },
        {
          "path": "knowledge/sources/ame2020-sn132-mass-curvature.md",
          "locator": "AME20-134SN-1"
        },
        {
          "path": "knowledge/sources/ame2020-sn132-mass-curvature.md",
          "locator": "AME20-RCT1-132SN-1"
        },
        {
          "path": "knowledge/sources/ame2020-sn132-mass-curvature.md",
          "locator": "AME20-RCT1-134SN-1"
        },
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "LC130SN-1"
        },
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "LC132SN-1"
        },
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "LC134SN-1"
        },
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "LC134TE-1"
        },
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "NUDAT134TE-1"
        },
        {
          "path": "knowledge/sources/varner-2005-coulomb-excitation-132-134sn.md",
          "locator": "VAR05-1"
        },
        {
          "path": "knowledge/sources/varner-2005-coulomb-excitation-132-134sn.md",
          "locator": "VAR05-2"
        },
        {
          "path": "knowledge/sources/li-2004-lifetimes-131ce.md",
          "locator": "LI04-2"
        },
        {
          "path": "knowledge/sources/li-2004-lifetimes-131ce.md",
          "locator": "LI04-5"
        },
        {
          "path": "knowledge/sources/singh-2016-lifetime-131ce-133pr.md",
          "locator": "SI16-16"
        },
        {
          "path": "knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md",
          "locator": "D21-1"
        },
        {
          "path": "knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md",
          "locator": "D21-6"
        },
        {
          "path": "knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md",
          "locator": "D21-9"
        },
        {
          "path": "knowledge/sources/ensdf-134te-coulomb-excitation.md",
          "locator": "ENSDF134TE-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-thesis-evidence-matrix.md",
      "summary": "Updated the next matrix increment to point to the canonical shell-gap bridge and avoid duplicate evidence rows.",
      "anchor": "Day 2 shell-gap/orbital evidence is persisted in [[a130-shell-gap-orbital-observable]]",
      "sources": [
        {
          "path": "knowledge/sources/ame2020-sn132-mass-curvature.md",
          "locator": "AME20-132SN-1"
        },
        {
          "path": "knowledge/sources/li-2004-lifetimes-131ce.md",
          "locator": "LI04-2"
        },
        {
          "path": "knowledge/sources/ding-2021-131ba-133ce-signature-splitting.md",
          "locator": "D21-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/questions.md",
      "summary": "Added an open question to partition the 132Sn N=82 mass-curvature and electromagnetic signatures into shell-gap, pairing and smooth-surface contributions.",
      "anchor": "N=82 shell-gap decomposition",
      "sources": [
        {
          "path": "knowledge/sources/ame2020-sn132-mass-curvature.md",
          "locator": "AME20-RCT1-132SN-1"
        },
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "LC132SN-1"
        },
        {
          "path": "knowledge/sources/varner-2005-coulomb-excitation-132-134sn.md",
          "locator": "VAR05-1"
        },
        {
          "path": "knowledge/sources/ensdf-134te-coulomb-excitation.md",
          "locator": "ENSDF134TE-1"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-3"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-4"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-6"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-8"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-10"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-11"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-12"
        },
        {
          "path": "knowledge/sources/radford-2005-130sn-coulomb-excitation-126-130sn.md",
          "locator": "RAD05-2"
        },
        {
          "path": "knowledge/sources/gray-2021-thesis-electromagnetic-moments-z50.md",
          "locator": "GRAY21-1"
        },
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "NUDAT132SN-2"
        },
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "NUDAT132SN-3"
        },
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "NUDAT132SN-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "Added source-index entries for the two AME/level data pages, Varner primary paper and two ENSDF Coulomb-excitation subfiles.",
      "anchor": "[[ame2020-sn132-mass-curvature]]",
      "sources": [
        {
          "path": "knowledge/sources/ame2020-sn132-mass-curvature.md",
          "locator": "AME20-132SN-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "Added source-index entries for the two AME/level data pages, Varner primary paper and two ENSDF Coulomb-excitation subfiles.",
      "anchor": "[[iaea-livechart-132sn-134te-levels]]",
      "sources": [
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "LC132SN-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "Added source-index entries for the two AME/level data pages, Varner primary paper and two ENSDF Coulomb-excitation subfiles.",
      "anchor": "[[varner-2005-coulomb-excitation-132-134sn]]",
      "sources": [
        {
          "path": "knowledge/sources/varner-2005-coulomb-excitation-132-134sn.md",
          "locator": "VAR05-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "Added source-index entries for the two AME/level data pages, Varner primary paper and two ENSDF Coulomb-excitation subfiles.",
      "anchor": "[[ensdf-132sn-coulomb-excitation]]",
      "sources": [
        {
          "path": "knowledge/sources/ensdf-132sn-coulomb-excitation.md",
          "locator": "ENSDF132C-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "Added source-index entries for the two AME/level data pages, Varner primary paper and two ENSDF Coulomb-excitation subfiles.",
      "anchor": "[[ensdf-134te-coulomb-excitation]]",
      "sources": [
        {
          "path": "knowledge/sources/ensdf-134te-coulomb-excitation.md",
          "locator": "ENSDF134TE-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/ame2020-sn132-mass-curvature.md",
      "summary": "Added verified AME2020 neutron, 131Sn and 133Sn mass rows used for the adjacent one-neutron difference.",
      "anchor": "AME2020 shell-gap mass-curvature records",
      "sources": [
        {
          "path": "knowledge/sources/ame2020-sn132-mass-curvature.md",
          "locator": "AME20-N-1"
        },
        {
          "path": "knowledge/sources/ame2020-sn132-mass-curvature.md",
          "locator": "AME20-131SN-1"
        },
        {
          "path": "knowledge/sources/ame2020-sn132-mass-curvature.md",
          "locator": "AME20-132SN-1"
        },
        {
          "path": "knowledge/sources/ame2020-sn132-mass-curvature.md",
          "locator": "AME20-133SN-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/ensdf-131sn-neutron-hole-levels.md",
      "summary": "Added evaluated N=81 low-lying level rows, S(n), XREF and pre-2018 evaluation boundary.",
      "anchor": "Key Results",
      "sources": [
        {
          "path": "knowledge/sources/ensdf-131sn-neutron-hole-levels.md",
          "locator": "ENSDF131SN-1"
        },
        {
          "path": "knowledge/sources/ensdf-131sn-neutron-hole-levels.md",
          "locator": "ENSDF131SN-2"
        },
        {
          "path": "knowledge/sources/ensdf-131sn-neutron-hole-levels.md",
          "locator": "ENSDF131SN-3"
        },
        {
          "path": "knowledge/sources/ensdf-131sn-neutron-hole-levels.md",
          "locator": "ENSDF131SN-4"
        },
        {
          "path": "knowledge/sources/ensdf-131sn-neutron-hole-levels.md",
          "locator": "ENSDF131SN-5"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/a130-shell-gap-orbital-observable.md",
      "summary": "Added Radford’s preliminary direct 130Sn B(E2), standard W.u. conversion and Gray thesis re-tabulation; exposed distinct 132Sn Varner/NuDat strength fields while preserving source/calibration limits.",
      "anchor": "### N=82 particle-hole sides and one-neutron mass difference",
      "sources": [
        {
          "path": "knowledge/sources/ame2020-sn132-mass-curvature.md",
          "locator": "AME20-N-1"
        },
        {
          "path": "knowledge/sources/ame2020-sn132-mass-curvature.md",
          "locator": "AME20-131SN-1"
        },
        {
          "path": "knowledge/sources/ame2020-sn132-mass-curvature.md",
          "locator": "AME20-132SN-1"
        },
        {
          "path": "knowledge/sources/ame2020-sn132-mass-curvature.md",
          "locator": "AME20-133SN-1"
        },
        {
          "path": "knowledge/sources/jones-2010-133sn-single-particle-transfer.md",
          "locator": "JON10-1"
        },
        {
          "path": "knowledge/sources/jones-2010-133sn-single-particle-transfer.md",
          "locator": "JON10-4"
        },
        {
          "path": "knowledge/sources/jones-2010-133sn-single-particle-transfer.md",
          "locator": "JON10-5"
        },
        {
          "path": "knowledge/sources/ensdf-133sn-transfer-levels.md",
          "locator": "ENSDF133SN-1"
        },
        {
          "path": "knowledge/sources/ensdf-133sn-transfer-levels.md",
          "locator": "ENSDF133SN-3"
        },
        {
          "path": "knowledge/sources/ensdf-133sn-transfer-levels.md",
          "locator": "ENSDF133SN-5"
        },
        {
          "path": "knowledge/sources/ensdf-131sn-neutron-hole-levels.md",
          "locator": "ENSDF131SN-2"
        },
        {
          "path": "knowledge/sources/ensdf-131sn-neutron-hole-levels.md",
          "locator": "ENSDF131SN-3"
        },
        {
          "path": "knowledge/sources/ensdf-131sn-neutron-hole-levels.md",
          "locator": "ENSDF131SN-4"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-1"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-2"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-3"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-4"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-5"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-6"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-7"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-8"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-9"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-10"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-11"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-12"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-13"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-14"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-15"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-16"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-17"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-18"
        },
        {
          "path": "knowledge/sources/radford-2005-130sn-coulomb-excitation-126-130sn.md",
          "locator": "RAD05-2"
        },
        {
          "path": "knowledge/sources/radford-2005-130sn-coulomb-excitation-126-130sn.md",
          "locator": "RAD05-3"
        },
        {
          "path": "knowledge/sources/radford-2005-130sn-coulomb-excitation-126-130sn.md",
          "locator": "RAD05-5"
        },
        {
          "path": "knowledge/sources/radford-2005-130sn-coulomb-excitation-126-130sn.md",
          "locator": "RAD05-6"
        },
        {
          "path": "knowledge/sources/radford-2005-130sn-coulomb-excitation-126-130sn.md",
          "locator": "RAD05-8"
        },
        {
          "path": "knowledge/sources/gray-2021-thesis-electromagnetic-moments-z50.md",
          "locator": "GRAY21-1"
        },
        {
          "path": "knowledge/sources/gray-2021-thesis-electromagnetic-moments-z50.md",
          "locator": "GRAY21-2"
        },
        {
          "path": "knowledge/sources/varner-2005-coulomb-excitation-132-134sn.md",
          "locator": "VAR05-1"
        },
        {
          "path": "knowledge/sources/varner-2005-coulomb-excitation-132-134sn.md",
          "locator": "VAR05-4"
        },
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "NUDAT132SN-2"
        },
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "NUDAT132SN-3"
        },
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "NUDAT132SN-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "Added Jones 2010 and ENSDF 131Sn/133Sn source index entries.",
      "anchor": "[[jones-2010-133sn-single-particle-transfer]]",
      "sources": [
        {
          "path": "knowledge/sources/jones-2010-133sn-single-particle-transfer.md",
          "locator": "JON10-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "Added Jones 2010 and ENSDF 131Sn/133Sn source index entries.",
      "anchor": "[[ensdf-133sn-transfer-levels]]",
      "sources": [
        {
          "path": "knowledge/sources/ensdf-133sn-transfer-levels.md",
          "locator": "ENSDF133SN-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "Added the 131Sn hole-side evaluation source to the index.",
      "anchor": "[[ensdf-131sn-neutron-hole-levels]]",
      "sources": [
        {
          "path": "knowledge/sources/ensdf-131sn-neutron-hole-levels.md",
          "locator": "ENSDF131SN-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/questions.md",
      "summary": "Expanded the N=82 question with particle-hole evidence and the distinct one-neutron mass indicator.",
      "anchor": "N=82 shell-gap decomposition",
      "sources": [
        {
          "path": "knowledge/sources/ame2020-sn132-mass-curvature.md",
          "locator": "AME20-131SN-1"
        },
        {
          "path": "knowledge/sources/ame2020-sn132-mass-curvature.md",
          "locator": "AME20-133SN-1"
        },
        {
          "path": "knowledge/sources/jones-2010-133sn-single-particle-transfer.md",
          "locator": "JON10-4"
        },
        {
          "path": "knowledge/sources/ensdf-131sn-neutron-hole-levels.md",
          "locator": "ENSDF131SN-2"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-3"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-4"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-6"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-8"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-10"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-11"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-12"
        },
        {
          "path": "knowledge/sources/radford-2005-130sn-coulomb-excitation-126-130sn.md",
          "locator": "RAD05-2"
        },
        {
          "path": "knowledge/sources/gray-2021-thesis-electromagnetic-moments-z50.md",
          "locator": "GRAY21-1"
        },
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "NUDAT132SN-2"
        },
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "NUDAT132SN-3"
        },
        {
          "path": "knowledge/sources/iaea-livechart-132sn-134te-levels.md",
          "locator": "NUDAT132SN-4"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
      "summary": "Expanded the Orlandi record to a hash-verified Surrey repository full-text audit of pp.615–620, Figs.1–5, Eqs.1–3, quantitative strengths and model/uncertainty limits.",
      "anchor": "Key Results",
      "sources": [
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-1"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-2"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-3"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-4"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-5"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-6"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-7"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-8"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-9"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-10"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-11"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-12"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-13"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-14"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-15"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-16"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-17"
        },
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-18"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "Indexed the Orlandi 2018 neutron-removal source and its Surrey full-text evidence boundary.",
      "anchor": "[[orlandi-2018-131sn-neutron-hole-transfer]]",
      "sources": [
        {
          "path": "knowledge/sources/orlandi-2018-131sn-neutron-hole-transfer.md",
          "locator": "ORL18-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/radford-2005-130sn-coulomb-excitation-126-130sn.md",
      "summary": "Added the direct preliminary 130Sn B(E2), level-energy locator, inverse-kinematics method and explicit beam/error boundaries.",
      "anchor": "Key Results",
      "sources": [
        {
          "path": "knowledge/sources/radford-2005-130sn-coulomb-excitation-126-130sn.md",
          "locator": "RAD05-1"
        },
        {
          "path": "knowledge/sources/radford-2005-130sn-coulomb-excitation-126-130sn.md",
          "locator": "RAD05-2"
        },
        {
          "path": "knowledge/sources/radford-2005-130sn-coulomb-excitation-126-130sn.md",
          "locator": "RAD05-3"
        },
        {
          "path": "knowledge/sources/radford-2005-130sn-coulomb-excitation-126-130sn.md",
          "locator": "RAD05-4"
        },
        {
          "path": "knowledge/sources/radford-2005-130sn-coulomb-excitation-126-130sn.md",
          "locator": "RAD05-5"
        },
        {
          "path": "knowledge/sources/radford-2005-130sn-coulomb-excitation-126-130sn.md",
          "locator": "RAD05-6"
        },
        {
          "path": "knowledge/sources/radford-2005-130sn-coulomb-excitation-126-130sn.md",
          "locator": "RAD05-7"
        },
        {
          "path": "knowledge/sources/radford-2005-130sn-coulomb-excitation-126-130sn.md",
          "locator": "RAD05-8"
        },
        {
          "path": "knowledge/sources/radford-2005-130sn-coulomb-excitation-126-130sn.md",
          "locator": "RAD05-9"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/gray-2021-thesis-electromagnetic-moments-z50.md",
      "summary": "Recorded Gray thesis Table 3.13 as a dependent 5.9(1.3)-W.u. restatement of Radford 2005 and traced its DOI citation.",
      "anchor": "Key Results",
      "sources": [
        {
          "path": "knowledge/sources/gray-2021-thesis-electromagnetic-moments-z50.md",
          "locator": "GRAY21-1"
        },
        {
          "path": "knowledge/sources/gray-2021-thesis-electromagnetic-moments-z50.md",
          "locator": "GRAY21-2"
        },
        {
          "path": "knowledge/sources/gray-2021-thesis-electromagnetic-moments-z50.md",
          "locator": "GRAY21-3"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "Indexed Radford 2005 direct 130Sn Coulomb-excitation value.",
      "anchor": "[[radford-2005-130sn-coulomb-excitation-126-130sn]]",
      "sources": [
        {
          "path": "knowledge/sources/radford-2005-130sn-coulomb-excitation-126-130sn.md",
          "locator": "RAD05-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "Indexed Gray thesis cross-check and its dependent-source boundary.",
      "anchor": "[[gray-2021-thesis-electromagnetic-moments-z50]]",
      "sources": [
        {
          "path": "knowledge/sources/gray-2021-thesis-electromagnetic-moments-z50.md",
          "locator": "GRAY21-1"
        }
      ]
    }
  ]
}
```

## Open questions and belief revision

- Orlandi 2018 全文已核；保留 0–65-keV doublet 假设、约10–20% optical-potential sensitivity、±150-keV unobserved-state boundary，以及无表格、关键值位于 Fig.3 文本讨论的定位限制。

- AME2020 `δ₂n` is a large shell-closure indicator, but the source files lack covariance and the second difference still contains pairing/smooth-surface terms. `130Sn` has only a tentative `(2+)` record in the queried ENSDF page; its `B(E2)` field is absent there. The closed Raman 2001 compilation and the 2003 `134Te` primary source are the highest-information full-text routes if institutional access becomes available.
- The `132Sn/134Te` isotope/isotone comparison warns against reading a single `E(2+)` as the single-particle gap: the evaluated `B(E2)` values in W.u. are similar within their uncertainties although their first `2+` energies differ substantially.
- **续接信念修订：** Radford 130Sn 的直接初级B(E2)已经补上；NuDat gamma-table 5.5 W.u.与T1/2=2.4 fs是B(E2)派生链，而adopted-level 0.11(3)字段与Varner CoulEx数值相同。该字段谱系与Varner效率边界仍未最终解释。

Orlandi 全文把空穴侧证据从“摘要级支持”推进到带条件的定量 DWBA 强度：332-keV s1/2 S=2.4(2)、1654-keV d5/2 S=6.4(1.8)，而 0–65-keV doublet 的 d3/2 结果取决于 h11/2 假设。替代光学势改变 S 约10–20%；作者以 ±150-keV 处理可能未观测态。自旋轨道的约50%归一化分裂降低由同强度 Woods–Saxon 模型归因于径向延展，仍是模型支持而非唯一解释。

**信念修订：** 主动回忆把 `E(2+)`、`B(E2)` 和质量差分视为互补证据；数值练习确认 N=82 的质量曲率很大，但不能将 `6.527 MeV` 直接称作单粒子能隙。另一个原本可能看作 Li/Singh 测量冲突的 `Q_t` 差异，经 `K` / rotational-aligned CG 复算后，改为同一寿命在不同转换约定下的派生值差异。


- Radford 2005 direct 130Sn B(E2) is now available but preliminary; the 1981 130Sn levels/transition-probability article remains closed. A unit/lineage audit is needed for the Radford “1.4 single-particle units” conclusion and NuDat 132Sn 5.5(15)-W.u. vs 0.11(3) fields. Varner efficiency calibration and AME covariance remain unresolved.
## L0–L4 state

- **L0：complete。** AME2020 官方文件、DOI、文件哈希与行 locator 已核验；Varner 2005 期刊 PDF 哈希、图表和不完整效率标定限制已核验；Li 2004 原始 Table 1 与 Singh 2016 Table 1 / Eq. (1)–(3) 已逐项对照；Ding 2021 Fig. 8–9 / Table III 已核对。
- **L1：complete。** Source 页面、A≈130 shell-gap project、thesis matrix 路由和开放问题已相连；新 source claims 保留原 review 状态，新加条目 `needs_review: true`。
- **L2：complete for this bounded Day 2 comparison。** 完成主动回忆、N=82 mass second difference、同位素/同位素链对照、`Q_t` rotor/K-mixing 复算、反证和来源依赖审计。
- **L3：candidate-L3。** 后续可研究 131Ce/131Ba/133Ce 的轨道交叉与模型可识别性，但公开源仍缺目标带完整的 δ、偏振、绝对强度和测量协方差；`130Sn` B(E2)、Raman 2001、`2005Ra09`（DOI `10.1016/j.nuclphysa.2005.02.040`）与 `2003Ba01` 是未闭合的新证据路线。
- **L4：not-ready。** 没有 `131Ce`/`N=82` 事件级数据、完整探测器响应和校准协方差、AME fitted-mass covariance 或可重跑代码包；Varner 也明确表示 `132Sn` 光子效率实验校准尚未完成。本轮只做可复算的表值与公式练习，不构造代理拟合。

- **本次续接来源边界：** Jones 2010 SI 的转移表格已核；Orlandi 2018 的 Surrey repository PDF 六页已通读并检查五幅图和三个公式；其七页 PDF 含一页仓储封面。该边界不提升任何 claim 的 human-reviewed 状态。

## Verification and continuation

- H2 暂存后再次运行 clean_knowledge_eol_dirty.py：exit 1，输出 7 个已暂存修改为 STAGED-NOT-TOUCHED，11 个本轮新增 knowledge Markdown 为 REVIEW-UNSAFE A（该脚本只比较 HEAD 已存在文件，不能对新增路径做换行回滚）。逐个扫描这11个新文件均无 CR 字节且以 LF 换行结束；这些路径均属于本轮新建来源页，没有覆盖入口已有文件。
- 本次续接检查：wiki_boundary_check.py exit 0；wiki_lint.py --fail-on error exit 0（errors=0、warnings=86、info=1208）；git diff --check exit 0；writeback anchors/locators validator exit 0（10 个固定标题、1 个机器块、29 items、0 错误）。本次追加 NUDAT132SN-4 并复验 machine locator。当前 warnings 分类为 CITATION_KEY_MISSING 80、REACTION_PARSE 3、ORPHAN_PAGE 2、RAW_GIT_CHANGE 1；均未触发 fail-on error。17 个公开 raw 快照哈希已复核，source-manifest 30行。run-02 仍 in-progress、未计数，state_file next_day_index=2。

- 写入前和 raw 源文件入库后 `wiki_boundary_check.py --root .` 均 exit `0`。`wiki_automation_preflight.py --root .` exit `0`，受保护 BibTeX 哈希匹配。11 个公开源快照经 SHA-256、PDF `%PDF` 签名、PDF 页数和目标数据行校验后从 `_incoming/20260928-day-02-02/` 晋升到 `raw/papers/gpt/day2-shell-gap-20260928/`；该目录保留本地且未暂存。
- `clean_knowledge_eol_dirty.py` exit `1`，原因是它按契约保留了 7 个有实质内容修改的 tracked knowledge 页；`refreshed=0`、`restored=0`、`unsafe/mixed=0`。它没有回滚任何研究内容。`knowledge/questions.md` 已按仓库 LF 约定归一化；最终 `git diff --check` exit `0`。
- 前一 checkpoint 的 Wiki lint 首次 exit 1，修正 source 模板后 exit 0（errors=0、warnings=86、info=1154）；该计数是先前阶段的历史记录。本次续接的最终检查另列于下方。
- 前一 checkpoint 的知识快照比较曾验证 16 个 writeback items；本次续接将唯一 writeback 区块更新为 25 items，并重新核验所有 anchors 与 atomic locators。
- continuation-prompt 先前列出 130Sn B(E2)、AME 协方差与 2003Ba01 等路线；本次根据新增的 133Sn/131Sn transfer 证据，已更新优先项为取得 Orlandi 2018 全文表格与误差，并禁止重复已失败端点。
- Git 发布由 Gitee `origin` 的 H3 gate 处理；仓库内以 `main` branch + commit subject 作为稳定指针，精确 hash 与 push outcome 由最终任务回执报告。`outputs/learning-milestones/2026-09-one-month-state.json` 只有在报告、writeback、lint 和 diff gate 均通过后才推进到 Day 3。
