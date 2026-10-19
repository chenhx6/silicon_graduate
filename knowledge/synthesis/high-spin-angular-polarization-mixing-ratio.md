---
type: synthesis
title: "High-spin angular distributions, polarization and mixing-ratio evidence"
aliases: [高自旋角分布偏振混合比证据综合]
created: 2026-09-21
updated: 2026-10-19
status: ai-draft
review_status: unreviewed
scope: high-spin-angular-polarization-mixing-ratio
confidence: medium
sources: [yamazaki-1967-aligned-angular-coefficients, suffert-1959-proton-capture-polarization, lange-kumar-hamilton-1982-multipole-admixtures, droste-1996-pdco-formalism, starosta-1999-pdco-experimental-test]
tags: [high-spin, angular-distribution, polarization, mixing-ratio, evidence-map]
---

# High-spin angular distributions, polarization and mixing-ratio evidence


## Agent active summary

Day16把DCO/δ判断落实为同一个跃迁、门、相位、取向、响应和联合误差对象。178W实际双候选与本run条件反演分层；两条件根的偏振同号，符号不足以选根。Rh99实际AD/P在允许任意非负对称布居的模型域内仍有两种EM族条件解，独立取向条件才改变可识别性。199Tl的粗网格漏解及完整混合比域的偏振重叠，又限制了局部扫描和固定点companion的排除能力。

保号的完整未观测feeding、指定布居prior、已测reference是三个层次。历史相位/轴/计数合同和本日软件组件核验均保留各自范围；正确Stokes与能量守恒不认证真实detector response。新增内容都是Codex self-audit或条件模型，没有新实验δ/Jπ、人审状态或正式Day17学分。快速复用见本页“Day16末段整合：哪些输入真正改变候选”。

## Question and Scope

This synthesis compares the method and application sources in the high-spin batch. It is a method map, not a universal calibration table.

## Evidence Matrix

| Layer | What the sources establish | Main boundary |
|---|---|---|
| Formalism | Yamazaki, Rose–Brink, Taras, Hamilton and Lange define statistical tensors, angular coefficients, polarization terms and δ conventions. | Operator phase, state order and emission/absorption convention must be mapped. |
| Population | Gaussian `σ/J`, attenuation coefficients and cascade `U_k` connect alignment to `A2/A4`. | Alignment and side feeding are reaction dependent. |
| Detector | GeLi, CLOVER, Gammasphere, SeGA, BGO and AFRODITE sources calibrate `P/A/Q`, `Q(E)`, efficiency and finite geometry. | Numerical `Q`, `R_ADO` and `R_DCO` are setup specific. |
| Assignment | DCO/ADO, angular distributions and linear polarization can jointly constrain spin, parity and multipole branch. | A single observable commonly retains multiple branches. |

## Synthesis

1. The reliable unit is a joint fit of transition identity, alignment, detector response, angular distribution, polarization and convention. A quoted δ without this context is not portable.
2. Polarization adds electric/magnetic sensitivity, while angular distributions and DCO primarily constrain angular momentum and multipole combinations. Their information is complementary, not interchangeable.
3. The strongest historical sources expose failure modes: unresolved cascades, background subtraction, finite solid angle, Gaussian alignment assumptions and sign conversion.
4. Modern sources add better detectors and simulations but retain the same logical dependencies. Better resolution narrows uncertainty; it does not remove model identifiability limits.

## Model Dependence

Alignment distributions, attenuation coefficients, detector response and phase conventions are source and setup dependent. Review tables provide transfer rules but do not replace a matched calibration.

## Counter-evidence

Unresolved cascades, finite solid angle, background and multiple δ branches can produce apparently consistent but non-identifying fits.

## Open L3 questions

- Under what covariance conditions can `A2/A4`, polarization and DCO identify δ uniquely?
- Which detector response quantities must be remeasured when transferring a calibration between arrays?
- Can a common likelihood express alignment, feeding, response and branch uncertainty without treating `σ/J` as a universal prior?

## Limitations and Missing Evidence

- `needs_review: true` remains on numerical claims intended for paper-level reuse.
- Review tables are provenance maps, not independent experiments.
- No L4 re-fit is claimed because raw response matrices and complete analysis code are generally unavailable.

## Sources

- [[yamazaki-1967-aligned-angular-coefficients]], [[rose-brink-1967-phase-defined-angular-distributions]], [[taras-1971-phase-defined-polarization-formulas]], [[hamilton-1948-successive-quanta-polarization]]
- [[suffert-1959-proton-capture-polarization]], [[lange-kumar-hamilton-1982-multipole-admixtures]]
- [[droste-1996-pdco-formalism]], [[starosta-1999-pdco-experimental-test]], [[droste-1999-ppco-polarization]]
- [[simpson-1983-sectored-geli-compton-polarimeter]], [[jones-1995-clover-compton-calibration]], [[schmid-1998-gammasphere-polarization]], [[miller-2007-sega-polarization]]

