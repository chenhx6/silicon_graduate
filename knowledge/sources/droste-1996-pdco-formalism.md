---
type: source
title: "Droste et al. 1996 - PDCO polarizational-directional correlation formalism"
aliases: [Droste 1996 PDCO]
created: 2026-09-21
updated: 2026-10-26
status: ai-draft
review_status: unreviewed
source_type: theory-method
reading_depth: deep-read
title_original: "PDCO: Polarizational-directional correlation from oriented nuclei"
authors: [Ch. Droste, S. G. Rohoziński, K. Starosta, T. Morek, J. Srebrny, P. Magierski]
journal: "Nuclear Instruments and Methods in Physics Research A"
year: 1996
doi: "10.1016/0168-9002(96)00426-3"
citation_key: droste_1996_PDCO
volume: 378
pages: "518-525"
pii: "0168-9002(96)00426-3"
canonical_source: "Droste et al., NIM A 378, 518-525 (1996)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1996_Droste et al_PDCO Polarizational-directional correlation from oriented nuclei.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1996_Droste et al_PDCO Polarizational-directional correlation from oriented nuclei.pdf"
raw_sha256: "dbfd6796aafc53693b446533c89094a14427e25624321bc16a6edae1b5d84247"
nuclei: [generic]
reactions: [heavy-ion-oriented-nuclei]
experiments: [CLOVER, PDCO, DCO, PPCO]
models: [statistical-tensor, Rose-Brink, oriented-state-correlation]
observables: [PDCO, DCO, polarization, spin-parity, mixing-ratio]
methods: [Compton-polarimetry, angular-correlation, statistical-tensor]
tags: [PDCO, DCO, CLOVER, polarization, angular-correlation]
---

# PDCO polarizational-directional correlation formalism

## Bibliographic Record

