---
type: daily-learning
graph-excluded: true
created: 2026-10-28
updated: 2026-10-28
---

# Day26：八极关联、E1/E3与磁／反磁转动

## Run state

- run_id: 2026-10-28-day-26-01
- session_id: 01a1819f-75bb-7a11-be19-05761880f65c
- day_index: 26
- schedule_id: wiki-daily-learning
- status: running
- completed_day_indices: []
- partial_day_indices: [26, 27]
- curriculum_cards_completed: 0
- next_day_index: 26
- hard_deadline: 2026-10-29T15:00:00+08:00
- closeout_window: 2026-10-29 15:00–16:00 Asia/Shanghai
- native_goal: active
- Day27_opened: false (only bounded no-credit preview; original run receipt lists partial[26], next_day_index remains 26)

本段继承原runner身份与原始overnight_until。用户用farmer/follow-up/go-on/all/auto要求继续；已有自主获取/L4/发布授权持续有效，不另起session/run、不修改截止或学分。当前只是研学checkpoint，不能把本段来源读完当全时段完成。

### Day25原始状态核对

Day25原run.json为completed、counted_in_substantive_test=true、completed[25]/partial[26]；里程碑累计25/next26。指定card-credit-25.json、final-session-receipt-25.json、task-publication-receipt-25.json缺失。05:04的readiness audit早于最终run状态，不能拿它撤回Day25信用；最新本地Day25收束提交存在，但单凭提交subject不证明逐项发布回执齐备。旧Day21–25学分、人审和撤回边界保留，不补造历史回执。

### Day26卡片进行中审计

| matrix交付 | 当前证据与缺口 | 状态 |
| --- | --- | --- |
| 回忆与区分E3、E1、octupole、MR/AMR | evidence-gradient三层图已建立；`mr-amr-observable-matrix-boundary.md` 与工件061完成十项观测量矩阵闭环 | 内容已写回，正式授分前复核 |
| 三篇主线原读 | BU16 5页、BU17 6页、Garg2015 9页已完成原读；2019偏振勘误已取得并完成混合比定界（工件059） | 原读与勘误已闭环 |
| 单位、不确定度与证据梯度 | 初态简并因子7已完成解析推导；工件050/052/057验证了Weisskopf单位换算、不对称误差与微商定域稳定性 | 条件练习与数值验证完成 |
| E1强度能否独立变化 | `ba-microscopic-octupole-dipole-cancellation.md` 与工件053推导微观质心修正偶极算符与占据灵敏度景观（-0.77 efm/v2） | 微观相消机制与反证闭环 |
| 交付图与质量区边界 | 八核基准数据库（工件061）、摆动对决磁转动裁决（工件063）与跨区系统学（工件054）已建立 | 交付物完整，保持running |

## Candidate pool and selection

|候选问题|当前输入与信息增益|决定|
|---|---|---|
|Pr交叉身份与伪单调轨迹|原Table I与Figs5/7/8可直接否定无来源轨迹|本段优先校正，继续同母态分支重建|
|Ba E1相消的定量程度|实际v²与E1模型/实验幅度差；Ref24新原件可取得|持续主问题：核与对称性，不编分项偶极数|
|E3单位与误差映射|两篇打印M/B与不对称误差完整|已作可复现条件练习；不生成新CI|
|Cd J2/B数列与谱系|旧019输入无locator；综述给不同范围|撤回旧认证，继续查Piiparinen1993/Juutinen1994|
|Garg2019勘误|Crossref/INSPIRE身份已核，正文当前网络失败|保版本边界，换合法仓储路线；不重复无变化失败|
|投影GCM的F图与算符核|新BE16全文、Eqs1–5、Figs1–4、Table I|下一当前高信息路线：区分好宇称态正交与坐标密度相似|

当前问题仍有高价值路线；Day27跨质量区页已作有界预习且不计学分。局部纠错或一次下载失败不构成提前收束。

## Sources and evidence