## Self-audit

- Evidence is separated into formalism, population model, detector response and nuclear assignment.
- Historical conventions are not silently converted; each source retains its own sign and state-order locator.
- This synthesis is a Codex self-audit and remains unreviewed.


## Day16 REFLECT：从同符号到同一个observable

| 必要对象 | 这轮原件能够闭合的内容 | 仍不能据此推出 |
| --- | --- | --- |
| 辐射振幅δ | [[krane-steffen-1970-cd110-mixing-ratios]]与[[droste-1996-pdco-formalism]]有本run已核的operator/state-order桥 | FH59δ/SU59x只因都是amplitude ratio就自动同KS/RB号；其上游原件仍缺 |
| electric-axis P | [[suffert-1959-proton-capture-polarization]] SEH59-4与[[fagg-hanna-1959-polarization-measurements]] FH59-5给P_SU=−P_plane | 这个坐标重写是新的物理解，或能认证B15 actualproducer |
| 计数与响应 | FH59-8/9的p/R/r三层给A=QP，circular R另含2；[[bizzeti-2015-agata-triple-cluster-polarimetry]] B15-7/16区分fit与endpoint符号 | 同字母R/Q/As或数值近似即同零点/同分析核 |
| 布居与权重 | B15-2的event-P不同于center-P；FH59-12同E3不同Ep/reference仍不同P | 同能量/EM便能跨selection给定P或直接迁移Q |
| companion与多解 | SEH59-9/10同25Al线在另一AD下仍两解；FH59-14/15保留未分辨cascade与外部赋值条件 | 添加偏振必唯一选根，或把不同AD对象合并为四根数据 |
| 证据独立性 | FH59-14的review原图/表是同Me50数据的复述，B15 modelgrid也非独立实验 | 用同一采集的多种处理/多篇转述增加实验票数 |

因此可复用单元应保存transition identity、source/gate/reference方向、δ完整phase、P轴和counterroles、response/averaging、误差与共有Cov。若其中一个对象未对齐，结果只能作为有条件候选；直接改P或δ的号不能补齐缺失响应。这个判断由已读原件及具体反例支持，不把review表中的数对冲突或模型purelimit当作新实验裁决。

已核源：[[suffert-1959-proton-capture-polarization]] SEH59-4/9/10；[[fagg-hanna-1959-polarization-measurements]] FH59-5/8/9/12/14/15；[[bizzeti-2015-agata-triple-cluster-polarimetry]] B15-2/7/16。仍未得BR1953/Fe55、Me50原producer和联合Cov；新FH59转述不替primary实验。


### Day16 self-audit triage

P0：本批未识别未隔离的来源身份/权限/raw/路径技术问题；历史operator phase与actualresponse缺口已显式保留，不能据此作新δ或实验结论。

| 优先级 | 实际判断及证据 | 后续使用需核的内容 |
| --- | --- | --- |
| P1 | phase/axis/count/response矩阵为Codex跨来源综合；SU59-4、FH59-5/8和B15-16支持同observable的合同，不能归为任何一篇原作者完整结论 | 用于论文前逐项回原轴、原countroles和producer；未对齐时有误翻号/混合数据对象风险 |
| P1 | FH59-12只为review转述的同E3不同布居反例；SEH59-10是原作者对替代AD保留双解的直接限制 | 不把两者合成同dataset或据此判当代array calibration；原实验/response/Cov缺口保持 |
| P2 | 末页、索引和preparedprompt更新只纠正导航/priming；未改reviewflags、raw或Bib | 后续formal17仍独立计卡，不能将本runpreview作学分 |


### Hamilton原件追加的null与分类边界

[[hamilton-1948-successive-quanta-polarization]] HAM48-7–12将前述“同一个observable”进一步限定到两个overallrole权重：8个purecase在等权下给null，故unresolvedsignal的P≈0不独立证明源完全不polarized。识别需要gate/能量/效率次序真正分开角色；Q/finiteacceptance仍另校。另有中间J=1的pureQQ rank4被禁止，所以按α4分类也要有可用rank的前提。新项是直接原式复算和明确选律推断，未作实际核赋值、未解决历史mixedδ operatorphase。


### Palit实测案例对联合观测的补强

[[palit-2000-rh99-clover-polarimetry]] P00-4/5提供实际1117keV同正P与不同EM混合候选、再用同跃迁AD排largeδ的作者分析；与SEH59-10替代AD仍两解互为必要限制。联合观测有判别力仍依原reference/phase/response和误差，不能升级成“多测P必唯一”的定理。P00-1/3又明确a与Q分层，其method引用不迁移C/D给Gargactualcalibration。此为Codex跨来源综合，新source/缺口仍unreviewed，未作新的核赋值。