- Ch. Droste *et al.*, *NIM A* **378**, 518–525 (1996), PII `0168-9002(96)00426-3`.
- 本session Crossref按exact title/作者/年份匹配DOI `10.1016/0168-9002(96)00426-3`；原件hash匹配，既有citation key不改。
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1996_Droste et al_PDCO Polarizational-directional correlation from oriented nuclei.pdf`。

## Scope and Reading Depth

- PDF pp.518–525 fully read: general two-polarized-γ correlation Eq.1, generalized F coefficients, DCO/PDCO/PPCO cases, emission geometry, deorientation, Gaussian alignment, POL-DIR/DIR-POL modes, symmetries, discussion and conclusion.
- Not covered: source code and later experimental calibrations.
- 当前使用Eq4时先应用[[starosta-1999-pdco-experimental-test]] printed17 footnote1的已发表勘误，见DR96-8；本次已核1999原件，并非仅凭1996印本转录。

## Key Results

- A single statistical-tensor formula covers four cases: DCO (direction–direction), PDCO (polarization–direction in either order) and PPCO (polarization–polarization) for two cascade photons from an oriented state (PDF pp.518–520, Eqs.1–8).
- Polarization angles, emission angles and detector-plane geometry enter through Wigner functions and `cos2φ` terms; sign/multipole effects cannot be separated from orientation and geometry (PDF pp.519–522, Eqs.9–16).
- Integrated PDCO over the second photon's full solid angle reduces to an uncorrelated singles polarization distribution; a measured cascade still requires deorientation coefficients `U_K` for intervening transitions (PDF pp.521–522, Eqs.14–18).
- For heavy-ion reactions, Gaussian substate populations `w(M)∝exp(−M²/2σ²)` are used; the formalism predicts strong dependence on spin sequence, mixing ratios, emission angles and `σ` (PDF pp.522–525, Eq.19 and discussion).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DR96-1 | The generalized PDCO formula unifies DCO, PDCO and PPCO correlations. | formalism-result | direct | PDF pp.518–522, Eqs.1–18 | false |
| DR96-2 | Geometry, orientation and deorientation coefficients are explicit inputs to polarization-direction correlations. | limitation | direct | PDF pp.519–525 | false |
| DR96-3 | Gaussian alignment and detector-angle choices can strongly alter polarization predictions. | transfer-boundary | direct | PDF pp.522–525 | true |
| DR96-4 | 对后续gamma2作完整4π方向积分，gamma1边缘分布回到其singles；反之不观测上游gamma1时，gamma2的发射态取向含U系数。两种积分不应合并为“门条件或feeding总能消失”。 | method-definition-and-boundary | direct | printed520 Eq12；printed521 Eq13–16 | true |
| DR96-5 | Eq5的绝对辐射振幅含i^(L+delta_TM)、能量和初末态约化算符矩阵元，alpha为模方之和；Eq7的广义F还含CG/9j及L−1相位。沿用同一delta符号或pure limits不构成全部相位定义相同的证明。 | convention-and-use-boundary | direct-and-self-audit | printed519 Eq3–6；printed520 Eq7及Bohr–Mottelson说明 | true |
| DR96-6 | Fig7/正文给5→4→2的作者模型例：sigma/I0=.3，DCO取0/90度、PDCO取90/90度phi0；R_DCO约.4时比较pureE1与M1+E2/arctanδ约−70°。其singles、POL-DIR、DIR-POL的P分别约(.34,.27)、(.56,.44)、(.56,.17)。无实测计数或误差，近似R/P不应混成一个精确实验点。 | author-model-calculation | direct | printed523 Sec3例；printed524 Fig7及图注 | true |
| DR96-7 | 作者说FORTRAN代码可向作者取得；本session未得到或运行它，只做独立点响应推导。代码可得的文字声明不等于论文响应已重放。 | reproducibility-boundary | direct-and-self-audit | printed521末段–printed522首段 | true |
| DR96-8 | Eq4 polarization系数的印刷磁项相位错误已由Starosta1999脚注公开更正：应以Tprime而非T判magnetic，即(-1)^(delta_(Tprime,M))。原件Eq4与脚注均核；作者称程序无此误，但本session未取得代码。此勘误不同于本任务delta_probe=−d_source的相对基底映射。 | published-erratum-and-use-boundary | direct-later-source-and-self-audit | printed519 Eq4；Starosta1999 printed17 footnote1 | true |
| DR96-9 | 在本任务新设3→2→0/E2gate及2→1→0/M1gate、固定正布居/real amplitudes/point geometry中，勘误后Eq1/4/7/8与显式photon trace吻合至1.1e−17 sr^-2；原T相位pure项也通过但mixed项偏离。还需显式psi_probe=−psi_Eq1，0/90分析轴不能测试此有向坐标。非作者代码、非实际detector校准，不外推halfspin/L>2/PPCO。 | bounded-formula-implementation-audit | task-calculation | printed519 Eq1–4；printed520 Eq7–8；Starosta1999 printed17 footnote1 | true |

## Summary

Droste *et al.* establish the formal backbone used by later Starosta 1999 PDCO and Droste 1999 PPCO papers. The source makes the observable hierarchy explicit: DCO constrains directional/multipole combinations, polarization supplies electric/magnetic sensitivity, and both share orientation/deorientation inputs.

## Competing Interpretations and Limitations

- PDCO/DCO/PPCO contours inherit alignment, deorientation, cascade order and detector-plane assumptions.
- A formal solution is not a unique multipole assignment when the response or orientation is underconstrained.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| DR96-AR-1 | Tensor chain | Oriented substate tensor → generalized F/R coefficients → DCO/PDCO/PPCO correlation. | PDF Eqs.1–8 | self-checking |
| DR96-AR-2 | Geometry chain | Emission/detector planes and polarization angles → `cos2φ`/Wigner terms → measured asymmetry. | PDF Eqs.9–16 | self-checking |
| DR96-AR-3 | Transfer condition | Re-establish `σ`, deorientation, cascade order and detector geometry before using a PDCO contour. | PDF pp.521–525 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[starosta-1999-pdco-experimental-test]], [[droste-1999-ppco-polarization]], [[compton-polarimetry]], [[angular-correlation]].
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `DR96-P0-1`: Preserve orientation/deorientation and detector geometry when applying PDCO/DCO/PPCO formulas.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[angular-correlation]], [[starosta-1999-pdco-experimental-test]]。

## 2026-10-17原件复核：完整主线、模式与相位坐标

本次在来源前冻结已暴露旧Wiki/Day15知识的primed回忆后，重核raw SHA-256 `dbfd6796aafc53693b446533c89094a14427e25624321bc16a6edae1b5d84247`，完整读8页（printed518–525）；视觉重点覆盖printed519–524的Eq1–21、geometry、U传播、Gaussian及Fig4–7。mainline是统一DCO/PDCO/PPCO→完整4π边缘与未观测级联U→两种PDCO模式/geometry/sigma依赖→模型双候选与改变测量模式；没有取得作者FORTRAN或实际array response/计数/完整Cov。DR96-1–3的既有flags和page review保持，新claims true，不扩张为人审。

Eq2的B张量、Eq3/4辐射系数与Eq5的a(TL)是本地符号；B不是B(E2)，P不是Compton计数asymmetry。Eq19的sigma是磁子态M分布宽度，sigma/I0是另一个量。用singles或4π积分数据校准sigma，不代表任意finite gate的条件态已经校准。

DR96-4特别区分先后顺序：积分下游gamma2不会改变已发射gamma1的边缘；积分上游gamma1则给带U去取向的daughter分布。source Eq17/18的stretched-cascade门不变性依赖明确的级联/sidefeeding/外场条件，不能扩写成所有换门都无影响。printed523还指出无alignment时PDCO仍可非零，且单γ最佳的90°位置并非所有条件PDCO的普适最优。

DR96-6是**作者计算**。Fig7图注的state parities unchanged对应M1/E2曲线，正文另用pureE1的电磁性质比较；其相位/分子分母依赖与sourceRef1应逐项保存。正文的.34/.27等值不完全相同，又未给实测sigma，不能将“难区分”的叙述改写为对全部联合observable严格不可识别。

[[dco-pdco-ambiguity-worksheet]]给本任务独立模型复算，保留原冻结probe与首轮mixed-sign不一致。使用Eq3/7的F矩阵（9j用六CG重耦合求得）独立校验后，推得该probe基底与source振幅坐标的相对变换；pure校验看不出这个相位差。它**没有**据此声称KS70/Rose–Brink/D96的全局delta定义已互换。source的−70°例与本任务精确同R根分开列，模型不是新增实测RDCO或作者FORTRAN重放。

### Eq4已发表勘误与实现基底分开

[[starosta-1999-pdco-experimental-test]] ST99-8（printed17 footnote1）将本篇Eq4的`(-1)^(delta_(T,M))`改成`(-1)^(delta_(Tprime,M))`。这改变复共轭振幅一侧的magnetic判别，不能在逐字实现原式时漏掉。作者表示其computer code没有该错误；这仍只是作者声明，本任务没有验证其producer代码。

本run早前的phase worksheet用Eq3/7的directional F和独立RB/Jones photon amplitudes核对，未将原印Eq4逐字作为PDCO kernel，因此不能把该勘误事后当作早前内部坐标换号的原因，也不据此宣称重放了作者PDCO程序。当前使用者须同时保存正确公式和自己的operator/basis定义。

随后按新冻结输入执行DR96-9的有界literal-formula核验，结果与失败路径保存在[[dco-pdco-ambiguity-worksheet]]的“勘误公式与有向分析轴的独立核验”。共享CG/Wigner基础函数，但tensor contraction与photon trace是不同代数路径，不是独立实验/独立原作者实现。总归一、互补分析轴之和、反射对称与两种积分阶数通过；早期斜向psi不一致被定位为固定Jones probe的有向坐标映射，未调物理角度、布居或delta。

## Day23：Gaussian宽度与有限门single-photon边界

本次定向读printed522–523 Eq19–21及singles/finite PDCO区别，fresh视觉522；原SHA相符。未新称重读整篇或运行原FORTRAN，旧flags及1999 Eq4勘误保留。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DR96-D23-001 | Eq19明确w(M)∝exp[−M²/(2σ²)]并在合法离散M上归一，σ是该Gaussian输入宽度；有限spin截断后的实际sqrt〈M²〉不必等于σ。按这个明确条件，本任务I17/2在输入σ/I=.8时离散rms/I=.542317，而.2时约.1999998；这些是分布数学量，不认证Lv2022使用variance一词时的原实现。 | source-width-and-discrete-population-boundary | direct-original-plus-declared-arithmetic | printed522 Eq.19; task halfspin-singles-response-013 | true |
| DR96-D23-002 | printed523说明singles/完整4π积分PDCO与有限条件PDCO不同：后者即使σ→∞也可非零polarization，最佳polarimeter角不普遍固定90°。本任务halfspin kernel只构singles，名义154/90的point比及local90 Stokes不能直接当实际Pr/Au Rac/P；全角gate字面不等于完整4π或无feeding/效率条件。 | response-transfer-and-conditional-gate-boundary | direct-original-and-task-scope | printed522 detector-integrated discussion; printed523 points5/6 and singles/4π-integrated paragraph | true |

halfspin振幅源与本任务控制见[[rose-brink-1967-phase-defined-angular-distributions]] RB67-D23-001/002，实验a/Q与散射计数仍须另接实际响应。共同取向参数和校准不能因同名sigma或同一formalism而在两个实验间自动共享。

## Day23：上游4π与下游迹的有界halfspin核验

本次回读并fresh视觉printed521 Eq13–15/U及上下游区别，原hash相符；旧勘误与flags保持。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DR96-D23-003 | Eq13–15明确：不观测上游γ1时，γ2母态已有U描述的取向变化；完整4π积分下游γ2才回到先发γ1的singles。任务halfspin两级联通过19项trace-preserving/CGchannel-vs-Wigner积分/正定/直接joint-vs-sequential/futuretrace及1/2→3/2→1/2 M1解析控制，最大两路差≤7.8e−16。以源自Lv的spin/gate身份构造，但布居与d_RB均design，非原数据/原producer认证。 | original-cascade-order-and-declared-component | direct-original-plus-task-check | printed521 Eqs.13–15 and preceding two paragraphs; task model-contract-014 | true |

具体门身份见[[lv-2022-evidence-against-wobbling-135pr]] L22-D23-004；矩阵元source结构另见[[rose-brink-1967-phase-defined-angular-distributions]] RB67-D23-003。本练习只说明所需响应层次；实际array有方位角/效率合并，不能把一个coplanar pointgate的相干效应直接叫实测偏差。

## Day23：有限门合并的有效pair权重

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DR96-D23-004 | 从本篇finite detector/gate积分前提出发，本任务将M1/E2上游gate的axisymmetric设计压成固定θ的ηq(q0…4)。uniform方位角可去offdiagonal，但实际effective gate权重须针对target-detector/gate pair、效率/live time/selection；名义array方位对称不保证选定Compton/符合条件仍同权。跨θ应先合未归一density/yield，再求P，不能平均P；没有actualpair response时不将pointgate的coherence差写成实验偏差。 | declared-response-averaging-contract | source-geometry-premise-and-task-inference | printed522 detector-integrated paragraph; printed523 finite PDCO discussion; RB67-D23-004 | true |

[[rose-brink-1967-phase-defined-angular-distributions]] RB67-D23-004给数学moment恒等式；source实际796/450身份仍见[[lv-2022-evidence-against-wobbling-135pr]] L22-D23-004。本任务未恢复actualpair权重或原P/Rac likelihood。

## Day23：镜角关系需保留门条件

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DR96-D23-005 | printed522–523说明finitePDCO off90°的反射关系需连同directional-detector角/φ处理，不普遍等于singles的单角反射。任务取pureE2上游pointgate45°/φ0、对角Gaussian初态，再发mixed目标，75.5与104.5的photonρ差约8.65e−5；同时把gate45→135、target镜角交换则P残差6.4e−16。只是声明point-design的旋转/条件性控制，不是实际Pr的门偏差；实际array方位合并可改变它。 | original-conditional-symmetry-and-task-control | source-geometry-premise-plus-task-numerics | printed522 symmetry points2–3; printed523 singles/finite-PDCO discussion; task pr-angle-group-response-026 | true |

实际角组源见[[lv-2022-evidence-against-wobbling-135pr]] L22-D23-005。组响应应先合未归一photon density再求P；任务所选例中naive均值与正确P仅差约1.9e−9，非实测效应/精度。首次检查用了未有依据的最小effect阈值，后改为相对数值噪声的非零检查并完整保留值，没有调整科学输入或声称大的实验影响。