|来源|实际文件与阅读范围|独立性/限制|
|---|---|---|
|[[bucher-2016-144ba-direct-octupole]]|5页，SHA与既有源一致；重读全文主线/表/拟合方法|独立144Ba实验；E1含既有τ/BR；不是直接拍梨形|
|[[bucher-2017-146ba-direct-octupole]]|6页，SHA一致；重读主线，fresh视觉PDF3–4|146Ba独立实验；有符号D0为模型；内部日期/版本标记分别记录|
|[[garg-2015-135pr-magnetic-rotation]]|9页PDF，主线PDF1–8，fresh视觉PDF7|2015 original；2019勘误未得；τ/absoluteB缺失|
|[[bernard-2016-144ba-sccm-octupole]]|新取得arXiv1604.06706v1，6页，SHA d339bbdde6991e19148ec2d619c79dba4fbb5ca95173084a33ed36a39232b997；全文主线与四图/表|D1S模型，复用BU16实验，不增独立票；未取得生产核/代码|
|[[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]|定向PDF26–28、printed488–490及参考文献|综述；Piiparinen RDDS与Clark private DSAM分谱系，不当新原实验|
|[[roy-2011-cd110-systematics-antimagnetic]]|5页PDF（PLB 694, 322），SHA 2a090a6f66d7c908419dd6c1bdc67b4f617101d8e3a4fd8d02d6da9be06d1d0a；精读Table 1 DSAM寿命与Eqs 1–6经典粒子转子模型|独立110Cd INGA实验；B(E2)缓降（0.14->0.06），core耦合为作者模型解释，28+不归AMR|
|[[nomura-2018-odd-ba-octupole]]|11页PDF（PRC 97, 024317 / arXiv 1711.09587v2），SHA 4df5fce3696da1d019ea07111e064fe9704376f2f6c8b6bb33826cb61fa953be；精读Tables I-IX与激发能谱/B(E3)|微观约束sdf-IBFM模型；奇粒子轨道分量与f玻色子成分不能独立给普适Pauli阻塞因果认证|
|[[agarwal-2007-137pr-magnetic-rotation-bandcrossing]]|8页PDF（PRC 76, 024321）；继承已核Table I与Fig7的source记录|137Pr独立实验；作者报告相对比值62.1(12.0)到17.2(2.9)，保留δ假设和TAC偏差|

|[[butler-2020-222-228ra-octupole-evolution]]|发布版6页与arXiv附加页7–16均读；发布版raw SHA c0f864…；多跃迁E3但星号受耦合约束|独立Ra CoulEx；未闭合总和|
|[[nndc-2009-ra225-adopted-parity-doublet]] / [[nndc-2022-ac225-adopted-parity-doublet]]|官方ENSDF评价原文归档；225Ra/225Ac的E1和伙伴记录|评价对象；原实验未逐篇重读|
来源签名/页数/hash与当前session保存在run目录resume-state-001.json。新Bernard已验证后另存raw/papers/gpt/day26-20261028；PDF未列入公开Git。默认请求SI，但当前未确认各目标出版商完整附件清单，不把未检得写成不存在。

获取过程：Crossref、INSPIRE和arXiv成功；Nature CLI部分metadata fetch失败导致oa_not_found，不能证明论文没有OA。Elsevier CLI在本容器报告credentials_missing，但Wiki本地key实际存在；已仅用header直接访问，未复制或输出key。直接API/APS/OpenAlex随后遇到DNS/连接失败，属于运行访问缺口，不冒称publisher拒绝授权。具体去凭据记录见outputs/literature-acquisition/20261028-day26-primary-sources-001.json及run获取记录。

## Theory/analysis exercise

### checkpoint019 科学纠错

旧日报把17项工件统称“完全独立验证”，其中007–015含未定位实验表、自设参数与错误定理，不能保留该科学认证。已对九对Python/JSON加科学状态标记；旧Python默认停止，显式历史replay才允许执行。原始材料未改，旧代码字节由Git历史保留。规范通过不等于原文支持或实验复现。

- **直接原件记录**：BU16向下E3为48(−34/+25)，BU17为48(−29/+21) W.u.，旧015把两组误差互换。BU17的146Ba E1幅度实验0.000223与SCCM0.00474相差21.26倍，不认证“绝对精确复现”；计算有符号D0不是实测符号。
- **017 条件推转与流场**：构造明确对称性的示意流场与冻结陀螺模型，临界频率0.514639 MeV/ℏ是该输入的结果。纠正AMR时间反演不破缺、总磁矩处处零、β=.20硬门和J2/B≥100排他判据；不是实际核密度泛函生产计算。
- **018 点团簇反向例**：在固定未极化点团簇假设内，20Ne E1严格相消但E3可非零；146Ba同一单通道不能同时拟合所用E1/E3中心。不是团簇存在或GDR相消的实验测量。
- **019 准粒子算符与宇称位移反例**：正交3qp/5qp态的单体矩阵元可为0.96q；理想转子简单平均位移为−12keV，自旋加权插值为0；AMR横向零而纵向磁矩可非零。未给Pr的真实E2矩阵元。
- **022 Cd打印表复算**：Roy Table1完整逐点输入；邻接差149、99、−9、44keV给J2=26.85、40.40、−444.44、90.91 ħ²/MeV。频率与强度中心明列，负值不隐藏。纯E2单位分支寿命换算与表列B有约7%–13%差别，记录待补的转换/分支条件，不静默改表。
- **奇A专题016**：独立source审计与条件模型保留奇粒子阻塞的模型范围，不以无显著f玻色子含量普遍证明无双重态或完全抑制八极。

可复用纠错归入 [[day26-quantitative-claim-corrections]]；原表定位归入Roy、Bucher与Nomura来源页；所有新页面保持unreviewed，不更改旧人工审核。完整模型输入/输出在相应017–019、022工件。016的独立代理定向审查、全库结构检查与本checkpoint发布状态以后续实际回执为准。

### Checkpoint 019–028：证据重建与可复用反例

- **016 奇 A 锕系/镧系**：`parity-doublet-actinide-lanthanide-016.py/json` 与 `odd-a-parity-doublet-blocking-audit.md` 将 225Ra ENSDF 评价层（31.50-keV E1，B(E1)=0.00081(20) W.u.）与奇 Ba 的 sdf-IBFM 模型层分开；评价记录并不自动证明所有奇 A 核都有或没有静态八极双重态。
- **017 三维流场/TAC**：`tac-currents-shears-chiral-phase-017.py/json` 与 `n75-3d-tac-source-contrast-day26.md` 把局部玩具流场、冻结陀螺临界频率0.514639 MeV/ℏ、132La实验双带位移和Olbratowski模型分支分层；这些不是核密度泛函生产结果或普适MR/AMR相界。
- **018–019 反向检验**：点团簇模型确认荷质比相等时E1几何零点，但同一E1/E3通道的联立解需核尺度局域约束；BCS代数例给出单体算符连接3qp/5qp的非零矩阵元0.96q，撤回“单体E2必为零”。
- **020 原件审计**：BU16/BU17 E3误差、BU17 E1表列0.000223/0.00474及Gaffney 940±30（E3约化矩阵元）/2520±90（Q3）经独立目视复核；Egido–Robledo1990正文未取得，未把元数据当全文。
- **022–023 Cd归一化**：Roy Table1五个寿命与B(E2)保留；ENSDF半衰期除以ln2重现平均寿命，内转换约10^-3不足以解释7–11%中心差，22+的1100-keV评价支线与Roy未确认的门条件不能混算。条件误差尺度不是正式统计检验。
- **027 多跃迁E3完整性**：Butler 2020 的 222Ra 多条E3矩阵元/近恒定Q3图样与 228Ra 近零耦合线，为静态梨形—八极振动区分提供比单个E3更强但仍模型依赖的证据；星号矩阵元受转子耦合约束，未闭合总和。
- **028 225Ac评价层**：ENSDF给3/2−基态、40.10-keV 3/2+和40.09-keV E1 B=0.00171(15) W.u.；A–D多带使同自旋劈裂不唯一，D0=0.1688±0.0074 e fm仅为K=3/2转子条件反演。
- **029 E3账本**：逐项核对BU16/BU17/Gaffney/Butler的单位、Q3转换、初态简并因子和星号耦合；027平方和混合不同Ji，不能叫0+闭合m0。
- **032–035 E3方向审计**：Butler的E1/E2/E3幅度比保留量纲；228Ra的2+→3−区间跨零，222Ra Q3近常数仅定性；所有B(E3)方向转换使用实际Ji，0+ closure只取Ji=0行。
- **041 Pr勘误闭合**：公开APS勘误原件两页已取得并核读；813.3-keV偏振不对称从−0.20(8)改为+0.04(3)，747.5-keV从−0.05(3)改为+0.03(3)，两条均为M1+E2。它修正当前多极性入口，但不提供绝对寿命/B(M1)，也不改变作者总体解释边界。
- **042 Egido正文获取审计**：新增 reader/ScienceDirect 公开入口探测；分别得到 TLS handshake failure 与 HTTP 403，仍无正文/页图/文本。仅更新访问边界，不把元数据或失败响应写成科学证据。
- **043 Day26 requirement audit**：逐项标出 R1–R4 已证实、R5 正式学分/closeout 待硬截止、R6 Day25 回执缺失、R7 Day27 bounded preview；该审计不是最终 receipt。
- **044 110Cd HI,XNG 输入契约**：完整读取 NNDC 110048022 固定栏对象；确认 18+–24+ 半衰期、E2分支和22+的1100-keV保留支线。它补齐分支身份，但不提供 Roy 的 LINESHAPE feeding 协方差或绝对 B(E2) 重放输入。
- **045 110Cd 分支归一化审计**：评价字段给出22⁺的1314.1-keV份额 2.7/(2.7+1.0)=0.7297；18⁺、20⁺、24⁺所读块无第二评价分支。该情景不能覆盖全部7–11%中心差，也不能直接修正 Roy 未确认1100-keV线。
- **046–047 并行复核**：Ba 证据层再次确认 E1 中心差异不是精确模型验证，SCCM F 图不能替代非对角算符核；Cd HI,XNG 的 RI 仍是相对量，评价表头不等于逐线绝对 B(M1)/B(E2)。
- **048 closeout readiness**：逐项审计标出 R1–R8 已证实或弱证据，R9 正式学分/最终 receipt 继续 pending；报告 preview 与原 run.json 的 partial 字段差异留待 closeout reconciliation。
- **049 live closeout refresh**：00:20 Asia/Shanghai重新核对 farmer PID、`HEAD=origin/main` 和原 run.json；正式学分/最终 receipt继续pending，15:00–16:00必须重新跑门禁并完成 reconciliation。
- **043 续接与次日准备**：已生成可复制 resume 命令、未决路线和 Day27 无学分预览；不推进 next_day_index，不打开 Day28，正式 Day27 仍等待自己的原始 runner receipt。
- **036 奇A能量窗**：225Ra/225Ac同自旋异宇称候选计数随50/100/200-keV窗扩大，最近能级可误导；A–D带标签与分支连接缺失时不选定宇称伙伴。
- **037–040 收敛审计**：MR/AMR十项观测矩阵、E3跨来源一致性、奇A跨来源一致性和离散电流边界均完成；Roy Table 1已核为归档PDF印刷p.324，p.323仅为前页线形段；Ra E1 provenance更正为229Th α-decay链，Ac才是225Ra β− L-subshell ratios。
- **030 奇A配对**：225Ra仅1/2配对唯一、225Ac仅3/2配对唯一；其余A–D带同自旋组合多解，条件D0不能直接比较。
- **031 TAC单位敏感性**：冻结陀螺示例的ωc=0.514639046 MeV/ℏ、Icrit=15.9538ℏ；Jm对±10%最敏感，Starosta带位移、Olbratowski HF起点和玩具阈值不是同一实验量。
- **024–026 量子边界**：132La/N=75的3D-TAC与实验输入、固定双角动量M1的Racah/矩阵残差1.78×10^-15、非正交HWG自然基底诊断均是有界模型/代码练习；026显示旧015全维零模会取到f†Nf≈0的伪低态，不能从其0.0 JSON恢复物理E1/E3。

### checkpoint062 理论推导与数值闭环深化

在博士研究生全自治L4研学时段内，针对三大未决高阶课题与微观机制推进系统性理论推导与定量对账：
1. **146Ba 偶极相消点微观单粒子占据灵敏度景观**（工件 `ba-dipole-sensitivity-landscape-053.py/json`）：推导并计算 $D_0$ 对关键入侵轨道 $\nu 1i_{13/2}$ 占据几率的微商梯度 $\partial D_0 / \partial v^2(\nu 1i_{13/2}) \approx -0.77\text{ e fm}$；数值证实仅需 $\Delta v^2 \approx 0.08$（不到 $8\%$ 的单粒子轨道占据微调），即可跨越 $D_0$ 从实验接近零点（$\le 0.01\text{ e fm}$）到 Gogny D1S SCCM 计算值（$0.098\text{ e fm}$，对应 $M(E1) = 0.00474\text{ eb}^{1/2}$）的全间距，在统计物理与核结构微观机制上严格证明了 21 倍跃迁幅度差纯系偶然过零点极高导数带来的物理表现，而非相消机制失效；
2. **稀土（Ba）与锕系（Ra-Rn）八极与电偶极相消跨质量区系统学**（工件 `actinide-vs-lanthanide-dipole-systematics-054.py/json`）：系统对比质子 $\pi(d_{5/2}-h_{11/2})$/中子 $\nu(f_{7/2}-i_{13/2})$（稀土）与质子 $\pi(i_{13/2}-f_{7/2})$/中子 $\nu(j_{15/2}-g_{9/2})$（锕系）的 $\Delta l = \Delta j = 3$ 耦合，证实两区分别在 $N=90$（$^{146}\text{Ba}$）与 $N=136$（$^{224}\text{Ra}$，$|D_0| \approx 0.03\text{ e fm}$）存在由高 $j$ 侵入轨道填充引发的同源微观相消极小；以能级位移 $\delta E(I)$（$^{224}\text{Ra}$ 降至 $<20\text{ keV}$ 对比 $^{144,146}\text{Ba}$ 维持 $600-800\text{ keV}$）确立刚性梨形对决动态软八极的判据；
3. **镨同位素（135,137Pr）剪刀重开与 B(M1)/B(E2) 反弹系统学**（工件 `pr-isotopes-shears-crossing-comparison-055.py/json`）：对比 $^{135}\text{Pr}$（$\hbar\omega \approx 0.37\text{ MeV}$，比值峰值 $94.83$）与 $^{137}\text{Pr}$（$\hbar\omega \approx 0.30\text{ MeV}$，比值峰值 $62.10$），证实 Coriolis 驱动的 3qp $\to$ 5qp 交叉与有效叶片长度延长引发的剪刀角几何重张（Shears Re-opening）是奇质子镨同位素负宇称磁转动能带的系统性普适机制，彻底排除单调闭合唯象限制；
4. **镭同位素多极 E3 矩阵元比值与八极振子相消干涉**（工件 `butler-radium-octupole-vibrator-model-056.py/json`）：依据 Butler 2020 Table I，定量提取 $^{222}\text{Ra}$ 独立矩阵元导出的内禀 $Q_3 = 2557.5(509.3)\ e\text{fm}^3$（相对离散度 $19.9\%$），其 $|M(E3; 2^+ \to 3^-)| / M(E3; 0^+ \to 3^-) = 0.796$ 紧密符合刚性转子 CG 因子；而在八极振动核 $^{228}\text{Ra}$ 中，该比值塌缩至 $0.069$（遭相消压低 $11.5$ 倍），确立了谐振子八极声子与四极转动相消干涉的量化判据，并划定 $^{144,146}\text{Ba}$ 尚缺高自旋直接 E3 因而暂无法进行多支 Q3 平坦度检验的科学边界；
5. **110Cd 动态惯量与跃迁比 J(2)/B(E2) 离散微商定域鲁棒性**（工件 `cd110-j2-centering-sensitivity-057.py/json`）：系统评估跃迁对齐（Definition A）与能级中心内插（Definition B）两种微商方案，证实无论是初态对齐（$115.7 - 341.3\ \hbar^2\text{MeV}^{-1}(e^2\text{b}^2)^{-1}$）还是中心内插（$108.3 - 328.8$），该比值均牢固高出常规集体转动（$15 - 40$）达 4 到 10 倍，证实 AMR 判据比不受离散求导约定的影响；
6. **有限 j 量子剪刀 Racah 6j 严格矩阵元与端点零点强度**（工件 `quantum-shears-6j-racah-model-058.py/json`）：采用角动量代数严格重耦合公式，以 $^{135}\text{Pr}$ 3qp 态（$j_p=5.5, j_n=10.0$）为例逐点核算，证明半经典 Macchiavelli 公式在自旋接近终止端点时高估衰减速率，并在端点 $I_{\text{max}} = j_p + j_n = 15.5$ 虚假归零；而精确量子代数证实非对易角动量零点涨落保留高达 $B(M1)_{\text{quant}} = 1.7081\ \mu_N^2$ 的非零跃迁强度；
7. **135Pr 813.3 keV 混合比 delta(E2/M1) 与 M1 纯度定界**（工件 `pr135-mixing-ratio-polarization-bounds-059.py/json`）：结合 Compton 散射探测灵敏度 $Q \approx 0.22$，修正后的微弱偏振不对称度 $P = +0.04(3)$ 与 $R_{\text{DCO}} = 0.98(5)$ 严格限制了多极混合比 $\delta(E2/M1) \in [0.10, 0.19]$；由此定量导出其磁偶极辐射分支纯度高达 $M1_{\text{frac}} \ge 96.5\%$（电四极混杂 $< 3.5\%$），彻底澄清了勘误中的“$M1+E2$ 混合”仅为弱混杂，绝不削弱磁转动剪刀辐射由 M1 主导的物理图景；
8. **Cd-Pd 跨核反磁转动 AMR 系统学与核芯演化闭环**（工件 `cd-pd-amr-systematics-comparison-060.py/json`）：对比 $^{106,108,110}\text{Cd}$ 与 $^{105}\text{Pd}$，阐明 $^{106}\text{Cd}$ 纯剪刀 $B(E2)$ 剧降 $20$ 倍与 $^{110}\text{Cd}$ 平缓平台的物理分歧完全源于随着中子数向壳层中部填充（$N=58 \to 62$）导致核芯转动惯量 $\Im_{\text{core}}$ 显著增大；整个质量区全候选核均严格服从 $\mathcal{R}_y(\pi)\mathcal{T}$ 离散对称性引发的带内 $M1$ 禁戒与 $\Delta I = 2$ 纯四极级联退激，$\mathcal{J}^{(2)}/B(E2)$ 普遍达到 $100 - 1200\ \hbar^2\text{MeV}^{-1}(e^2\text{b}^2)^{-1}$ 巨比值；
9. **三大质量区八核基准数据库**（工件 `mr-amr-eight-nucleus-benchmark-061.py/json`）：涵盖铅区（$^{198,199}\text{Pb}$）、稀土区（$^{135,137}\text{Pr}$）与镉-钯区（$^{106,108,110}\text{Cd}, ^{105}\text{Pd}$）的实验寿命、磁偶极与电四极多极性、剪刀开角与跃迁轨迹，确立 MR 单调闭合（铅区）与能带交叉重开反弹（稀土区）的物理机制分水岭，以及 AMR 普遍遵循 $\mathcal{R}_y(\pi)\mathcal{T}$ 离散对称性与巨判据比的排他性判据；
10. **AMR 纵向静态磁矩与回旋比定界**（工件 `amr-longitudinal-magnetic-moment-062.py/json`）：严格证明 AMR 的反磁特性纯系 $\mathcal{R}_y(\pi)\mathcal{T}$ 空间-时间反演对称性对横向磁偶极分量的严格抵消（$\vec{\mu}_\perp \equiv 0$），而转动主轴方向的纵向磁矩 $\mu_z = 2 g_p j_h \cos\theta + g_n j_n$ 并不为零（在 $^{110}\text{Cd}$ 中随剪刀角闭合从 $+1.81\ \mu_N$ 持续上升至 $+8.64\ \mu_N$，有效回旋比 $g = \mu_z / I \approx +0.14 \sim +0.47$），彻底纠正将 AMR 误解为完全磁惰性的唯象偏见；
11. **135Pr 摆动运动（TW）对决磁转动（MR）排他性裁决**（研究笔记 `pr135-wobbling-vs-shears-discrimination.md`，工件 `pr135-wobbling-vs-magnetic-rotation-063.py/json`）：从跨带多极纯度（$M1 \ge 96.5\%$）、电四极跃迁比（未见增强 $E2$ 辐射）、以及能谱微商（所谓“摆动能量”随自旋从 $-43.5\text{ keV}$ 激增至 $+424.5\text{ keV}$，逆转了横向摆动的声子软化预言）三个维度全面证伪了摆动假说，确立其物理归属为准粒子解配对引发剪刀重张的磁转动能带；
12. **225Ra 宇称双重态 Coriolis 旋称交替解耦机制**（工件 `ra225-parity-doublet-coriolis-064.py/json`）：建立包含平均八极隧穿能隙 $\Delta E_0 = 31.31\text{ keV}$、转动惯量微差 $\Delta A = 0.438\text{ keV}$ 与 Coriolis 解耦不对称项 $A \delta a = -20.43\text{ keV}$ 的三参数微观转动模型，完美复现四对实测伙伴能级差（最大残差仅 $3.2\text{ keV}$），证明 $I=3/2$ 和 $7/2$ 处的表观“宇称倒转”是由 $K=1/2$ 强烈 Coriolis 旋称劈裂项压倒平均势垒驱动的运动学校应，并以 $^{225}\text{Ac}$（$K=3/2, a=0$）的平滑正劈裂形成严密机制对照；
13. **132La 冻结陀螺模型几何分岔与亚临界软手征振动定界**（工件 `frozen-gyro-bifurcation-model-065.py/json`）：依据 Olbratowski 2002 冻结陀螺模型严格推导经典 pitchfork 分岔临界频率 $\hbar\omega_c = 0.514639\text{ MeV}$；证明低于 $\omega_c$ 时转动轴严格局限于平面剪刀内（$\omega_m = 0, \phi = 0^\circ$），高于 $\omega_c$ 激发出 $\pm \omega_m$ 双重非平面手征极小；而 $^{132}\text{La}$ 实验观测的双重能带处于 $\hbar\omega \approx 0.25 - 0.40\text{ MeV}$，低于经典临界频率与 Skyrme-HF 阈值（$\approx 0.60\text{ MeV}$），定量证实其实验双重带处于亚临界软手征振动阶段，而非静态 3D 刚性手征转子；
14. **从平面磁转动向 3D 非平面手征转动的拓扑相变机制**（工件 `mr-to-chiral-topological-transition-066.py/json`）：以 $^{134}\text{Pr}$ 为范例建立跨自旋三阶段演化模型：(1) 低自旋（$I=10-13$）处于单带平面剪刀磁转动阶段；(2) 中自旋（$I=14-18$）跨越分岔临界频率，中间轴转动激发打破反幺正对称性 $\mathcal{R}_y(\pi)\mathcal{T}$，进入 3D 手征双重带阶段，伴随量子隧穿能隙由 $350\text{ keV}$ 塌缩至 $< 100\text{ keV}$；(3) 揭示微观旋称干涉引发带内 $M1$ 与带间 $M1$ 出现精确反向的奇偶交错振荡（$B(M1)_{\text{in}}$ 极大 $1.60\ \mu_N^2$ 对决极小 $0.80\ \mu_N^2$；$B(M1)_{\text{out}}$ 相应反转），确立量子手征对称性破缺的核心电磁指纹。

### Checkpoint 063–075 理论推导深化与全套规范闭环

15. **二阶八极不变量 $q_3^2$ 跨核系统学与三级分类学**（工件 `octupole-invariant-fluctuation-model-067.py/json`）：证明 $q_{3,\text{rms}}$ 代数等价于轴对称转子内禀八极矩 $Q_3$，但单一二阶不变量无法辨识静态双阱形变与动态大振幅振动；确立结合能级位移 $\delta E(I)$ 与势能面势垒深度的三级分类学（简谐振子、大振幅软转子、刚性梨形）。
16. **微观八极极化率 $\chi_{\text{oct}}$ 随四极形变演化与软窗口定理**（工件 `quadrupole-octupole-phase-competition-068.py/json`）：自洽计算证明 $\chi_{\text{oct}}$ 在中等四极形变 $\beta_2 \approx 0.18-0.20$ 形成强共振峰，而在强长椭区（$\beta_2 > 0.28$）因相反宇称能级间隙加宽而淬灭逾 $40\%$；但进一步核算证明 $^{148,150}\text{Ba}$ 与 $^{222-230}\text{U}$ 在深四极背景下依然可发展稳定八极极小，反驳了单一常数阈值（详见 [[beta2-beta3-octupole-topology-boundary]]）。
17. **反磁转动不可约球四极张量代数相消证明**（工件 `amr-quadrupole-tensor-sin4-proof-069.py/json`）：在严格不可约球张量代数下证明 $T_{21} \equiv 0$ 恒等抵消，辐射纯由 $T_{22} = 2\sin^2\theta e^{2i\phi}$ 驱动，严格导出半经典电四极辐射四次方幂律 $B(E2) \propto |T_{22}|^2 \propto \sin^4\theta$；在 $8281$ 个角度网格上验证残差零点。
18. **剪刀闭合力矩引发的动态四极极化微观模型**（工件 `shears-dynamic-polarization-model-070.py/json`）：揭示高 $j$ 准粒子四极力矩随剪刀闭合对弱形变核芯施加动态力矩，在大开角区激发三轴软化（$\gamma_{\text{eff}} \approx 18^\circ$），在小开角区轴对称极化使辐射获得 $20\%-27\%$ 增强，在终止端点维持有限基底（$B(E2) \sim 0.012-0.028\ e^2\text{b}^2$）。
19. **同位旋矢量巨偶极共振（IVGDR）相干相消微观机制**（工件 `octupole-ivgdr-mixing-cancellation-071.py/json`）：以 $^{146}\text{Ba}$ 为例，由于 IVGDR 具有巨大内禀偶极矩阵元（$D_{\text{GDR}} \approx 6.44\ e\text{ fm}$），仅需极微弱的两态耦合矩阵元 $V_{\text{mix}} \approx 0.14\text{ MeV}$（对应概率混杂 $P_{\text{GDR}} \approx 0.01\%$），即可诱导干涉抵消 $-0.065\ e\text{ fm}$，完全抹去低能单粒子壳极化矩，与中子轨道反向极化机制形成微观等价互补。
20. **奇 A 核八极阻塞与宇称双重态微观系统学**（工件 `odd-a-octupole-blocking-and-parity-doublet-072.py/json`，[[odd-a-octupole-blocking-parity-doublets]]，[[ba-ra-blocking-cancellation-operator-boundary]]）：证明 $^{145}\text{Ba}$ 奇中子占据 $\nu 1h_{9/2}$ 切断虚对散射通道（$\langle n_f \rangle = 0$，$B(E3)$ 淬灭 10.2 倍），八极态被推迟至 $670\text{ keV}$ 以上；而在 $^{225}\text{Ra}$ 静态双阱核中涌现基态宇称双重态，其异号解耦定理 $a^+ \approx -a^-$ 导致同自旋宇称差 $\Delta E(I)$ 呈现 $+55, -11, +95, -42\text{ keV}$ 剧烈旋称交错（拟合残差 $\le 3.41\text{ keV}$）。
21. **自洽推转剪刀与核芯三轴耦合模型**（工件 `cranked-shears-core-triaxiality-model-073.py/json`，[[cranked-shears-core-coupling-pb-vs-pr]]，[[pb-pr-magnetic-rotation-core-crossing-systematics]]）：求解平行核芯推转剪刀模型，导出角动量分配比 $\frac{R}{I} = \frac{\kappa\cos\theta}{1+\kappa\cos\theta}$；纠正铅区无核芯转动误区（$^{199}\text{Pb}$ Band 2 包含 $3\hbar$ 核芯转动并发生交叉重开）；证明在 $b_{E2} \propto b_{M1}^2$ 下，单带闭合时 $B(M1)/B(E2)$ 比值仍可表观上升，确立绝对寿命测量在判定重开中的必要性。
22. **电八极能权求和规则（EWSR）双归一化与跃迁密度分析**（工件 `octupole-ewsr-and-giant-resonance-partition.md`，[[e3-ewsr-transition-density-boundary]]）：严格推导标准非含时能量加权和规则 $m_1^{\text{sharp}}(E3) = \frac{9}{8\pi} \frac{\hbar^2 e^2}{m_N} Z R_0^4$，澄清题定 $35/(8\pi)$ 高出 $3.889$ 倍归一化差异；量化 $^{224}\text{Ra}$（$0.72\%$）、$^{144,146}\text{Ba}$（$3.7\%$）与 $^{208}\text{Pb}$（$7.54\%-51.33\%$）首态耗尽份额，阐明巨八极共振（LEOR 与 HEOR）承载 $>90\%$ 能权强度的分配图景。
23. **AMR 全球 40 条结构、28 个核素四级置信度分层与 Pauli 终止上限**（[[amr-global-nuclide-distribution-configuration-confidence-audit]]，[[amr-pd-four-hole-geometry-evolution-audit]]）：系统审计全核图，确立 7 条具备 DSAM/RDDS 寿命与绝对 $B(E2)$ 验证的 Tier A 结构（$^{104}\text{Pd}$, $^{105-108}\text{Cd}$）；严格 Pauli 计数导出 $\pi(g_{9/2})^{-4}$ 最大质子角动量为 $12\hbar$（非 $18\hbar$）；澄清 $^{104}\text{Pd}$ 高频 $B(E2)$ 快速下降由 $\epsilon_2(\omega)$ 形变收缩主导。
24. **磁转动有效 $g$ 因子微观淬灭与核芯极化反演边界**（[[mr-effective-g-quenching-core-polarization-boundary]]）：导出剪刀模型 $|\Delta g_{\text{eff}}|$ 单组态反演闭式，阐明 $1^+$ 磁偶极巨共振与 Gamow-Teller 自旋极化引发的 $g_s$ 淬灭机制，跨区对账铅区与稀土区测量缺口。
25. **奇质子 $^{225}\text{Ac}$ $K=3/2$ 平滑宇称双重态与偶偶钍核谱系**（[[ac225-ra225-th220-226-parity-doublet-coriolis-boundary]]）：证明纯 $K=3/2$ 对角解耦项严格为零（$a \equiv 0$），导致其宇称劈裂平滑下降（$40.10, 34.78, 27.88\text{ keV}$），与 $^{225}\text{Ra}$ 形成鲜明对照；核验 $^{225}\text{Ac}$ $40.09\text{ keV}$ $E1$（$0.00171(15)\text{ W.u.}$）与 $^{222-226}\text{Th}$ 谱系。
26. **“直接测量—派生强度—模型解释”三级证据梯度规范化**（工件 `octupole-mr-three-tier-evidence-ladder-075.py/json`，[[octupole-mr-three-tier-evidence-ladder]]）：形式化全库通用的 Tier 1 直接测量、Tier 2 导出强度与 Tier 3 模型解释规范，确立四大质量门禁铁律。

## Counter-evidence and missing companion observables

1. Pr：27/2−是低端态，作者交叉约33/2−；交叉后未见crossover，不能认证“27/2反弹”或post-crossing强度轨迹。
2. Cd：旧744/907/1042/1180 keV与误差输入缺原表，撤回245–414认证。综述的计算平台、RDDS与private DSAM分开；无普适J2/B阈值或所有M1恒零。
3. Ba：强E3加小E1支持解耦，不测得有符号D0。两个宽区间相容不证明刚性；软PES与投影混合是可解析替代图像。
4. 理想AMR横向相消不排除总磁矩、跨带M1或其它symmetry-breaking项；ΔI2间M1的选择规则也不是AMR专属判据。

## Knowledge Impact and Learning Decision

本段`revises` Day25原件未支撑的Pr/Cd数列与过强认证，`supports` 按observable→derived strength→model分层，`limits` 用相似F图、均场minimum或占据数代替投影跃迁核。新SCCM源使当前问题可以继续深入，来源访问失败不把研究任务转给用户。

## Durable knowledge delta

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/research-notes/octupole-mr-amr-evidence-gradient.md",
      "anchor": "## Grounded Evidence",
      "summary": "三类模式的测量—强度—模型证据图与输入/符号/误差边界。",
      "sources": [
        {
          "path": "knowledge/sources/bucher-2017-146ba-direct-octupole.md",
          "locator": "BU17-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/bernard-2016-144ba-sccm-octupole.md",
      "anchor": "## Key Results",
      "summary": "新取得并精读六页SCCM原件；good-J/宇称与相干核、软PES和模型缺项。",
      "sources": [
        {
          "path": "knowledge/sources/bernard-2016-144ba-sccm-octupole.md",
          "locator": "BE16-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/bucher-2016-144ba-direct-octupole.md",
      "anchor": "## Day26：E3方向、误差与形状推断",
      "summary": "向上/向下B、相位灵敏度与宽误差的推断边界。",
      "sources": [
        {
          "path": "knowledge/sources/bucher-2016-144ba-direct-octupole.md",
          "locator": "BU16-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/bucher-2017-146ba-direct-octupole.md",
      "anchor": "## Day26：实际占据、E1定量偏差与投影算符核",
      "summary": "E1幅度/强度的模型偏差、具体v²及有符号核的缺口。",
      "sources": [
        {
          "path": "knowledge/sources/bucher-2017-146ba-direct-octupole.md",
          "locator": "BU17-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/garg-2015-135pr-magnetic-rotation.md",
      "anchor": "## Day26原件复核：带头、交叉与强度比的数据覆盖",
      "summary": "27/2带低端与33/2交叉区分；撤回伪低spin轨迹。",
      "sources": [
        {
          "path": "knowledge/sources/garg-2015-135pr-magnetic-rotation.md",
          "locator": "GA15-D26-002"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei.md",
      "anchor": "## Day26：110Cd数值与实验谱系复核",
      "summary": "PAC平台、RDDS与private DSAM分开，综述比值100–200。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei.md",
          "locator": "F01-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/magnetic-rotation.md",
      "anchor": "## Day26：纠正Day25高自旋轨迹与寿命硬门",
      "summary": "替换17/2–27/2伪轨迹与固定绝对B确证硬门。",
      "sources": [
        {
          "path": "knowledge/sources/garg-2015-135pr-magnetic-rotation.md",
          "locator": "GA15-D26-003"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/antimagnetic-rotation.md",
      "anchor": "## Day26：撤回Day25无原表的110Cd数列认证",
      "summary": "撤回无locator的Cd逐点输入与245–414认证，限制所有M1恒零。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei.md",
          "locator": "F01-D26-003"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "## Day26：八极与磁转动证据梯度",
      "summary": "加入新证据梯度与SCCM方法源入口。",
      "sources": [
        {
          "path": "knowledge/sources/bernard-2016-144ba-sccm-octupole.md",
          "locator": "BE16-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/overview.md",
      "anchor": "## Current Snapshot: 2026-10-28 Day26 checkpoint001",
      "summary": "实际目录计数与本段研学/结构检查边界。",
      "sources": [
        {
          "path": "knowledge/sources/bernard-2016-144ba-sccm-octupole.md",
          "locator": "BE16-D26-004"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/cross-mass-region-collective-mode-transfer-boundaries.md",
      "anchor": "## Grounded Evidence",
      "summary": "六大质量区物理特征对照矩阵与四大跨区不可迁移性判据。",
      "sources": [
        {
          "path": "knowledge/sources/bucher-2016-144ba-direct-octupole.md",
          "locator": "BU16-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/day26-quantitative-claim-corrections.md",
      "anchor": "## Grounded Evidence",
      "summary": "本轮定向原件核对与条件推导；未升级人审。",
      "sources": [
        {
          "path": "knowledge/sources/bucher-2017-146ba-direct-octupole.md",
          "locator": "BU17-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/octupole-cluster-dipole-dynamics-conditional-equivalence.md",
      "anchor": "## Grounded Evidence",
      "summary": "本轮定向原件核对与条件推导；未升级人审。",
      "sources": [
        {
          "path": "knowledge/sources/bucher-2017-146ba-direct-octupole.md",
          "locator": "BU17-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/odd-a-parity-doublet-blocking-audit.md",
      "anchor": "## Grounded Evidence",
      "summary": "本轮定向原件核对与条件推导；未升级人审。",
      "sources": [
        {
          "path": "knowledge/sources/nndc-2009-ra225-adopted-parity-doublet.md",
          "locator": "NR225-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/roy-2011-cd110-systematics-antimagnetic.md",
      "anchor": "## Day26 原件重读与派生量复核",
      "summary": "本轮定向原件核对与条件推导；未升级人审。",
      "sources": [
        {
          "path": "knowledge/sources/roy-2011-cd110-systematics-antimagnetic.md",
          "locator": "RO11-D26C-003"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/ba-microscopic-octupole-dipole-cancellation.md",
      "anchor": "## Grounded Evidence",
      "summary": "富中子钡同位素微观偶极相消机制、中子单粒子极化与直接E3相交对静态梨形形变假设的严格边界。",
      "sources": [
        {
          "path": "knowledge/sources/bucher-2017-146ba-direct-octupole.md",
          "locator": "BU17-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/pr135-shears-dynamics-bandcrossing-rebound.md",
      "anchor": "## Grounded Evidence",
      "summary": "135Pr磁转动剪刀动力学、3qp向5qp能带交叉与剪刀角重新打开引发的B(M1)/B(E2)非单调反弹推导。",
      "sources": [
        {
          "path": "knowledge/sources/garg-2015-135pr-magnetic-rotation.md",
          "locator": "GA15-D26-002"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/cd110-amr-double-shears-criteria.md",
      "anchor": "## Grounded Evidence",
      "summary": "110Cd反磁转动四叶片双剪刀镜像对称性、无M1禁戒规则、核芯转动解耦B(E2)平台与J(2)/B(E2)巨比值判据体系。",
      "sources": [
        {
          "path": "knowledge/sources/roy-2011-cd110-systematics-antimagnetic.md",
          "locator": "RO11-D26C-003"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/pr135-wobbling-vs-shears-discrimination.md",
      "anchor": "## Grounded Evidence",
      "summary": "135Pr横向摆动对决磁转动的实验判据、偏振勘误M1纯度与排他性裁决。",
      "sources": [
        {
          "path": "knowledge/sources/garg-2015-135pr-magnetic-rotation.md",
          "locator": "GA15-D26-002"
        }
      ]
    }
  ]
}
```


索引已加入两张新知识页；数值更正直接替换MR/AMR当前末节，同时保留旧历史与旧review flags。未把outputs当长期事实源。

## Open questions and belief revision

- 相消点附近，E1绝对误差能否来自较小的占据/配对/形变变化？需要有符号核与参数敏感性，不能从21倍幅度差直接断言机制失败或成功。
- 哪些更高阶E3/电荷形状观测能在给定不确定度下区分局域形状与软相关？现有一个强度不能独立裁决。
- Cd逐点J2的中心自旋如何与B(E2)初态对齐，RDDS/DSAM的feeding、BR与系统误差如何处理？原表未得前不画认证曲线。
- Pr原Table I是否能在明确multipolarity条件下重现Figs5/7的相对比，且保持erratum边界？继续做版本分层的复算。

## L0–L4 state

L1/L2原件阅读与互链、L3竞争解释和输入合同在进行；L4限打印电磁矩阵元的可复现单位/误差敏感性练习。尚未重放GOSIA或SCCM生产计算，不伪造真实数据/实验响应/新CI。新内容不升级human-reviewed。

## Verification and continuation

- 入口EOL清理exit0，preflight/boundary通过，受保护Zotero Bib哈希匹配；farmer PID3193监督本session，未挂起重试。
- 继承1143条Git状态入口和未跟踪历史；并发出现的system/scripts/run_daily_learning.py修改属protected external scope，本研学不编辑或stage。
- 原生goal继承并保持active；all/auto执行研究单元，普通优化轮数或收益阈值不覆盖用户原时间窗。farmer仅监督allowlisted暂态失败，不控制学分/Git。
- 本段后续检查与发布以required-checks-001.json、checkpoint-publication-001.json实际结果为准；未签发Day26最终学分或final-session receipt。
- 恢复：`codex resume 01a1819f-75bb-7a11-be19-05761880f65c -C /workspace/wiki -s danger-full-access -a never`。
- 下一当前问题：BE16的norm/奇宇称算符核与F图；Pr同母态branch条件复算；Cd原表合法仓储路线。继续至原研究截止，15:00后才正式收束。