### 实际Rh99摘要的条件可行性

[[rh99-1117-population-feasibility]]把前述companion问题落到P00 actuala2/a4/P：在明确point/freepositivepopulation和逐marginalbox条件下，两种EMfamily均有strictlypositiveq；sourcefullCov/response/布居prior缺失，不能由此作实验概率或parity更改。centralisolatedroots与convex分离证书又限制只靠网格扫描的排除。新认识是“联合观测的判别力必须连同实际联合统计域和布居约束表述”，未裁决原paper/135Pr模式。


P00-15的额外二阶取向条件给可检验companion：同发射态u2符号若独立成立，可改变同一AD/Pbox的EM可识别性；当前未测得，不能写成作者已给或用Gaussianσ替代。数学witness、额外准备条件与实验支持层分别保存。


### 同母态参考的纯度与测量代价

[[nndc-2017-99rh-matched-reference-records]] N099-13把companion从笼统“加reference”收窄为实际Rh99的561.3ΔJ0/820.4ΔJ1选择：前者模型符号对混合较稳但photon强度弱，后者计数多而需更严纯度。N099-1/10同时把2014新采集、2017编译与P00不同响应分开；未得primarybody/AD纯度条件时不宣布分支已经排除。


### 取向输入的物理支持不能省略完整选择

[[unobserved-feeding-alignment-sign]]串联[[diamond-1966-nuclear-alignment-heavy-ion-reactions]] D66-D16-1/2与[[cejnar-1996-spin-deorientation-alpha-2n-gamma]] C96-D16-1–7：入口低m预期、signedtransfer/保号域、source两链近Gaussian与实际reference是不同证据层。高spin低L的全域条件证明不包含任意蒸发或方向门；C96原range/flow文句须带定义域，原Fig7也保留prior下多极小。此为新self-audit，不改旧人审或把Rh99 u2升为已测。


### 实际三线AD中的条件存在与实验排除

[[199tl-three-ad-reference-feasibility]]针对[[diamond-1966-nuclear-alignment-heavy-ion-reactions]] D66-D16-2最初粗网格保存freeq至少8个、额外lowm找到3个源probable序列的witness；后续连续域找到第9个freeq，详下节。前后均不复现原19→5。共同上态rank4负比例使精确中央数不闭合，但误差box仍有解；这把“prior/companion影响选择”的判断落在实际输入上，未新增核赋值。


### 从Stokes输运到实际校准的对象合同

[[garciaraffi-1997-monte-carlo-compton-polarimeters]] GR97-5–14与[[gr97-stokes-response-and-merit]]把线性Stokes的reference/degree、不同threshold和absolute/activeΩ归一分开。正确normalizedP与PSD不独立认证能量权重；Q/M/派生ε也不是三组独立证据。原Eq13的误读已按原图纠正，不虚构sourceerratum；实际modifiedproducer/Σ缺口保持。


### Producer身份与字段的物理作用

[[geant3-vmc-2026-compton-baseline]] G3-1–10补真实codecomponent：三核原样编译/600000事件通过只验证unpolarizedKN、单位/守恒/旋转/cut语义。POLAR字段、同软件名和版本年不是GR97原modifiedproducer或新的独立实验；计算可复现层与核实验response/Cov层继续分开。


D66实际三线案例的连续域续核找到旧粗网格漏解，数值全域覆盖与独立MP80证书详[[199tl-three-ad-reference-feasibility]]。9free/3lowm是声明模型分类而非D66实验结论；偏振固定β投影差异不当完整family分离，近pure强度百分比也不消除相干干涉。


同D66既有候选在完整β域检查后，两个lowm混合族与新free族均可正/负P701；已撤销从固定点差异推全族可分的任何可能暗示。[[199tl-three-ad-reference-feasibility]]保留pureE2解析正界、七个signwitness和MP80复核，未新测偏振或裁决核赋值。


## Day16末段整合：哪些输入真正改变候选

这是本日已读证据的跨来源综合，不是新的实验分析或通用选根规则。

| 已有对象 | 本run可以复用的判断 | 能改变候选排序的下一输入 |
| --- | --- | --- |
| 178W921，两组实际DCO | [[kramer-flecken-1989-use-dco-ratios]] KF89-15/18的gate/observed角色不同；统一target方向时仅第一行倒数。原作者两支与本runpoint模型两根分开，后者P均负 | 同target/gate/角组的校准P幅值和误差、169参考完整phase与真实response/联合Cov；单个P号不足 |
| E2/M1符号 | [[krane-steffen-1970-cd110-mixing-ratios]] KS70-6/13、[[droste-1996-pdco-formalism]] DR96-5区分first-B/last-A及operator/state-order；相邻L的坐标翻号须同步变换核 | 明确每一multipole的辐射振幅定义和同一kernel对照；纯限无干涉，不能单独认证phase |
| Rh99实际AD/P | [[palit-2000-rh99-clover-polarimetry]] P00-4/14/15：free正布居边际box允许两EM族；额外未测lowm条件才排其中一族。P00-16另固定真实反应谱系 | 同发射态、同选择的独立取向约束与reference纯度；更多同dataset处理不增加独立实验 |
| 199Tl实际三线AD | [[diamond-1966-nuclear-alignment-heavy-ion-reactions]] D66-D16-2与条件note保留19→5→3作者判断、9free/3lowm自有数值域。完整β域中三个混合族各有P701正、负解，近99.04%E2也保留干涉 | 实际P幅值/误差、已知EM类型/参考与联合响应；不能从几个存在点或固定β投影宣称全族分离 |
| 未观测feeding | [[cejnar-1996-spin-deorientation-alpha-2n-gamma]] C96-D16-1/2/4/5与D66-D16-3给signedU、完整trace保号域和两链Gaussian边界；不测Rh99实际u2 | 实际入口/蒸发/feeding链及选择。方向门不满足完整trace，不能沿用未观测U |
| Stokes与软件 | [[garciaraffi-1997-monte-carlo-compton-polarimeters]] GR97-7的前因子是(E′/E)²；G3-2/3/5/7验证当前unpolarized组件而非原modified producer | 原polarized producer、geometry/cuts、校准ledger与Σ。POLAR字段、M平方或守恒检查不提供校准符号/真实Q |

边际box只用于条件可行性；没有联合Cov便不给CI。完整物理输入仍缺时，保留多解和readiness，比调σ、Q或参考号去强配预设分支更能检验下一步。强度份额δ²/(1+δ²)、有符号δ和相干项须分列；未观测trace中的强度混合与有方向的AD/P干涉也不能互换。


### 用边缘分布理解未观测与有门

[[droste-1996-pdco-formalism]] DR96-4的两个积分有不同的先后对象。若上游光子已发出，对下游光子的全部方向、偏振及未记录末态求和，完整测量的总概率为1，因此上游边缘分布回到其singles。若先忽略上游光子，子核态却已由发射通道改变；随后看到的下游singles仍携带这个转移后的取向。对角动量张量写出的U就是这种完整未观测通道的作用，见[[krane-steffen-1970-cd110-mixing-ratios]] KS70-6。

一个方向门只选取部分发射结果，条件子态还要除以该门的概率。它保留了不同的权重与可能的coherence，不能直接使用完整方向trace的U，或给daughter重新指定原Gaussian。这也解释[[unobserved-feeding-alignment-sign]]中非负CG概率与有符号U可以共存：概率分布始终非负，rank2基函数本身有正负值；[[cejnar-1996-spin-deorientation-alpha-2n-gamma]] C96-D16-1/2的符号边界属于张量转移，不能解释成负事件数。

这些是已读公式的物理解释。实际gate、feeding与detector response是否满足完整trace或共同密度前提，仍须按实验逐项核验；归一化正确本身不提供未知的联合Cov或唯一δ。

下式采用本任务的通道记法，对已读积分作代数解释。固定一条已经按辐射总概率归一的级联，令第一、第二步的方向/偏振结果分别由 \(K_a,L_b\)表示；末态自旋未记录；求和也包含对连续方向的积分。完整第二步满足

\[
\sum_b L_b^\dagger L_b=\mathbf 1,\qquad
p(a,b)=\operatorname{Tr}(L_bK_a\rho K_a^\dagger L_b^\dagger).
\]

于是循环取迹直接给\(\sum_b p(a,b)=\operatorname{Tr}(K_a\rho K_a^\dagger)\)。忽略第一步得到的中间态却是\(\Phi(\rho)=\sum_a K_a\rho K_a^\dagger\)，其取向一般不同于输入态；旋转协变完整通道的张量作用才对应U。

若下游记录只保留门G及其接受\(0\le\epsilon_b\le1\)，则

\[
E_G=\sum_{b\in G}\epsilon_b L_b^\dagger L_b,\qquad
p(a,G)=\operatorname{Tr}(E_GK_a\rho K_a^\dagger).
\]

\(E_G=c\mathbf1,\ c>0\)是保留上游singles角形状的充分条件；有限角门是否满足它须由真实响应核查。对受限态族，即使偶然给相同角形状，也只证明该族内相合。在\(p(G)>0\)时，条件谱还要除以\(p(G)\)，所以逐门归一后的谱与joint pair counts要分别记录normalizer。门后的分布描述事后选出的子样本。这里对已给定的辐射支归一；若把内部转换等未观测衰变也计入，须使用完整通道及其实际强度权重，见[[martin-1987-ensdf-mixing-ratio-phase-conventions]] MA87-3。这里没有新增真实计数、MC或原producer认证。
